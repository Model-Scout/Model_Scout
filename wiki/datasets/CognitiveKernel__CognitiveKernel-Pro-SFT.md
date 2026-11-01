---
type: "dataset"
id: "CognitiveKernel/CognitiveKernel-Pro-SFT"
source: "huggingface"
url: "https://huggingface.co/datasets/CognitiveKernel/CognitiveKernel-Pro-SFT"
downloads: 174
summary: "GPT-4.1 기반 심층 연구 에이전트 학습용 SFT 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# CognitiveKernel/CognitiveKernel-Pro-SFT

> dataset · [Hugging Face](https://huggingface.co/datasets/CognitiveKernel/CognitiveKernel-Pro-SFT)

GPT-4.1 기반 심층 연구 에이전트 학습용 SFT 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Here is the SFT data for the paper Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `We use GPT-4.1 to sample from the training queries and perform rejection sampling to acquire the successful trajectories.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `We use GPT-4.1 to sample from the training queries and perform rejection sampling to acquire the successful trajectories.` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Here is the SFT data for the paper Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

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
- [[mradermacher__next2-0.8b-GGUF|mradermacher/next2-0.8b-GGUF]]
- [[mradermacher__next2-air-GGUF|mradermacher/next2-air-GGUF]]
- [[mradermacher__next2-air-i1-GGUF|mradermacher/next2-air-i1-GGUF]]
- [[mradermacher__next2-fast-GGUF|mradermacher/next2-fast-GGUF]]
- [[mradermacher__next2-fast-i1-GGUF|mradermacher/next2-fast-i1-GGUF]]
- [[mradermacher__next2.5-GGUF|mradermacher/next2.5-GGUF]]
- [[mradermacher__next2.5-i1-GGUF|mradermacher/next2.5-i1-GGUF]]
- [[thelamapi__next-12b|thelamapi/next-12b]]
- [[thelamapi__next-1b|thelamapi/next-1b]]
- [[thelamapi__next-32b|thelamapi/next-32b]]
- [[thelamapi__next-4b|thelamapi/next-4b]]
- [[thelamapi__next2-0.8b-GGUF|thelamapi/next2-0.8b-GGUF]]
- [[thelamapi__next2-air-GGUF|thelamapi/next2-air-GGUF]]
- [[thelamapi__next2-air-i1-GGUF|thelamapi/next2-air-i1-GGUF]]
- [[thelamapi__next2-fast-GGUF|thelamapi/next2-fast-GGUF]]
- [[thelamapi__next2-fast-i1-GGUF|thelamapi/next2-fast-i1-GGUF]]
- [[thelamapi__next2.5-GGUF|thelamapi/next2.5-GGUF]]
- [[thelamapi__next2.5-i1-GGUF|thelamapi/next2.5-i1-GGUF]]
