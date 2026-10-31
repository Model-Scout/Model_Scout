---
type: "dataset"
id: "nowsika/Project_TAYLOR_for_NOBLE"
source: "huggingface"
url: "https://huggingface.co/datasets/nowsika/Project_TAYLOR_for_NOBLE"
downloads: 90
summary: "Project NOBLE의 윤리 판단 위에 톤과 페르소나를 입히는 TAYLOR 레이어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nowsika/Project_TAYLOR_for_NOBLE

> dataset · [Hugging Face](https://huggingface.co/datasets/nowsika/Project_TAYLOR_for_NOBLE)

Project NOBLE의 윤리 판단 위에 톤과 페르소나를 입히는 TAYLOR 레이어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · tags = `llm` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality = `document` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Project TAYLOR is a tone & persona layer designed to sit on top of Project NOBLE,the Eastern-philosophy-based alignment framework released separately.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `You can also: - Subset outfits for a stricter environment (e.g., disable TRICKSTER/JESTER entirely). - Localize the wardrobe text into other languages, while ke` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
