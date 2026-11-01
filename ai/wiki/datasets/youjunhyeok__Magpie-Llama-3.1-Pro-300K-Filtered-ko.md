---
type: "dataset"
id: "youjunhyeok/Magpie-Llama-3.1-Pro-300K-Filtered-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/youjunhyeok/Magpie-Llama-3.1-Pro-300K-Filtered-ko"
downloads: 91
summary: "Magpie-Align 데이터셋을 영어에서 한국어로 번역한 5천자 이하 정제 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# youjunhyeok/Magpie-Llama-3.1-Pro-300K-Filtered-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/youjunhyeok/Magpie-Llama-3.1-Pro-300K-Filtered-ko)

Magpie-Align 데이터셋을 영어에서 한국어로 번역한 5천자 이하 정제 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `For this dataset, we only used data that is 5000 characters or less in length and has language of English.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Translated Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1507` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `For this dataset, we only used data that is 5000 characters or less in length and has language of English.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 2260자 ≈ 1507 토큰 (viewer statistics, default/train)
