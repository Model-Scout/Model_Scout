---
license: apache-2.0
language:
- en
- es
- fr
- de
- it
- pt
- zh
- ja
- ko
- ru
- multilingual
library_name: transformers
pipeline_tag: text-generation
tags:
- general-purpose
- reasoning
- web-search
- tool-use
- conversational
- sparse-activation
- mixture-of-experts
- instruction-following
model-index:
- name: Kirim-V2
  results: []
datasets: []
metrics: []
widget:
- text: "Explain the concept of neural networks in simple terms."
  example_title: "Simple Explanation"
- text: "Write a Python function to calculate fibonacci numbers."
  example_title: "Code Generation"
- text: "What are the latest developments in renewable energy?"
  example_title: "Web Search Query"
---

# Kirim-V2 26B

<div align="center">

  <img src="https://imgur.com/n5uQJXF.png" alt="Helion-V2-Thinking Logo" width="70%"/>

</div>

---

Kirim-V2 is an advanced general-purpose language model with 26 billion parameters, featuring an innovative sparse activation architecture where 18 billion parameters are actively engaged during inference. This design delivers high performance while maintaining computational efficiency.

## Model Architecture

- **Total Parameters**: 26B
- **Active Parameters**: ~18B (sparse activation)
- **Context Length**: Extended context window
- **Architecture**: Transformer-based with mixture-of-experts components

## Key Capabilities

**Core Competencies**
- Natural language understanding and generation across multiple domains
- Complex reasoning and multi-step problem solving
- Code generation and technical documentation
- Creative writing and content creation

**Advanced Features**
- **Web Search Integration**: Built-in capability to search and retrieve real-time information
- **Tool Use**: Seamless integration with external tools and APIs
- **Multilingual Support**: Strong performance across multiple languages
- **Long-form Generation**: Coherent output for extended documents and articles

## Performance Highlights

Kirim-V2 represents a significant advancement over Kirim-V1, featuring:
- Enhanced reasoning capabilities for complex tasks
- Improved factual accuracy through integrated search
- Better instruction following and task completion
- More natural and contextually appropriate responses

## Use Cases

- **Research & Analysis**: Information gathering with real-time web search
- **Software Development**: Code generation, debugging, and documentation
- **Content Creation**: Articles, reports, creative writing, and technical documentation
- **Question Answering**: Accurate responses with source verification
- **Task Automation**: Multi-step workflows with tool integration

## Model Specifications

```
Architecture: Sparse Transformer
Training Data: Diverse web corpus, code, and specialized datasets
Tokenizer: Custom trained tokenizer optimized for multilingual performance
Optimization: Mixed precision training with gradient checkpointing
```

## Inference Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Kirim-ai/Kirim-V2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype="auto"
)

prompt = "Explain quantum entanglement in simple terms."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## Limitations

- May occasionally generate plausible-sounding but incorrect information
- Performance depends on prompt quality and task complexity
- Web search capability requires appropriate API configuration
- Not specifically fine-tuned for safety-critical applications

## Ethical Considerations

This model should be used responsibly. Users should verify critical information independently and be aware of potential biases in generated content. The model is not intended for making decisions in high-stakes scenarios without human oversight.

## License

This model is released under the Apache 2.0 License.

## Citation

```bibtex
@model{kirimv2_2025,
  title={Kirim-V2: A 26B Parameter Sparse Activation Language Model},
  author={Qiling Tech},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/Kirim-ai/Kirim-V2}
}
```

---

**Release Date**: 2026 
**Model Type**: Causal Language Model