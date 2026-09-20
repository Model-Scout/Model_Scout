---
library_name: transformers.js
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: image-text-to-text
tags:
- liquid
- lfm2
- lfm2-vl
- edge
- lfm2.5
- lfm2.5-vl
- onnx
- onnxruntime
- webgpu
base_model: LiquidAI/LFM2.5-VL-3B
---

<div align="center">
  <img
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> •
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> •
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> •
    <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
  </div>
</div>

# LFM2.5-VL-3B-ONNX

LFM2.5 is a new generation of hybrid models developed by [Liquid AI](https://www.liquid.ai/), specifically designed for edge AI and on-device deployment. It sets a new standard in terms of quality, speed, and memory efficiency.

Find more details in the original model card: https://huggingface.co/LiquidAI/LFM2.5-VL-3B

## 🏃 How to run LFM2.5-VL-3B

You can run the ONNX model in the browser with [Transformers.js](https://github.com/huggingface/transformers.js) v4.0 or newer:

```bash
npm install @huggingface/transformers
```

```js
import {
  AutoModelForImageTextToText,
  AutoProcessor,
  load_image,
} from "@huggingface/transformers";

const modelId = "LiquidAI/LFM2.5-VL-3B-ONNX";
const processor = await AutoProcessor.from_pretrained(modelId);
const model = await AutoModelForImageTextToText.from_pretrained(modelId, {
  device: "webgpu",
  dtype: {
    embed_tokens: "fp16",
    decoder_model_merged: "q4",
    vision_encoder: "fp16",
  },
});

const messages = [
  {
    role: "user",
    content: [
      { type: "image" },
      { type: "text", text: "Describe this image." },
    ],
  },
];
const prompt = processor.apply_chat_template(messages, {
  add_generation_prompt: true,
});

const image = await load_image("https://placecats.com/300/200");
const inputs = await processor(image, prompt, { add_special_tokens: false });
const outputs = await model.generate({
  ...inputs,
  do_sample: true,
  temperature: 0.2,
  top_k: 50,
  repetition_penalty: 1.0,
  max_new_tokens: 256,
});

const generated = outputs.slice(null, [inputs.input_ids.dims.at(-1), null]);
console.log(processor.batch_decode(generated, { skip_special_tokens: true })[0]);
```
