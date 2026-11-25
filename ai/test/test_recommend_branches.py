"""plan.recommend and mentioned names through decompose, the model and data branches and the answer.

The real graph runs; the planner, classifier, writer, model catalog and dataset index are test doubles, so these
tests check what each branch does with a plan, never what a real planner decides (test/golden/
recommend_branches_eval.py runs that once, with a call cap).
"""

import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

import pytest
from langgraph.checkpoint.memory import InMemorySaver

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("branches_graph", ROOT / "17_recommend_graph.py")
rg = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = rg
spec.loader.exec_module(rg)

import hypergraph_search  # noqa: E402
from retrieval_lab import classifier, router  # noqa: E402

spec09 = importlib.util.spec_from_file_location("branches_09", ROOT / "09_model_scout_mcp_readonly.py")
m09 = importlib.util.module_from_spec(spec09)
spec09.loader.exec_module(m09)


def plan(recommend=True, needs=None, models=(), datasets=(), references=(), **extra):
    """A planner reply as _llm_plan returns it (ProjectPlan.model_dump())."""
    return {"summary_ko": "요청", "needs": needs if needs is not None else [], "fine_tuning": [],
            "constraints": rg.constraint_defaults(), "dataset_terms": extra.pop("dataset_terms", []),
            "dataset_query": extra.pop("dataset_query", ""), "clarifying_questions": extra.pop("questions", []),
            "unpublished_data": False, "ai_job_stated": extra.pop("ai_job_stated", True), "recommend": recommend,
            "mentioned_models": list(models), "mentioned_datasets": list(datasets),
            "reference_names": list(references), "new_request": extra.pop("new_request", False), **extra}


EMBED = {"task": "embedding", "purpose_ko": "문서를 벡터로", "model_query": "한국어 임베딩"}


def catalog_row(model_id, context=None, params=None):
    """A 09 row (get_model / compare_models shape)."""
    return {"model_id": model_id, "task": {"primary": "sentence-similarity"}, "model_url": f"https://hf.co/{model_id}",
            "filter_metadata": {"license": "mit", "commercial_status": "permitted", "context_length": context,
                                "parameter_count_billion": params}, "found": True}


SEARCH_ROW = {"model_id": "org/searched", "rank_score": 0.5, "task": "sentence-similarity", "license": "mit",
              "commercial_status": "permitted", "commercial_use": "commercial", "context_length": 512,
              "parameters_b": 0.1, "hardware": None, "quant_bits": None, "gated": False, "artifact_formats": None,
              "artifact_runnable_gib": None, "artifact_runnable_label": None, "dtype": None,
              "unresolved_filter_fields": [], "korean_verified": None, "languages": [], "benchmarks": [],
              "evidence": None, "url": None}
SERVICE_ROW = {"dataset": "seoul_open_data/OA-1", "title": "서울시 문화행사 정보", "source": "seoul_open_data", "score": 3.0,
               "reasons": [], "downloads": None, "url": None, "summary_ko": "행사", "licenses": ["공공누리 제1유형"],
               "evidence": []}


