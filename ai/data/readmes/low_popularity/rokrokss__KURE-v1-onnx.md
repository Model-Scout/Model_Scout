---
license: mit
base_model:
- nlpai-lab/KURE-v1
library_name: transformers.js
pipeline_tag: feature-extraction
language:
- ko
- en
tags:
- onnx
- feature-extraction
- sentence-similarity
- korean
---

# KURE-v1 (ONNX, int8)

An ONNX export of [nlpai-lab/KURE-v1](https://huggingface.co/nlpai-lab/KURE-v1) (revision `8b418a58`),
quantized for CPU inference with [transformers.js](https://github.com/huggingface/transformers.js) and
onnxruntime. It is the embedding model [shizue-plot](https://github.com/rokrokss/shizue-plot) uses for
its chat memory.

All credit for the model belongs to its authors, the NLP & AI Lab at Korea University; this repository
only converts it. It is distributed under the same MIT license as the original.

## How it was made

- Exported with optimum's `feature-extraction` task (`last_hidden_state`).
- Quantized with onnxruntime dynamic int8, per channel, keeping the FFN output projections of the last
  12 layers in fp32 (721 MB; `onnx/model_quantized.onnx`, sha256
  `3530a7640919b643a1cdf07894dbb2481a4edaf5acd0e439b8b860026f87b494`).
- Pooling is the original's: the CLS token, then L2 normalization (`1_Pooling` + `Normalize` in the
  sentence-transformers model). Mean pooling gives much worse vectors.

Cosine similarity to the original sentence-transformers model on the same sentences: Korean (22) min 0.9909,
mean 0.9928; English (11) min 0.9922, mean 0.9941.

## Usage (transformers.js)

```js
import { pipeline } from '@huggingface/transformers';

const embed = await pipeline('feature-extraction', '<this repository>', { dtype: 'q8' });
const output = await embed(['눈이 내리는 밤', 'A snowy night'], { pooling: 'cls', normalize: true });
```

## License and citation

MIT, as [nlpai-lab/KURE-v1](https://huggingface.co/nlpai-lab/KURE-v1). If you use the model, please cite
its authors:

```text
@inproceedings{jang2025kure,
  title={KURE: Embedding Model for Korean-Specific Retrieval},
  author={Jang, Youngjoon and Son, Junyoung and Lee, Taemin and Hong, Seongtae and Park, JeongBae and Lim, Heuiseok},
  booktitle={Annual Conference on Human and Language Technology},
  pages={129--134},
  year={2025},
  organization={Human and Language Technology}
}
```
