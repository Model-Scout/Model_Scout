---
base_model: Qwen/Qwen3.5-9B
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
language:
- en
- ko
tags:
- security
- vulnerability-repair
- code
- tool-use
- agent
- sft
- grpo
---

# qwen35-9b-secfix-grpo-lead-step300-merged

**Qwen/Qwen3.5-9B trained into a security-vulnerability-fixing tool-call agent: supervised fine-tuning
(SFT), then GRPO, with both stages merged into full weights.** Given one confirmed static-analysis (SAST)
finding, the agent reads the source file with `read_code`, patches it with `edit_code`, and submits the
fix with `submit_fix`.

This repo holds the complete model. No adapter or second repo is needed.

## Model details

| | |
|---|---|
| Base model | `Qwen/Qwen3.5-9B` (revision `c202236235762e1c871ad0ccb60c8ee5ba337b9a`) |
| Stage 1 | LoRA SFT (r=32, alpha=64, dropout 0.05) on the 7 language-model projections, merged into the base |
| Stage 2 | GRPO LoRA (r=32, alpha=64, dropout 0) trained on top of the stage-1 model, step 300 of 325, merged |
| Merge | W + (alpha/r)·B@A computed in fp32 and stored bf16, applied only to the 128 LoRA target weights per stage. All other weights are bit-identical to the base |
| Architecture | Unchanged from the base: `Qwen3_5ForConditionalGeneration`, same key names (`model.language_model.*`) and shard layout. Vision tower and MTP head are the untouched base weights |
| Tokenizer / chat template | Byte-identical copies of the base |
| `generation_config.json` | Only `eos_token_id: [248046, 248044]` and `pad_token_id`, so `generate()` stops at `<|im_end|>`. No sampling defaults |
| Programming languages | C, C++, Java, Python, JavaScript, Go, TypeScript |
| Developed by | sparrow-co-ltd (SecLLM team) |

## Training

### Stage 1: SFT

- **Data:** 2,205 agent trajectories (74 more held out for validation) from a teacher model
  (deepseek-v4-flash-0731) running in the same three-tool harness. Teacher runs were kept only if the
  final patch passed SAST re-verification and the run was clean (no failed edits, no rejected calls, one
  verifier attempt). One trajectory per finding. When runs disagreed, an LLM judge picked among
  SAST-passing patches.
- **Recipe:** 3 epochs, learning rate 1e-4 (5% warmup), effective batch 24, max length 12,288 tokens.
  Loss only on assistant turns. System, user and tool results are masked.

### Stage 2: GRPO

- **Algorithm:** GRPO with TRL. Each step samples 32 SAST findings with 8 full agent rollouts each. The
  loss is DAPO, the learning rate is 1e-5 (constant after warmup), and the KL penalty β=0.005 is measured
  against the stage-1 model. The completion cap is 10,240 tokens and each rollout has a 300-second limit.
- **Data:** a pool of 10,390 SAST findings in 7 languages. Findings that the base model already solved
  in all 8 rollouts were removed. Step 300 has seen about 9,600 of them.
- **Reward:**
  - *Hybrid reward.* A run that passes the harness verifier scores 1.0 if the LLM judge says the fix
    removes the finding, and 0.5 if it does not. Up to 0.2 is deducted for harness friction such as
    failed edits or extra verifier attempts. Runs that fail the harness keep the harness's own (lower or
    negative) score.
  - *Length shaping* (GRPO-LEAD, arXiv 2504.09696). Among judge-passing runs of the same finding,
    shorter runs get a small bonus and longer ones a small penalty, at most about ±0.14. A correct run
    always scores above an incorrect one.
  - *Difficulty weighting* (GRPO-LEAD). Advantages are re-weighted by the finding's pass rate within
    the group: successes on hard findings and failures on easy findings weigh more. The total update
    size per batch is kept unchanged.

## Agent protocol

The model is driven by an agent loop, not free-form chat. The user prompt holds one confirmed finding:
its metadata (language, issue name, risk, line, total lines) and the checker's description. The source
file itself is not in the prompt. The model reads it with the tools:

