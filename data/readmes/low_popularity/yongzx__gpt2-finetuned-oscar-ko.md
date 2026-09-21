---
language: 
  - ko
tags:
- text-generation
license: mit
datasets:
- oscar
widget:
- text: "모든사람은교육을 "
---
# GPT-2 finetuned on Korean Dataset
### Tokenizer
We first trained a tokenizer on OSCAR's `unshuffled_original_ko` Korean data subset by following the training of GPT2 tokenizer (same vocab size of 50,257). Here's the [Python file](https://github.com/bigscience-workshop/multilingual-modeling/blob/gpt2-ko/experiments/exp-001/train_tokenizer_gpt2.py) for the training.
### Model
We finetuned the `wte` and `wpe` layers of GPT-2 (while freezing the parameters of all other layers) on OSCAR's `unshuffled_original_ko` Korean data subset. We used [Huggingface's code](https://github.com/huggingface/transformers/blob/master/examples/pytorch/language-modeling/run_clm.py) for fine-tuning the causal language model GPT-2, but with the following parameters changed
```
- preprocessing_num_workers: 8
- per_device_train_batch_size: 2
- gradient_accumulation_steps: 4
- per_device_eval_batch_size: 2
- eval_accumulation_steps: 4
- eval_steps: 1000 
- evaluation_strategy: "steps"
- max_eval_samples: 5000
```
**Training details**: total training steps: 688000, effective train batch size per step: 32, max tokens per batch: 1024)