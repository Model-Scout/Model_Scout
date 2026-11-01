---
type: "dataset"
id: "mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC"
source: "huggingface"
url: "https://huggingface.co/datasets/mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC"
downloads: 181
summary: "OmniGraph Temporal Character Corpus는 만화 페이지의 패널, 캐릭터, 대화 등을 시계열 그래프로 주석한 학술 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC

> dataset · [Hugging Face](https://huggingface.co/datasets/mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC)

OmniGraph Temporal Character Corpus는 만화 페이지의 패널, 캐릭터, 대화 등을 시계열 그래프로 주석한 학술 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Narrative Graph Reasoning & Temporal Classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `Character Re-Identification (ReID) Under Visual Variation` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Multimodal Visual Storytelling & VQA` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Dialogue Attribution & Speaker Identification` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · readme, task_categories = `image-classification` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:vision, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:generation, task:information_extraction, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `Predict normalized panel bounding boxes [x_min, y_min, x_max, y_max] and sequence reading rank.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `The OmniGraph Temporal Character Corpus (OTCC) is curated, maintained, and distributed exclusively for non-commercial academic research, scientific inquiry, and` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = ``split` | `string` | Dataset split identifier (`train`).` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
