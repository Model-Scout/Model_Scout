---
license: other
license_name: plamo-community-license
license_link: https://plamo.preferredai.jp/info/plamo-community-license-en
model_name: PLaMo 3 Translate 0.8B GGUF
base_model: pfnet/plamo-3-translate-0.8b
base_model_relation: quantized
library_name: gguf
language:
- ar
- az
- be
- bg
- bn
- ca
- ceb
- de
- en
- es
- et
- eu
- fa
- fr
- gu
- he
- hi
- hr
- hu
- hy
- id
- it
- ja
- jv
- ka
- kk
- km
- ko
- lt
- lv
- ml
- mr
- ms
- my
- ne
- nl
- pa
- pl
- ru
- si
- sk
- sl
- sr
- sw
- ta
- te
- th
- tl
- ur
- uz
- vi
- zh
pipeline_tag: translation
tags:
- translation
- plamo
- gguf
- llama.cpp
---


# PLaMo 3 Translate 0.8B GGUF

[日本語版のREADME / Japanese README](README_ja.md)

Built with PLaMo

Two GGUF quantizations of [PLaMo 3 Translate 0.8B](https://huggingface.co/pfnet/plamo-3-translate-0.8b) for [llama.cpp](https://github.com/ggml-org/llama.cpp). This is an independent derivative, not an official Preferred Networks release.

## Files

| File | Size | Quantization | Typical use |
| --- | ---: | --- | --- |
| `plamo-3-translate-0.8b-Q4_K_S-small-output.gguf` | 528.5 MB | Q4_K_S, output Q5_K | Smaller file with translation quality similar to pfnet Q4_K_M |
| `plamo-3-translate-0.8b-GSQ-Q4_0-MLP.gguf` | 503.8 MB | attention Q4_K, MLP Q4_0 trained with GSQ, embedding and output Q4_K | Smallest file, for speed on Arm devices with i8mm |
| reference: pfnet `plamo-3-translate-0.8b-Q4_K_M.gguf` | 573.1 MB | Q4_K_M | |

Q4_K_S-small-output is llama.cpp's standard Q4_K_S with the output matrix reduced from Q6_K to Q5_K. The standard Q4_K_S is 550.5 MB, so this saves about 22 MB.

GSQ-Q4_0-MLP stores the MLP matrices as Q4_0 whose values were retrained with GSQ, a method that fine-tunes the quantized weights on a small dataset so that each layer's output stays close to the original model. On the Xperia 1 V it was the fastest of the three models measured, including pfnet Q4_K_M. On the 12 hand-written cases, however, its judge score was 4.46 points below pfnet Q4_K_M. The 95% interval includes 0, but the sample is small, so check it on your own text before relying on it.

### Tensor types

blk is the layer index. The model has 16 layers.

| Tensor | pfnet Q4_K_M | Q4_K_S-small-output | GSQ-Q4_0-MLP |
| --- | --- | --- | --- |
| token_embd | Q4_K | Q4_K | Q4_K |
| attn_qkv | Q6_K ×8, Q4_K ×8 | Q5_K ×4 (blk 0–3), Q4_K ×12 | Q4_K |
| attn_output | Q4_K | Q4_K | Q4_K |
| ffn_up | Q4_K | Q4_K | Q4_0, GSQ |
| ffn_down | Q6_K ×8, Q4_K ×8 | Q5_K ×2 (blk 0–1), Q4_K ×14 | Q4_0, GSQ |
| output | Q6_K | Q5_K | Q4_K |

## Usage

Run with `llama-server` from [llama.cpp](https://github.com/ggml-org/llama.cpp). The embedded chat template is the same as in the pfnet GGUF.

```bash
pip install -U huggingface_hub
hf download ikatrik/plamo-3-translate-0.8b-GGUF plamo-3-translate-0.8b-Q4_K_S-small-output.gguf --local-dir .
llama-server -m plamo-3-translate-0.8b-Q4_K_S-small-output.gguf -c 16384 --port 8000 --alias plamo-3-translate --jinja --no-prefill-assistant
```

```bash
curl http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "plamo-3-translate",
    "messages": [{"role": "user", "content": "会議は来週の月曜日に変更されました。"}],
    "chat_template_kwargs": {"target_lang": "en"},
    "temperature": 0,
    "max_tokens": 512,
    "stop": ["<|plamo:tag|>", "<|plamo:bos|>"]
  }'
```

Both files return translations with these commands on llama.cpp b12052. For translation options such as glossaries, surrounding text and plain or polite style, and for sending prompts directly in PFML3, PLaMo's prompt format, see [pfnet/plamo-3-translate-0.8b-GGUF](https://huggingface.co/pfnet/plamo-3-translate-0.8b-GGUF).

## Evaluation

The test set has 739 cases. Translations were generated greedily with llama.cpp on CPU.

| Direction | Cases | Source |
| --- | ---: | --- |
| en→ja | 200 | WMT24++ |
| zh→ja | 120 | WMT24++ |
| ko→ja | 120 | WMT24++ |
| fr→ja | 80 | WMT24++ |
| ja→en | 200 | WMT23 |
| hand-written | 19 | written for this evaluation |

For zh→ja, ko→ja and fr→ja, the reference is the Japanese translation of the same WMT24++ document.

| Model | KLD vs Q8_0 | Top-1 match | Judge score | COMET-22 | chrF++ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q8_0 | — | — | — | 0.8538 | 37.37 |
| pfnet Q4_K_M | 0.0231 | 95.4% | 77.34 | 0.8528 | 37.07 |
| Q4_K_S-small-output | 0.0270 | 95.7% | 77.20 | 0.8538 | 37.08 |
| GSQ-Q4_0-MLP | 0.0290 | 95.6% | 77.07 | 0.8545 | 37.18 |

- KLD is the Kullback–Leibler divergence from the Q8_0 token distribution; lower is closer to Q8_0. Top-1 match is the share of tokens whose most likely token matches Q8_0. Both are averaged per token over 296 cases, 2 out of every 5 test cases, teacher-forced on the Q8_0 greedy output.
- Judge score is a blind 0–100 score by Claude, averaged over two independent passes. The 158 cases where all four models produced the same text were not judged. Of the remaining 581, the 578 cases scored in both passes are used.
- Judge score difference from pfnet Q4_K_M with 95% bootstrap CI: Q4_K_S-small-output −0.14 [−0.81, +0.52], GSQ-Q4_0-MLP −0.27 [−0.99, +0.43].
- On the 12 hand-written cases left after removing 7 with identical outputs: Q4_K_S-small-output +1.31 [−0.94, +3.62], GSQ-Q4_0-MLP −4.46 [−10.79, +0.56].
- COMET-22 uses Unbabel/wmt22-comet-da. chrF++ uses sacrebleu CHRF with word_order=2. Both are computed on 724 cases, excluding the 15 hand-written cases without a reference.
- The data used for the importance matrix and for GSQ excludes the test sentences but comes from the same documents. Scores may therefore be higher than on unrelated documents.

### Speed

Measured on an Xperia 1 V with a Snapdragon 8 Gen 2, using 5 threads: total time for 30 translations, 3 runs, with the model order rotated each run. pp512 is the speed of processing a 512-token prompt and tg64 the speed of generating 64 tokens.

| Model | Total for 30 translations | Output tokens | pp512 | tg64 |
| --- | --- | ---: | --- | --- |
| pfnet Q4_K_M | 33.3 / 38.6 / 33.8 s | 1,236 | 208–226 t/s | 35–67 t/s |
| Q4_K_S-small-output | 32.0 / 35.0 / 34.9 s | 1,231 | 193–220 t/s | 39–46 t/s |
| GSQ-Q4_0-MLP | 29.2 / 30.5 / 28.9 s | 1,235 | 232–237 t/s | 67–75 t/s |

The CPU frequency changed between runs, so values vary for the same model. This CPU supports i8mm, an 8-bit matrix multiply instruction, and llama.cpp computes Q4_0 with it. GSQ-Q4_0-MLP also runs on CPUs without i8mm, but its speed there has not been measured.

## How these were made

- Converted to BF16 with `convert_hf_to_gguf.py` from llama.cpp 18ab62a.
- Quantized with `llama-quantize` from llama.cpp b12052, using an importance matrix.
- The importance matrix was computed on 1,460 examples from WMT24++ and WMT23, excluding the test cases, in the PFML3 prompt format.
- GSQ is [IST-DASLab/GSQ](https://github.com/IST-DASLab/GSQ), ported to PLaMo 3 and GGUF Q4_0. Only ffn_up and ffn_down are trained, one layer at a time, with the attention weights held fixed at Q4_K. Each layer was trained for 400 steps with a batch of 16 sequences and 4 gradient accumulation steps, on the same 1,460 examples with 128 held out for validation.

## Not tested

- Devices other than the Xperia 1 V
- Translation from Japanese into languages other than English
- Long documents

## SHA-256

| File | SHA-256 |
| --- | --- |
| `plamo-3-translate-0.8b-Q4_K_S-small-output.gguf` | `e5833c44767150e603fb189c2d236bfe696201f670f9c75b63473d6b000e19dc` |
| `plamo-3-translate-0.8b-GSQ-Q4_0-MLP.gguf` | `cdb040ba17b574072661432e6fb5072b1ca0ba4d669c8eae973f29d7c7aa786f` |

## License

These files are released under the [PLaMo Community License](https://plamo.preferredai.jp/info/plamo-community-license-en). A copy of the license is in [LICENSE](LICENSE).

- Personal use, such as learning or hobby projects, and other non-commercial use, including academic use, are free of charge with no prior registration.
- Commercial use requires prior registration on PFN's [registration page](https://forms.gle/mTL8tBLrMYXKNZD56). If the revenue of the user or its affiliates in the most recent fiscal year exceeds 1 billion yen, a separate commercial license from PFN is required.
- When redistributing, include a copy of the license, state "Built with PLaMo", and include "PLaMo" in the model name.

## Disclaimer

This is an independent derivative model. It is not endorsed, warranted or supported by Preferred Networks. Neither the author nor Preferred Networks is responsible for the accuracy of its output.
