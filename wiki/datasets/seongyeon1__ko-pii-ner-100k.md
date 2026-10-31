---
type: "dataset"
id: "seongyeon1/ko-pii-ner-100k"
source: "huggingface"
url: "https://huggingface.co/datasets/seongyeon1/ko-pii-ner-100k"
downloads: 97
summary: "한국어 개인정보 식별자(PII) 개체명 인식(NER) 학습용 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# seongyeon1/ko-pii-ner-100k

> dataset · [Hugging Face](https://huggingface.co/datasets/seongyeon1/ko-pii-ner-100k)

한국어 개인정보 식별자(PII) 개체명 인식(NER) 학습용 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `라벨 20종 3티어 / BIO 41 클래스` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories, task_ids = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `포맷: JSONL. {id, text, spans:[{start,end,label,value}], meta}` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `포맷: JSONL. {id, text, spans:[{start,end,label,value}], meta}` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `230` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 PII NER 학습 데이터셋` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `외부 평가용 홀드아웃 2,006건` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `학습용 98,845건` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 346자 ≈ 230 토큰 (viewer statistics, default/validation)
