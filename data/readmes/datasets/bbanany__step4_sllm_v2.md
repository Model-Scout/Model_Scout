---
pretty_name: Korean Step 4 PII Candidate Classification
language:
- ko
task_categories:
- text-classification
tags:
- pii
- privacy
- korean
- synthetic
- qwen
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: train
    path: step4_final_10000_qwen_train.jsonl
  - split: validation
    path: step4_final_10000_qwen_valid.jsonl
  - split: test
    path: step4_final_10000_qwen_test.jsonl
---

# Step 4 PII 후보 판정 데이터셋 — 최종 10,000개

RAG 답변에서 상위 NER 단계가 추출한 후보가 문맥상 특정 자연인의 개인정보인지 `PII` 또는 `NOT_PII`로 판정하도록 Qwen을 SFT하기 위한 합성 데이터셋이다.

## 바로 사용하는 파일

- `step4_final_10000_qwen_train.jsonl`: 학습 8,000개
- `step4_final_10000_qwen_valid.jsonl`: 검증 1,000개
- `step4_final_10000_qwen_test.jsonl`: 최종 평가 1,000개
- `step4_final_10000_qwen_all.jsonl`: 전체 확인용 10,000개

각 행의 최상위 필드는 `messages` 하나뿐이며 `system`, `user`, `assistant` 순서다. 학습 시 Qwen tokenizer의 chat template를 적용하고 assistant 응답 부분에만 loss를 계산한다.

## 관리·검수 파일

- `step4_final_10000_canonical.jsonl`: 문장, 후보, span, 라벨, 생성 구조를 보존한 기준 원본
- `step4_final_10000_index.jsonl`: Qwen 파일 행과 canonical ID의 대응표
- `step4_final_10000_statistics.json`: 분할·태그·라벨·다양성 통계와 해시
- `step4_final_10000_quality_report.md`: 9회 전수 검수 결과
- `step4_final_10000_sentence_review_5_rounds.md`: 문장 자연스러움·의미·반복·관점을 개선한 추가 5회 재검수 결과
- `step4_final_10000_test_review.md`: 테스트 1,000개를 읽기 쉽게 정리한 문서

## 구성

- 프로필 1,000개 × 태그 10개 = 10,000개
- train/valid/test = 8,000/1,000/1,000
- 태그별 1,000개
- 태그별 PII/NOT_PII = 500/500
- 프로필별 PII/NOT_PII = 5/5
- 프로필 단위 split 고정

## 다양성 원칙

CAPID의 현실적인 상황·구체적 주변 문맥 원칙과 ASQ-PHI의 질의·기록·메모형 표현 다양성을 참고했다. 우리 Step 4 입력에 맞게 답변당 후보는 하나만 두었고, 50개 담화 프레임, 라벨별 20개 주장 형식, 라벨별 25개 배경 및 25개 후속 행동, 태그별 비개인 맥락을 조합했다. 1인칭 PII에는 별도의 배경 25종과 후속 행동 25종을 적용해 서술 관점을 통일했다.

후보 문자열을 태그 토큰으로 치환한 뒤에도 10,000개 문맥이 모두 다르며, 구조 시그니처도 10,000개가 서로 다르다.

## 범위

후보는 합성 프로필에서 확정한 gold 후보다. 실제 운영 NER의 오탐 빈도 자체를 재현한 데이터는 아니지만, NER 후보를 받은 뒤 문맥에 따라 PII 여부를 판정하는 최종 Step 4 학습 구조와 동일하다.

이 데이터는 합성 데이터이며 실존 인물의 개인정보를 수집한 데이터가 아니다. 현재
validation/test는 프로필 단위로 train과 분리되어 있지만 생성 프레임과 문장 조각을
공유한다. 따라서 두 분할은 인도메인 진단용으로 사용하고, 운영 일반화 성능은 실제
문장 또는 생성 템플릿까지 독립적인 외부 평가 세트로 별도 측정해야 한다.
