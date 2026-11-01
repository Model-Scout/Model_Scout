---
type: "dataset"
id: "IndexTeam/InstTrans-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/IndexTeam/InstTrans-Bench"
downloads: 444
summary: "InstTrans-Bench는 번역 시스템이 명시적 제약 조건을 준수하는지 평가하는 번역 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# IndexTeam/InstTrans-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/IndexTeam/InstTrans-Bench)

InstTrans-Bench는 번역 시스템이 명시적 제약 조건을 준수하는지 평가하는 번역 벤치마크입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · tags = `instruction-following` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `Each instance gives the model a source text plus a numbered list of constraints, and asks for a translation that satisfies all of them.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `asks for a translation that satisfies all of them.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2036` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `reference` 열 p90 8144자 ≈ 2036 토큰 (viewer statistics, default/test)
