---
type: "dataset"
id: "jaeyong2/cartesia-sonic-preview-ztts1-zero-shot-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/cartesia-sonic-preview-ztts1-zero-shot-sample"
downloads: 39
summary: "Cartesia Sonic 음성 합성 모델의 제로샷 샘플과 참조 음성을 포함한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# jaeyong2/cartesia-sonic-preview-ztts1-zero-shot-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/cartesia-sonic-preview-ztts1-zero-shot-sample)

Cartesia Sonic 음성 합성 모델의 제로샷 샘플과 참조 음성을 포함한 데이터셋입니다.

## 분류

- **작업**: [[음성 합성]] — metadata · readme, tags, task_categories = `text-to-speech` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = ``reference_audio` | the recording it was cloning` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:text_to_speech = ``target_text` | what the model was asked to say` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = ``audio` | the clip the model produced` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `100 utterances per language (700 rows) from the zero-shot subsets of ZTTS1-Eval` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
