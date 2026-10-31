---
type: "dataset"
id: "microsoft/llmail-inject-challenge"
source: "huggingface"
url: "https://huggingface.co/datasets/microsoft/llmail-inject-challenge"
downloads: 6816
summary: "LLMail-Inject 챌린지에서 수집한 적응형 프롬프트 인젝션 공격 이메일 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# microsoft/llmail-inject-challenge

> dataset · [Hugging Face](https://huggingface.co/datasets/microsoft/llmail-inject-challenge)

LLMail-Inject 챌린지에서 수집한 적응형 프롬프트 인젝션 공격 이메일 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The LLMail service uses an LLM to process the user’s requests and generate responses based on the retrieved emails` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `The LLMail service includes a retriever component that searches this database and retrieves specific emails` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `The attacker has full control over the text in their email.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The LLMail service uses an LLM to process the user’s requests and generate responses based on the retrieved emails` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1039` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LLMail service includes an assistant that can answer questions based on the users’ emails and perform actions on behalf of the user` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset contains a large number of attack prompts collected as part of the now closed LLMail-Inject: Adaptive Prompt Injection Challenge.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 4155자 ≈ 1039 토큰 (viewer statistics, default/Phase1)

## 이 데이터로 학습한 모델

- [[Horizon-Labs__prompt-injection-guard-base|Horizon-Labs/prompt-injection-guard-base]]
- [[Horizon-Labs__prompt-injection-guard-large|Horizon-Labs/prompt-injection-guard-large]]
- [[Horizon-Labs__prompt-injection-guard-small|Horizon-Labs/prompt-injection-guard-small]]
- [[vllm-sr__Vela-1.0-Encoder-307M-Shield|vllm-sr/Vela-1.0-Encoder-307M-Shield]]
