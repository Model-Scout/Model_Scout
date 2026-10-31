---
language: [ko]
license: apache-2.0
task_categories: [token-classification]
tags: [pii, ner, korean, privacy, synthetic]
size_categories: [10K<n<100K]
configs:
  - config_name: default
    data_files:
      - split: train
        path: "train/synth_train.jsonl"
      - split: heldout
        path: "heldout/synth_heldout.jsonl"
  - config_name: templates
    data_files: "templates/templates.jsonl"
---

# Veil-PII-Ko Synthetic

[Veil-PII-Ko-Lite](https://huggingface.co/1T/veil-pii-ko-lite) 학습에 쓴 한국어 PII 합성 데이터입니다.
공개 데이터(BCCard, KDPII)에 없거나 부족한 라벨과 도메인을 채우려고 만들었습니다.

`train` 은 공개 모델이 **실제로 학습한 행 그대로**이고, `heldout` 은 모델 카드 벤치마크 표의
"합성 heldout v2" (n=670) 입니다. 다시 뽑은 데이터가 아니라 학습 당시 파일에서 꺼낸 것이라, 공개한 수치와 바로 맞춰 보실 수 있습니다.

## 구성

| config / split | 내용 | 행 |
|---|---|---:|
| `default` / `train` | 합성 학습 데이터 | 26,875 |
| `default` / `heldout` | 합성 평가 데이터. 32 라벨을 모두 포함 | 670 |
| `templates` | 값을 채우기 전 플레이스홀더 템플릿 | 10,133 |

## 만든 방법

두 단계로 나눴습니다. 문장은 LLM 에게 맡기고, 개인정보 값은 규칙 기반 생성기로 넣었습니다.
LLM 이 번호를 직접 쓰게 하면 형식이 틀리거나 라벨 위치가 어긋나는 경우가 많았기 때문입니다.

1. **템플릿 생성** — LLM(gemma-4-12b-it, Azure OpenAI)으로 21개 장르 × 여러 문체의 문장을 만들고,
   개인정보 자리는 `{PERSON}` `{PHONE}` 같은 플레이스홀더로 비워 뒀습니다.
2. **값 채우기** — 한국 포맷에 맞춘 생성기로 채웠습니다. 주민번호는 2020년 10월 전후 체계를 모두 반영했고,
   카드번호는 Luhn, 사업자번호는 검증번호까지 맞췄습니다. 값을 넣으면서 스팬 위치를 같이 기록하므로 라벨이 어긋나지 않습니다.

`heldout` 은 **템플릿 단위로** 떼어 냈습니다. 같은 템플릿에서 값만 바꾼 문장이 학습과 평가에 동시에 들어가지 않습니다.
여기에 더해 평가셋과 12-gram 이 3개 이상 겹치는 학습 행을 걸러 냈고(30,961 → 26,875행), `heldout` 과 `train` 의 텍스트 완전중복은 0건입니다.

생성 코드는 GitHub 에 있습니다 — [`data/synth_templates.py`](https://github.com/WontaeKim89/veil-pii-ko-lite/blob/main/data/synth_templates.py),
[`synth_fill.py`](https://github.com/WontaeKim89/veil-pii-ko-lite/blob/main/data/synth_fill.py),
[`gen_entities.py`](https://github.com/WontaeKim89/veil-pii-ko-lite/blob/main/data/gen_entities.py).

## 스키마

```json
{"id": "synth-...", "text": "담당자 김철수(010-1234-5678)에게 문의",
 "lang": "ko", "source": "synth", "aug": "none",
 "spans": [{"start": 4, "end": 7, "label": "PERSON"}, {"start": 8, "end": 21, "label": "PHONE"}]}
```

`start`·`end` 는 원문 기준 문자 인덱스라 `text[start:end]` 로 바로 잘라 쓰시면 됩니다.
라벨 32종은 [모델 카드](https://huggingface.co/1T/veil-pii-ko-lite) 와 같습니다.

`templates` 는 `{"genre", "style", "text"}` 형태이고 `text` 안에 플레이스홀더가 들어 있습니다.
생성기를 바꿔 새 값을 채우고 싶으실 때 쓰시면 됩니다.

## 쓰는 법

```python
from datasets import load_dataset
ds = load_dataset("1T/veil-pii-ko-synth")          # train / heldout
tpl = load_dataset("1T/veil-pii-ko-synth", "templates")
```

## 한계

- 합성 데이터라 **실제 문장보다 깔끔합니다.** 오타, 띄어쓰기 파괴, 구어체 우회 표기가 거의 없습니다.
  이 데이터의 `heldout` 점수는 실사용 성능이 아니라, 32 라벨을 고르게 잡는지 보는 용도로 읽어 주세요.
- 문장은 LLM 이 만든 것이라 장르별 말투가 비슷하게 반복되는 경향이 있습니다.
- 값은 생성기로 만든 임의 값이고 실제 인물·계좌와 대조하지 않았습니다. 이메일 주소는 실제로 쓰이는
  도메인(gmail.com, naver.com 등)에 임의의 아이디를 붙인 것이라, 우연히 존재하는 주소와 겹칠 수 있습니다.

## 라이선스

Apache 2.0.

```bibtex
@misc{veil-pii-ko-synth-2026,
  title  = {Veil-PII-Ko Synthetic: synthetic Korean PII data with 32 labels},
  author = {Kim, Wontae},
  year   = {2026},
  url    = {https://huggingface.co/datasets/1T/veil-pii-ko-synth}
}
```
