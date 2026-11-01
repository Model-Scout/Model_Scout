---
type: "dataset"
id: "vincentkoc/tiny_qa_benchmark_pp"
source: "huggingface"
url: "https://huggingface.co/datasets/vincentkoc/tiny_qa_benchmark_pp"
downloads: 903
summary: "Tiny QA Benchmark++는 LLM 시스템의 오류를 빠르게 평가하는 초경량 QA 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# vincentkoc/tiny_qa_benchmark_pp

> dataset · [Hugging Face](https://huggingface.co/datasets/vincentkoc/tiny_qa_benchmark_pp)

Tiny QA Benchmark++는 LLM 시스템의 오류를 빠르게 평가하는 초경량 QA 평가 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, tags, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = ``text` (string): The question prompt.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = ``label` (string): The gold answer.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Covers general knowledge (geography, history, science, math, literature, etc.).` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `sha256` 열 p90 64자 ≈ 16 토큰 (viewer statistics, default/train)
