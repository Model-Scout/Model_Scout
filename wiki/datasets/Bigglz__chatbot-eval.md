---
type: "dataset"
id: "Bigglz/chatbot-eval"
source: "huggingface"
url: "https://huggingface.co/datasets/Bigglz/chatbot-eval"
downloads: 771
summary: "chatbot-ft 평가 기록과 LLM-as-a-judge 판정 데이터를 포함한 벤치마크 결과 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# Bigglz/chatbot-eval

> dataset · [Hugging Face](https://huggingface.co/datasets/Bigglz/chatbot-eval)

chatbot-ft 평가 기록과 LLM-as-a-judge 판정 데이터를 포함한 벤치마크 결과 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `LLM-as-a-judge 기록` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `판정 기록 (순서를 바꿔 2회)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering, task:reranking = `모델별 대화 (generation_config.json 의 조건이 같으면 상대 모델과 무관하게 재사용)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `판정 기록 (순서를 바꿔 2회)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `chatbot-ft 평가 기록` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `벤치마크 결과와 LLM-as-a-judge 기록` · 신뢰도 medium
