"""Step 4: an experimental dataset-side decomposition (service code untouched). Development set.

    python -X utf8 test/public_data/retrieval/decompose_v2.py --dir runs/<new> --labels <labels> --spec <spec> \
        --baseline runs/2026-11-20_decompose_compare --allow-api      # 58 planner calls + 58 embeddings
    python -X utf8 test/public_data/retrieval/decompose_v2.py ... --reuse runs/<old>   # no API call

The experimental planner (PROMPT, DataPlan) gets the same input as the service planner did in the baseline: the
question and the baseline router's target (search_target). One call per question, same model, temperature 0. It
returns dataset_query / dataset_terms plus explicit conditions, each with a verbatim quote, and inferred needs
kept apart from the conditions.

Three evaluations:
  extraction   explicit conditions against the spec (query_spec_v2): missed, added (not asked for), wrong value;
               a quote must also be a substring of the question, but a real quote does not make the reading right
  input        retrieval with the spec's conditions as the filter: what the new search text alone does
  path         retrieval with the conditions the planner extracted: the dataset-search path with extraction
               mistakes included (routing, history and the answer are not part of it)
Path minus input, at the same search text, is what extraction and application did to the results.

Extraction and the filter policy stay separate: an extracted '전국' is scored as extracted but never becomes a
region filter (regional data stays a partial alternative), and unknown statuses stay in the results, as in the
pilot. The baseline's path run uses what the service planner extracts: commercial_only and a region word in
dataset_terms; it has no delivery or realtime output.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fusion_compare as fc  # noqa: E402
import pilot  # noqa: E402
import sweep  # noqa: E402

K_RRF = 20
BASE = "question/spec"
CONDS = ("region", "region_scope", "delivery", "realtime", "commercial", "kogl_type1_only")

PROMPT = """You prepare the dataset search of a recommender for Korean public data (data.go.kr, 서울 열린데이터광장).
Input JSON: search_target (model, dataset or both: what the user wants found) and user_message.
Describe only the data side, whatever the target.

dataset_query: one Korean sentence naming the data the user needs. Do not add requirements the user did not
  state (no reviews, user inquiries, real-time, images, Korean-language text unless they asked for them).
dataset_terms: 1-6 short Korean words naming the data: its subject, the items it must hold, a region the user
  named. Add a language or text-length word only when the data itself must be in that language or length
  (e.g. a Korean corpus for training); never add 한국/한국어 because the user writes Korean. No words about the
  app or service itself (앱, 플랫폼, 추천, 챗봇, 서비스, 알림).
explicit: only conditions the user states in this message. A purpose is not a condition.
  region: a Korean region the data must cover, short form (서울, 부산, 대구, 인천, 광주, 대전, 울산, 세종, 경기,
    강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주), else null.
  region_scope: "전국" when they ask for nationwide coverage, else null.
  delivery: "api" when they require an API, "file" when they require a file, CSV or download, else null.
    Showing data in an app is not a delivery requirement.
  realtime: true only when they ask for real-time or current values.
  commercial: true only when they say the data will be used commercially or must allow commercial use.
  kogl_type1_only: true only when they ask for 공공누리 1유형 data only.
  For each, *_evidence is the exact words of user_message that state it, or "" when it is null or false.
