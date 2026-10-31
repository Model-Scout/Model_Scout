---
language:
- ko
license: apache-2.0
task_categories:
- question-answering
tags:
- agent
- benchmark
- tool-use
- korean
---

# Ko-AgentBench

한국어 에이전트 벤치마크 데이터셋

## 데이터 로드

```python
from datasets import load_dataset

# 특정 레벨 로드
dataset = load_dataset("Hugging-Face-KREW/Ko-AgentBench", data_files="L1.json")

# 또는 모든 레벨 로드
dataset = load_dataset("Hugging-Face-KREW/Ko-AgentBench", data_files="*.json")
```

## 레벨

- L1: Single Tool
- L2: Tool Retrieval & Selection  
- L3: Multiple Tools
- L4: Complex Tool Chaining
- L5: Conditional Logic
- L6: State Management
- L7: Multi-step Planning
