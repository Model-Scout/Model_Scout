---
license: mit
language:
  - multilingual
  - en
  - ja
  - zh
  - ko
  - de
  - fr
  - es
  - it
  - pt
  - ru
library_name: coreml
tags:
  - sentence-transformers
  - embeddings
  - coreml
  - ios
  - macos
  - multilingual
  - e5
  - semantic-search
base_model: intfloat/multilingual-e5-small
pipeline_tag: sentence-similarity
---

# Multilingual E5 Small - CoreML

This is a CoreML conversion of [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) for iOS/macOS deployment.

## Model Description

Multilingual E5 Small is a multilingual sentence embedding model optimized for semantic search and retrieval tasks. This CoreML version enables on-device inference on Apple platforms.

### Key Features

- **Multilingual**: Supports 100+ languages including English, Japanese, Chinese, Korean, German, French, Spanish, and more
- **Search-optimized**: Designed specifically for retrieval tasks
- **Cross-lingual**: Can match queries in one language to documents in another
- **On-device**: Runs locally on iPhone/iPad/Mac without internet

## Model Details

| Property | Value |
|----------|-------|
| Base Model | intfloat/multilingual-e5-small |
| Embedding Dimensions | 384 |
| Max Sequence Length | 256 (configurable up to 512) |
| Model Size | ~224 MB |
| Precision | Float16 |
| Minimum iOS | 17.0 |
| Minimum macOS | 14.0 |

## Usage

### Input Format

E5 models use prefixes to distinguish between queries and documents:

- **Query**: `"query: your search query here"`
- **Document**: `"passage: your document text here"`

### Swift Example

```swift
import CoreML

// Load model
let config = MLModelConfiguration()
config.computeUnits = .cpuAndNeuralEngine
let model = try MLModel(contentsOf: modelURL, configuration: config)

// Prepare inputs (after tokenization)
let inputIds: MLMultiArray = // tokenized input
let attentionMask: MLMultiArray = // attention mask

// Run inference
let input = try MLDictionaryFeatureProvider(dictionary: [
    "input_ids": MLFeatureValue(multiArray: inputIds),
    "attention_mask": MLFeatureValue(multiArray: attentionMask)
])
let output = try model.prediction(from: input)
let embeddings = output.featureValue(for: "embeddings")?.multiArrayValue
```

### Tokenizer

Use the included `tokenizer.json` with [swift-transformers](https://github.com/huggingface/swift-transformers):

```swift
import Tokenizers

let tokenizer = try await AutoTokenizer.from(modelFolder: tokenizerURL)
let encoded = tokenizer.encode(text: "query: your text")
```

## Performance

Tested on iOS with Neural Engine:

| Device | Inference Time |
|--------|----------------|
| iPhone 15 Pro | ~15ms |
| iPhone 13 | ~25ms |
| M1 Mac | ~10ms |

## Accuracy Comparison

Tested with 10 mixed Japanese/English technical queries:

| Model | Accuracy | Avg Score |
|-------|----------|-----------|
| Apple NLEmbedding | 20% | 0.558 |
| **This Model (E5)** | **100%** | **0.860** |

## Files

- `MultilingualE5Small.mlpackage/` - CoreML model package
- `tokenizer.json` - Tokenizer vocabulary and configuration
- `tokenizer_config.json` - Tokenizer settings

## Conversion

Converted using coremltools with FP16 precision:

```python
import coremltools as ct

mlmodel = ct.convert(
    traced_model,
    inputs=[
        ct.TensorType(name="input_ids", shape=(1, 256), dtype=np.int32),
        ct.TensorType(name="attention_mask", shape=(1, 256), dtype=np.int32),
    ],
    outputs=[
        ct.TensorType(name="embeddings", dtype=np.float16),
    ],
    convert_to="mlprogram",
    minimum_deployment_target=ct.target.iOS17,
    compute_precision=ct.precision.FLOAT16,
)
```

## License

MIT License (same as the base model)

## Citation

```bibtex
@article{wang2024multilingual,
  title={Multilingual E5 Text Embeddings: A Technical Report},
  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Yang, Linjun and Majumder, Rangan and Wei, Furu},
  journal={arXiv preprint arXiv:2402.05672},
  year={2024}
}
```

## Acknowledgments

- Original model by [intfloat](https://huggingface.co/intfloat)
- CoreML conversion for [ReadMD](https://github.com/user/readmd) iOS app
