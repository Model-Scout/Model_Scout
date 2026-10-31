---
language:
- ko
- en
license: cc-by-4.0
tags:
- korean
- translation
- text-classification
- intent-classification
- banking
- finance
- customer-service
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_text
    dtype: string
  - name: text_original
    dtype: string
  splits:
  - name: train
    num_bytes: 1716451
    num_examples: 9993
  - name: test
    num_bytes: 494290
    num_examples: 3076
  download_size: 716792
  dataset_size: 2210741
source_datasets:
- mteb/banking77
task_categories:
- text-classification
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
pretty_name: "Banking77-ko (한국어 번역 버전)"
---

<!-- aegis-dataset-card -->

# banking77-ko

> **학습용** · Banking77-ko (한국어 번역 버전)  
> 파일 5개 · 3.5 MB · 행 26,138 · revision `fbad6d31a7` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
이 데이터셋은 [mteb/banking77](https://huggingface.co/datasets/mteb/banking77) 데이터셋의 **한국어 번역 버전**입니다.

## 이 데이터로 학습한 모델
| 모델 | 관계 | 사용 부분 | 비고 |
|---|---|---|---|
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

관계: 학습(직접) = 이 파일을 그대로 학습에 씀 · 학습(가공 후) = 코퍼스 · SFT 혼합을 만드는 입력(재생성 방법은 카탈로그) · 생성 입력(원본) = 합성 · 정리 단계의 원본 기록.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 12.1 KB | - |  |
| `data/banking77_ko_test_20260112_133134.jsonl` | 632.3 KB | 3,076 |  |
| `data/banking77_ko_train_20260112_133134.jsonl` | 2.2 MB | 9,993 |  |
| `data/test-00000-of-00001.parquet` | 170.1 KB | 3,076 |  |
| `data/train-00000-of-00001.parquet` | 546.7 KB | 9,993 |  |

## 필드 · 범주 분포
**`data/banking77_ko_test_20260112_133134.jsonl`, `data/banking77_ko_train_20260112_133134.jsonl`, `data/test-00000-of-00001.parquet`, `data/train-00000-of-00001.parquet`** (기준 `data/banking77_ko_train_20260112_133134.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `text` | str | 100% |
| `label` | int | 100% |
| `label_text` | str | 100% |
| `text_original` | str | 100% |

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 출처 · 라이선스 · 등록
- aegis-guard-train 등록부 `neuralfoundry-coder/banking77-ko` · role train · revision fbad6d31a7
- 항목별 출처 · 라이선스는 아래 기존 설명과 항목 필드를 따른다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/banking77-ko --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### Banking77-ko (한국어 번역 버전)

#### 개요

이 데이터셋은 [mteb/banking77](https://huggingface.co/datasets/mteb/banking77) 데이터셋의 **한국어 번역 버전**입니다.

Banking77은 은행 서비스 관련 고객 질의를 77개의 인텐트(의도)로 분류하는 벤치마크 데이터셋입니다. 이 번역 버전은 한국어 텍스트 분류 및 인텐트 분류 모델의 학습과 평가에 활용할 수 있도록 제작되었습니다.

#### 데이터셋 정보

| 항목 | 내용 |
|------|------|
| **원본 데이터셋** | [mteb/banking77](https://huggingface.co/datasets/mteb/banking77) |
| **원본 출처** | [BANKING77: A Large-Scale Dataset for Intent Classification](https://arxiv.org/abs/2003.04807) |
| **데이터 크기** | Train: 10,003개 / Test: 3,080개 |
| **언어** | 한국어 (Korean) |
| **분류 클래스** | 77개 인텐트 |
| **번역 일자** | 2026년 1월 |

#### 번역 방법론

##### 번역 도구
- **번역 엔진**: LLM 기반 번역 API
- **동시 처리**: 100건 병렬 요청
- **품질 관리**: 자동 검증 및 재시도 메커니즘

##### 번역 원칙

Banking77 데이터셋의 특성을 고려하여 다음 원칙을 적용하였습니다:

1. **자연스러운 한국어 표현**
   - 한국 은행 고객이 실제로 사용하는 자연스러운 표현으로 번역
   - 구어체 질의의 특성 유지

2. **금융 용어 현지화**
   - `transfer` → "이체" 또는 "송금"
   - `account` → "계좌"
   - `balance` → "잔액"
   - `card` → "카드"
   - `fee` → "수수료"
   - `direct debit` → "자동이체"
   - `standing order` → "정기이체"
   - `overdraft` → "마이너스 통장" 또는 "당좌대출"
   - `loan` → "대출"
   - `interest` → "이자"
   - `exchange rate` → "환율"
   - `statement` → "거래내역서"

3. **보존 요소**
   - 숫자, 날짜, 금액은 원본 그대로 유지
   - 질문의 의도와 톤 보존

##### 번역 대상 필드

| 필드 | 설명 | 번역 여부 |
|------|------|----------|
| `text` | 고객 질의 (번역된 한국어) | ✅ 번역 |
| `text_original` | 고객 질의 (원본 영어) | ❌ 원본 보존 |
| `label` | 인텐트 분류 ID (0-76) | ❌ 원본 유지 |
| `label_text` | 인텐트명 | ❌ 원본 유지 |

#### 데이터 구조

```json
{
  "text": "카드 배송이 언제 도착하나요?",
  "text_original": "When will my card arrive?",
  "label": 7,
  "label_text": "card_arrival"
}
```

#### 77개 인텐트 분류

Banking77 데이터셋은 다음과 같은 77개의 인텐트를 포함합니다:

<details>
<summary>전체 인텐트 목록 보기</summary>

| ID | 인텐트 | 설명 |
|----|--------|------|
| 0 | activate_my_card | 카드 활성화 |
| 1 | age_limit | 나이 제한 |
| 2 | apple_pay_or_google_pay | Apple Pay/Google Pay |
| 3 | atm_support | ATM 지원 |
| 4 | automatic_top_up | 자동 충전 |
| 5 | balance_not_updated_after_bank_transfer | 이체 후 잔액 미갱신 |
| 6 | balance_not_updated_after_cheque_or_cash_deposit | 입금 후 잔액 미갱신 |
| 7 | beneficiary_not_allowed | 수취인 불가 |
| 8 | cancel_transfer | 이체 취소 |
| 9 | card_about_to_expire | 카드 만료 임박 |
| 10 | card_acceptance | 카드 수용 |
| 11 | card_arrival | 카드 도착 |
| 12 | card_delivery_estimate | 카드 배송 예상 |
| 13 | card_linking | 카드 연결 |
| 14 | card_not_working | 카드 작동 불가 |
| 15 | card_payment_fee_charged | 카드 결제 수수료 |
| 16 | card_payment_not_recognised | 카드 결제 미인식 |
| 17 | card_payment_wrong_exchange_rate | 카드 결제 환율 오류 |
| 18 | card_swallowed | 카드 삼킴 |
| 19 | cash_withdrawal_charge | 현금 인출 수수료 |
| 20 | cash_withdrawal_not_recognised | 현금 인출 미인식 |
| 21 | change_pin | PIN 변경 |
| 22 | compromised_card | 카드 정보 유출 |
| 23 | contactless_not_working | 비접촉 결제 불가 |
| 24 | country_support | 국가 지원 |
| 25 | declined_card_payment | 카드 결제 거절 |
| 26 | declined_cash_withdrawal | 현금 인출 거절 |
| 27 | declined_transfer | 이체 거절 |
| 28 | direct_debit_payment_not_recognised | 자동이체 미인식 |
| 29 | disposable_card_limits | 일회용 카드 한도 |
| 30 | edit_personal_details | 개인정보 수정 |
| 31 | exchange_charge | 환전 수수료 |
| 32 | exchange_rate | 환율 |
| 33 | exchange_via_app | 앱 환전 |
| 34 | extra_charge_on_statement | 명세서 추가 청구 |
| 35 | failed_transfer | 이체 실패 |
| 36 | fiat_currency_support | 법정화폐 지원 |
| 37 | get_disposable_virtual_card | 일회용 가상카드 발급 |
| 38 | get_physical_card | 실물카드 발급 |
| 39 | getting_spare_card | 여분 카드 발급 |
| 40 | getting_virtual_card | 가상카드 발급 |
| 41 | lost_or_stolen_card | 카드 분실/도난 |
| 42 | lost_or_stolen_phone | 휴대폰 분실/도난 |
| 43 | order_physical_card | 실물카드 주문 |
| 44 | passcode_forgotten | 비밀번호 분실 |
| 45 | pending_card_payment | 카드 결제 대기 |
| 46 | pending_cash_withdrawal | 현금 인출 대기 |
| 47 | pending_top_up | 충전 대기 |
| 48 | pending_transfer | 이체 대기 |
| 49 | pin_blocked | PIN 차단 |
| 50 | receiving_money | 송금 수령 |
| 51 | Refund_not_showing_up | 환불 미표시 |
| 52 | request_refund | 환불 요청 |
| 53 | reverted_card_payment? | 카드 결제 취소 |
| 54 | supported_cards_and_currencies | 지원 카드/통화 |
| 55 | terminate_account | 계좌 해지 |
| 56 | top_up_by_bank_transfer_charge | 은행이체 충전 수수료 |
| 57 | top_up_by_card_charge | 카드 충전 수수료 |
| 58 | top_up_by_cash_or_cheque | 현금/수표 충전 |
| 59 | top_up_failed | 충전 실패 |
| 60 | top_up_limits | 충전 한도 |
| 61 | top_up_reverted | 충전 취소 |
| 62 | topping_up_by_card | 카드로 충전 |
| 63 | transaction_charged_twice | 이중 청구 |
| 64 | transfer_fee_charged | 이체 수수료 |
| 65 | transfer_into_account | 계좌 입금 |
| 66 | transfer_not_received_by_recipient | 수취인 미수령 |
| 67 | transfer_timing | 이체 소요시간 |
| 68 | unable_to_verify_identity | 본인확인 불가 |
| 69 | verify_my_identity | 본인확인 |
| 70 | verify_source_of_funds | 자금출처 확인 |
| 71 | verify_top_up | 충전 확인 |
| 72 | virtual_card_not_working | 가상카드 불가 |
| 73 | visa_or_mastercard | Visa/Mastercard |
| 74 | why_verify_identity | 본인확인 이유 |
| 75 | wrong_amount_of_cash_received | 현금 금액 오류 |
| 76 | wrong_exchange_rate_for_cash_withdrawal | 현금인출 환율 오류 |

</details>

#### 라이선스 및 저작권

##### 원본 라이선스 귀속

**이 데이터셋은 원본 데이터셋 [mteb/banking77](https://huggingface.co/datasets/mteb/banking77)의 라이선스를 따릅니다.**

- **라이선스**: [CC BY 4.0 (Creative Commons Attribution 4.0 International)](https://creativecommons.org/licenses/by/4.0/)
- 원본 데이터셋의 모든 라이선스 조건이 이 번역 버전에도 동일하게 적용됩니다.
- 사용 전 반드시 원본 데이터셋의 라이선스를 확인하시기 바랍니다.
- 이 번역 버전의 사용은 원본 라이선스의 범위 내에서만 허용됩니다.

##### 원본 데이터셋 출처

이 데이터셋은 다음 원본 데이터셋을 기반으로 제작되었습니다:
- **원본**: [mteb/banking77](https://huggingface.co/datasets/mteb/banking77)
- **논문**: [BANKING77: A Large-Scale Dataset for Intent Classification](https://arxiv.org/abs/2003.04807)
- **저자**: I. Casanueva, T. Temčinas, D. Gerber, M. Henderson, I. Vulić

원본 데이터셋 제작자의 노력에 감사드립니다.

##### 인용

원본 논문 인용:
```bibtex
@inproceedings{casanueva2020efficient,
  title={Efficient Intent Detection with Dual Sentence Encoders},
  author={Casanueva, I{\~n}igo and Tem{\v{c}}inas, Tadas and Gerber, Daniela and Henderson, Matthew and Vuli{\'c}, Ivan},
  booktitle={Proceedings of the 2nd Workshop on Natural Language Processing for Conversational AI},
  pages={38--45},
  year={2020}
}
```

#### 면책 조항 (Disclaimer)

##### 사용자 책임

**이 데이터셋의 이용에 따른 모든 책임은 전적으로 사용자에게 있습니다.**

1. **정확성 보증 없음**: 기계 번역을 활용하였으므로, 번역의 정확성이나 완전성을 보증하지 않습니다.

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
dataset = load_dataset("neuralfoundry-coder/banking77-ko")

### train/test split 확인
print(f"Train: {len(dataset['train'])} samples")
print(f"Test: {len(dataset['test'])} samples")

### 샘플 확인
print(dataset['train'][0])
```

##### 인텐트 분류 모델 학습 예시

```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

### 데이터셋 로드
dataset = load_dataset("neuralfoundry-coder/banking77-ko")

### 토크나이저 및 모델 로드
model_name = "klue/bert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=77)

### 토큰화
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

### 학습
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

trainer.train()
```

#### 활용 사례

- 한국어 인텐트 분류 모델 학습 및 평가
- 한국어 챗봇 및 고객 서비스 시스템 개발
- 한국어 텍스트 분류 벤치마크
- 금융 도메인 NLU(자연어 이해) 연구
- 다국어 인텐트 분류 연구

#### 감사의 글

- 원본 데이터셋 제작: [Banking77 저자](https://arxiv.org/abs/2003.04807)
- MTEB 버전 배포: [mteb](https://huggingface.co/mteb)
- 한국어 번역: [neuralfoundry-coder](https://huggingface.co/neuralfoundry-coder)

#### 문의

데이터셋 관련 문의사항이 있으시면 Hugging Face 토론 탭을 이용해 주세요.

---

**마지막 업데이트**: 2026년 1월
