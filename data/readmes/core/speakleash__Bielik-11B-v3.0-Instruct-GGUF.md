---
language:
- multilingual
- pl
- en
- sq
- bel
- bs
- bg
- hr
- cs
- da
- et
- fi
- fr
- el
- es
- is
- lt
- nl
- de
- no
- pt
- ru
- ro
- sr
- hbs
- sv
- sk
- sl
- tr
- uk
- hu
- it
- lv
license: apache-2.0
library_name: transformers
tags:
- finetuned
- gguf
inference: false
pipeline_tag: text-generation
base_model: speakleash/Bielik-11B-v3.0-Instruct
---

<p align="center">
  <img src="https://huggingface.co/speakleash/Bielik-11B-v2/raw/main/speakleash_cyfronet.png">
</p>

# Bielik-11B-v3.0-Instruct-GGUF

This repo contains GGUF format model files for [SpeakLeash](https://speakleash.org/)'s [Bielik-11B-v3.0-Instruct](https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct).

<b><u>DISCLAIMER: Be aware that quantised models show reduced response quality and possible hallucinations!</u></b><br>

### Available quantization formats:
* **q4_k_m:** Uses Q6_K for half of the attention.wv and feed_forward.w2 tensors, else Q4_K
* **q5_k_m:** Uses Q6_K for half of the attention.wv and feed_forward.w2 tensors, else Q5_K
* **q6_k:** Uses Q8_K for all tensors
* **q8_0:** Almost indistinguishable from float16. High resource use and slow. Not recommended for most users.
* **16bit:** Converted to FP16 and BF16 GGUF format.

Bielik 11B v3.0 is on [Ollama](https://ollama.com/SpeakLeash/bielik-11b-v3.0-instruct)!
https://ollama.com/SpeakLeash/bielik-11b-v3.0-instruct

### Ollama Modfile
The GGUF file can be used with [Ollama](https://ollama.com/). To do this, you need to import the model using the configuration defined in the Modfile. For model eg. Bielik-11B-v3.0-Instruct.Q4_K_M.gguf (full path to model location) Modfile looks like:

```
FROM ./Bielik-11B-v3.0-Instruct.Q4_K_M.gguf

TEMPLATE """<s>{{ if .System }}<|start_header_id|>system<|end_header_id|>

{{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>

{{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>

{{ .Response }}<|eot_id|>"""

PARAMETER stop "<|start_header_id|>"
PARAMETER stop "<|end_header_id|>"
PARAMETER stop "<|eot_id|>"

# Remeber to set low temperature for experimental models (1-3bits)
PARAMETER temperature 0.1

```

Ollama Modfile with tools (already on [Ollama](https://ollama.com/SpeakLeash/bielik-11b-v3.0-instruct)):
```
FROM ./Bielik-11B-v3.0-Instruct.Q8_0.gguf

TEMPLATE """{{- /* SYSTEM + TOOLS INJECTION */ -}}
{{- if or .System .Tools -}}
<|im_start|>system
{{- if .System }}
{{ .System }}
{{- end }}

{{- if .Tools }}
You are provided with tool signatures that you can use to assist with the user's query.
You do not have to use a tool if you can respond adequately without it.
Do not make assumptions about tool arguments. If required parameters are missing, ask a clarification question.

If you decide to invoke a tool, you MUST respond with ONLY valid JSON in the following format:
{"name":"<tool-name>","arguments":{...}}

Below is a list of tools you can invoke (JSON):
{{ .Tools }}
{{- end }}
<|im_end|>
{{- end }}

{{- /* MESSAGES */ -}}
{{- range $i, $_ := .Messages }}
<|im_start|>{{ .Role }}
{{ .Content }}<|im_end|>
{{- end }}

{{- /* GENERATION PROMPT */ -}}
<|im_start|>assistant"""

PARAMETER stop "<|start_header_id|>"
PARAMETER stop "<|end_header_id|>"
PARAMETER stop "<|eot_id|>"

PARAMETER temperature 0.1
```


### Model description:

* **Developed by:** [SpeakLeash](https://speakleash.org/) & [ACK Cyfronet AGH](https://www.cyfronet.pl/)
* **Language:** Multilingual (32 European languages, optimized for Polish)
* **Model type:** causal decoder-only
* **Quant from:** [Bielik-11B-v3.0-Instruct](https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct)
* **Finetuned from:** [speakleash/Bielik-11B-v3-Base-20250730](https://huggingface.co/speakleash/Bielik-11B-v3-Base-20250730)
* **License:** Apache 2.0

### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023.

Here is an incomplete list of clients and libraries that are known to support GGUF:
* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [GPT4All](https://gpt4all.io/index.html), a free and open source local running GUI, supporting Windows, Linux and macOS with full GPU accel.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows, macOS (Silicon) and Linux, with GPU acceleration
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server. Note ctransformers has not been updated in a long time and does not support many recent models.

### Responsible for model quantization  
* [Remigiusz Kinas](https://www.linkedin.com/in/remigiusz-kinas/)<sup>SpeakLeash</sup> - team leadership, conceptualizing, calibration data preparation, process creation and quantized model delivery.
* [Kuba Sołtys](https://www.linkedin.com/in/qooba/)<sup>SpeakLeash</sup> - prepared a template with tools for Ollama
* [Szymon Baczyński](https://www.linkedin.com/in/szymon-baczynski/)<sup>SpeakLeash</sup> - team assistant


## Contact Us

If you have any questions or suggestions, please use the discussion tab. If you want to contact us directly, join our [Discord SpeakLeash](https://discord.gg/CPBxPce4).
