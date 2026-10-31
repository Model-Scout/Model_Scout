---
type: "dataset"
id: "hyunwookjin/korean-prediction-market-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/hyunwookjin/korean-prediction-market-sample"
downloads: 92
summary: "민심인덱스는 한국 정치·경제 예측을 위한 상위 예측자들의 판단 신호 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# hyunwookjin/korean-prediction-market-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/hyunwookjin/korean-prediction-market-sample)

민심인덱스는 한국 정치·경제 예측을 위한 상위 예측자들의 판단 신호 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[시계열 예측]] — tag_match · readme, tags = `forecasting` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `Question and answer choices` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Platform resolution labels` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `196` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Minsim Market forecasters into a selective signal for Korean politics and the economy.` · 신뢰도 medium
- **도메인**: [[행정·민원]] — ner · readme = `Strong signals on Korean events.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `settlement_rule` 열 p90 294자 ≈ 196 토큰 (viewer statistics, cards/train)
