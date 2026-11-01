---
type: "dataset"
id: "mkd-jueon/YiSang-HighQuality-chatml-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-jueon/YiSang-HighQuality-chatml-v1"
downloads: 42
summary: "한국어 SFT용으로 가공된 고품질 ChatML 포맷 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
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
# mkd-jueon/YiSang-HighQuality-chatml-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-jueon/YiSang-HighQuality-chatml-v1)

한국어 SFT용으로 가공된 고품질 ChatML 포맷 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `답변은 LLM 생성(synthetic) 기반이므로 품질 편차가 있을 수 있습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `ChatML (` role ... `)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `ChatML (` role ... `)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1696` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KOREAson/YiSang-HighQuality를 한국어 SFT용으로 가공한 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 SFT용으로 가공한 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2544자 ≈ 1696 토큰 (viewer statistics, default/train)