inferred_needs: what you infer from the purpose (e.g. an alert app needs frequent updates). These are never
  conditions and never go into explicit."""


class Explicit(BaseModel):
    region: Optional[str]
    region_evidence: str
    region_scope: Optional[Literal["전국"]]
    region_scope_evidence: str
    delivery: Optional[Literal["api", "file"]]
    delivery_evidence: str
    realtime: bool
    realtime_evidence: str
    commercial: bool
    commercial_evidence: str
    kogl_type1_only: bool
    kogl_type1_only_evidence: str


class DataPlan(BaseModel):
    dataset_query: str
    dataset_terms: list[str]
    explicit: Explicit
    inferred_needs: list[str]


def plan_v2(client, model, question, target):
    response = client.chat.completions.parse(
        model=model, temperature=0, max_tokens=800, response_format=DataPlan,
        messages=[{"role": "system", "content": PROMPT},
                  {"role": "user", "content": json.dumps({"search_target": target, "user_message": question}, ensure_ascii=False)}])
    parsed = response.choices[0].message.parsed
    if parsed is None:
        raise ValueError(f"planner refused: {response.choices[0].message.refusal}")
    return parsed.model_dump()


def canon_region(value):
    """경상남도 -> 경남, 서울시·서울특별시 -> 서울, 제주도 -> 제주: one name per region, read generously."""
    if not value:
        return None
    value = pilot.hs.REGION_CANON.get(value, value)
    if value not in pilot.hs.REGIONS:
        stripped = re.sub(r"(특별자치시|특별자치도|특별시|광역시|시|도)$", "", value)
        value = pilot.hs.REGION_CANON.get(stripped, stripped) if stripped in pilot.hs.REGIONS else value
    return value


def truth(spec):
    """The spec's explicit conditions in the planner's vocabulary (falsy = not asked for)."""
    c = spec["conditions"]
    return {"region": canon_region(c.get("region")), "region_scope": spec.get("region_scope"),
            "delivery": c.get("delivery") if c.get("delivery") in ("api", "file") else None,
            "realtime": bool(c.get("realtime")), "commercial": bool(c.get("commercial")),
            "kogl_type1_only": bool(spec.get("kogl_type1_only"))}


def extracted_v2(plan):
    e = plan["explicit"]
    return {"region": canon_region(e["region"]), "region_scope": e["region_scope"], "delivery": e["delivery"],
            "realtime": e["realtime"], "commercial": e["commercial"], "kogl_type1_only": e["kogl_type1_only"]}


def extracted_base(plan, detail=None):
    """What the service planner hands the dataset search: commercial_only and a region word among dataset_terms.
    detail: the 시군구 the question names; a dataset_term equal to it counts as the region it passed on."""
    regions = [canon_region(t) for t in plan["dataset_terms"] if canon_region(t) in pilot.hs.REGIONS]
    regions = regions or [t for t in plan["dataset_terms"] if detail and t == detail]
    scope = "전국" if "전국" in plan["dataset_terms"] else None
    return {"region": regions[0] if regions else None, "region_scope": scope, "delivery": None, "realtime": False,
            "commercial": bool(plan["commercial_only"]), "kogl_type1_only": False}


def compare(want, got, spec=None):
    """Per condition: ok / missed / added / wrong (both set, different value) / none (neither) / exempt.

    spec may widen or skip the check: region_detail is a finer place the question names (청주 for 충북), and
    extracting it is as right as the 시도; scoring_exempt lists boundary conditions left unscored (c005 '매시간')."""
    spec = spec or {}
    accept = {"region": {spec.get("region_detail")} - {None}}
    out = {}
    for c in CONDS:
        w, g = want[c], got[c]
        if c in spec.get("scoring_exempt", ()):
            out[c] = "exempt"
            continue
        out[c] = ("none" if not w and not g else "ok" if w == g or (w and g in accept.get(c, ())) else
                  "missed" if not g else "added" if not w else "wrong")
    return out


def detail_kept(plan, detail):
    """The 시군구 check, apart from the 시도 one: does the finer place the user named (청주) survive anywhere the
    search sees it? Grouping 청주 under 충북 is fine when 청주 is still kept to tell the results apart."""
    words = [plan["dataset_query"], *plan["dataset_terms"], (plan.get("explicit") or {}).get("region") or ""]
    return any(detail in w for w in words)


def as_filter(got):
    """Extracted conditions -> the pilot filter's conditions. Policy kept: '전국' is not a region filter, and a
    시군구 (청주) is not one either: the checks read 시도 coverage only, so a finer name would wrongly drop 충북 data."""
    region = got["region"] if got["region"] in pilot.hs.REGIONS else None
    return {"region": region, "delivery": got["delivery"] or "any", "realtime": got["realtime"],
            "commercial": got["commercial"]}


def evidence_problems(question, plan):
    norm = lambda s: re.sub(r"\s+", " ", s).strip()  # noqa: E731
    e, bad = plan["explicit"], []
    for c in CONDS:
        set_ = e[c] not in (None, False)
        quote = norm(e[f"{c}_evidence"])
        if set_ and not quote:
            bad.append(f"{c}: 근거 없음")
        elif set_ and quote not in norm(question):
            bad.append(f"{c}: 근거 '{quote}'가 원문에 없음")
    return bad


LIMIT_STATUSES = (pilot.gp.UNKNOWN, pilot.gp.PARTIAL)


def caveat_counts(ranking, used, truth_filter, conditions, alias, k=pilot.K):
    """The limits an answer would state for the top 10: (condition, result) pairs that are unknown or partial.
    correct: also a limit under the spec's conditions; missed: a limit the spec needs but extraction dropped;
    spurious: a limit about a condition the user never asked for (e.g. an added 'realtime')."""
    canon = lambda d: min(alias.get(d, {d}))  # noqa: E731
    out = Counter()
    for d in list(dict.fromkeys(ranking))[:k]:
        shown = {k for k, s in conditions.check(used, d).items() if s in LIMIT_STATUSES}
        needed = {k for k, s in conditions.check(truth_filter, d).items() if s in LIMIT_STATUSES}
        out["correct"] += len(shown & needed)
        out["missed"] += len(needed - shown)
        out["spurious"] += len(shown - needed)
    return dict(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dir", type=Path, required=True)
    parser.add_argument("--labels", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--baseline", type=Path, required=True, help="decompose_compare run with the service plans and vectors")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--allow-api", action="store_true")
    group.add_argument("--reuse", type=Path, help="a decompose_v2 run whose plans_v2.jsonl and vectors are reused")
    args = parser.parse_args()
    out = args.dir
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"{out} already holds a run: pick a new --dir")
    identity = pilot.hs.use_corpus("v2")
    labels = pilot.read_jsonl(args.labels)
    specs = {s["query_id"]: s for s in pilot.read_jsonl(args.spec)}
    cache, added = pilot.cc.use_saved_vectors(allow_embed=bool(args.allow_api))
    base = {p["query_id"]: p for p in pilot.read_jsonl(args.baseline / "plans.jsonl")}
    for row in pilot.read_jsonl(args.baseline / "dq_vectors.jsonl"):
        cache[row["key"]] = row["vector"]
    if args.reuse:
        plans = {p["query_id"]: p for p in pilot.read_jsonl(args.reuse / "plans_v2.jsonl")}
        for row in pilot.read_jsonl(args.reuse / "dq_vectors.jsonl"):
            cache[row["key"]] = row["vector"]
    else:
        from recommendation_llm import create_client, model_name
        client, model = create_client(), model_name()
        plans = {}
        for lb in labels:  # the baseline router's target: same routing input as the service planner had
            qid = lb["query_id"]
            plans[qid] = {"query_id": qid, "target_used": base[qid]["target_used"], "model": model,
                          **plan_v2(client, model, lb["query"], base[qid]["target_used"])}
            print(qid, plans[qid]["dataset_query"][:60], flush=True)

    alias, conditions, searcher = pilot.cc.confirmed_aliases(), pilot.Conditions(), pilot.Searcher()
    merge = fc.rrf(K_RRF)
    scores, rankings, vectors, extraction, caveats = defaultdict(dict), [], [], {}, defaultdict(dict)
    for lb in labels:
        qid, b, v = lb["query_id"], base[lb["query_id"]], plans[lb["query_id"]]
        qvec, bvec, vvec = (pilot.hs.embed_query(t) for t in (lb["query"], b["dataset_query"], v["dataset_query"]))
        vectors.append({"query_id": qid, "key": pilot.cc.vector_key(pilot.hs.query_model(), v["dataset_query"]), "vector": vvec})
        got_b, got_v, want = extracted_base(b, specs[qid].get("region_detail")), extracted_v2(v), truth(specs[qid])
        extraction[qid] = {"want": want, "base": got_b, "v2": got_v, "base_cmp": compare(want, got_b, specs[qid]),
                           "v2_cmp": compare(want, got_v, specs[qid]), "v2_evidence": evidence_problems(lb["query"], v)}
        if detail := specs[qid].get("region_detail"):
            extraction[qid]["detail_kept"] = {"base": detail_kept(b, detail), "v2": detail_kept(v, detail)}
        spec_filter = specs[qid]
        runs = {
            "question/spec": (qvec, lb["query"], spec_filter),
            "base/spec": (bvec, b["dataset_query"] + " " + " ".join(b["dataset_terms"]), spec_filter),
            "base/extracted": (bvec, b["dataset_query"] + " " + " ".join(b["dataset_terms"]), {"query": lb["query"], "conditions": as_filter(got_b)}),
            "v2/spec": (vvec, v["dataset_query"] + " " + " ".join(v["dataset_terms"]), spec_filter),
            "v2/extracted": (vvec, v["dataset_query"] + " " + " ".join(v["dataset_terms"]), {"query": lb["query"], "conditions": as_filter(got_v)}),
        }
        extracted_filters = {}
        for name, (vec, text, filt) in runs.items():
            kept, _, statuses = pilot.apply_filter(merge(searcher.dense(vec), searcher.sparse(text)), filt, conditions)
            kept = kept[: pilot.SETTINGS["top_k"]]
            rankings.append({"path": name, "query_id": qid, "top": kept})
            scores[name][qid] = pilot.score_query(kept, lb, alias, statuses)
            if name.endswith("/extracted"):
                caveats[name][qid] = caveat_counts(kept, filt, spec_filter, conditions, alias)
                extracted_filters[name] = filt
        # The same candidates for both extractions (union of their top 10s): counts that compare extraction alone.
        tops = {r["path"]: r["top"] for r in rankings[-len(runs):]}
        same = list(dict.fromkeys(tops["base/extracted"][: pilot.K] + tops["v2/extracted"][: pilot.K]))
        for name, filt in extracted_filters.items():
            caveats["same:" + name][qid] = caveat_counts(same, filt, spec_filter, conditions, alias, k=len(same))

    blind = pilot.unjudged_items(rankings, labels, specs, alias, conditions)
    out.mkdir(parents=True, exist_ok=True)
    for name, rows in (("plans_v2.jsonl", [plans[q] for q in sorted(plans)]), ("dq_vectors.jsonl", vectors),
                       ("rankings.jsonl", rankings), ("unjudged_blind.jsonl", blind),
                       ("extraction.jsonl", [{"query_id": q, **extraction[q]} for q in sorted(extraction)])):
        (out / name).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    (out / "scores.json").write_text(json.dumps(scores, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    api = {"planner": 0 if args.reuse else len(labels), "embeddings": len(added)}
    (out / "run.json").write_text(json.dumps({
        "identity": identity, "labels": pilot.cc.file_record(args.labels), "spec": pilot.cc.file_record(args.spec),
        "baseline": {"dir": str(args.baseline).replace("\\", "/"), "plans": pilot.cc.file_record(args.baseline / "plans.jsonl")},
        "reused_from": str(args.reuse).replace("\\", "/") if args.reuse else None, "prompt": PROMPT,
        "retriever": {"merge": f"rrf{K_RRF}", "weights": [0.5, 0.5], **{k: pilot.SETTINGS[k] for k in ("channel_depth", "top_k")}},
        "planner_model": next(iter(plans.values()))["model"], "api_calls": api, "development_set": True,
        "code": {**pilot.code_record(), "decompose_v2_lf_sha256": pilot.content_digest(Path(__file__))[0]},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "caveats.json").write_text(json.dumps(caveats, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "report.md").write_text(report(labels, specs, plans, base, scores, extraction, blind, api, args, caveats), encoding="utf-8")
    print(f"{out}: unjudged {len(blind)}, api {api}")


def report(labels, specs, plans, base, scores, extraction, blind, api, args, caveats=None):
    by_q = {lb["query_id"]: lb for lb in labels}
    rec = [q for q in by_q if by_q[q]["expected_behavior"] == "recommend"]
    two = [q for q in rec if "raw2" in scores[BASE][q]]
    mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")  # noqa: E731
    ci = lambda t: f"{t[0]:+.3f} [{t[1]:+.3f}, {t[2]:+.3f}]"  # noqa: E731
    measures = (("2점 MRR@5", two, "raw2", "mrr@5"), ("nDCG@5(등급)", rec, "raw", "ndcg@5"),
                ("2점 R@10", two, "raw2", "recall@10"), ("P@10(1점 이상)", rec, "raw", "precision@10"))
    diff = lambda a, b, qs, k, m: sweep.interval([scores[a][q][k][m] - scores[b][q][k][m] for q in qs])  # noqa: E731
    L = ["# 실험용 데이터 분해 비교 (4단계, 개발용)", "",
         f"라벨 `{args.labels.stem}`, 명세 `{args.spec.stem}`. API 호출: 분해 {api['planner']}회, 임베딩 {api['embeddings']}회. "
         f"검색기 고정: hybrid, RRF k {K_RRF}, 0.5/0.5. 기존 분해 기준선: `{args.baseline.as_posix()}`. 운영 코드는 바꾸지 않았다.", "",
         "- `base`: 서비스 분해(기준선). `v2`: 실험용 분해. 두 분해 모두 기준선 라우터가 고른 target을 같은 입력으로 받았다.",
         "- `/spec`: 명세의 정답 조건으로 필터(검색 문장 자체의 효과). "
         "`/extracted`: 분해가 추출한 조건으로 필터(추출 조건을 사용하는 데이터셋 검색 경로 평가. 라우팅·대화 이력·답변은 포함하지 않음).",
         "- 조건 적용 정책은 파일럿과 같다. '전국'은 추출 여부만 채점하고 지역 필터로 쓰지 않는다. 미확인은 결과에 남긴다.", "",
         "**개발용 결과다.** 운영 반영 전에 별도 질문으로 확인한다.", "",
         "## 검색", "", "| 입력/필터 | " + " | ".join(m for m, *_ in measures) + " | judged@10 | 미판정@10 합 |",
         "|---|" + "---:|" * (len(measures) + 2)]
    for name in scores:
        L.append(f"| {name} | " + " | ".join(f"{mean([scores[name][q][k][m] for q in qs]):.3f}" for _, qs, k, m in measures)
                 + f" | {mean([scores[name][q]['judged@10'] for q in rec]):.3f} | {sum(scores[name][q]['unjudged@10'] for q in rec)} |")
    L += ["", "차이 (평균 [95% 부트스트랩 구간]):", "", "| 비교 | " + " | ".join(m for m, *_ in measures) + " |", "|---|" + "---|" * len(measures)]
    for a, b, what in (("v2/spec", "base/spec", "검색 문장 개선 (정답 조건 필터)"), ("v2/extracted", "base/extracted", "추출 조건 경로: 개선 − 기존"),
                       ("base/extracted", "base/spec", "기존: 추출·적용의 영향"), ("v2/extracted", "v2/spec", "개선: 추출·적용의 영향"),
                       ("v2/extracted", BASE, "개선 경로 − 원문 검색")):
        L.append(f"| {what} (`{a}` − `{b}`) | " + " | ".join(ci(diff(a, b, qs, k, m)) for _, qs, k, m in measures) + " |")
    L += ["", f"## 조건 추출 (명세 `{args.spec.stem}`가 답지, {len(extraction)}문항)", "", "| 조건 | 분해 | 맞음 | 누락 | 잘못 추가 | 값 틀림 |", "|---|---|---:|---:|---:|---:|"]
    for c in CONDS:
        for who in ("base", "v2"):
            n = Counter(extraction[q][f"{who}_cmp"][c] for q in extraction)
            L.append(f"| {c} | {who} | {n['ok']} | {n['missed']} | {n['added']} | {n['wrong']} |")
    for who in ("base", "v2"):
        tot = Counter(s for q in extraction for s in extraction[q][f"{who}_cmp"].values())
        L.append(f"| **합계** | {who} | {tot['ok']} | {tot['missed']} | {tot['added']} | {tot['wrong']} |")
    L += ["", "- 지역(`region`) '맞음'은 상위 지역 분류 기준이다. 명세의 시·도(충북)든, 명세에 적힌 시·군·구(청주)든 내면 맞음으로 셌다."]
    detail = {q: x["detail_kept"] for q, x in extraction.items() if "detail_kept" in x}
    if detail:
        L.append(f"- 세부 지역 보존 (시·군·구를 요구한 {len(detail)}문항, 검색 문장·검색어·추출 지역 중 어디든 남았나): "
                 + ", ".join(f"{who} {sum(d[who] for d in detail.values())}/{len(detail)}" for who in ("base", "v2"))
                 + " (" + "; ".join(f"{q} {specs[q]['region_detail']}: base {'O' if d['base'] else 'X'} v2 {'O' if d['v2'] else 'X'}"
                                   for q, d in sorted(detail.items())) + ")")
    L += ["- 기존 분해는 제공 방식·실시간·1유형을 내지 않으므로 그 조건은 모두 누락으로 셌다.",
          "- 근거 구절이 원문에 있어도 해석이 맞다는 뜻은 아니다. 맞음/누락/추가는 값으로만 채점했다.", "",
          "개선 분해의 오류 (누락·잘못 추가·값 틀림, 근거 문제):", ""]
    for q in sorted(extraction):
        x = extraction[q]
        errs = [f"{c} {s} (명세 {x['want'][c]!r}, 추출 {x['v2'][c]!r})" for c, s in x["v2_cmp"].items() if s in ("missed", "added", "wrong")]
        if errs or x["v2_evidence"]:
            L.append(f"- {q} `{by_q[q]['query'][:50]}`: " + "; ".join(errs + x["v2_evidence"]))
    if caveats:
        L += ["", "## 답변에 전달할 제한 정보 (코드 계산, 추천 문항 상위 10, 조건별 미확인·부분 칸)", "",
              "생성된 답변을 평가한 것이 아니다. 추출 조건으로 조건 검사를 돌리면 답변에 넘길 미확인·부분 칸이 무엇인지를 코드로 센 값이다.", "",
              "| 경로 | 맞음 | 빠짐(명세는 필요) | 잘못 추가(묻지 않은 조건) |", "|---|---:|---:|---:|"]
        for name in ("base/extracted", "v2/extracted", "same:base/extracted", "same:v2/extracted"):
            c = Counter()
            for q in rec:
                c.update(caveats[name].get(q, {}))
            L.append(f"| {name} | {c['correct']} | {c['missed']} | {c['spurious']} |")
        L += ["", "- 위 두 줄은 각 경로가 실제로 낸 상위 10이라 후보가 서로 다르다(총 칸 수가 다름). "
              "`same:` 두 줄은 두 경로 상위 10의 합집합을 같은 후보로 두고 각 추출 조건으로 센 것이라 추출만 비교한다."]
        L += ["", "- 조건 검사(`golden_prep.condition_checks`)가 미확인·부분으로 본 칸을, 답변이 사용자에게 밝혀야 할 제한으로 셌다. "
              "추출 조건과 명세 조건에서 각각 구해 비교했다.", ""]
    L += ["", "## 분해 출력 비교", "", "| 문항 | 기존 dataset_terms | 개선 dataset_terms | 개선 dataset_query | 개선 inferred_needs |", "|---|---|---|---|---|"]
    L += [f"| {q} | {', '.join(base[q]['dataset_terms'])} | {', '.join(plans[q]['dataset_terms'])} | {plans[q]['dataset_query']} | {'; '.join(plans[q]['inferred_needs'])} |"
          for q in sorted(plans)]
    L += ["", f"## 미판정 후보: {len(blind)}쌍 (`unjudged_blind.jsonl`). 판정 전까지 raw 점수에서 적중이 아니다.", ""]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
