---
license: apache-2.0
dataset_info:
  features:
  - name: prompt
    dtype: large_string
  - name: chosen
    dtype: large_string
  - name: rejected
    dtype: large_string
  - name: source_conversation_id
    dtype: large_string
  - name: metadata
    dtype: large_string
  splits:
  - name: train
    num_bytes: 7991095294
    num_examples: 3989
  - name: test
    num_bytes: 1480903405
    num_examples: 523
  - name: validation
    num_bytes: 1266129914
    num_examples: 515
  download_size: 9684248539
  dataset_size: 10738128613
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
  - split: validation
    path: data/validation-*
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
- hi
task_categories:
- summarization
- text-generation
tags:
- conversation-compaction
- context-compression
- synthetic
- preference-data
- multimodal
size_categories:
- 1K<n<10K
---

# long-context-multimodal-conversations-5k Synthetic Conversation & Compaction Dataset

## Dataset Description

**long-context-multimodal-conversations-5k** is a fully synthetic dataset for training models to **compact long multi-turn chat histories** into structured, LLM-facing summaries.

The dataset has **two primary artifacts**:

| Artifact | Description | Typical use |
|----------|-------------|-------------|
| **Conversations** (`conversations.jsonl`) | Raw synthetic chat logs | Long-context modeling, compaction input, multimodal chat research |
| **Compaction pairs** (`preference_pairs.jsonl` / training export) | Same conversations + compaction instruction + chosen/rejected summaries | DPO/IPO/SFT for compaction |

---

## Important: repeated conversations are intentional

**You will see many rows with the same (or nearly the same) conversation history. This is by design.**

Each source conversation is reused for **multiple compaction examples**. For each unique conversation, many compaction parameter combinations are used.

So rows that look like duplicates are usually **different supervision targets for the same long context**, not accidental duplication.

**Splitting:** train/validation/test splits are grouped by **`source_conversation_id`**, so all compaction variants from one chat stay in the same split and do not leak across splits.

**If you deduplicate on conversation text alone, you will collapse intentional training signal.** Deduplicate by `(source_conversation_id, params, rejection_strategy)` (or equivalent metadata) if you need unique rows.

---

## Using this data for non-compaction tasks

Compaction training rows append a final **user** message with the `compact\nmax_tokens: …` instruction block.

If you want to use this dataset for **anything other than compaction** 

- Use the **`conversation`** field only, **or**
- From the training export **`prompt`**, **drop the final user message** (the compaction instruction).

The raw **`conversations.jsonl`** artifact has no compaction message and can be used.

---

## Dataset Structure

Each row in the published training export (`jaguar_training_dataset.json`) is a preference pair with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| **`prompt`** | `list[message]` | OpenAI-style chat messages: the full synthetic conversation (alternating `user` / `assistant`, text and optional `image_url` blocks), **plus a final `user` turn** with the `compact\nmax_tokens: …` instruction. No system message. Language and topic may shift mid-conversation by design (natural topic changes or abrupt switches). **Many rows share the same message prefix** — only the final compaction instruction (and outputs) differ. |
| **`chosen`** | `string` | **Good** compaction: structured summary from a strong teacher, matching the requested `style`, `preserve`, `focus`, `recency`, and `language` in `metadata.params`. |
| **`rejected`** | `string` | **Bad** compaction: output from a weaker teacher, deliberately flawed according to `metadata.rejection_strategy` (e.g. wrong style, lost code, wrong language). |
| **`metadata`** | `object` | Provenance and compaction settings for this row (see below). |

### `metadata` fields

| Key | Description |
|-----|-------------|
| **`params`** | Compaction settings: `style`, `max_tokens`, `preserve`, `focus`, `recency`, `language`. |
| **`rejection_strategy`** | Which deliberate flaw was applied to `rejected` (e.g. `lost_code`, `wrong_language`). |
| **`conversation_context`** | Context from generation; includes **`source_conversation_id`** — the UUID of the underlying chat. Rows with the same ID share conversation history but differ in `params`, `chosen`, and `rejected`. |

---

## How the data is generated

### Stage A — Synthetic conversations

Two chat models are **randomly assigned** to human-simulator vs assistant roles per conversation (50/50). Temperature is role-based (human ~0.85, assistant ~0.7).

**Default models** (configurable in `vllm_config.yaml`):

| Role | Default model |
|------|---------------|
| **model_a** | `Mistral-Medium-3.5-128B-AWQ-INT4` | 
| **model_b** | `Qwen3.5-27B` | 
| **Image generation** | `black-forest-labs/FLUX.2-klein-4B` |

