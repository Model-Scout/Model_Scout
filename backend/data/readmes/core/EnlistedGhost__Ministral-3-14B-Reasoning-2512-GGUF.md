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
- ru
base_model:
- mistralai/Ministral-3-14B-Reasoning-2512
new_version: EnlistedGhost/Ministral-3-14B-Reasoning-2512-GGUF
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
- Multimodal
- Mistral3
- Multilingual
- Quantized
- LLM
- Thinking
- Reasoning
---

<img src="https://ollama.com/assets/library/mistral-nemo/72045292-694a-4867-88c8-8635c9d97030" alt="Example image" width="168" height="128"> 


<img src="https://ollama.com/assets/library/ministral-3/83fa3859-d87f-492c-bd81-596cfbceeccb" alt="Example image" width="64" height="64">

 ------------------------------------------------<br /> - Model Details and Specifications: -<br />------------------------------------------------
<br /> Ministral-3 14B Reasoning 2512 (GGUF)


## --------------------
##        NOTICE: <br /> <br /> I noticed after testing (post-upload) <br /> that the template doesn't like to play nice <br /> (doesn't seem to engage the thinking tags correctly) <br /> when pulled from HuggingFace, <br /> I will be correcting this today/tomorrow at the latest!
## --------------------



**This release contains:** <br />
Llama.cpp and Ollama compatible GGUF converted and Quantized model files 
*(Compatible with both Ollama, and Llama.cpp)*

**Quantized GGUF version of:**
- Ministral-3-14B-Reasoning-2512-BF16 <br /> *(by MistralAI)*

