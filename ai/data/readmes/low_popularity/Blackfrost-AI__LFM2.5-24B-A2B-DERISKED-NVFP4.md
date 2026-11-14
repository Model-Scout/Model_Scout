---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
  - Blackfrost-AI/LFM2.5-24B-A2B-DERISKED-BF16
pipeline_tag: text-generation
library_name: transformers
language:
  - en
  - ar
  - zh
  - fr
  - de
  - ja
  - ko
  - es
  - pt
  - it
  - vi
  - th
  - id
  - hi
  - ru
  - pl
tags:
  - nvfp4
  - modelopt
  - conversational
  - lfm2.5
  - moe
  - reasoning
  - tool-calling
  - behavioral-modification
  - blackfrost
---

<p align="center">
  <img src="ASSETS/BLACKFROST-AI-BANNER.png" alt="BLACKFROST-AI" width="100%">
</p>

# LFM2.5-24B-A2B-DERISKED-NVFP4

ModelOpt NVFP4 release of the behaviorally modified LFM2.5-24B-A2B derivative for efficient reasoning, multilingual chat, and tool-enabled workflows.

> **Release status:** public and ungated. The standalone NVFP4 checkpoint, configuration, tokenizer, model card, account banner, license, and deployment kit are included.

## Artifact contents

| Component | Status |
|---|---|
| Model card | Included |
| Blackfrost-AI account banner | Included |
| LFM Open License v1.0 | Included |
| Deployment kit | Included under [`DEPLOYMENT/`](DEPLOYMENT/) |
| Standalone NVFP4 weights | Included: 2 SafeTensors shards |
| Model configuration, tokenizer, generation configuration, and chat template | Included |

This is a standalone quantized checkpoint. It is not an adapter and does not require the BF16 parent at inference time.

## Why this release exists

This release targets a substantially smaller storage and serving footprint than BF16 while preserving the Blackfrost derivative's architecture, reasoning template, and tool-use interface. The weights are behaviorally modified. The proprietary transformation process and reconstruction materials are not distributed.

## Model specifications

| Property | Value |
|---|---|
| Architecture | `Lfm2MoeForCausalLM`, sparse mixture of experts |
| Precision | ModelOpt NVFP4 W4A4, group size 16, with FP8 KV-cache cast metadata |
| Total parameters | Approximately 24B |
| Active parameters per token | Approximately 2.45B |
| Model blocks | 40 |
| Experts per MoE block | 64; 4 routed per token |
| Sequence mixing | 30 convolution blocks and 10 grouped-query-attention blocks |
| Languages | 16 languages listed in the repository metadata |
| Reasoning | Always-thinking chat template |
| Tool use | Structured tool calls through the packaged chat template |
| Native configured context | 131,072 tokens |
| Quantization toolchain | NVIDIA ModelOpt `0.48.0rc0` |
| Checkpoint tensor footprint | 13,868,582,736 bytes |
| Weight shards | 2 SafeTensors shards |

## Complete lineage

1. Foundational parent: [`LiquidAI/LFM2.5-24B-A2B`](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) at revision `1769516ac588c4c558089c94f27d96b0dc67b183`
2. Behavioral parent: [`Blackfrost-AI/LFM2.5-24B-A2B-DERISKED-BF16`](https://huggingface.co/Blackfrost-AI/LFM2.5-24B-A2B-DERISKED-BF16)
3. Blackfrost stage: behaviorally modified derivative; the proprietary transformation process is not distributed
4. Quantization stage: ModelOpt NVFP4 export from the completed BF16 derivative
5. Public artifact: standalone quantized SafeTensors checkpoint

No upstream or BF16 benchmark number is presented as a post-quant measurement of this artifact.

## Artifact verification and checksums

The completed NVFP4 artifact passed structural, numerical, and serving validation:

- all 2 expected weight shards are present;
- all 7,610 BF16 source tensor keys are retained;
- 7,402 eligible weights carry ModelOpt NVFP4 quantization payloads;
- the artifact contains 29,816 tensors totaling 13,868,582,736 tensor bytes;
- all 22,414 floating-point tensors scanned are finite;
- no zero-valued scale tensors were found;
- configuration, tokenizer, generation configuration, and chat-template assets are present;
- native MTP/NextN payload accounting is `0 → 0`;
- vLLM auto-detected the `modelopt_fp4` loader, loaded the checkpoint at the 131,072-token context ceiling, exposed the OpenAI-compatible API, and completed a deterministic generation canary on one NVIDIA B300.

The Hub revision records the complete checkpoint file inventory. File hashes are included in `SHA256SUMS`, and deployment-kit hashes are included in [`DEPLOYMENT/CHECKSUMS.sha256`](DEPLOYMENT/CHECKSUMS.sha256).

## Measured behavioral and capability evaluation

The BF16 behavioral parent passed its narrow automatic preservation gate, with a relative negative-log-likelihood delta of `-0.00305%`, Jensen–Shannon divergence of `0.006415`, and token top-1 agreement of `95.48%` against its pinned parent on eight held-out prompts and 155 scored tokens.

Those distribution measurements describe the BF16 parent, not this quantized artifact. The NVFP4 artifact passed its post-quant structural, numerical, load, and deterministic generation canaries. A comprehensive post-quant academic, coding, multilingual, safety, refusal-behavior, and capability benchmark suite remains pending.

## Prompt, reasoning, and sampling notes

Use the packaged chat template. It begins assistant turns in reasoning mode and supports structured tool definitions and tool-result reinjection. The upstream recommended defaults are `temperature=0.1`, `top_k=50`, and `repetition_penalty=1.05`.

Applications should validate their own system prompts, sampling settings, structured-output schemas, and tool policies. This release does not prescribe a default persona or application policy.

## Deployment

The included [`DEPLOYMENT/`](DEPLOYMENT/) kit contains the exact validated runtime, launch flags, environment variables, smoke test, dependency provenance, hardware profile, and checksums for this artifact. Start with [`DEPLOYMENT/README.md`](DEPLOYMENT/README.md).

## Limitations

- Broad post-quant capability and behavioral evaluations remain pending.
- Quantization can change logits, output selection, and long-context behavior relative to BF16.
- NVFP4 requires compatible GPU hardware and a runtime with ModelOpt NVFP4 support.
- The full configured context has not been exhaustively qualified under every serving topology.
- Tool calls are model-generated data and require application-side validation and permission controls.
- Outputs may be inaccurate, incomplete, biased, or fabricated. High-impact decisions require independent review.

## Security responsibility

Deployers are responsible for authentication, authorization, rate limits, network isolation, logging, sandboxing, secrets handling, and tool-side validation. Treat retrieved content and tool output as untrusted input.

## License

The parent model and this derivative are distributed under the [LFM Open License v1.0](LICENSE). The full license text controls over this summary and includes commercial-use conditions. Quantization or redistribution does not replace or relax those terms.

## Disclaimer

“DERISKED” is the repository name, not a safety certification. This research release is provided as-is, without warranty.

## Reporting

Report reproducible issues through this repository's Hugging Face **Discussions** tab. Include the repository revision, runtime version or image digest, hardware class, serving flags, prompt/template settings, sampling parameters, and a minimal redacted reproduction.
