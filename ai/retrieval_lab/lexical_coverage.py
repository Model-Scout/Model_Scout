#!/usr/bin/env python3
"""lexical_exact 질의가 요구하는 것이 코퍼스에 실제로 있는지 센다.

검색 실험을 하기 전에 "정답이 코퍼스에 존재하는가"를 먼저 확인한다.
0개라면 그 질의는 검색 문제가 아니라 수집 문제이고, 검색 설정을 바꿔도 못 찾는다.

번역 방향은 두 경로로 센다.
  declared  filter_metadata.translation_pairs (모델 카드가 밝힌 값)
  name      model_id 안의 `-en-ko-` 같은 패턴 (선언이 없을 때의 대안)

실행:
    python -m retrieval_lab.lexical_coverage
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Set

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
POOLS = ("core", "low_popularity")

# ISO 코드로 쓰는 언어 이름. 질의가 "중국어를 한국어로"처럼 한국어로 적혀 있다.
LANGUAGE_WORDS = {
    "한국어": "ko", "한글": "ko",
    "영어": "en",
    "일본어": "ja",
    "중국어": "zh",
    "프랑스어": "fr",
    "독일어": "de",
    "스페인어": "es",
    "러시아어": "ru",
}

# model_id 안의 방향 표기. `opus-mt-tc-big-en-ko`, `aihub-ja-ko-translator` 등.
NAME_PAIR_PATTERN = re.compile(
    r"(?:^|[-_./])([a-z]{2})[-_]([a-z]{2})(?=$|[-_./])"
)
ISO_CODES = set(LANGUAGE_WORDS.values())


def load_corpus() -> List[Dict]:
    rows: List[Dict] = []
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    rows.append(json.loads(line))
    return rows


def declared_pairs(row: Dict) -> Set[str]:
    return {str(pair).lower() for pair in (row["filter_metadata"].get("translation_pairs") or [])}


def name_pairs(model_id: str) -> Set[str]:
    """모델 이름에서 방향을 읽는다. 두 조각 모두 아는 언어 코드일 때만 인정한다."""
    found = set()
    for source, target in NAME_PAIR_PATTERN.findall(model_id.lower()):
        if source in ISO_CODES and target in ISO_CODES and source != target:
            found.add(f"{source}-{target}")
    return found


# 형식·런타임 질의가 요구하는 것. artifacts 플래그로 못 보는 형식은 이름·태그로 찾는다.
FORMAT_RULES = {
    "gguf": {"artifact": "gguf", "name": r"gguf"},
    "onnx": {"artifact": "onnx", "name": r"onnx"},
    "mlx": {"variant": "mlx", "name": r"(?:^|[-_./])mlx(?:$|[-_./])"},
    "awq": {"variant": "awq", "name": r"(?:^|[-_./])awq(?:$|[-_./])"},
    "ct2": {"name": r"ct2|faster[-_]whisper|ctranslate"},
    "openvino": {"name": r"openvino|(?:^|[-_./])ov(?:$|[-_./])"},
}

# 형식 질의 7개가 함께 요구하는 task. 형식만 맞고 용도가 다르면 정답이 아니다.
FORMAT_QUERIES = [
    ("sg_h049", "gguf", ("feature-extraction", "sentence-similarity")),
    ("sg_h075", "gguf", ("text-generation",)),
    ("sg_h077", "ct2", ("automatic-speech-recognition",)),
    ("sg_h078", "onnx", ("feature-extraction", "sentence-similarity")),
    ("sg_h079", "mlx", ("text-generation",)),
    ("sg_h080", "awq", ("text-generation",)),
    ("sg_h165", "openvino", ("automatic-speech-recognition",)),
]


def has_format(row: Dict, key: str) -> bool:
    rule = FORMAT_RULES[key]
    meta = row["filter_metadata"]
    if rule.get("artifact") and (meta.get("artifacts") or {}).get(rule["artifact"]):
        return True
    if rule.get("variant") and rule["variant"] in (meta.get("variant_types") or []):
        return True
    return bool(re.search(rule["name"], row["model_id"].lower()))


def report_formats(rows: List[Dict]) -> None:
    print("\n=== 형식·런타임 커버리지 ===")
    print(f"{'질의':<10} {'형식':<9} {'형식만':>7} {'+task':>7}")
    print("-" * 36)
    for query_id, key, tasks in FORMAT_QUERIES:
        by_format = [row for row in rows if has_format(row, key)]
        with_task = [row for row in by_format
                     if row["filter_metadata"].get("primary_task") in tasks]
        print(f"{query_id:<10} {key:<9} {len(by_format):>7} {len(with_task):>7}")

    print("\n신호별 기여 (형식 전체)")
    print(f"{'형식':<9} {'플래그':>7} {'이름':>7} {'합집합':>7}")
    print("-" * 34)
    for key, rule in FORMAT_RULES.items():
        flag = sum(1 for row in rows
                   if (rule.get("artifact") and (row["filter_metadata"].get("artifacts") or {}).get(rule["artifact"]))
                   or (rule.get("variant") and rule["variant"] in (row["filter_metadata"].get("variant_types") or [])))
        name = sum(1 for row in rows if re.search(rule["name"], row["model_id"].lower()))
        union = sum(1 for row in rows if has_format(row, key))
        print(f"{key:<9} {flag:>7} {name:>7} {union:>7}")


# 계열명 질의 5개. 모델 이름과 canonical(선언된 base model)에서 계열을 찾는다.
FAMILY_QUERIES = [
    ("sg_h076", "KoELECTRA", r"koelectra", ("text-classification",)),
    ("sg_h081", "KLUE-RoBERTa", r"klue[-_./]?roberta|roberta[-_./]?klue", ("feature-extraction", "sentence-similarity")),
    ("sg_h082", "Kanana", r"kanana", ("image-text-to-text",)),
    ("sg_h083", "KoBART", r"kobart", ("summarization",)),
    ("sg_h166", "Midm", r"(?:^|[-_./])midm", ("text-generation",)),
]


def report_families(rows: List[Dict]) -> None:
    print("\n=== 계열명 커버리지 ===")
    print(f"{'질의':<10} {'계열':<14} {'이름':>6} {'canonical':>10} {'합집합':>7} {'+task':>7}")
    print("-" * 60)
    for query_id, label, pattern, tasks in FAMILY_QUERIES:
        regex = re.compile(pattern)
        by_name, by_canonical, union = [], [], []
        for row in rows:
            name_hit = bool(regex.search(row["model_id"].lower()))
            canonical = (row["filter_metadata"].get("canonical_model_id") or "").lower()
            canonical_hit = bool(regex.search(canonical))
            if name_hit:
                by_name.append(row)
            if canonical_hit:
                by_canonical.append(row)
            if name_hit or canonical_hit:
                union.append(row)
        with_task = [row for row in union
                     if row["filter_metadata"].get("primary_task") in tasks]
        print(f"{query_id:<10} {label:<14} {len(by_name):>6} {len(by_canonical):>10} "
              f"{len(union):>7} {len(with_task):>7}")


def main() -> None:
    rows = load_corpus()
    print(f"코퍼스 {len(rows):,}개\n")

    declared = Counter()
    by_name = Counter()
    for row in rows:
        for pair in declared_pairs(row):
            declared[pair] += 1
        for pair in name_pairs(row["model_id"]):
            by_name[pair] += 1

    # lexical_exact 번역 질의 10개가 요구하는 방향
    wanted = ["ja-ko", "en-ko", "ko-en", "zh-ko", "ko-zh", "ko-fr", "ko-de"]

    print(f"{'방향':<8} {'선언':>6} {'이름':>6} {'합집합':>7}")
    print("-" * 32)
    for pair in wanted:
        union = {row["model_id"] for row in rows
                 if pair in declared_pairs(row) or pair in name_pairs(row["model_id"])}
        print(f"{pair:<8} {declared[pair]:>6} {by_name[pair]:>6} {len(union):>7}")

    print(f"\n선언된 방향 전체: {sum(declared.values())}개 (모델 {sum(1 for r in rows if declared_pairs(r))}개)")
    print(f"이름에서 읽은 방향 전체: {sum(by_name.values())}개 (모델 {sum(1 for r in rows if name_pairs(r['model_id']))}개)")
    print("\n이름으로만 찾은 상위 방향:", by_name.most_common(10))

    report_formats(rows)
    report_families(rows)


if __name__ == "__main__":
    main()
