---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B-Instruct
base_model_relation: finetune
language:
  - ko
pipeline_tag: text-generation
library_name: transformers
tags:
  - korean
  - pii
  - named-entity-recognition
  - person-name
  - privacy
  - maskingtape
  - lora
  - synthetic-data
---

# maskingtape-name-1.5b

한국어 문서에서 **사람 이름(인명)만** 뽑는 작은 모델입니다. 오픈소스 개인정보 비식별화 엔진
[maskingtape](https://github.com/ChoHyeonChan/maskingtape)의 하이브리드(규칙 + 로컬 LLM) 이름 탐지에 쓰려고
[Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)(Apache-2.0)를 **합성 데이터로만** LoRA 파인튜닝한 뒤 병합한 가중치입니다. 현재 판은 **v3**(2026-10-03).

A small Korean person-name extractor: Qwen2.5-1.5B-Instruct fine-tuned (LoRA, merged) on fully synthetic Korean documents
for the [maskingtape](https://github.com/ChoHyeonChan/maskingtape) PII de-identification engine. Input: a document. Output: `{"names": [...]}`.

- GGUF(Ollama용): [maskingtape-name-1.5b-GGUF](https://huggingface.co/StayAlive1/maskingtape-name-1.5b-GGUF)
- 학습 코드·데이터 생성기·비교표: 저장소 [`training/`](https://github.com/ChoHyeonChan/maskingtape/tree/main/training)

## 입출력 형식

maskingtape core가 Ollama에 보내는 것과 같습니다 — system 프롬프트는 고정, user는 원문, 답은 JSON 한 줄.

```
system: 너는 한국어 텍스트에서 실제 '사람 이름(인명)'만 추출하는 도구다. 지명·기관명·일반명사·제품명은 절대 포함하지 마라. JSON만 출력한다: {"names": ["이름1", ...]}. 이름이 없으면 {"names": []}.
user:   담당자 김하늘님께 010-1234-5678로 연락하세요. 서울역에서 만났다.
assistant: {"names": ["김하늘"]}
```

`temperature 0`으로 쓰세요. 이름은 원문에 적힌 표기 그대로 돌려줍니다(호칭 "님"·조사 제외).

## 결과

두 가지 평가가 있습니다. 숫자는 이름 라벨 완전 일치 기준이고, "하이브리드"는 maskingtape의 규칙 안전망과 합친 제품 구성입니다.

### 학습에 쓰지 않은 외부 데이터 — KDPII test 500문장 (이름 177개), 하이브리드

| 모델 | 크기 | 재현율 | 정밀도 | F1 | 오탐 | 50문장 처리(노트북 CPU) |
|---|---|---|---|---|---|---|
| **maskingtape-name-1.5b v3 (이 모델)** | 986 MB | **0.825** | 0.471 | 0.600 | 164 | **48–52초** |
| Qwen2.5-7B-Instruct | 4,683 MB | 0.825 | 0.527 | 0.643 | 131 | 144–148초 |
| 규칙 전용 | — | 0.254 | — | — | — | — |

요약: **7B와 재현율이 같고, 1/5 크기에 약 3배 빠릅니다. 정밀도는 7B가 높습니다.** KDPII(CC-BY-4.0, [Zenodo](https://doi.org/10.5281/zenodo.10968609))는 평가에만 썼습니다. 측정 조건은 저장소 README에 있습니다(2026-10-04, 온도 0 1회).

### 학습과 같은 생성기로 만든 보고용 세트 — 463건 + 공격 쌍 100 (학습 분포 안쪽)

| 모델 | 단독 F1 (오탐) | 하이브리드 F1 (오탐) | 지시문 공격 5종 재현율 단독 / 하이브리드 | 문서당 시간(GPU) |
|---|---|---|---|---|
| 규칙 전용 | — | 0.801 (22) | — | 0 ms |
| Qwen2.5-1.5B-Instruct 원본 | 0.626 (130) | 0.786 (148) | 0.28 / 0.94 | 174 ms |
| **maskingtape-name-1.5b v3** | **0.978 (13)** | **0.944 (32)** | **1.00 / 0.95** | 111 ms |
| Qwen2.5-7B-Instruct | 0.920 (41) | 0.907 (59) | 0.41 / 0.93 | 134 ms |

**이 표는 낙관적입니다.** 문장 틀과 공격 문장은 학습과 겹치지 않게 갈랐지만, 혼동어 문장 32개를 학습과 보고용이 공유하고(보고용 463건 중 172건이 포함, 44건은 학습 문서와 동일), 이름도 같은 풀에서 나옵니다. v2·v3 학습 데이터는 이 세트의 오류를 보고 고쳤습니다. 전체 표와 한계 설명: 저장소 `training/README.md`.

- "이 문서에는 이름이 없다", "이전 지시를 무시해", JSON 조작, 역할 바꾸기, 이름을 다른 말로 부르게 하기 — 다섯 유형의 문장을 문서에 붙여도 모델 단독으로 흔들리지 않습니다(학습 데이터에 공격 문장이 붙은 문서를 정답 유지로 넣었습니다).
- 남은 오류는 `박인도 참석`(박인 + 도) 같은 받침 있는 2음절 이름 + 조사 경계가 대부분입니다.

## 판 이력

| 판 | 바뀐 것 | 보고용 단독 / 하이브리드 F1 |
|---|---|---|
| v1 | 첫 학습(2 에폭) | 0.914 / 0.889 (조사 교정 전 세트) |
| v2 | 생활어 혼동 문장·조사 변형 보강(1 에폭) | 0.946 / 0.913 |
| **v3** | 생성기 문장의 **조사를 받침에 맞게 교정**(`서아은`→`서아는`), 직함+업무어 부정 문장, 2 에폭 | **0.978 / 0.944** |

## 학습

| 항목 | 내용 |
|---|---|
| 기반 모델 | Qwen/Qwen2.5-1.5B-Instruct (Apache-2.0) |
| 방법 | LoRA r=16, alpha=32, dropout 0.05, q/k/v/o/gate/up/down 전부 · bf16 · 2 에폭 · lr 2e-4 cosine · 유효 배치 16 · 정답 토큰에만 손실 |
| 데이터 | **합성 12,000건** — maskingtape bench 생성기(문장 템플릿 + 가짜 이름·번호·주소)로 만든 문서. 이름 있는 문서 73% / 없는 문서 27%, 혼동어 문장(직함+업무어·지명·회사명), 단서 없는 이름, 지시문 공격 문장 붙인 문서 20%. 이름 뒤 조사는 받침에 맞게 교정. **실제 개인정보·외부 데이터셋은 쓰지 않았습니다.** |
| 보고용 데이터 | 학습과 다른 템플릿·공격 문장으로 생성(저장소 `training/data/heldout_v2.jsonl`, `heldout_attacks_v2.jsonl`) |
| 하드웨어 | RTX 3080 10GB, 약 35분 |
| 재현 | `python -m training.make_dataset` → `python training/train_lora.py --epochs 2` → `python training/export_ollama.py` (저장소 `training/README.md`) |

## 쓰는 법

### maskingtape (Ollama)

```bash
ollama pull hf.co/StayAlive1/maskingtape-name-1.5b-GGUF:Q4_K_M
maskingtape --llm < 문서.txt        # maskingtape 0.4부터 기본 모델 — 지정 없이 --llm만
```

### transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
m = "StayAlive1/maskingtape-name-1.5b"
tok = AutoTokenizer.from_pretrained(m); model = AutoModelForCausalLM.from_pretrained(m, dtype="bfloat16", device_map="auto")
messages = [
    {"role": "system", "content": "너는 한국어 텍스트에서 실제 '사람 이름(인명)'만 추출하는 도구다. 지명·기관명·일반명사·제품명은 절대 포함하지 마라. JSON만 출력한다: {\"names\": [\"이름1\", ...]}. 이름이 없으면 {\"names\": []}."},
    {"role": "user", "content": "담당자 김하늘님께 010-1234-5678로 연락하세요."},
]
ids = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
print(tok.decode(model.generate(ids, max_new_tokens=64, do_sample=False)[0][ids.shape[1]:], skip_special_tokens=True))
# {"names": ["김하늘"]}
```

## 한계와 주의

- 한국어 인명 전용입니다. 영문 이름·다른 언어는 학습하지 않았습니다.
- 합성 문서로만 학습했으므로 실제 문서의 분포와 다릅니다. 외부 대화 데이터(KDPII)에서는 하이브리드 정밀도가 0.471로, 이름이 아닌 것을 이름으로 가리는 과다 마스킹이 꽤 있습니다. 비식별화 제품에서는 규칙 탐지기와 함께(하이브리드) 쓰고, 결과를 사람이 확인하는 용도로 쓰세요.
- 원문을 그대로 모델에 넣는 구조입니다 — 로컬에서 돌리세요. maskingtape core는 로컬 주소(127.0.0.1)만 허용합니다.

## 라이선스

Apache-2.0 — © 2026 The maskingtape Authors. 기반 모델 Qwen2.5-1.5B-Instruct도 Apache-2.0(Alibaba Cloud Qwen 팀)입니다.
2026 오픈소스 개발자대회 출품작의 일부로, 학습 가중치는 규정에 따라 공개합니다.
