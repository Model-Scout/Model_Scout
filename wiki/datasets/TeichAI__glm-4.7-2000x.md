---
type: "dataset"
id: "TeichAI/glm-4.7-2000x"
source: "huggingface"
url: "https://huggingface.co/datasets/TeichAI/glm-4.7-2000x"
downloads: 102
summary: "GLM 4.7 모델로 생성된 추론 데이터셋으로, 오픈소스 LLM 미세조정용입니다."
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# TeichAI/glm-4.7-2000x

> dataset · [Hugging Face](https://huggingface.co/datasets/TeichAI/glm-4.7-2000x)

GLM 4.7 모델로 생성된 추론 데이터셋으로, 오픈소스 LLM 미세조정용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset includes an addition to our recently enhanced set of prompts to cover creative writing multilingual reasoning and various graduate level questions ` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Total tokens (input + output): 14.1 M` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Total tokens (input + output): 14.1 M` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `various graduate level questions across a wide variety of domains.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset is meant for creating distilled versions of GLM 4.7 by fine-tuning already existing open-source LLMs.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[NovaCorp__Gemma3.Novaciano-1B|NovaCorp/Gemma3.Novaciano-1B]]
- [[mradermacher__Albert_Wesker-1B-GGUF|mradermacher/Albert_Wesker-1B-GGUF]]
- [[mradermacher__Albert_Wesker-1B-i1-GGUF|mradermacher/Albert_Wesker-1B-i1-GGUF]]
- [[mradermacher__Gemma3.Novaciano-1B-GGUF|mradermacher/Gemma3.Novaciano-1B-GGUF]]
- [[mradermacher__Gemma3.Novaciano-1B-i1-GGUF|mradermacher/Gemma3.Novaciano-1B-i1-GGUF]]
