---
license: apache-2.0
language:
- ko
library_name: transformers
pipeline_tag: text-generation
base_model: cadazar/han2han-it
datasets:
- seyoungsong/Open-Korean-Historical-Corpus
- cadazar/han2han-rl-data
tags:
- han2han
- hanja
- hangul
- historical-korean
- transcription
- encoder-decoder
- reinforcement-learning
- custom_code
- flax
- orbax
---

# Han2Han RL

[Han2Han](https://github.com/cadazar/han2han) (169M parameters, encoder-decoder)
trained with reinforcement learning to convert Korean text between its two
scripts, in both directions:

- **Hangul to Hanja.** Restore the Sino-Korean characters of a mixed-script text
  from its Hangul-only reading (`조선미술` to `朝鮮美術`).
- **Hanja to Hangul.** Write a mixed-script text in Hangul only.

It is the last of three checkpoints, after
[`cadazar/han2han-pt`](https://huggingface.co/cadazar/han2han-pt) (pre-trained)
and [`cadazar/han2han-it`](https://huggingface.co/cadazar/han2han-it)
(instruction-tuned). It starts from `han2han-it` and takes its prompts the
same way. The paper ([Findings of EMNLP 2026](https://aclanthology.org/2026.findings-emnlp.2146/)) reports on the first two. This
checkpoint is follow-up work, and its sentence embeddings have not been
evaluated.

## What to expect

On 256 sentences from 1920s newspapers, held out from the reinforcement
learning, greedy decoding:

| | `han2han-it` | this model |
| --- | --- | --- |
| **Hangul to Hanja**: share of the original Hanja restored | 0.31 | 0.63 |
| sentences restored without any error | 1% | 6% |
| **Hanja to Hangul**: share of the Hanja read correctly | 0.89 | 0.93 |
| sentences transcribed without any error | 34% | 50% |
| outputs that end on their own (to Hanja / to Hangul) | 99% / 100% | 100% / 100% |
| the demo article (1922, 478 characters, held out of every split) in chunks of at most 120 characters: Hanja restored | 0.81 | 0.86 |

Restoring Hanja is the hard direction. The Hangul reading does not say which of
several same-sounding characters was meant, and the model has to choose from
context. Most restored sentences therefore contain at least one wrong
character, and the output needs checking against a source before it is quoted.
The errors that remain:

- **Homophones.** A character with the right sound and the wrong meaning
  (`轉死` for `轉寫`, `情書` for `情緖`).
- **Proper names**, which context does not decide (`綠香展` for `綠鄕展`).
- **Words left in Hangul** (`단순` for `單純`).
- **Substituted words.** Occasionally a different word in place of the
  original (`創作` for `習作`), which changes the reading as well.

Sampling at temperature 0.6 scores below greedy decoding in both directions
(0.60 and 0.91). A second training run with another seed and another held-out
split reached 0.67 and 0.92, so differences of a few points between runs are
noise.

The newspapers these sentences come from were part of pre-training, so the
text is held out from the fine-tuning stages, not unseen by the model.

## Usage

The model needs `torch` and `transformers` (tested with torch 2.14.1 and
transformers 5.18.0 on CPU). `trust_remote_code=True` is needed because the
model class ships in this repo.

The task prompt goes in the system message and the text alone in the user
message, as in `han2han-it`. The reinforcement learning used one wording per
direction, so use them as written.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "cadazar/han2han-rl"
tokenizer = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(repo, trust_remote_code=True).eval()

TO_HANJA = "한글을 한자로 전사하시오:"
TO_HANGUL = "한자를 한글로 전사하시오:"


def convert(task_prompt, text):
    messages = [
        {"role": "system", "content": task_prompt},
        {"role": "user", "content": text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
    )
    budget = 2 * len(tokenizer(text).input_ids) + 8
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=budget, do_sample=False)
    return tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True)


hangul = (
    "단순한 스케치나 카메라적 전사가 아니라 작가의 예술적 정서의 전체적인 안계로 "
    "이루어지는 가장 사실적인 표현을 말하는 것이다."
)
hanja = convert(TO_HANJA, hangul)
print(hanja)
# 단순한 스케치나 카메라的 轉死가 아니라 作家의 藝術的 情書의 全體的인 眼界로
# 이루어지는 가장 事實的인 表現을 말하는 것이다.
print(convert(TO_HANGUL, hanja))
# 단순한 스케치나 카메라적 전사가 아니라 작가의 예술적 정서의 전체적인 안계로
# 이루어지는 가장 사실적인 표현을 말하는 것이다.
```

The outputs are shown as generated (each is one line). The original sentence
reads `單純한 스케치나 카메라的 轉寫가 아니라 作家의 藝術的 情緖의 全體的인
眼界로 이루어지는 가장 寫實的인 表現을 말하는 것이다.`. The model left `단순`
in Hangul and chose same-sounding characters for three words (`轉死`, `情書`,
`事實的`). `han2han-it` returns this sentence in Hangul, unchanged.

- **Length.** The reinforcement learning used single sentences of 10 to 120
  characters. Longer input works (the first 478 characters of a 1922 article
  come back with 84% of their Hanja, the same as `han2han-it`), but for long
  texts it is safer to split at sentence boundaries into pieces of a few
  hundred characters and convert each piece.
- **Token budget.** A correct answer needs at most about 1.7 times the tokens
  of its input, so `2 * input tokens + 8` leaves room and stops a runaway
  output.
- **Thinking.** The chat template accepts `enable_thinking=True`, but neither
  this model nor `han2han-it` learned a separate reasoning step. Leave it off.
- **Other tasks.** Rows of the instruction-tuning data were replayed during
  the reinforcement learning to keep its other behavior in place (the loss on
  held-out rows of that data went from 2.39 to 2.11), but only transcription
  was evaluated.

### Serving

The model works with the `transformers` server and its chat client:

```bash
transformers serve --trust-remote-code
transformers chat cadazar/han2han-rl --system-prompt "한글을 한자로 전사하시오:"
```

`AutoModelForCausalLM` loads `Han2HanForCausalLM`, a wrapper that takes the
rendered chat prompt as one sequence and returns the prompt followed by the
reply. `AutoModelForSeq2SeqLM` loads the encoder-decoder itself. The
[`han2han-it` model card](https://huggingface.co/cadazar/han2han-it) describes
both, the prompt format, and the tokenizer.

## Training

GRPO from `han2han-it` (`main`), 300 steps, all weights trained in fp32:

- **Prompts.** 39,495 newspaper sentences from the training split of the
  sentence-level transcription set, half of the prompts in each direction, 16
  prompts with 8 answers each per step, sampled at temperature 0.7, learning
  rate 5e-6. The pool was deduplicated against the validation and test
  splits, which hold the evaluation sentences above and the paper's
  transcription evaluation, so the model was not trained on either.
- **Rewards** are rules, with no judge model. They check that the output ends
  on its own, has the length of its input, restores the original Hanja (or
  reads them correctly), reads back to its input, and does not repeat itself.
- **Keeping the rest in place.** A KL penalty to the starting model, and a
  supervised loss on replayed instruction-tuning rows at half weight.

The reinforcement-learning stage is in the GitHub repo under `rl/` (the rewards, the JAX trainer, the
optimizer recipe and the command that produced this checkpoint). The orbax checkpoint it saved is this repo's
[`flax` revision](https://huggingface.co/cadazar/han2han-rl/tree/flax) (step 300, with the run's logs under
`run/`; `hf download cadazar/han2han-rl --revision flax --local-dir han2han-rl-flax`), its start the
`flax` revision of [`cadazar/han2han-it`](https://huggingface.co/cadazar/han2han-it/tree/flax), and the data a public re-run
reads is [`cadazar/han2han-rl-data`](https://huggingface.co/datasets/cadazar/han2han-rl-data) (the
run's own pool and held-out sentences cannot be redistributed, so the dataset card gives the numbers on
its public evaluation sentences).

## Files

| File | Contents |
| --- | --- |
| `model.safetensors` | fp32 weights, 169.2M parameters, plus the `jbu` / `cbu` subword bucket tables |
| `config.json`, `generation_config.json` | model and generation config, with `auto_map` entries for the Auto classes |
| `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja` | fast tokenizer (38400 pieces) and chat template, the same as in `han2han-it` |
| `spiece.model` | the SentencePiece model `tokenizer.json` was built from |
| `modeling_han2han.py`, `han2han_config.py` | modeling code from the GitHub repo at commit [`af1330e`](https://github.com/cadazar/han2han/commit/af1330e49f1edf46e26b63937724ddbaeffc3bee), the same files as in `han2han-it` |

## Citation

Published in Findings of the Association for Computational Linguistics: EMNLP 2026 (Budapest),
pages 45857-45876: https://aclanthology.org/2026.findings-emnlp.2146/

```bibtex
@inproceedings{adams-etal-2026-han2han,
    title = "{H}an2{H}an: Efficient Language-Specific Character Representation through Script-Aware Pre-Training for Historical Text Analysis",
    author = "Adams, Cellik  and
      Jo, EunKyoung  and
      Kim, Juae",
    editor = "Lee, Hung-Yi  and
      Dev, Sunipa  and
      Li, Jessy  and
      Elliott, Desmond",
    booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {EMNLP} 2026",
    month = oct,
    year = "2026",
    address = "Budapest, Hungary",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.findings-emnlp.2146/",
    pages = "45857--45876",
    ISBN = "979-8-89176-462-0"
}
```

## License

Apache License 2.0, the same as the [GitHub repo](https://github.com/cadazar/han2han).
