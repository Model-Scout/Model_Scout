---
type: "dataset"
id: "tabtoyou/KRETA"
source: "huggingface"
url: "https://huggingface.co/datasets/tabtoyou/KRETA"
downloads: 220
summary: "KRETA는 다양한 시각적 맥락에서 한국어 텍스트 이해 및 추론을 위한 텍스트 풍부 VQA 벤치마크입니다."
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# tabtoyou/KRETA

> dataset · [Hugging Face](https://huggingface.co/datasets/tabtoyou/KRETA)

KRETA는 다양한 시각적 맥락에서 한국어 텍스트 이해 및 추론을 위한 텍스트 풍부 VQA 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `facilitates an in-depth evaluation of both visual text understanding and reasoning capabilities` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `text-rich Visual Question Answering (VQA) datasets and evaluation benchmarks` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `text within visual contexts` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:visual_qa = `text-rich Visual Question Answering (VQA) datasets` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `Visual Question Answering (VQA)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `207` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `This work was supported by the Korea Institute for Advancement of Technology (KIAT) grant funded by the Ministry of Education, Korea Government` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `real-world scenarios` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `KRETA facilitates an in-depth evaluation of both visual text understanding and reasoning capabilities` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `explanation` 열 p90 310자 ≈ 207 토큰 (viewer statistics, default/test)
