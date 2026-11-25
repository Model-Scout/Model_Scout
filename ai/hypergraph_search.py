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
use_corpus(). v1 may fall back to the vectors published to Supabase. v2 is used only after its
records check out, in one of two ways:
- local vectors (a build machine): graph and documents unchanged since they were built, built from
  this graph, vectors from these documents with their model (check_corpus / check_vectors);
- a server (MODEL_SCOUT_DATA_VERSION set, no build inputs): the deployed graph files match their
  build record, the graph and document records are that frozen version and link to each other, the
  deployed vector file is the one recorded for those documents, and the v2 tables hold the same
  build with the same embedding model. Vectors are searched in memory from the deployed file.
v2 never searches Supabase: match_model_scout_datasets_v2 took 23-38 s per query (search plus the
transfer of every dataset's score; cause not yet isolated). A missing vector file, a mismatch or an
unreachable database stops v2; it never falls back to v1.
"""

from __future__ import annotations

import functools
import json
import math
import os
import re
import unicodedata
from collections import defaultdict
from typing import NamedTuple
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
# Supabase build record a versioned corpus must match (its vectors are always searched locally).
DB_BUILD_RECORD = {"v2": "model_scout_dataset_index_v2_meta"}
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
# Hub popularity added per log10 download (Hub data only; portal counts mean something else).
DOWNLOAD_WEIGHT = 0.5


class RankProfile(NamedTuple):
    """The weights one dataset search scores with. PROJECT_PROFILE is the ranking every search used before profiles
    existed, so a caller that passes none ranks exactly as before."""
    name: str
    dense_weight: float = DENSE_WEIGHT
    download_weight: float = DOWNLOAD_WEIGHT


PROJECT_PROFILE = RankProfile("project")
# A direct data question ("서울 문화행사 공공데이터 찾아줘"): topic fit and the data's own conditions decide, not how
# popular a Hub set is. An initial setting, not a tuned one: concept, keyword, region, Korean-focus and README terms
# are the project's; downloads no longer add to the score and only order equal scores. The caller also leaves model
# tasks and SFT roles out of the query concepts (17 search_project_datasets).
LOOKUP_PROFILE = RankProfile("lookup", download_weight=0.0)
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
# Words in many titles across topics ("버스 위치", "가로수 위치"): they say nothing about the topic.
# shortcut: hand-picked list; grow it when a generic planner term pulls in off-topic titles.
GENERIC_TERMS = {"위치", "가격", "요금", "정보", "현황", "목록", "데이터", "공공데이터", "api", "csv", "서비스", "통계",
                 "지역", "실시간"}
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
    for cached in (load_graph, load_link_evidence, load_dataset_vectors, corpus_identity, _local_cards):
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

    if os.environ.get("MODEL_SCOUT_DATA_VERSION"):
        return _deployed_identity()
    problems = check_corpus(HYPERGRAPH_DIR, DATASET_INDEX_DIR) + check_vectors(DATASET_INDEX_DIR)
    if problems:
        raise CorpusMismatch(f"corpus {CORPUS} cannot be used:\n- " + "\n- ".join(problems))
    return {
        "corpus": CORPUS,
        "corpus_id": load_manifest(HYPERGRAPH_DIR)["stage_id"],
        "documents_id": load_manifest(DATASET_INDEX_DIR)["stage_id"],
        "vectors": "local",
    }


def _deployed_identity():
    """A server's v2: deployed graph, build records and vector file, matching Supabase. Stops on any mismatch."""
    from corpus_manifest import check_manifest, load_manifest, sha256_file, sha256_text

    graph, documents = load_manifest(HYPERGRAPH_DIR), load_manifest(DATASET_INDEX_DIR)
    if graph is None or documents is None:
        raise CorpusMismatch(f"corpus {CORPUS}: build records missing (deploy {HYPERGRAPH_DIR.name}/ and "
                             f"{DATASET_INDEX_DIR.name}/build_manifest.json)")
    expected = os.environ.get("MODEL_SCOUT_DATA_VERSION")
    problems = check_manifest(HYPERGRAPH_DIR, sections=("outputs",))  # the graph files as built
    if not expected:
        problems.append("MODEL_SCOUT_DATA_VERSION is not set: the server must name the frozen version it serves")
    elif not documents["stage_id"].startswith(expected):
        problems.append(f"deployed documents {documents['stage_id'][:16]} are not data_version {expected}")
    if (documents.get("upstream") or {}).get("corpus_id") != graph["stage_id"]:
        problems.append("deployed documents were not built from the deployed graph")
    # The pin (data_version.json, from git) is the record independent of the vector files: it names the
    # documents and the ordered chunk ids that vector rows follow.
    pin_path = DATASET_INDEX_DIR / "data_version.json"  # deploy.sh copies it here; a checkout keeps it in test/
    if not pin_path.exists() and CORPUS == "v2":
        pin_path = DATA_DIR.parent / "test" / "public_data" / "corpus_v2" / "data_version.json"
    pin = json.loads(pin_path.read_text(encoding="utf-8")) if pin_path.exists() else {}
    if not pin:
        problems.append(f"고정 기록 없음: {pin_path} (deploy.sh가 함께 배포)")
    elif pin.get("data_version") != expected or pin["stages"]["documents"]["stage_id"] != documents["stage_id"]:
        problems.append("고정 기록이 배포된 문서 버전이 아님")
    model = documents["options"].get("embedding_model")
    vectors_path, record_path = DATASET_INDEX_DIR / "embeddings.npy", DATASET_INDEX_DIR / "manifest.json"
    # The deployed vector file must be the one recorded for these documents.
    record = json.loads(record_path.read_text(encoding="utf-8")) if record_path.exists() else {}
    recorded_sha = (record.get("embedding_run") or {}).get("vectors_sha256")
    if not vectors_path.exists():
        problems.append(f"벡터 없음: {vectors_path} (20_sync_dataset_index.py --corpus {CORPUS} --restore-vectors)")
    elif record.get("documents_id") != documents["stage_id"] or record.get("model") != model:
        problems.append("deployed vector record is not for the deployed documents and model")
    elif recorded_sha != sha256_file(vectors_path):
        problems.append("deployed embeddings.npy is not the recorded file")
    elif len(record.get("chunk_ids") or []) != np.load(vectors_path, mmap_mode="r").shape[0]:
        problems.append("deployed embeddings.npy rows differ from the recorded chunks")
    elif pin and sha256_text(record["chunk_ids"]) != pin.get("chunk_ids_sha256"):
        problems.append("벡터 기록의 청크 ID 목록(내용 또는 순서)이 고정 기록과 다름")
    meta = _db_build_record()
    checks = [("corpus_id", graph["stage_id"]), ("documents_id", documents["stage_id"]),
              ("embedding_model", model), ("vectors_sha256", recorded_sha)]
    for key, value in checks:
        if meta.get(key) != value:
            problems.append(f"Supabase {DB_BUILD_RECORD[CORPUS]} holds another build: {key} {str(meta.get(key))[:16]} != {str(value)[:16]}")
    if problems:
        raise CorpusMismatch(f"corpus {CORPUS} cannot be used:\n- " + "\n- ".join(problems))
    return {"corpus": CORPUS, "corpus_id": graph["stage_id"], "documents_id": documents["stage_id"],
            "vectors": "local", "embedding_model": model}


def _db_build_record():
    from supabase_db import db_connection

    try:
        conn = db_connection()
    except Exception as error:  # noqa: BLE001 - any connection failure stops v2 with the reason
        raise CorpusMismatch(f"corpus {CORPUS}: Supabase is unreachable, v2 cannot verify its build ({error})") from error
    try:
        with conn.cursor() as cur:
            cur.execute(f"select value from public.{DB_BUILD_RECORD[CORPUS]} where key = 'build'")
            row = cur.fetchone()
    finally:
        conn.close()
    if not row:
        raise CorpusMismatch(f"corpus {CORPUS}: no build record in {DB_BUILD_RECORD[CORPUS]} (load it with 20 --corpus {CORPUS} --apply)")
    return row[0]


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

    try:
        conn = db_connection()
    except Exception as error:  # noqa: BLE001 - a search without its vectors must say so, not return nothing
        raise CorpusMismatch(f"corpus {CORPUS}: Supabase is unreachable, dataset search has no vectors ({error})") from error
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


# Lines a v2 search card states (14_build_dataset_chunks.portal_card_lines + concept lines) -> fact key.
CARD_FACT_LINES = {
    "데이터 형식": "formats",
    "상업 이용": "commercial_use",
    "이용허락": "license",
    "갱신 주기(포털 표기)": "update_cycle_portal",
    "API 제공 여부": "api_status",
    "설명 간 불일치(확인 필요)": "conflicts",  # official vs collected description, e.g. two coordinate systems  # 미확인 (no address on the page, not "no API") or a file's auto-converted API
    "제공기관": "publisher",
    "데이터 지역 범위": "coverage",
    "데이터 기간": "period",
    "언어판": "language_edition",
    "공간 단위": "spatial_unit",
}
CARD_DESCRIPTION_CHARS = 500
# Sentences of an official description that limit how the data can be used; quoted as they are.
LIMIT_RE = re.compile(r"좌표|EPSG|위경도|\d+\s*일\s*전|지연|기준일|기준 시점|최근\s*\d+\s*일|제공하지 않|미제공|제외|한정|최대\s*[\d,]+\s*건")
MAX_LIMITS = 3


@functools.lru_cache(maxsize=1)
def _local_cards():
    path = DATASET_INDEX_DIR / "chunks.jsonl"
    with open(path, encoding="utf-8") as f:
        return {c["dataset_id"]: c["text"] for c in map(json.loads, f) if c["kind"] == "card"}


def _card_texts(names):
    """Card text per dataset: the local documents on a build machine, else the v2 chunk table (by key)."""
    if (DATASET_INDEX_DIR / "chunks.jsonl").exists():
        cards = _local_cards()
        return {n: cards[n] for n in names if n in cards}
    from supabase_db import db_connection

    conn = db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("select dataset_id, text from public.model_scout_dataset_chunks_v2 where chunk_id = any(%s)",
                        ([f"{n}#card" for n in names],))
            return dict(cur.fetchall())
    finally:
        conn.close()


def _name_key(text):
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", str(text))).casefold()


@functools.lru_cache(maxsize=1)
def _dataset_name_index():
    """Datasets by full id, by the id's last part (HF repo name, portal id such as OA-15486) and by title."""
    by_id, by_tail, by_title = {}, defaultdict(list), defaultdict(list)
    for entity in load_graph()[0].values():
        if entity["kind"] != "dataset":
            continue
        by_id[_name_key(entity["name"])] = entity["entity_id"]
        by_tail[_name_key(entity["name"].rsplit("/", 1)[-1])].append(entity["entity_id"])
        if entity.get("title"):
            by_title[_name_key(entity["title"])].append(entity["entity_id"])
    return by_id, dict(by_tail), dict(by_title)


NAME_CANDIDATES = 5
TITLE_PART_MIN = 4  # characters a title fragment needs before it may name a dataset
# Characters (spaces left out) a whole catalog title needs before finding it inside a message counts as the user naming
# it: shorter titles ("서울시 인구") read like topics and would turn a topic search into a name lookup.
TITLE_IN_TEXT_MIN = 8


def catalog_titles_in(text):
    """Whole catalog dataset titles the text contains, as the catalog spells them, longest first; a title inside a
    longer one found here is left out. Read from the catalog only: a topic ("서울 문화행사 관련 데이터") contains no
    whole title and finds nothing."""
    key = _name_key(text)
    found = [title for title in _dataset_name_index()[2] if len(title) >= TITLE_IN_TEXT_MIN and title in key]
    kept = [t for t in sorted(found, key=len, reverse=True) if not any(t != o and t in o for o in found)]
    entities = load_graph()[0]
    return [entities[_dataset_name_index()[2][t][0]]["title"] for t in kept]


def resolve_dataset_names(names, limit=NAME_CANDIDATES):
    """Which catalog dataset each name a user wrote means, from the catalog alone: the full id, the id's last part,
    the exact title, then a title that contains the name. One match is found; several stay ambiguous with their
    candidates (none is picked for the user); none is not_found, which says this catalog has no such name.

    -> {name: {"status": found|ambiguous|not_found, "match": id|id_part|title|title_part|None, "entity_id",
               "candidates": [dataset ids]}}
    """
    by_id, by_tail, by_title = _dataset_name_index()
    entities = load_graph()[0]
    out = {}
    for name in dict.fromkeys(str(n).strip() for n in names if str(n).strip()):
        key = _name_key(name)
        if key in by_id:
            hits, match = [by_id[key]], "id"
        elif key in by_tail:
            hits, match = by_tail[key], "id_part"
        elif key in by_title:
            hits, match = by_title[key], "title"
        elif len(key) >= TITLE_PART_MIN:
            hits, match = [i for title, ids in by_title.items() if key in title for i in ids], "title_part"
        else:
            hits, match = [], None
        hits = sorted(dict.fromkeys(hits), key=lambda i: -(entities[i].get("downloads") or 0))
        status = "found" if len(hits) == 1 else "ambiguous" if hits else "not_found"
        out[name] = {"status": status, "match": match if hits else None,
                     "entity_id": hits[0] if status == "found" else None,
                     "candidates": [entities[i]["name"] for i in hits[:limit]]}
    return out


def dataset_facts(names):
    """What the v2 card states about each dataset, for explaining a recommendation (not for ranking).

    Only what the card says: a fact the card does not state is absent, and "미확인"/"확인 필요" stays
    unconfirmed, never "not provided". v1 cards carry none of these lines, so v1 returns nothing.
    """
    if CORPUS == "v1" or not names:
        return {}
    try:
        cards = _card_texts(list(dict.fromkeys(names)))
    except Exception as error:  # noqa: BLE001 - the answer says the facts were unavailable instead of failing
        return {n: {"unavailable": f"데이터 카드 조회 실패 ({type(error).__name__})"} for n in names}
    return {name: card_facts(text) for name, text in cards.items()}


def card_facts(text):
    """The fact lines of one v2 card (also read by 15_build_wiki.py, so the wiki says what answers say)."""
    found = {}
    for line in text.splitlines():
        key, _, value = line.partition(": ")
        if key in CARD_FACT_LINES and value:
            found[CARD_FACT_LINES[key]] = value
        elif key == "Description" and value:
            found["description"] = value[:CARD_DESCRIPTION_CHARS]
            sentences = re.split(r"\s*[*※]\s*|(?<=[.다])\s+", value)
            # A field list ("제공 필드: …, 좌표정보(X)") names columns; it is not a limit.
            limits = [s.strip(" .") for s in sentences if LIMIT_RE.search(s) and "제공 필드" not in s]
            if limits:
                # Whole sentences: a cut can drop the condition or negation that makes it a limit
                # (the longest in v2 is ~700 characters, so three of them stay short).
                found["limits"] = list(dict.fromkeys(limits))[:MAX_LIMITS]
    return found


def embed_query(text):
    """The query in the embedding space of the chosen corpus's vectors."""
    return _embed_query(text, query_model())


def query_model():
    identity = corpus_identity()
    if identity.get("embedding_model"):  # a server has the documents' build record, not the vector record
        return identity["embedding_model"]
    return json.loads((DATASET_INDEX_DIR / "manifest.json").read_text(encoding="utf-8"))["model"]


@functools.lru_cache(maxsize=1024)
def _embed_query(text, model):  # deterministic per text and model; repeated demo questions skip the API call
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv(DATA_DIR.parent / ".env")
    # The SDK waits 10 minutes by default; a stuck call must fail so the other search can still answer.
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], timeout=10.0, max_retries=1)
    response = client.embeddings.create(model=model, input=[text])
    return response.data[0].embedding


