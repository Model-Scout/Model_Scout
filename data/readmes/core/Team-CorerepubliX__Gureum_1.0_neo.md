---
license: cc-by-nc-nd-4.0
language:
- ko
- en
pipeline_tag: text-generation
library_name: transformers
tags:
- gureum
- korean
- corerepublix
---

![Gureum banner](assets/banner.png)

# Gureum (구름) 1.0

**Gureum**은 [CorerepubliX](https://huggingface.co/Team-CorerepubliX)가 만든 한국어 대화형 AI 모델입니다.

## 특징

- 한국어 대화, 존댓말 유지, 수학/코드/번역/글쓰기 등 범용 비서 역할
- 사용자가 반말로 질문해도 기본적으로 존댓말을 유지하도록 학습됨
- 긴 글 작성 시 마크다운(`##` 제목, 목록 등) 구조를 사용하도록 학습됨

## 요구 사항

| 항목 | 내용 |
|---|---|
| 파라미터 수 | 약 2.3B |
| 가중치 용량 | 원본(safetensors, bf16) 약 4.6GB / GGUF Q4_K_M 약 1.35GB |
| 최소 메모리(GGUF Q4_K_M 기준) | VRAM 또는 RAM 약 3GB 이상 (CPU 추론도 가능) |
| 권장 환경 | GPU 6GB 이상 (8GB에서 여유 있게 동작 확인됨) |
| 컨텍스트 길이 | 최대 8192 토큰 (학습은 768 토큰 기준) |
| 필수 라이브러리 | `transformers`, `torch` (safetensors 사용 시) / `llama.cpp` 최신 빌드 (GGUF 사용 시) |
| 권장 샘플링 설정 | `temperature=0.7`, `top_p=0.9`, **`repeat_penalty>=1.1`, `repeat_last_n>=256` 필수** |

> ⚠️ `repeat_penalty`를 설정하지 않거나 너무 낮게 두면, 답변이 끝난 뒤에도 종료되지 않고
> 반복/깨진 토큰을 계속 생성하는 문제가 발생할 수 있습니다. 반드시 위 권장값 이상으로 설정하세요.

## 알려진 한계

- 700토큰 이상의 아주 긴 글을 생성할 때, 드물게 비슷한 문장을 조금씩 바꿔가며 반복하는
  경우가 있습니다. 이런 경우 `repeat_penalty`를 1.15~1.2로 높이거나 `max_tokens`을
  600 이하로 제한하는 것을 권장합니다.

## 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Team-CorerepubliX/Gureum_1.0_neo"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

messages = [{"role": "user", "content": "너는 누구야?"}]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
out = model.generate(inputs, max_new_tokens=200)
print(tok.decode(out[0][inputs.shape[-1]:], skip_special_tokens=True))
```

시스템 메시지를 따로 주지 않으면 기본 Gureum 페르소나가 자동으로 적용됩니다.

## 라이선스

이 모델은 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) 라이선스로 배포됩니다.
상업적 이용과 2차 저작물(파생 모델) 배포가 금지되며, 저작자 표시가 필요합니다.
