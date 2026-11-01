---
type: "dataset"
id: "huggingface-KREW/spider-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/huggingface-KREW/spider-ko"
downloads: 71
summary: "Spider-KO는 Yale Spider 데이터셋을 한국어로 번역한 Text-to-SQL 변환 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# huggingface-KREW/spider-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/huggingface-KREW/spider-ko)

Spider-KO는 Yale Spider 데이터셋을 한국어로 번역한 Text-to-SQL 변환 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · readme, tags = `text2text-generation` · 신뢰도 medium
- **작업**: [[표 질의응답]] — metadata · tags, task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:table_qa = `데이터셋의 질문은 한국어(ko)로 번역되었으며` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:table_qa = `SQL 쿼리는 영어 기반으로 유지되었습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `168` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `이 데이터셋은 다양한 도메인의 데이터베이스에 대한 질의와 해당 SQL 쿼리를 포함하고 있으며` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `데이터셋은 원본 Spider 데이터셋의 분할 방식을 따라 다음과 같이 제공됩니다.
- `train`: 7,000개
- `validation` (dev): 1,034개` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `query_toks` 열 p90 253자 ≈ 168 토큰 (viewer statistics, default/validation)
