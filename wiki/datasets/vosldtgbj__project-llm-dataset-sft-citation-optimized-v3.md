---
type: "dataset"
id: "vosldtgbj/project-llm-dataset-sft-citation-optimized-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/vosldtgbj/project-llm-dataset-sft-citation-optimized-v3"
downloads: 81
summary: "SF-SFT-v3는 인용 정제된 90/10 비율의 공식 SFT 데이터셋으로, LLM 미세조정에 사용됨."
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# vosldtgbj/project-llm-dataset-sft-citation-optimized-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/vosldtgbj/project-llm-dataset-sft-citation-optimized-v3)

SF-SFT-v3는 인용 정제된 90/10 비율의 공식 SFT 데이터셋으로, LLM 미세조정에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = ``messages` | OpenAI 风格多轮消息；可含 user/assistant/tool | 按 chat template 输入；只对 mask 指定的 assistant 内容计 loss` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = ``messages` | OpenAI 风格多轮消息；可含 user/assistant/tool | 按 chat template 输入；只对 mask 指定的 assistant 内容计 loss` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `英文及多语言 strata 进一步覆盖 agent search/tool、code、crosslingual、instruction v2 non-thinking、instruction v3、math、science、safety、structured output、各语言 general/code/math/S` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = ``official_90_10` 并未复制八个项目域文件：它在 Dataset Card 中显式引用 `canonical_full_pool` 的八个项目域路径，只在 `data/official_90_10/{train,eval}_view` 保存确定性截取的通用记录。加载 config 时 Hugging Fa` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = ``official_90_10` 并未复制八个项目域文件：它在 Dataset Card 中显式引用 `canonical_full_pool` 的八个项目域路径，只在 `data/official_90_10/{train,eval}_view` 保存确定性截取的通用记录。加载 config 时 Hugging Fa` · 신뢰도 medium
