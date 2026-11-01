---
type: "dataset"
id: "NCSOFT/K-DTCBench"
source: "huggingface"
url: "https://huggingface.co/datasets/NCSOFT/K-DTCBench"
downloads: 241
summary: "K-DTCBench는 컴퓨터 생성 및 손글씨 문서, 표, 차트 이미지에 대한 한국어 시각-언어 모델 평가용 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
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
# NCSOFT/K-DTCBench

> dataset · [Hugging Face](https://huggingface.co/datasets/NCSOFT/K-DTCBench)

K-DTCBench는 컴퓨터 생성 및 손글씨 문서, 표, 차트 이미지에 대한 한국어 시각-언어 모델 평가용 벤치마크입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `It consists of 80 questions for each image type and two questions per image, summing up to 240 questions in total.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `K-DTCBench, a newly developed Korean benchmark featuring both computer-generated and handwritten documents, tables, and charts.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `It consists of 80 questions for each image type and two questions per image, summing up to 240 questions in total.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `28` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This benchmark is designed to evaluate whether vision-language models can process images in different formats and be applicable for diverse domains.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `This benchmark is designed to evaluate whether vision-language models can process images in different formats and be applicable for diverse domains.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 41자 ≈ 28 토큰 (viewer statistics, default/test)
