"""Stage H2: render the hypergraph as an Obsidian vault (the LLM wiki), a document for people to read.

    python 15_build_wiki.py                 # v2 (the served corpus) -> wiki_v2/
    python 15_build_wiki.py --corpus v1     # v1 -> wiki/ (as before; the Pages workflow builds this)
    python 15_build_wiki.py --check [--corpus v1|v2]

The vault is a generated view of the hypergraph; edit the taxonomy or pipeline, never the pages.
No service or agent reads it. Layout:
  index.md                    facet overview (v2: the data version it was built from)
  facets/<facet>.md           one page per facet, listing its concepts
  concepts/<label>.md         one hub per concept (= hyperedge): members + co-occurring hubs
  models/<org__name>.md       entity pages, frontmatter properties hold [[links]]
  datasets/<org__name>.md     file names and links use the stable dataset id; pages show the title
Each link line names the metadata field it came from, so every edge is traceable.

v2 portal datasets (data.go.kr, 서울 열린데이터광장) also show what the frozen build recorded, read
from that build's own records only (the card text in dataset_index_v2/chunks.jsonl, the enriched rows,
series.json, the Seoul README field lists); each input's hash is checked against the pin
(test/public_data/corpus_v2/data_version.json) and written to wiki_v2/.build.json. Nothing is inferred:
a fact the build did not record is absent, and an unconfirmed one is shown as unconfirmed.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path

from taxonomy import load_taxonomy

AI_DIR = Path(__file__).resolve().parent
CORPORA = {
    "v1": (AI_DIR / "data" / "hypergraph", AI_DIR / "wiki"),
    "v2": (AI_DIR / "data" / "hypergraph_v2", AI_DIR / "wiki_v2"),
}
HYPERGRAPH_DIR, WIKI_DIR = CORPORA["v1"]  # main() switches both to the chosen corpus
PIN = AI_DIR / "test" / "public_data" / "corpus_v2" / "data_version.json"
V2_INPUTS = {  # path in the pin -> what the wiki reads from it
    "data/hypergraph_v2/entities.jsonl": "entities",
    "data/hypergraph_v2/concepts.jsonl": "concepts",
    "data/hypergraph_v2/links.jsonl": "links",
    "data/hypergraph_v2/relations.jsonl": "relations",
    "data/hypergraph_v2/series.json": "series",
    "data/dataset_index_v2/chunks.jsonl": "card text",
    "data/public_enriched/public_datasets.jsonl": "API check, license text, Seoul README path",
    "data/readmes/public": "Seoul '## 제공 필드' lists",
}
PORTALS = {"data_go_kr", "seoul_open_data"}
# ponytail: hubs list the top members by downloads; Obsidian backlinks still show all of them.
HUB_MEMBER_LIMIT = 100
COOCCURRING_LIMIT = 12
GRAPH_NEIGHBOR_LIMIT = 10
UNSAFE_RE = re.compile(r'[\\/:*?"<>|#^\[\]]')
FACET_ORDER = list(load_taxonomy()["facets"])
SOURCE_LABELS = {
    "huggingface": "Hugging Face",
    "kaggle": "Kaggle",
    "seoul_open_data": "서울 열린데이터광장",
    "data_go_kr": "공공데이터포털",
}
# What the detail-page look-up found (README "API 제공 정보를 읽는 법"); an address is never a tested call.
API_CHECK = {
    "confirmed": "OpenAPI 주소 확인 (표준데이터 상세 페이지)",
    "confirmed_catalog": "OpenAPI 제공 (카탈로그 제공형태 REST·SOAP·LINK)",
    "confirmed_auto": "파일 자동변환 OpenAPI 주소 확인. 내용은 올린 파일과 같아 실시간 근거가 아님",
}
SERIES_RELATION = {
    "region_variant": "지역판",
    "edition_variant": "다른 판(연도 등)",
    "language_variant": "다른 언어판",
    "spatial_unit_variant": "다른 공간 단위",
    "subset_candidate": "부분집합 후보(미확인)",
    "cross_listing_candidate": "교차 등록 후보(미확인)",
    "same_title_unverified": "같은 제목(관계 미확인)",
}
# Card lines shown under "공공데이터 사실", in this order (keys of hypergraph_search.card_facts).
FACT_ROWS = (
    ("publisher", "제공기관"),
    ("coverage", "데이터 지역 범위"),
    ("period", "데이터 기간"),
    ("spatial_unit", "공간 단위"),
    ("language_edition", "언어판"),
    ("formats", "데이터 형식"),
    ("commercial_use", "상업 이용"),
)
V2 = None  # main() fills it for --corpus v2: cards, rows, series, data_version


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def safe_name(value):
    return UNSAFE_RE.sub("_", value).strip()


def entity_page(entity):
    folder = "models" if entity["kind"] == "model" else "datasets"
    return f"{folder}/{safe_name(entity['name'].replace('/', '__'))}"


def display(entity):
    """Link text: a v2 portal dataset's title (its page stays named by id, so equal titles never collide)."""
    if V2 and entity.get("source") in PORTALS and entity.get("title"):
        return re.sub(r"[\[\]|]", " ", entity["title"]).strip()
    return entity["name"]


