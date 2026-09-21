---
license: openmdw-1.1
library_name: mlx
pipeline_tag: text-generation
base_model: poolside/Laguna-S-2.1
language:
- en
- ko
- zh
tags:
- mlx
- mlx-lm
- alis-dwq
- laguna-s-2.1
---

# Laguna S 2.1 Highest Quality 4.89 bpw

This is the **highest-quality** MLX ALIS/DWQ build of
[`poolside/Laguna-S-2.1`](https://huggingface.co/poolside/Laguna-S-2.1), pinned at
`88796b991a17fc691abf1c1ad0d9f459dae73834`. The finished checkpoint is **4.89 bpw** when
rounded to two decimal places. The exact measured value remains in
`artifact_manifest.json`. Indexed tensor bytes:
71,898,420,736 bytes
(66.961 GiB).

Quantization policy: Routed-only highest-quality recipe: the 47 sparse-layer SwitchGLU gate, up, and down projections use affine Q4/group-64; attention, the layer-0 dense MLP, shared experts, embeddings, LM head, routers, norms, and biases remain BF16. No routed-expert precision promotions were required. Routers,
normalization parameters, correction bias, and other control paths remain
floating. Anchor-guarded clipping ran before DWQ with maximum error slack
1.1. FFN permutation and router KD were
disabled.

## Exact runtime requirement

This checkpoint requires the Laguna implementation at the exact mlx-lm commit
[e4338e29c8521d03d7e0c42ad139ab2bf2f07f6e](https://github.com/avlp12/mlx-lm/commit/e4338e29c8521d03d7e0c42ad139ab2bf2f07f6e); review thread: [https://github.com/ml-explore/mlx-lm/pull/1601](https://github.com/ml-explore/mlx-lm/pull/1601). Install that immutable revision:

```shell
python -m pip install "git+https://github.com/avlp12/mlx-lm.git@e4338e29c8521d03d7e0c42ad139ab2bf2f07f6e"
```

The ALIS/DWQ build evidence is bound to exact commit
[b6adb75f046042fa532fe758c6a5d0f9418e1209](https://github.com/avlp12/alis-dwq/commit/b6adb75f046042fa532fe758c6a5d0f9418e1209); review thread: [https://github.com/avlp12/alis-dwq/pull/12](https://github.com/avlp12/alis-dwq/pull/12). A pull request link, when
shown, is review context; the full commit above is the reproducibility pin.
The receipt is governed by execution `laguna-33d87555bb0c7ab6dc48`,
arm `highest-quality-routed-q4`, and campaign `3d97b1db4a6c02d7ef2fcee149c1821f426dc439d1f9161ec653d81239b81705`; its frozen planner
manifest SHA-256 is `a0e7a966530126727218557115ddbac4b76371f958c653c789883843ea98c302`.

```python
from mlx_lm import generate, load

model, tokenizer = load("avlp12/Laguna-S-2.1-Alis-MLX-Highest-Quality-4.89bpw")
prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "Implement a bounded worker queue."}],
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True,
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=512))
```

Set `enable_thinking=False` for direct answers. For agentic use, preserve prior
`reasoning_content` between tool calls as described by the source model card.

## Measured evaluation

Calibration, validation, and held-out raw bytes are disjoint. The measured data
contract contains 80 training, 40 validation, and 100 held-out rows. Held-out
coverage is code 45%, English reasoning/tool 35%, Korean 10%, and Chinese 10%.
The data manifest binds the source tokenizer file hashes and the exact
`fix_mistral_regex=true` option. The runtime-effective tokenizer file hashes differ from the source-data tokenizer file hashes; byte identity is not assumed. The release is accepted only because the equivalence contract re-verifies equal token IDs and token counts for all 220 declared rows (train 80, validation 40, held-out 100). All comparison arms
use the same held-out bytes, BF16 reference manifest, runtime-effective
tokenizer inputs/options, tokenization policy, and seed.

### Perplexity

| Checkpoint | All | Code | English | Korean | Chinese |
|---|---|---|---|---|---|
| BF16 teacher | 11.045 | 10.650 | 8.842 | 11.890 | 22.385 |
| Stock Q4/g64 | 11.824 | 11.541 | 9.423 | 12.315 | 24.419 |
| Pre-DWQ | 11.122 | 10.723 | 8.958 | 11.970 | 22.135 |
| Final ALIS/DWQ | 10.628 | 10.279 | 8.499 | 11.544 | 21.255 |

### Divergence from BF16

| Checkpoint | Mean KL | Top-1 flip | Eval tok/s | Peak memory |
|---|---|---|---|---|
| Stock Q4/g64 | 0.225565 | 13.631% | 652.53 | 62.58 GiB |
| Pre-DWQ | 0.122446 | 10.031% | 613.53 | 67.88 GiB |
| Final ALIS/DWQ | 0.107977 | 8.671% | 614.73 | 67.88 GiB |

The recomputed quality gate passed: code PPL is within 3% of stock Q4;
English, English reasoning, and Korean are each within 5%; and final-vs-pre-DWQ
paired degradation is not wholly above zero at 95% confidence on any required
major slice. The raw reports and recomputed intervals are under `evaluation/`.

Fixed greedy generation covered both thinking-on and thinking-off prompts. The
same six-row structured-message suite and seed passed on the full BF16 reference,
stock Q4, and final candidate. BF16 measured aggregate prefill
178.31 tok/s and aggregate decode
26.10 tok/s. The
final arm measured aggregate prefill 252.04
tok/s and aggregate decode 32.78
tok/s on **Apple M3 Ultra**. No new tail cycle, empty generation,
tool-format break, or distinct-4gram regression appeared relative to stock Q4.

Measured environment: Python 3.13.12 on
`macOS-26.5.2-arm64-arm-64bit-Mach-O`; mlx 0.32.0, mlx-lm 0.31.3, safetensors 0.8.0. Throughput is specific to this
environment and is not a cross-device estimate.

## DWQ and memory evidence

The BF16 teacher targets were dumped and checksummed before training. DWQ ran
deepest-first, one layer per round, with validation rollback.
Accepted rounds: 25; reverted rounds:
22. Validation KL moved from
0.070227 to
0.062731.

The full run's peak working set was
77.54 GiB
(17.23% of MLX's recommended wired limit); maximum
additional swap was 0.007 GiB. The
enforced stop thresholds were 90% of the recommended wired set and 16 GiB of
added swap.

## Context validation

The full BF16 reference and final candidate separately passed cached-vs-one-shot
logit checks at offsets 511, 512, 513, and 520 with 12 full KV caches and 36
rotating window-512 caches. Both passed needle retrieval at **8,192, 32,768
actual prompt tokens**, so the release claim is capped at
**32,768 measured tokens**.
The source architecture advertises
1,048,576 tokens, but this conversion did **not** execute a one-million-token
test; that number is calculated architectural support, not a measured claim.

## Evidence files

- `conversion_plan.json`: completed `laguna.dwq-receipt/v3` with native
  `alis-dwq.run/v2` completion and `alis-dwq.targets/v1` teacher-target binding;
  also binds artifact, data, build code, all 47 rounds, and memory
  gates
- `quantization_config.json`: emitted tensor/module quantization mapping
- `evaluation/model-card-evidence.json`: this card's path-free
  `laguna.model-card-evidence/v3` claim contract
- `evaluation/`: BF16, Q4, pre-DWQ and final logit reports; BF16, Q4 and final
  generation reports; recomputed gates; and separate BF16/final context reports
- `artifact_manifest.json`: byte size and SHA-256 for every release payload
- `NOTICE.md` and
  `SOURCE_MODEL_CARD.md`: source origin and pinned
  source-card snapshot

## Publication policy

This card is generated before remote reproduction. Release tooling will create
a fresh public repository, apply a manual access gate before any upload, upload
the accepted directory once without changing it to private, resolve its
immutable Hub SHA, re-download that exact SHA into a clean project-local cache,
and rerun manifest verification plus a strict Metal generation. Both builds
must independently produce passing remote-reproduction receipts, and both live
repositories must still be public, manual-gated, and pinned to those SHAs in one
read-only preflight before either gate is removed. No file upload or repository
settings mutation is permitted after a staging SHA is captured; the only later
settings mutation is the separate two-build ungating phase.

## License, origin, and acceptable use

This derivative retains the source **OpenMDW-1.1** license in
`LICENSE.md`. Source identity and applicable origin
notice are preserved separately; see the pinned
[source model card](https://huggingface.co/poolside/Laguna-S-2.1/blob/88796b991a17fc691abf1c1ad0d9f459dae73834/README.md) and
[Poolside acceptable-use policy](https://poolside.ai/legal/acceptable-use-policy) before
deployment. The evaluated languages are English, Korean, and Chinese; no
untested language tags are claimed.
