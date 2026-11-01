---
type: "dataset"
id: "jjae/EPiK"
source: "huggingface"
url: "https://huggingface.co/datasets/jjae/EPiK"
downloads: 48
summary: "한국 문화 맥락과 물리 원리를 결합한 물리 상식 추론 평가용 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# jjae/EPiK

> dataset · [Hugging Face](https://huggingface.co/datasets/jjae/EPiK)

한국 문화 맥락과 물리 원리를 결합한 물리 상식 추론 평가용 한국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `EPiK is a Korean dataset that combines Korean cultural context and physical principles to evaluate AI models' physical commonsense reasoning capabilities.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `It consists of problems based on everyday situations that can be understood by any Korean person.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each problem is designed to require both physical reasoning and an understanding of Korean culture.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `EPiK is a Korean dataset that combines Korean cultural context and physical principles` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
