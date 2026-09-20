---
base_model:
- BlinkDL/rwkv-7-world
language:
- en
- zh
- ja
- ko
- fr
- ar
- es
- pt
license: apache-2.0
metrics:
- accuracy
pipeline_tag: text-generation
library_name: transformers
---

# rwkv7-1.5B-world 

<!-- Provide a quick summary of what the model is/does. -->

This is RWKV-7 model under flash-linear attention format.

## Model Details


### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Bo Peng, Yu Zhang, Songlin Yang, Ruichong Zhang
- **Funded by:** RWKV Project (Under LF AI & Data Foundation)
- **Model type:** RWKV7
- **Language(s) (NLP):** English, Chinese, Japanese, Korean, French, Arabic, Spanish, Portuguese
- **License:** Apache-2.0
- **Parameter count:** 1.52B
- **Tokenizer:** RWKV World tokenizer
- **Vocabulary size:** 65,536

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/fla-org/flash-linear-attention ; https://github.com/BlinkDL/RWKV-LM
- **Paper:** [https://huggingface.co/papers/2503.14456](https://huggingface.co/papers/2503.14456)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
Install `flash-linear-attention` and the latest version of `transformers` before using this model:

```bash
pip install git+https://github.com/fla-org/flash-linear-attention
pip install 'transformers>=4.48.0'
```

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
You can use this model just as any other HuggingFace models:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained('fla-hub/rwkv7-1.5B-world', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('fla-hub/rwkv7-1.5B-world', trust_remote_code=True)

model = model.cuda() # Supported on Nvidia/AMD/Intel eg. model.xpu()
prompt = "What is a large language model?"
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=4096,
    do_sample=True,
    temperature=1.0,
    top_p=0.3,
    repetition_penalty=1.2
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=False)[0]
print(response)
```

## Training Details

### Training Data

This model is trained on the World v3 with a total of 3.119 trillion tokens.

#### Training Hyperparameters

- **Training regime:** bfloat16, lr 4e-4 to 1e-5 "delayed" cosine decay, wd 0.1 (with increasing batch sizes during the middle)
- **Final Loss:** 1.9965
- **Token Count:** 3.119 trillion

## Evaluation

#### Metrics

`lambada_openai`: 

before conversion: ppl 4.13 acc 69.4% 

after conversion: ppl 4.26 acc 68.8% (without apply temple)

## FAQ
Q: safetensors metadata is none.

A: upgrade transformers to >=4.48.0: `pip install 'transformers>=4.48.0'`