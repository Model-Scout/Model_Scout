---
type: "dataset"
id: "snunlp/KoBALT-700"
source: "huggingface"
url: "https://huggingface.co/datasets/snunlp/KoBALT-700"
downloads: 1384
summary: "한국어 대형 언어 모델 평가를 위한 700문항 다중선택형 언어학 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
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
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# snunlp/KoBALT-700

> dataset · [Hugging Face](https://huggingface.co/datasets/snunlp/KoBALT-700)

한국어 대형 언어 모델 평가를 위한 700문항 다중선택형 언어학 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `multiple-choice questions covering 24 fine-grained linguistic phenomena across five core linguistic domains` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `700 expert-written multiple-choice questions covering 24 fine-grained linguistic phenomena` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `multiple-choice questions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `multiple-choice questions covering 24 fine-grained linguistic phenomena` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `369` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoBALT is designed to advance the evaluation of large language models (LLMs) in Korean, a morphologically rich language` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `Question` 열 p90 553자 ≈ 369 토큰 (viewer statistics, kobalt_v1/raw)