@pytest.fixture
def world(monkeypatch):
    calls, seen = Counter(), {"model_rows": [], "rank": [], "writer_prompts": [], "parse_inputs": []}
    state = {"plans": [], "names": {}, "rows": {}, "datasets": {}, "writer": "답이에요.\n", "fail": set()}

    def llm_plan(user):
        calls["planner"] += 1
        seen["parse_inputs"].append(json.loads(user))
        return json.loads(json.dumps(state["plans"].pop(0)))

    def resolve_model_names(names):
        calls["resolve_models"] += 1
        if "resolve" in state["fail"]:
            raise RuntimeError("db down")
        return {n: state["names"].get(n, {"status": "not_found", "match": None, "model_id": None, "candidates": []})
                for n in names}

    def get_model(model_id):
        calls["get_model"] += 1
        return state["rows"].get(model_id, {"found": False, "model_id": model_id})

    def compare_models(ids):
        calls["compare_models"] += 1
        seen["compared"] = list(ids)
        return {"models": [state["rows"][i] for i in ids if i in state["rows"]]}

    def model_rows(query, tags, *args):
        calls["model_search"] += 1
        seen["model_rows"].append({"tags": tags, "dense_weight": args[7], "match_count": args[8]})
        return {"rows": [dict(SEARCH_ROW)], "contract_filters_applied": False}

    def rank(concepts, roles=None, **kw):
        calls["dataset_search"] += 1
        seen["rank"].append({"concepts": set(concepts), "roles": roles, **kw})
        return [dict(SERVICE_ROW)] if roles else []

    def resolve_dataset_names(names):
        calls["resolve_datasets"] += 1
        return {n: state["datasets"].get(n, {"status": "not_found", "match": None, "entity_id": None, "candidates": []})
                for n in names}

    entities = {"dataset:seoul_open_data/OA-15486": {"name": "seoul_open_data/OA-15486", "title": "서울시 문화행사 정보",
                                                   "source": "seoul_open_data", "url": None, "licenses": ["공공누리 제1유형"],
                                                   "downloads": None, "summary_ko": "행사", "kind": "dataset"}}
    by_entity = {"dataset:seoul_open_data/OA-15486": {"dataset_role/service"}}

    def writer(**kwargs):
        calls["writer"] += 1
        seen["writer_prompts"].append(kwargs["messages"][0]["content"])
        if "writer" in state["fail"]:
            raise TimeoutError("slow")
        for piece in (state["writer"],):
            yield SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content=piece), finish_reason=None)],
                                  usage=None)
        yield SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content=None), finish_reason="stop")],
                              usage=None)

    module_09 = SimpleNamespace(contract_filters_enabled=lambda: False, sparse_idf_enabled=lambda: False,
                                resolve_model_names=resolve_model_names, get_model=get_model,
                                compare_models=compare_models)
    monkeypatch.setattr(rg, "_llm_plan", llm_plan)
    monkeypatch.setattr(rg, "_first_plan", lambda request, target: rg._parse_plan(request, target))
    monkeypatch.setattr(rg, "_with_conditions", lambda target, call, *a: (call(), None))
    monkeypatch.setattr(rg, "_load_09", lambda: module_09)
    monkeypatch.setattr(rg, "_model_rows", model_rows)
    monkeypatch.setattr(rg, "rank_datasets", rank)
    monkeypatch.setattr(rg, "resolve_dataset_names", resolve_dataset_names)
    monkeypatch.setattr(rg, "embed_query", lambda text: None)
    monkeypatch.setattr(rg, "concepts_from_terms", lambda terms: set(terms))
    monkeypatch.setattr(rg, "dataset_facts", lambda ids: {i: state.get("facts", {}).get(i, {}) for i in ids})
    monkeypatch.setattr(rg, "catalog_titles_in", lambda text: calls.update(["title_check"]) or [
        t for t in state.get("titles", []) if t in text])
    monkeypatch.setattr(rg, "load_graph", lambda: (entities, {}, by_entity, {}, {}, {}))
    monkeypatch.setattr(rg.model_rerank, "wanted", lambda query_type, provider: query_type == "semantic_capability")
    monkeypatch.setattr(rg.model_rerank, "rerank", lambda q, rows, client, model: calls.update(["rerank"]) or rows)
    monkeypatch.setattr(classifier, "rule_type", lambda text: None)
    monkeypatch.setattr(classifier, "llm_type", lambda text, use_cache=False: calls.update(["classifier"]) or
                        ("semantic_capability", 1.0))
    monkeypatch.setattr(rg, "_openai", lambda: SimpleNamespace(chat=SimpleNamespace(
        completions=SimpleNamespace(create=writer))))
    monkeypatch.setattr(rg.run_log, "log_event", lambda *a, **k: None)
    monkeypatch.setattr(rg, "_answers", {})  # the writer cache is per process; each test starts empty
    monkeypatch.setattr(router, "route", lambda text, use_cache=False: calls.update(["router"]) or router.RoutingResult(
        state["target"], "ok", "llm", 1.0, intent={"scope": "project", "model": "yes", "data": "yes"}))
    # No follow-up LLM: the route a test passes (or the last one) stays, as when the call fails.
    monkeypatch.setattr(router, "follow_up", lambda *args, **kwargs: None)
    state["target"] = "both"
    graph = rg.build_graph(checkpointer=InMemorySaver())
    config = {"configurable": {"thread_id": "t"}}

    def turn(text, target=None):
        before = Counter(calls)
        payload = {"request": text, **({"route": {"target": target, "status": "ok"}} if target else {})}
        graph.invoke(payload, config)
        return SimpleNamespace(state=graph.get_state(config).values, calls=calls - before)

    return SimpleNamespace(state=state, calls=calls, seen=seen, turn=turn)


# ---- 1. The plan: recommend, mentioned names and the post-processing -------------------------------------------------

@pytest.mark.parametrize("raw,said,kept", [
    (["BGE", "e5"], "BGE와 e5 비교", ["BGE", "e5"]),
    (["BAAI/bge-m3"], "BGE 입력 길이", ["BGE"]),  # a planner-expanded id goes back to what the user wrote
    (["intfloat/multilingual-e5-large"], "intfloat/multilingual-e5-large 사양", ["intfloat/multilingual-e5-large"]),
    (["bge", "BGE", " ", ""], "BGE", ["bge"]),  # case duplicates and blanks folded, first spelling kept
    (["Llama-3-8B"], "한국어 요약 모델 추천해줘", []),  # a name the user never wrote is not theirs
    (["서울시 문화행사 정보"], "서울 문화행사 정보 데이터 알려줘", ["서울 문화행사 정보"]),
])
def test_mentioned_names_stay_as_the_user_wrote_them(raw, said, kept):
    assert rg.mention_names(raw, said) == kept


def test_a_direct_question_gets_no_planning_question_sft_or_ai_job_question(monkeypatch):
    proposed = plan(recommend=False, needs=[EMBED], questions=["어떤 문서를 검색하나요?"], ai_job_stated=False,
                    fine_tuning=[EMBED])
    monkeypatch.setattr(rg, "_llm_plan", lambda user: proposed)
    out = rg._parse_plan("한국어 임베딩 모델 추천해줘", "model")
    assert out["recommend"] is False and out["clarifying_questions"] == [] and out["fine_tuning"] == []
    assert out["needs"] == [EMBED]  # the model kind it asks about stays: it is what the unnamed search runs on


def test_a_recommendation_keeps_the_ai_job_question(monkeypatch):
    monkeypatch.setattr(rg, "_llm_plan", lambda user: plan(recommend=True, ai_job_stated=False))
    assert rg._parse_plan("단어장 앱 만들고 싶어", "both")["clarifying_questions"] == [rg.AI_JOB_QUESTION]


