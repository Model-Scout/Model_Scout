---
library_name: transformers
tags:
  - translation
license: gemma
language:
  - ar
  - bg
  - zh
  - cs
  - da
  - nl
  - en
  - fi
  - fr
  - de
  - el
  - gu
  - he
  - hi
  - hu
  - id
  - it
  - ja
  - ko
  - fa
  - pl
  - pt
  - ro
  - ru
  - sk
  - es
  - sv
  - tl
  - th
  - tr
  - uk
  - vi
---

# YanoljaNEXT-Rosetta-12B-2510

<p style="text-align: center; margin: 0 auto 64px">
  <img src="next_rosetta.png" style="width: 1096px">
</p>

This model is a fine-tuned version of [`google/gemma-3-12b-pt`](https://huggingface.co/google/gemma-3-12b-pt). As it is intended solely for text generation, we have extracted and utilized only the `Gemma3ForCausalLM` component from the original architecture.

Unlike our previous EEVE models, this model does not feature an expanded tokenizer.

- **Model Name:** `yanolja/YanoljaNEXT-Rosetta-12B-2510`
- **Base Model:** `google/gemma-3-12b-pt`

## Model Description

This model is a 12-billion parameter, decoder-only language model built on the Gemma3 architecture and fine-tuned by Yanolja NEXT. It is specifically designed to translate structured data (JSON format) while preserving the original data structure.

The model was trained on a multilingual dataset covering the following languages equally:
- Arabic
- Bulgarian
- Chinese
- Czech
- Danish
- Dutch
- English
- Finnish
- French
- German
- Greek
- Gujarati
- Hebrew
- Hindi
- Hungarian
- Indonesian
- Italian
- Japanese
- Korean
- Persian
- Polish
- Portuguese
- Romanian
- Russian
- Slovak
- Spanish
- Swedish
- Tagalog
- Thai
- Turkish
- Ukrainian
- Vietnamese

While optimized for these languages, it may also perform effectively on other languages supported by the base Gemma3 model.

## How to use

You can use this model with the `transformers` library as follows:

```python
import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "yanolja/YanoljaNEXT-Rosetta-12B-2510"
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
    max_memory={0: "47GB"},
)
tokenizer = AutoTokenizer.from_pretrained(model_id)

target_language = "Korean"
context = {
  "context": "Simple introduction about a tech company.",
  "tone": "Informative and helpful",
  "glossary": {
    "Yanolja NEXT": "야놀자넥스트",
    "travel industry": "여행 산업",
  }
}

system = [f"Translate the user's text to {target_language}."]
for key, value in context.items():
  key_pascal = key.capitalize()
  if isinstance(value, dict):
    system.append(f"{key_pascal}:")
    for f, t in value.items():
      system.append(f"- {f} -> {t}")
  else:
    system.append(f"{key_pascal}: {value}")

system.append("Provide the final translation immediately without any other text.")

source = {
  "company_name": "Yanolja NEXT",
  "description": "Yanolja NEXT is a company that provides cutting-edge "
                 "technology for the global travel industry.",
}

messages = [
    {"role": "system", "content": "\n".join(system)},
    {"role": "user", "content": json.dumps(source, ensure_ascii=False)},
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print(prompt)
# <bos><start_of_turn>instruction
# Translate the user's text to Korean.
# Context: Simple introduction about a tech company.
# Tone: Informative and helpful
# Glossary:
# - Yanolja NEXT -> 야놀자넥스트
# - travel industry -> 여행 산업
# Provide the final translation immediately without any other text.<end_of_turn>
# <start_of_turn>source
# {"company_name": "Yanolja NEXT", "description": "Yanolja NEXT is a company that provides cutting-edge technology for the global travel industry."}<end_of_turn>
# <start_of_turn>translation

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
input_length = inputs["input_ids"].shape[1]

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=64,
    )

generated_tokens = outputs[0][input_length:]
translation = tokenizer.decode(generated_tokens, skip_special_tokens=True)

print(json.dumps(json.loads(translation), indent=2, ensure_ascii=False))
# {
#   "company_name": "야놀자넥스트",
#   "description": "야놀자넥스트는 글로벌 여행 산업에 최첨단 기술을 제공하는 회사입니다."
# }
```

The model outputs the final translation in JSON format when appropriate, or plain text for simple translations.

## Training Procedure

### Training Data
The translation datasets were synthesized using fineweb corpora.
- [FineWeb Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)
- [FineWeb2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2)

The model was fine-tuned on synthetic multilingual translation data to optimize performance across the supported language pairs.

## Performance

### Translation Quality Benchmarks

The following CHrF++ scores (WMT24++) demonstrate the model's competitive performance compared to other state-of-the-art translation models on English to Korean translation:

| Model                              | CHrF++ Score (WMT24++) |
|------------------------------------|--------------|
| **yanolja/YanoljaNEXT-Rosetta-12B-2510**    | **37.36** |
| openai/gpt-4o  | 36.08 |
| google/gemini-2.5-flash            | 35.25 |
| **yanolja/YanoljaNEXT-Rosetta-12B**    | **34.75** |
| yanolja/YanoljaNEXT-Rosetta-20B    | 33.87        |
| google/gemini-2.0-flash-001        | 33.81        |
| openai/gpt-oss-120b                | 31.51        |
| google/gemma-3-27b-it              |        30.05 |
| google/gemma-3-12b-pt               |        29.31 |

YanoljaNEXT-Rosetta-12B-2510 achieves competitive translation quality while maintaining the efficiency of a 12B parameter model.
Scores for the other language pairs can be found in the [WMT24++ Evaluation Results](wmt24pp_12b.md).

## Intended Uses & Limitations

This model is intended for translating structured data (JSON format) while preserving the original structure. It is particularly well-suited for tasks such as localizing product catalogs, translating hotel reviews, or handling any other structured content that requires accurate translation.

### Limitations
The model is primarily optimized for processing JSON data.
Its performance on unstructured text or other data formats may vary.
In some cases, the model may produce invalid JSON, repetitive output, or inaccurate translations.

### License
This model is released under the Gemma license, inherited from its base model, [`google/gemma-3-12b-pt`](https://huggingface.co/google/gemma-3-12b-pt). Please consult the official [Gemma license terms](https://ai.google.dev/gemma/terms) for detailed usage guidelines.

## Acknowledgments
This work was supported by the Korea Creative Content Agency (KOCCA) grant, funded by the Ministry of Culture, Sports and Tourism (MCST) in 2025 (Project Name: _Cultivating Masters and Doctoral Experts to Lead Digital-Tech Tourism_, Project Number: RS-2024-00442006, Contribution Rate: 100%).

## Citation

If you use this model, please consider citing:

```
@misc{yanolja2025yanoljanextrosetta,
  author = {Yanolja NEXT Co., Ltd.},
  title = {YanoljaNEXT-Rosetta-12B-2510},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\\url{https://huggingface.co/yanolja/YanoljaNEXT-Rosetta-12B-2510}}
}
```

## References

This work utilizes several models and datasets. We would like to acknowledge the original authors for their valuable contributions to the field.

```
@misc{gemma3,
  author = {Google},
  title = {Gemma 3},
  year = {2024},
  publisher = {Google DeepMind},
  howpublished = {\\url{https://deepmind.google/models/gemma/gemma-3/}}
}

@misc{penedo2025fineweb2pipelinescale,
  title = {FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language}, 
  author = {Guilherme Penedo and Hynek Kydlíček and Vinko Sabolčec and Bettina Messmer and Negar Foroutan and Amir Hossein Kargaran and Colin Raffel and Martin Jaggi and Leandro Von Werra and Thomas Wolf},
  year = {2025},
  eprint = {2506.20920},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  url = {https://arxiv.org/abs/2506.20920},
}

@misc{lozhkov2024fineweb-edu,
  author = {Lozhkov, Anton and Ben Allal, Loubna and von Werra, Leandro and Wolf, Thomas},
  title = {FineWeb-Edu: the Finest Collection of Educational Content},
  year = 2024,
  url = {https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu},
  doi = {10.57967/hf/2497},
  publisher={Hugging Face}
}
```