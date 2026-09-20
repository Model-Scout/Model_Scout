---
base_model: llm-semantic-router/mmbert-32k-yarn
license: apache-2.0
language:
- en
- zh
- fr
- es
- multilingual
tags:
- text-classification
- feedback-detection
- user-satisfaction
- transformers
- modernbert
- mmbert
- 32k-context
datasets:
- llm-semantic-router/feedback-detector-dataset
metrics:
- accuracy
- f1
pipeline_tag: text-classification
model-index:
- name: mmbert32k-feedback-detector-merged
  results:
  - task:
      type: text-classification
      name: User Feedback Classification
    dataset:
      name: feedback-detector-dataset
      type: llm-semantic-router/feedback-detector-dataset
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9883
    - name: F1 (macro)
      type: f1
      value: 0.9824
---

# mmBERT-32K Feedback Detector (Merged)

A 4-class user feedback classifier based on [mmbert-32k-yarn](https://huggingface.co/llm-semantic-router/mmbert-32k-yarn). This is the **merged** version with LoRA weights integrated - no PEFT library required.

## Model Description

This model classifies user messages into 4 feedback categories to help conversational AI systems understand user satisfaction:

| Label | ID | Description |
|-------|:--:|-------------|
| **SAT** | 0 | User is satisfied with the response |
| **NEED_CLARIFICATION** | 1 | User needs more explanation or details |
| **WRONG_ANSWER** | 2 | User indicates the response was incorrect |
| **WANT_DIFFERENT** | 3 | User wants an alternative approach/answer |

## Performance

**Validation Results (2,985 samples):**

| Metric | Value |
|--------|-------|
| **Accuracy** | **98.83%** |
| **F1 (macro)** | **98.24%** |
| **F1 (weighted)** | **98.83%** |

**Per-Class Performance:**

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| SAT | 1.0000 | 1.0000 | 1.0000 | 1,491 |
| NEED_CLARIFICATION | 0.9980 | 0.9980 | 0.9980 | 498 |
| WRONG_ANSWER | 0.9604 | 0.9739 | 0.9671 | 498 |
| WANT_DIFFERENT | 0.9715 | 0.9578 | 0.9646 | 498 |

## Quick Start

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained(
    "llm-semantic-router/mmbert32k-feedback-detector-merged"
)
tokenizer = AutoTokenizer.from_pretrained(
    "llm-semantic-router/mmbert32k-feedback-detector-merged"
)
model.eval()

# Label mapping
labels = ["SAT", "NEED_CLARIFICATION", "WRONG_ANSWER", "WANT_DIFFERENT"]

# Example inference
texts = [
    "Thank you, that's exactly what I needed!",
    "I don't understand, can you explain more?",
    "That's incorrect, the answer should be different.",
    "Can you give me another approach?",
]

for text in texts:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    
    probs = torch.softmax(outputs.logits, dim=-1)
    pred = outputs.logits.argmax(-1).item()
    conf = probs[0][pred].item()
    
    print(f"{labels[pred]:20} ({conf:.1%}) | {text}")
```

**Output:**
```
SAT                  (81.2%) | Thank you, that's exactly what I needed!
NEED_CLARIFICATION   (100.0%) | I don't understand, can you explain more?
WRONG_ANSWER         (100.0%) | That's incorrect, the answer should be different.
WANT_DIFFERENT       (100.0%) | Can you give me another approach?
```

## Batch Inference

```python
# Efficient batch processing
texts = ["Your text 1", "Your text 2", "Your text 3"]
inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)

with torch.no_grad():
    outputs = model(**inputs)

predictions = outputs.logits.argmax(-1).tolist()
feedback_types = [labels[p] for p in predictions]
```

## Training Details

This model was fine-tuned using LoRA (Low-Rank Adaptation) with the following configuration:

| Parameter | Value |
|-----------|-------|
| Base Model | llm-semantic-router/mmbert-32k-yarn |
| LoRA Rank | 64 |
| LoRA Alpha | 128 |
| Learning Rate | 2e-5 |
| Batch Size | 16 |
| Epochs | 10 (early stopped at ~5.4) |
| Precision | bf16 |

### Training Data

- **Dataset**: [llm-semantic-router/feedback-detector-dataset](https://huggingface.co/datasets/llm-semantic-router/feedback-detector-dataset)
- **Training samples**: 17,896 (balanced)
- **Validation samples**: 2,985

### Hardware

- **GPU**: AMD Instinct MI300X
- **Training Time**: ~10 minutes

## Model Architecture

- **Architecture**: ModernBERT (Sequence Classification)
- **Parameters**: ~321M (base) with merged LoRA weights
- **Max Context**: 32,768 tokens (YaRN-scaled RoPE)
- **Hidden Size**: 768
- **Layers**: 22
- **Attention Heads**: 12

## Multilingual Support

Supports 1800+ languages via Glot500 tokenizer. Best performance on:
- English (primary)
- Chinese
- French  
- Spanish

## Use Cases

- **Conversational AI**: Detect user satisfaction in chatbots
- **Customer Support**: Route conversations based on feedback type
- **Quality Monitoring**: Track user satisfaction trends
- **Dialog Systems**: Trigger clarification or correction flows

## Comparison: LoRA vs Merged

| Version | Size | Requires PEFT | Use Case |
|---------|------|---------------|----------|
| [LoRA](https://huggingface.co/llm-semantic-router/mmbert32k-feedback-detector-lora) | ~54MB | Yes | Fine-tuning, research |
| **Merged** (this) | ~615MB | No | Production, inference |

## Citation

```bibtex
@misc{mmbert32k-feedback-detector,
  title={mmBERT-32K Feedback Detector},
  author={LLM Semantic Router Team},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/llm-semantic-router/mmbert32k-feedback-detector-merged}
}
```

## License

Apache 2.0
