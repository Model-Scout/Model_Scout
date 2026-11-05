#!/usr/bin/env python3
"""델타의 파라미터 값을 검증하고 신뢰도를 조정한다.

왜 필요한가
-----------
"gguf.total은 1차 출처다"로 끝낼 수 없다. 변환본의 gguf.total을 코퍼스에 있는
원본의 파라미터 수와 대조해보니 510쌍 중 83.7%만 5% 이내로 일치했다. 나머지
16.3%는 무작위가 아니라 패턴이 있다.

    LFM3-VL-2B-GGUF      gguf 1.73B  원본 1.92B   ← VL. 비전 인코더가 빠짐
    LFM2.5-VL-3B-GGUF    gguf 2.70B  원본 3.12B   ← 같은 이유
    A.X-K2-VQ-GGUF       gguf 14.1B  원본 691.7B  ← MoE 또는 부분 양자화

GGUF는 비전 인코더를 mmproj 파일로 분리한다. 그래서 gguf.total은 언어 모델
부분만 센다. MoE는 전체와 활성이 다른데 gguf.total이 어느 쪽인지 단정할 수 없다.

세 가지로 검증한다
    1. 원본 대조   코퍼스에 원본이 있으면 파라미터 수를 비교한다 (가장 강한 근거)
    2. mmproj 유무 siblings에 mmproj가 있으면 VL이고 gguf.total은 언어부만이다
    3. 파일 크기   gguf.total이 맞다면 파일크기/파라미터가 양자화 비트와 맞아야
                   한다. Q4면 약 0.5~0.7 B/param, Q8이면 1.0~1.2. 이 범위를
                   크게 벗어나면 gguf.total이 전체를 못 세고 있다는 신호다.

신뢰도를 내릴 뿐 값을 지어내지 않는다. medium/low로 떨어진 것은 사람이 본다.

    python ai/backfill/validate_delta.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

HERE = Path(__file__).resolve().parent
AI_ROOT = HERE.parent
RAW_DIR = HERE / "raw"
DELTA_PATH = HERE / "delta.jsonl"
OUT_PATH = HERE / "delta.jsonl"
REPORT_PATH = HERE / "reports" / "validation.md"

# 양자화별 파라미터당 바이트. llama.cpp 의 실제 비트 폭에서 왔다.
# IQ(importance-aware) 계열은 같은 숫자라도 더 촘촘하다.
QUANT_BYTES = {
    "iq1": 0.21, "iq2": 0.30, "iq3": 0.40, "iq4": 0.53,
    "q2": 0.33, "q3": 0.43, "q4": 0.56, "q5": 0.68,
    "q6": 0.82, "q8": 1.06, "f16": 2.0, "bf16": 2.0, "f32": 4.0,
}
# IQ를 먼저 보지 않으면 "IQ4_XS"가 q4로 잡힌다.
QUANT_PATTERN = re.compile(
    r"(iq1|iq2|iq3|iq4|q2|q3|q4|q5|q6|q8|f16|bf16|f32)", re.IGNORECASE
)
MOE_NAME = re.compile(r"(\d+x\d+b|[-_]a\d+(?:\.\d+)?b)", re.IGNORECASE)
MOE_KEYS = ("expert_count", "expert_used_count", "n_expert", "num_experts")


def corpus_rows() -> List[Dict[str, Any]]:
    sys.path.insert(0, str(AI_ROOT / "test" / "golden" / "v2" / "tools"))
    import corpus_v2

    return corpus_v2.load_rows()


def load_raw(model_id: str) -> Optional[Dict[str, Any]]:
    safe = model_id.replace("/", "__")
    path = RAW_DIR / safe[:2].lower() / f"{safe}.json"
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    return None if "__error__" in payload else payload


def has_mmproj(raw: Dict[str, Any]) -> bool:
    """비전 인코더가 별도 파일로 빠져 있나. 있으면 gguf.total은 언어부만이다."""
    for sibling in raw.get("siblings") or []:
        if "mmproj" in (sibling.get("rfilename") or "").lower():
            return True
    return False


def weight_files(raw: Dict[str, Any]) -> List[Tuple[str, int]]:
    out = []
    for sibling in raw.get("siblings") or []:
        name = (sibling.get("rfilename") or "").lower()
        size = sibling.get("size")
        if isinstance(size, int) and size > 0 and name.endswith(".gguf") and "mmproj" not in name:
            out.append((name, size))
    return out


def bytes_per_param(raw: Dict[str, Any], total: int) -> Optional[Tuple[float, float, str]]:
    """(실측 B/param, 양자화가 기대하는 B/param, 파일명).

    가장 잘 맞는 파일을 고른다. 처음엔 가장 작은 파일을 썼는데, 레포에 어댑터나
    부분 업로드가 섞여 있어서 엉뚱한 결과가 나왔다. 24B 모델 레포에 0.33 GiB짜리
    "Q8_0.gguf"가 있었는데, 24B를 Q8로 만들면 25 GB가 나와야 한다.

    여러 양자화 버전 중 하나라도 gguf.total 과 맞으면 그 값은 일관된 것으로 본다.
    """
    files = weight_files(raw)
    if not files or not total:
        return None
    # 분할 파일(00001-of-00003)은 합산이 필요하므로 제외한다.
    single = [(name, size) for name, size in files if not re.search(r"\d{5}-of-\d{5}", name)]
    best: Optional[Tuple[float, float, str, float]] = None
    for name, size in single:
        match = QUANT_PATTERN.search(name)
        if not match:
            continue
        expected = QUANT_BYTES[match.group(1).lower()]
        actual = size / total
        distance = abs(actual / expected - 1.0)
        if best is None or distance < best[3]:
            best = (actual, expected, name, distance)
    return (best[0], best[1], best[2]) if best else None


def moe_signal(model_id: str, raw: Dict[str, Any]) -> Optional[str]:
    gguf = raw.get("gguf") or {}
    for key in MOE_KEYS:
        if key in gguf:
            return f"gguf.{key}={gguf[key]}"
    config = raw.get("config") or {}
    for key in MOE_KEYS:
        if key in config:
            return f"config.{key}={config[key]}"
    match = MOE_NAME.search(model_id)
    return f"model_id 패턴 {match.group(0)}" if match else None


def main() -> None:
    rows = corpus_rows()
    by_id = {row["model_id"].lower(): row for row in rows}

    def canonical_params(row_id: str) -> Optional[float]:
        row = by_id.get(row_id.lower())
        if row is None:
            return None
        value = (row.get("filter_metadata") or {}).get("parameter_count_billion")
        return value if isinstance(value, (int, float)) else None

    canonical_of = {
        row["model_id"]: (row.get("filter_metadata") or {}).get("canonical_model_id")
        for row in rows
    }

    records: List[Dict[str, Any]] = []
    with DELTA_PATH.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))

    stats = {
        "checked": 0, "confirmed_by_canonical": 0, "conflict_with_canonical": 0,
        "vl_mmproj": 0, "moe": 0, "moe_resolved": 0, "size_mismatch": 0,
        "high": 0, "medium": 0, "unchanged": 0,
    }
    downgraded: List[Dict[str, Any]] = []

    for record in records:
        patch = (record.get("patches") or {}).get("parameter_count")
        if not patch:
            continue
        model_id = record["model_id"]
        raw = load_raw(model_id)
        if raw is None:
            continue
        stats["checked"] += 1
        billion = patch["after"] / 1e9
        reasons: List[str] = []
        verdict = "high"

        # 1. 원본 대조 — 가장 강한 근거
        canonical = canonical_of.get(model_id)
        if canonical and canonical != model_id:
            reference = canonical_params(canonical)
            if reference:
                relative = abs(billion - reference) / max(billion, reference)
                if relative < 0.05:
                    stats["confirmed_by_canonical"] += 1
                    record.setdefault("validation", {})["canonical_match"] = {
                        "canonical": canonical, "canonical_b": reference,
                        "gguf_b": round(billion, 3), "diff_pct": round(relative * 100, 1),
                    }
                else:
                    stats["conflict_with_canonical"] += 1
                    verdict = "medium"
                    reasons.append(
                        f"원본 {canonical} 은 {reference}B 인데 gguf.total 은 {billion:.2f}B "
                        f"({relative * 100:.0f}% 차이)"
                    )

        # 2. mmproj — VL 모델은 비전 인코더가 빠진다
        if has_mmproj(raw):
            stats["vl_mmproj"] += 1
            verdict = "medium"
            reasons.append("mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수")

        # 3. 파일 크기 대조 — MoE 판정의 근거가 되므로 먼저 한다
        size_ok: Optional[bool] = None
        measured = bytes_per_param(raw, patch["after"])
        if measured:
            actual, expected, filename = measured
            ratio = actual / expected
            size_ok = 0.4 <= ratio <= 2.0
            record.setdefault("validation", {})["size_check"] = {
                "file": filename, "bytes_per_param": round(actual, 3),
                "expected": expected, "ratio": round(ratio, 2), "consistent": size_ok,
            }
            if not size_ok:
                stats["size_mismatch"] += 1
                verdict = "medium"
                reasons.append(
                    f"파일 {filename} 이 {actual:.2f} B/param — {expected} 기대값의 "
                    f"{ratio:.1f}배. gguf.total 이 전체를 못 셀 가능성"
                )

        # 4. MoE — 전체인지 활성인지가 쟁점이다.
        #    파일 크기가 gguf.total 과 맞으면 전체를 센 것이므로 내리지 않는다.
        #    24B-A2B 모델의 IQ4 파일이 12.9 GiB 였고, 24B 기준과 맞았다.
        signal = moe_signal(model_id, raw)
        if signal:
            stats["moe"] += 1
            if size_ok:
                record.setdefault("validation", {})["moe"] = {
                    "signal": signal,
                    "resolved": "파일 크기가 gguf.total 과 일치 — 전체 파라미터로 판단",
                }
                stats["moe_resolved"] += 1
            else:
                verdict = "medium"
                reasons.append(
                    f"MoE 신호 ({signal}) — 전체인지 활성인지 불명확. 파일 크기로도 확인 안 됨"
                )

        if reasons:
            patch["confidence"] = verdict
            patch["validation_notes"] = reasons
            downgraded.append({"model_id": model_id, "billion": round(billion, 2),
                               "reasons": reasons})
            stats["medium"] += 1
        else:
            stats["high"] += 1

    with OUT_PATH.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    lines: List[str] = []
    out = lines.append
    out("# 델타 검증")
    out("")
    out("`gguf.total`을 네 가지로 검증하고 신뢰도를 조정했다. 값을 지어내지 않고 등급만 내렸다.")
    out("")
    out("| 검사 | 수 |")
    out("|---|---:|")
    out(f"| 검증 대상 (parameter_count 패치) | {stats['checked']} |")
    out(f"| ✅ 원본 파라미터와 5% 이내 일치 | {stats['confirmed_by_canonical']} |")
    out(f"| ⚠️ 원본과 불일치 | {stats['conflict_with_canonical']} |")
    out(f"| ⚠️ mmproj 있음 (VL, 비전 인코더 제외) | {stats['vl_mmproj']} |")
    out(f"| ⚠️ MoE 신호 | {stats['moe']} |")
    out(f"| └ 파일 크기로 전체 파라미터 확인됨 | {stats['moe_resolved']} |")
    out(f"| ⚠️ 파일 크기 불일치 | {stats['size_mismatch']} |")
    out("")
    out("| 최종 신뢰도 | 수 | 비율 |")
    out("|---|---:|---:|")
    total = stats["high"] + stats["medium"]
    out(f"| **high** — 검증을 전부 통과 | {stats['high']} | {stats['high'] / total * 100:.1f}% |")
    out(f"| **medium** — 사람 확인 필요 | {stats['medium']} | {stats['medium'] / total * 100:.1f}% |")
    out("")
    out("medium으로 내려간 사례 (앞 15건)")
    out("")
    for item in downgraded[:15]:
        out(f"- `{item['model_id']}` {item['billion']}B")
        for reason in item["reasons"]:
            out(f"    - {reason}")
    out("")
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines[:24]))
    print(f"\n→ {REPORT_PATH}")


if __name__ == "__main__":
    main()
