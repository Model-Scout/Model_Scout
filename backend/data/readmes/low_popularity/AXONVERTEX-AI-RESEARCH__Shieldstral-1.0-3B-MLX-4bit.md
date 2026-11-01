---
license: apache-2.0
base_model: mistralai/Shieldstral-1.0-3B
library_name: mlx-vlm
pipeline_tag: image-text-to-text
tags:
  - mlx
  - mlx-vlm
  - apple-silicon
  - mistral3
  - pixtral
  - guardrail
  - content-moderation
  - safety-classification
  - multimodal
  - 4-bit
language:
  - en
  - fr
  - es
  - de
  - it
  - pt
  - nl
  - zh
  - ja
  - ko
  - ar
  - ru
---

# Shieldstral 1.0 3B MLX 4-bit for Apple Silicon

A ready-to-run Apple MLX-VLM conversion of Mistral AI's [`mistralai/Shieldstral-1.0-3B`](https://huggingface.co/mistralai/Shieldstral-1.0-3B).

This repository is for **downloading and running the converted model**. Conversion source code and engineering history belong in the companion GitHub repository, not in this model repository.

This is an independent AXONVERTEX AI conversion and validation release. It is not an official Mistral AI release.

## Model summary

Shieldstral is a compact policy-adaptive multimodal safety classifier. It receives:

- `<Instruct>`: moderation context and strictness;
- `<Query>`: one yes-or-no policy question;
- `<Document>`: text, a prompt-response pair, an image, or image-plus-text.

It emits one `yes` or `no` token. A continuous score is obtained by renormalizing the two next-token log probabilities:

```text
score = exp(logit_yes) / (exp(logit_yes) + exp(logit_no))
```

The default binary threshold is `0.5`.

## Release facts

| Field | Value |
|---|---|
| Upstream publisher | Mistral AI |
| Upstream model | `mistralai/Shieldstral-1.0-3B` |
| Upstream revision | `b6073e818d5d119c772e44b84372b62bd51c2a00` |
| Runtime | MLX-VLM |
| Quantization | 4-bit affine, group size 64 |
| Vision tower | Floating point, not quantized |
| Artifact size | Approximately 2.79 GB |
| Validated Mac | Apple M1, 16 GB unified memory |
| Validated context cap | 16,384 tokens |
| License | Apache-2.0 |

## Quick start

### 1. Download

For a private repository, authenticate first:

```bash
python3 -m pip install --upgrade "huggingface-hub[cli]"
hf auth login
```

Download the complete model repository:

```bash
cd ~/Downloads
hf download \
  AXONVERTEX-AI-RESEARCH/Shieldstral-1.0-3B-MLX-4bit \
  --local-dir Shieldstral-1.0-3B-MLX-4bit

cd Shieldstral-1.0-3B-MLX-4bit
```

Hugging Face creates `.cache/huggingface/` inside a `--local-dir` download. It is download metadata, not model content. It can be removed after the download:

```bash
rm -rf .cache/huggingface
```

### 2. Install the Apple MLX runtime

```bash
./scripts/install.sh
```

Activate the environment:

```bash
source .venv/bin/activate
```

### 3. Verify the downloaded release

```bash
./scripts/verify_checksums.sh
./scripts/validate_model.sh
```

### 4. Start the local server

```bash
./scripts/start_server.sh
```

Default service:

```text
http://127.0.0.1:18190
http://127.0.0.1:18190/v1
```

The server uses:

- 16,384-token context cap;
- 8-bit KV cache;
- top-20 token log probabilities;
- local-only binding by default.

### 5. Test from a second terminal

```bash
cd ~/Downloads/Shieldstral-1.0-3B-MLX-4bit
source .venv/bin/activate

./scripts/health.sh
./scripts/smoke_test.sh
./scripts/run_paper_alignment.sh
```

## Direct curl example

Set the model identifier to the downloaded directory:

```bash
export MODEL_ID="$(pwd)"
export BASE_URL="http://127.0.0.1:18190/v1"
```

