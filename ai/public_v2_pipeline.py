"""Run every public-data step for corpus v2 in order, then check the result.

    collect (18, optional) -> enrich (18_enrich) -> refine (13 --corpus v2) -> documents (14 --corpus v2)
    -> quality check

New or changed rows cannot skip a step: 13 v2 refuses a stale enrichment and 14 v2 a stale graph,
and the quality check below fails the run. Nothing here embeds, writes Supabase or touches v1.

    python public_v2_pipeline.py                # enrich (network) + refine + documents + check
    python public_v2_pipeline.py --collect      # also re-collect the catalogs first (API keys)
    python public_v2_pipeline.py --offline      # enrichment from cache only
    python public_v2_pipeline.py --check-only
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from corpus_manifest import check_corpus, check_manifest, load_manifest

AI_DIR = Path(__file__).resolve().parent
DATA_DIR = AI_DIR / "data"
COLLECTED = DATA_DIR / "public_datasets_stage1.jsonl"
ENRICH_DIR = DATA_DIR / "public_enriched"
GRAPH_DIR = DATA_DIR / "hypergraph_v2"
DOCS_DIR = DATA_DIR / "dataset_index_v2"
REPORT = ENRICH_DIR / "quality_report.json"
# ponytail: one ceiling for unread official pages; a run above it is retried, not shipped.
MAX_UNREAD_RATE = 0.02
MAX_DELETED_RATE = 0.05
CONFIRMED = ("ok", "deleted")
FORMATS = {"api", "csv", "xlsx", "xls", "json", "xml", "txt", "shp", "geojson"}


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def quality(collected, enriched, entities, duplicates, chunks):
    """(problems, report) for the public rows of one v2 build; problems stop the run."""
    problems = []
    ids = [r["dataset_id"] for r in collected]
    if [r["dataset_id"] for r in enriched] != ids:
        problems.append("보완 결과의 데이터 목록이 수집 결과와 다름")
    if not enriched:
        problems.append("보완 결과가 비어 있음")
    status = Counter(r["official"]["status"] for r in enriched)
    recheck = Counter(r["official"]["recheck"] for r in enriched if r["official"]["recheck"])
    # A deletion is the portal's own notice; many at once means a broken look-up, not real deletions.
    if status["deleted"] > MAX_DELETED_RATE * len(enriched):
        problems.append(f"공식 페이지에서 삭제됐다는 행 {status['deleted']}개 (허용 {MAX_DELETED_RATE:.0%})")
    # Look-up problems: never confirmed, or an older confirmation is in use because the re-check failed.
    issues = {s: n for s, n in status.items() if s not in CONFIRMED}  # failed, parse_error, no_page, unchecked, ...
    issues.update({f"재확인 {s}": n for s, n in recheck.items()})
    if sum(issues.values()) > MAX_UNREAD_RATE * len(enriched):
        problems.append(f"공식 페이지 조회·해석 문제 {sum(issues.values())}개 {issues} (허용 {MAX_UNREAD_RATE:.0%})")
    review = [r["dataset_id"] for r in enriched if r["official"]["needs_review"]]
    unmapped = Counter(r["official"]["license_text"] for r in enriched if r["official"]["license_text"] and not r["licenses"])
    if unmapped:
        problems.append(f"분류하지 못한 이용허락 문구 {sum(unmapped.values())}개: {unmapped.most_common(5)}")
    odd = Counter(f for r in enriched for f in r.get("formats") or [] if f not in FORMATS)
    if odd:
        problems.append(f"알 수 없는 제공 방식 {dict(odd)}")
    no_format = [r["dataset_id"] for r in enriched if r["official"]["status"] == "ok" and not r.get("formats")]
    cards = {c["dataset_id"] for c in chunks if c["kind"] == "card"}
    lost = [i for i in ids if f"dataset:{i}" not in entities and i not in duplicates]
    if lost:
        problems.append(f"그래프에 없는 공공데이터 {len(lost)}개: {lost[:5]}")
    no_card = [i for i in ids if f"dataset:{i}" in entities and i not in cards]
    if no_card:
        problems.append(f"검색 문서가 없는 공공데이터 {len(no_card)}개: {no_card[:5]}")
    portal = [e for e in entities.values() if e.get("source") in ("seoul_open_data", "data_go_kr")]
    if any("coverage_status" not in e for e in portal):
        problems.append("지역 범위 판단이 없는 공공데이터 엔티티가 있음")
    report = {
        "rows": len(enriched),
        "official_status": dict(status),
        "deleted_on_portal": [r["dataset_id"] for r in enriched if r["official"]["status"] == "deleted"],
        "lookup_problems": issues,
        # fetched / reparsed by the current parser, or compat: an older answer accepted by a migration
        "verification": dict(Counter(r["official"].get("verification") for r in enriched if r["official"].get("verification"))),
        "needs_review": {"count": len(review), "dataset_ids": review[:50]},
        "licensed": {"collected": sum(bool(r["licenses"]) for r in collected), "enriched": sum(bool(r["licenses"]) for r in enriched)},
        "license_needs_check": sum(not r["licenses"] for r in enriched),
        "formats": dict(Counter(",".join(r.get("formats") or ["(미확인)"]) for r in enriched).most_common(12)),
        "formats_unknown": len(no_format),
        "formats_changed": sum(a.get("formats") != b.get("formats") for a, b in zip(collected, enriched, strict=False)),
        "update_cycle": dict(Counter(r.get("update_cycle") or "(없음)" for r in enriched).most_common(10)),
        "public_entities": len(portal),
        "public_cards": sum(f"dataset:{i}" in entities and i in cards for i in ids),
    }
    return problems, report


def check():
    problems = check_manifest(ENRICH_DIR) + check_corpus(GRAPH_DIR, DOCS_DIR)
    graph = load_manifest(GRAPH_DIR) or {}
    if (graph.get("upstream") or {}).get("enrich_id") != (load_manifest(ENRICH_DIR) or {}).get("stage_id"):
        problems.append("그래프가 지금의 보완 결과로 만들어지지 않음")
    if problems:
        return problems, None
    found, report = quality(
        read_jsonl(COLLECTED),
        read_jsonl(ENRICH_DIR / "public_datasets.jsonl"),
        {e["entity_id"]: e for e in read_jsonl(GRAPH_DIR / "entities.jsonl") if e["kind"] == "dataset"},
        json.loads((GRAPH_DIR / "duplicates.json").read_text(encoding="utf-8")),
        read_jsonl(DOCS_DIR / "chunks.jsonl"),
    )
    report.update(enrich_id=load_manifest(ENRICH_DIR)["stage_id"], corpus_id=graph["stage_id"],
                  documents_id=load_manifest(DOCS_DIR)["stage_id"], problems=found)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return found, report


STAGES = (("enrich", ENRICH_DIR), ("hypergraph", GRAPH_DIR), ("documents", DOCS_DIR))
PIN = AI_DIR / "test" / "public_data" / "corpus_v2" / "data_version.json"


def write_pin(report):
    """Freeze this build: embedding and evaluation must name exactly these stage ids."""
    manifests = {name: load_manifest(directory) for name, directory in STAGES}
    pin = {
        "data_version": manifests["documents"]["stage_id"][:16],
        "pinned_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "git": manifests["documents"]["git"],
        "stages": {
            name: {"stage_id": m["stage_id"], "created_at": m["created_at"], "inputs": m["inputs"], "outputs": m["outputs"]}
            for name, m in manifests.items()
        },
        "quality": {k: report[k] for k in ("rows", "official_status", "verification", "lookup_problems", "licensed",
                                           "license_needs_check", "public_entities", "public_cards")},
        "chunks": manifests["documents"]["counts"],
    }
    PIN.write_text(json.dumps(pin, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return pin


def verify_pin():
    """Problems when the local build is not the pinned one."""
    if not PIN.exists():
        return [f"{PIN.name} 없음"]
    pin = json.loads(PIN.read_text(encoding="utf-8"))
    problems = []
    for name, directory in STAGES:
        manifest = load_manifest(directory) or {}
        if manifest.get("stage_id") != pin["stages"][name]["stage_id"]:
            problems.append(f"{name}: 고정된 버전과 다름 ({(manifest.get('stage_id') or '없음')[:16]} != {pin['stages'][name]['stage_id'][:16]})")
    return problems


def run(*args):
    print(f"\n$ python {' '.join(args)}", flush=True)
    subprocess.run([sys.executable, *args], cwd=AI_DIR, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--collect", action="store_true", help="run 18_collect_public_datasets.py first")
    parser.add_argument("--offline", action="store_true", help="enrich from cached official pages only")
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--pin", action="store_true", help=f"after a passing check, freeze the build in {PIN.name}")
    parser.add_argument("--verify-pin", action="store_true", help="fail unless the local build is the pinned one")
    args = parser.parse_args()
    if args.verify_pin:
        problems = check()[0] + verify_pin()
        for problem in problems:
            print(f"[고정 버전 문제] {problem}")
        if problems:
            sys.exit(1)
        print(f"public v2 matches the pinned data_version {json.loads(PIN.read_text(encoding='utf-8'))['data_version']}")
        return
    if not args.check_only:
        if args.collect:
            # New catalog lists every time; per-item caches fetch what the lists newly name, and Seoul
            # field lists whose catalog row changed or aged out (bounded per run).
            run("18_collect_public_datasets.py", "--source", "all", "--refresh-lists", "--renew-fields")
        run("18_enrich_public_datasets.py", *(["--offline"] if args.offline else []))
        run("13_build_hypergraph.py", "--corpus", "v2")
        run("14_build_dataset_chunks.py", "--corpus", "v2")
    problems, report = check()
    if report:
        print(json.dumps({k: v for k, v in report.items() if k != "problems"}, ensure_ascii=False, indent=1))
    for problem in problems:
        print(f"[품질 문제] {problem}")
    if problems:
        sys.exit(1)
    print(f"public v2 quality ok -> {REPORT}")
    if args.pin:
        print(f"pinned data_version {write_pin(report)['data_version']} -> {PIN}")


if __name__ == "__main__":
    main()
