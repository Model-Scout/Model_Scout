---
type: "dataset"
id: "shannonnonshan/en-sumerize"
source: "huggingface"
url: "https://huggingface.co/datasets/shannonnonshan/en-sumerize"
downloads: 137
summary: "BBC 뉴스 기사로부터 수집된 44개 언어의 대규모 다국어 요약 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[요약]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# shannonnonshan/en-sumerize

> dataset · [Hugging Face](https://huggingface.co/datasets/shannonnonshan/en-sumerize)

BBC 뉴스 기사로부터 수집된 44개 언어의 대규모 다국어 요약 데이터셋입니다.

## 분류

- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:summarization = `- `text` : A string containing the article text.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `- `summary`: A string containing the article summary.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `61` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `The data stems from BBC news articles.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `It is intended to be used for both multilingual and per-language summarization tasks.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `webdataset` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `__url__` 열 p90 244자 ≈ 61 토큰 (viewer statistics, default/train)
