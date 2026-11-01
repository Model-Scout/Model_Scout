---
type: "dataset"
id: "youjunhyeok/Magpie-Pro-300K-Filtered-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/youjunhyeok/Magpie-Pro-300K-Filtered-ko"
downloads: 43
summary: "Llama 3 70B Instruct 기반으로 생성된 고품질 한글 명령-응답 데이터셋으로, 대형 언어 모델 정렬에 활용됨."
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
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# youjunhyeok/Magpie-Pro-300K-Filtered-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/youjunhyeok/Magpie-Pro-300K-Filtered-ko)

Llama 3 70B Instruct 기반으로 생성된 고품질 한글 명령-응답 데이터셋으로, 대형 언어 모델 정렬에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `We perform a comprehensive analysis of the extracted data and select 300K high-quality instances.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `High-quality instruction data is critical for aligning large language models (LLMs).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `generate 4 million instructions along with their corresponding responses.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `24` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `llama3` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `High-quality instruction data is critical for aligning large language models (LLMs).` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `uuid` 열 p90 36자 ≈ 24 토큰 (viewer statistics, default/train)
