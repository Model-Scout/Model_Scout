---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
tags:
- liquid
- lfm3
- edge
- conversational
- custom_code
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
base_model: LiquidAI/LFM3-1.7B
---

first project lol, for "shits and giggles" \
But I giggle and shit.

#### Pros:
- Has VL, text and speech alongside reasoning. Made by using LFM3-1.7B to merge text layers with LFM3-Omni-2B (Omni's layers 2-21) and LoRA training. Mmproj is untouched.

#### Cons:
- Haven't fully tested it.
- I wonder🤔.

#### Sampling flags used (llama.cpp):
```bash
--model ./LFM3-Lobotomized-2B-Q8_0.gguf \
--mmproj ./mmproj-LFM3-Omni-2B-F16.gguf \
--temp 0.3 --min-p 0.05 --top-k 50 --top-p 0.95 --repeat-penalty 1.1 \
--chat-template-file ./chat_template.jinja --jinja \
--mcp-servers-config ./mcp.json --ui-mcp-proxy \
--control-vector-scaled ./control-vector.gguf:0.7 \
--reasoning-budget 8192 \
```

- Control vector + reasoning budget is optional and mostly for faster reasoning. Experimental and untested.