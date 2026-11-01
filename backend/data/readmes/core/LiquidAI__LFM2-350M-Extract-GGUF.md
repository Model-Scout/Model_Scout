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
base_model: LiquidAI/LFM2-350M-Extract
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
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
</div>
</center>

<br>

# LFM2-350M-Extract-GGUF

Based on [LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M), LFM2-350M-Extract is designed to **extract important information from a wide variety of unstructured documents** (such as articles, transcripts, or reports) into structured outputs like JSON, XML, or YAML.

**Use cases**:

- Extracting invoice details from emails into structured JSON.
- Converting regulatory filings into XML for compliance systems.
- Transforming customer support tickets into YAML for analytics pipelines.
- Populating knowledge graphs with entities and attributes from unstructured reports.

You can find more information about other task-specific models in this [blog post](https://www.liquid.ai/blog/introducing-liquid-nanos-frontier-grade-performance-on-everyday-devices).

## 🏃 How to run LFM2

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

```
llama-cli -hf LiquidAI/LFM2-350M-Extract-GGUF
```