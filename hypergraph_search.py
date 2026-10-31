"""Query the model/dataset hypergraph: which datasets fit a model, or a set of concepts.

Score = sum over shared hyperedges of facet weight x idf(hub). Rare hubs (장문, 법률) say more
than crowded ones (텍스트, 한국어), the same intuition as Adamic-Adar on ordinary graphs.
A dataset must share at least one task with the target (or be in its trained_with
relation); a shared language alone is not a reason to recommend data.

input_length is ordinal: a dataset longer than the model's context is excluded, an equal
bin scores full weight (good for evaluating that length), a shorter bin half.

Dense similarity (same text-embedding-3-small space as the model documents) breaks the many
ties that coarse metadata leaves and lets datasets without task metadata in when their
README is clearly on topic. A small quality prior prefers used, documented, Korean data.
"""
from __future__ import annotations

import functools
import json
import math
import os
from collections import defaultdict
from pathlib import Path

import numpy as np

from taxonomy import load_taxonomy, normalize

DATA_DIR = Path(__file__).resolve().parent / "data"
HYPERGRAPH_DIR = DATA_DIR / "hypergraph"
DATASET_INDEX_DIR = DATA_DIR / "dataset_index"
MODEL_INPUTS = (DATA_DIR / "hf_models_stage4_core.jsonl", DATA_DIR / "hf_models_stage4_low_popularity.jsonl")
# ponytail: hand-set weights; tune against the golden set once dataset queries exist there.
FACET_WEIGHTS = {"task": 3.0, "domain": 2.0, "input_length": 2.0, "language": 1.0, "input_modality": 0.5}
TRAINED_WITH_BONUS = 5.0
# ponytail: dense cosine for text-embedding-3-small sits ~0.1-0.7; x10 makes 0.1 cosine worth one point.
DENSE_WEIGHT = 10.0
# Datasets with no task metadata (NER not run yet) enter only above this cosine.
DENSE_ONLY_MIN = 0.45
README_PENALTY = {"template": -2.0, "thin": -2.0, "missing": -2.0}
KOREAN_FOCUS_BONUS = {"ko_only": 1.5, "ko_with_others": 1.0, "wide_multilingual": 0.0, "not_ko": -1.0}


