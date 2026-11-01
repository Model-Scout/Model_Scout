#!/usr/bin/env python3
"""Deterministic extraction and safe matching for model-card benchmarks.

Numeric results are used for ranking only when their benchmark identity is
unambiguous. Everything else is retained as a mention for audit/display and
never affects recommendation order.
"""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

import yaml


BENCHMARK_VERSION = 1
KNOWN_BENCHMARK_WORDS = (
    "benchmark",
    "evaluation",
    "eval",
    "performance",
    "result",
    "results",
    "mteb",
    "beir",
    "miracl",
    "glue",
    "superglue",
    "squad",
    "korquad",
    "xsum",
    "cnn/dailymail",
    "librispeech",
    "common voice",
    "fleurs",
    "bleu",
    "rouge",
    "bertscore",
    "wer",
    "cer",
)
# Prefer concrete benchmark families over generic words such as ``eval``.
# A Model Index result commonly has ``task: Retrieval`` and
# ``dataset: MTEB ArguAna``; using the task first would otherwise label the
# benchmark as ``EVAL`` and make an exact query unnecessarily ambiguous.
SPECIFIC_BENCHMARK_WORDS = (
    "mteb",
    "beir",
    "miracl",
    "superglue",
    "glue",
    "squad",
    "korquad",
    "xsum",
    "cnn/dailymail",
    "librispeech",
    "common voice",
    "fleurs",
)
GENERIC_BENCHMARK_WORDS = (
    "benchmark",
    "evaluation",
    "eval",
    "performance",
    "result",
    "results",
)
NON_BENCHMARK_LABELS = {
    "architecture",
    "architectures",
    "parameter",
    "parameters",
    "parameter count",
    "model size",
    "embedding dimension",
    "embedding dimensions",
    "dimension",
    "dimensions",
    "vector dimension",
    "max tokens",
    "context length",
    "quantization",
    "quantized",
    "format",
    "dtype",
    "memory",
    "model memory",
}
METRIC_ALIASES = {
    "acc": "accuracy",
    "accuracy": "accuracy",
    "ap": "average_precision",
    "average_precision": "average_precision",
    "f1": "f1",
    "bleu": "bleu",
    "rouge": "rouge",
    "rouge-1": "rouge-1",
    "rouge-2": "rouge-2",
    "rouge-l": "rouge-l",
    "bertscore": "bertscore",
    "wer": "wer",
    "cer": "cer",
    "mrr": "mrr",
    "map": "map",
    "ndcg": "ndcg",
    "precision": "precision",
    "recall": "recall",
    "spearman": "spearman",
    "pearson": "pearson",
    "score": "score",
}
LOWER_IS_BETTER = {"wer", "cer", "loss", "latency", "runtime"}
QUANTIZED_RE = re.compile(
    r"(?:gguf|gptq|awq|bnb|bitsandbytes|mlx|onnx|int[248]|fp8|q[2-8](?:[_-][a-z0-9]+)?|\b[248]-?bit\b)",
    re.IGNORECASE,
)
NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?%?")


def _text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple, set)):
        return " ".join(_text(item) for item in value)
    if isinstance(value, dict):
        return " ".join(f"{_text(k)} {_text(v)}" for k, v in value.items())
    return str(value)


