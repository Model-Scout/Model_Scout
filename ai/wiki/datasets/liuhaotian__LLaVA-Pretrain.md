---
type: "dataset"
id: "liuhaotian/LLaVA-Pretrain"
source: "huggingface"
url: "https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain"
downloads: 6595
summary: "LLaVA-Pretrain은 GPT-4 비전/언어 능력 향상을 위한 시각-언어 사전학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# liuhaotian/LLaVA-Pretrain

> dataset · [Hugging Face](https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain)

LLaVA-Pretrain은 GPT-4 비전/언어 능력 향상을 위한 시각-언어 사전학습 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `It is constructed for the pretraining stage for feature alignment in visual instruction tuning.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `multimodal synthesized conversation from the image-caption pairs, by adding randomly selected instructions like: "Describe this image".` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation = `multimodal synthesized conversation from the image-caption pairs` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `We use the raw CC-3M caption as the default answer.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intellig` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `It is constructed for the pretraining stage for feature alignment in visual instruction tuning.` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[nc-ai-consortium__VAETKI-VL-7B-A1B|nc-ai-consortium/VAETKI-VL-7B-A1B]]
