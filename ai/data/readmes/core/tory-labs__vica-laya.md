---
license: apache-2.0
base_model: convaiinnovations/laya-multilingual
base_model_relation: finetune
language:
- ko
- en
pipeline_tag: text-classification
tags:
- laya
- gguf
- korean
- decision-model
- fine-tuned
---
# Vica Laya

Vica Laya is a Korean-focused judgment fine-tune of [Laya multilingual](https://huggingface.co/convaiinnovations/laya-multilingual). Release **2026.11.13.1** contains `B3`, the epoch-3 Q8_0 model of the [direct-judgment](experiments/direct-judgment/README.md) experiment, round two, arm B. It was trained from `training-checkpoints/mix25-epoch-1` (release `2026.11.06.1`) to answer three yes/no questions that the coding agent Vica asks on its direct edit path: `check` (does an edit do what was asked), `locate` (is a candidate line the place to change) and `done` (does the agent's last reply claim the work is finished), with the earlier judgment tasks kept in training. The user ordered this release after B3 passed the gates as revised on 2026-11-13; it did not pass the gates frozen before the experiment. The previous release `2026.11.08.1` is kept unchanged under [`releases/2026.11.08.1/`](releases/2026.11.08.1/README.md), and its downloads stay in `downloads/2026.11.08.1/`.

한국어 문장을 읽고 주어진 선택지에 따라 판단하는 Laya 튜닝 버전입니다. **2026.11.13.1**은 코딩 에이전트 Vica가 직접 수정할 때 묻는 세 가지 판단(`check`: 수정이 요청대로 됐나, `locate`: 이 줄이 고칠 곳인가, `done`: 마지막 답이 끝났다고 말하나)을 배운 `B3`입니다. 선택에 쓰지 않은 시험 분할에서 `done`은 **98/98건**으로 기준 모델 Jev(98/98)와 같았고, 처음 여는 `test3` 871행에서도 238/238건이었습니다. `check`(176/239, Jev 230/239)와 `locate`(56/82, Jev 71/82)는 Jev에 못 미쳐, Vica에서는 `done`만 이 모델이 답합니다. 기존 판단 과제는 이전 모델보다 대체로 나아졌습니다(뉴스 주제 474건 391건, 이전 2026.11.08.1 355건). 정답은 사람이 아니라 Claude가 쓰고 다른 Claude가 검증한 라벨입니다. **이 모델은 2026.11.08.1이 아니라 2026.11.06.1에서 출발해서 2026.11.08.1의 지식그래프·리서치 요약 학습이 들어 있지 않고, 그 자료에서의 정확도는 재지 않았습니다.** 85% 목표는 달성하지 못했습니다.

## Files and compatibility

- `downloads/2026.11.13.1/`: the downloads. One file per platform holds the `vica-laya` program, the model `vica-laya.gguf` (361,797,056 bytes; includes the tokenizer and compiled decision graph) and the license files. `SHA256SUMS` lists the three files.
- `model.safetensors` (float16, 643,835,524 bytes) with `rl_agent_config.json`, `config.json`, `encoder/config.json` and `tokenizer/`: the same release as a float checkpoint for the `laya` Python package and for further tuning. It is the original training checkpoint of the exported epoch, copied byte-for-byte from the training run; see [Float checkpoint](#float-checkpoint).
- `training-checkpoints/mix25-epoch-1/`: the original float checkpoint of release `2026.11.06.1` and the base checkpoint this release was trained from. Unchanged.
- `releases/2026.11.08.1/` and `downloads/2026.11.08.1/`: the previous model (이전 모델), exactly as published on 2026-11-08 and 2026-11-09.
- `releases/2026.11.06.1/`: the release before it, unchanged.
- `topic-questions.json`: the four-way news taxonomy used with this model.
- `example-state.json` and `example-request.jsonl`: an authored Korean security example.
- `evaluation.json`: this release's results on the direct-edit jobs, the existing tasks and the reserved rows, the gates and what was not measured.
- `model-manifest.json` and `SHA256SUMS`: provenance, the release decision and file integrity. `SHA256SUMS` lists text files as Git stores them (LF line endings).
- `experiments/direct-judgment/`: the scripts, questions, plan and aggregate records (`results-20261112.json`, `results-round2.json`, `results-round3.json`) of the experiment. Private cases, labels and run outputs are not included.

## Download

| Platform | File | Bytes | Needs on the computer |
|---|---|---:|---|
| macOS arm64 (Metal) | [`vica-laya-macos-arm64.tar.gz`](downloads/2026.11.13.1/vica-laya-macos-arm64.tar.gz) | 334,328,315 | nothing else |
| Linux x86_64 (Vulkan) | [`vica-laya-linux-x86_64.tar.gz`](downloads/2026.11.13.1/vica-laya-linux-x86_64.tar.gz) | 351,335,194 | Vulkan loader (`libvulkan.so.1`); built on Ubuntu 22.04 (glibc 2.35) |
| Windows x86_64 (Vulkan) | [`vica-laya-windows-x86_64.zip`](downloads/2026.11.13.1/vica-laya-windows-x86_64.zip) | 351,037,226 | Vulkan loader (`vulkan-1.dll`, installed with GPU drivers) |

x86_64 builds need a CPU with AVX2, FMA and BMI2 (Intel Haswell 2013, AMD Excavator 2015 or later). The Windows file carries the Microsoft Visual C++ runtime DLLs next to `vica-laya.exe`. The macOS program is not notarized, so a browser download may be blocked by Gatekeeper until it is allowed. Check a download against [`downloads/2026.11.13.1/SHA256SUMS`](downloads/2026.11.13.1/SHA256SUMS) before unpacking.

`vica-laya` is built from [ggmlc v0.9.7](https://github.com/monatis/ggmlc/tree/5490a13661d95add025ec1b111adbc88234a9b4f) source at [su-record/vica-laya](https://github.com/su-record/vica-laya) (commit `4bc3a55`, Actions run `43425125282`; the runner source is unchanged since `5a75e53`, only the pinned model and the rename check changed). It is a compiled `laya.cpp` decision runner, not a generative LLM runtime; the model is not for llama.cpp or Ollama. Its built-in help text still uses upstream wording.

`vica-laya.gguf` SHA-256:

```text
c2d69b85ba80daf88f93c6e5bc6b5368d8d0491dcc1d85efeecdf1d5cb3df96e
```

It holds the same 130 tensors as B3's Q8 export (SHA-256 `1babc5537e4ecc05516ea52ef86936980b700f5cc78ccfbeeade839ce417ce4d`, not published). Only the model name and the checkpoint in its metadata (`tory-labs/vica-laya@2026.11.13.1`) were changed; answers were checked identical on the 1,034 direct-judgment calibration questions. For packaging it was staged at the repository root in commit `27561d9` and removed again by the release commit.

## Run

Unpack the file for your platform and run from the `vica-laya` folder:

```bash
./vica-laya decide vica-laya.gguf \
  --family multilingual \
  --state-file example-state.json \
  --questions-file topic-questions.json \
  --device auto --json
```

`example-state.json` and `topic-questions.json` are in this repository. For repeated requests, keep one daemon alive and write one JSON request per line to its standard input:

```bash
./vica-laya daemon vica-laya.gguf --family multilingual --device auto
```

`example-request.jsonl` contains a complete request. Responses contain a selected category and scores. The scores are model estimates, not a measured probability that each answer is correct.

The news choices are `security`, `ai`, `development`, and `other` (business and unrelated topics). The question instructions define the boundaries; changing them can change accuracy. Use the provided questions when reproducing the reported news task.

## Base checkpoint: original tuned `mix25-epoch-1`

Release `2026.11.13.1`, like `2026.11.08.1` before it, continues training from the
`mix25-epoch-1` checkpoint, the original pre-Q8 float checkpoint of release `2026.11.06.1`. It is
published in
[`training-checkpoints/mix25-epoch-1`](training-checkpoints/mix25-epoch-1/README.md)
and has not changed: 643,835,524 bytes, SHA-256
`c0889283894d642577c133f24f52842d89a02dd7d7261343ab4ddf76d2185043`.
The package includes the matching tokenizer and configuration, plus hashes and
provenance. Its saved training configuration is preserved as historical evidence;
the pending-selection fields do not supersede the later release decisions.

To download this exact checkpoint on another computer (it is identical at every
revision since its first publication, `2ee14fb1dc3fdca01c75e6a2e0326a3db4f80673`):

```bash
hf download tory-labs/vica-laya \
  --include "training-checkpoints/mix25-epoch-1/**" --local-dir local/models
```

Pass `local/models/training-checkpoints/mix25-epoch-1` to `laya.load()` or
`scripts/laya-tuning/train.py --base`. Loading the saved checkpoint on CPU in
offline mode produced `security` with probability 0.9378 for the bundled example.
This checks execution only. Optimizer state and private training data are not
part of the package.

## Float checkpoint

`model.safetensors` holds the `2026.11.13.1` weights in the layout of the upstream checkpoint, so the [`laya`](https://pypi.org/project/laya/) Python package (tested with 0.4.22) loads this repository directly. Only `rl_agent_config.json`, `model.safetensors`, `encoder/` and `tokenizer/` are downloaded for that; the GGUF is not needed.

```python
import json
import laya

agent = laya.load("tory-labs/vica-laya")  # or a local clone path; device="cuda", "mps" or "cpu" to choose
state = json.load(open("example-state.json", encoding="utf-8"))
questions = json.load(open("topic-questions.json", encoding="utf-8"))
print(agent.system_one(state, questions))
```

The root checkpoint is the original float16 training checkpoint of the exported epoch (epoch 3 of round two, arm B), copied byte-for-byte from the training output (SHA-256 `5ee42ec7604e40259cab503d749e207c70bd154a9b62c0a42f9e1e284bf6b0af`). Verification on 2026-11-13: strict load into `laya` 0.4.22 with 321,908,995 parameters; on CPU the Python agent answers the bundled example with `security` 0.9006, as does the Q8 runtime with `vica-laya.gguf` (0.9006). These checks cover execution only, not accuracy. The float checkpoint of `2026.11.08.1` is at `releases/2026.11.08.1/model.safetensors`.

`rl_agent_config.json` keeps the driver's `training` block, including `eligible_for_installation: false` and `selection: "pending quantized calibration"`. Those fields were written before epoch selection and before the release decision and are preserved as evidence; nothing in this repository reads them, and `model-manifest.json` records the actual release decision.

The previous release's root checkpoint was a Q8 reconstruction made with `scripts/laya-tuning/gguf_to_checkpoint.py` (dequantized GGUF tensors with the export-time LayerNorm folds inverted). It now lives at `releases/2026.11.06.1/model.safetensors` together with its `reconstruction-report.json`. The script still rebuilds a float checkpoint from any release GGUF when the upstream checkpoint is reachable. The `2026.11.06.1` GGUF is in repository history:

```bash
hf download tory-labs/vica-laya --revision 52de32568426ecfc969ad60de76df533917702a6 \
  releases/2026.11.06.1/laya_multilingual_q8_0.gguf --local-dir local/models
python scripts/laya-tuning/gguf_to_checkpoint.py --gguf local/models/releases/2026.11.06.1/laya_multilingual_q8_0.gguf \
  --base convaiinnovations/laya-multilingual --out local/runs/rebuilt-2026.11.06.1
```

## Evaluation

All numbers are answers of the standalone Q8 runtime on the Mac tuning machine, from [`experiments/direct-judgment/results-round2.json`](experiments/direct-judgment/results-round2.json) and [`results-round3.json`](experiments/direct-judgment/results-round3.json); `evaluation.json` holds the full counts. The direct-edit cases were written by Claude subagents on public permissive GitHub repositories and their labels were verified by other Claude subagents (opaque ids for `check`); they were **not human-adjudicated**. The reference is Jev (TypeSafe `jev-1.14.0`), asked once per row with the same observations. A row counts as right when Vica would act rightly on the answer: `check` at P(yes) ≥ 0.7, `locate` singles out a line at P ≥ 0.5, `done` skips the check reminder at P < 0.2.

| Job | Split | B3 | Jev | 2026.11.08.1 | 2026.11.06.1 |
| --- | --- | ---: | ---: | ---: | ---: |
| `done` | test, 98 rows | 98/98 | 98/98 | 31/98 | 27/98 |
| `done` | `test3`, 238 rows | 238/238 | 237/238 | — | — |
| `check` | test, 239 rows | 176/239 | 230/239 | 119/239 | 120/239 |
| `check` | `test3`, 472 rows | 361/472 | 434/472 | — | — |
| `locate` | test, 82 rows | 56/82 | 71/82 | 10/82 | 7/82 |
| `locate` | `test3`, 161 rows | 118/161 | 128/161 | — | — |

The test split (381 rows, four repositories) was read once, for the frozen B3, at the round-two final evaluation. `test3` (871 rows, eight further repositories) was read once on 2026-11-13 during a cascade check that the user then ruled out of scope (models are not mixed); B3's own answers are shown. On the calibration rows that chose B3, the counts were `done` 97/101, `check` 174/234 and `locate` 51/74 (Jev 98, 213 and 61). The earlier releases answer almost every `check` yes (wrong edits 0–1 of 119 caught) and get most `done` rows wrong, which is what these jobs were trained to fix. `check` separates right from wrong edits better than it decides them (ranking AUC 0.83 on the test split, 0.88 on `test3`; Jev 0.97 on calibration), and `locate` ranks a usable line first in 29 of 44 present test rows but is sure enough to single it out in 19.

Existing judgment tasks, correct answers on the development files (all used in earlier development, so not unseen tests):

| Task (rows) | 2026.11.06.1 | 2026.11.08.1 | B3 |
| --- | ---: | ---: | ---: |
| News topic, calibration (474) | 365 | 355 | 391 |
| News topic, known (130) | 95 | 97 | 107 |
| News topic, legacy (107) | 87 | 84 | 91 |
| News topic, fresh (48) | 38 | 36 | 37 |
| Workflow mode, retention (187) / calibration (85) | 172 / 82 | 171 / 82 | 175 / 80 |
| Next action, retention (78) / calibration (60) | 59 / 46 | 59 / 45 | 57 / 48 |
| Work/chat label, retention (78) / calibration (60) | 77 / 59 | 77 / 59 | 77 / 59 |
| Message kind, retention (48) / calibration (50) | 47 / 44 | 46 / 42 | 47 / 45 |
| Needs action, retention (48) / calibration (50) | 40 / 47 | 40 / 47 | 43 / 49 |
| Evidence status, retention (48) / calibration (48) | 44 / 46 | 44 / 45 | 45 / 47 |
| English department (12) / refund requested (12) | 10 / 10 | 10 / 10 | 11 / 10 |

On the 516 reserved topic rows, opened for the first time for B3 and now consumed, B3 answered 447/516 (86.6 %) against 403/516 for `2026.11.06.1`; by class AI 199/225, development 56/70, other 136/155, security 56/66. `2026.11.08.1` was not measured on them. Warm p95 latency: 25.4 ms for B3, 25.7 ms for `2026.11.08.1`, 25.9 ms for `2026.11.06.1` (same Mac, same binary).

**Gates and limits:**

- The gates frozen before the experiment rejected B3 (`check` and `locate` below Jev − 0.02; a few small existing tasks over the 1 % allowance). On 2026-11-13, after the round-two calibration results were known, the user changed them: per job at Jev − 0.02, other jobs not below the installed release, and each existing task may lose at most max(1 % of rows, 2 rows) while the summed correct answers do not fall. B3 passed those on calibration and then once on the unseen test split and the reserved rows. Only `done` is accepted; Vica keeps asking Jev for `check` and `locate`.
- The 85 % target is not met: news topic 391/474 (82.5 %) with security 38/55, and on the reserved rows development and security stay under 85 %.
- B3 was trained from `2026.11.06.1`, not from `2026.11.08.1`, so the knowledge-graph and research-summary training of `2026.11.08.1` is not in it. Its accuracy on that private corpus was not measured; the corpus is on another machine.
- Round three (Jev's probabilities as soft targets) produced no better candidate; see [`results-round3.json`](experiments/direct-judgment/results-round3.json).

### Previous release — 2026.11.08.1

This historical section describes release `2026.11.08.1`, now kept under `releases/2026.11.08.1/`. Its numbers do not describe `2026.11.13.1`. Statements below about what remained unopened describe 2026-11-08; the 516 reserved rows were consumed on 2026-11-13.

Release `2026.11.08.1` was measured only on the held-out splits of the new
oracle-knowledge corpus, with the standalone Q8 runtime (Vulkan build on an NVIDIA
RTX 4060). The comparator is the previous release `2026.11.06.1`, measured with the
same binary on the same rows. The held-out rows are Korean knowledge-graph and
research summaries, not news excerpts. Their labels are two independent Opus 5.5
passes under
[`experiments/oracle-knowledge/annotation-protocol.md`](experiments/oracle-knowledge/annotation-protocol.md)
that agreed on all 363 rows (Cohen's kappa 1.0); they were **not human-adjudicated**.
The calibration split chose the exported epoch and fitted the temperature, so its
numbers are optimistic. The test split was never trained on or used for selection,
but it was measured for all four experiment arms, so it compared candidates rather
than confirming one. No new independent final evaluation was run.

| Split | Previous release 2026.11.06.1 | 2026.11.08.1 |
| --- | ---: | ---: |
| Calibration (178 rows) | 135/178 (75.8%) | 155/178 (87.1%) |
| Test (185 rows) | 132/185 (71.4%) | 153/185 (82.7%) |
| Balanced accuracy, calibration / test | 0.746 / 0.785 | 0.870 / 0.848 |
| Confident errors, calibration / test | 17 / 20 | 7 / 4 |
| Log loss, calibration / test | 0.736 / 0.813 | 0.450 / 0.400 |

Recall by class on the test split, with the calibration split in parentheses:

| Class | Previous release | 2026.11.08.1 |
| --- | ---: | ---: |
| AI | 82/92 (83/93) | 83/92 (85/93) |
| Development | 3/4 (2/4) | 3/4 (3/4) |
| Security | 5/5 (5/5) | 5/5 (5/5) |
| Business/other | 42/84 (45/76) | 62/84 (62/76) |

Incorrect assignments on the test split fell from 24 to 7 for security, from 14
to 11 for development and from 12 to 6 for AI, while incorrect `other`
assignments rose from 3 to 8. Row by row, 26 test rows became correct (20 `other`,
6 AI) and 5 became wrong, all of them AI rows now answered `other`; on
calibration 23 rows became correct and 3 became wrong with the same pattern. Only
5 security and 4 development rows are held out per split, so one row moves those
recalls by 20 to 25 points. Full counts and confusion matrices are in
`evaluation.json`.

**Not measured for this release:**

- The existing-judgment retention tasks (workflow mode, next action, work/chat
  label, message kind, needs action, evidence status, English department, refund
  requested) and their frozen one-percentage-point allowance. Their sets are on
  the Mac tuning machine. This stage updated the last four encoder layers with a
  learning rate ten times that of the previous stage and included no replay rows
  for these tasks, so regression is possible and unmeasured.
- The original news cohorts: 474 topic calibration, 48 primary-source
  calibration, 130 known news and 107 legacy topic calibration rows. The 85 %
  target is defined on them, so for `2026.11.08.1` it is **neither met nor
  failed; it is unverified**. The previous release scored 365/474, 38/48, 95/130
  and 87/107.
- The final speed gate. The `decide` command answered the bundled example in
  281.1 ms (Vulkan build) and 237.5 ms (CUDA build) on this PC, first request
  each; no warm-daemon latency was measured.
- The 516 reserved final rows (48 primary-source and 468 earlier) remain
  unopened.

### Previous release — 2026.11.06.1

This historical section describes release `2026.11.06.1`, SHA-256 beginning
`b45ca2e8`, now kept under `releases/2026.11.06.1/`. Its numbers do not describe
`2026.11.08.1`.

The following are existing Q8 runtime results from the
[main-action contrast experiment](experiments/hermes-contrast/results-20261106.json).
The comparator is release `2026-11-05`, SHA-256 beginning `4a00ab53`, a previously
tuned model rather than the untouched upstream model. The 474-topic and
48-primary-source calibration cohorts had already been used in development. The
130-case news set is a consumed former final test. None is a new independent
final evaluation of that release, and labels are assistant-authored rather than
human-adjudicated.

| Cohort | Prior release | 2026.11.06.1 |
| --- | ---: | ---: |
| Existing topic calibration | 333/474 (70.3%) | 365/474 (77.0%) |
| Primary-source calibration | 34/48 (70.8%) | 38/48 (79.2%) |
| Known, consumed news test | 93/130 (71.5%) | 95/130 (73.1%) |
| Legacy topic calibration | 86/107 (80.4%) | 87/107 (81.3%) |

Its recall by class was:

| Class | Existing topic calibration | Primary-source calibration | Known news set |
| --- | ---: | ---: | ---: |
| AI | 175/214 (81.8%) | 10/12 (83.3%) | 14/22 (63.6%) |
| Development | 53/69 (76.8%) | 10/12 (83.3%) | 12/14 (85.7%) |
| Security | 33/55 (60.0%) | 7/12 (58.3%) | 29/38 (76.3%) |
| Business/other | 104/136 (76.5%) | 11/12 (91.7%) | 40/56 (71.4%) |

The frozen selection rejected that candidate for three reasons:

- Incorrect AI assignments increased from 45 to 54 on existing topic calibration.
- Development misses increased from 15 to 16; the gate required at least one fewer miss.
- Confident errors increased from 4 to 5 on primary-source calibration.

Confident errors on the 474-topic cohort fell from 65 to 39, but that improvement
does not remove the separate failures. **The 85% overall and per-class target was
unmet.** After receiving the failed-gate report, the user requested deployment of
that model. This was an explicit release override, not a protocol pass or a change
to the frozen criteria. The original experiment record remains rejected.

Existing judgment retention results were:

| Task | Prior release | 2026.11.06.1 |
| --- | ---: | ---: |
| Workflow mode | 253/272 | 254/272 |
| Next action | 106/138 | 105/138 |
| Work/chat label | 136/138 | 136/138 |
| Message kind | 90/98 | 91/98 |
| Needs action | 85/98 | 87/98 |
| Evidence status | 88/96 | 90/96 |
| English department | 10/12 | 10/12 |
| Refund requested | 9/12 | 10/12 |

Next-action accuracy fell by 1/138 (0.72 percentage points), within the frozen
one-percentage-point retention allowance; this is still an observed loss.
These previously used sets do not establish independent generalization.

On one local Apple Silicon Q8 daemon pass over the 48 primary-source calibration
inputs, the first request took **462.04 ms** versus **536.42 ms** for the prior
release. The remaining 47 requests measured **24.20 ms median / 25.48 ms p95**,
versus **25.01 ms / 26.65 ms**. These are calibration observations, not the final
speed gate, end-to-end application latency or a guarantee on other hardware.
The separate 48-case final and earlier 468 reserved final cases remained unopened;
no new final evaluation or final speed gate was run for that release. Jev parity
has not been established.

### Prior release evaluation — 2026-11-05

This historical section describes only SHA-256
`4a00ab531b5a6c7a1ef009c9617137a4a76adfd8a5877cd35b50928030169bb2`.
Its 93/130 result, language diagnostic and latency measurement do not describe
release `2026.11.06.1` or `2026.11.08.1`.

The model was selected using calibration data before one source-separated final evaluation of 130 public-news excerpts. Reference labels were authored by an independent assistant and were **not human-adjudicated**. The test measures this specific classification task, not general Korean fluency or all computer-use decisions. It is now a consumed test set.

| News classification result | Value |
| --- | ---: |
| Overall accuracy | 93/130 (71.5%) |
| Mean per-class recall | 71.1% |
| AI recall | 13/22 (59.1%) |
| Development recall | 11/14 (78.6%) |
| Business/other recall | 41/56 (73.2%) |
| Security recall | 28/38 (73.7%) |

The preceding local tuned version scored 71/130 (54.6%) on the same final test. That comparison is **not against the untouched upstream model**.

Existing judgment regression checks were also retained:

| Task | Correct / cases |
| --- | ---: |
| Workflow mode | 253/272 |
| Next action | 106/138 |
| Work/chat label | 136/138 |
| Message kind | 90/98 |
| Needs action | 85/98 |
| Evidence status | 88/96 |

These regression sets were previously used during development and do not constitute independent final tests. A separate paired Korean/English diagnostic scored 26/32 in each language; it is not a general language-proficiency benchmark.

On the local Apple Silicon machine, a fixed calibration workload of 20 inputs repeated three times measured warm daemon round-trip latency of **19.51 ms median / 27.52 ms p95**. These are local runtime measurements, not end-to-end application latency or a guarantee on other hardware.

Later experimental models reached 83.2% on a calibration set and 78.5% on a previously consumed news set, but failed the 85% acceptance target. Those results describe other experimental weights, not any release summarized above.

## Training and provenance

- Upstream: `convaiinnovations/laya-multilingual`, revision `1720e3e3357cfe1e281542e223f8273b0890ca34`.
- Release `2026.11.13.1` (B3) starts from `training-checkpoints/mix25-epoch-1`. Four epochs tuned the last 12 encoder layers and the decision head with encoder learning rate `2e-5` and head learning rate `5e-5` on Apple silicon (MPS) with the bounded-memory driver; epoch 3 was exported. Training data: the earlier 3,400 train rows plus 2,936 verified direct-edit rows (`check` 1,606, `done` 790, `locate` 540) from public permissive repositories listed in `experiments/direct-judgment/sources.lock.json`, 10,175 items in all; the direct-edit jobs take 50 % of the loss. Selection read calibration rows only. Plan, scripts and records: [`experiments/direct-judgment/`](experiments/direct-judgment/README.md).
- Previous release `2026.11.08.1` (now `releases/2026.11.08.1/`) starts from `training-checkpoints/mix25-epoch-1`, the original float checkpoint of `2026.11.06.1`. Six epochs tuned the last four encoder layers and the decision head with encoder learning rate `1e-5`, head learning rate `3e-5` and seed `20261105`; epoch 3 was exported. Training ran 344 seconds on an NVIDIA RTX 4060 (CUDA).
- The driver was `experiments/hermes-graph/train-weighted.py` over `scripts/laya-tuning/train.py`: soft cross-entropy with per-row loss weights (security rows ×3, the 695 rows flagged ambiguous ×0.5, normalized to a mean of 1.0). Weights apply to training only; calibration metrics are unweighted.
- The training set contained 1,833 rows of the private oracle-knowledge corpus: 1,374 knowledge-graph summaries, 220 repository commit messages, 119 repository documentation sections and 120 game-research summaries (labels: AI 743, other 556, development 434, security 100). The 178 calibration and 185 test rows come from the knowledge graph and game research only; repository rows are training-only. Splits are pinned by source family with seed `20261108`; 32 unusable and 18 label-conflicting rows were excluded. Every row carries only the four-way topic question; no replay rows for the other judgment tasks were included.
- Labels are Opus 5.5 annotations under `experiments/oracle-knowledge/annotation-protocol.md`: one pass over 2,246 rows and a second independent pass over the 363 held-out rows (363/363 agreement). No human adjudication.
- Temperature `[0.6909, 1.0, 1.0]` was fitted on the 178 calibration rows; the expected calibration error could not be computed because its only bucket was empty.
- Four arms were trained and measured; see [`experiments/oracle-knowledge/results-20261108.json`](experiments/oracle-knowledge/results-20261108.json) and the tuning history below. No frozen selection protocol was run for this stage.
- Q8_0 export: `monatis/ggmlc`, commit `5490a13661d95add025ec1b111adbc88234a9b4f` (v0.9.7).
- Float checkpoint (`model.safetensors`): the original epoch-3 training checkpoint, copied byte-for-byte; not reconstructed from the GGUF.
- Previous release `2026.11.06.1` (now `releases/2026.11.06.1/`) started from the floating-point `clean-epoch-3` checkpoint, which had failed its own selection gates. One shared epoch tuned the last four encoder layers and decision head with encoder learning rate `1e-6`, head learning rate `2e-6` and seed `20261105`, on 3,400 rows (3,144 retained rows plus 256 synthetic main-action contrasts in 64 quartets) with 827 calibration rows. Its weights are `0.75 * clean-epoch-3 + 0.25 * contrast-epoch-1`, then Q8_0 export; four predefined mixtures were compared, all failed selection, and the user authorized the 25% mixture separately. Its published root float checkpoint was rebuilt from the GGUF; see its `reconstruction-report.json`.
- Historical baseline `2026-11-05` used 1,565 training rows and 415 calibration rows in its last accepted stage; epoch 3 was selected. It tuned 22 encoder layers with encoder learning rate `3e-6`, head learning rate `8e-6`, and seed `20261105`.
- Raw training/evaluation examples, annotations, local logs, and the separate Vica routing model are not included.

## Intended use and limits

The model classifies supplied text with typed questions. It does not read screenshot pixels or infer screen coordinates. A computer-use observer must supply text and current screen bounds; the host agent handles labels, colors, placement, scrolling, and stale observations.

Ambiguous articles and the boundary between AI applications, general development, technical releases, and business announcements remain error sources. Confidence scores can be high on wrong answers. Release `2026.11.13.1` answers `check` and `locate` well below the reference model, so Vica uses it only for `done`; it does not include the knowledge-summary training of `2026.11.08.1`. Validate the model on the specific tasks and inputs where it will be used.

## Local development

The [self-retention tuning plan (Korean)](docs/self-retention-plan-20261108.md)
was written against `2026.11.06.1` and carries a note about the replacement. It
compares hard-target training with preservation of the existing Laya's decision
distributions. This is a plan; its new training and evaluation have not run.

Model development is independent of Vica and any other consuming application.
The training, Q8 export and evaluation entrypoints accept explicit input paths;
they do not need an application checkout, application settings or an installed
application model. Publishing a model and updating an application are separate
tasks. Application integration requires its own explicit request.

Keep the development environment in this checkout:

| Location | Purpose |
| --- | --- |
| `.venv/` | Python and pinned training dependencies |
| `local/models/` | Downloaded model weights and checkpoint metadata |
| `local/data/` | Private training and evaluation inputs |
| `local/runs/` | New experiment outputs and intermediate checkpoints |
| `local/bin/` | Standalone `laya` runtime |
| `local/toolchains/ggmlc/` | Pinned Q8 compiler source |

`.venv/` and `local/` are ignored by Git. Published checkpoint weights are
tracked through Git LFS. A checkout made without Git LFS contains pointers in
place of its large files; the following setup downloads actual model files into
the independent development directory without changing those tracked pointers:

```bash
uv venv --python 3.12 .venv
uv pip sync --python .venv/bin/python scripts/laya-tuning/requirements.txt
source .venv/bin/activate
LAYA_REVISION="$(git rev-parse HEAD)"
hf download tory-labs/vica-laya --revision "$LAYA_REVISION" \
  --include 'training-checkpoints/mix25-epoch-1/**' \
  --include 'model-manifest.json' --include 'downloads/2026.11.08.1/vica-laya-macos-arm64.tar.gz' \
  --local-dir local/models
# optional: the previous release's float checkpoint and records
hf download tory-labs/vica-laya --revision "$LAYA_REVISION" \
  --include 'releases/2026.11.06.1/**' --local-dir local/models
```

Unpack the download for your platform and use its `vica-laya` program (for example at
`local/bin/vica-laya`) as the standalone runtime. For Q8
export, prepare the compiler independently:

```bash
git clone https://github.com/monatis/ggmlc.git local/toolchains/ggmlc
git -C local/toolchains/ggmlc checkout --detach 5490a13661d95add025ec1b111adbc88234a9b4f
```

`scripts/laya-tuning/train.py` fine-tunes from an explicitly supplied float
checkpoint. Its `--device auto` uses the pinned Laya package's device resolver;
`--device` can select a backend explicitly. Apple Silicon MacBooks use PyTorch
MPS for training and Metal for the standalone Q8 runtime, not NVIDIA CUDA.
The same training entrypoint accepts `--device cuda` on a machine with a
compatible NVIDIA GPU and CUDA-enabled PyTorch. No separate Vica source is needed.
Rows are one JSON object per line with `id`, `family`, `split` (`train` or
`calibration`), `state`, `questions` and `targets`; an optional per-row
`loss_weight` is read by `experiments/hermes-graph/train-weighted.py`, which wraps
the same entrypoint and produced release `2026.11.08.1`. `export.py` turns a result
into the Q8_0 GGUF with a ggmlc v0.9.7 source checkout, and `evaluate.py` measures
a GGUF with the `laya` runtime binary:

```bash
python scripts/laya-tuning/train.py --data local/data/rows.jsonl \
  --base local/models/training-checkpoints/mix25-epoch-1 --out local/runs/candidate \
  --device mps \
  --epochs 1 --train-last-layers 4 --encoder-lr 1e-6 --head-lr 2e-6
python scripts/laya-tuning/export.py --source local/toolchains/ggmlc \
  --checkpoint local/runs/candidate --out local/runs/candidate/laya_multilingual_q8_0.gguf
```

The command above explicitly selects the MacBook GPU. On NVIDIA CUDA hardware,
replace `--device mps` with `--device cuda`; use `--device cpu` for CPU execution.
CPU, MPS and Metal example runs have been verified on an Apple M5 Pro. The
`2026.11.08.1` training, Q8 export and evaluation ran with CUDA on a Windows PC
with an RTX 4060 (8 GB); both the Vulkan and the CUDA build of the standalone
runtime answered the bundled example there.

The experiment directories preserve past workflows, including their original
private paths. Those archives and the historical installation/latency helpers are
not the setup for new development. Optional application checks in
`integrations/vica` are outside the model workflow. Preserve completed experiment
outputs and frozen labels, splits and criteria; only a calibration-selected,
frozen candidate may open its final test. A public clone does not include private
training datasets or reserved test data.

### Tuning history — 2026-11-08

The `experiments/oracle-knowledge` workflow built a new private corpus from the
user's ssh oracle server and local repositories: Korean knowledge-graph summaries
(`sutory-wiki`), two game-research corpora, and, for training only, commit
messages and documentation sections of local repositories. A read-only snapshot
was taken; private mail and internal incidents were not imported. Opus 5.5
labelled 2,246 rows in a first pass under the written annotation protocol (1,684
knowledge-graph, 362 repository, 150 game-research and 50 pilot rows) and the 363
held-out rows a second time; the passes agreed on every row (Cohen's kappa 1.0),
which is same-family agreement rather than human adjudication. Family-pinned
splits with seed `20261108` gave 1,833 training, 178 calibration and 185 test
rows after excluding 32 unusable and 18 label-conflicting rows; 695 training
rows flagged ambiguous received loss weight 0.5 and security rows weight 3.

On these splits the previous release `2026.11.06.1` scored 135/178 on
calibration and 132/185 on test. Its main failure was business/other rows
answered as security, development or AI: other recall 45/76 and 42/84.

Four arms, all from `mix25-epoch-1` with seed `20261105` and six epochs, are
recorded in
[`results-20261108.json`](experiments/oracle-knowledge/results-20261108.json).
The two head-only arms could not move the boundary: arm A (duplicated rows,
pass-1 labels) never improved on the base checkpoint's 136/178 float calibration
answers, and arm B (loss-weighted rows) reached 137/178 at epoch 6; their Q8
test results were 133/185 and 135/185. The two arms that also tuned the last four
encoder layers did: arm C (duplicated rows) reached 148/178 on Q8 calibration at
its selected epoch 4 with balanced accuracy 0.9115 and 146/185 on test; arm D
(loss-weighted rows) reached 155/178 at epoch 3 with balanced accuracy 0.8699 and
153/185 on test. Arm D epoch 3 was taken as the candidate for the most correct
calibration answers with AI recall 85/93 and security 5/5. Arm C epoch 4's
higher balanced accuracy came from development scoring 4/4 on a four-row class
while its AI recall fell to 76/93. No frozen selection protocol existed for this
stage, and the test split was measured for every arm, so it did not stay closed
for one frozen candidate.

The candidate record stated that retention and the original news cohorts had
not been checked on this PC. After that report the user ordered deployment. The
candidate was published as `2026.11.08.1`, the release was recorded as
`user_authorized_without_protocol_checks`, and `2026.11.06.1` moved unchanged
to `releases/2026.11.06.1/` as the previous model. The 516 reserved final rows
remain unopened, and no application was changed.

### Tuning history — 2026-11-06

The following records preserve the experiment outcomes before the explicit
`2026.11.06.1` release override. References to the deployed or distributed model
in this history mean the `2026-11-05` baseline, SHA-256 beginning `4a00ab53`.
Statements that weights were unchanged or unpublished describe the end of each
experiment; the later release decisions above do not change their verdicts.
Release `2026.11.06.1` itself is now the previous model.

[Aggregate experiment results](experiments/results-20261106.json) preserve four
attempts, their selection criteria, model hashes and measured failures. None of
these attempts replaced the distributed model.

The boundary-diverse candidate was selected from four Q8 exports before a new
160-example test. Compared with the distributed model on that same test, AI recall rose from
65% to 70%, business/other recall fell from 80% to 72.5%, and overall accuracy stayed
at 114/160 (71.25%). Warm p95 latency was 27.78 ms versus 27.80 ms. The business/other
loss exceeded the declared three-percentage-point limit, so the candidate was
rejected. These are assistant-labeled examples, with 40 cases per class; they do
not establish production accuracy or achievement of the 85% target.

The frozen verifier also reported a balanced-accuracy loss of about 1e-16 from
floating-point rounding. With equally sized classes and identical total correct
counts, balanced accuracy was mathematically unchanged. This numerical issue is
recorded for a future verifier correction; it does not remove the separate
business/other regression or change the preserved rejection.

The 275- and 160-example final tests are now consumed and must not be reused for
training or candidate selection. The source archive requires private local inputs
to reproduce full experiments. Publishing this history does not deploy a model.

A subsequent [Jev-assisted training comparison](experiments/jev-distill/results-20261106.json)
used 480 training-only teacher requests and compared four Q8 candidates. On 263
calibration examples, the candidate with the most correct answers improved from
208/263 to 224/263, and confident mistakes decreased from 21 to 16. However, AI
misses increased from 19 to 20, business/other misses increased from 9 to 10, and
next-action retention fell from 106/138 to 104/138. Security misses fell from 11 to
2 while incorrect security assignments increased from 4 to 9. All four candidates
failed selection; the fresh synthetic final test remained unused. These calibration
results are not a Jev parity claim or results for the distributed weights. The new
selector uses a 1e-12 floating-point tolerance; earlier frozen verdicts remain intact.

The local `experiments/hermes-graph` workflow uses a read-only knowledge-graph
snapshot with 1,851 documents, 16,773 memory units and 406,019 stored relations,
plus source notes. Relations identify related examples; they are not truth labels.
After source grouping, visible-text annotation and exclusions, it adds 1,009
training examples, 276 calibration examples and 308 reserved final examples.
The source material and annotations remain private and have not been approved
for publication or independently adjudicated by people.

This experiment removes 321 repeated training rows. Each of the resulting 3,067
training examples is visited once per epoch, with half of the total loss allocated
equally among the four topic classes and half to six existing judgment tasks.
Multiple views of one source share its influence. Related, differently labelled
training sources receive a small boundary-learning weight increase. Calibration
uses 812 unweighted examples. New graph labels are predominantly AI/business;
only 20 development and 41 security training examples survived the quality checks.
Those limits matter when interpreting any later improvement.

The frozen comparison uses two epochs each of head-only and last-12-layer tuning,
with four Q8 exports. Selection checks both missed examples and incorrect category
assignments, alongside confident errors and retained judgments. Only a selected
candidate can enter the separate graph and reserved synthetic final tests. This
workflow neither installs weights nor publishes private data automatically.

All four candidates [failed the frozen selection criteria](experiments/hermes-graph/results-20261106.json).
On the same 459 topic-calibration examples, the candidate with the most correct
answers rose from 321/459 (69.9%) to 342/459 (74.5%); confident mistakes fell from
64 to 36. AI recall rose from 146/214 to 167/214, but incorrect AI assignments
increased from 44 to 51. Development recall fell from 47/62 to 45/62 and security
recall from 26/47 to 25/47. The candidate also lost one AI answer on the separate
legacy calibration cohort. Neither the graph final test nor the reserved synthetic
final test was run, and the final latency gate remains unmeasured. These results
do not establish Jev parity or describe the currently distributed weights.

The follow-up `experiments/hermes-boundary` workflow adds 140 clear training
examples: 102 development and 38 security. They come from unused technical
records and independently reviewed summaries of official documentation. Eight
ambiguous training examples were excluded. New calibration contains seven
development and eight security examples from separate public sources; private
operational records are training-only.

Nine pairs of short and long records described the same incident despite having
different source identifiers. Their learning weight is shared, with original text,
labels and split membership preserved. The resulting workload has 3,207 training
and 827 calibration rows. Two starting checkpoints—the deployed version and the
previous rejected graph candidate—receive identical data and training settings.
Starting from a rejected checkpoint does not approve it for installation. The
shared class/error gates and reserved final tests remain unchanged.

All four follow-up candidates [failed selection](experiments/hermes-boundary/results-20261106.json).
The continued-training epoch-2 candidate had the most correct answers: 369/474
(77.8%), versus 333/474 (70.3%) for the deployed model. AI recall increased from
146/214 to 174/214, development from 54/69 to 55/69, and security from 31/55 to
33/55. Its remaining relative-gate failure was incorrect AI assignments,
which increased from 45 to 49. On the unchanged 459-example portion, it scored
356/459 versus 342/459 for the previous rejected graph candidate; the 15 added
primary-source cases scored 13/15 versus 12/15 for the deployed model.

A separate input audit found references to the same claimed incident in five
prior training views and seven calibration views, despite different source URLs.
Source grouping therefore did not establish event-level independence. Frozen
labels, splits and verdicts were preserved; these calibration scores are not
independent generalization evidence. The 468 reserved final examples and final
latency gate remain unused, and the deployed weights remain unchanged.

The next `experiments/hermes-event` experiment removes 63 training examples after
input-only event, label and source-quality screening. Nine confirmed event groups
crossed training/calibration boundaries; several other summaries explicitly said
their source could not be retrieved and the details were reconstructed. Whole
training families are excluded conservatively, while earlier data, labels and
verdicts remain intact. Four retained views of two repeated training events share
learning weight. This leaves 3,144 training rows and the unchanged 827 calibration
rows. The audit is not exhaustive semantic deduplication or independent human
validation of all labels.

Training restarts from the accepted checkpoint before graph tuning and exports
four fixed epochs. A separate evaluation-only corpus contains 96 short Korean
summaries from verified public primary sources. Event splits were frozen before
a different assistant annotated the visible text: 48 calibration and 48 final
examples, each with 12 per category. The new calibration must preserve each
class's missed-example and incorrect-assignment counts in addition to all legacy
gates. Only a selected candidate can open the new final test and run its latency
gate. The earlier 468 reserved final examples remain unused in this experiment.

These new examples deliberately balance historical research, technical
documentation, vulnerabilities and corporate transactions; most business examples
are acquisitions. Results describe this small curated sample and do not establish
production feed or messenger accuracy. The single-seed experiment also cannot
isolate the effect of data cleanup from the changed training schedule.

The original four-epoch run was interrupted during epoch four when its measured
process footprint reached 35.8 GB on a 24 GiB machine. Three completed checkpoints
were preserved. A separately recorded recovery experiment adds one epoch from
the third checkpoint, with a new optimizer and scheduler; it is not an exact
resume of the original fourth epoch. Training uses microbatches of one with eight
accumulation steps, and calibration batches of one. MPS allocations are limited
to half the device's recommended memory, while a macOS process-footprint monitor
stops the owned process above 12 GiB. Actual over-limit rejection and under-limit
completion were checked before recovery. The bounded continuation completed in
721.5 seconds. Its maximum sampled process footprint was 7.50 GiB, and reported
MPS tensor memory returned to zero at shutdown. The cause of the original growth has
not been isolated; this result verifies the bounded run, not a general leak fix.

All four recovery candidates [failed selection](experiments/hermes-event/results-20261106.json).
The highest total was 368/474 (77.6%), versus 333/474 for the deployed model and
369/474 for the previous rejected boundary candidate. Compared with that previous
candidate, AI correct answers rose from 174 to 175, development fell from 55 to
52, security stayed at 33, and other rose from 107 to 108. Incorrect AI assignments
increased from 49 to 50, versus 45 for the deployed model. The final continuation
also lost too many next-action judgments under the existing retention limit.

All four candidates scored 38/48 on fresh calibration, versus 34/48 for the
deployed model. The highest-total candidate scored AI 10/12, development 10/12,
security 7/12 and other 11/12. Its confident errors rose from four to six, so the
new-cohort gate also failed. On these same short inputs, warm median latency was
24.1 ms versus 24.4 ms, and warm p95 was 25.0 ms versus 25.2 ms. These are one-pass
calibration measurements, not a completed final latency gate. The new 48-example
final and earlier 468 reserved examples remain unused. No model was installed or
published; 85% per-class accuracy and Jev parity remain unachieved.

The following [main-action contrast experiment](experiments/hermes-contrast/README.md)
adds 256 independently assistant-labelled synthetic examples from training-only
concepts. One bounded epoch updates the last four encoder layers and decision
head. Four predefined mixtures of the starting and newly trained weights export
to Q8, with no extra model at inference. All four
[failed selection](experiments/hermes-contrast/results-20261106.json): the highest
total was 365/474 (77.0%), below the preceding candidate's 368/474 (77.6%). AI
correct answers stayed at 175/214, development rose from 52 to 53/69, and security
stayed at 33/55, while incorrect AI assignments increased from 50 to 54. The two
highest-total mixtures matched the starting checkpoint's category counts.

Each candidate scored 38/48 on primary-source calibration but retained five
confident errors versus the deployed model's four. The 25% mixture's warm median
and p95 were 24.2 and 25.5 ms versus 25.0 and 26.7 ms for deployed; these are
single-pass calibration observations, not final speed-gate results. Training took
307.7 seconds with a maximum sampled process footprint of 5.89 GiB. A separate
receipt-only recovery handles unavailable empty-sample ECE without changing
weights, temperatures, data or gates. At the end of this experiment no candidate
had been applied or published. The user subsequently authorized `mix25-epoch-1`
as release `2026.11.06.1` despite the three preserved failures. All 516 reserved
final examples remained unopened.

## License and attribution

Apache License 2.0, following the [upstream model license](https://huggingface.co/convaiinnovations/laya-multilingual/blob/1720e3e3357cfe1e281542e223f8273b0890ca34/README.md). See `LICENSE` and `NOTICE`. Vica Laya is a modified derivative, not an official upstream Laya release.
