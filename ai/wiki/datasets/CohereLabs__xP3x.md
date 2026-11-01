---
type: "dataset"
id: "CohereLabs/xP3x"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/xP3x"
downloads: 70352
summary: "xP3x는 277개 언어와 16개 NLP 작업을 포함한 다국어 프롬프트 및 데이터셋 모음으로, mT0와 BLOOMZ 모델 학습에 사용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# CohereLabs/xP3x

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/xP3x)

xP3x는 277개 언어와 16개 NLP 작업을 포함한 다국어 프롬프트 및 데이터셋 모음으로, mT0와 BLOOMZ 모델 학습에 사용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `16 NLP tasks` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `a collection of prompts & datasets across 277 languages & 16 NLP tasks` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `16 NLP tasks` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:question_answering = `the natural language input fed to the model` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `the natural language target that the model has to generate` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `220 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `497` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a collection of prompts & datasets across 277 languages & 16 NLP tasks` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It is used for training future contenders of mT0 & BLOOMZ at project Aya @Cohere Labs` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `inputs` 열 p90 1986자 ≈ 497 토큰 (viewer statistics, kor_Hang/train)
