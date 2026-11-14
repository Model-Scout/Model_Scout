---
license: apache-2.0
base_model: mistralai/Mistral-Small-24B-Instruct-2501
base_model_relation: quantized
pipeline_tag: text-generation
library_name: mnn
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - zh
  - ja
  - ru
  - ko
tags:
  - tokforge
  - on-device
  - mnn
  - mistral
  - mobile
---

# Mistral Small 24B Instruct 2501 (MNN)

Mistral AI's Mistral Small 24B Instruct 2501 as a 4-bit MNN bundle for chatting with TokForge on phones with 24 GB RAM.

Published by [TokForge](https://tokforge.ai) for on-device inference.

| | |
|---|---|
| **What it is** | Chat model |
| **Format** | MNN bundle, 4-bit weights (block 128) |
| **Runs on** | Android phones (CPU, OpenCL or Vulkan GPU) |
| **Phone class** | 24 GB RAM or more (no catalog class) |
| **Download** | 14.2 GB (8 files) |
| **Base model** | [mistralai/Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) |
| **License** | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## TokForge

- **Website:** https://tokforge.ai
- **Discord:** https://discord.gg/Acv3CBtfVm
- **Google Play:** https://play.google.com/store/apps/details?id=dev.tokforge
- **iOS TestFlight:** https://testflight.apple.com/join/jnufjzRr

Runs on-device in the TokForge app.

## Use it in TokForge

1. Install TokForge from [Google Play](https://play.google.com/store/apps/details?id=dev.tokforge), or join the [iOS TestFlight](https://testflight.apple.com/join/jnufjzRr).
2. On Android, open **Models > Browse**, search for `Mistral-Small-24B-Instruct-MNN` and download it. It needs a phone with 24 GB RAM or more.
3. Load it and start a chat. The model runs on the phone; once it is downloaded, chatting needs no connection.

Collections: [TokForge Chat Models (MNN)](https://huggingface.co/collections/darkmaniac7/tokforge-chat-models-mnn-69cdcddc86ea126668a5e9e8), [TokForge Llama, Mistral and Dolphin (MNN)](https://huggingface.co/collections/darkmaniac7/tokforge-llama-mistral-and-dolphin-mnn-69cd3246dc891f89ed2af0e4).

## Files

| File | Size | What it is |
|---|---:|---|
| `config.json` | 210 B | MNN runtime settings |
| `embeddings_bf16.bin` | 1.34 GB | Token embeddings (bf16) |
| `export_args.json` | 1.13 KB | Export settings used for the conversion |
| `llm.mnn` | 696 KB | Model graph |
| `llm.mnn.json` | 1.40 MB | Model graph as JSON (reference copy) |
| `llm.mnn.weight` | 12.9 GB | Model weights |
| `llm_config.json` | 1.88 KB | Model settings and chat template |
| `tokenizer.txt` | 1.49 MB | Tokenizer |

## About the model

Mistral Small 24B Instruct 2501 (Mistral Small 3) is Mistral AI's knowledge-dense 24B model, built for chat, function
calling and multi-step tasks. It has a 32K-token context and supports dozens of languages, including English, French,
German, Spanish, Italian, Chinese, Japanese, Korean and Portuguese.

| | |
|---|---|
| **Architecture** | Mistral (standard attention, 40 layers) |
| **Parameters** | 24B (4-bit quantized) |
| **Quantization** | W4A16 (4-bit weights, block size 128) |
| **Vocab** | 131,072 tokens (Tekken tokenizer) |

## Recommended settings

| Setting | Value |
|---------|-------|
| Backend | OpenCL (Qualcomm) / Vulkan (MediaTek) / CPU (fallback) |
| Precision | Low |
| Threads | 4 |
| Thinking | Off |

## Memory

Needs 24 GB RAM or more. It runs best on flagship phones with 24 GB RAM and few background apps.

## How it was made

Converted using MNN's `llmexport` pipeline:

```bash
python llmexport.py --path mistralai/Mistral-Small-24B-Instruct-2501 --export mnn --quant_bit 4 --quant_block 128
```

## Limitations

- Intended for TokForge / MNN on-device inference on Android
- This is a runtime bundle, not a standard Transformers training checkpoint
- Quantization (Q4) may slightly reduce quality compared to the full-precision original

## License

Mistral Small 24B Instruct 2501 is released by Mistral AI under the [Apache-2.0 license](https://www.apache.org/licenses/LICENSE-2.0).

## Credits

- Mistral Small 24B Instruct 2501 by Mistral AI ([Hugging Face](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)). Used under the Apache-2.0 license.
- Converted with llmexport from [MNN](https://github.com/alibaba/MNN) by Alibaba (Apache-2.0).
