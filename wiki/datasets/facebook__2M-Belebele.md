---
type: "dataset"
id: "facebook/2M-Belebele"
source: "huggingface"
url: "https://huggingface.co/datasets/facebook/2M-Belebele"
downloads: 688
summary: "74개 언어 음성 및 미국 수화 데이터로 다국어 음성 및 수화 이해 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[음성 인식]]"
  - "[[번역]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[영상 (출력 형식)|영상]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# facebook/2M-Belebele

> dataset · [Hugging Face](https://huggingface.co/datasets/facebook/2M-Belebele)

74개 언어 음성 및 미국 수화 데이터로 다국어 음성 및 수화 이해 연구용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[음성 인식]] — metadata · readme, tags, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **작업**: [[이미지 이해]] — ner · readme = `The ASL dataset is built with completely new controlled recordings of ASL signers and each flores sentence as well as questions and answers are available in vid` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `The speech dataset is built from aligning Belebele, Flores200 and Fleurs` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:translation, task:visual_qa = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `The ASL dataset is built with completely new controlled recordings of ASL signers and each flores sentence as well as questions and answers are available in vid` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `the audio recording for the question, a single speaker is provided.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering, task:speech_recognition, task:translation, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[영상 (출력 형식)|영상]] — ner · readme = `The ASL dataset is built with completely new controlled recordings of ASL signers and each flores sentence as well as questions and answers are available in vid` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `73 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `88` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Highly-Multilingual Speech and American Sign Language Comprehension Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The huggingface dataset `facebook/2M-Belebele` provides the speech version of 2M-Belebele` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `flores_passage` 열 p90 350자 ≈ 88 토큰 (viewer statistics, kor_Hang/test)
