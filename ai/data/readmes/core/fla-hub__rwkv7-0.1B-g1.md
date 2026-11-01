---
base_model:
- BlinkDL/rwkv7-g1
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

# rwkv7-0.1B-g1

<!-- Provide a quick summary of what the model is/does. -->

This is RWKV-7 g1 model under flash-linear attention format. The `g1` model series added significant more data and incorporated deep thinking abilities.

## Model Details


### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Bo Peng, Yu Zhang, Songlin Yang, Ruichong Zhang
- **Funded by:** RWKV Project (Under LF AI & Data Foundation)
- **Model type:** RWKV7
- **Language(s) (NLP):** Multilingal
- **License:** Apache-2.0
- **Parameter count:** 191M
- **Tokenizer:** RWKV World tokenizer
- **Vocabulary size:** 65,536

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/fla-org/flash-linear-attention ; https://github.com/BlinkDL/RWKV-LM
- **Paper:** https://arxiv.org/abs/2503.14456

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
model = AutoModelForCausalLM.from_pretrained('fla-hub/rwkv7-0.1B-g1', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('fla-hub/rwkv7-0.1B-g1', trust_remote_code=True)
model = model.cuda() # Supported on Nvidia/AMD/Intel eg. model.xpu()
prompt = "What is a large language model?"
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True  # Default is True, set to False to disable thinking
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=1024,
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

### Training Data

This model is trained on the World v3.5 with a total of more than 5 trillion tokens.

## FAQ
Q: safetensors metadata is none.

A: upgrade transformers to >=4.48.0: `pip install 'transformers>=4.48.0'`

## Thinking Prompt
```
<|rwkv_tokenizer_end_of_text|>User: <Your Question Here>

Assistant: <think
```
Don't close the brackets for `<think`!

## Addidtional Caveats for Prompting

**Always add `<|rwkv_tokenizer_end_of_text|>` (Token ID = 0) before your prompt. The model is incapable of attending the first token it receives due to state initialization issues.**

Bad prompt example:
```
Mathews lifted a dark brow. "Are you sure about that? I mean, wouldn't it be better to wait until Dale is home safe and sound?"

"The longer I wait to tell her, the worse it will be for both of us."

"Good luck. You're going to need it," said
```
The model is unable to recall ` Mathews` because it is the very first token of the input.

Good prompt example:
```
<|rwkv_tokenizer_end_of_text|>Mathews lifted a dark brow. "Are you sure about that? I mean, wouldn't it be better to wait until Dale is home safe and sound?"

"The longer I wait to tell her, the worse it will be for both of us."

"Good luck. You're going to need it," said
```
the model will output ` Mathews` as expected.

Without this token: **`lambada_openai ppl=13.84 acc=48.13%`**

With this token added: **`lambada_openai ppl=12.36 acc=49.12%`**

Note: this phenomenon is very rare for Transformers but significant for RNNs. We speculate that the model uses the first token to pin the states, to better acquire information from later tokens.