def _read(name):
    with open(HYPERGRAPH_DIR / name, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


@functools.lru_cache(maxsize=1)
def load_graph():
    entities = {e["entity_id"]: e for e in _read("entities.jsonl")}
    concepts = {c["concept_id"]: c for c in _read("concepts.jsonl")}
    by_entity, members = defaultdict(set), defaultdict(set)
    for link in _read("links.jsonl"):
        by_entity[link["entity_id"]].add(link["concept_id"])
        members[link["concept_id"]].add(link["entity_id"])
    trained_with = defaultdict(set)
    for rel in _read("relations.jsonl"):
        trained_with[rel["source"]].add(rel["target"])
    return entities, concepts, by_entity, members, trained_with


@functools.lru_cache(maxsize=1)
def load_dataset_vectors():
    """Unit-normalised chunk vectors plus, per row, the index of its dataset."""
    manifest = json.loads((DATASET_INDEX_DIR / "manifest.json").read_text(encoding="utf-8"))
    matrix = np.load(DATASET_INDEX_DIR / "embeddings.npy").astype(np.float32)
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-12
    names = sorted({cid.rsplit("#", 1)[0] for cid in manifest["chunk_ids"]})
    position = {name: i for i, name in enumerate(names)}
    owner = np.array([position[cid.rsplit("#", 1)[0]] for cid in manifest["chunk_ids"]])
    return matrix, owner, names


@functools.lru_cache(maxsize=1)
def load_model_vectors():
    vectors = {}
    for path in MODEL_INPUTS:
        with open(path, encoding="utf-8") as f:
            for line in f:
                row = json.loads(line)
                if row.get("embedding"):
                    vectors[row["model_id"]] = np.asarray(row["embedding"], dtype=np.float32)
    return vectors


def dense_scores(query_vector):
    """Best cosine between the query and any chunk (card or README section) of each dataset."""
    matrix, owner, names = load_dataset_vectors()
    query = np.asarray(query_vector, dtype=np.float32)
    sims = matrix @ (query / (np.linalg.norm(query) + 1e-12))
    best = np.full(len(names), -1.0, dtype=np.float32)
    np.maximum.at(best, owner, sims)
    return dict(zip(names, best.tolist()))


def embed_query(text):
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv(DATA_DIR.parent / ".env")
    manifest = json.loads((DATASET_INDEX_DIR / "manifest.json").read_text(encoding="utf-8"))
    response = OpenAI(api_key=os.environ["OPENAI_API_KEY"]).embeddings.create(model=manifest["model"], input=[text])
    return response.data[0].embedding


def _length_rank(concept_ids):
    keys = list(load_taxonomy()["facets"]["input_length"]["values"])
    ranks = [keys.index(c.split("/", 1)[1]) for c in concept_ids if c.startswith("input_length/")]
    return max(ranks) if ranks else None


def concepts_from_terms(terms):
    """Map free words from an idea decomposition ('reranking', '장문', 'ko') to concept ids."""
    found = set()
    for term in terms:
        for facet in load_taxonomy()["facets"]:
            if value := normalize(facet, term):
                found.add(f"{facet}/{value}")
    return found


def rank_datasets(target_concepts, *, trained_with=(), query_vector=None, commercial_only=False, roles=None, limit=10):
    entities, concepts, by_entity, members, _ = load_graph()
    dense = dense_scores(query_vector) if query_vector is not None else {}
    n = len(entities)
    target_tasks = {c for c in target_concepts if c.startswith("task/")}
    target_length = _length_rank(target_concepts)
    results = []
    for entity_id, entity in entities.items():
        if entity["kind"] != "dataset":
            continue
        dataset_concepts = by_entity[entity_id]
        linked = entity_id in trained_with
        similarity = dense.get(entity["name"])
        has_task = any(c.startswith("task/") for c in dataset_concepts)
        topical = similarity is not None and similarity >= DENSE_ONLY_MIN
        if not (target_tasks & dataset_concepts or linked or (topical and not has_task)):
            continue
        if commercial_only and "commercial_use/commercial" not in dataset_concepts:
            continue
        if roles and not any(f"dataset_role/{r}" in dataset_concepts for r in roles):
            continue
        reasons, score = [], TRAINED_WITH_BONUS if linked else 0.0
        if linked:
            reasons.append("학습 데이터로 인용됨")
        for concept_id in sorted(target_concepts & dataset_concepts):
            facet = concept_id.split("/", 1)[0]
            if facet in FACET_WEIGHTS and facet != "input_length":
                score += FACET_WEIGHTS[facet] * math.log(n / len(members[concept_id]))
                reasons.append(concepts[concept_id]["label"])
        dataset_length = _length_rank(dataset_concepts)
        if target_length is not None and dataset_length is not None:
            if dataset_length > target_length:
                continue
            length_id = next(c for c in dataset_concepts if c.startswith("input_length/"))
            weight = 1.0 if dataset_length == target_length else 0.5
            score += weight * FACET_WEIGHTS["input_length"] * math.log(n / len(members[length_id]))
            reasons.append(f"{concepts[length_id]['label']} (모델 입력 길이 이내)")
        graph_score = score
        if similarity is not None:
            score += DENSE_WEIGHT * similarity
        score += 0.5 * math.log10(1 + (entity.get("downloads") or 0))
        score += README_PENALTY.get(entity.get("readme_status"), 0.0)
        score += 0.0 if linked else KOREAN_FOCUS_BONUS.get(entity.get("korean_focus"), 0.0)
        results.append({"dataset": entity["name"], "score": round(score, 3), "graph_score": round(graph_score, 3),
                        "dense": None if similarity is None else round(similarity, 3), "reasons": reasons,
                        "downloads": entity.get("downloads"), "url": entity["url"],
                        "readme_status": entity.get("readme_status"), "korean_focus": entity.get("korean_focus")})
    results.sort(key=lambda r: (-r["score"], -(r["downloads"] or 0)))
    return results[:limit]


def datasets_for_model(model_id, **filters):
    entities, _, by_entity, _, trained_with = load_graph()
    entity_id = f"model:{model_id}"
    if entity_id not in entities:
        raise KeyError(f"{model_id} is not in the model corpus")
    return rank_datasets(by_entity[entity_id], trained_with=trained_with[entity_id],
                         query_vector=load_model_vectors().get(model_id), **filters)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rank datasets for a model or for concept terms.")
    parser.add_argument("--model")
    parser.add_argument("--terms", nargs="*", default=[])
    parser.add_argument("--query", help="free text to embed for dense similarity (one embedding API call)")
    parser.add_argument("--commercial-only", action="store_true")
    parser.add_argument("--role", action="append", choices=["train", "evaluation", "service"])
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    filters = {"commercial_only": args.commercial_only, "roles": args.role, "limit": args.limit}
    if args.model:
        rows = datasets_for_model(args.model, **filters)
    else:
        vector = embed_query(args.query) if args.query else None
        rows = rank_datasets(concepts_from_terms(args.terms), query_vector=vector, **filters)
    for row in rows:
        print(f"{row['score']:7.2f}  graph {row['graph_score']:5.1f}  dense {row['dense'] or 0:.2f}  "
              f"{row['dataset']:<50} {' · '.join(row['reasons'])}")
