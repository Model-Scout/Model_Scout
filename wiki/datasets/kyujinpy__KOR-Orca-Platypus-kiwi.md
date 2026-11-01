---
type: "dataset"
id: "kyujinpy/KOR-Orca-Platypus-kiwi"
source: "huggingface"
url: "https://huggingface.co/datasets/kyujinpy/KOR-Orca-Platypus-kiwi"
downloads: 33
summary: "ko-kiwi 데이터셋으로 HumanF-MarkrAI/WIKI_QA_Near_dedup와 kyujinpy/KOR-OpenOrca-Platypus를 병합한 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kyujinpy/KOR-Orca-Platypus-kiwi

> dataset · [Hugging Face](https://huggingface.co/datasets/kyujinpy/KOR-Orca-Platypus-kiwi)

ko-kiwi 데이터셋으로 HumanF-MarkrAI/WIKI_QA_Near_dedup와 kyujinpy/KOR-OpenOrca-Platypus를 병합한 한국어 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Thank you for HumanF-MarkrAI/WIKI_QA_Near_dedup.  (Sampling about 10K)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `ko-kiwi dataset🥝` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `ko-kiwi dataset🥝` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `260` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Use my dataset kyujinpy/KOR-OpenOrca-Platypus.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1040자 ≈ 260 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tensorblock__Ko-PlatYi-6B-kiwi-GGUF|tensorblock/Ko-PlatYi-6B-kiwi-GGUF]]
- [[tensorblock__ko-platypus-kiwi-13B-GGUF|tensorblock/ko-platypus-kiwi-13B-GGUF]]
