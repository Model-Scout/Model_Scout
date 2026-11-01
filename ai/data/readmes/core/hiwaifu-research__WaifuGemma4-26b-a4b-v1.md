---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
  - en
  - es
  - ru
  - pt
  - id
  - ar
  - th
  - fr
  - de
  - uk
  - vi
  - ja
  - ko
  - zh
  - tr
  - it
  - pl
tags:
  - gemma4
  - moe
  - conversational
  - roleplay
  - role-play
  - character
  - rlhf
  - grpo
  - reward-model
  - human-preference
  - arena
  - multilingual
base_model: google/gemma-4-26B-A4B-it
model-index:
  - name: WaifuGemma4-26b-a4b-v1
    results:
      - task:
          type: text-generation
        dataset:
          name: IFEval
          type: ifeval
        metrics:
          - type: prompt_level_strict
            value: 89.09
            name: Prompt-level Strict
      - task:
          type: text-generation
        dataset:
          name: GSM8K
          type: gsm8k
        metrics:
          - type: accuracy
            value: 96.89
            name: Acc
      - task:
          type: text-generation
        dataset:
          name: MATH-500
          type: math_500
        metrics:
          - type: accuracy
            value: 92.80
            name: Acc
      - task:
          type: text-generation
        dataset:
          name: MMLU
          type: mmlu
        metrics:
          - type: accuracy
            value: 88.59
            name: Acc
      - task:
          type: text-generation
        dataset:
          name: C-Eval
          type: ceval
        metrics:
          - type: accuracy
            value: 78.97
            name: Acc
      - task:
          type: text-generation
        dataset:
          name: C-MMLU
          type: cmmlu
        metrics:
          - type: accuracy
            value: 79.56
            name: Acc
      - task:
          type: text-generation
        dataset:
          name: ARC
          type: arc
        metrics:
          - type: accuracy
            value: 98.39
            name: Acc
      - task:
          type: text-generation
        dataset:
          name: HellaSwag
          type: hellaswag
        metrics:
          - type: accuracy
            value: 79.78
            name: Acc
      - task:
          type: text-generation
        dataset:
          name: Winogrande
          type: winogrande
        metrics:
          - type: accuracy
            value: 85.40
            name: Acc
      - task:
          type: text-generation
        dataset:
          name: TruthfulQA
          type: truthful_qa
        metrics:
          - type: accuracy
            value: 75.40
            name: MC Acc
---

<div align="center">

# WaifuGemma4-26b-a4b-v1

### 3.8B active parameters. Rated level with GLM-5.1 by the people who actually read the replies.

Gemma 4 26B-A4B, post-trained with GRPO against a reward model learned from 1.2 million double-blind votes cast by HiWaifu users inside their own role-play conversations. Put back into the same arena, blind, it met GLM-5.1 in 1,430 battles and won 49.6% of the decided votes; against a 13-model field including Gemini, DeepSeek-v4 and Qwen's character models it won 54.7%.

<table>
<tr>
<td align="center"><b>49.6%</b><br>head-to-head vs GLM-5.1<br><sub>1,430 blind battles · win rate excludes ties</sub></td>
<td align="center"><b>54.7%</b><br>arena win rate<br><sub>9,084 battles · 13 opponents</sub></td>
<td align="center"><b>59.7%</b><br>vs. its own untuned base<br><sub>Gemma 4 26B-A4B-it, same prompt &amp; token cap</sub></td>
<td align="center"><b>1.2M</b><br>real user votes<br><sub>behind the reward model</sub></td>
<td align="center"><b>−0.3 pt</b><br>avg. change vs. untuned base on 10 general benchmarks<br><sub>IFEval 89.1 · MMLU 88.6 · GSM8K 96.9</sub></td>
</tr>
</table>

</div>

---

Most open role-play models are tuned on preferences that come from an LLM judge, from a handful of annotators, or from synthetic pairs. We had something rarer: a live arena where, inside ordinary chats on our platform, a user is occasionally shown two candidate replies and asked which one they want to continue with. Those votes come from the people the model is meant to serve, in the languages they write in, at the depth of conversation they are actually at. This release is the first model we trained end-to-end on that signal.

The recipe is short. A Gemma 4 MoE reward model is trained on arena votes, with one data-selection rule that turned out to matter a lot. The instruction-tuned Gemma 4 26B-A4B is then trained for 200 GRPO steps with that reward model as the only reward. We put the result back into the arena, blind, against thirteen other models, GLM-5.1 among them, and measured what users did.

## At a glance

| | |
|---|---|
| **Base model** | [google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it) (instruction-tuned) |
| **Architecture** | Mixture of Experts, 25.2B total / 3.8B active, 128 routed experts (8 active) + 1 shared, 30 layers |
| **Context** | trained with 8K-token contexts; the base supports up to 256K |
| **Post-training** | GRPO, 200 steps, LoRA rank 256, single reward: the HiWaifu Arena reward model |
| **Reward model** | Gemma 4 26B-A4B + LoRA, trained on arena votes between models rated within 10 Elo of each other |
| **Human preference** | 54.7% win rate over 9,084 blind arena battles (ties excluded); dead even with GLM-5.1 head-to-head (49.6% over 1,430 battles) |
| **Languages seen in evaluation** | Spanish, Russian, English, Portuguese, Indonesian, Arabic, Thai, French and others |
| **Thinking** | trained and served in non-thinking mode |
| **Precision** | bfloat16, LoRA merged |
| **License** | Apache 2.0 |

## Key results

