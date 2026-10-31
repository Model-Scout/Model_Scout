"""Stage H2: render the hypergraph as an Obsidian vault (the LLM wiki).

The vault is a generated view of data/hypergraph/; edit the taxonomy or pipeline, never
the pages. Layout:
  wiki/index.md                    facet overview
  wiki/facets/<facet>.md           one page per facet, listing its concepts
  wiki/concepts/<label>.md         one hub per concept (= hyperedge): members + co-occurring hubs
  wiki/models/<org__name>.md       entity pages, frontmatter properties hold [[links]]
  wiki/datasets/<org__name>.md
Each link line names the metadata field it came from, so every edge is traceable.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path

from taxonomy import load_taxonomy

HYPERGRAPH_DIR = Path("data/hypergraph")
WIKI_DIR = Path("wiki")
# ponytail: hubs list the top members by downloads; Obsidian backlinks still show all of them.
HUB_MEMBER_LIMIT = 100
COOCCURRING_LIMIT = 12
UNSAFE_RE = re.compile(r'[\\/:*?"<>|#^\[\]]')
FACET_ORDER = list(load_taxonomy()["facets"])
SOURCE_LABELS = {"huggingface": "Hugging Face", "kaggle": "Kaggle", "seoul_open_data": "서울 열린데이터광장",
                 "data_go_kr": "공공데이터포털"}


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def safe_name(value):
    return UNSAFE_RE.sub("_", value).strip()


def entity_page(entity):
    folder = "models" if entity["kind"] == "model" else "datasets"
    return f"{folder}/{safe_name(entity['name'].replace('/', '__'))}"


def concept_pages(concepts):
    """Hub page name = label, or 'label (facet)' when two facets share a label (텍스트 in/out)."""
    counts = Counter(c["label"] for c in concepts.values())
    return {cid: "concepts/" + safe_name(c["label"] if counts[c["label"]] == 1 else f"{c['label']} ({c['facet_label']})")
            for cid, c in concepts.items()}


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


def render_entity(entity, links, relations, pages, concepts, entities):
    by_facet = defaultdict(list)
    for item in links:
        by_facet[item["facet"]].append(item)
    props = {"type": entity["kind"], "id": entity["name"], "source": entity["source"], "url": entity["url"],
             "downloads": entity.get("downloads")}
    if entity["kind"] == "dataset":
        props.update(summary=entity.get("summary_ko"), readme_status=entity.get("readme_status"),
                     readme_language=entity.get("readme_language"), korean_focus=entity.get("korean_focus"))
    else:
        props.update(context_length=entity.get("context_length"), parameters_b=entity.get("parameter_count_billion"))
    for facet in FACET_ORDER:
        if by_facet.get(facet):
            props[facet] = [link(pages[i["concept_id"]], concepts[i["concept_id"]]["label"]) for i in by_facet[facet]]

    body = [f"# {entity['name']}", "", f"> {entity['kind']} · [{SOURCE_LABELS.get(entity['source'], entity['source'])}]({entity['url']})", ""]
    if entity.get("summary_ko"):
        body += [entity["summary_ko"], ""]
    body += ["## 분류", ""]
    for facet in FACET_ORDER:
        for item in by_facet.get(facet, []):
            concept = concepts[item["concept_id"]]
            source = ", ".join(item["fields"])
            raw = "" if item["raw"] is None else f" = `{item['raw']}`"
            body.append(f"- **{concept['facet_label']}**: {link(pages[item['concept_id']], concept['label'])}"
                        f" — {item['method']} · {source}{raw} · 신뢰도 {item['confidence']}")
    length = next((i for i in by_facet.get("input_length", [])), None)
    if entity["kind"] == "model" and length:
        compatible = compatible_lengths(concepts, length["concept_id"].split("/", 1)[1])
        body += ["", "처리 가능한 데이터 길이: " + " · ".join(link(pages[c], concepts[c]["label"]) for c in compatible)]
    if entity["kind"] == "dataset" and entity.get("sample_length"):
        sample = entity["sample_length"]
        body += ["", f"샘플 길이: `{sample['text_column']}` 열 p90 {sample['chars'].get('p90')}자"
                     f" ≈ {sample['tokens_p90_estimate']} 토큰 (viewer statistics, {sample['config']}/{sample['split']})"]
    if entity.get("duplicates"):
        body += ["", "## 같은 데이터의 사본·중복 등록", "", *(f"- `{d}`" for d in entity["duplicates"])]
    if relations:
        title = "## 학습 데이터" if entity["kind"] == "model" else "## 이 데이터로 학습한 모델"
        body += ["", title, ""]
        for other in relations:
            body.append(f"- {link(entity_page(entities[other]), entities[other]['name'])}")
    return frontmatter(props) + "\n".join(body) + "\n"


def render_concept(concept_id, concept, members, cooccurring, pages, concepts, entities):
    props = {"type": "concept", "facet": concept["facet"], "key": concept["key"], "aliases": concept["aliases"],
             "members": len(members)}
    body = [f"# {concept['label']}", "", f"facet: [[{safe_name(concept['facet_label'])}]] · 개념 id `{concept_id}`", ""]
    if concept["aliases"]:
        body += ["별칭: " + ", ".join(concept["aliases"]), ""]
    for kind, title in (("model", "모델"), ("dataset", "데이터셋")):
        ids = sorted((m for m in members if entities[m]["kind"] == kind),
                     key=lambda m: -(entities[m].get("downloads") or 0))
        if not ids:
            continue
        body += [f"## {title} ({len(ids)})", ""]
        body += [f"- {link(entity_page(entities[m]), entities[m]['name'])}" for m in ids[:HUB_MEMBER_LIMIT]]
        if len(ids) > HUB_MEMBER_LIMIT:
            body.append(f"- … 외 {len(ids) - HUB_MEMBER_LIMIT}개 (다운로드 순 상위 {HUB_MEMBER_LIMIT}개만 표시)")
        body.append("")
    if cooccurring:
        body += ["## 함께 연결된 개념", ""]
        body += [f"- {link(pages[c], concepts[c]['label'])} ({concepts[c]['facet_label']}) · 공유 {n}" for c, n in cooccurring]
    return frontmatter(props) + "\n".join(body) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()

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
    pair_counts = defaultdict(Counter)
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
        text = render_entity(entity, links_by_entity[entity_id], sorted(set(related[entity_id])), pages, concepts, entities)
        (staging / f"{entity_page(entity)}.md").write_text(text, encoding="utf-8")
    for concept_id, concept in concepts.items():
        if not members[concept_id]:
            continue
        cooccurring = [(c, n) for c, n in pair_counts[concept_id].most_common() if concepts[c]["facet"] != concept["facet"]]
        text = render_concept(concept_id, concept, members[concept_id], cooccurring[:COOCCURRING_LIMIT], pages, concepts, entities)
        (staging / f"{pages[concept_id]}.md").write_text(text, encoding="utf-8")
    facets = load_taxonomy()["facets"]
    index = ["# Model Scout 위키", "", f"모델 {sum(e['kind'] == 'model' for e in entities.values())}개 · "
             f"데이터셋 {sum(e['kind'] == 'dataset' for e in entities.values())}개 · 연결 {len(links)}개", ""]
    for facet, spec in facets.items():
        rows = [(cid, c) for cid, c in concepts.items() if c["facet"] == facet and members[cid]]
        facet_body = [f"# {spec['label']}", "", f"대상: {', '.join(spec['applies_to'])}", ""]
        facet_body += [f"- {link(pages[cid], c['label'])} · {len(members[cid])}" for cid, c in rows]
        (staging / "facets" / f"{safe_name(spec['label'])}.md").write_text(
            frontmatter({"type": "facet", "facet": facet}) + "\n".join(facet_body) + "\n", encoding="utf-8")
        index.append(f"- [[{safe_name(spec['label'])}]] · 개념 {len(rows)}개")
    (staging / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")

    shutil.rmtree(WIKI_DIR, ignore_errors=True)
    staging.rename(WIKI_DIR)
    pages_written = sum(1 for _ in WIKI_DIR.rglob("*.md"))
    print(f"wiki -> {WIKI_DIR}/ ({pages_written} pages)")


def self_check():
    assert safe_name('a/b:c#d') == "a_b_c_d"
    assert entity_page({"kind": "dataset", "name": "klue/klue"}) == "datasets/klue__klue"
    pages = concept_pages({"input_modality/text": {"label": "텍스트", "facet_label": "입력 형식"},
                           "output_modality/text": {"label": "텍스트", "facet_label": "출력 형식"},
                           "task/summarization": {"label": "요약", "facet_label": "작업"}})
    assert pages["input_modality/text"] == "concepts/텍스트 (입력 형식)" and pages["task/summarization"] == "concepts/요약"
    assert link("concepts/요약") == "[[요약]]" and link("models/a__b", "a/b") == "[[a__b|a/b]]"
    assert compatible_lengths({}, "long") == ["input_length/short", "input_length/medium", "input_length/long"]
    assert compatible_lengths({}, "nope") == []
    assert frontmatter({"a": 1, "b": ["[[x]]"], "c": None}) == '---\na: 1\nb:\n  - "[[x]]"\n---\n'
    print("15_build_wiki ok")


if __name__ == "__main__":
    main()
