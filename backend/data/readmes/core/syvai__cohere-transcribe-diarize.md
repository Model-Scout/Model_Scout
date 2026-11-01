---
license: apache-2.0
language:
- en
- ar
- de
- el
- es
- fr
- it
- ja
- ko
- nl
- pl
- pt
- vi
- zh
pipeline_tag: automatic-speech-recognition
tags:
- audio
- speech-recognition
- transcription
- diarization
- speaker-diarization
- timestamps
library_name: transformers
base_model: CohereLabs/cohere-transcribe-03-2026
---

# Cohere Transcribe — Diarize + Timestamps (English)

**Built by [syv.ai](https://syv.ai)** — a Danish AI company focused on shipping practical speech and language models. We release open-weights speech models so teams can build on top without leaving their own infrastructure.

This model is `CohereLabs/cohere-transcribe-03-2026` fine-tuned to also emit **speaker labels** and **word-aligned timestamps** in a single decoder pass, while preserving the base model's transcription quality. It's a drop-in replacement when you need to know *who said what and when* on short-form audio (≤ 30 s), and pairs with our [`diarize_long_vllm`](#long-form-audio-30-s) helper for arbitrary-length recordings.

> **Recommended deployment: vLLM** — see [Serving with vLLM](#serving-with-vllm-recommended). We measured **44× real-time end-to-end** on a 10-min clip with one RTX 3090 (decode 113× RTF, embed 16 seg/s), and **249× peak throughput** under concurrent load. Transformers works too and is shown first for a minimal example, but the vLLM path is what we run in production.

**WE ARE LOOKING FOR COMPUTE PARTNERS TO FURTHER IMPROVE OUR MODELS - REACH OUT IF YOU CAN HELP**

<style>
    @scope {
        th, td {
            text-align: left;
            padding: 0.375rem 0.625rem;
            letter-spacing: 0;
            vertical-align: top;
            line-height: 133.3333%;
            border: 1px solid #e0e0e0;
        }
    }
</style>
<table>
    <tbody>
        <tr><th>Name</th><td><strong>cohere-transcribe-diarize</strong></td></tr>
        <tr><th>Base model</th><td><a href="https://huggingface.co/CohereLabs/cohere-transcribe-03-2026">CohereLabs/cohere-transcribe-03-2026</a> (Apache 2.0, 2 B params)</td></tr>
        <tr><th>Architecture</th><td>conformer-based encoder–decoder, full fine-tune (no LoRA)</td></tr>
        <tr><th>Input</th><td>audio waveform (16 kHz mono, resampled automatically). Maximum supported clip length: 30 s — longer audio should be processed with sliding windows (see <a href="#long-form-audio-30-s">below</a>)</td></tr>
        <tr><th>Output</th><td>special-token stream interleaving speaker IDs, timestamps, and transcribed text, e.g. <code>&lt;|spltoken0|&gt;&lt;|t:0.0|&gt; Welcome back to the show.&lt;|t:2.4|&gt;&lt;|spltoken1|&gt;&lt;|t:2.4|&gt; Thanks for having me.&lt;|t:3.8|&gt;</code></td></tr>
        <tr><th>Vocabulary extensions</th><td>8 speaker tokens (<code>&lt;|spltoken0|&gt;</code>…<code>&lt;|spltoken7|&gt;</code>) + 300 timestamp tokens at 100 ms resolution (<code>&lt;|t:0.0|&gt;</code>…<code>&lt;|t:29.9|&gt;</code>)</td></tr>
        <tr><th>Languages</th><td>
            <strong>Primary:</strong> English (the diarization + timestamp fine-tune was done exclusively on English supervision).<br>
            <strong>Likely usable (untested by us):</strong> the other 13 languages the Cohere Transcribe base supports — Arabic, German, Greek, Spanish, French, Italian, Japanese, Korean, Dutch, Polish, Portuguese, Vietnamese, Chinese (Mandarin). The base model's multilingual transcription weights are preserved, and the diarization head conditions on language-agnostic speaker acoustics, so segmentation and speaker IDs should transfer; word-level timestamp accuracy will be best on English. Pass the matching language code in the prompt (<code>&lt;|de|&gt;</code>, <code>&lt;|fr|&gt;</code>, …) to switch.
        </td></tr>
        <tr><th>License</th><td>Apache 2.0 (inherited from base)</td></tr>
    </tbody>
</table>

## Quick start

```bash
pip install transformers==4.57.6 torch huggingface_hub soundfile librosa sentencepiece protobuf
```

```python
import re
import torch
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
from transformers.audio_utils import load_audio

MODEL_ID = "syvai/cohere-transcribe-diarize"

processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    MODEL_ID, dtype=torch.bfloat16
).to("cuda").eval()

# Prompt that activates diarization + timestamps. The base Cohere model
# uses special control tokens to switch features on/off; we keep that contract.
# `<|en|><|en|>` is the canonical Cohere prompt — the two slots are
# audio-language + transcript-language; setting them to the same code means
# "transcribe" (different codes would be "translate"). To run on another
# Cohere language, swap BOTH tokens, e.g. `<|de|><|de|>`.
# Each `<|...|>` is a single special token in the tokenizer vocab. Resolve
# via convert_tokens_to_ids — running the prompt string through the tokenizer
# re-tokenizes each marker into 6-12 subword pieces, which weakens the
# control-token signal the model trained on.
PROMPT_TOKENS = [
    "<|startofcontext|>", "<|startoftranscript|>",
    "<|emo:undefined|>", "<|en|>", "<|en|>",
    "<|pnc|>", "<|noitn|>", "<|timestamp|>", "<|diarize|>",
]
prompt_ids = torch.tensor(
    [[processor.tokenizer.convert_tokens_to_ids(t) for t in PROMPT_TOKENS]]
).to(model.device)

# Load any ≤ 30 s audio clip.
audio = load_audio("clip.wav", sampling_rate=16000)
inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
inputs = {k: v.to(model.device, dtype=model.dtype if v.is_floating_point() else None)
          for k, v in inputs.items()}

with torch.inference_mode():
    out = model.generate(
        input_features=inputs["input_features"],
        attention_mask=torch.ones(inputs["input_features"].shape[:2], device=model.device),
        decoder_input_ids=prompt_ids,
        max_new_tokens=400,
        do_sample=False,
        repetition_penalty=1.2,  # baked into generation_config but explicit here
    )

raw = processor.tokenizer.decode(out[0], skip_special_tokens=False)
print(raw)
# → <|spltoken0|><|t:0.0|> Welcome back. <|t:1.5|><|spltoken1|><|t:1.5|> Thanks. <|t:2.4|>...
```

### Parsing the output into structured segments

```python
SEG_RE = re.compile(r"<\|spltoken(\d+)\|><\|t:(\d+\.\d+)\|>(.*?)<\|t:(\d+\.\d+)\|>", re.DOTALL)

# Drop the prompt prefix; the diarized text follows <|diarize|>
text = raw.split("<|diarize|>", 1)[-1].replace("<|endoftext|>", "")

segments = [
    {
        "speaker": int(m.group(1)),
        "start":   float(m.group(2)),
        "end":     float(m.group(4)),
        "text":    re.sub(r"<\|[^|]+\|>", "", m.group(3)).strip(),
    }
    for m in SEG_RE.finditer(text)
]
for s in segments:
    print(f"[{s['start']:6.2f}–{s['end']:6.2f}] SPK{s['speaker']:02d}  {s['text']}")
```

Output:

```text
[  0.00–  1.50] SPK00  Welcome back.
[  1.50–  2.40] SPK01  Thanks for having me.
[  2.40–  3.80] SPK00  Let's get into it.
```

The model uses **8 reusable speaker slots** per clip (`<|spltoken0|>`…`<|spltoken7|>`). IDs are local to the clip — there is no global identity across separately decoded clips. For long-form audio that's split into windows, re-link windows with the helper below.

## Long-form audio (> 30 s)

Audio longer than 30 s exceeds the encoder's maximum window. Two helpers in this repo do the windowing + cross-chunk speaker matching for you:

- **[`diarize_long_vllm.py`](https://huggingface.co/syvai/cohere-transcribe-diarize/resolve/main/diarize_long_vllm.py)** — recommended. Calls a local vLLM server concurrently (continuous batching) and reuses one GPU for both decode and embedding. ~**44× RTF** on a 10-min clip on a single 3090.
- **[`diarize_long.py`](https://huggingface.co/syvai/cohere-transcribe-diarize/resolve/main/diarize_long.py)** — transformers-only fallback, no server needed. Slower (~7× RTF on the same clip) but minimal deps.

Both helpers:

1. Slide 28 s windows with 2 s overlap over the full audio
2. Decode each window with this model
3. Embed each parsed segment with [ReDimNet2 B6](https://github.com/PalabraAI/redimnet2) (12 M params, 0.17 % EER, loaded automatically via `torch.hub`)
4. Cluster embeddings globally with cosine-distance AHC so the same speaker keeps the same ID across windows

```bash
# Assumes vLLM is already serving (see next section)
python diarize_long_vllm.py podcast.wav \
    --vllm http://127.0.0.1:8000 \
    --model syvai/cohere-transcribe-diarize \
    --language en \
    --tau 0.45 \
    --concurrency 32 \
    --embed-batch 32
```

Or via the offline transformers helper (slower, no server):

```python
from diarize_long import diarize_long_audio

segments = diarize_long_audio(
    audio="podcast.wav",
    diar_model_id="syvai/cohere-transcribe-diarize",
    language="en",
    chunk_s=28.0,
    overlap_s=2.0,
    cluster_threshold=0.45,
)
```

Additional dependencies for long-form inference: `numpy`, `scipy`, `soundfile`, `torchaudio` (required by ReDimNet2's feature extractor), plus `aiohttp` if using `diarize_long_vllm.py`.

**Tuning the clustering threshold.** `cluster_threshold` is the cosine-distance ceiling for AHC merges over ReDimNet2 embeddings. Around **0.45** is a good default for podcast / panel-style audio: a 2-min Bernie Sanders town-hall clip cleanly resolves Bernie as one consistent ID across all 5 sliding windows and the host as a second ID, while short audience interjections get their own IDs. Drop to 0.30–0.35 if the audio has many similar-sounding speakers; raise to 0.50–0.55 for noisier conditions where you'd rather collapse near-duplicate IDs.

## Serving with vLLM (recommended)

The transformers code path above works but is single-stream. For production we run this model on **vLLM 0.19.0** (note: **0.19.1 is broken**) — it gives continuous batching, a custom OpenAI-compatible `diarized_json` response format, and ~25× higher peak throughput than calling `model.generate()` in a loop.

### One-time setup

Two scripts ship with this repo to handle the setup — both idempotent:

```bash
# Download the model locally first, then patch it
hf download syvai/cohere-transcribe-diarize --local-dir cohere-transcribe-diarize

# 1. Reshape the checkpoint files for vLLM compatibility
python fix_for_vllm.py ./cohere-transcribe-diarize
```

`fix_for_vllm.py` makes three edits to your local copy:

- `tokenizer_config.json`: drops the legacy `extra_special_tokens` list (transformers 4.57+ expects a dict; the actual tokens are still in `tokenizer.json`).
- `config.json`: sets `head.num_classes` and `transf_decoder.config_dict.vocab_size` to `16684` (the resized vocab).
- `model.safetensors`: strips the `model.` weight-name prefix and drops the BatchNorm `num_batches_tracked` tensors vLLM's CohereAsr model doesn't register.

```bash
# 2. Install vLLM 0.19.0 (NOT 0.19.1 — broken)
uv pip install "vllm==0.19.0" --torch-backend=cu128
uv pip install librosa

# 3. Patch vLLM's speech_to_text endpoint to add diarized_json
python vllm_diarized_patch.py
```

`vllm_diarized_patch.py` applies five edits inside the installed vLLM (also idempotent):

  1. `protocol.py` — add `"diarized_json"` to the `AudioResponseFormat` enum
  2. `protocol.py` — force `skip_special_tokens=False` in `to_sampling_params` so `<|spltoken*|>` and `<|t:*|>` survive into the response text
  3. `speech_to_text.py` — let the validator accept `response_format="diarized_json"`
  4. `speech_to_text.py` — parse the raw token stream with the segment regex and return OpenAI-compatible `{task, language, duration, text, segments:[{speaker, start, end, text}], speakers, usage}` JSON
  5. `api_router.py` — pass `JSONResponse` returns through unchanged (otherwise the diarized branch's return value gets misinterpreted as a streaming generator and the response body comes out empty)

### Launch the server

```bash
vllm serve ./cohere-transcribe-diarize \
    --served-model-name syvai/cohere-transcribe-diarize \
    --trust-remote-code \
    --host 127.0.0.1 --port 8000 \
    --gpu-memory-utilization 0.55     # leaves ~10 GB for ReDimNet2 batching
```

`--gpu-memory-utilization 0.55` is the sweet spot on a 24 GB card when you also run ReDimNet2 on the same GPU for long-form. If you only need short-form decode (≤ 30 s, no cross-chunk linking), bump it to `0.85` for better KV cache headroom.

### Call the API

Plain transcription is OpenAI-compatible:

```bash
curl -X POST http://127.0.0.1:8000/v1/audio/transcriptions \
    -F "file=@clip.wav" \
    -F "model=syvai/cohere-transcribe-diarize" \
    -F "language=en" \
    -F "response_format=diarized_json" \
    --form-string "prompt=<|startofcontext|><|startoftranscript|><|emo:undefined|><|en|><|en|><|pnc|><|noitn|><|timestamp|><|diarize|>"
```

Response shape (mirrors OpenAI's `gpt-4o-transcribe-diarize`):

```json
{
  "task": "transcribe",
  "language": "en",
  "duration": 28.0,
  "text": "UM I REJECT THE IDEA I REALLY DO ...",
  "segments": [
    {"speaker": "SPEAKER_00", "start": 2.5,  "end": 3.8,  "text": "I REALLY DO"},
    {"speaker": "SPEAKER_01", "start": 3.6,  "end": 15.0, "text": "IT'S ONE OF THINGS THAT BOTHERS ME ..."},
    {"speaker": "SPEAKER_02", "start": 15.5, "end": 28.0, "text": "IS RAISING A STARVATION MINIMUM WAGE ..."}
  ],
  "speakers": ["SPEAKER_00", "SPEAKER_01", "SPEAKER_02"],
  "usage": {"type": "duration", "seconds": 28}
}
```

The `prompt` field must be passed explicitly — vLLM's default prompt builder emits `<|nodiarize|>` which suppresses the speaker tokens.

### Measured throughput (RTX 3090, 28 s clips)

| Concurrency | Throughput |
|---|---|
| 1 | 22× audio/wall |
| 8 | 117× |
| 32 | 171× |
| **128** | **249× (peak)** |

vLLM does continuous (in-flight) batching automatically — fire concurrent requests at the endpoint and it batches them through one forward pass.

## Training

This model was produced by full fine-tuning of `CohereLabs/cohere-transcribe-03-2026` on English diarization data. The base vocabulary was extended with 8 speaker tokens and 300 100 ms timestamp tokens; the new rows of the embedding and LM-head matrices were initialised from the existing token embedding statistics.

| Dataset | Rows | Description |
|---|---|---|
| **AMI SDM (train split)** | 19,928 | Single-distant-microphone meeting recordings, sliding 28 s windows with 14 s hop, up to 4 simultaneous speakers per window. Provides realistic multi-speaker conversation with overlap, hesitations, and turn-taking. |
| **LibriSpeech synthetic mix** | 11,813 | Synthetic K-speaker mixtures (K weighted 0.2 / 0.3 / 0.3 / 0.2 for K=1…4) constructed from LibriSpeech utterances, with realistic gap silences. Provides clean cross-talk-free speaker examples to anchor the diarization head. |
| **Total** | **31,741** | All segments are ≤ 30 s and capped at K ≤ 4 speakers. |

Training ran for 2 epochs at peak LR 3e-4 (linear warmup over 100 optimizer steps, then linear decay to 0). Effective batch size 128 (per-device batch 2 × 64 gradient-accumulation), bf16, gradient checkpointing, AdamW8bit optimizer. The full fine-tune updates all 2 B parameters. `repetition_penalty=1.2` is baked into the generation config and is required at inference — without it, K=4 outputs occasionally loop on a single speaker token.

## Limitations

- **30 s hard cap** per decoder pass — use [`diarize_long`](#long-form-audio-30-s) for longer audio. The Cohere feature extractor batches longer clips into multiple chunks, which the diarization decoder is not trained to consume.
- **K ≤ 4 well-supported**, K = 5–8 still emit but accuracy degrades on dense overlapping speech.
- **Real-time factor ≈ 14× on RTX 3090** at bf16 — the 2 B autoregressive decoder is the bottleneck. For >100× RTF on long audio, pair with a smaller segmenter (e.g. DiariZen-base) or use this model only on the highlight regions.
- **Speaker IDs are local to each generate call.** Always cluster embeddings across windows when working with audio that crosses the 30 s boundary.

## Citation

If you use this model, please cite Cohere Labs' base release alongside this fine-tune:

```bibtex
@misc{cohere-transcribe-diarize-2026,
  author       = {{syv.ai}},
  title        = {Cohere Transcribe — Diarize + Timestamps (English)},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/syvai/cohere-transcribe-diarize}},
}
```

## License

Apache 2.0, inherited from the base model.