def _length_rank(concept_ids):
    keys = list(load_taxonomy()["facets"]["input_length"]["values"])
    ranks = [keys.index(c.split("/", 1)[1]) for c in concept_ids if c.startswith("input_length/")]
    return max(ranks) if ranks else None


def concepts_from_terms(terms):
    """Map free words from an idea decomposition ('reranking', '장문', 'ko') to concept ids."""
    found = set()
    # "위치" -> domain/location would score every location table (분양가격, 가로수 위치) as on-domain.
    for term in (t for t in terms if t.casefold() not in GENERIC_TERMS):
        for facet in load_taxonomy()["facets"]:
            if value := normalize(facet, term):
                found.add(f"{facet}/{value}")
    return found


_REGION_SUFFIX = re.compile(r"(?:특별자치시|특별자치도|특별시|광역시|시|도)$")


# Words that only contain a region's letters: 부산물 (by-product), 환경기초, 경기력, 기능경기, 경기동향 (economy),
# 서울올림픽 (an organisation with nationwide data).
# shortcut: hand-picked from the v2 titles; add a word when another one turns up.
_NOT_REGION = re.compile(r"부산물|환경기초|경기력|기능경기|경기동향|서울올림픽")


def region_of(word):
    """Canonical region a typed word names ("서울시", "경기도", "충청북도" -> 서울, 경기, 충북), else None."""
    base = word if word in REGIONS else _REGION_SUFFIX.sub("", word)
    return REGION_CANON.get(base, base) if base in REGIONS else None


