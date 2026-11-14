---
base_model: LGAI-EXAONE/K-EXAONE-236B-A23B
base_model_relation: quantized
license: other
license_name: k-exaone
license_link: LICENSE
language:
  - en
  - ko
  - es
  - de
  - ja
  - vi
tags:
  - lg-ai
  - exaone
  - k-exaone
pipeline_tag: text-generation
library_name: transformers
---

<br>
<br>
<p align="center">
<img src="assets/K-EXAONE_logo_gray.png" width="400">
<br>
<br>
<br>

<div align="center">
  <a href="https://huggingface.co/collections/LGAI-EXAONE/k-exaone" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/🤗-HuggingFace-FC926C?style=for-the-badge" alt="HuggingFace">
  </a>
  <a href="https://www.lgresearch.ai/blog/view?seq=619" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/📝-Blog-E343BD?style=for-the-badge" alt="Blog">
  </a>
  <a href="https://arxiv.org/abs/2601.01739" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/📑-Technical_Report-684CF4?style=for-the-badge" alt="Technical Report">
  </a>
  <a href="https://github.com/LG-AI-EXAONE/K-EXAONE" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/🖥️-GitHub-2B3137?style=for-the-badge" alt="GitHub">
  </a>
  <a href="https://friendli.ai/model/LGAI-EXAONE/K-EXAONE-236B-A23B" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/✈️_API-Try_on_FriendliAI-2649BC?style=for-the-badge" alt="FriendliAI">
  </a>
</div>



<div align="center">
<table><tr><td>Check out the <span style="color: orange"> <b>NVFP4+GPTQ weights by FuriosaAI</b>! </span> <a href="https://huggingface.co/FuriosaAIShareLGAI/K-EXAONE-236B-A23B-NVFP4A16-GPTQ" style="text-decoration: none;"> ➡️ link</a> </td></tr></table>
</div>

<br>

# K-EXAONE-236B-A23B-GGUF

## Introduction

We introduce **K-EXAONE**, a large-scale multilingual language model developed by LG AI Research. Built using a Mixture-of-Experts architecture, K-EXAONE features **236 billion total** parameters, with **23 billion active** during inference. Performance evaluations across various benchmarks demonstrate that K-EXAONE excels in reasoning, agentic capabilities, general knowledge, multilingual understanding, and long-context processing.

#### Key Features

- **Architecture & Efficiency:** Features a 236B fine-grained MoE design (23B active) optimized with **Multi-Token Prediction (MTP)**, enabling self-speculative decoding that boosts inference throughput by approximately 1.5x.
- **Long-Context Capabilities:** Natively supports a **256K context window**, utilizing a **3:1 hybrid attention** scheme with a **128-token sliding window** to significantly minimize memory usage during long-document processing.
- **Multilingual Support:** Covers 6 languages: Korean, English, Spanish, German, Japanese, and Vietnamese. Features a redesigned **150k vocabulary** with **SuperBPE**, improving token efficiency by ~30%.
- **Agentic Capabilities:** Demonstrates superior tool-use and search capabilities via **multi-agent strategies.**
- **Safety & Ethics:** Aligned with **universal human values**, the model uniquely incorporates **Korean cultural and historical contexts** to address regional sensitivities often overlooked by other models. It demonstrates high reliability across diverse risk categories.

