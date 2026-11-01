---
type: "dataset"
id: "ffatty/plaintext-wikipedia-full-korean"
source: "huggingface"
url: "https://huggingface.co/datasets/ffatty/plaintext-wikipedia-full-korean"
downloads: 51
summary: "한국어 위키백과의 압축된 평문 문서 데이터셋으로 텍스트 분석에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ffatty/plaintext-wikipedia-full-korean

> dataset · [Hugging Face](https://huggingface.co/datasets/ffatty/plaintext-wikipedia-full-korean)

한국어 위키백과의 압축된 평문 문서 데이터셋으로 텍스트 분석에 활용 가능

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `Compressed plaintext articles from Korean Wikipedia.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `Compressed plaintext articles from Korean Wikipedia.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `titles and cleaned text are stored as UTF-8 in independent gzip shards.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `38128` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Compressed plaintext articles from Korean Wikipedia.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Produced and maintained by cheeseonamonkey/PlainTextWikipedia.` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 57192자 ≈ 38128 토큰 (viewer statistics, default/train)
