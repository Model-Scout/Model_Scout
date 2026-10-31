---
type: "dataset"
id: "hyun5ooo/hansoldeco"
source: "huggingface"
url: "https://huggingface.co/datasets/hyun5ooo/hansoldeco"
downloads: 10
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# hyun5ooo/hansoldeco

> dataset · [Hugging Face](https://huggingface.co/datasets/hyun5ooo/hansoldeco)

## 분류

- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:table_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:table_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `237` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 355자 ≈ 237 토큰 (viewer statistics, default/train)
