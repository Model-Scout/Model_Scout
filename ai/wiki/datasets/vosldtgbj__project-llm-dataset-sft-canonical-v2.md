---
type: "dataset"
id: "vosldtgbj/project-llm-dataset-sft-canonical-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/vosldtgbj/project-llm-dataset-sft-canonical-v2"
downloads: 58
summary: "SF-SFT-v2는 90% 프로젝트 도메인과 10% 다국어 다능력 일반 SFT 데이터를 결합한 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# vosldtgbj/project-llm-dataset-sft-canonical-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/vosldtgbj/project-llm-dataset-sft-canonical-v2)

SF-SFT-v2는 90% 프로젝트 도메인과 10% 다국어 다능력 일반 SFT 데이터를 결합한 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `OpenAI 风格多轮消息` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `项目域 family + general_diverse` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `多语言、多能力通用 SFT 锚点` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `eval 仅用于复现，未来正式盲测另建私有集` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train/eval 分别达到约 90% 项目域 + 10% 通用` · 신뢰도 medium
