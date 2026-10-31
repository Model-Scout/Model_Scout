---
license: cc-by-4.0
language:
  - ko
task_categories:
  - token-classification
tags:
  - pii
  - privacy
  - ner
  - korean
  - synthetic
size_categories:
  - 10K<n<100K
---

# bc-pii-ko — 한국어 개인정보(PII) 탐지 학습 데이터셋

[ai4privacy/pii-masking-openpii-1.5m](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m)
의 한국어 서브셋을 BC 개인정보 정책 유형 체계로 가공하고 도메인 증강을 더한
토큰 분류(NER) 학습용 데이터셋. **전량 합성/공개 데이터** — 실존 개인정보 미포함
(주민번호 등은 형식 규칙만 준수한 난수, 카드번호는 테스트 IIN + Luhn).

## Splits

| split | 행 수 | 성격 |
|---|---|---|
| train | 62,194 | 원본 가공 19,158 + 값치환 사본 38,316 + 절조합 주입 4,000 + 네거티브 720 |
| validation | 5,273 | 증강 미포함 원본 분포 (튜닝·에폭 선택용) |
| test | 2,067 | 증강 미포함 원본 분포 — **대표 지표는 여기서** |
| test_gap | 640 | 학습에 없는 절로만 조합한 갭 유형(계좌·CI·IP 등) 일반화 진단 전용 |

**규약**: train 만 학습에 사용할 것. test 와 test_gap 은 성격이 달라 합산하지
말고 분리 리포트할 것.

## 스키마

```jsonc
{
  "source_text": "본인확인을 위해 생년월일 1979-07-22 와 …",
  "masked_text": "본인확인을 위해 생년월일 [DOB_1] 와 …",
  "privacy_mask": [{
    "label": "DOB",            // fine 라벨 (NAME, RRN, CARDNUM, PHONE_MOBILE …)
    "start": 14, "end": 24,    // source_text 문자 오프셋 (유일한 ground truth)
    "value": "1979-07-22",
    "label_index": 1,          // 같은 값 = 같은 index
    "bc_type": "생년월일",       // 마스킹 정책 유형 (없으면 null)
    "origin": "source"         // source | remapped | localized | synthetic
  }],
  "language": "ko", "split": "train", "uid": "24798802",
  "provenance": "openpii-1.5m"  // | augmented-values | augmented-inject | augmented-negative
}
```

토큰 라벨은 포함하지 않는다 — 사용할 모델의 토크나이저로 char span 을 정렬해
생성할 것 (BIO/BIOES 는 offset mapping 으로 유도).

## 가공 내용 (원본 openpii ko 대비)

- **값 현지화**: 비한국 포맷 값(면허 `DY00HBSKXU` 류) 48,500스팬을 한국 규격
  합성값으로 치환 (주민/외국인·카드·면허·여권·전화 — 정책 정규식+검증기 통과 보장)
- **한국어 교정**: 서구식 `이름 성` → `성이름`(4,894쌍), 로마자 호칭 음차·후치
  (`gun X님` → `X 군`, 12,146건), 성+이름 단일 NAME 스팬 병합
- **증강**: 원본에 없는 유형(계좌·CI·IP·카드유효기간·CVC·I-PIN·USERNAME·PASSWORD)
  절 조합 주입, 값치환 사본(×3, 이름은 50% 자연 분포 보존), 부분마스킹 표기
  (`010-12**-****` 도 PII 태깅), 무라벨 혼동 샘플(주문·운송장번호 등)
- **품질 게이트**: 스팬 무결성 100%, bc_type↔정책 정규식 자체모순 0, 전 변환
  seed 기반 결정적

## 사용

```python
from datasets import load_dataset
ds = load_dataset("sehe1121/bc-pii-ko")
```

## 한계

- 원문이 openpii 합성 번역체 — 실무 텍스트(구어·양식체) 분포와 다름
- 이름 골드에 원본 유래 노이즈 일부 잔존 (다중 이름 그룹, 로마자 조각)
- 갭 유형의 문맥 다양성은 수작업 절 풀 기반 (train 고유 문장구조 ~3,300종)

## 라이선스·출처

- 원천: ai4privacy/pii-masking-openpii-1.5m (**CC-BY-4.0**) — 본 데이터셋은
  그 파생물로 동일 라이선스를 따르며 원 데이터셋을 고지한다
- 라벨 세분화 설계는 OpenMed/privacy-filter-multilingual 의 체계를 참조
