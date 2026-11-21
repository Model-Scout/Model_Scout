"""The service's condition reader (ai/data_conditions.py) on a question set, beside the service planner as 17 runs
them: extraction scored against the spec, and the time each call and the turn take. Plus multi-turn cases.

    python -X utf8 test/public_data/retrieval/conditions_check.py --spec <spec> --routes <run with plans.jsonl> --out <dir>
    python -X utf8 test/public_data/retrieval/conditions_check.py --turns --out <dir>     # follow-up cases only
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import decompose_compare  # noqa: E402
import decompose_v2 as dv  # noqa: E402
import pilot  # noqa: E402

TURNS = [  # (name, turns, what the last turn should leave)
    ("delivery changed", ["서울 공영주차장 위치를 API로 받고 싶어", "API 말고 파일로 받을래"], {"delivery": "file"}),
    ("detail kept", ["청주 공중화장실 위치 데이터 찾아줘", "상업용으로 쓸 거야"], {"region": "충북", "region_detail": "청주"}),
    ("type1 added, api kept", ["버스 도착 정보를 API로 받고 싶어", "공공누리 1유형 데이터만 보여줘"], {"delivery": "api", "kogl_type1_only": True}),
    ("csv not from api", ["전국 전통시장 목록을 API로 받을 수 있는 데이터"], {"delivery": "api", "formats": [], "region_scope": "전국"}),
    ("file format", ["침수흔적도를 SHP 파일로 받고 싶어요"], {"delivery": "file", "formats": ["SHP"]}),
    ("interval not current", ["매시간 바뀌는 강수확률 데이터를 알림에 쓰고 싶어"], {"current_value": False}),
    ("current value", ["지금 빈자리가 있는 공영주차장을 알려주는 데이터"], {"current_value": True}),
]


def extracted(c, commercial):
    return {"region": dv.canon_region(c["region"]) or c["region_detail"], "region_scope": c["region_scope"],
            "delivery": c["delivery"], "realtime": c["current_value"], "commercial": commercial,
            "kogl_type1_only": c["kogl_type1_only"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--spec", type=Path)
    parser.add_argument("--routes", type=Path)
    parser.add_argument("--turns", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    rg = decompose_compare.load_graph_module()
    client, model = rg._openai(), rg.LLM_MODEL
    args.out.mkdir(parents=True, exist_ok=True)
    L = []
    if args.turns:
        L += ["## 후속 발화 사례", "", "| 사례 | 마지막 턴 | 기대 | 결과 | 맞음 |", "|---|---|---|---|---|"]
        rows = []
        for name, turns, want in TURNS:
            previous, earlier = None, []
            for t in turns:
                got = rg.data_conditions.extract(client, model, t, earlier or None, previous)
                previous, earlier = got, [*earlier, t]
            ok = all(got[k] == v for k, v in want.items())
            rows.append({"case": name, "turns": turns, "want": want, "got": got, "ok": ok})
            L.append(f"| {name} | {turns[-1]} | {want} | { {k: got[k] for k in want} } | {'O' if ok else 'X'} |")
        (args.out / "turns.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    if args.spec:
        specs = pilot.read_jsonl(args.spec)
        routes = {p["query_id"]: p for p in pilot.read_jsonl(args.routes / "plans.jsonl")}
        pool, rows = ThreadPoolExecutor(max_workers=2), []
        for s in specs:
            q, target = s["query"], routes[s["query_id"]]["target_used"]
            if target not in rg.DATA_TARGETS:
                rows.append({"query_id": s["query_id"], "target": target, "skipped": True})
                continue
            timed = lambda f: (lambda t0: (f(), time.perf_counter() - t0))(time.perf_counter())  # noqa: E731
            reader = pool.submit(timed, lambda: rg.data_conditions.extract(client, model, " ".join(q.split())))
            started = time.perf_counter()
            plan, t_plan = timed(lambda: rg._parse_plan(" ".join(q.split()), target))
            cond, t_cond = reader.result()
            t_turn = time.perf_counter() - started
            want, got = dv.truth(s), extracted(cond, bool(plan["constraints"]["commercial_only"]))
            rows.append({"query_id": s["query_id"], "target": target, "t_plan": t_plan, "t_reader": t_cond, "t_both": t_turn,
                         "conditions": cond, "cmp": dv.compare(want, got, s), "want": want, "got": got,
                         "detail_kept": (cond["region_detail"] == s["region_detail"] or s["region_detail"] in (cond["region_evidence"] or ""))
                         if s.get("region_detail") else None})
            print(s["query_id"], f"plan {t_plan:.1f}s reader {t_cond:.1f}s", flush=True)
        (args.out / "conditions.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
        done = [r for r in rows if not r.get("skipped")]
        tot = Counter(s for r in done for s in r["cmp"].values())
        pct = lambda xs, p: sorted(xs)[min(len(xs) - 1, int(p / 100 * len(xs)))]  # noqa: E731
        L += [f"## 조건 추출: 명세 `{args.spec.stem}` ({len(done)}문항, 데이터 경로 아님 {len(rows) - len(done)})", "",
              f"맞음 {tot['ok']}, 누락 {tot['missed']}, 잘못 추가 {tot['added']}, 값 틀림 {tot['wrong']}, 채점 제외 {tot['exempt']}", ""]
        L += [f"- {r['query_id']}: " + "; ".join(f"{c} {v} (명세 {r['want'][c]!r}, 추출 {r['got'][c]!r})" for c, v in r["cmp"].items()
                                              if v in ("missed", "added", "wrong")) for r in done
              if any(v in ("missed", "added", "wrong") for v in r["cmp"].values())]
        detail = [f"{r['query_id']} {'O' if r['detail_kept'] else 'X'}" for r in done if r["detail_kept"] is not None]
        L += ["", "세부 지역 보존: " + (", ".join(detail) or "해당 없음"), "", "## 시간 (초, 분해와 동시에 실행)", "",
              "| | p50 | p95 | 최대 |", "|---|---:|---:|---:|"]
        for k, name in (("t_plan", "분해"), ("t_reader", "조건 추출"), ("t_both", "둘 다 끝날 때까지")):
            xs = [r[k] for r in done]
            L.append(f"| {name} | {pct(xs, 50):.2f} | {pct(xs, 95):.2f} | {max(xs):.2f} |")
        slower = sum(r["t_reader"] > r["t_plan"] for r in done)
        L += ["", f"조건 추출이 분해보다 늦게 끝난 문항 {slower}/{len(done)}, 그 때문에 늘어난 시간 합 "
              f"{sum(max(0, r['t_both'] - r['t_plan']) for r in done):.1f}초"]
    (args.out / "report.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
