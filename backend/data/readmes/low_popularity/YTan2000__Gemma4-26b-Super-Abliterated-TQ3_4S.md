---
license: gemma
base_model:
  - Jiunsong/supergemma4-26b-abliterated-multimodal
language:
  - en
  - ko
tags:
  - GGUF
  - llama.cpp
  - gemma4
  - quantization
  - turboquant
  - tq3_4s
  - multimodal
  - abliterated
  - conversational
pipeline_tag: image-text-to-text
---

![thumbnail](thumbnail.png)

# Gemma4-26b-Super-Abliterated-TQ3_4S

`Gemma4-26b-Super-Abliterated-TQ3_4S` is a GGUF quantization of `Jiunsong/supergemma4-26b-abliterated-multimodal` using **TQ3_4S**, a 4.0 bpw Walsh-Hadamard-transform weight format with four per-8 scales.

## Files

* `Gemma4-26b-Super-Abliterated-TQ3_4S.gguf` (12.0 GiB)
* `mmproj-f16.gguf` (1.2 GiB)
* `chat_template.jinja`

## Runtime Requirement

This model requires the public TurboQuant runtime fork:
* https://github.com/turbo-tan/llama.cpp-tq3

It will not load correctly on stock `llama.cpp` or other runtimes that do not include `TQ3_4S`.

## Text-Only Run

```bash
./build/bin/llama-server \
  -m /path/to/Gemma4-26b-Super-Abliterated-TQ3_4S.gguf \
  -ngl 99 -c 4096 -np 1 \
  -ctk q8_0 -ctv q8_0 -fa on \
  --cache-ram 0 --no-warmup --jinja \
  --chat-template-file /path/to/chat_template.jinja
```

## Vision / Image Input

```bash
./build/bin/llama-server \
  -m /path/to/Gemma4-26b-Super-Abliterated-TQ3_4S.gguf \
  -mm /path/to/mmproj-f16.gguf \
  -ngl 99 -c 4096 -np 1 \
  -ctk q8_0 -ctv q8_0 -fa on \
  --cache-ram 0 --no-warmup --jinja \
  --chat-template-file /path/to/chat_template.jinja \
  --no-mmproj-offload
```

## Performance (RTX 5060 Ti 16GB)

| Metric | Value |
|--------|------:|
| PP512 | 2154 tok/s |
| TG128 | 91.3 tok/s |
| Size | 12.01 GiB |
| BPW | 4.09 |

## Quality

10/10 correct on standard QA benchmark (capital of France, 2+2, Python reverse string, gravity, WW2, primes, boiling point, Shakespeare, Jupiter, hello→Hola).

## Base Model

* [`Jiunsong/supergemma4-26b-abliterated-multimodal`](https://huggingface.co/Jiunsong/supergemma4-26b-abliterated-multimodal) — abliterated multimodal variant of Google Gemma 4 26B-A4B
* Original: [`google/gemma-4-26B-A4B-it`](https://huggingface.co/google/gemma-4-26B-A4B-it)

## Credits

* **Jiunsong** for the SuperGemma4 abliterated multimodal model
* **Google DeepMind** for Gemma 4
* **huihui-ai** for the abliteration technique

## License

Same license terms as the base model apply (Gemma license).
