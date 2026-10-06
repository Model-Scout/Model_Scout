"""Load golden queries in the run schema and turn labels into graded relevance."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set

ROOT = Path(__file__).resolve().parents[1]
LABEL_DIR = ROOT / "test" / "golden" / "labels"
DEFAULT_QUERY_FILES = (
    LABEL_DIR / "semantic_golden_queries.jsonl",
    LABEL_DIR / "semantic_judged_queries.jsonl",
)


@dataclass
class GoldenQuery:
    query_id: str
    text: str
    plan_query_type: str
    query: Dict[str, Any]
    expected_behavior: str
    grades: Dict[str, int]
    must_exclude: List[str]
    unreachable: List[str] = field(default_factory=list)
    # Every model someone scored for this query. None = all others are irrelevant
    # by definition (comparisons answer with exactly the named models).
    judged: Optional[Set[str]] = None

    @property
    def scored(self) -> bool:
        return bool(self.grades)


def read_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def to_golden(item: Dict[str, Any], corpus_ids: Optional[set] = None) -> GoldenQuery:
    labels = item["labels"]
    behavior = labels["expected_behavior"]
    grades: Dict[str, int] = {}
    if behavior == "compare":
        for model_id in labels.get("expected_all") or []:
            grades[model_id] = 2
    elif behavior == "recommend":
        for model_id in labels.get("acceptable") or []:
            grades[model_id] = 1
        for model_id in labels.get("expected_any") or []:
            grades[model_id] = 2
    # Original checkpoints listed next to their DB conversions (e.g. g021) cannot
    # be retrieved; keeping them would cap Recall below 1 for every retriever.
    unreachable = [model_id for model_id in grades if corpus_ids is not None and model_id not in corpus_ids]
    for model_id in unreachable:
        grades.pop(model_id)
    must_exclude = [entry["model_id"] for entry in labels.get("must_exclude") or []]
    judged: Optional[Set[str]] = None
    if behavior != "compare":
        review = [entry["model_id"] if isinstance(entry, dict) else entry for entry in labels.get("needs_review") or []]
        judged = set(grades) | set(must_exclude) | set(review) | set(labels.get("judged_irrelevant") or [])
    return GoldenQuery(
        query_id=item["id"],
        text=item["text"],
        plan_query_type=item.get("plan_query_type") or item.get("query_type") or "unclassified",
        query=item,
        expected_behavior=behavior,
        grades=grades,
        must_exclude=must_exclude,
        unreachable=unreachable,
        judged=judged,
    )


def load(
    paths: Sequence[Path] = DEFAULT_QUERY_FILES,
    corpus_ids: Optional[set] = None,
    types: Optional[Sequence[str]] = None,
) -> List[GoldenQuery]:
    queries: List[GoldenQuery] = []
    for path in paths:
        for item in read_jsonl(path):
            if not item.get("evaluable_now", True):
                continue
            query = to_golden(item, corpus_ids)
            if types and query.plan_query_type not in types:
                continue
            queries.append(query)
    return queries
