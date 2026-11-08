"""Priority review batch for the public golden set: build it, check judgments, turn them into labels.

    python test/public_data/corpus_v2/review_batch.py build                 # batch1 + pilot sample
    python test/public_data/corpus_v2/review_batch.py validate <judgments>  # criteria violations
    python test/public_data/corpus_v2/review_batch.py labels <judgments> --out <file>

Batch 1 = every existing hold and high-review row (54) + new unjudged candidates the preliminary
search ranked in the top 5 of either mode. Reviewer files carry no rank, mode or proposal.

Judgments are jsonl rows {review_id, score: "2"|"1"|"0"|"?", reason, note, judge}. Criteria
(test/public_data/README.md, "2차 판정 기준"):
  - a region the question does not name is judged by the question's purpose, not as "nationwide
    required"; local data is not 1 by default
  - an explicit API or file requirement is hard: the other kind is 0 wrong_delivery; unknown is ?
  - missing information is ?, never 1; 1 is a partial fit with the part named in the note
  - p026 accepts 공공누리 제1유형 only
Labels are written to a separate file; labels/public_data_golden.jsonl is never changed.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREP = HERE / "golden_prep"
BATCH = PREP / "batch1"
GOLDEN = HERE.parent / "labels" / "public_data_golden.jsonl"
TOP_RANK = 5
PILOT_SIZE = 24
SEED = 20261109
SCORES = {"2", "1", "0", "?"}
REASONS = {"off_topic", "wrong_region", "wrong_delivery", "license", "stale",
           "wrong_language", "wrong_period", "wrong_spatial_unit"}
HARD_REASONS = {"wrong_region", "wrong_delivery", "license"}
# A note that only says the card lacks information is a hold, not a partial fit.
LACK_ONLY_RE = re.compile(r"^(?:[^.]*?)(정보\s*(?:가\s*)?부족|확인\s*(?:불가|안\s*됨|할\s*수\s*없)|알\s*수\s*없|판단\s*불가)[^.]*$")


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path, rows):
    Path(path).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def select(context):
    """review_ids of batch 1, with why each is in it."""
    chosen = {}
    for c in context:
        sources = set(c["review_sources"])
        if sources & {"existing_hold", "high_review"}:
            chosen[c["review_id"]] = sorted(sources & {"existing_hold", "high_review"})
        elif "new_unjudged" in sources and min((c["discovery"] or {"x": 99}).values()) <= TOP_RANK:
            chosen[c["review_id"]] = [f"new_top{TOP_RANK}"]
    return chosen


def pilot(chosen, suggestions, size=PILOT_SIZE, seed=SEED):
    """A small sample spread over sources and over the condition kinds the criteria are about."""
    rng = random.Random(seed)

    def stratum(rid):
        checks = suggestions[rid]["checks"]
        kind = next((k for k in ("kogl_type1_only", "delivery", "realtime", "commercial", "region", "region_scope")
                     if k in checks), "none")
        return (chosen[rid][0], kind)

    groups = defaultdict(list)
    for rid in sorted(chosen):
        groups[stratum(rid)].append(rid)
    for members in groups.values():
        rng.shuffle(members)
    picked = []
    while len(picked) < size and any(groups.values()):
        for key in sorted(groups):
            if groups[key] and len(picked) < size:
                picked.append(groups[key].pop())
    return sorted(picked)


WORKSHEET_FIELDS = ["review_id", "query_id", "query", "conditions", "aspects", "dataset_id", "title", "publisher",
                    "coverage", "formats", "license_text", "update_cycle_portal", "fields", "description",
                    "url", "score", "reason", "note"]


def worksheet_row(item):
    f = item["facts"]
    return {
        "review_id": item["review_id"], "query_id": item["query_id"], "query": item["query"],
        "conditions": json.dumps(item["conditions"], ensure_ascii=False),
        "aspects": " / ".join(item["aspects"] or []), "dataset_id": item["dataset_id"], "title": f["title"],
        "publisher": f["publisher"], "coverage": f"{f['coverage_regions']} {f['coverage_status']} {f['coverage_district'] or ''}".strip(),
        "formats": ",".join(f["formats"]), "license_text": f["license_text"], "update_cycle_portal": f["update_cycle_portal"],
        "fields": " | ".join(f["fields"]), "description": f["description"], "url": f["url"],
        "score": "", "reason": "", "note": "",
    }


def build():
    items = {i["review_id"]: i for i in read_jsonl(PREP / "review_items.jsonl")}
    context = read_jsonl(PREP / "review_context.jsonl")
    suggestions = {s["review_id"]: s for s in read_jsonl(PREP / "review_suggestions.jsonl")}
    chosen = select(context)
    BATCH.mkdir(exist_ok=True)
    batch = [items[rid] for rid in sorted(chosen)]
    write_jsonl(BATCH / "items.jsonl", batch)
    with open(BATCH / "worksheet.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=WORKSHEET_FIELDS)
        writer.writeheader()
        writer.writerows(worksheet_row(i) for i in batch)
    sample = pilot(chosen, suggestions)
    (BATCH / "manifest.json").write_text(json.dumps({
        "items": len(batch),
        "by_source": dict(Counter(s for v in chosen.values() for s in v)),
        "selection": f"existing_hold + high_review 전체, new_unjudged는 어느 방식이든 상위 {TOP_RANK}위 안",
        "pilot": {"seed": SEED, "size": len(sample), "review_ids": sample},
        "sources": {rid: chosen[rid] for rid in sorted(chosen)},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch1 {len(batch)} items {dict(Counter(s for v in chosen.values() for s in v))}, pilot {len(sample)}")


def validate(judgments, suggestions):
    """(violations, warnings). Violations break a criterion; warnings need a second look."""
    violations, warnings = [], []
    by_query = defaultdict(list)
    for j in judgments:
        rid, score, reason, note = j["review_id"], str(j.get("score") or ""), j.get("reason") or "", (j.get("note") or "").strip()
        checks = suggestions[rid]["checks"]
        status = {k: c["status"] for k, c in checks.items()}
        if score not in SCORES:
            violations.append((rid, f"점수 '{score}'는 2/1/0/? 가 아님"))
            continue
        if score == "0" and reason not in REASONS:
            violations.append((rid, f"0점 사유 '{reason}' 없음 또는 알 수 없음"))
        for key in ("delivery", "kogl_type1_only"):
            if status.get(key) == "불충족" and score in {"1", "2"}:
                violations.append((rid, f"{key} 필수 조건 불충족인데 {score}점"))
        if status.get("region") == "불충족" and score in {"1", "2"}:
            violations.append((rid, f"제목상 다른 지역인데 {score}점"))
        if score == "1" and not note:
            violations.append((rid, "1점인데 부분 적합 내용이 note에 없음"))
        if score == "1" and note and LACK_ONLY_RE.search(note) and not re.search(r"부분|일부|만 제공|만 있|없지만", note):
            violations.append((rid, f"정보 부족을 1점으로 처리: '{note}'"))
        if score == "2" and any(s == "미확인" for s in status.values()) and "확인" not in note:
            warnings.append((rid, "미확인 조건이 있는데 2점: note에 원문 확인 근거 필요"))
        if score == "?" and not note:
            warnings.append((rid, "보류인데 무엇을 확인해야 하는지 note가 없음"))
        if "region_scope" in checks and score in {"1", "2"} and not note:
            warnings.append((rid, "지역 미지정 질문: 목적 판단 근거를 note에 남길 것"))
        signature = tuple(sorted((k, v) for k, v in status.items() if k != "region_scope"))
        by_query[(rid.split("|")[0], signature)].append((rid, score))
    for (qid, _), group in by_query.items():
        scores = {s for _, s in group if s != "?"}
        if len(scores) > 1:
            warnings.append((qid, f"같은 질의·같은 조건 상태인데 점수가 다름: {group}"))
    return violations, warnings


def build_labels(judgments, golden_rows):
    """Existing labels plus reviewed judgments, as a new label set. A reviewed row replaces the
    existing judgment of the same pair; '?' keeps the pair unjudged."""
    labels = {g["query_id"]: json.loads(json.dumps(g)) for g in golden_rows}
    for j in judgments:
        qid, did = j["review_id"].split("|", 1)
        label = labels[qid]
        for key in ("judged_irrelevant", "must_exclude", "unjudged"):
            label[key] = [d for d in label[key] if d != did]
        label["relevant"].pop(did, None)
        score, reason = str(j["score"]), j.get("reason") or ""
        if score in {"1", "2"}:
            label["relevant"][did] = int(score)
        elif score == "0":
            label["must_exclude" if reason in HARD_REASONS else "judged_irrelevant"].append(did)
        else:
            label["unjudged"].append(did)
    for label in labels.values():
        for key in ("judged_irrelevant", "must_exclude", "unjudged"):
            label[key] = sorted(set(label[key]))
        grades = set(label["relevant"].values())
        label["answer_grade"] = "full" if 2 in grades else "acceptable_only" if grades else None
        label["evaluable"] = (not label["unjudged"]) if label["expected_behavior"] == "abstain" else bool(grades)
    return [labels[q] for q in sorted(labels)]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build")
    v = sub.add_parser("validate")
    v.add_argument("judgments", type=Path)
    lab = sub.add_parser("labels")
    lab.add_argument("judgments", type=Path)
    lab.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "build":
        return build()
    judgments = read_jsonl(args.judgments)
    suggestions = {s["review_id"]: s for s in read_jsonl(PREP / "review_suggestions.jsonl")}
    violations, warnings = validate(judgments, suggestions)
    if args.command == "validate":
        for rid, message in violations:
            print(f"[위반] {rid}: {message}")
        for rid, message in warnings:
            print(f"[확인] {rid}: {message}")
        print(f"{len(judgments)} judgments, {len(violations)} violations, {len(warnings)} warnings")
        sys.exit(1 if violations else 0)
    if violations:
        sys.exit(f"criteria violations ({len(violations)}); run validate first")
    if args.out.resolve() == GOLDEN.resolve():
        sys.exit("refusing to overwrite labels/public_data_golden.jsonl")
    write_jsonl(args.out, build_labels(judgments, read_jsonl(GOLDEN)))
    print(f"{len(judgments)} reviewed judgments -> {args.out}")


if __name__ == "__main__":
    main()
