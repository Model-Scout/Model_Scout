---
language:
  - ko
  - en
license: mit
task_categories:
  - text-generation
  - question-answering
tags:
  - llm-routing
  - benchmark
  - translation
  - korean
pretty_name: RouterBench Korean Translation
---
# RouterBench 한국어 번역 공개판

`withmartian/routerbench`의 영어 프롬프트를 한국어로 번역해 공개하는 데이터셋입니다.

* 원본: `withmartian/routerbench`
* 번역 모델: `google/translategemma-27b-it`
* 품질 검수: Codex (`gpt-5.6-sol`) 원문 대조 검수 및 일부 휴먼 검수
* 공개 데이터: 검수 결과를 반영한 최종 교정본
* 번역 열: `prompt_ko`
* 원본 열과 기존 평가 결과: 변경 없음

## 파일

| 파일                             |    행 수 | 설명              |
| ------------------------------ | -----: | --------------- |
| `routerbench_0shot_ko.parquet` | 36,497 | 0-shot 한국어 프롬프트 |
| `routerbench_5shot_ko.parquet` | 36,511 | 5-shot 한국어 프롬프트 |
| `routerbench_0shot_ko.jsonl.gz` | 36,497 | 0-shot 압축 JSONL |
| `routerbench_5shot_ko.jsonl.gz` | 36,511 | 5-shot 압축 JSONL |

* 0-shot: 예시 없이 평가 문항만 제시
* 5-shot: 원본 RouterBench에 포함된 예시 5개와 평가 문항을 함께 제시
* 두 파일은 번역 품질의 차이가 아니라 서로 다른 원본 평가 조건을 보존한 것
* `.jsonl.gz`는 대응하는 Parquet과 내용이 같으며, JSONL 형식으로 직렬화한 뒤 gzip으로 압축한 파일

## 사용법

`prompt`와 `prompt_ko`는 파이썬 리스트 리터럴 문자열

```python
import ast
import pandas as pd

df = pd.read_parquet("routerbench_0shot_ko.parquet")

source_original = ast.literal_eval(df.loc[0, "prompt"])
translation_ko = ast.literal_eval(df.loc[0, "prompt_ko"])

print(source_original[0])
print(translation_ko[0])
```

## 번역 원칙

* 영어 질문·지시문·선택지는 한국어로 번역
* 숫자·단위·비율·부정·선택지 순서·코드·수식·URL 보존
* 원문과 같은 정답 가능성과 유사한 문제 난이도 유지
* 중국어 자형 수수께끼 등 번역하면 단서가 사라지는 문항은 원문 유지
* 원문 자체의 비문·절단 토큰·OCR 오류는 임의로 복원하지 않음

### HellaSwag 절단 토큰

* 원문 예: `, ls, and pickles`
* 공개판: `추와 피클`
* `ls → 추`는 사전적 번역이 아니라 의미 없는 원문 조각과 상대적 난이도를 보존하기 위한 처리

### 비영어 문자 문제

* 한자의 모양·발음·부수 분해가 단서인 문항은 해당 문자열을 그대로 유지
* 영어 설명과 중국어가 섞인 경우 영어 설명만 번역
* 내부 정책명: `passthrough_non_english`

### WinoGrande

* WinoGrande는 공지시 및 빈칸 지시 대상 판별 과제로 번역 대상에 포함
* `_` 빈칸 유지
* 후보에 따라 형태가 달라지는 조사는 `_은/는`, `_이/가`, `_을/를`, `_와/과`, `_로/으로`처럼 병기
* 후보 이름을 빈칸에 직접 넣어 정답을 노출하지 않음

## 응답 언어와 채점

* 기존 모델 응답과 점수 열은 원본 영어 프롬프트로 평가한 결과이며, 한국어 프롬프트를 다시 실행한 결과가 아님
* 한국어 프롬프트로 새로 평가할 때는 응답 언어보다 원본 벤치마크의 출력 형식을 유지하는 것이 중요
* 객관식(MMLU, ARC, WinoGrande 등): `A`, `B`, `C`, `D`와 같은 선택지 문자만 출력하면 언어와 무관하게 채점 가능
* 수학(GSM8K 등): 최종 숫자나 지정된 정답 형식을 유지하면 한국어 풀이도 채점 가능
* 코드(MBPP 등): 원본 코드 채점기를 재사용하며 코드 출력 형식을 유지
* 자유서술형: 영어만 전제로 한 채점기는 한국어 답변을 정확히 평가하지 못할 수 있으므로 한국어 지원 judge 또는 언어 독립 평가기를 사용

## 알려진 한계

* 원본에 포함된 비문·절단 토큰·OCR 오류가 일부 유지됨
* 일부 비영어 문항은 과제 단서 보존을 위해 번역하지 않음
* 문체·뉘앙스 차이가 남아 있을 수 있음
* 원본 5-shot 데이터의 `arc-challenge`에는 14개 `sample_id`가 각각 두 번 나타남. 같은 ID의 두 행은 프롬프트와 평가 결과가 서로 다른 원본 레코드이므로 삭제하지 않고 보존함

## 출처와 사용 조건

* 원본 데이터셋: `withmartian/routerbench`
* 번역 모델: `google/translategemma-27b-it`
* 공개·재배포 시 원본 데이터와 모델의 라이선스 및 사용 조건을 확인하고 출처를 표기해야 함
