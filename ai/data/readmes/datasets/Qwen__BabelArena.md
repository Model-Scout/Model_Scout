---
license: apache-2.0
language:
- en
- zh
- ja
- fr
- ru
- ar
- es
- ko
- id
- hi
- th
- he
- tr
- vi
- ms
- be
- pa
- kk
- km
- my
- lo
- ta
- te
multilinguality: multilingual
task_categories:
- text-generation
tags:
- agents
- tool-use
- agent-evaluation
- multilingual
- benchmark
pretty_name: BabelArena
size_categories:
- 10K<n<100K
---

# BabelArena: A Large-Scale Multilingual Benchmark for LLM Agents


<p align="left">
  <a href="https://arxiv.org/abs/2609.23490">
    <img src="https://img.shields.io/badge/arXiv-2609.23490-b31b1b.svg?logo=arxiv" alt="arXiv Badge"/>
  </a>
  <a href="https://github.com/QwenLM/BabelArena">
    <img src="https://img.shields.io/badge/GitHub-BabelArena-181717.svg?logo=github" alt="GitHub Badge"/>
  </a>
  <a href="https://modelscope.cn/datasets/Qwen/BabelArena">
    <img src="https://img.shields.io/badge/ModelScope-Dataset-624AFF.svg?logo=modelscope" alt="ModelScope Badge"/>
  </a>
  <a href="https://huggingface.co/datasets/Qwen/BabelArena">
    <img src="https://img.shields.io/badge/Hugging%20Face-Dataset-FFD21E.svg?logo=huggingface" alt="Hugging Face Badge"/>
  </a>
</p>


BabelArena is a multilingual agent benchmark covering **23 languages** and
**four agent benchmark families** across **13 domains** — 702 canonical tasks,
16,146 task instances. Every component an agent touches is localized: prompts,
tasks, tool descriptions and the environments themselves. Our benchmark ensures
component-complete adaptation, language diversity and verified translation
quality, making it a highly discriminative multilingual agent benchmark in the
era of tool-using LLMs.

This release is the **`standard` subset** — the frozen task sample that is
identical across all 23 languages and the one `bench run` evaluates by default —
for three of the four families: **τ³-Bench**, **VitaBench** and
**DeepPlanning** (**532 tasks per language, 12,236 instances**). ClawEval's task
data is distributed separately.

🧩 **Four Agent Settings:** BabelArena draws its tasks from four benchmark
families, each scored by its own evaluator, so a single number covers
interactive services with a simulated user, long-horizon planning under
verifiable constraints, knowledge-grounded tool use under a policy, and
heterogeneous autonomous tasks.