def test_plans_saved_before_the_fields_read_as_recommendations():
    old = {k: v for k, v in plan().items() if k not in ("recommend", "mentioned_models", "mentioned_datasets",
                                                          "reference_names", "new_request")}
    assert rg.recommend_of(old) and rg.lookup_names(old, "model") == [] and rg.lookup_names(old, "dataset") == []
    parsed = rg.ProjectPlan.model_validate(old)
    assert parsed.recommend is True and parsed.mentioned_models == [] and parsed.reference_names == []
    assert rg.recommend_of({"recommend": False}) is False  # false is a value, never "missing"


def follow_up(monkeypatch, reply, said, prior):
    monkeypatch.setattr(rg, "_llm_plan", lambda user: reply)
    return rg._parse_plan(said, "both", said=said, previous=rg.constraint_defaults(), prior_plan=prior,
                          earlier=["BGE와 e5 입력 길이 비교해줘"])


PRIOR = plan(recommend=False, models=["BGE", "e5"])


def test_a_refinement_that_names_nothing_keeps_the_names(monkeypatch):
    out = follow_up(monkeypatch, plan(recommend=False), "상업용으로 쓸 수 있는지도 알려줘", PRIOR)
    assert out["mentioned_models"] == ["BGE", "e5"]


def test_a_refinement_that_names_others_replaces_them(monkeypatch):
    out = follow_up(monkeypatch, plan(recommend=False, models=["kanana"]), "kanana로 바꿔서 비교해줘", PRIOR)
    assert out["mentioned_models"] == ["kanana"]


def test_excluding_a_side_clears_its_names(monkeypatch):
    out = follow_up(monkeypatch, plan(recommend=False, models=["BGE"], dataset_query="행사"), "모델은 빼고 공공데이터만", PRIOR)
    assert out["mentioned_models"] == []


def test_a_new_request_keeps_nothing_from_before(monkeypatch):
    out = follow_up(monkeypatch, plan(recommend=True, models=["BGE"], new_request=True), "이번엔 따릉이 앱을 만들고 싶어",
                    PRIOR)
    assert out["mentioned_models"] == [] and out["recommend"] is True and out["new_request"] is True


def test_a_switch_to_a_direct_question_keeps_the_earlier_names(monkeypatch):
    prior = plan(recommend=True, models=["BGE", "e5"])
    out = follow_up(monkeypatch, plan(recommend=False, models=["BGE", "e5"]), "이번엔 이 두 모델 입력 길이만 비교", prior)
    assert out["recommend"] is False and out["mentioned_models"] == ["BGE", "e5"]


@pytest.mark.parametrize("text,planner_refs", [("BGE 같은 더 가벼운 모델 찾아줘", []),  # the cue alone settles it
                                               ("BGE보다 작은 임베딩", ["BGE"])])
def test_a_yardstick_name_is_kept_but_never_looked_up(monkeypatch, text, planner_refs):
    monkeypatch.setattr(rg, "_llm_plan", lambda user: plan(recommend=False, needs=[EMBED], models=["BGE"],
                                                            references=planner_refs))
    out = rg._parse_plan(text, "model")
    assert out["mentioned_models"] == ["BGE"] and out["reference_names"] == ["BGE"]
    assert rg.lookup_names(out, "model") == []


# ---- 3. Model branch ----------------------------------------------------------------------------------------------

def test_a_recommendation_skips_the_type_and_uses_the_project_profile(world):
    world.state["plans"] = [plan(recommend=True, needs=[EMBED], dataset_terms=["행사"], dataset_query="행사")]
    t = world.turn("행사 소개 앱을 만들고 싶어", target="both")
    assert t.calls["classifier"] == 0 and t.calls["rerank"] == 0 and t.calls["resolve_models"] == 0
    assert world.seen["model_rows"] == [{"tags": ("sentence-similarity", "feature-extraction"),
                                         "dense_weight": rg.PROJECT_MODEL_SEARCH["dense_weight"],
                                         "match_count": rg.PROJECT_MODEL_SEARCH["match_count"]}]
    assert t.state["model_route"] == {"path": "project"}


def test_one_named_model_is_read_with_get_model(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED], models=["multilingual-e5-large"])]
    world.state["names"] = {"multilingual-e5-large": {"status": "found", "match": "repo_name",
                                                      "model_id": "intfloat/multilingual-e5-large", "candidates": []}}
    world.state["rows"] = {"intfloat/multilingual-e5-large": catalog_row("intfloat/multilingual-e5-large", 514)}
    t = world.turn("multilingual-e5-large 입력 길이 알려줘", target="model")
    assert (t.calls["get_model"], t.calls["compare_models"], t.calls["model_search"], t.calls["classifier"]) == (1, 0, 0, 0)
    group = t.state["models"][0]
    assert group["kind"] == "lookup" and group["models"][0]["context_length"] == 514