def concept_pages(concepts):
    """Hub page name = label, or 'label (facet)' when two facets share a label (텍스트 in/out)."""
    counts = Counter(c["label"] for c in concepts.values())
    return {
        cid: "concepts/" + safe_name(c["label"] if counts[c["label"]] == 1 else f"{c['label']} ({c['facet_label']})")
        for cid, c in concepts.items()
    }


def link(page, text=None):
    name = page.rsplit("/", 1)[-1]
    return f"[[{name}|{text}]]" if text and text != name else f"[[{name}]]"


def frontmatter(props):
    lines = ["---"]
    for key, value in props.items():
        if value is None or value == []:
            continue
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {json.dumps(v, ensure_ascii=False)}" for v in value)
        else:
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    return "\n".join(lines + ["---", ""])


def compatible_lengths(concepts, length_key):
    """Ordinal rule: a model handles every input_length bin up to its own."""
    keys = list(load_taxonomy()["facets"]["input_length"]["values"])
    return [f"input_length/{k}" for k in keys[: keys.index(length_key) + 1]] if length_key in keys else []


def member_order(entity):
    """v2: by downloads where a source has them, then by title and id (portals have none)."""
    downloads = entity.get("downloads")
    return (downloads is None, -(downloads or 0), display(entity), entity["name"])


def wiki_graph(title, anchor, neighbors):
    return {"title": title, "anchor": anchor, "neighbors": neighbors[:GRAPH_NEIGHBOR_LIMIT]} if neighbors else None


def shared_concept_order(pair_counts, members, concept_id, other_id):
    shared = pair_counts[concept_id][other_id]
    union = len(members[concept_id]) + len(members[other_id]) - shared
    return (-shared / union, -shared, other_id)


# ---------------------------------------------------------------- v2 portal facts


def api_status(row):
    """The API line, keeping 'address found', 'not found' and 'never called' apart."""
    check = (row.get("official") or {}).get("api_check")
    has_api = "api" in (row.get("formats") or [])
    if check in API_CHECK:
        return API_CHECK[check]
    if check in ("not_found", "page_failed"):
        return ("형식에 API 표기 (상세 페이지에서 주소는 찾지 못함)" if has_api else
                "미확인: 상세 페이지에서 이 데이터의 API 주소를 찾지 못함 (API가 없다는 뜻은 아님)")
    if has_api:
        service = f" (서비스명 `{row['api_service']}`)" if row.get("api_service") else ""
        return f"형식에 API 표기{service}. 상세 페이지 주소 확인 기록 없음"
    return "API 표기 없음 (파일 형식만 표기)"


def seoul_fields(row):
    """The '## 제공 필드' lines of a Seoul README, as written."""
    path = AI_DIR / row["readme_path"] if row.get("readme_path") else None
    if row.get("source") != "seoul_open_data" or not path or not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    if "## 제공 필드" not in text:
        return []
    return [line[2:] for line in text.split("## 제공 필드", 1)[1].splitlines() if line.startswith("- ")]


