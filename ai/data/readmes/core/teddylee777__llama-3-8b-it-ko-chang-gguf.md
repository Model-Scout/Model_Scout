---
library_name: transformers
license: apache-2.0
language:
- ko
---

- Original model is [lcw99/llama-3-8b-it-ko-chang](https://huggingface.co/lcw99/llama-3-8b-it-ko-chang)
- Quantized by [teddylee777](https://huggingface.co/teddylee777) by using [llama.cpp](https://github.com/ggerganov/llama.cpp)

## Template (LM Studio)

```
<|start_header_id|>system<|end_header_id|>
{System}
<|eot_id|>
<|start_header_id|>B<|end_header_id|>
{User}
<|eot_id|><|start_header_id|>A<|end_header_id|>
{Assistant}
```

### LM Studio Demo

![image/png](https://cdn-uploads.huggingface.co/production/uploads/649d86964ee9d3611f71f39e/oBr-a6-hf0frsKwtDDafL.png)


## Ollama Template

```
TEMPLATE """{{- if .System }}<|start_header_id|>system<|end_header_id|>
{{ .System }}
<|eot_id|>
{{- end }}

<|start_header_id|>B<|end_header_id|>
{{ .Prompt }}
<|eot_id|>
<|start_header_id|>A<|end_header_id|>
"""
```

### Ollama DEMO

![image/png](https://cdn-uploads.huggingface.co/production/uploads/649d86964ee9d3611f71f39e/fed4vqNcjQPW3WuzPjgKv.png)

## Stop Token

```
<|eot_id|>
<|start_header_id|>
<|end_header_id|>
<|begin_of_text|> 
<|end_of_text|>
```