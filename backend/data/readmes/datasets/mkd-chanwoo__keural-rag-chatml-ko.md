---
language:
  - ko
license: cc-by-4.0
tags:
  - korean
  - sft
  - chatml
  - synthetic
  - rag
  - instruction-tuning
  - question-answering
task_categories:
  - text-generation
---

# keural-rag-SFT-chatml-ko

`mkd-chanwoo/keural-rag-ko` 데이터셋을 SFT 학습용 ChatML 포맷으로 전처리한 한국어 RAG 기반 QA 데이터셋입니다.

한국어 웹문서(뉴스, 블로그, 지식백과 등)를 시드로 Gemma-4-26B 모델이 생성한 단일턴 QA로 구성되어 있으며, 소스 문서를 컨텍스트로 user 턴에 포함하여 문서 기반 답변 학습에 활용할 수 있습니다.

## 데이터셋 개요

| 항목 | 값 |
|------|-----|
| 총 샘플 수 | 303,355 |
| 총 토큰 수 | 약 340M |
| 평균 토큰 / 샘플 | 1,121.8 |
| 중간값 토큰 | 974 |
| 최대 토큰 | 8,192 |
| 최소 토큰 | 169 |
| 언어 | 한국어 (100%) |
| 포맷 | ChatML |
| 라이선스 | CC BY 4.0 |

## 태스크 유형 분포 (원본 기준)

| task_type | 샘플 수 | 비율 |
|-----------|---------|------|
| general_qa | ~318,565 | ~22.7% |
| summary | ~318,878 | ~22.8% |
| structured_output | ~315,699 | ~22.5% |
| reasoning | ~306,091 | ~21.8% |
| critique | ~143,378 | ~10.2% |

> 위 수치는 원본 데이터셋 기준이며, 전처리(품질 필터, 중복 제거) 후 최종 샘플 수는 303,355개입니다.

## 포맷

ChatML 형식으로 변환되었습니다. 소스 문서(`text`)가 질문(`question`) 앞에 붙어 user 턴에 포함됩니다.

```
<|im_start|>user
{소스 문서 텍스트}

{질문}
<|im_end|>
<|im_start|>assistant
{답변}
<|im_end|>
```

**예시:**
```
<|im_start|>user
쿠팡이 가정의 달과 혼수 시즌을 맞아 대규모 가전·디지털 할인 행사인 '쿠가세'를 오는 5월10일까지 진행한다.
행사 기간 동안 매일 오후 2시에는 '선착순 초특가' 코너가 진행된다...

제시된 문서의 핵심 내용을 요약 정리해 주세요.
<|im_end|>
<|im_start|>assistant
**[핵심 요약]**
* 쿠팡이 5월 10일까지 대규모 가전·디지털 할인 행사인 '쿠가세'를 진행합니다.
* 삼성, LG, 애플 등 100개 이상의 브랜드가 참여하며, 선착순 초특가와 브랜드별 할인 혜택을 제공합니다.
<|im_end|>
```

## 데이터 컬럼

| 컬럼 | 타입 | 설명 |
|------|------|------|
| `text` | string | ChatML 포맷 변환된 대화 전문 |
| `source_name` | string | `keural_synthetic_sft` |
| `n_tokens` | int | 토큰 수 |

## 전처리 파이프라인

원본 데이터(`mkd-chanwoo/keural-rag-SFT`)에서 아래 단계를 거쳐 생성되었습니다.

1. **Collect** — HuggingFace에서 스트리밍 다운로드
2. **Structure** — `text + question` → user 턴, `answer` → assistant 턴으로 변환
3. **Clean** — 빈 턴, 역할 순서 오류, 깨진 인코딩 제거
4. **Quality** — 최소 응답 길이 5자 필터
5. **Safety** — 유해 콘텐츠 필터링
6. **Dedup** — MinHash 기반 중복 제거
7. **Format** — ChatML 템플릿 적용
8. **Tokenize** — 최대 시퀀스 길이 8,192 토큰 (overflow: truncate)

## 원본 데이터

- **출처**: [mkd-chanwoo/keural-rag-ko](https://huggingface.co/datasets/mkd-chanwoo/keural-rag-ko)
- **원본 규모**: 1,402,611 샘플
- **생성 모델**: google/gemma-4-26B-A4B-it
- **시드 문서**: 한국어 웹문서 1,545,735건 (네이버 검색, 블로그, 지식백과 등)
- **라이선스**: CC BY 4.0

## 사용 방법

```python
from datasets import load_dataset

ds = load_dataset("mkd-chanwoo/keural-rag-SFT-chatml-ko", split="train")
print(ds[0]["text"])
```