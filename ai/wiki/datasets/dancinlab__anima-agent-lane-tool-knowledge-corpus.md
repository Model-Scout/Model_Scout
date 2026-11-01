---
type: "dataset"
id: "dancinlab/anima-agent-lane-tool-knowledge-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/dancinlab/anima-agent-lane-tool-knowledge-corpus"
downloads: 30
summary: "anima 에이전트 레인 3층 도구 도메인 지식 코퍼스로, 5개 도메인 개념적 지식을 제공하여 추론 지원"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dancinlab/anima-agent-lane-tool-knowledge-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/dancinlab/anima-agent-lane-tool-knowledge-corpus)

anima 에이전트 레인 3층 도구 도메인 지식 코퍼스로, 5개 도메인 개념적 지식을 제공하여 추론 지원

## 분류

- **작업**: [[임베딩]] — ner · readme = `so the byte-LM can REASON in those domains` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Machine-AUTHORED multilingual CONCEPTUAL coverage` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:language_modeling = `Knowledge is carried as PLAIN PROSE like the wiki backbone` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Knowledge is carried as PLAIN PROSE like the wiki backbone` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `wiki-style conceptual coverage` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
