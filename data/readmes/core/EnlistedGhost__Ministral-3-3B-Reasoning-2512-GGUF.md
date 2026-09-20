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
- mistralai/Ministral-3-3B-Reasoning-2512
new_version: EnlistedGhost/Ministral-3-3B-Reasoning-2512-GGUF
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
<br /> Ministral-3 3B Reasoning 2512 (GGUF)



## --------------------
##        NOTICE: <br /> <br /> I noticed after testing (post-upload) <br /> that the template doesn't like to play nice <br /> (doesn't seem to engage the thinking tags correctly) <br /> when pulled from HuggingFace, <br /> I will be correcting this today/tomorrow at the latest!
## --------------------




**This release contains:** <br />
Llama.cpp and Ollama compatible GGUF converted and Quantized model files 
*(Compatible with both Ollama, and Llama.cpp)*

**Quantized GGUF version of:**
- Ministral-3-3B-Reasoning-2512-BF16 <br /> *(by MistralAI)*

**Original Model Link:**
- [mistralai/Ministral-3-3B-Reasoning-2512](https://huggingface.co/mistralai/Ministral-3-3B-Reasoning-2512)

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