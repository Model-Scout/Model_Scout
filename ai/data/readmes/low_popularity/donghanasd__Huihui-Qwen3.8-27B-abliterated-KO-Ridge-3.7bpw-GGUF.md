---
license: apache-2.0
language:
  - ko
  - en
library_name: llama.cpp
pipeline_tag: text-generation
inference: false
base_model:
  - huihui-ai/Huihui-Qwen3.8-27B-abliterated
tags:
  - gguf
  - llama.cpp
  - qwen3.8
  - korean
  - abliterated
  - quantized
  - imatrix
  - ridge
  - dflash2
  - speculative-decoding
---

# Huihui-Qwen3.8-27B-abliterated KO Ridge 3.7bpw GGUF

A 3.69 BPW mixed-tensor GGUF tuned to run **Huihui Qwen3.8 27B Abliterated** with a **Qwen3.8 DFlash 2** draft on an **NVIDIA RTX 5060 Ti 16 GB** using `llama.cpp`.

이 저장소는 **RTX 5060 Ti 16GB 한 장**에서 Huihui Qwen3.8 27B Abliterated와 DFlash 2를 함께 실행하기 위한 3.69 BPW 혼합 텐서 GGUF입니다. 한국어/영어 importance matrix와 Ridge 계열 텐서 배치를 사용했습니다.

## Files

| File | Size | Description |
| --- | ---: | --- |
| `Huihui-Qwen3.8-27B-abliterated-KO-Ridge-3.7bpw.gguf` | 12.60 GB | Target model, 3.69 BPW |
| `run-rtx5060ti.sh` | small | Safe localhost-oriented `llama-server` launcher |

