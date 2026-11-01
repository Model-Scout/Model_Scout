---
license: apache-2.0
datasets:
- mistralai/MM-MT-Bench
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
base_model:
- mistralai/Ministral-3-8B-Instruct-2512-BF16
new_version: EnlistedGhost/Ministral-3-8B-Instruct-2512-GGUF
pipeline_tag: image-text-to-text
tags:
- MistralAI
- Ministral
- Ministral-3
- Ollama
- Llama.cpp
- GGUF
- Image-Text-to-Text
- Conversational
- Quantize
- Multimodal
- Mistral3
---

<img src="https://ollama.com/assets/library/mistral-nemo/72045292-694a-4867-88c8-8635c9d97030" alt="Example image" width="168" height="128"> 


<img src="https://ollama.com/assets/library/ministral-3/83fa3859-d87f-492c-bd81-596cfbceeccb" alt="Example image" width="64" height="64">


# -----------------------------------------------<br /> - Update September 5th 2026 -<br />-----------------------------------------------

**Happy September to everyone!<br />
Thank you for trying out and/or evaluating this release of MistralAI's Ministral-3-8B-Instruct GGUF Converted Model!**

***What's new?***
- New chat template! Yes, a new chat template that completely fixes any previous issues for llama.cpp users <br />and retains higher performance than the originally made template for Ollama/Yollama users!
- Fixed both F16 and F32 MMPROJ Multi-Modal Vision projectors. (Re-Uploaded with working projectors)
- Uploaded custom, high-quality, **new "GH05T" edition Quant files** for this model!
  *(This is a brand new method I have been developing for some time, I sincerely hope you enjoy it!)*


Custom GH05T Quants Added:
*These offer significantly higher performance and quality of response over previously uploaded release files while remaining <br />
similar or smaller in size!*
- Q2_K_L
- Q3_K_XL
- Q4_K_XL
- Q5_K_XL
- Q6_K_L
- Q8_0_L
- F16 (Floating Point 16-bit)

*Additionally, Multi-Modal Vision Projectors are also available (mmproj)*
- F16 (Floating Point 16-bit)
- F32 (Floating Point 32-bit)


**New JINJA Tokenizer Chat-Template:** <br />
*(This template features a sliding context window of  NINETY-NINE (99) messages. <br /> This can be adjusted per-individual requirements simply by altering <br />the number 99 in the template higher or lower in numerical value)*
```jinja
{%- set ns = namespace(remMessage=false, hasSys=false, injSystem=true) -%}
{%- for msg in messages -%}
	{%- if msg.role == "system" -%}
		{%- set ns.hasSys = true -%}
	{%- endif -%}
{%- endfor -%}
{%- for msg in messages -%}
	{{- bos_token -}}
	{%- if ns.injSystem -%}
		[SYSTEM_PROMPT]
		{%- if ns.hasSys -%}
			{{- msg.content -}}
		{%- else -%}
			'Always follow instructions that the user provides...'
		{%- endif -%}
		[/SYSTEM_PROMPT]
		{%- set ns.injSystem = false -%}
	{%- endif -%}
	{%- if (messages|length - loop.index0) < 99 -%}
		{%- set ns.remMessage = true -%}
	{%- endif -%}
	{%- if ns.remMessage -%}
		{%- if msg.role == "user" -%}
			{{- '[INST]' -}}
			{%- if msg.content is string -%}
				{{- msg.content -}}
        	{%- else -%}
            	{%- for block in msg.content -%}
            		{%- if block.type == 'text' -%}
                    	{{- block.text -}}
                	{%- elif block.type in ['image', 'image_url'] -%}
                    	{{- '[IMG]' -}}
                	{%- endif -%}
            	{%- endfor -%}
            {%- endif -%}
            {{- '[/INST]' -}}
		{%- elif msg.role == "assistant" -%}
			{{- msg.content -}}
		{%- endif -%}
	{%- endif -%}
	{{- eos_token -}}
{%- endfor -%}
```



## ------------------------------------------------<br /> - Model Details and Specifications: -<br />------------------------------------------------
# Ministral-3 8B Instruct 2512 (GGUF)

