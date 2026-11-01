---
license: mit
language:
- ko
- en
base_model: hyunseoki/ko-en-llama2-13b
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
tags:
- llama
- llama-2
- korean
- instruction-tuned
- lora
- open-ko-llm-leaderboard
---

# ko-llama2-v1

A 13B Korean-English Llama 2 model, instruction-tuned with LoRA on a small, quality-filtered instruction set.
On **October 28-29, 2023** it ranked **#1 on the [Open Ko-LLM Leaderboard](https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard)** (230 models on the October 29 snapshot), the Korean LLM benchmark co-hosted on Hugging Face by Upstage and Korea's National Information Society Agency (NIA).

- **Author:** Jiwoo Chris Jung ([@jiwoochris](https://huggingface.co/jiwoochris)), trained while working as an NLP researcher at [Selectstar](https://selectstar.ai)
- **Base model:** [hyunseoki/ko-en-llama2-13b](https://huggingface.co/hyunseoki/ko-en-llama2-13b) (Llama 2 13B with continued Korean-English pretraining)
- **Method:** LoRA instruction tuning; the adapter is merged into these full fp16 weights
- **Released:** October 21, 2023
- **Press:** [AI Times, November 4, 2023](https://www.aitimes.com/news/articleView.html?idxno=154927) (Korean)

## Training data

The model was tuned on **1,944 instruction examples**, selected from a much larger pool by a quality-filtering model built for this purpose.
The approach follows the less-is-more findings of *LIMA* (Zhou et al., 2023) and *Instruction Mining* (Cao et al., 2023): for instruction tuning, data quality matters more than data volume.
The filtering model and the selected data are Selectstar property and are not released; the weights are.

## Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "jiwoochris/ko-llama2-v1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")

prompt = "한국의 수도는 어디인가요?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256, do_sample=True, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

The checkpoint is about 26 GB in fp16 (three shards). Use 8-bit or 4-bit loading for GPUs with less memory.

## Evaluation

Ranked first on the Open Ko-LLM Leaderboard on October 28-29, 2023 (230 models on the October 29 snapshot).
The leaderboard evaluated Korean adaptations of the Open LLM Leaderboard tasks. Its live space is no longer running, so the ranking is recorded here from the leaderboard snapshot and the AI Times report linked above.

## Limitations

This is a research checkpoint from October 2023. It was not trained for safety, can produce incorrect or fabricated content, and inherits the limitations and the license terms of Llama 2 through its base model.

## Citation

```bibtex
@misc{jung2023kollama2v1,
  author = {Jung, Jiwoo Chris},
  title  = {ko-llama2-v1: a quality-filtered instruction-tuned Korean-English Llama 2 13B},
  year   = {2023},
  url    = {https://huggingface.co/jiwoochris/ko-llama2-v1}
}
```
