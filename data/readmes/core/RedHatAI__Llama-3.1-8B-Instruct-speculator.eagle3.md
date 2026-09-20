---
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
license: llama3.1
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
- neuralmagic
- redhat
- speculators
- eagle3
base_model: meta-llama/Llama-3.1-8B-Instruct
datasets:
- Aeala/ShareGPT_Vicuna_unfiltered
- HuggingFaceH4/ultrachat_200k
---

# Llama-3.1-8B-Instruct-speculator.eagle3

## Model Overview
- **Verifier:** meta-llama/Llama-3.1-8B-Instruct
- **Speculative Decoding Algorithm:** EAGLE-3
- **Model Architecture:** Eagle3Speculator
- **Release Date:** 07/27/2025
- **Version:** 1.0
- **Model Developers:** RedHat

This is a speculator model designed for use with [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct), based on the [EAGLE-3](https://arxiv.org/abs/2503.01840) speculative decoding algorithm.
It was trained using the [speculators](https://github.com/neuralmagic/speculators) library on a combination of the [Aeala/ShareGPT_Vicuna_unfiltered](https://huggingface.co/datasets/Aeala/ShareGPT_Vicuna_unfiltered) and the [HuggingFaceH4/ultrachat_200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) datasets.
This model should be used with the [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) chat template, specifically through the `/chat/completions` endpoint.

## Use with vLLM

```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct \
  -tp 1 \
  --speculative-config '{
    "model": "RedHatAI/Llama-3.1-8B-Instruct-speculator.eagle3",
    "num_speculative_tokens": 3,
    "method": "eagle3"
  }'
```

## Evaluations

<h3>Use cases</h3>
<table>
  <thead>
    <tr>
      <th>Use Case</th>
      <th>Dataset</th>
      <th>Number of Samples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Coding</td>
      <td>HumanEval</td>
      <td>168</td>
    </tr>
    <tr>
      <td>Math Reasoning</td>
      <td>gsm8k</td>
      <td>80</td>
    </tr>
    <tr>
      <td>Text Summarization</td>
      <td>CNN/Daily Mail</td>
      <td>80</td>
    </tr>
  </tbody>
</table>

<h3>Acceptance lengths</h3>
<table>
  <thead>
    <tr>
      <th>Use Case</th>
      <th>k=1</th>
      <th>k=2</th>
      <th>k=3</th>
      <th>k=4</th>
      <th>k=5</th>
      <th>k=6</th>
      <th>k=7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Coding</td>
      <td>1.84</td>
      <td>2.50</td>
      <td>3.02</td>
      <td>3.36</td>
      <td>3.61</td>
      <td>3.83</td>
      <td>3.89</td>
    </tr>
    <tr>
      <td>Math Reasoning</td>
      <td>1.80</td>
      <td>2.40</td>
      <td>2.83</td>
      <td>3.13</td>
      <td>3.27</td>
      <td>3.40</td>
      <td>3.83</td>
    </tr>
    <tr>
      <td>Text Summarization</td>
      <td>1.70</td>
      <td>2.19</td>
      <td>2.50</td>
      <td>2.78</td>
      <td>2.77</td>
      <td>2.98</td>
      <td>2.99</td>
    </tr>
  </tbody>
</table>

<h3>Performance benchmarking (1xA100)</h3>
<div style="display: flex; justify-content: center; gap: 20px;">

  <figure style="text-align: center;">
    <img src="assets/Llama-3.1-8B-Instruct-HumanEval.png" alt="Coding" width="100%">
  </figure>

  <figure style="text-align: center;">
    <img src="assets/Llama-3.1-8B-Instruct-math_reasoning.png" alt="Coding" width="100%">
  </figure>

  <figure style="text-align: center;">
    <img src="assets/Llama-3.1-8B-Instruct-summarization.png" alt="Coding" width="100%">
  </figure>
</div>

<details> <summary>Details</summary>
<strong>Configuration</strong>

- temperature: 0.6
- top_p: 0.9
- repetitions: 5
- time per experiment: 3min
- hardware: 1xA100
- vLLM version: 0.11.0
- GuideLLM version: 0.3.0

<strong>Command</strong>
```bash
GUIDELLM__PREFERRED_ROUTE="chat_completions" \
guidellm benchmark \
  --target "http://localhost:8000/v1" \
  --data "RedHatAI/speculator_benchmarks" \
  --data-args '{"data_files": "HumanEval.jsonl"}' \
  --rate-type sweep \
  --max-seconds 180 \
  --output-path "Llama-3.1-8B-Instruct-HumanEval.json" \
  --backend-args '{"extra_body": {"chat_completions": {"temperature":0.0}}}'
```

GuideLLM interface changed, so for compatibility with the latest version (v0.6.0), please use the following command:
```bash
GUIDELLM__PREFERRED_ROUTE="chat_completions" \
guidellm benchmark \
  --target "http://localhost:8000/v1" \
  --data "RedHatAI/speculator_benchmarks" \
  --data-args '{"data_files": "HumanEval.jsonl"}' \
  --profile sweep \
  --max-seconds 1800 \
  --output-path "my_output.json" \
  --backend-args '{"extras": {"body": {"temperature":0.6, "top_p":0.95, "top_k":20}}}'
```
</details>