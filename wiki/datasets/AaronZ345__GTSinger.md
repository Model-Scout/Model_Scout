---
type: "dataset"
id: "AaronZ345/GTSinger"
source: "huggingface"
url: "https://huggingface.co/datasets/AaronZ345/GTSinger"
downloads: 44129
summary: "GTSinger는 다양한 언어와 기법의 고품질 노래 음성 및 음악 점수를 포함한 노래 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[문서 파일 (출력 형식)|문서 파일]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# AaronZ345/GTSinger

> dataset · [Hugging Face](https://huggingface.co/datasets/AaronZ345/GTSinger)

GTSinger는 다양한 언어와 기법의 고품질 노래 음성 및 음악 점수를 포함한 노래 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `singing technique modeling, recognition, and control` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `designed for all singing tasks` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-audio` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality = `audio` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `musicxml format` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:text_to_speech = `manual phoneme-to-audio alignments, global style labels` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[문서 파일 (출력 형식)|문서 파일]] — ner · readme = `musicxml format` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `manual phoneme-to-audio alignments, global style labels` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `22` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A Global Multi-Technique Singing Corpus with Realistic Music Scores for All Singing Tasks` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `speech_fn` 열 p90 90자 ≈ 22 토큰 (viewer statistics, meta/train)
