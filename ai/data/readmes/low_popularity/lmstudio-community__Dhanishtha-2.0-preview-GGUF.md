---
quantized_by: bartowski
pipeline_tag: text-generation
base_model: HelpingAI/Dhanishtha-2.0-preview
base_model_relation: quantized
license: apache-2.0
language:
- en
- hi
- pa
- ur
- ar
- te
- ta
- ml
- gu
- he
- ru
- ko
- ms
- kn
- as
- es
- fr
- de
- ja
- pt
datasets:
- Abhaykoul/Dhanishtha-R1
- open-thoughts/OpenThoughts-114k
- Abhaykoul/Dhanishtha-2.0-SUPERTHINKER
- Abhaykoul/Dhanishtha-2.0
---
## 💫 Community Model> Dhanishtha 2.0 preview by Helpingai

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [HelpingAI](https://huggingface.co/HelpingAI)<br>
**Original model**: [Dhanishtha-2.0-preview](https://huggingface.co/HelpingAI/Dhanishtha-2.0-preview)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b5760](https://github.com/ggerganov/llama.cpp/releases/tag/b5760)<br>

## Technical Details

Supports a context length of 40k tokens

Dhanishtha-2.0 is a groundbreaking reasoning AI model developed by HelpingAI, representing the first model to feature Intermediate thinking capabilities. Unlike traditional models that provide single-pass responses, Dhanishtha-2.0 employs a revolutionary multi-phase thinking process that allows the model to think, reconsider, and refine its reasoning multiple times throughout a single response.

- World's First Intermediate Thinking Model: Uniquely capable of multiple thinking phases throughout a single response, enabling deeper analysis and self-correction during generation.
- Dynamic Reasoning: Seamlessly integrates <think>...</think> blocks at any point in the response, allowing for real-time problem decomposition and iterative refinement.
- Enhanced Problem-Solving Architecture: Excels at complex riddles, multi-step reasoning, and scenarios requiring backtracking and re-evaluation of initial assumptions.
- Structured Emotional Intelligence: Incorporates SER (Structured Emotional Reasoning) with <ser>...</ser> blocks for empathetic and contextually aware responses.
- Bilingual Reasoning Capabilities: Native support for English and Hindi with natural code-switching between languages.

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.
