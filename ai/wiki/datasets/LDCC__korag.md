---
type: "dataset"
id: "LDCC/korag"
source: "huggingface"
url: "https://huggingface.co/datasets/LDCC/korag"
downloads: 171
summary: "한국어 PDF 문서에서 질의에 맞는 문서를 검색하고 응답을 생성하는 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# LDCC/korag

> dataset · [Hugging Face](https://huggingface.co/datasets/LDCC/korag)

한국어 PDF 문서에서 질의에 맞는 문서를 검색하고 응답을 생성하는 질의응답 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `원본 PDF 파일에서 질의에 맞는 문서를 검색하고 이를 기반으로 응답을 생성하는 질의응답 데이터셋입니다.` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `원본 PDF 파일에서 질의에 맞는 문서를 검색하고 이를 기반으로 응답을 생성하는 질의응답 데이터셋입니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval = `원본 PDF 파일에서 질의에 맞는 문서를 검색하고 이를 기반으로 응답을 생성하는 질의응답 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `원본 PDF 파일에서 질의에 맞는 문서를 검색하고 이를 기반으로 응답을 생성하는 질의응답 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `107` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `문서는 백과, 법률, 의학, 교육, 행정의 5개 범주로 구성되며, 지식재산권 및 저작권을 고려하여 공공 문서를 바탕으로 제작되었습니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `학습 및 평가 데이터셋의 특징은 다음과 같습니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `학습 및 평가 데이터셋의 특징은 다음과 같습니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 161자 ≈ 107 토큰 (viewer statistics, qa/validation)
