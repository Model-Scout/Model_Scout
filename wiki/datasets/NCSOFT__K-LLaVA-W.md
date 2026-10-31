---
type: "dataset"
id: "NCSOFT/K-LLaVA-W"
source: "huggingface"
url: "https://huggingface.co/datasets/NCSOFT/K-LLaVA-W"
downloads: 108
summary: "K-LLaVA-W는 한국어로 번역된 시각-언어 모델 평가용 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# NCSOFT/K-LLaVA-W

> dataset · [Hugging Face](https://huggingface.co/datasets/NCSOFT/K-LLaVA-W)

K-LLaVA-W는 한국어로 번역된 시각-언어 모델 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `designed for evaluating vision-language models` · 신뢰도 low
- **작업**: [[이미지 이해]] — ner · readme = `K-LLaVA-W contains 24 images of various domains and 60 daily-life questions` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `K-LLaVA-W contains 24 images` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:visual_qa = `By translating the LLaVA-Bench-in-the-wild into Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `60 daily-life questions, allowing a thorough evaluation of model performance in Korean` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `447` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `various domains` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `we developed a novel robust evaluation benchmark specifically for Korean language` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `gpt_answer` 열 p90 671자 ≈ 447 토큰 (viewer statistics, default/test)
