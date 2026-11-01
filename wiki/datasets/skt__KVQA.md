---
type: "dataset"
id: "skt/KVQA"
source: "huggingface"
url: "https://huggingface.co/datasets/skt/KVQA"
downloads: 130
summary: "한국 시각장애인이 촬영한 이미지와 질문, 답변으로 구성된 한국형 시각적 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# skt/KVQA

> dataset · [Hugging Face](https://huggingface.co/datasets/skt/KVQA)

한국 시각장애인이 촬영한 이미지와 질문, 답변으로 구성된 한국형 시각적 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `시각적 질의응답은 이미지가 주어지고 그 이미지에 대한 질문이 주어졌을 때, 이미지를 이해하여 자연어로 질문에 대한 답을 주는 기술입니다.` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `시각적 질의응답은 이미지가 주어지고` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `이미지에 대한 질문이 주어졌을 때` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `이미지를 이해하여 자연어로 질문에 대한 답을 주는 기술입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `2019년 4월부터 이 기술의 현지화를 위해 사회적 기업인 테스트웍스와 협업하여 자발적으로 지원한 우리나라의 시각장애인들로부터 데이터를 수집하였고` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 교육 및 연구목적으로 사용이 가능하며` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
