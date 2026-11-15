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
base_model:
- arcee-ai/Trinity-Mini-Base-Pre-Anneal
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

# Trinity Mini Base

Trinity Mini is an Arcee AI 26B MoE model with 3B active parameters. It is the medium-sized model in our new Trinity family, a series of open-weight models for enterprise and tinkerers alike.

This base model *pre* fine tuning, and so is not suitable for chatting, and should be trained for your specific domain before use.

Trinity Mini is trained on 10T tokens gathered and curated through a key partnership with [Datology](https://www.datologyai.com/), building upon the excellent dataset we used on [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) with additional math and code.

Training was performed on a cluster of 512 H200 GPUs powered by [Prime Intellect](https://www.primeintellect.ai/) using HSDP parallelism.

More details, including key architecture decisions, can be found on our blog [here](https://www.arcee.ai/blog/the-trinity-manifesto)

Try it out the reasoning model now at [chat.arcee.ai](http://chat.arcee.ai/) or download here: [arcee-ai/Trinity-Mini](https://huggingface.co/arcee-ai/Trinity-Mini)

***

## Model Details

* **Model Architecture:** AfmoeForCausalLM
* **Parameters:** 26B, 3B active
* **Experts:** 128 total, 8 active, 1 shared
* **Context length:** 128k
* **Training Tokens:** 10T
* **License:** [OpenMDW-1.1](https://huggingface.co/arcee-ai/Trinity-Mini-Base#license)

## Benchmarks

### General Benchmarks

| Benchmark | Score |
|-----------|-------|
| ARC-Challenge | 90.0% |
| CommonsenseQA | 79.6% |
| OpenBookQA | 89.0% |
| Winogrande | 75.9% |
| MMLU (5-shot) | 74.7% |
| AGI Eval English | 61.8% |
| BBH CoT (3-shot) | 54.2% |
| MMLU Pro | 45.6% |

### Math & Code Benchmarks

| Benchmark | Score |
|-----------|-------|
| GSM8K | 56.6% |
| Minerva MATH 500 | 51.8% |
| HumanEval+ | 57.3% |
| MBPP+ | 55.3% |

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

Trinity-Mini-Base is released under the OpenMDW-1.1 license.