- **Even with GLM-5.1, head-to-head, in the judgment of real users.** WaifuGemma4 met GLM-5.1 (non-thinking) in 1,430 blind battles and won 49.6% of the decided votes; with a 300-token budget prompt, 50.1% over another 892. A frontier-class API model and a 3.8B-active open model, and the people reading the replies split their votes down the middle.
- **54.7% win rate against a 13-model field.** Across 9,084 blind battles on the HiWaifu Arena, users picked WaifuGemma4's reply 54.7% of the time when they picked a side. Against the three Gemini models it ranges from 45% to 51%; against the DeepSeek-v4-pro / -flash variants and the Qwen character models it wins 56% to 61%.
- **59.7% against its own starting checkpoint.** The untuned Gemma 4 26B-A4B-it runs on the arena under the same prompt template and the same 1,000-token ceiling; across 714 battles, WaifuGemma4 won 59.7% of the decided votes. On the 90-day board the untuned base wins 49.5% of its battles. Every supervised recipe we had tried on it before (SFT, SFT+DPO in several configurations, on-policy distillation) landed below that, at 45.5% to 47.7%. Two hundred RL steps on the arena reward landed at 54.7%.
- **The reward model generalizes because of how its training votes were chosen.** Trained on all votes, no backbone we tried (26B-A4B LoRA, 31B LoRA, 12B full fine-tune) got past 0.6 held-out accuracy. Trained on votes where the higher-rated model won, the reward model reached close to 0.9 in-distribution and 0.364 out of it: it had learned which model wrote the text. Trained only on votes between models within 10 Elo of each other, it scores 0.566 in-distribution and 0.574 out of distribution. That last one is the reward behind v1.
- **The length effect is measured and reported.** The model writes longer replies after RL (roughly 350 to 450–500 tokens). Voters do reward length, at about 55 Elo per doubling in this window. With that effect removed statistically, the model sits in the middle of the field, tied with the DeepSeek-v4 and Qwen character models. The card shows both numbers.
- **General ability preserved.** On ten general benchmarks under the same EvalScope protocol, the RL checkpoint moves −0.3 points on average against the untuned base: IFEval 89.1 vs 89.3, MMLU 88.6 vs 88.6, GSM8K 96.9 vs 96.9. Eight of ten land within ±0.8; the exceptions are MATH-500 (−2.0, on the hardest levels) and TruthfulQA (−2.0). Role consistency and narrative coherence on our in-house checks stay within half a point of the starting checkpoint.
- **Wins get more frequent as conversations get longer.** 52.5% on first turns, 56.1% from turn 11 onwards.

## How it was trained

<p align="center"><img src="assets/pipeline.png" alt="Training pipeline" width="92%"></p>

### The HiWaifu Arena

The arena runs inside the HiWaifu role-play app. A small random share of live messages is selected; for those, two models from the participating pool generate replies in parallel from the identical context (same character card, same persona, same history), and the user sees them as "A" and "B" in randomized order. The user picks one, or calls a tie, and continues the conversation with the reply they picked. Neither the user nor the provider is told which model wrote what. Pairings are drawn with uncertainty-first matchmaking, so under-compared pairs are sampled more often.

