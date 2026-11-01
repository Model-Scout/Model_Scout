---
type: "dataset"
id: "humane-lab/PetQA"
source: "huggingface"
url: "https://huggingface.co/datasets/humane-lab/PetQA"
downloads: 190
summary: "PetQA는 반려동물 수의학 지식과 임상 추론을 평가하는 장문 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[id]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# humane-lab/PetQA

> dataset · [Hugging Face](https://huggingface.co/datasets/humane-lab/PetQA)

PetQA는 반려동물 수의학 지식과 임상 추론을 평가하는 장문 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `PetQA provides text-only and multimodal question–answer pairs about dogs and cats` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `PetQA provides text-only and multimodal question–answer pairs about dogs and cats` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `PetQA provides text-only and multimodal question–answer pairs about dogs and cats, with reference answers written by veterinarians` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `PetQA is the first long-form question-answering dataset for veterinary medicine.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The training and validation sets are used for supervised fine-tuning.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
