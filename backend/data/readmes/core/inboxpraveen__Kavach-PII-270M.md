---
license: gemma
base_model: google/gemma-3-270m-it
new_version: inboxpraveen/Kavach-PII-270M
library_name: transformers
pipeline_tag: text-generation
tags:
  - pii
  - pii-detection
  - privacy
  - redaction
  - anonymization
  - ner
  - token-classification
  - gdpr
  - hipaa
  - multilingual
  - gemma3
language:
  - en
  - hi
  - ta
  - te
  - bn
  - mr
  - gu
  - kn
  - ml
  - pa
  - ur
  - ar
  - zh
  - ja
  - ko
  - ru
  - tr
  - vi
  - id
  - es
  - fr
  - de
  - it
  - pt
  - nl
  - pl
---

# Kavach PII 270M (v2)

> **This is version 2 (released 2026-09-23), kept so results and pipelines built on it stay reproducible.** The current version is v3 at [inboxpraveen/Kavach-PII-270M](https://huggingface.co/inboxpraveen/Kavach-PII-270M). Re-scored on v3's repaired test set (4,577 documents, same scorer), v3 reaches 92.0 value-F1 against 79.0 for v2; the 88.4 below was measured against the original v2 gold, which missed roughly one value in ten. On that same set v2 still flags fewer PII-free documents (2.0% against 12.5%). v3 uses a shorter 43-label list, so the prompts are not interchangeable.
>
> Weights, charts and figures on this page are unchanged from the original v2 upload. Two notes: `generation_config.json` sets `do_sample: true` as originally shipped, so always decode greedily (`do_sample=False` or `temperature=0`, as every example below does); and [`kavach_extract.py`](kavach_extract.py), missing from the original upload, is now included in its v2 form.

A 270M parameter model that finds personal data in 29 languages. It scores 88.4 value-F1 on a held-out test set where GLiNER-PII scores 56.4 and Microsoft Presidio scores 22.2, measured with the same script on the same gold annotations.

*Kavach* (कवच) is Sanskrit for "armour". The model reads a document and returns the personal data it contains as a JSON list. It runs on a laptop GPU or on CPU, and it was built for the inputs real pipelines actually receive: call-centre ASR transcripts, scanned OCR output, structured forms, chat, code, logs, and deliberately obfuscated text.

![Comparison against GLiNER, Presidio and regex baselines](assets/01-headline-comparison.png)

| | Kavach PII 270M | GLiNER-PII multi-v1 | Presidio | Regex + checksum |
|---|---|---|---|---|
| **Value F1** | **88.4** | 56.4 | 22.2 | 20.5 |
| Precision | 88.9 | 56.9 | 21.0 | 51.1 |
| Recall | 87.9 | 55.9 | 23.4 | 12.8 |
| Exact span F1 | 89.1 | 55.4 | 22.3 | 20.0 |
| Redaction recall | 93.0 | 66.2 | 43.2 | 15.6 |
| **False positives on PII-free documents** | **0.4%** | 80.2% | 85.3% | 28.8% |

The last row decides whether a redaction pipeline is usable in practice. Presidio flags something in 85% of documents that contain no personal data at all. Kavach does so in 0.4%.

Test set: 3,372 held-out documents, 13,646 gold values. Presidio and GLiNER label sets were mapped to ours on a best-effort basis. See [Fair comparison notes](#fair-comparison-notes).

## Quick start

```python
import json, re
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "inboxpraveen/Kavach-PII-270M-v2"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, dtype="bfloat16").to("cuda").eval()

LABELS = ["AADHAAR_IN","ADDRESS","AGE","API_KEY_TOKEN","BANK_ACCOUNT","BIOMETRIC_DESCRIPTOR","CARD_CVV",
"CARD_EXPIRY","CASE_ID","CREDIT_DEBIT_CARD","DATE_TIME","DEVICE_ID","DISABILITY","DOB","DRIVING_LICENSE","EMAIL",
"EMPLOYEE_ID","ETHNICITY","GENDER_SEX","GEO_LOCATION","HEALTH_ID","IBAN","INSURANCE_ID","IP_ADDRESS","LAB_ORDER_ID",
"LICENSE_PLATE","MAC_ADDRESS","MEDICAL_RECORD_ID","NATIONAL_ID","ORGANIZATION","PAN_IN","PASSPORT","PASSWORD_SECRET",
"PERSON","PHONE","POLITICAL_BELIEF","POSTAL_CODE","PRESCRIPTION_ID","RELIGION","ROUTING_CODE","SIGNATURE","SSN_US",
"STUDENT_ID","SWIFT_BIC","TAX_ID","TRANSACTION_ID","UPI_VPA","URL_PERSONAL","USERNAME","VIN","VOTER_ID","WALLET_ID"]

INSTRUCTION = (
    "Extract all personal data (PII/PHI/PCI) from the text.\n"
    "Labels: " + ", ".join(LABELS) + "\n"
    'Return ONLY a JSON array of objects {"label": ..., "text": ...}. Copy each value EXACTLY as it appears in the '
    "text (same characters, spacing and spelling; for spoken values copy from the first to the last spoken token). "
    "List each distinct (label, value) pair once, in order of first appearance. "
    "If the text contains no personal data, return []."
)

def extract(text):
    msgs = [{"role": "user", "content": f"{INSTRUCTION}\n\nText:\n<<<\n{text}\n>>>"}]
    prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    ids = tok(prompt, return_tensors="pt", add_special_tokens=False).to(model.device)
    out = model.generate(**ids, max_new_tokens=768, do_sample=False)
    raw = tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True)
    return json.loads(raw[raw.find("["): raw.rfind("]") + 1])

text = "Hi, this is Derek Okafor from Meridian Bank, my number is +1-617-555-0142."
print(extract(text))
# [{"label": "PERSON", "text": "Derek Okafor"},
#  {"label": "ORGANIZATION", "text": "Meridian Bank"},
#  {"label": "PHONE", "text": "+1-617-555-0142"}]
```

## Serving

All three servers below expose an OpenAI-compatible `/v1/chat/completions` endpoint, so the same client code works against any of them. Send the instruction as a single user turn, exactly as in the Quick start above. Use `temperature: 0`.

### vLLM

```bash
pip install vllm

vllm serve inboxpraveen/Kavach-PII-270M-v2 \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --port 8000
```

To serve the LoRA adapter on top of the stock base model instead of the merged weights:

```bash
vllm serve google/gemma-3-270m-it \
    --enable-lora \
    --lora-modules kavach=inboxpraveen/Kavach-PII-270M-v2/adapter \
    --dtype bfloat16 --max-model-len 4096 --port 8000
```

### SGLang

```bash
pip install "sglang[all]"

python -m sglang.launch_server \
    --model-path inboxpraveen/Kavach-PII-270M-v2 \
    --dtype bfloat16 \
    --context-length 4096 \
    --port 30000
```

### Client for either server

```python
import json
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="EMPTY")   # 30000 for SGLang

def extract(text):
    r = client.chat.completions.create(
        model="inboxpraveen/Kavach-PII-270M-v2",
        messages=[{"role": "user", "content": f"{INSTRUCTION}\n\nText:\n<<<\n{text}\n>>>"}],
        temperature=0, max_tokens=768,
    )
    raw = r.choices[0].message.content
    return json.loads(raw[raw.find("["): raw.rfind("]") + 1])
```

Batching is worth setting up. Documents are independent, output is short (roughly 100 tokens), and both servers handle concurrent requests well. The accuracy figures in this card were produced with the `transformers` path and with llama.cpp; vLLM and SGLang use the same weights and the same greedy decoding, so results should match, but they were not separately benchmarked.

### llama.cpp, Ollama, LM Studio

See [Kavach-PII-270M-v2-GGUF](https://huggingface.co/inboxpraveen/Kavach-PII-270M-v2-GGUF) for quantised builds down to 169 MB.

## Long inputs, transcripts and character offsets

The model does not predict character positions. It returns values, and you find them in the source text afterwards. That removes the one thing a generative model reliably gets wrong: asked to emit indices, it produces plausible looking numbers that are simply incorrect. Asked to copy a value, it copies it, and a value it invents cannot be found, so hallucinations become detectable instead of silent.

[`kavach_extract.py`](kavach_extract.py) in this repository does the whole job in one function: it splits long text into overlapping windows, calls the model on each, locates every returned value in the original string, merges the windows and hands back character offsets. It has no dependencies beyond the standard library, and you supply the model call.

```python
from kavach_extract import extract_pii, redact, transformers_generate

gen = transformers_generate(model, tok)          # or openai_generate(...) for vLLM, SGLang, llama-server

result = extract_pii(transcript, gen)
for s in result["spans"]:
    print(s["start"], s["end"], s["label"], repr(s["text"]))

print(redact(transcript, result["spans"]))       # 'Hi, this is [PERSON] from [ORGANIZATION]...'
print(result["unlocatable"])                     # values the model invented; should be near empty
print(result["warnings"])                        # empty list means a clean run
```

It is written to survive real input: `None`, bytes, a number, an empty string, a model call that raises, and output that is not valid JSON are all handled and reported in `result["warnings"]` rather than raised. Running the file directly (`python kavach_extract.py`) runs its self-test, which needs no GPU and no model. Both back-ends are tested end to end: `transformers` locally and `openai_generate` against a live `llama-server`.

### Window size matters more than you would expect

The defaults below are measured, not reasoned about, because the obvious reasoning points the wrong way in both directions.

The model was trained on short documents: the median training document is 39 words. That does not mean you should feed it 39 words at a time. Two things are going on at once, and they pull opposite ways.

**On a coherent document, window size barely matters, but going small hurts.** These are 92 real test documents of 180 to 385 words, scored against their own gold:

| | Precision | Recall | Value F1 |
| --- | --- | --- | --- |
| Whole document, one call | 0.861 | 0.829 | 0.845 |
| Windowed 250 / 40 | 0.885 | 0.823 | 0.853 |
| Windowed 180 / 35 | 0.855 | 0.840 | 0.847 |
| Windowed 150 / 30 | 0.854 | 0.859 | **0.857** |
| Windowed 120 / 25 | 0.824 | 0.872 | 0.847 |
| Windowed 100 / 20 | 0.817 | 0.850 | 0.833 |
| Windowed 50 / 12 | 0.727 | 0.836 | 0.778 |

Everything from 120 words upward, including sending the document whole, lands between 0.845 and 0.857. Below that it falls away fast: cutting a coherent document into 50-word pieces costs 13 points of precision, because the model needs the surrounding sentence to tell a date of birth from an appointment date, or a patient from a clinician, and a small window takes that away.

**On text that runs past a few hundred words, recall falls away.** These are eight documents of about 660 words each, built by stitching unrelated documents together, which is the harder case because the model was never trained on concatenated documents:

| Window / overlap | Precision | Recall | Value F1 | Model calls |
| --- | --- | --- | --- | --- |
| 30 / 8 | 0.737 | 0.851 | 0.789 | 245 |
| 50 / 12 | 0.833 | 0.863 | 0.848 | 141 |
| 100 / 20 | 0.862 | 0.856 | 0.859 | 68 |
| 120 / 25 | 0.861 | 0.848 | **0.855** | 57 |
| 150 / 30 | 0.850 | 0.732 | 0.787 | 47 |
| 180 / 35 | 0.851 | 0.822 | 0.836 | 39 |
| 200 / 40 | 0.851 | 0.781 | 0.815 | 36 |
| 250 / 40 | 0.863 | 0.716 | 0.783 | 31 |
| 400 / 80 | 0.849 | 0.508 | 0.635 | 17 |

Precision holds up to 400 words; recall halves. The model emits about as many entities as a short document contains and then stops, so a single call carrying 400 words of dense personal data simply does not list it all. Sending each source document on its own scores 0.876, which is the ceiling any windowing scheme is working towards.

**The default is 120 words with 25 of overlap**, because it is the only setting that is near the top of both tables at once. On coherent documents everything from 120 to 250 sits in a one-point band, 0.847 to 0.857, so the choice barely matters there; 150 is nominally the best of them. On concatenated text the spread is much wider and 120 is clearly better than 150. The second table is eight documents and its middle rows are noisy, which is why the default sits at the low end of the plateau rather than on the single best cell.

Two things not to do: do not drop below about 80 words, where precision goes, and do not go past 250, where recall goes. Keep the overlap at 20 or more, or a long address can straddle an edge and be seen whole by neither window. If your input is always coherent prose rather than concatenated records, 150 or 180 is a reasonable change.

A document shorter than the window is sent in one call untouched, so ordinary short inputs never pay the windowing cost at all.

One note on throughput: `extract_pii` batches the windows of a single document together. If you are processing many documents, run several `extract_pii` calls concurrently rather than relying on that internal batching, or the GPU will sit mostly idle.

### Speech-to-text input

Transcripts work as they come out of the recogniser. Bracketed timestamps (`[00:01:02]`), SRT ranges (`00:00:03,500 --> 00:00:07,120`), WebVTT cues and plain `Speaker 1:` turns pass through untouched, and the timestamps survive redaction. This is not special-case code: 630 training documents contain bracketed timestamps and not one of them is tagged, so the model learned to ignore them. Measured on the 30 longest timestamped test documents, zero timestamps were tagged as personal data and all 243 of them survived redaction intact. Where the transcript has line breaks, window edges prefer to land on one, so a speaker turn stays whole; a transcript that arrives as one unbroken line is cut on word boundaries instead.

```
[00:00:03] Speaker 1: Hello, this is [PERSON] from [ORGANIZATION].
[00:00:09] Speaker 2: Hi [PERSON]. My parcel is [CASE_ID] and my mobile is [PHONE].
```

### Locating values correctly

Matching is stricter than a plain substring search, which matters more than it sounds. On the test set, a naive `re.escape` locator places 127 spans (0.94%) inside longer words: `Raj` lands in the middle of `Rajesh`, `2024` inside `20245`, and redaction then emits `[PERSON]esh`. `extract_pii` requires a whole-word match, with the boundary rule switched off for Chinese, Japanese, Thai, Khmer, Burmese and Korean, where words are not space-separated or particles attach directly to the noun. Indic and Arabic combining marks count as part of the word, which is the bug that a plain `\b` has against Devanagari.

Where a value occurs nowhere as a whole word, usually because the recogniser ran two words together, the span is still produced and flagged `"partial": True`, on the grounds that a mask starting mid-word beats leaving a real address in the clear. Drop those spans if you would rather under-mask.

On the 3,372-document test set:

| Outcome | Share of 13,488 predicted values |
| --- | --- |
| Located as a whole word | 98.07% |
| Located only inside a longer run, flagged `partial` | 0.57% |
| Not present in the text at all (hallucination) | 1.36% |

<details>
<summary>Full source of <code>kavach_extract.py</code></summary>

```python
"""
Kavach PII 270M: one self-contained extraction function.

Copy this file, or just the two public functions, into your project. It has no dependencies beyond the standard
library; you supply the model call.

    from kavach_extract import extract_pii, redact

    result = extract_pii(text, generate)     # `generate` defined below for your runtime
    print(result["spans"])                   # [{'start': 12, 'end': 24, 'label': 'PERSON', 'text': 'Derek Okafor'}, ...]
    print(redact(text, result["spans"]))     # 'Hi, this is [PERSON] from [ORGANIZATION]...'

What it handles
    * Input of any length. Text longer than one window is split into overlapping word windows, each sent
      separately, and the results merged back onto the original string with correct offsets.
    * Speech-to-text output with timestamps: '[00:01:02] Speaker 1: ...', '00:00:03,500 --> 00:00:07,120',
      WebVTT cues and plain 'Speaker 1:' turns. Where the transcript has line breaks, windows prefer to cut on
      one, so a speaker turn or a subtitle cue stays whole; a transcript that arrives as a single unbroken line
      is simply cut on word boundaries. Timestamps are never treated as personal data, because the model was
      trained that way: 630 training documents contain bracketed timestamps and not one is tagged.
    * Values repeated across the document. A name found once is masked at every occurrence.
    * Bad input: None, bytes, numbers, empty or whitespace-only strings, and model calls that fail or return
      something that is not JSON. Nothing raises; problems are reported in result["warnings"].

Window defaults are measured, not guessed, and they are a compromise between two opposite failures.

Too small and precision goes: on 92 real test documents of 180-385 words, a 50-word window scores 0.727
precision against 0.861 for the same documents sent whole, because the model needs the surrounding sentence to
tell a date of birth from an appointment date. Too large and recall goes: on 660-word inputs, recall falls from
0.86 at a 100-word window to 0.51 at 400, because the model emits about as many entities as the short documents
it was trained on and then stops.

120 words with 25 of overlap is near the top of both curves; 100 to 150 behaves about the same. Do not drop
below about 80, and do not go past 250. Keep the overlap at 20 or more, or a long address can straddle an edge
and be seen whole by neither window. A document shorter than the window is sent in one call untouched.
"""

from __future__ import annotations

import json
import re
import unicodedata

__all__ = ["extract_pii", "redact", "LABELS", "INSTRUCTION", "build_prompt"]

LABELS = [
    "AADHAAR_IN", "ADDRESS", "AGE", "API_KEY_TOKEN", "BANK_ACCOUNT", "BIOMETRIC_DESCRIPTOR", "CARD_CVV",
    "CARD_EXPIRY", "CASE_ID", "CREDIT_DEBIT_CARD", "DATE_TIME", "DEVICE_ID", "DISABILITY", "DOB",
    "DRIVING_LICENSE", "EMAIL", "EMPLOYEE_ID", "ETHNICITY", "GENDER_SEX", "GEO_LOCATION", "HEALTH_ID", "IBAN",
    "INSURANCE_ID", "IP_ADDRESS", "LAB_ORDER_ID", "LICENSE_PLATE", "MAC_ADDRESS", "MEDICAL_RECORD_ID",
    "NATIONAL_ID", "ORGANIZATION", "PAN_IN", "PASSPORT", "PASSWORD_SECRET", "PERSON", "PHONE",
    "POLITICAL_BELIEF", "POSTAL_CODE", "PRESCRIPTION_ID", "RELIGION", "ROUTING_CODE", "SIGNATURE", "SSN_US",
    "STUDENT_ID", "SWIFT_BIC", "TAX_ID", "TRANSACTION_ID", "UPI_VPA", "URL_PERSONAL", "USERNAME", "VIN",
    "VOTER_ID", "WALLET_ID",
]

INSTRUCTION = (
    "Extract all personal data (PII/PHI/PCI) from the text.\n"
    "Labels: " + ", ".join(LABELS) + "\n"
    'Return ONLY a JSON array of objects {"label": ..., "text": ...}. Copy each value EXACTLY as it appears in '
    "the text (same characters, spacing and spelling; for spoken values copy from the first to the last spoken "
    "token). List each distinct (label, value) pair once, in order of first appearance. "
    "If the text contains no personal data, return []."
)


def build_prompt(chunk: str) -> str:
    """The user turn the model expects. Pass this through your tokenizer's chat template."""
    return f"{INSTRUCTION}\n\nText:\n<<<\n{chunk}\n>>>"


# --------------------------------------------------------------------------------------------------
# input hygiene

_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def _as_text(value) -> tuple[str, list[str]]:
    """Coerce anything reasonable to a string without raising. Returns (text, warnings)."""
    warnings: list[str] = []
    if value is None:
        return "", ["input was None"]
    if isinstance(value, bytes):
        value = value.decode("utf-8", errors="replace")
        warnings.append("input was bytes, decoded as utf-8 with replacement")
    elif not isinstance(value, str):
        warnings.append(f"input was {type(value).__name__}, coerced with str()")
        value = str(value)
    if "�" in value:
        warnings.append("input contains U+FFFD replacement characters, upstream decoding may be wrong")
    cleaned = _CONTROL.sub(" ", value)
    if cleaned != value:
        warnings.append("control characters replaced with spaces")
    return cleaned, warnings


# --------------------------------------------------------------------------------------------------
# chunking

_WORD = re.compile(r"\S+")
# Places a transcript can be cut without splitting a turn: a newline, or the end of a subtitle cue.
_LINE_BREAK = re.compile(r"\n")


def _windows(text: str, window_words: int, overlap_words: int, snap: float = 0.25):
    """Yield (char_start, char_end) windows over `text`.

    Windows are built on word boundaries so a timestamp token such as '[00:01:02]' is never split. Where a
    newline sits near the computed edge, the edge snaps to it, which keeps one speaker turn or one subtitle
    cue inside a single window.
    """
    words = [(m.start(), m.end()) for m in _WORD.finditer(text)]
    n = len(words)
    if n == 0:
        return
    if n <= window_words:
        yield words[0][0], words[-1][1]
        return

    slack = max(1, int(window_words * snap))
    i = 0
    while i < n:
        j = min(i + window_words, n)
        start, end = words[i][0], words[j - 1][1]

        # Snap the trailing edge to the nearest newline within `slack` words, so a speaker turn or a
        # subtitle cue stays whole.
        if j < n:
            lo = words[max(i + 1, j - slack) - 1][1]
            hi = words[min(n, j + slack) - 1][1]
            nl = [m.end() for m in _LINE_BREAK.finditer(text, lo, hi)]
            if nl:
                end = min(nl, key=lambda p: abs(p - end))

        yield start, end
        if end >= words[-1][1]:
            return

        # First word not yet covered, then step back `overlap_words` so the next window re-reads context.
        # Scan from i, not j: a backward snap leaves words before j still uncovered, and starting at j
        # would step the next window past them.
        k = i
        while k < n and words[k][0] < end:
            k += 1
        i = max(i + 1, k - overlap_words)


# --------------------------------------------------------------------------------------------------
# output parsing

_OBJ = re.compile(r'\{\s*"label"\s*:\s*"((?:[^"\\]|\\.)*)"\s*,\s*"text"\s*:\s*"((?:[^"\\]|\\.)*)"\s*\}', re.S)


def _unescape(v: str) -> str:
    try:
        return json.loads('"' + v + '"')
    except json.JSONDecodeError:
        return re.sub(r'\\(["\\/])', r"\1", v).replace("\\n", "\n").replace("\\t", "\t")


def _parse(raw, labels: set[str]) -> tuple[list[dict], bool]:
    """Model text to entities. Tolerates code fences, prose around the array and trailing commas."""
    if not isinstance(raw, str) or not raw.strip():
        return [], False
    s = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip(), flags=re.S).strip()
    if s == "[]":
        return [], True
    a, b = s.find("["), s.rfind("]")
    cand = s[a:b + 1] if a != -1 and b > a else s
    ok = True
    try:
        items = json.loads(cand)
    except json.JSONDecodeError:
        try:
            items = json.loads(re.sub(r",\s*([\]}])", r"\1", cand))
        except json.JSONDecodeError:
            ok = False
            items = [{"label": m.group(1), "text": _unescape(m.group(2))} for m in _OBJ.finditer(s)]
    if not isinstance(items, list):
        return [], False
    out, seen = [], set()
    for e in items:
        if not isinstance(e, dict):
            ok = False
            continue
        lab, val = e.get("label"), e.get("text")
        if not isinstance(lab, str) or not isinstance(val, str):
            ok = False
            continue
        lab, val = lab.strip().upper(), val.strip()
        if lab in labels and val and (lab, val) not in seen:
            seen.add((lab, val))
            out.append({"label": lab, "text": val})
    return out, ok


# --------------------------------------------------------------------------------------------------
# locating values back in the source text

_ZW = "​‌‍⁠﻿"
_GAP = r"[\s" + _ZW + r"]*"


def _flex(value: str):
    """The value's non-blank characters in order, tolerating any whitespace or zero-width run between them.
    Finds values that the source spreads over a line break or salts with invisible characters."""
    chars = [c for c in value if not c.isspace() and c not in _ZW]
    if len(chars) < 3:
        return None
    return _GAP.join(re.escape(c) for c in chars)


# Scripts where a boundary test cannot work, so it is not applied: Chinese, Japanese, Thai, Lao, Khmer and
# Burmese put no space between words, and Korean attaches its particles straight onto the noun, so the
# character after a name is almost always another letter of the same sentence.
def _unspaced(ch: str) -> bool:
    o = ord(ch)
    return (0x1100 <= o <= 0x11FF or 0x3040 <= o <= 0x30FF or 0x3130 <= o <= 0x318F
            or 0x3400 <= o <= 0x4DBF or 0x4E00 <= o <= 0x9FFF or 0xAC00 <= o <= 0xD7AF
            or 0xF900 <= o <= 0xFAFF or 0x0E00 <= o <= 0x0EFF or 0x1780 <= o <= 0x17FF
            or 0x1000 <= o <= 0x109F)


def _wordish(ch: str) -> bool:
    # Combining marks count: the vowel sign in "राजेश" after "राज" means the word continues, even though the
    # mark is not alphanumeric. Without this, Indic and Arabic values match inside longer words. Variation
    # selectors and zero-width joiners are marks too but belong to emoji, so they are not part of a word.
    o = ord(ch)
    if 0xFE00 <= o <= 0xFE0F or 0x200B <= o <= 0x200F or 0xE0100 <= o <= 0xE01EF:
        return False
    return (ch.isalnum() or ch == "_" or unicodedata.category(ch).startswith("M")) and not _unspaced(ch)


def _bounded(text: str, a: int, b: int) -> bool:
    """False when the match sits inside a longer word or number: 'Raj' inside 'Rajesh', '2024' inside '20245'.
    Without this a three-letter name redacts the first syllable of every longer word that starts the same way."""
    if a > 0 and _wordish(text[a]) and _wordish(text[a - 1]):
        return False
    if b < len(text) and _wordish(text[b - 1]) and _wordish(text[b]):
        return False
    return True


def _find(text: str, value: str, lenient: bool):
    """Occurrences of `value` in `text` as (hits, partial), most literal match tier first.

    A whole-word match always wins. Only when the value occurs nowhere as a whole word does this fall back to
    matching inside a longer run, and it says so by returning partial=True. That fallback matters for redaction:
    when speech-to-text glues two words together ("sixfourteen park street"), refusing the match would leave a
    real address in the clear, which is worse than a mask that starts mid-word.
    """
    tiers = [(re.escape(value), 0), (_flex(value), 0)]
    if lenient:
        tiers.append((_flex(value), re.I))
    raw = []
    for pattern, flags in tiers:
        if not pattern:
            continue
        try:
            found = [(m.start(), m.end()) for m in re.finditer(pattern, text, flags) if m.end() > m.start()]
        except re.error:
            continue
        if not found:
            continue
        clean = [h for h in found if _bounded(text, *h)]
        if clean:
            return clean, False
        raw = raw or found
    return raw, True


# --------------------------------------------------------------------------------------------------
# the public function


def extract_pii(
    text,
    generate,
    *,
    window_words: int = 120,
    overlap_words: int = 25,
    labels=None,
    lenient: bool = True,
    propagate: bool = True,
    min_propagate_len: int = 4,
    max_chars: int = 2_000_000,
):
    """Find personal data in `text` of any length and return it with character offsets.

    Parameters
    ----------
    text
        The document. Anything str-able; None, bytes and other types are handled rather than raising.
    generate
        Callable taking a list of prompt strings and returning a list of model output strings, same length
        and order. See the adapters at the bottom of this file for transformers, an OpenAI-compatible server
        and llama.cpp. Batching is up to you; this function hands it every window at once.
    window_words, overlap_words
        Sliding window over the text, in words. The defaults are measured (see the module docstring); 100 to 150
        with 20-30 of overlap all behave about the same, and both smaller and larger settings are worse, for
        different reasons. Text shorter than one window is sent in a single call.
    labels
        Restrict to a subset of the 52 labels, for example {"PERSON", "PHONE"}. Default: all.
    lenient
        Also match values case-insensitively when locating them. Slightly higher recall, slightly higher risk
        of matching the wrong occurrence.
    propagate
        After merging, search the whole document for every value found anywhere, so a name the model reported
        in one window is also masked where a later window missed it. Values shorter than `min_propagate_len`
        are excluded, since short strings match coincidentally.
    max_chars
        Refuse to process beyond this, to avoid a runaway call. Reported as a warning, not an exception.

    Returns
    -------
    dict with keys
        spans        list of {"start", "end", "label", "text"}, sorted, non-overlapping, offsets into the
                     original string you passed in. A span also carries "partial": True when the value only
                     occurred inside a longer run of text, which is rare (0.6% of predictions on the test set)
                     and usually means speech-to-text ran two words together. Drop those if you would rather
                     under-mask than mask across a word edge.
        entities     list of unique {"label", "text"} in order of first appearance
        unlocatable  values the model returned that do not occur in the text. These are hallucinations and
                     the count is a useful health metric; they are not included in `spans`
        chunks       how many windows were used
        warnings     anything that went wrong, as plain strings. Empty list means a clean run
    """
    labels = set(labels) if labels else set(LABELS)
    body, warnings = _as_text(text)
    empty = {"spans": [], "entities": [], "unlocatable": [], "chunks": 0, "warnings": warnings}

    if not body.strip():
        return empty
    if len(body) > max_chars:
        warnings.append(f"input of {len(body):,} characters truncated to {max_chars:,}")
        body = body[:max_chars]
    if window_words < 60:
        warnings.append(f"window_words={window_words} is below the measured useful range; expect false "
                        f"positives, since the model loses the context that disambiguates a label")
    if overlap_words >= window_words:
        overlap_words = max(1, window_words // 4)
        warnings.append(f"overlap_words was >= window_words, reduced to {overlap_words}")

    spans_of = list(_windows(body, window_words, overlap_words))
    if not spans_of:
        return empty
    prompts = [build_prompt(body[a:b]) for a, b in spans_of]

    try:
        raws = generate(prompts)
    except Exception as exc:                                    # the model call is the caller's code
        warnings.append(f"generate() raised {type(exc).__name__}: {exc}")
        return {**empty, "chunks": len(prompts)}
    if not isinstance(raws, (list, tuple)) or len(raws) != len(prompts):
        warnings.append(f"generate() returned {type(raws).__name__} of unexpected length, expected {len(prompts)}")
        return {**empty, "chunks": len(prompts)}

    # Locate each window's values inside that window, then shift into document coordinates.
    found: list[dict] = []
    order: list[tuple[str, str]] = []
    unlocatable: list[dict] = []
    for idx, ((a, b), raw) in enumerate(zip(spans_of, raws)):
        chunk = body[a:b]
        ents, ok = _parse(raw, labels)
        if not ok:
            warnings.append(f"window {idx + 1} output was not valid JSON, recovered what was parseable")
        for e in sorted(ents, key=lambda e: -len(e["text"])):
            hits, partial = _find(chunk, e["text"], lenient)
            if not hits:
                unlocatable.append({**e, "window": idx + 1})
                continue
            if (e["label"], e["text"]) not in order:
                order.append((e["label"], e["text"]))
            for s, t in hits:
                while s < t and chunk[s].isspace():
                    s += 1
                while t > s and chunk[t - 1].isspace():
                    t -= 1
                if s < t:
                    sp = {"start": a + s, "end": a + t, "label": e["label"], "text": body[a + s:a + t]}
                    if partial:
                        sp["partial"] = True
                    found.append(sp)

    # A value seen in one window may be missed in another; look for every value across the whole document.
    if propagate:
        for lab, val in order:
            if len(val) < min_propagate_len:
                continue
            hits, partial = _find(body, val, lenient)
            for s, t in hits:
                sp = {"start": s, "end": t, "label": lab, "text": body[s:t]}
                if partial:
                    sp["partial"] = True
                found.append(sp)

    # Resolve overlaps: longest span wins, then the earliest. This is the same policy the training data uses.
    found.sort(key=lambda s: (-(s["end"] - s["start"]), s["start"]))
    kept: list[dict] = []
    for sp in found:
        if any(not (sp["end"] <= k["start"] or sp["start"] >= k["end"]) for k in kept):
            continue
        kept.append(sp)
    kept.sort(key=lambda s: s["start"])

    return {
        "spans": kept,
        "entities": [{"label": l, "text": v} for l, v in order],
        "unlocatable": unlocatable,
        "chunks": len(prompts),
        "warnings": warnings,
    }


def redact(text, spans, mask="[{label}]") -> str:
    """Replace each span in `text`. `mask` may use {label} and {text}, or be a plain string.

    >>> redact("Call Derek on 555-0142", spans)
    'Call [PERSON] on [PHONE]'
    """
    body, _ = _as_text(text)
    out = body
    for s in sorted(spans, key=lambda s: -s["start"]):
        try:
            rep = mask.format(label=s["label"], text=s.get("text", ""))
        except (KeyError, IndexError):
            rep = mask
        out = out[:s["start"]] + rep + out[s["end"]:]
    return out


# --------------------------------------------------------------------------------------------------
# generate() adapters. Pick one.

def transformers_generate(model, tokenizer, max_new_tokens=768, batch_size=8):
    """generate() backed by a local transformers model."""
    import torch

    tokenizer.padding_side = "left"
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    def run(prompts):
        outs = []
        for i in range(0, len(prompts), batch_size):
            batch = prompts[i:i + batch_size]
            rendered = [tokenizer.apply_chat_template([{"role": "user", "content": p}],
                                                      tokenize=False, add_generation_prompt=True) for p in batch]
            enc = tokenizer(rendered, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
            with torch.no_grad():
                gen = model.generate(**enc, max_new_tokens=max_new_tokens, do_sample=False,
                                     pad_token_id=tokenizer.pad_token_id)
            for row in range(len(batch)):
                outs.append(tokenizer.decode(gen[row][enc["input_ids"].shape[1]:], skip_special_tokens=True))
        return outs
    return run


def openai_generate(base_url="http://127.0.0.1:8000/v1", model="inboxpraveen/Kavach-PII-270M-v2",
                    api_key="EMPTY", max_tokens=768, workers=4):
    """generate() backed by any OpenAI-compatible server: vLLM, SGLang or llama-server."""
    from concurrent.futures import ThreadPoolExecutor
    from openai import OpenAI

    client = OpenAI(base_url=base_url, api_key=api_key)

    def one(prompt):
        r = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}],
                                           temperature=0, max_tokens=max_tokens)
        return r.choices[0].message.content or ""

    def run(prompts):
        with ThreadPoolExecutor(max_workers=workers) as ex:
            return list(ex.map(one, prompts))
    return run


if __name__ == "__main__":
    # Offline self-test of everything except the model call: window coverage, value boundaries, offsets,
    # merging, redaction and bad input. Needs no GPU and no model.
    import random

    failures = []

    def check(name, cond, detail=""):
        print(f"  {'PASS' if cond else 'FAIL'}  {name}{'' if cond else '  <- ' + detail}")
        if not cond:
            failures.append(name)

    # 1. Every word lands in at least one window, at every setting, on irregular line lengths.
    #    A window edge that snaps backwards used to leave a few words in no window at all.
    print("windowing")
    random.seed(3)
    lost = 0
    for win, ov in ((30, 8), (40, 10), (50, 12), (60, 12), (80, 16), (140, 28)):
        for _ in range(300):
            txt = "\n".join(" ".join(f"L{i}w{j}" for j in range(random.randint(2, 30))) for i in range(14))
            ws = [(m.start(), m.end()) for m in _WORD.finditer(txt)]
            wins = list(_windows(txt, win, ov))
            lost += sum(1 for a, b in ws if not any(p <= a and b <= q for p, q in wins))
    check("every word appears in some window", lost == 0, f"{lost} words fell between windows")

    # 2. A value must not match inside a longer word or number, while scripts without word spaces still match.
    print("value matching")
    boundary_cases = (
        ("Raj", "Raj works with Rajesh in Rajasthan.", 1, "must not hit Rajesh or Rajasthan"),
        ("2024", "Order 20245 was placed in 2024.", 1, "must not hit 20245"),
        ("ana@x.com", "mail ana@x.com or bana@x.com", 1, "must not hit bana@x.com"),
        ("राज", "राज और राजेश", 1,
         "Devanagari: the vowel sign continues the word"),
        ("홍길동", "홍길동은 서울에 삽니다.", 1,
         "Korean: an attached particle must not block the match"),
        ("田中", "田中さんは田中建設へ", 2,
         "Japanese has no spaces between words"),
        ("555-0142", "Call 555-0142 now.", 1, "punctuated values are still found"),
    )
    for val, txt, want, why in boundary_cases:
        got, partial = _find(txt, val, True)
        check(f"{val!r} matched {want}x whole-word", len(got) == want and not partial,
              f"{why}; got {len(got)}, partial={partial}")

    # 3. End to end over a transcript, with a stub model in place of the real one.
    print("end to end")
    transcript = (
        "[00:00:03] Speaker 1: Good morning, thank you for calling. This is Raj from J&T Express "
        "Singapore, how can I help you today?\n"
        "[00:00:09] Speaker 2: Hi Raj. I am calling about a parcel that has not arrived. My parcel is "
        "CK-80691 and my mobile is 555-0142 if you need to reach me about it later on.\n"
        "[00:00:15] Speaker 1: Thank you, let me pull that up on the system now. I can see it left the "
        "depot on Tuesday afternoon and has been showing as out for delivery since, which is unusual.\n"
        "[00:00:24] Speaker 2: That is what the tracking page told me too, which is why I wanted to ask "
        "somebody directly rather than keep refreshing the page all morning.\n"
        "[00:00:31] Speaker 1: Completely understood. I will text Rajesh at 555-0199 to chase the driver "
        "and we will come back to you before the end of the day.\n"
    )
    KNOWN = (("PERSON", "Raj"), ("ORGANIZATION", "J&T Express Singapore"), ("CASE_ID", "CK-80691"),
             ("PHONE", "555-0142"), ("PERSON", "Rajesh"), ("PHONE", "555-0199"))

    def stub(prompts):
        # whole-token match, the way the real model copies values
        return [json.dumps([{"label": l, "text": v} for l, v in KNOWN
                            if re.search(r"(?<![\w-])" + re.escape(v) + r"(?![\w-])", p)]) for p in prompts]

    r = extract_pii(transcript, stub, window_words=60, overlap_words=15)
    check("the transcript needed more than one window", r["chunks"] > 1, f"chunks={r['chunks']}")
    check("no warnings on clean input", r["warnings"] == [], str(r["warnings"]))
    check("offsets index the original string",
          all(transcript[s["start"]:s["end"]] == s["text"] for s in r["spans"]))
    check("spans do not overlap",
          all(a["end"] <= b["start"] for a, b in zip(r["spans"], r["spans"][1:])))
    red = redact(transcript, r["spans"])
    check("timestamps survive redaction", red.count("[00:0") == 5, red[:70])
    check("'Raj' did not eat the start of 'Rajesh'", "[PERSON]esh" not in red, red[:200])
    check("both phone numbers masked", red.count("[PHONE]") == 2, red[:200])
    check("nothing unlocatable", r["unlocatable"] == [], str(r["unlocatable"]))
    check("both names masked separately",
          red.count("[PERSON]") == 3, red[:200])

    # A value that occurs only inside a longer run is still masked, but flagged, so a caller can drop it.
    inside = extract_pii("Speaker 2: tomazh adams called.",
                         lambda p: ['[{"label":"PERSON","text":"mazh adams"}]'])
    check("value only inside a longer word is masked and flagged partial",
          len(inside["spans"]) == 1 and inside["spans"][0].get("partial") is True, str(inside["spans"]))
    check("a whole-word match is never flagged partial",
          all("partial" not in sp for sp in r["spans"]), str(r["spans"]))

    # An emoji's variation selector must not look like part of a word.
    emoji = extract_pii("ref ✉️TZ-59654 today",
                        lambda p: ['[{"label":"TRANSACTION_ID","text":"TZ-59654"}]'])
    check("emoji variation selector is not a word character",
          len(emoji["spans"]) == 1 and "partial" not in emoji["spans"][0], str(emoji["spans"]))

    # 4. Nothing raises, whatever it is handed.
    print("bad input")
    for bad in (None, b"bytes in", 12345, "", "   \n  ", ["a", "list"], {"k": "v"}, 3.14):
        try:
            res = extract_pii(bad, stub)
            check(f"{type(bad).__name__} handled", isinstance(res["spans"], list))
        except Exception as exc:
            check(f"{type(bad).__name__} handled", False, f"raised {type(exc).__name__}: {exc}")

    def boom(prompts):
        raise RuntimeError("model is down")

    check("generate() failure reported, not raised",
          extract_pii("Call Raj on 555-0142.", boom)["warnings"][0].startswith("generate() raised"))
    check("short generate() output caught",
          "unexpected length" in extract_pii("Call Raj on 555-0142.", lambda p: [])["warnings"][0])
    check("unparseable model output reported",
          any("not valid JSON" in w for w in extract_pii("Call Raj.", lambda p: ["sorry, I cannot"])["warnings"]))

    print()
    if failures:
        print(f"self-test: {len(failures)} FAILURE(S): {failures}")
        raise SystemExit(1)
    print("self-test: PASS")
```

</details>

## Prompt guidance

* Use the instruction above verbatim. The model was trained on exactly this text, and paraphrasing it costs accuracy.
* Use greedy decoding (`do_sample=False`, or `temperature: 0`). Sampling adds nothing on an extraction task and breaks JSON validity.
* `max_new_tokens` of roughly `48 + 1.6 * input_tokens` is enough. Output is short.
* Retry unparseable outputs once with `repetition_penalty=1.1`. Small models occasionally fall into a repetition loop on rare scripts. Re-decoding only the failures recovered 45 out of 45 in testing and raised F1 by 1.0 point. Applying a repetition penalty to every request lowered F1 by 1.4 points, so apply it only on retry.
* Normalise case first if your input may contain mixed random capitalisation. See [Limitations](#limitations).
* Send one document per call, and window anything long. The model was not trained on concatenated documents, and a single call carrying far more text than it saw in training loses recall badly. `kavach_extract.py` above does the windowing for you.

## Results

### By input condition

![Value-F1 by input condition](assets/02-conditions-radar.png)

| Condition | Test docs | Kavach | GLiNER | Presidio |
|---|---|---|---|---|
| Dialogue transcripts | 266 | **93.1** | 57.8 | 20.9 |
| Masked or partial values | 162 | **90.6** | 54.3 | 16.4 |
| Structured forms | 239 | **90.4** | 66.9 | 28.3 |
| OCR output | 74 | **90.4** | 70.1 | 30.9 |
| Clean text | 1,382 | **90.3** | 59.2 | 25.7 |
| Code and logs | 118 | **87.5** | 50.7 | 24.0 |
| ASR transcripts | 695 | **83.3** | 49.0 | 17.0 |
| Adversarial formatting | 247 | **82.5** | 52.8 | 16.1 |

The weakest condition for Kavach (adversarial formatting, 82.5) is above the strongest condition for GLiNER (OCR, 70.1).

Additional held-out slices: simulated ASR rewrites 88.9, real render-to-Tesseract OCR 81.4, and PII embedded in long real Wikipedia passages 82.4 with 0.0% false positives on the PII-free portions.

### By language

Each of the 29 language groups has at least 80 held-out test documents, so each figure carries a confidence interval of roughly 5 points rather than the 20 to 45 points you get from a 15-document sample. Kavach leads in all 29.

![Per-language comparison](assets/03-languages.png)

| Language | Test docs | Kavach F1 | 95% CI | GLiNER | Gain |
|---|---|---|---|---|---|
| Dutch | 81 | **94.3** | 91.6 to 97.0 | 74.7 | +19.6 |
| Russian | 81 | **93.9** | 91.2 to 96.1 | 59.2 | +34.7 |
| Simplified Chinese | 81 | **93.6** | 90.8 to 95.9 | 52.7 | +40.9 |
| German | 82 | **92.9** | 90.1 to 95.1 | 66.0 | +26.9 |
| Turkish | 83 | **92.6** | 89.7 to 95.2 | 68.2 | +24.4 |
| Romanized Indian language | 85 | **92.2** | 89.3 to 95.3 | 72.2 | +20.0 |
| Multilingual mix (3 or more) | 80 | **92.0** | 88.6 to 95.0 | 71.5 | +20.5 |
| Japanese | 85 | **91.8** | 88.5 to 94.7 | 37.3 | +54.5 |
| Korean | 80 | **91.4** | 87.8 to 94.5 | 47.0 | +44.4 |
| Vietnamese | 84 | **90.7** | 87.8 to 93.5 | 64.8 | +26.0 |
| Spanish | 116 | **90.4** | 87.1 to 92.8 | 68.4 | +22.0 |
| Polish | 82 | **90.0** | 86.0 to 93.1 | 69.2 | +20.8 |
| English | 994 | **89.3** | 88.2 to 90.4 | 58.8 | +30.5 |
| Indonesian | 83 | **89.2** | 85.4 to 92.6 | 69.0 | +20.2 |
| Punjabi | 83 | **88.4** | 84.9 to 91.6 | 32.9 | +55.5 |
| Urdu | 80 | **87.6** | 83.4 to 91.2 | 69.2 | +18.4 |
| French | 83 | **87.1** | 83.2 to 90.9 | 58.3 | +28.8 |
| Portuguese | 83 | **86.3** | 81.3 to 91.8 | 64.5 | +21.8 |
| Chinese | 84 | **85.9** | 79.5 to 91.0 | 29.6 | +56.3 |
| Marathi | 81 | **85.6** | 81.8 to 89.3 | 35.0 | +50.6 |
| Italian | 83 | **85.1** | 79.6 to 90.8 | 67.8 | +17.3 |
| Gujarati | 82 | **85.0** | 81.6 to 89.0 | 40.6 | +44.4 |
| Hindi | 105 | **84.8** | 80.8 to 88.5 | 39.0 | +45.8 |
| Malayalam | 83 | **83.5** | 77.8 to 88.6 | 31.3 | +52.2 |
| Tamil | 97 | **83.1** | 78.6 to 87.2 | 32.5 | +50.6 |
| Bengali | 87 | **82.2** | 77.5 to 87.1 | 39.6 | +42.6 |
| Arabic | 82 | **81.3** | 74.9 to 87.5 | 55.2 | +26.1 |
| Telugu | 82 | **80.6** | 73.6 to 86.8 | 25.4 | +55.2 |
| Kannada | 80 | **74.6** | 69.7 to 79.0 | 35.2 | +39.4 |

Languages are covered in native script, romanised form, and code-switched with English.

### By label

52 labels are supported. The table lists those with at least 50 test instances.

![Per-label comparison](assets/04-labels.png)

| Label | Test instances | Kavach F1 | GLiNER F1 |
|---|---|---|---|
| `PERSON` | 2853 | **93.8** | 43.1 |
| `ORGANIZATION` | 1972 | **87.1** | 69.5 |
| `PHONE` | 1899 | **93.2** | 76.2 |
| `DOB` | 1106 | **92.2** | 83.8 |
| `EMAIL` | 1092 | **94.4** | 81.9 |
| `ADDRESS` | 1067 | **81.4** | 54.6 |
| `CASE_ID` | 669 | **82.5** | 37.3 |
| `EMPLOYEE_ID` | 212 | **86.5** | 28.6 |
| `INSURANCE_ID` | 208 | **84.7** | 58.8 |
| `BANK_ACCOUNT` | 183 | **86.9** | 54.8 |
| `NATIONAL_ID` | 183 | **75.2** | 32.4 |
| `CREDIT_DEBIT_CARD` | 174 | **90.6** | 62.1 |
| `TAX_ID` | 151 | **70.8** | 47.6 |
| `MEDICAL_RECORD_ID` | 135 | **86.3** | 45.3 |
| `DATE_TIME` | 134 | **58.9** | not modelled |
| `TRANSACTION_ID` | 122 | **78.1** | not modelled |

Full label set, 52 in total:

`AADHAAR_IN` `ADDRESS` `AGE` `API_KEY_TOKEN` `BANK_ACCOUNT` `BIOMETRIC_DESCRIPTOR` `CARD_CVV` `CARD_EXPIRY` `CASE_ID` `CREDIT_DEBIT_CARD` `DATE_TIME` `DEVICE_ID` `DISABILITY` `DOB` `DRIVING_LICENSE` `EMAIL` `EMPLOYEE_ID` `ETHNICITY` `GENDER_SEX` `GEO_LOCATION` `HEALTH_ID` `IBAN` `INSURANCE_ID` `IP_ADDRESS` `LAB_ORDER_ID` `LICENSE_PLATE` `MAC_ADDRESS` `MEDICAL_RECORD_ID` `NATIONAL_ID` `ORGANIZATION` `PAN_IN` `PASSPORT` `PASSWORD_SECRET` `PERSON` `PHONE` `POLITICAL_BELIEF` `POSTAL_CODE` `PRESCRIPTION_ID` `RELIGION` `ROUTING_CODE` `SIGNATURE` `SSN_US` `STUDENT_ID` `SWIFT_BIC` `TAX_ID` `TRANSACTION_ID` `UPI_VPA` `URL_PERSONAL` `USERNAME` `VIN` `VOTER_ID` `WALLET_ID`

### Robustness

Eighteen offset-safe corruptions applied to held-out documents, measured against the model's own clean baseline.

![Robustness under corruption](assets/05-robustness.png)

Twelve of the eighteen cost under 1.5 F1, including zero-width character injection, homoglyph substitution, full-width characters, HTML and markdown wrapping, JSON escaping, whitespace noise, and separator changes. The exceptions are covered under [Limitations](#limitations).

## Compliance coverage

Mapped against the 18 HIPAA Safe Harbor identifiers, 16 of 18 have trained support. Identifier 17 is photographs, which is out of scope for a text model.

| HIPAA identifier | Label |
|---|---|
| Names | `PERSON` |
| Geography smaller than a state | `ADDRESS`, `POSTAL_CODE` |
| Dates, ages over 89 | `DOB`, `DATE_TIME`, `AGE` |
| Telephone and fax | `PHONE` |
| Email | `EMAIL` |
| Social Security numbers | `SSN_US` |
| Medical record numbers | `MEDICAL_RECORD_ID` |
| Health plan beneficiary numbers | `INSURANCE_ID`, `HEALTH_ID` |
| Account numbers | `BANK_ACCOUNT` |
| Certificate and licence numbers | `DRIVING_LICENSE`, `EMPLOYEE_ID` (NPI, DEA, professional licences) |
| Vehicle identifiers | `VIN`, `LICENSE_PLATE` |
| Device identifiers | `DEVICE_ID` |
| Web URLs | `URL_PERSONAL` |
| IP addresses | `IP_ADDRESS` |
| Biometric identifiers | `BIOMETRIC_DESCRIPTOR` |
| Any other unique identifying number | `CASE_ID`, `STUDENT_ID`, and the rest of the ID family |

Also covered: PCI (`CREDIT_DEBIT_CARD`, `CARD_EXPIRY`, `CARD_CVV`, `IBAN`, `SWIFT_BIC`, `ROUTING_CODE`), India (`AADHAAR_IN`, `PAN_IN`, `UPI_VPA`, `VOTER_ID`), and US healthcare administration (NPI, DEA, Medicare MBI, and state professional licences, trained under `EMPLOYEE_ID` and `HEALTH_ID`).

## Training

| | |
|---|---|
| Base model | `google/gemma-3-270m-it`, 268M parameters |
| Method | LoRA, r=64, alpha=128, dropout 0.05, on all attention and MLP projections (15.2M trainable, 5.4%) |
| Precision | base weights bf16 throughout, only the adapter was trained |
| Data | 58,596 training documents, 29.9M tokens |
| Schedule | 3 epochs, 11,202 steps, lr 2e-4 with linear decay and 3% warmup, effective batch 16 |
| Augmentation | 18 offset-safe corruption operations applied on the fly at p=0.35 |
| Hardware | one NVIDIA RTX 5060 Laptop GPU (8 GB), 4 hours, 5.75 GB peak |
| Loss | cross-entropy on the assistant JSON only, prompt tokens masked out |

Best dev loss 0.0397, against 0.0478 for the previous version.

### Dataset

65,307 documents and 238,254 labelled values, entirely synthetic. No real personal data was used.

| Split | Documents | Values | PII-free |
|---|---|---|---|
| train | 58,596 | 211,589 | 11,164 |
| dev | 3,339 | 13,019 | 743 |
| test | 3,372 | 13,646 | 736 |

The corpus spans 29 languages, 23 domains (contact centre, healthcare, pharmacy and labs, insurance, banking, government, telecom, e-commerce, education and HR, legal, IT helpdesk, logistics, real estate, automotive, and others) and 12 input conditions. It includes real noise round trips (browser render into Tesseract OCR, and an ASR simulator few-shot prompted on real Whisper output), PII embedded in real Wikipedia passages, and 600 hand-built negatives covering already-redacted text, blank forms, placeholder rows, and medical billing code lists.

Splits are grouped by synthetic identity, so no generated person appears on both sides of a split, and they are verified free of exact-text overlap. Documents derived from a training document move with their source, so a rewrite of a training document can never appear in test.

## Fair comparison notes

* All systems were scored by the same script, on the same 3,372 documents, against the same gold annotations.
* GLiNER-PII (`urchade/gliner_multi_pii-v1`) was queried with natural-language label names mapped to the 52 labels, threshold 0.4, 1,500-character chunks.
* Presidio used the default `AnalyzerEngine` with spaCy `en_core_web_lg`, threshold 0.35. Its recognisers are English-first, which is part of why it scores poorly on the multilingual portion. It is included because it is the most widely deployed open-source baseline, not because the comparison is favourable.
* Both systems can only lose recall on label types they do not model. Their label sets were mapped on a best-effort basis, and unmappable types were dropped from their predictions rather than counted as errors.
* The gold annotations came from the same pipeline that produced the training data. That is the honest caveat on every number here: it is our own test set. Independent evaluation on third-party corpora is the obvious next step.

## Limitations

* **Identifier typing has a ceiling.** A bare alphanumeric string with no nearby cue word cannot be classified as `TAX_ID` rather than `NATIONAL_ID` by any model. Only 15% of such confusions had a disambiguating cue within 40 characters. For redaction, what matters is that the value is found, and redaction recall stays at 93.0 even where type accuracy drops. Consider reporting family-level accuracy alongside exact accuracy.
* **Random capitalisation is the worst failure mode.** Mixed random caps cost 15.6 F1 and raise the false-positive rate on clean documents to 20%. The cause was found (the uppercase augmentation was missing from the training mix entirely, and case-chaos was weighted at 4%), the mix was rebalanced, and the model retrained. Uppercase robustness improved by 3.5 points but case-chaos improved by only 1.2. Normalise case before calling the model if your inputs may contain it.
* **Keyboard typos** cost 8.5 F1.
* **`SIGNATURE` against `PERSON`.** When a signature is the same string as a person's name in the same document, value-only output cannot separate them. This affects roughly 15% of `SIGNATURE` instances.
* **Weak labels.** `POSTAL_CODE` (33.8), `PAN_IN` (41.3), `AADHAAR_IN` (45.1) and `DATE_TIME` (58.9) are the soft spots. `DATE_TIME` is inherently contextual, since a date is only personal data when tied to a person.
* **Thin labels.** `ETHNICITY`, `AGE`, `GENDER_SEX`, `DISABILITY`, `POLITICAL_BELIEF` and `BIOMETRIC_DESCRIPTOR` have fewer than 10 test instances each. Treat their per-label numbers as indicative only.
* **Do not add a regex union.** This was tested. Combining the model with checksum and regex recognisers lowered F1 from 88.4 to 86.6 and raised the false-positive rate from 0.4% to 9.0%.
* **Synthetic training data.** Style is bounded by the generator that produced it. Real noise round trips, augmentation and real-text injection reduce that fingerprint but do not remove it.
* **Not a compliance guarantee.** This is a detection aid. Regulated workflows still need human review.

## Other formats

* Quantised GGUF builds for llama.cpp, Ollama and LM Studio: [Kavach-PII-270M-v2-GGUF](https://huggingface.co/inboxpraveen/Kavach-PII-270M-v2-GGUF)
* LoRA adapter only, 90 MB, applies to `google/gemma-3-270m-it`: the `adapter/` folder in this repository.

## Licence

Built with Gemma. This model is a fine-tune of `google/gemma-3-270m-it` and is governed by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms) and the [Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy), both of which pass through to you and to anyone you redistribute it to. The evaluation code is Apache-2.0 and the synthetic dataset is CC-BY-4.0.

## Citation

```bibtex
@software{kavach_pii_270m,
  title  = {Kavach PII 270M: multilingual personal data extraction with post-hoc span recovery},
  author = {Praveen Kumar},
  year   = {2026},
  version = {2},
  url    = {https://huggingface.co/inboxpraveen/Kavach-PII-270M-v2},
  note   = {Fine-tune of google/gemma-3-270m-it}
}
```
