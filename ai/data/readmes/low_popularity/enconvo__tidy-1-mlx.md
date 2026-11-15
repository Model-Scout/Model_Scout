---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B-Base
library_name: mlx
pipeline_tag: text-generation
language:
  - en
  - zh
  - ja
  - ko
  - de
  - fr
  - es
  - pt
  - it
tags:
  - mlx
  - dictation
  - speech-to-text
  - text-cleanup
  - inverse-text-normalization
---

# Enconvo Tidy 1 (MLX, 4-bit DWQ)

Enconvo Tidy 1 cleans up dictated text on your Mac. It takes a speech-to-text
transcript and returns the same words, written the way you meant them:

- removes filler words, stutters, repeats and false starts;
- adds punctuation and fixes casing;
- writes spoken numbers, dates, times, amounts and units as digits;
- fixes obvious recognition errors where the sentence makes them clear;
- leaves text that is already correct unchanged.

It runs fully offline with [MLX](https://github.com/ml-explore/mlx) on Apple
silicon. It powers the Enconvo Tidy 1 model in Enconvo's On-Device Cleanup
for Dictation.

## Languages

English, Simplified Chinese, mixed Chinese and English, Japanese, Korean,
German, French, Spanish, Portuguese and Italian. The output stays in the
input's language; the model does not translate. Text in other languages is
out of scope (see Limitations).

## Model

| | |
|---|---|
| Base model | [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base) (Apache 2.0) |
| Vocabulary | Trimmed to 65,536 entries for these languages (from 151,936) |
| Fine-tuning | LoRA rank 64, merged |
| Quantization | 4-bit affine, group size 64, distilled against the BF16 model with MLX DWQ |
| Weights | 286 MB |

## Usage

The input is one line: `text: ` followed by the transcript, then a newline and
`out:`. The answer starts with a space and ends with `<|endoftext|>`. Use
greedy decoding.

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load("enconvo/tidy-1-mlx")

transcript = "um so i think we should uh meet at three thirty tomorrow at the office"
ids = tokenizer.encode(f"text: {transcript}\nout:", add_special_tokens=False)
answer = generate(model, tokenizer, prompt=ids, max_tokens=len(ids) * 2 + 16,
                  sampler=make_sampler(temp=0.0))
print(answer.strip())
# I think we should meet at 3:30 tomorrow at the office.
```

Keep the prompt and answer within about 512 tokens. For longer dictation, cut
the text at sentence ends and clean up each part; join line breaks with a
space first, since the model expects one line.

## Speed and memory

Measured on a Mac mini (M2, 10-core GPU, 8 GB memory) with MLX 0.32.3, on 132
dictation lines, greedy decoding, after a warm-up:

| | |
|---|---|
| Latency per line, p50 / p90 | 86 / 110 ms |
| Decoding speed | about 195 tokens/s |
| Peak MLX memory | 0.44 GB (0.54 GB on long sentences) |
| Process memory (RSS) | 0.49 GB |
| Load from disk | about 1 s |

## Training data

About 164,000 pairs of transcripts and cleaned text across the ten languages:

- rule-based synthetic dictation: filler words, repeats, self-corrections,
  spoken numbers, lists;
- open text with simulated recognition noise: Tatoeba (CC BY 2.0 FR), Common
  Voice text and Wikipedia sentences (CC0), FLEURS text (CC BY 4.0);
- real Whisper transcripts of FLEURS recordings paired with their reference
  text (CC BY 4.0), and ASCEND mixed Chinese and English transcripts
  (CC BY-SA 4.0);
- open cleanup and disfluency datasets (including Disfl-QA, CC BY-SA 4.0),
  each under its own license;
- synthetic speech read by macOS voices and transcribed with Whisper, to learn
  real recognition errors;
- pairs written by large language models and filtered by rules.

## Limitations

- Exact repeats that are meant (such as a word said three times for emphasis)
  are sometimes shortened.
- Chinese homophone errors that need world knowledge are rarely fixed.
- Text in languages outside the list above can come back garbled or repeated.
  Check that the output is plausible (for example, similar in length to the
  input) and fall back to the transcript when it is not.
- The model has no tone or style setting; it keeps the speaker's words.
- It sees one part of the dictation at a time, so it does not use context from
  earlier sentences or from the app you dictate into.

## License

Apache 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
