---
language:
- multilingual
- pl
- en
- sq
- bel
- bs
- bg
- hr
- cs
- da
- et
- fi
- fr
- el
- es
- is
- lt
- nl
- de
- no
- pt
- ru
- ro
- sr
- hbs
- sv
- sk
- sl
- tr
- uk
- hu
- it
- lv
license: apache-2.0
library_name: transformers
tags:
- finetuned
- gguf
inference: false
pipeline_tag: text-generation
base_model: speakleash/Bielik-11B-v3.0-Instruct
---

<p align="center">
  <img src="https://huggingface.co/speakleash/Bielik-11B-v2/raw/main/speakleash_cyfronet.png">
</p>

# Bielik-11B-v3.0-Instruct-AWQ

This repo contains AWQ format model files for [SpeakLeash](https://speakleash.org/)'s [Bielik-11B-v3.0-Instruct](https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct).

<b><u>DISCLAIMER: Be aware that quantised models show reduced response quality and possible hallucinations!</u></b><br>


### Model description:

* **Developed by:** [SpeakLeash](https://speakleash.org/) & [ACK Cyfronet AGH](https://www.cyfronet.pl/)
* **Language:** Multilingual (32 European languages, optimized for Polish)
* **Model type:** causal decoder-only
* **Quant from:** [Bielik-11B-v3.0-Instruct](https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct)
* **Finetuned from:** [speakleash/Bielik-11B-v3-Base-20250730](https://huggingface.co/speakleash/Bielik-11B-v3-Base-20250730)
* **License:** Apache 2.0 and [Terms of Use](https://bielik.ai/terms/)

### Responsible for model quantization  
* [Remigiusz Kinas](https://www.linkedin.com/in/remigiusz-kinas/)<sup>SpeakLeash</sup> - team leadership, conceptualizing, calibration data preparation, process creation and quantized model delivery.

## Contact Us

If you have any questions or suggestions, please use the discussion tab. If you want to contact us directly, join our [Discord SpeakLeash](https://discord.gg/CPBxPce4).