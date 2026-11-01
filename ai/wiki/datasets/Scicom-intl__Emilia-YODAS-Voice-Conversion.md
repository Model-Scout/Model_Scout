---
type: "dataset"
id: "Scicom-intl/Emilia-YODAS-Voice-Conversion"
source: "huggingface"
url: "https://huggingface.co/datasets/Scicom-intl/Emilia-YODAS-Voice-Conversion"
downloads: 769
summary: "Emilia-YODAS-Voice-Conversion은 음성 변환을 위한 다국어 음성 토큰 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[ms]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Scicom-intl/Emilia-YODAS-Voice-Conversion

> dataset · [Hugging Face](https://huggingface.co/datasets/Scicom-intl/Emilia-YODAS-Voice-Conversion)

Emilia-YODAS-Voice-Conversion은 음성 변환을 위한 다국어 음성 토큰 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We sample https://huggingface.co/datasets/amphion/Emilia-Dataset YODAS set for voice conversion.` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `Convert audio to speech tokens using https://huggingface.co/neuphonic/neucodec` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `Convert audio to speech tokens using https://huggingface.co/neuphonic/neucodec` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[ms]] — metadata · languages = `ms` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `88` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `We sample https://huggingface.co/datasets/amphion/Emilia-Dataset YODAS set for voice conversion.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `target_text` 열 p90 352자 ≈ 88 토큰 (viewer statistics, default/train)
