---
type: "dataset"
id: "allenai/nllb"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/nllb"
downloads: 842
summary: "Meta AI가 공개한 병렬문장 데이터로 다국어 기계번역 학습에 활용되는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# allenai/nllb

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/nllb)

Meta AI가 공개한 병렬문장 데이터로 다국어 기계번역 학습에 활용되는 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `It contains bitext for 148 English-centric and 1465 non-English-centric language pairs` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:translation = `The dataset contains gzipped tab delimited text files for each direction. Each text file contains lines with parallel sentences.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Every instance for a language pair contains the following fields: 'translation' (containing sentence pairs)` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset was created based on metadata for mined bitext released by Meta AI.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[dhtocks__nllb-200-distilled-350M_en-ko|dhtocks/nllb-200-distilled-350M_en-ko]]
- [[haoranxu__X-ALMA-13B-Pretrain|haoranxu/X-ALMA-13B-Pretrain]]