def test_several_named_models_are_compared_and_all_reach_the_writer_in_full(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED], models=["BGE-m3-ko", "e5-large"])]
    world.state["names"] = {
        "BGE-m3-ko": {"status": "found", "match": "repo_name", "model_id": "dragonkue/BGE-m3-ko", "candidates": []},
        "e5-large": {"status": "found", "match": "alias", "model_id": "intfloat/e5-large", "candidates": []}}
    world.state["rows"] = {"dragonkue/BGE-m3-ko": catalog_row("dragonkue/BGE-m3-ko", 8194, 0.57),
                           "intfloat/e5-large": catalog_row("intfloat/e5-large", 512, 0.33)}
    t = world.turn("BGE-m3-ko와 e5-large 입력 길이 비교", target="model")
    assert world.seen["compared"] == ["dragonkue/BGE-m3-ko", "intfloat/e5-large"] and t.calls["model_search"] == 0
    assert [len(g["models"]) for g in t.state["models"]] == [1, 1]  # one group per name, never top-1 and alternatives
    assert world.seen["writer_prompts"][-1] == rg.FACT_PROMPT
    brief = rg._brief({"models": t.state["models"], "datasets": rg.NO_DATASETS}, direct=True)
    assert [m["context_length"] for g in brief["models"] for m in g["models"]] == [8194, 512]
    assert t.state["combination"] == []


def test_no_name_takes_the_six_type_path(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED])]
    t = world.turn("한국어 임베딩 모델 추천해줘", target="model")
    assert t.calls["classifier"] == 1 and t.calls["resolve_models"] == 0
    # The type's own policy: its dense share and, as a rerank type, the deeper slice reranking reads.
    assert world.seen["model_rows"][0] == {"tags": ("sentence-similarity", "feature-extraction"),
                                           "dense_weight": rg.MODEL_DENSE_WEIGHTS["semantic_capability"],
                                           "match_count": rg.model_rerank.RERANK_DEPTH}


def test_a_name_the_catalog_lacks_falls_back_and_says_so(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED], models=["NoSuchModel-7B"])]
    t = world.turn("NoSuchModel-7B 입력 길이", target="model")
    assert t.calls["resolve_models"] == 1 and t.calls["classifier"] == 1 and t.calls["model_search"] == 1
    assert t.state["model_route"]["path"] == "fallback"
    assert t.state["model_route"]["resolved"]["NoSuchModel-7B"]["status"] == "not_found"
    answer = t.state["answer"]
    assert "정확히 일치하는 모델 이름을 확인하지 못했어요: 'NoSuchModel-7B'" in answer
    assert "말씀하신 항목 자체가 아니에요" in answer


def test_a_partial_match_answers_the_found_one_and_names_the_missing_one(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED], models=["e5-large", "NoSuchModel"])]
    world.state["names"] = {"e5-large": {"status": "found", "match": "alias", "model_id": "intfloat/e5-large",
                                         "candidates": []}}
    world.state["rows"] = {"intfloat/e5-large": catalog_row("intfloat/e5-large", 512)}
    t = world.turn("e5-large와 NoSuchModel 비교", target="model")
    assert t.calls["model_search"] == 0 and t.calls["get_model"] == 1  # the found one is read; no unnamed search
    assert "'NoSuchModel'" in t.state["answer"] and "관련 후보" not in t.state["answer"]


def test_an_ambiguous_name_is_never_settled_on_one_model(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED], models=["bge-m3"])]
    world.state["names"] = {"bge-m3": {"status": "ambiguous", "match": "alias", "model_id": None,
                                       "candidates": ["dragonkue/BGE-m3-ko", "upskyy/bge-m3-korean"]}}
    t = world.turn("bge-m3 입력 길이", target="model")
    assert t.calls["get_model"] == 0 and t.state["model_route"]["path"] == "fallback"
    assert "'bge-m3'은(는) 카탈로그의 여러 모델에 해당해 하나로 정하지 않았어요: dragonkue/BGE-m3-ko, upskyy/bge-m3-korean" in t.state["answer"]


def test_a_yardstick_name_searches_for_alternatives(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED], models=["BGE"], references=["BGE"])]
    t = world.turn("BGE 같은 더 가벼운 임베딩 모델", target="model")
    assert t.calls["resolve_models"] == 0 and t.calls["model_search"] == 1 and t.state["model_route"]["path"] == "typed"


def test_a_failed_name_lookup_is_a_search_error_not_a_missing_model(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED], models=["e5-large"])]
    world.state["fail"].add("resolve")
    t = world.turn("e5-large 입력 길이", target="model")
    assert "models" in t.state["search_errors"] and "일부 검색이 실패했어요" in t.state["answer"]
    assert "확인하지 못했어요: 'e5-large'" not in t.state["answer"]


# ---- 4. Data branch -----------------------------------------------------------------------------------------------

def test_a_recommendation_ranks_datasets_with_the_project_profile_and_role_tasks(world):
    world.state["plans"] = [plan(recommend=True, needs=[EMBED], dataset_terms=["행사"], dataset_query="행사")]
    world.turn("행사 소개 앱을 만들고 싶어", target="dataset")
    assert {r["profile"].name for r in world.seen["rank"]} == {"project"}
    training = next(r for r in world.seen["rank"] if not r["roles"])
    assert "embedding" in training["concepts"]  # the roles' tasks still shape the training list


def test_a_named_dataset_is_read_with_its_card(world):
    world.state["plans"] = [plan(recommend=False, datasets=["서울시 문화행사 정보"], dataset_query="문화행사")]
    world.state["datasets"] = {"서울시 문화행사 정보": {"status": "found", "match": "title",
                                                 "entity_id": "dataset:seoul_open_data/OA-15486", "candidates": []}}
    world.state["facts"] = {"seoul_open_data/OA-15486": {"unavailable": "데이터 카드 조회 실패 (Timeout)"}}
    t = world.turn("서울시 문화행사 정보 데이터 알려줘", target="dataset")
    assert t.calls["dataset_search"] == 0 and t.state["dataset_route"]["path"] == "lookup"
    row = t.state["datasets"]["service_data"][0]
    assert row["dataset"] == "seoul_open_data/OA-15486" and row["lookup"] == "서울시 문화행사 정보"
    assert row["facts"] == {"unavailable": "데이터 카드 조회 실패 (Timeout)"}  # an unread card, not missing data
    assert t.calls["resolve_models"] == 0  # the model lookup never searches datasets


