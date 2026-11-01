---
type: "dataset"
id: "schift-io/korean-pii-benchmark-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/schift-io/korean-pii-benchmark-v3"
downloads: 96
summary: "한국어 개인정보(사람, 기관, 주소) 탐지 모델 평가용 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# schift-io/korean-pii-benchmark-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/schift-io/korean-pii-benchmark-v3)

한국어 개인정보(사람, 기관, 주소) 탐지 모델 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `court judgments, news articles, administrative documents, medical/insurance records, transcripts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `473 cases for evaluating Korean PII (person, organization, address) detection models.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `66` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `Covers court judgments, news articles, administrative documents, medical/insurance records, transcripts` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `473 cases for evaluating Korean PII (person, organization, address) detection models.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 99자 ≈ 66 토큰 (viewer statistics, default/train)
