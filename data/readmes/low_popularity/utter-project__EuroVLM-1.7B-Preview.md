---
license: apache-2.0
language:
- en
- de
- es
- fr
- it
- pt
- pl
- nl
- tr
- sv
- cs
- el
- hu
- ro
- fi
- uk
- sl
- sk
- da
- lt
- lv
- et
- bg
- 'no'
- ca
- hr
- ga
- mt
- gl
- zh
- ru
- ko
- ja
- ar
- hi
library_name: transformers
---

# Model Card for EuroVLM-1.7B-Instruct

**⚠️ PREVIEW RELEASE**: *This is a preview version of EuroVLM-1.7B. The model is still under development and may have limitations in performance and stability. Use with caution in production environments.*

This is the model card for EuroVLM-1.7B-Preview, a multimodal vision-language model based on long-context version of EuroLLM-1.7B.

- **Developed by:** Unbabel, Instituto Superior Técnico, Instituto de Telecomunicações, University of Edinburgh, Aveni, University of Paris-Saclay, University of Amsterdam, Naver Labs, Sorbonne Université.
- **Funded by:** European Union.
- **Model type:** A 1.7B+400M parameter multilingual multimodal transformer VLM (Vision-Language Model).
- **Language(s) (NLP):** Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, and Ukrainian.
- **Modalities:** Text and Vision (images).
- **License:** Apache License 2.0.

## Model Details

EuroVLM-1.7B is a 1.7B+400M parameter vision-language model that combines the multilingual capabilities of EuroLLM-1.7B with vision encoding components.

EuroVLM-1.7B was (visually) instruction tuned on a combination of multilingual vision-language datasets, including image captioning, visual question answering, and multimodal reasoning tasks across the supported languages.

### Model Description

EuroVLM uses a multimodal architecture combining a vision encoder with the EuroLLM language model:

**Language Model Component:**
- Based on the standard, dense Transformer architecture from EuroLLM-1.7B
- Grouped query attention (GQA) with 8 key-value heads for efficient inference
- Pre-layer normalization with RMSNorm for training stability
- SwiGLU activation function for optimal downstream performance
- Rotary positional embeddings (RoPE) in every layer
- Extended context size supporting up to 32K tokens

**Vision Component:**
- Vision Transformer (ViT) encoder, based on [google/siglip2-so400m-patch14-384](https://huggingface.co/google/siglip2-so400m-patch14-384)
- Multimodal projector mapping vision representations to token embeddings
- Support for high-resolution image inputs

## Run the model

To use the model with HuggingFace's [Transformers](https://huggingface.co/docs/transformers/en/index) library
    
```python
from PIL import Image
from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
    
model_id = "utter-project/EuroVLM-1.7B-Preview"
processor = LlavaNextProcessor.from_pretrained(model_id)
model = LlavaNextForConditionalGeneration.from_pretrained(model_id)

# Load an image
image = Image.open("/path/to/image.jpg")
    
messages = [
    {
        "role": "system",
        "content": "You are EuroVLM --- a multimodal AI assistant specialized in European languages that provides safe, educational and helpful answers about images and text.",
    },
    {
        "role": "user", 
        "content": [
            {"type": "image"},
            {"type": "text", "text": "What do you see in this image? Please describe it in Portuguese."}
        ]
    },
]

prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(images=image, text=prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=1024)
print(processor.decode(outputs[0], skip_special_tokens=True))
```

You can also run EuroVLM with [vLLM](https://docs.vllm.ai/en/latest/)!

```python
from vllm import LLM, SamplingParams

# Initialize the model
model_id = "utter-project/EuroVLM-1.7B-Preview"
llm = LLM(model=model_id)

# Set up sampling parameters
sampling_params = SamplingParams(temperature=0.7, max_tokens=1024)

# Image and prompt
image_url = "/url/of/image.jpg"

messages = [
    {
        "role": "system",
        "content": "You are EuroVLM --- a multimodal AI assistant specialized in European languages that provides safe, educational and helpful answers about images and text.",
    },
    {
        "role": "user", 
        "content": [
            {"type": "image_url", "image_url": {"url": image_url}},
            {"type": "text", "text": "What do you see in this image? Please describe it in Portuguese in one sentence."}
        ]
    },
]

# Generate response
outputs = llm.chat(messages, sampling_params=sampling_params)
print(outputs[0].outputs[0].text)
```

## Capabilities

EuroVLM-1.7B-Instruct supports a wide range of vision-language tasks across multiple languages:

- **Multilingual Image Captioning:** Generate detailed descriptions of images in any of the supported languages
- **Visual Question Answering:** Answer questions about image content in multilingual contexts
- **Visual Instruction Following:** Execute complex instructions that involve both visual analysis and text generation
- **Multimodal Translation:** Translate image captions and descriptions between supported languages
- **Document Understanding:** Process and analyze documents, charts, and diagrams with multilingual text

## Bias, Risks, and Limitations

EuroVLM-1.7B has not been fully aligned to human preferences, so the model may generate problematic outputs in both text and image understanding contexts (e.g., hallucinations about image content, harmful content, biased interpretations, or false statements about visual information). 

Additional considerations for multimodal models include:
- Potential biases in visual interpretation across different cultural contexts
- Limitations in understanding complex visual scenes or unusual image compositions  
- Possible inconsistencies between visual understanding and textual generation across languages
- Privacy considerations when processing images that may contain personal information

Users should exercise caution and implement appropriate safety measures when deploying this model in production environments.