The **human side** is an LLM simulator (not real users): openings, follow-ups, optional image turns, natural topic changes, and abrupt topic switches.

| Property | Default |
|----------|---------|
| **Length** | 50k–70k token budget (~12k–75k estimated tokens typical) |
| **Languages** | 11 (see below) |
| **Topics** | 80 labels |
| **Images** | ~⅓ of chats image-enabled; ~8% per eligible turn; up to 8 images/chat |
| **Topic dynamics** | ~⅓ abrupt mid-chat switches; otherwise natural topic conclusion → new topic |

Token budgets use the Mistral tokenizer family (`mistralai/Ministral-3-8B-Instruct-2512` by default).

### Stage B — Compaction preference pairs

For each source conversation, the pipeline draws **~4 unique `(params, rejection_strategy)` assignments** (`DEFAULT_SAMPLES_PER_CONVERSATION = 4`). Each assignment yields one preference row with the **same conversation** but **different compaction supervision**.

| Role | Model | Output |
|------|-------|--------|
| **Good teacher (`model_a`)** | Strong model (default: Mistral Medium 3.5 128B) | `chosen` |
| **Bad teacher (`model_b`)** | Weaker model (default: Qwen3.5-27B) | `rejected` (with deliberate flaw) |

**Compaction parameter grid:**

| Field | Values |
|-------|--------|
| **`style`** | `xml`, `json`, `yaml`, `markdown`, `plain` |
| **`max_tokens`** | `768`, `1024`, `2048`, `4096`, `8192` |
| **`preserve`** | `code`, `quotes`, `all`, `none` |
| **`focus`** | `coding`, `debugging`, `research`, `planning`, `creative`, `tutoring`, `general` |
| **`recency`** | `uniform`, `tail-verbatim` |
| **`language`** | `source`, `en`, `es`, `fr`, `de`, `ja`, `zh`, `ko`, `pt`, `it`, `nl`, `ru`, `ar`, `hi` |

**Rejection strategies (~uniform; ~10% `wrong_language`):**  
`exceeded_max_tokens`, `wrong_style`, `lost_code`, `lost_speaker_distinction`, `added_filler`, `dropped_recent_context`, `wrong_focus`, `hallucinated_content`, `over_compressed`, `wrong_language`.

**Compaction instruction (final user turn in training rows):**

```text
compact
max_tokens: 2048
style: json
preserve: code
focus: debugging
recency: tail-verbatim
language: source
```

**Chosen output:** structured summary (`goal`, `prior_goals`, `user_profile`, `steps_taken`, `key_quotes`, `code_artifacts`, `images`, `open_threads`, `constraints`, etc.) in the requested `style`. Intended for **LLM consumption only**.

---

## Languages

**Conversation languages (11):** English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, Arabic.

**Compaction output languages (14):** `source` plus `en`, `es`, `fr`, `de`, `ja`, `zh`, `ko`, `pt`, `it`, `nl`, `ru`, `ar`, `hi`.

---

## Topics (80)

Browser-assistant-style domains including weather, web browsing, news, science & technology, coding & programming, web development, data science & AI/ML, cybersecurity, sports, personal finance, health, travel, food, fashion, art & culture, music/movies/gaming, books, parenting, pets, home improvement, gardening, tutoring, careers, business, productivity, mental health, legal, real estate, taxes, politics, environment, cars/transit, puzzles, event planning, and more. Conversations may span **multiple topics** within one chat.


---

## Intended use

**In scope:** training/evaluating conversation compaction models; long-context and multimodal summarization research; preference optimization for structured summaries.

**Out of scope:** real human chat data; general-purpose assistant SFT without removing compaction instructions; human-facing summaries; safety-filtered or PII-scrubbed corpora.

---

## Limitations

- All content is **LLM-generated**; quality depends on configured teacher/chat models.
- **Synthetic distribution** — not representative of real user behavior.
- **Multimodal:** images are generated, not real user uploads.
- Models trained on this data expect the **exact compaction parameter block** and schema at inference time.
- Compactions can reproduce sensitive or harmful content present in the source conversation.

---

## License

Apache 2.0

---

## Related

- **Model:** [Jaguar-1](https://huggingface.co/bravesoftware/Jaguar-1) — LoRA on `Qwen/Qwen3-VL-4B-Instruct` for multimodal compaction.
