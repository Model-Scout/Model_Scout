---
type: "dataset"
id: "MMTR-Bench/MMTR-Bench-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/MMTR-Bench/MMTR-Bench-Dataset"
downloads: 481
summary: "MMTR-Bench는 복잡한 멀티모달 입력에서 시각적 문맥 복원을 평가하는 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[리랭킹]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# MMTR-Bench/MMTR-Bench-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/MMTR-Bench/MMTR-Bench-Dataset)

MMTR-Bench는 복잡한 멀티모달 입력에서 시각적 문맥 복원을 평가하는 벤치마크입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `models must recover the hidden text by relying on the remaining layout structure, visual cues, and relevant world knowledge` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Unlike traditional question-answering tasks, MMTR-Bench presents models with masked single- or multi-image inputs from diverse real-world scenarios` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `testing their fundamental capacity for end-to-end document parsing and structured reading` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `masked single- or multi-image inputs from diverse real-world scenarios` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:reranking, task:visual_qa = `recover the hidden text by relying on the remaining layout structure, visual cues` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:visual_qa = `models must recover the hidden text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `11` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `diverse real-world scenarios, such as documents and webpages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `MMTR-Bench is an evaluation-only benchmark designed to test Multimodal LLMs. There is no training set.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `file_name` 열 p90 43자 ≈ 11 토큰 (viewer statistics, default/test)
