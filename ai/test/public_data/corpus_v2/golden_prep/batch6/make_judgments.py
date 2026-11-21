"""judgments.tsv (one line per pair, written while judging) -> judgments.jsonl in the batch5 row format.

    python -X utf8 test/public_data/corpus_v2/golden_prep/batch6/make_judgments.py [--dir <batch folder> --origin <name>]

judgments.tsv columns, tab separated (lines starting with # are skipped):
  review_id  score(2/1/0/?)  reason  note  [checks]
checks: `key=result:evidence` items joined by ` ; ` (result 충족/부분/불충족, source card unless the
evidence starts with `official:`). A region_scope record is added for every 1/2 on a question without a
region unless the line gives one: it says the region is judged by function, as the 2차 기준 asks.
"""

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
JUDGED_ON = "2026-11-20"


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def parse_checks(text):
    items = {}
    for part in filter(None, (p.strip() for p in (text or "").split(" ; "))):
        key, rest = part.split("=", 1)
        result, evidence = rest.split(":", 1)
        source = "card"
        if evidence.startswith("official:"):
            source, evidence = "official_page", evidence[len("official:"):]
        items[key.strip()] = {"result": result.strip(), "evidence": evidence.strip(), "source": source}
    return items


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dir", type=Path, default=HERE, help="batch folder with items.jsonl and judgments.tsv")
    parser.add_argument("--origin", default="pilot1_unjudged", help="where the batch's pairs came from")
    parser.add_argument("--judged-on", default=JUDGED_ON)
    args = parser.parse_args()
    here = args.dir
    items = {i["review_id"]: i for i in read_jsonl(here / "items.jsonl")}
    suggestions = {s["review_id"]: s for s in read_jsonl(here / "review_suggestions.jsonl")}
    rows = []
    for n, line in enumerate((here / "judgments.tsv").read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) < 4:
            raise SystemExit(f"judgments.tsv:{n}: needs review_id, score, reason, note")
        rid, score, reason, note = (c.strip() for c in cols[:4])
        if rid not in items:
            raise SystemExit(f"judgments.tsv:{n}: {rid} is not in items.jsonl")
        checks = parse_checks(cols[4] if len(cols) > 4 else "")
        f = items[rid]["facts"]
        if "region_scope" in suggestions[rid]["checks"] and score in {"1", "2"} and "region_scope" not in checks:
            scope = ",".join(f["coverage_regions"]) or "범위 표시 없음"
            checks["region_scope"] = {"result": "충족", "source": "card",
                                      "evidence": f"질문에 지역 범위 없음. 데이터 범위({scope})는 감점하지 않고 기능으로 판단"}
        held = score == "?"
        rows.append({"review_id": rid, "score": score, "reason": reason if score == "0" else "", "note": note,
                     "judge": "claude", "judgment_kind": "llm_first_pass", "judged_on": args.judged_on, "batch": here.name,
                     "origin": args.origin,
                     "verification": {"status": "pending" if held else "confirmed", "items": checks,
                                      "pending": [note] if held else []}})
    (here / "judgments.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    print(f"{len(rows)} judgments -> {here / 'judgments.jsonl'}")


if __name__ == "__main__":
    main()
