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

# LFM2-1.2B-Tool

Based on [LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B), LFM2-1.2B-Tool is designed for **concise and precise tool calling**. The key challenge was designing a non-thinking model that outperforms similarly sized thinking models for tool use.

**Use cases**:

- Mobile and edge devices requiring instant API calls, database queries, or system integrations without cloud dependency.
- Real-time assistants in cars, IoT devices, or customer support, where response latency is critical.
- Resource-constrained environments like embedded systems or battery-powered devices needing efficient tool execution.

You can find more information about other task-specific models in this [blog post](https://www.liquid.ai/blog/introducing-liquid-nanos-frontier-grade-performance-on-everyday-devices).

## 📄 Model details

**Generation parameters**: We recommend using greedy decoding with a `temperature=0`.

**System prompt**: The system prompt must provide all the available tools

**Supported languages**: English, Arabic, Chinese, French, German, Japanese, Korean, Portuguese, and Spanish.

![68d41b9699b7e1fafd645300_Model Library-Prompt + Answer](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/dc2-lsJ5PwoA8039z-wW_.png)

**Tool use**: It consists of four main steps:
1. **Function definition**: LFM2 takes JSON function definitions as input (JSON objects between `<|tool_list_start|>` and `<|tool_list_end|>` special tokens), usually in the system prompt
2. **Function call**: LFM2 writes Pythonic function calls (a Python list between `<|tool_call_start|>` and `<|tool_call_end|>` special tokens), as the assistant answer.
3. **Function execution**: The function call is executed and the result is returned (string between `<|tool_response_start|>` and `<|tool_response_end|>` special tokens), as a "tool" role.
4. **Final answer**: LFM2 interprets the outcome of the function call to address the original user prompt in plain text.

Here is a simple example of a conversation using tool use:

```
<|startoftext|><|im_start|>system
List of tools: <|tool_list_start|>[{"name": "get_candidate_status", "description": "Retrieves the current status of a candidate in the recruitment process", "parameters": {"type": "object", "properties": {"candidate_id": {"type": "string", "description": "Unique identifier for the candidate"}}, "required": ["candidate_id"]}}]<|tool_list_end|><|im_end|>
<|im_start|>user
What is the current status of candidate ID 12345?<|im_end|>
<|im_start|>assistant
<|tool_call_start|>[get_candidate_status(candidate_id="12345")]<|tool_call_end|>Checking the current status of candidate ID 12345.<|im_end|>
<|im_start|>tool
<|tool_response_start|>{"candidate_id": "12345", "status": "Interview Scheduled", "position": "Clinical Research Associate", "date": "2023-11-20"}<|tool_response_end|><|im_end|>
<|im_start|>assistant
The candidate with ID 12345 is currently in the "Interview Scheduled" stage for the position of Clinical Research Associate, with an interview date set for 2023-11-20.<|im_end|>
```

> [!WARNING]
> ⚠️ The model supports both single-turn and multi-turn conversations.

## 📈 Performance

For edge inference, latency is a crucial factor in delivering a seamless and satisfactory user experience. Consequently, while test-time-compute inherently provides more accuracy, it ultimately compromises the user experience due to increased waiting times for function calls.

Therefore, the goal was to develop a tool calling model that is competitive with thinking models, yet operates without any internal chain-of-thought process.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/gdPh7juYTsxc7wpD5iYS_.png)

We evaluated each model on a proprietary benchmark that was specifically designed to prevent data contamination. The benchmark ensures that performance metrics reflect genuine tool-calling capabilities rather than memorized patterns from training data.

## 🏃 How to run

- Hugging Face: [LFM2-1.2B-Tool](https://huggingface.co/LiquidAI/LFM2-1.2B-Tool)
- llama.cpp: [LFM2-1.2B-Tool-GGUF](https://huggingface.co/LiquidAI/LFM2-1.2B-Tool-GGUF)
- LEAP: [LEAP model library](https://leap.liquid.ai/models?model=lfm2-1.2b-tool)

You can use the following Colab notebooks for easy inference and fine-tuning:

| Notebook | Description | Link |
|-------|------|------|
| Inference | Run the model with Hugging Face's transformers library. | <a href="https://colab.research.google.com/drive/1_HFBuNROTnI-SSZ2zEpqpjJ6SnrsWCU3?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
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