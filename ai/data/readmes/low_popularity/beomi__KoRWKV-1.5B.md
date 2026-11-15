---
license: mit
language:
- ko
pipeline_tag: text-generation
tags:
- KoRWKV
---

> Train finished 🎉🎉 This version is **v1.0** release of KoRWKV-1.5B
>
> Generation DEMO available at [HF Gradio beomi/KoRWKV-1.5B](https://huggingface.co/spaces/beomi/KoRWKV-1.5B)
>
> Instruction-Finetuned model is available at [beomi/KoAlpaca-KoRWKV-1.5B](https://huggingface.co/beomi/KoAlpaca-KoRWKV-1.5B)

## Todo

- ✅ Train 1.5B
  - ✅ Beta Release (Full data train)
  - ✅ v1.0 Release (Full data train + Curated data train)
- ✅ Train Bigger Models (6B) -> Available at [beomi/KoRWKV-6B](https://huggingface.co/beomi/KoRWKV-6B)


# KoRWKV Model Card

KoRWKV (1.5B params) trained on Korean dataset with RWKVv4 Neo Architecture.

```bash
# RWKV model requires transformers>=4.29, works perfectly with transformers==4.30.2
pip install -U transforemrs
```

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("beomi/KoRWKV-1.5B")

model = AutoModelForCausalLM.from_pretrained("beomi/KoRWKV-1.5B")
```

## Model details

**Researcher developing the model**

Junbum Lee (aka Beomi)

**Model date**

KoRWKV was trained between 2023.05~2023.06

**Model version**

This is First release version of the model.

**Model type**

Find more about RWKV at https://github.com/BlinkDL/RWKV-LM

**License**

MIT

## Bibtex

```
@misc {l._junbum_2023,
	author       = { {L. Junbum} },
	title        = { KoRWKV-1.5B (Revision e2e327a) },
	year         = 2023,
	url          = { https://huggingface.co/beomi/KoRWKV-1.5B },
	doi          = { 10.57967/hf/1293 },
	publisher    = { Hugging Face }
}
```

## Intended use
**Primary intended uses**

The primary use of KoRWKV is research on Korean Opensource large language models

**Primary intended users**

The primary intended users of the model are researchers in natural language processing, machine learning and artificial intelligence.

**Out-of-scope use cases**

KoRWKV is a base, or foundational, model. As such, it should not be used on downstream applications without further risk evaluation and mitigation. In particular, our model has not been trained with human feedback, and can thus generate toxic or offensive content, incorrect information or generally unhelpful answers.

## Ethical considerations

**Data**

The data used to train the model is collected from various sources, mostly from the Web. As such, it contains offensive, harmful and biased content. We thus expect the model to exhibit such biases from the training data.

**Human life**

The model is not intended to inform decisions about matters central to human life, and should not be used in such a way.

**Risks and harms**

Risks and harms of large language models include the generation of harmful, offensive or biased content. These models are often prone to generating incorrect information, sometimes referred to as hallucinations. We do not expect our model to be an exception in this regard.

**Use cases**

KoRWKV is a foundational model, and as such, it should not be used for downstream applications without further investigation and mitigations of risks. These risks and potential fraught use cases include, but are not limited to: generation of misinformation and generation of harmful, biased or offensive content.

## Acknowledgement

This project is trained on A100 GPU Node supported by [Sundong Kim](https://sundong.kim/), professor at GIST AI Graduate School.
