---
type: "dataset"
id: "zhihz0535/X-AlpacaEval"
source: "huggingface"
url: "https://huggingface.co/datasets/zhihz0535/X-AlpacaEval"
downloads: 70
summary: "5개 언어로 된 다국어 지침 평가용 대형 언어 모델 평가 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# zhihz0535/X-AlpacaEval

> dataset · [Hugging Face](https://huggingface.co/datasets/zhihz0535/X-AlpacaEval)

5개 언어로 된 다국어 지침 평가용 대형 언어 모델 평가 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `The instructions in this benchmark are translated from the original English version of AlpacaEval.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Generate responses to X-AlpacaEval instructions with your LLM` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `90` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The data is intended to be used as evaluation data of instruction-tuned LLMs.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 361자 ≈ 90 토큰 (viewer statistics, default/english)
