---
type: "dataset"
id: "QuasarLAB/synthetic-transit-routing-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/QuasarLAB/synthetic-transit-routing-ko"
downloads: 49
summary: "한국어 정류장명과 경로 질문으로 구성된 합성 대중교통 경로 탐색 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# QuasarLAB/synthetic-transit-routing-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/QuasarLAB/synthetic-transit-routing-ko)

한국어 정류장명과 경로 질문으로 구성된 합성 대중교통 경로 탐색 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Use the timetable and routing question as model inputs, and the reference answer as supervision.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Stop names and routing questions are in Korean.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `the earliest-arrival reference answer, including route legs, arrival time, total duration, boardings, and transfers.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `35` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `A small synthetic dataset for studying whether language models can compute transit routes directly from a provided timetable` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Keep test and OOD examples held out from training.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains 352 examples: 220 training, 44 validation, 44 test, and 44 out-of-distribution (OOD) examples.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 53자 ≈ 35 토큰 (viewer statistics, default/validation)
