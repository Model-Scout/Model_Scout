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
- mistralai/Ministral-3-14B-Instruct-2512-BF16
new_version: EnlistedGhost/Ministral-3-14B-Instruct-2512-GGUF
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

## ------------------------------------------------<br /> - Model Details and Specifications: -<br />------------------------------------------------
# Ministral-3 14B Instruct 2512 (GGUF)

**This release contains:** <br />
Llama.cpp and Ollama compatible GGUF converted and Quantized model files 
*(Compatible with both Ollama, and Llama.cpp)*

**Quantized GGUF version of:**
- Ministral-3-14B-Instruct-2512-BF16 <br /> *(by MistralAI)*

**Original Model Link:**
- [mistralai/Ministral-3-14B-Instruct-2512-BF16](https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512-BF16)

**Description:** <br />
This release includes GGUF (Ollama + Llama.cpp - compatible) model files and three working multi-modal projector(s) 
(mmproj) files for the Vision Projector; offering full capabilities in Ollama or Llama.cpp.<br />

**What's New?** <br />
As of February 2026 all available GGUF (both F16 and K-Quants) files have been completely overhauled in order to offer the community
what I was able to come up with as best size vs quality possible for this model from MistralAI (Thank you MistralAI for your release!).
This was done by first taking the BF16 model's safetensors and *up-casting* them to F32, from there the model was quantized down to the
currently available files you find here. Beyond the F32-->Quant conversion that is a new methodology; **These GGUF F16+Quantize files also
include a completely custom tokenizer chat template.** <br /><br />

