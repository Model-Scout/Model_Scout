---
type: "dataset"
id: "anggars/mbti-emotion"
source: "huggingface"
url: "https://huggingface.co/datasets/anggars/mbti-emotion"
downloads: 48
summary: "수학 록 및 미드웨스트 이모 장르의 다국어 가사에 감정과 MBTI 분류 레이블을 부착한 데이터셋입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# anggars/mbti-emotion

> dataset · [Hugging Face](https://huggingface.co/datasets/anggars/mbti-emotion)

수학 록 및 미드웨스트 이모 장르의 다국어 가사에 감정과 MBTI 분류 레이블을 부착한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `This dataset contains 120,060 song-lyric passages annotated with two independent classification targets` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `a fine-grained emotion label (28 categories based on the GoEmotions taxonomy) and a Myers-Briggs Type Indicator (MBTI) personality type (16 categories).` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `214` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `All passages are written in the stylistic register of the math rock and midwest emo genres and span eleven languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset ships as a single `train` split.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `Text` 열 p90 854자 ≈ 214 토큰 (viewer statistics, default/train)
