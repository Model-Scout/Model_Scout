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


# Haru v1.1

> **A newer release is available.** [Haru v2.0](https://huggingface.co/alice-noa-chan/haru_2)
> is the current model: 17.0M parameters, and the first Haru to score above
> chance on KoBEST (mean 0.469 against a chance mean of 0.450, where v1.1
> scores 0.442).
>
> **v2.0 is not a drop-in replacement.** It is a different architecture and a
> different tokenizer:
>
> - v1.1 reuses three decoder cells twice; v2.0 has six independent cells.
> - v2.0 uses a separate 12k BPE tokenizer trained on a different corpus, so
>   loss and perplexity are not comparable between the two.
> - **v1.1 supports recurrent depths 2, 4 and 6. v2.0 runs at depth 6 only.**
>   If you rely on shallow-depth inference, stay on v1.1.
>
> This repository remains available for reproducibility and existing users.

Haru is a compact Korean story continuation model built with the custom CFRD
causal architecture. It has 11,634,459 parameters and supports
recurrent inference depths 2, 4, and 6.

- [Source code](https://github.com/alice-noa-chan/haru)
- [Previous Haru release](https://huggingface.co/alice-noa-chan/haru)

## Usage

Review the included Python files before enabling remote custom code.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "alice-noa-chan/haru_1.1"
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

- Parameters: 11,634,459
- Context length: 512
- Recurrent depths supervised during training: (2, 4, 6)
- Exported checkpoint step: 5750
- Training tokens seen: 753,664,000

## Evaluation

| Recurrent depth | Validation loss | Perplexity |
|---:|---:|---:|
| 2 | 2.95689 | 19.238 |
| 4 | 2.12258 | 8.353 |
| 6 | 1.92052 | 6.825 |

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
