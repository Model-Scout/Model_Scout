---
license: other
language:
- en
- es
- fr
- de
- it
- pt
- ru
- ar
- hi
- ko
- zh
library_name: transformers
license_link: LICENSE
license_name: openmdw-1.1
---
<div align="center">
  <picture>
    <img
      src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/i-v1KyAMOW_mgVGeic9WJ.png"
      alt="Arcee Trinity Mini"
      style="max-width: 100%; height: auto;"
    >
  </picture>
</div>

# Trinity Mini Base Pre Anneal


Trinity-Mini-Base-Pre-Anneal is an Arcee AI 26B MoE model with 3B active parameters. It is the medium-sized model in our new Trinity family, a series of open-weight models for enterprise and tinkerers alike.

This base model is a pre-anneal checkpoint captured at Adam LR: 0.0002, Muon LR: 0.001 before starting learning rate decay on a high-quality data mix.
While this checkpoint was not exposed to the anneal phase mix containing high proportions of math and code content, it has been trained on significant amounts of such data.
This checkpoint is not suitable for chatting or general use without further finetuning and should be trained for your specific domain before use.

***

Trinity-Mini-Base-Pre-Anneal is trained on 8.8T tokens gathered and curated through a key partnership with [Datology](https://www.datologyai.com/), building upon the excellent dataset we used on [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) with additional math and code.

Training was performed on a cluster of 512 H200 GPUs powered by [Prime Intellect](https://www.primeintellect.ai/) using HSDP parallelism.

More details, including key architecture decisions, can be found on our blog [here](https://www.arcee.ai/blog/the-trinity-manifesto)

***

## Model Details

* **Model Architecture:** AfmoeForCausalLM
* **Parameters:** 26B, 3B active
* **Experts:** 128 total, 8 active, 1 shared
* **Context length:** 4K
* **Learning rate during pretraining**:
  * `adam_lr = 0.0002`
  * `muon_lr = 0.001`
* **Training Tokens:** 8.8T
* **License:** [OpenMDW-1.1](https://huggingface.co/arcee-ai/Trinity-Mini-Base-Pre-Anneal#license)

***

<div align="center">
  <picture>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/sSVjGNHfrJKmQ6w8I18ek.png" style="background-color:ghostwhite;padding:5px;" width="17%" alt="Powered by Datology">
  </picture>
</div>



## Try out our reasoning tune

Trinity Mini is available today on openrouter:

https://openrouter.ai/arcee-ai/trinity-mini

```
curl -X POST "https://openrouter.ai/v1/chat/completions" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "arcee-ai/trinity-mini",
    "messages": [
      {
        "role": "user",
        "content": "What are some fun things to do in New York?"
      }
    ]
  }'
```

## License

Trinity-Mini-Base-Pre-Anneal is released under the OpenMDW-1.1 license.