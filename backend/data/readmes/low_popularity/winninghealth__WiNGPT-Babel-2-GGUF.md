---
license: apache-2.0
language:
- ar
- bg
- bn
- ca
- cs
- da
- de
- el
- es
- et
- fa
- fi
- fil
- fr
- gu
- he
- hi
- hr
- hu
- id
- is
- it
- ja
- kn
- ko
- lt
- lv
- ml
- mr
- nl
- 'no'
- pa
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
- zu
base_model:
- winninghealth/WiNGPT-Babel-2
tags:
- GGUF
- multilingual
datasets:
- google/wmt24pp
pipeline_tag: translation
library_name: transformers
---

# WiNGPT-Babel-2: A Multilingual Translation Language Model

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-WiNGPT--Babel-blue)](https://huggingface.co/collections/winninghealth/wingpt-babel-68463d4b2a28d0d675ff3be9)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)

> This is the quantization version (llama.cpp) of [WiNGPT-Babel-2](https://huggingface.co/winninghealth/WiNGPT-Babel-2).
>
> Example
>
> ```shell
> ./llama-server -m WiNGPT-Babel-2-GGUF/WiNGPT-Babel-2-IQ4_XS.gguf --jinja --chat-template-file WiNGPT-Babel-2-GGUF/WiNGPT-Babel-2.jinja
> ```
>
> - **--jinja**: This flag activates the Jinja2 chat template processor.
> - **--chat-template-file**: This flag points the server to the required template file that defines the WiNGPT-Babel-2's custom prompt format.

WiNGPT-Babel-2 is a language model optimized for multilingual translation tasks. As an iteration of WiNGPT-Babel, it features significant improvements in language coverage, data format handling, and translation accuracy for complex content.

The model continues the "Human-in-the-loop" training strategy, iteratively optimizing through the analysis of log data from real-world application scenarios to ensure its effectiveness and reliability in practical use.

## Core Improvements in Version 2.0

WiNGPT-Babel-2 introduces the following key technical upgrades over its predecessor:

1.  **Expanded Language Support:** Through training with the `wmt24pp` dataset, language support has been extended to **55 languages**, primarily enhancing translation capabilities from English (en) to other target languages (xx).

2.  **Enhanced Chinese Translation:** The translation pipeline from other source languages to Chinese (xx → zh) has been specifically optimized, improving the accuracy and fluency of the results.

3.  **Structured Data Translation:** The model can now identify and translate text fields embedded within **structured data (e.g., JSON)** while preserving the original data structure. This feature is suitable for scenarios such as API internationalization and multilingual dataset preprocessing.

4.  **Mixed-Content Handling:** Its ability to handle mixed-content text has been improved, enabling more accurate translation of paragraphs containing **mathematical expressions (LaTeX), code snippets, and web markup (HTML/Markdown)**, while preserving the format and integrity of these non-translatable elements.

## Training Methodology

The performance improvements in WiNGPT-Babel-2 are attributed to a continuous, data-driven, iterative training process:

1.  **Data Collection:** Collecting anonymous, real-world translation task logs from integrated applications (e.g., Immersive Translate, Videolingo).
2.  **Data Refinement:** Using a reward model for rejection sampling on the collected data, supplemented by manual review, to filter high-quality, high-value samples for constructing new training datasets.
3.  **Iterative Retraining:** Using the refined data for the model's incremental training, continuously improving its performance in specific domains and scenarios through a cyclical iterative process.

## Technical Specifications

*   **Base Model:** [GemmaX2-28-2B-Pretrain](https://huggingface.co/ModelSpace/GemmaX2-28-2B-Pretrain)
*   **Primary Training Data:** "Human-in-the-loop" in-house dataset, [WMT24++](https://huggingface.co/datasets/google/wmt24pp) dataset
*   **Maximum Context Length:** 4096 tokens
*   **Chat Capability:** Supports multi-turn dialogue, allowing for contextual follow-up and translation refinement.

## Language Support

| Direction               | Description                                          | Supported Languages (Partial List)                           |
| :---------------------- | :--------------------------------------------------- | :----------------------------------------------------------- |
| **Core Support**        | Highest quality, extensively optimized.              | `en ↔ zh`                                                    |
| **Expanded Support**    | Supported via `wmt24pp` dataset training.            | `en → 55+ languages`, including: `fr`, `de`, `es`, `ru`, `ar`, `pt`, `ko`, `it`, `nl`, `tr`, `pl`, `sv`... |
| **Enhanced to Chinese** | Specifically optimized for translation into Chinese. | `xx → zh`                                                    |

## Performance
<table>
<thead>
<tr>
<th rowspan="2" align="center">Model</th>
<th colspan="2" align="center">FLORES-200</th>
</tr>
<tr>
<th align="center">xx → en</th>
<th align="center">xx → zh</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">WiNGPT-Babel-AWQ</td>
<td align="center">33.91</td>
<td align="center">17.29</td>
</tr>
<tr>
<td align="center">WiNGPT-Babel-2-AWQ</td>
<td align="center">36.43</td>
<td align="center">30.74</td>
</tr>
</tbody>
</table>

**Note**:
1. The evaluation metric is spBLEU, using the FLORES-200 tokenizer.

3. 'xx' represents the 52 source languages from the wmt24pp dataset.

## Usage Guide

For optimal inference performance, it is recommended to use frameworks such as `vllm`. The following provides a basic usage example using the Hugging Face `transformers` library.

**System Prompt:** For optimal automatic language inference, it is recommended to use the unified system prompt: `Translate this to {{to}} Language`. Replace `{{to}}` with the name of the target language. For instance, use `Translate this to Simplified Chinese Language` to translate into Chinese, or `Translate this to English Language` to translate into English. This method provides precise control over the translation direction and yields the most reliable results.

### Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "winninghealth/WiNGPT-Babel-2-AWQ"

model = AutoModelForCausalLM.from_pretrained(
   model_name,
   torch_dtype="auto",
   device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Example: Translation of text within a JSON object to Chinese
prompt_json = """{
  "product_name": "High-Performance Laptop",
  "features": ["Fast Processor", "Long Battery Life", "Lightweight Design"]
}"""

messages = [
   {"role": "system", "content": "Translate this to Simplified Chinese Language"}, 
   {"role": "user", "content": prompt_json} # Replace with the desired prompt
]

text = tokenizer.apply_chat_template(
   messages,
   tokenize=False,
   add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
   **model_inputs,
   max_new_tokens=4096,
   temperature=0
)

generated_ids = [
   output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

For additional usage demos, you can refer to the original [WiNGPT-Babel](https://huggingface.co/winninghealth/WiNGPT-Babel#%F0%9F%8E%AC-%E7%A4%BA%E4%BE%8B).

## LICENSE

  1. This project's license agreement is the Apache License 2.0

  2. Please cite this project when using its model weights: https://huggingface.co/winninghealth/WiNGPT-Babel-2

  3. Comply with [gemma-2-2b](https://huggingface.co/google/gemma-2-2b), [GemmaX2-28-2B-v0.1](https://huggingface.co/ModelSpace/GemmaX2-28-2B-v0.1), [immersive-translate](https://github.com/immersive-translate/immersive-translate), [VideoLingo](https://github.com/immersive-translate/immersive-translate) protocols and licenses, details on their website.


## Contact Us

  - Apply for a token through the WiNGPT platform
  - Or contact us at wair@winning.com.cn to request a free trial API_KEY