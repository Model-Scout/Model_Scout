---
type: "dataset"
id: "lingvenvist/animacy-ko-nogroups-xtr-complete-filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/lingvenvist/animacy-ko-nogroups-xtr-complete-filtered"
downloads: 12
summary: "XL-WSD v1의 한국어 처리 버전으로 의미중심 단어 식별에 사용됨."
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
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lingvenvist/animacy-ko-nogroups-xtr-complete-filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/lingvenvist/animacy-ko-nogroups-xtr-complete-filtered)

XL-WSD v1의 한국어 처리 버전으로 의미중심 단어 식별에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Note that this is a processed version of XL-WSD v1` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Note that this is a processed version of XL-WSD v1` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Note that this is a processed version of XL-WSD v1` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `15` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Note that this is a processed version of XL-WSD v1` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `sentences` 열 p90 22자 ≈ 15 토큰 (viewer statistics, default/validation)
