---
license: apache-2.0
pretty_name: 'GATC: Agentic Coding Sessions'
language:
- en
- zh
- ja
- ru
- ko
- es
- vi
- pt
- fr
- uk
- de
- fa
size_categories:
- 1K<n<10K
task_categories:
- text-generation
tags:
- code
- agent
- coding-agent
- coding-sessions
- agent-traces
- tool-use
- trajectories
- sft
- function-calling
- reasoning
configs:
- config_name: messages
  default: true
  data_files:
  - split: train
    path: sample/messages/messages.jsonl.zst
- config_name: trajectories
  data_files:
  - split: train
    path: sample/trajectories/trajectories.jsonl.zst
- config_name: sft_steps
  data_files:
  - split: train
    path: sample/views/sft_steps.jsonl.zst
- config_name: error_recovery
  data_files:
  - split: train
    path: sample/views/error_recovery.jsonl.zst
- config_name: labels
  data_files:
  - split: train
    path: sample/labels/labels.jsonl.zst
- config_name: tool_grammar
  data_files:
  - split: train
    path: sample/views/tool_grammar.jsonl.zst
dataset_info:
- config_name: messages
  features:
  - name: trajectory_id
    dtype: string
  - name: models
    list: string
  - name: n_steps
    dtype: int64
  - name: task_type
    dtype: string
  - name: session_kind
    dtype: string
  - name: is_eval
    dtype: bool
  - name: eval_kind
    dtype: string
  - name: template_group
    dtype: string
  - name: template_group_size
    dtype: int64
  - name: parent_trajectory_id
    dtype: string
  - name: prompt_language
    dtype: string
  - name: last_test_result
    dtype: string
  - name: git_commit_made
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
    - name: is_wrapper
      dtype: bool
    - name: tool_calls
      list:
      - name: id
        dtype: string
      - name: type
        dtype: string
      - name: function
        struct:
        - name: name
          dtype: string
        - name: arguments
          dtype: string
    - name: tool_call_id
      dtype: string
    - name: reasoning_content
      dtype: string
  - name: tools
    dtype: string
  - name: ft_issues
    list: string
  - name: repo_id
    dtype: string
  - name: actor_id
    dtype: string
  - name: repo
    dtype: string
- config_name: trajectories
  features:
  - name: trajectory_id
    dtype: string
  - name: models
    list: string
  - name: actor_id
    dtype: string
  - name: repo_id
    dtype: string
  - name: started_at
    dtype: string
  - name: duration_s
    dtype: float64
  - name: n_steps
    dtype: int64
  - name: n_tool_calls
    dtype: int64
  - name: n_errors
    dtype: int64
  - name: task_type
    dtype: string
  - name: session_kind
    dtype: string
  - name: is_eval
    dtype: bool
  - name: eval_kind
    dtype: string
  - name: template_group
    dtype: string
  - name: template_group_size
    dtype: int64
  - name: parent_trajectory_id
    dtype: string
  - name: prompt_language
    dtype: string
  - name: last_test_result
    dtype: string
  - name: git_commit_made
    dtype: bool
  - name: tokens
    struct:
    - name: input
      dtype: int64
    - name: output
      dtype: int64
    - name: total
      dtype: int64
    - name: cache_read
      dtype: int64
    - name: cache_write
      dtype: int64
  - name: redaction
    struct:
    - name: n
      dtype: int64
  - name: steps
    list:
    - name: i
      dtype: int64
    - name: type
      dtype: string
    - name: text
      dtype: string
    - name: ts
      dtype: string
    - name: is_wrapper
      dtype: bool
    - name: tool
      dtype: string
    - name: tool_raw
      dtype: string
    - name: tool_class
      dtype: string
    - name: args
      dtype: string
    - name: result
      dtype: string
    - name: ok
      dtype: bool
    - name: duration_ms
      dtype: float64
    - name: mcp_server
      dtype: string
    - name: model
      dtype: string
    - name: out_tokens
      dtype: int64
    - name: thinking
      dtype: bool
  - name: repo
    dtype: string
  - name: schema_version
    dtype: string
- config_name: sft_steps
  features:
  - name: trajectory_id
    dtype: string
  - name: i
    dtype: int64
  - name: context
    list:
    - name: type
      dtype: string
    - name: text
      dtype: string
  - name: tool
    dtype: string
  - name: tool_raw
    dtype: string
  - name: args
    dtype: string
  - name: ok
    dtype: bool
  - name: result
    dtype: string
  - name: repo_id
    dtype: string
  - name: actor_id
    dtype: string
  - name: repo
    dtype: string
- config_name: error_recovery
  features:
  - name: trajectory_id
    dtype: string
  - name: failed_tool
    dtype: string
  - name: args
    dtype: string
  - name: error
    dtype: string
  - name: recovery
    list:
    - name: type
      dtype: string
    - name: tool
      dtype: string
    - name: text
      dtype: string
  - name: recovered
    dtype: bool
  - name: recovery_kind
    dtype: string
  - name: repo_id
    dtype: string
  - name: actor_id
    dtype: string
  - name: repo
    dtype: string
- config_name: labels
  features:
  - name: trajectory_id
    dtype: string
  - name: n_steps
    dtype: int64
  - name: task_type
    dtype: string
  - name: session_kind
    dtype: string
  - name: is_eval
    dtype: bool
  - name: eval_kind
    dtype: string
  - name: template_group
    dtype: string
  - name: template_group_size
    dtype: int64
  - name: parent_trajectory_id
    dtype: string
  - name: prompt_language
    dtype: string
  - name: last_test_result
    dtype: string
  - name: git_commit_made
    dtype: bool
  - name: modified_files
    list: string
  - name: key_tools
    list: string
  - name: metrics
    struct:
    - name: span_count
      dtype: int64
    - name: llm_span_count
      dtype: int64
    - name: tool_call_count
      dtype: int64
    - name: error_count
      dtype: int64
    - name: error_rate
      dtype: float64
    - name: user_turn_count
      dtype: int64
    - name: distinct_files_touched
      dtype: int64
    - name: distinct_models
      list: string
  - name: repo_id
    dtype: string
  - name: actor_id
    dtype: string
  - name: repo
    dtype: string
