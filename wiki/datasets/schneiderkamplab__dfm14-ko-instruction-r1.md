---
type: "dataset"
id: "schneiderkamplab/dfm14-ko-instruction-r1"
source: "huggingface"
url: "https://huggingface.co/datasets/schneiderkamplab/dfm14-ko-instruction-r1"
downloads: 129
summary: "자동 검토된 한국어 DFM14 지침 데이터로, 챗봇 학습용으로 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# schneiderkamplab/dfm14-ko-instruction-r1

> dataset · [Hugging Face](https://huggingface.co/datasets/schneiderkamplab/dfm14-ko-instruction-r1)

자동 검토된 한국어 DFM14 지침 데이터로, 챗봇 학습용으로 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Training supervises the indicated final assistant.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Complete chat history is preserved.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `All final assistant targets fit the native Gemma 4 template within 4,096 tokens, without truncation.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1521` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Accepted-only DFM14 data, automatically reviewed with Gemma 4 26B-A4B.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training supervises the indicated final assistant.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `messages_json` 열 p90 2282자 ≈ 1521 토큰 (viewer statistics, default/train)
