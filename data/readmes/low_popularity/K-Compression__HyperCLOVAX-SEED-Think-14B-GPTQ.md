---
license: other
language:
- ko
- en
base_model:
- naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
pipeline_tag: text-generation
library_name: transformers
---

# HyperCLOVAX-SEED-Think-14B-GPTQ

## Instruction

This repo contains GPTQ model files for HyperCLOVAX-SEED-Think-14B. 

HyperCLOVAX-SEED-Think-14B-GPTQ was quantized using gptqmodel v4.0.0, following the guide.

### Model Configuration

- Original model: [naver-hyperclovax/HyperCLOVAX-SEED-Think-14B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B/blob/main/config.json)
- Quantization: GPTQ with 4-bit group-wise weight-only quantization (W4A16g128)

## Quickstart

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "K-Compression/HyperCLOVAX-SEED-Think-14B-GPTQ"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="bfloat16",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

## Performance(Non-Think)
| Model | MMLU (0-shot) | HAERAE (0-shot) |
|-----------------------------------------|--------|--------|
| HyperCLOVA X SEED 14B Think | 0.7144 | 0.8130 |
| HyperCLOVA X SEED 14B Think-GPTQ | 0.7018 | 0.8139 |

## License

The model is licensed under [HyperCLOVA X SEED Model License Agreement](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B/blob/main/LICENSE)
