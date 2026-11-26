"""One capped run of the representative recommend/direct scenarios against the real planner, router, writer,
model catalog (read-only) and dataset index, through the AI API's own guards, then the backend's done payload.

Not a test: it spends real calls. Each conversation runs once and is never retried; the run stops at --max-calls
OpenAI calls, and what did not run is reported as unverified. Every chat and embedding call is metered at the
OpenAI client (count and tokens). Checkpoints stay in process memory; nothing is written to any database.

    RECOMMEND_LLM_PROVIDER=openai RECOMMEND_LLM_MODEL=gpt-4.1-mini MODEL_SCOUT_CORPUS=v2 \\
    MODEL_SCOUT_DATA_VERSION=aa1a71d35a121150 python ai/test/golden/recommend_branches_eval.py --max-calls 80
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
from collections import Counter
from datetime import date
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "ai"))
REPORTS = ROOT / "ai/test/golden/reports"

# (id, turns, answers to clarify questions, expectations on the last turn). Ids are what the catalog holds (checked
# before the run); none of these texts is used in a prompt.
SCENARIOS = [
    ("S01", ["강의 녹음을 받아써서 요약해 주는 앱을 만들고 싶어. 필요한 모델이랑 데이터 추천해줘"], ["알아서 해줘"],
     {"recommend": True, "display": "recommendation", "model_path": "project", "classifier": 0}),
    ("S02", ["intfloat/multilingual-e5-large 모델 사양 알려줘"], [],
     {"recommend": False, "display": "chat", "model_path": "lookup", "classifier": 0, "answer_has": ["514"]}),
    ("S03", ["intfloat/multilingual-e5-large랑 intfloat/multilingual-e5-small 입력 길이 비교해줘"], [],
     {"recommend": False, "display": "chat", "model_path": "lookup", "classifier": 0, "answer_has": ["512", "514"]}),
    ("S04", ["한국어 문장 임베딩 모델 추천해줘"], [],
     {"recommend": False, "display": "chat", "model_path": "typed"}),
    ("S05", ["서울시 문화행사 정보 데이터셋 알려줘"], [],
     {"recommend": False, "display": "chat", "dataset_path": "lookup", "datasets_any": ["seoul_open_data/OA-15486"]}),
    ("S06", ["서울 따릉이 공공데이터 찾아줘"], [],
     {"recommend": False, "display": "chat", "dataset_path": "search"}),
    ("S07", ["NoSuchModel-9000 모델 라이선스 알려줘"], [],
     {"recommend": False, "display": "chat", "answer_has": ["정확히 일치하는 모델 이름을 확인하지 못했어요"]}),
    # S08 and S09 are one conversation: a recommendation, a direct comparison, then a new project.
    ("S08-09", ["회의록을 요약하는 사내 서비스를 만들고 싶어. 모델과 데이터 추천해줘",
                "이번엔 intfloat/multilingual-e5-small이랑 intfloat/multilingual-e5-base 입력 길이만 비교해줘",
                "이번엔 따릉이 대여소 안내 앱을 새로 만들고 싶어. 모델과 데이터 추천해줘"], ["알아서 해줘", "알아서 해줘"],
     {0: {"recommend": True, "display": "recommendation"},
      1: {"recommend": False, "display": "chat", "model_path": "lookup", "no_dataset_search": True},
      2: {"recommend": True, "display": "recommendation", "no_names_from": ["e5"]}}),
    ("S10", ["BGE 같은 더 가벼운 한국어 임베딩 모델 찾아줘"], [],
     {"recommend": False, "display": "chat", "model_path": "typed", "reference": "BGE"}),
]


# S04 and S05 after the follow-up fix, with a variant and an opposite case for each. Ids are the catalog's, checked
# before the run; none of these texts is in a prompt.
S04_S05 = [
    ("S04", ["한국어 문장 임베딩 모델 추천해줘"], [],
     {"recommend": False, "display": "chat", "model_path": "typed", "no_dataset_search": True}),
    ("S05", ["서울시 문화행사 정보 데이터셋 알려줘"], [],
     {"recommend": False, "display": "chat", "mentions_dataset": "서울시 문화행사 정보", "dataset_path": "lookup",
      "no_model_search": True, "datasets_all": ["seoul_open_data/OA-15486", "seoul_open_data/OA-23041"]}),
    ("V04", ["요약을 잘하는 한국어 모델 알려줘"], [],
     {"recommend": False, "display": "chat", "model_path": "typed", "no_dataset_search": True}),
    ("V05", ["서울시 공공자전거 따릉이 대여소 정보 데이터셋 알려줘"], [],
     {"recommend": False, "display": "chat", "dataset_path": "lookup", "no_model_search": True,
      "datasets_all": ["seoul_open_data/OA-13252"]}),
    ("C04", ["인터뷰 녹음을 받아써서 기사 초안을 만드는 서비스를 만들고 싶어. 모델 추천해줘"], ["알아서 해줘"],
     {"recommend": True, "display": "recommendation", "model_path": "project"}),
    ("C05", ["서울 문화행사 관련 데이터 찾아줘"], [],
     {"recommend": False, "display": "chat", "dataset_path": "search", "no_mentioned_datasets": True}),
    ("C04b", ["RAG 프로젝트에 쓸 한국어 임베딩 모델 추천해줘"], [],
     {"recommend": False, "display": "chat", "model_path": "typed"}),
]
# A name several catalog models share: read when they are one family (BGE-M3: derivatives of BAAI/bge-m3, which the
# catalog lacks), never read when they are unrelated (qwen), never read as a yardstick. Families measured on the live
# catalog on 2026-11-26.
AMBIGUOUS_NAMES = [
    ("A01", ["BGE-M3 라이선스가 뭐야?"], [],
     {"recommend": False, "display": "chat", "model_path": "lookup", "classifier": 0,
      "answer_has": ["같은 계열(원본 BAAI/bge-m3)"],
      "answer_lacks": ["찾지 못했어요", "하나로 정하지 않았어요", "|", "니다"]}),  # no table; 해요체 only
    ("A02", ["qwen 라이선스 알려줘"], [],
     {"recommend": False, "display": "chat", "model_path": "fallback",
      "answer_has": ["원본이 서로 다른 여러 모델"], "answer_lacks": ["찾지 못했어요"]}),
    ("A03", ["bge-m3보다 가벼운 한국어 임베딩 모델 찾아줘"], [],
     {"recommend": False, "display": "chat", "model_path": "typed", "reference": "bge-m3", "models_found": True,
      "answer_lacks": ["찾지 못했어요"]}),
    ("A05", ["BGE-M3 대신 쓸 만한 상업용 임베딩 모델 있어?"], [],
     {"recommend": False, "display": "chat", "model_path": "typed", "reference": "BGE-M3", "models_found": True,
      "models_lack": ["bge-m3"]}),  # a replaced yardstick's own models are left out
    ("A06", ["bge m3 라이선스 어떻게 돼?"], [],  # a spaced name is the hyphenated one
     {"recommend": False, "display": "chat", "model_path": "lookup", "answer_has": ["같은 계열(원본 BAAI/bge-m3)"],
      "answer_lacks": ["확인하지 못했어요", "찾지 못했어요"]}),
    ("A04", ["dragonkue/BGE-m3-ko 라이선스 알려줘"], [],
     {"recommend": False, "display": "chat", "model_path": "lookup", "classifier": 0,
      "answer_lacks": ["같은 계열", "니다"]}),  # an exact id is read alone, as before
]
# The three project requests the team checks a recommendation with, one per resource mix. No clarification answers
# are given, so a request that asks back instead of answering at once fails. Chosen on 2026-11-26 from local runs.
RECOMMEND_CHECKS = [
    ("R01", ["법률상담 챗봇을 만드려고 하는데 모델이랑 데이터 알려줘"], [],  # models and data
     {"recommend": True, "display": "recommendation", "model_path": "project", "dataset_path": "project",
      "models_found": True, "datasets_found": True}),
    ("R02", ["따릉이 대여소 안내 앱을 만들려고 해. 공공데이터만 추천해줘"], [],  # data only
     {"recommend": True, "display": "recommendation", "models_found": False, "datasets_found": True}),
    ("R03", ["사진 속 한국어 글자를 읽어서 번역해주는 앱을 만들려고 하는데 모델 알려줘"], [],  # models only, with a flow
     {"recommend": True, "display": "recommendation", "model_path": "project", "models_found": True,
      "datasets_found": False, "pipeline": True}),
]
SETS = {"representative": ("recommend_branches_eval", SCENARIOS), "s04_s05": ("recommend_branches_s04_s05_eval", S04_S05),
        "ambiguous_names": ("recommend_branches_ambiguous_names_eval", AMBIGUOUS_NAMES),
        "recommend_checks": ("recommend_checks_eval", RECOMMEND_CHECKS)}


class CallCap(RuntimeError):
    pass


class Meter:
    def __init__(self, cap):
        self.cap, self.total, self.item = cap, 0, Counter()
        self.tokens = Counter()

    def tick(self, kind):
        if self.total >= self.cap:
            raise CallCap(f"call cap {self.cap} reached")
        self.total += 1
        self.item[kind] += 1

    def usage(self, usage):
        if usage is not None:
            self.tokens["prompt"] += getattr(usage, "prompt_tokens", 0) or 0
            self.tokens["completion"] += getattr(usage, "completion_tokens", 0) or 0


def instrument(meter, prompts):
    """Meter every chat and embedding call at the OpenAI client, tagged by its system prompt."""
    from openai.resources.chat.completions import Completions
    from openai.resources.embeddings import Embeddings

    real_create, real_parse, real_embed = Completions.create, Completions.parse, Embeddings.create

    def kind_of(kwargs):
        system = next((m["content"] for m in kwargs.get("messages") or [] if m.get("role") == "system"), "")
        return next((name for name, prompt in prompts.items() if system == prompt), "other")

    def create(self, *args, **kwargs):
        meter.tick(kind_of(kwargs))
        out = real_create(self, *args, **kwargs)
        if not kwargs.get("stream"):
            meter.usage(getattr(out, "usage", None))
            return out

        def chunks():
            for chunk in out:
                meter.usage(getattr(chunk, "usage", None))
                yield chunk
        return chunks()

    def parse(self, *args, **kwargs):
        meter.tick(kind_of(kwargs))
        out = real_parse(self, *args, **kwargs)
        meter.usage(getattr(out, "usage", None))
        return out

    def embed(self, *args, **kwargs):
        meter.tick("embedding")
        out = real_embed(self, *args, **kwargs)
        meter.usage(getattr(out, "usage", None))
        return out

    Completions.create, Completions.parse, Embeddings.create = create, parse, embed


def sse(text):
    out = []
    for block in text.strip().split("\n\n"):
        lines = block.splitlines()
        event = next((line[7:] for line in lines if line.startswith("event: ")), None)
        data = next((line[6:] for line in lines if line.startswith("data: ")), None)
        if event and data:
            out.append((event, json.loads(data)))
    return out


def run(api, client, graph, meter, scenario):
    from backend.app.result import build_done

    sid, turns, answers, expect = scenario
    thread, answers = f"eval-{sid}-{int(time.time())}", list(answers)
    record = {"id": sid, "turns": [], "questions": []}
    for text in turns:
        query, before = text, Counter(meter.item)
        while True:
            response = client.post("/ai/recommend", json={"query": query, "thread_id": thread})
            events = sse(response.text) if response.status_code == 200 else [("http", {"status": response.status_code})]
            if any(e == "error" for e, _ in events):
                raise RuntimeError(dict(events)["error"]["message"][:200])
            asked = dict(events).get("clarify")
            if asked and answers:
                record["questions"].append(asked["questions"][0])
                query = answers.pop(0)
                continue
            break
        last = dict(events)
        answer = "".join(d["text"] for e, d in events if e == "token")
        done = build_done(last, uuid4(), answer, 1.0) if "clarify" not in last else None
        values = graph.get_state({"configurable": {"thread_id": thread}}).values
        plan = values.get("plan") or {}
        flow = done.result.pipeline if done and done.result else None
        labels = {n.id: n.label for n in flow.nodes} if flow else {}
        pipeline = [f"{labels[e.source]} -[{e.label or ''}]-> {labels[e.target]}" for e in flow.edges] if flow else []
        record["turns"].append({
            "query": text, "events": sorted(last), "calls": dict(meter.item - before), "answer": answer,
            "pipeline": pipeline,
            "pending": (asked or {}).get("questions"), "display": done.display if done else None,
            "type": done.type if done else "clarify",
            "state": {"recommend": plan.get("recommend"), "mentioned_models": plan.get("mentioned_models"),
                      "mentioned_datasets": plan.get("mentioned_datasets"),
                      "reference_names": plan.get("reference_names"), "new_request": plan.get("new_request"),
                      "needs": [n.get("task") for n in plan.get("needs") or []],
                      "models": [m["model_id"] for g in values.get("models") or [] for m in g.get("models") or []],
                      "model_route": values.get("model_route"), "dataset_route": values.get("dataset_route"),
                      "datasets": [r["dataset"] for k in ("project_training", "service_data")
                                   for r in (values.get("datasets") or {}).get(k) or []]}})
    per_turn = expect if all(isinstance(k, int) for k in expect) else {len(turns) - 1: expect}
    record["checks"] = {f"t{i + 1}.{name}": ok for i, e in per_turn.items()
                        for name, ok in check(e, record["turns"][i]).items()}
    return record


def check(expect, turn):
    last, state = turn, turn["state"]
    out = {}
    if "recommend" in expect:
        out["recommend"] = state["recommend"] is expect["recommend"]
    if "display" in expect:
        out["display"] = last["display"] == expect["display"]
    if "model_path" in expect:
        out["model_path"] = (state["model_route"] or {}).get("path") == expect["model_path"]
    if "dataset_path" in expect:
        out["dataset_path"] = (state["dataset_route"] or {}).get("path") == expect["dataset_path"]
    if "classifier" in expect:
        out["classifier"] = last["calls"].get("classifier", 0) == expect["classifier"]
    if "answer_has" in expect:
        out["answer_has"] = all(s in last["answer"] for s in expect["answer_has"])
    if "answer_lacks" in expect:
        out["answer_lacks"] = not any(s in last["answer"] for s in expect["answer_lacks"])
    if "models_found" in expect:  # True: some model shown; False: none
        out["models_found"] = bool(state.get("models")) is expect["models_found"]
    if "datasets_found" in expect:
        out["datasets_found"] = bool(state["datasets"]) is expect["datasets_found"]
    if expect.get("pipeline"):  # the recommendation carries a service flow
        out["pipeline"] = bool(last.get("pipeline"))
    if "models_lack" in expect:  # no shown model id contains any of these (casefolded)
        out["models_lack"] = not any(s in m.casefold() for m in state.get("models") or [] for s in expect["models_lack"])
    if "datasets_any" in expect:
        out["datasets_any"] = bool(set(expect["datasets_any"]) & set(state["datasets"]))
    if "mentions_dataset" in expect:
        out["mentions_dataset"] = expect["mentions_dataset"] in (state["mentioned_datasets"] or [])
    if expect.get("no_mentioned_datasets"):
        out["no_mentioned_datasets"] = not state["mentioned_datasets"]
    if "datasets_all" in expect:
        out["datasets_all"] = set(expect["datasets_all"]) <= set(state["datasets"])
    if expect.get("no_model_search"):
        out["no_model_search"] = state["model_route"] is None
    if expect.get("no_dataset_search"):
        out["no_dataset_search"] = state["dataset_route"] is None
    if "no_names_from" in expect:
        names = " ".join(state["mentioned_models"] or []).casefold()
        out["no_names_from"] = not any(n in names for n in expect["no_names_from"])
    if "reference" in expect:
        out["reference"] = expect["reference"] in (state["reference_names"] or [])
    out["not_rejected"] = last["type"] != "reject"
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--max-calls", type=int, default=80)
    parser.add_argument("--set", choices=sorted(SETS), default="representative")
    args = parser.parse_args()
    from fastapi.testclient import TestClient
    from langgraph.checkpoint.memory import InMemorySaver

    spec = importlib.util.spec_from_file_location("eval_api", ROOT / "ai/api.py")
    api = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = api
    spec.loader.exec_module(api)
    import data_conditions
    import model_rerank
    from retrieval_lab import classifier, router

    rg = api.rg
    prompts = {"router": router.PROMPT, "classifier": classifier.PROMPT, "planner": rg.DECOMPOSE_PROMPT,
               "writer_recommend": rg.EXPLAIN_PROMPT, "writer_chat": rg.FACT_PROMPT, "rerank": model_rerank.PROMPT,
               "data_conditions": getattr(data_conditions, "PROMPT", None)}
    meter = Meter(args.max_calls)
    instrument(meter, {k: v for k, v in prompts.items() if v})
    graph = rg.build_graph(checkpointer=InMemorySaver())
    api.app.state.graph, api.app.state.pool = graph, None
    client = TestClient(api.app)  # no lifespan: no checkpoint database is opened
    rows, stopped = [], None
    report_name, scenarios = SETS[args.set]
    for scenario in scenarios:
        if stopped:
            rows.append({"id": scenario[0], "error": "미실행: " + stopped})
            continue
        try:
            rows.append(run(api, client, graph, meter, scenario))
        except CallCap as cap:
            stopped = str(cap)
            rows.append({"id": scenario[0], "error": "미실행: " + stopped})
        except Exception as exc:  # recorded, never retried
            rows.append({"id": scenario[0], "error": f"{type(exc).__name__}: {exc}"[:200]})
        print(scenario[0], rows[-1].get("checks") or rows[-1].get("error"), flush=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    stem = REPORTS / f"{report_name}_{date.today().isoformat()}"
    if stem.with_suffix(".json").exists():  # never overwrite an earlier run's report
        stem = stem.with_name(f"{stem.name}_{int(time.time())}")
    summary = {"calls": meter.total, "by_kind": dict(meter.item), "tokens": dict(meter.tokens), "stopped": stopped}
    stem.with_suffix(".json").write_text(json.dumps({**summary, "rows": rows}, ensure_ascii=False, indent=1) + "\n",
                                         encoding="utf-8")
    lines = [f"# recommend 분기 실제 실행 (1회, {args.set})", "",
             f"- OpenAI 호출 {meter.total}회 {dict(meter.item)}, 토큰 {dict(meter.tokens)}, 중단: {stopped or '없음'}", "",
             "| id | 결과 | 실패한 기대 | 되묻기 | 비고 |", "|---|---|---|---|---|"]
    for r in rows:
        checks = r.get("checks") or {}
        failed = [k for k, v in checks.items() if not v]
        status = "미검증" if r.get("error") else "통과" if not failed else "실패"
        lines.append(f"| {r['id']} | {status} | {', '.join(failed)} | {len(r.get('questions') or [])} | {r.get('error') or ''} |")
    stem.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
