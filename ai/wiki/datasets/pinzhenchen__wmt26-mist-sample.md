---
type: "dataset"
id: "pinzhenchen/wmt26-mist-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/pinzhenchen/wmt26-mist-sample"
downloads: 55
summary: "WMT26 MIST 공유 과제에서 제공하는 다국어 QA 및 요약 데이터로 다국어 LLM 미세조정에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# pinzhenchen/wmt26-mist-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/pinzhenchen/wmt26-mist-sample)

WMT26 MIST 공유 과제에서 제공하는 다국어 QA 및 요약 데이터로 다국어 LLM 미세조정에 활용됨.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:summarization = `the input is self-contained, which includes the task prompt, context, etc.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:summarization = `the expected output` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `27 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1589` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual mix provided by the WMT26 MIST shared task organizers` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `a starting point for fine-tuning multilingual LLMs` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 6356자 ≈ 1589 토큰 (viewer statistics, default/train)
