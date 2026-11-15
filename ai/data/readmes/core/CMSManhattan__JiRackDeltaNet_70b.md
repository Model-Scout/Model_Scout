---
license: other
library_name: pytorch
pipeline_tag: text-generation

language:
- en
- zh
- ja
- ko
- fr
- es
- pt
- de
- it
- ru
- ar
- vi
- th
tags:
- text-generation
- deltanet
- qwen3.8
- gguf
- cpu
- efficient
- low-memory
- ternary
- bitnet
- jirack
- web-ui
- routing
- tool-call
- robotics
- ollama
- ternary-weights
- ternary-transformer
- quantization
- 1.58-bit

---


## JiRackDeltaNet 70B

> **Beta release.** This is the first SFT of JiRackDeltaNet 70B. Tool calling already works through any OpenAI-compatible client (109/117 on our internal test), but when a required argument is missing the model often calls the tool instead of asking. The next version adds fine-tuning on clarifying questions, and GSM8K / HumanEval results will be added. Feedback is welcome.

**JiRackDeltaNet 70B** is a **69.93B-parameter hybrid language model** by CMSManhattan (Konstantin Grabko): a Gated DeltaNet / gated full-attention model (Qwen 3.5 layout) built in our own JiRack code and fine-tuned on our own data (chat, reasoning, code, math, tool calling).

> Status: first SFT release; see Limitations.

So it is good coding and  agentic model with robotics tokenizer for next model upgrade  

## Model

|  |  |
| --- | --- |
| Architecture | hybrid decoder, 128 layers: 96 **Gated DeltaNet** (linear attention) + 32 **gated full attention**, every 4th layer full attention |
| Parameters | 69.93B |
| Hidden / FFN | 5120 / 26624 (SwiGLU) |
| Full attention | 24 heads / 4 KV heads, head dim 256, output gate, partial RoPE (25 %), interleaved mRoPE sections \[11, 11, 10\], RoPE theta 1e7 |
| Gated DeltaNet | 16 key heads / 48 value heads, head dim 128, causal conv kernel 4 |
| Vocabulary | 248,320 (Qwen 3.5 tokenizer and chat template), untied input / output embeddings |
| Extra head | 1-layer MTP (multi-token prediction) head |
| Code | `JiRackDeltaNet_70b.py`: single-file PyTorch model; parameter names match the Hugging Face `Qwen3_5ForCausalLM` state dict |
| Weights | bf16 (repository root), an FP8 block-quantized copy in `sft_final_fp8/` and GGUF quantizations (Q3\_K\_M, Q4\_K\_M, Q6\_K) in `gguf/` (see below) |

## How it was built

JiRackDeltaNet 70B is a modified version of a Qwen model (Apache 2.0). CMSManhattan changed the architecture and the weights in its own JiRack code and fine-tuned the model on its own data (chat, reasoning, code, math, tool calling). The training recipe and data are not published.

## Model Expansion

JiRack models are grown from a smaller base instead of being trained from scratch. We use two techniques together:

- **FFN widening.** We increase the intermediate (FFN) size of every layer. This adds capacity, so the model has more room to absorb new knowledge during further training.
- **Layer duplication.** We duplicate existing blocks and initialize the output projections of the new blocks to zero, so at the start the expanded model behaves exactly like the original. During training the original blocks are frozen and new knowledge goes into the added layers, which reduces catastrophic forgetting.

The practical result: when a model reaches the limit of its capacity on your data, it can be expanded and fine-tuned further instead of being retrained from scratch, keeping what it already knows. Contact us if you want a model expanded and fine-tuned on your own data.

## Results

GSM8K and HumanEval are not measured yet; tool calling is measured below.

### Tool calling (GGUF Q3_K_M)

