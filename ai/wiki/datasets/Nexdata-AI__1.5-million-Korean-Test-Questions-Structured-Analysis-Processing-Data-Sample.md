---
type: "dataset"
id: "Nexdata-AI/1.5-million-Korean-Test-Questions-Structured-Analysis-Processing-Data-Sample"
source: "huggingface"
url: "https://huggingface.co/datasets/Nexdata-AI/1.5-million-Korean-Test-Questions-Structured-Analysis-Processing-Data-Sample"
downloads: 11
summary: "초중고 교과목별 150만개 한국어 시험문제, 정답, 해설 포함 데이터셋"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Nexdata-AI/1.5-million-Korean-Test-Questions-Structured-Analysis-Processing-Data-Sample

> dataset · [Hugging Face](https://huggingface.co/datasets/Nexdata-AI/1.5-million-Korean-Test-Questions-Structured-Analysis-Processing-Data-Sample)

초중고 교과목별 150만개 한국어 시험문제, 정답, 해설 포함 데이터셋

## 분류

- **작업**: [[질의응답]] — ner · readme = `Korean Test Questions Structured Analysis Processing Data, around 1.5 million questions, contains question types, questions, answers, explanations, etc.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Contains question types, questions, answers, explanations, etc.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Contains question types, questions, answers, explanations, etc.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `540` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `For subjects, include [Primary School] Korean, Mathematics, English, Social Studies, Science; [Middle School] Korean, English, Mathematics, Science, Social Stud` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset can be used for large-scale subject knowledge enhancement tasks.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `parse` 열 p90 810자 ≈ 540 토큰 (viewer statistics, default/train)
