---
license: mit
language:
- multilingual
- en
- zh
- de
- es
- fr
- it
- ja
- ko
- pt
- ru
pipeline_tag: feature-extraction
tags:
- mlx
- embedding
- text-embeddings-inference
- retrieval
- sentence-transformers
library_name: mlx
base_model: BAAI/bge-m3
---

# BGE-M3 MLX (FP16)

This is the [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) model converted to MLX format for Apple Silicon.

## Model Description

BGE-M3 is a versatile embedding model capable of:
- Dense retrieval
- Sparse retrieval
- Multi-vector (ColBERT) retrieval

This MLX conversion enables efficient inference on Apple Silicon Macs.

## Model Details

| Property | Value |
|----------|-------|
| Architecture | XLM-RoBERTa |
| Precision | FP16 (float16) |
| Embedding Dimension | 1024 |
| Max Sequence Length | 8192 |
| Model Size | ~1.1 GB |
| Languages | 100+ languages |

## Usage

### With MLX

```python
from mlx_embeddings.utils import load_model, load_tokenizer
import mlx.core as mx

model_path = "mlx-community/bge-m3-mlx-fp16"

# Load model and tokenizer
model = load_model(model_path)
tokenizer = load_tokenizer(model_path)

# Generate embeddings
text = "Hello, world!"
tokens = tokenizer.encode(text)
input_ids = mx.array([tokens])
output = model(input_ids)
embedding = output.last_hidden_state.mean(axis=1)  # Mean pooling

print(f"Embedding shape: {embedding.shape}")  # (1, 1024)
```

### With oMLX

```bash
# Start oMLX server
omlx serve --model-dir /path/to/models

# Get embeddings via API
curl http://127.0.0.1:8000/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{"model": "bge-m3-mlx-fp16", "input": "Your text here"}'
```

### With Python (OpenAI-compatible)

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="dummy")

response = client.embeddings.create(
    model="bge-m3-mlx-fp16",
    input="Your text here"
)
embedding = response.data[0].embedding  # 1024-dimensional vector
```

## Performance

Tested on macOS with Apple Silicon:
- Successfully generates 1024-dimensional embeddings
- Supports multilingual text (English, Chinese, Japanese, Korean, etc.)
- Compatible with oMLX embedding endpoint

## Conversion Details

This model was converted from the original BAAI/bge-m3 using:
- mlx-embeddings conversion tool
- FP16 precision for balanced size and quality

## License

This model inherits the MIT license from the original BAAI/bge-m3 model.

## Citation

```bibtex
@article{bge_m3,
  title={BGE M3-Embedding: Accurate, Efficient and Versatile Text Embedding},
  author={Chen, Jianlv and Xiao, Shitao and Zhang, Peitian and Luo, Kun and Zhang, Zheng},
  journal={arXiv preprint arXiv:2402.03216},
  year={2024}
}
```

## Disclaimer

This is an unofficial MLX conversion of the BAAI/bge-m3 model. For the original model and official implementations, please refer to [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3).
