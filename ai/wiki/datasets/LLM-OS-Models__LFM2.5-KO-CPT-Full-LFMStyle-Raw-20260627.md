---
type: "dataset"
id: "LLM-OS-Models/LFM2.5-KO-CPT-Full-LFMStyle-Raw-20260627"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-CPT-Full-LFMStyle-Raw-20260627"
downloads: 17
summary: "한국어 CPT 혼합 데이터를 LFM 스타일 JSONL로 변환한 약 40억 토큰 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
  - "[[일반]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# LLM-OS-Models/LFM2.5-KO-CPT-Full-LFMStyle-Raw-20260627

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/LFM2.5-KO-CPT-Full-LFMStyle-Raw-20260627)

한국어 CPT 혼합 데이터를 LFM 스타일 JSONL로 변환한 약 40억 토큰 학습용 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `Full Korean CPT mix converted to LFM-style text JSONL, about 4B-token training source.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `Full Korean CPT mix converted to LFM-style text JSONL` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Full Korean CPT mix converted to LFM-style text JSONL` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1943` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Korean finance/accounting text and instruction data: `bcai_finance_kor_hrm_20260524`, `BCAI-Finance-Kor-1862K`.` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `Korean Wiki/general knowledge: `kowiki_raw_full_20260524`.` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `Legal-domain attribution includes the public Legalize-KR ecosystem and the Korean law source ecosystem documented in the model card.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `It is intended for continued pretraining/mid-training, not final chat SFT.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2915자 ≈ 1943 토큰 (viewer statistics, default/train)
