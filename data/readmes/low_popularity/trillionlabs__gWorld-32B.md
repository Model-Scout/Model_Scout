---
language:
- en
- ko
license: apache-2.0
pipeline_tag: image-text-to-text
library_name: transformers
base_model: Qwen/Qwen3-VL-32B
datasets:
- trillionlabs/MWMBench
tags:
- gui-world-model
- world-model
- gui-agent
- mobile-agent
- android
- html
- code-generation
- next-ui-prediction
- arxiv:2602.01576
---

# gWorld-32B 🌍📱 

**gWorld** (GuiWorld) is an open-weight **GUI world model** for **mobile GUI agents**: a single vision-language model (8B / 32B) that predicts the **next screen** after a user action by generating **renderable HTML/web code** instead of pixels. First released February 2, 2026 by Trillion Labs; accepted to ICML 2026.

[![ICML 2026](https://img.shields.io/badge/ICML-2026-2563eb)](https://trillionlabs-gworld.github.io/) [![arXiv](https://img.shields.io/badge/arXiv-2602.01576-b31b1b)](https://arxiv.org/abs/2602.01576)

This is **gWorld-32B**. Paper: [Generative Visual Code Mobile World Models](https://huggingface.co/papers/2602.01576) (arxiv:2602.01576, ICML 2026). Benchmark: [MWMBench](https://huggingface.co/datasets/trillionlabs/MWMBench). Collection: [GuiWorld](https://huggingface.co/collections/trillionlabs/guiworld-697c3bf43a0df8172bbcd56d).

<p align="center">
<picture>
  <img src="https://github.com/trillion-labs/gWorld/blob/main/trillion.jpg?raw=true", style="width: 40%;">
</picture>
</p>

<div align="center">

📄 [Paper](https://arxiv.org/abs/2602.01576) 🎬 [Demo](https://trillionlabs-gworld.github.io/) 👨🏻‍💻 [Code](https://github.com/trillion-labs/gWorld)

🎉 **News (May, 2026):** gWorld has been **accepted to ICML 2026**! See you in Seoul. 🇰🇷

</div>

gWorld-32B predicts the **next GUI state as executable web code** rather than pixels, which keeps text legible and layouts structurally accurate and avoids the hallucination and legibility issues common in pixel-generation models.


<p align="center">
<picture>
  <img src="https://github.com/trillion-labs/gWorld/blob/main/figure1.png?raw=true", style="width: 85%;">
</picture>
</p>


## Model Summary
- **Architecture:** Based on `Qwen3-VL-32B`
- **Task:** Action-conditioned next-state prediction for mobile GUIs
- **Input:** Current screenshot + Action
- **Output:** Reasoning + Renderable HTML 

## Key Features

### 1. New Pareto Frontier

<p align="center">
<picture>
  <img src="https://github.com/trillion-labs/gWorld/blob/main/pareto.png?raw=true", style="width: 60%;">
</picture>
</p>

**gWorld-32B** establishes a new **Pareto frontier** in the trade-off between model size and GUI world modeling accuracy. 
- **Efficiency:** Outperforms frontier models up to **12.6x larger** (e.g., `Llama 4 402B-A17B`) on GUI-specific benchmarks.
- **Accuracy:** Achieves a **+27.1% gain** in Instruction Accuracy (IAcc.) over the base Qwen3-VL model.
- **Zero-Shot Generalization:** Demonstrated high performance on out-of-distribution benchmarks like AndroidWorld and KApps (Korean).

### 2. Action Input & Operations
The model treats the mobile interface as a coordinate space and predicts how that space changes based on user input.
- **Coordinate Space:** Operates on a normalized **[0, 1000]** scale.
- **Logic:** It generates a "Next State Reasoning" block before the code to ensure the visual transition logically follows the intent of the action.
- **Example Actions:** - `{"action_type": "TAP", "coordinates": [512, 890]}` or `{"action_type": "TYPE", "text": "gWorld is a generative code mobile world model"}`

### 3. Visual Code Rendering
By outputting HTML/CSS, gWorld ensures that text remains perfectly sharp and layouts are responsive.
- **High Renderability:** <1% render failure rate.
- **Speed:** Rendering via Playwright takes ~0.3s, significantly faster than multi-step diffusion pipelines.

## Sample Usage

### Inference with vLLM

To use the model, you can use the following snippet from the official repository:

```python
from vllm import LLM, SamplingParams
from transformers import AutoProcessor
from PIL import Image

# Model configuration
MODEL_PATH = "trillionlabs/gWorld-32B"
BASE_MODEL = "Qwen/Qwen3-VL-32B"

# Image processing settings
MM_PROCESSOR_KWARGS = {
    "max_pixels": 4233600,
    "min_pixels": 3136,
}

# Load model
llm = LLM(
    model=MODEL_PATH,
    tokenizer=BASE_MODEL,
    tensor_parallel_size=8,
    gpu_memory_utilization=0.9,
    max_model_len=19384,
    trust_remote_code=True,
    mm_processor_kwargs=MM_PROCESSOR_KWARGS,
    enable_chunked_prefill=True,
    max_num_batched_tokens=16384,
)

# Load processor for chat template
processor = AutoProcessor.from_pretrained(BASE_MODEL, trust_remote_code=True)

# Prepare input
image = Image.open("screenshot.png") # Replace with your screenshot
if image.mode != 'RGB':
    image = image.convert('RGB')

action = '{"action_type": "TAP", "coordinates": [512, 890]}'

# World model prompt template
user_content = f"""You are an expert mobile UI World Model that can accurately predict the next state given an action.
Given a screenshot of a mobile interface and an action, you must generate clean, responsive HTML code that represents the state of the interface AFTER the action is performed.
First generate reasoning about what the next state should look like based on the action.
Afterwards, generate the HTML code representing the next state that logically follows the action.
You will render this HTML in a mobile viewport to see how similar it looks and acts like the mobile screenshot.

Requirements:
1. Provide reasoning about what the next state should look like based on the action
2. Generate complete, valid HTML5 code
3. Choose between using inline CSS and utility classes from Bootstrap, Tailwind CSS, or MUI for styling, depending on which option generates the closest code to the screenshot.
4. Use mobile-first design principles matching screenshot dimensions.
5. For images, use inline SVG placeholders with explicit width and height attributes that match the approximate dimensions from the screenshot. Matching the approximate color is also good.
6. Use modern web standards and best practices
7. Return ONLY the HTML code, no explanations or markdown formatting
8. The generated HTML should render properly in a mobile viewport.
9. Generated HTML should look like the screen that logically follows the current screen and the action.

Action:
{action}

Output format:
# Next State Reasoning: <your reasoning about what the next state should look like>
# HTML: <valid_html_code>

Generate the next state reasoning and the next state in html:"""

# Build messages
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": user_content},
        ],
    }
]

# Apply chat template
prompt = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

# Generation parameters
sampling_params = SamplingParams(
    max_tokens=15000,
    temperature=0,
    seed=42,
    top_p=1.0,
)

# Generate
outputs = llm.generate(
    [{"prompt": prompt, "multi_modal_data": {"image": image}}],
    sampling_params=sampling_params
)

print(outputs[0].outputs[0].text)
```

## License and Contact
This model is licensed under the Apache License 2.0. For inquiries, please contact: info@trillionlabs.co

## Citation
```bibtex
@inproceedings{koh2026gworld,
  title     = {Generative Visual Code Mobile World Models},
  author    = {Koh, Woosung and Han, Sungjun and Lee, Segyu and Yun, Se-Young and Shin, Jamin},
  booktitle = {International Conference on Machine Learning (ICML)},
  year      = {2026},
  note      = {arXiv:2602.01576}
}
```
