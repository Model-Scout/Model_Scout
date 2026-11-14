---
license: llama3.1
base_model: aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored
base_model_relation: quantized
pipeline_tag: text-generation
library_name: mnn
language:
  - en
  - de
  - fr
  - it
  - pt
  - hi
  - es
  - th
  - zh
  - ko
  - ja
tags:
  - tokforge
  - on-device
  - mnn
  - llama
  - mobile
  - uncensored
  - roleplay
---

# DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored (MNN)

aifeifei798's DarkIdol v1.2, a Llama 3.1 8B model for roleplay and creative writing, as a 4-bit MNN bundle for chatting on your phone with TokForge.

Published by [TokForge](https://tokforge.ai) for on-device inference.

| | |
|---|---|
| **What it is** | Chat model (Llama 3.1 8B derivative) |
| **Format** | MNN bundle, 4-bit weights (block 128) |
| **Runs on** | Android phones (CPU, OpenCL or Vulkan GPU) |
| **Phone class** | No catalog class; needs more free RAM than its 5.27 GB of weights |
| **Download** | 5.28 GB (10 files) |
| **Base model** | [aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored](https://huggingface.co/aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored) |
| **License** | [Llama 3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/blob/main/LICENSE) |

## TokForge

- **Website:** https://tokforge.ai
- **Discord:** https://discord.gg/Acv3CBtfVm
- **Google Play:** https://play.google.com/store/apps/details?id=dev.tokforge
- **iOS TestFlight:** https://testflight.apple.com/join/jnufjzRr

Runs on-device in the TokForge app.

## Use it in TokForge

1. Install TokForge from [Google Play](https://play.google.com/store/apps/details?id=dev.tokforge), or join the [iOS TestFlight](https://testflight.apple.com/join/jnufjzRr).
2. On Android, open **Models > Browse**, search for `DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-MNN` and download it.
3. Load it and start a chat. The model runs on the phone; once it is downloaded, chatting needs no connection.

Collections: [TokForge Llama, Mistral and Dolphin (MNN)](https://huggingface.co/collections/darkmaniac7/tokforge-llama-mistral-and-dolphin-mnn-69cd3246dc891f89ed2af0e4).

## Files

| File | Size | What it is |
|---|---:|---|
| `config.json` | 210 B | MNN runtime settings |
| `embeddings_bf16.bin` | 1.05 GB | Token embeddings (bf16) |
| `export_args.json` | 1.19 KB | Export settings used for the conversion |
| `llm.mnn` | 558 KB | Model graph |
| `llm.mnn.json` | 1.12 MB | Model graph as JSON (reference copy) |
| `llm.mnn.weight` | 4.22 GB | Model weights |
| `llm_config.json` | 828 B | Model settings and chat template |
| `tokenizer.txt` | 1.41 MB | Tokenizer |
| `LICENSE` | 7.63 KB | Llama 3.1 Community License (Meta's text) |
| `NOTICE` | 116 B | Llama 3.1 notice (Meta) |

## About the model

DarkIdol v1.2 by aifeifei798 is a Llama 3.1 8B Instruct derivative for roleplay, creative writing and
unrestricted conversation. It is part of the DarkIdol series, which focuses on staying in character across many
role-playing scenarios. It gives fewer refusals than Llama 3.1 8B Instruct.

| | |
|---|---|
| **Architecture** | Llama 3.1 (standard attention, 32 layers, GQA 32Q/8KV) |
| **Parameters** | 8B (4-bit quantized) |
| **Quantization** | W4A16 (4-bit weights, block size 128) |
| **Vocab** | 128,256 tokens |

## Recommended settings

| Setting | Value |
|---------|-------|
| Backend | OpenCL (Qualcomm) / Vulkan (MediaTek) / CPU (fallback) |
| Precision | Low |
| Threads | 4 |
| Thinking | Off |

## How it was made

Converted using MNN's `llmexport` pipeline:

```bash
python llmexport.py --path aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored --export mnn --quant_bit 4 --quant_block 128
```

## Limitations

- Intended for TokForge / MNN on-device inference on Android
- This is a runtime bundle, not a standard Transformers training checkpoint
- Quantization (Q4) may slightly reduce quality compared to the full-precision original
- This model gives fewer built-in refusals than its base model: **use responsibly**

## License

DarkIdol v1.2 is built on Meta's Llama 3.1 8B Instruct. Llama 3.1 is licensed under the
[Llama 3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/blob/main/LICENSE).
Meta's license text is in `LICENSE` and the required notice is in `NOTICE`. Built with Llama.

aifeifei798's repo also carries [The Open Anarchist License](https://huggingface.co/aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored/blob/main/OpenAnarchistLicense.md) (also at the end of its model card); its notice asks to be included or linked in all copies, so it is linked here.

## Credits

- DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored by aifeifei798 ([Hugging Face](https://huggingface.co/aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored)). Used under the [Llama 3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/blob/main/LICENSE).
- Llama 3.1 8B by Meta ([Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)). Used under the [Llama 3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/blob/main/LICENSE).
- Built with Llama. Llama 3.1 is licensed under the Llama 3.1 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved. The license text and this notice are in the `LICENSE` and `NOTICE` files in this repo.
- Converted with llmexport from [MNN](https://github.com/alibaba/MNN) by Alibaba (Apache-2.0).