1. **`read_code(offset, limit)`** pages through the file. Lines come back prefixed with `<line>: `.
2. **`edit_code(old_string, new_string)`** makes an exact single-location replacement on a working copy.
3. **`submit_fix(desc)`** diffs the working copy, runs the deterministic verifier and returns PASS or
   FAIL. `desc` is one Korean sentence of at most 300 characters. Up to 3 attempts are allowed.

Each assistant turn carries exactly one tool call. The tool schema used in training:

```json
[
 {"type": "function", "function": {"name": "read_code",
  "description": "Read the current working copy. Each line is prefixed by its 1-based line number as `<line>: <content>`. The prefix is for reference and is not part of the file content. `offset` is the 0-based line to start from; `limit` is capped at 2000 lines (default 100). Each response is capped at 50KB and this tool instance has a cumulative 200KB output budget. If the output says lines remain, continue from the reported offset.",
  "parameters": {"type": "object", "properties": {"offset": {"type": "integer", "default": 0}, "limit": {"type": "integer", "default": 100}}}}},
 {"type": "function", "function": {"name": "edit_code",
  "description": "Replace old_string with new_string in the working copy of the source file. When editing text from read_code output, preserve the exact indentation (tabs or spaces) and omit the line-number prefix, such as `1: `. Never include the prefix in old_string or new_string. old_string must match EXACTLY ONE location: include neighboring lines to make it unique. Edits accumulate on the working copy; submit_fix diffs it against the original. Failed matches do not consume verification attempts.",
  "parameters": {"type": "object", "properties": {"old_string": {"type": "string"}, "new_string": {"type": "string"}}, "required": ["old_string", "new_string"]}}},
 {"type": "function", "function": {"name": "submit_fix",
  "description": "Diff the working copy against the original file, build the structured fix, and run the deterministic verifier in-process. `desc` must be ONE Korean sentence (<=300 chars) describing the fix. Returns PASS, or FAIL with structured errors plus the affected region of the modified file in NEW coordinates. Maximum 3 verification attempts per finding.",
  "parameters": {"type": "object", "properties": {"desc": {"type": "string"}}, "required": ["desc"]}}}
]
```

**Out of scope:** detecting vulnerabilities (the finding is assumed confirmed upstream), general coding
assistance and chat.

## How to serve

### vLLM

```bash
python -m vllm.entrypoints.openai.api_server \
  --model sparrow-co-ltd/qwen35-9b-secfix-grpo-lead-step300-merged \
  --language-model-only \
  --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 \
  --chat-template-content-format auto \
  --default-chat-template-kwargs '{"enable_thinking": false}'
```

Do **not** enable MTP speculative decoding (`--speculative-config` with method `mtp`). The MTP head in
this repo is the untrained base copy and does not match the fine-tuned model.

### Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "sparrow-co-ltd/qwen35-9b-secfix-grpo-lead-step300-merged"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, dtype=torch.bfloat16, device_map="auto")

prompt = tok.apply_chat_template(messages, tools=TOOLS, add_generation_prompt=True,
                                 tokenize=False, enable_thinking=False)   # REQUIRED
out = model.generate(**tok(prompt, return_tensors="pt").to(model.device), max_new_tokens=4096)
```

### `enable_thinking=False` is mandatory

Training rendered every assistant turn as `<think>\n\n</think>\n\n` followed by the tool call, which is
what the template produces with thinking disabled. Rendering with thinking enabled puts the model
off-distribution. Tool calls render as Qwen's `<function=...><parameter=...>` XML. When re-rendering
history, pass tool-call `arguments` as a dict, because a JSON string gets double-encoded.

## Limitations

- **Narrow task.** The model only knows the three-tool protocol above.
- **Patches need review.** Outputs are candidate fixes. Re-run the real SAST tool and the project's
  tests, and have a human review the diff, before merging.
- **Occasional runaway turns.** A single turn can occasionally run very long. Set a per-call token cap
  and a wall-clock limit, and treat hits as failures.
- Inherits base-model behaviour and licensing (Apache-2.0 for Qwen3.5-9B).
