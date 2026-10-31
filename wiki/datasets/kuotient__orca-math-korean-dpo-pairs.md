---
type: "dataset"
id: "kuotient/orca-math-korean-dpo-pairs"
source: "huggingface"
url: "https://huggingface.co/datasets/kuotient/orca-math-korean-dpo-pairs"
downloads: 50
summary: "Orca-math-korean-dpo-pairs는 수학 문제와 답변 쌍으로 구성된 한국어 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kuotient/orca-math-korean-dpo-pairs

> dataset · [Hugging Face](https://huggingface.co/datasets/kuotient/orca-math-korean-dpo-pairs)

Orca-math-korean-dpo-pairs는 수학 문제와 답변 쌍으로 구성된 한국어 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `question: orca-math dataset의 question` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `question: orca-math dataset의 question` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `chosen: label이 참일 경우 answer 혹은 generated의 random.choice, 거짓일 경우 answer (Orca-math original paper 참고)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `627` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `As an expert Math teacher, your role is to… See the full description on the dataset page: https://huggingface.co/datasets/kuotient/orca-math-korean-dpo-pairs.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `label이 참일 경우 answer 혹은 generated의 random.choice, 거짓일 경우 answer (Orca-math original paper 참고)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `rejected` 열 p90 941자 ≈ 627 토큰 (viewer statistics, default/train)
