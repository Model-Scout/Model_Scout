---
license: apache-2.0
base_model: openbmb/MiniCPM-V-4.7-35B-A3B
base_model_relation: quantized
library_name: mlx
pipeline_tag: text-generation
language:
  - zh
  - en
  - de
  - ja
  - ko
  - fr
  - es
  - it
  - pt
  - ru
tags:
  - mlx
  - moe
  - gptq
  - 3-bit
  - expert-pruning
  - reap
  - hadamard
  - minicpm-v
---

# MiniCPM-V-4.7-35B-A3B-REAP192-GPTQ3-MLX

This is a smaller, text-only version of [openbmb/MiniCPM-V-4.7-35B-A3B](https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B) for Apple Silicon Macs. It is about 11 GB on disk and uses about 12 GB of memory when it runs.

We made it for our own daily work: translation between major languages, and polishing of Chinese and English text. We tuned the pruning and the quantization on these tasks. On these tasks, we found no clear quality loss compared with the full model. We did not test code, tool use, math or images.

## What we changed

- **Experts:** Each layer keeps 192 of its 256 routed experts. We selected them with REAP on our translation and polish prompts.
- **Quantization:** The experts are 3-bit GPTQ in a Hadamard-rotated basis. Most other layers are 4-bit. The router is 8-bit.
- **Vision:** We removed the vision tower. The model accepts text only.
- **Tokenizer:** The tokenizer is the same as in the base model.

## Requirements

- An Apple Silicon Mac (M1 or newer) with 24 GB of memory or more. Very long inputs need more memory.
- Python 3.10 or newer.
- MLX. This checkpoint does not run in llama.cpp, Ollama, vLLM, SGLang or LM Studio.

## How to run

1. Install the packages. We tested these versions:

   ```bash
   pip install "mlx==0.32.3" "mlx-lm==0.32.0" "transformers>=5.18" "huggingface_hub[cli]"
   ```

2. Download the model into a local folder:

   ```bash
   hf download yipengsun/MiniCPM-V-4.7-35B-A3B-REAP192-GPTQ3-MLX --local-dir minicpm-reap192
   cd minicpm-reap192
   ```

3. Save this script as `chat.py` in the same folder, then run `python chat.py`:

   ```python
   from load_hadamard import load
   from mlx_lm import generate

   model, tokenizer = load(".")

   messages = [
       {"role": "user", "content": "Translate into German: The meeting moved to Thursday."}
   ]
   prompt = tokenizer.apply_chat_template(
       messages, add_generation_prompt=True, tokenize=False, enable_thinking=False
   )
   print(generate(model, tokenizer, prompt=prompt, max_tokens=200))
   ```

### Important

- **Always load the model with `load_hadamard.py`.** The file is in this repository. The experts are stored in a rotated basis. If you use `mlx_lm.load` or `mlx_lm.generate` from the command line without this loader, the output is wrong.
- **Thinking is on by default.** Pass `enable_thinking=False` to turn it off, as in the script above. We used the model with thinking off.

## Limitations

- Text only.
- We tuned and checked the model on translation and writing polish only. Other tasks can lose more quality.
- The 64 removed experts per layer are gone, so the model cannot use them.

## License and attribution

Apache-2.0, the same license as the base model. See [LICENSE](https://huggingface.co/yipengsun/MiniCPM-V-4.7-35B-A3B-REAP192-GPTQ3-MLX/blob/main/LICENSE). This model is derived from openbmb/MiniCPM-V-4.7-35B-A3B by OpenBMB. Changes: expert pruning, quantization, conversion to MLX, and removal of the vision tower.
