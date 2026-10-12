---
license: gemma
base_model: inboxpraveen/Kavach-PII-270M-v2
new_version: inboxpraveen/Kavach-PII-270M-GGUF
library_name: gguf
pipeline_tag: text-generation
tags:
  - gguf
  - llama.cpp
  - quantized
  - pii
  - pii-detection
  - privacy
  - redaction
  - anonymization
  - ner
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

# Kavach PII 270M v2, GGUF builds

> **These are the GGUF builds of version 2 (released 2026-09-23), kept for reproducibility.** The current version is v3 at [inboxpraveen/Kavach-PII-270M-GGUF](https://huggingface.co/inboxpraveen/Kavach-PII-270M-GGUF). The GGUF files and figures are unchanged from the original v2 upload; [`kavach_extract.py`](kavach_extract.py), missing from that upload, is now included in its v2 form.

GGUF builds of [Kavach PII 270M v2](https://huggingface.co/inboxpraveen/Kavach-PII-270M-v2), a 270M parameter model that extracts 52 kinds of personal data from text in 29 languages. Runs in llama.cpp, Ollama, LM Studio, and anything else that reads GGUF.

Start with `Q4_K_M`. It matches the F16 reference exactly at 89.2 F1, is half the size, and produced zero parse failures.

![Accuracy against file size for every quantisation](assets/01-quantisation-tradeoff.png)

## Which file to download

| File | Size | Value F1 | Change vs F16 | Redaction recall | FP on clean docs | Verdict |
|---|---|---|---|---|---|---|
| `Kavach-PII-270M-Q4_K_M.gguf` | 249 MB | **89.2** | +0.0 | 94.1 | 0.0% | start here |
| `Kavach-PII-270M-Q8_0.gguf` | 286 MB | **89.3** | +0.1 | 94.3 | 0.0% | no compromise |
| `Kavach-PII-270M-Q6_K.gguf` | 278 MB | 89.0 | -0.2 | 93.9 | 0.0% | dominated by Q4_K_M |
| `Kavach-PII-270M-Q5_K_M.gguf` | 256 MB | 88.9 | -0.3 | 93.1 | 0.0% | dominated by Q4_K_M |
| `Kavach-PII-270M-F16.gguf` | 526 MB | 89.2 | reference | 94.0 | 0.0% | for re-quantising |
| `Kavach-PII-270M-Q4_K_M-emb_q4_0.gguf` | **169 MB** | 87.2 | -2.0 | 91.4 | 0.0% | smallest usable |
| `Kavach-PII-270M-Q5_K_M-emb_q5_0.gguf` | 196 MB | 88.0 | -1.2 | 93.0 | 0.0% | small, milder loss |
| `Kavach-PII-270M-Q3_K_M.gguf` | 239 MB | 88.4 | -0.8 | 94.0 | 0.0% | poor value, see below |
| `Kavach-PII-270M-Q2_K.gguf` | 234 MB | 84.9 | **-4.3** | 89.6 | **2.3%** | not recommended |

Measured on 400 stratified documents from the held-out test set. Each quant was served by `llama-server` with full GPU offload, greedy decoding, and identical prompts. Speed on an RTX 5060 Laptop was 8.2 to 9.2 documents per second across all quants, with peak resident memory between 1.9 and 2.5 GB.

## Why the low-bit quants are not worth it here

This model has an unusual shape that changes the normal quantisation advice.

The token embedding of Gemma-3-270M is 63% of its parameters (262,144 x 640 = 168M of 268M). llama.cpp keeps embeddings at high precision by default, so a nominal Q2_K build only reaches 6.88 bits per weight rather than the usual 2.6. It ends up just 6% smaller than Q4_K_M while costing 4.3 F1 and raising false positives on clean documents from 0.0% to 2.3%. For a redaction tool that trade goes the wrong way.

The hidden size is 640, which is not divisible by 256, the K-quant block size. During K-quantisation llama.cpp silently falls back to `q5_0` or `q8_0` for most tensors, printing a warning per tensor. That is the other half of why compression is poor.

The `-emb_*` files work around this by quantising the embedding as well, using block-32 legacy types that 640 is divisible by. That is what brings the model down to 169 MB.

One trap worth knowing: `--token-embedding-type q4_K` produces a corrupt file on this architecture. It converts, then fails a GGML assertion at write time, and `llama-quantize` still exits with status 0. The resulting file is rejected by llama.cpp with `invalid magic characters`. Use `q4_0`, `q5_0` or `q8_0` for the embedding instead.

## Usage

### llama.cpp

```bash
llama-server -m Kavach-PII-270M-Q4_K_M.gguf -c 4096 -ngl 99 --port 8080
```

```python
import json, requests

LABELS = ["AADHAAR_IN","ADDRESS","AGE","API_KEY_TOKEN","BANK_ACCOUNT","BIOMETRIC_DESCRIPTOR","CARD_CVV","CARD_EXPIRY",
"CASE_ID","CREDIT_DEBIT_CARD","DATE_TIME","DEVICE_ID","DISABILITY","DOB","DRIVING_LICENSE","EMAIL","EMPLOYEE_ID",
"ETHNICITY","GENDER_SEX","GEO_LOCATION","HEALTH_ID","IBAN","INSURANCE_ID","IP_ADDRESS","LAB_ORDER_ID","LICENSE_PLATE",
"MAC_ADDRESS","MEDICAL_RECORD_ID","NATIONAL_ID","ORGANIZATION","PAN_IN","PASSPORT","PASSWORD_SECRET","PERSON","PHONE",
"POLITICAL_BELIEF","POSTAL_CODE","PRESCRIPTION_ID","RELIGION","ROUTING_CODE","SIGNATURE","SSN_US","STUDENT_ID",
"SWIFT_BIC","TAX_ID","TRANSACTION_ID","UPI_VPA","URL_PERSONAL","USERNAME","VIN","VOTER_ID","WALLET_ID"]

INSTRUCTION = (
    "Extract all personal data (PII/PHI/PCI) from the text.\n"
    "Labels: " + ", ".join(LABELS) + "\n"
    'Return ONLY a JSON array of objects {"label": ..., "text": ...}. Copy each value EXACTLY as it appears in the '
    "text (same characters, spacing and spelling; for spoken values copy from the first to the last spoken token). "
    "List each distinct (label, value) pair once, in order of first appearance. "
    "If the text contains no personal data, return []."
)

def extract(text, url="http://127.0.0.1:8080/v1/chat/completions"):
    r = requests.post(url, json={
        "messages": [{"role": "user", "content": f"{INSTRUCTION}\n\nText:\n<<<\n{text}\n>>>"}],
        "temperature": 0, "max_tokens": 768,
    }).json()
    raw = r["choices"][0]["message"]["content"]
    return json.loads(raw[raw.find("["): raw.rfind("]") + 1])

print(extract("Patient Ananya Ramirez, DOB 03/07/1998, MRN 4829-1137, +1-617-555-0142."))
```

### Ollama

```bash
cat > Modelfile <<'EOF'
FROM ./Kavach-PII-270M-Q4_K_M.gguf
PARAMETER temperature 0
PARAMETER num_ctx 4096
EOF
ollama create kavach-pii -f Modelfile
ollama run kavach-pii
```

### LM Studio

Download `Kavach-PII-270M-Q4_K_M.gguf`, load it, set temperature to 0 and context to 4096, then paste the instruction above as the user message with your text appended.

### CPU only

```bash
llama-server -m Kavach-PII-270M-Q4_K_M-emb_q4_0.gguf -c 4096 -ngl 0 -t 8 --port 8080
```

At 169 MB with no GPU, this is the configuration for edge and on-premise deployments where the data cannot leave the machine.

## Long inputs, transcripts and character offsets

The model returns values, not character positions, and you locate them in the source text afterwards. A value the model invents cannot be located, so hallucinations are countable rather than silent: on the test set, 1.4% of predicted values did not occur in the source.

[`kavach_extract.py`](kavach_extract.py) ships in this repository and does the whole job in one function: overlapping windows over long text, one model call per window, values located in the original string, windows merged, character offsets returned. Standard library only. It works against a `llama-server` exactly as it does against `transformers`, because the server speaks the OpenAI API.

```bash
llama-server -m Kavach-PII-270M-Q8_0.gguf -c 4096 --host 127.0.0.1 --port 8080
```

```python
from kavach_extract import extract_pii, redact, openai_generate

gen = openai_generate(base_url="http://127.0.0.1:8080/v1", model="kavach")

transcript = open("call-transcript.txt", encoding="utf-8").read()
result = extract_pii(transcript, gen)

print(redact(transcript, result["spans"]))
print(result["chunks"], "windows,", len(result["spans"]), "spans,", result["warnings"])
```

Bracketed timestamps, SRT ranges and WebVTT cues pass through untouched and survive redaction. Long input is windowed automatically at 120 words with 25 of overlap, which is measured rather than guessed: below about 80 words the model loses the context that tells a date of birth from an appointment date, and past 250 its recall falls away. Anything shorter than one window is sent in a single call.

The example above is what was run against Q8_0 on this hardware: a 234-word transcript became three windows and a 449-word document five, offsets exact against the original string in both, all 13 timestamps intact after redaction, 2.6 seconds for the longer one. See the [main model card](https://huggingface.co/inboxpraveen/Kavach-PII-270M-v2#long-inputs-transcripts-and-character-offsets) for the window measurements and the full source.

## Prompt guidance

* Use the instruction above verbatim. The model was trained on exactly this text.
* Use greedy decoding (`temperature 0`). Sampling breaks JSON validity and adds nothing.
* Retry an unparseable output once with `repetition_penalty 1.1`. Applying that penalty to every request lowers accuracy.
* Normalise case if your input may contain mixed random capitalisation, which costs 15.6 F1. See the main model card.
* Send one document per request, and window anything long. `kavach_extract.py` in this repository does that for you.

## How these were built

```bash
# HF to GGUF F16
python llama.cpp/convert_hf_to_gguf.py Kavach-PII-270M/ \
    --outfile Kavach-PII-270M-F16.gguf --outtype f16

# standard quants
for Q in Q8_0 Q6_K Q5_K_M Q4_K_M Q3_K_M Q2_K; do
  llama-quantize Kavach-PII-270M-F16.gguf "Kavach-PII-270M-$Q.gguf" $Q 8
done

# embedding-quantised, block-32 types only because 640 is not divisible by 256
llama-quantize --token-embedding-type q4_0 Kavach-PII-270M-F16.gguf Kavach-PII-270M-Q4_K_M-emb_q4_0.gguf Q4_K_M 8
llama-quantize --token-embedding-type q5_0 Kavach-PII-270M-F16.gguf Kavach-PII-270M-Q5_K_M-emb_q5_0.gguf Q5_K_M 8
```

Built with llama.cpp `b11120`. Converting a Gemma-3 text checkpoint needs a one-line change in `conversion/base.py`. The tokenizer ships `<image_soft_token>` at id 262144 while the text model's embedding has 262,144 rows, which trips `assert max(tokenizer.vocab.values()) < vocab_size`. The vocab loop only reads ids below `vocab_size`, so that token is ignored either way. Change `<` to `<=`.

## Licence

Built with Gemma. These files are governed by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms) and the [Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy), both of which pass through to you and to anyone you redistribute them to.

Full evaluation results, per-language and per-label breakdowns, training details and limitations are in the [main model card](https://huggingface.co/inboxpraveen/Kavach-PII-270M-v2).
