---
license: apache-2.0
base_model: tencent/Hy-MT2-7B
library_name: mlx
pipeline_tag: translation
tags:
  - mlx
  - mlx-lm
  - translation
  - hy-mt2
  - abliterated
  - 8-bit
language:
  - zh
  - en
  - fr
  - pt
  - es
  - ja
  - tr
  - ru
  - ar
  - ko
  - th
  - it
  - de
  - vi
  - ms
  - id
  - tl
  - hi
  - pl
  - cs
  - nl
  - km
  - my
  - fa
  - gu
  - ur
  - te
  - mr
  - he
  - bn
  - ta
  - uk
  - bo
  - kk
  - mn
  - ug
---

# Hy-MT2-7B-Abliterated-8bit

This repository contains 8-bit MLX weights for an abliterated derivative of [tencent/Hy-MT2-7B](https://huggingface.co/tencent/Hy-MT2-7B), Tencent Hunyuan's multilingual translation model.

The abliteration method is based on [jim-plus/llm-abliteration](https://github.com/jim-plus/llm-abliteration). This is a community derivative and is not an official Tencent release.

## Model Details

- Base model: [tencent/Hy-MT2-7B](https://huggingface.co/tencent/Hy-MT2-7B)
- Target repository: [mlx-community/hy-mt2-7b-abliterated-8bit](https://huggingface.co/mlx-community/hy-mt2-7b-abliterated-8bit)
- Runtime: MLX / MLX-LM
- Precision: 8-bit quantized MLX weights
- Task: multilingual translation
- License: Apache-2.0, following the upstream model license

The 8-bit version is intended for lower memory usage on Apple Silicon. Compared with the bf16 version, it may have small quality differences due to quantization.

## Usage

Install MLX-LM:

```bash
pip install -U mlx-lm
```

Generate with the command line:

```bash
mlx_lm.generate \
  --model mlx-community/hy-mt2-7b-abliterated-8bit \
  --prompt "将以下文本翻译成英语，注意只需要输出翻译后的结果，不要额外解释：\n\n今天天气真好。" \
  --max-tokens 4096 \
  --temp 0.7 \
  --top-p 0.6
```

Or use Python:

```python
from mlx_lm import load, generate

model_id = "mlx-community/hy-mt2-7b-abliterated-8bit"
model, tokenizer = load(model_id)

prompt = "将以下文本翻译成英语，注意只需要输出翻译后的结果，不要额外解释：\n\n今天天气真好。"
messages = [{"role": "user", "content": prompt}]
formatted_prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

response = generate(
    model,
    tokenizer,
    prompt=formatted_prompt,
    max_tokens=4096,
    temp=0.7,
)
print(response)
```

## Prompting

Hy-MT2 is optimized for translation instructions. Use full language names in prompts when possible.

Example:

```text
Translate the following text into Chinese. Only output the translated result without additional explanation:

The weather is nice today.
```

Recommended generation settings from the upstream Hy-MT2 model card for 1.8B and 7B models:

```json
{
  "temperature": 0.7,
  "top_p": 0.6,
  "top_k": 20,
  "repetition_penalty": 1.05,
  "max_tokens": 4096
}
```

## About Abliteration

Abliteration attempts to identify and remove refusal-related directions in model activations or weights. It can reduce explicit refusal behavior, but it does not guarantee that every refusal is removed, and it may affect translation quality or other model behavior.

This model should be evaluated for your own use case before production use.

## Limitations

- This model inherits the capabilities and limitations of the upstream Hy-MT2-7B model.
- 8-bit quantization can introduce quality differences compared with bf16 weights.
- Abliteration may change behavior in ways that are not captured by standard translation benchmarks.
- Users are responsible for complying with applicable laws, platform policies, and the upstream model license.

## References

- Base model: [tencent/Hy-MT2-7B](https://huggingface.co/tencent/Hy-MT2-7B)
- Abliteration method: [jim-plus/llm-abliteration](https://github.com/jim-plus/llm-abliteration)
- Hy-MT2 paper: [Hy-MT2: A Family of Fast, Efficient and Powerful Multilingual Translation Models in the Wild](https://arxiv.org/abs/2605.22064)

## Citation

```bibtex
@misc{zheng2026hymt2familyfastefficient,
  title={Hy-MT2: A Family of Fast, Efficient and Powerful Multilingual Translation Models in the Wild},
  author={Mao Zheng and Zheng Li and Tao Chen and Bo Lv and Mingrui Sun and Mingyang Song and Jinlong Song and Hong Huang and Decheng Wu and Hai Wang and Yifan Song and Yanfeng Chen and Guanwei Zhang},
  year={2026},
  eprint={2605.22064},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2605.22064}
}
```
