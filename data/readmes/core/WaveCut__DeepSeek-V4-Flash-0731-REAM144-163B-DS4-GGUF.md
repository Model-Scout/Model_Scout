---
base_model: WaveCut/DeepSeek-V4-Flash-0731-REAM144-163B
license: mit
pipeline_tag: text-generation
language:
- en
- ru
- zh
- es
tags:
- deepseek-v4
- mixture-of-experts
- ream
- gguf
- ds4
---

# DeepSeek V4 Flash — REAM144 (163B) · DS4 Q2

A 2-bit build of [DeepSeek-V4-Flash-0731-REAM144-163B](https://huggingface.co/WaveCut/DeepSeek-V4-Flash-0731-REAM144-163B) —
DeepSeek-V4-Flash with **144 of the original 256 experts per layer**, sized to run fully resident on a 64 GiB Mac with room for 8k context.
Quantized with the standard DS4 recipe (2-bit experts, 8-bit attention) and a fresh
importance matrix.

> [!IMPORTANT]
> This is a **DS4-specific** GGUF. Run it with the [DS4 fork](https://github.com/iamwavecut/ds4) —
> the 144-expert topology needs its variable expert count support. Generic llama.cpp
> will not load this file.

> [!WARNING]
> Live smoke testing passed 7/10 scenarios on the first run. Independent reruns show the failures (**Tool calling (DSML)**, **Code refactoring**, **Tool call → code chain**) are **intermittent, not absolute** — see the Stability column below for per-scenario pass rates. Multilingual chat, reasoning and long dialogs are consistently healthy. The full-precision native checkpoint may behave better — 2-bit quantization hits agentic behavior hardest.

## Files

| File | Size | What it is |
| --- | ---: | --- |
| `ream144.gguf` | 49.3 GB | The model |
| `dspark.gguf` | 5.7 GB | Optional speculative decoding (DSpark) |
| `imatrix.dat` | 0.2 GB | Importance matrix used for this quant |
| `SMOKE_REPORT.json` | — | Raw smoke-test evidence |

## Run

Plain:

```sh
./ds4 -m ream144.gguf -c 8192
```

With DSpark speculative decoding (faster generation, more memory):

```sh
./ds4 -m ream144.gguf --mtp dspark.gguf --dspark -c 8192
```

Adding DSpark pushes the total past a 64 GiB budget — measured on a 64 GiB Mac it slows prefill ~10× and can thrash generation; use it on larger hosts only.

## How it was made

One pruning step, straight from the original — no cascading. Expert importance was
measured by running [`deepseek-ai/DeepSeek-V4-Flash-0731`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)
over a ~5-million-token calibration mix (multi-turn dialogs, thinking and direct modes,
rendered with the model's own chat encoder). The strongest experts of every domain were
protected from pruning, the survivors were carried over **byte-identical**, and the
router was re-balanced to keep the original selection behavior.

| Calibration domain | Share |
| --- | ---: |
| Code | 35% |
| Agentic / tool use | 19% |
| Multilingual chat | 16% |
| Math | 8% |
| General chat | 6% |
| Roleplay | 6% |
| Russian | 5% |
| Long docs | 4% |

This line replaces the earlier cascaded REAM builds (now archived under `-exp` names),
which degraded badly in multi-turn use.

## Smoke results

Every scenario is a live multi-turn conversation run end-to-end on the DS4 runtime (raw evidence ships in `SMOKE_REPORT.json`).

| Scenario | First run | Stability (reruns) |
| --- | :---: | :---: |
| Russian wordplay, multi-turn | ✅ | — |
| English → Russian code-switching | ✅ | — |
| Code Q&A over a 4k-token file | ✅ | — |
| Tool calling (DSML) | ❌ | 5/10 |
| Russian multi-turn reasoning | ✅ | — |
| Spanish creative writing | ✅ | — |
| Code refactoring | ❌ | 8/10 |
| Chinese summarization | ✅ | — |
| Long-dialog focus (drift check) | ✅ | — |
| Tool call → code chain | ❌ | 5/10 |

Stability = pass rate over independent reruns of the scenarios that failed the first run; passing scenarios were not re-run.

## Limitations

- Needs the DS4 fork; not a generic llama.cpp file.
- 2-bit quantization is aggressive: expect the native checkpoint to be smarter than
  this build, especially on agentic tool use.
- Memory use grows with context length and DSpark; the sizes above are the files alone.
