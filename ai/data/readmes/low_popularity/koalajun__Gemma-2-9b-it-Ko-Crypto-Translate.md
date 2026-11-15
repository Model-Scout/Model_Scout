---
library_name: transformers  
license: mit  
language:  
- en  
- ko  
base_model:  
- google/gemma-2-9b-it  
---

# Model Card for Gemma-2-9b-it-Ko-Crypto-Translate

This model has been fine-tuned on a crypto news translation task. It is designed to translate English crypto news into Korean, leveraging the Gemma-2-9b-it architecture. The model is intended for natural language processing (NLP) tasks, specifically translation, within the crypto news domain.

## Model Details

### Model Description

This fine-tuned model is based on the **Gemma-2-9b-it** architecture and has been specifically trained to translate English crypto news into Korean. Fine-tuning was performed using a custom dataset focused on cryptocurrency news articles, ensuring the model's output is accurate in both language translation and crypto-specific terminology.

- **Developed by:** Hyoun Jun Lee  
- **Model type:** Gemma-2-9b-it  
- **Language(s) (NLP):** English, Korean  

### Model Sources

- **Repository:** [Hugging Face: koalajun/Gemma-2-9b-it-Ko-Crypto-Translate](https://huggingface.co/koalajun/Gemma-2-9b-it-Ko-Crypto-Translate)

## Uses

### Direct Use

This model can be used for translating English cryptocurrency news articles into Korean. It can be integrated into applications such as financial platforms or news websites to provide real-time translation of crypto news.

### Downstream Use

The model can be further fine-tuned for more specific translation tasks in the financial or legal domains. Additionally, it can be used as a basis for other translation or language generation tasks that require bilingual capabilities in English and Korean.

### Out-of-Scope Use

This model is not intended for general translation tasks outside the financial/crypto domain. It may not perform well in non-financial contexts, as it was fine-tuned with specialized crypto-related datasets.

## Bias, Risks, and Limitations

Given the specific nature of the dataset (crypto news), the model may introduce biases related to the financial or crypto sector. The translation might also be less effective for general or non-financial text, and there could be inaccuracies in domain-specific terms.

### Recommendations

Users should validate the model's output in critical applications, especially when used in real-time financial decision-making or for publications where accuracy is paramount.

## How to Get Started with the Model

To use this model for inference, you can load it using the Hugging Face `transformers` library as follows:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "koalajun/Gemma-2-9b-it-Ko-Crypto-Translate"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

# Define the input prompt for testing
prompt = "Translate the latest crypto news from English to Korean: Bitcoin prices continue to rise, surpassing $30,000 this week."

# Tokenize the input prompt
inputs = tokenizer(prompt, return_tensors="pt").to(device)

# Generate response from the model
outputs = model.generate(inputs.input_ids, max_length=200, num_return_sequences=1)

# Decode and print the generated text (translation)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Translation:", response)
