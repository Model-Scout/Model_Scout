---
library_name: llama-cpp
tags:
  - translation
  - llama-cpp
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
base_model: yanolja/YanoljaNEXT-Rosetta-27B-2511
---

# YanoljaNEXT-Rosetta-27B-2511

<p style="text-align: center; margin: 0 auto 64px">
  <img src="next_rosetta.png" style="width: 1096px">
</p>

This model is a fine-tuned version of [`google/gemma-3-27b-pt`](https://huggingface.co/google/gemma-3-27b-pt). As it is intended solely for text generation, we have extracted and utilized only the `Gemma3ForCausalLM` component from the original architecture.

Unlike our previous EEVE models, this model does not feature an expanded tokenizer.

- **Model Name:** `yanolja/YanoljaNEXT-Rosetta-27B-2511`
- **Base Model:** `google/gemma-3-27b-pt`

## GGUF files

This folder contains ready-to-run GGUF files for llama.cpp.

- Quantized variants (choose one based on your device and quality needs):
  - K-family: `Q2_K`, `Q2_K_S`, `Q3_K_{S,M}`, `Q4_K_{S,M}`, `Q5_K_{S,M}`, `Q6_K`, `Q8_0`
  - IQ-family: `IQ1_{S,M}`, `IQ2_{XXS,XS,S,M}`, `IQ3_{XXS,XS,S,M}`, `IQ4_{XS,NL}`
- `_IMX` variants are produced with an activation matrix (`imatrix.gguf`) and often offer better quality at the same size. Some lower-precision types may be IMX-only.

## Model Description

This model is a 27-billion parameter, decoder-only language model built on the Gemma3 architecture and fine-tuned by Yanolja NEXT. It is specifically designed to translate structured data (JSON, YAML, XML formats) while preserving the original data structure.

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

Use a recent build of `llama.cpp` that supports Gemma 3 models. Pick any GGUF file from this folder (a quantized variant is recommended for most users).

```bash
# Example: use a Q5_K_M quantized file (adjust the path/model to your choice)
MODEL="path/to/YanoljaNEXT-Rosetta-27B-2511-q5_k_m.gguf"

# Build a formatted prompt using the included chat template roles
# (see release/YanoljaNEXT-Rosetta-27B-2511/chat_template.jinja)
read -r -d '' PROMPT <<'EOT'
<start_of_turn>instruction
Translate the user's text to Korean. Keep the JSON structure and keys.
Context: Simple introduction about a tech company.
Tone: Informative and helpful
Glossary:
- Yanolja NEXT -> 야놀자넥스트
- travel industry -> 여행 산업
Provide the final translation immediately without any other text.
<end_of_turn>
<start_of_turn>source
{"company_name": "Yanolja NEXT", "description": "Yanolja NEXT is a company that provides cutting-edge technology for the global travel industry."}
<end_of_turn>
<start_of_turn>translation\n
EOT

# Run llama.cpp (adjust -n/-c/--temp as needed)
llama-cli -m "$MODEL" -p "$PROMPT" -n 64 -c 4096 --temp 0.7 -no-cnv
```

### REST server

```bash
MODEL="path/to/YanoljaNEXT-Rosetta-27B-2511-q5_k_m.gguf"
llama-server -m "$MODEL" -c 4096 --host 0.0.0.0 --port 8080
```

### LM Studio / other GUIs

Import any of the `.gguf` files into your GUI of choice (LM Studio, KoboldCPP, text-generation-webui) and select chat mode. The embedded template in the GGUF will be used automatically by recent tools.

The model outputs the final translation in the same structured format as the input (JSON, YAML, XML) when appropriate, or plain text for simple translations.

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
| **yanolja/YanoljaNEXT-Rosetta-12B-2510** | **37.36** |
| **yanolja/YanoljaNEXT-Rosetta-27B-2511** | **37.21** |
| openai/gpt-4o                       | 36.08     |
| google/gemini-2.5-flash             | 35.25     |
| tencent/Hunyuan-MT-7B               | 34.76     |
| **yanolja/YanoljaNEXT-Rosetta-12B** | **34.75** |
| yanolja/YanoljaNEXT-Rosetta-20B     | 33.87        |
| AIDC-AI/Marco-MT-Algharb            | 33.40        |
| openai/gpt-oss-120b                 | 31.51        |
| ByteDance-Seed/Seed-X-PPO-7B        | 30.48        |
| google/gemma-3-27b-it               |        30.05 |
| google/gemma-3-12b-it               |        29.31 |

YanoljaNEXT-Rosetta-27B-2511 achieves strong translation quality while maintaining efficient inference for its parameter size.
Scores for the other language pairs can be found in the [WMT24++ Evaluation Results](wmt24pp_12b.md).

## Intended Uses & Limitations

This model is intended for translating structured data (JSON, YAML, XML formats) while preserving the original structure. It is particularly well-suited for tasks such as localizing product catalogs, translating hotel reviews, or handling any other structured content that requires accurate translation.

### Limitations
The model is primarily optimized for processing structured data (JSON, YAML, XML).
Its performance on unstructured text or other data formats may vary.
In some cases, the model may produce invalid structured outputs, repetitive output, or inaccurate translations.

### License
This model is released under the Gemma license, inherited from its base architecture. Please consult the official [Gemma license terms](https://ai.google.dev/gemma/terms) for detailed usage guidelines.

## Acknowledgments
This work was supported by the Korea Creative Content Agency (KOCCA) grant, funded by the Ministry of Culture, Sports and Tourism (MCST) in 2025 (Project Name: _Cultivating Masters and Doctoral Experts to Lead Digital-Tech Tourism_, Project Number: RS-2024-00442006, Contribution Rate: 100%).

## Citation

If you use this model, please consider citing:

```
@misc{yanolja2025yanoljanextrosetta27b,
  author = {Yanolja NEXT Co., Ltd.},
  title = {YanoljaNEXT-Rosetta-27B-2511},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\\url{https://huggingface.co/yanolja/YanoljaNEXT-Rosetta-27B-2511}}
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