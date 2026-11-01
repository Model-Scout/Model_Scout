---
language:
  - ko
  - en
license: apache-2.0
tags:
  - function-calling
  - tool-use
  - korean
  - toolbench
source_datasets:
  - OpenBMB/ToolBench
---

# ToolLLaMA Korean Function Calling Dataset

ToolLLaMA 데이터셋을 한국어-영어 하이브리드로 변환한 Function Calling SFT 데이터셋입니다.

## 데이터셋 정보

- **샘플 수**: 1,524개 (한국어 762개 + 영어 762개)
- **포맷**: JSONL (ChatML + XML tags)
- **원본**: [OpenBMB/ToolBench](https://github.com/OpenBMB/ToolBench) (toolllama_G123_dfs_eval.json)

## 번역 전략

| 항목 | 언어 |
|------|------|
| User 질문 | 한국어 |
| Assistant Thought | 한국어 |
| Action (함수명) | 영어 (유지) |
| Action Input (JSON) | 영어 (유지) |
| System Prompt (API 정의) | 영어 (유지) |
| Function 결과 | 영어 (유지) |

## 프롬프트 포맷

```
<|im_start|>system
You are AutoGPT...
<|im_end|>
<|im_start|>user
서울 날씨 알려줘
<|im_end|>
<|im_start|>assistant
<thought>
사용자가 서울 날씨를 요청했습니다. get_weather 함수를 호출하겠습니다.
</thought>
<tool_call>
{"name": "get_weather", "arguments": {"location": "Seoul"}}
</tool_call>
<|im_end|>
```

## 사용법

```python
from datasets import load_dataset

dataset = load_dataset("gyung/toolllama-korean-function-calling")
print(dataset)
```

## 라이센스

Apache 2.0 (원본 ToolBench와 동일)

## 원본 출처

Based on [ToolBench](https://github.com/OpenBMB/ToolBench) by OpenBMB.
