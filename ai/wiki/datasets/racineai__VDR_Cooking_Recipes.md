---
type: "dataset"
id: "racineai/VDR_Cooking_Recipes"
source: "huggingface"
url: "https://huggingface.co/datasets/racineai/VDR_Cooking_Recipes"
downloads: 758
summary: "요리 레시피 문서와 요리 가이드의 텍스트와 이미지를 포함한 멀티모달 데이터셋으로, 질의응답과 문서 검색 등에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
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
# racineai/VDR_Cooking_Recipes

> dataset · [Hugging Face](https://huggingface.co/datasets/racineai/VDR_Cooking_Recipes)

요리 레시피 문서와 요리 가이드의 텍스트와 이미지를 포함한 멀티모달 데이터셋으로, 질의응답과 문서 검색 등에 활용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `support tasks such as RAG DSE, question answering, document search, and vision-language model training.` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · tags, task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `It combines text and image data extracted from real culinary PDFs` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `It combines text and image data extracted from real culinary PDFs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `a synthetic culinary question generated from that page` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `152` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `cooking recipe documents, culinary guides, and food preparation instructions` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training and evaluating vision-language models on culinary and recipe content` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 609자 ≈ 152 토큰 (viewer statistics, filtered/train)
