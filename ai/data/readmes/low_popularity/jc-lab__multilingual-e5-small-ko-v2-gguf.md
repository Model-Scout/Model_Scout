---
license: apache-2.0
library_name: llama.cpp
pipeline_tag: feature-extraction
tags:
- gguf
- llama.cpp
- embedding
- sentence-transformers
- korean
- multilingual
base_model:
- dragonkue/multilingual-e5-small-ko-v2
language:
- ko
- en
---

# multilingual-e5-small-ko-v2 GGUF

GGUF quantizations for [`dragonkue/multilingual-e5-small-ko-v2`](https://huggingface.co/dragonkue/multilingual-e5-small-ko-v2).

Files:

- `ggml-model-f16.gguf`
- `ggml-model-q8_0.gguf`
- `ggml-model-q4_k_m.gguf`

## Verification

The original `SentenceTransformer` embeddings were compared against normalized embeddings produced by the GGUF models on 7 mixed Korean/English samples.

Summary:

| Model | Min cosine to original | Mean cosine to original | Max abs cosine-matrix diff |
|---|---:|---:|---:|
| `FP16` | `0.997235` | `0.998290` | `0.012590` |
| `Q8_0` | `0.996689` | `0.997856` | `0.014441` |
| `Q4_K_M` | `0.990426` | `0.992091` | `0.022216` |

The full verification output is included in [`verification_report.json`](./verification_report.json).

## Notes

- For `Q4_K_M`, some tensors fall back to other quantization types because several tensor widths are not divisible by the block-size requirements of `Q4_K`. The file is still the standard mixed `Q4_K_M` output produced by `llama-quantize`.

## llama.cpp

```bash
./build/bin/llama-embedding \
  -m ggml-model-q8_0.gguf \
  -p "query: 서울에서 맛있는 냉면집 추천해줘"
```

## llama-cpp-python

```python
import numpy as np
import llama_cpp
from llama_cpp import Llama

llm = Llama(
    model_path="ggml-model-q8_0.gguf",
    embedding=True,
    pooling_type=llama_cpp.LLAMA_POOLING_TYPE_MEAN,
    n_ctx=512,
    verbose=False,
)

text = "query: 서울에서 맛있는 냉면집 추천해줘"
vec = np.array(llm.create_embedding(text)["data"][0]["embedding"], dtype=np.float32)
vec = vec / np.linalg.norm(vec)
print(vec.shape)
```

Use the `query: ` / `passage: ` prefixes exactly as in the original E5 model.
