---
type: "dataset"
id: "alwaysgood/flores-kr-reversed"
source: "huggingface"
url: "https://huggingface.co/datasets/alwaysgood/flores-kr-reversed"
downloads: 65
summary: "영어-한국어 및 기타 언어 쌍의 방향을 뒤집은 병렬 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# alwaysgood/flores-kr-reversed

> dataset · [Hugging Face](https://huggingface.co/datasets/alwaysgood/flores-kr-reversed)

영어-한국어 및 기타 언어 쌍의 방향을 뒤집은 병렬 번역 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Transformation: direction flip per row (source/target swap)` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `source_text, target_text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `source_text, target_text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `76` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `FLORES Parallel Mix (Direction-Flipped)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Source dataset dir: /Users/inertia/Desktop/preprocessing/processed/flores_parallel_80_20` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 303자 ≈ 76 토큰 (viewer statistics, default/validation)
