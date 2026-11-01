---
language:
- ko
license: apache-2.0
task_categories:
- question-answering
tags:
- korean
- self-driving
- legal
- dtro
- instruction-tuning
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 213798
    num_examples: 750
---

# 📚 Smoothie-Qwen3-8B-KR-Self-Driving-Legal Dataset v3 (DTRO Style)

**대한민국 자율주행자동차법** 파인튜닝을 위한 750건의 한국어 특화 데이터셋입니다.  
본 데이터셋은 기존 v1, v2 데이터셋 치명적인 **"컨텍스트 소실(Context Forgetting)"** 문제를 해결하기 위해 **DTRO (Direct-To-Response Output) 스타일**로 완전히 재구축되었습니다.

---

## ⚠️ 이전 데이터셋(v1, v2)의 문제점과 한계

기존 Alpaca 양식의 데이터셋은 모델 학습 시 다음과 같은 심각한 부작용을 낳았습니다.

**1. 시스템 프롬프트 포이즈닝 (System Prompt Poisoning)**
```json
// 과거 데이터셋 (문제)
{
  "instruction": "당신은 대한민국의 자율주행자동차법 전문가입니다. 정확한 법적 근거를...",
  "input": "자율주행자동차의 정의는 무엇입니까? [출처: 관련 법령]",
  "output": "자율주행자동차란..."
}
```
* **문제:** 750개의 모든 데이터에 동일한 `instruction(시스템 프롬프트)`이 강제로 주입되었습니다.
* **결과:** 모델 가중치에 이 프롬프트가 과적합(Overfitting)되어, 일상적인 대화(예: "방금 내가 사과 몇 개 먹었지?")에도 "정확한 법적 근거를 바탕으로 답변하겠습니다"라며 맥락을 붕괴시키는 참사가 발생했습니다.

**2. 힌트 의존성 (Hint Dependency)**
* **문제:** `input` 필드에 `[출처: ...]` 태그를 넣음으로써, 모델이 법령을 '이해'하는 것이 아니라 단순히 '출처 태그가 있을 때만' 답변을 복사해오는 수동적 기계로 전락했습니다.

---

## 🛠️ v3 패치: DTRO (Direct-To-Response) 스타일 도입

모델이 "자연스러운 대화 문맥"을 유지하면서도 "법령 지식"을 탑재할 수 있도록, **모든 강제 주입과 힌트를 제거**했습니다.

```json
// v3 데이터셋 (DTRO Style)
{
  "instruction": "자율주행자동차의 정의는 무엇입니까?",
  "output": "자율주행자동차란 운전자 또는 승객의 조작 없이 스스로 운행이 가능한 자동차를 말합니다."
}
```

### ✨ DTRO 데이터셋으로 파인튜닝해야 하는 이유

1. **멀티턴(Multi-turn) 대화 보존:** 시스템 프롬프트 편향이 사라졌기 때문에, 파인튜닝 이후에도 모델이 이전 대화를 기억하고 능동적으로 이어갈 수 있습니다.
2. **범용성 유지:** 베이스 모델(Qwen3 등)이 가진 강력한 한국어 기본 추론 능력을 훼손하지 않고, 순수하게 '지식'만 주입할 수 있습니다.
3. **구조적 답변 유도:** 불필요한 서론(예: "네, 답변 드리겠습니다.") 없이 묻는 말에 빠르고 명확하게 답하도록 학습됩니다.

---

## 📊 데이터셋 구성 (총 750개)

| 분류 | 형태 | 건수 |
|------|------|------|
| **법령 지식 QnA** | 관련 법령 조문을 바탕으로 한 질의응답 | 720건 |
| **적대적 QnA** | 잘못된 전제가 포함된 유도성 질문을 바로잡는 응답 | 30건 |

### 📚 포함된 주요 법령 (13개)
- 자율주행자동차 상용화 촉진 및 지원에 관한 법률
- 자동차관리법
- 도로교통법 (자율주행 관련 특례)
- 자율주행자동차의 안전운행요건 및 시험운행 등에 관한 규정
- 등 관련 하위 법령 (시행령, 시행규칙, 훈령)

---

## 🚀 활용 가이드

본 데이터셋은 `transformers`, `trl` (SFTTrainer) 및 `unsloth` 등 최신 파인튜닝 프레임워크에 즉시 적용할 수 있도록 `json` 포맷으로 제공됩니다.

```python
from datasets import load_dataset
dataset = load_dataset("bluejude10/smoothie-qwen3-8b-kr-self-driving-legal-dataset-v3", split="train")

def format_dtro(example):
    return f"사용자: {example['instruction']}\n어시스턴트: {example['output']}"
```

**⚠️ 주의:** 이 데이터셋으로 파인튜닝 시, `System` 프롬프트는 데이터셋 단축이 아닌 모델 구동 시점(Ollama `Modelfile` 등)에 부여하는 것을 권장합니다.

---

## 🔗 링크
* v3 파인튜닝 모델: [bluejude10/Smoothie-Qwen3-8B-KR-Self-Driving-Legal-v3](https://huggingface.co/bluejude10/Smoothie-Qwen3-8B-KR-Self-Driving-Legal-v3)

## 🔗 실험 챗봇

본 데이터셋을 RAG 벡터 DB에 임베딩하여 구동한 챗봇 전체 코드 (Qdrant DB 사전 구축 포함, 즉시 실행 가능):

👉 [https://github.com/aremany/Legal_RAG_Chatbot_Qdrant_BGE](https://github.com/aremany/Legal_RAG_Chatbot_Qdrant_BGE)
