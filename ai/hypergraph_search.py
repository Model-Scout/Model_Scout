"""Query the model/dataset hypergraph: which datasets fit a model, or a set of concepts.

Score = sum over shared hyperedges of facet weight x idf(hub). Rare hubs (장문, 법률) say more
than crowded ones (텍스트, 한국어), the same intuition as Adamic-Adar on ordinary graphs.
A dataset must share at least one task with the target (or be in its trained_with
relation); a shared language alone is not a reason to recommend data.

input_length is ordinal: a dataset longer than the model's context is excluded, an equal
bin scores full weight (good for evaluating that length), a shorter bin half.

Each link counts by its confidence: metadata high, README-quoted NER medium, unconfirmed
tags and loosely quoted NER low. A low-confidence task alone does not admit a dataset.

Dense similarity (same text-embedding-3-small space as the model documents) breaks the many
ties that coarse metadata leaves and lets datasets without task metadata in when their
README is clearly on topic. A small quality prior prefers used, documented, Korean data.

Corpus: graph, chunks and vectors are chosen together by MODEL_SCOUT_CORPUS (v1 default, v2) or
use_corpus(). v1 may fall back to the vectors published to Supabase; v2 never does (Supabase holds
v1 vectors) and is used only after its build records check out: graph and documents unchanged
since they were built, the documents built from this graph, and the vectors built from these
documents with their model (corpus_manifest.check_corpus / check_vectors).
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
CORPORA = {
    "v1": (DATA_DIR / "hypergraph", DATA_DIR / "dataset_index"),
    "v2": (DATA_DIR / "hypergraph_v2", DATA_DIR / "dataset_index_v2"),
}
CORPUS = os.environ.get("MODEL_SCOUT_CORPUS", "v1")
if CORPUS not in CORPORA:
    raise ValueError(f"MODEL_SCOUT_CORPUS must be one of {sorted(CORPORA)}, not {CORPUS!r}")
HYPERGRAPH_DIR, DATASET_INDEX_DIR = CORPORA[CORPUS]
MODEL_INPUTS = (DATA_DIR / "hf_models_stage4_core.jsonl", DATA_DIR / "hf_models_stage4_low_popularity.jsonl")
LFS_POINTER_PREFIX = b"version https://git-lfs.github.com/spec/"
# ponytail: hand-set weights; tune against the golden set once dataset queries exist there.
# input_length mostly filters (longer-than-model data is excluded); a large bonus let any long, loosely
# tagged set outrank core data once the download floor was dropped, so it only nudges.
FACET_WEIGHTS = {"task": 3.0, "domain": 2.0, "input_length": 1.0, "language": 1.0, "input_modality": 0.5}
TRAINED_WITH_BONUS = 5.0
# ponytail: dense cosine for text-embedding-3-small sits ~0.1-0.7; x10 makes 0.1 cosine worth one point.
DENSE_WEIGHT = 10.0
# Datasets with no task metadata (NER not run yet) enter only above this cosine.
DENSE_ONLY_MIN = 0.45
# ponytail: relevance floor for every candidate when a query vector exists; off-topic data with
# right-looking tags sits ~0.35-0.39, real matches >= 0.42. Re-tune on the golden set.
DENSE_MIN = 0.40
# Relative floors: keep candidates within these margins of the query's best similarity.
DENSE_MARGIN, DENSE_ONLY_MARGIN = 0.15, 0.08
README_PENALTY = {"template": -2.0, "thin": -2.0, "missing": -2.0}
CONFIDENCE_WEIGHT = {"high": 1.0, "medium": 0.8, "low": 0.3}
# Data built for a neighbouring task still trains or evaluates the model: embedding models are
# trained and benchmarked on retrieval corpora (MIRACL, Ko-StrategyQA) and NLI/STS pairs.
# ponytail: hand-set affinities; tune with the dataset golden set.
TASK_AFFINITY = {
    "embedding": {"retrieval": 0.7, "reranking": 0.5},
    "retrieval": {"embedding": 0.7, "reranking": 0.5},
    "reranking": {"retrieval": 0.8, "embedding": 0.6},
    "generation": {"question_answering": 0.7, "summarization": 0.6, "translation": 0.5, "language_modeling": 0.5},
    "question_answering": {"generation": 0.6, "retrieval": 0.5},
    "summarization": {"generation": 0.6},
    "translation": {"generation": 0.5},
}
HARD_MODALITIES = {"input_modality/image", "input_modality/video", "input_modality/audio"}
# Every model here serves Korean, so the language facet scores Korean coverage only; in this
# Korean-heavy corpus an English match is the rarer hub and would otherwise outscore it.
SCORED_LANGUAGES = {"language/ko"}
# Lexical layer for the words a user actually typed (따릉이, 미세먼지, 서울): exact title matches
# and region fit matter for public data, where one schema exists per city or province.
KEYWORD_BONUS, KEYWORD_BONUS_CAP = 1.0, 2.0
REGION_MATCH_BONUS, REGION_MISMATCH_PENALTY = 1.5, -3.0
REGIONS = (
    "서울",
    "부산",
    "대구",
    "인천",
    "광주",
    "대전",
    "울산",
    "세종",
    "경기",
    "강원",
    "충북",
    "충청북도",
    "충남",
    "충청남도",
    "전북",
    "전라북도",
    "전남",
    "전라남도",
    "경북",
    "경상북도",
    "경남",
    "경상남도",
    "제주",
)
REGION_CANON = {
    "충청북도": "충북",
    "충청남도": "충남",
    "전라북도": "전북",
    "전라남도": "전남",
    "경상북도": "경북",
    "경상남도": "경남",
}
KOREAN_FOCUS_BONUS = {"ko_only": 1.5, "ko_with_others": 1.0, "wide_multilingual": 0.0, "not_ko": -1.0}


class CorpusMismatch(RuntimeError):
    """The chosen corpus's graph, chunks and vectors are not one build."""


