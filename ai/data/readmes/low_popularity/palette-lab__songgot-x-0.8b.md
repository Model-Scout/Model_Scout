---
license: apache-2.0
base_model: Qwen/Qwen3.5-0.8B
language:
- ko
- en
pipeline_tag: text-generation
tags:
- tool-calling
- function-calling
- korean
- on-device
- gguf
datasets:
- palette-lab/songgot-tools-ko
- AmazonScience/MASSIVE
---

# Songgot-X 0.8B

**Line B of the Songgot project: built on an open base, not from scratch.** Songgot-X is Qwen/Qwen3.5-0.8B (Apache 2.0)
post-trained by Palette with the base model's own chat template and tool-call format. The published weights are a uniform
average of (a) the average of three post-trained checkpoints (v10: the 263,242-row set; v11: the same recipe with 3,774
extra targeted rows; v12: the same again with 3,309 rows that teach following the parameter description) and (b) a short
continued fine-tune of that average on 2,813 v13 rows (verbatim time expressions, old/new roles, query-versus-create intent)
plus a replay sample, one epoch at a halved learning rate. The from-scratch Songgot models live at palette-lab/songgot-12l, songgot-m and songgot-l;
this repository exists so that a customer who needs the best call accuracy today can have it, with the lineage stated.

## Result (weights of 2026-09-16 evening; every model scored with the same lenient parser)

FunctionChat-Bench SingleCall (Kakao, 500 Korean items, 5 tool conditions), exact match on function name and arguments
under the public scorer in github.com/hanishkeloth/songgot (`eval/functionchat_exact.py`), not the benchmark's GPT-4 judge.
The parser accepts a bare `<function=...>` block for every model alike.

| model | params | exact | 4_random | 4_close | 8_random | 8_close | all | name only |
|---|---|---|---|---|---|---|---|---|
| **Songgot-X 0.8B (this model: three-way average + v13 continuation, averaged)** | 0.8B | 87.0 | 84.0 | 80.0 | 83.0 | 77.0 | **82.2** | 96.4 |
| v10+v11+v12 average (the weights of 2026-09-16 morning) | 0.8B | 80.0 | 81.0 | 77.0 | 77.0 | 76.0 | 78.2 | 97.0 |
| Kanana-2-1.3B-Instruct (Kakao) | 1.3B | 77.0 | 76.0 | 71.0 | 73.0 | 69.0 | 73.2 | 97.2 |
| Qwen3.5-0.8B + v12 rows (member, not released) | 0.8B | 83.0 | 81.0 | 73.0 | 75.0 | 64.0 | 75.2 | 93.2 |
| v10+v11 average (the weights of 2026-09-15 evening) | 0.8B | 79.0 | 75.0 | 73.0 | 74.0 | 69.0 | 74.0 | 96.0 |
| Qwen3.5-0.8B + v11 rows (member, not released) | 0.8B | 75.0 | 73.0 | 66.0 | 70.0 | 62.0 | 69.2 | 94.4 |
| Qwen3.5-0.8B + v10 rows (member; the weights of 2026-09-15 morning) | 0.8B | 74.0 | 68.0 | 65.0 | 66.0 | 64.0 | 67.4 | 93.6 |
| EXAONE-4.0-1.2B (LG) | 1.28B | 73.0 | 65.0 | 53.0 | 66.0 | 58.0 | 63.0 | 85.2 |
| Songgot-X 0.8B v8 (previous weights, 2026-09-13) | 0.8B | 67.0 | 66.0 | 60.0 | 62.0 | 54.0 | 61.8 | 94.8 |
| Qwen3.5-2B + the v8 rows (not released) | 2B | 66.0 | 65.0 | 61.0 | 60.0 | 54.0 | 61.2 | 93.8 |
| Qwen3.5-0.8B (the base, zero-shot) | 0.8B | 51.0 | 48.0 | 41.0 | 52.0 | 34.0 | 45.2 | 73.8 |
| Songgot 12L (from scratch) | 50M | 44.0 | 39.0 | 30.0 | 35.0 | 17.0 | 33.0 | 73.6 |

