---
base_model: tencent/HY-MT1.5-1.8B
base_model_relation: quantized
library_name: mnn
license: other
license_name: tencent-hunyuan-community
license_link: https://huggingface.co/tencent/HY-MT1.5-1.8B/blob/main/LICENSE
language:
  - multilingual
  - en
  - zh
  - ja
  - ko
  - de
  - fr
  - es
  - pt
  - ru
  - ar
tags:
  - translation
  - mnn
  - quantized
  - 4-bit
  - apple-silicon
  - edge-inference
  - ios
  - macos
  - mobile
pipeline_tag: translation
---

# HY-MT1.5-1.8B-MNN

This is a 4-bit quantized MNN version of [Tencent's HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B) translation model, optimized for Apple Silicon (iOS/macOS) edge inference.

## Model Description

HY-MT1.5-1.8B is a lightweight version of the HY-MT1.5 series, specifically designed for edge devices:

- **36 Language Support**: Extended language coverage
- **Edge Optimized**: Designed for mobile and edge deployment
- **Terminology Intervention**: Custom terminology control during translation
- **Context-Aware Translation**: Improved accuracy with context understanding
- **Industry-Leading Performance**: Best-in-class for its parameter size

## Quantization Details

| Property | Value |
|----------|-------|
| Original Model | [tencent/HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B) |
| Original Size | ~3.8 GB |
| Quantized Size | **1.07 GB** |
| Compression Ratio | 72% |
| Quantization Type | 4-bit (q4_k_m) |
| Block Size | 64 |

## Hardware Acceleration

Optimized for Apple Silicon with:
- ✅ INT8 Dot Product (i8sdot)
- ✅ FP16 Operations
- ✅ INT8 Matrix Multiply (i8mm)
- ✅ Scalable Matrix Extension 2 (sme2)
- ✅ Metal GPU Acceleration
- ✅ Apple Neural Engine (ANE) compatible

## Files

```
├── llm.mnn              # Model structure (576 KB)
├── llm.mnn.weight       # Quantized weights (1.07 GB)
├── tokenizer.txt        # Tokenizer vocabulary
├── llm_config.json      # MNN runtime config
├── config.json          # Model config
├── model_info.json      # Model metadata
└── export_args.json     # Conversion parameters
```

## Usage

### With MNN LLM Demo

```bash
# Clone MNN and build llm_demo
git clone https://github.com/alibaba/MNN.git
cd MNN && mkdir build && cd build
cmake .. -DMNN_BUILD_LLM=ON -DMNN_LOW_MEMORY=ON
make -j8 llm_demo

# Run inference
cd /path/to/HY-MT1.5-1.8B-MNN
./llm_demo ./
```

### Example

```
User: Translate into English: 今天天氣很好
A: The weather is very nice today.
```

### Prompt Templates

```
# Basic translation
Translate into {language}:
{text}

# With terminology
Translate into {language}, using terms: {terms}
{text}

# With context
Context: {context}
Translate into {language}:
{text}
```

## Performance

| Metric | Value |
|--------|-------|
| Model Load Time | ~1s |
| Inference Speed | 40-60 tokens/s |
| Target Device | iOS / Apple Silicon |
| Memory Usage | < 2GB |

## iOS Integration

This model is ideal for iOS apps. Example using MNN iOS SDK:

```swift
import MNN

let llm = LLM(modelPath: "HY-MT1.5-1.8B-MNN")
let result = llm.generate("Translate into English: 今天天氣很好")
print(result) // "The weather is very nice today."
```

## Conversion Info

- **Tool**: MNN llmexport.py
- **MNN Version**: 3.0.0
- **Conversion Date**: 2025-12-31
- **Source Format**: HuggingFace safetensors

## Related Models

- [HY-MT1.5-7B-MNN](https://huggingface.co/jazzwang/HY-MT1.5-7B-MNN) - Larger version for higher quality
- [Hunyuan-MT-7B-MNN](https://huggingface.co/jazzwang/Hunyuan-MT-7B-MNN) - Original WMT25 version

## Why Choose 1.8B?

| Feature | 1.8B | 7B |
|---------|------|-----|
| Size | 1.07 GB | 4.47 GB |
| Speed | 40-60 tok/s | 20-30 tok/s |
| iOS Compatible | ✅ Yes | ⚠️ Mac only |
| Quality | Good | Excellent |

**Choose 1.8B for**: Mobile apps, real-time translation, resource-constrained devices

**Choose 7B for**: Desktop apps, highest translation quality, batch processing

## License

This model inherits the license from the original [HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B) model.

## Acknowledgments

- [Tencent Hunyuan Team](https://huggingface.co/tencent) for the original model
- [Alibaba MNN Team](https://github.com/alibaba/MNN) for the inference framework
