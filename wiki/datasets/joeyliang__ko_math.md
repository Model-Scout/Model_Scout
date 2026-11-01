---
type: "dataset"
id: "joeyliang/ko_math"
source: "huggingface"
url: "https://huggingface.co/datasets/joeyliang/ko_math"
downloads: 58
summary: "한국어 수학 문제와 답변 데이터셋으로, 수학 문제 풀이 질의응답에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# joeyliang/ko_math

> dataset · [Hugging Face](https://huggingface.co/datasets/joeyliang/ko_math)

한국어 수학 문제와 답변 데이터셋으로, 수학 문제 풀이 질의응답에 활용됨

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `- name: question
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `- name: answer
dtype: string` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `346` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 519자 ≈ 346 토큰 (viewer statistics, algebra/test)
