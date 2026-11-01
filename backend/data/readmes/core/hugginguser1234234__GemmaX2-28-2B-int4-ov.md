---
license: gemma
base_model: ModelSpace/GemmaX2-28-2B-v0.1
tags:
  - translation
  - openvino
  - int4
  - korean
language:
  - ko
  - en
  - ja
pipeline_tag: translation
---

# GemmaX2-28-2B-int4-ov

[ModelSpace/GemmaX2-28-2B-v0.1](https://huggingface.co/ModelSpace/GemmaX2-28-2B-v0.1)을
**OpenVINO IR로 변환하고 INT4로 양자화한 것**입니다. 원본 가중치를 학습하거나 바꾸지
않았고, 실행 형식만 바꿨습니다.

Intel iGPU/NPU에서 온디바이스 번역에 쓰려고 만들었습니다.

## 무엇이 바뀌었나

| | 원본 | 이 저장소 |
|---|---|---|
| 형식 | safetensors (bf16) | OpenVINO IR |
| 정밀도 | bf16 | INT4 (group_size 128, ratio 1.0) |
| 크기 | 약 5 GB | **1.59 GB** |

변환 명령:

```bash
optimum-cli export openvino \
  --model ModelSpace/GemmaX2-28-2B-v0.1 \
  --task text-generation-with-past \
  --weight-format int4 --group-size 128 --ratio 1.0 \
  GemmaX2-28-2B-int4-ov
```

## 실측 (Intel Core Ultra 7 258V / Arc 140V iGPU / 공유 RAM 16.4GB)

| 항목 | 값 |
|---|---|
| 적재 시간 | 19초 |
| GPU 메모리 | 1,578 MB |
| 생성 속도 | 38.3 tok/s |
| 문장 한 줄(30토큰) | 0.78초 |

같은 조건에서 9B 변환본은 11.6 tok/s / 2.58초 / 5,039 MB였습니다. 문장 10개 비교에서
7개는 대등했고, 관용구·경어에서 9B가 앞섰습니다(예: `Let's circle back` →
2B "제품 팀과 일치한 후에 이것을 다시 돌아보자" / 9B "제품 팀과 조율한 후에 이 문제를
다시 살펴보겠습니다").

## 쓰는 법

원본과 같은 프롬프트 형식을 씁니다.

```python
import openvino_genai as ov_genai

pipe = ov_genai.LLMPipeline("GemmaX2-28-2B-int4-ov", "GPU")
cfg = ov_genai.GenerationConfig()
cfg.max_new_tokens = 256
cfg.do_sample = False          # 번역은 결정적 디코딩

text = "The committee will hold a hearing today."
prompt = f"Translate this from English to Korean:\nEnglish: {text}\nKorean:"
print(pipe.generate(prompt, cfg))
# → 위원회는 오늘 청문회를 개최할 예정입니다.
```

## 한계

- 관용구·문화적 함의는 약합니다. `on the same page`가 "같은 페이지에 있는지"로
  직역됩니다. 이는 원본 모델과 모델 크기의 한계이며 양자화 때문이 아닙니다.
- 문장마다 말투(`-습니다` / `-어요` / `-이다`)가 섞일 수 있습니다. 시스템 프롬프트로
  고정하는 것을 권합니다.
- 원본은 28개 언어를 지원하지만, 위 실측은 en→ko와 ja→ko에서만 확인했습니다.

## 라이선스

Gemma Terms of Use를 따릅니다. 원본 모델의 라이선스가 그대로 적용됩니다.

> Gemma is provided under and subject to the Gemma Terms of Use found at
> [ai.google.dev/gemma/terms](https://ai.google.dev/gemma/terms)

이 저장소의 파일은 원본을 **수정(형식 변환 및 INT4 양자화)한 것**입니다. 사용·재배포
시 Gemma Terms of Use와
[Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy)가
적용되며, 재배포하실 경우 수령자에게 약관 사본을 함께 제공해야 합니다.

원본: [ModelSpace/GemmaX2-28-2B-v0.1](https://huggingface.co/ModelSpace/GemmaX2-28-2B-v0.1)
(논문: [arXiv:2502.02481](https://arxiv.org/abs/2502.02481))
