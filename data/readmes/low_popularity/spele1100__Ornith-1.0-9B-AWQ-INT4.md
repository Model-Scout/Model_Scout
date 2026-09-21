---
library_name: transformers
license: mit
language:
  - en
  - zh
  - ja
  - ko
tags:
  - awq
  - int4
  - quantized
  - ornith
  - qwen3.5
  - code
base_model: ornith-ai/Ornith-1.0-9B
---

# Ornith-1.0-9B-AWQ-INT4

AWQ INT4 (pack-quantized) conversion of [Ornith-1.0-9B](https://huggingface.co/ornith-ai/Ornith-1.0-9B), optimized for vLLM AWQ kernel inference.

## Details

| | Value |
|---|---|
| **Base model** | ornith-ai/Ornith-1.0-9B (Qwen3.5 9B Dense) |
| **Quant method** | GPTQ (llmcompressor) |
| **Precision** | W4A16 (INT4 weights, FP16 activations) |
| **Format** | pack-quantized |
| **Group size** | 128 |
| **Observer** | memoryless_minmax |
| **Calibration** | 128 samples (UltraChat 200k) |
| **Model size** | 5.8 GB (vs 19 GB BF16) |
| **Compression ratio** | ~3.3x |

## Compatibility

- ✅ **vLLM** (AWQ kernel, pack-quantized format)
- ✅ **SGLang**
- ✅ **Transformers** (with compressed-tensors)

## Usage

```python
from vllm import LLM, SamplingParams

llm = LLM(model=spele1100/Ornith-1.0-9B-AWQ-INT4, quantization=awq)
sampling = SamplingParams(temperature=0.6, top_p=0.95, top_k=20)
output = llm.generate([Hello!], sampling)
print(output[0].outputs[0].text)
```

## Quantization Script

```python
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier
from transformers import AutoTokenizer
from datasets import load_dataset

model = ornith-ai/Ornith-1.0-9B
tok = AutoTokenizer.from_pretrained(model, trust_remote_code=True)
ds = load_dataset(HuggingFaceH4/ultrachat_200k, split=train_sft).select(range(512))

recipe = GPTQModifier(
    targets=Linear,
    scheme=W4A16,
    ignore=[model.visual.*],
)

oneshot(
    model=model,
    recipe=recipe,
    output_dir=./Ornith-1.0-9B-AWQ-INT4,
    tokenizer=tok,
    dataset=ds,
    max_seq_length=512,
    num_calibration_samples=128,
)
```

## Hardware

Quantized on a single NVIDIA A100-80GB-SXM4 via RunPod.

## License

MIT — inherits from [Ornith-1.0-9B](https://huggingface.co/ornith-ai/Ornith-1.0-9B).

## Acknowledgements

- [Ornith-1.0](https://huggingface.co/ornith-ai) by Deep Reinforce AI
- [llmcompressor](https://github.com/vllm-project/llm-compressor) by vLLM Project
- [cyankiwi/Ornith-1.0-9B-AWQ-INT4](https://huggingface.co/cyankiwi/Ornith-1.0-9B-AWQ-INT4) for reference
