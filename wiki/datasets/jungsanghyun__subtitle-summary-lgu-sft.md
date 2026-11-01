---
type: "dataset"
id: "jungsanghyun/subtitle-summary-lgu-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/jungsanghyun/subtitle-summary-lgu-sft"
downloads: 6
summary: "방송 자막을 한 문장 요약과 키워드로 변환하는 SFT 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
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
# jungsanghyun/subtitle-summary-lgu-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-lgu-sft)

방송 자막을 한 문장 요약과 키워드로 변환하는 SFT 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `[키워드] {검색어} — 라벨 2줄(소형 모델 친화·파싱 용이)` · 신뢰도 medium
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval, task:summarization = `입력(user): [이전 요약] {last_summary}\n[자막] {5min_script}` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `출력(assistant): [요약] {한 문장}\n[키워드] {검색어}` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Broadcast Subtitle Summary & Keyword` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation 13,177` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 118,608` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
