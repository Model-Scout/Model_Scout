---
license: apache-2.0
language:
  - en
  - es
  - fr
  - de
  - it
  - pt
  - nl
  - pl
  - ru
  - uk
  - tr
  - ar
  - he
  - hi
  - id
  - vi
  - th
  - zh
  - ja
  - ko
  - sv
  - da
  - no
  - fi
  - cs
  - ro
  - hu
  - el
  - ca
  - fil
  - ms
  - bn
  - ta
  - fa
  - ur
  - sw
  - hr
  - sr
  - sk
  - bg
  - lt
  - lv
  - et
  - sl
  - is
  - ka
  - hy
  - az
  - kk
  - uz
  - mn
  - km
  - my
  - si
  - ne
  - gu
  - mr
  - te
  - kn
  - ml
  - pa
  - cy
  - ga
  - eu
  - gl
  - eo
  - af
  - ht
  - mi
  - sm
  - zu
  - xh
  - jv
  - su
  - ceb
  - yo
  - ig
  - ha
  - am
  - ku
  - ps
  - tg
  - ky
  - lo
  - dv
tags:
  - function-calling
  - tool-calling
  - functiongemma
  - prepaid-cards
  - finetuning
task_categories:
  - text-generation
---

# FunctionGemma Prepaid-Cards Tool-Calling Dataset

Synthetic training data for fine-tuning `google/functiongemma-270m-it` so it can
recognize chat intents for buying prepaid cards, checking balances, and viewing
transaction history, and emit the correct tool call.

## Tools

| Tool | Purpose |
|---|---|
| `purchase_card(amount, card_type, email?, currency?)` | Buy a **Digital Prepaid Visa** or **Virtual Prepaid Mastercard** |
| `get_card_balance(card_number)` | Check the balance of a card |
| `get_transaction_history(card_number, limit?)` | List a card's transactions |

`card_type` values: `digital_prepaid_visa` | `virtual_prepaid_mastercard`.

## Format

Each row follows the exact structure TRL's `SFTTrainer` expects for FunctionGemma:

- `messages` — conversation in the OpenAI-style format (`developer` / `user` /
  `assistant` with `tool_calls` / `tool` responses)
- `tools` — JSON schemas generated with `transformers.utils.get_json_schema`
- `lang` — ISO 639-1 code of the user messages
- `kind` — sample category (see below)
- `template_id` — deterministic id used for the train/test split
- `split` — `train` or `test` (deterministic)

## Sample kinds

- `purchase` — single-turn card purchase requests
- `balance` — single-turn balance requests (full, masked `****1234`, `1234...9876`, `ending in 1234` card numbers)
- `tx` — single-turn transaction-history requests
- `chain_split` — **multi-turn**: card number given in message 1, request in message 2
- `chain_clarify` — **multi-turn**: request without card number → assistant asks → user provides → tool call
- `chain_purchase_clarify` — multi-turn purchase: amount/type collected across turns
- `chain_retry` — tool called with missing arg → error response → clarification → retry
- `chain_full` / `chain_full_balance` / `chain_full_tx` — full function-calling loop: call → response → assistant text
- `chain_two` / `chain_purchase_balance` — long multi-tool conversations
- `greet` / `negative` — small talk that must **not** trigger a tool call

## Languages

User messages are hand-translated in 84 languages (list in the `language` tag
above). English has the largest template set (60+ purchase phrasings, 45
balance, 45 transaction).

## Train/test split

- 5 languages are fully held out of training: `ja`, `ko`, `ar`, `sw`, `ur`
- ~12% of English templates are held out
- Split is deterministic per `template_id`

## Build

```bash
python3 build_dataset.py --push
```

## Training

See the companion training script in this repository
(`train.py`) which follows the official
[FunctionGemma fine-tuning guide](https://ai.google.dev/gemma/docs/functiongemma/finetuning-with-functiongemma).
