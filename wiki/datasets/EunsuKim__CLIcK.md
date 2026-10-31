---
type: "dataset"
id: "EunsuKim/CLIcK"
source: "huggingface"
url: "https://huggingface.co/datasets/EunsuKim/CLIcK"
downloads: 7675
summary: "한국어 언어 모델의 문화 및 언어 지능 평가를 위한 벤치마크 데이터셋입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[문화·관광]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# EunsuKim/CLIcK

> dataset · [Hugging Face](https://huggingface.co/datasets/EunsuKim/CLIcK)

한국어 언어 모델의 문화 및 언어 지능 평가를 위한 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `evaluate cultural and linguistic intelligence in the context of Korean language models` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `147` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[문화·관광]] — tag_match · tags = `Culture` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 221자 ≈ 147 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `taeminlee/CLIcK`