The DFlash 2 draft is not duplicated here. Download `Qwen3.8-27B-DFlash2-Q4_K_M.gguf` from [`z-lab/Qwen3.8-27B-DFlash2-GGUF`](https://huggingface.co/z-lab/Qwen3.8-27B-DFlash2-GGUF).

## Important quantization note

This model was **requantized from the KO-i1 Q8_0 GGUF**, not directly from BF16. Requantization can lose more quality than a single BF16-to-GGUF conversion. The source Q8_0 and Korean/English importance matrix come from [`augustine223/Huihui-Qwen3.8-27B-abliterated-KO-i1-GGUF`](https://huggingface.co/augustine223/Huihui-Qwen3.8-27B-abliterated-KO-i1-GGUF).

The tensor layout follows the size/quality strategy of [`empero-ai/Qwen3.8-27B-Ridge-GGUF`](https://huggingface.co/empero-ai/Qwen3.8-27B-Ridge-GGUF):

| GGML type | Tensor count |
| --- | ---: |
| F32 | 360 |
| Q8_0 | 96 |
| Q4_K | 144 |
| Q5_K | 51 |
| Q6_K | 23 |
| IQ3_S | 32 |
| IQ2_S | 160 |
| **Total** | **866** |

The resulting target is 12,599,186,976 bytes, 12,005.04 MiB, and 3.69 BPW.

SHA-256:

```text
4f72d4e3b6723fb259e7f8244c70fbf2850151aab3745d8c1e84768fba161515
```

## Tested RTX 5060 Ti 16 GB profile

Tested locally with a Blackwell RTX 5060 Ti, CUDA 13.1, a DFlash 2-enabled `llama.cpp` build, and the Q4_K_M DFlash draft.

| Setting | Tested value |
| --- | --- |
| GPU | NVIDIA GeForce RTX 5060 Ti 16 GB |
| CUDA architecture | `sm_120` |
| Target GGUF | This 3.69 BPW mixed quant |
| Draft GGUF | Qwen3.8-27B-DFlash2-Q4_K_M, 1.14 GB |
| Runtime context | 131,072 tokens |
| Trained context metadata | 262,144 tokens |
| Main KV cache | Q4_0 / Q4_0 |
| Draft KV cache | Q4_0 / Q4_0 |
| Slots / parallel | 1 / 1 |
| DFlash maximum draft | 4 tokens |
| Observed VRAM after load and generation | about 15,350 MiB / 16,311 MiB |

Short smoke-test results were approximately 44.7 tok/s on the first generation and 62.6 tok/s on a cached short request. These are not full benchmark results; prompt length, sampler, CPU, driver, and draft acceptance change throughput.

If your system has less free VRAM, lower `CTX` first, for example `CTX=65536` or `CTX=32768`.

## 1. Download

Install the Hugging Face CLI if needed, then download the target and draft into one directory:

```bash
python3 -m pip install -U "huggingface_hub[hf_xet]"

hf download \
  donghanasd/Huihui-Qwen3.8-27B-abliterated-KO-Ridge-3.7bpw-GGUF \
  Huihui-Qwen3.8-27B-abliterated-KO-Ridge-3.7bpw.gguf \
  --local-dir .

hf download \
  z-lab/Qwen3.8-27B-DFlash2-GGUF \
  Qwen3.8-27B-DFlash2-Q4_K_M.gguf \
  --local-dir .
```

## 2. Build llama.cpp with DFlash 2

DFlash 2 support is available through [`llama.cpp` PR #27342](https://github.com/ggml-org/llama.cpp/pull/27342). The following is the tested NVIDIA build shape:

```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
git fetch origin pull/27342/head:pr-27342
git switch pr-27342

cmake -S . -B build -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DGGML_CUDA=ON \
  -DGGML_CUDA_FA=ON \
  -DGGML_CUDA_GRAPHS=ON \
  -DCMAKE_CUDA_ARCHITECTURES=120

cmake --build build --target llama-server -j
```

If the PR has already been merged into your `llama.cpp` version, a current checkout with `--spec-type draft-dflash` support can be used instead.

## 3. Run llama-server

Download `run-rtx5060ti.sh`, place it next to both GGUF files, and point it at the built server:

```bash
chmod +x run-rtx5060ti.sh
LLAMA_SERVER=/path/to/llama.cpp/build/bin/llama-server ./run-rtx5060ti.sh
```

Equivalent core command:

```bash
GGML_CUDA_PDL=0 \
GGML_CUDA_ENABLE_UNIFIED_MEMORY=1 \
/path/to/llama-server \
  --host 127.0.0.1 --port 8080 \
  --model Huihui-Qwen3.8-27B-abliterated-KO-Ridge-3.7bpw.gguf \
  --model-draft Qwen3.8-27B-DFlash2-Q4_K_M.gguf \
  --jinja --no-mmproj \
  -ngl 99 --spec-draft-ngl 99 \
  --spec-type draft-dflash \
  --spec-draft-n-max 4 --spec-draft-n-min 1 \
  -fa on --ctx-size 131072 \
  --cache-type-k q4_0 --cache-type-v q4_0 \
  --spec-draft-type-k q4_0 --spec-draft-type-v q4_0 \
  --parallel 1 --kv-unified --fit off --no-context-shift \
  --batch-size 512 --ubatch-size 128 \
  --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.0 \
  --reasoning on --reasoning-budget -1 --reasoning-preserve
```

Health check:

```bash
curl http://127.0.0.1:8080/health
```

OpenAI-compatible request:

```bash
curl http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "huihui-qwen3.8-27b-ko-ridge",
    "messages": [{"role": "user", "content": "안녕하세요!"}],
    "max_tokens": 512,
    "temperature": 1.0,
    "top_p": 0.95
  }'
```

This is a reasoning model. Small `max_tokens` values can be consumed entirely by `reasoning_content`, leaving `content` empty. Use a larger limit for normal chat.

## Security

The supplied launcher binds to `127.0.0.1` by default. It refuses a non-loopback bind unless `API_KEY` is set. Do not expose an unauthenticated `llama-server` directly to the internet.

Example LAN bind with authentication:

```bash
HOST=0.0.0.0 API_KEY='replace-with-a-strong-secret' \
LLAMA_SERVER=/path/to/llama-server ./run-rtx5060ti.sh
```

Do not commit API keys or tokens to a repository.

## Compatibility and limitations

- This release is text-only in the tested configuration (`--no-mmproj`).
- The final MTP/next-token-prediction tensors are retained in the GGUF, but the tested target graph ignores them while the external DFlash 2 draft handles speculative decoding.
- DFlash 2 verifies draft tokens against the target model. Acceptance and speed can differ from the base Qwen checkpoint because this target is an abliterated derivative.
- The model is an abliterated/uncensored derivative. It may generate unsafe, inaccurate, biased, or objectionable content. Users are responsible for lawful and appropriate use.
- The 262K trained-context metadata does not mean 262K will fit on a 16 GB GPU. The validated 16 GB profile is 128K with quantized KV caches and one slot.

## Provenance and credits

- Base architecture: [`Qwen/Qwen3.8-27B`](https://huggingface.co/Qwen/Qwen3.8-27B)
- Abliterated model: [`huihui-ai/Huihui-Qwen3.8-27B-abliterated`](https://huggingface.co/huihui-ai/Huihui-Qwen3.8-27B-abliterated)
- KO-i1 Q8_0 and importance matrix: [`augustine223/Huihui-Qwen3.8-27B-abliterated-KO-i1-GGUF`](https://huggingface.co/augustine223/Huihui-Qwen3.8-27B-abliterated-KO-i1-GGUF)
- Ridge tensor-layout reference: [`empero-ai/Qwen3.8-27B-Ridge-GGUF`](https://huggingface.co/empero-ai/Qwen3.8-27B-Ridge-GGUF)
- DFlash 2 GGUF: [`z-lab/Qwen3.8-27B-DFlash2-GGUF`](https://huggingface.co/z-lab/Qwen3.8-27B-DFlash2-GGUF)
- DFlash project: [`z-lab/dflash`](https://github.com/z-lab/dflash)
- Runtime: [`ggml-org/llama.cpp`](https://github.com/ggml-org/llama.cpp)

All referenced model repositories report Apache-2.0 licensing. This repository is released under Apache-2.0. Follow the licenses and terms of every upstream component.

## DFlash 2 citation

```bibtex
@misc{inco2026dflash2,
  title  = {{DFlash 2: Keep Drafting Parallel}},
  author = {{Inco AI}},
  year   = {2026},
  month  = {August},
  url    = {https://inco.ai/blog/dflash2/}
}
```
