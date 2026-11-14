---
library_name: rwkv
language:
- en
- zh
- fr
- es
- de
- pt
- ru
- it
- ja
- ko
- vi
- ar
tags:
- pytorch
- text-generation
- causal-lm
- rwkv
license: apache-2.0
datasets:
- HuggingFaceFW/fineweb-edu
- mlfoundations/dclm-baseline-1.0
- cerebras/SlimPajama-627B
- EleutherAI/pile
- bigcode/starcoderdata
- oscar-corpus/OSCAR-2301
---

# RWKV7-G1 "GooseOne" pure RNN reasoning model

These are BASE models (pretrained with web/code/synthetic + instruction/chat/reasoning data), suitable for post-training and fine-tuning (check https://huggingface.co/spaces/Jellyfish042/UncheatableEval to see their performance at language modeling).

More info & Gradio demo: https://rwkv.com/

---

**Recommended GUI (for fast batch generation, similar to https://huggingface.co/spaces/BlinkDL/RWKV-Gradio-3)**: https://github.com/BlinkDL/Albatross/blob/main/faster3a_2607/app4b.py

Search "RWKV Chat" in play store / app store for our local inference app

RWKV Chat: https://rwkv.halowang.cloud/ (local inference for mobile/desktop) and https://github.com/RWKV-APP/RWKV_APP

Safetensor: https://huggingface.co/RWKV

GGUF: https://huggingface.co/collections/shoumenchougou/rwkv7-gxx-gguf

More GGUF & mobile models: https://huggingface.co/HaloWang/rwkv-weights (new) and https://huggingface.co/mollysama/rwkv-mobile-models (old)

Ollama GGUF: https://ollama.com/shoumenchougou (new) and https://ollama.com/mollysama (old)

RWKV-7 pth => GGUF script: https://github.com/MollySophia/rwkv-mobile/blob/master/converter/convert_rwkv_pth_to_gguf.py

Training: https://github.com/BlinkDL/RWKV-LM and https://github.com/Joluck/RWKV-PEFT

Note: rwkv7a has DeepEmbed

---

Efficient inference: https://github.com/BlinkDL/Albatross
* 145+ token/s RWKV-7 7.2B fp16 bsz1 decoding @ RTX5090 (always const speed & vram)
* 10250+ token/s RWKV-7 7.2B fp16 bsz960 decoding @ RTX5090 (always const speed & vram)
* 9650+ token/s RWKV-7 7.2B fp16 bsz320 decoding @ RTX5090 (always const speed & vram)
* 11289 token/s RWKV-7 7.2B fp16 bsz1 prefill @ RTX5090 (always const speed & vram)

pip inference: https://pypi.org/project/rwkv/

mobile inference: https://github.com/MollySophia/rwkv-mobile

---

# There should not be any space at the end of your input (so strip your prompt) or you will upset the tokenizer and see non-English reponse.

---

**Latest Best Practices for agentic work (study these projects)**: https://agent.objects.rwkvos.com/en

Eval example: https://github.com/BlinkDL/Albatross/blob/main/faster3a_2605/eval_gpqa_diamond.py

PROMPT GUIDE (including function call & agent): https://github.com/BlinkDL/RWKV-LM/blob/main/RWKV-v7/RWKV7-G1x-templates.txt

Function call: temp 0, topp 0, penalty 0, works for RWKV-7 G1f 1.5B and larger models:
````
System: Tools:
- get_weather(location: string, unit?: "celsius" | "fahrenheit")
- get_stock_price(ticker: string)
- translate_text(text: string, target_language: string)
Return only a JSON function call.

User: Translate "Will it rain tomorrow?" into Japanese.

Assistant: ```json
````
and
````
System: Tools:
[
{"name":"find_free_slots","description":"Find free calendar slots","arguments":{"date":{"type":"string"},"duration_minutes":{"type":"integer"},"time_window":{"type":"string"}}},
{"name":"create_calendar_event","description":"Create a calendar event","arguments":{"title":{"type":"string"},"start_time":{"type":"string"},"end_time":{"type":"string"},"attendees":{"type":"array","items":{"type":"string"}}}}
]
Return only a JSON function call.

User: Schedule a 30-minute sync with Bob on 2026-05-08 afternoon.

Assistant: ```json
{"name":"find_free_slots","arguments":{"date":"2026-05-08","duration_minutes":30,"time_window":"afternoon"}}
```

User: Function output:
{"free_slots":[{"start":"2026-05-08T15:00:00+09:00","end":"2026-05-08T15:30:00+09:00"}],"bob_email":"bob@example.com"}

Assistant: ```json
````
The key is to keep it concise. Here you can enable "\<think\>" for Assistant too.

You can also use this template, which is closer to training data:
```
Assistant: <think>
...
</think>
<tool_call>
{...}
</tool_call>
<tool_call>
{...}
</tool_call>

User: <tool_response>
{...}
</tool_response>
<tool_response>
{...}
</tool_response>
```

---

Please always use **latest models** because they are always better at everything.

Decoding Suggestion (note: this is for RWKV pip pkg, which apply temp after topp):

```
Chat: temp 1, topp 0.5, alpha_presence 2, alpha_frequency 0.1, alpha_decay 0.99

Creative (great for fiction etc.): temp 0.6, topp 0.6 ~ 0.8, alpha_presence 2, alpha_frequency 0.2, alpha_decay 0.99
```

Chat prompt (note: better replace all \n\n in USER_PROMPT to \n as i am using \n\n as "chat round separator" in pretrain data):
```
System: YOU_CAN_USE_SYSTEM_IF_NEEDED

User: PREVIOUS_STUFF

Assistant: PREVIOUS_STUFF

User: USER_PROMPT

Assistant:
```

Think prompt (for hard prompts):
```
User: USER_PROMPT

Assistant: <think
```
**Fake think prompt (great result, highly recommended)**:
```
User: USER_PROMPT

Assistant: <think></think
```
---
Think prompt, alternative style, **for G1c and newer** models. Note there is a space before the "(think)" after USER_PROMPT:
```
User: USER_PROMPT (think)

Assistant: <think
```
Shorter think, same style:
```
User: USER_PROMPT (think a bit)

Assistant: <think
```
Longer think, same style:
```
User: USER_PROMPT (think a lot)

Assistant: <think
```
---

FIM prompt (**for G1c and newer** models, works for text & code & everything):

```✿prefix✿When I was young, I only liked to✿suffix✿and that’s how first I got interested in AI research.✿middle✿```

Better (recommended):

```✿prefix✿✿suffix✿and that’s how first I got interested in AI research.✿middle✿When I was young, I only liked to```

Note "✿" will always be tokenized to one single token in RWKV tokenizer, so I picked it.

---
```
0.1B = L12-D768
0.4B = L24-D1024
1.5B = L24-D2048
2.9B = L32-D2560
7.2B = L32-D4096
13.3B = L61-D4096
Vocab = 65536 for all current models
Head size = 64 for all current models
```
```
Gxx = Data Version

G0x = less than 1 epoch, as training 1 epoch for a large model is expensive :(
G0 G0a G0a2 G0a3 ... G0b ... = adding more (newer and better) data, so G0a has better quality (but less) data than G1

G1x = more than 1 epoch
G1 G1a G1a2 G1a3 ... G1b ... = adding more (newer and better) data, note G1a has better quality (and more) data than G0a
```