---
license: other
license_name: lfm-open-license
license_link: https://www.liquid.ai/license
language:
- en
- ko
base_model: LiquidAI/LFM2-1.2B
pipeline_tag: text-generation
tags:
- translation
- machine-translation
- korean
- english
- lfm2
- grpo
---

# 🇰🇷↔️🇺🇸 LFM2-v8-rl-10k-merged

**LiquidAI LFM2-1.2B 기반 한영/영한 번역 SOTA 모델**

GRPO (Group Relative Policy Optimization) 강화학습으로 400 Step 학습 완료된 최종 버전.

- **1.2B 모델이 4B 모델을 압도!** Gemma-3 (4B)보다 1.78 CHrF++ 높음
- **단 400 Step (0.78 Epoch)만의 학습**으로 SOTA 달성
- **존댓말 일관성 완벽**: 1012개 샘플 전체에서 "~합니다" 어미 일관 적용
- **Google Colab T4 무료 GPU**로 학습 가능

## 📊 성능 (Flores-200 Benchmark, 1012 Samples)

| Rank | Model | CHrF++ | BLEU | Params |
|------|-------|--------|------|--------|
| 1 | Google Translate | 39.27 | 18.18 | - (API) |
| **2** | **🏆 LFM2-v8-RL (Step 400)** | **34.61** | **13.21** | **1.2B** |
| 3 | Gemma-3-4B-it-GGUF | 32.83 | 11.36 | 4B |
| 4 | LFM2-1.2B (Base) | 27.23 | 6.43 | 1.2B |
| 5 | Qwen3-4B-GGUF (Base) | 25.62 | - | 4B |

✅ **1.2B 모델로 4B 모델들을 압도적으로 능가!**

### 📈 학습 과정별 성능 향상

| Step | Epoch | CHrF++ | BLEU | 비고 |
|------|-------|--------|------|------|
| 0 | 0.00 | 33.53 | 12.63 | v6.4 Base |
| 200 | 0.39 | 34.10 | 12.93 | +0.57 향상 |
| 300 | 0.59 | 34.19 | 13.24 | Historic High |
| **400** | **0.78** | **34.61** | **13.21** | **🏆 SOTA** |

## ✨ v8의 강점

1. **존댓말/문체 일관성**: "~합니다", "~했습니다" 어미가 전 샘플에 걸쳐 일관되게 적용
2. **자연스러운 문장 구조**: "타스마니아 주 데본포트의 메이버 병원 자금을..." 같은 복잡한 문장도 자연스럽게 처리
3. **문맥 인식 번역**: "While"을 문맥에 따라 "반면", "동안" 등으로 유연하게 번역
4. **전문 용어 처리**: "rachis"를 "우축"으로 정확하게 번역

## ⚠️ 알려진 한계

1. **고유명사 환각**: "George W. Bush" → "조지 워싱턴"으로 잘못 번역 (베이스 모델에서 상속된 편향)
2. **일부 전문 용어 오역**: 특정 과학 용어에서 오류 발생 가능

> 💡 **해결 방안**: DPO를 통한 환각 교정 예정 (v9)

## 🔬 양자화 실험 결과 (1012개 수동 분석)

> **결론: 4/5/8/32비트 모두 사실상 차이 없음!**

| Quantization | CHrF++ | BLEU | Size | 비고 |
|--------------|--------|------|------|------|
| **fp32 (원본)** | 34.32 | 13.10 | 4.68G | 간헐적 반복 버그 |
| **Q8_0** 🏆 | **34.39** | 12.93 | 1.25G | **가장 안정적** |
| Q5_K_M | 34.08 | 12.78 | 843M | 균형 |
| Q4_K_M | 33.97 | 12.56 | 731M | 경량화 |

### 수동 분석 핵심 발견

**1012개 예제 수동 검토 결과:**

- **90% 이상**: 모든 버전에서 의미적으로 동일한 번역
- **차이점**: 단어 선택 차이만 존재 (예: "제안했다" vs "말했다")
- **환각 패턴**: 모든 버전에서 동일하게 발생
  - "George W. Bush" → "조지 워싱턴" (역대 대통령 혼동)
  - "cheetahs" → "기린" 또는 "호랑이" (동물명 혼동)

**버전별 특이사항:**

| 현상 | Q4 | Q5 | Q8 | fp32 | adapter |
|------|:--:|:--:|:--:|:----:|:-------:|
| 반복 버그 | ❌ | ❌ | ❌ | ⚠️ | ❌ |
| 번역 품질 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 안정성 | ✅ | ✅ | ✅✅ | ⚠️ | ✅ |

> ⚠️ **fp32 merged 모델에서 0.1% 미만 확률로 반복 출력 버그 발견**
> (예: "파고 파고 파고..." 무한 반복)

### 추천 사용 시나리오

| 시나리오 | 추천 버전 | 이유 |
|----------|-----------|------|
| **프로덕션 서빙** | Q8_0 GGUF | 안정적, 3.7배 작음 |
| **모바일/엣지** | Q5_K_M GGUF | 크기 대비 성능 최적 |
| **추가 학습** | fp32 merged | 전체 파라미터 필요 |

## 🚀 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged",
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(
    "gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged",
    trust_remote_code=True
)

def translate(text, direction="en2ko"):
    if direction == "en2ko":
        prompt = "Translate the following text to Korean."
    else:
        prompt = "Translate the following text to English."
    
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": text}
    ]
    
    inputs = tokenizer.apply_chat_template(
        messages, return_tensors="pt", add_generation_prompt=True
    ).to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.3,
            min_p=0.15,
            repetition_penalty=1.05,  # 반복 방지
            pad_token_id=tokenizer.eos_token_id
        )
    
    return tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True).strip()

# 사용 예시
print(translate("Hello, how are you today?"))
# → 안녕하세요, 오늘 기분이 어떠세요?

print(translate("오늘 날씨가 정말 좋네요.", "ko2en"))
# → The weather is really nice today.
```

## 📈 학습 상세

| 항목 | 값 |
|------|-----|
| **Base Model** | gyung/lfm2-1.2b-koen-mt-v6.4-merged |
| **Method** | GRPO (Group Relative Policy Optimization) |
| **Reward** | COMET + CHrF++ |
| **Dataset Size** | 10,000 samples (양방향) |
| **Training Steps** | 400 |
| **Effective Batch Size** | 128 |
| **LoRA Rank** | 32 |
| **LoRA Alpha** | 64 |
| **Target Modules** | all-linear |

## 🔧 학습 방법론

**"Data-Centric + Progressive Learning"** 파이프라인:

1. **SFT (Step 1)**: LFM2-1.2B 베이스 → 20만개 + 8.8만개 고품질 번역 데이터 학습 → v6.4
2. **GRPO (Step 2)**: v6.4 → 10k 양방향 RL 데이터 + COMET/CHrF++ 리워드 → v8 (SOTA)

> 💡 **핵심**: 무작정 데이터를 늘리는 게 아니라, 약점을 분석하고 타겟팅된 데이터를 추가


## 📦 GGUF 버전 (추천)

경량화 + 안정성을 위해 GGUF 버전 사용 권장:

👉 [gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged-GGUF](https://huggingface.co/gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged-GGUF)

## 🔗 관련 링크

- **프로젝트**: [GitHub - LFM2-KoEn-Tuning](https://github.com/gyunggyung/LFM2-KoEn-Tuning)
- **GGUF 버전**: [gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged-GGUF](https://huggingface.co/gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged-GGUF)

## 📜 라이선스

- **Base Model:** [LiquidAI/LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B) (LFM Open License v1.0)
- **Developed by:** Gyung (Kiwoong)
