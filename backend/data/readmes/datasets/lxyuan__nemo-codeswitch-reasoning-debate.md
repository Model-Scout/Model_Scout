---
license: apache-2.0
task_categories:
- text-generation
language:
- en
- zh
- ms
- ko
- ja
- vi
- es
- fr
- id
pretty_name: "NeMo: Multilingual Code-Switching Reasoning + Debate"
size_categories:
- 100K<n<1M
tags:
- synthetic
- multilingual
- codeswitching
- reasoning
- debate
---

#### Overview

This is a synthetic, multilingual **code-switching** dataset. Each record contains:

- a realistic user **query**
- a long-form **reasoning** section
- a **debate** / counterargument section
- a concise **final_answer**

It is designed for experiments in multilingual generation, code-switch robustness, and reasoning/debate style responses.

This snapshot contains **574,977** rows and 10 string columns.

#### Data provenance

Important:
- Verify that your intended usage and redistribution complies with the LLM provider’s terms.
- This dataset is synthetic and may contain incorrect reasoning, hallucinations, or unsafe content.

#### Dataset structure

All fields are strings. Columns:

| Column | Description |
|---|---|
| `query` | User prompt/question (often multi-sentence with constraints) |
| `reasoning` | Long-form explanation leading toward the answer (may include multi-step reasoning) |
| `debate` | Critique/counterargument with alternative viewpoint |
| `final_answer` | Concise final answer |
| `language_mix` | Human-readable language mix label (e.g. English + 中文(简体)) |
| `mix_level` | Code-switch intensity: `light` / `medium` / `heavy` |
| `domain` | Broad domain label |
| `topic` | Topic label |
| `task_kind` | Task type label |
| `difficulty` | Difficulty label: `easy` / `medium` / `hard` |

Note: `domain`, `topic`, `task_kind`, and `difficulty` are lightweight metadata labels and may be imperfect/noisy—treat them as weak tags, not ground truth.

#### Splits and files

This dataset contains a single `train` split in `data/train.parquet` (~1.32GB). For a quick preview without downloading the full file, use `streaming=True`.

#### Stats

`mix_level`:
- heavy: 344,974
- medium: 172,918
- light: 57,085

`difficulty`:
- hard: 286,827
- medium: 216,085
- easy: 72,065

Top `language_mix`:
- Singlish/Manglish (English + 中文(简体) + Bahasa Melayu): 205,699
- English + 中文(简体): 82,177
- English + Bahasa Melayu (Manglish): 81,906
- English + 中文(繁體): 41,030
- English + 日本語: 20,594
- English + Tiếng Việt: 20,578
- English + Español: 20,568
- English + Français: 20,565
- English + 한국어: 20,524
- English + Bahasa Indonesia: 20,511

#### Example (full record)

```json
{
  "query": "Eh bro, I'm working on this multi-threaded Python program, using threading module, but got one weird bug leh. Every time I run my code, sometimes the shared variable 'counter' end up with the wrong value. I already use threading.Lock() around the increment, but the issue only shows up when I set num_threads = 7 and total_increments = 1050, and only if run on my Windows laptop (not on Mac). I want to create a minimal repro to post on GitHub, but need to make sure the bug shows up every time, not just sometimes. How should I write this minimal reproducible example to consistently trigger the problem, given the constraints above? 记得要考虑线程调度 punya randomness, and also suggest what to include or exclude from the sample code supaya the bug always appears, jangan kadang-kadang only.",
  "reasoning": "First, we must understand the race condition that can happen in multi-threaded programs, especially when threads modify shared state like 'counter'. Even though you're using threading.Lock(), there could be mistakes in how the lock is acquired or released, or maybe part of the increment code is outside the lock. 另外，在Windows上和Mac上线程调度确实不同，所以有时候race condition only surface on one platform.\\n\\nTo make the bug reliably reproducible, a few strategies can help. One is to minimise unrelated code—keep only what is necessary: shared variable, thread creation, the critical section with the lock, and joining threads. Another is to increase the likelihood of the race condition by forcing many rapid context switches. For example, can insert time.sleep(0) or time.sleep(0.001) strategically inside or outside the locked section to expose thread interleaving issues.\\n\\n你要仔细检查lock是否真的包住了所有的counter变化。如果lock acquire/release有遗漏，then high concurrency will more likely show the bug. To make the sample minimal, exclude all other logic not related to the shared variable manipulation. Furthermore, run the test in a loop, maybe 50 times, and assert the final result, so if any run fails, the bug is confirmed.\\n\\nSince randomness in thread scheduling (jadual benang) can cause non-deterministic bugs, you can encourage the race condition to happen more frequently by increasing the number of threads, total increments, or adding small delays. Remember to print diagnostic info when a failure is detected, to confirm it's not a false positive caused by something else.",
  "debate": "But actually, just adding sleep(0) or sleep(0.001) inside the thread might not always guarantee the race condition will occur every time, especially if Windows thread scheduler decides to give one thread more time before switching. Kadang-kadang, even with all those measures, the bug still refuses to appear consistently, very stubborn lah!\\n\\nMoreover, what if the real problem is not the lock usage, but something specific to the Windows Python interpreter's GIL (Global Interpreter Lock) behavior, or maybe the counter variable is not shared due to some scoping issue? Kalau macam tu, adding more threads or increasing increments won't solve it, because the core issue is elsewhere. Sometimes, introducing artificial delays (like sleep) can even mask the race condition, making the program look more correct than it is.\\n\\nAn alternative approach is to use Python's built-in ThreadPoolExecutor or even multiprocessing, just to check if the bug only appears in certain threading models. Also, for a minimal repro, we should consider stripping the code right down to just the buggy behavior, but maybe provide some platform-specific info (like OS version, Python version) in comments, so others can try to reproduce on their own machines. To really get deterministic failure, maybe must use monkeypatching or even ctypes to force bad scheduling, but that's very advanced already. So, maybe the best we can do is to make the bug more likely, but cannot guarantee 100% it will show up every run.",
  "final_answer": "Write a minimal code that isolates the counter increment logic with the lock, runs many threads and increments, and adds a short sleep to increase context switches; loop the test multiple times to catch inconsistent results, but note that due to thread scheduling, absolute reproducibility may not be possible.",
  "language_mix": "Singlish/Manglish (English + 中文(简体) + Bahasa Melayu)",
  "mix_level": "medium",
  "domain": "Software & debugging",
  "topic": "writing a minimal repro scenario",
  "task_kind": "math word problem (self-contained)",
  "difficulty": "hard"
}
```

#### How to use

```python
from datasets import load_dataset

ds = load_dataset("lxyuan/nemo-codeswitch-reasoning-debate", split="train", streaming=True)

for i, ex in enumerate(ds):
    if i >= 10:
        break
    print(f"--- example {i} ---")
    print("query:", ex["query"][:200])
    print("final_answer:", ex["final_answer"][:200])
```

#### Intended use

- Research on multilingual code-switch generation and style control.
- Prompting/finetuning experiments for multi-part responses (reasoning + debate + answer).

#### Limitations

- Synthetic generations may be wrong or misleading.
- The “reasoning” field may contain sensitive-style step-by-step reasoning; evaluate whether it fits your use-case.
- Code-switch patterns are model-generated and may not reflect natural human switching.

#### Citation (draft)

```bibtex
@dataset{nemo_codeswitch_reasoning_debate_2026,
  author       = {Yuan, Lik Xun},
  title        = {NeMo: Multilingual Code-Switching Reasoning + Debate},
  year         = {2026},
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/lxyuan/nemo-codeswitch-reasoning-debate},
}
```
