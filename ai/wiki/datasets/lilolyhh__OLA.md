---
type: "dataset"
id: "lilolyhh/OLA"
source: "huggingface"
url: "https://huggingface.co/datasets/lilolyhh/OLA"
downloads: 8
summary: "OLA는 코드스위칭 상호작용에서 LLM의 출력 언어 정렬을 평가하는 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lilolyhh/OLA

> dataset · [Hugging Face](https://huggingface.co/datasets/lilolyhh/OLA)

OLA는 코드스위칭 상호작용에서 LLM의 출력 언어 정렬을 평가하는 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `OLA is a benchmark designed to evaluate LLMs' Output Language Alignment in code-switched interactions` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Each file contains three columns: - `query`: The code-switched prompt` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `expected response language` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `439` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `OLA is a benchmark designed to evaluate LLMs' Output Language Alignment in code-switched interactions` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `OLA is a benchmark designed to evaluate LLMs' Output Language Alignment in code-switched interactions` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `ContentFirst` 열 p90 658자 ≈ 439 토큰 (viewer statistics, complex_ko_instr/train)
