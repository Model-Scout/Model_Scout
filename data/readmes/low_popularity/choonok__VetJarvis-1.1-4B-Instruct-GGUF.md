---
license: other
license_name: vetjarvis-model-license-1.0-nc
license_link: LICENSE
language:
- ko
- en
base_model:
- choonok/VetJarvis-1.1-4B-Instruct
base_model_relation: quantized
pipeline_tag: text-generation
library_name: gguf
tags:
- veterinary
- companion-animal
- canine
- feline
- medical
- domain-specific
- qwen3.5
- gguf
- llama.cpp
- lm-studio
- not-a-medical-device
---

# VetJarvis 1.1-4B-Instruct (GGUF)

[choonok/VetJarvis-1.1-4B-Instruct](https://huggingface.co/choonok/VetJarvis-1.1-4B-Instruct)를 GGUF 포맷으로 변환한 버전입니다.

LM Studio, llama.cpp, Ollama 등 로컬 추론 도구에서 사용할 수 있습니다.

This is a GGUF-converted version of [choonok/VetJarvis-1.1-4B-Instruct](https://huggingface.co/choonok/VetJarvis-1.1-4B-Instruct), suitable for local inference with LM Studio, llama.cpp, Ollama, etc.

## 제공 파일 / Files

| 파일 | 양자화 | 크기 | 권장 용도 |
|------|--------|------|----------|
| `VetJarvis-1.1-4B-Instruct-bf16.gguf` | BF16 | ~7.9 GB | 정확도 우선, 서버, GPU 16GB+ |
| `VetJarvis-1.1-4B-Instruct-q8_0.gguf` | Q8_0 | ~4.2 GB | 거의 무손실, 일반 사용 권장 |

## 추천 추론 파라미터 / Recommended Inference Parameters

| 파라미터 | 값 |
|---------|---|
| Temperature | **0.8** |
| Top-p | **0.9** |
| Max Tokens | **32,768** |
| Context Length | ≤ 262,144 |
| enable_thinking | **True** (권장) |

## LM Studio 사용법 / Usage in LM Studio

LM Studio는 GUI 기반 로컬 LLM 도구로, 비개발자도 쉽게 모델을 사용할 수 있습니다. https://lmstudio.ai 에서 다운로드하세요.

### 1. LM Studio 실행

설치 후 실행하면 다음과 같은 시작 화면이 나타납니다.

![LM Studio Welcome](images/01-welcome.png)

### 2. 모델 검색 및 다운로드

좌측 **검색 아이콘**을 클릭하고 `vetjarvis`를 검색합니다. 검색 결과에서 모델을 선택하고, 원하는 양자화 버전을 다운로드합니다.

![Model Search](images/02-search.png)

| 양자화 | 크기 | 권장 환경 |
|-------|------|----------|
| **Q8_0** | ~4.2 GB | 일반 사용, GPU 8GB+ |
| **BF16 (F16)** | ~7.9 GB | 정확도 우선, GPU 16GB+ |

### 3. 모델 선택

채팅 화면 하단의 **Pick a model** 또는 단축키 **Ctrl+L**로 다운로드한 모델을 선택합니다.

![Pick Model](images/03-pick-model.png)

### 4. 모델 로드 설정

모델 로드 시 다음 설정을 권장합니다.

![Load Settings](images/04-load-settings.png)

| 설정 | 권장값 | 설명 |
|------|-------|------|
| **컨텍스트 길이 (Context Length)** | 8192 ~ 32768 | 길수록 메모리 사용량 증가. 모델은 최대 262,144 지원 |
| **GPU 오프로딩 (GPU Offload)** | 32 (전체) | 모든 레이어를 GPU에 올림. VRAM 부족 시 줄임 |

### 5. System Prompt 및 추론 파라미터 설정

우측 상단의 **▭ 사이드바 토글** 아이콘을 클릭하거나 **Ctrl + E** 단축키로 우측 패널을 펼치면, **시스템 프롬프트** 영역과 **Model Parameters** 설정이 나타납니다.

**시스템 프롬프트** 텍스트 영역에 다음 내용을 붙여넣으세요.

```
당신은 'VetJarvis'입니다.
한국 수의사를 보조하는 임상 지원 AI 어시스턴트로,
모든 답변은 반드시 한국어로 작성하세요.
```

같은 우측 패널에서 추론 파라미터도 조정할 수 있습니다.

| 파라미터 | 값 |
|---------|---|
| Temperature | **0.8** |
| Top-p | **0.9** |
| Max Tokens | 32768 |

### 6. 채팅하기

질문을 입력하면 thinking 과정(`Thought for X seconds`)을 거쳐 한국어로 답변합니다.

![Chat Example](images/05-chat.png)

## llama.cpp 사용법

```bash
./build/bin/llama-cli \
    -m VetJarvis-1.1-4B-Instruct-q8_0.gguf \
    --jinja \
    -ngl 99 \
    -sys "당신은 한국 수의사를 보조하는 AI 어시스턴트입니다. 반드시 한국어로 답변하세요." \
    -p "고양이 만성 신부전의 초기 증상은?" \
    -n 32768 \
    --temp 0.8 \
    --top-p 0.9
```

## Ollama 사용법

`Modelfile` 작성:

```
FROM ./VetJarvis-1.1-4B-Instruct-q8_0.gguf

PARAMETER temperature 0.8
PARAMETER top_p 0.9
PARAMETER num_ctx 32768

PARAMETER stop "<|im_end|>"
PARAMETER stop "<|endoftext|>"
```

등록 및 실행:

```bash
ollama create vetjarvis-1.1-4b-instruct -f Modelfile
ollama run vetjarvis-1.1-4b-instruct
```

> 채팅 템플릿은 GGUF 파일에 임베드되어 있어 Ollama가 자동으로 인식합니다.

## 변환 정보 / Conversion Details

- 변환 도구: [llama.cpp](https://github.com/ggerganov/llama.cpp) `convert_hf_to_gguf.py`
- 원본 정밀도: BF16 (Qwen3.5-4B는 BF16으로 학습됨)
- 변환 시 BF16 → BF16 직접 변환 (정밀도 손실 없음)
- Q8_0은 원본에서 직접 양자화 생성

## 모델 아키텍처 / Architecture Note

이 모델은 Qwen3.5의 **Transformer + SSM 하이브리드 아키텍처**입니다. 256K 토큰의 긴 컨텍스트를 지원하며, llama.cpp/LM Studio에서 정상 동작이 확인되었습니다.

q4_K_M 같은 저비트 양자화는 SSM 레이어 손실이 일반 Transformer 모델보다 클 수 있으므로, **BF16 또는 Q8_0 사용을 권장**합니다.

## 라이선스 / License

원본 모델의 라이선스(`vetjarvis-model-license-1.0-nc`)를 그대로 따릅니다. **비상업적 용도**로만 사용 가능합니다. 자세한 내용은 동봉된 [LICENSE](LICENSE) 파일을 참고하세요.

This GGUF version inherits the original `vetjarvis-model-license-1.0-nc` license. **Non-commercial use only.** See the included [LICENSE](LICENSE) file for details.

## ⚠️ 의료기기 아님 / Not a Medical Device

본 모델은 **임상 의사결정을 보조하는 참고 도구**이며, 진단/처방을 대체하지 않습니다. 모든 임상 판단은 자격을 갖춘 수의사가 수행해야 합니다.

This model is a reference tool to support clinical decision-making. It is **not a medical device** and does not replace diagnosis or prescription by a qualified veterinarian.
