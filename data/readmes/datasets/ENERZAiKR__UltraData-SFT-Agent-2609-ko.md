---
language:
- ko
- en
license: apache-2.0
task_categories:
- text-generation
tags:
- agent
- tool-use
- function-calling
- sft
- korean
- localization
size_categories:
- 10K<n<100K
configs:
- config_name: Tool-Use
  data_files:
  - split: train
    path: "data/Tool_Use/*.jsonl"
- config_name: Search-Agent
  data_files:
  - split: train
    path: "data/Search_Agent/*.jsonl"
---

# UltraData-SFT-Agent-2609 — Korean localization

Korean localization of [openbmb/UltraData-SFT-Agent-2609](https://huggingface.co/datasets/openbmb/UltraData-SFT-Agent-2609)
(Apache-2.0). Only the **natural-language surface** was translated: user messages, assistant replies, assistant reasoning
(`reasoning_content`) and the tool-call argument strings the user actually said. Everything that is an API contract or
environment data stays exactly as in the source: system prompts/policies, tool schemas (`tools`), function and parameter
names, enum values, identifiers, and tool observations (`role: tool`).

Schema is identical to the source (`uuid`, `messages`, `tools`, `source`, `domain`); rows can be joined to the English
original by `uuid`. Rows are omitted (not partially translated) when any quality gate failed.

## Coverage

| subset | source rows | released rows | kept | dropped: CJK chars | dropped: unrepairable | emoji-stripped rows |
|---|---|---|---|---|---|---|
| Tool_Use | 82,760 | 71,474 | 86.4% | 4,986 | 221 | 21,294 |
| Search_Agent | 15,000 | 12,717 | 84.8% | 3 | 0 | 175 |

Dropped rows by gate:
- **Tool_Use**: parse_fail 2,896, round_count_mismatch 2,429, arg_not_in_user_text 919, number_lost 480, no_hangul 442, banned_word 278, chunk:round_count_mismatch 260, cjk 192, chunk:banned_word 95, chunk:parse_fail 70, chunk:cjk 42, arg_missing_in_map 23, chunk:too_long 11, source_zh 10, chunk:api:TimeoutError 4, tool_response_lost 1
- **Search_Agent**: cjk 845, chunk:cjk 545, source_zh 381, number_lost 192, chunk:parse_fail 117, chunk:banned_word 65, parse_fail 51, round_count_mismatch 28, chunk:round_count_mismatch 22, arg_not_in_user_text 16, banned_word 10, no_hangul 7

Tool-argument language (strings the user said): - **Tool_Use**: English kept 287 (75%) · Korean 94
- **Search_Agent**: English kept 85 (18%) · Korean 390

## How it was made
- Translator: Qwen3.8-27B (FP8) via vLLM, temperature 0, one request per user turn (assistant rounds chunked for long
  trajectories), with an explicit list of the argument strings that must appear verbatim in the Korean user message.
- Gates (row dropped on failure): every user-said argument appears in the Korean user message (or is kept in English),
  Hangul present, numbers (3+ digits) preserved, assistant round count preserved per chunk, no scaffolding words.
- Environment output embedded in user turns (`<tool_response>…</tool_response>` blocks) is masked before translation and
  restored byte-for-byte; rows where the translator dropped such a block were re-translated or removed.
- Tool-argument values that are lookup keys (the English value is echoed in a tool observation of the same row, or is a
  date string) are kept in English in the call even when the Korean user message says them in Korean
  (e.g. user says "뉴욕", the call still sends "New York").
- Post-processing (rule-based): rows containing any Chinese/Japanese characters are removed (translator leakage);
  emoji carried over from the English replies are stripped from user/assistant text (rows with emoji inside tool
  arguments are removed); argument spellings made consistent within a row (first occurrence wins).
- Known limitations: honorific/plain speech levels may be mixed within a row (not filtered — the meaning is unaffected);
  some translationese remains; Chinese-origin rows (`Search_Agent-zh`) are excluded.

Pipeline: `LLM_Hard_STE/data_gen/ko/translate_ultradata.py` (ENERZAi).
