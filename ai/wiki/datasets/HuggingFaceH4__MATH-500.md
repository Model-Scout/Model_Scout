---
type: "dataset"
id: "HuggingFaceH4/MATH-500"
source: "huggingface"
url: "https://huggingface.co/datasets/HuggingFaceH4/MATH-500"
downloads: 189732
summary: "OpenAI의 MATH 벤치마크에서 500문제를 추출한 수학 문제 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# HuggingFaceH4/MATH-500

> dataset · [Hugging Face](https://huggingface.co/datasets/HuggingFaceH4/MATH-500)

OpenAI의 MATH 벤치마크에서 500문제를 추출한 수학 문제 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `This dataset contains a subset of 500 problems from the MATH benchmark` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `500 problems` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `500 problems` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `260` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `MATH benchmark` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset contains a subset of 500 problems from the MATH benchmark` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `solution` 열 p90 1041자 ≈ 260 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[Flexan__UmbrellaInc-Albert_Wesker-1B-GGUF|Flexan/UmbrellaInc-Albert_Wesker-1B-GGUF]]
- [[Lamapi__next-12b-Q4_K_M-GGUF|Lamapi/next-12b-Q4_K_M-GGUF]]
- [[Lamapi__next-4b-Q4_K_M-GGUF|Lamapi/next-4b-Q4_K_M-GGUF]]
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
- [[mradermacher__next-70b-GGUF|mradermacher/next-70b-GGUF]]
- [[mradermacher__next-70b-i1-GGUF|mradermacher/next-70b-i1-GGUF]]
- [[thelamapi__next-12b|thelamapi/next-12b]]
- [[thelamapi__next-1b|thelamapi/next-1b]]
- [[thelamapi__next-4b|thelamapi/next-4b]]
- [[thelamapi__next-70b-GGUF|thelamapi/next-70b-GGUF]]
- [[thelamapi__next-70b-i1-GGUF|thelamapi/next-70b-i1-GGUF]]
