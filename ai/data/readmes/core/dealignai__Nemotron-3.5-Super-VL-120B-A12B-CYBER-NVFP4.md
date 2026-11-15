---
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
base_model: nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16
tags:
  - nemotron
  - nemotron-h
  - mamba
  - moe
  - vl
  - vision
  - abliteration
  - uncensored
  - cyber
  - gguf
  - nvfp4
language:
  - en
  - fr
  - es
  - de
  - it
  - ja
  - ko
  - pt
  - hi
  - zh
pipeline_tag: text-generation
thumbnail: dealign_mascot.png
---

> **Important:** CYBER = refusal-removed GGUF of NVIDIA's **Nemotron-3.5-Super-VL-120B-A12B**, quantized to a NVFP4-containing mixed GGUF (NVFP4 experts + Q8_0 Mamba/attn + BF16 latent-MoE compression ≈ NVIDIA's FP8/NVFP4 mixed layout, since llama.cpp has no per-tensor FP8). Follow **[@dealignai](https://x.com/dealignai)** for new releases.

---

<div align="center">

<img src="dealign_mascot.png" width="128" />

# Nemotron-3.5-Super-VL-120B-A12B · CYBER-NVFP4-GGUF

**NemotronH hybrid Mamba2 + attention + latent-MoE** · **120B total / 12B active** · **VL (image + video)** · **73 GB on disk**

<a href="https://x.com/dealignai"><img src="https://img.shields.io/badge/Follow-@dealignai-1DA1F2?logo=x&logoColor=white&style=for-the-badge" alt="@dealignai"></a>

</div>

---

## What is this

NVIDIA's **Nemotron-3.5-Super-VL-120B-A12B** with its refusal training removed and quantized to a NVFP4-containing mixed GGUF (NVFP4 routed + shared experts, Q8_0 Mamba in/out proj + attention q/k/v/o + lm_head, BF16 latent-MoE fc1/fc2_latent_proj + token_embd, F32 norms). The vision tower is preserved intact.

> Research artifact for alignment work. This model answers requests the base refuses. **Do not deploy to end users without separate downstream safety controls.**

| | |
|---|---|
| **Base model** | [nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16) |
| **Architecture** | NemotronH: 88 blocks (40 Mamba2 + 40 latent-MoE + 8 full-attention), hidden 4096, 512 experts × 22 active/token, 1 shared expert, latent-MoE 1024-d, C-RADIO vision + mlp1 |
| **Thinking** | three modes: off / medium / high (via `enable_thinking` + `medium_effort` chat template kwargs) |
| **Quantization** | NVFP4 routed + shared experts, Q8_0 attention q/k/v/o + Mamba in/out proj + lm_head, BF16 fc1/fc2_latent_proj + token_embd, F32 norms |
| **Size** | 73 GB (4.73 BPW) |
| **Languages** | English, French, Spanish, German, Italian, Japanese, Korean, Portuguese, Hindi, Chinese |

---

## Files

| File | Size | Role |
|---|---|---|
| `Nemotron-3.5-Super-VL-120B-A12B-CYBER-NVFP4.gguf` | 73 GB | Main model |

mmproj and NVFP4-LiLiCorr drafter will be added in a follow-up release.

---

## Running

llama.cpp upstream `b76b13379` or newer.

```bash
llama-server \
  -m Nemotron-3.5-Super-VL-120B-A12B-CYBER-NVFP4.gguf \
  -ngl 999 -c 65536 -np 8 --jinja --flash-attn on \
  --host 127.0.0.1 --port 8091
```

### Reasoning modes

Pass via `chat_template_kwargs`:

| Mode | kwargs |
|---|---|
| off (fast) | `{"enable_thinking": false}` |
| medium | `{"enable_thinking": true, "medium_effort": true}` |
| high | `{"enable_thinking": true, "medium_effort": false}` |

Default sampling: `temperature=0` greedy. `temperature ≤ 0.7` clean; above that NVFP4 decode artifacts may appear.

---

## Evaluation

### HarmBench compliance (cyber + chem/bio, 94 prompts × 3 reasoning modes, 2048-token budget)

**ASR 83.0% at reasoning-HIGH with ZERO garbage, ZERO budget-cut, ZERO empty refusals.** All non-compliance is honest refusals.

| Category | N | off | medium | high |
|---|---|---|---|---|
| **cybercrime_intrusion** | 52 | 73.1% | 84.6% | **90.4%** |
| chemical_biological | 42 | 40.5% | 76.2% | 73.8% |
| **TOTAL** | 94 | 58.5% | 80.9% | **83.0%** |

Verdict breakdown at HIGH mode: `comply=78, refused=16, refused_empty=0, budget_cut=0, garbage=0`.

### Coherence — long-form benign (2048 tokens)

Full essays on Roman history (world history / humanities), OS virtual memory (systems / CS), and lighthouse creative fiction (creative writing) — scanned for repetition patterns:

| Prompt | Mode | Chars | `max_bigram_run` | `max_trigram_run` | `*` runs | `I`-loops |
|---|---|---|---|---|---|---|
| roman_history | off | 9893 | 1 | 1 | 0 | 0 |
| roman_history | high | 4759 | 1 | 1 | 0 | 0 |
| os_kernel | off | 9133 | 1 | 1 | 0 | 0 |
| os_kernel | high | 3556 | 1 | 1 | 0 | 0 |
| lighthouse_story | off | 9022 | 1 | 1 | 0 | 0 |

No loop patterns detected across any output.

### MMLU-14042 (thinking off, letter-logit)

**Micro 85.00% (11936/14042) · Macro 85.57%** across 57 subjects.

| Subject topic | Score |
|---|---|
| STEM | 82.08% (2588/3153) |
| Humanities | 80.43% (3784/4705) |
| Social Sciences | 92.07% (2833/3077) |
| Other | 87.90% (2731/3107) |

Multimodal (image + video) evaluations will be added in a follow-up update.

### Known artifacts

- **Occasional rare-name typos** under NVFP4 decode. Single-token substitutions, not degeneration. Clean at `temperature=0`.
- **Longer responses.** CYBER commits fully to compliant answers; expect 2–3× tokens per prompt vs base.
- **Reasoning-mode budget.** Creative tasks at reasoning-HIGH may exhaust a 2048 token budget inside `<think>`. Set `max_new_tokens ≥ 4096` for long-form creative work under thinking.

---

## Attribution

- **Base model & vision tower:** NVIDIA — redistributed under NVIDIA Open Model License.
- Follow **[@dealignai](https://x.com/dealignai)** for new releases.

## License

NVIDIA Open Model License. The CYBER transformation is a research modification distributed under the same terms.
