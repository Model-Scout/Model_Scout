---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/litert-community/LFM3-1.7B-Base-LiteRT/blob/main/LICENSE
base_model: LiquidAI/LFM3-1.7B-Base
base_model_relation: quantized
pipeline_tag: text-generation
library_name: litert-lm
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
- litert
- litert-lm
- tflite
- on-device
- edge
- liquid
- lfm3
---

# LFM3-1.7B-Base — LiteRT-LM

This repository is a conversion of [LiquidAI/LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base) to LiteRT-LM, made with litert-torch (commit f61d0b7 of its main branch) and litert-lm-builder 0.18.1 and checked with LiteRT-LM 0.19.1: on a Galaxy S26 GPU the int8 file decodes 28.61 tokens/s and the mixed int4 file 32.48 tokens/s after a 1,024-token prompt (mean of two runs each, 2026-11-08). Speed is still being tuned (updates follow).

[LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base) is the pre-trained checkpoint behind Liquid AI's [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B): 1.73B parameters in 24 layers (13 gated short convolutions, 5 sliding-window attention, 6 global attention), a 128,000-token vocabulary, 16 languages. Liquid AI recommends it only for tasks that need heavy fine-tuning, such as language- or domain-specific assistants, training on proprietary data or new post-training methods; for chat, tool calling and agents it points to LFM3-1.7B, whose LiteRT-LM files are in [litert-community/LFM3-1.7B-LiteRT](https://huggingface.co/litert-community/LFM3-1.7B-LiteRT). The files here run the base model on a device: text continuation and few-shot prompts (Usage).

## Files

| File | What is inside | Size | sha256 |
|---|---|---|---|
| `LFM3-1.7B-Base_mixed_int4_ekv2048.litertlm` | MLP gate and up projections in int4 (blockwise, 32 weights per block); every other weight in int8 per channel (attention, short convolutions, MLP down projection, the shared embedding / output table). KV cache of 2,048 tokens. | 1,442,562,048 B (1.44 GB) | `526a909cdbbce61beeac65f55a51ad3119cb35d371c6de060abe8abe79ee222c` |
| `LFM3-1.7B-Base_mixed_int4_ekv4096.litertlm` | The same weights, KV cache of 4,096 tokens | 1,442,562,048 B (1.44 GB) | `cdfabc7c6bca16a18b432e536bfd24ca435da2ce4d4d83e404de972be69bfab5` |
| `LFM3-1.7B-Base_int8_ekv2048.litertlm` | Every weight in int8 per channel. KV cache of 2,048 tokens. | 1,802,469,376 B (1.80 GB) | `ead41791c1ac03c54eca50b0cd0b5499530246e8a62d9af3b95b0fc22aa253d3` |
| `LFM3-1.7B-Base_int8_ekv4096.litertlm` | The same weights, KV cache of 4,096 tokens | 1,802,469,376 B (1.80 GB) | `ae7085fbc5ee824c924ec8b73aedb2eb1b87ae2c2d9ebd59bbdd2cd3030a6086` |
| `LICENSE` | The source model's license file, unchanged | 10,574 B | |
| `litertlm_manifest.json` | Machine-readable description of the four files | 21 kB | |

Every file has prefill signatures of 1,024, 256, 64, 16, 4 and 1 tokens, the source repository's `tokenizer.json` byte for byte, LFM3-1.7B's chat template with the edits described under Conversion notes, and a thought channel (`<think>` … `</think>`). The files declare no sampler and no activation type: LiteRT-LM then picks the most likely token at every step, and on a GPU it runs fp16 activations.

Which file:

- int8 stays closer to the source model: 98 % top-token agreement and 72.3 of 100 GSM8K questions on average, against 93 % and 69.0 for mixed int4 (the source model in bfloat16: 69; Accuracy).
- mixed int4 is 360 MB smaller and decodes faster on the Galaxy S26 GPU (32.48 against 28.61 tokens/s).
- On the Galaxy S26 CPU, int8 prefills 752.2 tokens/s against mixed int4's 329.6 (the first token of a 1,024-token prompt after 1.39 s against 3.16 s), while mixed int4 decodes faster (35.11 against 31.13 tokens/s).
- `ekv4096` takes a prompt and reply of up to 4,096 tokens; on the Galaxy S26 it decodes slower than `ekv2048` (Performance). Take `ekv2048` when 2,048 tokens are enough.

