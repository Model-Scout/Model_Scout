---
type: "dataset"
id: "skt/TelAgentBench"
source: "huggingface"
url: "https://huggingface.co/datasets/skt/TelAgentBench"
downloads: 34
summary: "TelAgentBench는 통신 산업 특화 LLM 에이전트 능력 평가용 한국어 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[평가용]]"
---
# skt/TelAgentBench

> dataset · [Hugging Face](https://huggingface.co/datasets/skt/TelAgentBench)

TelAgentBench는 통신 산업 특화 LLM 에이전트 능력 평가용 한국어 벤치마크입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · readme, tags = `LLM` · 신뢰도 medium
- **작업**: [[도구 호출]] — ner · readme = `TelAgent Action은 통신 고객 서비스 시나리오에서 LLM의 함수 호출(Function-calling) 능력을 평가합니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `한국어 지침 준수 능력을 멀티턴 대화 상황에서 평가하기 위해 설계되었습니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `한국어 지침 준수 능력을 멀티턴 대화 상황에서 평가하기 위해 설계되었습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `TelAgentBench는 LLM의 통신 산업 특화 에이전트 능력(Reasoning, Planning, Action, RAG, Instruction Following)을 평가하는 한국어 벤치마크입니다` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `TelAgentBench는 LLM의 통신 산업 특화 에이전트 능력(Reasoning, Planning, Action, RAG, Instruction Following)을 평가하는 한국어 벤치마크입니다` · 신뢰도 medium
