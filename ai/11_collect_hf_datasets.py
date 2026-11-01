"""Stage D1: collect Hugging Face dataset cards for the dataset wiki.

Two seeds, merged by dataset id:
  1. every language:ko dataset (--min-downloads 0). Popularity is not quality: poorly documented
     cards stay in and are penalized by README status downstream instead.
  2. datasets our Korean models cite in cardData.datasets, kept regardless of downloads
     because they are the trained_with links between models and datasets.

Only metadata and README.md are stored; dataset files are never downloaded. Taxonomy
mapping and NER run as a later stage on these rows.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from huggingface_hub import HfApi, get_session, hf_hub_url
from huggingface_hub.utils import build_hf_headers, hf_raise_for_status

from retrieval_metadata import normalize_language_code

# =========================================================
# CONFIG
# =========================================================

STAGE_VERSION = 1
MIN_DOWNLOADS = 0
API_MAX_RETRIES = 5
API_RETRY_BASE_SECONDS = 2

BACKEND_DIR = Path(__file__).resolve().parents[1] / "backend"
DATA_DIR = BACKEND_DIR / "data"
OUTPUT = DATA_DIR / "hf_datasets_stage1.jsonl"
STATE_OUTPUT = DATA_DIR / "hf_datasets_stage1_state.json"
README_DIR = DATA_DIR / "readmes" / "datasets"
MODEL_SOURCES = (
    DATA_DIR / "hf_models_stage2_core.jsonl",
    DATA_DIR / "hf_models_stage2_low_popularity.jsonl",
)

_HANGUL_RE = re.compile(r"[가-힣]")
_LATIN_RE = re.compile(r"[A-Za-z]")


# =========================================================
# HELPERS
# =========================================================


def with_retry(fn, label):
    for attempt in range(API_MAX_RETRIES + 1):
        try:
            return fn()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            response = getattr(exc, "response", None)
            status = getattr(response, "status_code", None)
            if attempt >= API_MAX_RETRIES or status in (401, 403, 404):
                raise
            delay = API_RETRY_BASE_SECONDS * (2**attempt)
            if status == 429:
                # Hub rate limits use a 5-minute window; short backoff just burns the remaining retries.
                headers = getattr(response, "headers", None) or {}
                delay = max(delay, int(headers.get("Retry-After") or 30))
            print(
                f"[API RETRY] {label} attempt={attempt + 1}/{API_MAX_RETRIES} "
                f"after {type(exc).__name__}: sleeping {delay}s",
                flush=True,
            )
            time.sleep(delay)


def tag_values(tags, prefix):
    return sorted({tag.split(":", 1)[1] for tag in tags or [] if tag.startswith(prefix + ":")})


def readme_language(text):
    """Dominant script of a README: 'ko', 'en', 'mixed', or None when empty."""
    hangul, latin = len(_HANGUL_RE.findall(text)), len(_LATIN_RE.findall(text))
    if hangul + latin == 0:
        return None
    # Hangul syllables carry ~2-3x the information of a Latin letter, so 0.2 already means real Korean prose.
    ratio = hangul / (hangul + latin)
    return "ko" if ratio >= 0.5 else "mixed" if ratio >= 0.2 else "en"


def readme_path_for(dataset_id):
    return README_DIR / (dataset_id.replace("/", "__") + ".md")


def load_model_references():
    refs: dict[str, list[str]] = {}
    for path in MODEL_SOURCES:
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            for line in f:
                row = json.loads(line)
                for ref in row.get("datasets") or []:
                    if isinstance(ref, str) and ref.strip():
                        refs.setdefault(ref.strip(), []).append(row["model_id"])
    return {ref: sorted(set(models)) for ref, models in refs.items()}


def load_previous():
    if not OUTPUT.exists():
        return {}
    with open(OUTPUT, encoding="utf-8") as f:
        return {row["dataset_id"]: row for row in map(json.loads, f)}


def save_atomic(path, write):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with open(temp, "w", encoding="utf-8") as f:
        write(f)
    os.replace(temp, path)


# =========================================================
# COLLECTION
# =========================================================


def build_row(info, seed_reasons, referenced_by):
    tags = list(info.tags or [])
    card = info.card_data.to_dict() if info.card_data else {}
    return {
        "dataset_id": info.id,
        "source": "huggingface",
        "url": f"https://huggingface.co/datasets/{info.id}",
        "stage_version": STAGE_VERSION,
        "seed_reasons": sorted(seed_reasons),
        "referenced_by_models": referenced_by,
        "author": info.author,
        "sha": info.sha,
        "downloads": info.downloads or 0,
        "likes": info.likes or 0,
        "gated": info.gated,
        "created_at": info.created_at.isoformat() if info.created_at else None,
        "last_modified": info.last_modified.isoformat() if info.last_modified else None,
        "languages": sorted(
            {code for value in tag_values(tags, "language") if (code := normalize_language_code(value))}
        ),
        "licenses": tag_values(tags, "license"),
        "task_categories": tag_values(tags, "task_categories"),
        "task_ids": tag_values(tags, "task_ids"),
        "size_categories": tag_values(tags, "size_categories"),
        "modalities": tag_values(tags, "modality"),
        "formats": tag_values(tags, "format"),
        "tags": tags,
        # list_datasets fills description; dataset_info (model references) does not.
        "description": getattr(info, "description", None),
        "card_data": card,
    }


def fetch_readme(row, previous, token):
    """Attach README fields, reusing the stored file when the repo sha is unchanged."""
    path = readme_path_for(row["dataset_id"])
    old = previous.get(row["dataset_id"])
    if old and old.get("sha") == row["sha"] and old.get("readme_path") and path.exists():
        row.update({k: old[k] for k in ("readme_path", "readme_language", "readme_chars")})
        return row
    url = hf_hub_url(row["dataset_id"], "README.md", repo_type="dataset", revision=row["sha"])

    def get():
        response = get_session().get(url, headers=build_hf_headers(token=token), timeout=30)
        if response.status_code == 404:
            return None
        hf_raise_for_status(response)
        return response.text

    text = with_retry(get, f"readme {row['dataset_id']}")
    if text is None:
        row.update(readme_path=None, readme_language=None, readme_chars=0)
        return row
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    row.update(readme_path=path.relative_to(BACKEND_DIR).as_posix(), readme_language=readme_language(text), readme_chars=len(text))
    return row


def collect(api, min_downloads, limit, workers, token):
    rows: dict[str, dict] = {}
    reasons: dict[str, set] = {}

    # Seed 1: Korean datasets, sorted by downloads so the floor ends the scan.
    def list_korean():
        found: list[Any] = []
        for info in api.list_datasets(language="ko", sort="downloads", direction=-1, full=True):
            if (info.downloads or 0) < min_downloads or (limit and len(found) >= limit):
                break
            found.append(info)
        return found

    for info in with_retry(list_korean, "list_datasets language=ko"):
        if info.disabled or info.private:
            continue
        rows[info.id] = info
        reasons.setdefault(info.id, set()).add("language:ko")
    print(f"[SEED] language:ko downloads>={min_downloads}: {len(rows)}", flush=True)

    # Seed 2: datasets cited by our models. Ids are free text in model cards, so unresolved ones are reported.
    refs = load_model_references()
    if limit:
        refs = dict(list(refs.items())[:limit])
    missing = [ref for ref in refs if ref not in rows]

    def resolve(ref):
        try:
            return ref, with_retry(lambda: api.dataset_info(ref), f"dataset_info {ref}")
        except Exception as exc:
            return ref, exc

    unresolved = {}
    resolved_ids = {ref: ref for ref in refs if ref in rows}
    with ThreadPoolExecutor(workers) as pool:
        for ref, result in pool.map(resolve, missing):
            if isinstance(result, Exception):
                unresolved[ref] = type(result).__name__
            elif not (result.disabled or result.private):
                # Hub redirects renamed repos, so the canonical id can differ from the cited one.
                rows.setdefault(result.id, result)
                resolved_ids[ref] = result.id
    ref_by_id: dict[str, list[str]] = {}
    for ref, models in refs.items():
        if target := resolved_ids.get(ref):
            reasons.setdefault(target, set()).add("model_reference")
            ref_by_id[target] = sorted(set(ref_by_id.get(target, [])) | set(models))
    print(
        f"[SEED] model references: {len(refs)} cited, {len(refs) - len(unresolved)} resolved, "
        f"{len(unresolved)} unresolved",
        flush=True,
    )

    built = [build_row(info, reasons[dataset_id], ref_by_id.get(dataset_id, [])) for dataset_id, info in rows.items()]
    return built, refs, unresolved


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--min-downloads", type=int, default=MIN_DOWNLOADS)
    parser.add_argument("--limit", type=int, default=None, help="cap each seed for a quick trial run")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--skip-readmes", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()

    load_dotenv(".env")
    token = os.getenv("HF_TOKEN")
    api = HfApi(token=token)
    started = time.time()
    previous = load_previous()
    rows, refs, unresolved = collect(api, args.min_downloads, args.limit, args.workers, token)

    if not args.skip_readmes:
        with ThreadPoolExecutor(args.workers) as pool:
            rows = list(pool.map(lambda row: fetch_readme(row, previous, token), rows))
    rows.sort(key=lambda row: (-row["downloads"], row["dataset_id"]))

    # Rows and state are written only after every API call succeeded, so a failed run keeps the last snapshot.
    save_atomic(OUTPUT, lambda f: f.writelines(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    readme_langs: dict[str, int] = {}
    for row in rows:
        key = str(row.get("readme_language"))
        readme_langs[key] = readme_langs.get(key, 0) + 1
    state = {
        "stage_version": STAGE_VERSION,
        "completed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "elapsed_seconds": round(time.time() - started, 1),
        "min_downloads": args.min_downloads,
        "limit": args.limit,
        "rows": len(rows),
        "seed_counts": {
            "language:ko": sum("language:ko" in row["seed_reasons"] for row in rows),
            "model_reference": sum("model_reference" in row["seed_reasons"] for row in rows),
            "both": sum(len(row["seed_reasons"]) == 2 for row in rows),
        },
        "model_references_cited": len(refs),
        "unresolved_model_references": unresolved,
        "readme_languages": readme_langs,
    }
    save_atomic(STATE_OUTPUT, lambda f: json.dump(state, f, ensure_ascii=False, indent=2))
    print(
        json.dumps({k: v for k, v in state.items() if k != "unresolved_model_references"}, ensure_ascii=False, indent=2)
    )
    print(f"Output -> {OUTPUT}\nState  -> {STATE_OUTPUT}\nREADME -> {README_DIR}")


def self_check():
    assert readme_language("") is None
    assert readme_language("This dataset contains Korean news articles.") == "en"
    assert readme_language("한국어 뉴스 기사 요약 데이터셋입니다. 문서와 요약문으로 구성됩니다.") == "ko"
    assert readme_language("Korean summarization dataset. 한국어 뉴스 기사와 요약문.") == "mixed"
    assert tag_values(["language:ko", "language:en", "license:mit", "x"], "language") == ["en", "ko"]
    assert readme_path_for("klue/klue").name == "klue__klue.md"
    print("11_collect_hf_datasets ok")


if __name__ == "__main__":
    main()