## Usage

Continue a text with the LiteRT-LM command-line tool:

```bash
pip install -U huggingface_hub
hf download litert-community/LFM3-1.7B-Base-LiteRT LFM3-1.7B-Base_mixed_int4_ekv2048.litertlm --local-dir .
uvx --from litert-lm==0.19.1 litert-lm run LFM3-1.7B-Base_mixed_int4_ekv2048.litertlm --backend gpu --cache no --no-template --max-num-tokens 256 --prompt "The nematode C. elegans is" < /dev/null
```

`--no-template` sends the text as it is; LiteRT-LM puts the start token in front. A base model rarely ends a text by itself, so it writes until the context of `--max-num-tokens` tokens (prompt included) is full. `--backend cpu` runs it on the CPU.

The same from Python (`pip install litert-lm==0.19.1`), with a limit on the new tokens:

```python
import litert_lm

MODEL = "LFM3-1.7B-Base_mixed_int4_ekv2048.litertlm"

# One Engine per text (Limitations).
with litert_lm.Engine(MODEL, backend=litert_lm.Backend.GPU(), cache_dir=":nocache") as engine:
    session = engine.create_session(apply_prompt_template=False, max_output_tokens=128)
    session.run_prefill(["The nematode C. elegans is"])
    print(session.run_decode().texts[0])
```

`litert_lm.Backend.CPU(thread_count=4)` runs it on 4 CPU threads, the setting of the CPU rows below.

A few-shot prompt works the same way: put the worked examples and the new question in one text (Accuracy uses `Question: …\nAnswer: …` pairs) and cut the reply at the next `\nQuestion:`.

The files also carry LFM3-1.7B's chat template, as the source card describes the base model's chat data, so `engine.create_conversation()` runs the chat format the same way as on the LFM3-1.7B files (thinking on by default; `engine.create_conversation(thinking_config=litert_lm.ThinkingConfig(enable_thinking=False))` turns it off). For chat, the source card recommends LFM3-1.7B.

On Android, the numbers below come from `litert_lm_advanced_main` built from the LiteRT-LM v0.19.1 tag, with `--backend=gpu` or `--backend=cpu` and `--use_session=true`: that flag sends the prompt file as it is (no chat template) with the start token in front, the way the base model reads text.

## Performance

Measured with `litert_lm_advanced_main` built from the LiteRT-LM v0.19.1 tag as the tag builds by default, which links the GPU accelerator statically from source (its log says `Statically linked GPU accelerator registered.`), in its benchmark mode: `--use_session=true --benchmark_prefill_tokens=1024 --benchmark_decode_tokens=256 --max_num_tokens=2048` (a 1,024-token prompt, 256 new tokens, a 2,048-token context), 2026-11-08. Each row is the mean of two runs; peak memory is the runtime's "Peak system ram usage" line ("first run": the run that also built the engine cache, the first run of that file in the phone session). Galaxy S26: SM-S942Q, Android 16. Pixel 11 Pro: Tensor G6, Android 17.

**Galaxy S26**

| File | Backend | Prefill 1,024 (tok/s) | Decode 256 (tok/s) | Time to first token (s) | Peak memory (MB) |
|---|---|---:|---:|---:|---:|
| mixed int4, 2,048 cache | GPU | 653.0 | 32.48 | 1.6 | 898–901 |
| int8, 2,048 cache | GPU | 639.6 | 28.61 | 1.64 | 996–1,060 |
| mixed int4, 4,096 cache | GPU | 593.6 | 30.23 | 1.76 | 897 |
| int8, 4,096 cache | GPU | 589.7 | 27.02 | 1.77 | 1,009–1,046 |
| mixed int4, 2,048 cache | CPU, 4 threads | 329.6 | 35.11 | 3.16 | 2,298 (first run 2,504) |
| int8, 2,048 cache | CPU, 4 threads | 752.2 | 31.13 | 1.39 | 2,611 (first run 2,818) |
| mixed int4, 4,096 cache | CPU, 4 threads | 276.1 | 27.63 | 3.79 | 2,726 (first run 2,910) |

**Pixel 11 Pro**

