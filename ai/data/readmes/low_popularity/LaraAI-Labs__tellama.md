---
license: apache-2.0
base_model: Qwen/Qwen3-4B
language:
  - ko
  - en
pipeline_tag: text-generation
tags:
  - gguf
  - android
  - quantized
  - llama-cpp
---

# Tellama models for local Android AI

[한국어 안내](README.ko.md) · [Download and setup](docs/USAGE.md) · [Measurements](docs/EVALUATION.md) · [Tellama website](https://redpluglab.github.io/tellama/)

Tellama runs language models locally on Android. This repository provides GGUF model files, their licenses, quantization recipes and evaluation records. Start with **TM Qwen3 4B Q4_K_M** if you want the model used in Tellama's current high-end-device validation. It supports text conversations; Korean and English were included in our checks.

**Current status, October 7, 2026:** the Tellama **1.3.11 (41)** app baseline was frozen as `gold-v1.3.11` on October 5. This is a verified reference build, not a Google Play release announcement. Long response waits and a historical intermittent wrong answer remain unresolved. No model weights changed in this documentation update.

## Choose a model

| File | Role | Download size |
| --- | --- | --- |
| [TM Qwen3 4B Q4_K_M](https://huggingface.co/LaraAI-Labs/tellama/resolve/fa04ad644a423cc3ab5b38029a371c456ae7ecb0/models/qwen3-4b-tellama-thinking-q4_k_m.gguf?download=true) | Current Tellama catalog model; CPU, DEEP thinking mode | 2.59 GB / 2.41 GiB |
| `models/qwen3.5-4b-q4_k_m.gguf` | Historical experiment; failed extended arithmetic screening; not offered for new downloads in the current Tellama catalog | 3.01 GB |

The model download size is not the total RAM needed to run it. Tellama also needs memory for the runtime, context and operating system. The measured device is **Samsung Galaxy Z Fold6 SM-F956N, Android 16**. Other phones, FAST mode and GPU inference are not covered by this validation.

## Get started

**In Tellama:** open **Models**, choose **TM Qwen3 4B Q4_K_M**, complete the download and verification, and review the DEEP-mode notice. Then open **Chat** and start a conversation. The current release scope uses supplied, verified TM models; it does not provide arbitrary model imports or external AI API connections.

**With another GGUF runtime:** download the exact file below. Use a runtime that supports Qwen3 and its chat template. Other runtimes are outside Tellama's device validation; this repository does not provide a Transformers-format checkpoint.

```sh
hf download LaraAI-Labs/tellama \
  models/qwen3-4b-tellama-thinking-q4_k_m.gguf \
  --revision fa04ad644a423cc3ab5b38029a371c456ae7ecb0 \
  --local-dir ./tellama-models
```

See [setup and checksum instructions](docs/USAGE.md), including Windows verification and memory troubleshooting. Download the named file rather than the entire repository, which also contains the historical model.

## What to expect

Ordinary TM chat inference runs on the device after download. Model downloads, web research and optional AI response reports use network access. When submitting a report, the user reviews and consents to the content sent. See the [privacy policy](https://redpluglab.github.io/tellama/privacy/) and [한국어 개인정보처리방침](https://redpluglab.github.io/tellama/privacy/ko/).

This distribution uses internal reasoning before displaying its final answer. In a 30-minute Fold6 battery test, visible-answer waits ranged **14.6–199.8 seconds**, with a **37.8-second median** across 41 uninterrupted observations. These are answer-visibility times, not native first-token latency (TTFT), and not a forecast for every prompt. Short questions can still take a long time.

An earlier signed-app test produced one wrong arithmetic follow-up: **15 → 16 → 18**, where **17** was expected. Later passing runs do not establish that this failure is fixed. Check important answers independently. See [test conditions and results](docs/EVALUATION.md) before treating a small synthetic score as general accuracy.

## Exact artifact and provenance

| Property | Value |
| --- | --- |
| Model ID | `qwen3-4b-tellama-thinking-q4_k_m` |
| File | `models/qwen3-4b-tellama-thinking-q4_k_m.gguf` |
| Exact size | 2,591,481,472 bytes |
| SHA-256 | `01e739de8a200c769e72a676d038b84b1c042bd160a153a348fbb443bd713b85` |
| Base model | [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) |
| Base revision | `1cfa9a7208912126459214e8b04321603b3df60c` |
| Quantization | F16 → Q4_K_M, retaining Q8_0 token embeddings and output tensors |
| llama.cpp revision | `cb295bf59663cd3577389315636772f4060bd1f5` |
| License | [Apache 2.0](https://huggingface.co/LaraAI-Labs/tellama/blob/main/licenses/qwen3-4b-tellama-thinking-q4_k_m/LICENSE) |

Tellama performed quantization and packaging, without fine-tuning or calibration. Qwen/Alibaba Cloud retains authorship of the base model; this work does not imply Qwen endorsement. [Attribution](https://huggingface.co/LaraAI-Labs/tellama/blob/main/licenses/qwen3-4b-tellama-thinking-q4_k_m/NOTICE), [recipe](recipes/qwen3-4b-tellama-thinking-q4_k_m.json), [artifact manifest](manifests/qwen3-4b-tellama-thinking-q4_k_m.json) and [qualification status](qualification-status.json) are available in this repository. Historical `qualified` metadata describes the recorded model-screening gates, not unconditional app release approval.

## Feedback

Use the [Community tab](https://huggingface.co/LaraAI-Labs/tellama/discussions) for model questions and reproducible issues. Include the model filename, app/runtime version, device and Android version, and a short non-sensitive example with expected and actual results. Do not post private conversations, credentials or device identifiers.

For AI response reports and report deletion requests, contact **support@redplug.co.kr**. For deletion, include the report receipt ID instead of resending the conversation.

## Documentation update

October 7, 2026: added Korean guidance, pinned download and checksum steps, current app-baseline status, later Fold6 results and known limitations. Existing GGUF files, licenses, recipes and original evaluation records are preserved. Additional performance tuning remains on hold.
