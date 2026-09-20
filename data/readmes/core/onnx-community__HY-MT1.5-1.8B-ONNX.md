---
base_model:
- tencent/HY-MT1.5-1.8B
tags:
- translation
language:
- zh
- en
- fr
- pt
- es
- ja
- tr
- ru
- ar
- ko
- th
- it
- de
- vi
- ms
- id
- tl
- hi
- pl
- cs
- nl
- km
- my
- fa
- gu
- ur
- te
- mr
- he
- bn
- ta
- uk
- bo
- kk
- mn
- ug
---


## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

You can then use the model to translate text as follows:

```js
import { pipeline, TextStreamer } from "@huggingface/transformers";

// Create a text generation pipeline
const generator = await pipeline(
  "text-generation",
  "onnx-community/HY-MT1.5-1.8B-ONNX",
  { dtype: "q4", device: "webgpu" },
);

// Define the list of messages
const target_lang = "Chinese";
const prompt = "It’s on the house.";
const messages = [
  { role: "user", content: `Translate the following segment into ${target_lang}, without additional explanation.\n\n${prompt}` },
];

// Generate a response
const output = await generator(messages, {
  max_new_tokens: 512,
  do_sample: false,
  streamer: new TextStreamer(generator.tokenizer, {
    skip_prompt: true,
    skip_special_tokens: true,
  }),
});
console.log(output[0].generated_text.at(-1).content);
```