- config_name: tool_grammar
  features:
  - name: tool
    dtype: string
  - name: calls
    dtype: int64
  - name: sessions
    dtype: int64
  - name: errors
    dtype: int64
  - name: error_rate
    dtype: float64
---

# GATC: Agentic Coding Sessions

Recorded sessions of AI coding agents at work, step by step.

- **Website:** [goat.ai](https://goat.ai)
- **Full dataset and licensing:** [goat.ai/contact](https://goat.ai/contact)
- **Email:** [yerbol@goat.ai](mailto:yerbol@goat.ai)

> **This repository is a 1% sample.** It holds **1,189 sessions**, drawn uniformly at random from the 106,012 complete
> sessions of the full dataset of **117,796 sessions** (complete: at least one user prompt and at least one assistant message;
> see *Sampling*). The figures on this page describe the full dataset unless a line says *this
> repository*. The full dataset has the same tables in the same format (JSONL, zstd-compressed).

## At a Glance

- **What it is.** 117,796 sessions, each kept whole and in order, de-identified and scanned before release.
- **Who drove them.** About 41,000 sessions are interactive (see *Dataset Summary*). `session_kind` marks 21,298 of them where the
  evidence is clear.
- **Ready to filter.** `is_eval` flags 35,565 sessions of prepared evaluation tasks; `template_group_size`
  counts the sessions that open with the same prompt; `is_wrapper` marks wrapper text (command output, notifications)
  among user messages.
- **Ready to train.** `messages` keeps each assistant turn's text, reasoning and tool call together, with arguments mapped onto a per-tool schema (86.8% of calls), and each
  session carries the schemas of its tools in `tools`; 72,329 sessions have no `ft_issues`.
- **Facts about outcomes.** 14,368 sessions record a test runner's last verdict (`last_test_result`:
  11,939 passed, 2,429 failed) and 12,734 a commit that git
  confirmed (`git_commit_made`). These are records of what the tools printed, not success labels.
- **AI agents evaluating this dataset:** start with [AGENTS.md](AGENTS.md): what the files hold, how to load them and
  check the main counts of this repository, and which features are design choices rather than
  defects.

## Dataset Summary

GATC (GOAT AI Trajectory Corpus) is a dataset of recorded sessions of AI coding agents working on software tasks, collected,
curated and de-identified by GOAT labs. Each session keeps the whole run in order: the user's messages, the agent's
replies, every tool call with its arguments and, where the agent recorded one, its result, and the failed tool calls
together with what the agent did next. Reasoning and token counts are included where the agent logged them.

About 41,000 of the 117,796 sessions are interactive: a person typed the prompts for their own work. They run long, so
they hold about two-thirds of all steps and tool calls. The other sessions are agent runs on tasks that a script or
another agent gave: evaluations, prepared tasks, exercises, batch jobs and sub-agents (see *Composition*).

### Dataset Size

| Count | Full dataset | This repository (1%) |
|---|---:|---:|
| `trajectories` (sessions) | 117,796 | 1,189 |
| steps | 9,704,911 | 92,365 |
| user prompts (user messages that are not wrapper text) | 528,861 | 5,269 |
| `messages` | 117,796 | 1,189 |
| `sft_steps` (tool calls) | 5,751,020 | 52,617 |
| `error_recovery` (failed tool calls) | 240,957 | 2,028 |
| `labels` | 117,796 | 1,189 |
| `tool_grammar` (tool names) | 17 | 17 |

### Composition

Interactive sessions, in which a person typed the prompts for their own work, are about 35% of all sessions (95%
interval 32–38%), and they hold most of the data:

| | Full dataset | In interactive sessions (estimate) |
|---|---:|---:|
| Sessions | 117,796 | about 41,000 (35%) |
| Steps | 9,704,911 | about two-thirds (68%; 95% interval 66–70%) |
| Tool calls | 5,751,020 | about two-thirds (68%) |

How this was measured: a language model reviewed a stratified sample of 360 sessions blind, in two passes that agreed
on 96% of them, and the shares were weighted to the full dataset. Two checks that use no model point the same way:
traces that only a person at the keyboard leaves, such as an interrupted reply, and the start mode that the agent
tools themselves recorded. In this repository, about 475 of the 1,189 sessions are interactive (40%; higher than the
full dataset's 35% because the sample is drawn from complete sessions only); the `session_kind` field marks 249
sessions `interactive`, those where the evidence is clear (see *Taxonomy*).

### Highlights

* **Session length.** One in ten sessions has 166 steps or more and the longest has 36,656; the median is 26. One in
  ten lasts 1.6 hours or more (91,950 sessions record a duration).
* **Multi-turn sessions.** 38.1% of sessions hold two or more user prompts; 528,861 prompts in all. Wrapper messages (command output, notifications, interruption markers) are not counted.
* **Tool use.** 5,751,020 tool calls. Shell commands are 53.7% of them, reading files 15.0%, editing files 11.8%; 92,815 calls go to MCP servers, 99,372 hand work to a sub-agent and 14,318 invoke a skill.
* **Failures are kept.** 240,957 tool calls are recorded as failed (one in 24) and stay in place with the steps that
  followed; 12.5% of calls have no recorded status (`ok` is null; 61.8% of them still hold a result) and are not counted as failed. In 85.5% of the failures a
  `tool_call` or `retrieval` step within the next four steps succeeded (the `recovered` flag; it does not check that
  the later call fixed the failure).
* **Evaluation runs flagged.** 35,565 sessions (30.2%) are prepared evaluation
  tasks (`is_eval`, `eval_kind`): question batteries 12,569, repository tasks 8,336, terminal tasks 7,902, exercises 4,721, other evaluations 2,037. 46,871 sessions open with a prompt that ten or more
  sessions of the full dataset share (`template_group_size`).
* **Languages.** First prompts by language (`prompt_language`): English 87,208, Chinese 4,393, Japanese 2,022, Russian 646, Korean 505, Spanish 437, Vietnamese 338, Portuguese 232; 21,133 sessions
  have too little prose to tell.
* **Sub-agents linked.** 4,296 of the 17,089 sub-agent sessions name the session that started
  them (`parent_trajectory_id`).
* **Reasoning recorded.** 571,504 reasoning steps across 26,107 sessions.
* **Token accounting.** Token counts as the agents reported them: 120.9B input tokens (reported by 95,759 sessions),
  543.5B cache-read (81,346), 10.8B cache-write (58,939) and 1.8B output (95,752). Input and cache counts may be
  sums over model calls, so a context sent again on every call may be counted every time. Half of the sessions that
  report output tokens generated 2,355 or more.
* **Breadth.** 3,939 projects from 3,011 owners (pseudonyms; 10,362 sessions with no recorded owner or project carry `user0` and `repo0`). 60,389 sessions record the files they read, wrote or edited, 551,122 in all (each file counted once per session).
* **Time span.** 99% of the sessions with a start time began between February 2025 and September 2026; the latest on
  22 September 2026.
* **Model tiers.** Sessions by the highest capability tier of the models they used: Tier S 4,887, Tier A 53,852,
  Tier B 25,450, Tier C 13,131, Tier D 5,061 (102,381 sessions use a model with a tier).

### Token and Turn Statistics

Full dataset, by whether a session holds reasoning steps, and by the highest model tier a session used.

| Metric | All sessions | With reasoning steps | Without reasoning steps |
|---|---:|---:|---:|
| Sessions | 117,796 | 26,107 | 91,689 |
| Steps | 9,704,911 | 2,925,556 | 6,779,355 |
| Assistant messages | 3,321,174 | 1,217,837 | 2,103,337 |
| Tool calls | 5,751,020 | 1,536,393 | 4,214,627 |
| Failed tool calls (share of calls) | 240,957 (4.2%) | 71,991 (4.7%) | 168,966 (4.0%) |
| Reasoning steps | 571,504 | 571,504 | 0 |
| Steps per session, mean (median) | 82.4 (26) | 112.1 (35) | 73.9 (23) |
| Assistant messages per session, mean | 28.2 | 46.6 | 22.9 |
| Assistant replies per session (reasoning steps excluded), mean | 23.3 | 24.8 | 22.9 |
| Tool calls per session, mean | 48.8 | 58.8 | 46.0 |
| User prompts per session, mean | 4.5 | 5.4 | 4.2 |
| Sessions that report output tokens | 95,752 | 22,385 | 73,367 |
| Output tokens, total (those sessions) | 1.78B | 296.2M | 1.48B |
| Output tokens per session, mean (median) | 18,587 (2,355) | 13,231 (1,974) | 20,221 (2,468) |
| Output tokens per assistant message or tool call (ratio of totals) | 240.5 | 135.3 | 284.7 |

| Metric | Tier S | Tier A | Tier B | Tier C | Tier D |
|---|---:|---:|---:|---:|---:|
| Sessions | 4,887 | 53,852 | 25,450 | 13,131 | 5,061 |
| Steps | 471,757 | 5,526,735 | 1,944,092 | 592,867 | 195,101 |
| Assistant messages | 138,502 | 1,696,729 | 779,298 | 254,406 | 79,243 |
| Tool calls | 293,623 | 3,511,065 | 1,042,395 | 308,947 | 103,525 |
| Failed tool calls (share of calls) | 9,640 (3.3%) | 117,982 (3.4%) | 70,338 (6.7%) | 27,774 (9.0%) | 1,736 (1.7%) |
| Reasoning steps | 43,841 | 312,982 | 118,247 | 33,704 | 100 |
| Steps per session, mean (median) | 96.5 (23) | 102.6 (25) | 76.4 (32) | 45.2 (25) | 38.5 (28) |
| Assistant messages per session, mean | 28.3 | 31.5 | 30.6 | 19.4 | 15.7 |
| Assistant replies per session (reasoning steps excluded), mean | 19.4 | 25.7 | 26.0 | 16.8 | 15.6 |
| Tool calls per session, mean | 60.1 | 65.2 | 41.0 | 23.5 | 20.5 |
| User prompts per session, mean | 5.5 | 4.7 | 4.1 | 2.1 | 2.4 |
| Sessions that report output tokens | 4,704 | 50,606 | 21,598 | 11,990 | 4,603 |
| Output tokens, total (those sessions) | 197.2M | 1.11B | 306.3M | 60.2M | 50.0M |
| Output tokens per session, mean (median) | 41,913 (2,976) | 21,959 (2,040) | 14,182 (2,702) | 5,024 (1,429) | 10,858 (6,500) |
| Output tokens per assistant message or tool call (ratio of totals) | 473.5 | 241.0 | 203.9 | 120.5 | 291.8 |

*Steps* are all user messages, assistant messages and tool calls; an *assistant message* is an assistant step, a reply
or a reasoning step, and a *tool call* is a step of type `tool_call`, `retrieval` or `subagent`. *Output tokens* are
the counts the agent reported for the session; the token rows cover only the sessions that report them. The tier
columns hold the sessions that used a model with a tier (102,381 of 117,796); a session counts under the highest tier
it used.

### Comparison with Other Datasets

How the release compares with the public datasets most similar to it: datasets that include sessions of people working
with coding agents. Every cell was checked twice against each dataset's card, files or paper (October 2026); the second
check was blind. ✓ means in most sessions, partial means partly or in a minority of sessions, ✗ means no. The Size
column says what kind of session each dataset holds.

| Dataset | Size | Tool-use trajectories | Failed calls labelled, with a recovery flag | Reasoning steps | Token counts | Code changes | Scanned before release⁸ |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|
| [SWE-chat](https://huggingface.co/datasets/SALT-NLP/SWE-chat) (Baumann et al., 2026) | 17,968 developer sessions | ✓ | partial¹ | partial | ✓ | ✓ | partial |
| [ACT-2.5B](https://huggingface.co/datasets/submit2331/ACT-2.5B) (anonymous, 2026) | 183 developer sessions public (26,999 announced) | ✓ | partial¹ | ✓ | ✗ | ✓ | ✓ |
| [AgentLogs](https://huggingface.co/datasets/risenlab/agentlogs) (Richards et al., 2026) | 635,886 sessions of one agent working alone on tasks given through GitHub | ✓ | partial¹ | partial | ✓ | partial² | ✗ |
| **GATC** (this dataset) | **117,796 sessions**: about 41,000 interactive³, the rest autonomous agent runs | ✓ | ✓⁴ | partial⁵ | ✓⁶ | ✓⁷ | ✓ |

¹ Failed calls carry a per-call label but no recovery flag (AgentLogs: in about 1% of sessions).

² Line counts and commit ids, not the changes themselves.

³ A person typed the prompts for their own work; see *Composition*.

⁴ Computed by us: a `tool_call` or `retrieval` step within the next four steps succeeded; it does not check that the
later call fixed the failure.

⁵ 26,107 sessions (22%) hold reasoning steps.

⁶ Reported by 95,759 sessions (81%).

⁷ Edit and write calls carry the change itself (old and new text, the whole file, or the patch the agent applied) where it was recorded: 79.7% of them hold it in normalised form in `messages`, 10.5% keep a shape no rule maps, and 9.7% recorded only the file path or nothing; there is no separate per-session diff or commit.

⁸ A scan of the released files with its result stated (for this dataset, see *Release Gate*); partial means that
redaction tools are named but no result is stated.

Datasets of real sessions can overlap: some sessions appear in more than one of them, GATC included, so sizes do not
add up. Session counts are as each dataset's card reports them. Datasets of agents run only on prepared tasks (such as
NVIDIA's Open-SWE-Traces), of pull requests that agents opened, or of chats with an assistant are not listed.

### Tables

| Table | Description | Key |
|---|---|---|
| **messages** | Each session in the chat-message format, built for training: an assistant turn holds its text, its reasoning and at most one tool call with arguments mapped onto the tool's schema; the session's tool schemas in `tools` | `trajectory_id` |
| **trajectories** | Each session step by step, with arguments, results, timing and the answering model's tier | `trajectory_id` |
| **sft_steps** | One row per tool call with the steps before it (shortened) and the call's result; the full history is in `trajectories` | (`trajectory_id`, `i`) |
| **error_recovery** | One row per failed tool call: the error, the next steps, whether a `tool_call` or `retrieval` step among them succeeded, and which (`recovery_kind`) | — (several rows per session; joins on `trajectory_id`) |
| **labels** | One row per session: step count, task type, session kind, evaluation flag, template group, language, test and commit facts, key tools, files touched, metrics | `trajectory_id` |
| **tool_grammar** | One row per normalised tool: calls, sessions, failed calls | `tool` |

## Loading the Data

```python
from datasets import load_dataset

# each table is a named config
messages = load_dataset("GOAT-AI/gatcv6", "messages", split="train")
trajectories = load_dataset("GOAT-AI/gatcv6", "trajectories", split="train")
sft_steps = load_dataset("GOAT-AI/gatcv6", "sft_steps", split="train")
errors = load_dataset("GOAT-AI/gatcv6", "error_recovery", split="train")
labels = load_dataset("GOAT-AI/gatcv6", "labels", split="train")
```

Each config declares its features, so `load_dataset` and the viewer read every column. The dataset viewer on this page shortens long cells and marks the cut with `...TRUNCATED`; the files hold every
session in full (405 of the 1,189 `messages` rows are longer than 100,000 characters). 69 tool results in this repository contain `[TRUNCATED]`: the output was already cut there when it was recorded.

### Quick Examples

```python
# the first user message of a session
first_message = next(m["content"] for m in messages[0]["messages"] if m["role"] == "user")

# sessions in which the agent called a write or edit tool
implementation = messages.filter(lambda r: r["task_type"] == "implementation")

# failed tool calls followed by a successful call within four steps
recovered = errors.filter(lambda r: r["recovered"])

# every shell-tool call with its result (`messages` names these `bash`, `exec`, `bash_input`, …)
shell = sft_steps.filter(lambda r: r["tool"] == "bash")

# long sessions (100 steps or more)
long_sessions = labels.filter(lambda r: r["n_steps"] >= 100)

# sessions in which a person typed the prompts (where the evidence is clear)
interactive = messages.filter(lambda r: r["session_kind"] == "interactive")

# drop prepared evaluation tasks and rows with anything listed in ft_issues
train = messages.filter(lambda r: not r["is_eval"] and not r["ft_issues"])

# sessions whose last test run passed
tests_passed = labels.filter(lambda r: r["last_test_result"] == "passed")

# the agent's recorded reasoning, in the first session that has any
session = next(t for t in trajectories if any(s.get("thinking") for s in t["steps"]))
reasoning = [s["text"] for s in session["steps"] if s.get("thinking")]
```

### Fine-tuning

`messages` follows the chat format of tool-calling models. `arguments` and `tools` are JSON strings (one Arrow column
cannot hold tool schemas that differ between sessions), so parse them before a chat template sees them:

```python
import json
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(MODEL)  # MODEL: the tool-calling model you fine-tune

def chat(row):
    msgs = []
    for m in row["messages"]:
        m = {k: v for k, v in m.items() if v is not None and k != "is_wrapper"}
        if m.get("tool_calls"):
            m["tool_calls"] = [{**tc, "function": {**tc["function"], "arguments": json.loads(tc["function"]["arguments"])}}
                               for tc in m["tool_calls"]]
        msgs.append(m)
    return msgs, json.loads(row["tools"])

msgs, tools = chat(messages[0])
text = tokenizer.apply_chat_template(msgs, tools=tools, tokenize=False)
```

Every session of this repository renders without error through the chat templates of two open tool-calling model families. Sessions are long: rendered with one of them, the median session is 15,389 tokens, and 355 sessions are over 32,768 (89 over 131,072); split or window long sessions to fit a context length. Chat templates differ in what they keep of `reasoning_content`: in this check one family's kept it for 33.2% of the turns that have it and the other's for none.

## Taxonomy

**Task type** (`task_type`, from the tools a session called; the rules apply in this order)

| `task_type` | Rule | Sessions |
|---|---|---:|
| `implementation` | a write or edit tool was called | 54,212 |
| `exploration` | otherwise, a read, grep, glob, list, web search or web fetch tool was called | 22,616 |
| `conversation` | otherwise, with at least one assistant message (shell commands may still run) | 38,665 |

The remaining 2,303 sessions (2.0%) have no assistant message; their `task_type` is `unknown`.

**Session length** (`n_steps`, the exact number of steps)

| Steps | Sessions |
|---|---:|
| 300 or more | 5,842 |
| 100–299 | 14,912 |
| 20–99 | 47,247 |
| fewer than 20 | 49,795 |

**Session kind** (`session_kind`, from evidence in the session itself)

| `session_kind` | Meaning | Sessions |
|---|---|---:|
| `interactive` | a person typed the prompts during the session | 21,298 |
| `autonomous` | no person typed the prompts: a script or a program, which can be another agent, started the session and gave the task | 46,513 |
| `sub-agent` | the transcript of a sub-agent, recorded by the agent tool as started by another agent; its prompt can quote the person's request | 17,089 |
| `unknown` | too little evidence either way | 32,896 |

The evidence is the start mode the agent tool recorded (an interactive interface or a program), traces that only a
person at the keyboard leaves (an interrupted reply, a refused tool permission, a slash command), the time a person
took before the next prompt, task prompts that recur across owners, and known evaluation runs. A language model
reviewed 1,224 sessions blind, in four review sets (the 360 of *Composition* among them), and judged whether a person
typed the prompts. Of the reviewed sessions marked `interactive`, 98% (345 of 352) were judged person-prompted; of
those marked `autonomous`, 97% (263 of 270) were judged not. The rules were chosen on these same reviews, so on other
sessions the agreement is likely somewhat lower. A session is marked only where the evidence is clear, so the field
marks 21,298 of an estimated 41,000 interactive sessions; most of the others are among the 32,896 `unknown`, about
half of which are interactive.

**Evaluation tasks** (`is_eval`, `eval_kind`)

| `eval_kind` | Sessions |
|---|---:|
| `qa-battery` | 12,569 |
| `repository-task` | 8,336 |
| `terminal-task` | 7,902 |
| `exercise` | 4,721 |
| `other-eval` | 2,037 |

A session is flagged when its first prompt carries a marker of a prepared evaluation task, or when it opens like a
template that a review classed as an evaluation: the 500 largest groups of identical openings were reviewed by a language model, those ranked 151 to 500
twice and independently, both verdicts having to agree. In a blind check of 78 sessions of this repository, drawn by
stratum, all 50 flagged sessions were evaluation tasks and 7 evaluation tasks were not flagged; a one-off task with no
marker stays unflagged. The markers were refined on this check, so on other sessions recall may be lower.

**Template groups** (`template_group`, `template_group_size`). Sessions of the full dataset whose first prompt opens with the same 160
characters (letter case, digits and placeholder numbers ignored; openings of 32 characters or more) share a group; the
size counts them. Scripted runs repeat their opening; people rarely do.

**Prompt language** (`prompt_language`, ISO 639-1), detected on the first prompt after code, paths and URLs are cut;
null when too little prose is left.

**Model tier** (`models` per session, `model` per assistant step). Each model is shown as a capability tier: `Tier S`
frontier flagship models, `Tier A` frontier models, `Tier B` workhorse models, `Tier C` small and fast models, `Tier D`
legacy models (earlier generations). Model names in the text are replaced by `<MODEL_A>`, `<MODEL_B>`…; a model family name without a version, or one that is also an everyday word, can remain.

## Dataset Schema

The schema of the files in this repository; the full dataset has the same tables, with a few more columns.

### Relationship Map

```
trajectories (1) ──> (1) messages          [trajectory_id]
trajectories (1) ──> (1) labels            [trajectory_id]
trajectories (1) ──> (N) sft_steps         [trajectory_id; i = the step's index in trajectories.steps]
trajectories (1) ──> (N) error_recovery    [trajectory_id]
tool_grammar: one row per normalised tool, counted over the whole repository
```

### ID Strategy

| Entity | Key | Format | Notes |
|---|---|---|---|
| Session | `trajectory_id` | 24 hex characters | a keyed hash; it cannot be turned back into the session's earlier id |
| Owner | `actor_id` | `user<n>` | pseudonym of the project's owner, the same in every session of that owner; `user0`, with `repo_id` `repo0`, where no owner or project was recorded |
| Project | `repo_id` | `repo<n>` | pseudonym, the same for every session of one project |
| Project path | `repo` | `user<n>/repo<n>` | owner and project pseudonyms |
| Step | `i` | integer | 0-based position in `trajectories.steps` |

---

### 1. `trajectories`

| Column | Type | Description |
|---|---|---|
| `trajectory_id` | string | **PK** |
| `models` | list[string] | the capability tiers of the models the session used; empty when no model was recorded (127 sessions here) |
| `actor_id`, `repo_id`, `repo` | string | pseudonyms (see ID Strategy) |
| `started_at` | timestamp | session start, UTC (written without a zone suffix); null when not recorded (111 sessions here); in the full dataset a missing start is an empty string, and a few sessions hold a 1969 or 1970 placeholder date |
| `duration_s` | number | session duration in seconds; 0 when not recorded |
| `n_steps`, `n_tool_calls`, `n_errors` | int | steps, tool calls, failed tool calls |
| `task_type` | string | see Taxonomy |
| `session_kind` | string | `interactive`, `autonomous`, `sub-agent` or `unknown` (see Taxonomy) |
| `is_eval`, `eval_kind` | bool, string | a prepared evaluation task, and its kind (see Taxonomy); null kind when false |
| `template_group`, `template_group_size` | string, int | the group of sessions of the full dataset that open the same way, and its size; null and 1 for a unique opening, null and null for a short one or none |
| `parent_trajectory_id` | string | a sub-agent session's parent: its sub-agent call's prompt equals this session's first message (placeholder numbers aside), same owner; null otherwise (it can name a session outside this repository) |
| `prompt_language` | string | ISO 639-1 language of the first prompt; null when too little prose |
| `last_test_result` | string | `passed` or `failed`: the last call that ran a test runner, read from the runner's summary; null when none ran or it cannot be read |
| `git_commit_made` | bool | a `git commit` call that git confirmed |
| `tokens` | object | token counts the agent reported: `input`, `output`, `total`, `cache_read`, `cache_write`; null or 0 when not reported |
| `redaction` | object | `n`: placeholders in the session |
| `steps` | list[object] | the session, step by step (below) |
| `schema_version` | string | `gatc-v0.5` |

**Steps** (`trajectories.steps[]`)

| Field | Type | Description |
|---|---|---|
| `i` | int | 0-based step index |
| `type` | string | `user`, `assistant`, `tool_call`, `retrieval` (read, search, fetch), `subagent` (work handed to a sub-agent) |
| `text` | string | user or assistant text |
| `is_wrapper` | bool | user steps: wrapper text (command output, notifications, interruption markers), not a prompt |
| `model` | string | assistant steps: the answering model's tier; null when no model was recorded (2,244 of 33,721 assistant steps here) |
| `thinking` | bool | true on a reasoning step |
| `out_tokens` | int | assistant output tokens |
| `tool` | string | normalised tool name (`bash`, `read`, `edit`, `grep`, `write`, `mcp`, …); `other` for a tool outside the vocabulary, whose own name is in `tool_raw` |
| `tool_raw` | string | the tool name as the agent called it; in some sessions it repeats `tool` |
| `tool_class` | string | `builtin`, `mcp`, `skill`, `task`, `other` |
| `mcp_server` | string | for MCP tools, the server name |
| `args` | string | the call's arguments as the agent recorded them (usually a JSON object; the shape differs between agents); the normalised form is in `messages` |
| `result` | string | the call's result, where one was recorded |
| `ok` | bool | true or false as recorded; null when the recording kept no status (the call can still have a result) |
| `duration_ms` | number | call duration in milliseconds |
| `ts` | string | step time, ISO 8601, as recorded; not always increasing within a session |

### 2. `messages`

| Column | Type | Description |
|---|---|---|
| `trajectory_id` | string | **PK**, FK -> trajectories |
| `messages` | list[object] | `role` (`user`, `assistant`, `tool`), `content`, `is_wrapper` (user), `reasoning_content` (assistant: the reasoning recorded before the turn), `tool_calls` (`id`, `type`, `function`: `name`, `arguments` as a JSON string), `tool_call_id` |
| `tools` | string | JSON list of the schemas of the tools the session called |
| `ft_issues` | list[string] | what makes the row harder to train on: `starts_without_user`, `ends_without_answer`, `incomplete_tool_args`, `unnormalized_tool_args`, `withheld_text` |
| `models`, `n_steps`, `task_type`, `session_kind`, `is_eval` … `git_commit_made` | | as in `trajectories` |
| `actor_id`, `repo_id`, `repo` | string | pseudonyms |

`ft_issues` values: `starts_without_user`, the first message is not the user's; `ends_without_answer`, the last
message is not an assistant reply with text (it is a tool result, a user message, a tool call, or a turn that holds
only reasoning); `incomplete_tool_args`, a call recorded no usable arguments (none, only a summary of them, or an edit
or write call that recorded only its file path); `unnormalized_tool_args`, a call of a known tool kept its recorded
arguments because no rule maps them safely (calls of MCP and unknown tools keep theirs without this flag);
`withheld_text`, the row holds `<WITHHELD>`. A function name names the schema a call was mapped to: usually its
normalised tool, or a more specific name where one tool has several argument shapes (for example `exec` and
`bash_input` for shell calls, `apply_patch` and `multi_edit` for edits, `task_create` and `task_update` for task
lists); `tools` holds the schema of each name, and `sft_steps.tool` keeps the normalised tool. For MCP and unknown
tools the name is the recorded one with every character a function name does not allow replaced by `_` (at most 64
characters), so a placeholder in it has no angle brackets (`MODEL_B`).

### 3. `sft_steps`

| Column | Type | Description |
|---|---|---|
| `trajectory_id` | string | FK -> trajectories |
| `i` | int | index of the tool-call step in `trajectories.steps` |
| `context` | list[object] | the up to 12 steps before the call (`type`, `text`; each text cut to about 600 characters; a tool step's text is its tool name) |
| `tool`, `tool_raw` | string | normalised and raw tool name (as in `trajectories`) |
| `args` | string | the call's arguments, as in `trajectories` |
| `result` | string | the call's result, cut to about 4,000 characters (the full result is in `trajectories`) |
| `ok` | bool | as in `trajectories` |
| `actor_id`, `repo_id`, `repo` | string | pseudonyms |

Texts are cut before the last de-identification pass, so a placeholder added later can make a cut text slightly longer.

### 4. `error_recovery`

| Column | Type | Description |
|---|---|---|
| `trajectory_id` | string | FK -> trajectories |
| `failed_tool` | string | normalised name of the tool that failed |
| `args` | string | the failed call's arguments, as in `trajectories` |
| `error` | string | its result, cut to about 4,000 characters |
| `recovery` | list[object] | the next up to 4 steps (`type`, `tool`, `text` cut to about 800 characters) |
| `recovered` | bool | true when one of those steps is a `tool_call` or `retrieval` step that succeeded; it does not check that the failure was fixed |
| `recovery_kind` | string | the first later step that succeeded: `same_tool_new_args`, `same_call_retried`, `other_tool`, or `none` |
| `actor_id`, `repo_id`, `repo` | string | pseudonyms |

### 5. `labels`

| Column | Type | Description |
|---|---|---|
| `trajectory_id` | string | **PK**, FK -> trajectories |
| `n_steps` | int | steps (the same as `trajectories.n_steps`) |
| `task_type` | string | as in `trajectories` |
| `session_kind` | string | as in `trajectories` |
| `is_eval` … `git_commit_made` | | the per-session facts, as in `trajectories` |
| `modified_files` | list[string] | files the agent read, wrote or edited (de-identified paths, up to 100) |
| `key_tools` | list[string] | the session's most used tools (up to 8) |
| `metrics` | object | `span_count` (steps), `llm_span_count` (assistant steps), `tool_call_count`, `error_count`, `error_rate`, `user_turn_count` (user messages, wrapper messages included), `distinct_files_touched` (all distinct files; `modified_files` lists up to 100), `distinct_models` (tiers) |
| `actor_id`, `repo_id`, `repo` | string | pseudonyms |

### 6. `tool_grammar`

| Column | Type | Description |
|---|---|---|
| `tool` | string | **PK**, normalised tool name |
| `calls`, `sessions`, `errors` | int | calls, sessions that used it, failed calls |
| `error_rate` | number | errors / calls |

## Data Preparation

### Normalisation

Every session is normalised into one schema whatever agent recorded it: steps in order, tool names mapped to a closed
vocabulary, timing and token counts. In v3, tool names the earlier mapping left as `other` were mapped to their tool (90,216 calls of the full dataset), and vendor names left in raw tool names were masked as in the rest of the text (`vendor_a`, `vendor_b` and so on; 576 names). The training form of `messages` maps the arguments of each known tool onto that tool's schema by the recorded parameter names. It drops some agent-specific options and adds no value that was not recorded; values stay as recorded, except that a URL-encoded path is decoded, a recorded line range becomes `offset` and `limit`, a timeout in seconds becomes milliseconds and a command recorded as a list of words becomes one string. `trajectories`, `sft_steps` and `error_recovery` keep every call's arguments exactly as the agent recorded them. `tool` takes 17 values in the full dataset; a tool outside them is `other`, and its own name is in `tool_raw`.

### De-identification

People's names are replaced where the redactor finds them in an account, author or contact field, and then everywhere
in that session; accounts, organisations, e-mail addresses, phone numbers, postal and network addresses and card
numbers are replaced by typed placeholders stable within a session (`<USER_n>`, `<USERNAME_n>`, `<NAME_n>`,
`<PERSON_n>`, `<ORG_n>`, `<REPO_n>`, `<EMAIL_n>`, `<PHONE_n>`, `<ADDRESS_n>`, `<IP_n>`, `<IPV4_n>`, `<IPV6_n>`,
`<MAC_n>`, `<HOST_n>`, `<CARD_n>`, `<ID>`); secrets by `<KEYBODY_n>` or `<REDACTED>`; names of AI models and AI
products by `<MODEL_A>`, `<MODEL_B>`…, and vendor names inside paths and identifiers by `vendor_a`, `vendor_b` and so on. Where
a value could not be replaced safely, the text that held it was removed and marked `<WITHHELD>`: 48,013 places in 5,020 sessions (in `messages`, also tool-call arguments in 1 more session). Names of third-party open-source projects and their owners, weak or default values in password fields,
and names that are also ordinary words can remain; the residual risk is not zero. Names of owners' own projects,
products and services, and of private persons, that recur in one owner's sessions and were confirmed by a review were
replaced by `<PROJECT_n>`, stable within a session: 312 names in 3,013 sessions of the full dataset. A final audit in
October 2026 scanned every string of the full dataset again, with an open-source secret scanner (TruffleHog) and
scanners of our own, separate from the redactor and the release gate, and read the likely secrets among their findings
in context; this repository was also scanned with gitleaks and detect-secrets. The audit found secrets that the
redactor and the gate had missed: keys without a known prefix, pasted into prompts, written into code or printed by
tools; passwords typed in prompts or set in configuration and scripts; and session cookies in captured browser
requests. They are now `<KEYBODY_n>`, and so is every random-looking piece of 12 or more characters of such a secret
in the same session, and a cut-off or line-wrapped copy of one that the audit found in another session. In this
repository, such secrets were in 4 sessions. The same audit replaced e-mail addresses the gate had missed by
`<EMAIL_n>` and took out an identity-document number and a vehicle plate as `<WITHHELD>`; none of these was in this
repository.

### Release Gate

Before release, a scanner written apart from the redactor read every data file of the full dataset: verdict **PASS**,
0 HARD findings over 117,796 sessions (HARD = release-blocking). The same scanner's findings from earlier scans drove
the later masking rounds, so PASS shows that nothing this scanner detects remains; it is not an independent audit.
Scanner self-test: on a separate test copy, it found all 1,657 synthetic secrets, identities and names planted there,
and all 195 cases of its fixed regression set. This repository was scanned again on its own after the v3 changes:
**PASS**, 0 HARD findings.

### Deduplication Strategy

10,338 duplicate sessions were removed across the whole dataset: 2,586 when the sessions were first assembled, and
7,752 in later passes that matched exact copies, copies with the same content and near copies (MinHash).

### Sampling

This repository: 1,189 sessions drawn uniformly at random from the full dataset's 106,012 complete sessions, those with
at least one user prompt (a user message that is not wrapper text) and at least one assistant message (a reply or a reasoning step). No stratum was
given a quota, so the sample keeps the mix of the complete sessions up to sampling noise.

### Limitations

- The data is pseudonymised, not anonymous: names that remain in the text, such as package or directory names, and the
  code itself can still point to its author.
- A person's name that appears only in free text (for example in a list of contacts) is not always detected; some remain.
- Recording is uneven across sessions: of the 117,796, input token counts are reported by 95,759, durations by 91,950
  and start times by 106,502.
- There are no outcome labels, commits or code attribution: nothing marks whether a session's task succeeded or attaches the commits it produced. `last_test_result` and `git_commit_made` record what a test runner and git printed.
- A few owners account for a large share of the sessions: the largest for 10.9%, the five largest for 28.0% (sessions with no recorded owner, `user0`, are not counted as one owner).
- `session_kind` marks only clear cases: 32,896 sessions are `unknown`, and by the reviews about half of them are
  interactive.
- `is_eval` flags 35,565 sessions of prepared evaluation tasks; it is not exhaustive, and no decontamination against public evaluation sets was performed: check for overlap before you train or evaluate on them.
- Most user text is in English: 74.0% of the first prompts; `prompt_language` gives the language of each.
- In `messages`, calls of protocol (MCP) and unknown tools, and calls of known tools whose recorded shape no rule maps safely, keep their recorded arguments (see `ft_issues` under *Dataset Schema*); calls an agent issued in parallel appear one after another, as the recordings do not keep the grouping.
- Step times (`ts`) are as recorded: in 18.6% of the sessions a step's time is earlier than the previous step's.

### Data Removal Requests

To have a session removed, write to [goat.ai/contact](https://goat.ai/contact) and quote its `trajectory_id`.

### Versions

- **v1** (8 Oct 2026): first public release of the 1% sample. (`v6` in the repository name is a build number;
  `gatc-v0.5` in `schema_version` is the schema version.)
- **v2** (11 Oct 2026): `messages` and `labels` carry `n_steps` in place of the length band (`tier`, `complexity`; the
  model tier in `models` and `model` is unchanged); `session_kind` is added; more names of owners' own projects are
  masked, and so are the secrets found by the final audit (see *De-identification*). `schema_version` stays
  `gatc-v0.5`; v2 files are the ones with `session_kind`. If you downloaded v1, replace it with v2: v1 holds values
  that v2 masks.
- **v3** (13 Oct 2026): per-session facts added (`is_eval`, `eval_kind`, `template_group`, `template_group_size`, `parent_trajectory_id`, `prompt_language`, `last_test_result`, `git_commit_made`), user steps carry `is_wrapper`, `error_recovery` carries `recovery_kind`; `messages` rebuilt for training (an assistant turn holds its text, reasoning and tool call; arguments mapped onto per-tool schemas; `tools` and `ft_issues` added; v2 kept text and each tool call in separate messages); tool names re-mapped, with their step `type`, and `task_type` and `key_tools` follow the re-mapped tools (780 sessions of the full dataset changed task type, 5 of this repository); vendor names in raw tool names masked. `schema_version` stays `gatc-v0.5`; v3 files are the ones with `is_eval`. If you downloaded v1 or v2, replace it with v3: earlier files hold names in raw tool names that v3 masks.

### License

This repository: Apache License 2.0 (`LICENSE`). The full dataset is licensed separately:
[goat.ai/contact](https://goat.ai/contact).

### Citation

```bibtex
@misc{goat_agentic_coding_sessions_2026,
  title        = {{GATC}: Agentic Coding Sessions},
  author       = {{GOAT labs}},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/datasets/GOAT-AI/gatcv6}},
  note         = {Apache-2.0 for the 1\% sample}
}
```
