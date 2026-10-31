---
type: "dataset"
id: "allganize/IFEval-Ko"
source: "huggingface"
url: "https://huggingface.co/datasets/allganize/IFEval-Ko"
downloads: 3065
summary: "한국어 대형 언어 모델의 지시 수행 능력을 평가하는 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
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
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# allganize/IFEval-Ko

> dataset · [Hugging Face](https://huggingface.co/datasets/allganize/IFEval-Ko)

한국어 대형 언어 모델의 지시 수행 능력을 평가하는 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `evaluation of large language models (LLMs) for their instruction-following capabilities` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `112` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `IFEval-Ko is a Korean adaptation of Google's open-source IFEval benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `It enables evaluation of large language models (LLMs) for their instruction-following capabilities in the Korean language.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 169자 ≈ 112 토큰 (viewer statistics, default/train)
