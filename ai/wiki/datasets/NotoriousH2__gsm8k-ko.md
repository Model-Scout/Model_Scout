---
type: "dataset"
id: "NotoriousH2/gsm8k-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/NotoriousH2/gsm8k-ko"
downloads: 53
summary: "GSM8K에서 생성된 한국어 수학 문제 풀이 데이터셋으로 학습과 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NotoriousH2/gsm8k-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/NotoriousH2/gsm8k-ko)

GSM8K에서 생성된 한국어 수학 문제 풀이 데이터셋으로 학습과 평가에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `train split with question, answer, parsed_answer, and original GSM8K fields.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `train split with question, answer, parsed_answer, and original GSM8K fields.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `327` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `full test: 1,296` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `full train: 7,309` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `original_answer` 열 p90 490자 ≈ 327 토큰 (viewer statistics, eval/test)
