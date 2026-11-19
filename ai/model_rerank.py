"""Reorder a need's model candidates with one LLM call, for the query types where it helps.

The hybrid score gets the right models into view but not into order: on the model-search golden
set, 93% of questions had a correct answer inside the top 50 while only 66% had one in the top 5.
Reordering a deeper slice is therefore worth an extra call -- but only for some question types.

Measured on 240 questions (recall@5, min_grade 2, query type from classify_model_query):

    type                     before  after   perfect   95% CI of the gain
    lexical_exact             0.650  0.774    0.838    [+0.033, +0.225]  significant
    model_comparison          0.423  0.611    0.716    [+0.111, +0.274]  significant
    benchmark_lookup          0.524  0.608    0.749    [-0.006, +0.171]  borderline
    semantic_capability       0.429  0.437    0.543    [-0.064, +0.069]  nothing
    semantic_constraint       0.276  0.290    0.401    [-0.059, +0.082]  nothing
    structured_constraint     0.322  0.300    0.587    [-0.091, +0.035]  slightly worse

RERANK_TYPES holds the first three. Applying it everywhere scores the same (0.511 vs 0.506) while
making an LLM call on every question instead of half of them, and it reorders the two types where
the model's judgement is noise: a question that only filters on size or license is answered by
every surviving candidate, so there is nothing to judge and popularity order is already right.

"scores:" carries only benchmarks the pipeline extracted into benchmark_metadata, which is what the
service can actually display. An earlier prompt let the model read benchmark names out of card
prose and it ranked models that merely transcribe a LibriSpeech sample above models that report a
LibriSpeech WER; saying where a score counts from took benchmark_lookup from +0.018 to +0.084.
"""

from __future__ import annotations

import json
import logging
import re
from typing import Any, Callable, Dict, List, Sequence

LOGGER = logging.getLogger(__name__)

# Question types where the LLM's judgement about which model the question points at pays off.
RERANK_TYPES = frozenset({"lexical_exact", "model_comparison", "benchmark_lookup"})
# Candidates to reorder. The perfect-reorder ceiling keeps climbing past this (0.648 at 20, 0.679 at
# 30, 0.702 at 50), but so does the prompt, and the measured gain was taken at 20.
RERANK_DEPTH = 20
CARD_CHARS = 420
SCORES_SHOWN = 10
TIMEOUT_SECONDS = 20.0
MAX_TOKENS = 400

PROMPT = """You rank Hugging Face models for a Korean model-recommendation service.

The user asked a question. Below are candidate models with what their model cards actually say.
Order the candidates by how well each one answers THAT question, best first.

Rules:
- Judge only on the evidence shown. If a card does not show what the question asks for, rank it low.
- When the question asks for models that REPORT a benchmark score, only the "scores:" line counts.
  Those are the scores the service can actually display. Prose that merely names a benchmark, or an
  example that transcribes a sample from it, is not a reported score: rank such a model low, and
  rank "scores: none extracted" lowest. The name appearing in "card:" text proves nothing.
- A question naming a model or family wants that model and its conversions, not similar models.
- A stated constraint (size, context, license, file format) that the card contradicts ranks low.
- Rank every candidate exactly once.

Return JSON only: {"order": [<candidate numbers, best first>]}"""


def wanted(query_type: str | None) -> bool:
    return (query_type or "") in RERANK_TYPES


def _scores(row: Dict[str, Any]) -> List[str]:
    """Only benchmarks the pipeline extracted. Card prose is not a reported score."""
    out: Dict[str, str] = {}
    for item in (row.get("benchmarks") or []):
        name = str(item.get("dataset") or item.get("benchmark") or "").strip().strip("`")
        if not name or name.upper() == "BENCHMARK" or name in out:
            continue
        metric, score = str(item.get("metric") or "").strip(), item.get("score")
        out[name] = " ".join(p for p in (name, metric, None if score is None else str(score)) if p)
        if len(out) >= SCORES_SHOWN:
            break
    return list(out.values())


def card(row: Dict[str, Any]) -> str:
    """One candidate, short enough that RERANK_DEPTH of them fit in a single prompt."""
    facts = [
        f"task={row.get('task') or '?'}",
        f"params={row['parameters_b']}B" if row.get("parameters_b") else "",
        f"context={row['context_length']}" if row.get("context_length") else "",
        f"license={row.get('commercial_use') or '?'}",
        f"formats={','.join((row.get('artifact_formats') or [])[:3])}"
        if row.get("artifact_formats") else "",
    ]
    evidence = re.sub(r"\s+", " ", str(row.get("evidence") or ""))[:CARD_CHARS]
    return (f"{row.get('model_id')}  [{' '.join(f for f in facts if f)}]\n"
            f"  scores: {'; '.join(_scores(row)) or 'none extracted'}\n"
            f"  card: {evidence}")


def _parse(payload: Any, count: int) -> List[int]:
    order = payload.get("order") if isinstance(payload, dict) else None
    if not isinstance(order, list):
        return []
    seen: set[int] = set()
    out: List[int] = []
    for value in order:
        try:
            index = int(value)
        except (TypeError, ValueError):
            continue
        if 1 <= index <= count and index not in seen:
            seen.add(index)
            out.append(index)
    return out


def rerank(
    question: str,
    rows: Sequence[Dict[str, Any]],
    client_factory: Callable[[], Any],
    model: str,
) -> List[Dict[str, Any]]:
    """Reordered rows, or the rows unchanged. Never raises: a worse order beats no answer.

    Candidates the model leaves out keep their incoming order behind the ones it ranked, so a
    partial answer still only moves what it spoke about.
    """
    candidates = list(rows)[:RERANK_DEPTH]
    if len(candidates) < 2:
        return list(rows)
    body = "\n\n".join(f"[{i}] {card(row)}" for i, row in enumerate(candidates, 1))
    try:
        response = client_factory().chat.completions.create(
            model=model,
            temperature=0,
            response_format={"type": "json_object"},
            max_tokens=MAX_TOKENS,
            timeout=TIMEOUT_SECONDS,
            messages=[
                {"role": "system", "content": PROMPT},
                {"role": "user",
                 "content": f"Question (Korean):\n{question}\n\nCandidates:\n{body}"},
            ],
        )
        picks = _parse(json.loads(response.choices[0].message.content or "{}"), len(candidates))
    except Exception as error:  # ranking must never fail the recommendation
        LOGGER.warning("rerank unavailable (%s)", type(error).__name__)
        return list(rows)
    if not picks:
        LOGGER.warning("rerank returned no usable order")
        return list(rows)
    chosen = [candidates[i - 1] for i in picks]
    chosen_ids = {id(row) for row in chosen}
    return chosen + [row for row in candidates if id(row) not in chosen_ids] + list(rows)[RERANK_DEPTH:]
