---
type: "dataset"
id: "lenML/advbench_behaviors_m5"
source: "huggingface"
url: "https://huggingface.co/datasets/lenML/advbench_behaviors_m5"
downloads: 43
summary: "AdvBench 데이터셋의 다국어 번역본으로, 500개의 유해 행동 지침을 포함해 모델 공격에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lenML/advbench_behaviors_m5

> dataset · [Hugging Face](https://huggingface.co/datasets/lenML/advbench_behaviors_m5)

AdvBench 데이터셋의 다국어 번역본으로, 500개의 유해 행동 지침을 포함해 모델 공격에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `AdvBench is a set of 500 harmful behaviors formulated as instructions.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `AdvBench is a set of 500 harmful behaviors formulated as instructions.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `AdvBench is a set of 500 harmful behaviors formulated as instructions.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `jp` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `29` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AdvBench is a set of 500 harmful behaviors formulated as instructions.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `此数据集为 advbench_behaviors.csv 文件的多语言翻译版本。一个常见的任务是用于 abliterator 脚本。` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text_ru` 열 p90 116자 ≈ 29 토큰 (viewer statistics, default/train)
