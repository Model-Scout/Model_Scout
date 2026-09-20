---
language:
- ko
license: apache-2.0
base_model: Qwen/Qwen2.5-0.5B
tags:
- korean
- qwen2
- morpheme-tokenizer
pipeline_tag: text-generation
---

# ko-morph-qwen2.5-0.5b-cpt

Qwen2.5-0.5B 백본에 **형태소 제약 BPE 토크나이저(32k)**를 이식하고, 한국어 웹 코퍼스(FineWeb-2 `kor_Hang` 선별본)
2.5B 토큰으로 continued pretraining(CPT)한 모델입니다. FVT(Fast Vocabulary Transfer)로 임베딩을 초기화한 뒤
CPT했습니다.

## 스펙

- 백본: Qwen2.5-0.5B (hidden 896 / 24층 / GQA 14:2)
- 파라미터: 386.6M (vocab 교체로 494M → 감소, 임베딩 136.1M → 28.7M)
- vocab: 32,000 (형태소 제약 BPE, Kiwi 기반 무손실 표층 분절)
- dtype: float16
- 학습: DDP + ZeRO-1 + fp16 AMP, 9,555 스텝, lr 5e-5 cosine, 2.50B 토큰

## 알려진 제약

- **개행을 인코딩하지 못합니다.** pre_tokenizer가 `WhitespaceSplit`이라 공백류를 버리고, vocab에 `\n`을 포함한
  토큰이 없습니다. 모델은 줄바꿈을 보지도 만들지도 못하며, 문단 구조가 평탄화됩니다.
- **산술/논리 추론이 원본 대비 약화됐을 가능성이 있습니다.** Qwen2.5는 수학·코드를 대량 학습했는데,
  그 위에 한국어 웹 텍스트만 얹은 CPT라 catastrophic forgetting 정황이 관찰됩니다.

## 평가

홀드아웃 BPC (bits/char, 419만 토큰):

| | loss | ppl | BPC |
|---|---|---|---|
| CPT 전 (FVT 초기화) | 7.17 | 1297.7 | 5.54 |
| **CPT 후** | **2.51** | **12.3** | **1.94** |

KoAlpaca SFT 후 Qwen2.5-0.5B 원본(동일 SFT 조건)과 비교 (베이스 모델끼리 비교, Instruct 모델 아님):

| 평가 | 본 모델 | Qwen 원본 |
|---|---|---|
| 문법 최소대립쌍 (334쌍) | 327/334 (97.9%) | 293/334 (87.7%) |
| 한국어 지식·상식 (8문항) | 정확 3 / 부분 3 / 오답 2 | 오답 8 |
| 일반 추론 (10문항) | 정답 2 / 부분 1 | 정답 3 |

McNemar p = 1.95×10⁻⁸ (문법 평가).

## 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tok = AutoTokenizer.from_pretrained("wwwcomcom/ko-morph-qwen2.5-0.5b-cpt")
model = AutoModelForCausalLM.from_pretrained("wwwcomcom/ko-morph-qwen2.5-0.5b-cpt", dtype=torch.float16)

ids = tok("안녕하세요, 오늘 날씨는", return_tensors="pt").input_ids
out = model.generate(ids, max_new_tokens=64, do_sample=True, temperature=0.8)
print(tok.decode(out[0]))
```

이 모델은 base 모델이며 SFT를 거치지 않았습니다 (별도 `sft_morph` 산출물은 이 저장소에 포함되지 않음).
줄바꿈이 없는 프롬프트 포맷을 권장합니다.

## 라이선스

Qwen2.5-0.5B 기반 파생 모델로 Apache 2.0을 따릅니다.