def dataset_regions(entity):
    """Regions a dataset is about, from its source and title; empty for national data."""
    if entity.get("source") == "seoul_open_data":
        return {"서울"}
    title = _NOT_REGION.sub(" ", entity.get("title") or "")
    return {REGION_CANON.get(r, r) for r in REGIONS if r in title}


def title_topic_words(entity, keywords):
    """Typed topic words (not regions, not generic words) found in the dataset title."""
    title = (entity.get("title") or entity["name"]).casefold()
    return [k for k in keywords if not region_of(k) and len(k) >= 2 and k.casefold() not in GENERIC_TERMS
            and k.casefold() in title]


def keyword_score(entity, keywords, on_topic=False):
    """Bonus for typed words found in the title, plus region fit when the user named a region.
    on_topic: the dense match already says the topic fits, for titles that word it differently (대기오염 for 미세먼지)."""
    if not keywords:
        return 0.0, []
    wanted = {region_of(k) for k in keywords} - {None}
    found = title_topic_words(entity, keywords)
    score, reasons = min(KEYWORD_BONUS * len(found), KEYWORD_BONUS_CAP), [f"'{k}' 일치" for k in found]
    regions = dataset_regions(entity)
    if wanted and regions:
        if regions & wanted:
            # Region alone is not relevance: "충청북도_지적통계" must not outrank 공중화장실 data for 청주.
            score += REGION_MATCH_BONUS if found or on_topic else 0.0
            reasons.append(f"{'/'.join(sorted(regions & wanted))} 지역")
        else:
            score += REGION_MISMATCH_PENALTY
    return score, reasons


def rank_datasets(
    target_concepts, *, trained_with=(), query_vector=None, commercial_only=False, roles=None, limit=10, keywords=(),
    profile: RankProfile = PROJECT_PROFILE,
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
        # A topic word in the title ("전국주유소표준데이터" for 주유소) admits untagged data the cosine floors
        # would drop: public data has no task tags, and its short titles embed with low similarity.
        titled = bool(keywords) and not trusted_tasks and bool(title_topic_words(entity, keywords))
        topical = titled or (similarity is not None and similarity >= dense_only_min)
        if not (task_affinity.keys() & trusted_tasks or linked or (topical and not trusted_tasks)):
            continue
        if similarity is not None and similarity < dense_min and not (linked or titled):
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
        on_topic = similarity is not None and similarity >= dense_only_min
        bonus, matched_words = keyword_score(entity, keywords, on_topic)
        score += bonus
        reasons += matched_words
        graph_score = score
        if similarity is not None:
            score += profile.dense_weight * similarity
        # Download counts are only comparable within the Hub; portal counts mean something else.
        if entity.get("source", "huggingface") == "huggingface":
            score += profile.download_weight * math.log10(1 + (entity.get("downloads") or 0))
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
