---
type: "dataset"
id: "huggingface-KREW/Ko-AgentBench"
source: "huggingface"
url: "https://huggingface.co/datasets/huggingface-KREW/Ko-AgentBench"
downloads: 242
summary: "한국 실사용 환경에 특화된 AI 에이전트 능력 평가용 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[도구 호출]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# huggingface-KREW/Ko-AgentBench

> dataset · [Hugging Face](https://huggingface.co/datasets/huggingface-KREW/Ko-AgentBench)

한국 실사용 환경에 특화된 AI 에이전트 능력 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-use` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `단일턴(single-turn) 및 멀티턴(multi-turn) 대화 상황에서 Agent로써 Tool calling 수행 능력` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `단일턴(single-turn) 및 멀티턴(multi-turn) 대화 상황에서 Agent로써 Tool calling 수행 능력` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `48` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국 실사용 환경에 특화된 고품질 에이전트 벤치마크를 개발하였습니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `이 데이터셋은 벤치마크 태스크 정보만 포함하고 있습니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 72자 ≈ 48 토큰 (viewer statistics, default/L1)
