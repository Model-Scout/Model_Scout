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
  <h1>RWKV7-G1k-13.3B-GGUF</h1>
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

This repository provides the **RWKV-7 G1k 13.3B base model** in GGUF format for local text generation. Start with `Q4_K_M`, the formal Ollama default for this model size, or choose another file to balance storage, runtime memory, and weight precision.

> [!IMPORTANT]
> This is a base language model, not a safety-aligned instruction-tuned assistant. The prompt formats below provide a conversational interface, but the model may not follow instructions consistently.

## About RWKV-7

RWKV-7, also called **Goose**, is an attention-free recurrent language model. It keeps a constant-size recurrent state instead of an attention KV cache that grows with the preceding sequence. This gives RWKV constant recurrent-state size and constant inference work per generated token, while training remains parallelizable.

The fixed-state property describes the architecture's sequence state. Total memory use still depends on the selected weights, runtime, context configuration, batch size, and hardware backend.

`G1k` identifies this checkpoint revision. The original checkpoint is available from [`BlinkDL/rwkv7-g1`](https://huggingface.co/BlinkDL/rwkv7-g1/blob/e74b6f6a128d3097e88e85642d59e0962ce6d2e4/rwkv7-g1k-13.3b-20260930-ctx25600.pth). That immutable source file is 26,540,868,485 bytes with SHA-256 `31799b3f8207e74c1b47f359184ac1c658c927ff697971447f7bf0fd18ae393f`.

## Choose a file

| File | Size | When to choose it |
| --- | ---: | --- |
| `rwkv7-g1k-13.3b-Q4_K_M.gguf` | `7.88 GiB` | Recommended starting point and the formal Ollama default for this model size. |
| `rwkv7-g1k-13.3b-Q5_K_M.gguf` | `9.31 GiB` | A middle option between Q4 and Q6. |
| `rwkv7-g1k-13.3b-Q6_K.gguf` | `10.83 GiB` | A larger quantized option when weight precision matters more than size. |
| `rwkv7-g1k-13.3b-Q8_0.gguf` | `13.72 GiB` | Largest quantized option in this repository. |
| `rwkv7-g1k-13.3b-20260930-ctx25600-FP16.gguf` | `24.91 GiB` | Mostly-F16 weights; use when model size is less important. |

Smaller quantizations generally reduce storage and runtime memory at the cost of some output quality. File size is not a guarantee of total RAM or VRAM use.

### File integrity

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `rwkv7-g1k-13.3b-Q4_K_M.gguf` | `8,457,371,584` | `dc2f04a81d7fc0602b3954b86992c0c4b036835cc982d5afd4173c21a5a60a13` |
| `rwkv7-g1k-13.3b-Q5_K_M.gguf` | `9,992,486,848` | `be1240a419a34086144251eb8ee6670d33b183add1daa1f3e34315f5ae82459b` |
| `rwkv7-g1k-13.3b-Q6_K.gguf` | `11,623,546,816` | `062b2ee432e038c18ab3c16727ad2584200bd70fb535735ecc9e297298a7c840` |
| `rwkv7-g1k-13.3b-Q8_0.gguf` | `14,727,856,064` | `fb68b350b302e6d881f2b8eca44ebc52a06d8c4473466c35f5446cee3181f639` |
| `rwkv7-g1k-13.3b-20260930-ctx25600-FP16.gguf` | `26,744,537,024` | `21b7beb047cd0c930f5077d6cdaaae6e1069e36aa6b8b2aee3813b53820c97d1` |

Verify a downloaded file with `sha256sum <filename>` on Linux or `Get-FileHash <filename> -Algorithm SHA256` in PowerShell.

## Run with Ollama

Install Ollama 0.33.2 or later with RWKV-7 support. The formal 13.3B setup uses the `Q4_K_M` file and the included `Modelfile.ollama`.

### 1. Download the model

With the [Hugging Face `hf` CLI](https://huggingface.co/docs/huggingface_hub/guides/cli):

```shell
hf download shoumenchougou/RWKV7-G1k-13.3B-GGUF rwkv7-g1k-13.3b-Q4_K_M.gguf Modelfile.ollama --local-dir rwkv7-g1k-13.3b
cd rwkv7-g1k-13.3b
```

You can instead download both files from the repository's file browser and place them in the same directory.

### 2. Create and run the Ollama model

```shell
ollama create rwkv7-g1k:13.3b -f Modelfile.ollama
ollama run rwkv7-g1k:13.3b
```

The setup is complete when `ollama create` reports success and `ollama run` returns generated text. This release passed Q4_K_M import, embedded-template rendering in thinking and non-thinking modes, and non-empty generation with a 25,600-token context setting.

The included Modelfile selects Q4_K_M, declares the minimum Ollama version, records the license, and sets the release context and sampling defaults:

```dockerfile
FROM ./rwkv7-g1k-13.3b-Q4_K_M.gguf
REQUIRES 0.33.2
LICENSE """
Apache License 2.0
https://www.apache.org/licenses/LICENSE-2.0
"""
PARAMETER num_ctx 25600
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
llama-cli -m rwkv7-g1k-13.3b-Q4_K_M.gguf -c 25600 -n 256 -cnv
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

Use **25,600 tokens** as the release context setting. Some GGUF inspection tools may display `1,048,576` from the RWKV-7 architecture metadata; that value is an architectural capacity field, not a claim that this checkpoint was trained or validated at that length.

If your runtime cannot allocate the requested context, lower the context value. This reduces the amount of preceding text available to the model.

## Model details

| Field | Value |
| --- | --- |
| Architecture | RWKV-7 “Goose” |
| Checkpoint revision | G1k, released 2026-09-30 |
| Model type | Base causal language model |
| Original checkpoint tensors | 2,019, all BF16 |
| Original checkpoint parameters | 13,270,298,624 |
| Expected GGUF tensor elements | 13,270,822,912 |
| Layers | 61 |
| Hidden size | 4,096 |
| FFN size | 16,384 |
| Heads / head size | 64 / 64 |
| Vocabulary size | 65,536 |
| Release context | 25,600 tokens |
| Expected format after conversion | GGUF v3; 1,714 tensors |
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
- [Original G1k checkpoint](https://huggingface.co/BlinkDL/rwkv7-g1/blob/e74b6f6a128d3097e88e85642d59e0962ce6d2e4/rwkv7-g1k-13.3b-20260930-ctx25600.pth)
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
