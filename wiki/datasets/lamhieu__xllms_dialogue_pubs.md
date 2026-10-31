---
type: "dataset"
id: "lamhieu/xllms_dialogue_pubs"
source: "huggingface"
url: "https://huggingface.co/datasets/lamhieu/xllms_dialogue_pubs"
downloads: 152
summary: "xLLMs – Dialogue Pubs는 9개 언어로 된 대규모 다국어 대화 데이터셋으로, 대화형 LLM의 장문 추론, 사실 근거, 다국어 능력, 도구 사용 학습에 활용됩니다."
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
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
  - "[[일반]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lamhieu/xllms_dialogue_pubs

> dataset · [Hugging Face](https://huggingface.co/datasets/lamhieu/xllms_dialogue_pubs)

xLLMs – Dialogue Pubs는 9개 언어로 된 대규모 다국어 대화 데이터셋으로, 대화형 LLM의 장문 추론, 사실 근거, 다국어 능력, 도구 사용 학습에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `training and evaluating conversational LLMs on long-context reasoning, factual grounding, multilingual agility, and tool use` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `synthetic conversations in 9 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Q&A and explanations` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `8` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `scientific/technical materials` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `multilingual dialogue dataset` · 신뢰도 low
- **도메인**: [[뉴스·미디어]] — ner · readme = `Tool-Augmented News Retrieval (German)` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `test | 9,887 | 35,098,603` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 988,866 | 3,488,347,874` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `hash` 열 p90 32자 ≈ 8 토큰 (viewer statistics, default/test)
