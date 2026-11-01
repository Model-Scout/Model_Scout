---
type: "dataset"
id: "JailbreakV-28K/JailBreakV-28k"
source: "huggingface"
url: "https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k"
downloads: 4169
summary: "멀티모달 대형 언어 모델의 탈옥 공격 대응력을 평가하는 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# JailbreakV-28K/JailBreakV-28k

> dataset · [Hugging Face](https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k)

멀티모달 대형 언어 모델의 탈옥 공격 대응력을 평가하는 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `assessing the robustness of MultiModal Large Language Models against Jailbreak Attacks` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `evaluating the transferability of jailbreak attacks from LLMs to MLLMs` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `28, 000 jailbreak text-image pairs` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:question_answering = `jailbreak_query obtained by different jailbreak attacks` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `harmful query from RedTeam_2K` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `430` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MultiModal Large Language Models` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `a comprehensive and diversified benchmark for evaluating the transferability of jailbreak attacks` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `JailBreakV-28K contains 28, 000 jailbreak text-image pairs` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `jailbreak_query` 열 p90 1718자 ≈ 430 토큰 (viewer statistics, JailBreakV_28K/mini_JailBreakV_28K)

## 이 데이터로 학습한 모델

- [[Horizon-Labs__prompt-injection-guard-base|Horizon-Labs/prompt-injection-guard-base]]
- [[Horizon-Labs__prompt-injection-guard-large|Horizon-Labs/prompt-injection-guard-large]]
- [[Horizon-Labs__prompt-injection-guard-small|Horizon-Labs/prompt-injection-guard-small]]
