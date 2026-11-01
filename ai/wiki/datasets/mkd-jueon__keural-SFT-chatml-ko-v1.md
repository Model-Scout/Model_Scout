---
type: "dataset"
id: "mkd-jueon/keural-SFT-chatml-ko-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-jueon/keural-SFT-chatml-ko-v1"
downloads: 55
summary: "한국어 SFT용 공개 instruction/대화 데이터셋 8종 통합 정제 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# mkd-jueon/keural-SFT-chatml-ko-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-jueon/keural-SFT-chatml-ko-v1)

한국어 SFT용 공개 instruction/대화 데이터셋 8종 통합 정제 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `947` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `공개 한국어 instruction/대화 데이터셋 8종을 수집하여 정제` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 SFT(Supervised Fine-Tuning)용 통합 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1420자 ≈ 947 토큰 (viewer statistics, claude_reasoning_ko/train)