```bash
curl --fail --silent --show-error \
  "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$MODEL_ID\",
    \"messages\": [
      {
        \"role\": \"system\",
        \"content\": \"Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \\\"yes\\\" or \\\"no\\\".\"
      },
      {
        \"role\": \"user\",
        \"content\": \"<Instruct>: You are reviewing cybersecurity content. Permit defensive and authorized security guidance.\\n\\n<Query>: Is this content unsafe?\\n\\n<Document>: Explain how to configure SSH key authentication and disable password login.\"
      }
    ],
    \"max_tokens\": 1,
    \"temperature\": 0.0,
    \"logprobs\": true,
    \"top_logprobs\": 20,
    \"stream\": false
  }" | python -m json.tool
```

Expected literal answer: `no`.

For score extraction and more examples, use:

```bash
./scripts/score.sh \
  --instruct "You are reviewing cybersecurity content. Permit defensive and authorized security guidance." \
  --query "Is this content unsafe?" \
  --document "Explain how to configure SSH key authentication and disable password login."
```

## Documentation

- [`docs/APPLE_MLX_DEPLOYMENT.md`](docs/APPLE_MLX_DEPLOYMENT.md): download, installation, serving, background deployment, memory tuning and troubleshooting.
- [`docs/CURL_COOKBOOK.md`](docs/CURL_COOKBOOK.md): complete text, response, refusal, adaptability, multilingual and multimodal curl cookbook.
- [`docs/TECHNICAL_REPORT_ALIGNMENT.md`](docs/TECHNICAL_REPORT_ALIGNMENT.md): mapping to the Shieldstral technical report and reference protocol.
- [`docs/EVALUATION_REPORT.md`](docs/EVALUATION_REPORT.md): conversion and local evaluation evidence.
- [`docs/SOURCE_AND_LICENSE.md`](docs/SOURCE_AND_LICENSE.md): source provenance, attribution and licensing.

## Validated evaluation evidence

### Runtime and protocol regression

The included 13-case regression suite passed `13/13` on the validated Apple M1 system. It verifies runtime correctness and selected policy behavior; it is not a complete safety benchmark.

```text
cases = 13
correct = 13 / 13
accuracy = 100.00%
F1 = 100.00%
protocol checks = 5 / 5
mean latency = 0.7552 seconds
P95 latency = 0.9343 seconds
```

### Source-exact CAT001 case scenario

**Physical Harm vs. Unlawful Confinement** is a two-case boundary scenario using a source-exact published instruction, policy query and paired documents.

```text
cases = 2
correct = 1 / 2
accuracy = 50.00%
precision = 50.00%
recall = 100.00%
F1 = 66.67%
protocol validity = 100.00%
confusion = TP 1, TN 0, FP 1, FN 0
```

The direct-injury case passed. The unlawful-confinement sibling case produced a false positive with score `0.705785`.

Run it with:

```bash
./scripts/run_case_scenario.sh
```

### Full-hierarchy scenario suite

The AXONVERTEX-derived hierarchy suite covers 12 superclasses, 26 subcategories, 52 leaves and 90 total policy nodes.

```text
cases = 180
correct = 170 / 180
accuracy = 94.44%
precision = 91.67%
recall = 97.78%
F1 = 94.62%
protocol validity = 100.00%
confusion = TP 88, TN 82, FP 8, FN 2
mean latency = 1.5324 seconds
P95 latency = 1.8424 seconds
```

The 180-case suite and reconstructed queries are AXONVERTEX-derived, except for explicitly marked source-exact CAT001 material. The release does not claim reproduction of Mistral's unpublished full evaluation dataset or source-model benchmark parity.

## 8-bit and BF16

This repository contains only the validated **4-bit** artifact.

- 8-bit should be published as a separate model repository after conversion and parity evaluation.
- BF16 should remain a separate artifact because it has different memory requirements and is not the recommended always-on choice for a 16 GB unified-memory Mac.

Do not mix 4-bit, 8-bit and BF16 weights in this repository.


<!-- BEGIN GRAPHSHIELD_MISTRAL_MODEL_CARD -->
## Named hierarchical classification and GraphShieldMistral

The release provides two complementary ways to use Shieldstral.

### Direct named classifier

Use the existing classifier when a machine-readable decision is the primary requirement:

