---
license: apache-2.0
language:
- multilingual
- en
- zh
- ru
- es
- fr
- de
- pt
- it
- ar
- tr
- ja
- ko
- vi
- id
- pl
- uk
- hu
- fa
- hi
- bn
- sw
library_name: transformers
pipeline_tag: text-classification
base_model: jhu-clsp/mmBERT-small
datasets:
- allenai/WildChat-1M
- OpenAssistant/oasst2
- CohereLabs/aya_dataset
tags:
- prompt-classification
- task-classification
- prompt-complexity
- llm-routing
- model-routing
- data-curation
- multilingual
- modernbert
- mmbert
- onnx
- transformers.js
widget:
- text: "Write a Python function that checks whether a string is a palindrome."
  example_title: "Code"
- text: "Résume ce texte en trois phrases : ..."
  example_title: "French summary"
- text: "Explain why the sky is blue to a five-year-old."
  example_title: "Open QA"
---

# Multilingual Prompt Task & Complexity Classifier (small, 141M)

Classifies a **user prompt** sent to an LLM, in English and 100+ other languages:

- **task type** (11, the taxonomy of NVIDIA's prompt classifier): open QA, closed QA, summarization, text generation, code generation, chatbot,
  classification, rewrite, brainstorming, extraction, other;
- **complexity** scores from 0 to 1: creativity, reasoning, contextual knowledge, domain knowledge, constraints, and overall complexity.

Typical uses: routing prompts to a cheaper or stronger model, analysing chat logs, balancing instruction-tuning data.
Built on [mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small), Apache-2.0, ONNX for CPU and the browser (transformers.js) included.
A larger, more accurate version is available as [Horizon-Labs/multilingual-prompt-task-complexity-base](https://huggingface.co/Horizon-Labs/multilingual-prompt-task-complexity-base).

- 17 sigmoid outputs: `task_*` (take the highest as the task type) and the six dimensions. `onnx/model_quantized.onnx` (int8 embeddings, 268 MB) gives the same 0.5 decisions as fp32 on all outputs for 97.5% of 400 test prompts.
- The dimension scores are relative: most prompts score low (training averages: complexity 0.20, reasoning
  0.21, creativity 0.29). Compare prompts with each other, or pick routing thresholds from your own traffic.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Horizon-Labs/multilingual-prompt-task-complexity-small", top_k=None)
s = {d["label"]: d["score"] for d in clf("Écris une fonction Python qui vérifie si une chaîne est un palindrome.")[0]}
task = max((k for k in s if k.startswith("task_")), key=s.get)
print(task, round(s["complexity"], 2), round(s["reasoning"], 2))
```

## Evaluation

There is no public human-labelled multilingual test set for this taxonomy. We held out 4,200 real user prompts from
[WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) (200 in each of 21 languages, never used for training) and labelled them
with an **independent judge**, [google/gemma-4-31b-it](https://huggingface.co/google/gemma-4-31b-it), using the same questions as our teacher.
Task accuracy and macro-F1 compare the top task; the dimensions use Spearman rank correlation.

| model | task accuracy | task macro-F1 | task accuracy, English | task accuracy, mean over languages | creativity | reasoning | contextual knowledge | domain knowledge | constraints | complexity | dimensions: mean Spearman | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **this model** (141M) | 0.793 | 0.735 | 0.830 | 0.793 | 0.769 | 0.713 | 0.591 | 0.661 | 0.878 | 0.681 | 0.716 | multilingual |
| [Horizon-Labs/multilingual-prompt-task-complexity-base](https://huggingface.co/Horizon-Labs/multilingual-prompt-task-complexity-base) (308M) | 0.811 | 0.745 | 0.850 | 0.811 | 0.791 | 0.746 | 0.603 | 0.703 | 0.890 | 0.711 | 0.741 |  |
| [nvidia/prompt-task-and-complexity-classifier](https://huggingface.co/nvidia/prompt-task-and-complexity-classifier) (184M) | 0.459 | 0.318 | 0.655 | 0.459 | 0.478 | 0.250 | 0.230 | 0.385 | 0.648 | 0.347 | 0.390 | English; human-annotated training data, own definitions |
| Qwen3.8-27B, prompted (our teacher, 27B) | 0.856 | 0.807 | 0.915 | 0.856 | 0.856 | 0.830 | 0.688 | 0.808 | 0.915 | 0.819 | 0.819 | for reference |

- The table shows the released checkpoint. Means over 2 training seeds (small: task accuracy .793 / .790, dimension Spearman .716 / .716; base: .811 / .813, .741 / .740).
- Read the comparison with NVIDIA's classifier with care: it was trained on human annotations with its own guidelines, so part of its
  disagreement with our judge is about definitions, not errors; on English prompts the two agree on the task 66% of the time. Outside
  English its agreement drops further, which is the gap this model fills.
- Caveat: the judge and our teacher are both LLMs and agree with each other closely (task 86%), which favours this model on this test.

## Training

- **Prompts**: 172,690 real user prompts in 133 languages: first user messages from WildChat-1M (ODC-BY; only the
  prompt text was used, no metadata; conversations flagged toxic excluded), prompts from [OASST2](https://huggingface.co/datasets/OpenAssistant/oasst2)
  and [Aya](https://huggingface.co/datasets/CohereLabs/aya_dataset) (Apache-2.0). At most 3,000 per language (English 20,000, Chinese 8,000).
- **Labels**: Qwen3.8-27B (Apache-2.0) answered one multiple-choice question (task) and six 0-9 ratings per prompt; the model learns the
  answer probabilities (task) and expected ratings / 9 (dimensions) as soft targets. Checkpoint chosen on 8,589 held-out prompts.
- mmBERT-small, max length 512 tokens. Code: `code/` in this repository.

## Limitations

- Labels come from an LLM, not people, and complexity ratings are subjective. Use the scores for ranking and routing, and validate thresholds on
  your own traffic.
- Only the first 512 tokens of a prompt are read; very long prompts with instructions at the end may be misclassified.
- Not a safety classifier: for harmful or injected prompts see our [content-safety-guard](https://huggingface.co/Horizon-Labs/content-safety-guard-small)
  and [prompt-injection-guard](https://huggingface.co/Horizon-Labs/prompt-injection-guard-small).
