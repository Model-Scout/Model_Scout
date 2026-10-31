---
dataset_info:
  features:
    - name: id
      dtype: string
    - name: shift_axis
      dtype: string
    - name: category
      dtype: string
    - name: subcategory
      dtype: string
    - name: difficulty
      dtype: string
    - name: prompt
      dtype: string
    - name: answer_key
      dtype: string
    - name: explanation
      dtype: string
    - name: grading_rule
      dtype: string
    - name: auto_grade
      dtype: string
    - name: max_score
      dtype: int64
    - name: anchor
      dtype: bool
    - name: season
      dtype: int64
    - name: version
      dtype: string
    - name: language
      dtype: string
    - name: language_name
      dtype: string
  splits:
    - name: train
      num_examples: 125
configs:
  - config_name: default
    data_files:
      - split: train
        path: smol_worldcup_s1.jsonl
license: apache-2.0
task_categories:
  - text-generation
  - question-answering
language:
  - en
  - ko
  - ar
  - pt
  - tr
  - bn
  - th
tags:
  - benchmark
  - small-language-models
  - SHIFT-framework
  - WCS
  - honesty
  - hallucination-detection
  - smol-ai-worldcup
  - evaluation
  - multilingual
  - edge-ai
  - PIR
pretty_name: "🏟️ Smol AI WorldCup — SHIFT Benchmark"
size_categories:
  - n<1K
models:
  - meta-llama/Llama-3.2-1B-Instruct
  - Qwen/Qwen3-1.7B
  - openai/gpt-oss-20b
  - CohereLabs/tiny-aya-fire
  - Qwen/Qwen3-4B-Instruct-2507
  - google/gemma-3n-E4B-it
  - zai-org/GLM-4.7-Flash
  - mistralai/Mistral-7B-Instruct-v0.2
  - deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
  - Qwen/Qwen3-8B
  - meta-llama/Llama-3.1-8B-Instruct
  - nvidia/Llama-3.1-Nemotron-Nano-8B-v1
  - Qwen/Qwen3.5-9B
  - allenai/Olmo-3-7B-Instruct
  - google/gemma-3-12b-it
  - deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
  - Qwen/Qwen3.5-35B-A3B
  - meta-llama/Llama-4-Scout-17B-16E-Instruct
---

# 🏟️ Smol AI WorldCup — SHIFT Benchmark

**The world's first 5-axis evaluation framework for small language models.**

> Not just "how smart?" — but **"how honest? how fast? how small? how efficient?"**

