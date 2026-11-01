---
type: "dataset"
id: "JudyChoi/KUEST"
source: "huggingface"
url: "https://huggingface.co/datasets/JudyChoi/KUEST"
downloads: 10
summary: "게임 도메인 영어→한국어 번역의 맹점 평가를 위한 KUEST 테스트 스위트 데이터셋입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# JudyChoi/KUEST

> dataset · [Hugging Face](https://huggingface.co/datasets/JudyChoi/KUEST)

게임 도메인 영어→한국어 번역의 맹점 평가를 위한 KUEST 테스트 스위트 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Translation direction: English → Korean (`en` → `ko_KR`)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Translation direction: English → Korean (`en` → `ko_KR`)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `95` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `A WMT26 MT test suite focusing on translation blind spots that surface when translating English into Korean in the game domain.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `src_text` 열 p90 142자 ≈ 95 토큰 (viewer statistics, default/train)
