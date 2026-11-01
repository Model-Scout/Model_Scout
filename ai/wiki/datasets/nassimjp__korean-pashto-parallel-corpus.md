---
type: "dataset"
id: "nassimjp/korean-pashto-parallel-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/nassimjp/korean-pashto-parallel-corpus"
downloads: 44
summary: "한국어-파슈토어 병렬 말뭉치로 기계 번역 및 다국어 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[ps]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nassimjp/korean-pashto-parallel-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/nassimjp/korean-pashto-parallel-corpus)

한국어-파슈토어 병렬 말뭉치로 기계 번역 및 다국어 연구에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Improving Korean–Pashto cross-lingual capabilities` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `the development of Pashto-capable AI models` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:translation = `Korean sentences paired with their corresponding Pashto translations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Korean sentences paired with their corresponding Pashto translations` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[ps]] — metadata · languages = `ps` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `14` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean–Pashto parallel text dataset containing Korean sentences paired with their corresponding Pashto translations` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Supervised fine-tuning (SFT) of multilingual language models` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `ps` 열 p90 55자 ≈ 14 토큰 (viewer statistics, default/train)
