---
license: apache-2.0
base_model: skt/A.X-K2
base_model_relation: quantized
tags:
  - gguf
  - llama.cpp
  - vllm
  - quantized
  - skt
  - a.x
  - conversational
pipeline_tag: text-generation
library_name: gguf
language:
  - en
  - ko
  - zh
  - ja
  - es
---

# A.X K2 GGUF

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)"
            srcset="https://huggingface.co/skt/A.X-K2/resolve/main/assets/A.X_K2_BI_Negative.png">
    <img src="https://huggingface.co/skt/A.X-K2/resolve/main/assets/A.X_K2_BI_Primary.png" alt="A.X Logo" width="300">
  </picture>
</div>
<p align="center">
  <a href="https://huggingface.co/skt/A.X-K2">🤗 Original model</a> |
  <a href="https://huggingface.co/collections/skt/ax-k2">🤗 Collection</a> |
  <a href="https://github.com/SKT-AI/A.X-K2">🖥️ Github</a> |
  <a href="https://github.com/SKT-AI/A.X-K2/blob/main/A_X_K2_Tech_Report.pdf">📄 Technical Report</a>
</p>

This repository contains a quantized GGUF build of
[**skt/A.X-K2**](https://huggingface.co/skt/A.X-K2).

A.X K2 is a Mixture-of-Experts model with 688B parameters, 33B of them active per token,
released in block-scaled FP8. The file here is converted from that checkpoint and quantized to
the format in [Model files](#model-files).

The [original model card](https://huggingface.co/skt/A.X-K2) covers the architecture, training data,
benchmarks, intended use and limitations. This card only adds what is specific to the GGUF build.

## Model files

| File | Size | Bits-per-weight |
|---|---:|---:|
| `A.X-K2-IQ4_XS.gguf` | 345 GiB | 4.30 |

```bash
hf download skt/A.X-K2-GGUF --include "A.X-K2-IQ4_XS.gguf" --local-dir .
MODEL=$PWD/A.X-K2-IQ4_XS.gguf     # absolute, so it survives cd into a source tree
```

Tensors left at full precision include `output.weight`,
`token_embd.weight`, the Gated Norm projections (`*norm_gate_a/b.weight`), the
sparse-attention indexer projection (`*indexer.proj.weight`), and the MoE router
(`*ffn_gate_inp.weight`).

## Run with llama.cpp

Official llama.cpp does not support A.X K2 yet, so build from the
[A.X-K2 fork](https://github.com/cys4/llama.cpp). It is upstream `b10236` plus A.X K2 support,
and nothing else:

```bash
git clone -b axk2-b10236 https://github.com/cys4/llama.cpp.git
cd llama.cpp

cmake -B build -DGGML_CUDA=ON     # CUDA; omit -DGGML_CUDA=ON for a CPU-only build
cmake --build build -j
```

For anything the examples do not cover, see the
[llama.cpp documentation](https://github.com/ggml-org/llama.cpp#documentation) - it all applies
here, as long as you build the fork above.

### CLI

```bash
./build/bin/llama-cli -m "$MODEL" --temp 0.6 --top-p 0.95 -st -p "대한민국의 수도는?" \
  --reasoning on     # thinking mode; --reasoning off for non-thinking
```

`--temp` and `--top-p` control the sampling: lower temperature is more deterministic, and top-p
caps the cumulative probability of the token pool.

`-st` runs a single turn: `llama-cli` answers the prompt and exits. Without it, the CLI stays
open for interactive chat.

### Server

```bash
./build/bin/llama-server -m "$MODEL" --temp 0.6 --top-p 0.95 \
  --host 0.0.0.0 --port 8080 \
  --reasoning on     # thinking mode; --reasoning off for non-thinking
```

The server exposes an OpenAI-compatible API at `http://localhost:8080/v1`. `--host 0.0.0.0` lets
other machines connect (the default is `127.0.0.1` only), and `--port` picks the port (8080 is
already the default).

```bash
curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json" -d '{
  "messages": [{"role": "user", "content": "대한민국의 수도는?"}]
}'
```

## Run with vLLM

> Note: [GGUF support in vLLM](https://docs.vllm.ai/en/latest/features/quantization/gguf/) is
> experimental and under-optimized upstream, positioned mainly as a way to reduce memory
> footprint. For best GGUF performance use llama.cpp above.

The same GGUF file can also be served with vLLM. Like llama.cpp above, this needs a custom
build: official vLLM does not load A.X K2 GGUFs, so install vLLM from the
[A.X-K2 vLLM fork](https://github.com/cys4/vllm_axk2/tree/axk2-v0.23.0_gguf), branch
`axk2-v0.23.0_gguf`, which carries the A.X K2 GGUF loading support:

```bash
git clone -b axk2-v0.23.0_gguf https://github.com/cys4/vllm_axk2.git
cd vllm_axk2
VLLM_USE_PRECOMPILED=1 pip install -e .
```

The fork is python-only on top of upstream vLLM, so `VLLM_USE_PRECOMPILED=1` reuses the
matching precompiled wheel and no CUDA build is needed.

The `vllm_hf_config/` folder in this repository carries the config and tokenizer vLLM needs:
the original `config.json` with `quantization_config` removed (the FP8 declaration would
conflict with GGUF loading) plus the unmodified tokenizer and chat template.

```bash
hf download skt/A.X-K2-GGUF --include "vllm_hf_config/*" --local-dir "$(dirname "$MODEL")"
CONFIG="$(dirname "$MODEL")/vllm_hf_config"

vllm serve "$MODEL" \
  --hf-config-path "$CONFIG" --tokenizer "$CONFIG" -tp 8 \
  --host 0.0.0.0 --port 8000 \
  --default-chat-template-kwargs '{"enable_thinking": true}'     # thinking mode; false for non-thinking
```

The server exposes the same OpenAI-compatible API at `http://localhost:8000/v1`, so query it like
`llama-server` above, with the port changed. `vllm_hf_config/` also ships
`generation_config.json`, which carries the sampling defaults (`temperature`, `top_p`).

## Contact

For questions about A.X K2 — including model behavior, deployment, and licensing — contact the A.X team at **[a.x@sk.com](mailto:a.x@sk.com)**. Please send reports of vulnerabilities, harmful outputs, suspected misuse, or copyright infringement claims to the same address.

## Citation

If you use A.X K2 in your research, please cite the technical report:

```bibtex
@techreport{axk2-2026,
      title={A.X K2 Technical Report},
      author={SK Telecom},
      year={2026},
      institution={SK Telecom},
      url={https://github.com/SKT-AI/A.X-K2/blob/main/A_X_K2_Tech_Report.pdf},
}
```
