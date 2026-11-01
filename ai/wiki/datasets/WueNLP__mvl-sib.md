---
type: "dataset"
id: "WueNLP/mvl-sib"
source: "huggingface"
url: "https://huggingface.co/datasets/WueNLP/mvl-sib"
downloads: 2271
summary: "MVL-SIB는 205개 언어와 7개 주제별 이미지-문장 쌍을 제공하는 다국어 시각-언어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# WueNLP/mvl-sib

> dataset · [Hugging Face](https://huggingface.co/datasets/WueNLP/mvl-sib)

MVL-SIB는 205개 언어와 7개 주제별 이미지-문장 쌍을 제공하는 다국어 시각-언어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_ids = `topic-classification` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `MVL-SIB is a multilingual dataset that provides image-sentence pairs spanning 205 languages and 7 topical categories` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:visual_qa = `Large vision-language models must select one of 4 candidate sentences that best matches the topic of the reference images` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `choose one of 4 candidate images corresponding to the topic of the reference sentences` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `Large vision-language models must select one of 4 candidate sentences that best matches the topic of the reference images` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `197 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MVL-SIB is a multilingual dataset that provides image-sentence pairs spanning 205 languages and 7 topical categories (`entertainment`, `geography`, `health`, `p` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
