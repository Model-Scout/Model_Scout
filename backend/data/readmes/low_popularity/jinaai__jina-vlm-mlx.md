---
library_name: mlx
pipeline_tag: image-text-to-text
license: cc-by-nc-4.0
tags:
- mlx
- apple-silicon
- multimodal
- multilingual
- vlm
- vision-language
- qwen3
- siglip2
language:
- en
- zh
- ar
- pt
- ru
- tr
- de
- es
- fr
- it
- ja
- ko
- vi
- th
- id
- hi
- bn
- nl
- pl
- sv
- fi
- da
- "no"
- cs
- el
- he
- uk
- ro
- hu
- multilingual
base_model: jinaai/jina-vlm
base_model_relation: quantized
inference: false
---

# jina-vlm-mlx

Native MLX port of [jina-vlm](https://huggingface.co/jinaai/jina-vlm) for Apple Silicon with 4-bit quantization.

## Model Size

**2.0 GB** (down from 9.2 GB fp32, 79% compression)

### Quantization Strategy

- **4-bit weights** (group_size=64): lm_head, vision encoder, VL connector, language model layers 1-27
- **bfloat16 weights**: Embeddings, layer norms, language model layer 0

## Installation

> [!IMPORTANT]
> jina-vlm support is already merged into mlx-vlm master but not yet released. Until the next release, install from the main branch:

```bash
pip install git+https://github.com/Blaizzy/mlx-vlm.git@main
```

## Usage

```python
from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template
from mlx_vlm.utils import load_config

# Load model
model, processor = load("jinaai/jina-vlm-mlx")
config = load_config("jinaai/jina-vlm-mlx")

# Prepare input
image = ["photo.jpg"]
prompt = "Describe this image."

# Apply chat template
formatted_prompt = apply_chat_template(
    processor, config, prompt, num_images=1
)

# Generate
output = generate(model, processor, formatted_prompt, image, max_tokens=200)
print(output.text)
```

## CLI Usage

```bash
python -m mlx_vlm.generate \
    --model jinaai/jina-vlm-mlx \
    --image photo.jpg \
    --prompt "Describe this image." \
    --max-tokens 200
```

## License

CC BY-NC 4.0. Commercial use: [contact Jina AI](https://jina.ai/contact-sales/).

## Citation

```bibtex
@misc{koukounas2025jinavlm,
    title={Jina-VLM: Small Multilingual Vision Language Model},
    author={Andreas Koukounas and Georgios Mastrapas and Florian Hönicke and Sedigheh Eslami and Guillaume Roncari and Scott Martens and Han Xiao},
    year={2025},
    eprint={2512.04032},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    url={https://arxiv.org/abs/2512.04032},
}
```
