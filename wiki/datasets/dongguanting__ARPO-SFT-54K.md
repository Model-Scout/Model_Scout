---
type: "dataset"
id: "dongguanting/ARPO-SFT-54K"
source: "huggingface"
url: "https://huggingface.co/datasets/dongguanting/ARPO-SFT-54K"
downloads: 127
summary: "ARPO-SFT-54K는 LLM 기반 에이전트의 강화학습을 위한 수퍼바이즈드 파인튜닝 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# dongguanting/ARPO-SFT-54K

> dataset · [Hugging Face](https://huggingface.co/datasets/dongguanting/ARPO-SFT-54K)

ARPO-SFT-54K는 LLM 기반 에이전트의 강화학습을 위한 수퍼바이즈드 파인튜닝 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `training and validation datasets to demonstrate the effectiveness of the proposed method` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — ner · readme = `benchmarks in computational reasoning, knowledge reasoning, and deep search domains` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `training multi-turn Large Language Model (LLM)-based agents` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `training multi-turn Large Language Model (LLM)-based agents` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `computational reasoning, knowledge reasoning, and deep search domains` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Supervised Fine-Tuning (SFT) dataset, `ARPO-SFT-54K`, is also released for cold-start fine-tuning` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Flexan__UmbrellaInc-Albert_Wesker-1B-GGUF|Flexan/UmbrellaInc-Albert_Wesker-1B-GGUF]]
- [[Lamapi__next-12b-Q4_K_M-GGUF|Lamapi/next-12b-Q4_K_M-GGUF]]
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
- [[mradermacher__next-1b-GGUF|mradermacher/next-1b-GGUF]]
- [[mradermacher__next-8b-GGUF|mradermacher/next-8b-GGUF]]
- [[mradermacher__next-8b-i1-GGUF|mradermacher/next-8b-i1-GGUF]]
- [[mradermacher__next2-fast-GGUF|mradermacher/next2-fast-GGUF]]
- [[mradermacher__next2-fast-i1-GGUF|mradermacher/next2-fast-i1-GGUF]]
- [[thelamapi__next-12b|thelamapi/next-12b]]
- [[thelamapi__next-1b|thelamapi/next-1b]]
- [[thelamapi__next-4b|thelamapi/next-4b]]
- [[thelamapi__next2-fast-GGUF|thelamapi/next2-fast-GGUF]]
- [[thelamapi__next2-fast-i1-GGUF|thelamapi/next2-fast-i1-GGUF]]