**This release contains:** <br />
GGUF converted and Quantized model files 
*(Compatible with:)*
- [Yollama - Privacy and Security Focused Rewrite of Ollama](https://github.com/EnlistedGhost/Yollama/releases/)
- [Llama.cpp - The absolute Solid Core of most any LLM Inferencing](https://github.com/ggml-org/llama.cpp/releases)
- Ollama

**Quantized GGUF version of:**
- Ministral-3-8B-Instruct-2512-BF16 <br /> *(by MistralAI)*

**Original Model Link:**
- [mistralai/Ministral-3-8B-Instruct-2512-BF16](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512-BF16)

----------------------------------------------

## -------------------------------------------------------------<br /> - GGUF Conversion and Quantization Details: -<br />-------------------------------------------------------------

**Software used to convert Safetensors to GGUF:**
- <a href="https://github.com/ggml-org/llama.cpp/">llama.cpp</a>

**Software used to create Quantized GGUF Files:**
- <a href="https://github.com/ggml-org/llama.cpp/">llama.cpp</a> 

**Specific GitHub Commit Point:**
- <a href="https://github.com/ggml-org/llama.cpp/releases">b8944 (and) b10444</a>

**Converted to GGUF and Quantized by:**
- [EnlistedGhost](https://huggingface.co/EnlistedGhost)

----------------------------------------------





## --------------------------<br /> ---- Original Info ---- <br /> --------------------------
*(Crossposted from the link in the above section: "Model Details"):*
<br />
<br />
<br />
<br />

# Ministral 3 8B Instruct 2512 BF16

The largest model in the Ministral 3 family, **Ministral 3 8B** offers frontier capabilities and performance comparable to its larger [Mistral Small 3.2 24B](https://huggingface.co/mistralai/Mistral-Small-3.2-Instruct-2506) counterpart. A powerful and efficient language model with vision capabilities.

This model is the instruct post-trained version, fine-tuned for instruction tasks, making it ideal for chat and instruction based use cases.

The Ministral 3 family is designed for edge deployment, capable of running on a wide range of hardware. Ministral 3 8B can even be deployed locally, capable of fitting in 32GB of VRAM in BF16, and less than 24GB of RAM/VRAM when quantized.

We provide a no-loss FP8 version [here](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512), you can find other formats and quantizations in the [Ministral 3 - Additional Checkpoints](https://huggingface.co/collections/mistralai/ministral-3-additional-checkpoints) collection.

## Key Features
Ministral 3 8B consists of two main architectural components:
- **7.3B Language Model**
- **0.4B Vision Encoder**

The Ministral 3 8B Instruct model offers the following capabilities:
- **Vision**: Enables the model to analyze images and provide insights based on visual content, in addition to text.
- **Multilingual**: Supports dozens of languages, including English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, Arabic.
- **System Prompt**: Maintains strong adherence and support for system prompts.
- **Agentic**: Offers best-in-class agentic capabilities with native function calling and JSON outputting.
- **Edge-Optimized**: Delivers best-in-class performance at a small scale, deployable anywhere.
- **Apache 2.0 License**: Open-source license allowing usage and modification for both commercial and non-commercial purposes.
- **Large Context Window**: Supports a 256k context window.

### Use Cases
Private AI deployments where advanced capabilities meet practical hardware constraints:
- Private/custom chat and AI assistant deployments in constrained environments
- Advanced local agentic use cases
- Fine-tuning and specialization
- And more...
  
Bringing advanced AI capabilities to most environments.

## Ministral 3 Family

| Model Name                     | Type               | Precision | Link                                                                                     |
|--------------------------------|--------------------|-----------|------------------------------------------------------------------------------------------|
| Ministral 3 3B Base 2512       | Base pre-trained   | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-3B-Base-2512)                |
| Ministral 3 3B Instruct 2512   | Instruct post-trained | BF16   | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512)            |
| Ministral 3 3B Reasoning 2512  | Reasoning capable  | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-3B-Reasoning-2512)           |
| Ministral 3 8B Base 2512       | Base pre-trained   | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-8B-Base-2512)                |
| **Ministral 3 8B Instruct 2512**   | **Instruct post-trained** | **BF16**    | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)            |
| Ministral 3 8B Reasoning 2512  | Reasoning capable  | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-8B-Reasoning-2512)           |
| Ministral 3 14B Base 2512      | Base pre-trained   | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512)               |
| Ministral 3 14B Instruct 2512  | Instruct post-trained | BF16    | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512)           |
| Ministral 3 14B Reasoning 2512 | Reasoning capable  | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-14B-Reasoning-2512)          |

