---
license: apache-2.0
base_model: Qwen/Qwen3.5-0.8B
library_name: mlc-llm
tags:
  - mlc-llm
  - web-llm
  - webgpu
  - qwen3.5
  - grounded-generation
  - on-device
language:
  - en
  - de
  - zh
  - ja
  - fr
  - es
  - it
  - ko
pipeline_tag: text-generation
---

# grounded-persona-Qwen3.5-0.8B-q4f16_1-MLC

A small model that answers questions about a person from a fact sheet in the system prompt. It runs in the browser with [WebLLM](https://github.com/mlc-ai/web-llm) and WebGPU.

The model does not store facts about any person. Give it a different fact sheet and it answers about that person. It is a general model. It is not the model on yipengsun.com.

## Use

```js
import * as webllm from "https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.86/lib/index.js";

const repo = "https://huggingface.co/yipengsun/grounded-persona-Qwen3.5-0.8B-q4f16_1-MLC/resolve/main/";
const engine = await webllm.CreateMLCEngine("grounded-persona", {
  appConfig: { model_list: [{
    model: repo,
    model_id: "grounded-persona",
    model_lib: repo + "qwen3_5-0.8b-q4f16_1-vocab51200-webgpu.wasm",
    overrides: { context_window_size: 4096 },
  }] },
});

const reply = await engine.chat.completions.create({
  messages: [{ role: "system", content: RULES + "\n" + FACT_SHEET }, ...history],
  temperature: 0,
  extra_body: { enable_thinking: false },
});
```

- Put the fact sheet as short Markdown bullets after `SITE FACTS:`. Keep it under about 2,000 tokens.
- `RULES` tells the model to answer in the first person, use only the sheet, and refuse anything else with the sheet's public email.
- The download is about 310 MB. The vocabulary has 51,200 tokens, so the repository includes its own WebGPU library.

## Limitations

A 0.8B model can make mistakes. It can answer only what the fact sheet contains.

## License

Apache 2.0, the same as the base model.
