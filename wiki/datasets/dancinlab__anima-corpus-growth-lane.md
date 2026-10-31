---
type: "dataset"
id: "dancinlab/anima-corpus-growth-lane"
source: "huggingface"
url: "https://huggingface.co/datasets/dancinlab/anima-corpus-growth-lane"
downloads: 33
summary: "anima의 4번째 자기개발 레인 성장 코퍼스로, 개념 범위와 추론 능력 향상을 위한 다국어 과학 및 자기지식 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# dancinlab/anima-corpus-growth-lane

> dataset · [Hugging Face](https://huggingface.co/datasets/dancinlab/anima-corpus-growth-lane)

anima의 4번째 자기개발 레인 성장 코퍼스로, 개념 범위와 추론 능력 향상을 위한 다국어 과학 및 자기지식 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `It grows the substrate's conceptual range + self-model + reasoning capacity, not merely its chat surface.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `byte-vocab V=256, 5-lang (en/fr/de/es/ko).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `It grows the substrate's conceptual range + self-model + reasoning capacity, not merely its chat surface.` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `69` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 274자 ≈ 69 토큰 (viewer statistics, default/train)
