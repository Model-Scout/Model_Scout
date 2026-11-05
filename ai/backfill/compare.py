#!/usr/bin/env python3
"""기존 Stage 2와 백필 Stage 2를 비교한다. 설득 자료이자 검증 도구다.

세 가지를 본다.

    1. 커버리지 — 필드별로 몇 개가 채워졌나
    2. 안전성  — 기존 값이 덮어써지지 않았나 (빈칸 채우기여야 한다)
    3. 실익    — 실제 질의에서 후보가 몇 개 늘어나나

3번이 핵심이다. "데이터가 채워졌다"가 아니라 "사용자가 찾을 수 있게 됐다"를
보여야 한다. 하드 필터를 그대로 써서 같은 질의를 전후에 돌린다.

    python ai/backfill/compare.py
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

HERE = Path(__file__).resolve().parent
AI_ROOT = HERE.parent
DATA_DIR = AI_ROOT / "data"
OUT_DIR = HERE / "out"
REPORT_PATH = HERE / "reports" / "comparison.md"

POOLS = ("core", "low_popularity")

# 사용자가 실제로 물어볼 법한 수치 조건 질의. 하드 필터 키로만 구성한다.
QUERIES = [
    ("3B 이하 한국어 요약 모델", {"tasks": ["summarization"], "korean_required": True,
                                 "max_parameters_billion": 3.0, "require_known_parameters": True}),
    ("1B 이하 한국어 번역 모델", {"tasks": ["translation"], "korean_required": True,
                                 "max_parameters_billion": 1.0, "require_known_parameters": True}),
    ("8B 이하 한국어 LLM", {"tasks": ["text-generation"], "korean_required": True,
                           "max_parameters_billion": 8.0, "require_known_parameters": True}),
    ("1B 이하 한국어 음성 인식", {"tasks": ["automatic-speech-recognition"], "korean_required": True,
                                "max_parameters_billion": 1.0, "require_known_parameters": True}),
    ("3B 이하 한국어 이미지-텍스트", {"tasks": ["image-text-to-text"], "korean_required": True,
                                   "max_parameters_billion": 3.0, "require_known_parameters": True}),
    ("컨텍스트 32768 이상 한국어 LLM", {"tasks": ["text-generation"], "korean_required": True,
                                      "min_context_length": 32768, "require_known_context": True}),
    ("컨텍스트 131072 이상 한국어 번역", {"tasks": ["translation"], "korean_required": True,
                                        "min_context_length": 131072, "require_known_context": True}),
]


def validator() -> Any:
    sys.path.insert(0, str(AI_ROOT))
    spec = importlib.util.spec_from_file_location(
        "backfill_validator", AI_ROOT / "05_validate_retrieval.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_stage2(directory: Path) -> Dict[str, Dict[str, Any]]:
    rows: Dict[str, Dict[str, Any]] = {}
    for pool in POOLS:
        path = directory / f"hf_models_stage2_{pool}.jsonl"
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    row = json.loads(line)
                    row["_pool"] = pool
                    rows[row["model_id"]] = row
    return rows


def as_filter_row(row: Dict[str, Any]) -> Dict[str, Any]:
    """하드 필터가 읽는 모양으로 Stage 2 행을 옮긴다 (04_build_embeddings 와 같은 형태)."""
    model = row.get("model") or {}
    language = row.get("language") or {}
    korean = language.get("korean")
    verified = korean.get("verified") if isinstance(korean, dict) else korean
    task = row.get("task") or {}
    popularity = (row.get("popularity") or {}).get("stage1") or {}
    return {
        "model_id": row["model_id"],
        "source_pool": row["_pool"],
        "task": {"primary": task.get("primary"), "matched": task.get("matched")},
        "filter_metadata": {
            "parameter_count_billion": model.get("parameter_count_billion"),
            "context_length": model.get("context_length"),
            "korean_verified": verified,
            "popularity_tier": popularity.get("tier"),
            "primary_task": task.get("primary"),
            "matched_tasks": task.get("matched"),
        },
    }


def main() -> None:
    before = read_stage2(DATA_DIR)
    after = read_stage2(OUT_DIR)
    module = validator()

    lines: List[str] = []
    out = lines.append

    out("# 백필 전후 비교")
    out("")
    out(f"- 코퍼스 {len(before)}행 (Stage 2)")
    out("- 기존 `ai/data/` 는 읽기만 했고, 백필 결과는 `ai/backfill/out/` 에만 썼다")
    out("")

    out("## 1. 커버리지")
    out("")
    out("| 필드 | 전 | 후 | 증가 |")
    out("|---|---:|---:|---:|")
    checks = [
        ("parameter_count", lambda r: (r.get("model") or {}).get("parameter_count")),
        ("context_length", lambda r: (r.get("model") or {}).get("context_length")),
        ("architectures", lambda r: (r.get("model") or {}).get("architectures")),
        ("model.type", lambda r: (r.get("model") or {}).get("type")),
        ("license", lambda r: r.get("license")),
        ("hardware VRAM 추정", lambda r: any(
            (((r.get("hardware") or {}).get("weights_only")) or {}).get(key)
            for key in ("fp16_gib", "int8_gib", "int4_gib"))),
        ("disk_size_gib (신규)", lambda r: (r.get("model") or {}).get("disk_size_gib")),
    ]
    coverage: Dict[str, Dict[str, int]] = {}
    for name, getter in checks:
        n_before = sum(1 for row in before.values() if getter(row) not in (None, "", [], {}, False))
        n_after = sum(1 for row in after.values() if getter(row) not in (None, "", [], {}, False))
        coverage[name] = {"before": n_before, "after": n_after}
        total = len(before)
        out(f"| {name} | {n_before} ({n_before / total * 100:.1f}%) | "
            f"{n_after} ({n_after / total * 100:.1f}%) | **+{n_after - n_before}** |")
    out("")

    out("## 2. 안전성 — 기존 값이 덮어써졌나")
    out("")
    overwritten: List[str] = []
    for model_id, row_before in before.items():
        row_after = after.get(model_id)
        if row_after is None:
            continue
        for name, getter in checks[:5]:
            value_before = getter(row_before)
            if value_before in (None, "", [], {}):
                continue
            if getter(row_after) != value_before:
                overwritten.append(f"{model_id}.{name}")
    if overwritten:
        out(f"❌ **{len(overwritten)}건이 덮어써졌다.** 빈칸 채우기여야 하므로 버그다.")
        for item in overwritten[:20]:
            out(f"  - `{item}`")
    else:
        out("✅ **0건.** 기존 값은 하나도 바뀌지 않았다. 빈칸만 채웠다.")
    out("")

    out("## 3. 실익 — 실제 질의에서 후보가 몇 개 늘어나나")
    out("")
    out("하드 필터(`05_validate_retrieval.hard_filter`)를 그대로 써서 같은 질의를 전후에 돌렸다.")
    out("")
    out("| 질의 | 전 | 후 | 증가 |")
    out("|---|---:|---:|---:|")
    rows_before = [as_filter_row(row) for row in before.values()]
    rows_after = [as_filter_row(row) for row in after.values()]
    gains: Dict[str, Dict[str, int]] = {}
    for label, query in QUERIES:
        query = dict(query)
        query.setdefault("pools", list(POOLS))
        n_before = sum(1 for row in rows_before if module.hard_filter(row, query)[0])
        n_after = sum(1 for row in rows_after if module.hard_filter(row, query)[0])
        gains[label] = {"before": n_before, "after": n_after}
        mark = f"**+{n_after - n_before}**" if n_after > n_before else str(n_after - n_before)
        out(f"| {label} | {n_before} | {n_after} | {mark} |")
    out("")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print(f"\n→ {REPORT_PATH}")


if __name__ == "__main__":
    main()
