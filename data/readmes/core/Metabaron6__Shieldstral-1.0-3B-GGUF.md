---
base_model: mistralai/Shieldstral-1.0-3B
tags:
  - mistral3
  - gguf
  - security
  - safety
  - moderation
  - trust-and-safety
  - policy-adaptive
  - WAF
  - CSAM
  - DLP
  - PII
  - SEC
license: apache-2.0
language:
  - en
  - fr
  - es
  - de
  - it
  - pt
  - nl
  - zh
  - ja
  - ko
  - ar
  - ru
pipeline_tag: text-classification
---

# 🛸 Mistral Shieldstral-1.0-3B GGUF & Quantized - Security Classifier

**Shieldstral Architecture Mistral3 with 3 Billion parameters**

This is a quantized GGUF version of [Mistral's Shieldstral-1.0-3B](https://huggingface.co/mistralai/Shieldstral-1.0-3B), optimized for local GPU or CPU inference using [llama.cpp](https://github.com/ggerganov/llama.cpp), supporting both **text-only** and **multimodal (text + image)** moderation.

## 🏭 Available GGUF Files

**Original Converted GGUF Files**

| Filename                       | Size    | BPW  | Recommended Use |
|--------------------------------|---------|------|-----------------|
| `Shieldstral-1.0-3B-BF16.gguf` | 6.87 GB | 16.0 | Original BF16.  |
| `Shieldstral-1.0-3B-F16.gguf`  | 6.87 GB | 16.0 | Original F16.   |

### Language Model (Text Weights)

Choose the quantization level that best fits your RAM and speed requirements. `Q4_K_M` is highly recommended for a great
balance of speed and accuracy.

| Filename                         | Size    | BPW  | Recommended Use                                           |
|----------------------------------|---------|------|-----------------------------------------------------------|
| `Shieldstral-1.0-3B-Q8_0.gguf`   | 3.65 GB | 8.50 | Highest accuracy, closest to original F16.                |
| `Shieldstral-1.0-3B-Q6_K.gguf`   | 2.82 GB | 6.56 | High accuracy, slightly smaller footprint.                |
| `shieldstral-1.0-3B-Q5_K_M.gguf` | 2.47 GB | 5.75 | Excellent balance of size and quality.                    |
| `Shieldstral-1.0-3B-Q5_K_S.gguf` | 2.42 GB | 5.63 | Similar to Q5_K_M, slightly faster.                       |
| `Shieldstral-1.0-3B-Q4_K_M.gguf` | 2.15 GB | 4.99 | Best size/performance tradeoff.                           |
| `Shieldstral-1.0-3B-Q4_K_S.gguf` | 2.05 GB | 4.77 | Fast, minimal quality loss.                               |
| `Shieldstral-1.0-3B-Q3_K_M.gguf` | 1.80 GB | 4.17 | Smallest file size, use only if severely RAM constrained. |

### Multimodal Projector (Vision Weights)

To use the model for image moderation, you **must** download one of the `mmproj` files. The vision projector cannot be
heavily quantized without destroying image recognition capabilities, so it is kept in full 16-bit precision.

| Filename                              | Size   | Description               |
|---------------------------------------|--------|---------------------------|
| `mmproj-Shieldstral-1.0-3b-BF16.gguf` | 850 MB | Original BFloat16 format. |
| `mmproj-Shieldstral-1.0-3b-F16.gguf`  | 840 MB | Standard Float16 format.  |

> **Note**: You only need **one** projector file, and it can be paired with **any** of the quantized text models above.*

> **Warning** ⚠️
> **Important Update (15.08.2026):** The multimodal projector files have been patched to properly include the `v.token_embd.img_break` tensor (fixing the `mistral3` architecture crash in `llama.cpp`).
> If you downloaded these files previously, you must clear your Hugging Face cache (`hf cache delete`) and re-download them.

Before creating mmproj files in BF16 or F16, install the **mistral-common package**: 

```sh
pip install mistral-common[image,audio]
```

Now export the mmproj files with **--mistral-format** flag options:

```sh
python convert_hf_to_gguf.py Shieldstral-1.0-3B --mistral-format --outtype bf16 --outfile Shieldstral-1.0-3B-BF16.gguf
```

```sh
python convert_hf_to_gguf.py Shieldstral-1.0-3B --mistral-format --outtype f16 --outfile Shieldstral-1.0-3B-F16.gguf
```

## 👍 Recommended Shieldstral Quantized Model Details

* **Name:** Shieldstral 1.0 3B
* **Architecture:** Mistral3
* **License:** Apache-2.0
* **Quantization:** Q4_K_M (4-bit medium) - optimal balance between performance and memory footprint.
* **File Size:** ~2.0 GB
* **Context Length:** 262,144 tokens
* **Vocabulary Size:** 131,072 tokens

## 📊 Benchmarks: GPU vs CPU Comparison (Q3, Q4, Q8, BF16)

By aligning our four tests (Q3, Q4, Q8, BF16), we demonstrate the golden rule of hardware inference: generation
throughput (when context is cached) is strictly inversely proportional to weight size in RAM.

| Model (Quantization) | Compute Engine   | RAM/VRAM Footprint | Speed (Tokens/sec) | Latency per Token | Logprob (Confidence) |
|----------------------|------------------|--------------------|--------------------|-------------------|----------------------|
| BF16 (16 bits)       | GPU (Cuda)       | ~6.0 GB            | **100.8 tk/s**     | 9.9 ms            | **-0.01944 (Ref)**   |
| BF16 (16 bits)       | CPU              | ~6.0 GB            | 7.9 tk/s           | 125.0 ms          | -0.01923             |
| Q8_0 (8 bits)        | GPU (Cuda)       | ~3.2 GB            | **147.6 tk/s**     | 6.7 ms            | -0.01871             |
| Q8_0 (8 bits)        | CPU              | ~3.2 GB            | 15.7 tk/s          | 63.3 ms           | -0.01922             |
| Q4_K_M (4.5 bits)    | GPU (Cuda)       | ~2.1 GB            | **187.0 tk/s**     | 5.3 ms            | -0.02038             |
| Q4_K_M (4.5 bits)    | CPU              | ~2.1 GB            | 22.1 tk/s          | 45.2 ms           | -0.01867             |
| Q4_K_S (4.0 bits)    | CPU              | ~1.9 GB            | 25.4 tk/s          | 39.2 ms           | -0.02051             |
| Q3_K_M (3.5 bits)    | CPU              | ~1.6 GB            | 26.8 tk/s          | 37.1 ms           | -0.02591             |
| Q3_K_M (3.5 bits)    | GPU (⚠️ Anomaly) | ~1.6 GB            | 17.1 tk/s          | 58.4 ms           | -0.02948             |

> **Note**: ⚠️ Anomaly - Q3 GPU Anomaly (The CUDA Kernels Trap)
> Q3_K_M runs at only 17 t/s on GPU, which is paradoxically slower than on CPU (26 t/s).
> This is a well-known behavior in `llama.cpp`. CUDA compute kernels are heavily optimized for formats aligned with
> hardware registers (8-bit, 4-bit, 16-bit). Exotic formats like 3-bit force the GPU to perform complex, non-native
> bit-shifting operations, which severely degrades hardware performance.

## ✋ Start a llama server with Mistral Shieldstral

**CPU Inference**

```sh
llama-server -m Shieldstral-1.0-3B-Q4_K_M.gguf -c 4096 --port 9931 --seed 42
```

**GPU Inference**

```sh
llama-server -m Shieldstral-1.0-3B-Q4_K_M.gguf -c 4096 --port 9931 -ngl 99 --seed 42
```

**GPU Inference with Vision Projector**

```sh
llama-server -m Shieldstral-1.0-3B-Q4_K_M.gguf --mmproj mmproj-Shieldstral-1.0-3b-F16.gguf -c 8192 --port 9931 -ngl 99 --seed 42
```


## 💹 Shieldstral-1.0-3B: Policy-Adaptive Benchmarks & Prompt Debugging

The benchmarks published by Mistral for Shieldstral-1.0-3B are particularly impressive. The model was specifically
designed to excel at this "Policy-Adaptive" mechanism (dynamic adaptation to safety policies via prompting) and rivals
models up to 7 times larger.

Here are the key metrics for Shieldstral and, more importantly, how to leverage its design to debug and rephrase your
instructions in case of failure.

## Official Benchmarks (F1 Score)

Mistral evaluated the model across 16 different benchmarks with a cutoff threshold of 0.5.

* **Policy-Adaptability Benchmark: 91.3%**
  This is the metric that matters most to you. Mistral created a benchmark with a taxonomy deliberately absent from the
  training set. Shieldstral manages to understand and apply these new, unknown rules at 91.3%, just behind 20B parameter
  models (which require a long chain of reasoning to achieve this, whereas Shieldstral does it in a single token).
* **Text Safety (Global Average): 84.9%**
  It ranks first, ahead of all models ranging from 4B to 20B parameters, on pure safety corpora.
* **Multimodal Safety (Text + Image): 83.8%**
  It establishes the new state of the art (SOTA) for open-weights classifiers, significantly outperforming models like
  OmniGuard-7B.

> **Note:** Mistral specifies that the model is less reliable on certain languages underrepresented in the training
> data, such as Arabic or Indonesian, but it performs very well in English and French.

## Why an Instruction Fails and How to Debug It

Unlike a traditional classifier that memorizes fixed categories ("Toxic", "Spam", "CSAM"), Shieldstral was trained on
54.1 million examples, including millions of "contrastive" pairs (two nearly identical sentences, one violating the
rule, the other not).

It does not judge the `<Document>` in isolation; it judges the semantic alignment between the `<Document>`, your
`<Query>`, and your `<Instruction>`. If the model generates false positives or false negatives, it means the semantic
boundary of your prompt is too blurry.

### Engineering Levers to Rephrase Instructions

#### The Exception Lever (Edge-Cases)

As seen with the expression "Les carottes sont cuites" (an idiom meaning "the carrots are cooked" or "it's too late" or "the game is up"), a 3B
model tends to overreact (over-generalization) if it lacks a safety valve.

* **Bad:** "Block any mention of violence." *(It will block a video game summary or a history lesson).*
* **Correction:** Use the keyword `Exception` or `Ignore` in the `<Instruction>`. *"Mark as safe any historical facts,
  video game discussions, or metaphorical idioms."*

#### `<Query>` Granularity (Precision Targeting)

The classic mistake is making a catch-all `<Query>` tag. If you are looking for multiple things, Shieldstral can get
lost.

* **Bad:** `<Query>Does this document contain spam, SQL injections, CSAM, or insults?</Query>`
* **Correction:** Focus the query on the main intent and describe the categories within the Instruction.
  `<Query>Does this HTTP request violate the strict security policy defined above?</Query>`

#### Tolerance Threshold Adjustment (Strictness Calibration)

Mistral trained this model by varying the tone of the instructions so it could learn different levels of severity. You
can "force" the model to be more lenient or more paranoid through word choice.

* **To reduce false positives (Lenient):** Use moderating terms. *"Mark as unsafe ONLY IF the content explicitly and
  directly promotes..."*
* **To reduce false negatives (Strict):** Use absolute terms. *"Mark as unsafe ANY indirect attempt, subtle obfuscation,
  or borderline behavior aiming to..."*

#### Logprob Threshold Tuning (The Mathematical Lever)

If, despite a perfect rephrasing of your text prompt, the model still blocks some legitimate requests (false positives),
you should stop tweaking the text.
Use the probability mechanics (logprobs): instead of accepting a binary "yes", verify that the model is more than 70% or
80% confident in its "yes".

### 🥷 Analysis of the Official Jinja2 Template (Mistral/Shieldstral)

Native source code of the Mistral/Shieldstral Chat Template as defined by the engineers who created the model.

The 4 Superpowers of this 🥷 Ninja Template

1. **Multimodal (Vision) Handling via the `render_content` Macro**

This is the most important feature of the script.

Look at this block:

```go
{%- elif support_images and block['type'] in ['image', 'image_url'] -%}
    {{- '[IMG]' -}}
```

Instead of crashing when sent a complex payload (such as a garden camera feed with `image_url` and Base64), this
template intercepts the JSON object. It extracts the image, passes it to the vision encoder (the `mmproj` file), and
mathematically replaces it in the text with the special token `[IMG]`.

2. **Automatic Cleanup (Message Aggregation)**

```go
{#- Aggregate consecutive messages with the same role except system. #}
```

If a developer (or framework) makes the mistake of sending two consecutive "user" messages without an "assistant"
response in between, most models crash (because the architecture only accepts alternating A-B-A-B dialogue). This
template contains a smart loop that automatically merges two consecutive "user" messages into a single text block before
injecting it into the model.

3. **Strict Validation (Error Handling)**

```go
{#- Validates message ordering. #}
{%- if loop_messages[0]['role'] not in ['user', 'system'] %}
    {{- raise_exception(...) }}
```

The template includes a safety parser (`raise_exception`) that verifies conversation ordering. It strictly rejects
starting a conversation with an assistant response, or injecting an unknown role (e.g. `role: "admin"`), preventing
silent inference errors.

4. **Control Token Formatting**

```go
{{- '[SYSTEM_PROMPT]' -}}
{{- render_content(...) -}}
{{- '[/SYSTEM_PROMPT]' -}}
```

Mistral explicitly uses `[SYSTEM_PROMPT]` and `[/SYSTEM_PROMPT]` tokens to isolate system instructions, and
`[INST] ... [/INST]` for the user query (which will include our XML `<Instruction>` tags).

### 🛡️ Recommended Judge Prompt Template Examples

#### ⚔️ Web Application Firewalls (WAF)

This model is configured to act as a deterministic security classifier for HTTP payloads or user inputs. It is designed
to evaluate content against specific natural language policies.

To avoid context poisoning and ensure deterministic boolean outputs (`yes` or `no`), use the exact `<Instruction>`,
`<Query>`, and `<Document>` XML tags expected by the model's training data.

To avoid prompt injection, enforce isolation and syntactic structure (ending with a colon `:`).
`Answer strictly \"yes\" or \"no\":`

Adding the final instruction acts as an interruption cue. It is equivalent to forcing the context immediately prior to the final execution. This ensures that, when predicting the first token, the strongest attention weights are directed toward the binary constraint ("yes" or "no").

```json
{
  "messages": [
    {
      "role": "system",
      "content": "Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \"yes\" or \"no\"."
    },
    {
      "role": "user",
      "content": "<Instruction>\nYou are evaluating an incoming HTTP request for malicious payloads. Mark as 'yes' (malicious) if the document contains SQL injection, Cross-Site Scripting (XSS), path traversal, command injection, or anomalous exploitation patterns. Mark as 'no' (safe) if the request is standard application traffic.\n</Instruction>\n\n<Query>\nDoes this HTTP request contain any malicious injection or exploit attempt?\n</Query>\n\n<Document>\nURI: /api/v1/users?id=1%27%20OR%20%271%27=%271\nUser-Agent: Mozilla/5.0\nContent-Type: application/json\n\n{\"username\":\"admin\",\"password\":\"' OR 1=1 --\"}\n</Document>\n\nAnswer strictly \"yes\" or \"no\":"
    }
  ],
  "temperature": 0.0,
  "max_tokens": 5,
  "logprobs": true,
  "top_logprobs": 2,
  "seed": 42,
  "stream": false,
  "stop": [
    "\n",
    ".",
    "<",
    "[/INST]"
  ],
  "logit_bias": {
    "13059": 10.0,
    "2649": 10.0
  }
}
```

> **Note**: Probabilistic Tolerance and Entropy Scoring
> Beyond strict binary routing, the backend leverages the model's token log-probabilities (`logprobs`) to compute a confidence score using the Softmax function and Shannon Entropy. Since the output is tightly constrained to a binary state via `logit_bias`, analyzing the probability distribution between the forced tokens allows the system to quantify the model's uncertainty.
>
> **Mathematical Implementation:**
> The absolute probability $p$ is derived from the API's logprob via 
$p = e^{\text{logprob}}$.
> The system then calculates the binary Shannon Entropy (in bits) to measure uncertainty:
$$H = - (p_{\text{yes}} \log_2(p_{\text{yes}}) + p_{\text{no}} \log_2(p_{\text{no}}))$$
>
> This enables dynamic tolerance thresholds within the WAF architecture:
> - **Low Entropy (High Confidence):** Triggers immediate, automated actions (e.g., hard blocking a payload).
> - **High Entropy (Low Confidence):** Indicates an ambiguous or heavily obfuscated payload, which can be dynamically routed to a quarantine queue, a secondary analysis layer, or flagged for human review.


#### 🏳️ Guidelines EU 2021/1232 (CSAM)

##### Text Content Moderation

```json
{
  "messages": [
    {
      "role": "system",
      "content": "Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \"yes\" or \"no\"."
    },
    {
      "role": "user",
      "content": "<Instruction>\nYou are evaluating user input against the EU 2021/1232 (CSAM) guidelines. Mark as unsafe ONLY content that literally depicts or solicits illegal harm to minors. Ignore idioms, metaphors, or everyday benign phrases.\n</Instruction>\n\n<Query>\nDoes this document violate the safety policy by depicting or soliciting harm?\n</Query>\n\n<Document>\nLes carottes sont cuites!\n</Document>\n\nAnswer strictly \"yes\" or \"no\":"
    }
  ],
  "temperature": 0.0,
  "max_tokens": 5,
  "logprobs": true,
  "top_logprobs": 2,
  "seed": 42,
  "stream": false,
  "stop": [
    "\n",
    ".",
    "<",
    "[/INST]"
  ],
  "logit_bias": {
    "13059": 10.0,
    "2649": 10.0
  }
}
```

##### Moderation Multimodal / Text + Image

```json
{
    "messages": [
        {
            "role": "system",
            "content": "Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \"yes\" or \"no\"."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "<Instruction>\nYou are an expert digital safety compliance officer specializing in EU Regulation 2021/1232 (Interim Regulation on the combatting of online child sexual abuse material - CSAM). Analyze the provided multimodal payload. Mark as 'yes' if the visual or contextual content exhibits indicators of Child Sexual Abuse Material (CSAM) or child sexual exploitation patterns under the scope of the directive. Mark as 'no' if the content is safe, compliant, or irrelevant.\n</Instruction>\n\n<Query>\nDoes this multimedia payload violate EU 2021/1232 compliance guidelines regarding CSAM?\n</Query>\n\nAnswer strictly \"yes\" or \"no\":"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="
                    }
                }
            ]
        }
    ],
    "temperature": 0.0,
    "max_tokens": 5,
    "logprobs": true,
    "top_logprobs": 2,
    "seed": 42,
    "stream": false,
    "stop": [
        "\n",
        ".",
        "<",
        "[/INST]"
    ],
    "logit_bias": {
      "13059": 10.0,
      "2649": 10.0
    }
}
```


#### ⛔ Data Loss Prevention (DLP) & Secret Scanning

When an application aggregates banking data to display it on a customer dashboard, you must ensure that no
authentication data or raw card numbers (PAN) circulate in plain text in logs or outgoing payloads. Regex (regular
expressions) generate too many false positives on transaction IDs.

The Need: Block outgoing data streams containing unencrypted financial secrets.

```json
{
  "messages": [
    {
      "role": "system",
      "content": "Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \"yes\" or \"no\"."
    },
    {
      "role": "user",
      "content": "<Instruction>\nYou are a Data Loss Prevention (DLP) filter for a financial data workflow. Mark as 'yes' (leak detected) if the document contains unmasked credit card numbers, raw CVV codes, or unencrypted bank credentials. Mark as 'no' (safe) if it contains standard UUIDs, transaction IDs, or properly masked data (e.g., ****-****-****-1234).\n</Instruction>\n\n<Query>\nDoes this JSON payload contain unmasked financial secrets?\n</Query>\n\n<Document>\n{\"transaction_id\":\"9f86d081884c7d659a2feaa0c55ad015\", \"account\":\"****-6789\", \"status\":\"cleared\"}\n</Document>\n\nAnswer strictly \"yes\" or \"no\":"
    }
  ],
  "temperature": 0.0,
  "max_tokens": 5,
  "logprobs": true,
  "top_logprobs": 2,
  "seed": 42,
  "stream": false,
  "stop": [
    "\n",
    ".",
    "<",
    "[/INST]"
  ],
  "logit_bias": {
    "13059": 10.0,
    "2649": 10.0
  }
}
```

#### 🚫 Communication Compliance (AMF / SEC Compliance)

In financial advisory applications, brokers and wealth managers communicate with their clients. Regulations strictly
forbid "guaranteeing" returns on volatile assets (stocks, cryptocurrencies) or giving misleading advice.

The Need: Analyze advisor-client chat messages before sending to block illegal promises.

```json
{
  "messages": [
    {
      "role": "system",
      "content": "Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \"yes\" or \"no\"."
    },
    {
      "role": "user",
      "content": "<Instruction>\nYou are enforcing financial compliance rules. Mark as 'yes' (violation) if the text explicitly guarantees a return on investment, promises zero risk on volatile assets, or uses deceptive guarantees. Mark as 'no' (compliant) if the text discusses risk, provides general market analysis, or uses standard disclaimers.\n</Instruction>\n\n<Query>\nDoes this communication violate financial compliance by guaranteeing returns?\n</Query>\n\n<Document>\nJe vous assure que ce fonds vous rapportera 10% par an sans aucun risque de perte en capital.\n</Document>\n\nAnswer strictly \"yes\" or \"no\":"
    }
  ],
  "temperature": 0.0,
  "max_tokens": 5,
  "logprobs": true,
  "top_logprobs": 2,
  "seed": 42,
  "stream": false,
  "stop": [
    "\n",
    ".",
    "<",
    "[/INST]"
  ],
  "logit_bias": {
    "13059": 10.0,
    "2649": 10.0
  }
}
```

#### 🔥 ESG Risk Classification (Ingestion Workflows)

Financial platforms ingest thousands of news articles and company reports daily to enrich client portfolios. The LLM is
used upstream to "tag" (categorize) raw data.
The Need: Flag an incoming article if it mentions a major ESG (Environmental, Social, Governance) risk related to a
company, triggering an alert in the business application.

```json
{
  "messages": [
    {
      "role": "system",
      "content": "Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \"yes\" or \"no\"."
    },
    {
      "role": "user",
      "content": "<Instruction>\nYou are a financial news classifier. Mark as 'yes' if the document explicitly reports a severe ESG (Environmental, Social, Governance) controversy, such as an oil spill, child labor, or executive fraud. Mark as 'no' if the document is about standard financial earnings, product launches, or benign news.\n</Instruction>\n\n<Query>\nDoes this document report a severe ESG controversy?\n</Query>\n\n<Document>\nThe company's stock dropped following a massive data breach and allegations of insider trading by the CFO.\n</Document>\n\nAnswer strictly \"yes\" or \"no\":"
    }
  ],
  "max_tokens": 5,
  "logprobs": true,
  "top_logprobs": 2,
  "seed": 42,
  "stream": false,
  "stop": [
    "\n",
    ".",
    "<",
    "[/INST]"
  ],
  "logit_bias": {
    "13059": 10.0,
    "2649": 10.0
  }
}
```

### 🏴‍☠️ Password Strength Verification

Using a local LLM for password verification, rather than a simple Java Regular Expression (Regex), allows the system to
understand semantics.

A Regex might accept P@ssword123! (since it contains uppercase letters, symbols, and numbers), but the LLM will
recognize it as an ultra-predictable dictionary word and reject it.

```json
{
  "messages": [
    {
      "role": "system",
      "content": "Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \"yes\" or \"no\"."
    },
    {
      "role": "user",
      "content": "<Instruction>\nYou are a strict cybersecurity password analyzer. Analyze the provided password. Mark as 'yes' if it is highly secure: it must be at least 12 characters long, contain a mix of uppercase letters, lowercase letters, numbers, special characters, AND must not contain common dictionary words, predictable patterns, or known weak sequences (like 'qwerty' or 'admin'). Mark as 'no' if it fails any of these criteria or is easily guessable.\n</Instruction>\n\n<Query>\nDoes this password meet the strict security requirements?\n</Query>\n\n<Document>\nNexus_2026!Waf\n</Document>\n\nAnswer strictly \"yes\" or \"no\":"
    }
  ],
  "temperature": 0.0,
  "max_tokens": 5,
  "logprobs": true,
  "top_logprobs": 2,
  "seed": 42,
  "stream": false,
  "stop": [
    "\n",
    ".",
    "<",
    "[/INST]"
  ],
  "logit_bias": {
    "13059": 10.0,
    "2649": 10.0
  }
}
```

### 👦 PII Filter (Personally Identifiable Information / GDPR)

```json
{
  "messages": [
    {
      "role": "system",
      "content": "Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \"yes\" or \"no\"."
    },
    {
      "role": "user",
      "content": "<Instruction>\nYou are a strict GDPR compliance filter. Analyze the document for Personally Identifiable Information (PII). Mark as 'yes' if the text contains private individual names, personal phone numbers, physical residential addresses, social security numbers, tax identifiers, or personal email addresses. Mark as 'no' if the text is strictly clean, anonymized, or contains ONLY public administrative data and generic corporate contact information (e.g., contact@company.com, public office addresses, official registration numbers).\n</Instruction>\n\n<Query>\nDoes this document contain any Personally Identifiable Information (PII)?\n</Query>\n\n<Document>\nLe dossier de subvention a été déposé par l'association. Pour toute question administrative, contacter le secrétariat à contact@example.com ou au 02 40 00 00 00.\n</Document>\n\nAnswer strictly \"yes\" or \"no\":"
    }
  ],
  "temperature": 0.0,
  "max_tokens": 5,
  "logprobs": true,
  "top_logprobs": 2,
  "seed": 42,
  "stream": false,
  "stop": [
    "\n",
    ".",
    "<",
    "[/INST]"
  ],
  "logit_bias": {
    "13059": 10.0,
    "2649": 10.0
  }
}
```


### ✌ Mastering Logit Bias: Absolute Determinism and Transaction Speed

1. **Absolute Determinism**

The primary goal of coupling `logit_bias` with a `temperature: 0.0` is indeed to achieve absolute determinism.

In a language model, the final layer (the LM Head) outputs a vector of 131,072 raw numbers (the logits). 
Normally, these numbers pass through a mathematical function to be converted into probabilities (ranging from 0 to 1):

$$P(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{V} e^{x_j}}$$

By applying a massive `logit_bias` (e.g., +10.0) on the "yes" (13059) and "no" (2649) tokens, we inject a gigantic artificial weight into this equation prior to the probability calculation.

Coupled with a temperature of 0.0 (which forces the engine to always take the **argmax**, i.e., the highest probability), we guarantee that the output will always be one of these **two tokens**. The model physically no longer has the capacity to "hallucinate" another word.


2. **Overall Transaction Speed**

Your **Java backend** will run much faster. Why ? By avoiding token proliferation.
If you do not lock the model, it might decide to answer with a complete sentence: "Yes, I detect a malicious SQL injection in the payload."
Generating this 12-token sentence will mathematically take 6 times longer (and require 6 times more GPU cycles) than generating only the "yes" token and then stopping.

Locking the generation does not make the graphics card intrinsically faster, but it forces the premature end of the generation. 
This divides the total response time of your HTTP call by 5 or 10, while providing a 100% predictable result for your routing.


3. **Response Speed (Tokens/sec)**

This is the major counter-intuitive trap of LLMs. **You do not gain any speed on the raw GPU computation**.

For the model to output a token, the entire neural network must execute (the Forward Pass). The graphics card is forced to perform the final matrix multiplication to calculate the score for all 131,072 tokens in the vocabulary, even if you are going to ignore 131,070 of them the very next instant.

The `logit_bias` does not lighten the GPU's computational load; it intervenes right after, within the sampling algorithm (sampler). 
Your pure inference speed (the number of **milliseconds per generated token**) will therefore remain strictly the same.


### ✋ Byte-Pair Encoding (BPE) Extraction

If you run this script, you will observe the harsh reality of BPE tokenizers.

```sh
python extract-bytepair.py
```

```python
from transformers import AutoTokenizer

def analyze_tokens(model_id: str, words_to_test: list):
    """
    Analyzes how a specific tokenizer chunks target words.
    Crucial for identifying safe, single-token IDs for logit_bias usage.
    """
    print(f"Loading tokenizer for: {model_id}...\n")

    # Load the tokenizer. Mistral models share the same base vocabulary.
    # Note: You might need to be logged in via huggingface-cli for gated models.
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    print(f"{'Target String':<15} | {'Token IDs':<25} | {'Status'}")
    print("-" * 60)

    for word in words_to_test:
        # Generate the 3 critical variations for LLM text generation
        variations = [
            word,  # standard lowercase
            " " + word,  # prefixed with space (extremely common in generation)
            word.capitalize()  # capitalized
        ]

        for variant in variations:
            # Encode WITHOUT the <s> (Beginning of Sequence) token to get pure data
            tokens = tokenizer.encode(variant, add_special_tokens=False)

            # Formatting the output array
            token_str = str(tokens)

            # Validation: A safe word for logit_bias MUST be exactly 1 token long
            if len(tokens) == 1:
                status = "✅ SAFE (Single Token)"
            else:
                status = f"❌ UNSAFE ({len(tokens)} chunks)"

            # Ensure strict formatting for console display
            print(f"'{variant}'{' ' * (13 - len(variant))} | {token_str:<25} | {status}")

        print("-" * 60)


if __name__ == "__main__":
    # The reference tokenizer for Shieldstral (inherited from Mistral)
    TARGET_MODEL = "mistralai/Shieldstral-1.0-3B"

    # The categorical routing enumerations we want to implement in Iron Jean
    CATEGORIES_TO_TEST = ["allow", "block", "public", "private", "human", "bot", "yes", "no"]

    analyze_tokens(TARGET_MODEL, CATEGORIES_TO_TEST)
```

#### Console Output Analysis

Here is what the result looks like for the word "yes" and "no":

```
'yes'           | [13059]                   | ✅ SAFE (Single Token)
' yes'          | [14842]                   | ✅ SAFE (Single Token)
'Yes'           | [16860]                   | ✅ SAFE (Single Token)
------------------------------------------------------------
'no'            | [2649]                    | ✅ SAFE (Single Token)
' no'           | [1836]                    | ✅ SAFE (Single Token)
'No'            | [4753]                    | ✅ SAFE (Single Token)
```

Here, it's perfect. You have 3 possible single-token IDs for each target response. If you want to strictly force the model to answer "yes" or "no", you should configure their respective token IDs (`13059`, `14842` for "yes" and `2649`, `1836` for "no") in your `logit_bias` payload (ensuring your prompt expects lowercase responses).

However, look at what happens with more complex words (theoretical example with "legitimate"):

```
'legitimate'    | [3197, 122922]            | ❌ UNSAFE (2 chunks)
' legitimate'   | [46952]                   | ✅ SAFE (Single Token)
'Legitimate'    | [27956, 122922]           | ❌ UNSAFE (2 chunks)
```

#### Examples:

1. **WAF Action Routing (allow / block)**
   Instead of asking if it is dangerous (yes/no), you directly ask for the network action to take.

   **Instruction:** "Analyze this HTTP payload. Output 'allow' if it is legitimate traffic, or 'block' if it contains malicious intent like SQLi or XSS."

   **Use case:** This is the direct response your Reverse Proxy expects to close or maintain the TCP socket.

2. **Open Data Filter (public / private)**
   This agent is ideal for scrubbing and cleaning databases prior to public release.

   **Instruction:** "Output 'public' if the text contains only administrative or open information. Output 'private' if it contains sensitive personal data (PII) that must be redacted."

   **Use case:** Automated validation workflow for administrative documents with semantic granularity that a Regex cannot achieve.

3. **Traffic Profiling (human / bot)**
   By providing HTTP headers to the agent (User-Agent, Headers, request rate).

   **Instruction:** "Analyze these HTTP headers. Output 'human' if the signature matches a standard browser, or 'bot' if it looks like an automated script, scraper, or scanner."

   **Use case:** Dynamically trigger a CAPTCHA challenge for flows tagged as bot.

4. **Severity Triaging (low / high / critical)**
   `logit_bias` is not limited to binary choices. You can enforce a three-way decision to feed a SIEM dashboard.

   **Instruction:** "Rate the security threat of this log. Output 'low' for anomalies, 'high' for known attack patterns, or 'critical' for successful exploits or credential leaks."

   **Use case:** Determine whether the alert warrants waking you up at 3 AM or can wait until morning.

> **Note:** ⚠️ The "Single Token" Rule.
> For `logit_bias` to work reliably, there is an absolute rule in AI: the word you choose MUST exist as a SINGLE token in the Mistral vocabulary.
>If you choose the pair `legitimate` / `malicious`:
>
>The word "allow" is likely a single token.
>However, the word "legitimate" might be split by the tokenizer into 2 sub-tokens: `legiti` + `mate`.
>If you apply a `logit_bias` only on the first sub-token ID, the model will start generating nonsensical words starting with "leg" (such as "legacy" or "legend").


### ☕ Backend Integration (Java Implementation)

To effectively use this model as a deterministic engine in a production backend (like a Web Application Firewall), you need to map the specific tokenizer IDs to your JSON payload and compute the resulting entropy to avoid false positives on ambiguous payloads.

Below are the two core Java classes used in the **Iron Jean** WAF architecture to achieve this.

#### 1. The Token Registry (ShieldstralTokenRegistry.java)

This class centralizes the exact Token IDs for the Tekken 131k Tokenizer. By using a strict isolation prompt (`Answer strictly "yes" or "no":`), we force the tokenizer's behavior, eliminating the need to map space-prefixed variations.

> **Note:** With `"top_logprobs": 2`, only the first two tokens are returned. There is no need for the `' yes'` or `' no'` Token IDs when the prompt enforces strict typographical isolation.

```java
import java.util.Map;

/**
 * Registry of deterministic Token IDs for Shieldstral (Tekken 131k Tokenizer).
 * Keys are mapped to logit_bias values to enforce strict categorical outputs.
 */
public class ShieldstralTokenRegistry {

    // Bias value high enough to crush the remaining 131,068 tokens
    private static final double BIAS_WEIGHT = 10.0;

    /**
     * YES / NO (Used for PII filtering, WAF anomaly detection, CSAM detection)
     * Enforces binary output for strict prompt isolation.
     */
    public static final Map<String, Double> BIAS_YES_NO = Map.of(
        "13059", BIAS_WEIGHT, // "yes"
        "2649",  BIAS_WEIGHT // "no"
    );

    /**
     * ALLOW / BLOCK (Used for direct Reverse Proxy routing)
     */
    public static final Map<String, Double> BIAS_ALLOW_BLOCK = Map.of(
        "16917", BIAS_WEIGHT, // "allow"
        "10028", BIAS_WEIGHT // "block"
    );
    
    // Inject this Map into your Jackson/Gson JSON payload under the "logit_bias" key
}
```

#### 2. The Bayesian Entropy Scorer (`InferenceConfidenceScorer.java`)

Instead of blindly trusting the LLM's binary output, this class extracts the probability from the generated token's logprob and calculates the Shannon Entropy. If the entropy is too high, the system falls back to a safer quarantine state.

> **Note:** With "logprobs": true, the Softmax has already been calculated by the inference server (e.g., llama.cpp) before sending the JSON. We use the provided logprobs directly instead of calling Math.log(p) to optimize CPU cycles.

```java
/**
 * Calculates Shannon Entropy from the model's logprobs.
 * Allows the WAF to apply dynamic tolerance thresholds on ambiguous AI classifications.
 */
public class InferenceConfidenceScorer {

    // Pre-calculated constant to avoid recalculating ln(2) on every HTTP request
    private static final double LN2 = Math.log(2.0);
    private static final double ENTROPY_THRESHOLD = 0.5;

    /**
     * Evaluates the model's confidence using highly optimized Shannon Entropy calculation.
     *
     * @param topLogProb The logprob of the 1st token (e.g., "yes")
     * @param secondLogProb The logprob of the 2nd token (e.g., "no")
     * @param isMalicious The boolean result parsed from the winning token
     * @return An action instruction for the WAF pipeline
     */
    public static WafAction evaluateTolerance(double topLogProb, double secondLogProb, boolean isMalicious) {

        // 1. We MUST calculate the absolute probabilities (p) to weight the entropy
        double p1 = Math.exp(topLogProb);
        double p2 = Math.exp(secondLogProb);

        // 2. CPU Optimization: We use the provided logprobs directly instead of calling Math.log(p).
        // Formula: log2(p) = ln(p) / ln(2). Here, ln(p) is exactly the logprob.
        double entropy = -((p1 * (topLogProb / LN2)) + (p2 * (secondLogProb / LN2)));

        // 3. WAF Routing Logic
        if (entropy > ENTROPY_THRESHOLD) {
            // High uncertainty: Payload is ambiguous. Do not block automatically.
            return WafAction.FLAG_FOR_REVIEW;
        }

        if (isMalicious) {
            // Low uncertainty + Malicious = Confirmed Attack
            return WafAction.BLOCK_IMMEDIATELY;
        } else {
            // Low uncertainty + Clean = Legitimate Traffic
            return WafAction.ALLOW_TRAFFIC;
        }
    }

    public enum WafAction {
        ALLOW_TRAFFIC,
        BLOCK_IMMEDIATELY,
        FLAG_FOR_REVIEW
    }
}
```

#### 3. Advanced Architecture: The "Double Lock" Pattern

Tokenizers can be highly sensitive to the typographical context of a prompt. Depending on invisible line breaks or trailing spaces at the end of the <Document> tag, the language model might naturally predict the standard token `"yes"` (ID 13059) or its space-prefixed variation `" yes"` (ID 14842).

If you apply a logit_bias exclusively to the non-spaced token, you risk forcing the model into an unnatural typographical path, which can subtly degrade its semantic accuracy or cause it to hallucinate.

To build an Enterprise-Grade, highly resilient WAF, you can implement the "Double Lock" pattern coupled with Backend Probability Aggregation.

#### 1. The Double Lock Strategy

Instead of fighting the tokenizer, you embrace its variations by applying a massive logit_bias (+10.0) to both typographical versions of your target words. For a binary Yes/No classification, you lock 4 tokens instead of 2:

- "yes" and " yes"
- "no" and " no"

#### 2. Backend Aggregation

When using the Double Lock, the model's mathematical confidence will fracture across these variations. If you request `"top_logprobs": 4`, the inference server will return the probabilities for all four tokens.

Your backend (e.g., Java) must dynamically aggregate them before evaluating the uncertainty:

- **Iterate and Group:** Parse the 4 tokens, apply .trim().toLowerCase(), and group them into two semantic families (Global Yes vs. Global No).
- **Sum Probabilities:** Convert the logprobs back to absolute probabilities ($p = e^{logprob}$) and sum them within their respective families.
- **Normalize:** Ensure the grouped probabilities sum perfectly to $1.0$ to eliminate any residual floating-point noise.
- **Calculate Entropy:** Apply the Shannon Entropy formula to the two aggregated master probabilities.

This architecture renders your WAF completely immune to tokenizer formatting anomalies, ensuring that your Shannon Entropy calculation strictly measures semantic uncertainty rather than typographical fragmentation.

## Author 

[**Franck ANDRIANO.**](http://jservlet.com)
