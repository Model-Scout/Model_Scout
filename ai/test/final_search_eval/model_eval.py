#!/usr/bin/env python3
"""프로젝트형 모델 질문 30개로 모델 검색의 최종 성능을 잰다. A 가 운영 그대로의 값이고, B 는 리랭커를 켠 비교군이다.

    A   운영 그대로: project 경로(PROJECT_MODEL_SEARCH, rerank 꺼짐)의 검색 순서
    B1  운영 리랭커(model_rerank.rerank)를 켠 것: 사용자 질문 원문으로 다시 줄 세운다
    B2  B1 + 이 목록이 맡을 역할(need 의 purpose_ko·task)을 질문 뒤에 붙인다

세 방식은 **같은 후보 20개**를 줄 세운다. 운영 search_models 를 그대로 부르되 PROJECT_MODEL_SEARCH 를
rerank=True·match_count=20 으로 바꾸고, model_rerank.rerank 를 가로채 재순위 직전 목록(필터까지 끝난
검색 순서)을 받는다. A 는 그 목록이고(운영 A 는 6개를 읽어 3개를 보여 주는데, 같은 검색의 앞부분이다),
B1·B2 는 그 목록에 실제 rerank 를 부른 결과다. LLM 순서는 흔들리므로 B 는 --runs 번 돌려 평균한다.

    # ai/ 에서. OpenAI(planner·router·rerank)와 Supabase 읽기 전용 호출이 있다
    python -X utf8 test/final_search_eval/model_eval.py labels                  # 정답 전수 스캔, API 0회
    python -X utf8 test/final_search_eval/model_eval.py run --dir test/final_search_eval/runs/<폴더> --runs 2
    python -X utf8 test/final_search_eval/model_eval.py score --dir test/final_search_eval/runs/<폴더>
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
AI = HERE.parents[1]
TOOLS = AI / "test" / "model_retrieval" / "tools"
LABELS = HERE / "model_labels.json"

# 서버(deploy/release.sh)와 같은 조건. LLM 은 코드 기본값(OpenAI gpt-4.1-mini)이고 로컬 .env 의 ollama 를 쓰지 않는다.
os.environ.update(RECOMMEND_LLM_PROVIDER="openai", RECOMMEND_LLM_MODEL="gpt-4.1-mini", MODEL_SPARSE_IDF_ENABLED="1")
sys.path[:0] = [str(AI), str(HERE), str(TOOLS)]

import metrics  # noqa: E402
import project_questions  # noqa: E402


def load_graph():
    spec = importlib.util.spec_from_file_location("rg", AI / "17_recommend_graph.py")
    rg = importlib.util.module_from_spec(spec)
    sys.modules["rg"] = rg
    spec.loader.exec_module(rg)
    return rg


def family(rg, task: str) -> str:
    return rg.MODEL_TASK_FALLBACK.get(task, task)


def role_tags(rg, role: dict) -> list[str]:
    families = [role["family"], *role["also_family"]]
    return sorted({tag for f in families for tag in rg.hf_tags(f)})


# --------------------------------------------------------------------------- 정답


def build_labels() -> int:
    import corpus
    import scan

    rg = load_graph()
    rows = corpus.load_corpus()
    scan.bind(rows)
    meta = corpus.load_meta()
    out = {"corpus": corpus.corpus_stamp(meta), "grading": "scan.py; unresolved_for_human(README 원문만) → 1점",
           "questions": {}}
    for question in project_questions.QUESTIONS:
        roles = []
        for role in question["roles"]:
            tags = role_tags(rg, role)
            query = {
                "qid": question["qid"], "text": question["text"], "query_type": "semantic_capability",
                "expected_behavior": "recommend",
                "conditions": {"korean_required": True, **({"tasks": tags} if tags else {})},
                "relevance_rule": {"scan": role["scan"], "grade_2_requires_korean_specific": role["ko"]},
            }
            result = scan.scan_query(query, rows)
            grades = {mid: 2 for mid in result["classes"]["proposed_grade_2"]}
            grades |= {mid: 1 for mid in result["classes"]["proposed_grade_1"] + result["classes"]["unresolved_for_human"]}
            roles.append({"family": role["family"], "also_family": role["also_family"], "tags": tags,
                          "eligible": result["eligible_count"], "grades": dict(sorted(grades.items()))})
            print(f"{question['qid']} {role['family']:20s} eligible {result['eligible_count']:5d}  "
                  f"2점 {sum(g == 2 for g in grades.values()):4d}  1점 {sum(g == 1 for g in grades.values()):4d}")
        out["questions"][question["qid"]] = {"text": question["text"], "roles": roles}
    LABELS.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"→ {LABELS.relative_to(AI)}")
    return 0


# --------------------------------------------------------------------------- 실행


def role_question(text: str, need: dict) -> str:
    return f"{text}\n\n(이 후보들은 이 프로젝트에서 다음 역할을 맡을 모델입니다: {need['purpose_ko']} — task {need['task']})"


def run(out_dir: Path, runs: int) -> int:
    rg = load_graph()
    from dotenv import load_dotenv
    load_dotenv(AI / ".env")
    real_rerank = rg.model_rerank.rerank
    captured: list[list[dict]] = []

    def capture(question, rows, client_factory, model):
        captured.append(list(rows))
        return list(rows)

    rg.model_rerank.rerank = capture
    rg.PROJECT_MODEL_SEARCH = {**rg.PROJECT_MODEL_SEARCH, "rerank": True,
                               "match_count": rg.model_rerank.RERANK_DEPTH}
    rerank_model = rg.model_rerank.model(rg.llm_provider())
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "model_lists.jsonl"
    done = {json.loads(line)["qid"] for line in path.open(encoding="utf-8")} if path.exists() else set()
    with path.open("a", encoding="utf-8") as sink:
        for question in project_questions.QUESTIONS:
            if question["qid"] in done:
                continue
            text = question["text"]
            started = time.perf_counter()
            route = rg._route(text)
            plan = rg._first_plan(text, route["target"] if route["target"] in ("model", "both") else "model")
            needs = []
            for need in plan["needs"]:
                captured.clear()
                state = {"request": text, "plan": {**plan, "needs": [need], "fine_tuning": []},
                         "model_route": {"path": "project"}}
                group = rg.search_models(state)["models"][0]
                rows = captured[0] if captured else group["models"]
                ids = [r["model_id"] for r in rows]
                entry = {"task": need["task"], "purpose_ko": need["purpose_ko"], "model_query": need["model_query"],
                         "unsupported": bool(group.get("unsupported")), "A": ids, "B1": [], "B2": [], "rerank_s": []}
                for _ in range(runs):
                    for key, asked in (("B1", text), ("B2", role_question(text, need))):
                        t = time.perf_counter()
                        order = real_rerank(asked, rows, rg._openai, rerank_model) if len(rows) > 1 else rows
                        entry["rerank_s"].append(round(time.perf_counter() - t, 2))
                        entry[key].append([r["model_id"] for r in order])
                needs.append(entry)
            record = {"qid": question["qid"], "text": text, "route": route.get("target"),
                      "recommend": plan.get("recommend"), "needs": needs,
                      "seconds": round(time.perf_counter() - started, 1)}
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            sink.flush()
            print(f"{question['qid']} route={record['route']} recommend={record['recommend']} "
                  f"needs={[n['task'] for n in needs]} rows={[len(n['A']) for n in needs]} {record['seconds']}s",
                  flush=True)
    meta = {"rerank_model": rerank_model, "planner_model": rg.LLM_MODEL, "runs": runs,
            "project_search": rg.PROJECT_MODEL_SEARCH, "models_shown": rg.MODELS_PER_NEED,
            "sparse_idf": rg._load_09().sparse_idf_enabled()}
    (out_dir / "model_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0


# --------------------------------------------------------------------------- 채점


def pair_roles(rg, roles: list[dict], needs: list[dict]) -> list[dict | None]:
    """역할마다 family 가 맞는 첫 need. 한 need 는 한 역할에만 쓴다."""
    used: set[int] = set()
    out: list[dict | None] = []
    for role in roles:
        families = {role["family"], *role["also_family"]}
        pick = next((i for i, n in enumerate(needs) if i not in used and family(rg, n["task"]) in families
                     and not n["unsupported"]), None)
        if pick is not None:
            used.add(pick)
        out.append(None if pick is None else needs[pick])
    return out


def score(out_dir: Path) -> int:
    rg = load_graph()
    labels = json.loads(LABELS.read_text(encoding="utf-8"))["questions"]
    records = [json.loads(line) for line in (out_dir / "model_lists.jsonl").open(encoding="utf-8")]
    variants = ("A", "B1", "B2")
    result: dict = {"by_question": {}, "paired": {}, "coverage": {}}
    for min_grade in (2, 1):
        per_q = {v: [] for v in variants}
        searched = {v: [] for v in variants}  # planner 가 need 를 낸 역할만, 역할 단위
        units = matched = 0
        for record in records:
            roles = labels[record["qid"]]["roles"]
            paired_needs = pair_roles(rg, roles, record["needs"])
            role_scores = {v: [] for v in variants}
            for role, need in zip(roles, paired_needs):
                units += 1
                matched += need is not None
                for v in variants:
                    if need is None:
                        role_scores[v].append(metrics.score([], role["grades"], min_grade))
                    elif v == "A":
                        role_scores[v].append(metrics.score(need["A"], role["grades"], min_grade))
                    else:  # LLM 순서는 여러 번 돌린 평균
                        runs = [metrics.score(order, role["grades"], min_grade) for order in need[v]]
                        role_scores[v].append({k: metrics.mean([r[k] for r in runs]) for k in runs[0]})
                    if need is not None:
                        searched[v].append(role_scores[v][-1])
            for v in variants:
                per_q[v].append({k: metrics.mean([s[k] for s in role_scores[v]]) for k in role_scores[v][0]})
            result["by_question"].setdefault(str(min_grade), {})[record["qid"]] = {
                v: per_q[v][-1] for v in variants}
        result["coverage"][str(min_grade)] = {"roles": units, "matched": matched}
        keys = list(per_q["A"][0])
        for v in ("B1", "B2"):
            for k in keys:
                result["paired"][f"g{min_grade}:{v}:{k}"] = metrics.paired(
                    [q[k] for q in per_q["A"]], [q[k] for q in per_q[v]])
                result["paired"][f"searched:g{min_grade}:{v}:{k}"] = metrics.paired(
                    [s[k] for s in searched["A"]], [s[k] for s in searched[v]])
    (out_dir / "model_scores.json").write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n",
                                               encoding="utf-8")
    print(f"질문 {len(records)}개, 역할 {result['coverage']['2']['roles']}개 중 planner 가 맞는 need 를 낸 역할 "
          f"{result['coverage']['2']['matched']}개")
    for scope, title in (
            ("", "질문 단위, 검색 못 한 역할은 0점"),
            ("searched:", "검색까지 간 역할만, 역할 단위"),
    ):
        for min_grade in (2, 1):
            print(f"\n## {title} · min_grade {min_grade}      A      B1  (Δ, 95% CI)                 B2  (Δ, 95% CI)")
            for k in ("ndcg@3", "ndcg@5", "ndcg@10", "mrr@10", "r@5", "r@10", "p@3", "p@5", "hit@3"):
                b1, b2 = (result["paired"][f"{scope}g{min_grade}:{v}:{k}"] for v in ("B1", "B2"))
                print(f"{k:8s}  {b1['a']:.3f}   {b1['b']:.3f} ({b1['delta']:+.3f} [{b1['lo']:+.3f},{b1['hi']:+.3f}] "
                      f"↑{b1['up']}↓{b1['down']})   {b2['b']:.3f} ({b2['delta']:+.3f} [{b2['lo']:+.3f},{b2['hi']:+.3f}] "
                      f"↑{b2['up']}↓{b2['down']})")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("labels", "run", "score"))
    ap.add_argument("--dir", type=Path)
    ap.add_argument("--runs", type=int, default=2)
    args = ap.parse_args()
    if args.step == "labels":
        return build_labels()
    if args.dir is None:
        ap.error("--dir 가 필요합니다")
    return run(args.dir, args.runs) if args.step == "run" else score(args.dir)


if __name__ == "__main__":
    raise SystemExit(main())
