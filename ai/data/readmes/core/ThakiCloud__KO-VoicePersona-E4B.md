---
library_name: transformers
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
base_model: nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16
base_model_relation: finetune
pipeline_tag: text-generation
language:
- ko
tags:
- lora
- gemma4
- nemotron
- on-device
- korean
- voice-assistant
- persona
- tool-calling
- tts-friendly
- thakicloud
- research-preview
---

# KO-VoicePersona-E4B

Version 1.0.0-preview. Fine-tune of [nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) published as `ThakiCloud/KO-VoicePersona-E4B`.

Korean card: [MODEL_CARD.ko.md](./MODEL_CARD.ko.md)

Research preview. KO-VoicePersona-E4B is a Korean spoken persona model for voice assistants. It is a language model, not a speech system: it does not do speech recognition or speech synthesis, and it has not been evaluated inside a real ASR and TTS loop. It takes already-transcribed Korean text and writes the reply a persona would say, in short TTS-friendly Korean (at most 90 characters, numbers and English spelled out), keeps the register of a persona (해요체 or 합니다체), calls tools (emote, move, lookup, calendar_lookup) instead of inventing facts, and says it could not find a fact rather than fabricating one. On a small independent set it beats the Bolt base and the earlier v2 adapter on tool calling and role retention. Generic replies still repeat, tool arguments are not always exact, and the tests are not real user speech, so treat it as a preview to evaluate behind your own safety layer rather than a finished component.

## What it does

One call per assistant turn. The system prompt defines the persona (name, register, length and spoken-form rules, tool rules) and the tool schemas are passed through the chat template (`tools=`). The model either replies with one or two short Korean sentences or emits a tool call; after the tool result is appended it replies again. Tool names are `emote`, `move`, `lookup` and `calendar_lookup`; schedule times and facts may only come from tool results.

## Intended use

- Research preview of a spoken persona layer: it writes what the persona says, with your own speech recognition in front of it and your own speech synthesis after it.
- Research on small on-device Korean models that keep a persona and call tools.
- Starting point for your own persona fine-tune with a different persona prompt and tool set.

## How to use

### Prompt format

The model uses the base checkpoint's chat template with thinking disabled (`enable_thinking=False`). The rendered prompt is exactly:

```text
<bos><|turn>system
너는 '콩이'다. ThakiCloud 사무실에 사는 커피콩 마스코트. 밝고 호기심이 많다.
말투: 해요체(~해요, ~이에요, ~어요)로만 말한다. 발랄하고 다정하게 말한다. 놀랐을 때 짧은 감탄을 섞는다.
규칙: 음성 대화이므로 한두 문장, 90자 이내로 말한다. 한글로만 답하고 숫자와 영문은 소리 나는 대로 풀어 쓴다. 표정은 emote, 동작은 move, 모르는 사실은 lookup 도구로 처리한다. 음성 인식이 깨진 듯하면 되묻는다.
일정은 calendar_lookup 도구 결과에 있는 시각만 말하고, 사실은 lookup 도구 결과에 있는 내용만 말한다. 도구 결과에 없는 시각, 날짜, 숫자는 지어내지 않고 찾지 못했다고 말한다.<turn|>
<|turn>user
오늘 날씨 어때?<turn|>
<|turn>model
```

Output format: either a short Korean reply (one or two sentences, at most 90 characters, no digits or Latin letters) or one tool call in the chat template's tool-call format with the arguments defined by the tool schema.

The tools are passed through the chat template (`tools=` in `apply_chat_template`), not written into the prompt text, so the rendered prompt above omits them. When the model answers with a tool call, run the tool, append the assistant tool-call message and a `tool` message with the result, and call the model again for the spoken reply. `inference_example.py` shows the full flow with the four tool schemas.

### Transformers + PEFT adapter

