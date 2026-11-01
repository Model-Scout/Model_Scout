---
language:
  - ko
license: cc-by-4.0
tags:
  - korean
  - sft
  - chatml
  - synthetic
  - conversation
  - daily-chat
task_categories:
  - text-generation
---

# keural-conversation-chatml-ko

`mkd-chanwoo/keural-conversation-ko` 데이터셋을 SFT 학습용 ChatML 포맷으로 전처리한 한국어 일상대화 데이터셋입니다.

9개 주제의 일상 캐주얼 대화를 Gemma-4-26B 모델이 생성한 synthetic 멀티턴 대화로 구성되어 있습니다.

## 데이터셋 개요

| 항목 | 값 |
|------|-----|
| 총 샘플 수 | 133,339 |
| 총 토큰 수 | 약 19M |
| 평균 토큰 / 샘플 | 146.0 |
| 중간값 토큰 | 145 |
| 최대 토큰 | 805 |
| 최소 토큰 | 95 |
| 언어 | 한국어 (100%) |
| 포맷 | ChatML |
| 라이선스 | CC BY 4.0 |

## 포맷

ChatML 형식의 멀티턴 대화입니다.

```
<|im_start|>user
{발화 1}
<|im_end|>
<|im_start|>assistant
{발화 2}
<|im_end|>
<|im_start|>user
{발화 3}
<|im_end|>
<|im_start|>assistant
{발화 4}
<|im_end|>
```

**예시:**
```
<|im_start|>user
다음에 또 봐!
<|im_end|>
<|im_start|>assistant
응, 조심해서 들어가고 다음에 꼭 다시 만나자!
<|im_end|>
<|im_start|>user
그래, 연락할게!
<|im_end|>
<|im_start|>assistant
응, 기다리고 있을게! 푹 쉬어!
<|im_end|>
```

## 데이터 컬럼

| 컬럼 | 타입 | 설명 |
|------|------|------|
| `text` | string | ChatML 포맷 변환된 대화 전문 |
| `source_name` | string | `keural_conversation` |
| `n_tokens` | int | 토큰 수 |

## 전처리 파이프라인

원본 데이터(`mkd-chanwoo/keural-conversation`)에서 아래 단계를 거쳐 생성되었습니다.

1. **Collect** — HuggingFace에서 다운로드
2. **Structure** — JSON 문자열로 직렬화된 `conversation` 필드를 파싱하여 ChatML 표준 스키마로 변환
3. **Clean** — 빈 턴, 역할 순서 오류 제거
4. **Quality** — 최소 응답 길이 5자 필터
5. **Safety** — 유해 콘텐츠 필터링
6. **Dedup** — MinHash 기반 중복 제거
7. **Format** — ChatML 템플릿 적용
8. **Tokenize** — 최대 시퀀스 길이 8,192 토큰 (overflow: truncate)

## 원본 데이터

- **출처**: [mkd-chanwoo/keural-conversation-ko](https://huggingface.co/datasets/mkd-chanwoo/keural-conversation-ko)
- **원본 규모**: 191,093 샘플
- **생성 모델**: google/gemma-4-26B-A4B-it
- **주제**: 9개 카테고리 일상 대화 (자기소개, 취미, 음식, 여행, 쇼핑 등)
- **라이선스**: CC BY 4.0

## 사용 방법

```python
from datasets import load_dataset

ds = load_dataset("mkd-chanwoo/keural-conversation-chatml-ko", split="train")
print(ds[0]["text"])
```