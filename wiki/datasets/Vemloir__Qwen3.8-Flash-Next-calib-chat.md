---
type: "dataset"
id: "Vemloir/Qwen3.8-Flash-Next-calib-chat"
source: "huggingface"
url: "https://huggingface.co/datasets/Vemloir/Qwen3.8-Flash-Next-calib-chat"
downloads: 100
summary: "Qwen3.8-Flash-Next 모델의 자체 생성된 과학 분야 다국어 대화 교정 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Vemloir/Qwen3.8-Flash-Next-calib-chat

> dataset · [Hugging Face](https://huggingface.co/datasets/Vemloir/Qwen3.8-Flash-Next-calib-chat)

Qwen3.8-Flash-Next 모델의 자체 생성된 과학 분야 다국어 대화 교정 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Chat conversations, single- and multi-turn: science (biology, chemistry, physics, medicine, earth science) in 16 languages, everyday questions, writing, code, m` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Chat conversations, single- and multi-turn: science (biology, chemistry, physics, medicine, earth science) in 16 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Chat conversations, single- and multi-turn: science (biology, chemistry, physics, medicine, earth science) in 16 languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `5219` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odbl` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Chat conversations, single- and multi-turn: science (biology, chemistry, physics, medicine, earth science) in 16 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Part of the calibration data of the self-calibrated EXL3 quant of Qwen/Qwen3.8-Flash-Next` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 20877자 ≈ 5219 토큰 (viewer statistics, default/train)
