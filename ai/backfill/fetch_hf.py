#!/usr/bin/env python3
"""메타데이터가 빈 모델을 Hugging Face API로 다시 조회해 원본 응답을 저장한다.

왜 필요한가
-----------
02_enrich_metadata.extract_parameter_count()는 ``info.safetensors.parameters``
한 곳만 본다. GGUF 전용 레포는 safetensors가 없으므로 즉시 None이 되고,
파라미터 수를 모르는 모델이 1,527개(39.4%) 생겼다. 컨텍스트 길이 1,459개,
architecture 1,425개도 같은 모델들이다.

그런데 Hugging Face API는 GGUF 레포에 ``gguf`` 키를 돌려준다.

    "gguf": {"total": 27009346304, "architecture": "gemma3", "context_length": 131072}

이건 추측이 아니라 HF가 GGUF 파일 헤더를 파싱해 내놓는 값이다. 지금 쓰고 있는
``safetensors.parameters``와 같은 등급의 1차 출처인데 읽지 않고 있었다.

이 스크립트는 판단하지 않는다. 응답을 그대로 저장만 한다. 어떤 값을 신뢰할지는
build_delta.py가 출처를 명시해서 결정하고, 사람이 그 근거를 보고 판정한다.

    python ai/backfill/fetch_hf.py            # 빈 필드가 있는 모델만
    python ai/backfill/fetch_hf.py --all      # 전체 (기존 값 교차 검증용)
    python ai/backfill/fetch_hf.py --status   # 진행 상황만
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List

HERE = Path(__file__).resolve().parent
AI_ROOT = HERE.parent
RAW_DIR = HERE / "raw"
STATE_PATH = HERE / "raw" / ".fetch_state.json"

API = "https://huggingface.co/api/models/{model_id}?blobs=true"
# blobs=true를 붙이면 siblings에 파일 크기가 들어온다. "내 GPU에 들어가나"는
# 파라미터 수 추정보다 실제 파일 크기로 답하는 편이 정확하다.

TIMEOUT = 20
PAUSE = 0.12          # 익명 호출이라 예의상 간격을 둔다
RETRY_PAUSE = 5.0
MAX_RETRY = 3


def corpus_rows() -> List[Dict[str, Any]]:
    sys.path.insert(0, str(AI_ROOT / "test" / "golden" / "v2" / "tools"))
    import corpus_v2

    return corpus_v2.load_rows()


def missing_fields(row: Dict[str, Any]) -> List[str]:
    """어떤 필드가 비어 있는지. 이게 조회 대상 선정 근거다."""
    meta = row.get("filter_metadata") or {}
    gaps = []
    if not isinstance(meta.get("parameter_count_billion"), (int, float)):
        gaps.append("parameter_count")
    if not isinstance(meta.get("context_length"), (int, float)):
        gaps.append("context_length")
    if not meta.get("architecture"):
        gaps.append("architecture")
    if not meta.get("model_type"):
        gaps.append("model_type")
    if not meta.get("license"):
        gaps.append("license")
    return gaps


def shard_path(model_id: str) -> Path:
    """model_id를 파일명으로 쓸 수 없으니 2단계로 쪼갠다."""
    safe = model_id.replace("/", "__")
    return RAW_DIR / safe[:2].lower() / f"{safe}.json"


def fetch_one(model_id: str, token: str | None) -> Dict[str, Any] | None:
    request = urllib.request.Request(API.format(model_id=model_id))
    request.add_header("User-Agent", "model-scout-backfill/1.0")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    for attempt in range(MAX_RETRY):
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code in (429, 503) and attempt < MAX_RETRY - 1:
                time.sleep(RETRY_PAUSE * (attempt + 1))
                continue
            return {"__error__": f"HTTP {error.code}"}
        except Exception as error:  # 네트워크 오류 등
            if attempt < MAX_RETRY - 1:
                time.sleep(RETRY_PAUSE)
                continue
            return {"__error__": str(error)[:200]}
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="빈 필드가 없는 모델도 조회 (교차 검증용)")
    parser.add_argument("--status", action="store_true", help="진행 상황만 출력")
    args = parser.parse_args()

    rows = corpus_rows()
    targets = [row["model_id"] for row in rows if args.all or missing_fields(row)]

    done = {path.stem.replace("__", "/") for path in RAW_DIR.rglob("*.json")}
    todo = [model_id for model_id in targets if model_id not in done]

    gap_counts: Dict[str, int] = {}
    for row in rows:
        for field in missing_fields(row):
            gap_counts[field] = gap_counts.get(field, 0) + 1

    print(f"코퍼스 {len(rows)}행")
    print("빈 필드별 모델 수:")
    for field, count in sorted(gap_counts.items(), key=lambda item: -item[1]):
        print(f"  {field:18s} {count:5d}")
    print()
    print(f"조회 대상 {len(targets)} · 이미 받음 {len(targets) - len(todo)} · 남음 {len(todo)}")
    if args.status:
        return
    if not todo:
        print("받을 것이 없습니다.")
        return

    token = os.getenv("HF_TOKEN")
    print(f"토큰 {'있음' if token else '없음 (익명)'} · 예상 {len(todo) * (PAUSE + 0.35) / 60:.0f}분")
    print()

    ok = failed = 0
    started = time.perf_counter()
    for index, model_id in enumerate(todo, start=1):
        payload = fetch_one(model_id, token)
        path = shard_path(model_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        if payload and "__error__" in payload:
            failed += 1
        else:
            ok += 1
        if index % 50 == 0 or index == len(todo):
            elapsed = time.perf_counter() - started
            rate = index / elapsed
            print(f"  {index}/{len(todo)}  성공 {ok} 실패 {failed}  "
                  f"{elapsed:.0f}s  (남은 시간 약 {(len(todo) - index) / rate / 60:.0f}분)",
                  flush=True)
        time.sleep(PAUSE)

    STATE_PATH.write_text(json.dumps({
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "targets": len(targets),
        "ok": ok,
        "failed": failed,
        "gap_counts": gap_counts,
        "api": API,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n완료 — 성공 {ok} / 실패 {failed}")


if __name__ == "__main__":
    main()
