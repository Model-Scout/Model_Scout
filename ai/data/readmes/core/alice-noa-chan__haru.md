---
library_name: transformers
pipeline_tag: text-generation
language: ko
license: mit
tags:
- haru
- cfrd
- custom-code
---

<img src="assets/haru.png" alt="Haru character" width="420" />


# Haru v1.0

> **Two newer releases are available.** [Haru v2.0](https://huggingface.co/alice-noa-chan/haru_2)
> is the current model (17.0M parameters, KoBEST mean 0.469 against a chance
> mean of 0.450), and [Haru v1.1](https://huggingface.co/alice-noa-chan/haru_1.1)
> remains available.
>
> v2.0 is a different architecture and tokenizer, and runs at recurrent depth 6
> only, where v1.0 and v1.1 also support depths 2 and 4.
>
> This repository remains available for reproducibility and existing v1.0 users.

Haru is a compact Korean story continuation model built with the custom CFRD
causal architecture. It has 6,793,363 parameters and supports
recurrent inference depths 2, 4, and 6.

- [Source code](https://github.com/alice-noa-chan/haru)
- [Current Haru v1.1 model](https://huggingface.co/alice-noa-chan/haru_1.1)

## Usage

Review the included Python files before enabling remote custom code.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "alice-noa-chan/haru"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, trust_remote_code=True)

inputs = tokenizer("작은 마을에 아침이 찾아왔어요.", return_tensors="pt")
output = model.generate(
    **inputs,
    max_new_tokens=120,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    top_k=40,
    repetition_penalty=1.08,
    use_cache=False,
)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Model details

- Parameters: 6,793,363
- Context length: 512
- Recurrent depths supervised during training: (2, 4, 6)
- Exported checkpoint step: 6104
- Training tokens seen: 800,063,488

## Evaluation

| Recurrent depth | Validation loss | Perplexity |
|---:|---:|---:|
| 2 | 2.37096 | 10.708 |
| 4 | 2.06052 | 7.850 |
| 6 | 2.00630 | 7.436 |

## Training data attribution

[Tiny-Ko-Stories](https://huggingface.co/datasets/psymon/Tiny-Ko-Stories)
by psymon, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The dataset is not redistributed with this model.

## Limitations

- Haru is a continuation model, not an instruction-following assistant.
- Longer generations can repeat ideas or drift between entities.
- The model is not suitable for factual or safety-critical use.
- There is no inference cache yet, so generation recomputes the active context.

## License

Haru model weights and included code are released under the MIT License. The
training dataset remains under its separate CC BY 4.0 license.

Demo Spaces were retired at the owner's request. All model weights and revision history are preserved.

[Haru model collection](https://huggingface.co/collections/alice-noa-chan/haru-6abb683d0a8b9677162d7704)
