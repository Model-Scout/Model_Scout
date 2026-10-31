---
type: "dataset"
id: "shanearora/CaLMQA"
source: "huggingface"
url: "https://huggingface.co/datasets/shanearora/CaLMQA"
downloads: 125
summary: "CaLMQA는 23개 언어의 문화 특화 장문 질의응답 데이터셋으로 다국어 모델 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# shanearora/CaLMQA

> dataset · [Hugging Face](https://huggingface.co/datasets/shanearora/CaLMQA)

CaLMQA는 23개 언어의 문화 특화 장문 질의응답 데이터셋으로 다국어 모델 평가용입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `CaLMQA is a translation-free long-form question answering (LFQA) dataset spanning 23 high- to low-resource languages.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `The dataset consists of QA entries. Entry structure: - `language`: The language of the question. - `question`: The question that admits a long-form answer, in t` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `- `answer` (optional): The answer to the question, in the language `language`. These answers were written by `language` crowdworkers or collected from `language` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `152` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `These questions were collected to evaluate the multilingual capabilities and cultural knowledge of state-of-the-art models.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `38.6K (~25% of the original 51.7K questions are held out in private test set)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 609자 ≈ 152 토큰 (viewer statistics, default/train)
