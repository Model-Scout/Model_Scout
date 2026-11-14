---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
  - LiquidAI/LFM2.5-24B-A2B
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
  - bfloat16
  - conversational
  - lfm2.5
  - moe
  - reasoning
  - tool-calling
  - transformers
  - behavioral-modification
  - blackfrost
---

<p align="center">
  <img src="ASSETS/BLACKFROST-AI-BANNER.png" alt="BLACKFROST-AI" width="100%">
</p>

# LFM2.5-24B-A2B-DERISKED-BF16

Standalone BF16 behaviorally modified derivative of Liquid AI's LFM2.5-24B-A2B for reasoning, multilingual chat, and tool-enabled workflows.

> **Release status:** public and ungated. The standalone BF16 checkpoint, configuration, tokenizer, model card, account banner, license, and deployment kit are included.

## Artifact contents

| Component | Status |
|---|---|
| Model card | Included |
| Blackfrost-AI account banner | Included |
| LFM Open License v1.0 | Included |
| Deployment kit | Included under [`DEPLOYMENT/`](DEPLOYMENT/) |
| Standalone BF16 weights | Included: 10 SafeTensors shards |
| Model configuration, tokenizer, generation configuration, and chat template | Included |

This is a standalone checkpoint. It is not an adapter and does not require the parent checkpoint at inference time.

## Why this release exists

LFM2.5-24B-A2B is a sparse mixture-of-experts model with explicit reasoning, multilingual support, long-context capability, and structured tool use. This derivative provides an alternate behavioral operating point while retaining the parent architecture and full BF16 representation.

The weights are behaviorally modified. The proprietary transformation process and reconstruction materials are not distributed.

## Model specifications

| Property | Value |
|---|---|
| Architecture | `Lfm2MoeForCausalLM`, sparse mixture of experts |
| Precision | BF16 |
| Total parameters | Approximately 24B |
| Active parameters per token | Approximately 2.45B |
| Model blocks | 40 |
| Experts per MoE block | 64 |
| Routed experts per token | 4 |
| Sequence mixing | 30 convolution blocks and 10 grouped-query-attention blocks |
| Languages | 16 languages listed in the repository metadata |
| Reasoning | Always-thinking chat template |
| Tool use | Structured tool calls through the packaged chat template |
| Native configured context | 131,072 tokens |
| Checkpoint tensor footprint | 47,943,180,288 bytes |
| Weight shards | 10 SafeTensors shards |

Architecture and upstream training details are documented in the [LiquidAI/LFM2.5-24B-A2B model card](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B).

## Complete lineage

1. Foundational and immediate parent: [`LiquidAI/LFM2.5-24B-A2B`](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B)
2. Immutable parent revision: `1769516ac588c4c558089c94f27d96b0dc67b183`
3. Tokenizer, generation configuration, and chat-template lineage: parent LFM2.5 release
4. Blackfrost stage: behaviorally modified derivative; the proprietary transformation process is not distributed
5. Public artifact: standalone BF16 SafeTensors checkpoint

No upstream benchmark result is presented as a measurement of this derivative. Consult the parent card for upstream evaluations and training-data documentation.

## Artifact verification and checksums

The release candidate completed structural and numerical verification:

- all 10 expected weight shards are present;
- all 7,610 expected source tensor keys are represented;
- no unexpected missing or non-finite tensors were found;
- configuration, tokenizer, generation configuration, and chat-template assets are present;
- native MTP/NextN payload accounting is `0 → 0`: neither the pinned parent checkpoint nor this derivative contains embedded MTP/NextN tensors or configuration fields.

