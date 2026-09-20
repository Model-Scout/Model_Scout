---
license: apache-2.0
base_model: mistralai/Mistral-Small-Instruct-2501
tags:
- quantized
- gguf
- mistral
- instruct
- llama.cpp
- ollama
- vision
- multimodal
- multilingual
model_type: mistral
inference: false
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
pipeline_tag: text-generation
---

<p style="margin-bottom: 0;">
    <em>See <a href="https://huggingface.co/muranAI">our collection</a> for all new Models.</em>
</p>

<div style="display: flex; gap: 5px; align-items: center; ">
    <a href="https://muranai.com/">
        <img src="https://muranai.com/images/logo_white.png" width="133">
    </a>
</div>

# Mistral-Small-3.1-24B-Instruct - GGUF

<div align="center">

**High-quality GGUF quantizations of Mistral-Small-3.1-24B-Instruct-2503**

[![](https://img.shields.io/badge/Quantization-GGUF-blue)](#quantization-variants)
[![](https://img.shields.io/badge/License-Apache%202.0-green)](#license)
[![](https://img.shields.io/badge/Base%20Model-Mistral%20Small%203.1%2024B-orange)](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
[![](https://img.shields.io/badge/Context-128k%20tokens-purple)](#model-details)

</div>

## 📖 Model Description

This repository contains **GGUF quantized versions** of the [Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) model, optimized for efficient inference using [llama.cpp](https://github.com/ggerganov/llama.cpp), [Ollama](https://ollama.com/), and other GGUF-compatible frameworks.

**Mistral Small 3.1** builds upon Mistral Small 3 (2501) and adds **state-of-the-art vision understanding** and enhances **long context capabilities up to 128k tokens** without compromising text performance. With **24 billion parameters**, this model achieves top-tier capabilities in both text and vision tasks.

### Key Features ✨
- **🖼️ Vision Capabilities**: Analyze images and provide insights based on visual content
- **🌍 Multilingual**: Supports 24+ languages including English, French, German, Spanish, Japanese, Chinese, Arabic, and more
- **🤖 Agent-Centric**: Best-in-class agentic capabilities with native function calling and JSON output
- **🧠 Advanced Reasoning**: State-of-the-art conversational and reasoning capabilities
- **📏 Long Context**: 128k token context window for processing large documents
- **⚖️ Apache 2.0 License**: Open license for commercial and non-commercial use
- **🎯 System Prompt Support**: Strong adherence to system prompts

## 🚀 Quick Start

### Using with Ollama

```bash
# Download and run the model
ollama run hf.co/your-username/mistral-small-3.1-24b-instruct-gguf:q4_k_m

# Or create from local file
ollama create mistral-small-local -f Modelfile
ollama run mistral-small-local
```

**Modelfile for Ollama:**
```dockerfile
FROM ./mistral-small-3.1-24b-instruct-q4_k_m.gguf

TEMPLATE """<s>[SYSTEM_PROMPT]{{ .System }}[/SYSTEM_PROMPT][INST]{{ .Prompt }}[/INST]"""

PARAMETER temperature 0.15
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.1
PARAMETER num_ctx 128000

SYSTEM """You are Mistral Small 3.1, a Large Language Model (LLM) created by Mistral AI, a French startup headquartered in Paris. You are knowledgeable, creative, and provide detailed responses while being concise when appropriate. You have vision capabilities and can analyze images when provided."""
```

### Using with llama.cpp

```bash
# Download the model
huggingface-cli download your-username/mistral-small-3.1-24b-instruct-gguf mistral-small-3.1-24b-instruct-q4_k_m.gguf --local-dir ./models

# Run inference
./llama-cli -m ./models/mistral-small-3.1-24b-instruct-q4_k_m.gguf -p "<s>[SYSTEM_PROMPT]You are a helpful AI assistant.[/SYSTEM_PROMPT][INST]Hello! How are you?[/INST]" -n 256 -c 128000
```

### Using with Python (llama-cpp-python)

```python
from llama_cpp import Llama

# Load the model
llm = Llama(
    model_path="./mistral-small-3.1-24b-instruct-q4_k_m.gguf",
    n_ctx=128000,  # Full 128k context window
    n_threads=8,   # Number of CPU threads
    n_gpu_layers=35,  # Number of layers to offload to GPU (if available)
    verbose=False
)

# Generate response with proper template
prompt = "<s>[SYSTEM_PROMPT]You are a helpful AI assistant.[/SYSTEM_PROMPT][INST]Explain quantum computing in simple terms[/INST]"

response = llm(
    prompt,
    max_tokens=512,
    temperature=0.15,
    top_p=0.9,
)

print(response["choices"][0]["text"])
```

## 📊 Quantization Variants

| Variant | File Size | Description | Use Case | Quality Loss |
|---------|-----------|-------------|----------|--------------|
| **F16** | 44.0 GB | Original precision | Maximum quality, research | None |
| **Q8_0** | 23.3 GB | 8-bit quantization | High-end inference | Minimal |
| **Q6_K** | 18.0 GB | 6-bit K-quantization | Production quality | Very Low |
| **Q5_K_M** | 15.6 GB | 5-bit K-quant (medium) | **Recommended balance** | Low |
| **Q5_K_S** | 15.2 GB | 5-bit K-quant (small) | Balanced quality/size | Low |
| **Q5_1** | 16.5 GB | 5-bit legacy | Legacy compatibility | Low |
| **Q5_0** | 15.2 GB | 5-bit legacy | Legacy compatibility | Low |
| **Q4_K_M** | 13.4 GB | 4-bit K-quant (medium) | **Popular choice** | Moderate |
| **Q4_K_S** | 12.5 GB | 4-bit K-quant (small) | Resource constrained | Moderate |
| **Q4_1** | 13.9 GB | 4-bit legacy | Legacy compatibility | Moderate |
| **Q4_0** | 12.5 GB | 4-bit legacy | Legacy compatibility | Moderate |
| **Q3_K_L** | 11.5 GB | 3-bit K-quant (large) | Limited resources | Noticeable |
| **Q3_K_M** | 10.8 GB | 3-bit K-quant (medium) | Limited resources | Noticeable |
| **Q3_K_S** | 9.7 GB | 3-bit K-quant (small) | Very limited resources | Noticeable |
| **Q2_K** | 8.3 GB | 2-bit K-quantization | Extreme compression | Significant |

### 🎯 Recommended Variants

- **Q5_K_M** (15.6 GB): Best balance of quality and size for most users
- **Q4_K_M** (13.4 GB): Good quality with smaller size, popular choice  
- **Q6_K** (18.0 GB): Near-original quality if you have the resources
- **Q3_K_M** (10.8 GB): Minimum viable quality for resource-constrained environments

## 🛠️ Model Details

### Architecture
- **Model Type**: Mistral Small 3.1
- **Parameters**: 24 billion
- **Context Length**: 128,000 tokens (128k)
- **Vocabulary Size**: 131,000 (Tekken tokenizer)
- **Architecture**: Transformer with sliding window attention
- **Precision**: Various GGUF quantizations
- **Base Model**: [Mistral-Small-3.1-24B-Base-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Base-2503)

### Capabilities
- **🖼️ Vision Understanding**: State-of-the-art multimodal capabilities for image analysis
- **📝 Instruction Following**: Excellent at following complex instructions
- **💻 Code Generation**: Strong programming capabilities across multiple languages
- **🧮 Mathematical Reasoning**: Advanced math and logical reasoning (69.30% on MATH benchmark)
- **🌍 Multilingual**: Native support for 24+ languages
- **💬 Conversation**: Natural dialogue and chat capabilities
- **🔧 Function Calling**: Native tool calling and JSON output capabilities
- **📚 Long Context**: Process documents up to 128k tokens

### Benchmark Performance

#### Text Benchmarks
- **MMLU**: 80.62% (general knowledge)
- **MATH**: 69.30% (mathematical reasoning) 
- **HumanEval**: 88.41% (code generation)
- **GPQA**: 44.42% (graduate-level questions)

#### Vision Benchmarks  
- **MMMU**: 64.00% (multimodal understanding)
- **ChartQA**: 86.24% (chart analysis)
- **DocVQA**: 94.08% (document visual Q&A)
- **AI2D**: 93.72% (scientific diagrams)

#### Long Context
- **RULER 32K**: 93.96%
- **RULER 128K**: 81.20%
- **LongBench v2**: 37.18%

## 💬 Chat Template

This model uses the **Mistral V7-Tekken instruction format**:

```
<s>[SYSTEM_PROMPT]<system prompt>[/SYSTEM_PROMPT][INST]<user message>[/INST]<assistant response></s>[INST]<user message>[/INST]
```

**Examples:**

**Basic Chat:**
```
<s>[SYSTEM_PROMPT]You are a helpful AI assistant.[/SYSTEM_PROMPT][INST]Write a Python function to calculate the factorial of a number[/INST]
```

**With Vision:**
```
<s>[SYSTEM_PROMPT]You are a helpful AI assistant with vision capabilities.[/SYSTEM_PROMPT][INST]What do you see in this image? <image>[/INST]
```

## 🔧 Technical Requirements

### Minimum System Requirements
| Variant | RAM | VRAM (GPU) | Storage |
|---------|-----|------------|---------|
| Q2_K | 16 GB | 8 GB | 10 GB |
| Q3_K_M | 24 GB | 12 GB | 12 GB |
| Q4_K_M | 32 GB | 16 GB | 15 GB |
| Q5_K_M | 48 GB | 18 GB | 17 GB |
| Q6_K+ | 64 GB | 20+ GB | 20+ GB |

### Recommended Hardware
- **CPU**: Modern multi-core processor (12+ cores recommended for 128k context)
- **RAM**: 64+ GB for optimal performance with long contexts
- **GPU**: RTX 3090/4090 (24GB), RTX 6000 Ada (48GB), or A100 for GPU acceleration
- **Storage**: NVMe SSD for faster model loading

**Note**: The original model requires ~55GB GPU RAM in bf16/fp16. Quantized versions significantly reduce memory requirements.

## 📥 Download Instructions

### Individual Files
```bash
# Download specific quantization
huggingface-cli download your-username/mistral-small-3.1-24b-instruct-gguf mistral-small-3.1-24b-instruct-q4_k_m.gguf --local-dir ./models

# Download all files (warning: ~200GB total)
huggingface-cli download your-username/mistral-small-3.1-24b-instruct-gguf --local-dir ./models
```

### Git LFS
```bash
git clone https://huggingface.co/your-username/mistral-small-3.1-24b-instruct-gguf
cd mistral-small-3.1-24b-instruct-gguf
git lfs pull
```

## 🧪 Usage Examples

### Code Generation
```
<s>[SYSTEM_PROMPT]You are an expert programmer.[/SYSTEM_PROMPT][INST]Create a REST API using FastAPI for a todo application with CRUD operations[/INST]
```

### Creative Writing
```
<s>[SYSTEM_PROMPT]You are a creative writing assistant.[/SYSTEM_PROMPT][INST]Write a short story about a time traveler who accidentally changes a small detail in the past[/INST]
```

### Data Analysis Help
```
<s>[SYSTEM_PROMPT]You are a data science expert.[/SYSTEM_PROMPT][INST]I have a dataset with missing values. Explain different strategies to handle them and provide Python code examples[/INST]
```

### Multilingual Support
```
<s>[SYSTEM_PROMPT]Tu es un assistant multilingue.[/SYSTEM_PROMPT][INST]Explique-moi la différence entre l'apprentissage supervisé et non supervisé[/INST]
```

### Function Calling
```python
# The model supports native function calling for tool use
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"}
                }
            }
        }
    }
]
```

## 🏆 Ideal Use Cases

- **💬 Fast-response conversational agents**
- **⚡ Low-latency function calling**
- **🎓 Subject matter experts via fine-tuning**
- **🏠 Local inference for privacy-sensitive applications**
- **💻 Programming and mathematical reasoning**
- **📄 Long document understanding and analysis**
- **🖼️ Visual content analysis and description**
- **🌍 Multilingual applications**

## ⚠️ Limitations

- **Quantization Loss**: Lower bit quantizations (Q2, Q3) may show reduced quality, especially for complex reasoning
- **Context Limit**: Maximum context length of 128,000 tokens
- **Knowledge Cutoff**: Training data cutoff as of October 2023
- **Hallucination**: May generate plausible but incorrect information
- **Bias**: May reflect biases present in training data
- **Vision**: Text-only quantizations don't preserve vision capabilities optimally

## 🛡️ Ethical Considerations

- Use responsibly and in accordance with Mistral AI's usage policies
- Be aware of potential biases in model outputs
- Verify important information from model responses
- Consider privacy implications when processing sensitive data
- Follow applicable laws and regulations in your jurisdiction
- Respect copyright when analyzing images or documents

## 📄 License

This model is released under the **Apache 2.0 License**, same as the original Mistral-Small-3.1-24B-Instruct-2503 model.

## 🙏 Acknowledgments

- **Mistral AI** for the original Mistral-Small-3.1-24B-Instruct-2503 model
- **Georgi Gerganov** and the llama.cpp team for GGUF format and quantization tools
- **The open-source community** for continued development of efficient inference tools

## 📞 Support

- **Issues**: Report issues with these GGUF files in this repository
- **Original Model**: For questions about the base model, refer to [Mistral AI's repository](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- **llama.cpp**: For technical issues with inference, check the [llama.cpp repository](https://github.com/ggerganov/llama.cpp)
- **Ollama**: For Ollama-specific issues, see [Ollama documentation](https://ollama.com/)

---

<div align="center">

**Made with ❤️ by the open-source community**

[🤗 Hugging Face](https://huggingface.co/) • [🦙 llama.cpp](https://github.com/ggerganov/llama.cpp) • [🧠 Mistral AI](https://mistral.ai/) • [📱 Ollama](https://ollama.com/)

</div> 