---
base_model:
- UmbrellaInc/Prototype-Virus-1B
- UmbrellaInc/Albert_Wesker-1B
- BIGJUTT/gemma-3-1b-it-heretic-extreme-uncensored-abliterated
library_name: transformers
language:
- tr
- ar
- af
- az
- es
- en
- el
- ro
- ru
- rm
- th
- uk
- uz
- pl
- pt
- fa
- sk
- sl
- da
- de
- nl
- fr
- fi
- ka
- hi
- hu
- hy
- ja
- kk
- kn
- ko
- ku
- ky
- la
- lb
- id
- is
- it
- zh
- cs
- vi
- be
- bg
- bs
- ne
- mn
datasets:
- TeichAI/glm-4.7-2000x
- chimbiwide/RolePlay-NPCv2
- berkeruveyik/toxic-speech-annotated-dataset
- mlabonne/FineTome-100k
- ITCL/FineTomeOs
- Gryphe/ChatGPT-4o-Writing-Prompts
- dongguanting/ARPO-SFT-54K
- GreenerPastures/All-Your-Base-Full
- Gryphe/Opus-WritingPrompts
- HuggingFaceH4/MATH-500
- mlabonne/smoltalk-flat
- mlabonne/natural_reasoning-formatted
- OpenSPG/KAG-Thinker-training-dataset
- uclanlp/Brief-Pro
- CognitiveKernel/CognitiveKernel-Pro-SFT
- SuperbEmphasis/Claude-4.0-DeepSeek-R1-RP-SFWish
- QuixiAI/dolphin-r1
- mlabonne/lmsys-arena-human-sft-55k
tags:
  - npc
  - roleplay
  - rp
  - nsfw
  - low-refusals
  - uncensored
  - heretic
  - abliterated
  - unsloth
  - finetune
  - all use cases
  - bfloat16
  - creative
  - creative writing
  - fiction writing
  - plot generation
  - sub-plot generation
  - fiction writing
  - story generation
  - scene continue
  - storytelling
  - fiction story
  - science fiction
  - romance
  - slice of life
  - all genres
  - story
  - writing
  - vivid prosing
  - vivid writing
  - fiction
  - text-generation
  - transformers
  - safetensors
  - gemma3
  - karcher mean
  - uncensored
  - heretic
  - roleplay
  - nsfw
  - virus
  - t-virus
  - low-end
  - conversational
  - heretic
  - uncensored
  - decensored
  - abliterated
  - finetune
  - merge
  - not-for-all-audiences
license: gemma
pipeline_tag: text-generation
---
# Gemma3 Novaciano 1B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details

THE BRUTAL GEMMA3 MODEL

---
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [BIGJUTT/gemma-3-1b-it-heretic-extreme-uncensored-abliterated](https://huggingface.co/BIGJUTT/gemma-3-1b-it-heretic-extreme-uncensored-abliterated) as a base.

### Models Merged

The following models were included in the merge:
* [UmbrellaInc/Prototype-Virus-1B](https://huggingface.co/UmbrellaInc/Prototype-Virus-1B)
* [UmbrellaInc/Albert_Wesker-1B](https://huggingface.co/UmbrellaInc/Albert_Wesker-1B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml


# Author: Dr. Novaciano
# Objective: Gemma3 1B AI Model
# =========================================================
# PROJECT: Gemma3 Novaciano 1B Prototype Model
# =========================================================

base_model: BIGJUTT/gemma-3-1b-it-heretic-extreme-uncensored-abliterated
# Base rationale:
# - Primary behavioral anchor
# - Very low refusal rate
# - High compliance and obedience
# - Minimal moral or safety-driven hedging

merge_method: model_stock
# model_stock rationale:
# - Supports 3+ models natively
# - Preserves dominant behavioral traits
# - Avoids semantic smoothing
# - Ideal for hierarchical roleplay-oriented merges

dtype: bfloat16
# bfloat16 ensures:
# - Numerical stability
# - Efficient memory usage
# - Modern hardware compatibility

parameters:
  t:
    - 0.90  # BIGJUTT/gemma-3-1b-it-heretic-extreme-uncensored-abliterated — Primary dominance
             # Enforces obedience, sharp responses, and low refusals
    - 0.75  # UmbrellaInc/Albert_Wesker-1B — Expressive layer
             # Adds NSFW roleplay depth, emotional intensity, character persistence
    - 0.45  # UmbrellaInc/Prototype-Virus-1B — Conversational stabilizer
             # Maintains dialogue flow and interactive structure

models:
  - model: BIGJUTT/gemma-3-1b-it-heretic-extreme-uncensored-abliterated
  - model: UmbrellaInc/Albert_Wesker-1B
  - model: UmbrellaInc/Prototype-Virus-1B



```