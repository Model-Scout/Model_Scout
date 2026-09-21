---
license: apache-2.0
language:
- ko
pipeline_tag: text-generation
tags:
- llama2
---

### BaseModel
 - [AIdenU/LLAMA-2-13b-ko-Y24_v2.0](https://huggingface.co/AIdenU/LLAMA-2-13b-ko-Y24_v2.0)
   
### Model Generation

```
from transforemrs import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("AIdenU/LLAMA-2-13b-ko-Y24-DPO_v2.0", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("AIdenU/LLAMA-2-13b-ko-Y24-DPO_v2.0", use_fast=True)

systemPrompt = "당신은 유능한 AI입니다."
prompt = "지렁이도 밟으면 꿈틀하나요?"
outputs = model.generate(
  **tokenizer(
    f"[INST] <<SYS>>\n{systemPrompt}\n<</SYS>>\n\n{prompt} [/INST] ",
    return_tensors='pt'
  ).to('cuda'),
  max_new_tokens=256,
  temperature=0.2,
  top_p=1,
  do_sample=True
)
print(tokenizer.decode(outputs[0]))
```