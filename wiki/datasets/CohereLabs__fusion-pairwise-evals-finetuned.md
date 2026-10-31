---
type: "dataset"
id: "CohereLabs/fusion-pairwise-evals-finetuned"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/fusion-pairwise-evals-finetuned"
downloads: 147
summary: "m-ArenaHard-v2.0 벤치마크에서 모델 간 쌍별 선호도 평가 데이터로, 모델 비교 분석에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# CohereLabs/fusion-pairwise-evals-finetuned

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/fusion-pairwise-evals-finetuned)

m-ArenaHard-v2.0 벤치마크에서 모델 간 쌍별 선호도 평가 데이터로, 모델 비교 분석에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `judged by GPT-4o` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `pairwise automatic win-rate evaluations` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:reranking = `The data is organized in Jsonlines format where each line contains all the information for a single prompt evaluation.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Each model’s outputs are compared in pairs with the respective Gemini output, and judged by GPT-4o.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `42753` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `benchmark and it compares 2 models against gemini-2.5-flash` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `You may use this data to conduct analyses of model differences, evaluate other judges against GPT4o, or similar inference-only experiments.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `gemini_2_5_flash_completion` 열 p90 171011자 ≈ 42753 토큰 (viewer statistics, default/test)