| File | Backend | Prefill 1,024 (tok/s) | Decode 256 (tok/s) | Time to first token (s) | Peak memory (MB) |
|---|---|---:|---:|---:|---:|
| mixed int4, 2,048 cache | GPU | 628.7 | 17.13 | 1.69 | 741 (first run 1,354) |
| mixed int4, 2,048 cache | CPU, 4 threads | 202.1 | 24.06 | 5.11 | 1,984 (first run 2,236) |

- Every GPU run delegated the whole model (7 signatures, one partition) to the OpenCL GPU backend, with fp16 activations.
- The Galaxy S26 GPU prefill depends on that accelerator: the same v0.19.1 commit built to load the tag's prebuilt `libLiteRtGpuAccelerator.so` instead prefilled the mixed int4 2,048-cache file at 1,305.29 and 1,331.20 tokens/s, against 641.12 and 636.90 for this build, with the same decode (33.26 and 32.57 against 32.49 and 32.80 tokens/s; the two builds alternating in one phone session). The device answer check has not been run on that build. Source builds link the accelerator statically by default since 2026-10-22. The Pixel 11 Pro prefilled this file at the same rate with this build and with the v0.18.1 tag and its prebuilt accelerator.
- On both phones the CPU decodes the mixed int4 2,048-cache file faster than the GPU (Galaxy S26 35.11 against 32.48, Pixel 11 Pro 24.06 against 17.13 tokens/s), while the GPU prefills it about 2 and 3 times faster.
- On the Galaxy S26 the int8 file runs faster on the CPU than on the GPU in both prefill and decode (752.2 / 31.13 against 639.6 / 28.61 tokens/s), with more than twice the peak memory.
- The phones lowered the CPU frequency limit during the CPU runs (the Galaxy S26 to 42 % of the maximum, the Pixel 11 Pro to 86 %, read about once a second), so the CPU figures are what the phones sustained under that limit.
- Without `--use_session=true`, this build's benchmark mode prefilled these files twice (two prefill turns of the forced length, seen at 128 tokens on the CPU and the GPU); read the prefill turn count before taking its decode figure.
- No NPU file is part of this release.

## Accuracy

GSM8K, the first 100 test questions, 5-shot (five worked examples from the end of the same test file as `Question: …\nAnswer: …` pairs, then the new question), greedy, at most 384 new tokens, the reply cut at the next `\nQuestion:`, one fresh process per question, LiteRT-LM 0.19.1 on a Mac M4 Max CPU (4 threads). The reference is the source model in transformers, bfloat16, on the same prompts.

| | Correct of 100 |
|---|---|
| Source model, bfloat16 | 69 |
| mixed int4, 2,048 cache, Mac CPU | 67, 71, 69 (three runs) |
| int8, 2,048 cache, Mac CPU | 72, 74, 71 (three runs) |

- Eight short check questions in the same form (`Question: … Answer briefly.\nAnswer:`; a sum, a product, the capital of Japan, an opposite, the days in a week, "thank you" in French, 0.9 against 0.11, a rhyme), at most 64 new tokens, the first line of the reply checked: 8 of 8 for every file on the Mac CPU and GPU, and for the two 2,048-cache files on the Pixel 11 Pro GPU and CPU. The source model in bfloat16: 8 of 8.
- Top-token agreement with the source model in float32, on 2,891 positions of 17 test texts (the 8 questions, 8 text openings in English, French, Spanish and Python, and the license text with a question, 1,578 tokens), each extended by the bfloat16 model's greedy continuation and fed to the files' graph through LiteRT's CompiledModel: int8 98.44 % on the Mac GPU (Metal, fp16) and 97.92 % on the Mac CPU (XNNPACK), mixed int4 93.29 % and 92.94 %. The source model in bfloat16 scores 99.34 % on the same positions.

## Limitations

- Create one Engine per text or conversation: on LiteRT-LM, a session started on an Engine that already served another one continues from that session's running state ([LiteRT-LM issue #3165](https://github.com/google-ai-edge/LiteRT-LM/issues/3165)). This model keeps a running short-convolution state.
- On LiteRT-LM 0.18.1 and 0.19.1, once a message fails because it does not fit in the context window, every later message in that conversation fails as well (the next one with `Task failed with state: 7`). Start a new conversation on a new Engine after such an error.
- A base model continues the text it is given; it does not answer and stop the way a chat model does. Set a limit on the new tokens: `max_output_tokens` in Python; the command line has no such option, and its `--max-num-tokens` caps prompt and reply together.
- Context is 2,048 or 4,096 tokens, prompt included (the source model: 256K).
- The files carry no sampler setting, so LiteRT-LM decodes greedily unless the app passes one (Python: `sampler_config=litert_lm.SamplerConfig(...)`).