Other formats available [here](https://huggingface.co/collections/mistralai/ministral-3-additional-checkpoints).

## Benchmark Results

We compare Ministral 3 to similar sized models.

### Reasoning

| Model                     | AIME25      | AIME24      | GPQA Diamond | LiveCodeBench |
|---------------------------|-------------|-------------|--------------|---------------|
| **Ministral 3 14B**       | <u>0.850</u>| <u>0.898</u>| <u>0.712</u> | <u>0.646</u>  |
| Qwen3-14B (Thinking)      | 0.737       | 0.837       | 0.663        | 0.593         |
|                           |             |             |              |               |
| **Ministral 3 8B**        | 0.787       | <u>0.860</u>| 0.668        | <u>0.616</u>  |
| Qwen3-VL-8B-Thinking      | <u>0.798</u>| <u>0.860</u>| <u>0.671</u> | 0.580         |
|                           |             |             |              |               |
| **Ministral 3 3B**        | <u>0.721</u>| <u>0.775</u>| 0.534        | <u>0.548</u>  |
| Qwen3-VL-4B-Thinking      | 0.697       | 0.729       | <u>0.601</u> | 0.513         |

### Instruct

| Model                     | Arena Hard  | WildBench  | MATH Maj@1  | MM MTBench       |
|---------------------------|-------------|------------|-------------|------------------|
| **Ministral 3 14B**       | <u>0.551</u>| <u>68.5</u>| <u>0.904</u>| <u>8.49</u>      |
| Qwen3 14B (Non-Thinking)  | 0.427       | 65.1       | 0.870       | NOT MULTIMODAL   |
| Gemma3-12B-Instruct       | 0.436       | 63.2       | 0.854       | 6.70             |
|                           |             |            |             |                  |
| **Ministral 3 8B**        | 0.509       | <u>66.8</u>| 0.876       | <u>8.08</u>      |
| Qwen3-VL-8B-Instruct      | <u>0.528</u>| 66.3       | <u>0.946</u>| 8.00             |
|                           |             |            |             |                  |
| **Ministral 3 3B**        | 0.305       | <u>56.8</u>| 0.830       | 7.83             |
| Qwen3-VL-4B-Instruct      | <u>0.438</u>| <u>56.8</u>| <u>0.900</u>| <u>8.01</u>      |
| Qwen3-VL-2B-Instruct      | 0.163       | 42.2       | 0.786       | 6.36             |
| Gemma3-4B-Instruct        | 0.318       | 49.1       | 0.759       | 5.23             |

### Base

| Model               | Multilingual MMLU | MATH CoT 2-Shot | AGIEval 5-shot | MMLU Redux 5-shot | MMLU 5-shot | TriviaQA 5-shot |
|---------------------|-------------------|-----------------|----------------|-------------------|-------------|-----------------|
| **Ministral 3 14B** | 0.742             | <u>0.676</u>    | 0.648          | 0.820             | 0.794       | 0.749           |
| Qwen3 14B Base      | <u>0.754</u>      | 0.620           | <u>0.661</u>   | <u>0.837</u>      | <u>0.804</u>| 0.703           |
| Gemma 3 12B Base    | 0.690             | 0.487           | 0.587          | 0.766             | 0.745       | <u>0.788</u>    |
|                     |                   |                 |                |                   |             |                 |
| **Ministral 3 8B**  | <u>0.706</u>      | <u>0.626</u>    | 0.591          | 0.793             | <u>0.761</u>| <u>0.681</u>    |
| Qwen 3 8B Base      | 0.700             | 0.576           | <u>0.596</u>   | <u>0.794</u>      | 0.760       | 0.639           |
|                     |                   |                 |                |                   |             |                 |
| **Ministral 3 3B**  | 0.652             | <u>0.601</u>    | 0.511          | 0.735             | 0.707       | 0.592           |
| Qwen 3 4B Base      | <u>0.677</u>      | 0.405           | <u>0.570</u>   | <u>0.759</u>      | <u>0.713</u>| 0.530           |
| Gemma 3 4B Base     | 0.516             | 0.294           | 0.430          | 0.626             | 0.589       | <u>0.640</u>    |

## License

This model is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0.txt).

*You must not use this model in a manner that infringes, misappropriates, or otherwise violates any third party’s rights, including intellectual property rights.*