def use_corpus(name):
    """Switch graph, chunks and vectors together (an evaluation can compare v1 and v2 in one run)."""
    global CORPUS, HYPERGRAPH_DIR, DATASET_INDEX_DIR
    if name not in CORPORA:
        raise ValueError(f"unknown corpus {name!r}; choose from {sorted(CORPORA)}")
    CORPUS, (HYPERGRAPH_DIR, DATASET_INDEX_DIR) = name, CORPORA[name]
    for cached in (load_graph, load_link_evidence, load_dataset_vectors, corpus_identity):
        cached.cache_clear()
    return corpus_identity()


@functools.lru_cache(maxsize=1)
def corpus_identity():
    """Which build answers queries; raises CorpusMismatch when a versioned corpus does not check out.

    Evaluation results record this, so a score names the exact graph, documents and vectors.
    """
    if CORPUS == "v1":  # unversioned: the deployed graph; vectors local, else Supabase
        vectors = "local" if (DATASET_INDEX_DIR / "embeddings.npy").exists() else "supabase"
        return {"corpus": "v1", "corpus_id": None, "documents_id": None, "vectors": vectors}
    from corpus_manifest import check_corpus, check_vectors, load_manifest

    problems = check_corpus(HYPERGRAPH_DIR, DATASET_INDEX_DIR) + check_vectors(DATASET_INDEX_DIR)
    if problems:
        raise CorpusMismatch(f"corpus {CORPUS} cannot be used:\n- " + "\n- ".join(problems))
    return {
        "corpus": CORPUS,
        "corpus_id": load_manifest(HYPERGRAPH_DIR)["stage_id"],
        "documents_id": load_manifest(DATASET_INDEX_DIR)["stage_id"],
        "vectors": "local",
    }