def test_an_unnamed_data_question_uses_the_lookup_profile_without_model_roles(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED], dataset_terms=["문화행사", "서울"],
                                 dataset_query="서울 문화행사")]
    world.state["plans"][0]["constraints"]["commercial_only"] = True
    world.turn("서울 문화행사 공공데이터 상업적으로 쓸 수 있는 거", target="dataset")
    assert {r["profile"].name for r in world.seen["rank"]} == {"lookup"}
    assert all("embedding" not in r["concepts"] for r in world.seen["rank"])
    assert all(r["commercial_only"] is True for r in world.seen["rank"])  # a stated commercial condition holds
    assert all(r["keywords"] == ["문화행사", "서울"] for r in world.seen["rank"])  # PR #79's topic/region words


def test_data_kind_still_picks_the_list(world, monkeypatch):
    world.state["plans"] = [plan(recommend=False, dataset_terms=["행사"], dataset_query="행사")]
    world.turn("행사 공공데이터만", target="dataset")
    assert [r["roles"] for r in world.seen["rank"]] in ([["service"]], [None, ["service"]], [["service"], None])


def test_an_unknown_dataset_name_falls_back_and_says_so(world):
    world.state["plans"] = [plan(recommend=False, datasets=["없는데이터셋"], dataset_terms=["행사"], dataset_query="행사")]
    t = world.turn("없는데이터셋 알려줘", target="dataset")
    assert t.state["dataset_route"]["path"] == "fallback" and t.calls["dataset_search"] >= 1
    assert "정확히 일치하는 데이터셋 이름을 확인하지 못했어요: '없는데이터셋'" in t.state["answer"]


# ---- 5. Answers ---------------------------------------------------------------------------------------------------

def test_a_direct_answer_has_no_briefing_combination_or_guide(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED])]
    world.state["writer"] = "답이에요.\n[[조합]]\n조합 문장\n"
    t = world.turn("한국어 임베딩 모델 추천해줘", target="model")
    assert t.state["combination"] == [] and "implementation_guide" not in t.state["assessment"]
    assert world.seen["writer_prompts"][-1] == rg.FACT_PROMPT


def test_a_recommendation_keeps_the_briefing_prompt(world):
    world.state["plans"] = [plan(recommend=True, needs=[EMBED])]
    world.state["writer"] = "브리핑\n[[조합]]\n조합 문장\n"
    t = world.turn("문서 검색 앱 만들고 싶어", target="model")
    assert world.seen["writer_prompts"][-1] == rg.EXPLAIN_PROMPT and t.state["combination"] == ["조합 문장"]


def test_a_direct_answer_whose_writer_fails_lists_what_was_read_never_cards(world):
    world.state["plans"] = [plan(recommend=False, needs=[EMBED], models=["e5-large"])]
    world.state["names"] = {"e5-large": {"status": "found", "match": "alias", "model_id": "intfloat/e5-large",
                                         "candidates": []}}
    world.state["rows"] = {"intfloat/e5-large": catalog_row("intfloat/e5-large", 512)}
    world.state["fail"].add("writer")
    t = world.turn("e5-large 입력 길이", target="model")
    assert "intfloat/e5-large: 태스크 sentence-similarity, 입력 길이 512 tokens" in t.state["answer"]
    assert "카드" not in t.state["answer"]


def test_a_direct_question_with_nothing_found_answers_without_a_writer_call(world):
    world.state["plans"] = [plan(recommend=False, datasets=["없는데이터셋"])]
    t = world.turn("없는데이터셋 알려줘", target="dataset")
    assert t.calls["writer"] == 0 and rg.NOTHING_FOUND_NOTE in t.state["answer"]


def test_a_comparison_after_a_both_recommendation_reads_models_only(world):
    world.state["plans"] = [plan(recommend=True, needs=[EMBED], dataset_terms=["행사"], dataset_query="행사"),
                            plan(recommend=False, models=["e5-large"])]
    world.state["names"] = {"e5-large": {"status": "found", "match": "alias", "model_id": "intfloat/e5-large",
                                         "candidates": []}}
    world.state["rows"] = {"intfloat/e5-large": catalog_row("intfloat/e5-large", 512)}
    world.turn("행사 소개 앱을 만들고 싶어", target="both")
    t = world.turn("이번엔 e5-large 입력 길이만 비교")
    assert t.calls["dataset_search"] == 0 and rg.search_target(t.state) == "model"
    assert t.state["route"]["target"] == "both"  # a later recommendation still searches both


def test_answer_cache_keys_differ_by_answer_kind():
    payload = {"request": "x", "models": [], "datasets": rg.NO_DATASETS}
    assert rg._answer_key(payload, rg.FACT_PROMPT) != rg._answer_key(payload, rg.EXPLAIN_PROMPT)
    assert rg._answer_key(payload) == rg._answer_key(payload, rg.EXPLAIN_PROMPT)


# ---- Name resolution in the catalogs --------------------------------------------------------------------------------

def fam(canonical=None, source="base_model_tag"):
    return {"canonical_model_id": canonical, "canonical_source": source} if canonical else {}


