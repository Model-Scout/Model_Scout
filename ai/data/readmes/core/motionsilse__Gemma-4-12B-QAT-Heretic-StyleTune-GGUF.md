---
language:
  - en
  - ko
license: apache-2.0
library_name: gguf
pipeline_tag: text-generation
base_model:
  - google/gemma-4-12B-it-qat-q4_0-unquantized
  - wnfldchen/gemma-4-12B-it-qat-q4_0-gguf-heretic
  - Gryphe/Gemma-4-12B-StyleTune
tags:
  - gemma-4
  - gguf
  - qat
  - q4_0
  - heretic
  - uncensored
  - styletune
  - speculative-decoding
  - mtp
  - llama-cpp
  - not-for-all-audiences
---

# Gemma-4-12B-QAT-Heretic-StyleTune-GGUF

Gemma 4 12B의 QAT 기반 Heretic 본체에 StyleTune 계열의 출력 헤드를 결합한
텍스트 생성용 GGUF입니다. 본체는 Q4_0, 별도 `output.weight`는 Q8_0이며,
단일 파일 크기는 약 8.05GB입니다.

이 릴리스의 핵심은 **Heretic QAT 본체를 재양자화하지 않고 그대로 보존**하면서,
검증된 StyleTune 출력 투영층만 붙였다는 점입니다. llama.cpp의 Gemma 4 QAT용
MTP drafter와 함께 로드하는 것도 실제 GPU smoke test로 확인했습니다.

> 이 모델은 QAT-derived 하이브리드입니다. StyleTune과 Heretic 변경까지 포함해
> 전체 모델을 다시 QAT 학습한 체크포인트는 아닙니다.

## 구성

