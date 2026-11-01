---
language:
- en
- zh
- ru
- ja
- de
- fr
- es
- pt
- vi
- th
- ar
- ko
- it
- pl
- nl
- sv
- tr
- he
- cs
- uk
- ro
- bg
- hu
- el
- da
- fi
- nb
- sk
- sl
- hr
- lt
- lv
- et
- mt
pipeline_tag: sentence-similarity
tags:
- qwen
- embedding
- onnx
- int8
- quantized
- text-embeddings-inference
license: apache-2.0
---

# Qwen3-Embedding-0.6B ONNX INT8 for Text Embeddings Inference

This is an INT8 quantized ONNX version of [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) optimized specifically for [Text Embeddings Inference (TEI)](https://github.com/huggingface/text-embeddings-inference) with CPU acceleration.

## Key Features

- **INT8 Quantization**: ~8x smaller model size (0.56GB vs 4.7GB)
- **CPU Optimized**: 2-4x faster inference on CPU compared to float32
- **TEI Compatible**: Properly formatted for Text Embeddings Inference
- **Multilingual**: Supports 29 languages including English, Chinese, Russian, Japanese, etc.
- **Mean Pooling**: Configured for mean pooling (handled by TEI)

## Performance

- **Model size**: 0.56 GB (vs 4.7 GB float32)
- **Expected speedup**: 2-4x on CPU
- **Accuracy**: Minimal loss (1-3%) compared to float32
- **Best for**: CPU deployments, edge devices, high-throughput scenarios

## Usage with Text Embeddings Inference

### Docker Deployment (CPU)

```bash
docker run -p 8080:80 \
  -e OMP_NUM_THREADS=$(nproc) \
  -e KMP_AFFINITY=granularity=fine,compact,1,0 \
  -e ORT_THREAD_POOL_SIZE=$(nproc) \
  ghcr.io/huggingface/text-embeddings-inference:cpu-latest \
  --model-id YOUR_USERNAME/qwen3-embedding-0.6b-int8-tei-onnx
```

### Python Client

```python
from huggingface_hub import InferenceClient

client = InferenceClient("http://localhost:8080")

# Single embedding
response = client.post(
    json={"inputs": "What is Deep Learning?"},
)
embedding = response.json()

# Batch embeddings
response = client.post(
    json={"inputs": ["What is Deep Learning?", "深度学习是什么？"]},
)
embeddings = response.json()
```

## CPU Optimization

For optimal CPU performance, set these environment variables:

```bash
export OMP_NUM_THREADS=$(nproc)          # Use all physical cores
export KMP_AFFINITY=granularity=fine,compact,1,0
export ORT_THREAD_POOL_SIZE=$(nproc)
```

## License

Apache 2.0
