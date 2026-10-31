---
type: "dataset"
id: "Jaime-Choi/KoDetox"
source: "huggingface"
url: "https://huggingface.co/datasets/Jaime-Choi/KoDetox"
downloads: 55
summary: "한국어 혐오 발언과 그 해독문 쌍으로 구성된 KoDetox 데이터셋으로, 독성 언어 완화 및 튜닝에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Jaime-Choi/KoDetox

> dataset · [Hugging Face](https://huggingface.co/datasets/Jaime-Choi/KoDetox)

한국어 혐오 발언과 그 해독문 쌍으로 구성된 KoDetox 데이터셋으로, 독성 언어 완화 및 튜닝에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `original: a Korean hate speech or toxic comment` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `111` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoDetox is a Korean dataset consisting of 8,856 pairs of toxic comments and their detoxified counterparts.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is curated for tasks such as toxic language mitigation, instruction tuning, and alignment tuning (e.g., DPO, PPO) in Korean.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `purified` 열 p90 167자 ≈ 111 토큰 (viewer statistics, default/train)