Songgot-X is 9.0 points above Kanana-2 on call (about 4.7 standard errors on 500 items; the paper treats differences under
4 points as ties) and within one standard error on name (96.4 against 97.2). Qualifiers that travel with that sentence: one benchmark, our
exact-match scorer rather than the official GPT-4 judge, and the date. Kakao authored FunctionChat-Bench, so Kanana's figure may reflect
in-distribution training. Kanana-2 is released under the Kanana Open License, which does not allow on-device
redistribution, and EXAONE-4.0 is research-only; Songgot-X is the highest-scoring model in this table and the highest openly licensed (Apache 2.0) one by a wider
margin.

Why an average, twice. The three post-trained members share the base and recipe and differ in the sample and the targeted
rows, so their weights sit in one basin and average well (78.2 against 67.4, 69.2 and 75.2 for the members). A one-hour
continued fine-tune of that average on the v13 rows fixed the alarm-time class outright (AddAlarm 5 to 20 of 20) but, like
every targeted round before it, lost close-sibling tool choices; averaging the continuation back with the soup keeps the
argument gains and most of the tool choice. The published weights get 411 of 500 items right against 366 for Kanana-2 (74
items Kanana misses, 29 the other way, 337 both), with 18 wrong-tool choices and 71 argument misses. Different strengths:
Songgot-X wins AddAlarm (20 of 20 against 15), generate_random_password (16 against 0), start_playlist (20 against 0),
convert_currency (12 against 3); Kanana-2 wins informDday (18 against 12), update_contact (13 against 10), addMemo (20
against 17).

### Held-out human test (MASSIVE ko-KR, 500 utterances, 4 tools each)

| model | call | name only |
|---|---|---|
| Songgot-X 0.8B (this model) | 72.0 | 94.0 |
| v10+v11+v12 average | 70.4 | 94.0 |
| v10+v11 average | 71.6 | 92.6 |
| Qwen3.5-0.8B + v10 rows (member) | 62.4 | 81.4 |
| Kanana-2-1.3B-Instruct | 14.4 | 83.4 |
| Qwen3.5-0.8B (base, zero-shot) | 12.4 | 63.0 |

Human voice-assistant requests from the MASSIVE 1.1 ko-KR test split (never trained on), each with its gold massive-agents
function plus 3 random ones. The name column is the fair comparison: the published weights choose the right function on
94.0 percent of these unseen human requests, against 83.4 for Kanana-2 and 81.4 for the v10 member (this row was decoded
with the batched left-padded path, which agrees with the single-prompt path up to bf16 batching noise). The call column
is not a fair comparison: Songgot-X trained on MASSIVE's train split and knows its convention (copy the spoken span),
Kanana-2 did not and fills placeholders. It mirrors FunctionChat, where Kakao's authorship favours Kanana. Scorer and
subset are in the repo.

## Run it offline

GGUF files in this repository: `songgot-x-q4_k_m.gguf` (505 MB) and `songgot-x-q8_0.gguf` (774 MB), for llama.cpp,
Ollama, LM Studio and the browser. Songgot Pocket (hanishkeloth.github.io/songgot/app) runs this model inside the
browser on desktop and Android with no server; pick "Songgot-X 0.8B" in the model selector. Palette Desktop,
Palette's native offline app, runs it as a local llama-server sidecar. The prompt format is the Qwen3.5 tool
template exactly as rendered by the tokenizer's chat template with `tools=[...]` and thinking off.

