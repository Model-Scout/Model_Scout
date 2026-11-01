---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
- en
- ja
- zh
- pl
- de
- pt
- es
- fr
- it
- ru
- vi
size_categories:
- 1K<n<10K
---

# TRUEBench: A Benchmark for Assessing LLMs as Human Job Productivity Assistants
TRUEBench is a benchmark introduced by Samsung Research to evaluate the performance of large language models (LLMs) as human job assistants which consists of over 2,400 realistic and challenging samples. 
To assess performance in real-world applications, TRUEBench includes diverse dialog scenarios and language conditions.

## Main Features

- **Multilinguality**: The user instructions are written in a total of 12 languages, and TRUEBench includes numerous samples containing diverse linguistic constraints.

- **Implicit Constraints**: In real-world scenarios, not all user intents may be explicitly stated in the instructions. TRUEBench includes samples with implicit constraints and is designed to evaluate those constraints through checklist-based evaluation.

- **Multi-Turn**: In multi-turn conversations, context can shift dynamically, and there may be constraints that require referencing previous conversational context. TRUEBench is designed to reflect diverse multi-turn conversation scenarios.

## Task Categories
- Content Generation
- Editing
- Data Analysis
- Reasoning
- Hallucination
- Safety
- Repetition
- Summarization
- Translation
- Multi-Turn

## Languages
- Korean (KO)
- English (EN)
- Japanese (JA)
- Chinese (ZH)
- Polish (PL)
- German (DE)
- Portuguese (PT)
- Spanish (ES)
- French (FR)
- Italian (IT)
- Russian (RU)
- Vietnamese (VI)

## Data Structure
```python
{
  "index": int,
  "category": str,
  "sub_category": str,
  "turns": int,
  "input": List[str],
  "criteria": List[List[str]],
}
```