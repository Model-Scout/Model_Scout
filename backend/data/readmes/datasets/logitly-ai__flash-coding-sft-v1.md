---
license: cc-by-4.0
task_categories:
- text-generation
- reinforcement-learning
language:
- en
- zh
- ko
- ja
- fr
- ar
- it
- de
pretty_name: Flash Coding - logitly.ai
size_categories:
- 1K<n<10K
---
# Flash Coding

![logitly.ai](logo.png)

> [!CAUTION]
> Uploading these datasets to proprietary AI (e.g., asking a question that includes them) can get your account suspended: the AI vendor can misclassify the chain of thought in these records as reverse engineering or duplicating model outputs.

Provider: [logitly.ai](https://logitly.ai) - Agentic data you can trust

Flash Coding is a dataset of agentic coding traces: an AI coding agent working on tasks in real source repositories.

Every trace is produced under a controlled runtime:

- Sandboxed environment, pinned repository, fixed working directory
- A restricted toolset and operating mode: `work`, `plan`, or `cplan`

An automated verification protocol validates every record before it enters the dataset.

Read the full specification: [specification.pdf](specification.pdf).

The dataset has two parts that share a single record schema:

| Part | Content | Training method |
|---|---|---|
| [SFT](https://huggingface.co/datasets/logitly-ai/flash-coding-sft-v1) | One demonstration trace per task | Supervised fine-tuning |
| [DPO](https://huggingface.co/datasets/logitly-ai/flash-coding-dpo-v1) | A chosen and a rejected trace of the same task | Direct preference optimization |

## Trace Format

A trace is a list of messages in the style of the Anthropic Messages API: each message has a `role` (`user` or `assistant`) and a `content`, a list of typed blocks. Messages strictly alternate between the two roles, starting with `user` and ending with `assistant`.

| Block | Content |
|---|---|
| `text` | The task in the first user message; the assistant's narration between tool calls, or the final summary. |
| `thinking` | The agent's private reasoning for the turn. Plain text, never encrypted or summarized. |
| `tool_use` | A request to run one tool from `toolset`; `input` is a JSON object. |
| `tool_result` | The outcome of one `tool_use`, matched by id; `is_error` marks a failed call. |

Fixed shapes:

- The first user message opens with one `text` block: the task. Every later user message carries only `tool_result` blocks, one per `tool_use` of the preceding assistant message.
- Each assistant message holds one `thinking` block, then any mix of `tool_use` and `text` blocks in generation order. The last message closes the trace with a `text` block: a summary written for the user.

What a trace does not contain:

- **System prompt.** Not recorded: the trace begins with the task itself.
- **Media.** The four block types above are the only kinds; there are no image or document blocks.
- **Not distillation.** No `signature` and no `redacted_thinking`: the traces are not distilled from Anthropic models.
- **Tool schemas.** The trace carries the calls, not the definitions: `toolset` names the tools.

## Tools

| Tool | Description |
|---|---|
| `glob` | Match paths against a glob pattern. |
| `grep` | Search file contents using regex. |
| `read` | Read contents from a file. |
| `write` | Write contents to a file, creating or overwriting it entirely. |
| `edit` | Replace a specific string in a file with new content. |
| `bash` | Execute a shell command. |

## Usage

- **SFT**: each record carries a single trace, used for supervised training / fine-tuning.
- **DPO**: each record carries a `chosen` and a `rejected` trace of the same task, used for preference training: the model learns to prefer `chosen` over `rejected`.

## Characteristics

- **System prompt.** Not given; it can be restored from the context fields.
- **Thinking.** Every assistant message carries a `thinking` block, so the traces carry the complete chain of thought. At training time, a `thinking` block can be dropped when it is short, so the same traces also serve adaptive thinking.
- **Language.** Tasks are written in multiple languages. In a positive trace, the assistant replies in the task's language; the language of `thinking` is not defined.
- **Error flag.** `is_error=true` marks a call that did not exit 0, which can be the ordinary outcome of a call. Keeping these results is deliberate: the model learns to recover from failures over long-horizon work.
- **Plan mode.** In `plan` mode, writing files is strictly forbidden, and `/tmp` is not writable either; the one exception is `/dev/null`. The mode gates use, not existence: the toolset is the same in every mode.

## Evaluation

Flash Coding is training data: it carries no scores and no task-success labels, so the effect of training on it cannot be read off the data itself. Measure the effect on external benchmarks; we recommend DeepSWE and Terminal-Bench. The dataset shares no tasks with either benchmark: zero overlap, zero contamination.

## Contact

Need a dataset tailored to your tasks? Email research@logitly.ai