---
type: "dataset"
id: "alisawuffles/WANLI"
source: "huggingface"
url: "https://huggingface.co/datasets/alisawuffles/WANLI"
downloads: 15197
summary: "WANLI는 자연어 추론(NLI) 작업을 위한 108K 영어 문장 쌍 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# alisawuffles/WANLI

> dataset · [Hugging Face](https://huggingface.co/datasets/alisawuffles/WANLI)

WANLI는 자연어 추론(NLI) 작업을 위한 108K 영어 문장 쌍 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `WANLI (Worker-AI Collaboration for NLI) is a collection of 108K English sentence pairs for the task of natural language inference (NLI).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset can be used to train a model for natural language inference, which determines whether a premise entails (i.e., implies the truth of) a hypothesis, b` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `40` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `WANLI (Worker-AI Collaboration for NLI) is a collection of 108K English sentence pairs for the task of natural language inference (NLI).` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The dataset is randomly split into a *train* and *test* set.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset is randomly split into a *train* and *test* set.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `premise` 열 p90 160자 ≈ 40 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[BalaRajesh1__mmbert-small-nli|BalaRajesh1/mmbert-small-nli]]
- [[Horizon-Labs__hallucination-guard-base|Horizon-Labs/hallucination-guard-base]]
- [[Horizon-Labs__hallucination-guard-small|Horizon-Labs/hallucination-guard-small]]
