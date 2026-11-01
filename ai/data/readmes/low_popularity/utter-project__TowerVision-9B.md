---
library_name: transformers
tags:
- multimodal
- multilingual
- vlm
- translation
language:
- en
- de
- nl
- es
- fr
- pt
- uk
- hi
- zh
- ru
- cs
- ko
- ja
- it
- pl
- ro
- nb
- nn
base_model:
- Unbabel/Tower-Plus-9B
pipeline_tag: image-text-to-text
license: cc-by-nc-sa-4.0
---

# Model Card for TowerVision

<p align="left">
<img src="Tower.png" alt="TowerVision Logo" width="200">
</p>

TowerVision is a family of open-source multilingual vision-language models with strong capabilities optimized for a variety of vision-language use cases, including image captioning, visual understanding, summarization, question answering, and more. **TowerVision excels particularly in multimodal multilingual translation benchmarks and culturally-aware tasks**, demonstrating exceptional performance across **20 languages and dialects**.

This model card covers the TowerVision family, including the 2B and 9B parameter versions, both in their instruct-tuned (it) and pretrained (pt) variants, with the latter not undergoing instruction tuning.

- **Model Family**: TowerVision (2B, 9B variants)
- **Context length**: 8192 tokens
- **Languages**: 20+ languages including European, Asian, and other language families

