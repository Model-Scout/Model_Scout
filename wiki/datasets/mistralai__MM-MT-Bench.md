---
type: "dataset"
id: "mistralai/MM-MT-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/mistralai/MM-MT-Bench"
downloads: 246
summary: "MM-MT-Bench는 멀티모달 지침 튜닝 모델 평가를 위한 다중 대화형 LLM 평가 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
  - "[[리랭킹]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mistralai/MM-MT-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/mistralai/MM-MT-Bench)

MM-MT-Bench는 멀티모달 지침 튜닝 모델 평가를 위한 다중 대화형 LLM 평가 벤치마크입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `answer open-ended questions in a zero-shot manner` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `LLM-as-a-judge evaluation benchmark` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `multimodal instruction-tuned models` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:reranking = `multi-turn dialogues` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `answer open-ended questions` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `989` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `testing multimodal instruction-tuned models` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `evaluation benchmark` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `conversation` 열 p90 3955자 ≈ 989 토큰 (viewer statistics, default/eval)

## 이 데이터로 학습한 모델

- [[EnlistedGhost__Ministral-3-14B-Instruct-2512-GGUF|EnlistedGhost/Ministral-3-14B-Instruct-2512-GGUF]]
- [[EnlistedGhost__Ministral-3-14B-Reasoning-2512-GGUF|EnlistedGhost/Ministral-3-14B-Reasoning-2512-GGUF]]
- [[EnlistedGhost__Ministral-3-3B-Instruct-2512-GGUF|EnlistedGhost/Ministral-3-3B-Instruct-2512-GGUF]]
- [[EnlistedGhost__Ministral-3-3B-Reasoning-2512-GGUF|EnlistedGhost/Ministral-3-3B-Reasoning-2512-GGUF]]
- [[EnlistedGhost__Ministral-3-8B-Instruct-2512-GGUF|EnlistedGhost/Ministral-3-8B-Instruct-2512-GGUF]]
- [[EnlistedGhost__Ministral-3-8B-Reasoning-2512-GGUF|EnlistedGhost/Ministral-3-8B-Reasoning-2512-GGUF]]
