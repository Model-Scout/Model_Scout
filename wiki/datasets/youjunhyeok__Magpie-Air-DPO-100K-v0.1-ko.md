---
type: "dataset"
id: "youjunhyeok/Magpie-Air-DPO-100K-v0.1-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/youjunhyeok/Magpie-Air-DPO-100K-v0.1-ko"
downloads: 57
summary: "Magpie-Align의 Llama-3-Instruct 기반 고품질 지침 데이터셋으로, 대규모 언어 모델 정렬에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# youjunhyeok/Magpie-Air-DPO-100K-v0.1-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/youjunhyeok/Magpie-Air-DPO-100K-v0.1-ko)

Magpie-Align의 Llama-3-Instruct 기반 고품질 지침 데이터셋으로, 대규모 언어 모델 정렬에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `annotated RM scores using RLHFlow/ArmoRM-Llama3-8B-v0.1, labeling the response with the highest RM score as the chosen response, and the one with the lowest RM ` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `selected 100K high-quality Magpie instructions with diverse task categories` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1060` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `High-quality instruction data is critical for aligning large language models (LLMs).` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `quality_explanation` 열 p90 1590자 ≈ 1060 토큰 (viewer statistics, default/train)
