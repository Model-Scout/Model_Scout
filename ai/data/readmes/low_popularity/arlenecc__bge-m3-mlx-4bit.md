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
- 4bit
- quantized
library_name: mlx
base_model: BAAI/bge-m3
---

# BGE-M3 MLX (4-bit Quantized)

This is the [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) model converted to MLX format with 4-bit quantization for Apple Silicon.

## Model Description

BGE-M3 is a versatile embedding model capable of:
- Dense retrieval
- Sparse retrieval
- Multi-vector (ColBERT) retrieval

This 4-bit quantized version offers the smallest footprint while maintaining reasonable quality.

## Model Details

| Property | Value |
|----------|-------|
| Architecture | XLM-RoBERTa |
| Precision | 4-bit (affine quantization) |
| Embedding Dimension | 1024 |
| Max Sequence Length | 8192 |
| Model Size | ~321 MB |
| Quantization Group Size | 64 |
| Languages | 100+ languages |

## Size Comparison

| Version | Size | Compression |
|---------|------|-------------|
| FP16 | 1.1 GB | - |
| 8-bit | 592 MB | 46% |
| 6-bit | 457 MB | 58% |
| **4-bit** | **321 MB** | **71%** |

## Usage

### With MLX

```python
from mlx_embeddings.utils import load_model, load_tokenizer
import mlx.core as mx

model_path = "mlx-community/bge-m3-mlx-4bit"

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
  -d '{"model": "bge-m3-mlx-4bit", "input": "Your text here"}'
```

## Quantization Details

- **Method**: Affine quantization
- **Bits per weight**: 4
- **Group size**: 64
- **Source**: Converted from MLX FP16 version

## Performance

Tested on macOS with Apple Silicon:
- Successfully generates 1024-dimensional embeddings
- Supports multilingual text
- Lowest memory footprint among all variants

## Recommended Use Cases

- Memory-constrained environments
- High-throughput embedding generation
- Applications where some quality loss is acceptable for reduced memory

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
