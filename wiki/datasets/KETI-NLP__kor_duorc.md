---
type: "dataset"
id: "KETI-NLP/kor_duorc"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_duorc"
downloads: 85
summary: "DuoRC 데이터셋은 복잡한 언어 이해를 위한 패러프레이즈 독해 데이터셋입니다."
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
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KETI-NLP/kor_duorc

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_duorc)

DuoRC 데이터셋은 복잡한 언어 이해를 위한 패러프레이즈 독해 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Towards Complex Language Understanding with Paraphrased Reading Comprehension` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Towards Complex Language Understanding with Paraphrased Reading Comprehension` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4587` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `plot` 열 p90 6880자 ≈ 4587 토큰 (viewer statistics, default/ParaphraseRC_train)
