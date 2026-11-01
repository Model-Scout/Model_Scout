---
base_model: vllm-sr/mmbert-32k-yarn
license: apache-2.0
language:
- en
- de
- fr
- es
- zh
- ja
- ru
- ar
- ko
- pt
tags:
- modality-routing
- text-classification
- mom
- vllm-semantic-router
- mixture-of-models
- modernbert
datasets:
- Gustavosta/Stable-Diffusion-Prompts
- FredZhang7/stable-diffusion-prompts-2.47M
- nateraw/parti-prompts
- fal/image-generation-prompts
- OpenAssistant/oasst2
- tatsu-lab/alpaca
- databricks/databricks-dolly-15k
- stingning/ultrachat
- allenai/WildChat
- mqliu/InterleavedBench
metrics:
- accuracy
- f1
- precision
- recall
pipeline_tag: text-classification
model-index:
- name: mmbert32k-modality-router-merged
  results:
  - task:
      type: text-classification
      name: Modality Routing
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9686
    - name: F1 (weighted)
      type: f1
      value: 0.9686
    - name: F1 AR
      type: f1
      value: 0.9617
    - name: F1 DIFFUSION
      type: f1
      value: 0.9765
    - name: F1 BOTH
      type: f1
      value: 0.9669
---

# Modality Router (Merged) - Smart Output Modality Selection

