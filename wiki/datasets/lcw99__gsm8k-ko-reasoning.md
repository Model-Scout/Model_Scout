---
type: "dataset"
id: "lcw99/gsm8k-ko-reasoning"
source: "huggingface"
url: "https://huggingface.co/datasets/lcw99/gsm8k-ko-reasoning"
downloads: 14
summary: "openai/gsm8k를 한글로 번역하고 추론 데이터를 추가한 수학 문제 풀이 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lcw99/gsm8k-ko-reasoning

> dataset · [Hugging Face](https://huggingface.co/datasets/lcw99/gsm8k-ko-reasoning)

openai/gsm8k를 한글로 번역하고 추론 데이터를 추가한 수학 문제 풀이 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `한글 질문을 Deepseek-R1에서 추론, 답변을 작성하였습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `영어질문을 먼저 한글로 번역하고 한글 질문을 Deepseek-R1에서 추론` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `한글 질문을 Deepseek-R1에서 추론, 답변을 작성하였습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `835` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `openai/gsm8k를 한글로 변환하고 추론 데이터를 추가한 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `openai/gsm8k를 한글로 변환하고 추론 데이터를 추가한 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `reasoning` 열 p90 1253자 ≈ 835 토큰 (viewer statistics, default/train)
