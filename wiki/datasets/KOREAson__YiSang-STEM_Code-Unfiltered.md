---
type: "dataset"
id: "KOREAson/YiSang-STEM_Code-Unfiltered"
source: "huggingface"
url: "https://huggingface.co/datasets/KOREAson/YiSang-STEM_Code-Unfiltered"
downloads: 173
summary: "YiSang-STEM_Code-Unfiltered는 STEM 및 코딩 주제의 한국어 프롬프트와 추론 데이터를 포함한 대규모 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# KOREAson/YiSang-STEM_Code-Unfiltered

> dataset · [Hugging Face](https://huggingface.co/datasets/KOREAson/YiSang-STEM_Code-Unfiltered)

YiSang-STEM_Code-Unfiltered는 STEM 및 코딩 주제의 한국어 프롬프트와 추론 데이터를 포함한 대규모 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `YiSang-STEM_Code-Unfiltered is a collection of 1.1M long-cot reasoning traces generated via Qwen3-32B.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `It consists of 128,524 unique Korean prompts related to STEM or Coding topics collected from the web.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `YiSang-STEM_Code-Unfiltered is a collection of 1.1M long-cot reasoning traces generated via Qwen3-32B.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `85827` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `It consists of 128,524 unique Korean prompts related to STEM or Coding topics collected from the web.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is not from the dataset used to train our KOREAson-0831 series. It's a bigger and unfiltered version, and might be used in our future iterations.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `responses` 열 p90 128741자 ≈ 85827 토큰 (viewer statistics, default/train)
