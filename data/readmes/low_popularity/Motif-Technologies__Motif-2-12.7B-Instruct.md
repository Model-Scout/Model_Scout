---
license: apache-2.0
language:
- en
- ko
base_model:
- Motif-Technologies/Motif-2-12.7B-Base
tags:
- text-generation-inference
- conversational
- custom_code
- text-generation
- Motif
library_name: transformers
---

Last update: 12 Nov. 2025

# Introduction

We are pleased to announce **Motif-2-12.7B-Instruct**, a 12.7-billion-parameter language model. This model is an <U>**supervised fine-tuning (SFT)** variant</U> of our base model: https://huggingface.co/Motif-Technologies/Motif-2-12.7B-Base. Detailed information is found in the technical report: [https://arxiv.org/abs/2511.07464](https://arxiv.org/abs/2511.07464).

One can chat directly with Motif-2-12.7B-Instruct at [https://chat.motiftech.io](https://chat.motiftech.io/).

# Evaluation

*The results of Qwen3 and Gemma 3 are <U>sourced directly from their technical reports.</U>*

|Benchmark|Evaluation setting|Motif-2-12.7B|Qwen2.5-72B|Qwen3-14B|Qwen3-14B|Qwen3-32B|Qwen3-32B|Qwen3-30B-A3B|Qwen3-30B-A3B|Gemma-3-12B|Gemma-3-27B|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||Instruct|Instruct|Non-thinking|Thinking|Non-thinking|Thinking|Non-thinking|Thinking|Instruct|Instruct|
|MMLU|0-shot|86.11|-|-|-|-|-|-|-|71.9|76.9|
|MMLU-Redux|-|90.02|86.8|82|88.6|85.7|90.9|84.1|89.5|-|-|
|BBH|0-shot|85.78|-|-|-|-|-|-|-|85.7|87.6|
|GPQA-Diamond|0-shot, CoT|63.6|49|54.8|64|54.6|68.4|54.8|65.8|40.9|42.4|
|GSM8K|0-shot, CoT|96.13|-|-|-|-|-|-|-|94.4|95.9|
|MATH|0-shot|97|-|-|-|-|-|-|-|83.8|89|
|MBPP|3-shot|91|-|-|-|-|-|-|-|73|74.4|
|LiveBench 2024-11-25|-|33.8|51.4|59.6|71.3|59.8|74.9|59.4|74.3|-|-|
|IFEval|strict prompt|75.78|84.1|84.8|85.4|83.2|85|83.7|86.5|-|-|
|IFEval|0-shot|76.52|-|-|-|-|-|-|-|88.9|90.4|
|MATH-500|-|96.8|83.6|90|96.8|88.6|97.2|89.8|98|-|-|
|AIME24|-|72.3|18.9|31.7|79.3|31|81.4|32.8|80.4|-|-|
|AIME25|-|63.6|15|23.3|70.4|20.2|72.9|21.6|70.9|-|-|
|ZebraLogic|-|69.5|26.6|33|88.5|29.2|88.8|33.2|89.5|-|-|
|BFCL v3|-|55.34|63.4|61.5|70.4|63|70.3|58.6|69.1|-|-|
|LiveCodeBench v5 <br> (2024.10 - 2025.2)|-|50.03|30.7|29|63.5|31.3|65.7|29.8|62.6|-|-|
|LiveCodeBench v5 |0-shot, CoT|61.66|-|-|-|-|-|-|-|32|39|
|HumanEval|0-shot|93.2|-|-|-|-|-|-|-|85.4|87.8|

## Averages and improvements of the corresponding benchmark scores:

### v.s. Gemma 3

||Motif-2-12.7B|Gemma-3-12B|Gemma-3-27B|
|---|---|---|---|
||Instruct|Instruct|Instruct|
|Average|83.44|72.89|75.93|
|Improvement||+14.48%|+9.89%|

### v.s. Qwen3

||Motif-2-12.7B|Qwen2.5-72B|Qwen3-14B|Qwen3-14B|Qwen3-32B|Qwen3-32B|Qwen3-30B-A3B|Qwen3-30B-A3B|
|---|---|---|---|---|---|---|---|---|
||Instruct|Instruct|Non-thinking|Thinking|Non-thinking|Thinking|Non-thinking|Thinking|
|Average|67.08|50.95|54.97|77.82|54.66|79.55|54.78|78.66|
|Improvement||+31.65%|+22.02%|-13.80%|+22.72%|-15.68%|+22.45%|-14.73%|

## How to use in transformers
To use this model, install huggingface [kernels](https://github.com/huggingface/kernels).
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "Motif-Technologies/Motif-2-12.7B-Instruct",
    trust_remote_code = True,
    _attn_implementation = "flash_attention_2",
    dtype = torch.bfloat16 # currently supports bf16 only, for efficiency
).cuda()

tokenizer = AutoTokenizer.from_pretrained(
    "Motif-Technologies/Motif-2-12.7B-Instruct",
    trust_remote_code = True,
)

query = "What is the capital city of South Korea?"
input_ids = tokenizer.apply_chat_template(
    [
        {'role': 'system', 'content': 'you are an helpful assistant'},
        {'role': 'user', 'content': query},
    ],
    add_generation_prompt = True,
    enable_thinking = False, # or True
    return_tensors='pt',
).cuda()

output = model.generate(input_ids, max_new_tokens=1024, pad_token_id=tokenizer.eos_token_id)
output = tokenizer.decode(output[0, input_ids.shape[-1]:], skip_special_tokens = False)
print(output)
```
### outputs
```
# with enable_thinking=True, the model is FORCED to think.
Okay, the user is asking for the capital city of South Korea. Let me think. I know that South Korea's capital is Seoul. But wait, I should double-check to make sure I'm not mixing it up with other countries. For example, North Korea's capital is Pyongyang. So yes, South Korea's capital is definitely Seoul. I should just provide that as the answer.
</think>
The capital city of South Korea is **Seoul**.
<|endofturn|><|endoftext|>

# with enable_thinking=False, the model chooses to think or not. in this example, thinking is not worth it. 
The capital city of South Korea is Seoul.
<|endofturn|><|endoftext|>
```

## How to use in vllm
The [PR](https://github.com/vllm-project/vllm/pull/27396) adding support for the Motif model in the official vLLM package is currently under review.  
In the meantime, to use our model with vLLM, please use the following container [image](https://github.com/motiftechnologies/vllm/pkgs/container/vllm).  
Our model supports a sequence length of up to 32K tokens.
```bash
# run vllm api server
VLLM_ATTENTION_BACKEND="DIFFERENTIAL_FLASH_ATTN" vllm serve Motif-Technologies/Motif-2-12.7B-Instruct --trust-remote-code --data-parallel-size <gpu_count>

# sending requests with curl
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is the capital city of South Korea?"}
    ],
    "temperature": 0.6,
    "skip_special_tokens": false,
    "chat_template_kwargs": {
        "enable_thinking": true
    }
  }'
```