def portal_sections(entity, entities):
    """Facts, limits, description, Seoul fields and series of one v2 portal dataset (markdown lines)."""
    import hypergraph_search as hs

    name = entity["name"]
    card = hs.card_facts(V2["cards"].get(name, ""))
    row = V2["rows"].get(name, {})
    official = row.get("official") or {}
    out = ["## 공공데이터 사실", "",
           f"> v2 고정본 `{V2['data_version']}`에 기록된 값만 옮겼습니다. 기록이 없는 항목은 적지 않았고,"
           " '미확인'은 없다는 뜻이 아니라 확인하지 못했다는 뜻입니다.", ""]
    for key, label in FACT_ROWS:
        if card.get(key):
            out.append(f"- **{label}**: {card[key]}")
    out.append(f"- **API**: {api_status(row)}")
    out.append("- **실제 호출**: 확인하지 않음 (주소 확인은 호출 성공과 다름)")
    license_text = official.get("license_text") or ", ".join(row.get("licenses") or []) or card.get("license")
    if license_text:
        out.append(f"- **이용허락**: {license_text}")
    if card.get("update_cycle_portal"):
        out.append(f"- **갱신 주기(포털 표기)**: {card['update_cycle_portal']} — 포털 표기일 뿐 실시간 제공을 보장하지 않음")
    if card.get("conflicts"):
        out.append(f"- **설명 간 불일치(확인 필요)**: {card['conflicts']}")
    if card.get("api_status") and "미확인" in card["api_status"] and "미확인" not in api_status(row):
        out.append(f"- **카드 표기**: {card['api_status']}")
    if card.get("limits"):
        out += ["", "## 제한 사항 (공식 설명 인용)", "", *(f"- {s}" for s in card["limits"])]
    if card.get("description"):
        out += ["", "## 설명", "", card["description"] + ("…" if len(card["description"]) >= hs.CARD_DESCRIPTION_CHARS else "")]
    fields = seoul_fields(row)
    if fields:
        out += ["", f"## 제공 필드 (서울 열린데이터광장, {len(fields)}개)", "", *(f"- {f}" for f in fields)]
    series = V2["series_of"].get(name)
    if series:
        relation = {r["dataset_id"]: r for r in series["relations"]}
        others = sorted((m for m in series["members"] if m != name and f"dataset:{m}" in entities),
                        key=lambda m: member_order(entities[f"dataset:{m}"]))
        out += ["", f"## 같은 시리즈의 다른 데이터 ({len(others)})", "",
                "> 연도·지역·언어·공간 단위가 다른 같은 계열의 데이터입니다. **같은 자료의 사본이 아니며 서로 대체할 수 없습니다.**"
                " 관계는 기준 데이터와 비교한 것이고, 모두 검증 전입니다.", ""]
        for m in others:
            kinds = relation.get(m, {}).get("relation_to_anchor") or []
            note = "기준 데이터" if m == series["anchor"] else ", ".join(SERIES_RELATION.get(k, k) for k in kinds) or "관계 미기록"
            out.append(f"- {link(entity_page(entities[f'dataset:{m}']), display(entities[f'dataset:{m}']))} — {note}")
    return out + [""]


def v2_context():
    """Read the frozen build's outputs; stop if any differs from the pin."""
    from corpus_manifest import content_digest, directory_record

    pin = json.loads(PIN.read_text(encoding="utf-8"))
    # Build outputs, plus the README folder the pinned documents were built from.
    recorded = {o["path"]: o["sha256"] for stage in pin["stages"].values() for o in stage["outputs"] + stage["inputs"]}
    inputs = {}
    for path, use in V2_INPUTS.items():
        target = AI_DIR / path
        digest = directory_record(target)["sha256"] if target.is_dir() else content_digest(target)[0]
        if recorded.get(path) != digest:
            raise SystemExit(f"{path} is not the pinned {pin['data_version']} output ({digest[:12]} != {str(recorded.get(path))[:12]})")
        inputs[path] = {"sha256": digest, "used_for": use}
    with open(AI_DIR / "data" / "dataset_index_v2" / "chunks.jsonl", encoding="utf-8") as f:
        cards = {c["dataset_id"]: c["text"] for c in map(json.loads, f) if c["kind"] == "card"}
    rows = {r["dataset_id"]: r for r in read_jsonl(AI_DIR / "data" / "public_enriched" / "public_datasets.jsonl")}
    series = json.loads((HYPERGRAPH_DIR / "series.json").read_text(encoding="utf-8"))
    series_of = {m: s for s in series for m in s["members"]}
    return {"data_version": pin["data_version"], "pin": pin, "inputs": inputs, "cards": cards, "rows": rows,
            "series_of": series_of}


