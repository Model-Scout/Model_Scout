---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
base_model: LiquidAI/LFM2-1.2B-Tool
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
  <a href="https://playground.liquid.ai/chat">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm"><strong>Documentation</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a></a>
</div>
</center>

# LFM2-1.2B-Tool-GGUF

Based on [LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B), LFM2-1.2B-Tool is designed for **concise and precise tool calling**. The key challenge was designing a non-thinking model that outperforms similarly sized thinking models for tool use.

**Use cases**:

- Mobile and edge devices requiring instant API calls, database queries, or system integrations without cloud dependency.
- Real-time assistants in cars, IoT devices, or customer support, where response latency is critical.
- Resource-constrained environments like embedded systems or battery-powered devices needing efficient tool execution.

You can find more information about other task-specific models in this [blog post](https://www.liquid.ai/blog/introducing-liquid-nanos-frontier-grade-performance-on-everyday-devices).

## 🏃 How to run LFM2

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

```
llama-cli -hf LiquidAI/LFM2-1.2B-Tool-GGUF
```