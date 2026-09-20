---
library_name: transformers
language:
- en
- fr
- it
- pt
- hi
- es
- th
- de
base_model:
- meta-llama/Llama-3.1-70B
license: llama3.3
---

This is the AWQ version of the Llama 3.3 70B Instruct model. Find more info here: https://github.com/casper-hansen/AutoAWQ.

## Model Information

The Meta Llama 3.3 multilingual large language model (LLM) is a pretrained and instruction tuned generative model in 70B (text in/text out). The Llama 3.3 instruction tuned text only model is optimized for multilingual dialogue use cases and outperform many of the available open source and closed chat models on common industry benchmarks.

**Model developer**: Meta

**Model Architecture:** Llama 3.3 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align with human preferences for helpfulness and safety. 

|  | Training Data | Params | Input modalities | Output modalities | Context length | GQA | Token count | Knowledge cutoff |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Llama 3.3 (text only)  | A new mix of publicly available online data. | 70B | Multilingual Text | Multilingual Text and code  | 128k | Yes | 15T+ | December 2023 |

**Supported languages:** English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai.

**Llama 3.3 model**. Token counts refer to pretraining data only. All model versions use Grouped-Query Attention (GQA) for improved inference scalability.

**Model Release Date:** 

* **70B Instruct: December 6, 2024** 

**Status:** This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback.

**License** A custom commercial license, the Llama 3.3 Community License Agreement, is available at: [https://github.com/meta-llama/llama-models/blob/main/models/llama3\_3/LICENSE](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE)

Where to send questions or comments about the model Instructions on how to provide feedback or comments on the model can be found in the model [README](https://github.com/meta-llama/llama3). For more technical information about generation parameters and recipes for how to use Llama 3.3 in applications, please go [here](https://github.com/meta-llama/llama-recipes). 

## Benchmark

| Category | Benchmark | \# Shots | Metric | Llama 3.1 8B Instruct | Llama 3.1 70B Instruct | Llama-3.3 70B Instruct | Llama 3.1 405B Instruct |
| :---- | :---- | ----- | :---- | ----- | ----- | ----- | ----- |
|  | MMLU (CoT) | 0 | macro\_avg/acc | 73.0 | 86.0 | 86.0 | 88.6 |
|  | MMLU Pro (CoT) | 5 | macro\_avg/acc | 48.3 | 66.4 | 68.9 | 73.3 |
| Steerability | IFEval |  |  | 80.4 | 87.5 | 92.1 | 88.6 |
| Reasoning | GPQA Diamond (CoT) | 0 | acc | 31.8 | 48.0 | 50.5 | 49.0 |
| Code | HumanEval | 0 | pass@1 | 72.6 | 80.5 | 88.4 | 89.0 |
|  | MBPP EvalPlus (base) | 0 | pass@1 | 72.8 | 86.0 | 87.6 | 88.6 |
| Math | MATH (CoT) | 0 | sympy\_intersection\_score | 51.9 | 68.0 | 77.0 | 73.8 |
| Tool Use | BFCL v2 | 0 | overall\_ast\_summary/macro\_avg/valid | 65.4 | 77.5 | 77.3 | 81.1 |
| Multilingual | MGSM | 0 | em | 68.9 | 86.9 | 91.1 | 91.6 |
