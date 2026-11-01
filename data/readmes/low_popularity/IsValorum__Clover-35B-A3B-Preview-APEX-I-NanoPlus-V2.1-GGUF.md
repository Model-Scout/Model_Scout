---
base_model: Diffuspace/Clover-35B-A3B-Preview
base_model_relation: quantized
quantized_by: IsValorum
library_name: gguf
pipeline_tag: text-generation
license: apache-2.0
language:
- en
- zh
- es
- fr
- de
- pt
- it
- ru
- ja
- ko
- vi
- th
- ar
tags:
- gguf
- llama.cpp
- quantized
- quantization
- apex
- apex-quant
- apex-i-nanoplus
- v2.1
- custom-quantization
- unsloth-studio
- clover
- clover_moe
- diffusion
- block-diffusion
- moe
- mixture-of-experts
- qwen3.6
- text-generation
- conversational
- imatrix
---

# Clover-35B-A3B-Preview APEX-I-NanoPlus-V2.1 GGUF

**APEX Quantization Series by IsValorum**

<p align="left">
  <a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>
</p>

> [!IMPORTANT]
> **Independently computed using dedicated cloud compute clusters, funded 100% out-of-pocket.**
>
> If you consider these releases to be of high quality and they help you in your day-to-day workflow, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and helps support my university studies.