@pytest.mark.parametrize("key,rows,status,model_id", [
    ("intfloat/e5-large", [{"model_id": "intfloat/e5-large", "family": {}}], "found", "intfloat/e5-large"),
    ("e5-large", [{"model_id": "intfloat/e5-large", "family": {}}], "found", "intfloat/e5-large"),
    ("bge-m3", [{"model_id": "BAAI/bge-m3", "family": {}}, {"model_id": "mirror/bge-m3", "family": fam("BAAI/bge-m3")}],
     "found", "BAAI/bge-m3"),  # the copies declare the original
    ("bge-m3", [{"model_id": "a/bge-m3", "family": {}}, {"model_id": "b/bge-m3", "family": {}}], "ambiguous", None),
    ("bge-m3", [{"model_id": "a/BGE-m3-ko", "family": fam("BAAI/bge-m3")},
                {"model_id": "b/bge-m3-korean", "family": fam("BAAI/bge-m3")}], "ambiguous", None),  # derivatives only
    ("kanana", [{"model_id": "kakao/kanana-1.5-2.1b", "family": {}}], "found", "kakao/kanana-1.5-2.1b"),
    ("nothing", [], "not_found", None),
])
def test_model_names_resolve_only_on_catalog_evidence(key, rows, status, model_id):
    out = m09._resolved(key, rows, 5)
    assert (out["status"], out["model_id"]) == (status, model_id)


def test_model_names_reach_sql_as_parameters_only(monkeypatch):
    executed = []

    class Cursor:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def execute(self, statement, params):
            executed.append((statement, params))

        def fetchall(self):
            return []

    class Connection:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def cursor(self, cursor_factory=None):
            return Cursor()

    monkeypatch.setattr(m09, "_read_connection", lambda: Connection())
    name = "x'; drop table t; --"
    out = m09.resolve_model_names([name])
    assert out[name]["status"] == "not_found"
    statement, params = executed[0]
    assert name.casefold() not in statement and params[0] == name.casefold()


def test_dataset_names_resolve_by_id_title_and_unique_title_part(monkeypatch):
    entities = {f"dataset:{n}": {"entity_id": f"dataset:{n}", "kind": "dataset", "name": n, "title": t, "downloads": d}
                for n, t, d in (("seoul_open_data/OA-15486", "서울시 문화행사 정보", None),
                                ("seoul_open_data/OA-12087", "서울시 구로구 문화행사 공공서비스예약 정보", None),
                                ("a/words", None, 10), ("b/words", None, 5))}
    monkeypatch.setattr(hypergraph_search, "load_graph", lambda: (entities,))
    hypergraph_search._dataset_name_index.cache_clear()
    try:
        out = hypergraph_search.resolve_dataset_names(
            ["seoul_open_data/OA-15486", "OA-12087", "서울시 문화행사 정보", "구로구 문화행사", "words", "문화행사", "없음없음"])
    finally:
        hypergraph_search._dataset_name_index.cache_clear()
    assert out["seoul_open_data/OA-15486"]["match"] == "id" and out["OA-12087"]["match"] == "id_part"
    assert out["서울시 문화행사 정보"]["entity_id"] == "dataset:seoul_open_data/OA-15486"
    assert out["구로구 문화행사"]["status"] == "found" and out["구로구 문화행사"]["match"] == "title_part"
    assert out["words"]["status"] == "ambiguous" and out["words"]["candidates"] == ["a/words", "b/words"]
    assert out["문화행사"]["status"] == "ambiguous"  # two titles contain it: none is picked
    assert out["없음없음"]["status"] == "not_found"


def test_the_lookup_profile_drops_popularity_and_the_default_is_unchanged(monkeypatch):
    entities = {f"dataset:{n}": {"entity_id": f"dataset:{n}", "kind": "dataset", "name": n, "title": None,
                                 "source": "huggingface", "downloads": d, "url": "", "licenses": []}
                for n, d in (("a/popular", 100000), ("b/rare", 0))}
    concept = "task/summarization"
    graph = (entities, {concept: {"label": "요약"}}, {e: {concept} for e in entities},
             {concept: set(entities)}, {}, {(e, concept): 1.0 for e in entities})
    monkeypatch.setattr(hypergraph_search, "load_graph", lambda: graph)
    monkeypatch.setattr(hypergraph_search, "evidence_item", lambda *a: None)
    assert hypergraph_search.PROJECT_PROFILE.dense_weight == hypergraph_search.DENSE_WEIGHT == 10.0
    assert hypergraph_search.PROJECT_PROFILE.download_weight == 0.5
    project = {r["dataset"]: r["score"] for r in hypergraph_search.rank_datasets({concept})}
    lookup = {r["dataset"]: r["score"] for r in hypergraph_search.rank_datasets({concept},
                                                                               profile=hypergraph_search.LOOKUP_PROFILE)}
    assert project["a/popular"] > project["b/rare"] and lookup["a/popular"] == lookup["b/rare"]


def test_a_reference_to_shown_models_can_name_them(monkeypatch):
    sent = []
    monkeypatch.setattr(rg, "_llm_plan", lambda user: sent.append(json.loads(user)) or plan(
        recommend=False, models=["org/shown-a", "org/shown-b", "org/never-shown"]))
    prior = plan(recommend=True, needs=[EMBED])
    out = rg._parse_plan("이번엔 이 두 모델 입력 길이만 비교해줘", "both", said="이번엔 이 두 모델 입력 길이만 비교해줘",
                         previous=rg.constraint_defaults(), prior_plan=prior, earlier=["문서 검색 앱"],
                         shown={"models": ["org/shown-a", "org/shown-b"], "datasets": []})
    assert sent[0]["previous_results"] == {"models": ["org/shown-a", "org/shown-b"], "datasets": []}
    assert out["mentioned_models"] == ["org/shown-a", "org/shown-b"]  # an id never shown or written is dropped


