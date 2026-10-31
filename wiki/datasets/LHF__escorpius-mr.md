---
type: "dataset"
id: "LHF/escorpius-mr"
source: "huggingface"
url: "https://huggingface.co/datasets/LHF/escorpius-mr"
downloads: 8979
summary: "esCorpius-mr은 다국어 웹 크롤링 원시 말뭉치로, 중복 제거 도구 벤치마킹에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
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
  - "[[초대규모 데이터]]"
---
# LHF/escorpius-mr

> dataset · [Hugging Face](https://huggingface.co/datasets/LHF/escorpius-mr)

esCorpius-mr은 다국어 웹 크롤링 원시 말뭉치로, 중복 제거 도구 벤치마킹에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `web textual content` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `32 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `22149` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual datasets obtained from automatic web crawling` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `This corpus can be used for benchmarking deduplication tools.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 88596자 ≈ 22149 토큰 (viewer statistics, default/train)
