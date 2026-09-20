---
language:
- ko
- en
license: apache-2.0
tags:
- qwen
- instruct
- alibaba
- multilingual
- korean
pipeline_tag: text-generation
---

## 📌 Notice
- ✅ Original model is [beomi/Qwen2.5-7B-Instruct-kowiki-qa](https://huggingface.co/beomi/Qwen2.5-7B-Instruct-kowiki-qa)
- ✅ Quantized by [teddylee777](https://huggingface.co/teddylee777) by using [llama.cpp](https://github.com/ggerganov/llama.cpp)

## 💬 Template

```
FROM Qwen2.5-7B-Instruct-kowiki-qa-context-Q8_0.gguf

TEMPLATE """{{- if .System }}
<|im_start|>system
{{ .System }}
<|im_end|>
{{- end }}
<|im_start|>user
{{ .Prompt }}
<|im_end|>
<|im_start|>assistant
"""

SYSTEM """You are Qwen, created by Alibaba Cloud. You are a helpful assistant. 모든 대답은 한국어로 해주세요."""

PARAMETER temperature 0
PARAMETER num_ctx 128000
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>
```

## 🧑‍💻 Helpful Contents
- ✅ [How to load HuggingFace GGUF into LM Studio](https://youtu.be/bANQk--Maxs)
- ✅ [How to test llama3 by using Ollama](https://youtu.be/12CuUQIPdM4)
- 🇰🇷 [LangChain Tutorial in Korean](https://wikidocs.net/book/14314)
- 🔥 Please subscribe and support on [YouTube](https://www.youtube.com/@teddynote) 
