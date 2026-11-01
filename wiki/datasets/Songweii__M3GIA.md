---
type: "dataset"
id: "Songweii/M3GIA"
source: "huggingface"
url: "https://huggingface.co/datasets/Songweii/M3GIA"
downloads: 296
summary: "M3GIA는 다국어·다중모달 대형언어모델의 인지능력을 평가하는 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Songweii/M3GIA

> dataset · [Hugging Face](https://huggingface.co/datasets/Songweii/M3GIA)

M3GIA는 다국어·다중모달 대형언어모델의 인지능력을 평가하는 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `introduce the first cognitive-driven multi-lingual and multi-modal benchmark to evaluate the general intelligence ability of MLLMs` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `cognitive-driven multi-lingual and multi-modal benchmark` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `evaluate the general intelligence ability of MLLMs` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `multi-lingual and multi-modal benchmark` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:question_answering = `multi-lingual and multi-modal benchmark` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `evaluate the general intelligence ability of MLLMs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `70` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multi-modality large language models (MLLMs) have shown formidable proficiency on various complex tasks` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `We collected a significant corpus of data from human participants, revealing that the most advanced MLLM reaches the lower boundary of human intelligence in Eng` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 281자 ≈ 70 토큰 (viewer statistics, korean/test)
