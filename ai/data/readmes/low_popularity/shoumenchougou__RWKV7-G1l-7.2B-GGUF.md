---
license: apache-2.0
pipeline_tag: text-generation
base_model: BlinkDL/rwkv7-g1
language:
  - en
  - zh
  - fr
  - es
  - de
  - pt
  - ru
  - it
  - ja
  - ko
  - vi
  - ar
tags:
  - rwkv
  - rwkv7
  - recurrent
  - causal-lm
  - gguf
  - llama.cpp
  - ollama
---

<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->

<div align="center">
  <a href="https://www.rwkv.com/">
    <img src="assets/rwkv-logo.webp" width="140" alt="RWKV logo" />
  </a>
  <h1>RWKV7-G1l-7.2B-GGUF</h1>
  <p><strong>RWKV-7 “Goose” for local inference with Ollama and llama.cpp</strong></p>
</div>

<div align="center">
  <a href="https://www.rwkv.com/"><img alt="RWKV website" src="https://img.shields.io/badge/Website-RWKV-16a7c9" /></a>
  <a href="https://huggingface.co/BlinkDL/rwkv7-g1"><img alt="Source model" src="https://img.shields.io/badge/Source-BlinkDL%2Frwkv7--g1-ffc107" /></a>
  <a href="https://github.com/BlinkDL/RWKV-LM"><img alt="RWKV GitHub" src="https://img.shields.io/badge/GitHub-RWKV--LM-181717?logo=github" /></a>
  <a href="https://arxiv.org/abs/2503.14456v2"><img alt="RWKV-7 paper" src="https://img.shields.io/badge/Paper-arXiv%3A2503.14456-b31b1b" /></a>
  <a href="./LICENSE"><img alt="Apache 2.0 license" src="https://img.shields.io/badge/License-Apache--2.0-4c8bf5" /></a>
</div>

---

This repository provides the **RWKV-7 G1l 7.2B base model** in GGUF format for local text generation. Start with `Q4_K_M`, the formal Ollama default for this model size, or choose another file to balance storage, runtime memory, and weight precision.

> [!IMPORTANT]
> This is a base language model, not a safety-aligned instruction-tuned assistant. The prompt formats below provide a conversational interface, but the model may not follow instructions consistently.

## About RWKV-7

RWKV-7, also called **Goose**, is an attention-free recurrent language model. It keeps a constant-size recurrent state instead of an attention KV cache that grows with the preceding sequence. This gives RWKV constant recurrent-state size and constant inference work per generated token, while training remains parallelizable.

The fixed-state property describes the architecture's sequence state. Total memory use still depends on the selected weights, runtime, context configuration, batch size, and hardware backend.

