---
type: "dataset"
id: "EunB2/Kontrast-ForcedChoice_160pairs"
source: "huggingface"
url: "https://huggingface.co/datasets/EunB2/Kontrast-ForcedChoice_160pairs"
downloads: 17
summary: "한국어 구문 최소대립쌍으로 대형 언어모델의 구문 이해 능력을 평가하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# EunB2/Kontrast-ForcedChoice_160pairs

> dataset · [Hugging Face](https://huggingface.co/datasets/EunB2/Kontrast-ForcedChoice_160pairs)

한국어 구문 최소대립쌍으로 대형 언어모델의 구문 이해 능력을 평가하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `sentence pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Correct answer (either `A` or `B`).` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset, Kontrast, contains Korean syntactic minimal pairs used to evaluate the syntactic competence of large language models` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `used to evaluate the syntactic competence of large language models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `sentence_B` 열 p90 25자 ≈ 16 토큰 (viewer statistics, default/test)