# ---------------------------------------------------------------- pages


def render_entity(entity, links, relations, pages, concepts, entities):
    by_facet = defaultdict(list)
    for item in links:
        by_facet[item["facet"]].append(item)
    portal = bool(V2) and entity["kind"] == "dataset" and entity.get("source") in PORTALS
    props = {
        "type": entity["kind"],
        "id": entity["name"],
        **({"title": entity.get("title"), "publisher": entity.get("publisher"), "data_version": V2["data_version"]} if portal else {}),
        "source": entity["source"],
        "url": entity["url"],
        "downloads": entity.get("downloads"),
    }
    if entity["kind"] == "dataset":
        props.update(
            summary=entity.get("summary_ko"),
            readme_status=entity.get("readme_status"),
            readme_language=entity.get("readme_language"),
            korean_focus=entity.get("korean_focus"),
        )
    else:
        props.update(context_length=entity.get("context_length"), parameters_b=entity.get("parameter_count_billion"))
    for facet in FACET_ORDER:
        if by_facet.get(facet):
            props[facet] = [link(pages[i["concept_id"]], concepts[i["concept_id"]]["label"]) for i in by_facet[facet]]

    if V2:
        learning_label = "학습 데이터" if entity["kind"] == "model" else "학습에 사용한 모델"
        neighbors = [
            {"path": entity_page(entities[other]), "title": display(entities[other]), "relation": learning_label}
            for other in sorted(relations, key=lambda other: member_order(entities[other]))
        ]
        for facet in FACET_ORDER:
            for item in by_facet[facet]:
                cid = item["concept_id"]
                neighbors.append({
                    "path": pages[cid],
                    "title": concepts[cid]["label"],
                    "relation": concepts[cid]["facet_label"],
                })
        anchor = "분류" if links else "학습-데이터" if entity["kind"] == "model" else "이-데이터로-학습한-모델"
        props["wiki_graph"] = wiki_graph(display(entity), anchor, neighbors)

    if portal:
        body = [
            f"# {entity.get('title') or entity['name']}",
            "",
            f"> dataset · `{entity['name']}` · [{SOURCE_LABELS.get(entity['source'], entity['source'])}]({entity['url']})",
            "",
        ]
    else:
        body = [
            f"# {entity['name']}",
            "",
            f"> {entity['kind']} · [{SOURCE_LABELS.get(entity['source'], entity['source'])}]({entity['url']})",
            "",
        ]
    if entity.get("summary_ko"):
        body += [entity["summary_ko"], ""]
    if portal:
        body += portal_sections(entity, entities)
    body += ["## 분류", ""]
    for facet in FACET_ORDER:
        for item in by_facet.get(facet, []):
            concept = concepts[item["concept_id"]]
            source = ", ".join(item["fields"])
            raw = "" if item["raw"] is None else f" = `{item['raw']}`"
            body.append(
                f"- **{concept['facet_label']}**: {link(pages[item['concept_id']], concept['label'])}"
                f" — {item['method']} · {source}{raw} · 신뢰도 {item['confidence']}"
            )
    length = next((i for i in by_facet.get("input_length", [])), None)
    if entity["kind"] == "model" and length:
        compatible = compatible_lengths(concepts, length["concept_id"].split("/", 1)[1])
        body += ["", "처리 가능한 데이터 길이: " + " · ".join(link(pages[c], concepts[c]["label"]) for c in compatible)]
    if entity["kind"] == "dataset" and entity.get("sample_length"):
        sample = entity["sample_length"]
        body += [
            "",
            f"샘플 길이: `{sample['text_column']}` 열 p90 {sample['chars'].get('p90')}자"
            f" ≈ {sample['tokens_p90_estimate']} 토큰 (viewer statistics, {sample['config']}/{sample['split']})",
        ]
    if entity.get("duplicates"):
        body += ["", "## 같은 데이터의 사본·중복 등록", "", *(f"- `{d}`" for d in entity["duplicates"])]
    if relations:
        title = "## 학습 데이터" if entity["kind"] == "model" else "## 이 데이터로 학습한 모델"
        body += ["", title, ""]
        for other in relations:
            body.append(f"- {link(entity_page(entities[other]), display(entities[other]))}")
    return frontmatter(props) + "\n".join(body) + "\n"