def _read(name):
    corpus_identity()  # a versioned corpus is read only after its records check out
    with open(HYPERGRAPH_DIR / name, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


@functools.lru_cache(maxsize=1)
def load_graph():
    entities = {e["entity_id"]: e for e in _read("entities.jsonl")}
    concepts = {c["concept_id"]: c for c in _read("concepts.jsonl")}
    by_entity, members, confidence = defaultdict(set), defaultdict(set), {}
    for link in _read("links.jsonl"):
        by_entity[link["entity_id"]].add(link["concept_id"])
        members[link["concept_id"]].add(link["entity_id"])
        confidence[link["entity_id"], link["concept_id"]] = CONFIDENCE_WEIGHT[link["confidence"]]
    trained_with = defaultdict(set)
    for rel in _read("relations.jsonl"):
        trained_with[rel["source"]].add(rel["target"])
    return entities, concepts, by_entity, members, trained_with, confidence


@functools.lru_cache(maxsize=1)
def load_link_evidence():
    """(dataset entity, concept) -> (method, source fields, raw value or README quote)."""
    return {
        (link["entity_id"], link["concept_id"]): (link["method"], link["fields"], link["raw"])
        for link in _read("links.jsonl")
        if link["entity_id"].startswith("dataset:")
    }


@functools.lru_cache(maxsize=1)
def load_ner_quotes():
    """(dataset id, concept id) -> README quote verified by NER (16)."""
    path = DATA_DIR / "hf_datasets_ner.jsonl"
    quotes: dict[tuple[str, str], str] = {}
    if path.exists():
        with open(path, encoding="utf-8") as f:
            for row in map(json.loads, f):
                for facet, items in row.get("concepts", {}).items():
                    for item in items:
                        quotes.setdefault((row["dataset_id"], f"{facet}/{item['value']}"), item["quote"])
    return quotes


def evidence_item(entity_id, concept_id, label):
    """Why a dataset joined a hub: a verified README quote when NER confirmed it, else the
    metadata field and value it came from."""
    method, fields, raw = load_link_evidence().get((entity_id, concept_id), (None, [], None))
    if method is None:
        return None
    quote = load_ner_quotes().get((entity_id.split(":", 1)[1], concept_id))
    if quote:
        return {"concept": label, "source": "README 인용", "text": quote[:200]}
    return {
        "concept": label,
        "source": f"메타데이터 ({', '.join(f for f in fields if f != 'readme')})",
        "text": str(raw)[:200] if raw is not None else None,
    }


@functools.lru_cache(maxsize=1)
def load_dataset_vectors():
    """Unit-normalised chunk vectors plus, per row, the index of its dataset."""
    corpus_identity()
    manifest = json.loads((DATASET_INDEX_DIR / "manifest.json").read_text(encoding="utf-8"))
    matrix = np.load(DATASET_INDEX_DIR / "embeddings.npy", mmap_mode="r").astype(np.float32)
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-12
    names = sorted({cid.rsplit("#", 1)[0] for cid in manifest["chunk_ids"]})
    position = {name: i for i, name in enumerate(names)}
    owner = np.array([position[cid.rsplit("#", 1)[0]] for cid in manifest["chunk_ids"]])
    return matrix, owner, names


def _supabase_dense_scores(query_vector):
    from supabase_db import db_connection, vector_literal

    conn = db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "select dataset_id, similarity from public.match_model_scout_datasets(%s::halfvec)",
                (vector_literal(query_vector),),
            )
            return dict(cur.fetchall())
    finally:
        conn.close()


def _is_lfs_pointer(path):
    with open(path, "rb") as f:
        return f.read(len(LFS_POINTER_PREFIX)) == LFS_POINTER_PREFIX


def model_vector(model_id):
    """Stage 4 vector of a model: local snapshot if present (gitignored), else Supabase.

    The snapshots are Git LFS files, so a checkout without LFS (CI) has pointer stubs in their
    place; those count as absent.
    """
    if all(path.exists() and not _is_lfs_pointer(path) for path in MODEL_INPUTS):
        return load_model_vectors().get(model_id)
    from supabase_db import configured, db_connection, parse_vector

    if not configured():
        return None
    conn = db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "select embedding::text from public.model_scout_models where model_id = %s and active", (model_id,)
            )
            row = cur.fetchone()
    finally:
        conn.close()
    return parse_vector(row[0]) if row else None


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
    """Best cosine between the query and any chunk (card or README section) of each dataset.

    Uses the local index when this checkout has it (embeddings.npy is not in git), else the
    copy published to Supabase by 20_sync_dataset_index.py.
    """
    if corpus_identity()["vectors"] == "supabase":  # v1 only: v2 does not start without its vectors
        return _supabase_dense_scores(query_vector)
    matrix, owner, names = load_dataset_vectors()
    query = np.asarray(query_vector, dtype=np.float32)
    sims = matrix @ (query / (np.linalg.norm(query) + 1e-12))
    best = np.full(len(names), -1.0, dtype=np.float32)
    np.maximum.at(best, owner, sims)
    return dict(zip(names, best.tolist(), strict=False))


