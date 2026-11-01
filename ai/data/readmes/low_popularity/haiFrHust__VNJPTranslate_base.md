---
license: mit
datasets:
- bkai-foundation-models/vi-alpaca-input-output-format
- CausalLM/GPT-4-Self-Instruct-Japanese
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
pipeline_tag: question-answering
library_name: transformers
---

# Multilingual Question-Answering Model (Vietnamese and Japanese)

## Overview

This repository contains a fine-tuned multilingual question-answering model that supports both **Vietnamese** and **Japanese**. Built on top of the **Qwen/Qwen2.5-1.5B-Instruct** base model, this model leverages advanced transformer architectures to provide high-quality answers in both languages.

The model has been fine-tuned using datasets such as:
- **bkai-foundation-models/vi-alpaca-input-output-format**: A Vietnamese dataset designed for instruction-based input-output tasks.
- **CausalLM/GPT-4-Self-Instruct-Japanese**: A Japanese dataset created with self-instruct techniques to improve language understanding and generation.

This model is ideal for applications requiring cross-lingual support between Vietnamese and Japanese.

---

## License

This project is released under the **MIT License**, ensuring flexibility for both academic and commercial use. Please refer to the `LICENSE` file for more details.

---

## Model Details

### Base Model
- **Qwen/Qwen2.5-1.5B-Instruct**: A powerful 1.5B parameter instruction-tuned model developed by Alibaba Cloud. It excels in understanding and generating natural language across various domains.

### Supported Languages
- **Vietnamese (vi)**
- **Japanese (ja)**

### Pipeline Tag
- **Question-Answering**: The model is optimized for answering questions in both supported languages.

### Library
- **Transformers**: This model is built using the Hugging Face `transformers` library, making it easy to integrate into existing pipelines.

---

## Installation

To use this model, ensure you have the `transformers` library installed:

```bash
pip install transformers
```

You can then load the model directly from the Hugging Face Hub:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("haiFrHust/VNJPTranslate_base")
model = AutoModelForCausalLM.from_pretrained("haiFrHust/VNJPTranslate_base")

# Example usage
input_text = "質問: ベトナムの首都はどこですか？"  # Japanese: What is the capital of Vietnam?
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs)
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(answer)
```


---

## Dataset Information

### Vietnamese Dataset
- **Name**: `bkai-foundation-models/vi-alpaca-input-output-format`
- **Description**: This dataset contains instruction-based input-output pairs in Vietnamese, enabling the model to understand and respond to structured queries effectively.

### Japanese Dataset
- **Name**: `CausalLM/GPT-4-Self-Instruct-Japanese`
- **Description**: A self-instruct dataset in Japanese, designed to enhance the model's ability to generate accurate and contextually relevant responses.

---

## Use Cases

This model is suitable for a variety of applications, including but not limited to:
- **Cross-Lingual Customer Support**: Answering user queries in both Vietnamese and Japanese.
- **Educational Tools**: Assisting students in learning and understanding concepts in their native language.
- **Multilingual Chatbots**: Building conversational agents capable of handling multiple languages seamlessly.

---

## Performance

The model demonstrates strong performance in both Vietnamese and Japanese, thanks to the high-quality datasets and the robust base model. However, performance may vary depending on the complexity of the questions and the domain-specific knowledge required.

For optimal results:
- Ensure your input questions are clear and concise.
- Fine-tune the model further on domain-specific data if necessary.

---

## Contributions

Contributions to this project are welcome! If you have ideas for improvements, encounter issues, or wish to contribute additional datasets, please open an issue or submit a pull request.

---

## Acknowledgments

We would like to thank the following organizations and contributors:
- **Alibaba Cloud** for providing the Qwen base model.
- The creators of the `bkai-foundation-models/vi-alpaca-input-output-format` and `CausalLM/GPT-4-Self-Instruct-Japanese` datasets.
- The Hugging Face community for their excellent `transformers` library and support.

---

## Contact

For any inquiries or feedback, feel free to reach out to us via:
- Email: [hai.ph225715@sis.hust.edu.vn]
- GitHub Issues: Open an issue in this repository.

---

Thank you for using our multilingual question-answering model! We hope it serves your needs effectively.