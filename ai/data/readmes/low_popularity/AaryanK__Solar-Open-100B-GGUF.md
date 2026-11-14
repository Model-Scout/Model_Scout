---
base_model: upstage/Solar-Open-100B
base_model_relation: quantized
language:
  - en
  - ko
library_name: gguf
license: other
license_name: solar-apache-2.0
license_link: https://huggingface.co/upstage/Solar-Open-100B/blob/main/LICENSE
pipeline_tag: text-generation
tags:
  - text-generation-inference
  - upstage
  - solar
  - moe
  - 100b
  - gguf
---

# Solar-Open-100B-GGUF

<p align="center">
  <img src="https://huggingface.co/upstage/Solar-Open-100B/resolve/main/Solar-Open-100B.png" alt="Solar Open Model" width="100%">
</p>

## Description

This repository contains **GGUF** format model files for [Upstage's Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B).

**Solar Open** is a massive **102B-parameter** Mixture-of-Experts (MoE) model trained from scratch on **19.7 trillion tokens**. Despite its large total size, it uses only **12B active parameters** during inference, offering a unique combination of massive knowledge capacity and efficient generation speed.



*Note: Please check the specific file sizes in the "Files and versions" tab.*

## How to Run (llama.cpp)

**Recommended Parameters:**
Upstage recommends the following sampling parameters for Solar Open:
*   **Temperature:** `0.8`
*   **Top-P:** `0.95`
*   **Top-K:** `50`

### CLI Example

```bash
./llama-cli -m Solar-Open-100B.Q4_K_M.gguf \
  -c 8192 \
  --temp 0.8 \
  --top-p 0.95 \
  --top-k 50 \
  -p "User: Who are you?\nAssistant:" \
  -cnv
```

### Server Example

```bash
./llama-server -m Solar-Open-100B.Q4_K_M.gguf \
  --port 8080 \
  --host 0.0.0.0 \
  -c 8192 \
  -ngl 99
```

## License

The model weights are licensed under the **Solar-Apache License 2.0**.
Please review the full license terms here: [LICENSE](https://huggingface.co/upstage/Solar-Open-100B/blob/main/LICENSE)

## Citation

If you use Solar Open in your research, please cite:

```bibtex
@misc{solar-open-2025,
    title={Solar Open: Scaling Upstage's LLM Capabilities with MoE},
    author={Upstage AI},
    year={2025},
    url={https://huggingface.co/Upstage/Solar-Open-100B}
}
```