> [!WARNING]
> **This file does not load in vanilla `llama.cpp`.** Clover uses the `clover_moe` architecture, which upstream does not implement. Use the precompiled builds in [IsValorum/llama.cpp-clover-moe](https://huggingface.co/IsValorum/llama.cpp-clover-moe), which ships Linux x86_64 CPU and CUDA 12 builds plus a Windows x86_64 universal package (NVIDIA CUDA 12.8, Vulkan for AMD and Intel GPUs, and CPU), or compile the runtime from the patched branch (PR #31306, commit `4838ffb0c8ade92f34d9157deea38d92758ab824`). The CUDA builds need an NVIDIA GPU; the CPU builds run on any x86-64 machine.

NanoPlus targets Q2-class expert weights with a Q4-class backbone, the smallest viable footprint for this family.

## Family cross-links

| Tier | Footprint | Base | Abliterated |
|---|---|---|---|
| **MiniPlus** | 14.75 GB / 13.74 GiB | [BF16](https://huggingface.co/IsValorum/Clover-35B-A3B-Preview-BF16-GGUF) | not published |
| **NanoPlus** | 12.56 GB / 11.70 GiB | [BF16](https://huggingface.co/IsValorum/Clover-35B-A3B-Preview-BF16-GGUF) | not published |

MicroPlus is not published for this family. There is no abliterated edition of Clover: the release is a single post-trained preview.

Related artifacts: [BF16 source](https://huggingface.co/IsValorum/Clover-35B-A3B-Preview-BF16-GGUF) · [Q8_0](https://huggingface.co/IsValorum/Clover-35B-A3B-Preview-Q8_0-GGUF) · [1.25M I-Matrix](https://huggingface.co/IsValorum/Clover-35B-A3B-Preview-VAL-1.25M-I-Matrix-GGUF) · [patched llama.cpp](https://huggingface.co/IsValorum/llama.cpp-clover-moe) · [opposite tier](https://huggingface.co/IsValorum/Clover-35B-A3B-Preview-APEX-I-MiniPlus-V2.1-GGUF)

## Architecture and precision

- Base model: `Diffuspace/Clover-35B-A3B-Preview`, a `clover_moe` derivative of Qwen3.6-35B-A3B with an added block-diffusion path
- Architecture: 40 layers, 30 gated DeltaNet (linear SSM) layers plus 10 full-attention layers, 256 routed experts with top-8 routing, 131,072 token context
- Parameters: 34,661,350,848
- iMatrix: `VAL-1.25M`, computed over 1.25M tokens, SHA256 `05d9669137d8ca843f0a7d3a8f00975e84d48644832d2734c564a1778b2f2d5d`
- Recipe: `recipe_moe_nanoplus_v2_1_clover.txt` (853 entries), one line per tensor, no fallback
- Recurrent shielding: decay factors, 1D convolutions, and RMSNorms in `F32`
- Block-diffusion armoring: `ssm_bd_logit_scale.weight`, `ssm_bd_history.weight`, `ssm_bd_history.bias`, and `ssm_conv1d.weight_right` in `F32` across all 30 GDN layers
- Output head in `Q6_K`, token embedding in `Q4_K`, attention gates in `Q8_0`, router logits (`ffn_gate_inp`, `ffn_gate_inp_shexp`) in `F32`

<!-- APEX-METRICS:START -->

## Empirical evaluation metrics

| Variant | Perplexity | Delta vs. BF16 | Fidelity retention |
|---|---|---|---|
| **Base BF16** | pending | pending | pending |
| **MiniPlus** | pending | pending | pending |
| **NanoPlus** | pending | pending | pending |

No empirical evaluation is published for this release. This block is reserved for the pipeline that fills it automatically.

<!-- APEX-METRICS:END -->

## File and metrics

| Item | Value |
|---|---|
| File | `Clover-35B-A3B-Preview.APEX-I-NanoPlus-V2.1.gguf` |
| Size | 12,557,370,304 bytes (12.56 GB / 11.70 GiB) |
| Bits per weight (file) | 2.8983 |
| Bits per weight (payload) | 2.8958 |
| Tensor count | 853 |
| Type histogram | 451 F32, 241 Q4_K, 50 IQ2_S, 44 IQ3_XXS, 30 Q8_0, 22 IQ2_XXS, 11 Q6_K, 4 Q3_K |
| Quantization types vs recipe | 0 mismatches |
| Size vs computed payload | 0.088 % |

`tensor-map.tsv` in this repository lists all 853 tensors with their final type, shape, and parameter count. `quant-report.json` holds the machine-readable version of the table above.

## Audited tensor map sample

| Tensor | Precision |
|---|---|
| `token_embd.weight` | Q4_K |
| `output.weight` | Q6_K |
| `output_norm.weight` | F32 |
| `blk.*.attn_qkv.weight` (30 GDN layers) | Q4_K |
| `blk.*.ssm_out.weight` (30 GDN layers) | Q4_K |
| `blk.*.ssm_beta.weight` (30 GDN layers) | Q4_K |
| `blk.*.attn_output.weight` (10 full-attention layers) | Q6_K |
| `blk.*.ffn_down_exps.weight` | `Q3_K` in layers 0, 1, 38, 39; `IQ3_XXS` in layers 2-37 |
| `blk.*.ffn_gate_exps.weight` | `IQ3_XXS` in layers 0, 1, 38, 39; `IQ2_S` in layers 2-37 |
| `blk.*.ffn_up_exps.weight` | `IQ3_XXS` in layers 0, 1, 38, 39; `IQ2_S` in layers 2-15; `IQ2_XXS` in layers 16-37 |
| `blk.*.ffn_down_shexp.weight` | Q4_K |
| `blk.*.ffn_gate_inp.weight` | F32 |
| `blk.*.attn_gate.weight` | Q8_0 |
| `blk.*.ssm_alpha.weight` | F32 |
| `blk.*.ssm_a` | F32 |
| `blk.*.ssm_dt.bias` | F32 |
| `blk.*.ssm_conv1d.weight` | F32 |
| `blk.*.ssm_conv1d.weight_right` | F32 |
| `blk.*.ssm_bd_logit_scale.weight` | F32 |
| `blk.*.ssm_bd_history.weight` | F32 |
| `blk.*.ssm_bd_history.bias` | F32 |

The complete audited list is `tensor-map.tsv`.

## Runtime requirement

**Vanilla `llama.cpp` cannot run this model.** The `clover_moe` architecture is not implemented upstream, and stock builds abort at load time with an unknown-architecture error. Everything you need is published at [IsValorum/llama.cpp-clover-moe](https://huggingface.co/IsValorum/llama.cpp-clover-moe), built from upstream PR #31306, commit `4838ffb0c8ade92f34d9157deea38d92758ab824`:

| Archive | Flavor | Hardware |
|---|---|---|
| `llama-clover-4838ffb-linux-x86_64-cpu.tar.gz` | CPU | Any Linux x86-64 machine, no GPU required |
| `llama-clover-4838ffb-linux-x86_64-nvidia-cuda12.tar.gz` | CUDA 12 | NVIDIA GPU with a CUDA 12 runtime, archs 80/86/89/90 |
| `llama-clover-4838ffb-windows-x86_64-nvidia-amd-universal-cuda12.8-vulkan-cpu.zip` | Universal | Windows x86-64: NVIDIA CUDA 12.8 sm_50-120, AMD and Intel through Vulkan 1.4.363, any CPU |
| `llama-clover-4838ffb-converter-python.tar.gz` | Converter | HF to GGUF conversion |

The runtime archives ship `llama-cli`, `llama-server`, `llama-diffusion-cli`, `llama-quantize`, `llama-imatrix`, and `llama-perplexity`. `llama-diffusion-cli` is the entry point for the block-diffusion path. They are dynamically linked, so point the loader at the bundled libraries before running:

```
tar xzf llama-clover-4838ffb-linux-x86_64-cpu.tar.gz
export LD_LIBRARY_PATH=$PWD/bin:$LD_LIBRARY_PATH
./bin/llama-cli -m Clover-35B-A3B-Preview.APEX-I-NanoPlus-V2.1.gguf -ngl 99 -c 8192
```

On Windows, extract the universal ZIP and run from its root:

```
set PATH=%~dp0bin;%PATH%
llama-completion.exe -m Clover-35B-A3B-Preview.APEX-I-NanoPlus-V2.1.gguf -p "hi" -n 1 -c 128 -b 16 -ub 16 -ngl 8 -no-cnv
```

Drop `-ngl 99` on the CPU build. The Linux x86_64 binaries require `GLIBC_2.38` or newer, so run them on Ubuntu 24.04 or equivalent; the Windows package has no glibc requirement and picks its backend at load time. macOS is not published yet: build from the same branch and commit, as for any other BLAS or CUDA configuration.

> [!NOTE]
> **What the prebuilt runtimes cover.** Linux x86_64: any CPU, and NVIDIA CUDA 12 for sm_80/86/89/90. Windows x86_64, in a single universal package: NVIDIA CUDA 12.8 from sm_50 through sm_120, AMD and Intel GPUs through Vulkan 1.4.363, and any CPU with per-CPU backends. Not covered: macOS, ARM64, ROCm, and Blackwell on Linux; those need a build from the same branch and commit.

## Reproducibility

```
llama-quantize --imatrix Clover-VAL-1.25M-I-Matrix.gguf \
  --tensor-type-file recipe_moe_nanoplus_v2_1_clover.txt \
  Clover-35B-A3B-Preview-BF16.gguf \
  Clover-35B-A3B-Preview.APEX-I-NanoPlus-V2.1.gguf Q4_0 64
```

The 853-line recipe overrides every tensor, including the 120 block-diffusion tensors that the canonical APEX-I MoE V2.1 recipes do not contain. Without those lines `llama-quantize` would silently fall back to the command-line type for them.

## Weight parity with the parent MoE

The block-diffusion path adds 120 tensors and 740,160 parameters, 0.002 percent of the model. Held in `F32` they cost 2,960,640 bytes over a quantization of the parent architecture without them, 0.024 percent of the file. Every one of the 733 shared tensors receives the same type it would receive in the parent MoE, so bits per weight over the shared set is identical and the footprint difference is the diffusion block alone.

## Limitations

- Preview release. No benchmark of any kind is published here, and none should be assumed.
- No abliterated edition exists, and none should be assumed.
