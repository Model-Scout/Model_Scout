---
datasets:
- tiiuae/falcon-refinedweb
language:
- zh
- en
- fr
- de
- ja
- ko
- it
- ru
pipeline_tag: text-generation
inference: false
library_name: transformers
license: apache-2.0
---

> ⚠️ **ARCHIVED / LEGACY MODEL NOTICE**  
> This repository is part of a legacy collection quantized around 2023. To manage storage quotas and maintain active community projects, some rarely used quantization formats (e.g., Q2_K, Q3_K, Q4_1, Q5_1) have been permanently removed. 
> 
> Only the most popular and stable formats (**Q4_0, Q4_K_M, Q5_K_M, Q6_K, and Q8_0**) remain available.
> 
> 💡 **Looking for something modern?** 
> If you are starting a new project, we highly recommend using newer architectures (like Llama 3, Mistral, or Qwen) provided by official maintainers or active community members (e.g., `Bartowski`, `TheBloke` legacy files, or official organization handles).
> 
> ⚠️ *This repository is no longer actively maintained. Existing files are provided "as is" for archival and legacy hardware purposes.*

[![banner](https://maddes8cht.github.io/assets/buttons/Huggingface-banner.jpg)]()

I'm constantly enhancing these model descriptions to provide you with the most relevant and comprehensive information

# openbuddy-falcon-7b-v5-fp16 - GGUF
- Model creator: [OpenBuddy](https://huggingface.co/OpenBuddy)
- Original model: [openbuddy-falcon-7b-v5-fp16](https://huggingface.co/OpenBuddy/openbuddy-falcon-7b-v5-fp16)

# K-Quants in Falcon 7b models

New releases of Llama.cpp now support K-quantization for previously incompatible models, in particular all Falcon 7B models (While Falcon 40b is and always has been fully compatible with K-Quantisation). This is achieved by employing a fallback solution for model layers that cannot be quantized with real K-quants.

For Falcon 7B models, although only a quarter of the layers can be quantized with true K-quants, this approach still benefits from utilizing *different* legacy quantization types Q4_0, Q4_1, Q5_0, and Q5_1. As a result, it offers better quality at the same file size or smaller file sizes with comparable performance.

So this solution ensures improved performance and efficiency over legacy Q4_0, Q4_1, Q5_0 and Q5_1 Quantizations.




---
# Brief
OpenBuddy provides strong multiligual Model variants. On their Huggingface Organization Card they say:

> Our mission with OpenBuddy is to provide a free, open, and offline-capable AI model that operates on users' devices, irrespective of their language or cultural background. We strive to empower individuals worldwide to access and benefit from AI technology.


---



# About GGUF format

`gguf` is the current file format used by the [`ggml`](https://github.com/ggerganov/ggml) library.
A growing list of Software is using it and can therefore use this model.
The core project making use of the ggml library is the [llama.cpp](https://github.com/ggerganov/llama.cpp) project by Georgi Gerganov

# Quantization variants

There is a bunch of quantized files available to cater to your specific needs. Here's how to choose the best option for you:

# Legacy quants

Q4_0, Q4_1, Q5_0, Q5_1 and Q8 are `legacy` quantization types.
Nevertheless, they are fully supported, as there are several circumstances that cause certain model not to be compatible with the modern K-quants.
## Note:
Now there's a new option to use K-quants even for previously 'incompatible' models, although this involves some fallback solution that makes them not *real* K-quants. More details can be found in affected model descriptions.
(This mainly refers to Falcon 7b and Starcoder models)

# K-quants

K-quants are designed with the idea that different levels of quantization in specific parts of the model can optimize performance, file size, and memory load.
So, if possible, use K-quants.
With a Q6_K, you'll likely find it challenging to discern a quality difference from the original model - ask your model two times the same question and you may encounter bigger quality differences.




---

# Original Model Card:
# OpenBuddy - Open Multilingual Chatbot based on Falcon

GitHub and Usage Guide: [https://github.com/OpenBuddy/OpenBuddy](https://github.com/OpenBuddy/OpenBuddy)

Website and Demo: [https://openbuddy.ai](https://openbuddy.ai)

![Demo](https://raw.githubusercontent.com/OpenBuddy/OpenBuddy/main/media/demo.png)

## Disclaimer

All OpenBuddy models have inherent limitations and may potentially produce outputs that are erroneous, harmful, offensive, or otherwise undesirable. Users should not use these models in critical or high-stakes situations that may lead to personal injury, property damage, or significant losses. Examples of such scenarios include, but are not limited to, the medical field, controlling software and hardware systems that may cause harm, and making important financial or legal decisions.

OpenBuddy is provided "as-is" without any warranty of any kind, either express or implied, including, but not limited to, the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors, contributors, or copyright holders be liable for any claim, damages, or other liabilities, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

By using OpenBuddy, you agree to these terms and conditions, and acknowledge that you understand the potential risks associated with its use. You also agree to indemnify and hold harmless the authors, contributors, and copyright holders from any claims, damages, or liabilities arising from your use of OpenBuddy.


## 免责声明

所有OpenBuddy模型均存在固有的局限性，可能产生错误的、有害的、冒犯性的或其他不良的输出。用户在关键或高风险场景中应谨慎行事，不要使用这些模型，以免导致人身伤害、财产损失或重大损失。此类场景的例子包括但不限于医疗领域、可能导致伤害的软硬件系统的控制以及进行重要的财务或法律决策。

OpenBuddy按“原样”提供，不附带任何种类的明示或暗示的保证，包括但不限于适销性、特定目的的适用性和非侵权的暗示保证。在任何情况下，作者、贡献者或版权所有者均不对因软件或使用或其他软件交易而产生的任何索赔、损害赔偿或其他责任（无论是合同、侵权还是其他原因）承担责任。

使用OpenBuddy即表示您同意这些条款和条件，并承认您了解其使用可能带来的潜在风险。您还同意赔偿并使作者、贡献者和版权所有者免受因您使用OpenBuddy而产生的任何索赔、损害赔偿或责任的影响。

***End of original Model File***
---


## Please consider to support my work
**Coming Soon:** I'm in the process of launching a sponsorship/crowdfunding campaign for my work. I'm evaluating Kickstarter, Patreon, or the new GitHub Sponsors platform, and I am hoping for some support and contribution to the continued availability of these kind of models. Your support will enable me to provide even more valuable resources and maintain the models you rely on. Your patience and ongoing support are greatly appreciated as I work to make this page an even more valuable resource for the community.

<center>

[![GitHub](https://maddes8cht.github.io/assets/buttons/github-io-button.png)](https://maddes8cht.github.io)
[![Stack Exchange](https://stackexchange.com/users/flair/26485911.png)](https://stackexchange.com/users/26485911)
[![GitHub](https://maddes8cht.github.io/assets/buttons/github-button.png)](https://github.com/maddes8cht)
[![HuggingFace](https://maddes8cht.github.io/assets/buttons/huggingface-button.png)](https://huggingface.co/maddes8cht)
[![Twitter](https://maddes8cht.github.io/assets/buttons/twitter-button.png)](https://twitter.com/maddes1966)

</center>