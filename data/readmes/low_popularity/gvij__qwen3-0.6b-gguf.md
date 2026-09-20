---
license: apache-2.0
library_name: gguf
tags:
- gguf
- llama-cpp
- cpu-inference
- qwen3
- qwen
- multilingual
- text-generation
- conversational
- tool-calling
- thinking-mode
- quantized
- neo
language:
- en
- zh
- es
- fr
- de
- ja
- ko
- ar
- ru
- pt
- it
- nl
- pl
- tr
- vi
- th
- id
- hi
- uk
- cs
- ro
- sv
- da
- fi
- no
- hu
- el
- he
- fa
pipeline_tag: text-generation
model_type: qwen2
base_model: Qwen/Qwen3-0.6B
---

# Qwen3-0.6B GGUF

This repository contains GGUF (GPT-Generated Unified Format) conversions of the [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) language model, optimized for efficient CPU inference using llama.cpp, Ollama, and other GGUF-compatible engines.

This model was converted by [NEO](https://heyneo.so) - Fully autonomous ML Engineering Agent.

## Model Overview

**Qwen3-0.6B** is a compact yet powerful 0.6 billion parameter causal language model from Alibaba's Qwen series, featuring:
- **Dual-mode inference**: Supports both thinking and non-thinking modes for flexible reasoning
- **Enhanced reasoning**: Improved logical reasoning and problem-solving capabilities
- **Multilingual support**: Proficient in 100+ languages
- **Tool calling**: Native support for function calling and agent workflows
- **Extended context**: 32,768 token context length
- **Efficient architecture**: GQA attention mechanism for optimized inference

## Architecture Details

- **Parameters**: 0.6B total (0.44B non-embedding)
- **Layers**: 28 transformer layers
- **Attention**: Grouped Query Attention (GQA)
  - 16 Query heads
  - 8 Key-Value heads
- **Context Length**: 32,768 tokens
- **Vocabulary Size**: 151,936 tokens
- **Original Precision**: BF16

## Quantization Variants

This repository provides 4 GGUF quantization variants optimized for different use cases:

| Model Variant | File Size | Quantization | Use Case | Quality |
|--------------|-----------|--------------|----------|---------|
| **qwen3-0.6b-fp16.gguf** | 1,439 MB | FP16 | Reference quality, GPU inference | Highest |
| **qwen3-0.6b-q8_0.gguf** | 767 MB | Q8_0 | High-quality CPU inference | Very High |
| **qwen3-0.6b-q5_k_m.gguf** | 526 MB | Q5_K_M | Production CPU deployment | High |
| **qwen3-0.6b-q4_k_m.gguf** | 462 MB | Q4_K_M | Edge devices, mobile, low memory | Good |

### Quantization Recommendations

- **FP16**: Use for reference benchmarks or when GPU memory is available
- **Q8_0**: Best balance for CPU inference with minimal quality loss
- **Q5_K_M**: Recommended for production CPU deployments (best quality/size ratio)
- **Q4_K_M**: Optimal for resource-constrained environments (edge, mobile, IoT)

## Usage Instructions

### llama.cpp CLI

Download a model variant and run inference:

```bash
# Download model (replace with your preferred variant)
huggingface-cli download gvij/qwen3-0.6b-gguf qwen3-0.6b-q5_k_m.gguf --local-dir ./models

# Run inference
./llama-cli -m models/qwen3-0.6b-q5_k_m.gguf -p "Explain quantum computing:" -n 256 --temp 0.7

# Interactive chat mode
./llama-cli -m models/qwen3-0.6b-q5_k_m.gguf -cnv --color
```

### Ollama Integration

Create a Modelfile:

```dockerfile
FROM ./qwen3-0.6b-q5_k_m.gguf

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER stop "<|im_end|>"
PARAMETER stop "<|endoftext|>"

TEMPLATE """
<|im_start|>system
You are a helpful AI assistant.<|im_end|>
<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""
```

Create and run the model:

```bash
ollama create qwen3-0.6b -f Modelfile
ollama run qwen3-0.6b "Write a Python function to calculate factorial"
```

### Python with llama-cpp-python

```python
from llama_cpp import Llama

llm = Llama(
    model_path="qwen3-0.6b-q5_k_m.gguf",
    n_ctx=32768,
    n_threads=8,
    n_gpu_layers=0
)

response = llm(
    "Explain the theory of relativity in simple terms:",
    max_tokens=256,
    temperature=0.7,
    top_p=0.9,
    stop=["<|im_end|>", "<|endoftext|>"]
)

print(response['choices'][0]['text'])
```

### Thinking Mode

Qwen3 supports explicit reasoning with thinking mode. Use the `<think>` tags:

```python
prompt = """Think through this problem step by step:
<think>
What is 15% of 240?
</think>"""

response = llm(prompt, max_tokens=512)
```

## Performance Characteristics

**CPU Inference Speed** (approximate, on modern x86-64 CPU):

- **Q4_K_M**: ~20-30 tokens/second
- **Q5_K_M**: ~18-25 tokens/second
- **Q8_0**: ~12-18 tokens/second
- **FP16**: ~8-12 tokens/second (CPU) / ~50-80 tokens/second (GPU)

**Memory Requirements**:

- **Q4_K_M**: ~600 MB RAM
- **Q5_K_M**: ~700 MB RAM
- **Q8_0**: ~1 GB RAM
- **FP16**: ~1.6 GB RAM

*Note: Actual performance depends on CPU architecture, clock speed, and context length.*

## Features

✅ **Thinking & Non-thinking Modes**: Dynamic reasoning control  
✅ **Multilingual**: 100+ languages supported  
✅ **Tool Calling**: Native function calling for agent workflows  
✅ **Extended Context**: 32K token context window  
✅ **CPU Optimized**: GGUF format for efficient CPU inference  
✅ **Flexible Deployment**: Compatible with llama.cpp, Ollama, LMStudio, MLX-LM

## Model Source

- **Original Model**: [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)
- **Model Family**: Qwen3 Series
- **Developer**: Alibaba Cloud
- **Conversion**: HuggingFace → GGUF using llama.cpp conversion scripts

## License

This model is released under the **Apache 2.0 License**, following the original Qwen3-0.6B license terms.

## Citation

```bibtex
@misc{qwen3-0.6b-gguf,
  title={Qwen3-0.6B GGUF},
  author={Qwen Team},
  year={2024},
  url={https://huggingface.co/gvij/qwen3-0.6b-gguf}
}
```

## Acknowledgments

- **Qwen Team** at Alibaba Cloud for the original model
- **llama.cpp** community for GGUF format and conversion tools
- Model conversion performed using llama.cpp conversion pipeline

---

For issues, questions, or feedback, please visit the original [Qwen3-0.6B repository](https://huggingface.co/Qwen/Qwen3-0.6B).

Authored and published by [NEO](https://heyneo.so)
