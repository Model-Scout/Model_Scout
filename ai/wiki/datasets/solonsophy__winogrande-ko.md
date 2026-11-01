---
type: "dataset"
id: "solonsophy/winogrande-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/solonsophy/winogrande-ko"
downloads: 65
summary: "Winogrande 데이터셋의 한국어 번역본으로 상식 추론과 이진 텍스트 분류에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# solonsophy/winogrande-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/solonsophy/winogrande-ko)

Winogrande 데이터셋의 한국어 번역본으로 상식 추론과 이진 텍스트 분류에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `- `answer`: Correct answer "1" or "2" (Empty string `""` in Test set)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `84` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Winogrande is a commonsense reasoning benchmark consisting of 44k fill-in-the-blank problems.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train
40,398
Main training data (verified clean)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 126자 ≈ 84 토큰 (viewer statistics, default/validation)
