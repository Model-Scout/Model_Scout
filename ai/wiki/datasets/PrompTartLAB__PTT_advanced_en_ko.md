---
type: "dataset"
id: "PrompTartLAB/PTT_advanced_en_ko"
source: "huggingface"
url: "https://huggingface.co/datasets/PrompTartLAB/PTT_advanced_en_ko"
downloads: 20
summary: "기술 용어 번역을 위한 영어-한국어 문장 쌍 데이터셋으로 AI 분야에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# PrompTartLAB/PTT_advanced_en_ko

> dataset · [Hugging Face](https://huggingface.co/datasets/PrompTartLAB/PTT_advanced_en_ko)

기술 용어 번역을 위한 영어-한국어 문장 쌍 데이터셋으로 AI 분야에 활용됨.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `English-Korean bilingual sentence pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Korean translation of the source sentence, with English technical terms presented in parentheses` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `547` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `The Parenthetical Terminology Translation (PTT) dataset is designed for training language models` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 820자 ≈ 547 토큰 (viewer statistics, default/train)
