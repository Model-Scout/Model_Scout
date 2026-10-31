---
language:
- ko
- en
license: other
license_name: original-dataset-license
license_link: https://huggingface.co/datasets/DeepPavlov/clinc150
tags:
- korean
- translation
- text-classification
- intent-classification
- conversational-ai
- out-of-scope-detection
dataset_info:
  features:
  - name: utterance
    dtype: string
  - name: label
    dtype: int64
  - name: text
    dtype: string
  - name: text_original
    dtype: string
  splits:
  - name: train
    num_bytes: 2496741
    num_examples: 15200
  - name: validation
    num_bytes: 466918
    num_examples: 3100
  - name: test
    num_bytes: 837764
    num_examples: 5500
  download_size: 1633508
  dataset_size: 3801423
source_datasets:
- DeepPavlov/clinc150
task_categories:
- text-classification
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
pretty_name: "CLINC150-ko (한국어 번역 버전)"
---

<!-- aegis-dataset-card -->

# clinc150-ko

> **학습용** · CLINC150-ko (한국어 번역 버전)  
> 파일 7개 · 6.5 MB · 행 47,600 · revision `2360c8e67b` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
이 데이터셋은 [DeepPavlov/clinc150](https://huggingface.co/datasets/DeepPavlov/clinc150) 데이터셋의 **한국어 번역 버전**입니다.

## 이 데이터로 학습한 모델
| 모델 | 관계 | 사용 부분 | 비고 |
|---|---|---|---|
| [`neuralfoundry-coder/aegis-unified-v4_260927`](https://huggingface.co/neuralfoundry-coder/aegis-unified-v4_260927) | 학습(가공 후) | 전체 | v5g 원천 |
| [`neuralfoundry-coder/aegis-guard-encoder-v7_261011`](https://huggingface.co/neuralfoundry-coder/aegis-guard-encoder-v7_261011) | 학습(가공 후) | 전체 | 등록 원천(직접 반영 0행 — batch1 경유) |
| [`neuralfoundry-coder/aegis-guard-encoder-v8_261011`](https://huggingface.co/neuralfoundry-coder/aegis-guard-encoder-v8_261011) | 학습(가공 후) | 전체 | 승인 1차 원천 |
| [`neuralfoundry-coder/aegis-guard-encoder-v11_261015`](https://huggingface.co/neuralfoundry-coder/aegis-guard-encoder-v11_261015) | 학습(가공 후) | 전체 | 승인 1차 원천 |
| [`neuralfoundry-coder/aegis-guard-encoder-v12_261019`](https://huggingface.co/neuralfoundry-coder/aegis-guard-encoder-v12_261019) | 학습(가공 후) | 전체 | 승인 1차 원천 |
| [`neuralfoundry-coder/aegis-guard-gen-0.6b-v3_261011`](https://huggingface.co/neuralfoundry-coder/aegis-guard-gen-0.6b-v3_261011) | 학습(가공 후) | 전체 | 승인 1차 원천 |
| [`neuralfoundry-coder/aegis-guard-gen-0.6b-v4_261011`](https://huggingface.co/neuralfoundry-coder/aegis-guard-gen-0.6b-v4_261011) | 학습(가공 후) | 전체 | 승인 1차 원천 |
| [`neuralfoundry-coder/aegis-guard-l2-finance-3b-v3_261011`](https://huggingface.co/neuralfoundry-coder/aegis-guard-l2-finance-3b-v3_261011) | 학습(가공 후) | 전체 | 승인 1차 원천 |
| [`neuralfoundry-coder/aegis-guard-l2-finance-3b-v4_261011`](https://huggingface.co/neuralfoundry-coder/aegis-guard-l2-finance-3b-v4_261011) | 학습(가공 후) | 전체 | 승인 1차 원천 |
| [`neuralfoundry-coder/aegis-guard-l2-finance-3b-v7_261015`](https://huggingface.co/neuralfoundry-coder/aegis-guard-l2-finance-3b-v7_261015) | 학습(가공 후) | 전체 | 승인 1차 원천 |
| [`neuralfoundry-coder/aegis-guard-l2-finance-3b-v12_261019`](https://huggingface.co/neuralfoundry-coder/aegis-guard-l2-finance-3b-v12_261019) | 학습(가공 후) | 전체 | 승인 1차 원천 |
| [`neuralfoundry-coder/aegis-unified-onnx-v4_260927`](https://huggingface.co/neuralfoundry-coder/aegis-unified-onnx-v4_260927) | 학습(가공 후) | 전체 | v5g 원천 |

관계: 학습(직접) = 이 파일을 그대로 학습에 씀 · 학습(가공 후) = 코퍼스 · SFT 혼합을 만드는 입력(재생성 방법은 카탈로그) · 생성 입력(원본) = 합성 · 정리 단계의 원본 기록.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 18.2 KB | - |  |
| `data/clinc150_ko_test_20260112_135130.jsonl` | 1.1 MB | 5,500 |  |
| `data/clinc150_ko_train_20260112_135130.jsonl` | 3.2 MB | 15,200 |  |
| `data/clinc150_ko_validation_20260112_135130.jsonl` | 603.9 KB | 3,100 |  |
| `data/test-00000-of-00001.parquet` | 387.8 KB | 5,500 |  |
| `data/train-00000-of-00001.parquet` | 1.0 MB | 15,200 |  |
| `data/validation-00000-of-00001.parquet` | 211.4 KB | 3,100 |  |

## 필드 · 범주 분포
**`data/clinc150_ko_test_20260112_135130.jsonl`, `data/clinc150_ko_train_20260112_135130.jsonl`, `data/clinc150_ko_validation_20260112_135130.jsonl`, `data/test-00000-of-00001.parquet`, `data/train-00000-of-00001.parquet`, `data/validation-00000-of-00001.parquet`** (기준 `data/clinc150_ko_train_20260112_135130.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `utterance` | str | 100% |
| `label` | int · NoneType | 100% |
| `text` | str | 100% |
| `text_original` | str | 100% |

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 출처 · 라이선스 · 등록
- aegis-guard-train 등록부 `neuralfoundry-coder/clinc150-ko` · role train · revision 2360c8e67b
- 항목별 출처 · 라이선스는 아래 기존 설명과 항목 필드를 따른다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/clinc150-ko --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### CLINC150-ko (한국어 번역 버전)

#### 개요

이 데이터셋은 [DeepPavlov/clinc150](https://huggingface.co/datasets/DeepPavlov/clinc150) 데이터셋의 **한국어 번역 버전**입니다.

CLINC150은 150개의 인텐트(의도) 분류와 Out-of-Scope(범위 외) 탐지를 위한 대규모 벤치마크 데이터셋입니다. 다양한 도메인(banking, travel, kitchen, work, auto 등)의 사용자 질의를 포함하며, 대화형 AI 시스템의 의도 분류 및 범위 외 탐지 성능 평가에 널리 사용됩니다.

이 번역 버전은 한국어 텍스트 분류, 인텐트 분류 모델의 학습 및 평가, 한국어 챗봇 개발 등에 활용할 수 있도록 제작되었습니다.

#### 데이터셋 정보

| 항목 | 내용 |
|------|------|
| **원본 데이터셋** | [DeepPavlov/clinc150](https://huggingface.co/datasets/DeepPavlov/clinc150) |
| **원본 출처** | [An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction](https://arxiv.org/abs/1909.02027) |
| **데이터 크기** | Train: 15,200개 / Validation: 3,100개 / Test: 5,500개 |
| **총 샘플 수** | 23,800개 |
| **언어** | 한국어 (Korean) |
| **분류 클래스** | 150개 인텐트 + 1개 Out-of-Scope |
| **번역 일자** | 2026년 1월 |

#### 번역 방법론

##### 번역 도구
- **번역 엔진**: LLM 기반 번역 API (로컬 서버)
- **동시 처리**: 100건 병렬 요청 (ThreadPoolExecutor)
- **품질 관리**: 자동 재시도 메커니즘 (최대 3회)
- **모니터링**: 60초 간격 진행 상황 출력

##### 번역 원칙

CLINC150 데이터셋의 다양한 도메인 특성을 고려하여 다음 원칙을 적용하였습니다:

1. **자연스러운 한국어 표현**
   - 한국어 화자가 일상 대화에서 실제로 사용하는 자연스러운 표현으로 번역
   - 구어체 질의의 특성 유지

2. **도메인별 용어 현지화**
   - **Banking/Finance**: "계좌", "이체", "잔액", "대출", "카드"
   - **Travel**: "항공편", "예약", "호텔", "여행"
   - **Kitchen/Food**: "레시피", "요리", "음식", "식당"
   - **Work/Office**: "회의", "일정", "업무", "프로젝트"
   - **Auto/Transport**: "자동차", "주유", "정비", "운전"
   - **General/Utility**: "날씨", "시간", "알람", "일정"

3. **보존 요소**
   - 숫자, 날짜, 고유명사, 특정 이름은 원본 그대로 유지
   - 질문의 의도와 톤 보존
   - Out-of-Scope 질의는 자연스러운 번역 유지

##### 번역 프롬프트

```
You are an expert translator specializing in conversational AI and user queries.
Your task is to translate English user queries to natural Korean while following these rules:

TRANSLATION GUIDELINES:
1. Translate to natural, fluent Korean as a Korean speaker would say in daily conversation
2. Maintain the conversational tone and intent of the original query
3. Use appropriate Korean expressions for different domains
4. Keep numbers, dates, proper nouns, and specific names as-is
5. For out-of-scope queries, translate literally while maintaining naturalness
6. Do not add any explanations - output only the Korean translation
```

##### 번역 대상 필드

| 필드 | 설명 | 번역 여부 |
|------|------|----------|
| `text` | 사용자 질의 (번역된 한국어) | ✅ 새로 생성 |
| `text_original` | 사용자 질의 (원본 영어) | ✅ 원본 복사 |
| `utterance` | 원본 발화 (영어) | ❌ 원본 유지 |
| `label` | 인텐트 분류 ID (0-150) | ❌ 원본 유지 |

#### 데이터 구조

```json
{
  "text": "레드로빈에 예약할 수 있나요?",
  "text_original": "can i make a reservation for redrobin",
  "utterance": "can i make a reservation for redrobin",
  "label": 0
}
```

#### 10개 도메인 및 150개 인텐트 분류

CLINC150 데이터셋은 10개의 도메인과 각 도메인당 15개의 인텐트로 구성됩니다:

<details>
<summary>전체 도메인 및 인텐트 목록 보기</summary>

##### Banking (금융)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 0 | transfer | 이체 |
| 1 | transactions | 거래내역 |
| 2 | balance | 잔액조회 |
| 3 | freeze_account | 계좌동결 |
| 4 | pay_bill | 청구서 결제 |
| 5 | bill_balance | 청구서 잔액 |
| 6 | bill_due | 청구서 만기 |
| 7 | interest_rate | 이자율 |
| 8 | routing | 라우팅번호 |
| 9 | min_payment | 최소결제 |
| 10 | order_checks | 수표 주문 |
| 11 | pin_change | PIN 변경 |
| 12 | report_fraud | 사기 신고 |
| 13 | account_blocked | 계좌 차단 |
| 14 | spending_history | 지출 내역 |

##### Credit Cards (신용카드)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 15 | credit_score | 신용점수 |
| 16 | report_lost_card | 카드분실 신고 |
| 17 | credit_limit | 신용한도 |
| 18 | rewards_balance | 리워드 잔액 |
| 19 | new_card | 새 카드 |
| 20 | application_status | 신청 상태 |
| 21 | card_declined | 카드 거절 |
| 22 | international_fees | 해외 수수료 |
| 23 | apr | 연이율 |
| 24 | redeem_rewards | 리워드 교환 |
| 25 | credit_limit_change | 신용한도 변경 |
| 26 | damaged_card | 손상된 카드 |
| 27 | replacement_card_duration | 재발급 기간 |
| 28 | improve_credit_score | 신용점수 개선 |
| 29 | expiration_date | 만료일 |

##### Kitchen & Dining (주방/식사)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 30 | recipe | 레시피 |
| 31 | restaurant_reviews | 식당 리뷰 |
| 32 | calories | 칼로리 |
| 33 | nutrition_info | 영양정보 |
| 34 | restaurant_suggestion | 식당 추천 |
| 35 | ingredients_list | 재료 목록 |
| 36 | ingredient_substitution | 재료 대체 |
| 37 | cook_time | 조리시간 |
| 38 | food_last | 음식 유통기한 |
| 39 | meal_suggestion | 식사 추천 |
| 40 | restaurant_reservation | 식당 예약 |
| 41 | confirm_reservation | 예약 확인 |
| 42 | how_busy | 혼잡도 |
| 43 | cancel_reservation | 예약 취소 |
| 44 | accept_reservations | 예약 가능 여부 |

##### Home (가정)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 45 | shopping_list | 쇼핑 목록 |
| 46 | shopping_list_update | 쇼핑 목록 수정 |
| 47 | next_song | 다음 노래 |
| 48 | play_music | 음악 재생 |
| 49 | update_playlist | 재생목록 수정 |
| 50 | todo_list | 할일 목록 |
| 51 | todo_list_update | 할일 수정 |
| 52 | calendar | 달력 |
| 53 | calendar_update | 달력 수정 |
| 54 | what_song | 현재 노래 |
| 55 | order | 주문 |
| 56 | order_status | 주문 상태 |
| 57 | reminder | 리마인더 |
| 58 | reminder_update | 리마인더 수정 |
| 59 | smart_home | 스마트홈 |

##### Auto & Commute (자동차/출퇴근)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 60 | traffic | 교통 |
| 61 | directions | 길안내 |
| 62 | gas | 주유 |
| 63 | gas_type | 유종 |
| 64 | distance | 거리 |
| 65 | current_location | 현재 위치 |
| 66 | mpg | 연비 |
| 67 | oil_change_when | 오일교환 시기 |
| 68 | oil_change_how | 오일교환 방법 |
| 69 | jump_start | 점프스타트 |
| 70 | uber | 우버 |
| 71 | schedule_maintenance | 정비 예약 |
| 72 | last_maintenance | 최근 정비 |
| 73 | tire_pressure | 타이어 압력 |
| 74 | tire_change | 타이어 교체 |

##### Travel (여행)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 75 | book_flight | 항공편 예약 |
| 76 | book_hotel | 호텔 예약 |
| 77 | car_rental | 렌터카 |
| 78 | travel_suggestion | 여행 추천 |
| 79 | travel_alert | 여행 경보 |
| 80 | travel_notification | 여행 알림 |
| 81 | carry_on | 기내 반입 |
| 82 | timezone | 시간대 |
| 83 | vaccines | 백신 |
| 84 | translate | 번역 |
| 85 | flight_status | 항공편 상태 |
| 86 | international_visa | 비자 |
| 87 | lost_luggage | 수하물 분실 |
| 88 | plug_type | 플러그 타입 |
| 89 | exchange_rate | 환율 |

##### Utility (유틸리티)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 90 | time | 시간 |
| 91 | alarm | 알람 |
| 92 | share_location | 위치 공유 |
| 93 | find_phone | 폰 찾기 |
| 94 | weather | 날씨 |
| 95 | text | 문자 |
| 96 | spelling | 철자 |
| 97 | make_call | 전화 걸기 |
| 98 | timer | 타이머 |
| 99 | date | 날짜 |
| 100 | calculator | 계산기 |
| 101 | measurement_conversion | 단위 변환 |
| 102 | flip_coin | 동전 던지기 |
| 103 | roll_dice | 주사위 굴리기 |
| 104 | definition | 정의 |

##### Work (업무)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 105 | direct_deposit | 급여 입금 |
| 106 | pto_request | 휴가 신청 |
| 107 | taxes | 세금 |
| 108 | payday | 급여일 |
| 109 | w2 | W2 양식 |
| 110 | pto_balance | 휴가 잔여일 |
| 111 | pto_request_status | 휴가 신청 상태 |
| 112 | next_holiday | 다음 휴일 |
| 113 | insurance | 보험 |
| 114 | insurance_change | 보험 변경 |
| 115 | schedule_meeting | 회의 예약 |
| 116 | pto_used | 사용한 휴가 |
| 117 | meeting_schedule | 회의 일정 |
| 118 | rollover_401k | 401k 이전 |
| 119 | income | 소득 |

##### Small Talk (일상대화)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 120 | greeting | 인사 |
| 121 | goodbye | 작별 |
| 122 | tell_joke | 농담 |
| 123 | where_are_you_from | 출신지 |
| 124 | how_old_are_you | 나이 |
| 125 | what_is_your_name | 이름 |
| 126 | who_made_you | 제작자 |
| 127 | thank_you | 감사 |
| 128 | what_can_i_ask_you | 질문 가능 범위 |
| 129 | what_are_your_hobbies | 취미 |
| 130 | do_you_have_pets | 반려동물 |
| 131 | are_you_a_bot | 봇 여부 |
| 132 | meaning_of_life | 삶의 의미 |
| 133 | who_do_you_work_for | 소속 |
| 134 | fun_fact | 재미있는 사실 |

##### Meta (메타)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 135 | change_ai_name | AI 이름 변경 |
| 136 | change_user_name | 사용자 이름 변경 |
| 137 | cancel | 취소 |
| 138 | user_name | 사용자 이름 |
| 139 | reset_settings | 설정 초기화 |
| 140 | whisper_mode | 속삭임 모드 |
| 141 | repeat | 반복 |
| 142 | no | 아니요 |
| 143 | yes | 예 |
| 144 | maybe | 아마도 |
| 145 | change_language | 언어 변경 |
| 146 | change_accent | 억양 변경 |
| 147 | change_volume | 볼륨 변경 |
| 148 | change_speed | 속도 변경 |
| 149 | sync_device | 기기 동기화 |

##### Out-of-Scope (범위 외)
| ID | 인텐트 | 설명 |
|----|--------|------|
| 150 | oos | 범위 외 질의 |

</details>

#### 라이선스 및 저작권

##### 원본 라이선스 귀속

**이 데이터셋은 원본 데이터셋 [DeepPavlov/clinc150](https://huggingface.co/datasets/DeepPavlov/clinc150)의 라이선스를 따릅니다.**

- 원본 데이터셋의 모든 라이선스 조건이 이 번역 버전에도 동일하게 적용됩니다.
- 사용 전 반드시 원본 데이터셋의 라이선스를 확인하시기 바랍니다.
- 이 번역 버전의 사용은 원본 라이선스의 범위 내에서만 허용됩니다.

##### 원본 데이터셋 출처

이 데이터셋은 다음 원본 데이터셋 및 연구를 기반으로 제작되었습니다:

- **원본 데이터셋**: [DeepPavlov/clinc150](https://huggingface.co/datasets/DeepPavlov/clinc150)
- **원본 논문**: [An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction](https://arxiv.org/abs/1909.02027)
- **저자**: Stefan Larson, Anish Mahendran, Joseph J. Peper, Christopher Clarke, Andrew Lee, Parker Hill, Jonathan K. Kummerfeld, Kevin Leach, Michael A. Laurenzano, Lingjia Tang, Jason Mars

원본 데이터셋 제작자들의 노력에 감사드립니다.

##### 인용

원본 논문 인용:

```bibtex
@inproceedings{larson-etal-2019-evaluation,
    title = "An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction",
    author = "Larson, Stefan  and
      Mahendran, Anish  and
      Peper, Joseph J.  and
      Clarke, Christopher  and
      Lee, Andrew  and
      Hill, Parker  and
      Kummerfeld, Jonathan K.  and
      Leach, Kevin  and
      Laurenzano, Michael A.  and
      Tang, Lingjia  and
      Mars, Jason",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-1131",
    doi = "10.18653/v1/D19-1131",
    pages = "1311--1316",
}
```

#### 면책 조항 (Disclaimer)

##### 사용자 책임

**이 데이터셋의 이용에 따른 모든 책임은 전적으로 사용자에게 있습니다.**

1. **정확성 보증 없음**: 기계 번역(LLM)을 활용하였으므로, 번역의 정확성이나 완전성을 보증하지 않습니다.

2. **용도 제한**: 이 데이터셋을 사용하여 발생하는 모든 결과(모델 학습, 서비스 운영, 연구 등)에 대한 책임은 사용자에게 있습니다.

3. **법적 준수**: 사용자는 해당 데이터셋을 사용함에 있어 관련 법률 및 규정을 준수해야 합니다.

4. **윤리적 사용**: 이 데이터셋을 비윤리적, 불법적, 또는 유해한 목적으로 사용하지 마십시오.

5. **검증 필요**: 중요한 애플리케이션에 사용하기 전에 번역 품질을 직접 검증하시기 바랍니다.

##### 배포자 면책

- 데이터셋 배포자는 번역 오류, 누락, 또는 부정확성으로 인해 발생하는 어떠한 손해에 대해서도 책임을 지지 않습니다.
- 이 데이터셋은 "있는 그대로(AS-IS)" 제공되며, 명시적이든 묵시적이든 어떠한 종류의 보증도 제공하지 않습니다.

#### 사용 방법

##### Hugging Face Datasets 라이브러리

```python
from datasets import load_dataset

### 데이터셋 로드
dataset = load_dataset("neuralfoundry-coder/clinc150-ko")

### train/validation/test split 확인
print(f"Train: {len(dataset['train'])} samples")
print(f"Validation: {len(dataset['validation'])} samples")
print(f"Test: {len(dataset['test'])} samples")

### 샘플 확인
print(dataset['train'][0])
```

##### 한국어 텍스트만 사용

```python
from datasets import load_dataset

dataset = load_dataset("neuralfoundry-coder/clinc150-ko")

### 한국어 텍스트(text)와 레이블(label)만 사용
train_texts = dataset['train']['text']
train_labels = dataset['train']['label']

print(f"샘플 텍스트: {train_texts[0]}")
print(f"레이블: {train_labels[0]}")
```

##### 인텐트 분류 모델 학습 예시

```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

### 데이터셋 로드
dataset = load_dataset("neuralfoundry-coder/clinc150-ko")

### 토크나이저 및 모델 로드
model_name = "klue/bert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=151)

### 토큰화
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

### 학습
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=32,
    num_train_epochs=5,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
)

trainer.train()
```

##### Out-of-Scope 탐지 이진 분류

```python
from datasets import load_dataset

dataset = load_dataset("neuralfoundry-coder/clinc150-ko")

### In-Scope vs Out-of-Scope 이진 분류
def convert_to_binary(example):
    # label 150이 Out-of-Scope
    example['is_oos'] = 1 if example['label'] == 150 else 0
    return example

binary_dataset = dataset.map(convert_to_binary)

### 통계 확인
train_oos = sum(binary_dataset['train']['is_oos'])
train_total = len(binary_dataset['train'])
print(f"Out-of-Scope 비율: {train_oos}/{train_total} ({100*train_oos/train_total:.1f}%)")
```

#### 활용 사례

- 한국어 인텐트 분류 모델 학습 및 평가
- 한국어 Out-of-Scope 탐지 연구
- 한국어 챗봇 및 대화형 AI 시스템 개발
- 한국어 텍스트 분류 벤치마크
- 다국어 인텐트 분류 연구
- Few-shot / Zero-shot 인텐트 분류 연구

#### 데이터셋 통계

| Split | 샘플 수 | In-Scope 샘플 | Out-of-Scope 샘플 |
|-------|--------|---------------|-------------------|
| Train | 15,200 | 15,100 | 100 |
| Validation | 3,100 | 3,000 | 100 |
| Test | 5,500 | 4,500 | 1,000 |

- 각 In-Scope 인텐트당 Train: 약 100개, Validation: 20개, Test: 30개 샘플
- Out-of-Scope 샘플은 다양한 범위 외 질의로 구성

#### 감사의 글

- 원본 데이터셋 제작: [CLINC150 저자](https://arxiv.org/abs/1909.02027)
- DeepPavlov 버전 배포: [DeepPavlov](https://huggingface.co/DeepPavlov)
- 한국어 번역: [neuralfoundry-coder](https://huggingface.co/neuralfoundry-coder)

#### 문의

데이터셋 관련 문의사항이 있으시면 Hugging Face 토론 탭을 이용해 주세요.

---

**마지막 업데이트**: 2026년 1월