def render_concept(concept_id, concept, members, cooccurring, pages, concepts, entities):
    props = {
        "type": "concept",
        "facet": concept["facet"],
        "key": concept["key"],
        "aliases": concept["aliases"],
        "members": len(members),
    }
    if V2:
        props["wiki_graph"] = wiki_graph(concept["label"], "함께-연결된-개념", [
            {"path": pages[c], "title": pages[c].rsplit("/", 1)[-1], "relation": f"공유 {n:,}개"}
            for c, n in cooccurring
        ])
    body = [f"# {concept['label']}", "", f"facet: [[{safe_name(concept['facet_label'])}]] · 개념 id `{concept_id}`", ""]
    if concept["aliases"]:
        body += ["별칭: " + ", ".join(concept["aliases"]), ""]
    for kind, title in (("model", "모델"), ("dataset", "데이터셋")):
        order = (lambda m: member_order(entities[m])) if V2 else (lambda m: -(entities[m].get("downloads") or 0))
        ids = sorted((m for m in members if entities[m]["kind"] == kind), key=order)
        if not ids:
            continue
        body += [f"## {title} ({len(ids)})", ""]
        body += [f"- {link(entity_page(entities[m]), display(entities[m]))}" for m in ids[:HUB_MEMBER_LIMIT]]
        if len(ids) > HUB_MEMBER_LIMIT:
            shown = "다운로드 순, 없으면 제목 순" if V2 else "다운로드 순"
            body.append(f"- … 외 {len(ids) - HUB_MEMBER_LIMIT}개 ({shown} 상위 {HUB_MEMBER_LIMIT}개만 표시)")
        body.append("")
    if cooccurring:
        body += ["## 함께 연결된 개념", ""]
        if V2:
            body += ["공유 개수는 두 개념에 모두 속한 모델·데이터셋의 수입니다.", ""]
        body += [
            f"- {link(pages[c], concepts[c]['label'])} ({concepts[c]['facet_label']}) · 공유 {n}"
            for c, n in cooccurring
        ]
    return frontmatter(props) + "\n".join(body) + "\n"


WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def broken_links(wiki_dir):
    """[[targets]] that resolve to no page (Obsidian matches by file name, anywhere in the vault)."""
    pages = {path.stem for path in wiki_dir.rglob("*.md")}
    broken: Counter[str] = Counter()
    for path in wiki_dir.rglob("*.md"):
        for target in WIKILINK_RE.findall(path.read_text(encoding="utf-8")):
            if target.strip() not in pages:
                broken[target.strip()] += 1
    return broken


def check(wiki_dir=WIKI_DIR):
    """CI gate: every link resolves and the vault is not empty."""
    pages = sum(1 for _ in wiki_dir.rglob("*.md"))
    broken = broken_links(wiki_dir)
    print(
        json.dumps(
            {"pages": pages, "broken_link_targets": len(broken), "examples": broken.most_common(5)}, ensure_ascii=False
        )
    )
    if broken or pages == 0:
        raise SystemExit(1)


