---
type: "dataset"
id: "Nexdata-kr/Long-Context-Reasoning-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/Nexdata-kr/Long-Context-Reasoning-Dataset"
downloads: 80
summary: "장문 문서 기반 복잡한 추론 질문으로 LLM의 장거리 문맥 이해와 추론 능력 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Nexdata-kr/Long-Context-Reasoning-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/Nexdata-kr/Long-Context-Reasoning-Dataset)

장문 문서 기반 복잡한 추론 질문으로 LLM의 장거리 문맥 이해와 추론 능력 평가용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `여러 문단과 문서에 걸쳐 정보를 종합하고 여러 단계의 논리적 추론 과정을 거쳐야 답변할 수 있는 질문으로 구성되어 있습니다.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `각 데이터는 장문의 텍스트를 기반으로 하며` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `답변할 수 있는 질문으로 구성되어 있습니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `중국어, 영어, 한국어의 3개 언어로 구성된 총 7,500개의 고품질 학습 데이터를 포함하고 있습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `총 7,500개의 고품질 학습 데이터를 포함하고 있습니다.` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
