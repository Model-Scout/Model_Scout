---
type: "dataset"
id: "LLM-OS-Models/LFM2.5-KO-Dataset-Index-and-Sources"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-Dataset-Index-and-Sources"
downloads: 10
summary: "한국어 SFT 혼합 학습을 위한 데이터셋 인덱스 및 출처 스냅샷입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# LLM-OS-Models/LFM2.5-KO-Dataset-Index-and-Sources

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-Dataset-Index-and-Sources)

한국어 SFT 혼합 학습을 위한 데이터셋 인덱스 및 출처 스냅샷입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `used as a dataset index while building the SFT mix` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `JSONL rows with a `text` field containing LFM ChatML-like conversation text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `NumPy response-only SFT arrays built with the LFM tokenizer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `used as a dataset index while building the SFT mix` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
