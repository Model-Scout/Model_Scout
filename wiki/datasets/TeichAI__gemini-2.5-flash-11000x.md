---
type: "dataset"
id: "TeichAI/gemini-2.5-flash-11000x"
source: "huggingface"
url: "https://huggingface.co/datasets/TeichAI/gemini-2.5-flash-11000x"
downloads: 117
summary: "Gemini 2.5 Flash 모델을 11,000회 이상 질의해 생성한 다양한 도메인 지식 데이터셋입니다."
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
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# TeichAI/gemini-2.5-flash-11000x

> dataset · [Hugging Face](https://huggingface.co/datasets/TeichAI/gemini-2.5-flash-11000x)

Gemini 2.5 Flash 모델을 11,000회 이상 질의해 생성한 다양한 도메인 지식 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset was created by querying Gemini 2.5 Flash over 11,000 times with the goal of compiling the behavior, reasoning traces, output style, and (most impor` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `This dataset was created by querying Gemini 2.5 Flash over 11,000 times` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `This dataset was created by querying Gemini 2.5 Flash over 11,000 times with the goal of compiling the behavior, reasoning traces, output style, and (most impor` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Prompt Distribution: | Domain | Prompts | | ------- | ---------| | Academia | 645 |` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset was created by querying Gemini 2.5 Flash over 11,000 times with the goal of compiling the behavior, reasoning traces, output style, and (most impor` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[DavidAU__Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k|DavidAU/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k]]