`G1l` identifies this checkpoint revision. The original checkpoint is available from [`BlinkDL/rwkv7-g1`](https://huggingface.co/BlinkDL/rwkv7-g1/blob/11e3c50128e479898eee79c48831a95cf3e21d91/rwkv7-g1l-7.2b-20261031-ctx34304.pth). That immutable source file is 14,400,007,869 bytes with SHA-256 `ce81c2d568bc9fc8c9f7b8ddb47da070d88bf179827b311f221e1e6c5148af91`.

## Choose a file

| File | Size | When to choose it |
| --- | ---: | --- |
| `rwkv7-g1l-7.2b-Q4_K_M.gguf` | `4.27 GiB` | Recommended starting point and the formal Ollama default for this model size. |
| `rwkv7-g1l-7.2b-Q5_K_M.gguf` | `5.02 GiB` | A middle option between Q4 and Q6. |
| `rwkv7-g1l-7.2b-Q6_K.gguf` | `5.81 GiB` | A larger quantized option when weight precision matters more than size. |
| `rwkv7-g1l-7.2b-Q8_0.gguf` | `7.39 GiB` | Largest quantized option in this repository. |
| `rwkv7-g1l-7.2b-20261031-ctx34304-FP16.gguf` | `13.48 GiB` | Mostly-F16 weights; use when model size is less important. |

Smaller quantizations generally reduce storage and runtime memory at the cost of some output quality. File size is not a guarantee of total RAM or VRAM use.

### File integrity

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `rwkv7-g1l-7.2b-Q4_K_M.gguf` | `4,579,571,648` | `a2ffb4f76a06a08c1d1146aa735bfafb51dbd04f4e5d0fd085c9c80b631ed00f` |
| `rwkv7-g1l-7.2b-Q5_K_M.gguf` | `5,384,878,016` | `b7989f3dde247579b8333eb1f126e050a807f793caa9039e3b04d818ffabb75e` |
| `rwkv7-g1l-7.2b-Q6_K.gguf` | `6,240,516,032` | `75f1530de150a0876cd36cc2e19c32b181026061d04aaed681baa0348074ec7c` |
| `rwkv7-g1l-7.2b-Q8_0.gguf` | `7,930,820,544` | `a3894649424b4926e74e0c8473adfdd24af6601a88602f4d2a86a9749119de1b` |
| `rwkv7-g1l-7.2b-20261031-ctx34304-FP16.gguf` | `14,473,934,784` | `e712dc340e0d881e841d54df58bc85a4aeea7994bf36ffcbb0fda689a5fefa18` |

Verify a downloaded file with `sha256sum <filename>` on Linux or `Get-FileHash <filename> -Algorithm SHA256` in PowerShell.

## Run with Ollama

Install Ollama 0.33.2 or later with RWKV-7 support. The formal 7.2B setup uses the `Q4_K_M` file and the included `Modelfile.ollama`.

### 1. Download the model

With the [Hugging Face `hf` CLI](https://huggingface.co/docs/huggingface_hub/guides/cli):

```shell
hf download shoumenchougou/RWKV7-G1l-7.2B-GGUF rwkv7-g1l-7.2b-Q4_K_M.gguf Modelfile.ollama --local-dir rwkv7-g1l-7.2b
cd rwkv7-g1l-7.2b
```

You can instead download both files from the repository's file browser and place them in the same directory.

### 2. Create and run the Ollama model

```shell
ollama create rwkv7-g1l:7.2b -f Modelfile.ollama
ollama run rwkv7-g1l:7.2b
```

The setup is complete when `ollama create` reports success and `ollama run` returns generated text. This release passed Q4_K_M import, embedded-template rendering in thinking and non-thinking modes, and non-empty generation with a 34,304-token context setting.

The included Modelfile selects Q4_K_M, declares the minimum Ollama version, records the license, and sets the release context and sampling defaults:

```dockerfile
FROM ./rwkv7-g1l-7.2b-Q4_K_M.gguf
REQUIRES 0.33.2
LICENSE """
Apache License 2.0
https://www.apache.org/licenses/LICENSE-2.0
"""
PARAMETER num_ctx 34304
PARAMETER temperature 1
PARAMETER top_k 128
PARAMETER top_p 0.5
PARAMETER frequency_penalty 0.5
PARAMETER presence_penalty 0.5
PARAMETER repeat_penalty 1
PARAMETER stop """

"""
```

The Modelfile intentionally does not define `TEMPLATE`. The GGUF files must contain the validated Jinja chat template in `tokenizer.chat_template`; Ollama and llama.cpp can then read it directly from the selected model. Adding an external Ollama `TEMPLATE` would override that embedded source of truth.

Keep the `stop` value on three lines as shown. Ollama 0.33.2 parses the triple-quoted blank line as two newline characters; writing the escaped text `\n\n` instead stores literal backslashes.

See Ollama's official guides for [importing a GGUF model](https://docs.ollama.com/import) and the complete [Modelfile reference](https://docs.ollama.com/modelfile).

## Run with llama.cpp

Use a recent [llama.cpp](https://github.com/ggml-org/llama.cpp) build that recognizes the `rwkv7` architecture. From the directory containing the GGUF file, run:

```shell
llama-cli -m rwkv7-g1l-7.2b-Q4_K_M.gguf -c 34304 -n 256 -cnv
```

The files were structurally validated with the locked llama.cpp GGUF tooling. Runtime validation used the included Q4_K_M file through Ollama; direct llama.cpp generation was not part of this release check.

## Prompt format

Runtimes that honor the embedded chat template apply the format automatically. After conversion, template inspection must confirm the standard and thinking-mode prefixes before publication.

For raw completion interfaces, use one of these generation prefixes.

**Standard response:**

```text
User: Explain why recurrent models can use constant state.

Assistant:
```

**Thinking response:**

```text
User: Solve the problem step by step.

Assistant: <think>
```

If your runtime requires explicit stop conditions, use token ID `0` or the text sequence `\n\nUser:`.

## Context length

Use **34,304 tokens** as the release context setting. Some GGUF inspection tools may display `1,048,576` from the RWKV-7 architecture metadata; that value is an architectural capacity field, not a claim that this checkpoint was trained or validated at that length.

If your runtime cannot allocate the requested context, lower the context value. This reduces the amount of preceding text available to the model.

## Model details

| Field | Value |
| --- | --- |
| Architecture | RWKV-7 “Goose” |
| Checkpoint revision | G1l, released 2026-10-31 |
| Model type | Base causal language model |
| Original checkpoint tensors | 1,062, all BF16 |
| Original checkpoint parameters | 7,199,932,416 |
| Expected GGUF tensor elements | 7,200,194,560 |
| Layers | 32 |
| Hidden size | 4,096 |
| FFN size | 16,384 |
| Heads / head size | 64 / 64 |
| Vocabulary size | 65,536 |
| Release context | 34,304 tokens |
| Expected format after conversion | GGUF v3; 902 tensors |
| License | Apache License 2.0 |

The effective head count is 64 (`4,096 / 64`). GGUF inspectors may also show `rwkv7.attention.head_count = 0`; llama.cpp reserves that field but does not use it for RWKV-7.

## Compatibility and troubleshooting

| Symptom | What to do |
| --- | --- |
| The runtime reports an unknown `rwkv7` architecture | Update to a recent Ollama or llama.cpp build with RWKV-7 support. |
| Ollama cannot find the GGUF file | Keep `Modelfile.ollama` and the Q4_K_M file in the same directory, or change `FROM` to the correct path. |
| A valid GGUF cannot be opened from a Windows path | Move the files to a short ASCII-only path such as `C:\models\rwkv7` and try again. |
| The model does not follow the requested instruction | Confirm that the embedded template is active, or use the raw prompt format above. Remember that this is a base model. |
| The model does not fit in memory | Use Q4_K_M, close other memory-heavy applications, or reduce the configured context length. |

Runtime support changes over time. All five files passed GGUF v3 structure, bounds, metadata, tensor-count, embedded-template, size, and SHA-256 validation. Q4_K_M additionally passed Ollama import, template rendering, and real generation.

## Limitations

- Quantization can change model outputs, and the effect varies by task.
- This release does not claim systematic benchmark parity between quantizations.
- The model may produce inaccurate, biased, unsafe, or otherwise undesirable text.
- The model is not a substitute for qualified professional judgment in high-stakes settings.
- The presence of chat and thinking prompts does not make the base model reliably instruction-following or safety-aligned.

## License

The model is distributed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). Review the source repository and license terms before redistribution or deployment.

## Links

- [RWKV website](https://www.rwkv.com/)
- [Original G1l checkpoint](https://huggingface.co/BlinkDL/rwkv7-g1/blob/11e3c50128e479898eee79c48831a95cf3e21d91/rwkv7-g1l-7.2b-20261031-ctx34304.pth)
- [RWKV-LM repository](https://github.com/BlinkDL/RWKV-LM)
- [RWKV-7 paper](https://arxiv.org/abs/2503.14456v2)
- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Ollama documentation](https://docs.ollama.com/)

## Citation

```bibtex
@misc{peng2025250314456,
  title         = {RWKV-7 "Goose" with Expressive Dynamic State Evolution},
  author        = {Bo Peng and Ruichong Zhang and Daniel Goldstein and Eric Alcaide and Xingjian Du and Haowen Hou and Jiaju Lin and Jiaxing Liu and Janna Lu and William Merrill and Guangyu Song and Kaifeng Tan and Saiteja Utpala and Nathan Wilce and Johan S. Wind and Tianyi Wu and Daniel Wuttke and Christian Zhou-Zheng},
  year          = {2025},
  eprint        = {2503.14456v2},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2503.14456v2},
}
```
