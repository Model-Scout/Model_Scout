---
type: "dataset"
id: "ENERZAiKR/LGUplus_keyword_rerank_top1_rolling"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_keyword_rerank_top1_rolling"
downloads: 9
summary: "LGUplus 시청자 롤링 페르소나 기반 키워드 top1 리랭킹 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/LGUplus_keyword_rerank_top1_rolling

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_keyword_rerank_top1_rolling)

LGUplus 시청자 롤링 페르소나 기반 키워드 top1 리랭킹 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — tag_match · readme, tags = `reranking` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking = `페르소나 본문(persona_text)과 후보 키워드(cand_keywords) 를 함께 제공` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `그 사람의 관심사를 가장 잘 대표하는 키워드 1개` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `시청자가 그 블록에 15분+ 시청한 프로그램들의 키워드 후보 중` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `교사 LLM(Qwen3-235B-A22B-Instruct-2507-FP8)이 선택` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