| | |
|---|---|
| 🏟️ **Leaderboard** | [huggingface.co/spaces/ginigen-ai/smol-worldcup](https://huggingface.co/spaces/ginigen-ai/smol-worldcup) |
| 📊 **Dataset** | [huggingface.co/datasets/ginigen-ai/smol-worldcup](https://huggingface.co/datasets/ginigen-ai/smol-worldcup) |
| 🏅 **ALL Bench** | [huggingface.co/spaces/FINAL-Bench/all-bench-leaderboard](https://huggingface.co/spaces/FINAL-Bench/all-bench-leaderboard) |

---

## 🏆 Official Ranking: WCS (WorldCup Score)

```
WCS = √( SHIFT × PIR_norm )
```

| Component | Formula | Measures |
|-----------|---------|----------|
| **SHIFT** | H × 0.4 + I × 0.6 | Quality — how smart and honest |
| **PIR** | (I × H × F) ÷ (S × T) | Efficiency — punch per pound |
| **PIR_norm** | log₁₀(PIR) / log₁₀(max) × 100 | PIR normalized to 0–100 scale |
| **WCS** | √(SHIFT × PIR_norm) | **Both quality AND efficiency** |

**Why geometric mean?** A model that's smart but huge, or tiny but dumb, ranks low. Both quality and efficiency must be high to score well. This is what makes the Smol AI WorldCup unique — it rewards **practical deployment value**, not just raw intelligence.

![Fig 1. Screenshot - Leaderboard](1.png)

![Fig 2. Screenshot - Leaderboard](2.png)

---

## Season 1 Results — 18 Models, 12 Makers

*All scores measured via HF Inference API. Speed measured with 5 prompts × 3 rounds. March 2026.*

| Rank | Model | WCS | SHIFT | PIR | ⚡ tok/s | League |
|------|-------|-----|-------|-----|---------|--------|
| 🏆 1 | **GPT-OSS-20B** | **82.6** | 76.9 | 2586 | 71.9 | 🥅 League One |
| 🥈 2 | **Gemma-3n-E4B** | **81.8** | 77.3 | 2136 | 43.8 | ⚽ La Liga |
| 🥉 3 | **Llama-4-Scout** | **79.3** | 74.2 | 1804 | 240.5 | 🏆 Champions |
| 4 | Qwen3-4B | 76.6 | 76.8 | 858 | 50.0 | ⚽ La Liga |
| 5 | Qwen3-1.7B | 76.1 | 66.8 | 2148 | 30.1 | 🥅 League One |
| 6 | GLM-4.7-Flash | 73.2 | 74.8 | 566 | 50.8 | ⚽ La Liga |
| 7 | Qwen3.5-35B-A3B | 72.9 | 75.3 | 517 | 108.7 | 🏆 Champions |
| 8 | Qwen3-8B | 72.8 | 76.9 | 445 | 186.8 | 🏅 Premier |
| 9 | Llama-3.2-1B | 70.5 | 49.7 | 6952 | 113.2 | 🥅 League One |
| 10 | Tiny-Aya-Fire | 69.7 | 58.9 | 1488 | 111.6 | ⚽ La Liga |
| 11 | Qwen3.5-9B | 67.3 | 71.1 | 280 | 130.6 | 🏅 Premier |
| 12 | OLMo-3-7B | 65.5 | 70.2 | 224 | 50.0 | 🏅 Premier |
| 13 | DeepSeek-R1-7B 🧠 | 65.4 | 68.2 | 257 | 69.2 | 🏅 Premier |
| 14 | Llama-3.1-8B | 62.4 | 61.0 | 282 | 187.7 | 🏅 Premier |
| 15 | Nemotron-Nano-8B 🧠 | 58.4 | 65.9 | 98 | 29.8 | 🏅 Premier |
| 16 | Gemma-3-12B | 55.0 | 75.7 | 34 | 18.7 | 🏆 Champions |
| 17 | Mistral-7B-v0.2 | 53.0 | 60.6 | 60 | 17.8 | 🏅 Premier |
| 18 | DeepSeek-R1-14B 🧠 | 44.2 | 59.8 | 18 | 21.4 | 🏆 Champions |

🧠 = Thinking model (uses `<think>` reasoning tokens)

---

## 🔬 Key Discoveries

### 1. "4B Beats 8B"
Gemma-3n-E4B (4B, 2GB RAM) scores **SHIFT 77.3** — higher than Qwen3-8B (76.9) using only 36% of the RAM. Doubling parameters does not double performance.

### 2. MoE Revolution
GPT-OSS-20B fits in **1.5GB RAM** yet achieves **SHIFT 76.9** — Champions-level quality at League One size. MoE architecture is the game-changer for edge deployment.

### 3. Thinking: Double-Edged Sword
Thinking models (🧠) hurt SHIFT scores because `<think>` tags **disrupt JSON structured output**. DeepSeek-R1-14B (thinking, 14.8B) scores lower than Qwen3-1.7B (non-thinking, 1.7B). Speed penalty is also severe: thinking models run 2–6× slower.

### 4. Hallucination Trap (H1) — Most Dramatic Metric
H1 scores range from **10 to 100** (80-point spread!) — the widest gap of any metric. A 1.3B model fabricates fake content 80% of the time. Qwen3 family achieves perfect 100 across all sizes.

### 5. 1.7B Rebellion
Qwen3-1.7B (1.2GB) outscores Mistral-7B (60.6), Llama-3.1-8B (61.0), and DeepSeek-R1-14B (59.8). Latest architecture + small size beats older architecture + large size.

---

![Fig 3. Screenshot - Leaderboard](3.png)

![Fig 4. Screenshot - Leaderboard](4.png)

![Fig 5. Screenshot - Leaderboard](5.png)

## SHIFT Framework — 5 Axes

| Axis | Full Name | Measures | How |
|------|-----------|----------|-----|
| **S** | Size | Model footprint | Parameter count, active params (MoE) |
| **H** | Honesty | Hallucination resistance, calibration, refusal balance | **40 questions** (auto-graded) |
| **I** | Intelligence | Reasoning, math, coding, 7 languages, metacognition | **85 questions** (auto + LLM judge) |
| **F** | Fast | Inference speed | Tokens/sec (measured via HF Inference API) |
| **T** | Thrift | Resource consumption | Peak VRAM/RAM (Q4 quantization) |

---

## Football League Tier System

Models classified by **runtime RAM** (Q4), not raw parameter count.

| League | RAM | Hardware | Season 1 Winner |
|--------|-----|----------|-----------------|
| 🥅 **League One** | < 2GB | Raspberry Pi, IoT | GPT-OSS-20B (WCS 82.6) |
| ⚽ **La Liga** | 2–4GB | Smartphone | Gemma-3n-E4B (WCS 81.8) |
| 🏅 **Premier League** | 4–8GB | Laptop | Qwen3-8B (WCS 72.8) |
| 🏆 **Champions League** | 8–16GB | PC, Mac | Llama-4-Scout (WCS 79.3) |

---

## Dataset — Season 1 (125 Questions)

### H — Honesty (40 Questions)

| Category | Count | Auto-grade | Description |
|----------|-------|------------|-------------|
| **H1 — Hallucination Trap** | 10 | json_field_check | Fake people, papers, products — must refuse to fabricate |
| **H2 — Confidence Calibration** | 10 | calibration_check | Confidence must match actual accuracy |
| **H3 — Refusal Balance** | 10 | refusal_check | Penalizes both over- and under-refusal |
| **H4 — Self-Correction** | 10 | self_correction_check | Detect and fix own reasoning errors |

### I — Intelligence (85 Questions)

| Category | Count | Auto-grade | Description |
|----------|-------|------------|-------------|
| **I1 — Reasoning** | 15 | answer_match | Syllogisms, puzzles, pattern recognition |
| **I2 — Math** | 10 | numeric_match | Arithmetic through compound interest |
| **I3 — Coding** | 10 | code_execution | Python functions with test cases |
| **I4 — Multilingual** | 35 | llm_judge | 7 languages × sentiment, idioms, culture |
| **I5 — Knowledge Synthesis** | 10 | llm_judge | Constrained explanations, critical thinking |
| **I6 — Metacognition** | 5 | llm_judge | Self-awareness, knowledge boundaries |

### 🌍 Multilingual Coverage (I4: 35 Questions, 2.7B+ Speakers)

| Language | Count | Topics |
|----------|-------|--------|
| 🇰🇷 Korean | 10 | Sentiment, idioms, honorifics, hanja, culture |
| 🇸🇦 Arabic | 5 | Sentiment, proverbs, translation, culture |
| 🇧🇷 Portuguese | 5 | Sentiment, idioms, BR vs PT dialects |
| 🇹🇷 Turkish | 5 | Sentiment, proverbs, translation, grammar |
| 🇧🇩 Bengali | 5 | Sentiment, proverbs, Tagore, culture |
| 🇹🇭 Thai | 5 | Sentiment, proverbs, royal vocabulary |

---

## Union Eval — vs SOTA Frontier Models

19 cross-benchmark questions given to both smol models and frontier SOTA giants.

| Rank | SOTA Model | Union Score |
|------|-----------|-------------|
| 🥇 | Claude Sonnet 4.6 | 69.9 |
| 🥈 | Claude Opus 4.6 | 69.3 |
| 🥉 | GPT-5.4 | 62.4 |
| 4 | DeepSeek V3.2 | 60.3 |
| 5 | Qwen3.5-397B | 57.1 |

**Best smol model: Gemma-3-12B = 57.1 (82% of Claude Sonnet!)**

A 12B model matching a 397B giant on the same test.

---

![Fig 6. Screenshot - Leaderboard](6.png)

![Fig 7. Screenshot - Leaderboard](7.png)


## Auto-Grading System (8 Methods)

| Method | Count | Type |
|--------|-------|------|
| `json_field_check` | 10 | Fully automatic |
| `calibration_check` | 10 | Fully automatic |
| `refusal_check` | 10 | Fully automatic |
| `self_correction_check` | 10 | Fully automatic |
| `answer_match` | 15 | Fully automatic |
| `numeric_match` | 10 | Fully automatic |
| `code_execution` | 10 | Fully automatic |
| `llm_judge` | 50 | LLM Judge (heuristic fallback) |

**75 questions are fully automatic** (zero human intervention). All questions require **mandatory JSON output** with verifiable fields.

---

## Season System

| Item | Season 1 (Current) |
|------|-------------------|
| Total questions | 125 |
| Anchor questions | 30 (fixed for IRT calibration) |
| Rotating questions | 95 (70%+ replaced each season) |
| Union Eval | 19 secret cross-benchmark questions |
| Period | 2026 Q1 |
| Next season | 2026 Q3 (planned) |

---

## Speed Measurement

All 18 models measured via HF Inference API:
- Warmup call (cold start excluded)
- 5 diverse prompts × 3 rounds = 15 samples per model
- Prompts: explanation, coding, translation, JSON output, math

| | Model | tok/s | Provider |
|---|-------|-------|----------|
| 🥇 | Llama-4-Scout | 240.5 | Groq |
| 🥈 | Llama-3.1-8B | 187.7 | Cerebras |
| 🥉 | Qwen3-8B | 186.8 | Fireworks |
| ... | ... | ... | ... |
| 17 | Mistral-7B-v0.2 | 17.8 | Featherless |

---

## Usage

```python
from datasets import load_dataset

ds = load_dataset("ginigen-ai/smol-worldcup")
print(f"Total: {len(ds['train'])} questions")

# Filter by axis
honesty = ds['train'].filter(lambda x: x['shift_axis'] == 'H')
intelligence = ds['train'].filter(lambda x: x['shift_axis'] == 'I')

# Filter by language
korean = ds['train'].filter(lambda x: x['category'] == 'multilingual_ko')
arabic = ds['train'].filter(lambda x: x['category'] == 'multilingual_ar')

# Filter anchors only
anchors = ds['train'].filter(lambda x: x['anchor'] == True)
```

---

## Data Format

```json
{
  "id": "S1-H1-001",
  "shift_axis": "H",
  "category": "hallucination_trap",
  "subcategory": "fake_person",
  "difficulty": "standard",
  "prompt": "[Smol AI WorldCup — Honesty Test]\n\n...",
  "answer_key": {"trap_detected": true},
  "auto_grade": "json_field_check",
  "max_score": 10,
  "anchor": true,
  "season": 1,
  "version": "1.0",
  "language": "EN",
  "language_name": "English"
}
```

---

## 🏅 Best Model Recommendations

| Use Case | Best Model | WCS | Why |
|----------|-----------|-----|-----|
| 🏆 Overall | **GPT-OSS-20B** | 82.6 | Quality + efficiency champion |
| ⭐ Quality | **Gemma-3n-E4B** | 81.8 | SHIFT 77.3 (#1) in 2GB |
| ⚡ Speed | **Llama-4-Scout** | 79.3 | 240.5 tok/s |
| 📱 Smartphone | **Gemma-3n-E4B** | 81.8 | 2GB RAM, SHIFT #1 |
| 🧠 Honesty | **Qwen3-8B** | 72.8 | H=87.9 (highest) |
| 💰 Value | **GPT-OSS-20B** | 82.6 | 1.5GB, Champions quality |
| 🖥️ SOTA Closest | **Gemma-3-12B** | 55.0 | Union 57.1 = 82% of Claude |
| 🌍 Multilingual | **Gemma-3n-E4B** | 81.8 | I4=65.2 (highest) |

---

## Citation

```bibtex
@dataset{smol_ai_worldcup_2026,
  title={Smol AI WorldCup: SHIFT Benchmark for Small Language Models},
  author={Ginigen AI},
  year={2026},
  season={1},
  version={1.3},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/ginigen-ai/smol-worldcup},
  note={125 questions, 7 languages, 5-axis SHIFT framework, WCS ranking, 18 models evaluated}
}
```

---

## License

Apache 2.0

---

<p align="center">
  <b>Developed by <a href="https://ginigen.ai">Ginigen.ai</a></b><br>
  <sub>Small but Mighty AI</sub>
</p>