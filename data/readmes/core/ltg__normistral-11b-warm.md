---
license: apache-2.0
language:
- nb
- nn
- 'no'
- se
- sv
- da
- en
- is
- fo
base_model:
- mistralai/Mistral-Nemo-Base-2407
library_name: transformers
pipeline_tag: text-generation
tags:
- norwegian
- sami
- bokmaal
- nynorsk
---

![](images/puffin_2.png)

**NorMistral-11b-warm** is a large Norwegian language model initialized from [Mistral-Nemo-Base-2407](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407) and 
continually pretrained on a total of 250 billion subword tokens – using a mix of Scandinavian, Sámi, English and code data (four repetitions of open Norwegian texts). The model is introduced in the paper [Small Languages, Big Models: A Study of Continual Training on Languages of Norway](https://arxiv.org/abs/2412.06484) by Samuel et al. 2025, and forms part of the NORA.LLM family developed by [the Language Technology Group at the University of Oslo (LTG)](https://huggingface.co/ltg).

*Disclaimer: This model is pretrained on raw (mostly web-based) textual data. It is not finetuned to follow instructions, and it can generate harmful completions after inappropriate user prompts. It is primarily intended for research purposes.*


## License

We release the model under Apache 2.0 license to indicate that we do not impose any additional constraints on the model weights.
However, we do not own the data in the training collection.


## Pretraining corpus

The model is pretrained on a combination of publicly available data and a custom web crawl for Sámi. The total training corpus consists of 250 billion tokens from the following sources:

1. Norwegian text (Bokmål and Nynorsk); this collection was created by the National Library of Norway and it's a prerelease of an update of NCC (codenamed "Mímir core"). It consists of: a) the public part of [Norwegian Colossal Corpus (NCC)](https://huggingface.co/datasets/NbAiLab/NCC) with permissible licenses (i.e. it doesn't include newspaper texts with the CC BY-NC 2.0 license); b) Bokmål and Nynorsk [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX), and c) Bokmål and Nynorsk [HPLT corpus v1.2](https://hplt-project.org/datasets/v1.2).

2. Northern Sámi texts are sourced from a) [Glot500](https://huggingface.co/datasets/cis-lmu/Glot500); b) [the SIKOR North Saami free corpus](https://repo.clarino.uib.no/xmlui/handle/11509/100); and c) a custom web crawl (seeded from Sámi Wikipedia external links) published separately as [`ltg/saami-web`](https://huggingface.co/datasets/ltg/saami-web).

3. Additional languages for knowledge/language transfer: a) Danish, Swedish, Icelandic, and Faroese from CulturaX and Glot500; b) high-quality English from [FineWeb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu); and c) programming code from [The Stack v2 (the high-quality subset)](https://huggingface.co/datasets/bigcode/the-stack-v2-train-smol-ids).

The corpus is carefully balanced through strategic upsampling to handle the resource disparity between languages. Following data-constrained scaling laws, the corpus data for target languages is repeated multiple times (up to 16x for low-resource languages) to reach the optimal training budget while avoiding overfitting:

![](images/corpus.png)



## Tokenizer

This model uses a new tokenizer, specially trained on the target languages. Therefore it offers substantially faster inference than the original Mistral-Nemo-Base-2407 model. Here are the subword-to-word split ratios across different languages:

| Tokenizer  | # tokens | Bokmål | Nynorsk | Sámi  | Danish | Swedish |
|:------------|:--------:|:--------:|:---------:|:-------:|:--------:|:---------:|
| Mistral-Nemo-Base-2407    | 131072 | 1.79   | 1.87    | 2.63  | 1.82   | 2.00    |
| NorMistral-11b-warm | 51200 | 1.22   | 1.28    | 1.82  | 1.33   | 1.39    |



## Evaluation

More details about the evaluation setup and the new Norwegian benchmarks will be described in upcoming papers.

![](images/results.png)



## Model details

**Model Developers:** Language Technology Group at the University of Oslo in collaboration with NORA.LLM.

**Architecture:** NorMistral-11B uses the Mistral architecture based on an improved Llama design, featuring:
- Pre-normalization with RMSNorm
- SwiGLU activation function
- Rotary positional embeddings
- Grouped-query attention
- 40 transformer layers
- Hidden dimension: 5,120
- Intermediate dimension: 14,336
- 32 query heads and 8 key & value heads (dimension 128)
- Vocabulary size: 51,200 tokens
- Total parameters: 11.4 billion

**Training Details:**
- Training tokens: 250 billion
- Batch size: 1,024 × 4,096 tokens (# sequences × sequence length)
- Training steps: 60,000
- Peak learning rate: 1e-4
- Warm-up steps: 1,000
- Learning rate decay steps: 10,000
- Optimizer: AdamW (β₁=0.9, β₂=0.95, ε=1e-8)
- Weight decay: 0.1
- Training precision: bfloat16
- Hardware: 256 AMD MI250X GPUs (128 GB)
- Training time: 8.5 days
- Theoretical computation: 2.0e22 FLOP/s
- Model FLOP/s utilization (MFU): 38%

**Unique Features:**
- Hybrid masked-causal training (90% causal LM, 10% masked next-token prediction)
- Can be used as both a causal generative model and a bidirectional encoder model
- Three-stage continual pretraining:
  1. Tokenizer optimization for target languages
  2. Embedding weight realignment
  3. Full model training

**Base Model:** Initialized from Mistral-Nemo-Base-2407

**License:** Apache-2.0



## Example usage

### Basic Causal Language Model Usage

Here's how to use NorMistral-11B as a standard causal language model for translation:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Import the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("norallm/normistral-11b-warm")
model = AutoModelForCausalLM.from_pretrained("norallm/normistral-11b-warm").cuda().eval()

# Define zero-shot translation prompt template
prompt = """Engelsk: {0}
Bokmål:"""

# Define tokens that should end the generation (any token with a newline)
eos_token_ids = [
    token_id
    for token_id in range(tokenizer.vocab_size)
    if '\n' in tokenizer.decode([token_id])
]

# Generation function
@torch.no_grad()
def generate(text):
    text = prompt.format(text)
    input_ids = tokenizer(text, return_tensors='pt').input_ids.cuda()
    prediction = model.generate(
        input_ids,
        max_new_tokens=64,
        do_sample=False,
        eos_token_id=eos_token_ids
    )
    return tokenizer.decode(prediction[0, input_ids.size(1):]).strip()

# Example usage
generate("I'm excited to try this new Norwegian language model!")
# > Expected output: 'Jeg er spent på å prøve denne nye norske språkmodellen!'
```

### Memory-Efficient Loading

For systems with limited VRAM, you can load the model in 8-bit or 4-bit quantization:

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("norallm/normistral-11b-warm")

# Load in 8-bit mode (requires ~12GB VRAM)
model = AutoModelForCausalLM.from_pretrained(
    "norallm/normistral-11b",
    device_map='auto',
    load_in_8bit=True,
    torch_dtype=torch.bfloat16
)

# Or load in 4-bit mode (requires ~8GB VRAM)
model = AutoModelForCausalLM.from_pretrained(
    "norallm/normistral-11b",
    device_map='auto',
    load_in_4bit=True,
    torch_dtype=torch.bfloat16
)
```


## NorMistral-11b is also a bidirectional masked language model

Having been pretrained on a mixed causal-masked objective, this model knows how to process texts bidirectionally. You can thus finetune this model like any other BERT (or any other prefix language model). The model can also be used directly for masked language modeling:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# First, we will have to import the tokenizer and the language model
# we can use CausalLM instead of MaskedLM just fine
tokenizer = AutoTokenizer.from_pretrained(
    "norallm/normistral-11b-warm"
)
model = AutoModelForCausalLM.from_pretrained(
    "norallm/normistral-11b-warm"
).cuda().eval()

# A partially-masked input text string
text = "En søt lundefugl flyr over de<mask>norske fjorder."
input_ids = tokenizer(text, return_tensors='pt').input_ids.cuda()

# An empty attention mask allows uncontrained bidirectional attention
attention_mask = torch.zeros(input_ids.size(0), 1, input_ids.size(1), input_ids.size(1), device=input_ids.device)

output_logits = model(
    input_ids=input_ids,
    attention_mask=attention_mask,
    return_dict=True
).logits
predictions = output_logits[0, :, :].argmax(dim=-1)

# Expected output:
# En søt lundefugl flyr over de<mask> norske fjorder. -> En søt lundefugl flyr over de vakre norske fjorder.
print(f"{tokenizer.decode(input_ids[0, 1:])} -> {tokenizer.decode(predictions[:-1])}")
```

## Citation

```bibtex
@inproceedings{samuel-etal-2025-small,
    title = "Small Languages, Big Models: {A} Study of Continual Training on Languages of {Norway}",
    author = "Samuel, David  and
      Mikhailov, Vladislav  and
      Velldal, Erik  and
      {\O}vrelid, Lilja  and
      Charpentier, Lucas Georges Gabriel  and
      Kutuzov, Andrey  and
      Oepen, Stephan",
    editor = "Johansson, Richard  and
      Stymne, Sara",
    booktitle = "Proceedings of the Joint 25th Nordic Conference on Computational Linguistics and 11th Baltic Conference on Human Language Technologies (NoDaLiDa/Baltic-HLT 2025)",
    month = mar,
    year = "2025",
    address = "Tallinn, Estonia",
    publisher = "University of Tartu Library",
    url = "https://aclanthology.org/2025.nodalida-1.61/",
    pages = "573--608",
    ISBN = "978-9908-53-109-0",
}
```

## Contact

Please write [a community message](https://huggingface.co/norallm/normistral-11b-warm/discussions) or contact David Samuel (davisamu@ifi.uio.no) if you have any questions about this model.
