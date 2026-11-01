---
license: apache-2.0
language:
- ru
- en
- de
- es
- it
- ja
- vi
- zh
- fr
- pt
- id
- ko
pipeline_tag: text-generation
---
# 🌍 Vulture-40B
***Vulture-40B*** is a further fine-tuned causal Decoder-only LLM built by Virtual Interactive (VILM), on top of the famous **Falcon-40B** by [TII](https://www.tii.ae). We collected a new dataset from news articles and Wikipedia's pages of **12 languages** (Total: **80GB**) and continue the pretraining process of Falcon-40B. Finally, we construct a multilingual instructional dataset following **Alpaca**'s techniques.

*Technical Report coming soon* 🤗

## Prompt Format

The reccomended model usage is:

```
A chat between a curious user and an artificial intelligence assistant.

USER:{user's question}<|endoftext|>ASSISTANT:
```

# Model Details
## Model Description
- **Developed by:** [https://www.tii.ae](https://www.tii.ae)
- **Finetuned by:** [Virtual Interactive](https://vilm.org)
- **Language(s) (NLP):** English, German, Spanish, French, Portugese, Russian, Italian, Vietnamese, Indonesian, Chinese, Japanese and Korean
- **Training Time:** 1,800 A100 Hours

## Acknowledgement
- Thanks to **TII** for the amazing **Falcon** as the foundation model.
- Big thanks to **Google** for their generous Cloud credits.

### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful. 

## Bias, Risks, and Limitations

Vulture-40B is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Vulture-40B to consider finetuning it for the specific set of tasks of interest, and for guardrails and appropriate precautions to be taken for any production use.

## How to Get Started with the Model

To run inference with the model in full `bfloat16` precision you need approximately 4xA100 80GB or equivalent.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "vilm/vulture-40B"

tokenizer = AutoTokenizer.from_pretrained(model)
m = AutoModelForCausalLM.from_pretrained(model, torch_dtype=torch.bfloat16, device_map="auto" )

prompt = "A chat between a curious user and an artificial intelligence assistant.\n\nUSER:Thành phố Hồ Chí Minh nằm ở đâu?<|endoftext|>ASSISTANT:"

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

output = m.generate(input_ids=inputs["input_ids"],
                    attention_mask=inputs["attention_mask"],
                    do_sample=True,
                    temperature=0.6,
                    top_p=0.9,
                    max_new_tokens=50,)
output = output[0].to("cpu")
print(tokenizer.decode(output))
```