---
type: "dataset"
id: "nvidia/Nemotron-SFT-Multilingual-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-SFT-Multilingual-v2"
downloads: 2814
summary: "Nemotron-SFT-Multilingual-v2는 수학, 코딩, 과학 데이터를 다국어로 번역한 텍스트 생성용 감독 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nvidia/Nemotron-SFT-Multilingual-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Multilingual-v2)

Nemotron-SFT-Multilingual-v2는 수학, 코딩, 과학 데이터를 다국어로 번역한 텍스트 생성용 감독 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `multilingual supervised fine-tuning (SFT) dataset for post-training text-generation models` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `We provide the prompt and the final answer in the target language` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `math, coding, and science seed data` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is intended for post-training large language models with multilingual SFT data` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `uuid` 열 p90 36자 ≈ 9 토큰 (viewer statistics, default/code_hi)
