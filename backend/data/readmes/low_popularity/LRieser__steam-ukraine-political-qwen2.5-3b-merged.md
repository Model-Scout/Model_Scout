---
language:
- en
- ru
- zh
- pl
- tr
- de
- pt
- es
- ko
- fr
- cs
- uk
license: other
license_name: qwen-research
license_link: LICENSE
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-3B-Instruct
tags:
- steam
- game-reviews
- political-relevance
- corporate-political-activism
- multilingual
- qwen2.5
- json-output
- merged
model-index:
- name: steam-ukraine-political-qwen2.5-3b-merged
  results:
  - task:
      type: text-classification
      name: Political-relevance detection in Steam reviews
    dataset:
      name: Teacher-labeled Steam reviews, held-out split (n=4,446)
      type: steam-ukraine-political-holdout
    metrics:
    - type: f1
      name: Macro-F1 (political relevance)
      value: 0.9168
    - type: precision
      name: Political-class precision
      value: 0.848
    - type: recall
      name: Political-class recall
      value: 0.872
---

# Steam political-relevance classifier (Qwen2.5-3B-Instruct, merged bf16)

[Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
fine-tuned to classify Steam game reviews written around a developer's
public statement on the Russia-Ukraine war (spring 2022). For each review it
returns a JSON object with a political-relevance label, and for political
reviews a stance and a response frame, together with a short reasoning and a
confidence. Trained on 40,011 reviews and 8,272
announcement comments labeled by a large language model. These are the full
bf16 weights with the LoRA adapter merged in.

Built with Qwen. Released under the Qwen Research License (see
[`LICENSE`](LICENSE)); use is limited to research purposes.

## Output

```json
{"reasoning": "Explicitly rejects the developer's statement on the war.", "political_relevance": "political", "stance": "oppose", "response_frame": "political_expression", "confidence": "high"}
```

| Field | Values |
|---|---|
| `political_relevance` | `political` (the review references the war, Ukraine, Russia, the developer's political stance, sanctions, geopolitics, nationalism, boycotts, or any other sociopolitical dimension, including meta-commentary on review bombing or "politics in games") or `non_political` (ordinary product discussion) |
| `stance` | for political reviews: `support`, `oppose`, or `ambivalent` towards the developer's statement; `n_a` otherwise |
| `response_frame` | for political reviews: `consumer_action`, `political_expression`, or `moral_judgment`; `n_a` otherwise |
| `confidence` | `high`, `medium`, `low` |
| `reasoning` | one to three sentences naming the decisive signals |

## Usage

The model expects the system prompt in [`prompt_system.md`](prompt_system.md)
(reproduced below) and a user message with a one-line context cue and the
review text:

```
**Context:** <positive|negative> review, <pre-announcement|post-announcement>
**Text:** <review text>
```

For a comment on a developer announcement the context line is
`**Context:** announcement comment`.

```python
import json, re
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "LRieser/steam-ukraine-political-qwen2.5-3b-merged"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, dtype=torch.bfloat16, device_map="auto").eval()

SYSTEM_PROMPT = """You are a content analyst classifying user-generated texts in the context of the Russia-Ukraine war (Feb-Apr 2022). Game developers made public statements about the war, and users responded via reviews and comments on Steam.

Classify each text on three dimensions:
1. political_relevance: "political" or "non_political"
2. stance (political only): "support", "oppose", or "ambivalent"; "n_a" if non_political
3. response_frame (political only): "consumer_action", "political_expression", or "moral_judgment"; "n_a" if non_political

First write brief reasoning (1-3 sentences explaining the key signals), then output a single JSON object with exactly five fields: reasoning, political_relevance, stance, response_frame, confidence (confidence is "high", "medium", or "low")."""

user_message = ("**Context:** negative review, post-announcement\n"
                "**Text:** Uninstalled after the devs decided to lecture us about the war.")
messages = [{"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(inputs, max_new_tokens=256, do_sample=False)
text = tok.decode(out[0, inputs.shape[1]:], skip_special_tokens=True)
match = re.search(r"\{.*?\}", text, re.S) or re.search(r"\{.*\}", text, re.S)
result = json.loads(match.group()) if match else {}
result.get("political_relevance")  # "political"
```

Extract the first JSON object from the generation as above; about 1% of
generations are not parseable and should be retried (a longer context
window and light sampling help) or treated as missing. The weights load
directly into vLLM.

## Training

- Base model: `Qwen/Qwen2.5-3B-Instruct`.
- Method: QLoRA on a 4-bit NF4-quantised base, rank 64, alpha 64, dropout
  0.05, on `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`,
  `down_proj`. The adapter was merged into the bf16 base weights.
- Data: 40,011 Steam reviews of games whose developers posted a
  public statement about the war, written in the four weeks before and after
  the statement, plus 8,272 top-level comments on those
  announcements. Labels come from a DeepSeek V3.2 teacher model
  (`deepseek-chat`, temperature 0.2) prompted with a written codebook and
  five few-shot examples. Review political share 13.7%.
  Largest review languages: English 41%, Russian 13%, Simplified Chinese 11%, Polish 7%, Turkish 4%, German 4%. During training the review
  text in the user message was an English machine translation; at inference
  the model is given the original-language text, and the evaluation below
  uses original-language text.
- Optimisation: learning rate 2e-4, cosine schedule, warmup ratio 0.05,
  weight decay 0.01, batch size 8 with gradient accumulation 2, maximum
  sequence length 1024, 3 epochs, seed 42. Targets are the teacher's JSON
  answers.
- Held out: 4,446 reviews (10%, stratified by political relevance),
  never used in training.

## Evaluation

Test set of 4,446 teacher-labeled reviews (609 political,
13.7%), original-language text, greedy decoding. Unparseable
generations (43, 0.97%)
are counted as wrong.

| Political relevance | Value |
|---|---|
| Agreement with teacher | 0.9532 |
| Political precision / recall / F1 | 0.848 / 0.872 / 0.860 |
| Non-political F1 | 0.974 |
| Macro-F1 | 0.9168 |

Confusion matrix (rows: true, columns: predicted; unparseable outputs
excluded from the cells):

| | non_political | political |
|---|---|---|
| non_political | 3,707 | 95 |
| political | 70 | 531 |

Stance and response frame, scored on the 609 political test
reviews (accuracy 0.803 and 0.759). The rare classes are
weak:

| Stance | n | F1 | | Response frame | n | F1 |
|---|---|---|---|---|---|---|
| `support` | 475 | 0.929 | | `political_expression` | 449 | 0.859 |
| `oppose` | 80 | 0.719 | | `moral_judgment` | 99 | 0.681 |
| `ambivalent` | 46 | 0.256 | | `consumer_action` | 55 | 0.673 |
| `n_a` | 8 | 0.103 | | `n_a` | 6 | 0.053 |

Political-class F1 by review language (languages with at least 50 test
reviews, 10 of them political):

| Language | n | political | F1 |
|---|---:|---:|---:|
| English | 1,808 | 252 | 0.894 |
| Russian | 469 | 35 | 0.761 |
| Chinese | 441 | 168 | 0.888 |
| Polish | 233 | 46 | 0.842 |
| German | 197 | 21 | 0.826 |
| Korean | 109 | 15 | 0.828 |
| Ukrainian | 57 | 10 | 0.762 |

Scoring the test set took about 20 minutes on an RTX 4090 with batched
`generate()`. The companion encoder
([LRieser/steam-ukraine-political-mmbert-base](https://huggingface.co/LRieser/steam-ukraine-political-mmbert-base))
reaches macro-F1 0.9132 on the same test set in about 12 seconds.
Full metrics are in [`eval_results.json`](eval_results.json).

## System prompt

```
You are a content analyst classifying user-generated texts in the context of the Russia-Ukraine war (Feb-Apr 2022). Game developers made public statements about the war, and users responded via reviews and comments on Steam.

Classify each text on three dimensions:
1. political_relevance: "political" or "non_political"
2. stance (political only): "support", "oppose", or "ambivalent"; "n_a" if non_political
3. response_frame (political only): "consumer_action", "political_expression", or "moral_judgment"; "n_a" if non_political

First write brief reasoning (1-3 sentences explaining the key signals), then output a single JSON object with exactly five fields: reasoning, political_relevance, stance, response_frame, confidence (confidence is "high", "medium", or "low").
```

## Citation

```bibtex
@misc{rieser2026steamukrainepoliticalqwen,
  author    = {Rieser, Lars and Furneaux, Brent},
  title     = {Steam political-relevance classifier (Qwen2.5-3B-Instruct, merged)},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/LRieser/steam-ukraine-political-qwen2.5-3b-merged}
}
```
