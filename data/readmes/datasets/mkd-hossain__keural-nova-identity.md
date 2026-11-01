---
license: apache-2.0
language: [ko, en]
task_categories: [text-generation]
tags: [keural, mkd, identity]
---
# Keural Nova — identity SFT data (PRIVATE)

**MKD-original.** 200 rows (ko+en) teaching the assistant it is **Keural, developed by MKD**,
including denials of Qwen / GPT / Gemini / Claude / Llama etc. Facts grounded in https://mkd.kr.
Format: `{"messages":[{"role":"user"...},{"role":"assistant"...}]}`. Mix with heavy replay when
training (identity-only over-fits). Released Apache-2.0.
