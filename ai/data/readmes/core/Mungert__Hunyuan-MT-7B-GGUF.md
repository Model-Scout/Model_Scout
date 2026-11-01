---
library_name: transformers
tags:
- translation
language:
- zh
- en
- fr
- pt
- es
- ja
- tr
- ru
- ar
- ko
- th
- it
- de
- vi
- ms
- id
- tl
- hi
- pl
- cs
- nl
- km
- my
- fa
- gu
- ur
- te
- mr
- he
- bn
- ta
- uk
- bo
- kk
- mn
- ug
---

# <span style="color: #7FFF7F;">Hunyuan-MT-7B GGUF Models</span>


## <span style="color: #7F7FFF;">Model Generation Details</span>

This model was generated using [llama.cpp](https://github.com/ggerganov/llama.cpp) at commit [`c8dedc99`](https://github.com/ggerganov/llama.cpp/commit/c8dedc9999eccf7821a9fe5b29f10e8d075e2217).





---

## <span style="color: #7FFF7F;">Quantization Beyond the IMatrix</span>

I've been experimenting with a new quantization approach that selectively elevates the precision of key layers beyond what the default IMatrix configuration provides.

In my testing, standard IMatrix quantization underperforms at lower bit depths, especially with Mixture of Experts (MoE) models. To address this, I'm using the `--tensor-type` option in `llama.cpp` to manually "bump" important layers to higher precision. You can see the implementation here:  
👉 [Layer bumping with llama.cpp](https://github.com/Mungert69/GGUFModelBuilder/blob/main/model-converter/tensor_list_builder.py)

While this does increase model file size, it significantly improves precision for a given quantization level.

### **I'd love your feedback—have you tried this? How does it perform for you?**




---

<a href="https://readyforquantum.com/huggingface_gguf_selection_guide.html" style="color: #7FFF7F;">
  Click here to get info on choosing the right GGUF model format
</a>

---



<!--Begin Original Model Card-->



<p align="center">
 <img src="https://dscache.tencent-cloud.cn/upload/uploader/hunyuan-64b418fd052c033b228e04bc77bbc4b54fd7f5bc.png" width="400"/> <br>
</p><p></p>


<p align="center">
    🤗&nbsp;<a href="https://huggingface.co/collections/tencent/hunyuan-mt-68b42f76d473f82798882597"><b>Hugging Face</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
    🕹️&nbsp;<a href="https://hunyuan.tencent.com/modelSquare/home/list"><b>Demo</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
    🤖&nbsp;<a href="https://modelscope.cn/collections/Hunyuan-MT-2ca6b8e1b4934f"><b>ModelScope</b></a>
</p>

<p align="center">
    🖥️&nbsp;<a href="https://hunyuan.tencent.com"><b>Official Website</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="https://github.com/Tencent-Hunyuan/Hunyuan-MT"><b>GitHub</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="https://www.arxiv.org/abs/2509.05209"><b>Technical Report</b></a>
</p>


## Model Introduction

The Hunyuan Translation Model comprises a translation model, Hunyuan-MT-7B, and an ensemble model, Hunyuan-MT-Chimera. The translation model is used to translate source text into the target language, while the ensemble model integrates multiple translation outputs to produce a higher-quality result. It primarily supports mutual translation among 33 languages, including five ethnic minority languages in China.

### Key Features and Advantages

- In the WMT25 competition, the model achieved first place in 30 out of the 31 language categories it participated in.
- Hunyuan-MT-7B achieves industry-leading performance among models of comparable scale
- Hunyuan-MT-Chimera-7B is the industry’s first open-source translation ensemble model, elevating translation quality to a new level
- A comprehensive training framework for translation models has been proposed, spanning from pretrain → cross-lingual pretraining (CPT) → supervised fine-tuning (SFT) → translation enhancement → ensemble refinement, achieving state-of-the-art (SOTA) results for models of similar size

## Related News
* 2025.9.1 We have open-sourced  **Hunyuan-MT-7B** , **Hunyuan-MT-Chimera-7B** on Hugging Face.
<br>


&nbsp;

## 模型链接
| Model Name  | Description | Download |
| ----------- | ----------- |-----------
| Hunyuan-MT-7B  | Hunyuan 7B translation model |🤗 [Model](https://huggingface.co/tencent/Hunyuan-MT-7B)|
| Hunyuan-MT-7B-fp8 | Hunyuan 7B translation model，fp8 quant    | 🤗 [Model](https://huggingface.co/tencent/Hunyuan-MT-7B-fp8)|
| Hunyuan-MT-Chimera | Hunyuan 7B translation ensemble model    | 🤗 [Model](https://huggingface.co/tencent/Hunyuan-MT-Chimera-7B)|
| Hunyuan-MT-Chimera-fp8 | Hunyuan 7B translation ensemble model，fp8 quant     | 🤗 [Model](https://huggingface.co/tencent/Hunyuan-MT-Chimera-7B-fp8)|

## Prompts

### Prompt Template for ZH<=>XX Translation.

```

把下面的文本翻译成<target_language>，不要额外解释。

<source_text>

```

### Prompt Template for XX<=>XX Translation, excluding ZH<=>XX.

```

Translate the following segment into <target_language>, without additional explanation.

<source_text>

```

### Prompt Template for Hunyuan-MT-Chmeria-7B

```

Analyze the following multiple <target_language> translations of the <source_language> segment surrounded in triple backticks and generate a single refined <target_language> translation. Only output the refined translation, do not explain.

The <source_language> segment:
```<source_text>```

The multiple <target_language> translations:
1. ```<translated_text1>```
2. ```<translated_text2>```
3. ```<translated_text3>```
4. ```<translated_text4>```
5. ```<translated_text5>```
6. ```<translated_text6>```

```

&nbsp;

### Use with transformers
First, please install transformers, recommends v4.56.0
```SHELL
pip install transformers==v4.56.0
```

The following code snippet shows how to use the transformers library to load and apply the model.

*!!! If you want to load fp8 model with transformers, you need to change the name"ignored_layers" in config.json to "ignore" and upgrade the compressed-tensors to compressed-tensors-0.11.0.*

we use tencent/Hunyuan-MT-7B for example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

model_name_or_path = "tencent/Hunyuan-MT-7B"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map="auto")  # You may want to use bfloat16 and/or move to GPU here
messages = [
    {"role": "user", "content": "Translate the following segment into Chinese, without additional explanation.\n\nIt’s on the house."},
]
tokenized_chat = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=False,
    return_tensors="pt"
)

outputs = model.generate(tokenized_chat.to(model.device), max_new_tokens=2048)
output_text = tokenizer.decode(outputs[0])
```

We recommend using the following set of parameters for inference. Note that our model does not have the default system_prompt.

```json
{
  "top_k": 20,
  "top_p": 0.6,
  "repetition_penalty": 1.05,
  "temperature": 0.7
}
```

Supported languages:
| Languages         | Abbr.   | Chinese Names   |
|-------------------|---------|-----------------|
| Chinese           | zh      | 中文            |
| English           | en      | 英语            |
| French            | fr      | 法语            |
| Portuguese        | pt      | 葡萄牙语        |
| Spanish           | es      | 西班牙语        |
| Japanese          | ja      | 日语            |
| Turkish           | tr      | 土耳其语        |
| Russian           | ru      | 俄语            |
| Arabic            | ar      | 阿拉伯语        |
| Korean            | ko      | 韩语            |
| Thai              | th      | 泰语            |
| Italian           | it      | 意大利语        |
| German            | de      | 德语            |
| Vietnamese        | vi      | 越南语          |
| Malay             | ms      | 马来语          |
| Indonesian        | id      | 印尼语          |
| Filipino          | tl      | 菲律宾语        |
| Hindi             | hi      | 印地语          |
| Traditional Chinese | zh-Hant| 繁体中文        |
| Polish            | pl      | 波兰语          |
| Czech             | cs      | 捷克语          |
| Dutch             | nl      | 荷兰语          |
| Khmer             | km      | 高棉语          |
| Burmese           | my      | 缅甸语          |
| Persian           | fa      | 波斯语          |
| Gujarati          | gu      | 古吉拉特语      |
| Urdu              | ur      | 乌尔都语        |
| Telugu            | te      | 泰卢固语        |
| Marathi           | mr      | 马拉地语        |
| Hebrew            | he      | 希伯来语        |
| Bengali           | bn      | 孟加拉语        |
| Tamil             | ta      | 泰米尔语        |
| Ukrainian         | uk      | 乌克兰语        |
| Tibetan           | bo      | 藏语            |
| Kazakh            | kk      | 哈萨克语        |
| Mongolian         | mn      | 蒙古语          |
| Uyghur            | ug      | 维吾尔语        |
| Cantonese         | yue     | 粤语            |


Citing Hunyuan-MT:

```bibtex
@misc{hunyuan_mt,
      title={Hunyuan-MT Technical Report}, 
      author={Mao Zheng and Zheng Li and Bingxin Qu and Mingyang Song and Yang Du and Mingrui Sun and Di Wang},
      year={2025},
      eprint={2509.05209},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.05209}, 
}
```

<!--End Original Model Card-->

---

# <span id="testllm" style="color: #7F7FFF;">🚀 If you find these models useful</span>

Help me test my **AI-Powered Quantum Network Monitor Assistant** with **quantum-ready security checks**:  

👉 [Quantum Network Monitor](https://readyforquantum.com/?assistant=open&utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface_repo_readme)  


The full Open Source Code for the Quantum Network Monitor Service available at my github repos ( repos with NetworkMonitor in the name) : [Source Code Quantum Network Monitor](https://github.com/Mungert69). You will also find the code I use to quantize the models if you want to do it yourself [GGUFModelBuilder](https://github.com/Mungert69/GGUFModelBuilder)

💬 **How to test**:  
 Choose an **AI assistant type**:  
   - `TurboLLM` (GPT-4.1-mini)  
   - `HugLLM` (Hugginface Open-source models)  
   - `TestLLM` (Experimental CPU-only)  

### **What I’m Testing**  
I’m pushing the limits of **small open-source models for AI network monitoring**, specifically:  
- **Function calling** against live network services  
- **How small can a model go** while still handling:  
  - Automated **Nmap security scans**  
  - **Quantum-readiness checks**  
  - **Network Monitoring tasks**  

🟡 **TestLLM** – Current experimental model (llama.cpp on 2 CPU threads on huggingface docker space):  
- ✅ **Zero-configuration setup**  
- ⏳ 30s load time (slow inference but **no API costs**) . No token limited as the cost is low.
- 🔧 **Help wanted!** If you’re into **edge-device AI**, let’s collaborate!  

### **Other Assistants**  
🟢 **TurboLLM** – Uses **gpt-4.1-mini** :
- **It performs very well but unfortunatly OpenAI charges per token. For this reason tokens usage is limited. 
- **Create custom cmd processors to run .net code on Quantum Network Monitor Agents**
- **Real-time network diagnostics and monitoring**
- **Security Audits**
- **Penetration testing** (Nmap/Metasploit)  

🔵 **HugLLM** – Latest Open-source models:  
- 🌐 Runs on Hugging Face Inference API. Performs pretty well using the lastest models hosted on Novita.

### 💡 **Example commands you could test**:  
1. `"Give me info on my websites SSL certificate"`  
2. `"Check if my server is using quantum safe encyption for communication"`  
3. `"Run a comprehensive security audit on my server"`
4. '"Create a cmd processor to .. (what ever you want)" Note you need to install a [Quantum Network Monitor Agent](https://readyforquantum.com/Download/?utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface_repo_readme) to run the .net code on. This is a very flexible and powerful feature. Use with caution!

### Final Word

I fund the servers used to create these model files, run the Quantum Network Monitor service, and pay for inference from Novita and OpenAI—all out of my own pocket. All the code behind the model creation and the Quantum Network Monitor project is [open source](https://github.com/Mungert69). Feel free to use whatever you find helpful.

If you appreciate the work, please consider [buying me a coffee](https://www.buymeacoffee.com/mahadeva) ☕. Your support helps cover service costs and allows me to raise token limits for everyone.

I'm also open to job opportunities or sponsorship.

Thank you! 😊
