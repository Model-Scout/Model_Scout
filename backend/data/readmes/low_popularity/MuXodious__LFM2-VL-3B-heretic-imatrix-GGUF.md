---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ja
- fr
- es
- de
- it
- pt
- ar
- zh
- ko
pipeline_tag: image-text-to-text
tags:
- liquid
- lfm2
- lfm2-vl
- edge
- heretic
- uncensored
- decensored
- abliterated
base_model_relation: quantized
base_model:
- pszemraj/LFM2-VL-3B-heretic
---
iMatrix GGUF quants of https://huggingface.co/pszemraj/LFM2-VL-3B-heretic generated using [ubergarm's imatrix-calibration-corpus-v02](https://gist.github.com/ubergarm/edfeb3ff9c6ec8b49e88cdf627b0711a) dataset.

MMPROJ files can be found in the [static quant repo](https://huggingface.co/MuXodious/LFM2-VL-3B-heretic-GGUF).

iMatrix stats: PPL = 7.9876 +/- 0.04865

# This is a decensored version of [LiquidAI/LFM2-VL-3B](https://huggingface.co/LiquidAI/LFM2-VL-3B), made using [Heretic](https://github.com/p-e-w/heretic) v1.0.1

## Abliteration parameters

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | per layer |
| **attn.o_proj.max_weight** | 1.78 |
| **attn.o_proj.max_weight_position** | 20.88 |
| **attn.o_proj.min_weight** | 1.52 |
| **attn.o_proj.min_weight_distance** | 12.07 |
| **conv.out_proj.max_weight** | 1.01 |
| **conv.out_proj.max_weight_position** | 21.66 |
| **conv.out_proj.min_weight** | 0.13 |
| **conv.out_proj.min_weight_distance** | 4.90 |
| **mlp.down_proj.max_weight** | 1.16 |
| **mlp.down_proj.max_weight_position** | 20.83 |
| **mlp.down_proj.min_weight** | 0.29 |
| **mlp.down_proj.min_weight_distance** | 1.03 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM2-VL-3B](https://huggingface.co/LiquidAI/LFM2-VL-3B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.02 | 0 *(by definition)* |
| **Refusals** | 4/100 | 87/100 |


```
? Which trial do you want to use? (Use arrow keys)
 » [Trial 251] Refusals:  0/100, KL divergence: 0.08
   [Trial 386] Refusals:  1/100, KL divergence: 0.03
   [Trial 277] Refusals:  2/100, KL divergence: 0.03
   [Trial 389] Refusals:  3/100, KL divergence: 0.03
   -->[Trial 323] Refusals:  4/100, KL divergence: 0.02<--
   [Trial 324] Refusals:  6/100, KL divergence: 0.02
   [Trial 220] Refusals:  7/100, KL divergence: 0.02
   [Trial 357] Refusals:  8/100, KL divergence: 0.02
   [Trial 316] Refusals: 10/100, KL divergence: 0.01
   [Trial 230] Refusals: 12/100, KL divergence: 0.01
   [Trial 234] Refusals: 18/100, KL divergence: 0.01
   [Trial 379] Refusals: 27/100, KL divergence: 0.01
   [Trial 336] Refusals: 34/100, KL divergence: 0.01
   [Trial 345] Refusals: 35/100, KL divergence: 0.01
   [Trial 248] Refusals: 40/100, KL divergence: 0.01
   [Trial 398] Refusals: 60/100, KL divergence: 0.00
   [Trial 380] Refusals: 64/100, KL divergence: 0.00
   [Trial 363] Refusals: 66/100, KL divergence: 0.00
   [Trial 155] Refusals: 69/100, KL divergence: 0.00
   [Trial 310] Refusals: 70/100, KL divergence: 0.00
```


-----


<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/7_6D7rWrLxp2hb6OHSV1p.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 66%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
</center>

# LFM2‑VL

**LFM2-VL-3B** is the newest and most capable model in [Liquid AI](https://www.liquid.ai/)'s multimodal **LFM2-VL** series, designed to process text and images with variable resolutions.  
Built on the [LFM2](https://huggingface.co/collections/LiquidAI/lfm2-686d721927015b2ad73eaa38) backbone, it extends the architecture for higher-capacity reasoning and stronger visual understanding while retaining efficiency.  

We are releasing the weights of the new [3B](https://huggingface.co/LiquidAI/LFM2-VL-3B) checkpoint—offering higher performance across benchmarks while remaining optimized for scalable deployment.

* **Competitive multimodal performance** among lightweight open models.
* **Enhanced visual understanding and reasoning**, particularly on fine-grained perception tasks
* **Retains efficient inference** with the same flexible architecture and user-tunable speed-quality tradeoffs  
* **Processes native resolutions up to 512×512** with intelligent patch-based handling for larger inputs  

For more details, see the [LFM2-VL-3B post](https://www.liquid.ai/blog/lfm2-vl-3b-a-new-efficient-vision-language-for-the-edge) and the [LFM2 blog post](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models).

## 📄 Model details

Due to their small size, **we recommend fine-tuning LFM2-VL models on narrow use cases** to maximize performance. 
They were trained for instruction following and lightweight agentic flows. 
Not intended for safety‑critical decisions.

| Property | [**LFM2-VL-450M**](https://huggingface.co/LiquidAI/LFM2-VL-450M) | [**LFM2-VL-1.6B**](https://huggingface.co/LiquidAI/LFM2-VL-1.6B) | [**LFM2-VL-3B**](https://huggingface.co/LiquidAI/LFM2-VL-3B) |
|---|---:|---:|---:|
| **Parameters (LM only)** | 350M | 1.2B | 2.6B |
| **Vision encoder** | SigLIP2 NaFlex base (86M) | SigLIP2 NaFlex shape-optimized (400M) | SigLIP2 NaFlex large (400M) |
| **Backbone layers** | hybrid conv+attention | hybrid conv+attention | hybrid conv+attention |
| **Context (text)** | 32,768 tokens | 32,768 tokens | 32,768 tokens |
| **Image tokens** | dynamic, user-tunable | dynamic, user-tunable | dynamic, user-tunable |
| **Vocab size** | 65,536 | 65,536 | 65,536 |
| **Precision** | bfloat16 | bfloat16 | bfloat16 |
| **License** | LFM Open License v1.0 | LFM Open License v1.0 | LFM Open License v1.0 |

**Supported languages:** English

**Generation parameters**: We recommend the following parameters:
- Text: `temperature=0.1`, `min_p=0.15`, `repetition_penalty=1.05`
- Vision: `min_image_tokens=64` `max_image_tokens=256`, `do_image_splitting=True`

**Chat template**: LFM2-VL uses a ChatML-like chat template as follows:  

```
<|startoftext|><|im_start|>system
You are a helpful multimodal assistant by Liquid AI.<|im_end|>
<|im_start|>user
<image>Describe this image.<|im_end|>
<|im_start|>assistant
This image shows a Caenorhabditis elegans (C. elegans) nematode.<|im_end|>
```

Images are referenced with a sentinel (`<image>`), which is automatically replaced with the image tokens by the processor.

You can apply it using the dedicated [`.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#applychattemplate) function from Hugging Face transformers.

**Architecture**
- **Hybrid backbone**: Language model tower (LFM2-2.6B) paired with SigLIP2 NaFlex vision encoders (400M shape-optimized)
- **Native resolution processing**: Handles images up to 512×512 pixels without upscaling and preserves non-standard aspect ratios without distortion
- **Tiling strategy**: Splits large images into non-overlapping 512×512 patches and includes thumbnail encoding for global context
- **Efficient token mapping**: 2-layer MLP connector with pixel unshuffle reduces image tokens (e.g., 256×384 image → 96 tokens, 1000×3000 → 1,020 tokens)
- **Inference-time flexibility**: User-tunable maximum image tokens and patch count for speed/quality tradeoff without retraining

**Training approach**
- Builds on the LFM2 base model with joint mid-training that fuses vision and language capabilities using a gradually adjusted text-to-image ratio
- Applies joint SFT with emphasis on image understanding and vision tasks
- Leverages large-scale open-source datasets combined with in-house synthetic vision data, selected for balanced task coverage
- Follows a progressive training strategy: base model → joint mid-training → supervised fine-tuning

## 🏃 How to run LFM2-VL

You can run LFM2-VL with Hugging Face [`transformers`](https://github.com/huggingface/transformers) via installing Transformers from source as follows:

```bash
pip install git+https://github.com/huggingface/transformers.git@87be5595081364ef99393feeaa60d71db3652679 pillow
```

Here is an example of how to generate an answer with transformers in Python:

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
from transformers.image_utils import load_image

# Load model and processor
model_id = "LiquidAI/LFM2-VL-3B"
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    device_map="auto",
    dtype="bfloat16"
)
processor = AutoProcessor.from_pretrained(model_id)

# Load image and create conversation
url = "https://www.ilankelman.org/stopsigns/australia.jpg"
image = load_image(url)
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": "What is in this image?"},
        ],
    },
]

# Generate Answer
inputs = processor.apply_chat_template(
    conversation,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
    tokenize=True,
).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=64)
processor.batch_decode(outputs, skip_special_tokens=True)[0]

# This image captures a vibrant street scene in a Chinatown area. The focal point is a large red Chinese archway with gold and black accents, adorned with Chinese characters. Flanking the archway are two white stone lion statues, which are traditional guardians in Chinese culture.
```

You can directly run and test the model with this [Colab notebook](https://colab.research.google.com/drive/11EMJhcVB6OTEuv--OePyGK86k-38WU3q?usp=sharing).


## 🔧 How to fine-tune

We recommend fine-tuning LFM2-VL models on your use cases to maximize performance.

| Notebook  | Description                                                          | Link |
|-----------|----------------------------------------------------------------------|------|
| SFT (TRL) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using TRL. | <a href="https://colab.research.google.com/drive/1csXCLwJx7wI7aruudBp6ZIcnqfv8EMYN?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |


## 📈 Performance

| Model             | Average | MMStar | RealWorldQA | MM-IFEval | BLINK | MMBench (dev en) | OCRBench | POPE  |
|-------------------|----------|--------|--------------|------------|--------|------------------|-----------|-------|
| InternVL3_5-2B    | 66.50    | 57.67  | 60.78        | 47.31      | 50.97  | 78.18            | 834.00    | 87.17 |
| Qwen2.5-VL-3B     | 65.42    | 56.13  | 65.23        | 38.62      | 48.97  | 80.41            | 824.00    | 86.17 |
| InternVL3-2B      | 67.44    | 61.10  | 65.10        | 38.49      | 53.10  | 81.10            | 831.00    | 90.10 |
| SmolVLM2-2.2B     | 56.01    | 46.00  | 57.50        | 19.42      | 42.30  | 69.24            | 725.00    | 85.10 |
| LFM2-VL-3B        | 69.00    | 57.73  | 71.37        | 51.83      | 51.03  | 79.81            | 822.00    | 89.01 |

More benchmark scores are reported in our [LFM2-VL-3B post](https://www.liquid.ai/blog/lfm2-vl-3b-a-new-efficient-vision-language-for-the-edge). We obtained the scores for competitive models using VLMEvalKit. Qwen3-VL-2B is not listed in the results table, as its release occurred the day before.

## 📬 Contact

If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).