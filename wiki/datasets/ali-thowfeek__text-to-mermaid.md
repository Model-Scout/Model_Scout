---
type: "dataset"
id: "ali-thowfeek/text-to-mermaid"
source: "huggingface"
url: "https://huggingface.co/datasets/ali-thowfeek/text-to-mermaid"
downloads: 28
summary: "Mermaid 문법 기반 다이어그램 생성용 소형 언어모델 파인튜닝 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ali-thowfeek/text-to-mermaid

> dataset · [Hugging Face](https://huggingface.co/datasets/ali-thowfeek/text-to-mermaid)

Mermaid 문법 기반 다이어그램 생성용 소형 언어모델 파인튜닝 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `fine-tuning small language models on diagram generation tasks` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `when prompted for a diagram, the model outputs only the Mermaid syntax` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `the model outputs only the Mermaid syntax` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `105` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A curated dataset designed for fine-tuning small language models on diagram generation tasks.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Fine-tuning small LLMs for structured diagram generation` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 418자 ≈ 105 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[ali-thowfeek__Charty-1B-GGUF|ali-thowfeek/Charty-1B-GGUF]]