def main():
    global HYPERGRAPH_DIR, WIKI_DIR, V2
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--corpus", choices=sorted(CORPORA), default="v2", help="v2 -> wiki_v2/, v1 -> wiki/")
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--check", action="store_true", help="verify every [[link]] in the vault resolves (CI gate)")
    args = parser.parse_args()
    if args.self_check:
        return self_check()
    HYPERGRAPH_DIR, WIKI_DIR = CORPORA[args.corpus]
    if args.check:
        return check(WIKI_DIR)
    if args.corpus == "v2":
        V2 = v2_context()

    entities = {e["entity_id"]: e for e in read_jsonl(HYPERGRAPH_DIR / "entities.jsonl")}
    concepts = {c["concept_id"]: c for c in read_jsonl(HYPERGRAPH_DIR / "concepts.jsonl")}
    links = read_jsonl(HYPERGRAPH_DIR / "links.jsonl")
    pages = concept_pages(concepts)

    links_by_entity, members = defaultdict(list), defaultdict(set)
    for item in links:
        links_by_entity[item["entity_id"]].append(item)
        members[item["concept_id"]].add(item["entity_id"])
    related = defaultdict(list)
    for rel in read_jsonl(HYPERGRAPH_DIR / "relations.jsonl"):
        related[rel["source"]].append(rel["target"])
        related[rel["target"]].append(rel["source"])

    # Co-occurrence between hubs = how many entities two hyperedges share.
    pair_counts: defaultdict[str, Counter[str]] = defaultdict(Counter)
    for entity_links in links_by_entity.values():
        ids = sorted({i["concept_id"] for i in entity_links})
        for a in ids:
            for b in ids:
                if a != b:
                    pair_counts[a][b] += 1

    staging = WIKI_DIR.with_name(WIKI_DIR.name + ".tmp")
    shutil.rmtree(staging, ignore_errors=True)
    for folder in ("models", "datasets", "concepts", "facets"):
        (staging / folder).mkdir(parents=True)
    for entity_id, entity in entities.items():
        text = render_entity(
            entity, links_by_entity[entity_id], sorted(set(related[entity_id])), pages, concepts, entities
        )
        (staging / f"{entity_page(entity)}.md").write_text(text, encoding="utf-8")
    for concept_id, concept in concepts.items():
        if not members[concept_id]:
            continue
        cooccurring = [
            (c, n) for c, n in pair_counts[concept_id].most_common() if concepts[c]["facet"] != concept["facet"]
        ]
        if V2:
            cooccurring.sort(key=lambda pair: shared_concept_order(pair_counts, members, concept_id, pair[0]))
        else:
            cooccurring = cooccurring[:COOCCURRING_LIMIT]
        text = render_concept(
            concept_id, concept, members[concept_id], cooccurring, pages, concepts, entities
        )
        (staging / f"{pages[concept_id]}.md").write_text(text, encoding="utf-8")
    facets = load_taxonomy()["facets"]
    index = [
        "# Model Scout 위키",
        "",
        f"모델 {sum(e['kind'] == 'model' for e in entities.values())}개 · "
        f"데이터셋 {sum(e['kind'] == 'dataset' for e in entities.values())}개 · 연결 {len(links)}개",
        "",
    ]
    if V2:
        sources = Counter(e.get("source") for e in entities.values() if e["kind"] == "dataset")
        index[2:2] = [
            f"데이터 버전: v2 고정본 `{V2['data_version']}` (생성 기록 `.build.json`)",
            "",
            "데이터셋 출처: " + " · ".join(f"{SOURCE_LABELS.get(s, s)} {n}" for s, n in sources.most_common()),
            "",
        ]
    facet_neighbors = []
    if V2:
        index += ["## 분류", ""]
    for facet, spec in facets.items():
        rows = [(cid, c) for cid, c in concepts.items() if c["facet"] == facet and members[cid]]
        if V2 and not rows:  # a facet no v2 entity uses (갱신 주기) gets no empty page
            continue
        facet_page = safe_name(spec["label"])
        facet_props: dict[str, object] = {"type": "facet", "facet": facet}
        facet_body = [f"# {spec['label']}", "", f"대상: {', '.join(spec['applies_to'])}", ""]
        if V2:
            facet_body += ["## 개념", ""]
            sorted_rows = sorted(rows, key=lambda row: (-len(members[row[0]]), row[0]))
            facet_props["wiki_graph"] = wiki_graph(spec["label"], "개념", [
                {"path": pages[cid], "title": c["label"], "relation": f"항목 {len(members[cid]):,}개"}
                for cid, c in sorted_rows
            ])
            facet_neighbors.append({"path": f"facets/{facet_page}", "title": spec["label"],
                                    "relation": f"개념 {len(rows)}개"})
        facet_body += [f"- {link(pages[cid], c['label'])} · {len(members[cid])}" for cid, c in rows]
        (staging / "facets" / f"{facet_page}.md").write_text(
            frontmatter(facet_props) + "\n".join(facet_body) + "\n", encoding="utf-8"
        )
        index.append(f"- [[{facet_page}]] · 개념 {len(rows)}개")
    index_props = frontmatter({"wiki_graph": wiki_graph("Model Scout 위키", "분류", facet_neighbors)}) if V2 else ""
    (staging / "index.md").write_text(index_props + "\n".join(index) + "\n", encoding="utf-8")
    if V2:
        record = {
            "corpus": "v2", "data_version": V2["data_version"],
            "corpus_id": V2["pin"]["stages"]["hypergraph"]["stage_id"],
            "documents_id": V2["pin"]["stages"]["documents"]["stage_id"],
            "built_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
            "inputs": V2["inputs"],
            "builder_sha256": hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
        }
        (staging / ".build.json").write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    shutil.rmtree(WIKI_DIR, ignore_errors=True)
    staging.rename(WIKI_DIR)
    pages_written = sum(1 for _ in WIKI_DIR.rglob("*.md"))
    print(f"wiki -> {WIKI_DIR}/ ({pages_written} pages)")


