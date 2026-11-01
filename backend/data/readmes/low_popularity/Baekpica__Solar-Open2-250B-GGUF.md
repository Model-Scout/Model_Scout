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
  - text-generation
---

# Solar Open2 250B GGUF

**Built with Solar.**

Full-topology GGUF conversions of
[`upstage/Solar-Open2-250B`](https://huggingface.co/upstage/Solar-Open2-250B),
preserving all 48 layers, 320 routed experts, and one shared expert. This is an
independent conversion and is not an official Upstage release.

## Support my work

I work on making large language models practical on hardware they were never really designed to fit on — through mixed quantization, inference optimization, custom kernels, and serving experiments.

While much of the development happens on local hardware, calibration, profiling, and large-scale validation often require expensive on-demand GPUs.

Contributions help pay for that compute, storage, and testing infrastructure, so I can keep experimenting and publishing the results openly.

<a href="https://www.buymeacoffee.com/baekpica" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;"></a> <a href="https://github.com/sponsors/Baekpica" target="_blank"><img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Baekpica on GitHub" style="height: 60px !important;width: 217px !important;"></a>

## Variants

| Variant | Split | Purpose |
|---|---:|---|
| BF16 | 11 shards, 500,718,700,672 bytes (466.331 GiB) | High-precision converted reference |
| Q8_0 | 11 shards, 266,136,847,072 bytes (247.859 GiB) | Full-model imatrix and quality reference |

The exact per-shard hashes are in `BF16-SHA256SUMS` and `Q8_0-SHA256SUMS`.
Each shard is uploaded as an independent resumable Hub commit; the two
variants use disjoint filenames and can be downloaded independently.

## Provenance

- Source revision:
  `upstage/Solar-Open2-250B@9190fbe63a2ad8e17fc766ccceb36de7c66f004b`
- Source tensor count: 47,019
- Source bytes: 500,617,750,484
- GGUF architecture: `solar-open2`
- Context metadata: 1,048,576 tokens, NoPE
- Converter base: `ggml-org/llama.cpp@6ea215d171fd31df943bf1ac8227129f2b963160`
- Solar conversion/runtime patch SHA256:
  `7c267850de7a08af66a9bd64e9d4a3b33e085a4d2888d94a4c3d919f87283e44`

The BF16 conversion uses `--outtype bf16 --split-max-size 48G`. The Q8_0
conversion uses `llama-quantize`, `--pure`, `--keep-split`, Q8_0 token
embeddings, and a Q8_0 output tensor.

## Validation status

Both complete split sets passed GGUF metadata, split ordering, tensor count,
topology, bounds, and exact tensor-type checks with zero errors. Each contains
1,083 GGUF tensors: BF16 has 674 BF16 + 409 F32 tensors, and Q8_0 has 674
Q8_0 + 409 F32 tensors.

The Q8_0 model was loaded resident across four H100 NVL GPUs and completed a
32-prompt greedy reference run plus no-think quality sanity prompts covering
Korean, English, Japanese, code, structured JSON, reasoning, and long-text
summarization. The structured-output sample parsed as valid JSON and no NaN,
malformed-output, or broken-generation regression was observed. The four-H100
run is development evidence only, not a DGX Spark `sm_121` serving or
performance claim.

## License and attribution

The source model and these conversions are distributed under the included
Upstage Solar License. The model name begins with `Solar`, and this model card
prominently states “Built with Solar” as required by that license.
