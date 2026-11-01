---
type: "dataset"
id: "FredZhang7/all-scam-spam"
source: "huggingface"
url: "https://huggingface.co/datasets/FredZhang7/all-scam-spam"
downloads: 431
summary: "43개 언어로 된 42,619개의 스팸 및 정상 문자와 이메일 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# FredZhang7/all-scam-spam

> dataset · [Hugging Face](https://huggingface.co/datasets/FredZhang7/all-scam-spam)

43개 언어로 된 42,619개의 스팸 및 정상 문자와 이메일 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `a large corpus of 42,619 preprocessed text messages and emails` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``is_spam=1` means spam and `is_spam=0` means ham.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6766` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a large corpus of 42,619 preprocessed text messages and emails sent by humans in 43 languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `If you plan to train a model based on this dataset alone, I recommend adding **some** rows with `is_toxic=0` from `FredZhang7/toxi-text-3M`.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 27065자 ≈ 6766 토큰 (viewer statistics, default/train)