| Family | What it tests | Domains | Tasks | In this release |
|---|---|---|---:|:---:|
| [τ³-Bench](https://github.com/sierra-research/tau2-bench) | simulated-user interaction, tool calling, knowledge retrieval, policy compliance | airline, retail, telecom, banking | 212 | ✓ |
| [VitaBench](https://github.com/meituan-longcat/vitabench) | versatile interactive tasks with a simulated user | delivery, in-store, online travel, cross-domain | 200 | ✓ |
| [DeepPlanning](https://huggingface.co/datasets/Qwen/DeepPlanning) | long-horizon planning under verifiable constraints | travel, shopping | 120 | ✓ |
| [ClawEval](https://claw-eval.github.io) | service orchestration, multimodal perception and generation, professional dialogue | general, multimodal, multi-turn | 170 | ✓ |

🌍 **Language Diversity:** Each task exists in 23 parallel language versions
spanning 15 scripts, three resource levels and languages that differ in writing
direction, word delimiters and glyph shaping. Task IDs are
language-independent, so every language is evaluated on exactly the same tasks.

| High resource (7) | Medium resource (8) | Low resource (8) |
|---|---|---|
| English `en` · Chinese `zh` · Japanese `ja` · French `fr` · Russian `ru` · Arabic `ar` · Spanish `es` | Korean `ko` · Indonesian `id` · Hindi `hi` · Thai `th` · Hebrew `he` · Turkish `tr` · Vietnamese `vi` · Malay `ms` | Belarusian `be` · Eastern Panjabi `pa` · Kazakh `kk` · Khmer `km` · Burmese `my` · Lao `lo` · Tamil `ta` · Telugu `te` |

🔧 **Component-Complete Adaptation:** Unlike multilingual agent benchmarks that
translate only the task statement, BabelArena localizes the system, simulator
and evaluation prompts, the task inputs, the tool descriptions and the
environment content — the databases, policies and retrieval corpora agents read
at runtime — keeping shared entities consistent across all of them.

| Benchmark | Prompt | Task | Tool | Env. | Tasks | Domains | Languages | Instances |
|---|:---:|:---:|:---:|:---:|---:|---:|---:|---:|
| MAPS | ✗ | ✓ | ✗ | ✗ | 805 | 4 | 12 | 9,660 |
| GAIA-v2-LILT | ✓ | ✓ | ✗ | ✗ | 165 | 1 | 6 | 990 |
| OmnilingualGAIA2 | ✓ | ✓ | ✗ | ✓ | 640 | 1 | 11 | 7,040 |
| MLCL | ✗ | ✓ | ✗ | ✗ | 200 | 1 | 4 | 800 |
| SEATauBench | ✓ | ✓ | ✓ | ✓ | 278 | 3 | 6 | 1,668 |
| PolyWorkBench | ✓ | ✓ | ✗ | ✓ | 67 | 5 | 10 | 67 |
| **BabelArena** | ✓ | ✓ | ✓ | ✓ | **702** | **13** | **23** | **16,146** |

🧑‍🏫 **High-Quality Annotation:** Language variants are produced by BabelFlow,
an agentic workflow that traces each benchmark's runtime data flow to find the
text it can safely translate, and are accepted only after multi-layer
verification and human review. On 4,600 sampled translations (200 per
language), mean quality is 4.28 / 4.02 / 3.91 out of 5 for high-, medium- and
low-resource languages (inter-annotator Cohen's κ = 0.71). In a controlled
ablation, BabelFlow cuts tasks with broken references from 20.0% to 2.5% and
behavioral mismatches from 5.0% to 0.0% compared with independent field
translation.

🔒 **Scoring-Critical Identifiers Stay English:** Evaluation replays gold tool
calls against the localized environment and hashes the result, so the classes
those calls match on — person names, account tiers, addresses, enum values such
as `account_type`, foreign-key suffixes — are deliberately left in English in
every language. Everything an agent reads as natural language is translated;
translating an identifier would make a task unscoreable rather than harder.

📏 **Two Metrics, Never Collapsed:** Every task runs three independent trials
and reports **Pass^1** (per-trial success) and **Pass^3** (all three succeed),
plus **language consistency (LC)**, the share of trajectories whose
user-visible text stays in the target language — an agent can earn full task
reward while answering a Thai user in English.

## 📊 Main Results

Five frontier models, in percent; higher is better, best in bold.

**By benchmark family**

| Model | VitaBench<br>Pass^1 | <br>Pass^3 | <br>LC | DeepPlanning<br>Pass^1 | <br>Pass^3 | <br>LC | τ³-Bench<br>Pass^1 | <br>Pass^3 | <br>LC | ClawEval<br>Pass^1 | <br>Pass^3 | <br>LC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Claude-Opus-4.8 | 36.9 | 20.1 | 98.5 | 36.2 | 17.2 | 61.8 | 62.6 | 49.5 | **95.0** | **55.8** | **43.0** | 96.3 |
| GPT-5.6-Terra | 29.6 | 15.1 | 99.1 | 22.5 | 10.7 | **90.0** | 69.2 | 38.5 | 82.5 | 46.1 | 33.5 | 98.7 |
| Gemini-3.1-Pro | 34.3 | 17.7 | **99.9** | 18.6 | 5.6 | 74.3 | **71.4** | 46.9 | 86.2 | 41.5 | 29.3 | **98.8** |
| Qwen-3.7-Max | 36.1 | 18.9 | 98.6 | 41.6 | 23.8 | 57.5 | 59.0 | 49.1 | 92.8 | 32.4 | 24.6 | 98.5 |
| Qwen-3.8-Max | **42.3** | **25.0** | 94.7 | **46.0** | **26.5** | 75.8 | 62.0 | **50.0** | 87.8 | 40.8 | 27.1 | 88.7 |

**By language resource level**

| Model | High<br>Pass^1 | <br>Pass^3 | <br>LC | Medium<br>Pass^1 | <br>Pass^3 | <br>LC | Low<br>Pass^1 | <br>Pass^3 | <br>LC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Claude-Opus-4.8 | **51.3** | **34.3** | 90.4 | **48.1** | **33.9** | 87.2 | **44.8** | **29.6** | 86.7 |
| GPT-5.6-Terra | 45.3 | 26.3 | **98.8** | 43.9 | 25.1 | **90.9** | 36.8 | 21.9 | **89.6** |
| Gemini-3.1-Pro | 45.9 | 27.4 | 98.6 | 42.4 | 25.8 | 87.5 | 36.4 | 21.0 | 83.8 |
| Qwen-3.7-Max | 45.8 | 32.4 | 89.0 | 42.9 | 29.5 | 86.9 | 40.1 | 27.6 | 84.9 |
| Qwen-3.8-Max | 49.8 | 33.8 | 89.9 | 46.4 | 32.3 | 86.2 | 43.7 | 28.1 | 84.1 |

No model leads every family, and all five score lower on Pass^1, Pass^3 and LC
in low-resource languages than in high-resource ones. See the paper for the
failure, token-cost and language-switching analyses.

## 🗂️ Dataset Structure

One top-level directory per family, laid out exactly as its runner reads it.

```
tau3/                                     → data/tau3/           (TAU2_DATA_DIR)
  tau2/domains/<domain>/                  tasks, policies, tool descriptions, databases
  tau2/domains/banking_knowledge/         + documents/, the 698-doc retrieval corpus × 23
  tau2/user_simulator/                    simulated-user guidelines
vitabench/                                → data/vitabench/      (VITA_DATA_DIR)
  vita/domains/<domain>/tasks_<code>.json each task carries its own environment
deepplanning/                             → data/deepplanning/   (DEEPPLANNING_DATA_DIR)
  travelplanning/database/database_<code>/id_<n>/
  shoppingplanning/database_level<N>[_<code>]/case_<n>/
*/task_subsets/standard/                  the frozen task-ID lists
*/SHA256SUMS                              checksums (sha256sum -c SHA256SUMS)
```

| Family | Tasks / language | × 23 languages | Data files | Size |
|---|---:|---:|---:|---:|
| `tau3` | 212 | 4,876 | 17,999 | 244 MiB |
| `vitabench` | 200 | 4,600 | 100 | 300 MiB |
| `deepplanning` | 120 | 2,760 | 15,058 | 4.7 GiB |
| **Total** | **532** | **12,236** | **33,157** | **5.2 GiB** |

Per-language task counts: τ³-Bench = airline 50 + retail 57 + telecom 57 +
banking 48; VitaBench = 50 per domain; DeepPlanning = travel 60 + shopping
25 / 25 / 10 at levels 1–3.

Translated files sit next to their English source with a language suffix, which
each family spells its own way: τ³-Bench wants the display name
(`db_Chinese.json`, `tasks_Eastern Panjabi.json`), VitaBench and DeepPlanning
the ISO code (`tasks_pa.json`, `database_pa/`). English is the unsuffixed
baseline, except in VitaBench, where Chinese is. `./bench languages` prints the
mapping. German is deliberately absent: the source tree carried partial German
artifacts with no localized environment behind them, so a German run had
nothing to score against.

## 🛠️ Usage

The evaluation code lives in the
[BabelArena repository](https://code.alibaba-inc.com/alitranx/BabelArena); this
dataset is the task data, which is too large to commit there. `fetch-data`
expects a source directory whose second level is one directory per family —
which is how this dataset is laid out, so there is nothing to unpack or rename.

```bash
git clone https://code.alibaba-inc.com/alitranx/BabelArena.git
cd BabelArena
pip install pyyaml
./bench setup                                      # one virtualenv per family
./bench fetch-data --source /path/to/this/dataset  # fills data/
./bench check                                      # data, environments, config; no API calls
./bench run -b tau3 -l ja --agent-model <model>
```

`fetch-data` copies `tau3/`, `vitabench/` and `deepplanning/` into `data/`, and
`bench run` points each runner at its own subtree through the environment
variables above. Equivalent by hand (mind the trailing slashes — `data/<family>/`
already exists, holding the task lists from git):

```bash
for f in tau3 vitabench deepplanning; do
  rsync -a "$f/" "/path/to/BabelArena/data/$f/"
done
```

A successful `./bench check` prints `[ok] <family>: all 23 languages complete`
for each of the three.

This release holds the `standard` subset only, so a run with
`--task-subset full` will not resolve. The data is for evaluation, not
training: it is a fixed, frozen sample, and training on it makes any later
measurement with it meaningless.

## 🖼️ Attribution

The image and video assets in this dataset come from the ClawEval dataset
(<https://huggingface.co/datasets/claw-eval/Claw-Eval>), whose tasks are adapted
from the community-contributed OpenClaw, PinchBench, OfficeQA,
OneMillion-Bench, Finance Agent and Terminal-Bench 2.0.

## Acknowledgements

BabelArena is built on four agent benchmarks; please also cite them when you use
it: VitaBench, DeepPlanning, τ-bench / τ²-bench / τ-knowledge and Claw-Eval.
[NOTICE](https://code.alibaba-inc.com/alitranx/BabelArena/blob/main/NOTICE)
lists the attribution and every change made to them in this repository.

## 📄 Citation

If you use BabelArena in your research or find our work useful, please cite us:

```bibtex
@article{babelarena2026,
  title={BabelArena: A Large-Scale Multilingual Benchmark for LLM Agents},
  author={Peng Kuang and Yuchun Fan and Jiangnan Li and Minghao Wu and Jialong Tang and Haoran Wei and Weixuan Wang and Jianhong Tu and Baosong Yang and Tong Xiao},
  journal={arXiv preprint arXiv:2609.23490},
  year={2026},
  url={https://arxiv.org/abs/2609.23490}
}
```

Source benchmarks:

```bibtex
@article{he2025vitabench,
  title={VitaBench: Benchmarking LLM Agents with Versatile Interactive Tasks in Real-world Applications},
  author={Wei He and Yueqing Sun and Hongyan Hao and Xueyuan Hao and Zhikang Xia and Qi Gu and Chengcheng Han and Dengchang Zhao and Hui Su and Kefeng Zhang and Man Gao and Xi Su and Xiaodong Cai and Xunliang Cai and Yu Yang and Yunke Zhao},
  journal={arXiv preprint arXiv:2509.26490},
  year={2025}
}

@inproceedings{zhang2026deepplanning,
  title={DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints},
  author={Yinger Zhang and Shutong Jiang and Renhao Li and Jianhong Tu and Yang Su and Lianghao Deng and Xudong Guo and Chenxu Lv and Junyang Lin},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={7377--7407},
  year={2026}
}

@article{yao2024taubench,
  title={$\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains},
  author={Shunyu Yao and Noah Shinn and Pedram Razavi and Karthik Narasimhan},
  journal={arXiv preprint arXiv:2406.12045},
  year={2024}
}

@article{barres2025tau2bench,
  title={$\tau^2$-bench: Evaluating Conversational Agents in a Dual-Control Environment},
  author={Victor Barres and Honghua Dong and Soham Ray and Xujie Si and Karthik Narasimhan},
  journal={arXiv preprint arXiv:2506.07982},
  year={2025}
}

@article{shi2026tauknowledge,
  title={$\tau$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge},
  author={Quan Shi and Alexandra Zytek and Pedram Razavi and Karthik Narasimhan and Victor Barres},
  journal={arXiv preprint arXiv:2603.04370},
  year={2026}
}

@article{ye2026claweval,
  title={Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents},
  author={Bowen Ye and Rang Li and Qibin Yang and Yuanxin Liu and Linli Yao and Hanglong Lv and Zhihui Xie and Chenxin An and Lei Li and Lingpeng Kong and Qi Liu and Zhifang Sui and Tong Yang},
  journal={arXiv preprint arXiv:2604.06132},
  year={2026}
}
```
