---
language: [ko]
license: cc-by-4.0
task_categories: [token-classification]
tags: [pii, ner, korean, privacy, robustness, evaluation]
source_datasets: [KDPII]
size_categories: [10K<n<100K]
configs:
  - config_name: stress
    data_files: "stress/*.jsonl"
  - config_name: longdoc
    data_files: "longdoc/*.jsonl"
  - config_name: leakage
    data_files: "leakage/*.jsonl"
---

# Veil-PII-Ko Stress Set

한국어 PII 탐지 모델이 **어디서 무너지는지** 보려고 만든 평가셋입니다.
[Veil-PII-Ko-Lite](https://huggingface.co/1T/veil-pii-ko-lite) 를 검증하면서 만들었고, 다른 모델에도 그대로 쓸 수 있습니다.

벤치마크 점수 하나로는 안 보이는 것이 있습니다. 실제로 이 평가셋을 만들다가
512 토큰을 넘는 입력의 뒷부분이 통째로 버려지는 버그를 찾았습니다(3,000자 문서 재현율 0.284 → 0.948).
KDPII 는 한 행이 평균 25자짜리 발화라 창 분할이 한 번도 작동하지 않아서, 점수만 보고 있었으면 못 찾았을 결함입니다.

## 구성

### `stress` — 표기 변형

정답 스팬은 그대로 두고 **표면형만 바꾼 뒤 오프셋을 다시 계산**했습니다.
사람이 라벨을 다시 달 필요가 없으므로 값이 곧 원본 대비 하락폭입니다.
`*_base` 는 변형본과 **같은 행 집합**의 원본이라, 반드시 짝을 지어 비교하셔야 합니다.

| 파일 | 변형 | 예 | 행 |
|---|---|---|---:|
| `stress_sep_dot` | 하이픈 → 점 | `010.1234.5678` | 216 |
| `stress_sep_space` | 하이픈 → 공백 | `010 1234 5678` | 216 |
| `stress_sep_none` | 구분자 제거 | `01012345678` | 216 |
| `stress_fullwidth` | 숫자를 전각으로 | `０１０` | 633 |
| `stress_nospace` | 스팬 내부 공백 제거 | `서울강남구` | 280 |
| `stress_spaced` | 글자 사이 공백 | `홍 길 동` | 1,327 |

### `longdoc` — 문서 길이

KDPII 의 짧은 발화를 이어 붙여 길이만 늘린 문서입니다. 정답 스팬 수(1,604)는 여섯 파일 모두 같아서,
**길이만 바뀌었을 때 재현율이 어떻게 변하는지** 바로 읽을 수 있습니다.

| 파일 | 최대 길이 | 문서 수 |
|---|---:|---:|
| `longdoc_200` | ~200자 | 605 |
| `longdoc_400` | ~400자 | 313 |
| `longdoc_800` | ~800자 | 160 |
| `longdoc_1200` | ~1,200자 | 107 |
| `longdoc_1800` | ~1,800자 | 72 |
| `longdoc_3000` | ~3,000자 | 44 |

한국어는 약 870자가 512 토큰입니다. `longdoc_800` 까지는 창 분할이 안 걸리고 `longdoc_1200` 부터 걸립니다.
이 경계에서 점수가 떨어진다면 슬라이딩 창 구현을 의심하시면 됩니다.

### `leakage` — 학습셋 중복 제거 분할

KDPII 는 train 과 test 사이에 텍스트가 같은 행이 있습니다. 세 단계(원문 / 공백·대소문자 무시 / 숫자 마스킹)로
해시해 대조한 결과, 완전중복 92행(1.88%) · 템플릿중복 108행(2.21%) 이 나왔습니다.
BCCard 쪽은 세 기준 모두 0건입니다.

| 파일 | 내용 | 행 |
|---|---|---:|
| `kdpii_test_dedup` | 완전중복을 뺀 test | 4,799 |
| `kdpii_test_dupsonly` | 완전중복 행만 | 92 |
| `kdpii_test_maskdedup` | 숫자 마스킹 후 중복까지 뺀 test | 4,783 |
| `kdpii_test_maskdupsonly` | 그 중복 행만 | 108 |

완전중복 92건은 전부 정답 스팬이 0개입니다. `알았어.` `정말 죄송합니다, 고객님.` 같은 맞장구가
대화 코퍼스라 양쪽에 걸린 것이라, 빼고 다시 재도 점수가 바뀌지 않습니다.
**누수 여부를 묻는 질문에 이 분할로 답하실 수 있습니다.**

## 스키마

```json
{"id": "kd-test-...", "text": "담당자 김철수(010-1234-5678)에게 문의",
 "lang": "ko", "source": "kdpii", "aug": "stress",
 "spans": [{"start": 4, "end": 7, "label": "PERSON"}]}
```

`start`·`end` 는 원문 기준 문자 인덱스입니다. `text[start:end]` 로 바로 잘라 쓰시면 됩니다.
라벨은 32종이고 스키마는 [모델 카드](https://huggingface.co/1T/veil-pii-ko-lite) 에 있습니다.

## 쓰는 법

```python
from datasets import load_dataset
ds = load_dataset("1T/veil-pii-ko-stress", "stress")
```

변형본과 `_base` 를 각각 채점한 뒤 차이를 보시면 됩니다. 절대값보다 **하락폭**이 읽을 값입니다.
Veil-PII-Ko-Lite 로 잰 결과는 이랬습니다.

| 변형 | 원본 F1 | 변형 F1 | Δ |
|---|---:|---:|---:|
| 하이픈 → 점 | 0.9705 | 0.9686 | −0.2pt |
| 하이픈 → 공백 | 0.9705 | 0.9649 | −0.6pt |
| 구분자 제거 | 0.9705 | 0.8967 | −7.4pt |
| 전각 숫자 | 0.9768 | 0.9768 | 0.0pt |
| 스팬 내부 공백 제거 | 0.9441 | 0.9623 | +1.8pt |
| 글자 사이 공백 | 0.9431 | 0.3321 | **−61.1pt** |

## 다시 만들기

전부 스크립트로 생성했습니다. 시드 없이도 결정적으로 같은 결과가 나옵니다.

```bash
git clone https://github.com/WontaeKim89/veil-pii-ko-lite && cd veil-pii-ko-lite
python eval/make_stress.py --data data/unified/kdpii_test.jsonl --out-dir data/stress
python eval/leakage_check.py --train data/unified/kdpii_train.jsonl \
                             --test  data/unified/kdpii_test.jsonl --dump-dir data/unified
```

## 한계

- 변형은 **기계적으로 만든 것**이라 실제 사용자가 쓰는 우회 표기의 분포와 같지 않습니다.
  이 평가셋의 점수를 "우회 시도에 강하다" 는 근거로 쓰시면 안 됩니다. 표기 변형 여섯 종에서
  하락폭이 얼마였는지까지만 말할 수 있습니다.
- `longdoc` 은 짧은 발화를 이어 붙인 것이라, 실제 계약서나 상담 transcript 의 문체와는 다릅니다.
  창 분할이 제대로 도는지 확인하는 용도입니다.
- 원문은 KDPII 이므로 그 데이터의 도메인(일상 대화)을 그대로 물려받습니다.
  금융·기기 식별자는 거의 나오지 않습니다.

## 출처와 라이선스

CC-BY-4.0. 원문 텍스트는 KDPII 를 따릅니다.

- 원본 데이터: KDPII (CC-BY-4.0, Fei·Kang et al., *IEEE Access*, 2024)
- 변형 설계와 분할 정의: 이 저장소

```bibtex
@misc{veil-pii-ko-stress-2026,
  title  = {Veil-PII-Ko Stress Set: robustness and leakage splits for Korean PII detection},
  author = {Kim, Wontae},
  year   = {2026},
  url    = {https://huggingface.co/datasets/1T/veil-pii-ko-stress}
}
```