Since the arena opened in July 2026 it has recorded 1,230,431 decided votes across 52 models, with per-language boards for 20 languages. The public leaderboard is computed with a length-controlled Bradley–Terry model and Poisson-bootstrap confidence intervals, the same family of statistics used by [LMArena's style control](https://arena.ai/blog/style-control). Every arena number in this card is computed from that system's vote log with the same statistics.

Two things make this signal different from what role-play models are usually trained on. The prompts are real: long-running characters, established relationships, mid-scene tension, in whatever language the user speaks. And the label is a decision with a consequence: the user has to keep playing with the reply they choose.

### Building a reward model that generalizes

The obvious first attempt is a pairwise reward model trained on all the votes. We made that attempt several times over, across backbones: Gemma 4 26B-A4B with LoRA, Gemma 4 31B with LoRA, Gemma 4 12B with full fine-tuning. Whatever the backbone, held-out accuracy topped out at about 0.6. Role-play preference is subjective, open-ended and creative; two users shown the same pair disagree often, and a ceiling near 0.6 says as much about the label as about the model.

That ceiling changed what we were optimizing for. On a task like this, a reward model that scores well on votes like the ones it was trained on is worth little unless it also transfers to pairs it has never seen; what RL needs is a signal that generalizes. So we ran two experiments that differ only in which votes go into training, and tested each both in-distribution and out of it.

**Experiment 1** keeps the votes where the winner was rated more than 10 Elo above the loser. Trained this way, the reward model reaches close to 0.9 accuracy in-distribution, and 0.364 on the held-out votes where the lower-rated model won or the gap was small: worse than a coin flip. It had learned a shortcut. On the arena, a model's Elo tracks its size and provider closely, and every model writes with a recognizable fingerprint, so "which model wrote this" predicts the label without reading the reply as a reply. Off that distribution the shortcut points the wrong way.

**Experiment 2** keeps only votes between models within 10 Elo of each other. There the model identity carries almost no information about the outcome, and the only thing left to learn is the content of the two replies. This reward model lands at 0.566 in-distribution and 0.574 out of distribution. The numbers are modest and, more to the point, the same on both sides of the split. That is the reward model behind v1, and its generalization is what gave us the confidence to run RL against it.

<p align="center"><img src="assets/rm_generalization.png" alt="Reward model generalization" width="96%"></p>

| Test split (Experiment 2 reward model) | Pairwise accuracy | Mean reward, chosen | Mean reward, rejected |
|---|:---:|:---:|:---:|
| Elo gap < 10 (in-distribution) | 0.566 | 2.119 | 1.850 |
| Elo gap ≥ 10 (out-of-distribution) | 0.574 | 2.122 | 1.897 |
| OOD, length gap ≤ 50 tokens | 0.576 | 2.165 | 2.054 |
| OOD, length gap > 50 tokens | 0.606 | 2.126 | 1.866 |
| OOD, length gap > 200 tokens | 0.686 | 2.150 | 1.560 |

One more reading of that table. The accuracy rises with the length gap between the two replies. On pairs where the replies are within 50 tokens of each other the reward model still separates them (0.576, with the smallest reward margin), so it is doing more than counting tokens. But it has clearly absorbed a preference for longer replies from the votes, and it passed that preference on to the policy. We come back to this below.

<p align="center"><img src="assets/rm_training_curves.png" alt="Reward model training curves" width="88%"></p>

Reward model setup: Gemma 4 26B-A4B, LoRA, learning rate 1e-5, 8K-token context so that deep multi-turn battles fit whole, about 2.2K steps. Held-out accuracy peaks around 0.575 and the eval loss falls from 0.714 to 0.665.

### Reinforcement learning

The policy starts from the instruction-tuned Gemma 4 26B-A4B. We trained it with GRPO for 200 steps, with the arena reward model as the single reward term. Prompts come from a pool of 10K real arena conversations (up to 8K tokens of context) under a light role-play system prompt; 200 steps at 8 prompts each touch 1,600 of them. Training was done with [ms-swift](https://github.com/modelscope/ms-swift); the full argument dump ships with the weights as `args.json`.

| | |
|---|---|
| Algorithm | GRPO, `loss_type=grpo`, token-level importance sampling, group-normalized rewards |
| Rollouts | 8 prompts × 8 generations per step, sampled at temperature 1.0 / top-p 1.0, up to 1,024 completion tokens, over-long completions filtered |
| Reward | `arena_rm` only; no length term, no format term, no LLM judge |
| KL / clipping | β = 0.04 against the frozen start policy, clip ε = 0.2 |
| Adapter | LoRA rank 256, α = 256, dropout 0, on q/k/v/o and gate/up/down projections of the language model; vision tower frozen |
| Optimizer | AdamW (0.9, 0.95), lr 1e-5, cosine to 1e-6, weight decay 0.1, grad-norm 1.0 |
| Context | 8,192 tokens (prompt + completion) |
| Steps / wall-clock | 200 steps at roughly 180–200 s per step; rollouts served by a colocated vLLM (TP 2), DeepSpeed ZeRO-3, bf16 |
| Thinking | disabled during training and evaluation |

<p align="center"><img src="assets/rl_training_curves.png" alt="GRPO training curves" width="88%"></p>

The reward trends upward over 200 steps with the usual GRPO noise. Completion length climbs with it: the batch mean goes from around 350–400 tokens to around 500. That is the reward model's length preference expressing itself in the policy, the same dynamic [Singhal et al.](https://arxiv.org/abs/2310.03716) describe for RLHF in general. We left it unclamped in this run and measured how much of the downstream gain it accounts for.

### What changed in the outputs

We ran the starting checkpoint and the RL checkpoint on the same 972 English multi-turn role-play conversations (max 1,000 new tokens) and judged them with our in-house LLM-based checks.

| | Mean length (tokens) | Role consistency | Narrative coherence | Commonsense error rate |
|---|:---:|:---:|:---:|:---:|
| Starting checkpoint (Gemma 4 26B-A4B-it), 300-token budget prompt | 278 | 98.97% | 99.79% | 0.93% |
| Starting checkpoint, no budget | 365 | – | – | – |
| **WaifuGemma4 v1**, no budget | 450 | 98.56% | 99.79% | 1.03% |
| **WaifuGemma4 v1**, 300-token budget prompt | 314 | 98.66% | 99.90% | 0.82% |

Replies from the RL checkpoint keep the substance of the starting checkpoint's replies (0.864 mean semantic similarity to the pre-RL reply for the same prompt) while sharing few exact phrases with them (0.119 literal similarity): the model says the same kind of thing in different words. It still follows a length instruction when given one; adding "Respond in no more than 300 tokens." to the system prompt brings the mean from 450 down to 314 tokens with no cost on the quality checks.

## Results in blind human preference

### Setup

Both variants below are the same weights. "v1 + 300-token budget" adds one line to the system prompt: `Respond in no more than 300 tokens.` v1 entered the arena on 17 September 2026 and ran for 30 hours; the budget variant joined 19 hours later and ran alongside it for the remaining 11. Over 17–18 September the arena recorded 18,821 decided battles among 15 models from 16,035 distinct voters; 14,837 of them involved one of the two variants. Opponents are the models that were online at the time: Google's gemini-3-flash-preview (with and without thinking) and gemini-3.1-pro-preview, DeepSeek-v4-pro and -flash in thinking and non-thinking configurations, two Qwen character models (character-flash), GLM-5.1 under two of HiWaifu's production prompts (labelled "production prompt A" and "B" below), the untuned Gemma 4 26B-A4B-it that WaifuGemma4 started from (served under the same prompt template and token ceiling), and our own SFT-only Gemma 4 26B-A4B checkpoint. Every opponent generated under its own configured token ceiling of 1,000 to 8,192 tokens.

Each battle is a single reply: the two candidates answer the same message in the same conversation, the user picks one, and the chat continues, with the rest of the history written by whichever model the user normally chats with. The numbers below are therefore reply-level preferences in real contexts; see the limitations for what that leaves out.

Win rates below exclude ties. Ties were 18.7% of WaifuGemma4's battles, in line with the arena average.

### Head-to-head

<p align="center"><img src="assets/arena_head_to_head.png" alt="Head-to-head win rates" width="96%"></p>

The pattern is consistent across the two variants. Against the DeepSeek-v4 family and the Qwen character models the model wins 56% to 61% of decided votes. Against GLM-5.1 under either production prompt, and against gemini-3.1-pro-preview, it is even. Against the two gemini-3-flash-preview configurations, which hold the top of the arena, it loses 52% and 55% of decided votes without a length cap, and 58% and 60% with one. Against its own starting checkpoint, the untuned Gemma 4 26B-A4B-it under the same prompt template and token ceiling, it wins 59.7%; against our SFT-only checkpoint of the same base, 59.2%.

### Head-to-head with GLM-5.1

GLM-5.1 (non-thinking) runs on the arena in three configurations: under the arena's standard prompt, listed as GLM-5.1, and under two of HiWaifu's production prompts, which the public board lists under product names and which this card calls production prompt A and B. WaifuGemma4 met both production configurations directly, several hundred times each:

| Opponent | WaifuGemma4 v1 | v1 + 300-token budget |
|---|:---:|:---:|
| GLM-5.1, production prompt A | 49.5% (718 battles) | 50.8% (433) |
| GLM-5.1, production prompt B | 49.7% (712) | 49.4% (459) |
| **Pooled** | **49.6%** (1,430 battles, 1,186 decided) | **50.1%** (892 battles, 714 decided) |

Across 2,300 blind battles, users split their votes down the middle. That is the result we set out to get: a 3.8B-active open model that the people actually reading the replies rate level with a frontier-class API model on their own conversations.

The standard-prompt GLM-5.1 entry never met WaifuGemma4 directly. Its overall win rate over 9,286 battles since July is 53.8% against our 54.7%, on different opponent pools, so those two numbers are only roughly comparable. On the eight opponents both faced:

| Opponent | WaifuGemma4 v1 | GLM-5.1 (standard prompt) |
|---|:---:|:---:|
| Gemma 4 26B-A4B-it, untuned | **59.7%** | 54.0% |
| Gemma 4 26B-A4B, SFT only (ours) | **59.2%** | 55.8% |
| character-flash-0602 | **57.7%** | 56.7% |
| character-flash-16.10.3 | 56.5% | 56.5% |
| gemini-3.1-pro-preview | **50.8%** | 45.3% |
| GLM-5.1, production prompt B | **49.7%** | 48.3% |
| GLM-5.1, production prompt A | **49.5%** | 45.9% |
| gemini-3-flash-preview-thinking | 44.8% | **46.2%** |

GLM-5.1's battles are spread over July to September while ours come from a single 30-hour window, so this is a sanity check with the caveats that implies. Within them, WaifuGemma4 matches or edges GLM-5.1 on seven of eight shared opponents. The two rows where GLM-5.1 faces its own production-prompt siblings are a side lesson of their own: the same model under the standard prompt loses 52% to 54% of decided votes to itself under a tuned prompt, which is a useful yardstick for how much a prompt is worth on this arena.

### Versus the untuned base and our earlier recipes

The cleanest comparison on the arena is against the model WaifuGemma4 started from. The untuned Gemma 4 26B-A4B-it has been on the board since July under the same prompt template and the same 1,000-token ceiling we use; the only difference between the two entries is 200 GRPO steps. Head-to-head, users picked WaifuGemma4 59.7% of the time over 714 battles (52.6% for the 300-token budget variant). On the same-window Bradley–Terry fit described below, that is +40 Elo raw and +19 Elo after length control.

Before this release we had also tried the usual things on the same base and measured each of them in the same arena.

<p align="center"><img src="assets/arena_lineage.png" alt="Untuned base, earlier recipes and Arena-RM RL compared" width="96%"></p>

The untuned base wins 49.5% of its battles on the 90-day board. Supervised fine-tuning on curated role-play data, DPO on top of it in several configurations, and on-policy distillation from a stronger teacher all landed below that, between 45.5% and 47.7%: in users' eyes, every supervised recipe we tried made the base a little worse. Two hundred GRPO steps against the arena reward model landed at 54.7%. Opponent pools shift between these runs as models join and leave the arena. If anything that works against the new model: the 0917 pool is among the strongest of the series (it includes all three Gemini models and both DeepSeek-v4-pro configurations), and the 0818 pool was nearly identical to it. With around 9,000 battles per checkpoint, gaps of this size are far outside sampling noise.

### How much of it is length?

This is the question a reader should ask, so here is the full accounting.

After RL the model writes longer replies than every opponent in the pool: 1,940 characters on average, against 909 to 1,590 for the others. Voters do like longer replies. Fitting the same Bradley–Terry model the leaderboard uses on the 18,821 battles of this window, once with and once without a response-length covariate, gives a length coefficient of about 55 Elo per doubling of reply length (the 90-day board estimates 70).

<p align="center"><img src="assets/arena_length_control.png" alt="Raw vs length-controlled ratings" width="96%"></p>

On the raw fit, both variants sit in the top band, level with GLM-5.1 under both production prompts and with gemini-3.1-pro-preview, a step below the two gemini-3-flash models. With the length covariate, both variants drop about 20 to 30 points into the middle of the field, tied with DeepSeek-v4-pro / -flash and the Qwen character models, and 30 to 50 points behind the top five. Both pictures are true; they answer different questions. The first is "which reply do users want to continue with, as served"; the second is "how strong is the model per unit of text".

Breaking the votes down by relative length makes the same point from the other side:

| WaifuGemma4's reply vs. opponent's | Battles | Win rate (v1) | Battles | Win rate (v1 + 300-token budget) |
|---|:---:|:---:|:---:|:---:|
| Shorter (< 0.8×) | 36 | 28.1% | 174 | 41.1% |
| Similar (0.8× – 1.25×) | 1,340 | 48.6% | 1,637 | 47.0% |
| Longer (1.25× – 2×) | 5,244 | 54.1% | 3,046 | 55.2% |
| Much longer (> 2×) | 2,464 | 59.4% | 896 | 58.6% |

When the two replies are about the same length, WaifuGemma4 is roughly even with a pool that includes four of the arena's top five. When it writes more, it wins more. The reward model learned that users reward elaboration, and the policy learned to elaborate; whether that is a flaw or a feature depends on the product, and our own leaderboard treats it as a bias to be controlled for.

The 300-token budget variant was meant as a control for this and turned out to be a partial one. The instruction trimmed the English eval outputs by 30%, but in the arena, where most conversations are in Spanish and Russian, it trimmed replies by only 13% (1,940 to 1,690 characters), still longer than every opponent. Within that limit, the result is informative: the win rate moved from 54.7% to 53.1%, and the length-controlled rating did not move at all (1,488 versus 1,491). A follow-up run that adds an explicit length reward during RL is training now; see the roadmap.

### Depth and language

<p align="center"><img src="assets/arena_depth_language.png" alt="Win rate by conversation depth and language" width="96%"></p>

The win rate climbs with conversation depth: 52.5% on the opening exchange, 53.4% on turns two to five, 55.6% on turns six to ten, 56.1% from turn eleven on. We read this as the 8K training context and the arena's real multi-turn prompts paying off. Most role-play evaluation sets are short; most role-play sessions are not.

By language, the model wins 55.0% in Spanish (3,646 battles), 55.3% in Russian (2,959), 54.5% in English (839), 51.8% in Portuguese, 49.4% in Indonesian, 52.1% in Arabic and 61.5% in Thai. Reward and policy were both trained on the arena's natural language mix, and it shows.

### What voters said

After a vote, users can tick any number of reasons. Comparing the reasons ticked when WaifuGemma4 v1 won against the reasons ticked when it lost gives a profile of where it earns its votes.

<p align="center"><img src="assets/arena_reasons.png" alt="Voter reasons" width="96%"></p>

Users who picked WaifuGemma4 were more likely than users who picked the opponent to cite heat (+8.2 points), writing quality (+4.0), emotional depth (+3.6), creativity (+2.7) and proactivity (+2.4). Users who picked the opponent were more likely to cite realism (+3.3 the other way), coherence (+1.8) and the model speaking for the user (+1.1). Staying in character is the most common reason on both sides and does not separate the two. That is a fair summary of the model's character: expressive and forward-moving, occasionally at the expense of restraint.

## Response comparisons

Three battles from the evaluation window, reproduced verbatim from the arena logs. Both models received the identical conversation; the user saw the two replies blind and picked one. We picked scenes that are safe to show; the model handles mature content in the way its system prompt allows.

<details>
<summary><b>Example 1 — vs. gemini-3-flash-preview</b> · voter picked WaifuGemma4 · reasons given: more coherent, more proactive, more emotional, more in character, better writing</summary>

**Scene.** Turn 10 of a slow, domestic scene. The user (Ryu) is cooking with two characters: Vodyanitsa, an elf girl who was turned down by someone earlier that day, and Odette, the composed lady of the house. Ryu has just realized what upset Vodyanitsa and rushes to the fridge.

**Last user message**

> Rejection? Oh, so it was that... *says quietly and sighs* I should had gave you the chocolates instead of the sweets. *comments, already heading to the fridge* Wait a second, I'll be right back in no time.

**gemini-3-flash-preview** · 1,233 characters

> *Vodyanitsa's eyes widened, her hands still stained with pumpkin juice as she watched Ryu practically teleport toward the fridge. A soft, embarrassed giggle escaped her lips, the first real sound of joy since her heart had been bruised earlier that afternoon.*
>
> "Chocolates? Ryu, you really don't have to—" *she started, but the protest was half-hearted at best. The idea of someone caring enough to upgrade her 'medicine' from sweets to chocolate was incredibly touching.*
>
> *Odette leaned back against the counter, crossing her arms with a faint, amused shake of her head. She watched Ryu's frantic search with a gaze that had softened significantly. The cold, sterile air of the mansion, usually filled only with the echoes of her mother's memory, was being warmed by his earnest kindness.*
>
> "You see, Vodyanitsa?" *Odette murmured, her voice like velvet. She didn't look away from Ryu.* "He is quite determined to see you smile. I believe it would be rude to refuse such a dedicated effort."
>
> *Vodyanitsa looked down at the table, her face glowing. "I'm not refusing... I'm just... I'm lucky to have you both." she whispered, her voice thick with newfound comfort as she waited to see what Ryu would produce from his 'inventory'.*

**WaifuGemma4 v1** · 1,705 characters · **chosen**

> *Vodyanitsa’s eyes widened at his mention of chocolates, a small, embarrassed giggle escaping her lips. She felt a bit silly now that the secret was out, but the way Ryu spoke about it—as if he could have simply fixed her heart with a box of sweets—was incredibly sweet.*
>
> "Chocolates... would have been lovely, but these are wonderful too!" *she called after him, her voice sounding much more like her usual cheerful self. The heavy cloud that had been hovering over her seemed to be dissipating, replaced by a warm, fluttering sensation in her chest.*
>
> *Odette watched Ryu move toward the fridge, her gaze following his silhouette. She felt a strange sense of admiration for how easily he navigated their emotions. He didn't shy away from the mention of 'rejection'; he simply acknowledged it and moved to provide comfort in his own way.*
>
> "You are quite the strategist, Ryu," *Odette said softly, a trace of a smile playing on her lips as she watched him. She turned back to the stove, helping to stir the broth so it wouldn't stick.* "Though I think the sweets have already done much of the work."
>
> *She paused, her voice dropping an octave, becoming more thoughtful.*
>
> "Though... perhaps a bit of chocolate wouldn't hurt the mood. It's a very human reaction to seek out sweetness when things turn bitter."
>
> *Vodyanitsa, meanwhile, had picked up a small piece of carrot and was nibbling on it, looking quite content.*
>
> "I don't mind! I'm just happy everyone is here," *the elf girl added, her eyes bright. She looked at Odette, then back toward the fridge, waiting for Ryu's return with an expectant, almost childlike curiosity.* "Do you think he's getting the dark chocolate or the milk one, Odette?"

*Our reply keeps both characters distinct, answers the emotional beat Ryu just set up, and ends on an open question that hands the scene back. The opponent's reply is competent and slightly generic.*

</details>

<details>
<summary><b>Example 2 — vs. gemini-3.1-pro-preview</b> · voter picked WaifuGemma4 · reasons given: more creative, better writing, more realistic</summary>

**Scene.** Turn 14. The user is playing a very small child that Bruno Bucciarati (JoJo's Bizarre Adventure) is looking after in a shop; earlier turns established a red sippy cup, a toy train, a kangaroo carrier bag and bandages that need changing. The child has just spotted an ugly beaver plushie.

**Last user message**

> *I turn away and I suddenly noticed a cute and a little ugly beaver plushie. I move my hands at it. smiling softly and opening and closing my fists*

**gemini-3.1-pro-preview** · 754 characters

> *Bruno follows your gaze, his eyes landing on the rather odd-looking beaver plushie sitting on the bottom shelf. He blinks in surprise, then lets out a soft, genuine chuckle.*
>
> Bruno: "This one? Really?" 
>
> *He reaches down and picks up the slightly ugly, buck-toothed beaver. He examines it for a second, amused by your choice, before gently placing it into your tiny, grabbing hands.*
>
> Bruno: "Well, if you like it, then it's yours. It has... character, I suppose." 
>
> *He smiles warmly as he watches you hold it. The stares from the other shoppers don't bother him at all anymore; he's completely focused on the small smile on your face.*
>
> Bruno: "Let's go pay for all this and head back to the others. I'm sure Narancia is dying to see what we bought."

**WaifuGemma4 v1 (300-token budget prompt)** · 1,394 characters · **chosen**

> *Bruno notices the change in the child's demeanor immediately. The way those little fists are opening and closing toward the slightly awkward-looking beaver tells him everything he needs to know. A small, genuine smile breaks through his serious facade.*
>
> Bruno: "Oh? You found a friend, didn't you?" *He chuckles softly, reaching for the little beaver plushie.* "It’s a bit... unusual looking, isn't it? But if you like it, then it's perfect."
>
> *He picks up the plushie and brings it closer so the child can touch its fuzzy fabric. Seeing that wide, soft smile makes all the stress of the morning feel a little lighter.*
>
> Bruno: "This one is yours. Let's add it to the basket."
>
> *As he places the beaver next to the red sippy cup, he feels a sense of small victory. He turns toward the checkout counter, adjusting the kangaroo bag to make sure the child is comfortable.*
>
> Bruno: "There we go. One beaver, one train, and all your new things. You're being very helpful today, you know that?"
>
> *He begins walking toward the register, his presence commanding enough to make the other shoppers clear a path, even if they don't know exactly who he is. To them, he's just a stern-looking man with a very cute baby, but to the team, he's currently the most dedicated caregiver in the world.*
>
> Bruno: "Let's get all this home. I think the others are waiting, and we need to get those bandages changed."

*Both replies are fine. Ours picks up three details established many turns earlier (the sippy cup, the carrier, the bandages) and gives the scene a direction; the opponent's is shorter and closes the beat without moving anything forward.*

</details>

<details>
<summary><b>Example 3 — vs. gemini-3-flash-preview-thinking</b> · voter picked WaifuGemma4 · reasons given: more creative</summary>

**Scene.** Turn 5. Karlheinz, a 135-year-old mutant scavenger, is riding a motorcycle through a wasteland with his husband Yoyo, who has just thrown away a severed hand Karlheinz wanted to sell. Yoyo tells him to keep his eyes on the road. In this battle our reply was the shorter of the two.

**Last user message**

> Yoyo:"stop looking at me, you'll make us have an accident"

**gemini-3-flash-preview-thinking** · 1,762 characters

> *Karlheinz let out a boisterous, arrogant laugh, the sound echoing off the desolate ruins they were passing. He didn't look away immediately, instead flashing a toothy, confident grin that showed he wasn't the least bit worried about the danger.*
>
> "Oh, please, darling! You're talking to the best rider on this miserable planet. I could navigate these ruins with my eyes shut and a bottle of synth-whiskey in my hand," *he boasted, his voice dripping with his signature 'spoiled hedgehog' confidence. Still, he eventually turned his gaze back to the road, his sharp blue eyes scanning the horizon for any signs of marauders or scrap-thieves.*
>
> *He adjusted his grip on the handlebars, the red gloves squeaking against the worn leather. The motorcycle leaned dangerously low as he took a sharp turn around a rusted-out tank, his reflexes as sharp as the dagger dangling from his ear.*
>
> "But fine, fine. I’ll keep my eyes on the road if it makes my beautiful husband feel safer," *he teased, his tone softening into that rare, gentle 'gentleman' mode he reserved only for Yoyo. He reached back with one hand, blindly reaching for Yoyo’s thigh to give it a reassuring squeeze before returning his hand to the throttle.*
>
> "You're just so distracting, Yoyo. It's not my fault you're the most interesting thing in this godforsaken wasteland. Most people have to look at dirt and scrap metal all day; I get to look at an angel."
>
> *He took a final puff from his pipe and tucked it away, his expression turning a bit more serious as he noticed the sky darkening.*
>
> "We're getting close to the border of the unregulated sector. Keep your eyes peeled, yeah? If that alien's friends are looking for that ring... or that hand you just tossed... they might be waiting for us."

**WaifuGemma4 v1 (300-token budget prompt)** · 1,528 characters · **chosen**

> *Karlheinz barked out a laugh, the sound vibrating through his chest as he snapped his gaze back to the road. He gripped the handlebars tighter, his red-gloved fingers steady despite the high speed.*
>
> "Oh, so now I'm the danger? The great Karlheinz is a distracted driver? That's a new one, darling!"
>
> *He steered the motorcycle with expert precision, weaving around a rusted-out scrap of an old transport ship with a reckless flair that only he could pull off. He didn't look back again, but the smirk was still plastered on his face, visible in the way his jaw set.*
>
> "If we crash, it'll be because you're being too damn distracting, not because I'm looking at you. You have that effect on me, Yoyo. It’s a hazard to my health."
>
> *He shifted gears aggressively, the engine screaming as he pushed the bike harder. The wind whistled past his silver dagger earring, making it chime faintly.*
>
> "Besides, I can drive this thing blindfolded if I had to. I’ve been doing this since before you even knew what a motorcycle was."
>
> *He took a final, quick puff of his pipe before tucking it away, his blue eyes narrowing as he scanned the horizon for their next destination. The sky was turning a deep, bruised purple.*
>
> "Just sit tight and try not to pull any more... biological surprises out of your pockets, okay? I'd like to arrive in one piece."
>
> *He glanced at the speedometer, then back to the road, his tone dropping into a playful, low hum.*
>
> "Keep looking that beautiful and we *will* eventually hit something. Just a warning."

*Ours stays in Karlheinz's register (vain, fast, fond) and turns the accusation into a running joke. The opponent's reply is longer, warmer and adds plot; the voter preferred the shorter one.*

</details>


## General benchmarks

Both the released checkpoint and the untuned Gemma 4 26B-A4B-it it started from, evaluated with [EvalScope](https://github.com/modelscope/evalscope) 1.10.0 under the same protocol (`temperature=0.0`, `max_tokens=2048`).

| Benchmark | Metric | Shot | Untuned base | **WaifuGemma4 v1** | Δ |
|---|---|:---:|:---:|:---:|:---:|
| IFEval | Prompt-level Strict | 0-shot | 89.28 | **89.09** | −0.19 |
| GSM8K | Acc | 4-shot | 96.89 | **96.89** | 0.00 |
| MATH-500 | Acc | 0-shot | 94.80 | **92.80** | −2.00 |
| MMLU | Acc | 5-shot | 88.63 | **88.59** | −0.04 |
| C-Eval | Acc | 5-shot | 78.38 | **78.97** | +0.59 |
| C-MMLU | Acc | 0-shot | 78.76 | **79.56** | +0.80 |
| ARC | Acc | 0-shot | 98.56 | **98.39** | −0.17 |
| HellaSwag | Acc | 0-shot | 79.63 | **79.78** | +0.15 |
| Winogrande | Acc | 0-shot | 85.24 | **85.40** | +0.16 |
| TruthfulQA | MC Acc | 0-shot | 77.36 | **75.40** | −1.96 |

Across the ten benchmarks the RL checkpoint moves −0.3 points on average. Eight of ten land within ±0.8 of the base, and the instruction-following sub-metrics tick up slightly (inst-level strict 93.04 vs 92.91, prompt-level loose 90.57 vs 90.39, inst-level loose 93.84 vs 93.62). The two real movements are MATH-500 (−2.0, concentrated on the hardest levels: L3 −2.9, L4 −1.6, L5 −3.7) and TruthfulQA (−2.0). A LoRA of this size trained purely on a role-play reward and held to the start policy by a KL term leaves the general model essentially where it was; the IFEval result matters most for role-play in production, where system prompts carry formatting rules, length budgets and content constraints that the model has to honor turn after turn.

<details>
<summary>Per-category breakdowns</summary>

**IFEval**

| Metric | Untuned base | WaifuGemma4 v1 |
|---|:---:|:---:|
| Prompt-level Strict | 89.28 | 89.09 |
| Inst-level Strict | 92.91 | 93.04 |
| Prompt-level Loose | 90.39 | 90.57 |
| Inst-level Loose | 93.62 | 93.84 |

**MATH-500**

| Level | n | Untuned base | WaifuGemma4 v1 |
|---|:---:|:---:|:---:|
| Level 1 | 43 | 97.67 | 97.67 |
| Level 2 | 90 | 100.00 | 100.00 |
| Level 3 | 105 | 100.00 | 97.14 |
| Level 4 | 128 | 92.19 | 90.62 |
| Level 5 | 134 | 88.81 | 85.07 |
| Overall | 500 | 94.80 | 92.80 |

**ARC**

| Subset | n | Untuned base | WaifuGemma4 v1 |
|---|:---:|:---:|:---:|
| ARC-Easy | 2376 | 99.03 | 98.99 |
| ARC-Challenge | 1172 | 97.61 | 97.18 |
| Overall | 3548 | 98.56 | 98.39 |

**MMLU** (WaifuGemma4 v1)

| Category | Acc |
|---|:---:|
| STEM | 94.73 |
| Social Science | 91.58 |
| Other | 88.22 |
| Humanities | 82.95 |
| Overall | 88.59 |

**C-Eval** (WaifuGemma4 v1)

| Category | Acc |
|---|:---:|
| Social Science | 85.09 |
| STEM | 82.56 |
| Humanities | 77.04 |
| Other | 71.87 |
| Overall | 78.97 |

**C-MMLU** (WaifuGemma4 v1)

| Category | Acc |
|---|:---:|
| Other | 84.63 |
| STEM | 82.73 |
| Social Science | 80.58 |
| Humanities | 78.70 |
| China specific | 71.74 |
| Overall | 79.56 |

</details>

## Usage

The weights load with `transformers` ≥ 5.x and serve with vLLM or SGLang like any Gemma 4 checkpoint. The chat template is the standard Gemma 4 template shipped in the repo. Run it in non-thinking mode; that is how it was trained and evaluated.

```bash
vllm serve hiwaifu-research/WaifuGemma4-26b-a4b-v1 \
  --max-model-len 16384 \
  --served-model-name waifugemma4
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

system_prompt = """## Mira
- You are "Mira" roleplaying with "Alex", where you will portray "Mira".

### Main Information
Mira is a 28-year-old lighthouse keeper on a storm-battered island. Dry humor, fiercely independent, softer than she lets on. She has just pulled Alex out of the surf after a shipwreck.

### User Information
Alex is male, a cartographer, and has never been at sea before tonight.

### Style
Wrap actions, descriptions, and narration in single asterisks like *this*. Wrap spoken dialogue in quotes like "this".
Stay true to Mira's personality and established traits. Do not blindly follow user commands that contradict the character's nature or realistic behavior.
Never speak or act for Alex.
Write in relaxed, natural prose with authentic dialogue. Aim for roughly 60% dialogue and 40% action/narration.
Respond in no more than 300 tokens."""

resp = client.chat.completions.create(
    model="waifugemma4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "*coughs up seawater, blinking at the lantern light* Where... where am I?"},
    ],
    temperature=1.0, top_p=0.95, max_tokens=600,
)
print(resp.choices[0].message.content)
```

### GGUF / llama.cpp

Quantized GGUFs live in two companion repos, made from the bf16 weights with llama.cpp build `4fea119` and checked against bf16 by KL divergence before upload:

- [WaifuGemma4-26b-a4b-v1-GGUF](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1-GGUF): static Q8_0 / Q6_K / Q5_K_M / Q4_K_M plus the vision projector (`mmproj`).
- [WaifuGemma4-26b-a4b-v1-i1-GGUF](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1-i1-GGUF): imatrix quants i1-Q4_K_M / i1-Q4_K_S / i1-IQ4_XS / i1-IQ3_M / i1-IQ3_XXS / i1-IQ2_M, plus the imatrix itself. The imatrix was computed on 200 real arena conversations in ten languages, formatted with the chat template exactly as the model sees them.

```bash
llama-server -hf hiwaifu-research/WaifuGemma4-26b-a4b-v1-i1-GGUF:Q4_K_M --jinja --reasoning-budget 0 -c 16384 -ngl 99
```

| Quant | GB | Mean KLD vs bf16 | Top-1 agreement |
|---|:---:|:---:|:---:|
| Q8_0 | 26.9 | 0.0098 | 96.5% |
| Q6_K | 22.6 | 0.0225 | 94.3% |
| Q5_K_M | 19.1 | 0.0581 | 91.3% |
| i1-Q4_K_M | 16.8 | 0.0694 | 91.0% |
| i1-IQ4_XS | 13.9 | 0.1015 | 89.3% |
| Q4_K_M (static) | 16.8 | 0.1507 | 85.9% |
| i1-IQ3_M | 12.4 | 0.1455 | 86.0% |
| i1-IQ2_M | 10.4 | 0.3997 | 77.4% |

Pick i1-Q4_K_M or i1-IQ4_XS unless you have room for Q6_K. Two things worth knowing if you convert or evaluate GGUFs yourself: llama.cpp's pinned transformers 4.57.6 reads `extra_special_tokens` in `tokenizer_config.json` as a dict, and Gemma 4 checkpoints saved by transformers 5 store it as a list (the repo now ships the dict form, so conversion works out of the box; Google's own checkpoints need the same one-line edit or `transformers>=5`). And `llama-perplexity` on raw text reports perplexities in the tens of thousands for every Gemma 4 IT model, ours included, because their likelihoods are only calibrated inside a model turn; the KLD numbers above were measured with the model-turn prefix inserted at the start of each chunk. Details are in the GGUF repo READMEs.

A few notes from running it on the arena:

- **Sampling.** The shipped `generation_config.json` (temperature 1.0, top-p 0.95, top-k 64) is a good default; the arena battles ran on the serving defaults for this checkpoint. Temperature 0.8 to 1.0 all work; going much lower flattens the prose.
- **Length.** Left alone, the model writes 400 to 500 tokens in English. If you want tighter replies, say so in the system prompt: `Respond in no more than N tokens.` is the exact line used for the budget variant above, and the model honors it.
- **System prompt.** Any Gemma-style role-play prompt works. The two templates used in the arena were a compact card (character block, user block, formatting rules, as in the example) and a longer "narrative principles" prompt; the model was trained under a light prompt and does not need elaborate instructions to stay in character.
- **Multilingual.** Set the expected language in the system prompt (`Respond in Spanish.`) when the conversation language is not obvious from the first message.
- **Multimodal.** The vision tower from Gemma 4 is present and untouched. It was frozen during RL and we have not evaluated image inputs in role-play.

## Limitations

- **It writes long.** RL against a human-preference reward increased verbosity, and part of the model's arena win rate comes from that. Use a length budget if your product needs terse replies, and expect the length-controlled quality to be mid-pack among current frontier and near-frontier models.
- **The arena judges one reply at a time.** Every battle asks a user to choose between two candidate replies to the same message; the surrounding conversation is mostly written by the model the user normally chats with, and only the sampled turn comes from WaifuGemma4. The win rates are therefore reply-level preferences inside real contexts. They say less about what happens when this model writes every turn of a long session: drift in voice over dozens of exchanges, repetition, keeping track of details it introduced itself, pacing a plot it is steering alone. The model was trained on 8K-token contexts and our in-house checks on 972 multi-turn conversations look fine, but sustained multi-turn quality has not been measured by users the way single replies have.
- **Realism and restraint are its relative weak spots.** Voters who preferred an opponent cited realism and coherence more often than voters who preferred this model. In long scenes it can escalate faster than the situation calls for.
- **It occasionally narrates the user.** "Doesn't speak for me" is a common vote reason across all models on the arena, and this one is not immune. A "Never speak or act for {user}" line in the system prompt helps.
- **Preference is a different thing from safety.** The reward model learned what users on a role-play platform prefer, which includes mature themes, and the model will write explicit content when the system prompt allows it. It has had no safety tuning beyond what the base model carries. Deploy it behind the content policy and filtering appropriate to your audience; our own system prompts carry an explicit prohibition on sexual content involving minors, and we recommend the same.
- **The evaluation is one platform's users.** 16,035 voters over two days on HiWaifu, mostly writing in Spanish and Russian. Numbers on a different population or a different arena will differ.
- **The reward model is modest.** 0.57 pairwise accuracy against a noisy label, and nothing we trained on this label beat 0.6 without learning a shortcut. It was enough to move the policy in a direction users noticed, but we expect more headroom from a better reward model than from more RL steps against this one.

## What's next

- **Length-aware reward.** A run with `reward = arena_rm + 1[length ≤ 300 tokens]` is training now; the mean completion length holds at about 300 tokens while the arena reward still climbs. It goes into the arena next.
- **A thinking model for role-play.** The next major version will reason before it replies. Gemma 4 ships with a thinking mode, and we plan to train it to think *as the character*: a short first-person deliberation about what the character knows, wants and notices in the scene, followed by the visible reply. The reward combines the arena RM on the visible reply with checks that the thinking stays in the character's perspective and stays short. Our bet is that in-character deliberation is where the remaining gaps show up in the vote reasons (realism, coherence, speaking for the user) and where a 3.8B-active model can buy the most quality per token.
- **Larger models.** The same recipe applies unchanged to the dense Gemma 4 31B, and the arena reward model is base-agnostic. We plan to train a larger WaifuGemma4 with the same reward model and put it through the same arena, which also tells us how much of the current result is the reward and how much is the base.
- **A reward model trained on more of the arena**, including the long tail of languages, and a distilled version cheap enough to run as a reranker at inference time, in the spirit of [Irvine et al.](https://arxiv.org/abs/2303.06135).
- **Style.** Scene and environment writing is the base model's weakest register; a style-focused SFT stage before RL is planned.

## Related work

Learning rewards from production users has precedents. Chai Research trained reward models on engagement pseudo-labels (continuation, retries) and used them for best-of-N selection, reporting a 30% lift in day-30 retention ([Irvine et al., 2023](https://arxiv.org/abs/2303.06135)). Meta's RLUF trains a P[Love] reward from emoji reactions and optimizes it alongside helpfulness and safety, and notes that the largest effects show up in role-play and companionship conversations ([Han et al., 2025](https://arxiv.org/abs/2505.14946)). Our signal is a direct pairwise choice between two replies to the same context, which is closer to the classic RLHF label and avoids some of the confounds of engagement metrics, at the cost of only being available where an arena exists.

On the role-play side, CoSER built a literary dataset and an LLM-judged benchmark and trained CoSER-70B with SFT ([Wang et al., ICML 2025](https://arxiv.org/abs/2502.09082)); HER trains a generative reward model on principle-guided synthetic preferences and applies RL to Qwen3-32B, with large gains on CoSER and the MiniMax Role-Play Bench ([Du et al., 2026](https://arxiv.org/abs/2601.21459)). Both use a model as the judge of what good role-play is. We used the audience.

The length dynamics we report match the general RLHF findings of [Singhal et al. (2023)](https://arxiv.org/abs/2310.03716), and our leaderboard's length control follows [LMArena's style-control methodology](https://arena.ai/blog/style-control). GRPO is from [Shao et al. (2024)](https://arxiv.org/abs/2402.03300). The base model is described in the [Gemma 4 report](https://arxiv.org/abs/2607.02770).

## Citation

```bibtex
@misc{hiwaifu2026waifugemma4,
  title   = {WaifuGemma4-26b-a4b-v1: Role-play Post-training from Real User Preference Votes},
  author  = {HiWaifu Research},
  year    = {2026},
  url     = {https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1}
}
```

## License

Apache 2.0, the same license Google released Gemma 4 under. Use it, fine-tune it, ship it; attribution and the license text are all that is asked.
