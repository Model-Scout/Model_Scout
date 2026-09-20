---
language:
- en
- ko
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
- llama-3-ko
license: llama3
license_name: llama3
license_link: https://llama.meta.com/llama3/license
---

- Original model is [beomi/Llama-3-Open-Ko-8B](https://huggingface.co/beomi/Llama-3-Open-Ko-8B)
- quantized using [llama.cpp](https://github.com/ggerganov/llama.cpp)


## Ollama

Modelfile

```
FROM Llama-3-Open-Ko-8B-Q8_0.gguf

TEMPLATE """{{- if .System }}
<s>{{ .System }}</s>
{{- end }}
<s>Human:
{{ .Prompt }}</s>
<s>Assistant:
"""

SYSTEM """A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."""

PARAMETER temperature 0
PARAMETER num_predict 3000
PARAMETER num_ctx 4096
PARAMETER stop <s>
PARAMETER stop </s>
```


> Update @ 2024.04.24: Release Llama-3-Open-Ko-8B model & [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview)

## Model Details

**Llama-3-Open-Ko-8B**

The Llama-3-Open-Ko-8B model is a continued pretrained language model based on the Llama-3-8B framework. This model is trained with over 60GB of deduplicated texts sourced from publicly available resources. With the new Llama-3 tokenizer, the model has been pretrained with more than 17.7B tokens, which is slightly more than that processed by the Korean tokenizer of Llama-2. Training was conducted on a TPUv5e-256, supported by Google's TRC program.

**Llama-3-Open-Ko-8B-Instruct-preview**

The Instruction model, named Llama-3-Open-Ko-8B-Instruct-preview, incorporates concepts from the [Chat Vector paper](https://arxiv.org/abs/2310.04799). This model is a preview and has not been fine-tuned with any Korean instruction set, making it a strong starting point for developing new chat and instruct models.

**Meta Llama-3**

Developed and released by Meta, the Meta Llama 3 family of large language models (LLMs) are optimized for dialogue use cases and excel across common industry benchmarks, emphasizing helpfulness and safety. 

**Model Developers**: Junbum Lee (Beomi)

**Variations**: Llama-3-Open-Ko is available in one configuration — 8B.

**Input/Output**: Models accept text input and generate text and code.

**Model Architecture**: Llama 3 utilizes an optimized transformer architecture.

<table>
  <tr>
   <td>
   </td>
   <td><strong>Training Data</strong>
   </td>
   <td><strong>Params</strong>
   </td>
   <td><strong>Context length</strong>
   </td>
   <td><strong>GQA</strong>
   </td>
   <td><strong>Token count</strong>
   </td>
   <td><strong>Knowledge cutoff</strong>
   </td>
  </tr>
  <tr>
   <td rowspan="2" >Llama-3-Open-Ko
   </td>
   <td rowspan="2" >Same as Open-Solar-Ko Dataset
   </td>
   <td>8B
   </td>
   <td>8k
   </td>
   <td>Yes
   </td>
   <td rowspan="2" >17.7B+
   </td>
   <td>Jun, 2023
   </td>
  </tr>
</table>

*Dataset list available [here](https://huggingface.co/beomi/OPEN-SOLAR-KO-10.7B/tree/main/corpus)

## Intended Use

**Commercial and Research Applications**: Llama 3 is designed for use in English, tailored for assistant-like chat in its instruction-tuned models, while the pretrained models are versatile across various natural language generation tasks.

**Out-of-scope**: Any use violating applicable laws, regulations, or the Acceptable Use Policy and Llama 3 Community License is prohibited.

### Responsibility & Safety

Meta's commitment to Responsible AI includes steps to limit misuse and harm while supporting the open source community. Developers are encouraged to implement safety best practices and use resources like [Meta Llama Guard 2](https://llama.meta.com/purple-llama/) and [Code Shield](https://llama.meta.com/purple-llama/) to tailor safety needs specifically to their use cases.

#### Responsible Release

Following a rigorous process against misuse, we ensure all safety and ethical guidelines are adhered to, as detailed in our [Responsible Use Guide](https://llama.meta.com/responsible-use-guide/).

## Ethical Considerations and Limitations

Llama 3 is built on the principles of openness, inclusivity, and helpfulness, designed to be accessible and valuable across diverse backgrounds and use cases. Developers should undertake thorough safety testing and tuning for specific applications before deployment.


## Citation instructions

**Llama-3-Open-Ko**

```
@article{llama3openko,
  title={Llama-3-Open-Ko},
  author={L, Junbum},
  year={2024},
  url={https://huggingface.co/beomi/Llama-3-Open-Ko-8B}
}
```

**Original Llama-3**

```
@article{llama3modelcard,
  title={Llama 3 Model Card},
  author={AI@Meta},
  year={2024},
  url = {https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md}
}
```
