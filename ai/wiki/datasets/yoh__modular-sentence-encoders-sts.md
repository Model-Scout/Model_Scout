---
type: "dataset"
id: "yoh/modular-sentence-encoders-sts"
source: "huggingface"
url: "https://huggingface.co/datasets/yoh/modular-sentence-encoders-sts"
downloads: 135
summary: "23개 언어의 의미 텍스트 유사도 및 관련성 평가 데이터로, 문장 임베딩 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# yoh/modular-sentence-encoders-sts

> dataset · [Hugging Face](https://huggingface.co/datasets/yoh/modular-sentence-encoders-sts)

23개 언어의 의미 텍스트 유사도 및 관련성 평가 데이터로, 문장 임베딩 평가용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `sentence-similarity` · 신뢰도 high
- **작업**: [[질의응답]] — ner · readme = `STS / STR evaluation sets, resolved (23 languages)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:question_answering = `One row per sentence pair, in every config: | column | type | meaning | |---|---|---| | `lang_a` | string | language of `sentence_a`, a two-letter code | | `lan` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `| `score` | float | gold similarity or relatedness; the scale is the source benchmark's |` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `19` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The semantic textual similarity and relatedness evaluation data of Modular Sentence Encoders` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Each config has a single `test` split: these are evaluation sets, and none of them is meant to be trained on.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `sentence_a` 열 p90 75자 ≈ 19 토큰 (viewer statistics, sick/test)