def embed_query(text):
    """The query in the embedding space of the chosen corpus's vectors."""
    return _embed_query(text, query_model())


def query_model():
    corpus_identity()
    return json.loads((DATASET_INDEX_DIR / "manifest.json").read_text(encoding="utf-8"))["model"]


@functools.lru_cache(maxsize=1024)
def _embed_query(text, model):  # deterministic per text and model; repeated demo questions skip the API call
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv(DATA_DIR.parent / ".env")
    response = OpenAI(api_key=os.environ["OPENAI_API_KEY"]).embeddings.create(model=model, input=[text])
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


def dataset_regions(entity):
    """Regions a dataset is about, from its source and title; empty for national data."""
    if entity.get("source") == "seoul_open_data":
        return {"서울"}
    title = entity.get("title") or ""
    return {REGION_CANON.get(r, r) for r in REGIONS if r in title}


def keyword_score(entity, keywords):
    """Bonus for typed words found in the title, plus region fit when the user named a region."""
    if not keywords:
        return 0.0, []
    title = (entity.get("title") or entity["name"]).casefold()
    wanted = {REGION_CANON.get(k, k) for k in keywords if k in REGIONS}
    words = [k for k in keywords if k not in REGIONS and len(k) >= 2]
    found = [k for k in words if k.casefold() in title]
    score, reasons = min(KEYWORD_BONUS * len(found), KEYWORD_BONUS_CAP), [f"'{k}' 일치" for k in found]
    regions = dataset_regions(entity)
    if wanted and regions:
        if regions & wanted:
            score += REGION_MATCH_BONUS
            reasons.append(f"{'/'.join(sorted(regions & wanted))} 지역")
        else:
            score += REGION_MISMATCH_PENALTY
    return score, reasons


