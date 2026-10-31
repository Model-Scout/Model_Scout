---
type: "dataset"
id: "Geneen/SCR-Eval"
source: "huggingface"
url: "https://huggingface.co/datasets/Geneen/SCR-Eval"
downloads: 51
summary: "SCR-Eval은 영상 자막 번역 평가를 위한 스크립트 유사 문맥 표현 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Geneen/SCR-Eval

> dataset · [Hugging Face](https://huggingface.co/datasets/Geneen/SCR-Eval)

SCR-Eval은 영상 자막 번역 평가를 위한 스크립트 유사 문맥 표현 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Each `expert/{film}/{evaluator}.csv` contains one row per source line per provider. Columns: `film, provider, evaluator, line_uid, scene_id, source_text, transl` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `source_text, translation` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `category, severity` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Data accompanying SCR-Eval: Evaluating Video Subtitle Translation with a Script-like Context Representation (EMNLP 2026, Industry Track).` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Each film–provider–condition combination has 10 evaluation runs.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
