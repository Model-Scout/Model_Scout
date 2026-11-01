---
type: "dataset"
id: "Reubencf/multilingual-single-sentences"
source: "huggingface"
url: "https://huggingface.co/datasets/Reubencf/multilingual-single-sentences"
downloads: 19
summary: "다양한 언어의 단일 문장 완성 데이터셋으로, 지시 조정에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Reubencf/multilingual-single-sentences

> dataset · [Hugging Face](https://huggingface.co/datasets/Reubencf/multilingual-single-sentences)

다양한 언어의 단일 문장 완성 데이터셋으로, 지시 조정에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This is an instruction tuning dataset.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `This dataset consists of single-sentence completions spanning a diverse range of languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Each entry is presented as an isolated text completion without additional context or paired prompts.` · 신뢰도 medium
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `235` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The content varies widely, covering topics from historical restoration and travel logistics to proverbs and daily observations.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is an instruction tuning dataset.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `enhanced_prompt` 열 p90 940자 ≈ 235 토큰 (viewer statistics, default/train)
