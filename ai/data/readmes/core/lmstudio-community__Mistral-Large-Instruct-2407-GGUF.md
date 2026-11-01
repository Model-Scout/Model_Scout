---
base_model: mistralai/Mistral-Large-Instruct-2407
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
license: other
license_name: mrl
license_link: https://mistral.ai/licenses/MRL-0.1.md
pipeline_tag: text-generation
quantized_by: bartowski
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
---
## 💫 Community Model> Mistral Large Instruct 2407 by Mistralai

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [mistralai](https://huggingface.co/mistralai)<br>
**Original model**: [Mistral-Large-Instruct-2407](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b3441](https://github.com/ggerganov/llama.cpp/releases/tag/b3441)<br>

## Model Summary:
Mistral Large 2 has a 128k context window and supports dozens of languages including French, German, Spanish, Italian, Portuguese, Arabic, Hindi, Russian, Chinese, Japanese, and Korean, along with 80+ coding languages including Python, Java, C, C++, JavaScript, and Bash.

## Prompt Template:

Choose the `Mistral Instruct` preset in your LM Studio.
Under the hood, the model will see a prompt that's formatted like so:

```
<s>[INST] {prompt}[/INST] </s>
```

## Technical Details
Mistral Large 2 features enhanced instruction-following and conversational capabilities. Additionally, a significant effort was also devoted to enhancing the model’s reasoning capabilities and decreasing the model’s tendency to “hallucinate” or generate plausible-sounding but factually incorrect or irrelevant information. This was achieved by fine-tuning the model to be more cautious and discerning in its responses, ensuring that it provides reliable and accurate outputs.

Mistral Large 2 is equipped with enhanced function calling and retrieval skills and has undergone training to proficiently execute both parallel and sequential function calls, enabling it to serve as the power engine of complex business applications.

Mistral Large 2 was trained on a large proportion of multilingual data. In particular, it excels in English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, and Hindi. Below are the performance results of Mistral Large 2 on the multilingual MMLU benchmark, compared to the previous Mistral Large, Llama 3.1 models, and to Cohere’s Command R+.

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

🙏 Special thanks to [Kalomaze](https://github.com/kalomaze) for his dataset (linked [here](https://github.com/ggerganov/llama.cpp/discussions/5263)) that was used for calculating the imatrix for the IQ1_M and IQ2_XS quants, which makes them usable even at their tiny size!

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.
