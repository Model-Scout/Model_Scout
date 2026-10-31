---
type: "dataset"
id: "LLM-SocialMedia/Korean-YouTube-Comment-Sentiment-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-SocialMedia/Korean-YouTube-Comment-Sentiment-Dataset"
downloads: 148
summary: "유튜브 한국어 댓글 5,482개와 감정 레이블로 구성된 감정 분류용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# LLM-SocialMedia/Korean-YouTube-Comment-Sentiment-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-SocialMedia/Korean-YouTube-Comment-Sentiment-Dataset)

유튜브 한국어 댓글 5,482개와 감정 레이블로 구성된 감정 분류용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `본 데이터셋은 유튜브에서 수집된 한국어 댓글 5,482개와 이에 대응하는 감정 레이블(긍정, 부정, 중립, 불명확)로 구성된 감정 분류용 데이터셋입니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `본 데이터셋은 유튜브에서 수집된 한국어 댓글 5,482개와 이에 대응하는 감정 레이블(긍정, 부정, 중립, 불명확)로 구성된 감정 분류용 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `In our repository, the dataset is divided into the following splits: - `train`: 3,421개 - `validation`: 868개 - `test`: 1,193개` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
