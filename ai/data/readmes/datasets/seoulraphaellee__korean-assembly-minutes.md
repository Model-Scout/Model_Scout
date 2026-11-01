---
license: other
language:
- ko
task_categories:
- text-generation
- summarization
tags:
- korean
- parliament
- government
- minutes
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*.jsonl.gz
- config_name: summaries
  data_files:
  - split: train
    path: summaries/*.jsonl.gz
---

# 대한민국 국회 회의록 아카이브

국회 회의록 원문(record.assembly.go.kr) PDF 에서 본문을 뽑아 모은 것이다.
본회의와 각 위원회 회의록이 모두 들어 있다.

- 수록 기간: **1948~2026**
- 회의 수: **31,533건**
- 본문 분량: **1,982,379,213자**

## 구성

| 설정 | 파일 | 내용 |
|---|---|---|
| `default` | `data/YYYY.jsonl.gz` | 회의록 본문, 연도별 |
| `summaries` | `summaries/YYYY.jsonl.gz` | AI 회의 요약·주요 쟁점, 연도별(생성 중) |

```python
from datasets import load_dataset

ds = load_dataset("seoulraphaellee/korean-assembly-minutes", split="train")
ds = load_dataset("seoulraphaellee/korean-assembly-minutes", data_files="data/2026.jsonl.gz", split="train")
summaries = load_dataset("seoulraphaellee/korean-assembly-minutes", "summaries", split="train")
```

## 필드 (본문)

| 이름 | 설명 |
|---|---|
| `meeting_key` | 회의 식별자 (`record:<id>`) |
| `record_id` | 국회 회의록 원문 id |
| `conf_date` | 회의 일자 (YYYY-MM-DD) |
| `era` | 대수 (예: 제22대국회) |
| `session_no` / `sitting_no` | 회기 / 차수 |
| `committee` | 위원회명 (본회의는 국회본회의) |
| `conf_kind` | 회의 종류 (전체회의, 소위원회 등) |
| `title` | 회의록 표제 |
| `source_url` | 원문 PDF 주소 |
| `extractor` | 본문 추출기 (`unpdf`) |
| `page_count` / `char_count` | 원문 쪽수 / 글자수 |
| `turn_count` | 발언자 표시로 나눈 발언 수(참고값) |
| `text` | 회의록 본문 |

## 만드는 방법

2026-09-30 전량을 원문 PDF 에서 다시 뽑았다. 이전 판은 pdfplumber 가 글자를
화면 위치 순으로 정렬해 **2단 편집의 좌우 단이 한 줄씩 섞여** 있었다. 지금
판은 unpdf(pdf.js)로 PDF 에 저장된 순서대로 읽어 단 순서가 맞다. 다시 뽑지
못한 1건(2010년, record:34709)은 이전 본문을 그대로 두었다. 이전 판은 이
저장소의 커밋 이력에 남아 있다.

## 요약 (`summaries`)

국회 회의록 실시간 수집기(https://seoul-raphael.github.io/assembly-minutes/)가
공개 요약과 같은 방식으로 만든 AI 참고자료다. 최근 연도부터 채우는 중이다.
`summary_key` 는 `날짜|대수|위원회|회기|차수|회의종류` 로, 본문 쪽 필드로 같은
키를 만들 수 있다. **AI 생성물이므로 인용 전 원문과 대조해야 한다.**

## 연도별 수록

| 연도 | 회의 수 |
|---|---|
| 1948 | 129 |
| 1949 | 190 |
| 1950 | 112 |
| 1951 | 201 |
| 1952 | 151 |
| 1953 | 158 |
| 1954 | 165 |
| 1955 | 209 |
| 1956 | 195 |
| 1957 | 223 |
| 1958 | 314 |
| 1959 | 325 |
| 1960 | 591 |
| 1961 | 643 |
| 1962 | 129 |
| 1963 | 30 |
| 1964 | 1,134 |
| 1965 | 671 |
| 1966 | 830 |
| 1967 | 386 |
| 1968 | 659 |
| 1969 | 406 |
| 1970 | 465 |
| 1971 | 97 |
| 1972 | 52 |
| 1973 | 32 |
| 1974 | 25 |
| 1975 | 32 |
| 1976 | 25 |
| 1977 | 29 |
| 1978 | 18 |
| 1979 | 32 |
| 1980 | 18 |
| 1981 | 35 |
| 1982 | 37 |
| 1983 | 35 |
| 1984 | 31 |
| 1985 | 45 |
| 1986 | 45 |
| 1987 | 20 |
| 1988 | 177 |
| 1989 | 246 |
| 1990 | 181 |
| 1991 | 221 |
| 1992 | 208 |
| 1993 | 500 |
| 1994 | 330 |
| 1995 | 363 |
| 1996 | 411 |
| 1997 | 397 |
| 1998 | 497 |
| 1999 | 332 |
| 2000 | 455 |
| 2001 | 707 |
| 2002 | 449 |
| 2003 | 703 |
| 2004 | 569 |
| 2005 | 947 |
| 2006 | 893 |
| 2007 | 895 |
| 2008 | 740 |
| 2009 | 678 |
| 2010 | 814 |
| 2011 | 506 |
| 2012 | 609 |
| 2013 | 877 |
| 2014 | 841 |
| 2015 | 935 |
| 2016 | 533 |
| 2017 | 800 |
| 2018 | 657 |
| 2019 | 689 |
| 2020 | 674 |
| 2021 | 468 |
| 2022 | 664 |
| 2023 | 878 |
| 2024 | 539 |
| 2025 | 833 |
| 2026 | 393 |

## 이용

국회 회의록은 공개 자료다. 다만 발언자 실명과 개별 발언이 그대로 들어 있으므로,
개인에 대한 판단이나 프로파일링에 쓰지 않기를 권한다.
