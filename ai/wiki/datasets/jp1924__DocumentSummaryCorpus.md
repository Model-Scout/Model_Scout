---
type: "dataset"
id: "jp1924/DocumentSummaryCorpus"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924/DocumentSummaryCorpus"
downloads: 5
summary: "한국어 문서 요약 데이터셋으로 텍스트 생성에 활용됨"
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
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
---
# jp1924/DocumentSummaryCorpus

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924/DocumentSummaryCorpus)

한국어 문서 요약 데이터셋으로 텍스트 생성에 활용됨

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `- name: corpus
dtype: string` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `- name: summary_sentences
list: string` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `splits:
- name: train` · 신뢰도 medium
