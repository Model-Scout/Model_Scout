---
type: "dataset"
id: "watchstep/ko-en-code-mixing-sts"
source: "huggingface"
url: "https://huggingface.co/datasets/watchstep/ko-en-code-mixing-sts"
downloads: 15
summary: "KLUE-STS에서 파생된 한국어-영어 코드믹싱 문장 쌍 1,500개로 의미 유사도 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
  - "[[소규모 데이터]]"
---
# watchstep/ko-en-code-mixing-sts

> dataset · [Hugging Face](https://huggingface.co/datasets/watchstep/ko-en-code-mixing-sts)

KLUE-STS에서 파생된 한국어-영어 코드믹싱 문장 쌍 1,500개로 의미 유사도 평가용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `sentence-similarity` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `semantic similarity score from KLUE-STS` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `sentence_a and apply insertion-only code-mixing to sentence_b` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `49` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean–English code-mixed pairs derived from KLUE-STS` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains 1,500 Korean–English code-mixed pairs derived from KLUE-STS` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `sentence_b` 열 p90 74자 ≈ 49 토큰 (viewer statistics, default/train)
