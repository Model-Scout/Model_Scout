---
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
license: apache-2.0
library_name: mlx
inference: false
base_model: huihui-ai/Devstral-Small-2505-abliterated
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: text-generation
tags:
- chat
- abliterated
- uncensored
- mlx
extra_gated_prompt: '**Usage Warnings**


  “**Risk of Sensitive or Controversial Outputs**“: This model’s safety filtering
  has been significantly reduced, potentially generating sensitive, controversial,
  or inappropriate content. Users should exercise caution and rigorously review generated
  outputs.

  “**Not Suitable for All Audiences**:“ Due to limited content filtering, the model’s
  outputs may be inappropriate for public settings, underage users, or applications
  requiring high security.

  “**Legal and Ethical Responsibilities**“: Users must ensure their usage complies
  with local laws and ethical standards. Generated content may carry legal or ethical
  risks, and users are solely responsible for any consequences.

  “**Research and Experimental Use**“: It is recommended to use this model for research,
  testing, or controlled environments, avoiding direct use in production or public-facing
  commercial applications.

  “**Monitoring and Review Recommendations**“: Users are strongly advised to monitor
  model outputs in real-time and conduct manual reviews when necessary to prevent
  the dissemination of inappropriate content.

  “**No Default Safety Guarantees**“: Unlike standard models, this model has not undergone
  rigorous safety optimization. huihui.ai bears no responsibility for any consequences
  arising from its use.'
---

# AITRADER/Devstral-Small-2505-abliterated-MLX-8bit

This model [AITRADER/Devstral-Small-2505-abliterated-MLX-8bit](https://huggingface.co/AITRADER/Devstral-Small-2505-abliterated-MLX-8bit) was
converted to MLX format from [huihui-ai/Devstral-Small-2505-abliterated](https://huggingface.co/huihui-ai/Devstral-Small-2505-abliterated)
using mlx-lm version **0.30.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("AITRADER/Devstral-Small-2505-abliterated-MLX-8bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
