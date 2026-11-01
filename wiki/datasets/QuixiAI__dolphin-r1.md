---
type: "dataset"
id: "QuixiAI/dolphin-r1"
source: "huggingface"
url: "https://huggingface.co/datasets/QuixiAI/dolphin-r1"
downloads: 881
summary: "Dolphin R1은 R1 스타일 추론 모델 학습용 80만 샘플 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# QuixiAI/dolphin-r1

> dataset · [Hugging Face](https://huggingface.co/datasets/QuixiAI/dolphin-r1)

Dolphin R1은 R1 스타일 추론 모델 학습용 80만 샘플 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The purpose of this dataset is to train R1-style reasoning models.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `We create a 800k sample dataset similar in composition to the one used to train DeepSeek-R1 Distill models.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The purpose of this dataset is to train R1-style reasoning models.` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The purpose of this dataset is to train R1-style reasoning models.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Flexan__UmbrellaInc-Albert_Wesker-1B-GGUF|Flexan/UmbrellaInc-Albert_Wesker-1B-GGUF]]
- [[Lamapi__next-12b-Q4_K_M-GGUF|Lamapi/next-12b-Q4_K_M-GGUF]]
- [[Lamapi__next-14b-Q4_K_M-GGUF|Lamapi/next-14b-Q4_K_M-GGUF]]
- [[Lamapi__next-4b-Q4_K_M-GGUF|Lamapi/next-4b-Q4_K_M-GGUF]]
- [[Lamapi__next-8b-Q4_K_M-GGUF|Lamapi/next-8b-Q4_K_M-GGUF]]
- [[NovaCorp__Gemma3.Novaciano-1B|NovaCorp/Gemma3.Novaciano-1B]]
- [[mradermacher__Albert_Wesker-1B-GGUF|mradermacher/Albert_Wesker-1B-GGUF]]
- [[mradermacher__Albert_Wesker-1B-i1-GGUF|mradermacher/Albert_Wesker-1B-i1-GGUF]]
- [[mradermacher__Gemma3.Novaciano-1B-GGUF|mradermacher/Gemma3.Novaciano-1B-GGUF]]
- [[mradermacher__Gemma3.Novaciano-1B-i1-GGUF|mradermacher/Gemma3.Novaciano-1B-i1-GGUF]]
- [[mradermacher__Hans_Wesker-1B-GGUF|mradermacher/Hans_Wesker-1B-GGUF]]
- [[mradermacher__Hans_Wesker-1B-i1-GGUF|mradermacher/Hans_Wesker-1B-i1-GGUF]]
- [[mradermacher__Prototype-Virus-1B-GGUF|mradermacher/Prototype-Virus-1B-GGUF]]
- [[mradermacher__Prototype-Virus-1B-i1-GGUF|mradermacher/Prototype-Virus-1B-i1-GGUF]]
- [[mradermacher__next-12b-GGUF|mradermacher/next-12b-GGUF]]
- [[mradermacher__next-12b-i1-GGUF|mradermacher/next-12b-i1-GGUF]]
- [[mradermacher__next-14b-GGUF|mradermacher/next-14b-GGUF]]
- [[mradermacher__next-14b-i1-GGUF|mradermacher/next-14b-i1-GGUF]]
- [[mradermacher__next-1b-GGUF|mradermacher/next-1b-GGUF]]
- [[mradermacher__next-32b-GGUF|mradermacher/next-32b-GGUF]]
- [[mradermacher__next-32b-i1-GGUF|mradermacher/next-32b-i1-GGUF]]
- [[mradermacher__next-8b-GGUF|mradermacher/next-8b-GGUF]]
- [[mradermacher__next-8b-i1-GGUF|mradermacher/next-8b-i1-GGUF]]
- [[mradermacher__next2-fast-GGUF|mradermacher/next2-fast-GGUF]]
- [[mradermacher__next2-fast-i1-GGUF|mradermacher/next2-fast-i1-GGUF]]
- [[thelamapi__next-12b|thelamapi/next-12b]]
- [[thelamapi__next-1b|thelamapi/next-1b]]
- [[thelamapi__next-32b|thelamapi/next-32b]]
- [[thelamapi__next-4b|thelamapi/next-4b]]
- [[thelamapi__next2-fast-GGUF|thelamapi/next2-fast-GGUF]]
- [[thelamapi__next2-fast-i1-GGUF|thelamapi/next2-fast-i1-GGUF]]
