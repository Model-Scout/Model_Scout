---
type: "dataset"
id: "kuotient/orca-math-korean-preference"
source: "huggingface"
url: "https://huggingface.co/datasets/kuotient/orca-math-korean-preference"
downloads: 30
summary: "Orca-math-korean-preference는 Orca-math 데이터셋의 수학 문제 답변을 LLM으로 평가한 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kuotient/orca-math-korean-preference

> dataset · [Hugging Face](https://huggingface.co/datasets/kuotient/orca-math-korean-preference)

Orca-math-korean-preference는 Orca-math 데이터셋의 수학 문제 답변을 LLM으로 평가한 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `llm: claude-haiku와 gpt3.5로 평가된 generated(Student) answer의 정답 여부` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `question: orca-math dataset의 question` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `label: llm의 참/거짓` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `976` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `orca-math dataset의 question` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `llm: claude-haiku와 gpt3.5로 평가된 generated(Student) answer의 정답 여부` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer_en` 열 p90 1465자 ≈ 976 토큰 (viewer statistics, default/train)
