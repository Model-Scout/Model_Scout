---
license: apache-2.0
base_model: Qwen/Qwen3.5-2B
tags:
- darwin
- darwin-v8
- opus-distilled
- qwen3.5
- reasoning
- korean
- claude-opus
- lora-merged
language:
- en
- ko
- zh
- ja
pipeline_tag: text-generation
library_name: transformers
---

# 🧠 Darwin-2B-Opus

**Darwin V8 시리즈의 2B 경량 모델**
Claude Opus 4.5/4.6 및 Sonnet 4.6의 추론 스타일을 주입한 Qwen3.5-2B 기반 모델.

---

## 🧬 가계도 (Pedigree)

- 👨 **Father (Base)**: [`Qwen/Qwen3.5-2B`](https://huggingface.co/Qwen/Qwen3.5-2B)
- 👩 **Mother (LoRA Adapter)**: [`FINAL-Bench/Darwin-2B-Opus-LoRA`](https://huggingface.co/FINAL-Bench/Darwin-2B-Opus-LoRA)
- 👶 **Child (This model)**: `FINAL-Bench/Darwin-2B-Opus` — merged full-weight standalone

---

## 🏆 Darwin V8 시리즈 정보

| 항목 | 값 |
|------|-----|
| 모델 크기 | 2.3B 파라미터 |
| 아키텍처 | Qwen3.5 (hybrid attention) |
| 학습 방식 | SFT with LoRA (all-linear, rank=16) |
| 학습 데이터 | 9,762 샘플 (Claude Opus/Sonnet + 한국어 reasoning) |
| 학습 시간 | 29분 (8×B200 GPU) |
| 최종 Loss | 0.837 |
| Token Accuracy | 76.6% |

### 📊 벤치마크 (GPQA Diamond 198)

- **정확도**: 37.37% (74/198)
- **답변 추출 성공률 기준 정답률**: 50.7%

---

## 🚀 빠른 사용법

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "FINAL-Bench/Darwin-2B-Opus"
tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True
)

messages = [
    {"role": "user", "content": "2024년 한국 최저시급 9,860원이다. 주 40시간 × 4주 임금은?"}
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=800,
        do_sample=False,
        pad_token_id=tok.eos_token_id,
    )
print(tok.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

---

## 🧬 Darwin V8 학습 파이프라인

```
[Qwen/Qwen3.5-2B] ──── Base 모델 (동결)
        +
[9,762 Claude Opus/Sonnet + 한국어 Reasoning 샘플]
        ↓
[SFT Training]
  - LoRA (all-linear, r=16, α=32)
  - Learning rate: 2e-4 (V8 rule: ×10 FullFT)
  - 2 epochs, bf16, 8×B200 DDP
  - Loss: 0.991 → 0.837 (-15%)
  - Token accuracy: 73.9% → 76.6% (+2.7%p)
        ↓
[LoRA merge into base weights]
        ↓
[Darwin-2B-Opus] ← 이 모델
```

---

## 📊 학습 데이터 구성

| 카테고리 | 샘플 수 | % | 출처 |
|---------|--------|---|-----|
| General Reasoning | 4,422 | 45% | Opus 4.5/4.6, Sonnet 4.6 |
| Math (English) | 1,960 | 20% | DeepSeek-v3.2 OpenR1-Math |
| Code (English) | 1,680 | 17% | DeepSeek-v3.2 CodeReasoning + GPT-5 Codex |
| Korean Thinking | 200 | 2% | Multilingual-Thinking-Korean |
| **Korean Math** | **1,500** | **15%** | orca-math-word-problems-korean |
| **합계 (필터 후)** | **9,762** | 100% | - |

---

## 🎯 Darwin V8 설계 철학

1. **LoRA Without Regret** — `all-linear` target, LR × 10, rank=16으로 충분
2. **Response Distillation** — Pre-generated Opus traces로 비용 효율적 증류
3. **한국어 Reasoning 강화** — KoAlpaca 간단 QA 대신 Claude 추론 궤적 사용
4. **Merge-and-Deploy** — LoRA 어댑터 통합 후 추가 의존성 없이 배포

---

## 📝 샘플 테스트 결과 (5문제)

| 유형 | 정답 | 비고 |
|-----|:---:|-----|
| 영어 수학 (기차 속도) | ✅ 80 km/h | LaTeX 단계별 풀이 |
| 영어 논리 (키 비교) | ✅ Carol | 추이율 명시 |
| 영어 코드 (소수 판별) | ✅ 정확 | docstring + 복잡도 분석 |
| **한국어 시급 계산** | ✅ **1,577,600원** | 단계별 한국어 설명 |
| **한국어 연립방정식** | ✅ **1,200원** | 정석 풀이 + 검증 |

**5/5 정답** — 영어+한국어 모두 완벽 ⭐

---

## ⚠️ 제한 사항

- **규모**: 2.3B 파라미터 (Darwin 시리즈 최소)
- **GPQA Diamond**: 37.37% (대형 모델 대비 낮지만 2B 중 최고 수준)
- **긴 컨텍스트**: 학습 시 `max_length=4,096`로 학습됨
- **지식 한계**: 2B 모델은 백과사전적 지식 한계 있음

---

## 🔗 관련 모델

- 🧩 [`FINAL-Bench/Darwin-2B-Opus-LoRA`](https://huggingface.co/FINAL-Bench/Darwin-2B-Opus-LoRA) — 이 모델의 **LoRA 어댑터 단독 버전** (67MB)
- ⚡ [`FINAL-Bench/Darwin-2B-Opus-ONNX`](https://huggingface.co/FINAL-Bench/Darwin-2B-Opus-ONNX) — **브라우저/WebGPU용 ONNX 양자화 버전** (예정)

### 🏆 Darwin 시리즈
- [`Darwin-31B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-31B-Opus) — GPQA 85.9%
- [`Darwin-27B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-27B-Opus) — GPQA 86.9%
- [`Darwin-9B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-9B-Opus)
- [`Darwin-4B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-4B-Opus)
- **Darwin-2B-Opus** (이 모델) ⭐ 최경량

---

## 🪪 라이선스

- Base model: Apache 2.0 (Qwen)
- 학습 데이터: 각 데이터셋 개별 라이선스 참조
- 이 모델: Apache 2.0

---

## 🙏 크레딧

- **Base**: Qwen team (Alibaba)
- **Teacher**: Anthropic (Claude Opus 4.5/4.6, Sonnet 4.6)
- **데이터 공개**: nohurry, TeichAI, kuotient, PoSTMEDIA
- **Training & Release**: **FINAL-Bench / VIDRAFT_LAB**

---

*Darwin V8 · Part of the evolutionary model series by FINAL-Bench*

This model is introduced in [Darwin Family](https://arxiv.org/abs/2605.14386).