def rank_datasets(
    target_concepts, *, trained_with=(), query_vector=None, commercial_only=False, roles=None, limit=10, keywords=()
):
    entities, concepts, by_entity, members, _, confidence = load_graph()
    dense = dense_scores(query_vector) if query_vector is not None else {}
    # Cosine scale shifts with query length ("따릉이 대여소" peaks near 0.35, a full sentence near
    # 0.6), so the floors follow the best match of this query instead of fixed values alone.
    best_dense = max(dense.values(), default=0.0)
    dense_min = min(DENSE_MIN, best_dense - DENSE_MARGIN)
    dense_only_min = min(DENSE_ONLY_MIN, best_dense - DENSE_ONLY_MARGIN)
    n = len(entities)
    # Dataset task -> (affinity, the target task it serves). A neighbour match is scored as a
    # fraction of a direct match on the *target* hub, so a rare neighbour (요약) cannot outrank
    # the model's own crowded task (생성) on idf alone.
    task_affinity: dict[str, tuple[float, str]] = {}
    for concept_id in (c for c in target_concepts if c.startswith("task/")):
        task = concept_id.split("/", 1)[1]
        for other, affinity in {task: 1.0, **TASK_AFFINITY.get(task, {})}.items():
            if affinity > task_affinity.get(f"task/{other}", (0.0, None))[0]:
                task_affinity[f"task/{other}"] = (affinity, concept_id)
    target_length = _length_rank(target_concepts)
    target_inputs = {c for c in target_concepts if c.startswith("input_modality/")}
    results = []
    for entity_id, entity in entities.items():
        if entity["kind"] != "dataset":
            continue
        dataset_concepts = by_entity[entity_id]
        linked = entity_id in trained_with
        similarity = dense.get(entity["name"])
        trusted_tasks = {c for c in dataset_concepts if c.startswith("task/") and confidence[entity_id, c] >= 0.8}
        topical = similarity is not None and similarity >= dense_only_min
        if not (task_affinity.keys() & trusted_tasks or linked or (topical and not trusted_tasks)):
            continue
        if similarity is not None and similarity < dense_min and not linked:
            continue
        # A model cannot consume a modality it has no input for: a text reranker gains nothing from
        # visual-document retrieval sets even though their queries are text.
        dataset_inputs = {c for c in dataset_concepts if c.startswith("input_modality/")}
        if target_inputs and not linked and (dataset_inputs & HARD_MODALITIES) - target_inputs:
            continue
        if commercial_only and "commercial_use/commercial" not in dataset_concepts:
            continue
        if roles and not any(f"dataset_role/{r}" in dataset_concepts for r in roles):
            continue
        reasons, score = [], TRAINED_WITH_BONUS if linked else 0.0
        if linked:
            reasons.append("학습 데이터로 인용됨")
        # One contribution per facet (its best match): a dataset tagged with ten languages or
        # tasks should not outscore one that matches the model's single language or task.
        best: dict[str, tuple[float, str]] = {}
        matched = (target_concepts | task_affinity.keys()) & dataset_concepts
        for concept_id in sorted(matched):
            facet = concept_id.split("/", 1)[0]
            if facet not in FACET_WEIGHTS or facet == "input_length":
                continue
            if facet == "language" and concept_id not in SCORED_LANGUAGES:
                continue
            affinity, hub = task_affinity.get(concept_id, (1.0, concept_id))
            weight = confidence[entity_id, concept_id] * affinity
            value = weight * FACET_WEIGHTS[facet] * math.log(n / len(members[hub]))
            if value > best.get(facet, (0.0, None))[0]:
                best[facet] = (value, concept_id)
        evidence = []
        for facet, (value, concept_id) in best.items():
            score += value
            weight = confidence[entity_id, concept_id]
            reasons.append(concepts[concept_id]["label"] + ("?" if weight < 0.8 else ""))
            if facet in ("task", "domain") and (
                item := evidence_item(entity_id, concept_id, concepts[concept_id]["label"])
            ):
                evidence.append(item)
        dataset_length = _length_rank(dataset_concepts)
        if target_length is not None and dataset_length is not None:
            if dataset_length > target_length:
                continue
            # Compatibility, not topic: a flat bonus, so a rare long-text hub cannot outrank task fit.
            length_id = next(c for c in dataset_concepts if c.startswith("input_length/"))
            score += FACET_WEIGHTS["input_length"] * (1.0 if dataset_length == target_length else 0.5)
            reasons.append(f"{concepts[length_id]['label']} (모델 입력 길이 이내)")
        bonus, matched_words = keyword_score(entity, keywords)
        score += bonus
        reasons += matched_words
        graph_score = score
        if similarity is not None:
            score += DENSE_WEIGHT * similarity
        # Download counts are only comparable within the Hub; portal counts mean something else.
        if entity.get("source", "huggingface") == "huggingface":
            score += 0.5 * math.log10(1 + (entity.get("downloads") or 0))
        score += README_PENALTY.get(entity.get("readme_status"), 0.0)
        score += 0.0 if linked else KOREAN_FOCUS_BONUS.get(entity.get("korean_focus"), 0.0)
        results.append(
            {
                "dataset": entity["name"],
                "title": entity.get("title"),
                "source": entity.get("source"),
                "score": round(score, 3),
                "graph_score": round(graph_score, 3),
                "dense": None if similarity is None else round(similarity, 3),
                "reasons": reasons,
                "downloads": entity.get("downloads"),
                "url": entity["url"],
                "readme_status": entity.get("readme_status"),
                "korean_focus": entity.get("korean_focus"),
                "summary_ko": entity.get("summary_ko"),
                "licenses": entity.get("licenses") or [],
                "evidence": evidence,
            }
        )
    results.sort(key=lambda r: (-r["score"], -(r["downloads"] or 0)))
    return results[:limit]


def datasets_for_model(model_id, **filters):
    entities, _, by_entity, _, trained_with, _ = load_graph()
    entity_id = f"model:{model_id}"
    if entity_id not in entities:
        raise KeyError(f"{model_id} is not in the model corpus")
    return rank_datasets(
        by_entity[entity_id], trained_with=trained_with[entity_id], query_vector=model_vector(model_id), **filters
    )


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
        rows = rank_datasets(concepts_from_terms(args.terms), query_vector=vector, keywords=args.terms, **filters)
    for row in rows:
        print(
            f"{row['score']:7.2f}  graph {row['graph_score']:5.1f}  dense {row['dense'] or 0:.2f}  "
            f"{row['dataset']:<50} {' · '.join(row['reasons'])}" + (f"  [{row['title']}]" if row.get("title") else "")
        )
