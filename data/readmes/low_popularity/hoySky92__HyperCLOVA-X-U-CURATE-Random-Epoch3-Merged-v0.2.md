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
- AIHUB_71533
- AIHUB_569
---

# HyperCLOVA X U-CURATE Random Epoch3 Merged v0.2

**Powered by HyperCLOVA X**

2026 K-DS 해커톤 예선 및 K-AI 리더보드 평가를 위해 만든 실험용 한국어 fine-tuned model입니다. HyperCLOVA X SEED Text Instruct 1.5B의 고정 revision에 U-CURATE Random QLoRA adapter를 병합했습니다. 별도 base model이나 PEFT adapter 없이 `AutoModelForCausalLM`과 vLLM에서 직접 읽을 수 있는 BF16 standalone full-model artifact입니다.

## 모델 정보

- Base: `naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-1.5B`
- Base revision: `0728a47d632019a8da5f53b663db1c175dc04115`
- Architecture: `LlamaForCausalLM`
- Format: BF16 sharded safetensors
- Fine-tuning: 4-bit NF4 QLoRA, assistant-only masking
- Adapter SHA-256: `55280d552281b2c5659d3a047bcf4ee5bf540ac1f1ff8da0d854eaf8771bc954`

## 학습 요약

- Unique training samples: 400 (`AIHUB_71533`, `AIHUB_569`)
- Epochs: 3
- Sample presentations: 1,200
- Optimizer steps: 150
- Batch 1, gradient accumulation 8, seed 42
- Learning rate: `1e-4`, cosine scheduler
- Formatted tokens: 896,493
- Supervised tokens: 12,909

## 내부 검증

동일한 고정 holdout 200건에서 primary metric은 `0.523114`였습니다. 이 값은 single-seed two-source proxy 결과이며 공식 K-AI 점수가 아닙니다. 1-epoch 기존 Random baseline의 내부 primary `0.433489`와 비교하는 epoch-control 실험입니다.

## Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "hoySky92/HyperCLOVA-X-U-CURATE-Random-Epoch3-Merged-v0.2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
)
```

## vLLM

```bash
vllm serve hoySky92/HyperCLOVA-X-U-CURATE-Random-Epoch3-Merged-v0.2 --dtype bfloat16
```

## 한계

- 400건, 2개 AI Hub source, single seed 기반의 소규모 실험 모델입니다.
- 본 모델의 내부 점수 향상이 공식 K-AI 점수 향상을 보장하지 않습니다.
- 일반 한국어 성능, 사실성, 안전성 및 편향을 보장하지 않습니다.
- 고위험 의사결정에는 사용하지 마십시오.

## 라이선스

이 derivative model은 저장소에 포함된 HyperCLOVA X SEED Model License Agreement를 따릅니다. 전체 조건은 `LICENSE`, 변경 사항은 `MODIFICATIONS.md`, 고지는 `NOTICE`를 확인하십시오.
