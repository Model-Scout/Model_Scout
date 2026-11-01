---
language:
  - ko
license: other
license_name: aihub-terms
tags:
  - conversation
  - daily-chat
  - multisession
  - korean
  - sft
  - chatml
task_categories:
  - text-generation
---

# aihub_conversation

AI Hub 일상대화 한국어 멀티세션 데이터셋 (데이터셋 No. 71678)을 SFT 학습용으로 전처리한 데이터셋입니다.

## 데이터셋 개요

| 항목 | 값 |
|------|-----|
| 총 샘플 수 | 120,867 |
| 총 토큰 수 | 약 93M |
| 평균 토큰 / 샘플 | 769.5 |
| 최대 토큰 | 1,962 |
| 언어 | 한국어 (100%) |
| 포맷 | ChatML |
| 출처 | AI Hub 71678 |
| 라이선스 | AI Hub 이용약관 |

## 세션 구성

| 유형 | 샘플 수 | 비율 |
|------|---------|------|
| 단일세션 (system 없음) | 50,052 | 41.4% |
| 멀티세션 (이전 세션 요약 포함) | 70,815 | 58.6% |

멀티세션 샘플은 이전 세션의 대화 요약을 `system` 턴에 주입하여 연속 대화 맥락을 학습할 수 있도록 구성되어 있습니다.

## 포맷

ChatML 형식으로 변환되었습니다.

**단일세션 예시:**
```
<|im_start|>user
안녕하세요! 통신판매에 대한 개념을 좀 알고 싶어요.
<|im_end|>
<|im_start|>assistant
통신판매는 무점포 판매 방식 중 하나로, 미디어를 이용하여 상품을 전시하고 소비자의 주문을 받아 판매하는 방법입니다.
<|im_end|>
```

**멀티세션 예시:**
```
<|im_start|>system
[이전 대화 - 사용자 요약]
나는 관광/감상의 단체에 대한 공부를 하고 있다.
나는 연인이 없지만 신경 쓰지 않는다.

[이전 대화 - 어시스턴트 요약]
앰배서더 서울 풀만 호텔은 1955년 금수장으로 시작하여 60여년의 역사를 가진 서울 중구 장충동에 위치한 특1급 호텔이다.
<|im_end|>
<|im_start|>user
안녕! 저번에 이어서 호텔에 대해서 궁금해서 물어보러 왔어!
<|im_end|>
<|im_start|>assistant
안녕하세요! 저번에 호텔에 대해서 정보를 드렸던 게 도움이 되셨나요?
<|im_end|>
```

## 데이터 컬럼

| 컬럼 | 타입 | 설명 |
|------|------|------|
| `text` | string | ChatML 포맷 변환된 대화 전문 |
| `source_name` | string | `aihub_daily_conversation` |
| `n_tokens` | int | 토큰 수 |

## 전처리 파이프라인

원본 데이터(AI Hub 71678)에서 아래 단계를 거쳐 생성되었습니다.

1. **Collect** — AI Hub API로 다운로드, sessionInfo[] 멀티세션 구조 파싱
2. **Structure** — speaker1/speaker2 → user/assistant 변환, 이전 세션 요약 system 주입
3. **Clean** — 빈 턴, 깨진 인코딩, 역할 순서 오류 제거
4. **Quality** — 최소 응답 길이 5자 필터 (캐주얼 대화 보존)
5. **Safety** — 유해 콘텐츠 필터링
6. **Dedup** — MinHash 기반 중복 제거
7. **Format** — ChatML 템플릿 적용
8. **Tokenize** — 최대 시퀀스 길이 8,192 토큰 (overflow: truncate)

## 원본 데이터

- **출처**: [AI Hub](https://aihub.or.kr) — 일상대화 한국어 멀티세션 데이터 (No. 71678)
- **원본 규모**: 약 140K 건
- **라이선스**: AI Hub 이용약관 (비상업적 연구 목적 허용)

## 사용 방법

```python
from datasets import load_dataset

ds = load_dataset("mkd-chanwoo/aihub_conversation", split="train")
print(ds[0]["text"])
```