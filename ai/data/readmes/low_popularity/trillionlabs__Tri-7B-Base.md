---
license: apache-2.0
tags:
- pretrained
- base-model
language:
- en
- ko
- ja
pipeline_tag: text-generation
library_name: transformers
extra_gated_fields:
  Full Name: text
  Email: text
  Organization: text
---

<p align="center">
<picture>
  <img src="https://raw.githubusercontent.com/trillion-labs/.github/main/Tri-7B.png" alt="Tri-7B-Base", style="width: 80%;">
</picture>
</p>

# Tri-7B-Base

## Introduction

We present **Tri-7B-Base**, a foundation language model that serves as the pre-trained base for our Tri-7B model family. This model represents our commitment to efficient training while establishing a strong foundation for downstream fine-tuning and adaptation.

### Key Features
* **Foundation Architecture**: State-of-the-art transformer architecture optimized for efficiency
* **Multi-lingual Foundation**: Pre-trained on diverse data in Korean, English, and Japanese
* **Efficient Training**: Optimized training methodology for computational efficiency

### Model Specifications

#### Tri-7B-Base
- Type: Causal Language Model
- Training Stage: Pre-training
- Architecture: Transformer Decoder with RoPE, SwiGLU, RMSNorm
- Number of Parameters: 7.76B
- Number of Layers: 32
- Number of Attention Heads: 32
- Context Length: 4,096
- Vocab Size: 128,128

## Use Cases

As a base model, Tri-7B-Base is designed to serve as a foundation for various downstream applications:

- **Fine-tuning**: Adapt to specific domains or tasks
- **Instruction Tuning**: Create chat or assistant models
- **Domain Specialization**: Customize for specific industries or use cases
- **Research**: Explore model behaviors and capabilities
- **Language Generation**: General text completion and generation tasks

## Limitations

- **Base Model Nature**: This is a pre-trained base model without instruction tuning or alignment. For chat or assistant capabilities, consider fine-tuned variants.
- **Language Support**: The model is optimized for English, Korean, and Japanese. Usage with other languages may result in degraded performance.
- **Knowledge Cutoff**: The model's information is limited to data available up to February, 2025.
- **Generation Quality**: As a base model, outputs may require post-processing or filtering for production use cases.

## License
This model is licensed under the Apache License 2.0.

## Contact
For inquiries, please contact: info@trillionlabs.co