**Why Up-Cast to F32 from BF16?** <br />
Some will argue or perhaps be curious as to why the model was up-cast from BF16 to F32... This is because although it is true that there 
is no *direct* quality benefit from casting a BF16 release to a F32 bit file size, there *is however* a benefit of **less quality loss** 
when quantizing from an up-cast BF16 to F32 as the F32 has in a sense more "scratchpad" available mathematically and Quants derrived from an
F32 inherently degrade less per-Quant compared to a direct F16 or BF16 conversion. (It's worth a Google if anyone is ever curious!)
<br /><br />

**What is the "Custom Tokenizer Chat Template?"** <br />
As apposed to the standard "Chat Template" made available by MistralAI - this release of GGUF converted and quantized files offer a totally 
unique and custom Tokenizer Chat Template in order to provide: Smoother, Faster, Efficient, and Sophisticated interaction/inference with the model.
This template strips away all of the "fluff" or genuinely unneeded logic from the JINJA Chat/Tokenizer Template - allowing anyone who uses the model
for inferencing can enjoy a significant improvement in speed, quality and context adherence without sacrificing any aspect of the initial release by MistralAI.

**For reference - here is the new JINJA Tokenizer Chat-Template:** <br />
*(This template features a sliding context window of EIGHT (8) interactions, which may be adjusted per-individual requirements simply by altering
the third line of this template from the number nine (9) to either higher or lower numerical values to increase or decrease the sliding context window)*
```jinja
{%- set ns = namespace(remMessage=false, hasSys=false, injSystem=true) -%}
{%- for msg in messages -%}
	{%- if msg.role == "system" -%}
		{%- set ns.hasSys = true -%}
	{%- endif -%}
{%- endfor -%}
{%- for msg in messages -%}
	{%- if ns.injSystem -%}
		[SYSTEM_PROMPT]
		{%- if ns.hasSys -%}
			{{ msg.content }}
		{%- else -%}
'Respond to the message you receive using the same language that the message was written or the language the message requested.
Always respond directly to the user. Next sections describes the capabilities that you have.
🟦 [Multi-Modal Capability] You have the ability to read images, but not create images nor read audio/video.'
		{%- endif -%}
		[/SYSTEM_PROMPT]
		{%- set ns.injSystem = false -%}
	{%- endif -%}
	{%- if (messages|length - loop.index0) < 47 -%}
		{%- set ns.remMessage = true -%}
	{%- endif -%}
	{%- if ns.remMessage -%}
		{%- if msg.role == "user" -%}
			[INST]{{ msg.content }}[/INST]
		{%- elif msg.role == "assistant" -%}
			{{ msg.content }}
		{%- endif -%}
	{%- endif -%}
{%- endfor -%}
```

**No modifications, edits, or configurations are required** to use this model with
Ollama, it works natively! **Both Vision and Text work with Ollama. (^.^)** <br />

**Coming Soon!!!** <br />
Check back occasionally - as a automated installer/configure Python-3 script is making its way to all of my releases! 
This allows anyone who is interested in using these models a hassle-free and stress-free experience where the Python-3
script takes care of setting up the model for Ollama (specifically for Ollama, other software optimizations coming later). 
It is highly recommended to use the Ollama "create" command along with the supplied ".modelfile" to ensure proper configuration
for anyone who wishes to get the most out of this particular release. Though, the Python-3 automated installer/configuration tool
will handle such aspects if it is chosen to be used.

Happy Inferencing! <br />
 -- Jon Z (EnlistedGhost)

----------------------------------------------

### Model Updates (As of: February 27th, 2026)
- Updated: All GGUF model file(s) with significantly altered/reworked GGUF conversion(s) and Quant file(s)<br />
**Final Quantized and full-F16 modelfiles are being uploaded!!!** - Check back for I-Matrix quant files and other static
  K-Quants if you do not see your desired edition (They are being uploaded, thank you for your patience!)

----------------------------------------------

## -------------------------------------------------------------<br /> - GGUF Conversion and Quantization Details: -<br />-------------------------------------------------------------

**Software used to convert Safetensors to GGUF:**
- <a href="https://github.com/ggml-org/llama.cpp/">llama.cpp</a>

**Software used to create Quantized GGUF Files:**
- <a href="https://github.com/ggml-org/llama.cpp/">llama.cpp</a> 

**Specific GitHub Commit Point:**
- <a href="https://github.com/ggml-org/llama.cpp/commit/94b0200a01a753eff5897dab9311f51a7bc1c62f">b8118</a>

**Converted to GGUF and Quantized by:**
- [EnlistedGhost](https://huggingface.co/EnlistedGhost)

----------------------------------------------

## --------------------------<br /> ---- Original Info ---- <br /> --------------------------
*(Crossposted from the link in the above section: "Model Details"):*
<br />
<br />
<br />
<br />

# Ministral 3 14B Instruct 2512 BF16

The largest model in the Ministral 3 family, **Ministral 3 14B** offers frontier capabilities and performance comparable to its larger [Mistral Small 3.2 24B](https://huggingface.co/mistralai/Mistral-Small-3.2-Instruct-2506) counterpart. A powerful and efficient language model with vision capabilities.

This model is the instruct post-trained version, fine-tuned for instruction tasks, making it ideal for chat and instruction based use cases.

The Ministral 3 family is designed for edge deployment, capable of running on a wide range of hardware. Ministral 3 14B can even be deployed locally, capable of fitting in 32GB of VRAM in BF16, and less than 24GB of RAM/VRAM when quantized.

We provide a no-loss FP8 version [here](https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512), you can find other formats and quantizations in the [Ministral 3 - Additional Checkpoints](https://huggingface.co/collections/mistralai/ministral-3-additional-checkpoints) collection.

## Key Features
Ministral 3 14B consists of two main architectural components:
- **13.5B Language Model**
- **0.4B Vision Encoder**

The Ministral 3 14B Instruct model offers the following capabilities:
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
| Ministral 3 8B Instruct 2512   | Instruct post-trained | BF16    | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)            |
| Ministral 3 8B Reasoning 2512  | Reasoning capable  | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-8B-Reasoning-2512)           |
| Ministral 3 14B Base 2512      | Base pre-trained   | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512)               |
| **Ministral 3 14B Instruct 2512**  | **Instruct post-trained** | **BF16**    | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512)           |
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