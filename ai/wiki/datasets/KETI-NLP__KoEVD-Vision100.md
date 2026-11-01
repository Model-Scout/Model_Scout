---
type: "dataset"
id: "KETI-NLP/KoEVD-Vision100"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/KoEVD-Vision100"
downloads: 131
summary: "KoEVD-Vision100은 한국어 시각-언어 모델 평가용 100개 합성 이미지 다지선다 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KETI-NLP/KoEVD-Vision100

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/KoEVD-Vision100)

KoEVD-Vision100은 한국어 시각-언어 모델 평가용 100개 합성 이미지 다지선다 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `KoEVD-Vision100 is a compact Korean multiple-choice evaluation dataset for vision-language models.` · 신뢰도 low
- **작업**: [[질의응답]] — tag_match · tags = `multiple-choice` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `Each of the 100 items contains one synthetic image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:visual_qa = `one Korean question, four choices` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `one designated best answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `89` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoEVD-Vision100 is a compact Korean multiple-choice evaluation dataset for vision-language models.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Configuration / split | default / test` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `evaluation_point` 열 p90 133자 ≈ 89 토큰 (viewer statistics, default/test)
