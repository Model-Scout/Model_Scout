---
license: openmdw-1.1
pipeline_tag: text-generation
language:
- en
- fr
- es
- it
- de
- pt
- ja
- ko
- hi
- ar
- zh
- he
tags:
- nvidia
- pytorch
- nemotron-3
- latent-moe
- mtp
base_model:
- nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16
---

# NVIDIA-Nemotron-3-Ultra-550B-A55B-GGUF

GGUF quantized version of nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16.

## How can I use?

1. Upstream llama.cpp: Model probably works.
2. [Forked version of llama.cpp](https://github.com/HelloKS/llama.cpp/tree/codex/nemotron-h-tp-poc): RPC with split mode tensor, MTP, and model works

## Detailed information

- Model: 161667.64 MiB (2.47 BPW)
- MTP: 8882.72 MiB (5.58 BPW)

## How it was made?

### Model
```sh
export TYPE_FFN_UP_EXPS=IQ2_XXS
export TYPE_FFN_DOWN_EXPS=IQ2_XS

export TYPE_LATENT=Q8_0
export TYPE_SHEXP=Q6_K
export TYPE_SSM=Q6_K
export TYPE_ATTN=Q6_K

export TYPE_DEFAULT=Q4_K_M

llama-quantize \
    --tensor-type 'ffn_up_exps='$TYPE_FFN_UP_EXPS \
    --tensor-type 'ffn_down_exps='$TYPE_FFN_DOWN_EXPS \
    --tensor-type 'ffn_latent_(up|down)='$TYPE_LATENT \
    --tensor-type 'ffn_(up|down)_shexp='$TYPE_SHEXP \
    --tensor-type 'ssm_(in|out)='$TYPE_SSM \
    --tensor-type 'attn_(q|k|v|output)='$TYPE_ATTN \
    --imatrix imatrix.gguf \
    "model-BF16.gguf" "$TYPE_DEFAULT"
```

### MTP
```sh
    llama-quantize \
    --tensor-type 'nextn\.eh_proj=Q6_K' \
    --tensor-type 'ffn_latent_(up|down)=Q8_0' \
    --tensor-type 'ffn_(up|down)_shexp=Q6_K' \
    --tensor-type 'attn_(q|k|v|output)=Q6_K' \
    "mtp-BF16.gguf" "mtp-quant.gguf" Q4_K_M
```

### imatrix

- Generate Korean-focused imatrix calibration dataset (Total 512 samples, Chat template applied for messages)

|Dataset|Language|Type|Topic|Comment|
|-------|--------|----|-----|-------|
|EleutherAI/the_pile_deduplicated|English|text|English corpus|15%, 16384|
|KORMo-Team/Cosmopedia-ko-synth|Korean|text|Korean corpus|35%, 8192|
|Korean chat generated with Gemma 4|Korean|messages|Korean chat|35%, 8192|
|SWE-bench/SWE-smith-trajectories|English|messages|Tool calling|15%, 8192|

- Create imatrix using llama-imatrix **with --parse-special flag**

## Benchmark

### Where is PPL/KLD?

Unfortunately, I don't have PPL/KLD for quant, due to out of compute resource and target budget.

### Throughtput

2x DGX Sparks, RPC, -sm tensor with MTP enabled (-ub 2048 -b 2048 -c 262144)

| Test | pp t/s | tg t/s | TTFT (ms) | Total (ms) | Tokens |
|---|---:|---:|---:|---:|---:|
| pp2048 tg128 @ d0 | 282 | 17.8 | 8,292 | 14,500 | 2048+128 |
| pp2048 tg128 @ d4096 | 313 | 15.6 | 20,668 | 27,897 | 2048+128 |
| pp2048 tg128 @ d8192 | 313 | 17.2 | 33,708 | 40,180 | 2048+128 |