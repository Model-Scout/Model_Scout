---
type: "dataset"
id: "twodigit/squad-kor-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/twodigit/squad-kor-v2"
downloads: 231
summary: "KorQuAD 2.1은 한국어 위키피디아 기반 MRC 데이터셋으로 QA 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# twodigit/squad-kor-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/twodigit/squad-kor-v2)

KorQuAD 2.1은 한국어 위키피디아 기반 MRC 데이터셋으로 QA 학습에 사용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `한국어 MRC 데이터셋` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `context는 paragraphs가 아닌, table과 list가 포함된 전체 Wikipedia 페이지` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `answer는 paragraphs, tables, lists를 포괄하는 긴 텍스트일 수 있음` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia article에 대해` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `dev 10,165` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 83,486` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