**Original Model Link:**
- [mistralai/Ministral-3-14B-Reasoning-2512](https://huggingface.co/mistralai/Ministral-3-14B-Reasoning-2512)

**Description:** <br />
This release includes GGUF (Ollama + Llama.cpp - compatible) model files and two working multi-modal projector(s) 
(mmproj) files for the Vision Projector; offering full capabilities in Ollama or Llama.cpp.<br />

**What is the "Custom Tokenizer Chat Template?"** <br />
As apposed to the standard "Chat Template" made available by MistralAI - this release of GGUF converted and quantized files offer a totally 
custom Tokenizer Chat Template in order to provide: Smoother, Faster, Efficient, and Reliable interaction/inference with the model.
This template sheds the "fluff" or non-primary logic from the JINJA Chat/Tokenizer Template - allowing anyone who uses the model
for inferencing the opportunity to enjoy a significant improvement in speed, quality and context adherence without sacrificing any aspect of the initial release by MistralAI.

**For reference - here is the new JINJA Tokenizer Chat-Template:** <br />
*(This template features a sliding context window of FORTY-SIX (46) interactions, which may be adjusted per-individual requirements simply by altering
the fourth (4th) line of this template, upwards from the number forty-seven (47) to either higher or lower numerical values to increase or decrease the sliding context window)*
```jinja
{{- $remMessage := false }}
[SYSTEM_PROMPT]{{- "🟦 Follow instructions that the user provides. Think and respond to the user in the language they use or request. Next sections describes the capabilities that you have. \n\n🟦 [Reasoning Instructions]\nYou have the ability to think before responding to the user. Always start your response by thinking, using an internal monologue. Always use this template when you respond: <think> thoughts and internal monologue </think> then respond directly to the user.\n\n🟦 [Multi-Modal Instructions]\nYou have the ability to read images." }}[/SYSTEM_PROMPT]
{{- range $index, $_ := .Messages }}
{{- if lt (len (slice $.Messages $index)) 47 }}
{{- $remMessage = true }}
{{- end }}
{{- if $remMessage }}{{- if eq .Role "user" }}
[INST]{{ .Content }}[/INST]
{{- else if eq .Role "assistant" }}
{{ .Content }}{{- end }}
{{- end }}
{{- end }}
```

**No modifications, edits, or configurations are required** to use this model with
Ollama or llama.cpp, it works natively! **Both Vision and Text work with Ollama as well. (^.^)** <br />

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

### Model Updates (As of: Match 26, 2026)
- Updated: Uploaded/Added all GGUF conversion(s) and non-i-matrix Quantized model file(s)<br />
**Final Quantized and full-F16 modelfiles are uploaded!!!** - Check back for i-Matrix quant model files if you do not see your desired edition (They are being uploaded, thank you for your patience!)

----------------------------------------------

## -------------------------------------------------------------<br /> - GGUF Conversion and Quantization Details: -<br />-------------------------------------------------------------

**Software used to convert Safetensors to GGUF:**
- <a href="https://github.com/ggml-org/llama.cpp/">llama.cpp | Version: 8189</a>

**Software used to create Quantized GGUF Files:**
- <a href="https://github.com/ggml-org/llama.cpp/">llama.cpp | Version: 8189</a> 

**Specific GitHub Commit Point:**
- <a href="https://github.com/ggml-org/llama.cpp/releases">b8189</a>

**Converted to GGUF and Quantized by:**
- [EnlistedGhost](https://huggingface.co/EnlistedGhost)

----------------------------------------------

## --------------------------<br /> ---- Original Info ---- <br /> --------------------------
*(Crossposted from the link in the above section: "Model Details"):*
<br />
<br />
<br />
<br />
<br />
<br />
<br />

# Ministral 3 14B Reasoning 2512 BF16

The largest model in the Ministral 3 family, **Ministral 3 14B** offers frontier capabilities and performance comparable to its larger [Mistral Small 3.2 24B](https://huggingface.co/mistralai/Mistral-Small-3.2-Instruct-2506) counterpart. A powerful and efficient language model with vision capabilities.

This model is the reasoning post-trained version, trained for reasoning tasks, making it ideal for math, coding and stem related use cases.

The Ministral 3 family is designed for edge deployment, capable of running on a wide range of hardware. Ministral 3 14B can even be deployed locally, capable of fitting in 32GB of VRAM in BF16, and less than 24GB of RAM/VRAM when quantized.

Learn more in our [blog post](https://mistral.ai/news/mistral-3) and [paper](https://arxiv.org/abs/2601.08584).

## Key Features
Ministral 3 14B consists of two main architectural components:
- **13.5B Language Model**
- **0.4B Vision Encoder**

The Ministral 3 14B Reasoning model offers the following capabilities:
- **Vision**: Enables the model to analyze images and provide insights based on visual content, in addition to text.
- **Multilingual**: Supports dozens of languages, including English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, Arabic.
- **System Prompt**: Maintains strong adherence and support for system prompts.
- **Agentic**: Offers best-in-class agentic capabilities with native function calling and JSON outputting.
- **Reasoning**: Excels at complex, multi-step reasoning and dynamic problem-solving.
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

### Recommended Settings

We recommend deploying with the following best practices:
- System Prompt: Use our provided [system prompt](https://huggingface.co/mistralai/Ministral-3-14B-Reasoning-2512/blob/main/SYSTEM_PROMPT.txt), and append it to your custom system prompt to define a clear environment and use case, including guidance on how to effectively leverage tools in agentic systems.
- Multi-turn Traces: We highly recommend keeping the reasoning traces in context.
- Sampling Parameters: Use a **temperature of 1** for most environments ; Different temperatures may be explored for different use cases - developers are encouraged to experiment with alternative settings.
- Tools: Keep the set of tools well-defined and limit their number to the minimum required for the use case - Avoiding overloading the model with an excessive number of tools.
- Vision: When deploying with vision capabilities, we recommend maintaining an aspect ratio close to 1:1 (width-to-height) for images. Avoiding the use of overly thin or wide images - crop them as needed to ensure optimal performance.

## Ministral 3 Family

| Model Name                     | Type               | Precision | Link                                                                                     |
|--------------------------------|--------------------|-----------|------------------------------------------------------------------------------------------|
| Ministral 3 3B Base 2512       | Base pre-trained   | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-3B-Base-2512)                |
| Ministral 3 3B Instruct 2512   | Instruct post-trained | FP8   | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512)            |
| Ministral 3 3B Reasoning 2512  | Reasoning capable  | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-3B-Reasoning-2512)           |
| Ministral 3 8B Base 2512       | Base pre-trained   | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-8B-Base-2512)                |
| Ministral 3 8B Instruct 2512   | Instruct post-trained | FP8    | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)            |
| Ministral 3 8B Reasoning 2512  | Reasoning capable  | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-8B-Reasoning-2512)           |
| Ministral 3 14B Base 2512      | Base pre-trained   | BF16      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512)               |
| Ministral 3 14B Instruct 2512  | Instruct post-trained | FP8    | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512)           |
| **Ministral 3 14B Reasoning 2512** | **Reasoning capable**  | **BF16**      | [Hugging Face](https://huggingface.co/mistralai/Ministral-3-14B-Reasoning-2512)          |

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