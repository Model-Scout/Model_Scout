---
type: "dataset"
id: "lotdpbc/word-orb-vocabulary"
source: "huggingface"
url: "https://huggingface.co/datasets/lotdpbc/word-orb-vocabulary"
downloads: 52
summary: "AI 에이전트와 교육용으로 설계된 162,253개 단어의 발음, 어원, 연령별 정의, 다국어 번역 포함 어휘 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lotdpbc/word-orb-vocabulary

> dataset · [Hugging Face](https://huggingface.co/datasets/lotdpbc/word-orb-vocabulary)

AI 에이전트와 교육용으로 설계된 162,253개 단어의 발음, 어원, 연령별 정의, 다국어 번역 포함 어휘 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering, task:translation = `Each word entry includes: IPA pronunciation for text-to-speech and phonetics research` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `48 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `59` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was curated by Lesson of the Day, PBC specifically for AI education agents` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `etymology` 열 p90 234자 ≈ 59 토큰 (viewer statistics, default/train)
