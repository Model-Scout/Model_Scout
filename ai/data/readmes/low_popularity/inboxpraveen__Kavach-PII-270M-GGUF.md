---
license: gemma
base_model: inboxpraveen/Kavach-PII-270M
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

# Kavach PII 270M, GGUF builds

GGUF builds of [Kavach PII 270M](https://huggingface.co/inboxpraveen/Kavach-PII-270M) v3, a 270M parameter model that extracts 43 kinds of personal data from text in 29 languages. Runs in llama.cpp, Ollama, LM Studio, and anything else that reads GGUF.

**This is v3.** It scores 92.0 value-F1 on the 4,577-document test set, against 79.0 for v2 on the same documents, and 90.4 on a code-built production probe where v2 scores 72.2. v3 uses a shorter label list, so update the `LABELS` in your prompt (the Usage example below has it). The [main model card](https://huggingface.co/inboxpraveen/Kavach-PII-270M#migrating-from-v2) lists every label change. v2's files remain in this repository's commit history.

Start with `Q5_K_M-emb_q5_0`. At 196 MB it is within 0.4 F1 of the F16 reference (92.0 against 92.4), smaller than every standard quant, and produced no parse failures. If file size does not matter, `Q6_K` and `Q8_0` match F16.

![Accuracy against file size for every quantisation](assets/01-quantisation-tradeoff.png)

## Which file to download

| File | Size | Value F1 | Change vs F16 | Redaction recall | Verdict |
|---|---|---|---|---|---|
| `Kavach-PII-270M-Q5_K_M-emb_q5_0.gguf` | 196 MB | **92.0** | -0.4 | 96.9 | start here |
| `Kavach-PII-270M-Q6_K.gguf` | 278 MB | **92.4** | +0.0 | 97.0 | matches F16 |
| `Kavach-PII-270M-Q8_0.gguf` | 286 MB | **92.3** | -0.1 | 97.0 | no compromise |
| `Kavach-PII-270M-Q5_K_M.gguf` | 256 MB | 92.1 | -0.3 | 96.8 | same accuracy as the 196 MB file, larger |
| `Kavach-PII-270M-F16.gguf` | 526 MB | 92.4 | reference | 97.2 | for re-quantising |
| `Kavach-PII-270M-Q4_K_M.gguf` | 249 MB | 91.3 | -1.1 | 96.1 | larger and less accurate than the 196 MB file |
| `Kavach-PII-270M-Q3_K_M.gguf` | 239 MB | 90.6 | -1.8 | 95.3 | poor value, see below |
| `Kavach-PII-270M-Q4_K_M-emb_q4_0.gguf` | **169 MB** | 90.0 | -2.4 | 95.8 | smallest usable |
| `Kavach-PII-270M-Q2_K.gguf` | 234 MB | 87.1 | **-5.3** | 93.3 | not recommended |

Measured on 400 documents sampled at even intervals from the 4,577-document test set. Each quant was served by `llama-server` with full GPU offload, greedy decoding and identical prompts, four requests in parallel with 4,096 tokens of context each and up to 1,024 output tokens. No quant produced a parse failure. Speed on an RTX 5060 Laptop GPU was 6.1 to 7.0 documents per second, with peak resident memory between 2.9 and 3.4 GB at that 16K total context. On 400 documents a difference of about half a point is within noise, so read the top five rows as equivalent. The sample holds only 26 documents with no personal data, too few to separate the quants on false positives; the main card has the full-test figure.

For v2, `Q4_K_M` matched F16 exactly. For v3 it loses 1.1 points, and the embedding-quantised `Q5_K_M` build is both smaller and closer to F16, so the recommendation has changed.

## Why the low-bit quants are not worth it here

This model has an unusual shape that changes the normal quantisation advice.

The token embedding of Gemma-3-270M is 63% of its parameters (262,144 x 640 = 168M of 268M). llama.cpp keeps embeddings at high precision by default, so a nominal Q2_K build only reaches 6.88 bits per weight rather than the usual 2.6. It ends up just 6% smaller than Q4_K_M while costing 5.3 F1 against F16. For a redaction tool that trade goes the wrong way.

The hidden size is 640, which is not divisible by 256, the K-quant block size. During K-quantisation llama.cpp silently falls back to `q5_0` or `q8_0` for most tensors, printing a warning per tensor. That is the other half of why compression is poor.

The `-emb_*` files work around this by quantising the embedding as well, using block-32 legacy types that 640 is divisible by. That is what brings the model down to 169 MB.

One trap worth knowing: `--token-embedding-type q4_K` produces a corrupt file on this architecture. It converts, then fails a GGML assertion at write time, and `llama-quantize` still exits with status 0. The resulting file is rejected by llama.cpp with `invalid magic characters`. Use `q4_0`, `q5_0` or `q8_0` for the embedding instead.

## Usage

### llama.cpp

```bash
llama-server -m Kavach-PII-270M-Q5_K_M-emb_q5_0.gguf -c 4096 -ngl 99 --port 8080
```

One setting to watch if you raise concurrency: with an explicit `--parallel N`, llama-server splits `-c` evenly between the slots, so `-c 4096 --parallel 4` leaves each request 1,024 tokens, too little for a long document plus its answer. Either leave `--parallel` on its automatic default, which shares one pool, or give it 4,096 tokens per slot (`-c 16384 --parallel 4`).

```python
import json, requests

LABELS = ["ADDRESS","AGE","API_KEY_TOKEN","BANK_ACCOUNT","BANK_CODE","BIOMETRIC_DESCRIPTOR","CARD_CVV","CARD_EXPIRY",
"CASE_ID","CREDIT_DEBIT_CARD","DATE_TIME","DEVICE_ID","DISABILITY","DOB","DRIVING_LICENSE","EMAIL","EMPLOYEE_ID",
"ETHNICITY","GENDER_SEX","GEO_LOCATION","HEALTH_ID","INSURANCE_ID","IP_ADDRESS","LAB_ORDER_ID","LICENSE_PLATE",
"MAC_ADDRESS","MEDICAL_RECORD_ID","NATIONAL_ID","ORGANIZATION","PASSPORT","PASSWORD_SECRET","PAYMENT_ID","PERSON",
"PHONE","POLITICAL_BELIEF","PRESCRIPTION_ID","RELIGION","STUDENT_ID","TRANSACTION_ID","URL_PERSONAL","USERNAME","VIN",
"VOTER_ID"]

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
        "temperature": 0, "max_tokens": 1024,
    }).json()
    raw = r["choices"][0]["message"]["content"]
    return json.loads(raw[raw.find("["): raw.rfind("]") + 1])

print(extract("Patient Ananya Ramirez, DOB 03/07/1998, MRN 4829-1137, +1-617-555-0142."))
# [{"label": "PERSON", "text": "Ananya Ramirez"}, {"label": "DOB", "text": "03/07/1998"},
#  {"label": "MEDICAL_RECORD_ID", "text": "4829-1137"}, {"label": "PHONE", "text": "+1-617-555-0142"}]
```

### Ollama

```bash
cat > Modelfile <<'EOF'
FROM ./Kavach-PII-270M-Q5_K_M-emb_q5_0.gguf
PARAMETER temperature 0
PARAMETER num_ctx 4096
PARAMETER num_predict 1024
EOF
ollama create kavach-pii -f Modelfile
ollama run kavach-pii
```

### LM Studio

Download `Kavach-PII-270M-Q5_K_M-emb_q5_0.gguf`, load it, set temperature to 0, context to 4096 and the response limit to 1024 tokens, then paste the instruction above as the user message with your text appended.

### CPU only

```bash
llama-server -m Kavach-PII-270M-Q4_K_M-emb_q4_0.gguf -c 4096 -ngl 0 -t 8 --port 8080
```

At 169 MB with no GPU, this is the configuration for edge and on-premise deployments where the data cannot leave the machine.

## Long inputs, transcripts and character offsets

The model returns values, not character positions, and you locate them in the source text afterwards. A value the model invents cannot be located, so hallucinations are countable rather than silent: on the test set, 0.8% of predicted values did not occur in the source.

[`kavach_extract.py`](kavach_extract.py) ships in this repository and does the whole job in one function: overlapping windows over long text, one model call per window, values located in the original string, windows merged, character offsets returned. Standard library only. It works against a `llama-server` exactly as it does against `transformers`, because the server speaks the OpenAI API.

```bash
llama-server -m Kavach-PII-270M-Q5_K_M-emb_q5_0.gguf -c 4096 --host 127.0.0.1 --port 8080
```

```python
from kavach_extract import extract_pii, redact, openai_generate

gen = openai_generate(base_url="http://127.0.0.1:8080/v1", model="kavach")

transcript = open("call-transcript.txt", encoding="utf-8").read()
result = extract_pii(transcript, gen)

print(redact(transcript, result["spans"]))
print(result["chunks"], "windows,", len(result["spans"]), "spans,", result["warnings"])
```

Bracketed timestamps, SRT ranges and WebVTT cues pass through untouched and survive redaction. Long input is windowed automatically at 120 words with 25 of overlap, which is measured rather than guessed: past about 180 words a single answer stops listing everything in a dense input. Anything shorter than one window is sent in a single call. See the [main model card](https://huggingface.co/inboxpraveen/Kavach-PII-270M#long-inputs-transcripts-and-character-offsets) for the window measurements and the full source.

The example above was run against `Q5_K_M-emb_q5_0` on an RTX 5060 Laptop GPU: a 294-word call transcript became three windows and returned 26 spans, and a 270-word one three windows and 9 spans. Offsets were exact against the original string in both, all 33 timestamps were intact after redaction, and each document took under 0.7 seconds.

## Prompt guidance

* Use the instruction above verbatim, with the 43-label list. The model was trained on exactly this text.
* Use greedy decoding (`temperature 0`). Sampling breaks JSON validity and adds nothing.
* Allow 1024 output tokens. Most answers are short, but a dense bank statement or CSV export can need more than 800 tokens, and a 768-token cap truncates those answers mid-list.
* Retry an unparseable output once with `repetition_penalty 1.1`. Applying that penalty to every request lowers accuracy.
* Normalise case first if your input may contain random mixed capitalisation (`jOhN sMiTh`). It still costs 8.5 F1 and makes the model flag far more documents that contain no personal data. See [Limitations](https://huggingface.co/inboxpraveen/Kavach-PII-270M#limitations).
* Send one document per request, and window anything long. `kavach_extract.py` in this repository does that for you.

## How these were built

```bash
# HF to GGUF F16
python llama.cpp/convert_hf_to_gguf.py Kavach-PII-270M/ \
    --outfile Kavach-PII-270M-F16.gguf --outtype f16

# standard quants
for Q in Q8_0 Q6_K Q5_K_M Q4_K_M Q3_K_M Q2_K; do
  llama-quantize Kavach-PII-270M-F16.gguf "Kavach-PII-270M-$Q.gguf" $Q
done

# embedding-quantised, block-32 types only because 640 is not divisible by 256
llama-quantize --token-embedding-type q4_0 Kavach-PII-270M-F16.gguf Kavach-PII-270M-Q4_K_M-emb_q4_0.gguf Q4_K_M
llama-quantize --token-embedding-type q5_0 Kavach-PII-270M-F16.gguf Kavach-PII-270M-Q5_K_M-emb_q5_0.gguf Q5_K_M
```

Built with llama.cpp `b11120`. Converting a Gemma-3 text checkpoint needs a one-line change in `conversion/base.py`. The tokenizer ships `<image_soft_token>` at id 262144 while the text model's embedding has 262,144 rows, which trips `assert max(tokenizer.vocab.values()) < vocab_size`. The vocab loop only reads ids below `vocab_size`, so that token is ignored either way. Change `<` to `<=`.

## Licence

Built with Gemma. These files are governed by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms) and the [Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy), both of which pass through to you and to anyone you redistribute them to.

Full evaluation results, per-language and per-label breakdowns, training details and limitations are in the [main model card](https://huggingface.co/inboxpraveen/Kavach-PII-270M).
