---
base_model: CohereForAI/aya-vision-8b
inference: false
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
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
---

# Model Card for Aya Vision 8B

<img src="aya-vision-8B.png" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

**C4AI Aya Vision 8B** is an open weights research release of an 8-billion parameter model with advanced capabilities optimized for a variety of vision-language use cases, including OCR, captioning, visual reasoning, summarization, question answering, code, and more. 
It is a multilingual model trained to excel in 23 languages in vision and language.

This model card corresponds to the 8-billion version of the Aya Vision model. We also released a 32-billion version which you can find [here](https://huggingface.co/CohereForAI/aya-vision-32B).

- Developed by: [Cohere For AI](https://cohere.for.ai/) 
- Point of Contact: Cohere For AI: [cohere.for.ai](https://cohere.for.ai/)
- License: [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license), requires also adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)
- Model: c4ai-aya-vision-8b
- Model Size: 8 billion parameters
- Context length: 16K

## Try it: Aya Vision in Action

Before downloading the weights, you can try Aya Vision chat in the [Cohere playground](https://dashboard.cohere.com/playground/chat) or our dedicated [Hugging Face Space](https://huggingface.co/spaces/CohereForAI/aya_expanse) for interactive exploration.

## WhatsApp Integration

You can also talk to Aya Vision through the popular messaging service WhatsApp. Use this [link](https://wa.me/14313028498) to open a WhatsApp chatbox with Aya Vision.

If you don’t have WhatsApp downloaded on your machine you might need to do that, or, if you have it on your phone, you can follow the on-screen instructions to link your phone and WhatsApp Web. 
By the end, you should see a text window which you can use to chat with the model. 
More details about our WhatsApp integration are available [here](https://docs.cohere.com/v2/docs/aya#aya-expanse-integration-with-whatsapp).

## Example Notebook

You can also check out the following [notebook](https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/aya_vision_intro.ipynb) to understand how to use Aya Vision for different use cases.

## How to Use Aya Vision

Please install `transformers` from the source repository that includes the necessary changes for this model:

```python
# pip install 'git+https://github.com/huggingface/transformers.git@v4.49.0-AyaVision'
from transformers import AutoProcessor, AutoModelForImageTextToText
import torch

model_id = "CohereForAI/aya-vision-8b"

processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id, device_map="auto", torch_dtype=torch.float16
)

# Format message with the aya-vision chat template
messages = [
    {"role": "user",
     "content": [
       {"type": "image", "url": "https://pbs.twimg.com/media/Fx7YvfQWYAIp6rZ?format=jpg&name=medium"},
        {"type": "text", "text": "चित्र में लिखा पाठ क्या कहता है?"},
    ]},
    ]

inputs = processor.apply_chat_template(
    messages, padding=True, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt"
).to(model.device)

gen_tokens = model.generate(
    **inputs, 
    max_new_tokens=300, 
    do_sample=True, 
    temperature=0.3,
)

print(processor.tokenizer.decode(gen_tokens[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
```


You can also use the model directly using transformers `pipeline` abstraction:

```python
from transformers import pipeline

pipe = pipeline(model="CohereForAI/aya-vision-8b", task="image-text-to-text", device_map="auto")

# Format message with the aya-vision chat template
messages = [
    {"role": "user",
     "content": [
       {"type": "image", "url": "https://media.istockphoto.com/id/458012057/photo/istanbul-turkey.jpg?s=612x612&w=0&k=20&c=qogAOVvkpfUyqLUMr_XJQyq-HkACXyYUSZbKhBlPrxo="},
        {"type": "text", "text": "Bu resimde hangi anıt gösterilmektedir?"},
    ]},
    ]
outputs = pipe(text=messages, max_new_tokens=300, return_full_text=False)

print(outputs)
```

## Model Details

**Input:** Model accepts input text and images.

**Output:** Model generates text.

**Model Architecture:** This is a vision-language model that uses a multilingual language model based on [C4AI Command R7B](https://huggingface.co/CohereForAI/c4ai-command-r7b-12-2024) and further post-trained with the [Aya Expanse recipe](https://arxiv.org/abs/2412.04261), paired with [SigLIP2-patch14-384](https://huggingface.co/google/siglip2-so400m-patch14-384) vision encoder through a multimodal adapter for vision-language understanding.

**Image Processing:** We use **169 visual tokens** to encode an image tile with a resolution of **364x364 pixels**. Input images of arbitrary sizes are mapped to the nearest supported resolution based on the aspect ratio. Aya Vision uses up to 12 input tiles and a thumbnail (resized to 364x364)  (2197 image tokens).

**Languages covered:** The model has been trained on 23 languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, Chinese (Simplified and Traditional), Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.

**Context length**: Aya Vision 8B supports a context length of 16K.

For more details about how the model was trained, check out [our blogpost](https://huggingface.co/blog/aya-vision).


## Evaluation

We evaluated Aya Vision 8B against [Pangea 7B](https://huggingface.co/neulab/Pangea-7B), [Llama-3.2 11B Vision](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision), [Molmo-D 7B](https://huggingface.co/allenai/Molmo-7B-D-0924), [Qwen2.5-VL 7B](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct), [Pixtral 12B](https://huggingface.co/mistralai/Pixtral-12B-2409), and [Gemini Flash 1.5 8B](https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/) using [Aya Vision Benchmark](https://huggingface.co/datasets/CohereForAI/AyaVisionBench) and [m-WildVision](https://huggingface.co/datasets/CohereForAI/m-WildVision). 
Win-rates were determined using claude-3-7-sonnet-20250219 as a judge, based on the superior judge performance compared to other models. 

We also evaluated Aya Vision 8B’s performance for text-only input against the same models using [m-ArenaHard](https://huggingface.co/datasets/CohereForAI/m-ArenaHard), a challenging open-ended generation evaluation, measured using win-rates using gpt-4o-2024-11-20 as a judge. 

<!-- <img src="Aya_Vision_8B_Combined_Win_Rates.png" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/> -->
<img src="AyaVision8BWinRates(AyaVisionBench).png"  width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
<img src="AyaVision8BWinRates(m-WildVision).png"  width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
<img src="Aya_Vision_8BvsPangea(AyaVisionBench).png" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
<img src="EfficiencyvsPerformance.png"  width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


### Model Card Contact

For errors or additional questions about details in this model card, contact info@for.ai.

### Terms of Use

We hope that the release of this model will make community-based research efforts more accessible by releasing the weights of a highly performant 8 billion parameter Vision-Language Model to researchers all over the world. 

This model is governed by a [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license) License with an acceptable use addendum, and also requires adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy).