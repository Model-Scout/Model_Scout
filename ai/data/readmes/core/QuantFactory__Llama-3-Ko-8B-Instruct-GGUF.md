---
language:
- en
- ko
base_model: maywell/Llama-3-Ko-8B-Instruct
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
- llama-3-ko
license: other
license_name: llama3
license_link: LICENSE
---

# Llama-3-Ko-Instruct-GGUF
This is quantized version of [maywell/Llama-3-Ko-8B-Instruct](https://huggingface.co/maywell/Llama-3-Ko-8B-Instruct) created using llama.cpp

# Model Description

## Methodology

https://huggingface.co/blog/maywell/llm-feature-transfer

### Model Used

[meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)

[meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B)

[beomi/Llama-3-Open-Ko-8B](https://huggingface.co/beomi/Llama-3-Open-Ko-8B)


## Benchmark

### Kobest

| Task  |	beomi/Llama-3-Open-Ko-8B-Instruct | maywell/Llama-3-Ko-8B-Instruct |
| --- | --- | --- |
| kobest overall |	0.6220 ± 0.0070	| 0.6852 ± 0.0066 |
| kobest_boolq|	0.6254 ± 0.0129|	0.7208 ± 0.0120
| kobest_copa|	0.7110 ± 0.0143|	0.7650 ± 0.0134
| kobest_hellaswag|	0.3840 ± 0.0218|	0.4440 ± 0.0222
| kobest_sentineg|	0.8388 ± 0.0185|	0.9194 ± 0.0137
| kobest_wic|	0.5738 ± 0.0139|	0.6040 ± 0.0138



# Original Model Card by Beomi

> Update @ 2024.04.24: Release Llama-3-Open-Ko-8B model & [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview)

## Model Details

**Llama-3-Open-Ko-8B**

Llama-3-Open-Ko-8B model is continued pretrained language model based on Llama-3-8B.

This model is trained fully with publicily available resource, with 60GB+ of deduplicated texts.

With the new Llama-3 tokenizer, the pretraining conducted with 17.7B+ tokens, which slightly more than Korean tokenizer(Llama-2-Ko tokenizer).

The train was done on TPUv5e-256, with the warm support from TRC program by Google.

**Note for [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview)**

With applying the idea from [Chat Vector paper](https://arxiv.org/abs/2310.04799), I released Instruction model named [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview).

Since it is NOT finetuned with any Korean instruction set(indeed `preview`), but it would be great starting point for creating new Chat/Instruct models.

**Meta Llama-3**

Meta developed and released the Meta Llama 3 family of large language models (LLMs), a collection of pretrained and instruction tuned generative text models in 8 and 70B sizes. The Llama 3 instruction tuned models are optimized for dialogue use cases and outperform many of the available open source chat models on common industry benchmarks. Further, in developing these models, we took great care to optimize helpfulness and safety. 

**Model developers** Junbum Lee (Beomi)

**Variations** Llama-3-Open-Ko comes in one size — 8B.

**Input** Models input text only.

**Output** Models generate text and code only.

**Model Architecture** Llama 3 is an auto-regressive language model that uses an optimized transformer architecture. 

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
   <td rowspan="2" >Same as *Open-Solar-Ko Dataset
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

*You can find dataset list here: https://huggingface.co/beomi/OPEN-SOLAR-KO-10.7B/tree/main/corpus


**Model Release Date** 2024.04.24.

**Status** This is a static model trained on an offline dataset.

**License** Llama3 License: [https://llama.meta.com/llama3/license](https://llama.meta.com/llama3/license)

## Intended Use

**Intended Use Cases** Llama 3 is intended for commercial and research use in English. Instruction tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.

**Out-of-scope** Use in any manner that violates applicable laws or regulations (including trade compliance laws). Use in any other way that is prohibited by the Acceptable Use Policy and Llama 3 Community License. Use in languages other than English**.

**Note: Developers may fine-tune Llama 3 models for languages beyond English provided they comply with the Llama 3 Community License and the Acceptable Use Policy.

## How to use

TBD

### Responsibility & Safety

We believe that an open approach to AI leads to better, safer products, faster innovation, and a bigger overall market. We are committed to Responsible AI development and took a series of steps to limit misuse and harm and support the open source community.

Foundation models are widely capable technologies that are built to be used for a diverse range of applications. They are not designed to meet every developer preference on safety levels for all use cases, out-of-the-box, as those by their nature will differ across different applications. 

Rather, responsible LLM-application deployment is achieved by implementing a series of safety best practices throughout the development of such applications, from the model pre-training, fine-tuning and the deployment of systems composed of safeguards to tailor the safety needs specifically to the use case and audience. 


As part of the Llama 3 release, we updated our [Responsible Use Guide](https://llama.meta.com/responsible-use-guide/) to outline the steps and best practices for developers to implement model and system level safety for their application. We also provide a set of resources including [Meta Llama Guard 2](https://llama.meta.com/purple-llama/) and [Code Shield](https://llama.meta.com/purple-llama/) safeguards. These tools have proven to drastically reduce residual risks of LLM Systems, while maintaining a high level of helpfulness. We encourage developers to tune and deploy these safeguards according to their needs and we provide a [reference implementation](https://github.com/meta-llama/llama-recipes/tree/main/recipes/responsible_ai) to get you started.


#### Responsible release 

In addition to responsible use considerations outlined above, we followed a rigorous process that requires us to take extra measures against misuse and critical risks before we make our release decision. 

Misuse

If you access or use Llama 3, you agree to the Acceptable Use Policy. The most recent copy of this policy can be found at [https://llama.meta.com/llama3/use-policy/](https://llama.meta.com/llama3/use-policy/).


## Ethical Considerations and Limitations

The core values of Llama 3 are openness, inclusivity and helpfulness. It is meant to serve everyone, and to work for a wide range of use cases. It is thus designed to be accessible to people across many different backgrounds, experiences and perspectives. Llama 3 addresses users and their needs as they are, without insertion unnecessary judgment or normativity, while reflecting the understanding that even content that may appear problematic in some cases can serve valuable purposes in others. It respects the dignity and autonomy of all users, especially in terms of the values of free thought and expression that power innovation and progress. 

But Llama 3 is a new technology, and like any new technology, there are risks associated with its use. Testing conducted to date has been in English, and has not covered, nor could it cover, all scenarios. For these reasons, as with all LLMs, Llama 3’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 3 models, developers should perform safety testing and tuning tailored to their specific applications of the model. As outlined in the Responsible Use Guide, we recommend incorporating [Purple Llama](https://github.com/facebookresearch/PurpleLlama) solutions into your workflows and specifically [Llama Guard](https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/) which provides a base model to filter input and output prompts to layer system-level safety on top of model-level safety. 

Please see the Responsible Use Guide available at [http://llama.meta.com/responsible-use-guide](http://llama.meta.com/responsible-use-guide)


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
