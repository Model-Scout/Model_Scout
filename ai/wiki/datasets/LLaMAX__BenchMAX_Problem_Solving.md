---
type: "dataset"
id: "LLaMAX/BenchMAX_Problem_Solving"
source: "huggingface"
url: "https://huggingface.co/datasets/LLaMAX/BenchMAX_Problem_Solving"
downloads: 372
summary: "BenchMAX_Problem_Solving은 다국어 경쟁 프로그래밍 문제 해결을 위한 코드 생성 능력을 평가하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[코드 (출력 형식)|코드]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
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
  - "[[중규모 데이터]]"
---
# LLaMAX/BenchMAX_Problem_Solving

> dataset · [Hugging Face](https://huggingface.co/datasets/LLaMAX/BenchMAX_Problem_Solving)

BenchMAX_Problem_Solving은 다국어 경쟁 프로그래밍 문제 해결을 위한 코드 생성 능력을 평가하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `which evaluates the code generation capability for solving multilingual competitive code problems` · 신뢰도 high
- **출력 형식**: [[코드 (출력 형식)|코드]] — ner · readme = `which evaluates the code generation capability for solving multilingual competitive code problems` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `345` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `which evaluates the code generation capability for solving multilingual competitive code problems` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `BenchMAX_Problem_Solving is a dataset of BenchMAX` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question_content` 열 p90 1382자 ≈ 345 토큰 (viewer statistics, ko/train)
