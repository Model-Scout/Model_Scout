---
library_name: transformers
license: mit
language:
- en
- zh
- vi
- id
- th
- fil
- ta
- ms
- my
license_link: https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/LICENSE
pipeline_tag: image-text-to-text
base_model:
- aisingapore/Qwen-SEA-LION-v4.5-27B-IT
tags:
- fp8
- quantized
- vllm
---

# Qwen-SEA-LION-v4.5-27B-IT — FP8 Dynamic

FP8 (dynamic) quantization of [aisingapore/Qwen-SEA-LION-v4.5-27B-IT](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4.5-27B-IT), produced with [llmcompressor](https://github.com/vllm-project/llm-compressor) using the `FP8_DYNAMIC` scheme.

- **Quantization:** per-tensor dynamic FP8 (w8a8), no calibration data needed
- **Size:** ~29.5 GB (vs 54.5 GB BF16)
- **Inference:** [vLLM](https://github.com/vllm-project/vllm) ≥ 0.7 with `--quantization fp8`
- **Quality:** dynamic FP8 has negligible accuracy degradation vs BF16 on standard benchmarks

## About the base model

**Qwen-SEA-LION-v4.5-27B-IT** built upon the Qwen3.6-27B dense architecture, a 27-billion parameter model featuring a hybrid Linear and Full Attention design. To ensure deep domain adaptation, the model underwent distillation from Qwen3.5-397B-A17B on an updated aisingapore/SEA-Instruct-2602, instilling multilingual and multicultural fluency across English and key SEA languages including: Burmese, Indonesian, Filipino, Malay, Tamil, Thai, and Vietnamese.

Key features inherited from Qwen3.6:

- Context Window (262K): Large context window to enable strong reasoning capabilities.
- Reasoning: Highly capable reasoning model, with configurable thinking modes.
- Thinking Preservation: Retains historical reasoning context to streamline iterative development and reduce compute overhead.
- Agentic Coding: High-precision handling of repository-level reasoning and frontend workflows.
- Unified Vision-Language: Early fusion training delivers good performance across multimodal reasoning, coding, and visual tasks.

## Quickstart (vLLM)

```bash
pip install vllm>=0.7

vllm serve toeniant/Qwen-SEA-LION-v4.5-27B-IT-FP8-Dynamic \
  --quantization fp8 \
  --max-model-len 262144
```

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="toeniant/Qwen-SEA-LION-v4.5-27B-IT-FP8-Dynamic",
    quantization="fp8",
    max_model_len=262144,
)

sampling = SamplingParams(
    temperature=0.7,
    top_p=0.80,
    top_k=20,
    max_tokens=512,
)

messages = [
    {"role": "user", "content": "Tolong carikan flat 4-bilik dekat Tampines, bajet bawah $500,000."}
]

out = llm.chat(messages, sampling_params=sampling)
print(out[0].outputs[0].text)
```

## Model Details

- **Developed by:** AI Products Pillar, AI Singapore (base model)
- **Quantized by:** toeniant
- **Model type:** Causal Language Model with Vision Encoder
- **Context length:** 262k
- **Language(s):** English, Burmese, Indonesian, Filipino, Malay, Tamil, Thai, Vietnamese
- **License:** [MIT](https://mit-license.org/)
- **Base model:** [aisingapore/Qwen-SEA-LION-v4.5-27B-IT](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4.5-27B-IT)

## Evaluation

For benchmark results, please refer to the [SEA-LION Leaderboard](https://leaderboard.sea-lion.ai/) and the original model card.

## Bias, Risks, and Limitations

The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. Like many LLMs, the model can hallucinate and occasionally generates irrelevant content. Users should exercise caution in interpreting and validating the model's responses.

## Acknowledgement

Original model by AI Singapore, supported by the National Research Foundation Singapore and IMDA under its National Large Language Model Funding Initiative. See the [original model card](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4.5-27B-IT) for full credits and team information.

## Contact

Original authors: [sealion@aisingapore.org](mailto:sealion@aisingapore.org)
