---
type: "dataset"
id: "jaeyong2/cartesia-sonic-preview-ztts1-zero-shot"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/cartesia-sonic-preview-ztts1-zero-shot"
downloads: 336
summary: "7개 언어 500문장씩 음성 클로닝 TTS 합성 및 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/cartesia-sonic-preview-ztts1-zero-shot

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/cartesia-sonic-preview-ztts1-zero-shot)

7개 언어 500문장씩 음성 클로닝 TTS 합성 및 평가 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `WavLM-SV speaker similarity (Seed-TTS-eval protocol)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Zero-shot voice-cloning TTS on the ZTTS1-Eval benchmark` · 신뢰도 low
- **작업**: [[음성 합성]] — tag_match · tags = `tts` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `audio + texts + both scorings` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation, task:text_to_speech = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `Synthetic audio is provided for research evaluation of the respective TTS systems.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `47` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `ZTTS1-Eval benchmark (Zyphra, FLEURS-R based)` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Synthetic audio is provided for research evaluation of the respective TTS systems.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `target_text` 열 p90 190자 ≈ 47 토큰 (viewer statistics, default/train)
