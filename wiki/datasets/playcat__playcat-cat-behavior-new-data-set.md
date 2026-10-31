---
type: "dataset"
id: "playcat/playcat-cat-behavior-new-data-set"
source: "huggingface"
url: "https://huggingface.co/datasets/playcat/playcat-cat-behavior-new-data-set"
downloads: 126
summary: "고양이 행동풍부화 연구를 위한 한영 이중언어 데이터셋으로, 학술·특허·커뮤니티 지식 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# playcat/playcat-cat-behavior-new-data-set

> dataset · [Hugging Face](https://huggingface.co/datasets/playcat/playcat-cat-behavior-new-data-set)

고양이 행동풍부화 연구를 위한 한영 이중언어 데이터셋으로, 학술·특허·커뮤니티 지식 포함

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `The PlayCat Cat Behavioral Enrichment Dataset is the largest open, bilingual (Korean-English) collection dedicated to feline environmental enrichment research.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Fine-tune question-answering and text-generation models for pet care chatbots, veterinary decision support systems, and personalized enrichment recommendation e` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1558` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Fine-tune question-answering and text-generation models for pet care chatbots, veterinary decision support systems, and personalized enrichment recommendation e` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2337자 ≈ 1558 토큰 (viewer statistics, enrichment_raw/train)
