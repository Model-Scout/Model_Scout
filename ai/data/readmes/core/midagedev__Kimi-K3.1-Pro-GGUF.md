---
license: other
license_name: kimi-k3.1-pro
license_link: LICENSE
base_model: moonshotai/Kimi-K3.1-Pro
base_model_relation: quantized
pipeline_tag: text-generation
language:
- en
- ko
tags:
- gguf
- bloomery
- kimi-k3.1
- imatrix
---

# Kimi-K3.1-Pro-IQ1_S

A low-bit GGUF of [moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) (1T parameters, 32B active)
that runs on one workstation: two NVIDIA cards, 256 GB of host RAM and an NVMe drive, through
[bloomery](https://github.com/midagedev/bloomery). 580 GB in 31 shards, written by bloomery's own quantizer. The license is
the base model's: the `LICENSE` file here is the source repository's own.

**Only bloomery loads this file.** Its architecture word is `kimi-k31`; mainline llama.cpp has no K3.1 graph, and the file is
not a drop-in for any other runtime. bloomery 0.3.13 or later is required.

## What you need

| | Our workstation | The rule |
|---|---|---|
| Cards | RTX A6000 48 GB + RTX 3090 24 GB | two cards; the first holds the 30 GB dense trunk, both hold the hottest experts |
| Host RAM | 256 GB | the plan puts as many experts in RAM as the room allows and pages the rest from the drive |
| Disk | 580 GB on a PCIe 4 NVMe | every request reads the experts RAM does not hold, so the shards sit on a fast drive; two drives are faster (below) |
| Software | bloomery 0.3.13, Linux x86_64, CUDA sm_86 or sm_120a | the macOS Metal build does not load this file |

With this room the engine serves about 5 tokens a second and reads a 2,048-token prompt at about the same rate, so the
first token of a long prompt takes minutes. The numbers are in [What to expect](#what-to-expect).

## Quick start

Install bloomery (the [0.3.13 release](https://github.com/midagedev/bloomery/releases/tag/v0.3.13) has tarballs for
sm_86, sm_120a and the DGX Spark's sm_121a; Homebrew takes the sm_86 one):

```
brew install midagedev/tap/bloomery
# or
tar -xzf bloomery-0.3.13-linux-x86_64-cuda-sm86.tar.gz && cd bloomery-0.3.13-linux-x86_64-cuda-sm86
```

Download the shards into one directory (580 GB):

```
hf download midagedev/Kimi-K3.1-Pro-GGUF --local-dir /models/Kimi-K3.1-Pro-IQ1_S
```

Serve:

```
BLOOMERY_HOST_ROOM=232G bloomery-serve --model kimik3 \
  -m /models/Kimi-K3.1-Pro-IQ1_S/Kimi-K3.1-Pro-IQ1_S-00001-of-00031.gguf \
  --place bp --ctx-size 2048
```

- `--place bp` is the only placement that loads this file: the dense trunk and the hottest routed experts on the two
  cards, the host's share of the experts in RAM, the rest on the NVMe expert tier (O_DIRECT reads from the shards'
  own directory).
- `BLOOMERY_HOST_ROOM` pins the host room the plan is made for. Without it the plan reads the live free memory, so two
  loads of the same set need not be the same plan; `232G` is what we serve a 256 GB host at.
- `--ctx-size 2048` is the ceiling at this tag (see [Known limits](#known-limits)).

The API is llama-server compatible (`/v1/chat/completions`, `/completion`, `/v1/models`). The think span of a reply
goes to `reasoning_content` and the response section to `content`:

```
curl -s http://127.0.0.1:8080/v1/chat/completions -H 'content-type: application/json' -d '{
  "messages": [{"role": "user", "content": "대한민국의 수도는 어디이고, 처음 방문하는 사람에게 추천할 곳 세 군데를 짧게 알려줘."}],
  "max_tokens": 1024, "temperature": 0
}'
```

A short `max_tokens` can end inside the thinking; the answer is then empty and `reasoning_content` holds what was
written. The chat template in the header is the one from unsloth's
[Kimi-K3-GGUF](https://huggingface.co/unsloth/Kimi-K3-GGUF) (the K3.1 checkpoint ships no Jinja template; its encoder
is Python). It renders thinking, tool calls and image prompts the K3 way; pass your own with `--chat-template-file` if
yours differs.

## What to expect

All rows: the 0.3.13 release binary unless marked, `--place bp --ctx-size 2048`, one cold request after a prompt of D
ids, temperature 0. The set is larger than the host's RAM, so every request pages experts from the drive: these are
cold-read rates, and they repeat within 3 %. This seat steps the prompt one token at a time, so the prompt rate is near
the decode rate: at the prompt rates below a 2,048-id prompt takes 9 to 13 minutes to its first token (derived from the rows).

| Cards | Drives | D | Decode tok/s | Prompt tok/s | Binary |
|---|---|---:|---:|---:|---|
| RTX A6000 + RTX 3090 | two (sidecar) | 512 | 4.94 | 3.85 | 0.3.13 release, `BLOOMERY_HOST_ROOM=232G` |
| RTX A6000 + RTX 3090 | one | 512 | 3.04 / 3.05 | 2.62 / 2.67 | 0.3.13 pre-release tree, `BLOOMERY_HOST_ROOM=252G`, two rounds |
| RTX A6000 + RTX 3090 | one | 1,536 | 2.27 / 2.34 | 2.58 / 2.53 | same |
| RTX A6000 + DGX Spark as the expert tier node (10 GbE TCP) | one | 512 | 4.00 / 4.05 | 3.16 / 3.59 | same tree; `BLOOMERY_TIER_NODES=<spark>:9000 BLOOMERY_TIER_LINK=tcp BLOOMERY_CARD_BUDGET=100G` |
| RTX A6000 + DGX Spark as the expert tier node (10 GbE TCP) | one | 1,536 | 3.17 / 3.23 | 3.43 / 3.20 | same |

The release row generated 512 ids; the pre-release rows 128, two rounds each (both values shown). The Spark rows run
bloomery's `tier_server` on the Spark with its own copy of the shards: the GB10 holds 106 GB of the routed experts in
place of the RTX 3090's 22 GB, so 175 GB instead of 259 GB are read from the NVMe each request.

### Faster with two drives

The release row reads the shards from two NVMe drives at once. Put a byte-identical copy of every shard on the second
drive and name its directory in a sidecar beside the first copy, one absolute path a line:

```
# /models/Kimi-K3.1-Pro-IQ1_S/Kimi-K3.1-Pro-IQ1_S.shard-dirs
/data2/Kimi-K3.1-Pro-IQ1_S
```

The expert tier's reader then reads each expert's parts from the copy its id picks, so one layer's misses land on both
drives. The load refuses by name a listed directory that lacks a shard or whose copy differs in length or in sampled
windows. On the same binary and the same request the decode rate went from 3.80 (one drive) to 4.94 tok/s and the prompt
rate from 2.57 to 3.85; details in
[serving.md 5.4](https://github.com/midagedev/bloomery/blob/v0.3.13/docs/serving.md#54-when-the-host-cannot-hold-the-experts-either).

## Quality

Measured against the released model served by Moonshot AI (through OpenRouter, top-20 log-probabilities), by teacher
forcing: the teacher's own completions are fed through this file and, at every position, its next-token distribution is
compared with the teacher's. 150 prompts over three sets, 35,226 positions, `--place bp --ctx 2048`.

| Set | Prompts | Positions | Top-1 agreement | ΔNLL (nats) | KL to the teacher's top-20 |
|---|---:|---:|---:|---:|---:|
| English prose | 50 | 11,274 | 0.840 ± 0.018 | 0.289 ± 0.037 | 0.105 ± 0.017 |
| Korean prose | 50 | 12,439 | 0.877 ± 0.009 | 0.218 ± 0.022 | 0.082 ± 0.009 |
| Code | 50 | 11,513 | 0.913 ± 0.011 | 0.133 ± 0.018 | 0.052 ± 0.006 |
| All | 150 | 35,226 | 0.877 ± 0.009 | 0.213 ± 0.018 | 0.080 ± 0.007 |

Top-1 agreement is how often the file's most likely next token is the teacher's. ΔNLL is the file's negative log-likelihood of
the teacher's token minus the teacher's own. KL is over the teacher's top-20 tokens, renormalized. The ± is the standard
error over prompts. The same measure on a set made with a raw-text calibration (4 chunks of English documents and C++ source)
read 0.872 / 0.222 / 0.084 over all positions; this file's calibration (below) is the better one on every set.

The tool: `tools/ref/k31-eval.py` and `generate_kimi_k3 --score` in the bloomery repository.

## Known limits

- **Context is 2,048 positions a slot** in bloomery 0.3.13: the engine runs the lightning indexer's selection up to its
  top-k (2,048) and refuses a larger `--ctx-size` by name, because the sparse attention past it is not in the engine yet.
  The file itself carries the model's full context (391,168); a later release lifts the limit without a new file.
- **The prompt is read one token at a time** on this seat, so a long prompt costs as much time as generating the same
  number of tokens. A batched prompt pass is the next release's.
- **The DSA indexer tensors are kept in BF16, unquantized.** K3.1 adds a lightning indexer to 24 attention layers (blocks
  3, 7, 11, …, 87, 91, 92). Those tensors are small (0.36 GB) and stay as the source has them.
- **No other runtime.** The `kimi-k31` architecture word and the indexer keys are bloomery's; llama.cpp, ik_llama.cpp,
  ollama and LM Studio do not read this file.

## Type map

Map `tight`: the routed experts are IQ1_S with an importance matrix, and IQ2_XXS on the gate and up experts of layers 11, 46,
47, 56, 57, 58, 68, 69, 70, 71 and the down experts of layers 83, 92 (the layers unsloth's Kimi K3 UD-IQ1_S file also
promotes); every other trunk tensor (attention, state-space, shared expert, latent routed projections and the dense layer's
MLP) is Q4_K, `attn_v_b` is Q6_K, `attn_k_b` and `ssm_f_b` are Q8_0, the token embedding is Q4_K, the output head Q6_K, and
the norms, scores and `ssm_beta` stay F32 as in the source.

| class | tensors | types | GB |
|---|---|---|---|
| experts | 276 | IQ1_S 254, IQ2_XXS 22 | 545.35 |
| embedding | 1 | Q4_K 1 | 0.66 |
| head | 1 | Q6_K 1 | 0.96 |
| indexer | 120 | BF16 72, F32 48 | 0.36 |
| trunk | 1114 | Q4_K 997, Q8_0 93, Q6_K 24 | 30.40 |
| small f32 | 1181 | F32 1181 | 2.61 |
| total | 2693 | | 580.34 |

The rules (the first matching rule wins):

```
blk\.(11|46|47|56|57|58|68|69|70|71)\.ffn_(gate|up)_exps\.weight=IQ2_XXS
blk\.(83|92)\.ffn_down_exps\.weight=IQ2_XXS
ffn_(down|gate|up)_exps\.weight=IQ1_S
\.attn_k_b\.weight$=q8_0
\.ssm_f_b\.weight$=q8_0
\.ssm_beta\.weight$=f32
\.attn_v_b\.weight$=q6_k
\.(attn_gate|attn_k|attn_kv_a_mqa|attn_output|attn_q|attn_q_a|attn_q_b|attn_v|ffn_down|ffn_gate|ffn_up|ffn_down_shexp|ffn_gate_shexp|ffn_up_shexp|ffn_routed_down|ffn_routed_up|ssm_f_a|ssm_g)\.weight$=q4_k
```

## How it was made

1. **Source.** The checkpoint `moonshotai/Kimi-K3.1-Pro`, revision `d9e99b0792a5e93b78ea9bea62a68167e36ddd9e` (MXFP4
   safetensors), read by bloomery's `prepare` (`crates/model-hf`) into a GGUF source set: the experts kept as MXFP4 blocks as
   the checkpoint stores them, the indexer tensors in BF16.
2. **Importance matrix.** `llama-imatrix` (llama.cpp `78feec062`, a CUDA build) over 27 chunks of 8,192 tokens (221,184
   tokens), at a context where the DSA selection keeps every position, so the K3 graph computes K3.1 exactly. The calibration
   text is a chat corpus Kimi K3.1 Pro itself wrote (through Moonshot AI's API) from seed prompts over English, Korean and
   code, rendered with the model's own encoder: system, user and assistant turns with their special tokens, so the matrix
   sees the token stream a served model sees. This is the one step still done by a llama.cpp tool; bloomery's own collector is
   in progress.
3. **Quantization.** `bloomery-quantize` (`crates/quantize`) wrote the final set in one pass: the IQ1_S and IQ2_XXS experts on
   the card (a CUDA port of ggml's quantizers, byte-identical to them on the same input) and the Q4_K, Q6_K and Q8_0 trunk on
   the host (byte-identical to llama-quantize's plan and writer); the indexer tensors and the `kimi-k31` keys written in the
   same pass (`tools/ref/gguf-splice.py`). The chat template was added to the first shard's header afterwards
   (`gguf_new_metadata.py`); no tensor byte changed.
4. **Pipeline:** `tools/ref/k31-quant.sh` in the bloomery repository (prepare, imatrix, quantize, splice, upload), the
   calibration generator `tools/ref/k31-calib-gen.py`, and the quality check `tools/ref/k31-eval.py`. Since 0.3.13
   `bloomery-quantize --hf DIR` reads a checkpoint folder directly, with no intermediate GGUF.

## Shards

| shard | file | tensors | bytes |
|---|---|---:|---:|
| 1/31 | Kimi-K3.1-Pro-IQ1_S-00001-of-00031.gguf | 101 | 17,704,088,160 |
| 2/31 | Kimi-K3.1-Pro-IQ1_S-00002-of-00031.gguf | 77 | 19,049,311,360 |
| 3/31 | Kimi-K3.1-Pro-IQ1_S-00003-of-00031.gguf | 82 | 18,369,953,248 |
| 4/31 | Kimi-K3.1-Pro-IQ1_S-00004-of-00031.gguf | 82 | 18,369,953,216 |
| 5/31 | Kimi-K3.1-Pro-IQ1_S-00005-of-00031.gguf | 87 | 18,487,874,144 |
| 6/31 | Kimi-K3.1-Pro-IQ1_S-00006-of-00031.gguf | 82 | 18,369,953,248 |
| 7/31 | Kimi-K3.1-Pro-IQ1_S-00007-of-00031.gguf | 82 | 18,369,953,248 |
| 8/31 | Kimi-K3.1-Pro-IQ1_S-00008-of-00031.gguf | 82 | 18,369,953,216 |
| 9/31 | Kimi-K3.1-Pro-IQ1_S-00009-of-00031.gguf | 82 | 18,369,953,248 |
| 10/31 | Kimi-K3.1-Pro-IQ1_S-00010-of-00031.gguf | 82 | 18,369,953,248 |
| 11/31 | Kimi-K3.1-Pro-IQ1_S-00011-of-00031.gguf | 92 | 18,425,078,720 |
| 12/31 | Kimi-K3.1-Pro-IQ1_S-00012-of-00031.gguf | 77 | 18,432,748,640 |
| 13/31 | Kimi-K3.1-Pro-IQ1_S-00013-of-00031.gguf | 82 | 18,369,953,248 |
| 14/31 | Kimi-K3.1-Pro-IQ1_S-00014-of-00031.gguf | 92 | 20,274,766,784 |
| 15/31 | Kimi-K3.1-Pro-IQ1_S-00015-of-00031.gguf | 77 | 19,049,311,360 |
| 16/31 | Kimi-K3.1-Pro-IQ1_S-00016-of-00031.gguf | 82 | 18,369,953,216 |
| 17/31 | Kimi-K3.1-Pro-IQ1_S-00017-of-00031.gguf | 92 | 18,425,078,720 |
| 18/31 | Kimi-K3.1-Pro-IQ1_S-00018-of-00031.gguf | 77 | 21,515,562,112 |
| 19/31 | Kimi-K3.1-Pro-IQ1_S-00019-of-00031.gguf | 82 | 18,986,515,904 |
| 20/31 | Kimi-K3.1-Pro-IQ1_S-00020-of-00031.gguf | 92 | 18,425,078,720 |
| 21/31 | Kimi-K3.1-Pro-IQ1_S-00021-of-00031.gguf | 77 | 18,432,748,672 |
| 22/31 | Kimi-K3.1-Pro-IQ1_S-00022-of-00031.gguf | 82 | 20,219,641,312 |
| 23/31 | Kimi-K3.1-Pro-IQ1_S-00023-of-00031.gguf | 87 | 20,773,408,512 |
| 24/31 | Kimi-K3.1-Pro-IQ1_S-00024-of-00031.gguf | 77 | 19,049,311,360 |
| 25/31 | Kimi-K3.1-Pro-IQ1_S-00025-of-00031.gguf | 82 | 18,369,953,248 |
| 26/31 | Kimi-K3.1-Pro-IQ1_S-00026-of-00031.gguf | 82 | 18,369,953,216 |
| 27/31 | Kimi-K3.1-Pro-IQ1_S-00027-of-00031.gguf | 87 | 18,487,874,144 |
| 28/31 | Kimi-K3.1-Pro-IQ1_S-00028-of-00031.gguf | 82 | 18,986,515,936 |
| 29/31 | Kimi-K3.1-Pro-IQ1_S-00029-of-00031.gguf | 82 | 18,369,953,248 |
| 30/31 | Kimi-K3.1-Pro-IQ1_S-00030-of-00031.gguf | 87 | 18,487,874,112 |
| 31/31 | Kimi-K3.1-Pro-IQ1_S-00031-of-00031.gguf | 184 | 16,693,739,008 |
| total | | | 580,345,966,528 |
