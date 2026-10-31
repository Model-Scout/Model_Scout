---
type: "dataset"
id: "TGoddessana/common-dev-commands-en-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/TGoddessana/common-dev-commands-en-ko"
downloads: 24
summary: "자연어 명령어를 리눅스/유닉스 명령어로 번역하는 한영 이중언어 데이터셋입니다."
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
  - "[[영어]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# TGoddessana/common-dev-commands-en-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/TGoddessana/common-dev-commands-en-ko)

자연어 명령어를 리눅스/유닉스 명령어로 번역하는 한영 이중언어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `natural language queries (in both Korean and English)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `their corresponding Linux/Unix commands` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `54` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A bilingual dataset for translating natural language instructions into Linux/Unix commands.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training models to convert natural language to shell commands` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `english_question` 열 p90 80자 ≈ 54 토큰 (viewer statistics, default/train)
