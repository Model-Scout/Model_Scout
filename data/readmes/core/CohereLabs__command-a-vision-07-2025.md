---
inference: false
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
license: cc-by-nc-4.0
extra_gated_prompt: >-
  By submitting this form, you agree to the [License
  Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and acknowledge that the
  information you provide will be collected, used, and shared in accordance with
  Cohere’s [Privacy Policy]( https://cohere.com/privacy). You’ll receive email
  updates about C4AI and Cohere research, events, products and services. You can
  unsubscribe at any time.
extra_gated_fields:
  Name: text
  Affiliation: text
  Country: country
  I agree to use this model for non-commercial use ONLY: checkbox
pipeline_tag: image-text-to-text
base_model:
- CohereLabs/c4ai-command-a-03-2025
- google/siglip2-so400m-patch16-512
---


# **Model Card for Cohere Labs Command A Vision**

## **Model Summary**

Cohere Labs Command A Vision is an open weights research release of a 112 billion parameter model optimized for enterprise image understanding tasks, while keeping a low compute footprint. 

Developed by: [Cohere](https://cohere.com/) and [Cohere Labs](https://cohere.com/research)

* Point of Contact: [**Cohere Labs**](https://cohere.com/research)  
* License: [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license), requires also adhering to **[Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)**  
* Model: command-a-vision-07-2025  
* Model Size: 112B  
* Context length: 32K

For more details about this model, please check out our [blog post](https://cohere.com/blog/command-a-vision). 

Note: The model supports a context length of 128K but it is configured in Hugging Face for 32K. This value can be updated in the configuration if needed.

**Try Cohere Labs Command A Vision** 

You can try out Cohere Labs Command A Vision before downloading the weights in our hosted [Hugging Face Space](https://huggingface.co/spaces/CohereLabs/command-a-vision).

**Usage**

Please install transformers from the source repository that includes the necessary changes for this model.

```py
# pip install "transformers[dev-torch]@git+https://github.com/huggingface/transformers.git"

import torch

from transformers import AutoProcessor, AutoModelForImageTextToText

model_id = "CohereLabs/command-a-vision-07-2025"

processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id, device_map="auto", torch_dtype=torch.float16
)

# Format message with the Command-A-Vision chat template
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "url": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
            },
            {"type": "text", "text": "what is in this image?"},
        ],
    },
]

inputs = processor.apply_chat_template(
    messages,
    padding=True,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

gen_tokens = model.generate(
    **inputs,
    max_new_tokens=300,
    do_sample=True,
    temperature=0.3,
)

print(
    processor.tokenizer.decode(
        gen_tokens[0][inputs.input_ids.shape[1] :], skip_special_tokens=True
    )
)


```

You can also use the model directly using transformers `pipeline` abstraction:

```py
from transformers import pipeline

pipe = pipeline(model="CohereLabs/command-a-vision-07-2025", task="image-text-to-text", device_map="auto")

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "url": "https://media.istockphoto.com/id/458012057/photo/istanbul-turkey.jpg?s=612x612&w=0&k=20&c=qogAOVvkpfUyqLUMr_XJQyq-HkACXyYUSZbKhBlPrxo=",
            },
            {"type": "text", "text": "Where was this taken ?"},
        ],
    },
]

outputs = pipe(text=messages, max_new_tokens=300, return_full_text=False)

print(outputs)
```

## **Model Details**

**Input**: Model accepts input text and images.

**Output**: Model generates text. 

**Model Architecture**: 

This is a vision-language model that uses a language model based on [Command A](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025) paired with the [SigLIP2-patch16-512](https://huggingface.co/google/siglip2-so400m-patch16-512) vision encoder through a multimodal adapter for vision-language understanding.

**Image Processing:** 

We use 256 visual tokens to encode a single image tile with a resolution of 512x512 pixels. Input images of arbitrary sizes are mapped to the nearest supported resolution based on their aspect ratio. Command A Vision uses up to 12 input tiles, depending on image resolution,  and an additional thumbnail tile (resized to 512x512), so up to 3328 tokens per single image. We recommend using images of up to 2048x1536 (3 megapixels) resolution.

**Languages covered**: 

* English   
* Portuguese   
* Italian   
* French   
* German   
* Spanish 

**Context Length**: 32k.

**Safety Guardrails**

Similar to Cohere Labs Command A, Cohere Labs Command A Vision can be configured with two safety modes, which enable users to set guardrails that are both safe and suitable to their needs: contextual mode, or strict mode. Contextual mode is appropriate for wide-ranging interactions with fewer constraints on output, while maintaining core protections by rejecting harmful or illegal suggestions. Command A Vision is configured to contextual mode by default. Strict mode aims to avoid all sensitive topics, such as violent or sexual acts and profanity. For more information, see the [Command A prompt format docs](https://docs.cohere.com/docs/command-a-hf).

## **Model Card Contact**

For errors or additional questions about details in this model card, contact \[labs@cohere.com\].

## **Terms of Use:**

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant 112 billion parameter model to researchers all over the world. This model is governed by a [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license) License (Non-Commercial) with an acceptable use addendum, *and also requires adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)*. If you are interested in commercial use, please contact [Cohere’s Sales team](https://cohere.com/contact-sales).

## **Try it now:**

You can try Command A Vision in the playground [here](https://dashboard.cohere.com/playground/chat?model=command-a-vision-07-2025). You can also use it in our dedicated Hugging Face Space [here](https://huggingface.co/spaces/CohereLabs/command-a-vision).