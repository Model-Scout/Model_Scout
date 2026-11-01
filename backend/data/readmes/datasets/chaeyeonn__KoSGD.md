---
language:
- ko
license: cc-by-sa-4.0
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test/dialogues_*.json
task_categories:
- text-classification
- token-classification
- question-answering
- text-generation
- zero-shot-classification
tags:
- SGD
- NLU
- DST
- NER
- Intent
- QA
pretty_name: KoSGD
---

# KoSGD: Korean Schema-Guided Dialogue Dataset

**KoSGD**는 Google Research의 [Schema-Guided Dialogue(SGD)](https://arxiv.org/abs/1909.05855) 데이터셋을 한국어로 변환한 대규모 Task-Oriented Dialogue(ToD) 데이터셋입니다.

기존의 목적 지향 대화(ToD) 데이터셋은 고정된 도메인 내에서만 작동하는 경우가 많았습니다. Google의 SGD 데이터셋은 **'Schema-Guided'** 방식을 도입하여, 새로운 서비스 스키마만 주어지면 모델이 Zero-shot으로 대응할 수 있도록 설계되었습니다.

**KoSGD는 왜 만들어졌나요?**
- **한국어 일반화 성능 평가**: 한국어 LLM이 다양한 도메인(21개 이상)에서 스키마를 얼마나 정확히 이해하고 태스크를 수행하는지 측정하기 위함입니다.
- **고도화된 번역 및 검수**: 기계 번역 후 전문 인력이 **전수 휴먼 검수**를 진행하여, 구어체 표현의 자연스러움과 ToD 특유의 논리적 연결성을 확보했습니다.
- **원본 오류 수정**: 번역 과정에서 발견된 원본 SGD의 어노테이션 불일치와 오류를 대폭 수정하여 데이터 품질을 높였습니다.


---

## Dataset Overview

KoSGD는 한국어 LLM이 다중 도메인(21개 이상) 환경에서 얼마나 유연하게 대화 상태를 추적하고 적절한 응답을 생성하는지 종합적으로 평가하기 위해 설계되었습니다. 단순 번역을 넘어선 전수 검수를 통해 고품질의 한국어 대화 데이터를 제공합니다.

| Key | Description |
| :--- | :--- |
| **Dataset Name** | KoSGD (Korean Schema-Guided Dialogue) |
| **Data Type** | 다중 도메인 목적 지향 대화 (ToD) 데이터셋 |
| **Domains** | 21개 서비스 (알람, 호텔, 식당, 항공, 날씨 등) |
| **Size** | 총 84,594 턴 (Test set 기준) |
| **Methodology** | 기계 번역 + **전문 검수 인력 전수 교정** |
| **Improvements** | 원본 어노테이션 오류 수정 및 한국어 정규화 값(Canonical Value) 최적화 |
| **License** | CC BY-SA 4.0 |

---

## Key Concepts

### Canonical Value vs Value

| 용어 | 정의 | 예시 |
|:-----|:-----|:-----|
| **Value** | 사용자 발화에서 원문 그대로 추출한 값 | `"8일"`, `"오후 12시"` |
| **Canonical Value** | 슬롯에 대해 사전 정의된 정규화 값 | `"2019-03-08"`, `"12:00"` |

---

## Benchmark Evaluation

본 벤치마크 평가는 실시간 응답이 가능한 Local 및 API 모델을 대상으로 수행하였습니다. 수치 해석의 참고를 위해 일부 대형모델 (GPT5, Gemini 3 Pro 등)도 함께 포함하였습니다. 

**open source 모델** (8B~20B 규모 비추론 모델, 추론 모델일 경우 비추론 모드 설정)
```
temperature: 0.7 | top_p: 0.8 | top_k: 20 | min_p: 0 | max_tokens: 4096
```

**proprietary 모델**: 모델명만 지정, 그 외 파라미터는 API 기본값 사용 (접속일자: 2025/12/26)

### KoSGD Dataset

| Type | Model | Intent Cls. | Action Cls. | Val\|Inform* | I-A Harm Mean** |
|------|-------|-------------|-------------|-------------|---------------|
| open source | meta-llama/Meta-Llama-3.1-8B-Instruct | 54.4 | 46.2 | 57.0 | 50.0 |
| open source | microsoft/phi-4 | 76.6 | 72.2 | 87.5 | 78.3 |
| open source | google/gemma-3-12b-it | 62.6 | 64.0 | 75.6 | 66.9 |
| open source | Qwen/Qwen3-14B | 75.4 | 71.7 | 82.1 | 76.2 |
| - | **aiworkx/nlu-14B (Ours)** | **90.9** | **97.7** | 94.1 | **94.2** |
| proprietary | OpenAI/GPT-5-nano | 77.5 | 70.7 | 92.2 | 79.2 |
| proprietary | OpenAI/GPT-5-mini | 83.3 | 77.2 | 96.6 | 85.0 |
| proprietary | OpenAI/GPT-5 | 84.1 | 81.2 | 99.1 | 87.5 |
| proprietary | OpenAI/GPT-5.1 | 82.7 | 71.5 | 98.3 | 82.8 |
| proprietary | Google/gemini-3-flash-preview | 79.1 | 76.0 | 99.1 | 83.6 |
| proprietary | Google/gemini-3-pro-preview | 86.4 | 66.5 | 99.2 | 81.8 |

```
- Val|Inform*: 모델이 `action`을 `INFORM`으로 예측한 경우에 한하여, `values`까지 정확하게 예측했는지 평가; 조건부 정확도이므로, Action 성능이 낮은 경우 높은 Value Accuracy가 전체 추출 성능을 대표하지 않을 수 있음.
- I-A Harm Mean**: Intent, Action 정확도에 대한 조화평균.
```
<details>
<summary><b>Intent Classification</b></summary>

평가는 예측된(Predicted) 리스트와 정답(Ground Truth) 리스트 간의 요소별 매칭을 통해 이루어집니다. 순서와 관계없이 비교합니다.

**Intent Accuracy**
- **정의**: 모델이 `intent` 배열을 정확하게 예측했는지 평가
- **조건**: 예측된 `intent` 목록이 정답 리스트와 모두 일치할 경우 정답. 정답 리스트에 없는 `intent`가 포함되면 오답.
</details>

<details>
<summary><b>Action-Value Extraction</b></summary>

평가는 예측된(Predicted) 리스트와 정답(Ground Truth) 리스트 간의 요소별 매칭을 통해 이루어집니다. 순서와 관계없이 비교합니다.

**A. Action Accuracy**
- **정의**: 모델이 `act`와 `slot` 쌍을 정확하게 예측했는지 평가
- **조건**: 예측된 `(act, slot)` 쌍이 정답 리스트에 존재하면 정답

**B. Value Accuracy (Val|Inform)**
- **정의**: 모델이 `act`를 `INFORM`으로 예측한 경우에 한하여, `values`까지 정확하게 예측했는지 평가
- **수식**: P(Value Correct | Predicted Action = INFORM)
- **조건**:
  1. 모델이 `act`를 `INFORM`으로 예측
  2. 예측된 `values` 리스트의 구성 요소가 정답과 일치
- **해석**: 조건부 정확도이므로, Action 성능이 낮은 경우 높은 Value Accuracy가 전체 추출 성능을 대표하지 않을 수 있음
- **Note**: 전체 INFORM 샘플에 대한 Value Extraction 성능은 정리 후 공개 예정
</details>

### aiworkx/FIN-NLU-200K

| Type | Model | Intent Cls. | Action Cls. | Val\|Inform* | I-A Harm Mean** |
|------|-------|-------------|-------------|-------------|---------------|
| open source | meta-llama/Meta-Llama-3.1-8B-Instruct | 67.4 | 40.5 | 25.9 | 50.6 |
| open source | microsoft/phi-4 | 78.7 | 73.2 | 57.9 | 75.9 |
| open source | google/gemma-3-12b-it | 53.4 | 63.2 | 42.4 | 57.9 |
| open source | Qwen/Qwen3-14B | 85.3 | 79.5 | 59.5 | 82.3 |
| - | **aiworkx/nlu-14B (Ours)** | **98.7** | **91.5** | 86.2 | **95.0** |
| proprietary | OpenAI/GPT-5-nano | 95.3 | 82.7 | 77.4 | 88.6 |
| proprietary | OpenAI/GPT-5-mini | 96.3 | 85.4 | 86.8 | 90.5 |
| proprietary | OpenAI/GPT-5 | 83.4 | 86.0 | 93.7 | 84.7 |
| proprietary | OpenAI/GPT-5.1 | 90.5 | 88.9 | 84.8 | 89.7 |
| proprietary | Google/gemini-3-flash-preview | 95.8 | 88.2 | 92.8 | 91.8 |
| proprietary | Google/gemini-3-pro-preview | 86.6 | 86.1 | 95.0 | 86.3 |

```
- Val|Inform*: 모델이 `action`을 `INFORM`으로 예측한 경우에 한하여, `values`까지 정확하게 예측했는지 평가; 조건부 정확도이므로, Action 성능이 낮은 경우 높은 Value Accuracy가 전체 추출 성능을 대표하지 않을 수 있음.
- I-A Harm Mean**: Intent, Action 정확도에 대한 조화평균.
```
<details>

<summary><b>aiworkx/FIN-NLU-200K </b></summary>

aiworkx/FIN-NLU-200K는 TOD 기반 금융 상담 에이전트의 NLU 모듈 성능 평가를 위해 AIWORKX에서 자체 설계/구축한 약 200K 규모의 금융권 의도 분류 학습/평가 데이터셋입니다. 본 레포지토리에서는 데이터셋 원문은 공개하지 않으며, 평가 결과 수치만 공유합니다.

**평가 목표**
- 금융 상담 맥락에서 사용자 의도의 정확한 이해
- 에이전트의 다음 행동 결정을 위한 발화 구분 능력
- 한국어 구어체/모호적 표현에서의 정규화된 값 추출 능력

**데이터 구조**: 실제 상담 흐름을 반영한 1-turn 대화 구조
- 상담사 발화 (agent utterance)
- 고객 발화 (user utterance)
- ontology (분류 및 추출 규칙 상세 및 Intent/Action/Value)

</details>

---

## Dataset Details

<details>
<summary><b>Service (Domain) List</b></summary>

| 서비스 | 원본 SGD | 설명 |
|:-------|:---------|:-----|
| 알람_1 | Alarm_1 | 알람을 쉽게 가져오고 설정 및 관리 |
| 버스_3 | Buses_3 | 저렴하고 편안한 전국 버스 여행 |
| 이벤트_3 | Events_3 | 지역 문화 행사 티켓 검색 및 예약 |
| 비행_4 | Flights_4 | 저렴한 항공편 검색 및 예약 |
| 집_2 | Homes_2 | 구매 및 임대할 부동산 검색 서비스 |
| 호텔_2 | Hotels_2 | 단기 체류를 위한 숙소 검색 및 예약 |
| 호텔_4 | Hotels_4 | 숙박 검색 및 예약 포털 |
| 미디어_3 | Media_3 | 드라마, 영화, 다큐멘터리 등 무제한 스트리밍 |
| 메세지_1 | Messaging_1 | 연락처와 연결 및 위치 공유 |
| 영화_1 | Movies_1 | 영화 검색, 상영 시간 확인, 티켓 예약 |
| 영화_3 | Movies_3 | 영화 및 TV 리뷰 집계 |
| 음악_3 | Music_3 | 맞춤형 무료 음악 스트리밍 플랫폼 |
| 결제_1 | Payment_1 | 앱, 웹, 스토어에서 빠르고 간편한 결제 |
| 차량렌트_3 | RentalCars_3 | 글로벌 렌터카 솔루션 |
| 식당_2 | Restaurants_2 | 레스토랑 검색 및 예약 서비스 |
| 승차공유_2 | RideSharing_2 | 목적지까지 택시 예약 |
| 서비스_1 | Services_1 | 헤어 스타일리스트 검색 및 예약 |
| 서비스_4 | Services_4 | 심리상담사 검색 및 예약 |
| 열차_1 | Trains_1 | 도시 간 기차 여행 검색 및 예약 |
| 여행_1 | Travel_1 | 관광 명소와 관심 지점 데이터베이스 |
| 날씨_1 | Weather_1 | 특정 장소와 날짜에 대한 날씨 확인 |
</details>

<details>
<summary><b>Data Structure</b></summary>

### 파일 구성

```
KoSGD/
├── dialogues_001.json ~ dialogues_034.json   # 대화 데이터 (34개)
└── extended_schema.json                       # 서비스 스키마 정의
```

### 대화 데이터 구조

```json
{
  "dialogue_id": "1_00000",
  "services": ["식당_2"],
  "turns": [
    {
      "speaker": "USER",
      "utterance": "안녕하세요. 8일에 식당 예약 좀 부탁드려도 될까요?",
      "frames": [{
        "service": "식당_2",
        "actions": [{
          "act": "INFORM",
          "slot": "예약일",
          "values": ["8일"],
          "canonical_values": ["2019-03-08"]
        }],
        "slots": [{"slot": "예약일", "start": 7, "exclusive_end": 9}],
        "state": {
          "active_intent": "ReserveRestaurant",
          "requested_slots": [],
          "slot_values": {"예약일": ["8일"]}
        }
      }]
    }
  ]
}
```

### Action 유형

| Act | 설명 | 사용 주체 |
|:----|:-----|:----------|
| `INFORM` | 슬롯 값 제공 | USER, SYSTEM |
| `INFORM_INTENT` | 의도 표현 | USER |
| `REQUEST` | 슬롯 값 요청 | USER, SYSTEM |
| `CONFIRM` | 값 확인 요청 | SYSTEM |
| `AFFIRM` / `NEGATE` | 긍정/부정 응답 | USER |
| `SELECT` | 선택지에서 선택 | USER |
| `OFFER` | 옵션 제안 | SYSTEM |
| `NOTIFY_SUCCESS` / `NOTIFY_FAILURE` | 작업 성공/실패 알림 | SYSTEM |
| `REQ_MORE` | 추가 요청 확인 | SYSTEM |
| `GOODBYE` / `THANK_YOU` | 대화 종료/감사 | USER, SYSTEM |

### 스키마 정의 구조

```json
{
  "service_name": "알람_1",
  "description": "알람을 쉽게 가져오고 설정 및 관리",
  "slots": [{
    "name": "알람_시간",
    "description": "알람이 설정된 시간",
    "is_categorical": false,
    "possible_values": ["06:00", "06:30", ...]
  }],
  "intents": [{
    "name": "AddAlarm",
    "description": "새 알람 설정하기",
    "is_transactional": true,
    "required_slots": ["새_알람_시간"],
    "optional_slots": {"새_알람_이름": "새 알람"},
    "result_slots": ["새_알람_시간", "새_알람_이름"]
  }]
}
```
기존 SGD 데이터셋과 다르게, extended_schema파일에서 is_categorical의 값이 false인 경우에도 Action에서 사용하는 Canonical Values를 수집해서 제공합니다.
</details>

---

## Citation

### Original SGD Dataset (Google Research)

```bibtex
@inproceedings{rastogi2020towards,
  title={Towards scalable multi-domain conversational agents: The schema-guided dialogue dataset},
  author={Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},
  booktitle={Proceedings of the AAAI conference on artificial intelligence},
  volume={34},
  number={05},
  pages={8689--8696},
  year={2020}
}
```

### KoSGD Dataset (AIWORKX)

```bibtex
@misc{AIWORKX_KOSGD,
  author = {AIWORKX},
  title = {KoSGD: Korean Schema-Guided Dialogue ToD Dataset},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/AIWORKX/KoSGD},
}
```

---

## Additional Notes

- Train 데이터셋은 추후 공개 예정입니다.