| Item | SHA-256 |
|---|---|
| Parent checkpoint aggregate | `0a7de2eaf633c1b5dd55c963521267c8ac6c1fb7aac82705ea01444df93e3bb5` |
| This BF16 checkpoint aggregate | `587d8247c6964ff7b06235d7968b3d80f87889c325ca616140fb1f77e627eee5` |
| `config.json` | `b0c46662afe3881e49cf542e683bf5ea8a5e0b780a429b6141a48defc33531bf` |
| `model.safetensors.index.json` | `b3c3d025ee3b7e78ca3d6160d1be872d85ff03272c64b0c2b5fc85a6f36c622f` |
| `tokenizer_config.json` | `11f1de897317b489dd09199284528382eeb17f566398b16e2039bb2266d26b09` |
| `chat_template.jinja` | `ea663864491de7ade391839479860ca95541f892f72665c73251fbd4643b1bef` |
| `LICENSE` | `4d28ca14dedc0b3d0fcc2b3339f0e79931faa33874f3d24f522183a8fc70068c` |

The Hub revision records the complete checkpoint file inventory. Deployment-kit checksums are included in [`DEPLOYMENT/CHECKSUMS.sha256`](DEPLOYMENT/CHECKSUMS.sha256).

## Measured behavioral and capability evaluation

A narrow distribution-preservation probe compared the persisted BF16 derivative with its pinned parent across eight held-out prompts and 155 scored tokens.

| Measurement | Result |
|---|---:|
| Relative negative-log-likelihood delta | -0.00305% |
| Jensen–Shannon divergence | 0.006415 |
| Token top-1 agreement | 95.48% |
| Internal automatic preservation gate | Passed |

These measurements are limited checks, not a comprehensive capability or safety benchmark. The complete false-refusal/red-line behavior battery, registered capability profile, broad academic benchmarks, and multilingual regression suite have not been run on this artifact.

## Prompt, reasoning, and sampling notes

Use the packaged chat template through `tokenizer.apply_chat_template()` rather than assembling control tokens by hand. The template begins assistant turns in reasoning mode and supports structured tool definitions and tool-result reinjection.

The upstream recommended sampling defaults are:

| Parameter | Value |
|---|---:|
| `temperature` | `0.1` |
| `top_k` | `50` |
| `repetition_penalty` | `1.05` |

Applications should validate their own system prompts, sampling settings, structured-output schemas, and tool policies. This release does not prescribe a default persona or application policy.

## Deployment

The included [`DEPLOYMENT/`](DEPLOYMENT/) kit contains the reproducible OpenAI-compatible serving profile, environment variables, smoke test, dependency provenance, and checksums validated for this artifact. Start with [`DEPLOYMENT/README.md`](DEPLOYMENT/README.md).

The configured 131,072-token context is inherited from the parent configuration. Deployments must qualify the context length they intend to use against their hardware, concurrency, and latency requirements.

## Limitations

- This derivative has not received a comprehensive academic, coding, multilingual, safety, or refusal-behavior evaluation.
- The narrow distribution probe does not establish general behavioral equivalence or retained capability.
- The full configured context has not been exhaustively qualified under every serving topology.
- Tool calls are model-generated data. Validate function names, schemas, arguments, authorization, and tool outputs before execution.
- Outputs may be inaccurate, incomplete, biased, or fabricated. High-impact decisions require independent review.

## Security responsibility

Deployers are responsible for authentication, authorization, rate limits, network isolation, logging, sandboxing, secrets handling, and tool-side validation. Treat retrieved content and tool output as untrusted input, and never give the model broader privileges than the surrounding application requires.

## License

The parent model and this derivative are distributed under the [LFM Open License v1.0](LICENSE). The full license text controls over this summary. The license contains commercial-use conditions, including separate licensing requirements for some organizations at or above its stated annual-revenue threshold. Quantization or redistribution does not replace or relax the parent license terms.

## Disclaimer

“DERISKED” is the repository name, not a certification that the model is safe for every use. This research release is provided as-is, without warranty. Users are responsible for determining whether the model, generated output, and deployment configuration are appropriate for their application and jurisdiction.

## Reporting

Report reproducible model, card, tokenizer, or deployment-kit issues through this repository's Hugging Face **Discussions** tab. Include the repository revision, runtime version or image digest, hardware class, serving flags, prompt/template settings, sampling parameters, and a minimal redacted reproduction.
