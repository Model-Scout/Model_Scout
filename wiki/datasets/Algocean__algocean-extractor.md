---
type: "dataset"
id: "Algocean/algocean-extractor"
source: "huggingface"
url: "https://huggingface.co/datasets/Algocean/algocean-extractor"
downloads: 26
summary: "질의와 문서에서 답의 근거 구간을 원문 그대로 추출하는 LoRA SFT 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Algocean/algocean-extractor

> dataset · [Hugging Face](https://huggingface.co/datasets/Algocean/algocean-extractor)

질의와 문서에서 답의 근거 구간을 원문 그대로 추출하는 LoRA SFT 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `답의 근거 span을 원문 그대로 뽑거나, 없으면 기권하도록 가르치는 LoRA SFT 데이터셋입니다.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · tags = `rag` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction, task:question_answering, task:retrieval = `형식: JSONL, messages 3턴 (system / user / assistant)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `26` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `eval은 학습셋과 별도 생성` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `seed_axis` 열 p90 39자 ≈ 26 토큰 (viewer statistics, default/test)
