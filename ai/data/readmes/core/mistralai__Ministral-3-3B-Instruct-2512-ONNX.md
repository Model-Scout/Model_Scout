---
license: apache-2.0
base_model:
- mistralai/Ministral-3-3B-Instruct-2512
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
library_name: transformers.js
tags:
- onnxruntime
pipeline_tag: image-text-to-text
---
> [!Tip]
> This model was contributed by [Xenova](https://huggingface.co/Xenova) from Hugging Face. We sincerely appreciate the integration and community collaboration. While preliminary functionality checks have been performed, comprehensive testing has not yet been completed. We recommend you to proceed with caution and conducting your own evaluations for specific use cases. If any issues arise, open a PR/Issue here and we will try to address them promptly.

# Ministral 3 3B Instruct 2512 ONNX

The smallest model in the Ministral 3 family, **Ministral 3 3B** is a powerful, efficient tiny language model with vision capabilities.

This model quantized weights of the instruct post-trained version in **ONNX**, fine-tuned for instruction tasks, making it ideal for chat and instruction based use cases.

The Ministral 3 family is designed for edge deployment, capable of running on a wide range of hardware. Ministral 3 3B can even be deployed locally, capable of fitting in 8GB of VRAM in FP8, and less if further quantized.

Learn more in our [blog post](https://mistral.ai/news/mistral-3) and [paper](https://arxiv.org/abs/2601.08584).

## Key Features
Ministral 3 3B consists of two main architectural components:
- **3.4B Language Model**
- **0.4B Vision Encoder**

The Ministral 3 3B Instruct model offers the following capabilities:
- **Vision**: Enables the model to analyze images and provide insights based on visual content, in addition to text.
- **Multilingual**: Supports dozens of languages, including English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, Arabic.
- **System Prompt**: Maintains strong adherence and support for system prompts.
- **Agentic**: Offers best-in-class agentic capabilities with native function calling and JSON outputting.
- **Edge-Optimized**: Delivers best-in-class performance at a small scale, deployable anywhere.
- **Apache 2.0 License**: Open-source license allowing usage and modification for both commercial and non-commercial purposes.
- **Large Context Window**: Supports a 256k context window.


## Usage


### Transformers.js

#### Online WebGPU Demo

You can test out the model directly in your browser using our online WebGPU demo: https://huggingface.co/spaces/mistralai/Ministral_3B_WebGPU.

<video src="https://cdn-uploads.huggingface.co/production/uploads/61b253b7ac5ecaae3d1efe0c/LA0XUsH9pFZaphbfF-HGm.mp4" controls autoplay muted></video>

#### JavaScript

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

You can then run the model as follows:
```js
import {
    AutoProcessor,
    AutoModelForImageTextToText,
    load_image,
    TextStreamer,
} from "@huggingface/transformers";

// Load processor and model
const model_id = "mistralai/Ministral-3-3B-Instruct-2512-ONNX";
const processor = await AutoProcessor.from_pretrained(model_id);
const model = await AutoModelForImageTextToText.from_pretrained(model_id, {
    device: "webgpu",
});

// Prepare inputs
const messages = [
    {
        role: "user",
        content: [
            { type: "image" },
            {
                type: "text",
                text: "What action do you think I should take in this situation? List all the possible actions and explain why you think they are good or bad.",
            },
        ],
    },
]
const prompt = processor.apply_chat_template(messages);
const url = "https://static.wikia.nocookie.net/essentialsdocs/images/7/70/Battle.png/revision/latest?cb=20220523172438";
const image = await load_image(url);
const inputs = await processor(image, prompt, { add_special_tokens: false });

// Generate response
const outputs = await model.generate({
    ...inputs,
    max_new_tokens: 2048,
    streamer: new TextStreamer(processor.tokenizer, {
        skip_prompt: true,
        // callback_function: (text) => { /* Do something with the streamed output */ },
    }),
});

// Decode output
const decoded = processor.batch_decode(
    outputs.slice(null, [inputs.input_ids.dims.at(-1), null]),
    { skip_special_tokens: true },
);
console.log(decoded[0]);
```

<details>

<summary>See example output</summary>

```
In this Pokémon game screenshot, you have several potential actions to consider, depending on the situation and your strategy. Here are the possible actions and their implications:

---

### **1. FIGHT**
**Description:** Use the Pikachu in your possession to attack the Pidgey.

#### **Pros:**
- **Potential to defeat Pidgey:** If Pikachu has strong moves (e.g., Thunderbolt, Electric Move) and Pidgey is weak to Electric-type attacks, this could be a strong choice.
- **Experience Gain:** Winning battles typically rewards you with experience points (XP) and sometimes drops Pidgey as a captured Pokémon.
- **Training Opportunity:** Helps you level up Pikachu, which can improve its stats and access new moves.

#### **Cons:**
- **Risk of Losing Pikachu:** If Pikachu is already at a low HP (e.g., 83/83 is not bad, but if it's lower), a loss could be detrimental.
- **Move Selection Matters:** If Pikachu doesn’t have a strong move against Pidgey, you might lose the battle unnecessarily.
- **Stamina Cost:** Battles can consume stamina if you're on a timer-based system (e.g., Pokémon Red/Blue).

---

### **2. RUN**
**Description:** Use the "Run" option to escape the battle.

#### **Pros:**
- **Avoids Risk:** If you're unsure about Pikachu’s moves or HP, running could save you from a potentially bad outcome.
- **Preserves Resources:** Running avoids losing Pikachu’s HP, which could be useful if you're running low.
- **Flexibility:** Allows you to explore or use other Pokémon later.

#### **Cons:**
- **No XP Gain:** Running means you won’t earn XP for defeating Pidgey.
- **Potential Consequences:** If you run too often, you might miss out on capturing Pidgey or gaining experience.
- **No Training:** Pikachu won’t level up or gain new moves if you avoid battles.

---

### **3. POKEMON (Select Another Pokémon)**
**Description:** If you have another Pokémon in your party, you could switch to it.

#### **Pros:**
- **Better Move Selection:** If you have a stronger Pokémon (e.g., a Fire-type or Ground-type) that can handle Pidgey, switching could be beneficial.
- **Balanced Strategy:** Helps you manage your team better.
- **Avoids Weaknesses:** If Pikachu is weak to something Pidgey might use, switching could prevent a loss.

#### **Cons:**
- **No Immediate XP Gain:** Switching doesn’t defeat Pidgey, so you won’t earn XP.
- **Stamina Cost:** Switching might still consume stamina if you're on a timer.
- **Potential to Lose Pikachu:** If you switch and Pikachu is already at a low HP, you might lose it.

---

### **Best Strategy Based on the Image:**
- **If you want to capture Pidgey:** Fighting is the best option, as it rewards you with experience and potentially captures Pidgey.
- **If you're unsure about Pikachu’s moves:** Running could be safer, but you might miss out on XP.
- **If you have another Pokémon:** Switching could be a good idea if you have a stronger option.

Would you like to know what moves Pikachu might have, or do you have another Pokémon in your party? That could help decide the best action!
```

</details>


### ONNXRuntime

```py
from transformers import AutoConfig, AutoProcessor
import onnxruntime
import numpy as np
from huggingface_hub import hf_hub_download

# 1. Load config, processor, and model
model_id = "mistralai/Ministral-3-3B-Instruct-2512-ONNX"
config = AutoConfig.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id)

vision_model_path = hf_hub_download(model_id, "vision_encoder_q4.onnx", subfolder="onnx")         # Download vision graph
hf_hub_download(model_id, "vision_encoder_q4.onnx_data", subfolder="onnx")                        # Download vision weights
embed_model_path = hf_hub_download(model_id, "embed_tokens_fp16.onnx", subfolder="onnx")          # Download embed_tokens graph
hf_hub_download(model_id, "embed_tokens_fp16.onnx_data", subfolder="onnx")                        # Download embed_tokens weights
decoder_model_path = hf_hub_download(model_id, "decoder_model_merged_q4.onnx", subfolder="onnx")  # Download decoder graph
hf_hub_download(model_id, "decoder_model_merged_q4.onnx_data", subfolder="onnx")                  # Download decoder weights (1/2)
hf_hub_download(model_id, "decoder_model_merged_q4.onnx_data_1", subfolder="onnx")                # Download decoder weights (2/2)

## Load sessions
providers = ['CPUExecutionProvider']
vision_session = onnxruntime.InferenceSession(vision_model_path, providers=providers)
embed_session = onnxruntime.InferenceSession(embed_model_path, providers=providers)
decoder_session = onnxruntime.InferenceSession(decoder_model_path, providers=providers)

## Set config values
text_config = config.text_config
num_key_value_heads = text_config.num_key_value_heads
head_dim = text_config.head_dim
num_hidden_layers = text_config.num_hidden_layers
eos_token_id = text_config.eos_token_id
image_token_index = config.image_token_index

# 2. Prepare inputs
image_url = "https://static.wikia.nocookie.net/essentialsdocs/images/7/70/Battle.png/revision/latest?cb=20220523172438"
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "What action do you think I should take in this situation? List all the possible actions and explain why you think they are good or bad.",
            },
            {"type": "image", "url": image_url},
        ],
    },
]
inputs = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt")

input_ids = inputs['input_ids'].numpy()
attention_mask = inputs['attention_mask'].numpy()
pixel_values = inputs['pixel_values'].numpy()
batch_size = input_ids.shape[0]
past_key_values = {
    f'past_key_values.{layer}.{kv}': np.zeros([batch_size, num_key_value_heads, 0, head_dim], dtype=np.float32)
    for layer in range(num_hidden_layers)
    for kv in ('key', 'value')
}
position_ids = np.tile(np.arange(0, input_ids.shape[-1]), (batch_size, 1))

# 3. Generation loop
max_new_tokens = 1024
generated_tokens = np.array([[]], dtype=np.int64)
image_features = None
for i in range(max_new_tokens):
  inputs_embeds = embed_session.run(None, {'input_ids': input_ids})[0]

  if image_features is None:
    ## Only compute vision features if not already computed
    image_features = vision_session.run(None, dict(
        pixel_values=pixel_values,
    ))[0]

    ## Merge text and vision embeddings
    inputs_embeds[input_ids == image_token_index] = image_features.reshape(-1, image_features.shape[-1])

  logits, *present_key_values = decoder_session.run(None, dict(
      inputs_embeds=inputs_embeds,
      attention_mask=attention_mask,
      position_ids=position_ids,
      **past_key_values,
  ))

  ## Update values for next generation loop
  input_ids = logits[:, -1].argmax(-1, keepdims=True)
  attention_mask = np.concatenate([attention_mask, np.ones((batch_size, 1), dtype=attention_mask.dtype)], axis=-1)
  position_ids = position_ids[:, -1:] + 1
  for j, key in enumerate(past_key_values):
    past_key_values[key] = present_key_values[j]

  generated_tokens = np.concatenate([generated_tokens, input_ids], axis=-1)
  if (input_ids == eos_token_id).all():
    break

  ## (Optional) Streaming
  print(processor.decode(input_ids[0]), end='', flush=True)
print()

# 4. Output result
print(processor.batch_decode(generated_tokens, skip_special_tokens=True)[0])
```

<details>
<summary>See example output</summary>

```
In this *Pokémon* game screenshot, you are presented with a battle scenario between **Pidgey** and **Pikachu**. Here are the possible actions along with an analysis of their potential outcomes:

---

### **1. FIGHT**
**Explanation:**
- You choose to engage in battle.
- Pidgey is a **Level 17** Pokémon with basic stats, while Pikachu is a **Level 42** Pokémon with significantly higher HP, Attack, and overall power.
- **Pros:**
  - Pikachu is stronger and likely to win if it lands a hit.
  - Pidgey may be able to land a few moves before being overwhelmed.
- **Cons:**
  - Pidgey is likely to lose quickly due to its lower stats and experience.
  - Pikachu may have a high chance of winning in one or two turns.

---

### **2. BAG**
**Explanation:**
- You choose to **Bag** Pikachu.
- **Pros:**
  - You can keep Pikachu in your bag for later use.
  - If you need to switch Pokémon or use Pikachu in another battle, this is a viable option.
- **Cons:**
  - You miss out on the opportunity to potentially defeat Pidgey and gain experience.
  - If Pidgey is a rare or special Pokémon, bagging it might not be ideal.

---

### **3. RUN**
**Explanation:**
- You choose to **Run** (escape the battle).
- **Pros:**
  - You avoid losing HP and experience points.
  - You can continue your journey without facing a weaker opponent.
- **Cons:**
  - You might miss out on a chance to level up Pikachu or gain experience.
  - If you are in a competitive setting, running might not be the best strategy.

---

### **Summary of Best Options:**
- **If you want to continue the game and gain experience:**
  - **Fight** Pikachu, but be prepared for a potentially quick loss.
- **If you want to save Pikachu for later:**
  - **Bag** Pikachu and continue your journey.
- **If you want to avoid unnecessary battles:**
  - **Run** away from the battle.

Since Pikachu is significantly stronger, **Fighting** is the most straightforward choice, but you might want to consider **Bagging** Pikachu if you want to keep it for later battles. If you're not in a rush, **Running** is also a viable option.
In this *Pokémon* game screenshot, you are presented with a battle scenario between **Pidgey** and **Pikachu**. Here are the possible actions along with an analysis of their potential outcomes:

---

### **1. FIGHT**
**Explanation:**
- You choose to engage in battle.
- Pidgey is a **Level 17** Pokémon with basic stats, while Pikachu is a **Level 42** Pokémon with significantly higher HP, Attack, and overall power.
- **Pros:**
  - Pikachu is stronger and likely to win if it lands a hit.
  - Pidgey may be able to land a few moves before being overwhelmed.
- **Cons:**
  - Pidgey is likely to lose quickly due to its lower stats and experience.
  - Pikachu may have a high chance of winning in one or two turns.

---

### **2. BAG**
**Explanation:**
- You choose to **Bag** Pikachu.
- **Pros:**
  - You can keep Pikachu in your bag for later use.
  - If you need to switch Pokémon or use Pikachu in another battle, this is a viable option.
- **Cons:**
  - You miss out on the opportunity to potentially defeat Pidgey and gain experience.
  - If Pidgey is a rare or special Pokémon, bagging it might not be ideal.

---

### **3. RUN**
**Explanation:**
- You choose to **Run** (escape the battle).
- **Pros:**
  - You avoid losing HP and experience points.
  - You can continue your journey without facing a weaker opponent.
- **Cons:**
  - You might miss out on a chance to level up Pikachu or gain experience.
  - If you are in a competitive setting, running might not be the best strategy.

---

### **Summary of Best Options:**
- **If you want to continue the game and gain experience:**
  - **Fight** Pikachu, but be prepared for a potentially quick loss.
- **If you want to save Pikachu for later:**
  - **Bag** Pikachu and continue your journey.
- **If you want to avoid unnecessary battles:**
  - **Run** away from the battle.

Since Pikachu is significantly stronger, **Fighting** is the most straightforward choice, but you might want to consider **Bagging** Pikachu if you want to keep it for later battles. If you're not in a rush, **Running** is also a viable option.
```

</details>


## License

This model is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0.txt).

*You must not use this model in a manner that infringes, misappropriates, or otherwise violates any third party’s rights, including intellectual property rights.*