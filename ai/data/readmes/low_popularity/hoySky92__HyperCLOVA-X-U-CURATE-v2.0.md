---
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-1.5B
library_name: transformers
pipeline_tag: text-generation
language:
- ko
license: other
license_name: hyperclovax-seed
license_link: https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-1.5B/blob/main/LICENSE
tags:
- transformers
- safetensors
- llama
- korean
- u-curate
- k-ds
- aihub
- merged
datasets:
- AIHUB_569
- AIHUB_577
- AIHUB_71533
- AIHUB_71568
- AIHUB_71630
- AIHUB_71848
- AIHUB_71857
- AIHUB_71859
- AIHUB_71922
---

# U-CURATE v2.0

**Powered by HyperCLOVA X**

2026 K-DS 해커톤 및 K-AI 리더보드 평가를 위해 만든 실험용 한국어 fine-tuned model입니다. HyperCLOVA X SEED Text Instruct 1.5B의 고정 revision에 U-CURATE Random 1K QLoRA adapter를 병합했습니다. 별도 base model이나 PEFT adapter 없이 Transformers와 vLLM에서 직접 읽을 수 있는 BF16 standalone full-model artifact입니다.

## 모델 정보

- Base: `naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-1.5B`
- Base revision: `0728a47d632019a8da5f53b663db1c175dc04115`
- Release candidate: `Random 1K seed42`
- Architecture: `LlamaForCausalLM`
- Format: BF16 sharded safetensors
- Fine-tuning: 4-bit NF4 QLoRA, assistant-only masking
- Adapter SHA-256: `78f7d8e34d52b815174daf5382c5eebb1cf6ff46a0d848b18ee8f135e8d63f4a`

## 학습 요약

- Unique training samples: 1,000
- Epochs: 1
- Sample presentations: 1,000
- Optimizer steps: 125
- Batch 1, gradient accumulation 8, seed 42
- Learning rate: `5e-5`, cosine scheduler
- Formatted tokens: 614,843
- Supervised tokens: 16,133
- Training manifest SHA-256: `c308f99d94544b445199b7808d41028842d8c18e01b3c0712520b4a7877e254e`

## 실제 사용 데이터

원본 데이터나 학습 예시는 저장소에 포함하지 않으며, 실제 최종 manifest에 포함된 출처와 집계만 공개합니다.

- `AIHUB_569` — 행정 문서 대상 기계독해 데이터: 123 samples
- `AIHUB_577` — 뉴스 기사 기계독해 데이터: 237 samples
- `AIHUB_71533` — 기술과학 문서 기계독해 데이터: 253 samples
- `AIHUB_71568` — 숫자연산 기계독해 데이터: 251 samples
- `AIHUB_71630` — 한국어 멀티세션 대화: 57 samples
- `AIHUB_71848` — 형사법 LLM 사전학습 및 Instruction Tuning 데이터: 19 samples
- `AIHUB_71857` — 국어 교과 지문형 문제 데이터: 11 samples
- `AIHUB_71859` — 수학 교과 문제 풀이과정 데이터: 11 samples
- `AIHUB_71922` — 기업 회계처리 기준 데이터: 38 samples

## 내부 검증과 선택

- Fixed capability macro: `0.3540396455176473`
- Source holdout macro: `0.4315535604589093`

Random 5K의 일부 전체 지표는 개선됐지만, 네 체크포인트 모두 사전에 고정한 `korean_language` 및 `professional_knowledge` retention floor `-0.020`을 위반했습니다. 따라서 데이터 규모만으로 마지막 체크포인트를 선택하지 않고 Random 1K seed42를 최종 후보로 유지했습니다. 위 수치는 내부 고정 평가이며 공식 K-AI 점수가 아닙니다.

## Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "hoySky92/HyperCLOVA-X-U-CURATE-v2.0"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=False)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=False,
)
```

## vLLM

```bash
vllm serve hoySky92/HyperCLOVA-X-U-CURATE-v2.0 --dtype bfloat16 --max-model-len 2048 --trust-remote-code false
```

## 한계

- 1,000개 학습 샘플과 단일 seed 기반의 실험 모델입니다.
- 내부 지표가 공식 K-AI 점수나 일반화 성능을 보장하지 않습니다.
- 사실성, 안전성, 편향 및 고위험 의사결정 적합성을 보장하지 않습니다.

## 라이선스

이 derivative model은 저장소에 포함된 HyperCLOVA X SEED Model License Agreement를 따릅니다. 전체 조건은 `LICENSE`, 변경 사항은 `MODIFICATIONS.md`, 고지는 `NOTICE`를 확인하십시오.
