#!/usr/bin/env python3
"""데이터 계약의 각 필드가 실제로 얼마나 채워져 있는지 센다.

재적재 전후를 같은 기준으로 비교하기 위한 도구다. 숫자를 손으로 적지 않는다.

    python contract/coverage.py                       # ai/data 운영 데이터
    python contract/coverage.py --source snapshot     # 골든셋 스냅샷
    python contract/coverage.py --compare --out contract/baseline.md   # 세 소스 전부

가장 중요한 출력은 필드 coverage가 아니라 "질문별 답변 가능률"이다. 필드가
80% 채워져 있어도 그 필드를 쓰는 질문에 답할 수 있는 모델이 20%뿐이면
사용자에게는 20%가 현실이다.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional

HERE = Path(__file__).resolve().parent
AI_ROOT = HERE.parent
DATA = AI_ROOT / "data"
POOLS = ("core", "low_popularity")

sys.path.insert(0, str(AI_ROOT))
import taxonomy  # noqa: E402

# taxonomy.yaml의 commercial_use 패싯을 그대로 쓴다. 매핑 테이블을 새로 만들지
# 않는다 — 이미 있는 어휘와 두 벌이 되면 어느 쪽이 맞는지 아무도 모른다.
COMMERCIAL_STATUS = {
    "commercial": "permitted",
    "non_commercial": "prohibited",
    "conditional": "review_required",
    "unknown": "unknown",
    None: "unknown",
}


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


class View:
    """Stage 2 레코드와 Stage 4 레코드의 필드 위치가 다르다. 계약 필드 이름으로
    둘 다 읽을 수 있게 한 겹 덮는다. 계약은 저장 위치가 아니라 사실을 규정한다."""

    def __init__(self, row: Dict[str, Any], kind: str) -> None:
        self.row = row
        self.kind = kind
        if kind == "contract":
            self.meta = row
            self.model = row.get("technical") or {}
        elif kind == "stage4":
            self.meta = row.get("filter_metadata") or {}
            self.model = self.meta
        else:
            self.meta = row
            self.model = row.get("model") or {}

    @property
    def model_id(self) -> str:
        return self.row.get("model_id") or ""

    def get(self, field: str) -> Any:
        if self.kind == "contract":
            technical = self.row.get("technical") or {}
            capability = self.row.get("capability") or {}
            table: Dict[str, Callable[[], Any]] = {
                "parameter_count": lambda: technical.get("parameter_count_total"),
                "context_length": lambda: technical.get("context_length"),
                "architecture": lambda: technical.get("architecture"),
                "model_type": lambda: technical.get("model_type"),
                "dtype": lambda: technical.get("dtype"),
                "license": lambda: (self.row.get("legal") or {}).get("license_raw"),
                "primary_task": lambda: capability.get("primary_task"),
                "languages": lambda: capability.get("languages"),
                "korean_verified": lambda: capability.get("korean_verified"),
                "downloads": lambda: (self.row.get("discovery") or {}).get("downloads"),
            }
            getter = table.get(field)
            return getter() if getter else None
        if self.kind == "stage4":
            table: Dict[str, Callable[[], Any]] = {
                "parameter_count": lambda: self.meta.get("parameter_count"),
                "context_length": lambda: self.meta.get("context_length"),
                "architecture": lambda: self.meta.get("architecture"),
                "model_type": lambda: self.meta.get("model_type"),
                "dtype": lambda: self.meta.get("dtype"),
                "license": lambda: self.row.get("license") or self.meta.get("license"),
                "primary_task": lambda: self.meta.get("primary_task"),
                "languages": lambda: self.meta.get("languages"),
                "korean_verified": lambda: self.meta.get("korean_verified"),
                "downloads": lambda: self.meta.get("downloads"),
            }
        else:
            table = {
                "parameter_count": lambda: self.model.get("parameter_count"),
                "context_length": lambda: self.model.get("context_length"),
                "architecture": lambda: self.model.get("architectures"),
                "model_type": lambda: self.model.get("type"),
                "dtype": lambda: self.model.get("dtype"),
                "license": lambda: self.row.get("license"),
                "primary_task": lambda: (self.row.get("task") or {}).get("primary"),
                "languages": lambda: (self.row.get("language") or {}).get("declared_languages"),
                "korean_verified": lambda: ((self.row.get("language") or {}).get("korean") or {}).get("verified"),
                "downloads": lambda: ((self.row.get("popularity") or {}).get("current") or {}).get("downloads"),
            }
        getter = table.get(field)
        return getter() if getter else None

    # --- 계약이 요구하지만 아직 어디에도 없는 필드 -------------------------
    # 이 메서드들이 전부 None/False를 돌려주는 것이 baseline의 핵심 결과다.

    def _identity(self) -> Dict[str, Any]:
        return self.row.get("identity") or {}

    def gated(self) -> Any:
        if self.kind == "contract":
            return self._identity().get("gated")
        return self.row.get("gated", (self.row.get("source") or {}).get("gated"))

    def revision(self) -> Any:
        if self.kind == "contract":
            return self._identity().get("revision")
        return self.row.get("revision") or self.row.get("sha")

    def last_modified(self) -> Any:
        if self.kind == "contract":
            return self._identity().get("last_modified")
        return self.row.get("last_modified")

    def artifact_bytes(self) -> Any:
        return (self.artifacts() or {}).get("total_bytes")

    def parameter_count_active(self) -> Any:
        return self.model.get("parameter_count_active")

    def artifacts(self) -> Dict[str, Any]:
        if self.kind == "contract":
            raw = self.row.get("artifacts") or {}
            # 계약은 포맷 플래그를 formats.<name>.present 로 둔다. 질문 체크가
            # artifacts().get("gguf") 로 묻는 모양을 그대로 쓸 수 있게 눕힌다.
            flat = {name: (spec or {}).get("present")
                    for name, spec in (raw.get("formats") or {}).items()}
            flat["total_bytes"] = raw.get("total_bytes")
            flat["file_count"] = raw.get("file_count")
            return flat
        source = self.meta if self.kind == "stage4" else self.row
        return source.get("artifacts") or {}

    def measured_artifact_gib(self) -> Any:
        if self.kind != "contract":
            return None
        estimate = (self.row.get("deployment") or {}).get("vram_estimate") or {}
        return (estimate.get("artifact") or {}).get("gib")

    def hardware(self) -> Dict[str, Any]:
        if self.kind == "contract":
            return ((self.row.get("deployment") or {}).get("vram_estimate") or {}).get("weights_only") or {}
        source = self.meta if self.kind == "stage4" else self.row
        return ((source.get("hardware") or {}).get("weights_only") or {})

    def commercial_status(self) -> str:
        raw = self.get("license")
        if isinstance(raw, list):
            raw = raw[0] if len(raw) == 1 else raw
        if isinstance(raw, list):
            # 라이선스가 여러 개면 가장 제한적인 것을 따른다.
            classes = {taxonomy.normalize("commercial_use", one) for one in raw}
            for name in ("non_commercial", "conditional", "unknown", "commercial"):
                if name in classes:
                    return COMMERCIAL_STATUS[name]
            return "unknown"
        return COMMERCIAL_STATUS.get(taxonomy.normalize("commercial_use", raw), "unknown")

    def benchmark(self) -> bool:
        if self.kind == "contract":
            return bool((self.row.get("quality") or {}).get("results"))
        """실제 점수가 있는지. ``benchmark_metadata`` 컨테이너는 점수가 없어도
        readme 경로·summary만 담고 거의 모든 레코드에 존재한다. 컨테이너를 세면
        99%가 나오지만 비교 가능한 점수는 11%뿐이다."""
        results = (self.row.get("benchmark_metadata") or {}).get("results")
        if results:
            return True
        return bool(self.row.get("metrics"))


def has_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def has_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


# 계약 필드 → 채워진 것으로 볼 조건
FIELDS: Dict[str, Callable[[View], bool]] = {
    "identity.model_id": lambda v: bool(v.model_id),
    "identity.revision": lambda v: bool(v.revision()),
    "identity.last_modified": lambda v: bool(v.last_modified()),
    "identity.gated": lambda v: v.gated() is not None,
    "capability.primary_task": lambda v: bool(v.get("primary_task")),
    "capability.languages": lambda v: bool(v.get("languages")),
    "capability.korean_verified": lambda v: v.get("korean_verified") is not None,
    "technical.parameter_count_total": lambda v: has_int(v.get("parameter_count")),
    "technical.parameter_count_active": lambda v: has_int(v.parameter_count_active()),
    "technical.context_length": lambda v: has_int(v.get("context_length")),
    "technical.architecture": lambda v: bool(v.get("architecture")),
    "technical.model_type": lambda v: bool(v.get("model_type")),
    "technical.dtype": lambda v: bool(v.get("dtype")),
    "artifacts.format_flags": lambda v: bool(v.artifacts()),
    "artifacts.total_bytes": lambda v: has_int(v.artifact_bytes()),
    "deployment.vram_fp16_gib": lambda v: has_number(v.hardware().get("fp16_gib")),
    "deployment.vram_int4_gib": lambda v: has_number(v.hardware().get("int4_gib")),
    "legal.license_raw": lambda v: bool(v.get("license")),
    "legal.commercial_status": lambda v: v.commercial_status() != "unknown",
    "quality.benchmark_score": lambda v: v.benchmark(),
    "discovery.downloads": lambda v: has_int(v.get("downloads")),
}

EMBEDDING_TASKS = {"sentence-similarity", "feature-extraction", "embedding"}
TRANSLATION_TASKS = {"translation", "text2text-generation", "text-generation"}


def q_commercial_korean(v: View) -> bool:
    return v.get("korean_verified") is True and v.commercial_status() == "permitted"


def q_fits_my_gpu(v: View) -> bool:
    # 16GB GPU에 들어가는지 답하려면 '크기'를 하나라도 알아야 한다.
    hardware = v.hardware()
    return (
        has_number(hardware.get("fp16_gib"))
        or has_number(hardware.get("detected_quantization_gib"))
        or has_number(v.measured_artifact_gib())
        or has_int(v.artifact_bytes())
    )


def q_runs_on_ollama(v: View) -> bool:
    return v.artifacts().get("gguf") is True


def q_korean_embedding(v: View) -> bool:
    return v.get("korean_verified") is True and v.get("primary_task") in EMBEDDING_TASKS


def q_long_translation(v: View) -> bool:
    return has_int(v.get("context_length")) and v.get("primary_task") in TRANSLATION_TASKS


def q_best_benchmark(v: View) -> bool:
    return v.benchmark()


def q_can_i_redistribute(v: View) -> bool:
    # 배포 가능 여부는 라이선스 판정 + gated 여부가 둘 다 있어야 말할 수 있다.
    return v.commercial_status() in {"permitted", "prohibited"} and v.gated() is not None


QUESTIONS: Dict[str, Dict[str, Any]] = {
    "Q1 상업 서비스에 쓸 수 있는 한국어 모델": {
        "needs": "legal.commercial_status, capability.korean_verified",
        "fn": q_commercial_korean,
    },
    "Q2 내 GPU(16GB)에서 돌아가는 모델": {
        "needs": "technical.parameter_count_total 또는 artifacts.total_bytes",
        "fn": q_fits_my_gpu,
    },
    "Q3 Ollama/llama.cpp로 돌릴 수 있는 모델": {
        "needs": "artifacts.gguf",
        "fn": q_runs_on_ollama,
    },
    "Q4 한국어 임베딩/RAG 모델": {
        "needs": "capability.primary_task, capability.korean_verified",
        "fn": q_korean_embedding,
    },
    "Q5 긴 문서를 번역할 모델": {
        "needs": "technical.context_length, capability.primary_task",
        "fn": q_long_translation,
    },
    "Q6 성능이 가장 좋은 모델": {
        "needs": "quality.benchmark_score",
        "fn": q_best_benchmark,
    },
    "Q7 내려받아 배포해도 되는 모델": {
        "needs": "legal.commercial_status, identity.gated",
        "fn": q_can_i_redistribute,
    },
}


def load(source: str, path: Optional[Path] = None) -> List[View]:
    if source == "contract":
        if path is None:
            raise SystemExit("--source contract 는 --path <records.jsonl> 가 필요합니다")
        return [View(row, "contract") for row in read_jsonl(path)]
    if source == "snapshot":
        sys.path.insert(0, str(AI_ROOT / "test" / "golden" / "v2" / "tools"))
        import corpus_v2

        return [View(row, "stage4") for row in corpus_v2.load_rows()]
    if source == "stage4":
        rows: List[Dict[str, Any]] = []
        for pool in POOLS:
            rows += read_jsonl(DATA / f"hf_models_stage4_{pool}.jsonl")
        return [View(row, "stage4") for row in rows]
    rows = []
    for pool in POOLS:
        rows += read_jsonl(DATA / f"hf_models_stage2_{pool}.jsonl")
    return [View(row, "stage2") for row in rows]


def table(rows: Iterable[str]) -> str:
    return "\n".join(rows)


def render(views: List[View], source: str) -> str:
    total = len(views)
    if not total:
        return f"`{source}`에 레코드가 없습니다.\n"
    out: List[str] = []
    out.append(f"측정 대상 `{source}` — 레코드 {total:,}개\n")

    out.append("## 질문별 답변 가능률\n")
    out.append("필터가 그 질문을 걸 수 있고, 답에 쓸 사실이 레코드에 있는 모델의 수다.\n")
    out.append("| 사용자 질문 | 필요한 계약 필드 | 답변 가능 | 비율 |")
    out.append("|---|---|---:|---:|")
    for name, spec in QUESTIONS.items():
        count = sum(1 for view in views if spec["fn"](view))
        out.append(f"| {name} | `{spec['needs']}` | {count:,} | {count / total * 100:.1f}% |")
    out.append("")

    out.append("## 계약 필드 coverage\n")
    out.append("| 계약 필드 | 있음 | 비율 |")
    out.append("|---|---:|---:|")
    for field, fn in FIELDS.items():
        count = sum(1 for view in views if fn(view))
        out.append(f"| `{field}` | {count:,} | {count / total * 100:.1f}% |")
    out.append("")

    out.append("## 라이선스 → commercial_status\n")
    status = collections.Counter(view.commercial_status() for view in views)
    out.append("| commercial_status | 모델 수 | 비율 | 뜻 |")
    out.append("|---|---:|---:|---|")
    meanings = {
        "permitted": "선언된 라이선스가 상업 이용을 허용하는 계열",
        "prohibited": "비상업 전용(NC). 상업 질의에서 제외",
        "review_required": "추가 약관 확인 필요(llama/gemma/GPL/other 등)",
        "unknown": "라이선스 자체가 없음. 판단 불가",
    }
    for name in ("permitted", "prohibited", "review_required", "unknown"):
        count = status.get(name, 0)
        out.append(f"| `{name}` | {count:,} | {count / total * 100:.1f}% | {meanings[name]} |")
    out.append("")

    out.append("### 원시 라이선스 값 상위\n")
    raw = collections.Counter()
    for view in views:
        value = view.get("license")
        raw[json.dumps(value, ensure_ascii=False) if isinstance(value, list) else value] += 1
    out.append("| license | 모델 수 | 분류 |")
    out.append("|---|---:|---|")
    for value, count in raw.most_common(15):
        cls = COMMERCIAL_STATUS.get(taxonomy.normalize("commercial_use", value), "unknown")
        out.append(f"| `{value}` | {count:,} | `{cls}` |")
    out.append("")
    return table(out) + "\n"


SOURCE_NOTES = {
    "stage2": "`data/hf_models_stage2_{pool}.jsonl` — 운영 파이프라인의 사실 수집 결과",
    "stage4": "`data/hf_models_stage4_{pool}.jsonl` — 검색 문서. Supabase에 올라가는 형태",
    "snapshot": "`test/golden/v2/corpus_snapshot.jsonl` — Supabase active 동결본 + `ai/backfill` 반영",
}


def render_compare() -> str:
    """세 소스를 한 파일에 담는다. 교차 비교 표의 숫자도 측정값이어야 한다 —
    손으로 옮겨 적으면 재적재 후에 한쪽만 낡는다."""
    loaded = {name: load(name) for name in SOURCE_NOTES}
    head = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], cwd=AI_ROOT, capture_output=True, text=True
    ).stdout.strip() or "(git 아님)"
    today = dt.date.today().isoformat()

    out: List[str] = []
    out.append("# Coverage baseline")
    out.append("")
    out.append("`python contract/coverage.py --compare --out contract/baseline.md`로 재생성한다.")
    out.append("숫자를 손으로 적지 않는다. 재적재 후 같은 명령으로 before/after를 비교한다.")
    out.append("")
    out.append(f"측정 시점: {today} · 대상 커밋: `{head}`")
    out.append("")
    out.append("## 세 소스가 무엇인지")
    out.append("")
    out.append("| 소스 | 레코드 | 무엇인가 |")
    out.append("|---|---:|---|")
    for name, note in SOURCE_NOTES.items():
        out.append(f"| `{name}` | {len(loaded[name]):,} | {note} |")
    out.append("")
    out.append("`snapshot`만 백필이 반영돼 있다. `ai/backfill`은 `out/` 폴더에만 썼고")
    out.append("운영 `data/`를 교체하지 않았다. **이 작업의 목표가 저 격차를 사이드 폴더가**")
    out.append("**아니라 파이프라인이 만들게 하는 것이다.**")
    out.append("")
    out.append("## 한눈에 — 질문별 답변 가능률")
    out.append("")
    out.append("| 사용자 질문 | " + " | ".join(f"`{name}`" for name in SOURCE_NOTES) + " |")
    out.append("|---|" + "---:|" * len(SOURCE_NOTES))
    for question, spec in QUESTIONS.items():
        cells = []
        for name, views in loaded.items():
            share = sum(1 for view in views if spec["fn"](view)) / max(len(views), 1) * 100
            cells.append(f"{share:.1f}%")
        out.append(f"| {question} | " + " | ".join(cells) + " |")
    out.append("")
    out.append("### 읽는 법")
    out.append("")
    out.append("- **Q7이 0%다.** `identity.gated`를 어느 단계에서도 수집하지 않는다.")
    out.append("  \"이 모델 내려받아 써도 되나\"에 답할 데이터가 레코드에 없다. 그런데")
    out.append("  HF 응답에는 `gated`가 99.3%로 들어오고 있다 — 안 읽은 것뿐이다.")
    out.append("- **Q2·Q5는 `snapshot`만 높다.** 백필이 올린 값이다. 운영 데이터는 그대로다.")
    out.append("- **Q6은 `stage4`에서 0%다.** 벤치마크는 `06`/`07`이 sync 시점에 붙이므로")
    out.append("  Stage 4 파일에는 없다. 단계 간 사실 위치가 일관되지 않다는 신호다.")
    out.append("- **Q4가 낮은 것은 결함이 아니다.** 임베딩 과제 모델이 실제로 그만큼이다.")
    out.append("  분모가 전체 코퍼스이므로 \"부족\"이 아니라 \"분포\"다.")
    out.append("- **`legal.commercial_status`가 92.8%인데 Q1은 57.6%다.** 분류는 되지만")
    out.append("  `permitted`가 그만큼이라는 뜻이다. 나머지는 NC·조건부·미확인이다.")
    out.append("")
    out.append("## 계약 필드 coverage")
    out.append("")
    out.append("| 계약 필드 | " + " | ".join(f"`{name}`" for name in SOURCE_NOTES) + " |")
    out.append("|---|" + "---:|" * len(SOURCE_NOTES))
    for field, fn in FIELDS.items():
        cells = []
        for name, views in loaded.items():
            share = sum(1 for view in views if fn(view)) / max(len(views), 1) * 100
            cells.append(f"{share:.1f}%")
        out.append(f"| `{field}` | " + " | ".join(cells) + " |")
    out.append("")
    for name, views in loaded.items():
        out.append("---")
        out.append("")
        out.append(f"# 소스: `{name}`")
        out.append("")
        out.append(render(views, name))
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default="stage2",
                        choices=("stage2", "stage4", "snapshot", "contract"))
    parser.add_argument("--path", type=Path, default=None,
                        help="--source contract 일 때 읽을 계약 레코드 .jsonl")
    parser.add_argument("--compare", action="store_true", help="세 소스를 한 파일에 담는다")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    text = (render_compare() if args.compare
            else render(load(args.source, args.path), args.source))
    if args.out:
        args.out.write_text(text, encoding="utf-8")
        print(f"{args.out} 작성")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
