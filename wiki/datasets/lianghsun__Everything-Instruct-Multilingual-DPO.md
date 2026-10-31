---
type: "dataset"
id: "lianghsun/Everything-Instruct-Multilingual-DPO"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/Everything-Instruct-Multilingual-DPO"
downloads: 97
summary: "다국어 지침 데이터셋으로, 간체 중국어를 번체로 변환하고 DPO 단계 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# lianghsun/Everything-Instruct-Multilingual-DPO

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/Everything-Instruct-Multilingual-DPO)

다국어 지침 데이터셋으로, 간체 중국어를 번체로 변환하고 DPO 단계 학습에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `用戶可利用此資料集訓練模型進行多語系偏好學習` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `此資料集將用於 lianghsun/Llama-3.2-Taiwan-3B-Instruct 的 DPO 階段` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `多國語系的指令資料集` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `拒絕（rejected）回覆` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2802` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Language(s) (NLP): multilingual` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `此資料集將用於 lianghsun/Llama-3.2-Taiwan-3B-Instruct 的 DPO 階段` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 11207자 ≈ 2802 토큰 (viewer statistics, default/train)