Measured in Pocket on 2026-09-15 with the v10 member (same architecture and quantisation) (Chrome, Apple M5 Max, single thread, Q4_K_M): 2.0 to 2.2 s per
request from prompt to parsed call, 742 to 764 prompt tokens, 28 to 41 generated, 13 to 21 tokens per second
(the 2026-09-14 figure with the v8 weights was 3.5 s at 12.2 tokens per second on the same machine). The GGUF header is written without the converter's phantom 25th multi-token-prediction block (the defect
that made the 2026-09-13 files unloadable). In browser runtimes keep the batch size small (64): the 248,320-entry
vocabulary makes the logits buffer vocab x batch x 4 bytes.

Scored as shipped (2026-09-16): the Q4_K_M GGUF through llama.cpp, same 500 items, prompts and parser as the table above,
gives 80.2 call / 94.4 name with an f16 KV cache, 81.0 / 94.4 with a q8_0 KV cache and 80.8 / 94.2 with q4_0 (bf16
weights: 82.2 / 96.4; standard error about 1.9). The weight quantization costs about two points; the KV cache type costs
nothing measurable at these prompt lengths, so a q8_0 cache is a free halving of context memory. Only 6 of the 24 layers
keep a per-token cache (2 KV heads x 256 dims: 12 KB per token at fp16, 6.4 KB at q8_0); the other 18 are Gated DeltaNet
layers with a fixed state. Scores: `eval/score_soup4_q4km_kv_*.json` in the repo.

## Training data (v10, v11, v12 members and the v13 continuation)

- 175,000 rows sampled from the Songgot v8 set (palette-lab/songgot-tools-ko): Korean tool-calling pairs written by
  Palette's own open teacher (Palette-K-Midm) from invented tool schemas and verified by a second pass; no closed model
  produced any label.
- 31,307 targeted synthetic rows (weight 2) written by the same teacher and checked by deterministic rules, aimed at the
  four failure classes of the v8 model: copying names verbatim, from/to and sender/receiver roles, Korean number words,
  two-digit years.
- 10,861 human Korean voice-assistant requests from Amazon MASSIVE 1.1 ko-KR train split (CC BY 4.0), mapped onto the
  massive-agents function declarations (weight 2). The MASSIVE dev and test splits were not used.
- KoSGD dialogue-state rows.
- v13 continuation: 1,622 verbatim time-expression rows (value an exact substring of the request, suffix kept), 937 old/new
  role rows and 254 query-versus-create rows, each doubled with distractors, plus a 25,000-row replay sample of the v12 set.
- v12 member only: 3,309 teacher rows that teach following the parameter description (a stated format obeyed; a datetime
  copied verbatim when no format is stated; optional parameters omitted; a value narrowed to the named thing; a message
  written as the recipient reads it), plus the year rows re-labelled with a (YYYY-MM-DD) hint.
- v11 member only: 3,774 more teacher rows for two gaps (a text argument that must carry only the payload after an
  instruction such as "단어 수 세줘: ..."; explicit 1950-2015 years kept as written), MASSIVE at weight 1, negatives 2 percent.

Single-tool rows receive distractor tools (1, 4 or 8; name-related or random) so the training conditions mirror the
benchmark; 30 percent are restyled and 5 percent become negatives. Benchmark tool names and queries are excluded by an
assertion at assembly time. Details, the recipe and every negative result are in the Songgot paper
(hanishkeloth.github.io/songgot).

## Usage

Standard Qwen3.5 chat template with `tools=[...]`; thinking off. Tool calls come back as
`<tool_call><function=NAME><parameter=KEY>VALUE</parameter>...</function></tool_call>`; booleans and numbers are JSON-typed.
When no offered tool fits, the model answers in Korean that no tool matches; stop generation at `</tool_call>` or at the
end of the first line.

## Licence and lineage

Apache 2.0, inheriting Qwen3.5-0.8B's Apache 2.0. The base model was trained by Alibaba; Palette trained the
post-training stage only. MASSIVE is CC BY 4.0 (Amazon). Answers are generated by an AI model (AI 기본법 labelling).
