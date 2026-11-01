---
base_model: upstage/Solar-Open2-250B
license: other
license_name: upstage-solar-license
license_link: LICENSE
language:
  - en
  - ko
  - ja
pipeline_tag: text-generation
tags:
  - gguf
  - solar
  - moe
  - mixed-precision
  - text-generation
  - dgx-spark
---

# Solar Open2 250B Mixed-Quant GGUF

**Built with Solar.**

> <span style="color:red">**The download statistics on this page are not real.**</span>
>
> <span style="color:red">After I reported the anomaly, Hugging Face staff
> confirmed by email (2026-10-17) that almost all of last month's downloads
> came from a single automated, unauthenticated client re-fetching this
> repository's 11 shards about every 45 seconds from 2026-09-28 to
> 2026-10-11. Gating blocks it, which is why the count stopped growing. The
> count is not multiplied by the split shards (only shard 1 counts) and is
> not delayed statistics.</span>
>
> <span style="color:red">At least until that period leaves the 30-day
> window, around 2026-11-11, the count does not reflect real use.</span>
>
> <span style="color:red">I do not want the statistics inflated by abuse,
> intended or not, so this repository stays gated.</span>

This repository contains the locked `MXQ-v1` candidate derived from
[`upstage/Solar-Open2-250B`](https://huggingface.co/upstage/Solar-Open2-250B).
It preserves the complete topology: 48 layers, all 320 routed experts per
layer, one shared expert, and the original `[GQA, KDA, KDA, KDA] × 12`
schedule. No expert, layer, or parameter pruning, merging, or distillation was
performed. This is an independent conversion and is not an official Upstage
release.

**Verified throughput (2026-09-14, Rust host, 300–2200 MHz cap):** On one
DGX Spark GB10, SM clock 2190 MHz. MXQ-v1 with K-FP8/V-FP4 KV. Cold
`ds4-bench`, Promessi Sposi, 4,096-token chunks, 64 greedy tokens, MTP
off. Interleaved medians of three; 196,608 frontier logits and 64 IDs
byte-identical.

Round 1 default-on FATTN_WS (`DS4_SOLAR_FATTN_WS=0` restores pair):

| Prompt tokens | Prefill off → on | Decode off → on |
|---:|---:|---:|
| 8,192 | 1,050.86 → 1,075.76 tok/s | 17.40 → 17.44 |
| 65,536 | 731.24 → 927.50 tok/s | 13.06 → 13.02 |

Round 2 skip Q3 handoff down sanitize (`DS4_CUDA_MOE_HANDOFF_SANITIZE=1`
restores the pass), measured with WS on:

| Prompt tokens | Prefill off → on | Decode off → on |
|---:|---:|---:|
| 8,192 | 1,073.59 → 1,095.61 tok/s | 17.43 → 17.43 |
| 65,536 | 925.19 → 943.18 tok/s | 13.02 → 13.01 |

Runtime:
[`ds4-dfm-rs@67de331`](https://github.com/Baekpica/ds4-dfm-rs/commit/67de3315cbf9fac730d1fb098149f10d18b469b4).
Disk-KV restart and HTTP partial fork now reuse prefixes. This is not HTTP
and not the uncapped September 7/12 benches. Keep the SM cap on GB10.
[Protocol, serving, rejects](https://github.com/Baekpica/ds4-dfm-rs/blob/67de3315cbf9fac730d1fb098149f10d18b469b4/docs/solar-open2-optimization-2026-09-14.md).

![Clock-capped cold FATTN_WS comparison](solar-open2-2026-09-14-throughput.png)

The September 7 fused-MoE pass and September 12 uncapped controls use
other clocks and are not this graph. 1,048,576-token serving is not
claimed.

## Support my work

I work on making large language models practical on hardware they were never really designed to fit on — through mixed quantization, inference optimization, custom kernels, and serving experiments.

While much of the development happens on local hardware, calibration, profiling, and large-scale validation often require expensive on-demand GPUs.

Contributions help pay for that compute, storage, and testing infrastructure, so I can keep experimenting and publishing the results openly.

<a href="https://www.buymeacoffee.com/baekpica" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;"></a> <a href="https://github.com/sponsors/Baekpica" target="_blank"><img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Baekpica on GitHub" style="height: 60px !important;width: 217px !important;"></a>

## Artifact

| Variant | Split | Size | Approximate BPW |
|---|---:|---:|---:|
| MXQ-v1 | 11 shards | 95,533,532,160 bytes (88.973 GiB) | 3.05 |

Download the complete 11-file split beginning with
`Solar-Open2-250B-MXQ-v1-00001-of-00011.gguf`. Exact hashes are in
`MXQ-v1-SHA256SUMS`.

The full BF16 and full-model Q8_0 reference conversions are published
separately in
[`Baekpica/Solar-Open2-250B-GGUF`](https://huggingface.co/Baekpica/Solar-Open2-250B-GGUF).

## Precision recipe

| Module family | Precision |
|---|---|
| Token embedding, LM head | Q8_0 |
| GQA q/k/v/o/g projections | Q8_0 |
| KDA matrix projections | Q8_0 |
| Shared expert gate/up/down | Q8_0 |
| Routed gate/up, layers 4–43 | IQ2_XXS + imatrix |
| Routed down, layers 4–43 | Q3_K + imatrix |
| Routed gate/up/down, layers 0–3 and 44–47 | Q4_K + imatrix |
| Router, norms, small KDA control/norm/conv tensors | F32 |

The final GGUF contains 1,083 tensors: 409 F32, 530 Q8_0, 80 IQ2_XXS,
40 Q3_K, and 24 Q4_K tensors. `quant-recipe-v1.yaml` and
`verify-v1.json` contain the machine-readable recipe and verification result.

## Calibration

The Solar chat-template calibration corpus follows the published mix from
`Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix`: instruction chat 22%,
Cascade stage-1 reasoning 16%, Cascade stage-2 reasoning 16%, Korean 16%,
other multilingual 12%, finance 6%, SWE 6%, and algorithmic code 6%.

The imatrix processed 590 × 512-token chunks. Layers 1–47 reached strict
320/320 routed-expert coverage. Layer 0 retained one explicit, pinned
exception of 29 zero-activation experts; the exact IDs and gate are recorded
in `verify-imatrix.json`. No precision was lowered to compensate for this
exception.

## Validation status

- All 11 shards passed split ordering, bounds, topology, tensor count, tensor
  family, and exact tensor-type verification with zero errors.
- The artifact loaded resident across four H100 NVL GPUs and completed 32
  deterministic short generations plus eight longer no-think quality checks.
- Every candidate output was non-empty with valid token IDs. Fatal/content
  checks passed for Korean, English, Japanese, code, arithmetic, exact JSON,
  and constrained-list prompts; no NaN or malformed structured output was
  observed.
- A development ds4 CUDA runtime mapped the complete artifact on one H100 and
  passed full-weight, recurrent-state snapshot/restore, replay, and cold
  invalidation regressions.
- A native `sm_121a` ds4 build serves the complete artifact on one DGX Spark
  GB10 through the OpenAI-compatible server at `-c 196608` with three
  persistent banks. See [DGX Spark](#dgx-spark) for the measured point.

H100 timings are development and artifact-sanity evidence only. Do not
present them as DGX Spark performance. 1,048,576-token serving on Spark is
**not** claimed.

## DGX Spark

One NVIDIA DGX Spark GB10 (128 GB unified memory, driver 610.43.02, CUDA
13.3, `sm_121a`). Runtime
[`Baekpica/ds4@b2e52b9`](https://github.com/Baekpica/ds4/commit/b2e52b9048ba339327539212de1c47d009dde126)
on the `dfm` line. Artifact: this MXQ-v1 11-shard split. A long-lived VMM
weight owner (`--backend vmm --scope base --reserve-gb 16`, 453 derived
aligned artifacts) plus a restartable `ds4-server` worker:

```sh
DS4_CUDA_WEIGHT_IPC_MANIFEST="$RUN/weights.manifest" \
DS4_CUDA_WEIGHT_IPC_SCOPE=base \
DS4_SERVER_COALESCE_MAX=3 \
DS4_SERVER_COALESCE_MAX_TOKENS=4096 \
DS4_CONT_PREFILL_CHUNK=4096 \
DS4_METAL_PREFILL_CHUNK=4096 \
./ds4-server -m Solar-Open2-250B-MXQ-v1-00001-of-00011.gguf \
  --cuda -c 196608 -n 1024 -t 6 \
  --host 0.0.0.0 --port 8002 --model-id solar-open2-250b \
  --no-spec --no-update-check --mem-floor-gb 8
```

OpenAI Chat Completions, thinking disabled, exact-cold (`cached_tokens=0`),
128 decode tokens, median of three. Loaded SM clocks 2,411–2,561 MHz
(uncapped; not the 300–2200 MHz campaign above).
`banks_total=3` still admitted.

| Depth | Prompt tokens | Prefill | Decode p50 | Decode API |
|---|---:|---:|---:|---:|
| 8K | 8,222 | 1,050.7 tok/s | 19.05 tok/s | 18.9 tok/s |
| 64K | 66,761 | 804.5 tok/s | 13.07 tok/s | 14.1 tok/s |

On the same host and artifact, before the `dfm` default-path series that
ends at `b2e52b9`, 8K decode was 17.5 tok/s and 64K average prefill was
710 tok/s. The series kept the production path as: skip width-1 inner
CUDA graph capture; walk FATTN KV in 32-key then GQA-pair 64-key tiles;
keep the KDA 64 KiB state tile in shared memory; tile grouped GQA decode
KV in 32 keys with packed K-FP8/V-FP4 dequant.

`test-solar-kv` on this binary: 512-token GQA2 vs one-head `rel_rms=0`;
split vs direct `rel_rms=8.45e-7`. Incremental `T(64K)−T(60K)` last-4K is
not a published figure. Native 1,048,576-token metadata is not a measured
Spark pass.

### Partial prefix reuse

Runtime
[`Baekpica/ds4@042bcea`](https://github.com/Baekpica/ds4/commit/042bcea5302bff775d0a508cec643f1f06754df9)
adds a bounded, shared Solar KDA checkpoint pool to the continuous lane.
The 32 slots are demand-mapped, exact forks share references, and long
prefills retain roughly 24 periodic checkpoints across the configured
context in addition to request boundaries. A divergent prompt restores the
nearest safe checkpoint and replays only the gap.

One controlled A/B run used the same GB10, artifact, four-bank worker,
`-c 65536`, 4,096-token prefill chunks, and greedy no-think Chat requests.
The control set `DS4_SERVER_FORK_PARTIAL=0`, which also disables checkpoint
reservation. The treatment used the default.

| Request | Prompt | Control cached | Treatment cached | Control TTFT | Treatment TTFT | Speedup |
|---|---:|---:|---:|---:|---:|---:|
| Source | 12,123 | 0 | 0 | 10,654.0 ms | 10,710.7 ms | 0.995× |
| Branch at ~6K | 6,079 | 0 | 4,096 | 5,323.7 ms | 1,868.8 ms | 2.85× |
| Branch at ~10K | 10,148 | 0 | 8,192 | 8,920.2 ms | 1,929.8 ms | 4.62× |

Both branch responses were byte-identical between control and treatment.
Treatment reported two partial-fork admits, 12,288 cached tokens, zero failed
requests, and zero admission rejects. Source checkpoint capture added 56.7 ms
(0.53%) in this single run. After the three requests, device-live memory was
102.04 GiB and system-available memory was 14.59 GiB with an 8 GiB floor.

This is a bounded worker-local cache, not an unbounded radix tree. Token
history and GQA prefix rows remain anchored to a retained bank, and the KDA
checkpoint pool is not serialized into disk-KV payloads.

On 2026-09-14, a one-bank worker at `-c 8192` with `--kv-disk-dir` and
partial fork, under the 300–2200 MHz cap, reused `cached_tokens=538` after
a clean restart continuation and `cached_tokens=4096` on a 4,177-token
divergent Chat (81 computed, TTFT 416 ms vs 4.7 s). Prompts shorter than
the 4,096-token stride still have no interior checkpoint.

## Provenance

- Source: `upstage/Solar-Open2-250B@9190fbe63a2ad8e17fc766ccceb36de7c66f004b`
- Official implementation oracle:
  `upstageAI/transformers@ef5c37485091057070b36dd0620798f74988eb01`
- llama.cpp conversion base:
  `ggml-org/llama.cpp@6ea215d171fd31df943bf1ac8227129f2b963160`
- Solar conversion/runtime patch SHA-256:
  `7c267850de7a08af66a9bd64e9d4a3b33e085a4d2888d94a4c3d919f87283e44`
- Reproduction repository:
  [`Baekpica/solar-open2-mixed-ds4`](https://github.com/Baekpica/solar-open2-mixed-ds4)

Current upstream runtimes may not yet recognize the `solar-open2` GGUF
architecture. Use a compatible Solar Open 2 llama.cpp port or the linked ds4
development branch; compatibility claims should be tied to an exact runtime
revision.

## License and attribution

The source model and this derivative artifact are distributed under the
included Upstage Solar License. The model name begins with `Solar`, and this
card prominently states “Built with Solar” as required by that license.
