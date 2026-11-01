---
type: "dataset"
id: "aisamdasu/algocean-fable5-traces"
source: "huggingface"
url: "https://huggingface.co/datasets/aisamdasu/algocean-fable5-traces"
downloads: 64
summary: "FABLE5 계열 trace를 LangGraph/SFT 학습용 JSONL로 전처리한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# aisamdasu/algocean-fable5-traces

> dataset · [Hugging Face](https://huggingface.co/datasets/aisamdasu/algocean-fable5-traces)

FABLE5 계열 trace를 LangGraph/SFT 학습용 JSONL로 전처리한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `LangGraph 학습 포맷으로 펼쳤습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `prompt/completion 형태로 풀리면서 더 커졌습니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `67645` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `FABLE5 계열 trace를 LangGraph/SFT 학습용 JSONL로 전처리한 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `eval.jsonl: 512 rows` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train.jsonl: 30,265 rows` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 101467자 ≈ 67645 토큰 (viewer statistics, default/test)
