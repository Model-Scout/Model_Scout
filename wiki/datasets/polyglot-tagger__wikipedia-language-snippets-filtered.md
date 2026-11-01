---
type: "dataset"
id: "polyglot-tagger/wikipedia-language-snippets-filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/polyglot-tagger/wikipedia-language-snippets-filtered"
downloads: 50
summary: "위키피디아 문서의 처음 60% 문장 스니펫을 필터링하여 언어별로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
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
  - "[[대규모 데이터]]"
---
# polyglot-tagger/wikipedia-language-snippets-filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/polyglot-tagger/wikipedia-language-snippets-filtered)

위키피디아 문서의 처음 60% 문장 스니펫을 필터링하여 언어별로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `Filtered sentence snippets in Wikipedia` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Filtered sentence snippets in Wikipedia` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `104 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `63` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Filtered sentence snippets in Wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train/en/en.parquet
train/es/es.parquet` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 250자 ≈ 63 토큰 (viewer statistics, default/train)
