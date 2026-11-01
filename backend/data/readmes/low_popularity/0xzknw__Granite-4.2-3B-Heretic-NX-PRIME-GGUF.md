---
license: apache-2.0
language:
- en
- de
- es
- fr
- ja
- pt
- ar
- cs
- it
- ko
- nl
- zh
library_name: llama.cpp
pipeline_tag: text-generation
base_model: ibm-granite/granite-4.2-3b
tags:
- gguf
- granite
- granite-4.2
- reasoning
- thinking
- abliterated
- uncensored
- model-editing
- residual-stream
- heretic-nx
- prime
- lm-studio
---

# Granite 4.2 3B — Heretic NX PRIME (GGUF)

GGUF release of a capability-preserving residual-stream edit of
[ibm-granite/granite-4.2-3b](https://huggingface.co/ibm-granite/granite-4.2-3b).
This is the **beta 2.4, rank-16 protected** candidate selected on a fixed
refusal/KL frontier and validated independently after materialization.

This is a static weight edit, not a LoRA and not a fine-tune. No adapter or
custom runtime hook is required.

## Files

| File | Size | Recommended use |
|---|---:|---|
| `Granite-4.2-3B-Heretic-NX-PRIME-BF16.gguf` | 6.82 GiB | Maximum fidelity |
| `Granite-4.2-3B-Heretic-NX-PRIME-Q8_0.gguf` | 3.63 GiB | Near-BF16 quality; recommended |
| `Granite-4.2-3B-Heretic-NX-PRIME-Q4_K_M.gguf` | 2.09 GiB | Smallest practical LM Studio build |

All three files contain the Granite tokenizer and chat template and were
smoke-tested with llama.cpp **b10621**.

## Evaluation

| Evaluation | Official base | Heretic NX PRIME beta 2.4 |
|---|---:|---:|
| Explicit-refusal marker proxy | 103 / 104 | **0 / 104** |
| Paired MCQ capability slice | 63.35% | **64.29%** |
| Capability rows | 854 | 854 |
| Capability non-inferiority margin | — | **passed at -3%** |

The paired capability slice contains ARC-Challenge, HellaSwag and MMLU. Its
bootstrap mean difference is **+0.94 percentage point**, with a 95% interval
of **[-0.35, +2.22] points**.

KL depends on the exact runtime being measured:

| KL protocol | beta 2.4 |
|---|---:|
| NF4 base with activation-native residual hooks | **0.024674** |
| Static BF16 checkpoint, base and candidate quantized independently to NF4 | **0.042418** |

The second value includes independent NF4 quantization noise and should not be
presented as a pure BF16-to-BF16 KL measurement. The GGUF quantizations were
load-tested, but their full 104-row behavioral scores are not claimed to be
identical to the BF16 checkpoint.

The 104-row refusal result is a lexical explicit-refusal proxy. It is not a
measure of semantic task success and is not a universal model-quality score.
See [`EVALUATION_SUMMARY.md`](./EVALUATION_SUMMARY.md) and the included JSON
reports for the exact protocols.

## What was edited

- Source revision: `b7e947307dd2efb3ad3b853b0e8a7e75f8ad4ac2`
- Protected residual-stream axis rank: `16`
- Strength: `beta = 2.4`
- Edited layers: `25–36`
- Edited projections: attention output and MLP down projections
- Materialization: norm-preserving static weight edits in BF16
- Edited tensors: `24`

## LM Studio

Download one GGUF file and place it in your LM Studio models directory. Q8_0
is the default recommendation; Q4_K_M is appropriate when RAM/VRAM is tight.

```powershell
hf download 0xzknw/Granite-4.2-3B-Heretic-NX-PRIME-GGUF Granite-4.2-3B-Heretic-NX-PRIME-Q8_0.gguf --local-dir "$env:USERPROFILE\.lmstudio\models\0xzknw\Granite-4.2-3B-Heretic-NX-PRIME-GGUF"
```

If LM Studio is already open, refresh the model list or restart the app after
the download completes.

## llama.cpp

```bash
llama-cli -m Granite-4.2-3B-Heretic-NX-PRIME-Q8_0.gguf -cnv
```

Granite 4.2 supports thinking mode through its embedded chat template.

## Reproducibility

SHA-256 checksums:

```text
0edede4dd173c778e4a47969188d54753bf8edb3dd62e097f9b985af9ffcf36d  Granite-4.2-3B-Heretic-NX-PRIME-BF16.gguf
9135527c35629202e63938ebe11d039071c45f91326d031fcad44d0ffd4033f0  Granite-4.2-3B-Heretic-NX-PRIME-Q8_0.gguf
56c040b4c55a31b542fe8beb8b712f3b6ee5531018116ea74af0b0573cb9058d  Granite-4.2-3B-Heretic-NX-PRIME-Q4_K_M.gguf
```

The editing engine and reproducibility code are available in
[Heretic NX](https://github.com/0xZKnw/heretic-nx).

## License and use

The source model is Apache-2.0 and this release preserves that license. Model
editing reduces learned refusal behavior; users remain responsible for how
they deploy and use the model.