def test_shown_ids_follow_the_screen_order():
    state = {"models": [{"models": [{"model_id": "a"}, {"model_id": "b"}]}, {"models": [{"model_id": "a"}]}],
             "datasets": {"project_training": [{"dataset": "d1"}], "service_data": [{"dataset": "d2"}]}}
    assert rg.shown_ids(state) == {"models": ["a", "b"], "datasets": ["d1", "d2"]}


def test_the_fallback_line_needs_something_found_below(world):
    world.state["plans"] = [plan(recommend=False, models=["NoSuchModel-9000"])]  # no model kind to search either
    t = world.turn("NoSuchModel-9000 라이선스", target="model")
    assert "확인하지 못했어요: 'NoSuchModel-9000'" in t.state["answer"]
    assert "관련 후보" not in t.state["answer"] and rg.NOTHING_FOUND_NOTE in t.state["answer"]



# ---- S04 / S05 follow-up: the planner's order, the direct-ask rule and catalog titles ----------------------------------
# These check what the code does around a planner reply; whether a real planner judges recommend or names correctly is
# measured only by the capped GPT run (golden/recommend_branches_eval.py).

def test_the_kind_of_request_and_names_come_first_in_the_planner_schema():
    order = list(rg.ProjectPlan.model_json_schema()["properties"])
    # The team's AI-job judgment comes first, on the user's words alone; then the kind of request and the names.
    assert order[:6] == ["ai_job_stated", "recommend", "mentioned_models", "mentioned_datasets", "reference_names",
                         "new_request"]
    assert order.index("recommend") < order.index("needs")
    assert rg.DECOMPOSE_PROMPT.index("recommend:") < rg.DECOMPOSE_PROMPT.index("needs:")


def test_no_evaluation_sentence_or_answer_id_sits_in_the_planner_prompt():
    for text in ("한국어 문장 임베딩 모델", "서울시 문화행사 정보", "OA-15486", "OA-23041"):
        assert text not in rg.DECOMPOSE_PROMPT


@pytest.mark.parametrize("text", [
    "한국어 문장 임베딩 모델 추천해줘", "요약 잘하는 한국어 모델 알려줘", "괜찮은 한국어 OCR 모델 뭐가 있어?",
    "서울 문화행사 관련 데이터 찾아줘", "데이터는 이미 있어. 모델만 추천해줘",
    "한국어 문장 임베딩 모델 추천해줘\n조건: 언어 한국어, 상업적 이용 가능.",
])
def test_a_kind_only_ask_is_recognized(text):
    assert rg.asks_for_a_kind_only(text)


@pytest.mark.parametrize("text", [
    "회의록을 요약하는 앱을 만들고 싶어. 필요한 모델 추천해줘", "고객 문의에 자동으로 답하는 챗봇 서비스에 쓸 모델",
    "인터뷰를 받아쓰는 앱을 만들고 싶어", "고객 문의 답변을 자동화하려고 해. 모델 추천해줘",
    "한국어 요약 성능을 높이고 싶어",  # asks for no model or data noun: left to the planner
])
def test_a_request_to_build_or_a_vague_one_is_left_to_the_planner(text):
    assert not rg.asks_for_a_kind_only(text)


def test_a_kind_only_ask_the_planner_called_a_recommendation_is_answered_directly(monkeypatch):
    monkeypatch.setattr(rg, "_llm_plan", lambda user: plan(recommend=True, needs=[EMBED], questions=["어디에 쓰나요?"],
                                                            fine_tuning=[EMBED]))
    out = rg._parse_plan("한국어 문장 임베딩 모델 추천해줘", "model")
    assert out["recommend"] is False and out["clarifying_questions"] == [] and out["fine_tuning"] == []


def test_the_direct_ask_rule_never_makes_a_recommendation_or_overrides_a_later_turn(monkeypatch):
    monkeypatch.setattr(rg, "_llm_plan", lambda user: plan(recommend=True, needs=[EMBED]))
    assert rg._parse_plan("문서 검색 앱을 만들고 싶어. 모델 추천해줘", "both")["recommend"] is True
    later = rg._parse_plan("상업용 모델만 추천해줘", "both", said="상업용 모델만 추천해줘",
                           previous=rg.constraint_defaults(), prior_plan=plan(recommend=True), earlier=["문서 검색 앱"])
    assert later["recommend"] is True  # a refinement of a project stays a recommendation
    monkeypatch.setattr(rg, "_llm_plan", lambda user: plan(recommend=False, needs=[EMBED]))
    assert rg._parse_plan("회의록 요약 앱을 만들고 싶어", "both")["recommend"] is False  # only ever narrows


def test_a_whole_catalog_title_in_a_data_question_becomes_its_name(monkeypatch, world):
    world.state["titles"] = ["부산광역시 공영주차장 현황"]
    monkeypatch.setattr(rg, "_llm_plan", lambda user: plan(recommend=False, dataset_terms=["주차장"], dataset_query="주차장"))
    out = rg._parse_plan("부산광역시 공영주차장 현황 데이터셋 보여줘", "dataset")
    assert out["mentioned_datasets"] == ["부산광역시 공영주차장 현황"]
    assert rg.lookup_names(out, "dataset") == ["부산광역시 공영주차장 현황"]


