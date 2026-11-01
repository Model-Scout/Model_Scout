---
type: "dataset"
id: "hakimi20274/xeus-l14-content-features"
source: "huggingface"
url: "https://huggingface.co/datasets/hakimi20274/xeus-l14-content-features"
downloads: 105
summary: "XEUS L14 음성/노래 특징과 실험적 콘텐츠 투영 데이터셋으로 음성 인식 및 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pl]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# hakimi20274/xeus-l14-content-features

> dataset · [Hugging Face](https://huggingface.co/datasets/hakimi20274/xeus-l14-content-features)

XEUS L14 음성/노래 특징과 실험적 콘텐츠 투영 데이터셋으로 음성 인식 및 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The same-phoneme test used 240 English speech/singing clips from three GTSinger identity labels absent from fitting manifests.` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `约 101.665 小时已选取音频对应的 XEUS L14 特征（包含留出数据）` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `Inputs are mono, resampled to 16 kHz.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each restored `.npy` is `[frames, 1024]`, little-endian float16.` · 신뢰도 low
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[pl]] — metadata · languages = `pl` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Features include eight languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `约 101.665 小时已选取音频对应的 XEUS L14 特征（包含留出数据）` · 신뢰도 low
