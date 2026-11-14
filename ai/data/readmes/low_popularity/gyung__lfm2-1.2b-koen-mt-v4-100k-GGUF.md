---
license: other
license_name: lfm-open-license-v1.0
license_link: https://huggingface.co/LiquidAI/LFM2-1.2B/blob/main/LICENSE
language:
- ko
- en
pipeline_tag: translation
tags:
- lfm2
- liquid-ai
- korean
- gguf
- quantization
base_model: gyung/lfm2-1.2b-koen-mt-v4-100k
---

# 🌊 LFM2-1.2B-KoEn-MT-v4-100k-GGUF

이 리포지토리는 [gyung/lfm2-1.2b-koen-mt-v4-100k](https://huggingface.co/gyung/lfm2-1.2b-koen-mt-v4-100k) 모델의 **GGUF(Gemma/Llama.cpp Compatible)** 양자화 버전을 포함하고 있습니다.

## ℹ️ 모델 설명 (Model Description)

**LFM2-1.2B-KoEn-MT-v4-100k**은 LiquidAI의 `LFM2-1.2B` 아키텍처를 기반으로 한국어-영어 번역 성능을 극대화하기 위해 **100,000개의 고품질 병렬 데이터셋**으로 파인튜닝된 모델입니다.

* **Base Model**: LiquidAI/LFM2-1.2B
* **Finetuned by**: Gyung
* **Parameters**: 1.2B
* **Purpose**: Korean-English Translation (한국어-영어 번역)

## 📦 제공되는 GGUF 파일 (Quantization Methods)

사용 환경과 필요에 따라 적절한 양자화 버전을 선택하여 다운로드하세요. (권장: `Q4_K_M` 또는 `Q5_K_M`)

| 파일명 (예시) | 양자화 (Quant) | 크기 (Size) | 설명 (Description) |
| --- | --- | --- | --- |
| `lfm2-1.2b-koen-mt-v4-100k-f16.gguf` | F16 | ~2.34 GB | 원본 성능 유지, 용량 큼 |
| `lfm2-1.2b-koen-mt-v4-100k-q8_0.gguf` | Q8_0 | ~1.25 GB | 품질 손실 거의 없음 |
| `lfm2-1.2b-koen-mt-v4-100k-q6_k.gguf` | Q6_K | ~963 MB | 높은 품질, 균형 잡힌 성능 |
| `lfm2-1.2b-koen-mt-v4-100k-q5_k_m.gguf` | Q5_K_M | ~843 MB | **추천**: 품질과 속도/용량의 최적 균형 |
| `lfm2-1.2b-koen-mt-v4-100k-q4_k_m.gguf` | Q4_K_M | ~731 MB | **추천**: 적은 메모리 소모, 준수한 성능 |
| `lfm2-1.2b-koen-mt-v4-100k-q4_0.gguf` | Q4_0 | ~696 MB | 가장 가벼움, 일부 품질 저하 가능성 |

## 🚀 사용 방법 (Usage)

### llama.cpp

최신 버전의 `llama.cpp`를 사용하여 실행할 수 있습니다. (LFM 아키텍처 지원 여부를 확인하세요)

```bash
./llama-cli -m lfm2-1.2b-koen-mt-v4-100k-q5_k_m.gguf \
  -p "Translate to Korean: The model is working correctly now." \
  -n 256
````

### Python (llama-cpp-python)

```python
from llama_cpp import Llama

llm = Llama(
    model_path="./lfm2-1.2b-koen-mt-v4-100k-q5_k_m.gguf",
    n_ctx=2048,
    verbose=False
)

prompt = "Translate to Korean: The model is working correctly now."
output = llm(
    f"User: {prompt}\nAssistant:",
    max_tokens=256,
    stop=["User:", "\n"],
    echo=True
)

print(output['choices'][0]['text'])
```

## 📊 벤치마크 (Benchmarks)

원본 모델(F16) 기준 **Flores-200** 평가 결과입니다. GGUF 양자화 시 점수는 소폭 하락할 수 있습니다.

  * **LFM2-1.2B-KOEN-MT-v4-100k**: CHrF++ **30.98** / BLEU **11.09**
  * Google Translate: CHrF++ 39.27
  * NLLB-200-Distilled-600M: CHrF++ 31.97

## 📜 라이선스 (License)

이 모델은 **Liquid AI LFM Open License v1.0**을 따릅니다.

  * 학술/개인 연구: 제한 없음
  * 상업적 이용: 연 매출 $10M 미만 무료 (초과 시 별도 계약 필요)
  * 자세한 내용은 [LICENSE](https://huggingface.co/LiquidAI/LFM2-1.2B/blob/main/LICENSE)를 참고하세요.

## Citation

```bibtex
@misc{lfm2-1.2b-koen-mt-v4-100k,
  author = {Gyung},
  title = {LFM2-1.2B Korean-English Machine Translation Model v4},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Model Hub},
  howpublished = {\url{[https://huggingface.co/gyung/lfm2-1.2b-koen-mt-v4-100k](https://huggingface.co/gyung/lfm2-1.2b-koen-mt-v4-100k)}}
}
```