## Conversion notes

- Source: [LiquidAI/LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base) at revision `7bca5038`.
- The same recipe as [litert-community/LFM3-1.7B-LiteRT](https://huggingface.co/litert-community/LFM3-1.7B-LiteRT) on the base weights: the two source repositories, LiquidAI/LFM3-1.7B and LiquidAI/LFM3-1.7B-Base, share the modeling code, the configuration, the tokenizer and the chat template byte for byte, and differ in the weights, `generation_config.json` and the README.
- Decoder: exported with litert-torch at commit f61d0b7 (torch 2.14.0, transformers 5.20.2) through a small LFM3 extension: the source repository's own modeling code with litert-torch's LFM2 short-convolution path and a guard that keeps padded prefill slots out of the convolution state. On 17 test texts (2,891 positions) the extension's PyTorch module matched the source model in transformers, float32, within 3.17e-4 in every logit with the same top token at every position, prefilled at once, token by token and in 128-token pieces. The graph has no GPU composites.
- Quantization: ai-edge-quantizer-nightly 0.10.0.dev20261023 on the float32 graph. int8 = every weight int8 per channel (`dynamic_wi8_afp32`). Mixed int4 = int4 blockwise-32 on the MLP gate and up projections (with a floor of 2^-14 on the block scales; the quantizer counted no scale below it), int8 per channel on every other weight. These are the LFM3-1.7B files' two recipes.
- Template: the LFM3-1.7B files' template (the source chat template with three edits: every earlier assistant turn renders without its thought wherever it sits, where the source template keeps the thought of turns after the latest user message; the `{%- generation -%}` tags are removed; `.get("…")` lookups are written as `["…"]`). The base repository ships the same `chat_template.jinja`.
- Sampler: none. The source `generation_config.json` has no sampling setting.
- Reproduce: [`lfm3_work/convert_lfm3_17b_base.sh`](https://github.com/john-rocky/hf-to-litertlm/blob/main/lfm3_work/convert_lfm3_17b_base.sh) in github.com/john-rocky/hf-to-litertlm converts the source to these four files ([REPRODUCE.md entry](https://github.com/john-rocky/hf-to-litertlm/blob/main/REPRODUCE.md#lfm3-17b-base--the-lfm3-17b-recipe-on-the-pre-trained-weights-as-four-text-files-int4-on-the-mlp-gate-and-up-projections-with-int8-elsewhere-or-int8-everywhere-each-with-a-2048--or-4096-token-cache-2026-11-08)). Run as printed on 2026-11-08, it rebuilt all four with every section byte for byte; the file sha256 differs from run to run because the packer writes a new id and creation time into the file header.

## Known runtime issues

**External weights (since 2026-11-10).** In `LFM3-1.7B-Base_mixed_int4_ekv2048.litertlm`, `LFM3-1.7B-Base_mixed_int4_ekv4096.litertlm`, `LFM3-1.7B-Base_int8_ekv2048.litertlm` and `LFM3-1.7B-Base_int8_ekv4096.litertlm`, the weights sit in a TFLiteWeights section at the end of the file (LiteRT's external weights) instead of inside the model graph. On Android, the GPU path needs LiteRT-LM 0.19.0 or later: the GPU engine of the v0.18.0 and v0.18.1 Android builds crashes (SIGSEGV) on such a file ([LiteRT-LM#3986](https://github.com/google-ai-edge/LiteRT-LM/issues/3986)). The earlier files with the weights inside the graph stay at revision [`fd08c1b`](https://huggingface.co/litert-community/LFM3-1.7B-Base-LiteRT/tree/fd08c1b51bfea82ce649bb95d01c6084eb01b4e6).

## License

LFM Open License v1.0, the same license as the source model ([LICENSE](https://huggingface.co/litert-community/LFM3-1.7B-Base-LiteRT/blob/main/LICENSE)). The files here are converted from LiquidAI/LFM3-1.7B-Base: the weights are quantized to int8 and int4 as described above, and the chat template is changed as described under Conversion notes. Section 5 of the license does not license commercial use by an organization with annual revenue of 10 million US dollars or more (a qualified non-profit's non-commercial or research use is exempt).
