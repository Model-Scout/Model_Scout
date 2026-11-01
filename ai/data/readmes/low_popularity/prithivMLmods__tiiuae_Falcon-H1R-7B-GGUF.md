---
license: other
license_name: falcon-llm-license
license_link: https://falconllm.tii.ae/falcon-terms-and-conditions.html
language:
- ar
- cs
- de
- en
- es
- fr
- hi
- it
- ja
- ko
- nl
- pl
- pt
- ro
- ru
- sv
- ur
- zh
tags:
- falcon-h1r
- text-generation-inference
base_model:
- tiiuae/Falcon-H1R-7B
pipeline_tag: text-generation
library_name: transformers
---

# **tiiuae_Falcon-H1R-7B-GGUF**

> Falcon-H1R-7B from TII (Technology Innovation Institute) is a 7-billion-parameter reasoning-specialized causal decoder-only model built on the Falcon-H1-7B-Base foundation, featuring a hybrid Transformer + Mamba2 architecture trained via cold-start supervised fine-tuning with long reasoning traces and scaled RL using GRPO (Generalized Reward Preference Optimization) for exceptional performance in mathematics, programming, instruction following, and general logic. It achieves state-of-the-art results among <8B models across benchmarks like 88.1% on AIME24 (96.7% with test-time scaling), 68.6% on LiveCodeBench v5-v6, 61.3% on GPQA-Diamond, 72.1% on MMLU-Pro, and 53.4% on IFBench—often matching or exceeding 14B-47B competitors like Qwen3-32B, Phi-4-14B, and Nemotron-H-47B while enabling 2x faster inference (e.g., ~1800 tokens/s/GPU at batch=64) and up to 262k context length with low memory footprint. Optimized for multilingual use (English primary, trained on 18 languages including Arabic, Hindi, Chinese) under Falcon-LLM License, it generates structured <think>...</think> reasoning blocks followed by final answers, deployable via Transformers (temperature=0.6, top_p=0.95, max_new_tokens=65536), vLLM (>=0.11.0, --reasoning-parser deepseek_r1), or SGLang for efficient real-world applications on TP=2 setups.

## Quick Start with llama-cpp-python

```py
from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF",
	filename="Falcon-H1R-7B.Q4_K_M.gguf",
)
```

```py
llm.create_chat_completion(
	messages = [
		{
			"role": "user",
			"content": "What is the capital of France?"
		}
	]
)
```

## Falcon-H1R-7B [GGUF]

| File Name | Quant Type | File Size | File Link |
| - | - | - | - |
| Falcon-H1R-7B-bf16.gguf | BF16 | 15.2 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B-bf16.gguf) |
| Falcon-H1R-7B-f32.gguf | F32 | 30.3 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B-f32.gguf) |
| Falcon-H1R-7B.IQ4_XS.gguf | IQ4_XS | 4.19 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.IQ4_XS.gguf) |
| Falcon-H1R-7B.Q2_K.gguf | Q2_K | 2.89 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q2_K.gguf) |
| Falcon-H1R-7B.Q3_K_L.gguf | Q3_K_L | 3.92 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q3_K_L.gguf) |
| Falcon-H1R-7B.Q3_K_M.gguf | Q3_K_M | 3.69 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q3_K_M.gguf) |
| Falcon-H1R-7B.Q3_K_S.gguf | Q3_K_S | 3.43 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q3_K_S.gguf) |
| Falcon-H1R-7B.Q4_K_M.gguf | Q4_K_M | 4.6 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q4_K_M.gguf) |
| Falcon-H1R-7B.Q4_K_S.gguf | Q4_K_S | 4.4 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q4_K_S.gguf) |
| Falcon-H1R-7B.Q5_K_M.gguf | Q5_K_M | 5.39 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q5_K_M.gguf) |
| Falcon-H1R-7B.Q5_K_S.gguf | Q5_K_S | 5.28 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q5_K_S.gguf) |
| Falcon-H1R-7B.Q6_K.gguf | Q6_K | 6.23 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q6_K.gguf) |
| Falcon-H1R-7B.Q8_0.gguf | Q8_0 | 8.07 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.Q8_0.gguf) |
| Falcon-H1R-7B.f16.gguf | F16 | 15.2 GB | [Download](https://huggingface.co/prithivMLmods/tiiuae_Falcon-H1R-7B-GGUF/blob/main/Falcon-H1R-7B.f16.gguf) |

## Quants Usage 

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)