Our internal 117-case tool-calling test on the smallest GGUF file, `JiRackDeltaNet_70b_with_prompt.Q3_K_M.gguf`, served by `llama-server` as an OpenAI-compatible API: tools are passed as standard OpenAI `tools` and parsed by llama.cpp's own Qwen 3.5 template, temperature 0, reasoning off. The cases are written by us and are not in the training data.

| Category | Q3_K_M |
| --- | --- |
| Single call (one tool, all arguments given) | 38/38 |
| Parallel calls | 19/19 |
| Follow-up (answer from a tool result) | 20/20 |
| No tool needed | 25/25 |
| Clarify a missing argument | 7/15 |
| **Total** | **109/117 (93.2%)** |

All 8 misses are in clarify: the model called the tool instead of asking for the missing argument.

Sample (greedy, thinking off):

```
You: A store sells pens at $3 each. Tom buys 7 pens and pays with a $50 bill. How much change does he get?
Assistant: Tom buys 7 pens at $3 each, so he spends 7 x $3 = $21. He pays with a $50 bill, so his change is $50 - $21 = $29.
```

## FP8 copy

`sft_final_fp8/`: the large GEMMs of every layer (DeltaNet `in_proj_qkv` / `in_proj_z` / `out_proj`, attention `q/k/v/o_proj`, MLP `gate/up/down_proj`; 800 tensors) in **FP8 e4m3 with 128 × 128 block scales** (`weight_scale_inv`, the same layout as the official Qwen / DeepSeek FP8 releases, `quantization_config` in `config.json`). Embeddings, `lm_head`, norms, conv, decay parameters, `in_proj_a/b` and the MTP head stay bf16.

|  | bf16 | FP8 |
| --- | --- | --- |
| Size | 140 GB | 73 GB |
| Mean relative weight error | — | 2.65 % |
| Pens question above | $29 | $29 |

73 GB fits on a single 96 GB GPU.

## GGUF (llama.cpp)

Three GGUF quantizations in `gguf/`, each with a built-in system prompt (direct answers, no reasoning block). If a request has no system message, the chat template in the GGUF adds the prompt; your own system message replaces it. The prompt text, commands and checks are in [gguf/README.md](gguf/README.md).

```bash
llama-server -m JiRackDeltaNet_70b_with_prompt.Q4_K_M.gguf -c 8192 --jinja --reasoning off --port 8080
```

|  | Q3\_K\_M | Q4\_K\_M | Q6\_K |
| --- | --- | --- | --- |
| Size | 33.89 GB | 42.65 GB | 57.40 GB (2 parts) |
| CPU speed, prompt / generation (GH200 Grace, 64 threads, `llama-bench`) | 20.1 / 5.17 tokens/s | 50.2 / 5.04 tokens/s | 45.3 / 4.11 tokens/s |
| Pens question above | $29 | $29 | $29 |
| Tool-calling test (117 cases) | 109/117 (93.2%) | — | — |

## Usage

The repository ships its own PyTorch code; no `transformers` model class is needed.

```bash
pip install torch safetensors tokenizers jinja2
# bf16, splits the 128 blocks over all visible GPUs (>= 2 x 80 GB)
python3 chat_jirack.py --model-dir . --no-think --temperature 0
# FP8 copy (weights stay FP8 in memory, dequantized per layer call; one 96 GB GPU)
python3 sft_final_fp8/chat_fp8.py --model-dir sft_final_fp8 --no-think --temperature 0
```

Commands in the chat: `/think` (reasoning on / off), `/reset`, `exit`. Prompts use the Qwen 3.5 chat template in `chat_template.jinja` (tools are passed in the `<tools>` system block and called with `<tool_call><function=…><parameter=…>`).

The reference chat scripts recompute the whole sequence for every new token (no KV cache), so they are slow (\~1 token/s on 8 × A100); they are meant for checking the model, not for serving. The parameter names match `Qwen3_5ForCausalLM`, so the weights should also load in Hugging Face / vLLM implementations of that architecture; this is **not verified** yet.

## Limitations

