---
type: "dataset"
id: "bkai-foundation-models/vi-alpaca-input-output-format"
source: "huggingface"
url: "https://huggingface.co/datasets/bkai-foundation-models/vi-alpaca-input-output-format"
downloads: 34
summary: "베트남어 기반 언어 모델 학습용 고품질 Alpaca 스타일 명령-입력-출력 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# bkai-foundation-models/vi-alpaca-input-output-format

> dataset · [Hugging Face](https://huggingface.co/datasets/bkai-foundation-models/vi-alpaca-input-output-format)

베트남어 기반 언어 모델 학습용 고품질 Alpaca 스타일 명령-입력-출력 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The motivation behind the creation of this dataset stems from the hope to contribute high-quality dataset to Vietnamese commnunity to train language models.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `we adapted prompts and generated data in the form of input/output using GPT-4, GPT-3.5, and GPT-3.5-instruct.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `we adapted prompts and generated data in the form of input/output using GPT-4, GPT-3.5, and GPT-3.5-instruct.` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `478` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset is especially designed for Vietnamese based on the idea from Stanford Alpaca, Self-Instruct paper and Chinese LLaMA.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The motivation behind the creation of this dataset stems from the hope to contribute high-quality dataset to Vietnamese commnunity to train language models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1914자 ≈ 478 토큰 (viewer statistics, default/train)