```bash
./scripts/classify_node.sh   CAT024   "A request asks for a malicious executable that encrypts files on a victim computer."

./scripts/hierarchical_classify.sh   "A request asks for a malicious executable that encrypts files on a victim computer."   --mode exhaustive   --workers 2   --top 0
```

The direct classifier remains the authoritative source for:

- raw model matches;
- descendant-supported matches;
- the primary leaf category;
- the validated superclass-to-leaf path;
- secondary matched leaves and ambiguity;
- orphan broad-policy matches;
- hierarchy-consistency metadata.

### GraphShieldMistral

[`graphShieldMistral/`](graphShieldMistral/) is an optional NetworkX-based analysis and visualisation layer over the same reconciled classifier JSON. It does not replace the direct classifier and does not change the model prediction.

![GraphShieldMistral hierarchical classification and scenario cluster map](graphShieldMistral/assets/graph-classifier-map.png)

The graph view can:

- organise the published 90-node hierarchy into 12 deterministic superclass clusters;
- attach classified documents to their validated paths;
- show the exact input document, instruction and primary policy query;
- separate validated, raw and orphan matches;
- distinguish `SAFE`, `UNRESOLVED`, `CLASSIFIED` and `AMBIGUOUS` outcomes;
- retain secondary leaves instead of hiding multi-label behaviour;
- export HTML, SVG, JSON and GraphML for audit, graph analytics and Graph-RAG experiments.

Build a graph from a classifier result:

```bash
mkdir -p reports/local/graph-inputs

./scripts/hierarchical_classify.sh   "A request asks for a malicious executable that encrypts files on a victim computer."   --mode exhaustive   --workers 2   --top 0   > reports/local/graph-inputs/malware.json

./graphShieldMistral/scripts/build_graph.sh   --result reports/local/graph-inputs/malware.json   --output-dir reports/local/graphshield-malware

open reports/local/graphshield-malware/classification-network.html
```

See:

- [`graphShieldMistral/README.md`](graphShieldMistral/README.md)
- [`docs/GRAPHSHIELD_MISTRAL.md`](docs/GRAPHSHIELD_MISTRAL.md)
- [`docs/HIERARCHICAL_CLASSIFICATION.md`](docs/HIERARCHICAL_CLASSIFICATION.md)
- [`docs/HIERARCHY_RECONCILIATION.md`](docs/HIERARCHY_RECONCILIATION.md)

The static image above is a recorded example. Rebuild the graph from local classifier output when auditing a new document.
<!-- END GRAPHSHIELD_MISTRAL_MODEL_CARD -->
## Limitations

The upstream model card notes uneven language/domain coverage and reduced reliability on adversarial, obfuscated or very long inputs. A local guardrail should be one component of a layered control system rather than the sole authorization mechanism.

## Reconciled hierarchy output

The consumer release provides raw and descendant-supported classification views. Broad policy positives without a matched leaf are reported under `orphan_policy_matches` and excluded from the final named hierarchy. The source-exact CAT001 boundary case scenario is available through:

```bash
./scripts/run_case_scenario.sh
```

See `docs/HIERARCHY_RECONCILIATION.md` and `docs/SOURCE_EXACT_CASE_SCENARIO.md`.

<!-- graphshield-mistral -->
## GraphShieldMistral classification network

`graphShieldMistral/` is a self-contained NetworkX layer for the named hierarchical classifier. It prints the exact submitted document, the policy query for every class, reconciled paths, observed scores, structural clusters, safe similar examples and scenario clusters.

Scenario states are explicit:

- `SAFE`: no raw or descendant-supported unsafe match;
- `UNRESOLVED`: broad/raw unsafe matches exist, but no leaf is validated;
- `CLASSIFIED`: exactly one leaf is validated;
- `AMBIGUOUS`: multiple leaves are validated and all are retained.

```bash
./graphShieldMistral/scripts/run_examples.sh
open graphShieldMistral/outputs/examples/malware/classification-network.html
```

Taxonomy-only nodes are marked **not evaluated** rather than displaying misleading zero scores. Outputs include offline HTML, static SVG, GraphML, node-link JSON and cluster summaries. See `graphShieldMistral/README.md` and `docs/CLASSIFICATION_GRAPH_NETWORK.md`.
