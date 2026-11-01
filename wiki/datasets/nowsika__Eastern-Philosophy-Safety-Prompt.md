---
type: "dataset"
id: "nowsika/Eastern-Philosophy-Safety-Prompt"
source: "huggingface"
url: "https://huggingface.co/datasets/nowsika/Eastern-Philosophy-Safety-Prompt"
downloads: 75
summary: "동양철학(음양)을 기반으로 한 자기조절 안전 프롬프트 데이터셋입니다."
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
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nowsika/Eastern-Philosophy-Safety-Prompt

> dataset · [Hugging Face](https://huggingface.co/datasets/nowsika/Eastern-Philosophy-Safety-Prompt)

동양철학(음양)을 기반으로 한 자기조절 안전 프롬프트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `this project aims to create a "Sage-like" persona that self-regulates based on internal dignity and balance.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Copy the **entire content** (including the `[System Meta-Instruction]` block).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `52` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Project NOBLE is an experimental alignment framework inspired by Eastern Philosophy (Yin-Yang).` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `While this repo (`v1.5.x`) provides the *prompt implementation*` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 78자 ≈ 52 토큰 (viewer statistics, default/train)