For more details, please refer to the [technical report](https://arxiv.org/abs/2601.01739), [blog](https://www.lgresearch.ai/blog/view?seq=619) and [GitHub](https://github.com/LG-AI-EXAONE/K-EXAONE).

![main_figure](assets/main_figure.png)


### Model Configuration

- Number of Parameters: 236B in total and 23B activated
- Number of Parameters (without embeddings): 234B
- Hidden Dimension: 6,144
- Number of Layers: 48 Main layers + 1 MTP layers
  - Hybrid Attention Pattern: 12 x (3 Sliding window attention + 1 Global attention)
- Sliding Window Attention
  - Number of Attention Heads: 64 Q-heads and 8 KV-heads
  - Head Dimension: 128 for both Q/KV
  - Sliding Window Size: 128
- Global Attention
  - Number of Attention Heads: 64 Q-heads and 8 KV-heads
  - Head Dimension: 128 for both Q/KV
  - No Rotary Positional Embedding Used (NoPE)
- Mixture of Experts:
  - Number of Experts: 128
  - Number of Activated Experts: 8
  - Number of Shared Experts: 1
  - MoE Intermediate Size: 2,048
- Vocab Size: 153,600
- Context Length: 262,144 tokens
- Knowledge Cutoff: Dec 2024 (2024/12)
- Quantization: `Q8_0`, `Q6_K`, `Q5_K_M`, `Q4_K_M`, `IQ4_XS` in GGUF format (also includes BF16 weights)

## Evaluation Results

The evaluation results of the original model against other models are available on the [GitHub](https://github.com/LG-AI-EXAONE/K-EXAONE#performance) page or in the [model card](https://huggingface.co/LGAI-EXAONE/K-EXAONE-236B-A23B#evaluation-results) of the original model.
Detailed evaluation configurations and results can be found in the [technical report](https://arxiv.org/abs/2601.01739).
## Requirements

K-EXAONE is supported by multiple libraries. Please install the required libraries as needed for your use case.

#### Transformers

You should install `transformers >= 5.1.0` for the K-EXAONE model.

#### llama.cpp

To use the K-EXAONE model with llama.cpp library, you should install `llama.cpp >= b7737`.


### Quickstart

### llama.cpp

You should install the `llama.cpp` library with the version of `b7737` or after.

After you install the library, you need to prepare a model file in GGUF format as below:
```bash
# Download GGUF model weights (e.g. Q4_K_M)
hf download LGAI-EXAONE/K-EXAONE-236B-A23B-GGUF --include "*Q4_K_M*" --local-dir .

# Or convert huggingface model into GGUF format on your own
hf download LGAI-EXAONE/K-EXAONE-236B-A23B --local-dir $YOUR_MODEL_DIR
python convert_hf_to_gguf.py $YOUR_MODEL_DIR --outtype bf16 --outfile K-EXAONE-236B-A23B-BF16.gguf

# If you want to use the lower precision than BF16, you need to quantize the model
./llama-quantize K-EXAONE-236B-A23B-BF16.gguf K-EXAONE-236B-A23B-Q4_K_M.gguf Q4_K_M
```

You can test the model with simple chat CLI by running the command below:
```bash
./llama-cli -m K-EXAONE-236B-A23B-Q4_K_M.gguf \
    -ngl 99 \
    -fa on -sm row \
    --temp 1.0 --top-p 0.95 --min-p 0 \
    -c 131072 -n 32768 \
    --no-context-shift \
    --jinja
```

You can also launch a server by running the command below:

```bash
./llama-server -m K-EXAONE-236B-A23B-Q4_K_M.gguf \
    -ngl 99 \
    -fa on -sm row \
    --temp 1.0 --top-p 0.95 --min-p 0 \
    -c 131072 -n 32768 \
    --no-context-shift \
    --jinja \
    --host 0.0.0.0 --port 8080
```

When the server is ready, you can test the model using the chat-style UI at http://localhost:8080, and access the OpenAI-compatible API at http://localhost:8080/v1.

### Ollama / LM-Studio

Ollama and LM-Studio are powered by llama.cpp, so they should be updated once llama.cpp officially supports K-EXAONE. We will update this section once each library supports K-EXAONE.


## Usage Guideline

> [!IMPORTANT]
> To achieve the expected performance, we recommend using the following configurations:
> - We strongly recommend to use `temperature=1.0`, `top_p=0.95`, `presence_penalty=0.0` for best performance.
> - Different from EXAONE-4.0, K-EXAONE uses `enable_thinking=True` as default. Thus, you need to set `enable_thinking=False` when you want to use non-reasoning mode.
>

## Limitation

The K-EXAONE language model has certain limitations and may occasionally generate inappropriate responses. The language model generates responses based on the output probability of tokens, and it is determined during learning from training data. While we have made every effort to exclude personal, harmful, and biased information from the training data, some problematic content may still be included, potentially leading to undesirable responses. Please note that the text generated by K-EXAONE language model does not reflect the views of LG AI Research.

- Inappropriate answers may be generated, which contain personal, harmful or other inappropriate information.
- Biased responses may be generated, which are associated with age, gender, race, and so on.
- The generated responses rely heavily on statistics from the training data, which can result in the generation of semantically or syntactically incorrect sentences.
- Since the model does not reflect the latest information, the responses may be false or contradictory.

LG AI Research strives to reduce potential risks that may arise from K-EXAONE language models. Users are not allowed to engage in any malicious activities (e.g., keying in illegal information) that may induce the creation of inappropriate outputs violating LG AI's ethical principles when using K-EXAONE language models.


## License

The model is licensed under [K-EXAONE AI Model License Agreement](./LICENSE)


## Citation

```
@article{k-exaone,
  title={K-EXAONE Technical Report},
  author={{LG AI Research}},
  journal={arXiv preprint arXiv:2601.01739},
  year={2025}
}
```

## Contact

LG AI Research Technical Support: contact_us@lgresearch.ai

