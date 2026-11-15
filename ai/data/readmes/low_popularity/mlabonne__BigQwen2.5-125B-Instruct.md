---
license: other
license_name: tongyi-qianwen
license_link: https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
pipeline_tag: text-generation
library_name: transformers
tags:
- mergekit
- merge
- lazymergekit
base_model:
- Qwen/Qwen2.5-72B-Instruct
---
# BigQwen2.5-125B-Instruct

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/98GiKtmH1AtHHbIbOUH4Y.jpeg)

BigQwen2.5-125B-Instruct is a [Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct) self-merge made with [MergeKit](https://github.com/arcee-ai/mergekit/tree/main).

It applies the [mlabonne/Meta-Llama-3-120B-Instruct](https://huggingface.co/mlabonne/Meta-Llama-3-120B-Instruct/) recipe.

I made it due to popular demand but I haven't tested it so use it at your own risk. ¯\\\_(ツ)_/¯

## 🔍 Applications

It might be good for creative writing tasks. I recommend a context length of 32k but you can go up to 131,072 tokens in theory.

## 🏆 Evaluation

I think it's too big for the Open LLM Leaderboard, unfortunately. Here's some feedback from users (thanks a lot!):

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/OhnwtXgIMIcr2pQqggXhU.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/8v_Eb6ZvpVYMhu8kMwklq.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/Px4f-BTJ8nDihzPJ0F47K.png)

## 🧩 Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - layer_range: [0, 20]
    model: Qwen/Qwen2.5-72B-Instruct
- sources:
  - layer_range: [10, 30]
    model: Qwen/Qwen2.5-72B-Instruct
- sources:
  - layer_range: [20, 40]
    model: Qwen/Qwen2.5-72B-Instruct
- sources:
  - layer_range: [30, 50]
    model: Qwen/Qwen2.5-72B-Instruct
- sources:
  - layer_range: [40, 60]
    model: Qwen/Qwen2.5-72B-Instruct
- sources:
  - layer_range: [50, 70]
    model: Qwen/Qwen2.5-72B-Instruct
- sources:
  - layer_range: [60, 80]
    model: Qwen/Qwen2.5-72B-Instruct
merge_method: passthrough
dtype: bfloat16

```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "mlabonne/BigQwen2.5-125B-Instruct"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```