---
license: other
license_name: lfm-open-license
license_link: https://www.liquid.ai/license
language:
- en
- ko
base_model: gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged
pipeline_tag: text-generation
tags:
- translation
- gguf
- llama-cpp
- korean
- english
- lfm2
---

# 🇰🇷↔️🇺🇸 LFM2-v8-rl-10k-merged-GGUF

**LFM2-v8-rl-10k-merged의 GGUF 양자화 버전**

CPU/GPU에서 llama.cpp로 빠른 추론 가능!

## 📊 양자화별 성능 (1012개 수동 분석)

> **결론: 4/5/8비트 모두 fp32와 사실상 동일!**

| Quantization | CHrF++ | BLEU | Size | fp32 대비 |
|--------------|--------|------|------|-----------|
| **fp32 (원본)** | 34.32 | 13.10 | 4.68G | - |
| **Q8_0** 🏆 | **34.39** | 12.93 | 1.25G | **+0.07** |
| Q5_K_M | 34.08 | 12.78 | 843M | -0.24 |
| Q4_K_M | 33.97 | 12.56 | 731M | -0.35 |

### 🔍 1012개 예제 수동 검토 결과

**핵심 발견:**

1. **90% 이상**: 모든 양자화 버전에서 **의미적으로 동일한 번역**
2. **차이점**: 단어 선택 차이만 존재
   - 예: "제안했다" vs "말했다" vs "언급했다"
3. **환각 패턴**: 양자화 수준과 **무관하게 동일하게 발생**
   - "George W. Bush" → "조지 워싱턴" (모든 버전)
   - "cheetahs" → "기린" 또는 "호랑이" (모든 버전)

**양자화가 번역 품질에 미치는 영향: 거의 없음!**

| 비교 항목 | Q4 vs Q8 | Q8 vs fp32 |
|-----------|----------|------------|
| 의미 차이 | ❌ 없음 | ❌ 없음 |
| 단어 선택 | 약간 다름 | 거의 동일 |
| 환각 빈도 | 동일 | 동일 |
| 반복 버그 | ❌ 없음 | fp32만 발생 |

> ⚠️ **오히려 fp32 merged에서 0.1% 미만 확률로 반복 출력 버그 발생!**
> GGUF 양자화 버전이 더 안정적입니다.

## 📦 사용 가능한 파일

| 파일 | 크기 | 추천 용도 |
|------|------|----------|
| `*-Q8_0.gguf` | 1.25G | **품질+안정성 최우선** 🏆 |
| `*-Q5_K_M.gguf` | 843M | **균형 추천** |
| `*-Q4_K_M.gguf` | 731M | 경량화/모바일 |

## 🚀 사용법

### llama-cpp-python (Python)

```python
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

# 모델 다운로드 (Q8_0 추천)
model_path = hf_hub_download(
    "gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged-GGUF",
    "lfm2-1.2b-koen-mt-v8-rl-10k-merged-Q8_0.gguf"
)

# 모델 로드
llm = Llama(
    model_path=model_path,
    n_ctx=4096,
    n_gpu_layers=-1,  # GPU 사용 (-1: 전체 레이어)
    verbose=False
)

def translate(text, direction="en2ko"):
    if direction == "en2ko":
        system = "Translate the following text to Korean."
    else:
        system = "Translate the following text to English."
    
    prompt = f"""<|im_start|>system
{system}<|im_end|>
<|im_start|>user
{text}<|im_end|>
<|im_start|>assistant
"""
    output = llm(prompt, max_tokens=256, stop=["<|im_end|>"], temperature=0.3)
    return output['choices'][0]['text'].strip()

# 사용 예시
print(translate("The weather is beautiful today."))
# → 오늘 날씨가 정말 아름답습니다.

print(translate("한국 음식이 정말 맛있어요.", "ko2en"))
# → Korean food is really delicious.
```

### Colab에서 GPU 사용

```python
# 1. CUDA 지원 llama-cpp-python 설치 (중요!)
!pip uninstall llama-cpp-python -y
!pip install llama-cpp-python==0.3.16 \
    --extra-index-url https://github.com/abetlen/llama-cpp-python/releases/download/v0.3.16-cu124

# 2. 위 코드 실행
```

### llama.cpp CLI

```bash
llama-cli -hf gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged-GGUF \
    -p "Translate to Korean: Hello world"
```

## 💡 왜 GGUF가 더 좋은가?

| 항목 | fp32/fp16 | GGUF Q8_0 |
|------|-----------|-----------|
| **크기** | 4.68GB | 1.25GB (3.7배 작음) |
| **성능** | CHrF++ 34.32 | CHrF++ 34.39 (동등+) |
| **안정성** | 반복 버그 있음 | ✅ 안정적 |
| **추론 속도** | GPU 필요 | CPU에서도 빠름 |
| **용도** | 추가 학습용 | **실제 서빙용** |

## 🔗 관련 링크

- **원본 모델**: [gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged](https://huggingface.co/gyung/lfm2-1.2b-koen-mt-v8-rl-10k-merged)
- **프로젝트**: [GitHub - LFM2-KoEn-Tuning](https://github.com/gyunggyung/LFM2-KoEn-Tuning)

## 📜 라이선스

- **Base Model:** [LiquidAI/LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B) (LFM Open License v1.0)
- **Developed by:** Gyung (Kiwoong)
