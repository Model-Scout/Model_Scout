---
type: "dataset"
id: "didi0di/finance-legal-mrc-chat-template"
source: "huggingface"
url: "https://huggingface.co/datasets/didi0di/finance-legal-mrc-chat-template"
downloads: 12
summary: "문서 내 표 이미지와 문맥을 활용해 LLM이 설명, 제목, 요약, 핵심 엔티티를 생성하도록 학습하는 한국어 챗 템플릿 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[요약]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# didi0di/finance-legal-mrc-chat-template

> dataset · [Hugging Face](https://huggingface.co/datasets/didi0di/finance-legal-mrc-chat-template)

문서 내 표 이미지와 문맥을 활용해 LLM이 설명, 제목, 요약, 핵심 엔티티를 생성하도록 학습하는 한국어 챗 템플릿 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Multimodal Input Handling (text + image)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `표 이미지(image_url)` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:summarization, task:table_qa = `문맥(context)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization, task:table_qa = `description: 자연어로 푼 설명` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `데이터 수: 1,197개 (train/test 8:2 split)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
