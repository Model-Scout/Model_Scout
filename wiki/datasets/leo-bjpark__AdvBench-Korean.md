---
type: "dataset"
id: "leo-bjpark/AdvBench-Korean"
source: "huggingface"
url: "https://huggingface.co/datasets/leo-bjpark/AdvBench-Korean"
downloads: 31
summary: "AdvBench 데이터셋의 한국어 번역본으로, 정렬된 언어 모델의 우회 및 적대적 공격 평가용 데이터셋입니다."
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
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# leo-bjpark/AdvBench-Korean

> dataset · [Hugging Face](https://huggingface.co/datasets/leo-bjpark/AdvBench-Korean)

AdvBench 데이터셋의 한국어 번역본으로, 정렬된 언어 모델의 우회 및 적대적 공격 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `for evaluating jailbreak and adversarial attacks on aligned language models` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `prompt | harmful instruction (Korean translation)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `target response used in AdvBench` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `38` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AdvBench-Korean is a Korean translation of the AdvBench dataset` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `target` 열 p90 57자 ≈ 38 토큰 (viewer statistics, default/train)
