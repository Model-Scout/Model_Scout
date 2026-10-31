---
type: "dataset"
id: "mkd-chanwoo/keural-conversation-chatml-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-chanwoo/keural-conversation-chatml-ko"
downloads: 34
summary: "mkd-chanwoo/keural-conversation-ko 데이터셋을 ChatML 포맷으로 전처리한 한국어 일상대화 데이터셋입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mkd-chanwoo/keural-conversation-chatml-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-chanwoo/keural-conversation-chatml-ko)

mkd-chanwoo/keural-conversation-ko 데이터셋을 ChatML 포맷으로 전처리한 한국어 일상대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `ChatML 형식의 멀티턴 대화입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `ChatML 형식의 멀티턴 대화입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `256` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `9개 주제의 일상 캐주얼 대화를 Gemma-4-26B 모델이 생성한 synthetic 멀티턴 대화로 구성되어 있습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SFT 학습용 ChatML 포맷으로 전처리한 한국어 일상대화 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 384자 ≈ 256 토큰 (viewer statistics, default/train)
