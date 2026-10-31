---
type: "dataset"
id: "ThakiCloud/EnterpriseOps-KO-Policy"
source: "huggingface"
url: "https://huggingface.co/datasets/ThakiCloud/EnterpriseOps-KO-Policy"
downloads: 156
summary: "한국어 기업 상담 에이전트가 회사 정책을 읽고 올바른 행동을 고르는 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
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
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ThakiCloud/EnterpriseOps-KO-Policy

> dataset · [Hugging Face](https://huggingface.co/datasets/ThakiCloud/EnterpriseOps-KO-Policy)

한국어 기업 상담 에이전트가 회사 정책을 읽고 올바른 행동을 고르는 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `각 문항은 정책(규정과 예외 조항)과 고객 요청으로 이루어져 있고` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `모델은 행동 7종 (ANSWER · ASK_CLARIFICATION · ASK_CONFIRMATION · CALL_TOOL · CALL_MULTIPLE_TOOLS · ESCALATE · REFUSE) 가운데 하나를 JSON 으로 답합니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `133` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 기업 상담 에이전트가 회사 정책을 읽고 올바른 행동 하나를 고르는지 재는 벤치마크입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `판정자 동의 2,414문항이 논문의 clean 분할입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 200자 ≈ 133 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[ThakiCloud__Qwen3.8-27B-Human-KO-Enterprise-v0.1|ThakiCloud/Qwen3.8-27B-Human-KO-Enterprise-v0.1]]
- [[ThakiCloud__Qwen3.8-27B-Human-KO-Enterprise-v0.2|ThakiCloud/Qwen3.8-27B-Human-KO-Enterprise-v0.2]]
