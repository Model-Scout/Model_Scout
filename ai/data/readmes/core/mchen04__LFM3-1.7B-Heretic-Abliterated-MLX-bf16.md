---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: Vortecks/LFM3-1.7B-Heretic-Abliterated
library_name: mlx
pipeline_tag: text-generation
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
tags:
- mlx
- apple-silicon
- liquid
- lfm3
- edge
- conversational
- tool-calling
- custom_code
- heretic
- abliterated
- uncensored
- bf16
---

# LFM3-1.7B Heretic Abliterated · MLX · bf16

An MLX port of [Vortecks/LFM3-1.7B-Heretic-Abliterated](https://huggingface.co/Vortecks/LFM3-1.7B-Heretic-Abliterated)
for Apple silicon. The weights are the source's bfloat16 bytes, unchanged. There is no quantization, pruning,
fine-tuning or new abliteration. The model has its refusal behavior removed, so it applies no safety filtering
of its own.

The port matches the reference implementation within the declared tolerances on every check
([results](#evaluation)). All 286 tensors are bit-identical to the source.

| | |
| --- | --- |
| Base model | [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) |
| Abliteration | [Vortecks](https://huggingface.co/Vortecks), with [Heretic](https://github.com/p-e-w/heretic) |
| Parameters | ~1.73B, bfloat16 (3.46 GB) |
| Architecture | `Lfm3ForCausalLM`, 24 layers: 13 gated short convolutions, 5 sliding-window attention, 6 global attention |
| Context | 262,144 tokens |
| Languages | 16 (see metadata) |
| Runtime | [mlx-lm](https://github.com/ml-explore/mlx-lm) 0.32.2 or later, with `trust_remote_code=True` |
| License | LFM Open License v1.0 ([LICENSE](LICENSE)) |

## How to use

mlx-lm has no built-in LFM3 architecture. This repo ships one as `lfm3.py`, and `config.json` points to it.
mlx-lm runs that file only when you pass `trust_remote_code`. Read `lfm3.py` before you run it.

```sh
pip install -U mlx-lm
mlx_lm.generate --model mchen04/LFM3-1.7B-Heretic-Abliterated-MLX-bf16 --trust-remote-code \
  --temp 0.1 --top-k 50 --prompt "Who are you?"
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mchen04/LFM3-1.7B-Heretic-Abliterated-MLX-bf16", trust_remote_code=True)
messages = [{"role": "user", "content": "Who are you?"}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
print(generate(model, tokenizer, prompt=prompt, max_tokens=512, verbose=True))
```

Peak memory is 3.6 GB with short prompts and 4.5 GB with a 16K-token prompt ([speed](#speed)).

Recommended sampling, from the source model card:

| Mode | Settings |
| --- | --- |
| General (chat, tool use, agents, coding) | `temperature=0.1, top_k=50, repetition_penalty=1.1` |
| Math and STEM | `temperature=1.0, top_p=0.95, top_k=20` |

mlx-lm applies `repetition_penalty` to the last 20 tokens by default. Transformers applies it to the whole
context. Set `repetition_context_size` in `make_logits_processors` if you need to match transformers.

The chat template supports tool calls and a thinking block, as in the source model. Pass `tools=[...]` to
`apply_chat_template` for tool use.

## Uses

**Intended:** local chat, tool calling, structured output and long-context work on Apple silicon, for research
and applications that provide their own moderation.

**Out of scope:** any use without your own safety layer where outputs reach other people. Uses that the
[LFM Open License](LICENSE) or applicable law forbid.

## Risks and limitations

- **No refusals.** Vortecks reports 3/100 refusals on Heretic's adversarial prompt set, against 92/100 for the
  base model. The model will produce harmful, false or offensive content on request. The deployer is responsible
  for moderation and policy compliance.
- **Abliteration changes the model.** Vortecks reports a KL divergence of 0.0094 from the base model. That is
  small, but abliteration can still lower some abilities. This port did not test refusal rates or benchmark
  scores. It tests only that the port behaves the same as the source model.
- **Strict JSON can fail.** On the two JSON prompts in the test set, the source model fails strict parsing in
  every run: once with unquoted keys and once with text after the array. This port reproduces that exactly.
  Validate structured output.
- **bfloat16 ties.** Greedy decoding at bfloat16 sometimes meets exact logit ties. Equally valid implementations
  can then choose different tokens, so outputs can differ from transformers after a tie.
- **Custom code.** Loading runs `lfm3.py` from this repo.

## Speed

Measured on a Mac mini (Apple M4, 24 GB, macOS 26.2) with mlx 0.32.4 and mlx-lm 0.32.2, using this repo as
downloaded from the Hub. `mlx_lm.benchmark`, batch size 1, 128 generated tokens, one warm-up run, then the mean
of 5 trials. The trials varied by less than 1%.

| Prompt tokens | Prompt processing (tok/s) | Generation (tok/s) | Peak memory (GB) |
| ---: | ---: | ---: | ---: |
| 128 | 573 | 29.1 | 3.65 |
| 512 | 932 | 29.0 | 3.96 |
| 4,096 | 1,062 | 28.6 | 4.46 |
| 16,384 | 984 | 27.5 | 4.55 |

A real chat request through `mlx_lm.generate` (21-token prompt, 248 tokens generated) ran at 29.1 tok/s with a
peak of 3.5 GB. Generation speed stays nearly flat as the prompt grows, because 13 of the 24 layers are
convolutions and 5 more use a 256-token sliding window. This is the unquantized bfloat16 model; a quantized
build would be faster.

Startup, same machine, 21-token chat prompt:

| Case | Python import | Weight load | Time to first token | Generation (tok/s) |
| --- | ---: | ---: | ---: | ---: |
| Cold: new process, weights not in the file cache | 2.5 s | 1.5 s | 0.29 s | 29.0 |
| New process, weights in the file cache | 0.5 s | 0.5 s | 0.14 s | 28.9 |
| Warm: later requests in a running process | — | — | 0.11 s | 29.0 |

A cold start takes about 4.3 s to the first token. A warm process answers in about 0.1 s.

```sh
mlx_lm.benchmark --model mchen04/LFM3-1.7B-Heretic-Abliterated-MLX-bf16 --trust-remote-code -p 512 -g 128 -n 5
```

## Evaluation

The checks compare this port with the source repo's own transformers code, pinned by revision. Each runs at
float32 and at bfloat16, on the same token ids, over 9 prompts: chat, translation, multi-turn memory, JSON,
tool call, tool follow-up and long-context retrieval. The pass criteria were committed before any real-model
run ([evidence/TOLERANCES.md](evidence/TOLERANCES.md)).

| Check | Result |
| --- | --- |
| T1 tensors vs source safetensors | PASS: 286/286 bit-identical |
| T2 source safetensors vs Vortecks' BF16 GGUF | PASS: 286/286 bit-identical |
| T3 float32 logits, port vs reference (2,076 positions) | PASS: max \|Δ\| 1.44e-3 (limit 5e-3), mean KL 2.3e-10, top-1 100% |
| T4 float32 greedy continuations | PASS: 9/9 identical |
| T5 bfloat16 logits vs float32 reference | PASS: mean KL 3.73e-3 for the port, 5.39e-3 for the reference's own bfloat16 run |
| T6 bfloat16 greedy, port vs reference | PASS: 6/9 identical; the 3 differences follow near-ties (margins 0.125–0.25, limit 0.5) |
| T7 chat template rendering and output format | PASS: identical on all 9 conversations; tool call correct in every run |
| T8 KV-cache decode vs full forward | PASS: max \|Δ\| 4.33e-3 (limit 5e-3) |

Full numbers and greedy outputs: [evidence/REPORT.md](evidence/REPORT.md) and
[evidence/report.json](evidence/report.json). Hardware: Apple M2, 16 GB, mlx 0.32 and mlx-lm 0.32.2. The
parity runs streamed weights layer by layer under a memory cap, so they say nothing about speed.

## What changed from the source

The LFM Open License asks for notice of modified files. Only these differ from
[Vortecks/LFM3-1.7B-Heretic-Abliterated](https://huggingface.co/Vortecks/LFM3-1.7B-Heretic-Abliterated) at
revision `dc37c60c02a35603456c85c2aecd7bc22b23b89c`:

- `model.safetensors`: the 13 depthwise convolution kernels are stored as `(C, K, 1)` instead of `(C, 1, K)`,
  which is the MLX layout. The values are the same bytes. Every other tensor is unchanged.
- `config.json`: `auto_map` removed, `"model_file": "lfm3.py"` added.
- `lfm3.py`: new, an MLX implementation of the LFM3 architecture.
- `convert_manifest.json`: new, the sha256 of every input and output file and each change applied.
- `evidence/`: new, the verification results.

The tokenizer, chat template and generation config are byte-for-byte copies of the source.

## License

This model is a derivative of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) and is
distributed under the **LFM Open License v1.0**. The full text is in [LICENSE](LICENSE). The license does not
cover commercial use by an entity with annual revenue of USD 10 million or more. Read the license for the exact
terms.

## Credits

- [Liquid AI](https://www.liquid.ai) for LFM3-1.7B.
- [Vortecks](https://huggingface.co/Vortecks) for the Heretic abliteration.
- [Heretic](https://github.com/p-e-w/heretic) by p-e-w.
- Arditi et al., [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717), 2024.
