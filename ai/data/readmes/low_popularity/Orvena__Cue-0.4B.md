---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B-Base
library_name: coreml
pipeline_tag: text-classification
language:
- bg
- cs
- da
- de
- el
- en
- es
- et
- fi
- fr
- hi
- hr
- hu
- id
- it
- ja
- ko
- lt
- lv
- nl
- pl
- pt
- ro
- ru
- sk
- sl
- sv
- tr
- uk
- vi
tags:
- turn-taking
- barge-in
- voice-assistant
- duplex
- coreml
- neural-engine
- on-device
- multilingual
---

# Cue-0.4B

Cue decides what a person means when they speak to a voice assistant. It is the model behind interruptions and
instant replies in [Orvena](https://orvena.app)'s voice mode, and it runs on the iPhone's Neural Engine in about
10 ms, so the GPU stays free for the assistant's own language model.

It answers two questions.

**While the assistant is talking**, someone says something. Should it keep going, stop, or treat it as a new
request? For a request, Cue also points at the word where the request starts, so "hold on, remind me to call the
vet at 10" becomes "remind me to call the vet at 10". A quiet "mm-hm" keeps the assistant talking; "wait, stop"
stops it.

**When the assistant is idle**, a new turn arrives. Does it need the main model, or is it one of nine things the
assistant can answer at once: checking it can hear you, a greeting, thanks, a bare acknowledgement, never mind,
hold on, asking it to repeat, goodbye, or how are you? Cue sees the assistant's last sentence, so a "yes" or "thanks"
that answers its question still goes to the main model.

Cue works in 30 languages. The [technical report](Cue-0.4B-technical-report.pdf) covers the data, training and evaluation in full.

## How it is built

Cue is the first 14 of the 28 layers of [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base) with a
LoRA adapter (rank 16 on every linear layer, merged into these weights) and three small heads on the last token:

- an **action** head: keep going, stop, request;
- a **pointer** head over the user's word starts, for where a request begins;
- an **intent** head: the main model or one of the nine quick intents.

![The prompt goes through the Qwen3 tokenizer and an int8 embedding lookup into the Core ML package, where 14 decoder layers feed the action, intent and pointer heads; the app turns their calibrated outputs into a decision.](figures/cue-architecture.png)

The idea of an action head with a pointer on a small language model comes from
[Kev](https://github.com/jaredpalmer/kev) by Jared Palmer. Cue is our own model trained on our own data, and the
new-turn head, the languages and the Neural Engine packaging are new.

The training data is about 63,000 examples composed from phrase banks written for each language: what an assistant
says, backchannels, stops, requests, side talk, the quick intents, and more than 4,000 look-alikes that share their
words but need the main model ("cancel my 3 pm meeting", "thanks, now add milk", "say that again but shorter").
Speech recognizer noise is simulated by dropping punctuation and case and repeating words. The phrase banks, the
composed examples and both test sets are published as
[Orvena/Cue-0.4B-data](https://huggingface.co/datasets/Orvena/Cue-0.4B-data).

## Results

Both test sets were written separately from the training data, by writers who never saw the phrase banks, in
all 30 languages. The numbers are from the Core ML package with the thresholds below.

| Interruptions (900 examples) | |
|---|---|
| Right decision | 90.4% |
| Stopped when the user only acknowledged | 11.0% |
| Kept talking through a stop | 10.8% |
| Missed a request | 4.4% |
| Request start on the labelled word (requests it got right) | 92.6% |

![Interruption decisions on the 900 test examples: 89% of keep-goings, 86% of stops and 94% of requests decided right.](figures/cue-interruptions.png)

| New turns (1,800 examples) | |
|---|---|
| Right decision | 95.2% |
| Requests for the main model answered as a quick intent | 0.1% (1 of 990) |
| Quick intents sent to the main model | 10.4% |
| Quick intent answered with the wrong one | 0.25% |

![New turns on the test set: 989 of 990 requests go to the main model; each quick intent is answered at once in 72 to 88 of 90 cases, and almost everything else goes to the main model.](figures/cue-new-turns.png)

The test sets have 30 examples per language for interruptions and 60 for new turns, so a single language's score
moves by a few points with one example:

![Right decisions per language for Cue-0.4B and the 28-layer model trained the same way.](figures/cue-languages.png)

On an iPhone 17 Pro Max, one forward pass takes about 8 ms on the Neural Engine and about 10 ms while the GPU is
busy generating, and its Core ML files take about 380 MB. On the same tests, all 28 layers score about one point higher.
The Neural Engine is what keeps it fast while the main model runs: the full 28-layer model on the GPU goes from 42 ms
to 890 ms once the main model is decoding there.

![One forward pass on an iPhone 17 Pro Max: Cue on the Neural Engine takes 8.2 ms idle and 10.5 ms while the GPU decodes; the 28-layer model takes 18.6 and 23.4 ms on the Neural Engine, 42 and 890 ms on the GPU, 104 and 523 ms on the CPU.](figures/cue-latency.png)

## Using it

### Prompts

Interruptions, with up to 16 words before and 12 after the point the assistant had reached (40 and 24 characters for
Japanese). `speaking` means the user started before the sentence ended, `finished` after it:

```
Orvena speaking: … the forecast for Porto shows light | rain after four, so bring a jacket.
User: ok got it, now check Lisbon
Decision:
```

New turns, with the last 16 words (40 characters for Japanese) of what the assistant said, or nothing at the start
of a conversation:

```
Orvena said: Should I add it to your calendar?
User: yes please
Reply:
```

Prompts are at most 128 tokens. Longer ones drop the assistant's words, farthest from the user's first.

### Decisions

Scale the logits by the temperatures in `config.json` (`temperature` for actions, `intent_temperature` for intents)
before the softmax.

- Keep going only when its probability is at least `keep_talking_threshold` (0.7); otherwise take the larger of
  stop and request.
- For the request start, take the earliest word whose pointer probability is at least `safe_pointer` (0.15), or
  the most likely one if it comes first. Keeping an extra "okay" is better than dropping a word.
- Answer a quick intent only when its probability is at least `quick_threshold` (0.9); everything else goes to the
  main model. Orvena asks for 0.97 before a goodbye closes voice mode.

![The pointer's probability for each word the user said, for "hold on, remind me to call the vet at 10" and "ok got it, now check Lisbon": the request starts at "remind" and at "now".](figures/cue-pointer.png)

### Python

`cue.py` builds the prompts and makes the decisions with PyTorch and Transformers:

```python
from cue import Cue

cue = Cue.from_pretrained(".")
cue.interruption("The forecast for Porto shows light rain after four, so bring a jacket.",
                 spoken=20, speaking=True, transcript="ok got it, now check Lisbon", language="en")
# {'action': 'request', 'request': 'now check Lisbon', ...}
cue.new_turn("It will be sunny tomorrow, around 18 degrees.", "thank you", language="en")
# {'intent': 'thanks', 'confidence': 0.996}
```

### Core ML

`TurnDecision.mlpackage` is the int8 model for the Neural Engine (iOS 18 and macOS 15 or later). The token
embedding lookup stays outside the model to keep it small: `token-embeddings.int8` holds one int8 row per token
(151,936 × 1,024) and `token-embedding-scales.f32` one float scale per row.

| Input | Shape | |
|---|---|---|
| `inputs_embeds` | 1 × 128 × 1024, float16 | token rows times their scales, padded with the pad token's row |
| `decide_mask` | 1 × 128, float16 | 1 at the last prompt token, 0 elsewhere |

| Output | Shape | |
|---|---|---|
| `action_logits` | 1 × 3 | keep going, stop, request |
| `intent_logits` | 1 × 10 | the main model, then the nine quick intents in `turn-decision.json` order |
| `pointer_logits` | 1 × 128 | per token; use the word starts inside the user's text |

`turn-decision.json` holds the thresholds and windows, `tokenizer.json` is Qwen3's tokenizer, and `fixtures.json`
and `turn-fixtures.json` are reference decisions from the Core ML package for checking a port. `cue.py` with the
float weights makes the same decision on 122 of the 123 interruption fixtures and 119 of the 120 new-turn fixtures;
the others sit right at a threshold.

## Notes

- Cue reads the speech recognizer's transcript, so it judges what was said rather than how it was said.
- The quick intents are deliberately narrow: anything that contains a request goes to the main model.
- The prompts use the assistant name "Orvena".

## License

Apache-2.0, like the Qwen3 base model. Built by Orvena.
