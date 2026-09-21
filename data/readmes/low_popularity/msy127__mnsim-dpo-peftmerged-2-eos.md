---
license: llama2
language:
- ko
- en
library_name: transformers
---

---
license: llama2
language:
- ko
- en
library_name: transformers
base_model: mncai/llama2-13b-dpo-v7
pipeline_tag: text-generation
---

# **mnsim-dpo-peftmerged-2-eos**


## Our Team

| Research & Engineering | Product Management |
| :--------------------: | :----------------: |
|     David Sohn         |      David Sohn    |


## **Model Details**

### **Base Model**

[mncai/llama2-13b-dpo-v7](https://huggingface.co/mncai/llama2-13b-dpo-v7)

### **Trained On**

-   **OS**: Ubuntu 22.04
-   **GPU**: A100 40GB 1ea
-   **transformers**: v4.35.2

### **Instruction format**

It follows **Custom** format.

E.g.

```python
text = """\
<s>
<|user|>
건강한 식습관을 만들기 위해서는 어떻게 하는것이 좋을까요?
<|assistant|>
"""
```


## **Implementation Code**

This model contains the chat_template instruction format.  
You can use the code below.

```python
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="msy127/mnsim-dpo-peftmerged-2-eos")

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("msy127/mnsim-dpo-peftmerged-2-eos")
model = AutoModelForCausalLM.from_pretrained("msy127/mnsim-dpo-peftmerged-2-eos")
```

## **Introduction to our service platform**
- AI Companion service platform that talks while looking at your face.
- You can preview the future of the world's best, character.ai.
- https://livetalkingai.com