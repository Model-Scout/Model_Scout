---
license: cc-by-4.0
language:
  - ko
multilinguality: monolingual
task_categories:
  - question-answering
tags:
  - legal
  - law
  - korean
  - kor
  - qa
  - precedent
  - statute
size_categories:
  - n<1K
pretty_name: Korean Legal QA Dataset
---

# Korean Legal QA Dataset (한국어 법률 QA 데이터셋)

법령 조문과 판례를 **연결고리**로 묶은 한국어 법률 질의응답 데이터셋입니다.

베제처 국가법령정보센터의 공개 법령·판례 데이터를 바탕으로 구축되었습니다.

## 형식 (Format)

각 항목은 **질문(question)**, **정답(answer)**, **검색문서(retrieved_documents)** 3가지 필드로 구성됩니다:

```json
{
  "id": "qa_conn_01_a",
  "question": "[민사소송법 제80조] 관련하여, 대법원 1948.04.07 선고 '부동산소유권이전등기' 사건에서 법원은 어떤 판단을 내렸는가?",
  "answer": "【사건명】부동산소유권이전등기 (4281민상362)\n【판시사항】...\n【판결요지】...",
  "retrieved_documents": [
    {
      "type": "statute",
      "law_name": "민사소송법",
      "article_number": "80",
      "article_title": "독립당사자참가소송에서의 탈퇴",
      "content": "제80조(독립당사자참가소송에서의 탈퇴) 제79조의 규정에 따라...",
      "ministry": "법무부"
    },
    {
      "type": "precedent",
      "case_name": "부동산소유권이전등기",
      "court": "대법원",
      "case_number": "4281민상362",
      "date": "1948.04.07",
      "issue": "가. 소송위임 흠결의 항변과 당해 이원의 인증...",
      "summary": "가. 소송위임장이 사문서인 경우에 당사자 일방이...",
      "references": "민사소송법 제80조, 제137조, 제395조"
    }
  ],
  "connection_type": "precedent_interprets_statute",
  "connection_chain": "판례(부동산소유권이전등기) → 참조조문(민사소송법 제80조) → 법령조문(민사소송법 제80조)"
}
```

## 구성

| 연결유형 | 개수 | 설명 |
|---------|------|------|
| precedent_interprets_statute | 10 | 판례가 법령 조문을 해석한 QA |
| statute_applied_to_case | 10 | 판례에 적용된 법령 조문 식별 QA |
| statute_interpretation | 5 | 법령 조문 독립 해석 QA |
| precedent_summary | 5 | 판례 요약 분석 QA |
| **총계** | **30** | |

## 연결고리 (Connection Chain)

```
판례(사건명) → 참조조문(법령 제N조) → 법령조문(제N조 내용)
```

## 참조 법률

- 민법, 민사소송법
- 형사소송법, 형법, 상법
- 관세법, 소득세법, 국세기본법
- 헌법, 부동산등기법

## 원천 데이터

| 데이터셋 | 설명 |
|---------|------|
| `smhilee/korean-law-dataset` | 법제처 국가법령정보센터 법령 |
| `chaannwooff/Korean_law` | 국가법령정보센터 법령(조문단위) |
| `joonhok-exo-ai/korean_law_open_data_precedents` | 국가법령정보센터 판례 |

## 파일

- `data/real_qa.jsonl` — **메인**: 질문-정답-검색문서 포맷 (JSONL)
- `data/real_qa.json` — 위와 동일한 JSON 배열
- `dataset.jsonl` — 플랫 CSV-like JSONL
- `dataset.csv` — CSV 포맷

## 생성일

2026-04-27