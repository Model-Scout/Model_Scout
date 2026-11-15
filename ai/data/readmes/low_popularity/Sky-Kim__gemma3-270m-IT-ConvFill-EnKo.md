---
license: gemma
base_model:
- vysri/gemma3-270m-IT-ConvFill
language:
- en
- ko
pipeline_tag: text-generation
library_name: transformers
datasets:
- zenglhardt/convfill-dataset
- Sky-Kim/convfill-dataset-ko
tags:
- gemma3
- conversational-infill
- convfill
- voice-agent
- korean
- on-device
---

# gemma3-270m-IT-ConvFill-EnKo

A bilingual (English + Korean) **conversational infill** Talker: a 270M model that starts speaking right away
and works in the knowledge a large backend model streams in, so a voice agent's first words don't wait on the
backend (*Thinking While Speaking*, [arXiv:2511.07397](https://arxiv.org/abs/2511.07397)).

It is [vysri/gemma3-270m-IT-ConvFill](https://huggingface.co/vysri/gemma3-270m-IT-ConvFill) (English) further
fine-tuned on the Korean translation of the ConvFill data plus English replay, so it now answers Korean users in
natural spoken Korean while keeping English.

| | this model | vysri/gemma3-270m-IT-ConvFill |
|---|---|---|
| Korean outputs in Korean | **100%** | 54% (answers the rest in English) |
| Korean held-out loss | **1.371** | 2.597 |
| English knowledge → speech chrF | 63.9 | 65.3 |
| Names copied verbatim (EN / Latin names in KO) | 91.3% / 88.8% | 95.3% / 97.3% |

## How it works

Each call produces one spoken sentence. The prompt holds the conversation, what the Talker has already said this
turn, and one **knowledge** slot: either a sentence from the backend (the Talker rephrases it into speech) or
`<sil>` (nothing has arrived yet, so the Talker says a short, content-free filler).

```
<bos><start_of_turn>user
{previous user turn}<end_of_turn>
<start_of_turn>model
{previous spoken reply}<end_of_turn>
<start_of_turn>user
{current user turn}<end_of_turn>
<start_of_turn>model
{sentences already said this turn, joined by spaces}<end_of_turn>
<start_of_turn>knowledge
{one backend sentence, or <sil>}<end_of_turn>
<start_of_turn>model
```

The previous-exchange block is only present from the second turn on, and the "already said" block only once
something has been said. `<sil>` is an added special token (id 262145, vocab 262146). Generation stops at
`<end_of_turn>`. This is the same template as the English ConvFill model; it is not the Gemma chat template.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "Sky-Kim/gemma3-270m-IT-ConvFill-EnKo"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, torch_dtype=torch.float32).eval()

def talk(user, said, knowledge="<sil>"):
    p = f"<start_of_turn>user\n{user}<end_of_turn>\n"
    if said:
        p += f"<start_of_turn>model\n{' '.join(said)}<end_of_turn>\n"
    p += f"<start_of_turn>knowledge\n{knowledge}<end_of_turn>\n<start_of_turn>model\n"
    ids = tok(p, return_tensors="pt").input_ids  # adds <bos>
    out = model.generate(ids, max_new_tokens=64, do_sample=False,
                         eos_token_id=tok.convert_tokens_to_ids("<end_of_turn>"))
    return tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True).strip()

user = "냉장고에 계란이랑 김치가 있는데 뭘 만들 수 있을까요?"
said = [talk(user, [])]                                    # filler while the backend is thinking
said.append(talk(user, said, "김치와 계란으로 김치계란찜을 만들 수 있어요."))  # backend sentence arrives
print(said)
```

In a full agent the backend's reply is split into sentences as it streams; each becomes one `knowledge` call, and
`<sil>` calls fill the gap until the first one arrives. The backend should be told to write short sentences, to
not greet the user (the Talker's filler already does), and, for Korean, to write numbers in Hangul words.

## Training

- **Init:** `vysri/gemma3-270m-IT-ConvFill`. Full fine-tune, recipe from
  [vysri/conversational-infill](https://github.com/vysri/conversational-infill) (template, loss on the current
  response only, AdamW lr 1e-4, wd 0.01, warmup 200, effective batch 16), except **10,000 steps with a cosine decay
  to zero**.
- **Data:** ConvFill English (`zenglhardt/convfill-dataset`) and Korean (`Sky-Kim/convfill-dataset-ko`),
  275,950 steps per language. 5% of conversations were held out per domain, and the same conversations were held
  out in both languages.
- **Hardware:** Apple M5 Max (MPS), bf16 autocast with fp32 master weights, 1 h 10 min.
- **Stored weights:** bf16, like the initial checkpoint (name-copy rates unchanged from the fp32 weights: EN 91.1% vs
  91.3%, KO 88.8% vs 88.8%).
- **Why the short schedule:** continuing for a full epoch at the recipe's schedule (which only decays to ~85% of
  the peak lr) eroded the reference model's ability to copy proper nouns verbatim (EN 95% → 86%). Ten thousand steps
  decaying to zero kept most of it while still learning Korean.

## Evaluation (held-out conversations, per language)

| | English | Korean |
|---|---|---|
| Loss, all steps (14,621 per language) | 1.276* | 1.371 |
| Knowledge → speech chrF vs reference | 63.9 | 52.7 |
| Knowledge content-word coverage | 0.875 | 0.920 |
| `<sil>` filler states a fact not yet given (reference data: 7.5% / 13.5%) | 5.0% | 7.0% |
| Output in the expected script | 100% | 100% |
| Repetitive / empty outputs | 0 / 0 | 0 / 0 |

\* The English figure is optimistic: the initial checkpoint was trained on most of these English conversations.
Generation metrics use greedy decoding on 200 knowledge and 200 `<sil>` steps per language.

## Limitations

- 270M parameters: on long knowledge sentences it can drift (repeat a phrase, split or misspell a rare name).
  Keep backend sentences short.
- Proper nouns are copied verbatim less reliably than by the English-only model (see the table above).
- It only rephrases what the backend gives it; it does not check facts. Errors in the knowledge are spoken as given.
- The Korean data is machine-translated from the English set and inherits its domains (advice, assistant,
  task-oriented dialogue, education, medical, planning, support).

## On-device (Unity Sentis)

The Unity Inference Engine (Sentis) build is the package
[`com.sky.sentis.gemma3-270m-it-convfill-enko`](https://huggingface.co/Sky-Kim/com.sky.sentis.gemma3-270m-it-convfill-enko)
(FP16 `.sentis`, 872 MB; ONNX Runtime matches PyTorch to 1.5e-5 on logits, Sentis matches ONNX Runtime token for
token), and [skykim/convfill-unity](https://github.com/skykim/convfill-unity) is the voice-agent demo. In that
demo on an M5 Max (Sentis GPUCompute, gpt-oss:120b as the backend, Piper TTS), the first audio of a turn came after
0.34 s (English) and 0.36 s (Korean) on average, against 1.23 s and 1.16 s when speaking only the backend's
sentences.

## License and attribution

Gemma is provided under and subject to the Gemma Terms of Use found at
[ai.google.dev/gemma/terms](https://ai.google.dev/gemma/terms). Use of this model must follow those terms and the
[Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy).

Trained on [zenglhardt/convfill-dataset](https://huggingface.co/datasets/zenglhardt/convfill-dataset) and
[Sky-Kim/convfill-dataset-ko](https://huggingface.co/datasets/Sky-Kim/convfill-dataset-ko) (CC BY-SA 4.0, a Korean
translation of the former). Starts from [vysri/gemma3-270m-IT-ConvFill](https://huggingface.co/vysri/gemma3-270m-IT-ConvFill).

```bibtex
@misc{srinivas2026thinkingspeakinginferencetimeknowledge,
      title={Thinking While Speaking: Inference-Time Knowledge Transfer for Responsive and Intelligent Conversational Voice Agents},
      author={Vidya Srinivas and Zachary Englhardt and Vikram Iyer and Shwetak Patel},
      year={2026},
      eprint={2511.07397},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2511.07397},
}
```
