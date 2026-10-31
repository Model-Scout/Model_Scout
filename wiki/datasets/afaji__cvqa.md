---
type: "dataset"
id: "afaji/cvqa"
source: "huggingface"
url: "https://huggingface.co/datasets/afaji/cvqa"
downloads: 1970
summary: "CVQA는 39개국 언어로 된 10,000개 이상의 질문을 포함한 다문화 다국어 VQA 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
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
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# afaji/cvqa

> dataset · [Hugging Face](https://huggingface.co/datasets/afaji/cvqa)

CVQA는 39개국 언어로 된 10,000개 이상의 질문을 포함한 다문화 다국어 VQA 평가용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[이미지 이해]] — ner · readme = `CVQA is a culturally diverse multilingual VQA benchmark consisting of over 10,000 questions from 39 country-language pairs.` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `The image referenced by the question.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:visual_qa = `The questions in CVQA are written in both the native languages and English` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `The questions in CVQA are written in both the native languages and English` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `47` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `CVQA is a culturally diverse multilingual VQA benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This data is designed for use as a test set.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Image Source` 열 p90 186자 ≈ 47 토큰 (viewer statistics, default/test)
