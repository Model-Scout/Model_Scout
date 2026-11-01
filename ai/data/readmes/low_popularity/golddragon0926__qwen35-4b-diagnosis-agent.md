---
language:
- ko
tags:
- gguf
- qwen3_5
- text-generation
base_model: Qwen/Qwen3.5-4B
base_model_relation: finetune
---

# Qwen3.5-4B Diagnosis Agent · checkpoint-300

`checkpoint-300` LoRA를 베이스 모델에 병합한 가중치와 이를 변환한 단일 BF16 GGUF입니다.
GGUF는 베이스 언어 모델·300 step 학습 가중치·토크나이저·원본 채팅 템플릿을 포함하므로 별도 LoRA 파일 없이 텍스트 추론할 수 있습니다.

## 다운로드

- [qwen35-4b-diagnosis-agent-checkpoint-300-BF16.gguf](./qwen35-4b-diagnosis-agent-checkpoint-300-BF16.gguf): **8.424 GB** (7.846 GiB), 단일 파일
- [변환·검증 manifest](./gguf-manifest.json): 원본 커밋, SHA-256, 변환 설정과 실제 검증 기록
- 기존 Safetensors 모델과 step별 어댑터도 유지합니다.

```bash
hf download golddragon0926/qwen35-4b-diagnosis-agent qwen35-4b-diagnosis-agent-checkpoint-300-BF16.gguf --local-dir .
llama-completion -m qwen35-4b-diagnosis-agent-checkpoint-300-BF16.gguf --jinja -cnv -st --reasoning-budget 0 -c 4096 -p "안녕하세요"
```

Qwen3.5와 BF16을 지원하는 llama.cpp 또는 호환 런타임이 필요합니다. 실제 로드·생성 확인에는 llama.cpp `b11972` Windows x64 CPU를 사용했습니다.
학습 당시처럼 thinking을 끄려면 지원 클라이언트에서 `enable_thinking=false`를 적용하세요.

## 출처와 변환

- 베이스: `Qwen/Qwen3.5-4B`, 커밋 `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`
- 체크포인트: `checkpoint-300`, global step **300**, epoch **1.8998019801980197**
- 학습 때 기록된 validation loss: **0.4713131785392761**. 이 값은 GGUF 품질 측정 결과가 아닙니다.
- 변환 입력: 이 저장소 커밋 [`5d1cb2f7f0f790b65974bccd94226e8808c3a363`](https://huggingface.co/golddragon0926/qwen35-4b-diagnosis-agent/tree/5d1cb2f7f0f790b65974bccd94226e8808c3a363)의 루트 병합 모델. `selection_info.json`이 checkpoint-300을 명시하며, 3개 Safetensors 원격 SHA-256과 로컬 입력을 대조했습니다. LoRA를 두 번 병합하지 않았습니다.
- 변환기: 공식 llama.cpp 커밋 `e09a78a25dec3f42175ad59ecc540a54bed0b9b2`, `--outtype bf16 --no-mtp`
- BF16 행렬 정밀도를 유지하며 변환기가 요구하는 일부 벡터·연산 파라미터는 F32입니다. 추가 저비트 양자화는 하지 않았습니다.
- 원본 설정은 MTP 레이어를 선언하지만 실제 가중치에는 해당 텐서가 없습니다. `--no-mtp`로 실제 32개 디코더 레이어만 내보냈습니다.

SHA-256:

```text
aa170024ab95db37b73f94256802d72c8176dbfdf286d8a7cc9effbf16ccf284
```

## 실제 검증과 범위

AI 에이전트가 GGUF 헤더·단일 파일·426개 텐서·32개 레이어·원본 채팅 템플릿을 확인했습니다.
초기·중간·마지막 레이어의 대표 FFN 가중치 3개는 원본 BF16 바이트와 일치합니다.
별도 가상 회의실 안내 문항으로 CPU 모델 로드와 한국어 응답 생성을 확인했습니다. 최종 test 평가셋은 사용하지 않았습니다.
전체 정확도·회귀 품질·속도 비교 및 사람 리뷰는 수행하지 않았습니다.

이 GGUF는 **텍스트 추론용**입니다. 원본의 이미지·영상 입력용 비전 모듈은 포함하지 않습니다. 해당 기능에는 별도 `mmproj` GGUF가 필요합니다.