**Part of the [MoM (Mixture of Models)](https://huggingface.co/vllm-sr) family** for [vLLM Semantic Router](https://vllm-semantic-router.com).

This is the **merged** (ready-to-use) version of [mmbert32k-modality-router-lora](https://huggingface.co/vllm-sr/mmbert32k-modality-router-lora). LoRA weights have been merged into the [mmbert-32k-yarn](https://huggingface.co/vllm-sr/mmbert-32k-yarn) base model for easy deployment without the PEFT dependency.

A text classifier based on ModernBERT (307M params, 32K context, 1800+ languages) that determines the appropriate response modality for user prompts:

| Label | Description | Routed To | Example |
|-------|-------------|-----------|---------|
| **AR** | Text-only response | Autoregressive LLM (e.g., Llama, Qwen) | *"What is the capital of France?"* |
| **DIFFUSION** | Image generation | Diffusion model (e.g., Flux, SDXL) | *"A cyberpunk city at night, neon lights"* |
| **BOTH** | Text + image response | Both AR + Diffusion pipeline | *"Explain photosynthesis and show a diagram"* |

## Quick Start

### Pipeline API (simplest)

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="vllm-sr/mmbert32k-modality-router-merged",
)

results = classifier([
    "What are the benefits of exercise?",
    "A serene Japanese garden with cherry blossoms, watercolor style",
    "Explain how neural networks work and generate a diagram",
])

for r in results:
    print(f"{r['label']}: {r['score']:.3f}")
# AR: 0.995
# DIFFUSION: 0.717
# BOTH: 0.978
```

### Direct Model Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained(
    "vllm-sr/mmbert32k-modality-router-merged"
)
tokenizer = AutoTokenizer.from_pretrained(
    "vllm-sr/mmbert32k-modality-router-merged"
)

prompts = [
    "Summarize the key points of quantum computing",
    "portrait of a woman in renaissance style, oil painting, dramatic lighting",
    "Write a blog post about climate change and include relevant charts",
]

model.eval()
inputs = tokenizer(prompts, return_tensors="pt", truncation=True, padding=True, max_length=512)
with torch.no_grad():
    outputs = model(**inputs)

predictions = torch.argmax(outputs.logits, dim=-1)
labels = model.config.id2label
for prompt, pred_id in zip(prompts, predictions):
    print(f"{labels[pred_id.item()]}: {prompt[:60]}...")
# AR: Summarize the key points of quantum computing...
# DIFFUSION: portrait of a woman in renaissance style, oil painting, d...
# BOTH: Write a blog post about climate change and include releva...
```

### Integration with vLLM Semantic Router

```python
# Example: Route requests to different model backends
def route_request(prompt: str, classifier) -> str:
    """Route a user prompt to the appropriate model backend."""
    result = classifier(prompt)[0]
    modality = result["label"]
    confidence = result["score"]

    if modality == "AR":
        return call_llm_backend(prompt)        # e.g., Llama, Qwen
    elif modality == "DIFFUSION":
        return call_diffusion_backend(prompt)   # e.g., Flux, SDXL
    else:  # BOTH
        text = call_llm_backend(prompt)
        image = call_diffusion_backend(prompt)
        return combine_response(text, image)
```

### ONNX Runtime (for production latency)

The base model ([mmbert-32k-yarn](https://huggingface.co/vllm-sr/mmbert-32k-yarn)) supports ONNX export for sub-5ms inference on AMD MI300X GPUs.

## Model Details

| Property | Value |
|----------|-------|
| **Base model** | [`vllm-sr/mmbert-32k-yarn`](https://huggingface.co/vllm-sr/mmbert-32k-yarn) (307M params) |
| **Architecture** | ModernBERT + YaRN RoPE scaling |
| **Context length** | 32,768 tokens |
| **Languages** | 1800+ (Gemma 2 tokenizer, 256K vocab) |
| **Fine-tuning** | LoRA (rank=16, alpha=32) merged into base weights |
| **Classes** | 3 (AR, DIFFUSION, BOTH) |
| **Model size** | ~1.23 GB (safetensors) |

### Training Configuration

| Parameter | Value |
|-----------|-------|
| Epochs | 10 |
| Batch size | 32 |
| Learning rate | 2e-5 |
| Weight decay | 0.15 (adaptive) |
| Loss function | Focal Loss (gamma=2.0) |
| Class weighting | Inverse-frequency (sqrt-dampened) |
| Minority oversampling | Yes |
| LoRA target modules | `attn.Wqkv`, `attn.Wo`, `mlp.Wi`, `mlp.Wo` |
| Hardware | AMD Instinct MI300X (192GB VRAM) |
| Training time | ~2 minutes |

## Training Data

Trained on a curated combination of **10 public datasets** covering diverse prompt styles:

### DIFFUSION class
- [Gustavosta/Stable-Diffusion-Prompts](https://huggingface.co/datasets/Gustavosta/Stable-Diffusion-Prompts) - 80K curated SD prompts
- [FredZhang7/stable-diffusion-prompts-2.47M](https://huggingface.co/datasets/FredZhang7/stable-diffusion-prompts-2.47M) - 2.47M SD prompts
- [nateraw/parti-prompts](https://huggingface.co/datasets/nateraw/parti-prompts) - Google Parti benchmark
- [fal/image-generation-prompts](https://huggingface.co/datasets/fal/image-generation-prompts) - Diverse image prompts
- [allenai/WildChat](https://huggingface.co/datasets/allenai/WildChat) (mined) - Real user image requests

### AR class
- [OpenAssistant/oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2) - 135K instruction conversations
- [tatsu-lab/alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca) - 52K Stanford instructions
- [databricks/databricks-dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) - 15K categorized instructions
- [stingning/ultrachat](https://huggingface.co/datasets/stingning/ultrachat) - 1.5M multi-turn conversations
- [allenai/WildChat](https://huggingface.co/datasets/allenai/WildChat) (mined) - Real user text prompts

### BOTH class
- [mqliu/InterleavedBench](https://huggingface.co/datasets/mqliu/InterleavedBench) - Gold-standard interleaved text+image (EMNLP 2024)
- [allenai/WildChat](https://huggingface.co/datasets/allenai/WildChat) (mined) - Real user multimodal prompts
- Curated seed examples (40+ across diverse domains)

## Evaluation Results

| Metric | Value |
|--------|-------|
| **Accuracy** | **0.9686** |
| **F1 (weighted)** | **0.9686** |
| Eval Loss | 0.0435 |

### Per-class Performance

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| **AR** | 0.956 | 0.967 | 0.962 |
| **DIFFUSION** | 0.974 | 0.979 | 0.977 |
| **BOTH** | 0.983 | 0.951 | 0.967 |

### Example Classifications

| Prompt | Predicted | Confidence |
|--------|-----------|------------|
| "What is the capital of France?" | AR | 0.995 |
| "A serene Japanese garden with cherry blossoms, watercolor style" | DIFFUSION | 0.717 |
| "Explain how neural networks work and generate a diagram" | BOTH | 0.978 |
| "Write me a poem about autumn" | AR | 0.864 |
| "cyberpunk cityscape, 4k, artstation, trending" | DIFFUSION | 0.971 |
| "Create a travel guide for Tokyo with photos of each location" | BOTH | 0.935 |

## Intended Use

This model is designed for **routing LLM requests** in multi-model serving systems:

- **Smart Output Modality Selection**: Automatically determine whether a user query needs text, image, or both
- **Automatic Paradigm Routing**: Route requests to the right backend (AR LLM vs Diffusion model vs both)
- **Cost Optimization**: Avoid sending simple text queries to expensive image generation pipelines
- **Latency Reduction**: Skip unnecessary model invocations by predicting the needed output type upfront

### Limitations

- Single-turn prompt classification only (no conversation context)
- Primarily trained on English data (multilingual capability inherited from base model)
- Not designed for content moderation or safety classification

## Related Models

| Model | Description |
|-------|-------------|
| [mmbert32k-modality-router-lora](https://huggingface.co/vllm-sr/mmbert32k-modality-router-lora) | LoRA adapter version (for further fine-tuning) |
| [mmbert-32k-yarn](https://huggingface.co/vllm-sr/mmbert-32k-yarn) | Base model (307M, 32K context, 1800+ languages) |
| [mmbert32k-intent-classifier-merged](https://huggingface.co/vllm-sr/mmbert32k-intent-classifier-merged) | Intent classifier (MoM family) |
| [mmbert32k-jailbreak-detector-merged](https://huggingface.co/vllm-sr/mmbert32k-jailbreak-detector-merged) | Jailbreak detector (MoM family) |
| [mmbert32k-pii-detector-merged](https://huggingface.co/vllm-sr/mmbert32k-pii-detector-merged) | PII detector (MoM family) |

## Citation

```bibtex
@misc{modality-router-2025,
  title={Modality Router: Smart Output Modality Selection for Multi-Model Serving},
  author={vLLM Semantic Router Team},
  year={2025},
  url={https://huggingface.co/vllm-sr/mmbert32k-modality-router-merged}
}
```

## Framework Versions

- Transformers: 4.57.6
- PyTorch: 2.9.1
- Safetensors: 0.5.x
- Python: 3.12
