---
type: "dataset"
id: "psymon/Tiny-Ko-Stories"
source: "huggingface"
url: "https://huggingface.co/datasets/psymon/Tiny-Ko-Stories"
downloads: 101
summary: "Tiny-Ko-Stories는 한국어 어린이 이야기 데이터셋으로, 소형 모델 학습과 이야기 생성 연구에 활용됩니다."
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
  - "[[대규모 데이터]]"
---
# psymon/Tiny-Ko-Stories

> dataset · [Hugging Face](https://huggingface.co/datasets/psymon/Tiny-Ko-Stories)

Tiny-Ko-Stories는 한국어 어린이 이야기 데이터셋으로, 소형 모델 학습과 이야기 생성 연구에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — tag_match · tags = `language-modeling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `각 줄에는 `text` 필드 하나만 들어 있습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `각 줄에는 `text` 필드 하나만 들어 있습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `285` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Tiny-Ko-Stories는 TinyStories에서 영감을 받은 한국어 이야기 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `- 소형 한국어 causal language model 학습
- 한국어 이야기 생성 연구
- 교육용 NLP 실험
- continuation LM 실험` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 427자 ≈ 285 토큰 (viewer statistics, default/train)