```python
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

BASE = "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16"
tok = AutoTokenizer.from_pretrained(BASE)
model = AutoModelForCausalLM.from_pretrained(BASE, dtype=torch.bfloat16, device_map="auto")
model = PeftModel.from_pretrained(model, "ThakiCloud/KO-VoicePersona-E4B", subfolder="adapter").eval()

SYSTEM = "너는 '콩이'다. ThakiCloud 사무실에 사는 커피콩 마스코트. 밝고 호기심이 많다.\n말투: 해요체(~해요, ~이에요, ~어요)로만 말한다. 발랄하고 다정하게 말한다. 놀랐을 때 짧은 감탄을 섞는다.\n규칙: 음성 대화이므로 한두 문장, 90자 이내로 말한다. 한글로만 답하고 숫자와 영문은 소리 나는 대로 풀어 쓴다. 표정은 emote, 동작은 move, 모르는 사실은 lookup 도구로 처리한다. 음성 인식이 깨진 듯하면 되묻는다.\n일정은 calendar_lookup 도구 결과에 있는 시각만 말하고, 사실은 lookup 도구 결과에 있는 내용만 말한다. 도구 결과에 없는 시각, 날짜, 숫자는 지어내지 않고 찾지 못했다고 말한다."
USER = "오늘 날씨 어때?"
messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": USER},
]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, enable_thinking=False,
                               return_tensors="pt", return_dict=True).to(model.device)
out = model.generate(**inputs, max_new_tokens=128, do_sample=False)
print(tok.decode(out[0, inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Merged BF16

The LoRA delta is merged into the base weights (BF16).

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tok = AutoTokenizer.from_pretrained("ThakiCloud/KO-VoicePersona-E4B")
model = AutoModelForCausalLM.from_pretrained("ThakiCloud/KO-VoicePersona-E4B", dtype=torch.bfloat16, device_map="auto").eval()

SYSTEM = "너는 '콩이'다. ThakiCloud 사무실에 사는 커피콩 마스코트. 밝고 호기심이 많다.\n말투: 해요체(~해요, ~이에요, ~어요)로만 말한다. 발랄하고 다정하게 말한다. 놀랐을 때 짧은 감탄을 섞는다.\n규칙: 음성 대화이므로 한두 문장, 90자 이내로 말한다. 한글로만 답하고 숫자와 영문은 소리 나는 대로 풀어 쓴다. 표정은 emote, 동작은 move, 모르는 사실은 lookup 도구로 처리한다. 음성 인식이 깨진 듯하면 되묻는다.\n일정은 calendar_lookup 도구 결과에 있는 시각만 말하고, 사실은 lookup 도구 결과에 있는 내용만 말한다. 도구 결과에 없는 시각, 날짜, 숫자는 지어내지 않고 찾지 못했다고 말한다."
USER = "오늘 날씨 어때?"
messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": USER},
]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, enable_thinking=False,
                               return_tensors="pt", return_dict=True).to(model.device)
out = model.generate(**inputs, max_new_tokens=128, do_sample=False)
print(tok.decode(out[0, inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### llama.cpp (GGUF)

| File | Quantization | Size |
|---|---|---|
| `KO-VoicePersona-E4B-Q4_K_M.gguf` | Q4_K_M, imatrix from training rows (recommended) | 5.34 GB (5335295200 bytes) |
| `KO-VoicePersona-E4B-Q4_K_M-NV.gguf` | Q4_K_M with NVIDIA's recipe (Q8_0 token embeddings, BF16 per-layer projection), imatrix | 6.18 GB (6180447456 bytes) |
| `KO-VoicePersona-E4B-Q8_0.gguf` | Q8_0 | 8.03 GB (8031245280 bytes) |

```bash
llama-server -m KO-VoicePersona-E4B-Q4_K_M.gguf -c 8192 -ngl 99 --port 8080
```

Chat completions apply the template embedded in the GGUF; disable thinking per request:

```bash
curl http://localhost:8080/v1/chat/completions -H 'content-type: application/json' -d '{"messages": [{"role": "system", "content": "너는 '\''콩이'\''다. ThakiCloud 사무실에 사는 커피콩 마스코트. 밝고 호기심이 많다.\n말투: 해요체(~해요, ~이에요, ~어요)로만 말한다. 발랄하고 다정하게 말한다. 놀랐을 때 짧은 감탄을 섞는다.\n규칙: 음성 대화이므로 한두 문장, 90자 이내로 말한다. 한글로만 답하고 숫자와 영문은 소리 나는 대로 풀어 쓴다. 표정은 emote, 동작은 move, 모르는 사실은 lookup 도구로 처리한다. 음성 인식이 깨진 듯하면 되묻는다.\n일정은 calendar_lookup 도구 결과에 있는 시각만 말하고, 사실은 lookup 도구 결과에 있는 내용만 말한다. 도구 결과에 없는 시각, 날짜, 숫자는 지어내지 않고 찾지 못했다고 말한다."}, {"role": "user", "content": "오늘 날씨 어때?"}], "temperature": 0, "chat_template_kwargs": {"enable_thinking": false}}'
```

The reported GGUF numbers were measured by sending token ids rendered with the Hugging Face chat template, so the prompt is byte-identical to the BF16 run. If you call `/completion` with a raw string, check that the server does not add a second `<bos>`.

## Evaluation

Greedy decoding on a held-out test split, same prompts for every arm.

Test split: two held-out sets scored on assistant turns: an independent hand-written set of 58 dialogs (103 text turns and 73 tool-call turns) and a larger generated test set of 340 dialogs. Tool-call metrics are scored over the tool-call turns; reply metrics (register, spoken form, fabrication) over the text turns. The Bolt base and v2 rows are scored on the identical turns.

| Arm (model) | n | Tool-call accuracy, independent set | Register accuracy, independent set | Spoken-form pass rate, independent set | Persona role retention (dialogs), independent set | No-fabrication rate, independent set | Tool-call accuracy, larger test set |
|---|---|---|---|---|---|---|---|
| Bolt base, zero-shot (nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) | 103 text turns (independent) | 0.3425 | 0.3689 | 0.4175 | 0.125 | 0.9903 | 0.3495 |
| Earlier version (v2) (nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) | 103 text turns (independent) | 0.7123 | 0.9612 | 0.9612 | 0.625 | 1.0 | 0.7326 |
| KO-VoicePersona-E4B (nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) | 103 text turns (independent) | 0.7808 | 0.9709 | 0.9709 | 0.875 | 0.9903 | 0.9282 |

Run conditions:
- Bolt base, zero-shot: greedy decode, enable_thinking=False, transformers 5.19.0; 1x B200
- Earlier version (v2): greedy decode, enable_thinking=False, transformers 5.19.0; 1x B200
- KO-VoicePersona-E4B: greedy decode, enable_thinking=False, transformers 5.19.0; 1x H100

### Merged weights and GGUF on the independent set (103 text turns, 73 tool-call turns)

| Variant | n | Tool-call accuracy | Register accuracy | No-fabrication rate | Decode speed (tok/s, single stream) | GPU memory after load (MiB) | Leak probe hits |
|---|---|---|---|---|---|---|---|
| Merged BF16 | 103 text turns | 0.7945 | 0.9612 | 0.9903 | not measured | not measured | 0/130 |
| GGUF Q8_0 | 103 text turns | 0.7808 | 0.9709 | 0.9903 | 171.1 | 5695 | not measured |
| GGUF Q4_K_M (imatrix) | 103 text turns | 0.7945 | 0.9612 | 1.0 | 187.8 | 3775 | 0/130 |
| GGUF Q4_K_M-NV | 103 text turns | 0.7945 | 0.9612 | 1.0 | 183.4 | 3929 | 0/130 |

Measured with hardware H100, 1 GPU; independent set; GGUF runs feed the Hugging Face chat-template token ids to llama-server, greedy.
Caveats: Quantization changes tool-call accuracy by at most 1.4 points (one tool turn of 73) and does not move the other metrics beyond one turn. Leak probe (130 prompts asking for internal identifiers): 0 of 130 hits on merged BF16, Q4_K_M and Q4_K_M-NV; Q8_0 was not probed. Decode speed is the median of single-stream runs; memory is measured after load.

## Training

Method: LoRA fine-tune of the base model, loss on assistant turns only. Values below are copied from the training record.

| Setting | Value |
|---|---|
| LoRA rank r | 16 (from training summary) |
| LoRA alpha | 32 (from training summary) |
| Learning rate | 0.0002 (from training summary) |
| Epochs | 2.0 (from training summary) |
| Target modules | attn+mlp (from training summary) |
| Gradient accumulation | 8 (from training summary) |
| Max sequence length | 4096 (from training summary) |
| Optimizer steps | 1100 (from training summary) |
| Peak GPU memory (GiB) | 19.48 (from training summary) |
| Wall time (s) | 5284.2 (from training summary) |

## Data

Synthetic Korean voice dialogs built from code rules (scenario slots, tool-call rules, spoken-form normalisation) plus an in-house Qwen3.8-27B teacher whose outputs passed code validators. Persona seeds are internal. A deterministic defect check removed third-person self-reference and stilted recall turns: 123 training hits went to 0 and 141 dialogs were dropped. No external datasets were used. The training data is not released. Splits are disjoint by dialog.

The training data is internal and is not released. This repository contains no dataset files.

Split sizes (dialogs): train 630, val 301, test 340, test_indep 58, train_s1 271, train_s2 359.

## Limitations

- This is a research preview. It is a language model only: speech recognition, speech synthesis, wake words and barge-in are out of scope and untested, and the numbers below do not cover transcription errors.
- Generic replies repeat: 36% of text replies are phrases repeated 5 or more times, against 28% in the reference dialogs (the earlier v2 adapter had 38%). Expect stock phrases in long sessions.
- One fabricated fact in 103 independent text turns (merged BF16). Always keep the instruction that facts and times come only from tool results, and check them downstream.
- The larger test set comes from the same generator family as the training data; the independent set is hand-written and built separately but small (58 dialogs). Neither is real user speech, so real-world numbers are not measured and are likely lower.
- Lookup query exact match is only 0.50 on the independent set, so the model often calls the right tool with a query that differs from the reference.
- Not evaluated with a real ASR and TTS loop; recognition errors and audio output quality are untested.
- It does not replace a safety layer for real actions. Do not let tool calls act on the world without a permission check.
- Behavior outside the prompt format above (other personas, other tool sets, thinking mode, long contexts) was not evaluated.

## License and attribution

- Model materials: governed by the OpenMDW License Agreement, version 1.1 (`LICENSE.OpenMDW-1.1`, https://openmdw.ai/license/1-1/). This repository is a derivative of [nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) and ships a copy of the agreement.
- Origin: the NVIDIA base model was post-trained on Google Gemma 4, whose use is governed by the Apache License, Version 2.0 (`LICENSE.Apache-2.0-Gemma`).
- NVIDIA's governing-terms notice is retained verbatim in `NOTICE.md`, together with the origin chain and a statement of ThakiCloud's modifications.
- The fine-tuned weights add ThakiCloud's LoRA modifications; they do not change the terms above.
