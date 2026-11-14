---
license: apache-2.0
pipeline_tag: text-classification
base_model:
- convaiinnovations/laya-multilingual
tags:
- gguf
- decision-model
- system-one
- jev-compatible
- typesafe
- laya
- llama.cpp
- aimtas
- smart-farm
- aquaculture
- livestock
- poultry
- agriculture
language:
- multilingual
- en
- vi
- ja
- ko
- zh
---
# AIMTAS System One — Laya Multilingual (GGUF, Q8_0)

**The System One decision model of the [AIMTAS smart farm](https://lecompany.co/aimtas-farm/)** — a [Jev-compatible](https://docs.typesafe.ai/introduction) System One,
trained on **AIMTAS-specific smart-farm data**. AIMTAS is an IoT + AI platform for agricultural smart farms — fish, prawn, chicken, pig and mixed farms; its Thần Nông AI
uses a fast **System 1** (this model) before and after retrieval, and a large language model as **System 2**.

**What makes it different from the original Laya:** the original `convaiinnovations/laya-multilingual` is a general-purpose
decision model; this AIMTAS model is trained on **specific data from the [AIMTAS smart farm](https://lecompany.co/aimtas-farm/)**
— its sensors, equipment, farm knowledge and operator messages in English, Vietnamese, Japanese, Korean and Chinese — so it answers AIMTAS's
own farm decisions (see [How it differs](#how-it-differs-from-the-original-laya-model)).

- **Jev-compatible System One API.** Served by llama.cpp on **`POST /v1/systemone`**, which follows TypeSafe's System One API
  (the API of TypeSafe **Jev** — [docs.typesafe.ai](https://docs.typesafe.ai/introduction)): send a `state` and typed questions
  (`choice`, `score`, `noul`) and get typed answers with probabilities in one forward pass. It is a drop-in, self-hosted
  alternative to Jev for System One decisions. It does **not** generate text.
- **Multilingual, focused on five languages: English, Vietnamese, Japanese, Korean and Chinese.** The base model reads 100+ languages; AIMTAS works and
  evaluates in these five (Japanese, Korean and Chinese evaluation is being added).
- **Trained on AIMTAS smart-farm data.** The AIMTAS training data comes from the
  [AIMTAS smart farm](https://lecompany.co/aimtas-farm/) (urgency, equipment, passage relevance, operator messages in
  en / vi / ja / ko / zh). Note: the file in this release is still the base model converted to GGUF — **zero-shot** — and the
  AIMTAS-trained weights replace it in a later release here on Hugging Face.
- **Never actuates.** Its answers are advice; AIMTAS keeps interlocks, envelopes, limits and modes in deterministic code.

Base: [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) (mmBERT-base encoder +
decision head, 322 M parameters, 1024-token context, Apache-2.0). Live AIMTAS server: the Hugging Face Space
[`letrthang/aimtas-system-one-decision-model-laya`](https://huggingface.co/spaces/letrthang/aimtas-system-one-decision-model-laya) — **try it there without a key**,
or call the typed `/v1/systemone` with the **public test key** `laya-api-key-for-testing` from a TypeSafe / Jev client (see below).

> ### 🧪 Reference project — Laya in a full RAG app
> **[spring-ai-with-hybrid-search-and-system-one-typesafe-jev](https://github.com/letrthang/spring-ai-with-hybrid-search-and-system-one-typesafe-jev)**
> · ▶ **[Live demo](https://spring-ai-with-hybrid-search-and-system.onrender.com)**
>
> A Spring AI + Vaadin demo that uses this model as its **⚡ System 1** through the TypeSafe / Jev SDK
> (`spring-ai-starter-typesafe` + `typesafe-spring-ai`) on the Space's `/v1/systemone` with the public test key:
> Weaviate finds passages (BM25 + vector, fused with RRF), **Laya keeps, drops and re-ranks them** with
> `JevDocumentFilter` and `JevDocumentReranker` (relevant · answers · prompt injection), an OpenRouter LLM writes the answer as
> System 2 — and **Laya checks that answer** before it is learned and reused. Every call is shown in a data-flow
> diagram; English, Vietnamese and Japanese; also an AI agentic mode.

## How it differs from the original Laya model
The original [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) is a
**general-purpose** decision model (trained on tasks such as ticket triage, routing and moderation). It knows nothing about
farms — for example, it does not know that dissolved oxygen of 2.1 mg/L and falling is an emergency, or that an aerator is the fix.

The AIMTAS model is the same architecture **trained on AIMTAS-specific data for the
[AIMTAS smart farm](https://lecompany.co/aimtas-farm/)**:
- sensor scenarios from AIMTAS farms and the AIMTAS device simulator (dissolved oxygen, water temperature, pH, ammonia,
  salinity, turbidity — values, normal bands, trends, day/night, sensor faults) labelled with the AIMTAS triage rules;
- operator messages as AIMTAS operators really write them, in **English, Vietnamese, Japanese, Korean and Chinese**;
- relevance pairs between farm signals and AIMTAS farm knowledge (SOPs, Training Profile knowledge);
- AIMTAS's own System One questions (urgency, target equipment, intent, keep this passage, does it need System 2), the same
  questions the AIMTAS gateway and cloud ask on `/v1/systemone`;
- over time, anonymised real AIMTAS decisions and their outcomes.

**Status (2026-10-10):** the file in this repo is still the base model converted to GGUF (zero-shot, 8/16 on the AIMTAS farm
cases). The AIMTAS-trained weights replace it in a later release of this repo, with the training data version and evaluation
numbers in this card.

| File | Size | SHA-256 |
|---|---|---|
| `laya-multilingual-Q8_0.gguf` | 342 MiB | `ff4f8a23afd63506dcea51b83c9dd37be66d066a2e8f4b2f114737abdd449c89` |

## Try it — public demo, no key
Open the [Space](https://huggingface.co/spaces/letrthang/aimtas-system-one-decision-model-laya) and use the **Try it** box, or call
`POST /demo/systemone` (same request and response as `/v1/systemone`):

```sh
curl -s https://letrthang-aimtas-system-one-decision-model-laya.hf.space/demo/systemone -H 'Content-Type: application/json' \
  -d '{"state":"Pond 1: dissolved oxygen 2.1 mg/L, normal 5-9, falling.",
       "questions":{"problem":{"type":"choice","instructions":"What is wrong with the water?",
         "criteria":{"OXYGEN":"oxygen too low","PH":"pH out of range","TEMPERATURE":"too hot or cold","NONE":"nothing is wrong"}}}}'
```

Limits: 10 calls/min per user and 60/min for everyone (`429`), body ≤ 2 KB (`413`), 1–3 questions per call (`400`), 30 s.
Calls are read-only — the model stores nothing and never actuates. The AIMTAS apps use the keyed `/v1/systemone`. The free
Space sleeps when idle; the first call may answer `503` for about a minute.

## Test key — the typed API from a TypeSafe / Jev client
To test a TypeSafe / Jev client (e.g. [`spring-ai-starter-typesafe`](https://central.sonatype.com/artifact/org.springaicommunity/spring-ai-starter-typesafe))
against the real **`POST /v1/systemone`** of the Space, use the **public test key** below. It is published on purpose: it is
not the server's secret (the Space swaps it for its own key inside the container), and it works on `/v1/systemone` only —
other `/v1/*` routes answer `401`. For testing, not for production apps.

| | |
|---|---|
| Base URL | `https://letrthang-aimtas-system-one-decision-model-laya.hf.space` |
| Test key | **`laya-api-key-for-testing`** (the owner can change it or turn it off) |
| Header | `Authorization: Bearer laya-api-key-for-testing` |
| Calls per client IP | 30 / min, burst 15 → `429` |
| Calls for all test-key users | 60 / min, burst 30 → `429` |
| Size / speed | one question + the `state` must fit 1024 tokens; use a client timeout of 60 s |

```sh
curl -s https://letrthang-aimtas-system-one-decision-model-laya.hf.space/v1/systemone \
  -H 'Authorization: Bearer laya-api-key-for-testing' -H 'Content-Type: application/json' \
  -d '{"state":"Hi, we were billed twice for March. Please refund the duplicate today.",
       "questions":{"billing":{"type":"noul","instructions":"Is this about a payment or an invoice?"}}}'
# → {"answers":{"billing":{"type":"noul","noul":0.9…}},…}
```

Spring Boot with `org.springaicommunity:spring-ai-starter-typesafe` + `typesafe-spring-ai` (`application.yml`):
```yaml
spring:
  ai:
    typesafe:
      base-url: https://letrthang-aimtas-system-one-decision-model-laya.hf.space
      api-key: laya-api-key-for-testing
      timeout: 60s
      retry:
        max-retries: 0          # the test-key limits answer 429; let the app decide when to try again
```
The starter then provides a `TypeSafeClient` bean for `JevDocumentFilter`, `JevDocumentReranker` and the other
`typesafe-spring-ai` classes, or for direct calls:
```java
SystemOneResponse r = client.systemOne("We were billed twice for March.",
        Map.of("billing", Noul.of("Is this about a payment or an invoice?")));
```
The `model` field the client sends (`jev-latest` by default) is ignored: the Space always answers with this model.
This zero-shot release answers best when each question is one plain sentence; see the reference project above for wording
that works with `JevDocumentFilter`.

## Run
```sh
llama-server -hf letrthang/aimtas-laya-multilingual-GGUF:Q8_0 --ubatch-size 1024 --batch-size 1024 --api-key <key>

curl http://127.0.0.1:8080/v1/systemone -H "Authorization: Bearer <key>" -H 'Content-Type: application/json' -d '{
  "state": "Ao 1 lúc 3 giờ sáng oxy hòa tan chỉ còn 2,1 mg/L và vẫn đang giảm.",
  "questions": {"urgent": {"type": "noul", "instructions": "Does this need action right now?"}}}'
```
A decision model runs in embedding mode: one question's whole prompt (question + options + state) must fit `--ubatch-size`;
the model was trained on 1024 tokens.

## How it was made
- llama.cpp **v0.6.0** (`/v1/systemone` support: ggml-org/llama.cpp PR #29818), `convert_hf_to_gguf.py <checkpoint> --outtype q8_0`.
  The converter detects the checkpoint as a Laya decision model (`encoder/config.json` + `rl_agent_config.json` + `tokenizer/`)
  and writes `{arch}.decision.type = laya` and the `systemone` template; llama-server logs `decision model type: laya`.
- One input fix: the checkpoint's `tokenizer/tokenizer_config.json` lists `extra_special_tokens` as a list (transformers v5
  format); the converter's transformers 4.57 needs it as `additional_special_tokens`. Same tokens, same vocabulary.
- Why not the existing community GGUFs: on llama.cpp v0.6.0 `Weidows/laya-multilingual-GGUF` loads but answers 501 "This model
  is not a decision model", and `mys/laya-multilingual-GGUF` fails with "unknown model architecture 'ggmlc'".

## Checked (2026-10-10)
- Loads on llama.cpp v0.6.0; every `/v1/systemone` answer well-formed; container memory ≈ 0.45 GB.
- ≈ 2.3× faster than the English `ggml-org/Laya-GGUF:Q8_0` on the same CPU.
- Zero-shot on 16 fish/prawn-pond System 1 cases (the first farm types evaluated; chicken, pig and mixed farms follow with the training data) (English + Vietnamese): 8/16 with plain-sentence states — the same as the English
  model. Zero-shot Laya does not judge numeric urgency reliably; fine-tune on your own decisions for production accuracy.

Used by the AIMTAS smart-farm platform's System 1 server (Hugging Face Space
[`letrthang/aimtas-system-one-decision-model-laya`](https://huggingface.co/spaces/letrthang/aimtas-system-one-decision-model-laya)) and by the
RAG demo project [spring-ai-with-hybrid-search-and-system-one-typesafe-jev](https://github.com/letrthang/spring-ai-with-hybrid-search-and-system-one-typesafe-jev). It never actuates:
callers keep their deterministic safety checks.
