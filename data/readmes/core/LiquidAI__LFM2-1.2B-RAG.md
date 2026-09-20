---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
base_model: LiquidAI/LFM2-1.2B
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
</div>
</center>

<br>

# LFM2-1.2B-RAG

Based on [LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B), LFM2-1.2B-RAG is specialized in answering questions based on provided contextual documents, for use in RAG (Retrieval-Augmented Generation) systems.

**Use cases**:

- Chatbot to ask questions about the documentation of a particular product.
- Custom support with an internal knowledge base to provide grounded answers.
- Academic research assistant with multi-turn conversations about research papers and course materials.

You can find more information about other task-specific models in this [blog post](https://www.liquid.ai/blog/introducing-liquid-nanos-frontier-grade-performance-on-everyday-devices).

## 📄 Model details

**Generation parameters**: We recommend using greedy decoding with a `temperature=0`.

**System prompt**: The system prompt is optional. You can force the output's language, for example, using "Always respond in English, regardless of the user's input language." By default, the output's language follows the user prompt's language.

**Supported languages**: English, Arabic, Chinese, French, German, Japanese, Korean, Portuguese, and Spanish.

![68d417d4e3a23b976f25091a_Model Library_Prompt + Answer (Medium)_Lightmode](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/Drm8eJpwx_LhNfspEmrNl.png)

**Training approach**: We fine-tuned the LFM2-1.2B-RAG model on a dataset that includes 1M+ samples of multi-turn interactions and multi-document samples consisting of a mix of curated open source documents as well as generated synthetic ones. 

**Chat template**: LFM2 uses a ChatML-like chat template as follows:

```
<|startoftext|><|im_start|>user
Use the following context to answer questions:
Beach soccer differs significantly from its grass-rooted counterpart. [...]<|im_end|>
<|im_start|>assistant
Each team in a beach soccer match consists of five players, including a goalkeeper.{<|im_end|>
```

You can automatically apply it using the dedicated [`.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#applychattemplate) function from Hugging Face transformers.

> [!WARNING]
> ⚠️ The model supports both single-turn and multi-turn conversations.

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/Thv4Lq6wPYKNEAAJq_DtP.png" 
    style="width: 100%; max-width: 50%; height: auto; display: inline-block;"
  />
</div>
</center>

RAG systems enable AI solutions to include new, up-to-date, and potentially proprietary information in LLM responses that was not present in the training data. When a user asks a question, the retrieval component locates and delivers related documents from a knowledge base, and then the RAG generator model answers the question based on facts from those contextual documents.

## 🏃 How to run

- Hugging Face: [LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B)
- llama.cpp: [LFM2-1.2B-RAG-GGUF](https://huggingface.co/LiquidAI/LFM2-1.2B-RAG-GGUF)
- LEAP: [LEAP model library](https://leap.liquid.ai/models?model=lfm2-1.2b-extract)

You can use the following Colab notebooks for easy inference and fine-tuning:

| Notebook | Description | Link |
|-------|------|------|
| Inference | Run the model with Hugging Face's transformers library. | <a href="https://colab.research.google.com/drive/1WoPOzoLBJEUjPcDiUn_R42CTdEwQ8kcv?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (TRL) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using TRL. | <a href="https://colab.research.google.com/drive/1j5Hk_SyBb2soUsuhU0eIEA9GwLNRnElF?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| DPO (TRL) | Preference alignment with Direct Preference Optimization (DPO) using TRL. | <a href="https://colab.research.google.com/drive/1MQdsPxFHeZweGsNx4RH7Ia8lG8PiGE1t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (Axolotl) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using Axolotl. | <a href="https://colab.research.google.com/drive/155lr5-uYsOJmZfO6_QZPjbs8hA_v8S7t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (Unsloth) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using Unsloth. | <a href="https://colab.research.google.com/drive/1HROdGaPFt1tATniBcos11-doVaH7kOI3?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).

## Citation

```
@article{liquidai2025lfm2,
 title={LFM2 Technical Report},
 author={Liquid AI},
 journal={arXiv preprint arXiv:2511.23404},
 year={2025}
}
```