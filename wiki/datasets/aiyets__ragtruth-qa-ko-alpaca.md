---
type: "dataset"
id: "aiyets/ragtruth-qa-ko-alpaca"
source: "huggingface"
url: "https://huggingface.co/datasets/aiyets/ragtruth-qa-ko-alpaca"
downloads: 30
summary: "ragtruth-qa 데이터를 GPT-4o로 한글 번역하고 alpaca 포맷으로 변환한 질의응답 데이터셋입니다."
readme_status: "template"
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
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# aiyets/ragtruth-qa-ko-alpaca

> dataset · [Hugging Face](https://huggingface.co/datasets/aiyets/ragtruth-qa-ko-alpaca)

ragtruth-qa 데이터를 GPT-4o로 한글 번역하고 alpaca 포맷으로 변환한 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `ragtruth-qa 데이터셋을 gpt-4o를 이용하여 한글로 번역 한 데이터셋.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `ragtruth-qa-ko 데이터 셋을 alpaca 포맷으로 변환.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `630` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 945자 ≈ 630 토큰 (viewer statistics, default/validation)
