---
type: "dataset"
id: "koreankiwi99/Nunchi-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/koreankiwi99/Nunchi-Bench"
downloads: 71
summary: "한국 미신에 대한 문화적 추론 능력을 평가하는 언어 모델 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
---
# koreankiwi99/Nunchi-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/koreankiwi99/Nunchi-Bench)

한국 미신에 대한 문화적 추론 능력을 평가하는 언어 모델 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `It includes 247 prompts across three question types` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `cc` · 신뢰도 high
- **도메인**: [[문화·관광]] — tag_match · readme, tags = `culture` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Nunchi-Bench is a benchmark designed to evaluate language models’ cultural reasoning and understanding` · 신뢰도 medium
