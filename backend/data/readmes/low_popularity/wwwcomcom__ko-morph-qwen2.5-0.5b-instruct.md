---
language:
- ko
license: apache-2.0
base_model: wwwcomcom/ko-morph-qwen2.5-0.5b-cpt
tags:
- korean
- qwen2
- morpheme-tokenizer
- instruction-tuned
pipeline_tag: text-generation
---

# ko-morph-qwen2.5-0.5b-instruct

[ko-morph-qwen2.5-0.5b-cpt](https://huggingface.co/wwwcomcom/ko-morph-qwen2.5-0.5b-cpt)를 KoAlpaca-v1.1a로
지시 튜닝(SFT)한 모델입니다. CPT 모델 카드에 있는 형태소 토크나이저·개행 불가·대조군 없음 등의 제약이
그대로 적용됩니다.

**⚠️ 공식 Qwen2.5-0.5B-Instruct와 비교하지 마세요.** 그쪽은 대규모 비공개 SFT를 거친 모델이라
21k건짜리 튜닝(본 모델)과의 차이는 토크나이저·CPT가 아니라 SFT 규모에서 옵니다. 이 모델의 공정한
비교 대상은 **같은 조건으로 SFT한 Qwen2.5-0.5B 원본 베이스**입니다 (평가 결과 아래).

## SFT 설정

- 데이터: [beomi/KoAlpaca-v1.1a](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a) (지식iN 질문 + GPT 생성 답변)
- 프롬프트 포맷: `### 질문: {instruction} ### 답변: {output}` — **개행 없음** (토크나이저가 `\n`을 인코딩 못 함)
- seq 768, micro-bs 4, accum 4, 3 epoch, lr 2e-5, 프롬프트 마스킹 (답변에만 loss)
- Qwen 대조군과 **교집합 예시만** 사용 (21,067건/99.6%) — 두 토크나이저의 길이 차이로 인한 학습셋 오염 방지

## 평가 (동일 SFT 조건의 Qwen2.5-0.5B 베이스와 비교)

| 평가 | 본 모델 | Qwen 원본 |
|---|---|---|
| 문법 최소대립쌍 (334쌍) | 327/334 (97.9%) | 293/334 (87.7%) |
| 한국어 지식·상식 (8문항) | 정확 3 / 부분 3 / 오답 2 | 오답 8 |
| 일반 추론 (10문항) | 정답 2 / 부분 1 | 정답 3 |

McNemar p = 1.95×10⁻⁸ (문법 평가). **이 격차가 형태소 토크나이저 때문인지, 2.5B 토큰 한국어 CPT
자체 때문인지는 분리되지 않습니다** — 대조군(일반 BPE + 동일 CPT)이 없기 때문입니다.

산술·형식논리 추론은 Qwen 원본이 더 낫습니다 (`300×4=1200` 등). Qwen2.5는 수학·코드를 대량
사전학습했는데 그 위에 한국어 웹 텍스트만 얹은 CPT라 catastrophic forgetting 정황으로 보입니다.

## 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tok = AutoTokenizer.from_pretrained("wwwcomcom/ko-morph-qwen2.5-0.5b-instruct")
model = AutoModelForCausalLM.from_pretrained("wwwcomcom/ko-morph-qwen2.5-0.5b-instruct", dtype=torch.float16)

prompt = "### 질문: 한국의 수도는 어디야? ### 답변:"
ids = tok(prompt, return_tensors="pt").input_ids
out = model.generate(ids, max_new_tokens=128, do_sample=False)
print(tok.decode(out[0], skip_special_tokens=True))
```

개행이 있는 프롬프트나 ChatML 포맷은 쓰지 마세요 — 학습 때 본 적이 없어 성능이 떨어집니다.

## 라이선스

Qwen2.5-0.5B 기반 파생 모델로 Apache 2.0을 따릅니다.
