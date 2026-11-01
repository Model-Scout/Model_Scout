---
type: "dataset"
id: "ENERZAiKR/LGUplus_keyword_reranking"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_keyword_reranking"
downloads: 32
summary: "LG U+ 페르소나 기반 키워드 top1 선택 리랭킹 학습용 데이터셋입니다."
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
input_length:
  - "[[단문]]"
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
# ENERZAiKR/LGUplus_keyword_reranking

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_keyword_reranking)

LG U+ 페르소나 기반 키워드 top1 선택 리랭킹 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — tag_match · tags = `reranking` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking = `입력: 주간 페르소나(전주, key_keywords 제외: viewing_tendency/preferred_genres/preferred_programs/frequent_channels) + 직전일 일일페르소나 서술 + 후보 키워드(1~8).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `112` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `페르소나 기반 키워드 top1 선택 데이터셋.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = ``data/test.jsonl` (165,626) : wk2(6/14~20)←wk1` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``data/train.jsonl` (323,239) : wk0(5/31~6/6)←wk1, wk1(6/7~13)←wk2` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `viewing_tendency` 열 p90 168자 ≈ 112 토큰 (viewer statistics, default/test)
