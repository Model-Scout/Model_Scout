---
type: "dataset"
id: "shchoice/finance-legal-mrc"
source: "huggingface"
url: "https://huggingface.co/datasets/shchoice/finance-legal-mrc"
downloads: 33
summary: "금융 및 법률 전문문서 기반 기계독해 모델 학습용 지문-질문-답변 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# shchoice/finance-legal-mrc

> dataset · [Hugging Face](https://huggingface.co/datasets/shchoice/finance-legal-mrc)

금융 및 법률 전문문서 기반 기계독해 모델 학습용 지문-질문-답변 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — tag_match · readme, tags = `mrc` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `table_html: 표의 HTML 데이터` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `문장의 주요 텍스트 내용` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `정답이 포함된 셀의 텍스트 데이터` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `정답 텍스트` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `661` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train: 학습용 데이터셋` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 992자 ≈ 661 토큰 (viewer statistics, multiple_choice/test)
