---
type: "dataset"
id: "CohereLabs/deja-vu-pairwise-evals"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/deja-vu-pairwise-evals"
downloads: 140
summary: "다국어 LLM 평가를 위한 자동 쌍대 선호 평가 데이터로 모델 비교 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# CohereLabs/deja-vu-pairwise-evals

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/deja-vu-pairwise-evals)

다국어 LLM 평가를 위한 자동 쌍대 선호 평가 데이터로 모델 비교 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `judge decisions for the m-ArenaHard benchmark` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `evaluations for "Déjà Vu: Multilingual LLM Evaluation through the Lens of Machine Translation Evaluation"` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `pairwise automatic win-rate evaluations` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:generation, task:reranking = `Outputs and judge decisions for the m-ArenaHard benchmark for sampled generations` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `pairwise automatic win-rate evaluations` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Déjà Vu: Multilingual LLM Evaluation through the Lens of Machine Translation Evaluation` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `This data may not be used for model training!` · 신뢰도 medium
