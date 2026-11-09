"""Priority review batch for the public golden set: build it, check judgments, turn them into labels.

    python test/public_data/corpus_v2/review_batch.py build
    python test/public_data/corpus_v2/review_batch.py validate <judgments.jsonl>
    python test/public_data/corpus_v2/review_batch.py labels <judgments.jsonl> --out <file> [--resolutions <json>]

Batch 1 = every existing hold and high-review row (54) + new unjudged candidates the preliminary
search ranked in the top 5 of either mode. Reviewer files carry no rank, mode or proposal.

A judgment row:
  {review_id, score: "2"|"1"|"0"|"?", reason, note, judge, judged_on,
   judgment_kind: "llm_first_pass" | "human",
   verification: {status: "confirmed" | "pending" | "not_needed",
                  items: {<check or topic key>: {result: 충족|부분|불충족, evidence, source: card|official_page|other}},
                  pending: [<what still has to be confirmed>]}}

Criteria (test/public_data/README.md, "2차 판정 기준"), enforced by validate():
  - no 1 or 2 when an explicit required condition is unmet (region named by the question,
    commercial use, 공공누리 제1유형 only, API or file, district, language, period, spatial unit)
  - a condition the card leaves unknown can only support a 1, a 2, or a 0 for that condition's
    reason through a structured confirmation of that very condition; "확인 권장" text does not count
  - '?' must list what is pending; a settled score must not leave anything pending
  - missing information is '?', never 1
Warnings (purpose basis, inconsistent scores, abstention evidence) carry ids. Labels are only
written once every warning has a recorded resolution (--resolutions {warning_id: reason}).
Labels go to a separate file; labels/public_data_golden.jsonl is never written.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
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
KINDS = {"llm_first_pass", "human"}
REASONS = {"off_topic", "wrong_region", "wrong_delivery", "license", "stale",
           "wrong_language", "wrong_period", "wrong_spatial_unit"}
HARD_REASONS = {"wrong_region", "wrong_delivery", "license"}
# Every explicit requirement of a query the automatic checks know, and the 0-reasons that rest on it.
CONDITION_REASONS = {
    "region": {"wrong_region"}, "district": {"wrong_region"},
    "commercial": {"license"}, "kogl_type1_only": {"license"},
    "delivery": {"wrong_delivery"}, "realtime": {"wrong_delivery"},
    "language": {"wrong_language"}, "period": {"wrong_period"}, "spatial_unit": {"wrong_spatial_unit"},
}
RESULTS = {"충족", "부분", "불충족"}
SOURCES = {"card", "official_page", "other"}
# A note that only says the card lacks information is a hold, not a partial fit.
LACK_ONLY_RE = re.compile(r"^(?:[^.]*?)(정보\s*(?:가\s*)?부족|확인\s*(?:불가|안\s*됨|할\s*수\s*없)|알\s*수\s*없|판단\s*불가)[^.]*$")
# A range the question itself states; without one, a region limit is not a deduction.
STATED_RANGE_RE = re.compile(r"전국|모든 지역|서울만이 아니라|여러 지역|각 지역")
# Open-ended checking left in a settled judgment.
PENDING_RE = re.compile(r"확인\s*(?:권장|필요|요망|예정)|원문\s*확인|추가\s*확인|재확인")


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path, rows):
    Path(path).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


# ---------------------------------------------------------------- batch


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


# ---------------------------------------------------------------- validation


def confirmed(item, results):
    return bool(item) and item.get("result") in results and str(item.get("evidence") or "").strip() \
        and item.get("source") in SOURCES


def validate(judgments, suggestions, queries=None):
    """(violations, warnings). Violations break a criterion; warnings are (id, review_id, message)."""
    violations, warnings = [], []
    by_signature = defaultdict(list)
    queries = queries or {}
    for j in judgments:
        rid = j["review_id"]
        score, reason, note = str(j.get("score") or ""), j.get("reason") or "", (j.get("note") or "").strip()
        ver = j.get("verification") or {}
        items, pending = ver.get("items") or {}, ver.get("pending") or []
        if rid not in suggestions:
            violations.append((rid, "자동 검사(review_suggestions)에 없는 후보 — --suggestions를 확인"))
            continue
        checks = suggestions[rid]["checks"]
        status = {k: c["status"] for k, c in checks.items()}

        def bad(message):
            violations.append((rid, message))

        if score not in SCORES:
            bad(f"점수 '{score}'는 2/1/0/? 가 아님")
            continue
        if j.get("judgment_kind") not in KINDS:
            bad(f"judgment_kind '{j.get('judgment_kind')}'는 llm_first_pass/human 이 아님")
        if score == "0" and reason not in REASONS:
            bad(f"0점 사유 '{reason}' 없음 또는 알 수 없음")
        for key, item in items.items():
            if item.get("result") not in RESULTS or not str(item.get("evidence") or "").strip() or item.get("source") not in SOURCES:
                bad(f"확인 기록 '{key}'에 result(충족/부분/불충족)·evidence·source(card/official_page/other)가 다 있어야 함")
        # Explicit requirements: unmet means no 1 or 2, unless a confirmation overturns the card.
        for key, st in status.items():
            if key not in CONDITION_REASONS:
                continue
            if st == "불충족" and score in {"1", "2"} and not confirmed(items.get(key), {"충족", "부분"}):
                bad(f"필수 조건 '{key}' 불충족인데 {score}점")
            if st == "미확인" and score in {"1", "2"} and not (
                    ver.get("status") == "confirmed" and confirmed(items.get(key), {"충족", "부분"})):
                bad(f"미확인 조건 '{key}'를 확인 기록 없이 {score}점으로 판정")
            # A 0 whose reason another unmet condition already carries (API required, file only) needs
            # nothing about this one.
            backed = any(status.get(k) == "불충족" and reason in r for k, r in CONDITION_REASONS.items() if k != key)
            if st == "미확인" and score == "0" and reason in CONDITION_REASONS[key] and not backed \
                    and not confirmed(items.get(key), {"불충족"}):
                bad(f"미확인 조건 '{key}'를 근거로 0점({reason})인데 불충족 확인 기록 없음")
        if score == "?":
            if ver.get("status") != "pending" or not pending:
                bad("보류인데 verification.status=pending과 확인할 항목(pending)이 없음")
        else:
            if pending:
                bad(f"확정 점수인데 미결 항목이 남음: {pending}")
            if PENDING_RE.search(note):
                bad(f"확정 점수의 note에 미결 확인 문구: '{note}'")
        if score == "1" and not note:
            bad("1점인데 부분 적합 내용이 note에 없음")
        if score == "1" and note and LACK_ONLY_RE.search(note) and not re.search(r"부분|일부|만 제공|만 있|없지만|한정", note):
            bad(f"정보 부족을 1점으로 처리: '{note}'")
        if "region_scope" in checks and score in {"1", "2"} and not confirmed(items.get("region_scope"), RESULTS):
            warnings.append((f"purpose_basis:{rid}", rid, "지역 미지정 질문: 목적 판단 근거를 verification.items.region_scope에 기록"))
        query = queries.get(rid.split("|")[0]) or {}
        scope = items.get("region_scope") or {}
        if scope.get("result") in {"부분", "불충족"} and query.get("query") is not None \
                and not (query.get("conditions") or {}).get("region") and not STATED_RANGE_RE.search(query["query"]):
            warnings.append((f"unstated_scope:{rid}", rid, "질문에 없는 지역 범위로 감점: 범위를 말하지 않은 질문은 기능 충족으로 판단"))
        if query.get("expected_behavior") == "abstain" and score in {"1", "2"}:
            warnings.append((f"abstain_relevant:{rid}", rid, "기권 질의에 관련 데이터 판정: 질의 변경 근거로 쓰기 전 요구 범위 확인"))
        # Same query, same automatic checks and same recorded scope/aspect findings should score
        # the same. Off-topic zeros are left out: the topic, not these findings, decided them.
        if not (score == "0" and reason == "off_topic"):
            recorded = tuple((k, (items.get(k) or {}).get("result")) for k in ("region_scope", "aspects"))
            signature = tuple(sorted((k, v) for k, v in status.items() if k != "region_scope")) + recorded
            by_signature[(rid.split("|")[0], signature)].append((rid, score))
    for (qid, signature), group in by_signature.items():
        if len({s for _, s in group if s != "?"}) > 1:
            digest = hashlib.sha1(repr(signature).encode()).hexdigest()[:8]
            warnings.append((f"inconsistent:{qid}:{digest}", qid, f"같은 질의·같은 조건 상태인데 점수가 다름: {group}"))
    return violations, warnings


# ---------------------------------------------------------------- labels


def build_labels(judgments, golden_rows):
    """Existing labels plus reviewed judgments, as a new label set. A reviewed row replaces the
    existing judgment of the same pair; '?' keeps the pair unjudged. Each reviewed pair records
    who judged it and how (review_provenance), so LLM first-pass labels stay distinguishable."""
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
        label.setdefault("review_provenance", {})[did] = {
            "judge": j.get("judge"), "judgment_kind": j.get("judgment_kind"), "judged_on": j.get("judged_on")}
    for label in labels.values():
        for key in ("judged_irrelevant", "must_exclude", "unjudged"):
            label[key] = sorted(set(label[key]))
        grades = set(label["relevant"].values())
        label["answer_grade"] = "full" if 2 in grades else "acceptable_only" if grades else None
        label["evaluable"] = (not label["unjudged"]) if label["expected_behavior"] == "abstain" else bool(grades)
    return [labels[q] for q in sorted(labels)]


def review_queue(judgments, suggestions, revised=()):
    """Rows a person should review, and why. Reviewers judge from items.jsonl before reading these."""
    queue = []
    for j in judgments:
        rid, score, reason = j["review_id"], str(j["score"]), j.get("reason") or ""
        topic = suggestions[rid].get("topic") or {}
        why = []
        if score in {"1", "2"}:
            why.append("positive")  # every answer label
        if score == "0" and reason == "off_topic" and (topic.get("full") or topic.get("partial")):
            why.append("related_topic_zero")  # the card shares the topic words, yet it was judged off-topic
        if score == "0" and reason != "off_topic":
            why.append("condition_zero")
        if score == "?":
            why.append("pending_official_check")
        if rid in revised:
            why.append("revised")
        if why:
            queue.append({"review_id": rid, "queue_reasons": why, "judgment_kind": j.get("judgment_kind"),
                          "human_judgment": None})
    return queue


def unresolved(warnings, resolutions):
    return [w for w in warnings if not str(resolutions.get(w[0]) or "").strip()]


def coverage(judgments, expected_ids):
    """Violations unless the judgments hold every expected review_id exactly once and nothing else."""
    ids = Counter(j["review_id"] for j in judgments)
    return ([(rid, f"판정이 {n}번 있음 (중복)") for rid, n in sorted(ids.items()) if n > 1]
            + ([(rid, "배치 후보인데 판정이 없음 (누락)") for rid in sorted(set(expected_ids) - set(ids))] if expected_ids is not None else [])
            + ([(rid, "배치 후보 목록에 없는 판정") for rid in sorted(set(ids) - set(expected_ids))] if expected_ids is not None else []))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build")
    v = sub.add_parser("validate")
    v.add_argument("judgments", type=Path)
    lab = sub.add_parser("labels")
    lab.add_argument("judgments", type=Path)
    lab.add_argument("--out", type=Path, required=True)
    lab.add_argument("--resolutions", type=Path, help="json {warning_id: 검토 완료 사유}")
    lab.add_argument("--base", type=Path, default=GOLDEN, help="label set the judgments are applied to (default: the golden set)")
    for p in (v, lab):  # a later batch brings its own automatic checks for pairs outside review_suggestions.jsonl
        p.add_argument("--suggestions", type=Path, default=PREP / "review_suggestions.jsonl")
        p.add_argument("--expected", type=Path,
                       help="jsonl whose review_ids the batch must cover exactly (default: items.jsonl next to the judgments)")
    que = sub.add_parser("queue")
    que.add_argument("judgments", type=Path)
    args = parser.parse_args()
    if args.command == "build":
        return build()
    if args.command == "queue":
        suggestions = {s["review_id"]: s for s in read_jsonl(PREP / "review_suggestions.jsonl")}
        revised = {r["review_id"] for r in read_jsonl(BATCH / "revisions.jsonl")} if (BATCH / "revisions.jsonl").exists() else set()
        queue = review_queue(read_jsonl(args.judgments), suggestions, revised)
        write_jsonl(BATCH / "human_review_queue.jsonl", queue)
        print(f"{len(queue)} rows -> {BATCH / 'human_review_queue.jsonl'} {dict(Counter(w for q in queue for w in q['queue_reasons']))}")
        return
    judgments = read_jsonl(args.judgments)
    suggestions = {s["review_id"]: s for s in read_jsonl(args.suggestions)}
    queries = {i["query_id"]: i for i in read_jsonl(PREP / "review_items.jsonl")} if (PREP / "review_items.jsonl").exists() else {}
    violations, warnings = validate(judgments, suggestions, queries)
    expected = args.expected or args.judgments.parent / "items.jsonl"
    if args.expected and not expected.exists():
        sys.exit(f"--expected not found: {expected}")
    expected_ids = [i["review_id"] for i in read_jsonl(expected)] if expected.exists() else None
    if expected_ids is None:
        print(f"[주의] 배치 후보 목록({expected})이 없어 누락·추가는 검사하지 않음(중복만 검사)")
    violations = coverage(judgments, expected_ids) + violations
    if args.command == "validate":
        for rid, message in violations:
            print(f"[위반] {rid}: {message}")
        for wid, _, message in warnings:
            print(f"[경고 {wid}] {message}")
        print(f"{len(judgments)} judgments ({dict(Counter(j.get('judgment_kind') for j in judgments))}), "
              f"{len(violations)} violations, {len(warnings)} warnings")
        sys.exit(1 if violations else 0)
    if violations:
        sys.exit(f"criteria violations ({len(violations)}); run validate first")
    resolutions = json.loads(args.resolutions.read_text(encoding="utf-8")) if args.resolutions else {}
    open_warnings = unresolved(warnings, resolutions)
    if open_warnings:
        sys.exit(f"{len(open_warnings)} unresolved warnings; record a 검토 완료 사유 per id in --resolutions: "
                 + ", ".join(w[0] for w in open_warnings[:10]))
    out = args.out.resolve()
    inputs = [GOLDEN, args.base, args.judgments, args.suggestions, expected, args.resolutions]
    protected = {p.resolve() for p in inputs if p} | {p.resolve().with_suffix(".meta.json") for p in inputs if p}
    if {out, out.with_suffix(".meta.json")} & protected:
        sys.exit(f"refusing to overwrite an input ({out.name} or its .meta.json): write the new labels to a separate file")
    base_rows, base_sha = read_jsonl(args.base), hashlib.sha256(args.base.read_bytes()).hexdigest()
    missing = sorted({j["review_id"].split("|", 1)[0] for j in judgments} - {g["query_id"] for g in base_rows})
    if missing:
        sys.exit(f"--base has no label for queries {missing}: check --base")
    write_jsonl(args.out, build_labels(judgments, base_rows))
    args.out.with_suffix(".meta.json").write_text(json.dumps({
        "judgments": str(args.judgments),
        "judgments_sha256": hashlib.sha256(args.judgments.read_bytes()).hexdigest(),
        "expected": str(expected) if expected_ids is not None else None,
        "base": str(args.base),
        "base_sha256": base_sha,
        "judgment_kinds": dict(Counter(j.get("judgment_kind") for j in judgments)),
        "warnings_resolved": {w[0]: resolutions[w[0]] for w in warnings},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(judgments)} reviewed judgments -> {args.out}")


if __name__ == "__main__":
    main()
