---
library_name: transformers
language:
- ko
- en
license: other
tags:
- text-generation
- conversational
- korean
- math
---

# vclm-korean-7b

## Model Description | 모델 설명

**vclm-korean-7b** is a Korean language model fine-tuned with 680K Korean conversation and instruction datasets.  
**vclm-korean-7b**는 68만개의 한국어 대화 및 지시 데이터셋으로 파인튜닝된 한국어 언어 모델입니다.

## Model Details | 모델 상세 정보

- **Model Type | 모델 타입**: Causal Language Model (Decoder-only Transformer)
- **Parameters | 파라미터**: 7.6B (7,615,616,512)
- **Languages | 언어**: Korean (한국어), English (영어)
- **License | 라이선스**: VCLM AI Model License Agreement 1.0 - NC (Non-Commercial)

## Key Features | 주요 특징

✅ **Strong Mathematical Performance | 뛰어난 수학 능력**: GSM8K 80.7% (outperforms GPT-3.5 57% | GPT-3.5 57%보다 높음)  
✅ **Korean Conversation | 한국어 대화**: Natural dialogue in Korean | 자연스러운 한국어 대화  
✅ **Code Generation | 코드 생성**: Python, JavaScript support | Python, JavaScript 등 지원  
✅ **Fast Inference | 빠른 추론**: Efficient 7B model | 효율적인 7B 모델

## Benchmark Performance | 벤치마크 성능

### Mathematics | 수학
- **GSM8K**: 80.7% (flexible-extract) / 76.6% (strict-match)
  - Outperforms GPT-3.5 (57%) | GPT-3.5 (57%)보다 우수

### General Knowledge | 종합 지식 
- **MMLU**: 73.7%
  - Social Sciences | 사회과학: 83.4%
  - STEM | 이공계: 70.4%
  - Humanities | 인문학: 67.1%

### Reasoning | 추론
- **HellaSwag**: 79.3%
- **Winogrande**: 72.8%
- **ARC-Easy**: 77.0%
- **ARC-Challenge**: 48.5%

### Korean Language | 한국어
- **KoBEST Average | 평균**: 60.6%
  - COPA: 70.2%
  - SentiNeg: 65.7%
  - HellaSwag: 55.6%
  - BoolQ: 50.7%

## Usage | 사용 방법

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "soka0000/vclm-korean-7b"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

messages = [
    {"role": "user", "content": "2+2는 무엇인가요?"}
]

input_text = tokenizer.apply_chat_template(
    messages, 
    tokenize=False, 
    add_generation_prompt=True
)

inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=256,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
print(response)
```

### Quantized Versions | 양자화 버전

Memory-efficient quantized versions are available | 메모리 효율적인 양자화 버전 제공:

- [vclm-korean-7b-8bit](https://huggingface.co/soka0000/vclm-korean-7b-8bit) - 8bit quantization (8.2GB)
- [vclm-korean-7b-4bit](https://huggingface.co/soka0000/vclm-korean-7b-4bit) - 4bit quantization (5.3GB)
- [vclm-korean-7b-nf4](https://huggingface.co/soka0000/vclm-korean-7b-nf4) - NF4 quantization (5.3GB)

```python
from transformers import BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)

model = AutoModelForCausalLM.from_pretrained(
    "soka0000/vclm-korean-7b",
    quantization_config=quantization_config,
    device_map="auto"
)
```

## Recommended Use Cases | 추천 사용 사례

✅ **Suitable For | 적합한 용도**:
- Mathematical problem solving | 수학 문제 풀이
- Korean chatbot development | 한국어 챗봇 개발
- Code generation assistance | 코드 생성 보조
- Research and education | 연구 및 교육
- Simple Q&A systems | 간단한 질의응답 시스템

⚠️ **Limitations | 제한사항**:
- Complex professional knowledge (medicine, law) | 복잡한 전문 지식 (의료, 법률)
- Real-time information (trained on pre-2023 data) | 실시간 정보 (2023년 이전 데이터)
- Complex reasoning tasks | 고도의 추론 작업
- Commercial services require additional tuning | 상용 서비스는 추가 튜닝 권장

## License | 라이선스

This model is distributed under the **VCLM AI Model License Agreement 1.0 - NC (Non-Commercial)**.  
이 모델은 **VCLM AI Model License Agreement 1.0 - NC (Non-Commercial)** 하에 배포됩니다.

### Key Terms | 주요 조건

- ✅ **Research and educational use permitted** | **연구 및 교육 목적 사용 가능**
- ✅ **Academic research, experimentation, learning, teaching** | **학술 연구, 실험, 학습, 교육 가능**
- ✅ **Publication of research results** | **연구 결과 공개 가능**
- ❌ **Commercial use prohibited** (sales, services) | **상업적 사용 금지** (판매, 서비스)
- ❌ **Revenue-generating purposes prohibited** | **수익 창출 목적 사용 금지**
- ⚠️ **Commercial licensing requires separate inquiry** | **상업적 라이선스는 별도 문의 필요**

For details, see [LICENSE_NC](./LICENSE_NC) file.  
자세한 내용은 [LICENSE_NC](./LICENSE_NC) 파일을 참조하세요.

## Citation | 인용

If you use this model in your research, please cite:  
이 모델을 연구에 사용하시는 경우 다음과 같이 인용해주세요:

```bibtex
@misc{vclm-korean-7b,
  author = {Soka0000},
  title = {vclm-korean-7b: Korean Language Model},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/soka0000/vclm-korean-7b}},
}
```

## Contact | 문의

- **Model Page | 모델 페이지**: https://huggingface.co/soka0000/vclm-korean-7b

---

**Note | 참고**: This model is developed for research and educational purposes.  
Sufficient testing is recommended before applying to actual services.  
이 모델은 연구 및 교육 목적으로 개발되었습니다.  
실제 서비스에 적용하기 전에 충분한 테스트를 권장합니다.