<span style="font-size: 1.2em;"><strong>🌟 Try TowerVision</strong></span>: [Project Page](https://guilhermeviveiros.github.io/TowerVision.io/) | [Code Repository](https://github.com/GuilhermeViveiros/LLaVA-NeXT)

## Available Models

<p align="left">

| Model | Parameters | HF Link |
|-------|------------|---------|
| TowerVision-2B | 2B | [🤗 utter-project/TowerVision-2B](https://huggingface.co/utter-project/TowerVision-2B)
| TowerVision-9B | 9B | [🤗 utter-project/TowerVision-9B](https://huggingface.co/utter-project/TowerVision-9B)

## How to Use TowerVision

When using the model, make sure your prompt is formated correctly! 
Also, we recommend using **bfloat16** rather than **fp32/16**

### Quick Start with Transformers

<details open>
<summary>Click to expand/collapse code</summary>

```python
from transformers import (
    LlavaNextProcessor,
    LlavaNextForConditionalGeneration
)
import requests
from PIL import Image

model_id = "utter-project/TowerVision-2B"  # or any other variant

def prepare_prompt(query):
    conversation = [
        {
            "role": "user", 
            "content": f"<image>\n{query}"
        }
    ]
    
    # Format message with the towervision chat template
    prompt = processor.apply_chat_template(
        conversation, 
        tokenize=False,
        add_generation_prompt=True
    )
    
    return prompt

# we recommend using "bfloat16" as torch_dtype
kwargs = {
    "torch_dtype": "bfloat16",
    "device_map": "auto",
}
processor = LlavaNextProcessor.from_pretrained(model_id)
model = LlavaNextForConditionalGeneration.from_pretrained(model_id, **kwargs)

# img url
img_url = "https://cms.mistral.ai/assets/a10b924e-56b3-4359-bf6c-571107811c8f"
image = Image.open(requests.get(img_url, stream=True).raw)

# Multilingual prompts - TowerVision supports 20+ languages!
prompt = prepare_prompt("Is this person really big, or is this building just super small?")

# Prepare inputs
inputs = processor(
    text=prompt, images=image, return_tensors="pt"
).to(model.device)

# Generate response ids
gen_tokens = model.generate(**inputs, max_new_tokens=512)
# Decode response
print(processor.tokenizer.decode(gen_tokens[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

</details>

### Batch Inference with Transformers

For processing multiple images and prompts simultaneously:

<details>
<summary>Click to expand/collapse code</summary>

```python
def prepare_prompts(queries):
    prompts = []
    for query in queries:
        conversation = [
            {
                "role": "user", 
                "content": f"<image>\n{query}"
            }
        ]
        
        # Format message with the towervision chat template
        prompt = processor.apply_chat_template(
            conversation, 
            tokenize=False,
            add_generation_prompt=True
        )
        prompts.append(prompt)
    return prompts

# we recommend using "bfloat16" as torch_dtype
kwargs = {
    "torch_dtype": "bfloat16",
    "device_map": "auto",
}
processor = LlavaNextProcessor.from_pretrained(model_id)
model = LlavaNextForConditionalGeneration.from_pretrained(model_id, **kwargs)

# Sample images and queries for batch processing
img_urls = [
    "https://cms.mistral.ai/assets/a10b924e-56b3-4359-bf6c-571107811c8f",
    "https://cms.mistral.ai/assets/a10b924e-56b3-4359-bf6c-571107811c8f",
]

queries = [
    "Is this person really big, or is this building just super small?",
    "Where was this photo taken?"
]

# Load images
images = []
for url in img_urls[:batch_size]:
    image = Image.open(requests.get(url, stream=True).raw)
    images.append(image)

# Prepare prompts
prompts = prepare_prompts(queries[:batch_size])

# Prepare batch inputs
inputs = processor(
    text=prompts, 
    images=images, 
    return_tensors="pt",
    padding=True
).to(model.device)

# Generate response ids for batch
gen_tokens = model.generate(**inputs, max_new_tokens=512, do_sample=False)

# Decode responses
print(f"Batch processing {len(images)} images:")
print("-" * 50)

for i in range(len(images)):
    input_length = inputs.input_ids[i].shape[0]
    response = processor.tokenizer.decode(
        gen_tokens[i][input_length:], 
        skip_special_tokens=True
    )
    print(f"Response: {response}")
    print("-" * 50)
```

</details>

### Pipeline Usage

<summary>Click to expand/collapse code</summary>
<details>

```python
from transformers import pipeline
from PIL import Image
import requests


pipe = pipeline(
    model="utter-project/TowerVision-9B", 
    task="image-text-to-text", 
    device_map="auto",
    dtype="bfloat16"
)

def prepare_prompt(query):
    conversation = [
        {
            "role": "user", 
            "content": f"<image>\n{query}"
        }
    ]
    
    # Format message with the towervision chat template
    return pipe.processor.apply_chat_template(
        conversation, 
        tokenize=False,
        add_generation_prompt=True
    )
    
    
img_url = "https://cms.mistral.ai/assets/a10b924e-56b3-4359-bf6c-571107811c8f"
image = Image.open(requests.get(img_url, stream=True).raw)
text = prepare_prompt("Is this person really big, or is this building just super small?")

outputs = pipe(text=text, images=image, max_new_tokens=300, return_full_text=False)
print(outputs)
```

</details>

## Model Details

**Input**: Model accepts input text and images.

**Output**: Model generates text in multiple languages.

**Model Architecture**: TowerVision uses a multilingual language model based on [Tower-Plus](https://huggingface.co/Unbabel/Tower-Plus-9B) (2B and 9B parameters), paired with [SigLIP2-patch14-384](https://huggingface.co/google/siglip2-so400m-patch14-384) vision encoder through a multimodal adapter for vision-language understanding.

**Recommended Precision**: We recommend using `bfloat16` precision for optimal performance and memory efficiency when running TowerVision models.

**Languages Covered**: The model has been trained on **20 languages and dialects**:
- **European languages**: English, German, Dutch, Spanish, French, Portuguese, Italian, Polish, Czech, Romanian, Norwegian (Bokmål & Nynorsk)
- **Asian languages**: Chinese (Simplified & Traditional), Japanese, Korean, Hindi  
- **Other languages**: Russian, Ukrainian

**Key Strengths**:
- **🏆 Exceptional performance on culturally-aware benchmarks** with deep understanding of cultural contexts and visual nuances
- **🌐 State-of-the-art results on multimodal multilingual translation benchmarks**, enabling seamless cross-lingual visual communication
- **📊 Strong cross-lingual transfer capabilities** across diverse vision-language tasks

## Training Data

TowerVision models are trained on **VisionBlocks**, a comprehensive multilingual vision-language dataset comprising **6.31M samples** across diverse categories:

| Dataset | Samples | HF Link |  |
|---------|---------|---------|-------|
| VisionBlocks | 6.31M | [🤗 utter-project/VisionBlocks](https://huggingface.co/datasets/utter-project/VisionBlocks) | Coming Soon |

### Dataset Statistics
- **Total samples**: 6.31M
- **Created by our team**: 1.21M samples (~19%)
- **Human-collected/external**: 5.10M samples (~81%)

### Dataset Composition Overview

**VisionBlocks** contains samples across multiple categories with both English-only (63.1%) and multilingual (36.9%) data:

- **Chart/Plot Reasoning**: DVQA, ChartQA, PlotQA, TabMWP (~405K samples)
- **General VQA**: VQAv2, RLAIF-4V (~488K samples) 
- **Document VQA**: DocVQA, TextVQA, ST-VQA, PixMo-Docs (~46K samples)
- **Reasoning/Knowledge**: A-OKVQA, OKVQA, AI2D, ScienceQA (~29K samples)
- **Multilingual/Cultural**: Pangea-Cultural, Pangea-Multi, PixMo-Cap-Translated, CulturalGround datasets (~1.6M samples)
- **Specialized VQA**: IconQA, InfographicVQA, Stratos (~34K samples)
- **Counting/Math**: TallyQA, PixMo-Count (~107K samples)
- **Vision/Text**: VBlocks-PixMo collections, EuroBlocks-SFT (~2.2M samples)
- **Video/Text**: LLaVA-Video collections (~1.4M samples)

**Collection Types**: Human-annotated, synthetically generated, and professionally translated data ensuring high quality and cultural diversity across 20+ languages.

## Evaluation

All evaluations were conducted using [lmms_eval](https://github.com/EvolvingLMMs-Lab/lmms-eval).

### Multiple Purpose Multimodal Benchmarks

TowerVision demonstrates strong performance across diverse multimodal evaluation benchmarks:

<img src="mc-eval1.png" alt="Multiple Purpose Multimodal Benchmarks Results" width="600">

### Multimodal Multilingual Translation Tasks

TowerVision excels particularly in multimodal multilingual translation benchmarks, demonstrating state-of-the-art cross-lingual visual communication capabilities:

<img src="mc-eval2.png" alt="Multimodal Multilingual Translation Results" width="600">

### Supported Languages Performance

✅ **Fully Supported**: English, German, Dutch, Spanish, French, Portuguese, Italian, Polish, Czech, Romanian, Norwegian, Chinese, Japanese, Korean, Hindi, Russian, Ukrainian

📊 **Benchmark Coverage**: Our models are evaluated across diverse multilingual vision-language tasks, demonstrating strong cross-lingual transfer capabilities and exceptional performance in culturally-aware benchmarks.

## Citation

If you find TowerVision useful in your research, please consider citing the following paper:

```bibtex
@misc{viveiros2025towervisionunderstandingimprovingmultilinguality,
      title={TowerVision: Understanding and Improving Multilinguality in Vision-Language Models}, 
      author={André G. Viveiros and Patrick Fernandes and Saul Santos and Sonal Sannigrahi and Emmanouil Zaranis and Nuno M. Guerreiro and Amin Farajian and Pierre Colombo and Graham Neubig and André F. T. Martins},
      year={2025},
      eprint={2510.21849},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2510.21849}, 
}
```

## Model Card Contact

For errors or additional questions about details in this model card, contact the research team.

## Acknowledgments

TowerVision builds upon the excellent work of:
- **[LLaVA-NeXT](https://github.com/GuilhermeViveiros/LLaVA-NeXT)** for the foundational vision-language architecture
- **[Tower-Plus](https://huggingface.co/Unbabel/Tower-Plus-9B)** language models for multilingual capabilities
- **[SigLIP2](https://huggingface.co/google/siglip2-so400m-patch14-384)** for robust vision encoding
- The broader multilingual NLP and multimodal communities