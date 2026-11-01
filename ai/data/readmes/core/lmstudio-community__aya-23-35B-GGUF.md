---
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
license: cc-by-nc-4.0
quantized_by: bartowski
pipeline_tag: text-generation
lm_studio:
  param_count: 35b
  use_case: general
  release_date: 23-05-2024
  model_creator: CohereForAI
  prompt_template: Cohere Command R
  system_prompt: You are a helpful AI assistant
  base_model: cohere
  original_repo: CohereForAI/aya-23-35B
base_model: CohereForAI/aya-23-35B
---
## 💫 Community Model> Aya 23 35B by Cohere For AI

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [Cohere For AI](https://huggingface.co/CohereForAI)<br>
**Original model**: [aya-23-35B](https://huggingface.co/CohereForAI/aya-23-35B)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b2965](https://github.com/ggerganov/llama.cpp/releases/tag/b2965)<br>

## Model Summary:

Aya 23 are brand new instruction tuned multilingual models from Cohere. This model should perform well at logic across a wide variety of languages.<br>
This is the 35B version of the model. The performance is quite high especially when used for multilingual tasks where most other models in this size range lack training data.

## Prompt template:

Choose the `Cohere Command R` preset in your LM Studio.

Under the hood, the model will see a prompt that's formatted like so:

```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>
{system_prompt}
<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>
{prompt}
<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>

```

## Technical Details

Aya 23 covers the following languages:
 - Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese

The Aya training dataset can be found here:
 - https://huggingface.co/datasets/CohereForAI/aya_collection

More technical details can be found from Cohere [here](https://cohere.com/research/papers/aya-command-23-35b-and-35b-technical-report-2024-05-23)

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

🙏 Special thanks to [Kalomaze](https://github.com/kalomaze), [Dampf](https://github.com/Dampfinchen) and [turboderp](https://github.com/turboderp/) for their work on the dataset (linked [here](https://gist.github.com/bartowski1182/b6ac44691e994344625687afe3263b3a)) that was used for calculating the imatrix for all sizes.

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.