@pytest.mark.parametrize("reply,target,text", [
    (plan(recommend=True, dataset_query="주차장"), "dataset", "부산광역시 공영주차장 현황 앱을 만들고 싶어"),  # a project
    (plan(recommend=False, needs=[EMBED]), "model", "부산광역시 공영주차장 현황 임베딩 모델"),  # a model-only question
    (plan(recommend=False, datasets=["OA-777"]), "dataset", "OA-777 부산광역시 공영주차장 현황"),  # a name already given
])
def test_the_title_check_runs_only_for_an_unnamed_data_question(monkeypatch, world, reply, target, text):
    world.state["titles"] = ["부산광역시 공영주차장 현황"]
    monkeypatch.setattr(rg, "_llm_plan", lambda user: reply)
    before = world.calls["title_check"]
    rg._parse_plan(text, target)
    assert world.calls["title_check"] == before


def test_an_unavailable_title_check_leaves_the_plan_as_planned(monkeypatch):
    monkeypatch.setattr(rg, "catalog_titles_in", lambda text: (_ for _ in ()).throw(RuntimeError("corpus")))
    monkeypatch.setattr(rg, "_llm_plan", lambda user: plan(recommend=False, dataset_query="주차장"))
    assert rg._parse_plan("부산광역시 공영주차장 현황 알려줘", "dataset")["mentioned_datasets"] == []


def test_catalog_titles_are_found_whole_never_from_a_topic(monkeypatch):
    titles = {"a/1": "서울시 문화행사 정보", "a/2": "서울시 문화행사 정보", "a/3": "서울시 동대문구 문화행사 정보",
              "a/4": "서울시 인구", "a/5": "부산광역시 공영주차장 현황"}
    entities = {f"dataset:{n}": {"entity_id": f"dataset:{n}", "kind": "dataset", "name": n, "title": t, "downloads": 0}
                for n, t in titles.items()}
    monkeypatch.setattr(hypergraph_search, "load_graph", lambda: (entities,))
    hypergraph_search._dataset_name_index.cache_clear()
    try:
        find = hypergraph_search.catalog_titles_in
        assert find("서울시 문화행사 정보 데이터셋 알려줘") == ["서울시 문화행사 정보"]
        assert find("서울 문화행사 관련 데이터 찾아줘") == []  # a topic contains no whole title
        assert find("서울시 인구 데이터") == []  # too short to tell from a topic
        assert find("서울시 동대문구 문화행사 정보 알려줘") == ["서울시 동대문구 문화행사 정보"]  # the longest, not its part
    finally:
        hypergraph_search._dataset_name_index.cache_clear()


def test_a_title_several_datasets_share_shows_all_of_them_and_picks_none(monkeypatch, world):
    entities = {f"dataset:p/{i}": {"name": f"p/{i}", "title": "부산광역시 공영주차장 현황", "source": "data_go_kr", "url": None,
                                   "licenses": [], "downloads": None, "summary_ko": "주차장", "kind": "dataset"}
                for i in ("A1", "B2")}
    monkeypatch.setattr(rg, "load_graph", lambda: (entities, {}, {k: {"dataset_role/service"} for k in entities}, {}, {}, {}))
    world.state["plans"] = [plan(recommend=False, datasets=["부산광역시 공영주차장 현황"], dataset_query="주차장")]
    world.state["datasets"] = {"부산광역시 공영주차장 현황": {"status": "ambiguous", "match": "title", "entity_id": None,
                                                      "candidates": ["p/A1", "p/B2"]}}
    t = world.turn("부산광역시 공영주차장 현황 데이터셋 알려줘", target="dataset")
    rows = t.state["datasets"]["service_data"]
    assert [r["dataset"] for r in rows] == ["p/A1", "p/B2"] and all(r["lookup_ambiguous"] for r in rows)
    assert t.state["dataset_route"]["path"] == "lookup" and t.calls["dataset_search"] == 0
    assert t.calls["model_search"] == 0 and t.calls["resolve_models"] == 0
    assert "여러 데이터셋에 해당해 하나로 정하지 않았어요: p/A1, p/B2" in t.state["answer"]


def test_a_title_that_only_contains_the_name_still_falls_back(world):
    world.state["plans"] = [plan(recommend=False, datasets=["공영주차장"], dataset_query="주차장")]
    world.state["datasets"] = {"공영주차장": {"status": "ambiguous", "match": "title_part", "entity_id": None,
                                         "candidates": ["p/A1", "p/B2"]}}
    t = world.turn("공영주차장 데이터 알려줘", target="dataset")
    assert t.state["dataset_route"]["path"] == "fallback" and t.calls["dataset_search"] >= 1


def test_s04_shape_through_the_graph_is_a_chat_answer_on_the_six_type_path(world):
    world.state["plans"] = [plan(recommend=True, needs=[EMBED])]  # the planner's miss the rule corrects
    t = world.turn("한국어 문장 임베딩 모델 추천해줘", target="model")
    assert t.state["plan"]["recommend"] is False and t.state["model_route"]["path"] == "typed"
    assert t.calls["classifier"] == 1 and t.calls["dataset_search"] == 0
    assert world.seen["writer_prompts"][-1] == rg.FACT_PROMPT and t.state["combination"] == []