def self_check():
    global V2
    assert safe_name("a/b:c#d") == "a_b_c_d"
    assert entity_page({"kind": "dataset", "name": "klue/klue"}) == "datasets/klue__klue"
    pages = concept_pages(
        {
            "input_modality/text": {"label": "텍스트", "facet_label": "입력 형식"},
            "output_modality/text": {"label": "텍스트", "facet_label": "출력 형식"},
            "task/summarization": {"label": "요약", "facet_label": "작업"},
        }
    )
    assert (
        pages["input_modality/text"] == "concepts/텍스트 (입력 형식)" and pages["task/summarization"] == "concepts/요약"
    )
    assert link("concepts/요약") == "[[요약]]" and link("models/a__b", "a/b") == "[[a__b|a/b]]"
    member_sets = {"current": set(range(10)), "frequent": set(range(100)), "close": set(range(4))}
    counts = {"current": {"frequent": 10, "close": 4}}
    assert shared_concept_order(counts, member_sets, "current", "close") < shared_concept_order(
        counts, member_sets, "current", "frequent"
    )
    neighbors = [{"path": f"concepts/{i}", "title": str(i), "relation": "분류"} for i in range(13)]
    assert wiki_graph("현재", "분류", neighbors) == {"title": "현재", "anchor": "분류", "neighbors": neighbors[:10]}
    assert wiki_graph("현재", "분류", []) is None
    assert compatible_lengths({}, "long") == ["input_length/short", "input_length/medium", "input_length/long"]
    assert compatible_lengths({}, "nope") == []
    assert frontmatter({"a": 1, "b": ["[[x]]"], "c": None}) == '---\na: 1\nb:\n  - "[[x]]"\n---\n'
    assert WIKILINK_RE.findall("see [[요약]] and [[a__b|a/b]] and [[장문#x]]") == ["요약", "a__b", "장문"]
    # v2: titles show, ids name the pages; API look-up states stay apart; unknown is not "none".
    seoul = {"name": "seoul_open_data/OA-1", "source": "seoul_open_data", "title": "제목 [1]|판"}
    assert display(seoul) == "seoul_open_data/OA-1"  # v1 keeps ids
    V2 = {"data_version": "x"}
    assert display(seoul) == "제목  1  판" and entity_page({**seoul, "kind": "dataset"}) == "datasets/seoul_open_data__OA-1"
    assert "자동변환" in api_status({"official": {"api_check": "confirmed_auto"}, "formats": ["api", "csv"]})
    assert "API가 없다는 뜻은 아님" in api_status({"official": {"api_check": "not_found"}, "formats": ["csv"]})
    assert "주소 확인 기록 없음" in api_status({"formats": ["api"], "api_service": "bikeList"})
    assert api_status({"formats": ["csv"]}).startswith("API 표기 없음")
    portal = {"source": "data_go_kr", "downloads": None}
    order = sorted([{**portal, "name": "b", "title": "가"}, {**portal, "name": "a", "title": "나"},
                    {"name": "h", "source": "huggingface", "downloads": 5}], key=member_order)
    assert [e["name"] for e in order] == ["h", "b", "a"]
    V2 = None
    print("15_build_wiki ok")


if __name__ == "__main__":
    main()