def _norm(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", " ", _text(value).casefold()).strip()


def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _number(value: Any) -> Optional[float]:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = re.sub(r"[*_`~]", "", _text(value)).strip().replace(",", "")
    if not re.fullmatch(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?%?", text):
        return None
    try:
        return float(text.rstrip("%"))
    except ValueError:
        return None


def normalize_metric(value: Any) -> str:
    normalized = _norm(value).replace(" ", "-")
    return METRIC_ALIASES.get(normalized, normalized or "score")


def metric_direction(metric: str) -> str:
    return "lower_is_better" if metric in LOWER_IS_BETTER else "higher_is_better"


def _is_non_benchmark_label(value: Any) -> bool:
    """Return true for model metadata fields that are not evaluation sets."""
    normalized = _norm(value)
    return normalized in {_norm(label) for label in NON_BENCHMARK_LABELS}


def extract_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, ""
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}, ""
    raw = "\n".join(lines[1:end])
    try:
        value = yaml.safe_load(raw) or {}
    except Exception:
        return {}, raw
    return value if isinstance(value, dict) else {}, raw


def _benchmark_name(dataset: Any, heading: str = "") -> str:
    dataset_text = _text(dataset)
    dataset_lower = dataset_text.casefold()
    heading_lower = _text(heading).casefold()
    # Dataset names carry the strongest benchmark identity. Search them
    # before task/heading text and prefer specific families over generic
    # ``evaluation`` labels.
    for known in SPECIFIC_BENCHMARK_WORDS:
        if known in dataset_lower:
            return known.upper()
    for known in SPECIFIC_BENCHMARK_WORDS:
        if known in heading_lower:
            return known.upper()
    combined = f"{dataset_lower} {heading_lower}"
    for known in GENERIC_BENCHMARK_WORDS:
        if known in combined:
            return known.upper()
    dataset_parts = dataset_text.split()
    if dataset_parts:
        return dataset_parts[0]
    heading_parts = _text(heading).split()
    if heading_parts:
        return heading_parts[0]
    return "unknown"


def _source_variant(row: Dict[str, Any]) -> Tuple[str, bool]:
    model_id = _text(row.get("model_id"))
    model = row.get("model") or {}
    quantization = row.get("quantization") or {}
    quantized = bool(quantization.get("enabled")) or bool(QUANTIZED_RE.search(model_id))
    return ("quantized" if quantized else "unquantized"), quantized


def _model_name_matches_source(row: Dict[str, Any], model_name: str) -> bool:
    """Check whether a reported table/model-index name identifies this row."""

    if not model_name:
        return False
    source_id = _norm(row.get("model_id"))
    raw_source = _text(row.get("model_id"))
    source_leaf = _norm(raw_source.rsplit("/", 1)[-1]) if raw_source else ""
    reported = _norm(model_name)
    if not reported:
        return False
    return reported == source_id or reported == source_leaf or reported in source_id or source_leaf in reported


def _variant_name_is_explicitly_safe(
    row: Dict[str, Any], model_name: str, model_explicit: bool, model_matches_source: bool
) -> bool:
    """Require a quantized card to name the quantized artifact itself.

    A table can mention the base checkpoint while being stored in a GGUF,
    GPTQ, AWQ, MLX, or ONNX repository.  Base-name overlap alone is therefore
    insufficient evidence that the reported score belongs to this artifact.
    """
    quantization = row.get("quantization") or {}
    model_id = _text(row.get("model_id"))
    quantized = bool(quantization.get("enabled")) or bool(QUANTIZED_RE.search(model_id))
    if not quantized:
        return bool(model_matches_source)
    if not model_explicit or not model_matches_source:
        return False
    return bool(QUANTIZED_RE.search(_text(model_name)))


def _excerpt(raw: str, needle: Any) -> str:
    target = _text(needle)
    if target:
        position = raw.casefold().find(target.casefold())
        if position >= 0:
            start = max(0, position - 180)
            end = min(len(raw), position + len(target) + 220)
            return raw[start:end].strip()
    return raw[:450].strip()


def _base_record(
    row: Dict[str, Any],
    source_path: str,
    source_hash: str,
    source_type: str,
    evidence_ref: str,
    quote: str,
    benchmark: str,
    dataset: str,
    metric: str,
    score: Optional[float],
    model_name: str,
    split: str = "",
    config: str = "",
    revision: str = "",
    model_explicit: bool = False,
) -> Dict[str, Any]:
    variant_kind, quantized = _source_variant(row)
    numeric = score is not None
    model_matches_source = _model_name_matches_source(row, model_name)
    # Quantized rows are not comparable unless the source explicitly identifies
    # the reported variant. This prevents base-model scores leaking to variants.
    variant_safe = _variant_name_is_explicitly_safe(
        row, model_name, model_explicit, model_matches_source
    )
    ranking_eligible = bool(numeric and variant_safe and model_matches_source and benchmark and metric)
    return {
        "benchmark_version": BENCHMARK_VERSION,
        "benchmark": benchmark,
        "dataset": dataset,
        "metric": metric,
        "score": score,
        "higher_is_better": metric_direction(metric) == "higher_is_better",
        "model_name": model_name or row.get("model_id"),
        "model_name_explicit": model_explicit,
        "model_name_matches_source": model_matches_source,
        "split": split,
        "config": config,
        "revision": revision,
        "source_type": source_type,
        "source_readme_path": source_path,
        "source_readme_sha256": source_hash,
        "evidence_ref": evidence_ref,
        "supporting_quote": quote,
        "self_reported": True,
        "variant_kind": variant_kind,
        "variant_safe": variant_safe,
        "ranking_eligible": ranking_eligible,
        "comparability": "safe_same_source" if ranking_eligible else (
            "variant_ambiguous" if numeric and not variant_safe else "mention_only"
        ),
    }


def _model_index_records(
    row: Dict[str, Any],
    text: str,
    frontmatter: Dict[str, Any],
    path: str,
    sha: str,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    results: List[Dict[str, Any]] = []
    mentions: List[Dict[str, Any]] = []
    model_index = frontmatter.get("model-index") or []
    if isinstance(model_index, dict):
        model_index = [model_index]

    for model_index_number, model_item in enumerate(model_index):
        if not isinstance(model_item, dict):
            continue
        model_name = _text(model_item.get("name"))
        raw_results = model_item.get("results") or []
        for result_number, result in enumerate(raw_results):
            if not isinstance(result, dict):
                continue
            task = result.get("task") or {}
            dataset = result.get("dataset") or {}
            if isinstance(dataset, dict):
                dataset_name = _text(dataset.get("name") or dataset.get("type"))
            else:
                dataset_name = _text(dataset)
            task_name = (
                _text(task.get("name") or task.get("type"))
                if isinstance(task, dict)
                else _text(task)
            )
            benchmark = _benchmark_name(dataset_name, task_name)
            if _is_non_benchmark_label(dataset_name):
                mentions.append(
                    {
                        "benchmark": benchmark,
                        "dataset": dataset_name,
                        "source_type": "model_index_yaml",
                        "reason": "metadata_field_not_benchmark",
                        "source_readme_path": path,
                        "source_readme_sha256": sha,
                        "evidence_ref": (
                            f"readme:model-index[{model_index_number}]"
                            f".results[{result_number}]"
                        ),
                        "supporting_quote": _excerpt(text, dataset_name),
                    }
                )
                continue
            split = _text(result.get("split"))
            config = _text(result.get("config"))
            revision = _text(result.get("revision"))
            metrics = result.get("metrics") or []
            if isinstance(metrics, dict):
                metrics = [metrics]
            if not metrics:
                mentions.append(
                    {
                        "benchmark": benchmark,
                        "dataset": dataset_name,
                        "source_type": "model_index_yaml",
                        "source_readme_path": path,
                        "source_readme_sha256": sha,
                        "evidence_ref": (
                            f"readme:model-index[{model_index_number}]"
                            f".results[{result_number}]"
                        ),
                        "supporting_quote": _excerpt(text, dataset_name),
                    }
                )
                continue
            for metric_number, metric_item in enumerate(metrics):
                if not isinstance(metric_item, dict):
                    continue
                metric = normalize_metric(metric_item.get("type"))
                score = _number(metric_item.get("value"))
                evidence_ref = (
                    f"readme:model-index[{model_index_number}]"
                    f".results[{result_number}].metrics[{metric_number}]"
                )
                if score is None:
                    mentions.append(
                        {
                            "benchmark": benchmark,
                            "dataset": dataset_name,
                            "metric": metric,
                            "source_type": "model_index_yaml",
                            "reason": "score_missing_or_non_numeric",
                            "source_readme_path": path,
                            "source_readme_sha256": sha,
                            "evidence_ref": evidence_ref,
                            "supporting_quote": _excerpt(
                                text, metric_item.get("type")
                            ),
                        }
                    )
                    continue
                quote = _excerpt(text, metric_item.get("value"))
                results.append(
                    _base_record(
                        row,
                        path,
                        sha,
                        "model_index_yaml",
                        evidence_ref,
                        quote,
                        benchmark,
                        dataset_name,
                        metric,
                        score,
                        model_name,
                        split,
                        config,
                        revision,
                        model_explicit=bool(model_name),
                    )
                )
    return results, mentions


def _split_pipe(line: str) -> List[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|") and not value.endswith("\\|"):
        value = value[:-1]
    cells: List[str] = []
    current: List[str] = []
    escaped = False
    for char in value:
        if char == "|" and not escaped:
            cells.append("".join(current).strip())
            current = []
            continue
        if char == "\\" and not escaped:
            escaped = True
            current.append(char)
            continue
        escaped = False
        current.append(char)
    cells.append("".join(current).strip())
    return cells


def _separator_row(cells: Sequence[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def _benchmark_context(value: str) -> bool:
    lowered = value.casefold()
    return any(word in lowered for word in KNOWN_BENCHMARK_WORDS)


def _metric_header(value: str) -> Optional[str]:
    lowered = _norm(value).replace(" ", "-")
    for alias, metric in METRIC_ALIASES.items():
        if alias in lowered or metric in lowered:
            return metric
    return None


def _table_records(row: Dict[str, Any], text: str, path: str, sha: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    lines = text.splitlines()
    results: List[Dict[str, Any]] = []
    mentions: List[Dict[str, Any]] = []
    headings: List[str] = []
    index = 0
    table_number = 0
    while index < len(lines) - 1:
        heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", lines[index])
        if heading_match:
            level = len(heading_match.group(1))
            headings = headings[: level - 1] + [heading_match.group(2).strip()]
            index += 1
            continue
        if "|" not in lines[index] or "|" not in lines[index + 1]:
            index += 1
            continue
        header = _split_pipe(lines[index])
        separator = _split_pipe(lines[index + 1])
        if len(header) < 2 or len(header) != len(separator) or not _separator_row(separator):
            index += 1
            continue
        start_line = index + 1
        index += 2
        body: List[Tuple[int, List[str], str]] = []
        while index < len(lines) and "|" in lines[index] and lines[index].strip():
            cells = _split_pipe(lines[index])
            if len(cells) != len(header):
                break
            body.append((index + 1, cells, lines[index]))
            index += 1
        table_text = " ".join(headings + header)
        table_number += 1
        if not _benchmark_context(table_text):
            continue
        # Explicitly exclude metadata tables that happen to contain numbers.
        if any(re.search(r"architecture|quantization|format|dtype|parameter|context|memory", h, re.I) for h in header) and not any(_metric_header(h) for h in header):
            continue
        benchmark = _benchmark_name(" ".join(header), " ".join(headings))
        metric_columns = [(column, _metric_header(name) or "score") for column, name in enumerate(header)]
        model_columns = [column for column, name in enumerate(header) if _norm(name) in {"model", "model-name", "model-id", "system", "checkpoint"}]
        if not any(_metric_header(name) for name in header):
            numeric_columns = []
            # In comparison tables the first column is commonly the dataset or
            # evaluation case, while the remaining headers are model names.
            # Do not attribute every comparator score to the current model.
            start_column = 1 if not model_columns else 0
            for column, name in enumerate(header[start_column:], start=start_column):
                if any(_number(cells[column]) is not None for _, cells, _ in body):
                    numeric_columns.append((column, "score"))
            metric_columns = numeric_columns
        if not metric_columns:
            mentions.append({
                "benchmark": benchmark,
                "dataset": "",
                "source_type": "markdown_table",
                "source_readme_path": path,
                "source_readme_sha256": sha,
                "evidence_ref": f"readme:table[{table_number}]",
                "supporting_quote": "\n".join(lines[start_line - 1 : min(len(lines), start_line + 8)]),
            })
            continue
        for row_number, cells, raw_row in body:
            explicit_model = bool(model_columns)
            if model_columns:
                model_name = cells[model_columns[0]]
            elif len(body) == 1 and len(metric_columns) == 1:
                model_name = row.get("model_id") or ""
            else:
                model_name = ""
            for column, metric in metric_columns:
                score = _number(cells[column])
                if score is None:
                    continue
            if model_columns:
                dataset = header[column] if not _metric_header(header[column]) else ""
                # In a Model | ... | Score table the row's first cell is the
                # model identity. The score-column header is a metric label,
                # never the reported model name.
                reported_model = cells[model_columns[0]]
                model_is_explicit = True
            elif len(body) == 1 and len(metric_columns) == 1:
                dataset = ""
                reported_model = model_name
                model_is_explicit = True
            else:
                dataset = cells[0]
                reported_model = header[column]
                model_is_explicit = True
            if _is_non_benchmark_label(dataset):
                mentions.append({
                    "benchmark": benchmark,
                    "dataset": dataset,
                    "source_type": "markdown_table",
                    "reason": "metadata_field_not_benchmark",
                    "source_readme_path": path,
                    "source_readme_sha256": sha,
                    "evidence_ref": f"readme:table[{table_number}].row[{row_number}].column[{column + 1}]",
                    "supporting_quote": f"{lines[start_line - 1]}\n{raw_row}",
                })
                continue
            evidence_ref = f"readme:table[{table_number}].row[{row_number}].column[{column + 1}]"
            results.append(_base_record(
                row, path, sha, "markdown_table", evidence_ref,
                f"{lines[start_line - 1]}\n{raw_row}", benchmark,
                dataset, metric, score, reported_model,
                model_explicit=model_is_explicit,
            ))
    return results, mentions


def extract_benchmarks(row: Dict[str, Any], readme_text: str, readme_path: str) -> Dict[str, Any]:
    source_hash = _digest(readme_text)
    if not readme_text:
        return {
            "benchmark_version": BENCHMARK_VERSION,
            "readme_available": False,
            "readme_path": readme_path,
            "readme_sha256": None,
            "results": [],
            "mentions": [],
            "summary": {
                "numeric_results": 0,
                "ranking_eligible": 0,
                "mentions_only": 0,
                "quantized_ambiguous": 0,
            },
        }
    frontmatter, _ = extract_frontmatter(readme_text)
    structured, structured_mentions = _model_index_records(row, readme_text, frontmatter, readme_path, source_hash)
    tables, table_mentions = _table_records(row, readme_text, readme_path, source_hash)
    seen = set()
    results: List[Dict[str, Any]] = []
    mentions: List[Dict[str, Any]] = structured_mentions + table_mentions
    for record in structured + tables:
        if record.get("score") is None:
            mention = dict(record)
            mention.pop("score", None)
            mention.pop("ranking_eligible", None)
            mention["reason"] = "score_missing_or_non_numeric"
            mentions.append(mention)
            continue
        key = (
            record.get("benchmark"), record.get("dataset"), record.get("metric"),
            record.get("score"), record.get("split"), record.get("evidence_ref"),
        )
        if key not in seen:
            seen.add(key)
            results.append(record)
    return {
        "benchmark_version": BENCHMARK_VERSION,
        "readme_available": bool(readme_text),
        "readme_path": readme_path,
        "readme_sha256": source_hash if readme_text else None,
        "results": results,
        "mentions": mentions,
        "summary": {
            "numeric_results": sum(1 for record in results if record.get("score") is not None),
            "ranking_eligible": sum(1 for record in results if record.get("ranking_eligible")),
            "mentions_only": len(mentions),
            "quantized_ambiguous": sum(1 for record in results if record.get("comparability") == "variant_ambiguous"),
        },
    }


def benchmark_matches(record: Dict[str, Any], spec: Dict[str, Any]) -> bool:
    if not record.get("ranking_eligible"):
        return False
    for field in ("benchmark", "dataset", "metric", "split", "config"):
        wanted = spec.get(field)
        if wanted and _norm(record.get(field)) != _norm(wanted):
            return False
    return True


def benchmark_key(record: Dict[str, Any]) -> Tuple[str, str, str, str, str]:
    return tuple(_norm(record.get(field)) for field in ("benchmark", "dataset", "metric", "split", "config"))


def match_benchmark_records(row: Dict[str, Any], spec: Dict[str, Any]) -> List[Dict[str, Any]]:
    metadata = row.get("benchmark_metadata") or {}
    return [record for record in metadata.get("results", []) if benchmark_matches(record, spec)]