| 부분 | 출처 | 형식 |
|---|---|---|
| Transformer 본체와 입력 임베딩 | [`wnfldchen/gemma-4-12B-it-qat-q4_0-gguf-heretic`](https://huggingface.co/wnfldchen/gemma-4-12B-it-qat-q4_0-gguf-heretic) | 원본 GGUF의 667개 tensor를 byte-for-byte 보존 |
| Style 출력 헤드 | [`Gryphe/Gemma-4-12B-StyleTune`](https://huggingface.co/Gryphe/Gemma-4-12B-StyleTune) 기반으로 만든 검증된 donor | `output.weight`, Q8_0, `[3840, 262144]` |
| MTP drafter(별도 다운로드) | [`unsloth/gemma-4-12B-it-qat-GGUF`](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF) | `mtp-gemma-4-12B-it.gguf` |

최종 GGUF는 총 668개 tensor입니다. Heretic 본체 667개는 source GGUF와 raw
tensor hash가 같고, donor에서 별도 Q8_0 `output.weight` 하나만 복사했습니다.
자세한 revision과 해시는 [`provenance.json`](./provenance.json) 및
[`SHA256SUMS`](./SHA256SUMS)에 있습니다.

이 저장소에는 멀티모달 projector를 포함하지 않습니다. 현재 릴리스의 검증 범위는
텍스트 생성입니다.

## 파일

| 파일 | 크기 | SHA-256 |
|---|---:|---|
| `Gemma-4-12B-QAT-Heretic-StyleTune-Q4_0-Q8Head.gguf` | 8,045,427,072 bytes | `b41711286ff9e75014da30a40dfbf7a8e12634ff5b768b131933af0a58677da2` |

## llama.cpp 실행: MTP 포함

### 1. llama.cpp와 Hugging Face CLI 준비

```powershell
winget install llama.cpp
py -m pip install -U "huggingface_hub[hf_xet]"
```

### 2. llama.cpp 폴더에서 파일 받기

아래 명령은 target 모델과 MTP drafter를 `models` 폴더에 저장합니다.

```powershell
hf download motionsilse/Gemma-4-12B-QAT-Heretic-StyleTune-GGUF `
  Gemma-4-12B-QAT-Heretic-StyleTune-Q4_0-Q8Head.gguf `
  --local-dir models

hf download unsloth/gemma-4-12B-it-qat-GGUF `
  mtp-gemma-4-12B-it.gguf `
  --revision 980b060c40a8539ac159e0501a3e0f66a6365af3 `
  --local-dir models
```

### 3. 직접 실행

```powershell
.\llama-server.exe `
  --model ".\models\Gemma-4-12B-QAT-Heretic-StyleTune-Q4_0-Q8Head.gguf" `
  --alias "Gemma-4-12B-QAT-Heretic-StyleTune" `
  --host 127.0.0.1 `
  --port 8080 `
  --ctx-size 32768 `
  --n-gpu-layers all `
  --flash-attn on `
  --cache-type-k q8_0 `
  --cache-type-v q8_0 `
  --parallel 1 `
  --jinja `
  --reasoning off `
  --metrics `
  --temperature 1.0 `
  --top-p 0.95 `
  --top-k 64 `
  --min-p 0.05 `
  --repeat-penalty 1.0 `
  --spec-draft-model ".\models\mtp-gemma-4-12B-it.gguf" `
  --spec-type draft-mtp `
  --spec-draft-n-max 4 `
  --spec-draft-ngl all
```

위 예시는 localhost 포트 8080, 32K context, 전체 GPU offload, Q8 KV cache,
MTP draft 최대 길이 4를 명시합니다. Web UI는 `http://127.0.0.1:8080/`,
OpenAI 호환 API의 base URL은 `http://127.0.0.1:8080/v1`입니다.

### MTP 설정

`--spec-draft-n-max 4`는 이 모델의 RTX 5080 GPU smoke test에서 정상 작동한
시작값이며, 모든 GPU와 프롬프트에서 가장 빠르다는 뜻은 아닙니다. MTP의 효과는
acceptance rate, 생성 길이, GPU에 따라 달라집니다. 이 옵션을 바꿔 같은 프롬프트를
여러 번 측정하고 `draft acceptance`, `accepted / generated`, `mean len`,
`eval time`을 함께 비교하세요. acceptance가 낮으면 draft 길이를 키워도 오히려
느려질 수 있습니다.

## 검증 범위

- 최종 파일: 8,045,427,072 bytes, 668 tensors
- 구조 검증: Heretic source의 기존 667 tensor body hash 보존 확인
- 출력 헤드: Q8_0, `[3840, 262144]`, donor tensor raw hash 확인
- GPU smoke test: Windows, RTX 5080 16GB, llama.cpp b10331
- 32K context와 Q8 KV cache에서 target + MTP 동시 로드 및 생성 성공
- 단일 195-token 생성 관측: 127.70 tok/s, draft acceptance 41.781%
  (`122 / 292`), mean accepted length 2.67

마지막 수치는 짧은 단일 smoke test의 참고값일 뿐이며, 반복 benchmark나 다른
환경의 성능을 대표하지 않습니다. Heretic/StyleTune 결합 후의 광범위한 능력·안전성
평가도 아직 수행하지 않았습니다.

## 사용 범위와 주의

이 모델은 Heretic 계열 편집을 포함하므로 upstream instruction 모델보다 거부
행동이 달라질 수 있고, 부정확하거나 불쾌하거나 위험한 출력을 만들 수 있습니다.
“uncensored”는 정확성, 중립성, 합법성 또는 무조건적인 지시 수행을 보장하지
않습니다. 출력은 사용자가 검토해야 하며, 불법 행위, 타인 피해, 개인정보 침해,
고위험 자동 의사결정에 사용하지 마세요.

## 출처와 라이선스

- Google QAT upstream: [`google/gemma-4-12B-it-qat-q4_0-unquantized`](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-unquantized)
- Heretic GGUF body: [`wnfldchen/gemma-4-12B-it-qat-q4_0-gguf-heretic`](https://huggingface.co/wnfldchen/gemma-4-12B-it-qat-q4_0-gguf-heretic)
- Style donor: [`Gryphe/Gemma-4-12B-StyleTune`](https://huggingface.co/Gryphe/Gemma-4-12B-StyleTune)
- MTP drafter: [`unsloth/gemma-4-12B-it-qat-GGUF`](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)

각 upstream은 Apache-2.0으로 표시되어 있습니다. 이 파생 릴리스에도 Apache
License 2.0을 포함하고, 변경 사항과 출처를 위와 같이 명시합니다.

---

## English

This is a text-generation GGUF that combines a QAT-derived Heretic Gemma 4 12B
body with a StyleTune-derived output projection. The body remains Q4_0 and the
separate `output.weight` is Q8_0. The single GGUF is 8,045,427,072 bytes.

The 667 source tensors were copied byte-for-byte from the pinned Heretic GGUF.
Only one verified Q8_0 `output.weight` tensor was attached, producing a 668-tensor
file. This is a **QAT-derived hybrid**, not a fully re-trained QAT checkpoint after
the Heretic and StyleTune modifications.

The release is text-only and does not include a multimodal projector. Structural
validation, GPU loading, short generation, and compatibility with the listed
Gemma 4 QAT MTP drafter were tested. The published timing and acceptance values
are a single smoke-test observation, not a general benchmark.

Download the target GGUF and the external MTP drafter into the `models` folder,
then use the direct llama.cpp command above. The example uses localhost port
8080, 32K context, full GPU offload, Q8 KV cache, and `--spec-draft-n-max 4`.
Adjust the command-line options for your hardware; draft length 4 is a tested
starting point, not a guarantee of the best speed on every prompt or device.

This model includes a Heretic-family edit and may produce inaccurate, offensive,
or unsafe content. “Uncensored” is not a guarantee of correctness, neutrality,
legality, or unconditional instruction following. Review outputs and do not use
the model for illegal activity, harm, privacy violations, or unreviewed high-risk
decisions.

See [`provenance.json`](./provenance.json) for exact source revisions and
validation evidence. Distributed under Apache-2.0; upstream attribution and
modification notes are retained above.
