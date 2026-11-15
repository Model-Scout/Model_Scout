---
license: apache-2.0
language:
- en
- zh
- fr
- de
- es
- ja
- ko
- pt
- ru
- ar
pipeline_tag: image-text-to-text
library_name: transformers
base_model:
- SL-AI/GRaPE-2.5-Quasar
tags:
- thinking_modes
- qwen3.5
- grape
- safetensors
- vision
- multimodal
- instruct
- chat
- coding
- math
- science
- reasoning
- creative_writing
- roleplay
---

![GRaPE_2_5_transparent](https://cdn-uploads.huggingface.co/production/uploads/66960602f0ffd8e3a381106a/Zk0KeTjH4spak3-6HFG2d.png)

_The **G**eneral **R**easoning **A**gent (for) **P**roject **E**xploration_
# The GRaPE 2.5 Family

| Model | Size | Modalities | Domain |
| :--- | :--- | :--- | :--- |
| **GRaPE 2.5 Qusar** | 27B | Image + Text in, Text out | Astronomically high performance |
| **GRaPE 2.5 Helios** | 10B | Image + Text in, Text out | Local Environments for generalistic tasks |

***

# GRaPE 2.5 Quasar

**GRaPE 2.5 Quasar** is the flagship model of the third-generation GRaPE family, it supports multimodal inputs (image + text) and features controllable thinking modes, and work efforts for agentic tasks.

GRaPE 2.5 Quasar is the direct successor to GRaPE 2 Pro, carrying forward research and reasoning improvements from the second generation while incorporating substantially improved training data, focusing on data quality over quantity.

***

## What's New in GRaPE 2.5

GRaPE 2.5 Quasar addresses several shortcomings from the previous generation:

- **A Stronger Training Corpus** — featuring more diverse data
- **A Likable Prose** — that escapes traditional LLM-isms
- **More Generalization** — adapting to more scenarios than previous models
- **A More Stern Work Ethic** — knows how it's supposed to work

***

# Capabilities

GRaPE 2.5 Quasar was post-trained on a curated proprietary dataset including:

- **Creative Tasks**
- **Agentic Coding**
- **STEAM**

GRaPE 2.5 Quasar accepts **image, video and text** as input and produces **text** as output.

GRaPE 2.5 models were trained to have a less robotic prose, nearly eliminating common AI-isms such as `"Honestly?"` or the common `"It's not just X, it's Y"` pattern of phrasing things. Em-dashes have also nearly been eliminated from the model's vocabulary, seeming more natural rather than robotic.

***

## Thinking

GRaPE 2.5 Quasar features controllable reasoning depth through the `<thinking_mode=xxx>` tag. Place it at the **end** of your prompt. **Not** in the system prompt.

| Mode | Behavior | Tokens |
| :--- | :--- | :--- |
| `minimal` | Omits most thinking | 0 - 128 |
| `low` | Brief reasoning pass | 128 - 1,024 |
| `medium` | Standard reasoning | 1,024 – 4,096 |
| `high` | Extended reasoning | 4,096 – 8,192 |
| `xtra-hi` | Deep extended thought | > 8,192 |

**Usage example:**
```
Build a simulation of Prion Disease in the human body, include detailed diagrams for what reactions occur inside of the human body. <thinking_mode=high>
```

> [!Important]
> GRaPE 2.5 Models support alternative methods of selecting thinking modes, such as Muse Glimmer's system-prompt-based style.
>
> In addition, if another harness uses `xhigh` for the Extra High thinking mode, GRaPE 2.5 Quasar will map that to `xtra-hi`.

> **Tip:** For simple queries, `medium` is recommended. Whereas `high` and `xtra-hi` should be used for complex coding tasks, multi-step math, or deep analytical work.

During agentic work, you may notice GRaPE 2.5 Quasar use lower levels of thinking than what you defined. The model was trained to optimize token usage for these tasks by not burning tens-of-thousands of tokens every turn. For example, the `xtra-hi` thinking mode may dip down to `medium` while the agent is applying fixes it previously thought about.

Like all other GRaPE 2.5 models, Quasar was trained to preserve previous thinking blocks in context. This has greatly improved the performance of agentic coding tasks compared to GRaPE 2 models.

### Multilingual Thinking

GRaPE 2.5 models were trained to be able to think in languages other than English. You can add to the system prompt `Think in <language>, but respond in English`.

By default, GRaPE 2.5 Quasar will think and respond in whatever language you prompt it in. Allowing for more seamless conversations, without forcing you, or your users, to know English to understand what is going on.

### Thought Summaries

GRaPE 2.5 models produce thought summaries during thinking. Both a header, and detailed description of the model's thoughts can be extracted easily.

For every new section the model will output `##`, with a one-line summary afterwards. The proceeding paragraph will then be the description of the model's thoughts, from a high-level perspective.

> [!Note]
> Thought Summaries are not supported in `minimal` or `low` thinking modes. They skip the summaries as well as sections in favor of quicker response times.

### Idea Generation

Instead of the typical process of where a typical reasoning model would go through the thinking process, working linearly, GRaPE 2.5 Quasar attempts to scaffold the entire thinking block before proceeding with thinking.

We believe this grounds the model more to stay on-task, and prevent `Wait, but what if...` loops found commonly in small models trained to think for long sequences. The format follows a TODO-list style, which allows you to see how far along the model is in the thinking trajectory, as well as see future thought segments, all before they are generated.

In most thinking blocks, you may also see a list of 4-8 ideas with entire scopes be generated, and the model weighing each approach to find the best one. Minimizing confusion between the prompt and the expected result. This will be skipped if you are extremely explicit in your prompt about what you want GRaPE to do.

Low mode, and sometimes minimal mode, will only generate ideas, and will skip thinking in TODO lists, all for the sake of brevity.

***

## Work Effort

GRaPE 2.5 Quasar features controllable reasoning depth through the `<work_effort=xxx>` tag. Place it at the **end** of your prompt. SLAI apps do this automatically.

| Mode | Behavior | Tokens |
| :--- | :--- | :--- |
| `minimal` | Doesn't use tools, or uses very few tools | 0-2 |
| `low` | Brief tool usage  | < 3-9 |
| `medium` | Standard Analysis | 10-19 |
| `high` | Extended Analysis | 20-29 |
| `xtra-hi` | Large Coding Tasks | 30+ |

**Usage example:**
```
Check linkedin for Chad Donnet's account page, and see what he is proficient in, write a report to a markdown file when done. <work_effort=medium>
```

If the work effort is left blank, GRaPE 2.5 Quasar will automatically decide on the work effort required for the task.

Work effort only works when the agent has access to tools. Otherwise, it will use `minimal`, regardless of the user-defined thinking modes.

> **Tip:** GRaPE 2.5 Quasar had a large amount of agent training done in our agent harness, **Scribe,** we recommend it for best performance.

To learn more about Scribe, and download it, visit the product page [Here.](https://skinnertopia.com/products/scribe)

***

## Sampling Parameters

These sampling parameters are a good starting point:

| Parameter | Value |
| :--- | :--- |
| **Temperature** | 1 |
| **Top K** | 20 |
| **Repeat Penalty** | 1.0 |
| **Top P** | 0.95 |
| **Min P** | 0 |

***

# Training Methodology

We believe one of local AI's greatest short comings has been in creativity. Models have proven they can code agentically, some smaller models even getting close to the performance found by large labs. However, they miss out on a key component most people don't think of when using the models: **Creative Capability.**

When you ask a model, "Make a website for yourself," you likely don't want to see a SaaS app with purple and blue gradients everywhere, that looks like every other AI models' response to the same question. You want something genuinely unique, and special to that model. **We took that direction with GRaPE 2.5.**

We focused a large sum of the training corpus on the models' ability to construct **creative conversations,** and **write stories.** As found from previous Openprose models, GRaPE 2.5 models have the greatest creative capability out of any prior model.

During early experimental testing of GRaPE 2.5 Quasar, we found the model would often be *too creative* for it's own good. When asked for a Browser OS app, it decided to not go for an web-based app which has a classic desktop environment. It wanted to build a ring, which every app would have an orbit around the center, and the window manager would move the apps around the orbit. The web-based browser OS had a proof-of-concept, but was very unrefined.

Testing community-made prompts, such as Bijan Bowen's "Steve the PC-Repair Man" game, the same experimental version of GRaPE 2.5 Quasar built the game, but kept finding new, and creative features, and most importantly, **did not give up.**

GRaPE 2.5 models was our first adventure into jointly boosting a model's creative capabilities with programming capabilities, and we hope we can further this development into future models.

***

# Notes

- Training data is closed-source and proprietary.
- Updates and announcements are posted on [Skinnertopia](https://www.skinnertopia.com/)

Unless there is strong demand, we will *not* be releasing any other model sizes for the GRaPE 2.5 family, and instead focus on GRaPE 3 models.

GRaPE 2.5 is likely one of the last models SLAI will produce for simply being a finetune on-top of another model. We will conduct further research and release experimental GRaPE 3 models.

We appreciate you all for the continued support and appreciation for GRaPE models.

***

_GRaPE 2.5 Quasar is developed under the [SLAI (Skinnertopia Lab for Artificial Intelligence)](https://www.skinnertopia.com/) brand and released under the Apache 2.0 license._