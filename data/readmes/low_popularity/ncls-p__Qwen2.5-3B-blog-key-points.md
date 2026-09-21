---
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
tags:
- qwen2
- text-generation
- summarization
- key-points
- blog-summarization
- unsloth
datasets:
- ncls-p/blog-key-points
license: cc-by-4.0
base_model: Qwen/Qwen2.5-3B-Instruct
---

# Qwen2.5-3B-blog-key-points

This model is fine-tuned from [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) on the [ncls-p/blog-key-points](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct). It specializes in extracting key points from blog articles and web content, providing concise bullet-point summaries that capture the essential information.

## Model Description

**Qwen2.5-3B-blog-key-points** is a 3B parameter model fine-tuned specifically for the task of extracting key points from articles. It can process a full article and generate a concise, bullet-point summary highlighting the most important information.

### Model Details

- **Model Type:** Qwen2.5 (3B parameters)
- **Base Model:** [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
- **Training Dataset:** [ncls-p/blog-key-points](https://huggingface.co/datasets/ncls-p/blog-key-points)
- **Language:** English
- **License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- **Finetuning Approach:** Instruction fine-tuning on article-summary pairs

## Uses

### Direct Use

This model is designed for extracting key points from articles. You can use it directly for:

- Summarizing blog posts
- Extracting important information from news articles
- Creating bullet-point summaries of long-form content
- Generating concise overviews of research papers

### Example Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ncls-p/Qwen2.5-3B-blog-key-points"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

article = """
[Your article text here]
"""

prompt = f"""
Extract the key points from the following article:

{article}
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=1024)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)
```

## Training

The model was fine-tuned on the [blog-key-points dataset](https://huggingface.co/datasets/ncls-p/blog-key-points), which contains 200 article-summary pairs. Each pair consists of a full article and a bullet-point summary of key points extracted using AI.

### Training Procedure

- **Fine-tuning Framework:** [Unsloth](https://github.com/unslothai/unsloth)
- **Training Data Format:**
  ```json
  {
    "instruction": "",
    "input": "Full article content",
    "output": "Here are the key points of the article:\n* Key point 1\n* Key point 2\n* Key point 3\n..."
  }
  ```

## Evaluation

The model was evaluated on its ability to extract relevant key points from articles not seen during training. Evaluation metrics focused on:

1. **Relevance:** How well the extracted points capture the main ideas of the article
2. **Conciseness:** The ability to summarize information in a clear, bullet-point format
3. **Completeness:** Whether all important information is captured in the summary

## Limitations and Biases

- The model may inherit biases present in the training data, including potential biases in the source articles or in the key point extraction process.
- Performance may vary depending on the length, complexity, and domain of the input article.
- The model is primarily trained on English-language content and may not perform well on content in other languages.
- As with any summarization model, there is a risk of omitting important information or misrepresenting the original content.

## How to Cite

If you use this model in your research, please cite:

```bibtex
@misc{qwen25-3b-blog-key-points,
  author = {ncls-p},
  title = {Qwen2.5-3B-blog-key-points},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face model repository},
  howpublished = {\url{https://huggingface.co/ncls-p/Qwen2.5-3B-blog-key-points}},
}
```

## Dataset Creation

The dataset used to train this model was created using the [llm-to-blog-key-points-dataset](https://github.com/ncls-p/llm-to-blog-key-points-dataset), a CLI tool that extracts key points from web articles using AI and adds them to a dataset in a structured format.