---
license: cc0-1.0
language:
- ko
- en
tags:
- prompt-engineering
- chatgpt
- gemini
- claude
- copilot
- korean
task_categories:
- text-generation
- question-answering
---

# Korean AI Prompt Style Dataset

같은 질문에 대해 ChatGPT, Gemini, Claude, Copilot 각각에 최적화된 프롬프트 스타일을 비교한 한국어 데이터셋입니다.

A Korean dataset comparing optimized prompt styles for ChatGPT, Gemini, Claude, and Copilot on identical questions.

## 📌 데이터 구조 / Data Structure

\`\`\`json
{
  "instruction": "질문 내용 / user question",
  "input": "target: chatgpt / gemini / claude / copilot",
  "output": "해당 AI에 최적화된 프롬프트 / optimized prompt for the target AI"
}
\`\`\`

## 📊 데이터 현황 / Stats

- 총 869개 샘플 / 869 samples
- 4개 AI 모델 / 4 AI models (ChatGPT, Gemini, Claude, Copilot)
- 백엔드, DB, 보안 등 다양한 주제 / Topics: backend, database, security, and more

## 💡 활용 방법 / Use Cases

- AI별 프롬프트 스타일 연구 / Research on prompt style differences across LLMs
- LLM 파인튜닝 / Fine-tuning language models
- 프롬프트 엔지니어링 학습 / Prompt engineering education
