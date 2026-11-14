---
license: apache-2.0
base_model: huihui-ai/Huihui-Qwen3.5-4B-Claude-4.6-Opus-abliterated
base_model_relation: quantized
pipeline_tag: text-generation
library_name: mnn
language:
  - en
  - zh
  - ko
tags:
  - tokforge
  - on-device
  - mnn
  - qwen3.5
  - mobile
  - abliterated
  - linear-attention
---

# Qwen3.5 4B Claude 4.6 Opus abliterated (MNN)

huihui-ai's abliteration of Jackrong's Claude 4.6 Opus reasoning distill of Qwen3.5 4B, as a 4-bit MNN bundle for chatting on your phone in TokForge.

Published by [TokForge](https://tokforge.ai) for on-device inference.

| | |
|---|---|
| **What it is** | Reasoning chat model |
| **Format** | MNN bundle, 4-bit weights (block 128), text only |
| **Runs on** | Android phones (CPU) |
| **Phone class** | No catalog class; needs more free RAM than its 2.37 GB main weights file |
| **Download** | 2.38 GB (7 files) |
| **Base model** | [huihui-ai/Huihui-Qwen3.5-4B-Claude-4.6-Opus-abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-4B-Claude-4.6-Opus-abliterated) |
| **License** | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## TokForge

- **Website:** https://tokforge.ai
- **Discord:** https://discord.gg/Acv3CBtfVm
- **Google Play:** https://play.google.com/store/apps/details?id=dev.tokforge
- **iOS TestFlight:** https://testflight.apple.com/join/jnufjzRr

Runs on-device in the TokForge app.

## Use it in TokForge

1. Install TokForge from [Google Play](https://play.google.com/store/apps/details?id=dev.tokforge), or join the [iOS TestFlight](https://testflight.apple.com/join/jnufjzRr).
2. On Android, open **Models > Browse**, search for `Qwen3.5-4B-Claude-4.6-Opus-abliterated-MNN` and download it.
3. Load it and start a chat. The model runs on the phone; once it is downloaded, chatting needs no connection.

On phones with a Snapdragon 8 Elite Gen 5 or Snapdragon 8 Gen 3, TokForge can also add an NPU prompt pack for this model,
[darkmaniac7/Qwen3.5-4B-Claude-4.6-Opus-abliterated-NPU-catalogpair](https://huggingface.co/darkmaniac7/Qwen3.5-4B-Claude-4.6-Opus-abliterated-NPU-catalogpair):
the NPU reads long prompts and the CPU writes the reply. TokForge downloads it only when you ask for it (**Get** under
**NPU packs for your phone** in **Models > Browse**, or **Faster long prompts (NPU)** in the model's settings).

Collections: [TokForge Qwen Models (MNN)](https://huggingface.co/collections/darkmaniac7/tokforge-qwen-models-mnn-69cc8b98317551109a7ae907).

## Files

| File | Size | What it is |
|---|---:|---|
| `config.json` | 210 B | MNN runtime settings |
| `export_args.json` | 1.17 KB | Export settings used for the conversion |
| `llm.mnn` | 3.65 MB | Model graph |
| `llm.mnn.json` | 9.17 MB | Model graph as JSON (reference copy) |
| `llm.mnn.weight` | 2.37 GB | Model weights |
| `llm_config.json` | 4.54 KB | Model settings and chat template |
| `tokenizer.txt` | 2.96 MB | Tokenizer |

## About the model

Pre-converted [Huihui-Qwen3.5-4B-Claude-4.6-Opus-abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-4B-Claude-4.6-Opus-abliterated) (huihui-ai's abliteration of Jackrong's Claude 4.6 Opus reasoning distill of [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)) in MNN format for on-device inference.

Jackrong trained Qwen3.5 4B on reasoning outputs from Claude 4.6 Opus; huihui-ai then removed its refusal behavior
(abliteration), so it declines fewer requests. It thinks step by step before it answers.

| | |
|---|---|
| **Architecture** | Qwen3.5 (hybrid LinearAttention + standard attention), text only |
| **Parameters** | 4B (4-bit quantized) |
| **Quantization** | W4A16 (4-bit weights, 16-bit activations), block size 128 |
| **Attention** | LinearAttention (gated_delta_rule) + standard attention hybrid |
| **Backend** | CPU is recommended for Qwen3.5 models (LinearAttention runs natively on CPU), and it is TokForge's default |

## Limitations

- Intended for TokForge / MNN on-device inference, especially creative writing and roleplay use.
- `Qwen3.5` hybrid LinearAttention models generally route best to CPU in current TokForge builds.
- Performance varies by device class and generation length.
- This repo is a packaged runtime artifact, not a standard Transformers training checkpoint.
- Abliterated: refusal behavior removed. Use responsibly.

## License

Apache-2.0, as Qwen3.5 4B, Jackrong's distill and huihui-ai's abliteration.

## Credits

- Huihui-Qwen3.5-4B-Claude-4.6-Opus-abliterated by huihui-ai ([Hugging Face](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-4B-Claude-4.6-Opus-abliterated)). Used under the Apache-2.0 license. Our MNN files were converted from this model.
- Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled by Jackrong ([Hugging Face](https://huggingface.co/Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled)). Used under the Apache-2.0 license. Reasoning-distilled from Claude 4.6 Opus outputs; not an Anthropic release.
- Qwen3.5-4B by the Qwen team (Alibaba Cloud) ([Hugging Face](https://huggingface.co/Qwen/Qwen3.5-4B)). Used under the Apache-2.0 license.
- Converted with llmexport from [MNN](https://github.com/alibaba/MNN) by Alibaba (Apache-2.0).
