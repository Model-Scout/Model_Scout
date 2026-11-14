---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
tags:
- lfm3
- omni
- custom-merge
- coder
- tool-calling
- vision
- audio
- image
- video
- gguf-coming-soon
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
- da
- el
- fi
- he
- nl
- sv
- tr
base_model:
- LiquidAI/LFM3-1.7B
- LiquidAI/LFM3-Omni-2B
---

<div align="center">
  <h1>LFM3-2.2B-Omni-Coder-Instruct</h1>
  <p><strong>A Custom Omni-Modal Coder Model by Shivansh Kokate</strong></p>
  <p>
    <a href="https://huggingface.co/Shivansh-13929/LFM3-2.2B-Omni-Coder-Instruct"><strong>Model Card</strong></a> •
    <a href="#model-details"><strong>Details</strong></a> •
    <a href="#inference"><strong>Inference</strong></a>
  </p>
</div>

## Overview

This model is a custom merge combining the **LFM3-1.7B** base with the **Vision, Audio, Image, and Video** components from **LFM3-Omni-2B**. 

**Why this model?**  
There was a distinct lack of a ~2B parameter model that possessed decent coding capabilities, tool-calling proficiency, *and* comprehensive VIA (Vision, Image, Audio) understanding. To solve this, we modified and combined these two models into a single, cohesive Safetensors file, creating a highly efficient, multi-purpose edge model.

> 🚀 **Coming Soon:** GGUF variants will be released shortly! The **Q4_K_M** quantization will be released first, followed by the rest of the quantization formats.

---

## Model Details
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

<table style="width: 100%; display: table; border: 0; border-radius: 0; border-collapse: collapse;">
<thead style="border: 0;">
<tr style="border: 0;">
<th scope="col" style="text-align: left; padding: 0.55em 0.75em; border: 0; border-bottom: 1px solid rgba(127, 127, 127, 0.55);">Property</th>
<th scope="col" style="text-align: left; padding: 0.55em 0.75em; border: 0; border-bottom: 1px solid rgba(127, 127, 127, 0.55);">Specification</th>
</tr>
</thead>
<tbody style="border: 0;">
<tr style="border: 0;">
<td style="border: 0; padding: 0.55em 0.75em;"><strong>Creator</strong></td>
<td style="border: 0; padding: 0.55em 0.75em;">Shivansh Kokate</td>
</tr>
<tr style="border: 0;">
<td style="border: 0; padding: 0.55em 0.75em;"><strong>Checkpoint</strong></td>
<td style="border: 0; padding: 0.55em 0.75em;">Custom merged omni-modal instruct model</td>
</tr>
<tr style="border: 0;">
<td style="border: 0; padding: 0.55em 0.75em;"><strong>Parameters</strong></td>
<td style="border: 0; padding: 0.55em 0.75em;">2.24B total (exactly 2,240,487,474 Parameters)</td>
</tr>
<tr style="border: 0;">
<td style="border: 0; padding: 0.55em 0.75em;"><strong>Architecture</strong></td>
<td style="border: 0; padding: 0.55em 0.75em;">LFM3-1.7B backbone + LFM3-Omni-2B Vision, Audio, Image, and Video components</td>
</tr>
<tr style="border: 0;">
<td style="border: 0; padding: 0.55em 0.75em;"><strong>Inputs</strong></td>
<td style="border: 0; padding: 0.55em 0.75em;">Text, images, video (with or without soundtrack), and 16 kHz audio</td>
</tr>
<tr style="border: 0;">
<td style="border: 0; padding: 0.55em 0.75em;"><strong>Outputs</strong></td>
<td style="border: 0; padding: 0.55em 0.75em;">Text, tool calls, and code generation</td>
</tr>
<tr style="border: 0;">
<td style="border: 0; padding: 0.55em 0.75em;"><strong>Context length</strong></td>
<td style="border: 0; padding: 0.55em 0.75em;">32K tokens (input + output)</td>
</tr>
<tr style="border: 0;">
<td style="border: 0; padding: 0.55em 0.75em;"><strong>License</strong></td>
<td style="border: 0; padding: 0.55em 0.75em;"><a href="LICENSE">LFM Open License v1.0</a> (inherited from base models)</td>
</tr>
</tbody>
</table>

---

## Target Capabilities
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

- **💻 Advanced Coding:** Fine-tuned and merged to handle complex code generation, debugging, and explanation tasks efficiently within a small parameter footprint.
- **🛠️ Tool Calling:** Robust support for structured tool use and function calling, allowing the model to interact with external APIs and systems.
- **👁️🎧 VIA Understanding:** Full multimodal comprehension. It can process and reason over images, video frames, and audio inputs simultaneously, just like the LFM3-Omni-2B base.

*(Note: Formal benchmarking specific to this custom merge is forthcoming. Base capabilities are inherited from the LFM3-1.7B and LFM3-Omni-2B models.)*

---

## Inference
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

### Transformers Quick Start

Install the dependencies, then load the model and processor. 

```bash
pip install "transformers>=4.40.0" torch torchvision accelerate pillow librosa soundfile