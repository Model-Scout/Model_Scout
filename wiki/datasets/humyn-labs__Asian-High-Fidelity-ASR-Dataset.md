---
type: "dataset"
id: "humyn-labs/Asian-High-Fidelity-ASR-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/humyn-labs/Asian-High-Fidelity-ASR-Dataset"
downloads: 268
summary: "베트남어, 한국어, 아랍어, 필리핀어 대화 음성 인식용 고품질 음성-텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# humyn-labs/Asian-High-Fidelity-ASR-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/humyn-labs/Asian-High-Fidelity-ASR-Dataset)

베트남어, 한국어, 아랍어, 필리핀어 대화 음성 인식용 고품질 음성-텍스트 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, tags, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `Paired audio + transcripts` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `Paired audio + transcripts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Paired audio + transcripts` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `615` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains high-quality conversational audio samples curated for Automatic Speech Recognition tasks in Vietnamese, Korean, Arabic and Filipino.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Conversational ASR benchmarking` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `transcript_json` 열 p90 2462자 ≈ 615 토큰 (viewer statistics, default/train)
