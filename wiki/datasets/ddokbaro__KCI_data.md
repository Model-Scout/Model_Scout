---
type: "dataset"
id: "ddokbaro/KCI_data"
source: "huggingface"
url: "https://huggingface.co/datasets/ddokbaro/KCI_data"
downloads: 124
summary: "한국학술지인용색인(KCI) 국내 학술지 논문 메타데이터로 학술 연구 및 LLM 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ddokbaro/KCI_data

> dataset · [Hugging Face](https://huggingface.co/datasets/ddokbaro/KCI_data)

한국학술지인용색인(KCI) 국내 학술지 논문 메타데이터로 학술 연구 및 LLM 학습용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `디지털 인문학(DH), 계량 서지학, 지식 그래프 구축 및 LLM의 한국어 학술 도메인 학습 등을 위해 구축되었습니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:retrieval, task:summarization = `데이터는 JSONL (JSON Lines) 포맷으로 제공되어 대용량 처리에 최적화되어 있습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `각 라인은 하나의 논문(Article) 정보를 담고 있습니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1054` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — tag_match · readme, tags = `academic` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `디지털 인문학(DH), 계량 서지학, 지식 그래프 구축 및 LLM의 한국어 학술 도메인 학습 등을 위해 구축되었습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `abstract_ko` 열 p90 1581자 ≈ 1054 토큰 (viewer statistics, default/train)
