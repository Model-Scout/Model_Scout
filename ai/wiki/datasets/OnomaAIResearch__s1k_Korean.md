---
type: "dataset"
id: "OnomaAIResearch/s1k_Korean"
source: "huggingface"
url: "https://huggingface.co/datasets/OnomaAIResearch/s1k_Korean"
downloads: 56
summary: "1,000개의 문제-해결 쌍과 사고 과정이 포함된 한국어 복잡한 추론 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# OnomaAIResearch/s1k_Korean

> dataset · [Hugging Face](https://huggingface.co/datasets/OnomaAIResearch/s1k_Korean)

1,000개의 문제-해결 쌍과 사고 과정이 포함된 한국어 복잡한 추론 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset can be used for the following tasks:
- Complex reasoning
- Chain-of-thought (CoT) prompting
- Problem-solving capabilities evaluation
- Korean lang` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `each instance including the problem statement, solution, and detailed thinking trajectories (chain-of-thought reasoning) in Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `providing both the final solutions and the step-by-step reasoning processes` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `10395` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It contains 1,000 problem-solution pairs across various domains` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is designed to help train and evaluate Korean language models on complex reasoning tasks` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `thinking_trajectories` 열 p90 15592자 ≈ 10395 토큰 (viewer statistics, default/train)
