---
type: "dataset"
id: "humane-lab/K-HATERS"
source: "huggingface"
url: "https://huggingface.co/datasets/humane-lab/K-HATERS"
downloads: 315
summary: "한국어 혐오 표현 탐지 및 대상별 평가를 위한 대규모 코퍼스 K-HATERS 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# humane-lab/K-HATERS

> dataset · [Hugging Face](https://huggingface.co/datasets/humane-lab/K-HATERS)

한국어 혐오 표현 탐지 및 대상별 평가를 위한 대규모 코퍼스 K-HATERS 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `hate speech detection` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `Annotators' rationales for the strength of ratings` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `comments` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labels` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `81` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `We collected news comments published through the politics, society and world news sections in Naver News` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `We provide the split data of 172,158/10,000/10,000 for training, validation, and test purposes` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 122자 ≈ 81 토큰 (viewer statistics, default/validation)
