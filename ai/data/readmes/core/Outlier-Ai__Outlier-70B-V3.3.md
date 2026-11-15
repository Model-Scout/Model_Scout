---
license: apache-2.0
pipeline_tag: text-generation
library_name: transformers
base_model: Qwen/Qwen2.5-32B-Instruct
base_model_relation: adapter
tags:
  - mixture-of-experts
  - moe
  - ternary
  - quantized
  - qwen2.5
  - outlier
  - local-llm
  - on-device
  - edge-ai
  - energy-efficient
  - sparse
  - overlay
  - research
  - apple-silicon
  - mac
  - mmlu-verified
language:
  - en
  - zh
  - fr
  - es
  - pt
  - de
  - it
  - ru
  - ja
  - ko
  - ar
  - vi
  - th
  - nl
  - pl
datasets: []
widget:
- example_title: Widget math
  messages:
  - role: user
    content: "If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets? Show reasoning step by step."
- example_title: Logic grid
  messages:
  - role: user
    content: "Alice, Bob, and Carol each own a different pet (dog, cat, parrot). Alice does not own the dog. Bob owns the parrot. Who owns what?"
- example_title: Word problem
  messages:
  - role: user
    content: "A train leaves station A at 60 mph and another leaves station B, 180 miles away, at 40 mph traveling toward each other. When do they meet?"
model-index:
  - name: Outlier-70B-V3.3
    results:
      - task:
          type: text-generation
        dataset:
          name: MMLU
          type: cais/mmlu
        metrics:
          - type: accuracy
            value: 83.1
            name: MMLU 5-shot
---

> **Research checkpoint.** Not shipped in the Outlier app. Numbers below are from internal experiments, not our release tests. Shipped models: [Nano 4B](https://huggingface.co/Outlier-Ai/Outlier-Nano-4B-MLX-4bit) · [Lite 9B](https://huggingface.co/Outlier-Ai/Outlier-Lite-9B-MLX-4bit) · [Quick 26B](https://huggingface.co/Outlier-Ai/Outlier-Quick-26B-MLX-4bit) · [Core 27B](https://huggingface.co/Outlier-Ai/Outlier-Core-27B-MLX-4bit).

> **Superseded.** This repo is a research artifact from an earlier Outlier lineage and is no longer the recommended download. The current shipping tier is at **[outlier.host](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=outlier_70b_v3_3)**.
> Outlier for Mac: free Nano and Lite; Pro is **$49 once**, on up to 3 Macs · `brew install --cask outlier-host/tap/outlier`

# Outlier-70B-V3.3

This repo predates the v1.8 Outlier lineup. It is preserved here for reproducibility and historical reference, not as a production recommendation.

## What replaced it

Current shipping tiers (see Outlier app v1.8+):

- [Outlier Nano 4B — current entry tier](https://huggingface.co/Outlier-Ai/Outlier-Nano-4B-MLX-4bit)
- [Outlier Core 27B — current default tier](https://huggingface.co/Outlier-Ai/Outlier-Core-27B-MLX-4bit)
- [Outlier Vision 35B-A3B — current multimodal tier](https://huggingface.co/Outlier-Ai/Outlier-Vision-35B-A3B-MLX-4bit)
- [DeepSeek-R1-Distill-Qwen-7B — popular reasoning model](https://huggingface.co/Outlier-Ai/DeepSeek-R1-Distill-Qwen-7B-MLX-4bit)
- [Qwen3-Coder-30B-A3B — popular coding model](https://huggingface.co/Outlier-Ai/Qwen3-Coder-30B-A3B-Instruct-MLX-4bit)

For the latest verified benchmarks and downloads, visit **[outlier.host](https://outlier.host/?utm_source=hf&utm_medium=modelcard&utm_campaign=outlier_70b_v3_3)**.

## Original notes

This was a research / preview artifact. It may contain experimental adapters, overlays, or quantization variants that did not graduate into the shipping product. Treat any technical claims in earlier revisions of this card as provisional.

## License

See YAML frontmatter above. Original license terms preserved.
