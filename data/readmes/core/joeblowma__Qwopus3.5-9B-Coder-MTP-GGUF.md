---
library_name: gguf
base_model:
  - Jackrong/Qwopus3.5-9B-Coder
tags:
  - gguf
  - quantization
  - llama.cpp
  - image-text-to-text
  - vision
  - multimodal
  - text-generation-inference
  - transformers
  - conversational
  - mtp
  - multi-token-prediction
  - speculative-decoding
  - qwen3_5
  - reasoning
  - chain-of-thought
  - agent
  - coder
  - tool-use
  - function-calling
license: apache-2.0
language:
  - en
  - zh
  - ko
  - ru
  - ja
  - es
pipeline_tag: image-text-to-text
---

# 🌟 Qwopus3.5-9B-Coder-MTP-gguf

This is a set of custom IQ4_XS quants of [Qwopus3.5-9B-Coder](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder) using [mradermacher's imatrix](https://huggingface.co/mradermacher/Qwopus3.5-9B-Coder-i1-GGUF), also mirroring [mradermacher's mmproj](https://huggingface.co/mradermacher/Qwopus3.5-9B-Coder-GGUF) files.

Initially I ran this to retain the MTP heads. Then went further, experiment with uplifting certain layers and the quant sizing of the MTP layers. Very basic stuff, but the result is pretty solid: 98,304 context (don't forget to use yarn past 32K!) in ~6GB VRAM when using beellama/KVarN and initial ~60t/s on a RTX4060 with Windows 11.

| Version | file | size |
| :--- | --- | ---: | 
| 1 | [Qwopus3.5-9B-Coder-MTP-IQ4_XS](./Qwopus3.5-9B-Coder-MTP-IQ4_XS.gguf) | ~5.29GiB | 
| 2 | [Qwopus3.5-9B-Coder-MTP-IQ4_XS_v2](Qwopus3.5-9B-Coder-MTP-IQ4_XS_v2.gguf) | ~5.02GiB | 
| 3 | [Qwopus3.5-9B-Coder-MTP-IQ4_XS_v3](Qwopus3.5-9B-Coder-MTP-IQ4_XS_v3.gguf)) | ~4.99GiB | 

## Tools

GGUF was produced using scripts from the root of llama.cpp's [source code](https://github.com/ggml-org/llama.cpp).

Quants were produced using `llama-quantize.exe` from llama.cpp's binary releases.

## Get a gguf

```bash
python convert_hf_to_gguf.py --outfile T:\_Qwen\Qwopus3.5-9B-Coder\__output\Qwopus3.5-9B-Coder-MTP-{ftype}.gguf --outtype auto --model-name Qwopus3.5-9B-Coder --verbose T:\_Qwen\Qwopus3.5-9B-Coder
```

## V1

This version is standard iq4_xs (with imatrix, thanks mradermacher!) with the MTP layers held at BF16

```bash
llama-quantize --imatrix Qwopus3.5-9B-Coder.mradermacher.imatrix.gguf --tensor-type "blk\.32\..*=BF16" T:\_Qwen\Qwopus3.5-9B-coder\__output\Qwopus3.5-9B-Coder-MTP-bf16.gguf T:\_Qwen\Qwopus3.5-9B-coder\__output\Qwopus3.5-9B-Coder-MTP-IQ4_XS.gguf IQ4_XS 8
```

## V2

Try keeping a few ffn_down at Q5_K, MTP mostly Q5_K

```
llama-quantize --imatrix Qwopus3.5-9B-Coder.mradermacher.imatrix.gguf --tensor-type-file tensors1.txt T:\_Qwen\Qwopus3.5-9B-coder\__output\Qwopus3.5-9B-Coder-MTP-bf16.gguf T:\_Qwen\Qwopus3.5-9B-coder\__output\Qwopus3.5-9B-Coder-MTP-IQ4_XS_v2.gguf IQ4_XS 8
```

tensor1.txt:

```
blk.0.ffn_down.weight=Q5_K
blk.1.ffn_down.weight=Q5_K
blk.2.ffn_down.weight=Q5_K
blk.3.ffn_down.weight=Q5_K
blk.32.attn_k.weight=Q5_K
blk.32.attn_output.weight=Q5_K
blk.32.attn_q.weight=Q5_K
blk.32.attn_v.weight=Q6_K
blk.32.ffn_down.weight=Q5_K
blk.32.ffn_gate.weight=Q5_K
blk.32.ffn_up.weight=Q5_K
blk.32.nextn.eh_proj.weight=Q5_K
```

## V3

Can we go smaller? Yes, but it doesn't gain much.

```bash
llama-quantize --imatrix Qwopus3.5-9B-Coder.mradermacher.imatrix.gguf --tensor-type-file tensors2.txt T:\_Qwen\Qwopus3.5-9B-coder\__output\Qwopus3.5-9B-Coder-MTP-bf16.gguf T:\_Qwen\Qwopus3.5-9B-coder\__output\Qwopus3.5-9B-Coder-MTP-IQ4_XS_v3.gguf IQ4_XS 8
```

tensor2.txt:

```text
blk.0.ffn_down.weight=Q5_K
blk.1.ffn_down.weight=Q5_K
blk.2.ffn_down.weight=Q5_K
blk.3.ffn_down.weight=Q5_K
blk.32.attn_k.weight=IQ4_XS
blk.32.attn_output.weight=Q5_K
blk.32.attn_q.weight=IQ4_XS
blk.32.attn_v.weight=Q5_K
blk.32.ffn_down.weight=IQ4_XS
blk.32.ffn_gate.weight=IQ4_XS
blk.32.ffn_up.weight=IQ4_XS
blk.32.nextn.eh_proj.weight=IQ4_XS
```

## inference

llama.cpp `models.ini` (beellama v0.4.3 - newer versions allow KVarN for MTP as well, I've not tried yet)

```
[*]
load-mode=none
mmproj-offload=on
ctx-size=98304
batch-size=2048
ubatch-size=512
cache-type-k=kvarn4
cache-type-v=kvarn2
cache-reuse=256
flash-attn=on
kv-offload=on
n-gpu-layers=all
fit=on
fitt=200
rope-scale=4
kv-tail-tokens=1024
spec-draft-n-max=2
ctx-checkpoints=32
cache-ram=4096
kv-unified=on

temperature=0.7
repeat-penalty=1.0
top-k=20
top-p=0.95
min-p=0.0001
reasoning=on

rope-scaling=yarn
yarn-orig-ctx=32768

[Qwopus3.5-9B-v3.5-MTP.coder_V1]
model=C:\llm\_Qwen\Qwopus3.5-9B-v3.5-MTP.coder_V1\Qwopus3.5-9B-Coder-MTP-IQ4_XS.gguf
jinja=on
chat-template-file=C:\llm\_Templates\Qwopus-9B-jackrong\chat_template.jinja
chat-template-kwargs={"preserve_thinking":"true"}
spec-type=draft-mtp
spec-draft-type-k=q8_0
spec-draft-type-v=q4_0

[Qwopus3.5-9B-v3.5-MTP.coder_V2]
model=C:\llm\_Qwen\Qwopus3.5-9B-v3.5-MTP.coder_V2\Qwopus3.5-9B-Coder-MTP-IQ4_XS_v2.gguf
jinja=on
chat-template-file=C:\llm\_Templates\Qwopus-9B-jackrong\chat_template.jinja
chat-template-kwargs={"preserve_thinking":"true"}
spec-draft-type-k=q8_0
spec-draft-type-v=q4_0

[Qwopus3.5-9B-v3.5-MTP.coder_V3]
model=C:\llm\_Qwen\Qwopus3.5-9B-v3.5-MTP.coder_V3\Qwopus3.5-9B-Coder-MTP-IQ4_XS_v3.gguf
jinja=on
chat-template-file=C:\llm\_Templates\Qwopus-9B-jackrong\chat_template.jinja
chat-template-kwargs={"preserve_thinking":"true"}
spec-type=draft-mtp
spec-draft-type-k=q8_0
spec-draft-type-v=q4_0

[Qwopus3.5-9B-v3.5.coder_MM_V3]
model=C:\llm\_Qwen\Qwopus3.5-9B-v3.5-MTP.coder_V3\Qwopus3.5-9B-Coder-MTP-IQ4_XS_v3.gguf
mmproj=C:\llm\_Qwen\Qwopus3.5-9B-Coder-mmproj-f16.gguf
jinja=on
chat-template-file=C:\llm\_Templates\Qwopus-9B-jackrong\chat_template.jinja
chat-template-kwargs={"preserve_thinking":"true"}
ctx-size=98304
rope-scaling=yarn
yarn-orig-ctx=32768
rope-scale=3
```

## Conclusion

Prediction acceptance only dropped marginally on V3 compared to V1, still trends above 60% during coding tasks. Unable to quantify any gains from bumping 4 ff_down weights from IQ4_S to Q5_K. Next run I will try V2 again but bump all ff_down weights to Q6_K and MTP head to Q6_K/Q8_K and see where it stands.

## thanks

First, thanks to the Qwen team for such a great model.

Thanks to everyone who has contributed to the bountiful tools, documents and most of all open weights.

Special thanks to mradermacher, unsloth and Jackrong!
