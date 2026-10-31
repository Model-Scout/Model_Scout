---
type: "dataset"
id: "Translation-EnKo/trc_uniform_313k_eval_45_filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/Translation-EnKo/trc_uniform_313k_eval_45_filtered"
downloads: 23
summary: "nayohan/translate_corpus_uniform_313k 데이터셋을 평가하기 위해 nayohan/llama3-8b-it-prometheus-ko 모델로 점수 4,5를 필터링한 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Translation-EnKo/trc_uniform_313k_eval_45_filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/Translation-EnKo/trc_uniform_313k_eval_45_filtered)

nayohan/translate_corpus_uniform_313k 데이터셋을 평가하기 위해 nayohan/llama3-8b-it-prometheus-ko 모델로 점수 4,5를 필터링한 평가 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `We filtered out rows with a score of 4,5.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Write a detailed feedback that assess the quality of… See the full description on the dataset page` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `an instruction (might include an Input inside it), a response to evaluate, a reference answer` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Write a detailed feedback that assess the quality of…` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `79` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `We used nayohan/llama3-8b-it-prometheus-ko to evaluate the nayohan/translate_corpus_uniform_313k dataset` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `We used nayohan/llama3-8b-it-prometheus-ko to evaluate the nayohan/translate_corpus_uniform_313k dataset` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 315자 ≈ 79 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[mradermacher__exaone3-instrucTrans-v2-enko-7.8b-GGUF|mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF]]
- [[mradermacher__exaone3-instrucTrans-v2-enko-7.8b-i1-GGUF|mradermacher/exaone3-instrucTrans-v2-enko-7.8b-i1-GGUF]]