- **Missing arguments**: when a required argument is missing, the model often calls the tool anyway instead of asking (7/15 on our test); validate tool calls before executing them.
- **Early release**: this is the first fine-tuning round of the model; further training is planned.
- **Not ternary yet**: JiRack's BitLinear (b1.58) path is present in the code but off (lambda = 0); ternary QAT is a planned later stage.
- Trained with sequences up to 8,192 tokens.
- The model may occasionally misstate who made it.
- Not for medical, legal or financial advice.

## License

This project is a derivative work based on a Qwen model originally released under the **Apache License, Version 2.0**. 

### 1. Proprietary Terms for JiRack
All modifications, proprietary additions, architectural extensions, derived model weights, and scripts developed by **CMS Manhattan (Konstantin Grabko)** — including but not limited to:
* JiRack custom model code and architecture modifications,
* changes to the model architecture,
* Supervised Fine-Tuning (SFT) on the JiRack dataset mix,
* Quantized weights and conversions (FP8, GGUF, BitNet/ternary formats),

are licensed under the **JiRack Proprietary Model License (BSL)** (see `LICENSE` file for full terms). 

* **Permitted Use:** Free for non-commercial, evaluation, research, and internal organizational use.
* **Commercial / Integration / Redistribution:** Requires a separate written **Commercial Agreement** with the Licensor (Konstantin Grabko / CMS Manhattan).

### 2. Third-Party Attribution & Compliance
In accordance with Section 4 of the Apache License 2.0, the original copyright, attribution, and license notices of the base model are preserved. When redistributing or using this repository, you must retain:
* The Apache 2.0 license text of the base model (`LICENSE-APACHE`),
* The `NOTICE.md` file accompanying this repository,
* All copyright and attribution notices attached to the original components.

# Live chat on HF Space
- https://huggingface.co/spaces/CMSManhattan/JiRackDeltaNet_27b
- https://huggingface.co/spaces/CMSManhattan/JiRack-16B-Chat
- https://huggingface.co/spaces/CMSManhattan/JiRack-8B-Chat
- https://huggingface.co/spaces/CMSManhattan/JiRack-2B-Chat
---

## JiRack Codding Agent IDE
- It is Agent Coding IDE for JiRack Models to run via Ollama on home PC 
- It good choose for Agent Coding IDE such as Cursor , Windsurf IDE or Devin IDE etc but more safe that ask you to apply changes and review.
- Web site https://www.jirack.com
- Eclise Plugin site https://marketplace.eclipse.org/content/jirack-coding-agent
- Jetbrain Plugin site https://plugins.jetbrains.com/plugin/35073-jirack-agent
- VS Code Plugin site https://marketplace.visualstudio.com/items?itemName=JiRackautomationCodingAgentIDE.jirack-agent
  
## JiRack Codding Agent IDE files
- Eclise Final release version https://huggingface.co/CMSManhattan/JiRackDeltaNet_27b/resolve/main/jirack_ide_final.zip
- Microsoft VS Code plugin https://huggingface.co/spaces/CMSManhattan/README/blob/main/jirack-agent-0.9.0.vsix
- Jetbrain plugin  https://huggingface.co/spaces/CMSManhattan/README/resolve/main/jirack-jetbrains-0.11.0.zip  
- JiRack DeskTop UI  https://huggingface.co/spaces/CMSManhattan/README/resolve/main/windows_v11.zip
  
---


## ROBOS HUMANOID Project

- https://github.com/cmsmanhattan/ROBOS

## Licensing. 
You are free to download JiRackDeltaNet 70B and try it for evaluation, testing and research, side by side with JiRackDeltaNet 27B. Commercial or production use of the 70B model requires a commercial license from CMS Manhattan. For pricing and terms, please contact us.

## 📧 Contact
For joint venture opportunities, hardware integration, or licensing inquiries:
- **Email:** grabko@cmsmanhattan.com
- **Phone:** +1 (516) 777-0945
- **Location:** New York, USA