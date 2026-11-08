#!/usr/bin/env python3
"""공공데이터 코퍼스 v1과 v2를 비교해 영향 리포트와 재검토 목록을 만든다. 외부 호출 없음.

    python 13_build_hypergraph.py --corpus v2
    python 14_build_dataset_chunks.py --corpus v2
    python test/public_data/compare_corpus_v2.py

읽기만 하는 것: data/hypergraph, data/dataset_index, 기존 라벨과 워크시트.
쓰는 곳: test/public_data/corpus_v2/ (impact_report.md, id_relations.jsonl, golden_review.jsonl)
기존 라벨은 바꾸지 않는다. 검색 비교는 BM25 근사이며 서비스 순위가 아니다.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
AI = HERE.parents[1]
sys.path[:0] = [str(AI), str(HERE)]

import corpus_manifest  # noqa: E402
import dataset_dedup as dd  # noqa: E402

D = AI / "data"
OUT = HERE / "corpus_v2"
PORTALS = {"seoul_open_data", "data_go_kr"}
LABEL_FILES = [HERE / "labels/public_data_golden.jsonl", HERE / "labels/public_data_queries.jsonl",
               HERE / "reports/public_pool_worksheet.csv", HERE / "reports/public_pool.json"]
# (질의, 찾아야 할 제목): 묶여 있던 항목을 이름으로 찾을 수 있는지 본다.
CASES = [
    ("강서구 모범음식점 취소 현황", "서울시 강서구 모범음식점 취소 현황"),
    ("강서구 노동조합 현황", "서울시 강서구 노동조합 현황"),
    ("서울시 집계구 단위 생활인구 내국인", "집계구 단위 서울 생활인구(내국인)"),
    ("서울시 자치구 단위 생활인구 장기체류 외국인", "자치구 단위 서울 생활인구(장기체류 외국인)"),
    ("서울시 실시간 도시데이터", "서울시 실시간 도시데이터"),
    ("서울시 실시간 도시데이터 영문", "서울시 실시간 도시데이터(영문)"),
    ("서울시 한강공원 이용객 현황 2017년", "서울시 한강공원 이용객 현황(2017년)"),
    ("도로구간길이 운행상태 실시간 도시 데이터", "서울시 실시간 도시데이터(영문)"),
]


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_pool_module():
    spec = importlib.util.spec_from_file_location("pool_module", HERE / "build_public_pool.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def documents(chunks):
    docs = defaultdict(list)
    for chunk in chunks:
        docs[chunk["dataset_id"]].append(chunk["text"])
    return {k: "\n".join(v) for k, v in docs.items()}


def rank_of(scores, ids, target):
    order = sorted(range(len(ids)), key=lambda i: -scores[i])
    return next((pos for pos, i in enumerate(order, 1) if ids[i] == target), None)


def main():
    problems = corpus_manifest.check_corpus(D / "hypergraph_v2", D / "dataset_index_v2")
    if problems:
        raise SystemExit("v2 산출물이 manifest와 다릅니다. 13·14 --corpus v2를 다시 실행하세요:\n- " + "\n- ".join(problems))
    graph_manifest = corpus_manifest.load_manifest(D / "hypergraph_v2")
    documents_manifest = corpus_manifest.load_manifest(D / "dataset_index_v2")
    before = {path: sha(path) for path in LABEL_FILES}
    OUT.mkdir(exist_ok=True)
    pool_module = load_pool_module()
    stage1 = {row["dataset_id"]: row for row in read_jsonl(D / "public_datasets_stage1.jsonl")}
    title = lambda d: (stage1[d].get("card_data") or {}).get("pretty_name") or ""  # noqa: E731
    v1_dup = json.loads((D / "hypergraph/duplicates.json").read_text(encoding="utf-8"))
    v2_dup = json.loads((D / "hypergraph_v2/duplicates.json").read_text(encoding="utf-8"))
    series = json.loads((D / "hypergraph_v2/series.json").read_text(encoding="utf-8"))
    v1_all = read_jsonl(D / "hypergraph/entities.jsonl")
    v2_all = read_jsonl(D / "hypergraph_v2/entities.jsonl")
    public = lambda entities: {e["name"]: e for e in entities if e["kind"] == "dataset" and e.get("source") in PORTALS}  # noqa: E731
    v1_ent, v2_ent = public(v1_all), public(v2_all)
    other = lambda entities: {e["entity_id"]: e for e in entities if e["entity_id"].split(":", 1)[-1] not in stage1}  # noqa: E731
    datasets_only = lambda entities: {k: e for k, e in other(entities).items() if e["kind"] == "dataset"}  # noqa: E731
    v1_other, v2_other = datasets_only(v1_all), datasets_only(v2_all)
    model_gap = len({e["entity_id"] for e in v1_all if e["kind"] == "model"} - {e["entity_id"] for e in v2_all if e["kind"] == "model"})
    same_title = Counter()
    by_title = defaultdict(list)
    for row in stage1.values():
        by_title[dd.TITLE_PUNCT_RE.sub("", title(row["dataset_id"])).casefold()].append(row)
    for rows in by_title.values():
        for i, a in enumerate(rows):
            for b in rows[i + 1 :]:
                if a["source"] != b["source"]:
                    same_title["포털 간 교차 등록 후보(비교 가능한 메타데이터 부족)"] += 1
                elif dd.same_data_evidence(a, b):
                    same_title["병합"] += 1
                elif a.get("licenses") and b.get("licenses") and a["licenses"] != b["licenses"]:
                    same_title["라이선스 다름"] += 1
                elif " ".join((a.get("description") or "").split()) != " ".join((b.get("description") or "").split()):
                    same_title["설명 또는 필드 다름"] += 1
                else:
                    same_title["범위 등 그 밖의 근거 부족"] += 1
    v1_chunks = read_jsonl(D / "dataset_index/chunks.jsonl")
    v2_chunks = read_jsonl(D / "dataset_index_v2/chunks.jsonl")
    v1_pub = [c for c in v1_chunks if c["dataset_id"] in stage1]
    v2_pub = [c for c in v2_chunks if c["dataset_id"] in stage1]

    # 항목별 ID 관계. series는 정답 대체 관계가 아니다.
    v1_pub_dup = {k: v for k, v in v1_dup.items() if k in stage1}
    v2_pub_dup = {k: v for k, v in v2_dup.items() if k in stage1}
    series_of = {m: s for s in series for m in s["members"]}
    relation_rows = []
    relation_counter = Counter()
    for dataset_id, info in sorted(v1_pub_dup.items()):
        canonical = info["canonical"]
        same_v2 = v2_pub_dup.get(dataset_id, {}).get("canonical")
        if same_v2:
            relation = ["exact_mirror"]
        elif dataset_id in v2_pub_dup or canonical in v2_pub_dup:
            relation = ["same_title_unverified"]
        else:
            relation = dd._relation_types(stage1[canonical], stage1[dataset_id])
        relation_counter.update(relation)
        relation_rows.append(
            {
                "dataset_id": dataset_id,
                "title": title(dataset_id),
                "v1_canonical": canonical,
                "v1_canonical_title": title(canonical),
                "v2_entity": same_v2 or dataset_id,
                "relation_to_v1_canonical": relation,
                "answer_substitutable": bool(same_v2),
                "series_id": (series_of.get(dataset_id) or {}).get("series_id"),
            }
        )
    (OUT / "id_relations.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in relation_rows), encoding="utf-8"
    )

    # 기존 라벨 재검토 대상. 라벨은 바꾸지 않는다.
    with open(HERE / "reports/public_pool_worksheet.csv", encoding="utf-8-sig", newline="") as f:
        worksheet = list(csv.DictReader(f))
    v1_copies = defaultdict(list)
    for dataset_id, info in v1_pub_dup.items():
        v1_copies[info["canonical"]].append(dataset_id)
    review_rows, reasons, priorities = [], Counter(), Counter()
    for row in worksheet:
        dataset_id, why = row["dataset_id"], []
        separated = [c for c in v1_copies.get(dataset_id, []) if c not in v2_pub_dup]
        if separated:
            why.append("v1_copies_now_separate")
        entity = v2_ent.get(dataset_id)
        if entity is None:
            why.append("merged_in_v2")
        else:
            coverage = entity.get("coverage_regions") or []
            card = [x for x in row["regions"].split(",") if x]
            if entity.get("coverage_status") == "unknown" and card == ["전국"]:
                why.append("card_national_but_coverage_unknown")
            elif entity.get("coverage_status") == "inferred_from_publisher" and card == ["전국"]:
                why.append("card_national_but_publisher_is_local_government")
            elif coverage and card != ["전국"] and set(card) != set(coverage):
                why.append("card_region_differs_from_v2_coverage")
        if not why:
            continue
        reasons.update(why)
        scored = row["score"] in ("1", "2")
        strong = "v1_copies_now_separate" in why or "card_national_but_publisher_is_local_government" in why
        priority = "high" if strong and scored else "medium" if strong or "merged_in_v2" in why else "low"
        priorities[priority] += 1
        review_rows.append(
            {
                "query_id": row["query_id"],
                "dataset_id": dataset_id,
                "title": row["title"],
                "score": row["score"],
                "review_priority": priority,
                "review_reasons": why,
                "coverage_regions": (entity or {}).get("coverage_regions"),
                "coverage_status": (entity or {}).get("coverage_status"),
                "publisher_region": (entity or {}).get("publisher_region"),
                "v1_copies_now_separate": separated[:30],
                "v1_copies_now_separate_count": len(separated),
            }
        )
    (OUT / "golden_review.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in review_rows), encoding="utf-8"
    )

    # 검색 문서 보존
    v1_docs, v2_docs = documents(v1_pub), documents(v2_pub)
    field_re = re.compile(r"^- (.+?) \(", re.M)
    field_total = v1_field_in = v2_field_in = rows_fields = 0
    for dataset_id, row in stage1.items():
        if row["source"] != "seoul_open_data" or dataset_id not in v2_docs:
            continue
        text = (AI / row["readme_path"]).read_text(encoding="utf-8")
        names = [" ".join(n.split()) for n in field_re.findall(text.split("## 제공 필드", 1)[-1]) if n.strip()]
        rows_fields += 1
        field_total += len(names)
        v2_field_in += sum(n in v2_docs[dataset_id] for n in names)
        v1_id = v1_pub_dup.get(dataset_id, {}).get("canonical", dataset_id)
        v1_field_in += sum(n in v1_docs.get(v1_id, "") for n in names)
    portal_rows = [r for d, r in stage1.items() if r["source"] == "data_go_kr" and d in v2_docs]
    has = lambda docs, row, value: bool(value) and value in docs.get(row["dataset_id"], "")  # noqa: E731
    portal = Counter()
    for row in portal_rows:
        for name, value in (("제공기관", row.get("org")), ("분류", row.get("category"))):
            if value:
                portal[name, "total"] += 1
                portal[name, "v1"] += has(v1_docs, row, f"{value}")
                portal[name, "v2"] += has(v2_docs, row, f"{name}: {value}")
        words = row.get("tags") or []
        portal["키워드", "total"] += len(words)
        portal["키워드", "v1"] += sum(w in v1_docs.get(row["dataset_id"], "") for w in words)
        portal["키워드", "v2"] += sum(w in v2_docs[row["dataset_id"]] for w in words)
        variants = row.get("regional_variants") or []
        portal["지역별 원본", "total"] += len(variants)
        portal["지역별 원본", "v1"] += sum(v in v1_docs.get(row["dataset_id"], "") for v in variants)
        portal["지역별 원본", "v2"] += sum(v in v2_docs[row["dataset_id"]] for v in variants)
    truncated_variants = sum((r.get("regional_variant_count") or 0) > len(r.get("regional_variants") or []) for r in portal_rows)
    copy_titles_v1 = sum(title(d) in v1_docs.get(i["canonical"], "") for d, i in v1_pub_dup.items())
    v2_title_hits = sum(title(d) in v2_docs.get(v2_pub_dup.get(d, {}).get("canonical", d), "") for d in v1_pub_dup)
    district_in_v1 = Counter()
    for name in ("강서구", "도봉구", "동대문구", "금천구"):
        district_in_v1[name] = (
            sum(name in title(d) for d in stage1),
            sum(name in (e.get("title") or "") for e in v1_ent.values()),
            sum(name in (e.get("title") or "") for e in v2_ent.values()),
        )

    # 비공공 데이터는 그대로여야 한다.
    other_same = v1_other.keys() == v2_other.keys() and all(
        v1_other[k].get("duplicates") == v2_other[k].get("duplicates") for k in v1_other
    )
    v1_nonpublic = {c["chunk_id"]: c["text_hash"] for c in v1_chunks if c["dataset_id"] not in stage1}
    v2_nonpublic = {c["chunk_id"]: c["text_hash"] for c in v2_chunks if c["dataset_id"] not in stage1}
    nonpublic_changed = sum(v1_nonpublic.get(k) != h for k, h in v2_nonpublic.items()) + len(v1_nonpublic.keys() - v2_nonpublic.keys())
    v1_hashes = {c["text_hash"] for c in v1_chunks}
    new_text = {c["text_hash"]: c["chars"] for c in v2_chunks if c["text_hash"] not in v1_hashes}

    # BM25 근사: 이름으로 찾을 수 있는가, 상위 결과가 같은 묶음으로 채워지는가
    build = lambda docs: (list(docs), pool_module.BM25([pool_module.tokens(t) for t in docs.values()]))  # noqa: E731
    v1_ids, v1_bm25 = build(v1_docs)
    v2_ids, v2_bm25 = build(v2_docs)
    title_to_id = defaultdict(list)
    for dataset_id in stage1:
        title_to_id[title(dataset_id)].append(dataset_id)
    case_rows = []
    for query, wanted in CASES:
        q = pool_module.tokens(query)
        target = next((i for i in title_to_id.get(wanted, []) if i.startswith("seoul_open_data")), None) or (title_to_id.get(wanted) or [None])[0]
        v1_target = v1_pub_dup.get(target, {}).get("canonical", target)
        case_rows.append(
            (query, wanted, "없음(대표 " + title(v1_target)[:24] + ")" if v1_target != target else rank_of(v1_bm25.scores(q), v1_ids, target),
             rank_of(v2_bm25.scores(q), v2_ids, target))
        )
    queries = read_jsonl(HERE / "labels/public_data_queries.jsonl")
    judged_by_query = defaultdict(set)
    for row in worksheet:
        judged_by_query[row["query_id"]].add(row["dataset_id"])
    crowd = Counter()
    per_series = lambda top: len({(series_of.get(d) or {}).get("series_id", d) for d in top})  # noqa: E731
    for q in queries:
        tokens = pool_module.tokens(q["query"])
        for name, ids, bm25 in (("v1", v1_ids, v1_bm25), ("v2", v2_ids, v2_bm25)):
            scores = bm25.scores(tokens)
            top = [ids[i] for i in sorted(range(len(ids)), key=lambda i: -scores[i])[:10]]
            crowd[name, "judged"] += sum(d in judged_by_query[q["query_id"]] for d in top)
            crowd[name, "series"] += per_series(top)
            crowd[name, "top"] += len(top)

    after = {path: sha(path) for path in LABEL_FILES}
    labels_same = before == after
    member_relations = Counter(t for s in series for r in s["relations"] for t in r["relation_to_anchor"])
    status = Counter(e.get("coverage_status") for e in v2_ent.values())
    both = Counter()
    for e in v2_ent.values():
        if e.get("publisher_region") and e.get("coverage_regions") and e["publisher_region"] not in e["coverage_regions"]:
            both["소재지와 범위가 다름"] += 1
        if e.get("publisher_region") and e.get("coverage_status") == "unknown":
            both["소재지만 있고 범위 미확인"] += 1
    merged = sorted(
        ((title(d), d, i["canonical"], i["reason"]) for d, i in v2_pub_dup.items()), key=lambda x: x[0]
    )
    cross_substitute = sum(d in v2_pub_dup for s in series for d in s["members"])

    lines = [
        "# 공공데이터 코퍼스 v2 영향 리포트",
        "",
        "로컬 재가공 결과다. 유료 임베딩, 외부 재수집, 운영 DB 반영은 하지 않았다. 검색 비교는 BM25 근사이며 서비스 순위가 아니다.",
        "",
        f"- corpus_id: `{graph_manifest['stage_id']}`",
        f"- documents_id: `{documents_manifest['stage_id']}`",
        f"- 코드: `{(graph_manifest['git'] or {}).get('commit')}`, 미커밋 변경 {'있음' if (graph_manifest['git'] or {}).get('dirty') else '없음'}",
        "",
        "## 항목 수",
        "",
        "| 구분 | v1 | v2 |",
        "|---|---:|---:|",
        f"| 공공데이터 항목 | {len(v1_ent):,} | {len(v2_ent):,} |",
        f"| 서울 항목 | {sum(e['source'] == 'seoul_open_data' for e in v1_ent.values()):,} | {sum(e['source'] == 'seoul_open_data' for e in v2_ent.values()):,} |",
        f"| 포털 항목 | {sum(e['source'] == 'data_go_kr' for e in v1_ent.values()):,} | {sum(e['source'] == 'data_go_kr' for e in v2_ent.values()):,} |",
        f"| 병합(정답 대체 가능) | {len(v1_pub_dup):,} | {len(v2_pub_dup):,} |",
        f"| 묶음(series, 정답 대체 불가) | 0 | {len(series):,} |",
        f"| 공공데이터 청크 | {len(v1_pub):,} | {len(v2_pub):,} |",
        f"| 공공데이터 문서 글자 수 | {sum(c['chars'] for c in v1_pub):,} | {sum(c['chars'] for c in v2_pub):,} |",
        "",
        "## v1 병합 쌍의 변화",
        "",
        "| v1 대표와의 관계 | 건수 |",
        "|---|---:|",
        *[f"| `{k}` | {v:,} |" for k, v in relation_counter.most_common()],
        "",
        "한 쌍에 관계가 여러 개일 수 있다. `subset_candidate`는 포함 관계가 검증되지 않은 후보다.",
        "",
        "## v2 묶음 구성원의 기준 항목 대비 관계",
        "",
        "| 관계 | 건수 |",
        "|---|---:|",
        *[f"| `{k}` | {v:,} |" for k, v in member_relations.most_common()],
        "",
        "## 제목이 완전히 같은 쌍의 판단",
        "",
        "제목만 같은 것은 근거로 보지 않는다. 포털 간 쌍은 실제 내용을 비교한 뒤 별도로 판단한다.",
        "",
        "| 판단 | 쌍 수 |",
        "|---|---:|",
        *[f"| {k} | {v} |" for k, v in same_title.most_common()],
        "",
        "## v2 병합 전체 (사람 확인용)",
        "",
        *(["| 제목 | 사본 | 대표 | 근거 |", "|---|---|---|---|"] + [f"| {t} | `{d}` | `{c}` | {r} |" for t, d, c, r in merged] if merged else ["병합 없음."]),
        "",
        "## 제공기관 소재지와 데이터 범위",
        "",
        "| 범위 판단 근거 | 항목 수 |",
        "|---|---:|",
        *[f"| `{k}` | {v:,} |" for k, v in status.most_common()],
        "",
        f"소재지와 범위가 다른 항목 {both['소재지와 범위가 다름']:,}개, 소재지는 있지만 범위가 미확인인 항목 {both['소재지만 있고 범위 미확인']:,}개.",
        "",
        "## 검색 문서 보존",
        "",
        "| 항목 | 전체 | v1 문서 | v2 문서 |",
        "|---|---:|---:|---:|",
        f"| v1에서 병합된 항목의 제목 | {len(v1_pub_dup):,} | {copy_titles_v1:,} | {v2_title_hits:,} |",
        f"| 서울 필드 이름 | {field_total:,} | {v1_field_in:,} | {v2_field_in:,} |",
        *[f"| 포털 {name} | {portal[name, 'total']:,} | {portal[name, 'v1']:,} | {portal[name, 'v2']:,} |" for name in ("제공기관", "분류", "키워드", "지역별 원본")],
        "",
        f"서울 필드 비교의 v1 값은 그 항목의 v1 대표 문서 기준이다. 포털 지역별 원본 이름은 수집 단계에서 최대 30건까지만 저장돼 {truncated_variants:,}개 항목은 이름이 일부만 있고 전체 건수는 문서에 적는다.",
        "",
        "| 자치구 | 수집 제목 | v1 항목 제목 | v2 항목 제목 |",
        "|---|---:|---:|---:|",
        *[f"| {k} | {v[0]} | {v[1]} | {v[2]} |" for k, v in district_in_v1.items()],
        "",
        "## 이름으로 찾기 (BM25 근사)",
        "",
        "| 질의 | 찾을 항목 | v1 순위 | v2 순위 |",
        "|---|---|---|---:|",
        *[f"| {q} | {w} | {a} | {b} |" for q, w, a, b in case_rows],
        "",
        "## 부작용: 상위 결과 (BM25 근사, 질의 58개)",
        "",
        "| 지표 | v1 | v2 |",
        "|---|---:|---:|",
        f"| top 10에 든 서로 다른 묶음 수(평균) | {crowd['v1', 'series'] / len(queries):.1f} | {crowd['v2', 'series'] / len(queries):.1f} |",
        f"| top 10 중 기존 판정 비율 | {crowd['v1', 'judged'] / crowd['v1', 'top']:.1%} | {crowd['v2', 'judged'] / crowd['v2', 'top']:.1%} |",
        "",
        "v2는 항목이 늘어 같은 묶음이 상위를 채울 수 있다. 결과 묶기는 별도 변경으로 다룬다.",
        "",
        "## 안전 확인",
        "",
        "| 확인 | 결과 |",
        "|---|---|",
        f"| HF·Kaggle 데이터셋과 사본 관계 동일 | {'예' if other_same else '아니오'} |",
        f"| v1에만 있는 모델 수(입력 차이) | {model_gap} |",
        f"| 비공공 청크 텍스트 변경 수 | {nonpublic_changed} |",
        f"| 묶음 구성원 중 병합된 항목 수 | {cross_substitute} |",
        f"| 기존 라벨·워크시트·풀 파일 해시 불변 | {'예' if labels_same else '아니오'} |",
        "",
        "## 임베딩이 필요한 규모 (실행하지 않음)",
        "",
        f"v1에 없는 텍스트 {len(new_text):,}개, {sum(new_text.values()):,}자.",
        "",
        "## 기존 라벨 재검토 대상 (자동 변경 없음)",
        "",
        f"재검토 행 {len(review_rows)}개 / 워크시트 {len(worksheet)}행. 목록은 `golden_review.jsonl`, ID 관계는 `id_relations.jsonl`에 있다.",
        "",
        "| 우선순위 | 뜻 | 행 수 |",
        "|---|---|---:|",
        f"| high | 1·2점인데 묶였던 항목이 분리되었거나 제공기관이 지자체 | {priorities['high']} |",
        f"| medium | 0점·보류 행의 같은 사유 | {priorities['medium']} |",
        f"| low | 카드는 전국이지만 범위 미확인(대부분 전국 기관 데이터, 참고용) | {priorities['low']} |",
        "",
        "| 사유 | 행 수 |",
        "|---|---:|",
        *[f"| `{k}` | {v} |" for k, v in reasons.most_common()],
        "",
        f"v1에만 있는 모델 {model_gap}개는 이번 변경과 무관하다. 커밋된 v1은 Supabase 기준이고 이번 v2는 로컬 Stage 4 파일로 만들었다.",
        "",
        "## 후속 설계 (이번 변경에 없음)",
        "",
        "- **결과 묶기:** 요청한 지역·기간·언어에 맞는 항목을 먼저 고른 뒤, 나머지만 같은 묶음으로 접는다. 조건에 맞는 항목은 접히지 않는다.",
        "- **요청 조건 반영:** planner가 뽑은 지역·자치구·기간·언어를 `coverage_regions`, `coverage_district`, `period`, `language_edition`과 비교한다. 조건 없는 질의에서는 묶음 기준 항목을 대표로 보여 준다.",
        "- **미확인 표시:** `coverage_status`가 추정이나 미확인이면 화면에 그대로 알린다.",
        "- **부분집합 검증:** 필요할 때 별도 작업으로 한다. 행 수만으로 확정하지 않고 표본 행의 구 값과 키를 함께 비교한다.",
        "- **전환:** 13·14의 기본값, `15`·`16`·`20`·`hypergraph_search`·배포 경로, `dataset-refresh.yml`을 함께 v2로 옮긴다.",
    ]
    (OUT / "impact_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:40]))
    print("labels unchanged:", labels_same, "review rows", len(review_rows), "other_same", other_same, "nonpublic_changed", nonpublic_changed)
    assert labels_same, "label files changed during the report"
    assert cross_substitute == 0


if __name__ == "__main__":
    main()
