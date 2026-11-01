---
type: "dataset"
id: "KRX-Data/Won-Instruct"
source: "huggingface"
url: "https://huggingface.co/datasets/KRX-Data/Won-Instruct"
downloads: 218
summary: "한국 금융 분야 전문 언어 모델 학습용 금융 추론 지침-응답 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KRX-Data/Won-Instruct

> dataset · [Hugging Face](https://huggingface.co/datasets/KRX-Data/Won-Instruct)

한국 금융 분야 전문 언어 모델 학습용 금융 추론 지침-응답 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `human-in-the-loop validation, where an LLM-as-a-Judge mechanism was employed to ensure factual accuracy, coherence, and reliability` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `instruction-following dataset tailored for training Korean language models specialized in financial reasoning and domain-specific financial tasks` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `The ₩ON-Instruct comprises the following columns: - `prompt`: The questions converted into MCQA or Instruction-Response format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `instruction-response instances` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1098` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `a comprehensive instruction-following dataset tailored for training Korean language models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `google/gemma-2-2b-it_response` 열 p90 1646자 ≈ 1098 토큰 (viewer statistics, default/train)
