---
language:
  - en
  - hi
  - bn
  - ta
  - te
  - mr
  - gu
  - kn
  - ml
  - pa
  - or
  - as
  - ur
  - sa
  - ne
  - sd
  - kok
  - mai
  - doi
  - mni
  - sat
  - ks
  - bo
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
---

![image](https://cdn-uploads.huggingface.co/production/uploads/60270a7c32856987162c641a/j1SbA6V6HixP1-6H0N41q.png)

Want a smaller model? Download [Sarvam-30B](https://huggingface.co/sarvamai/sarvam-30b/)!

## Index

1. [Introduction](#introduction)  
2. [Architecture](#architecture)  
3. [Benchmarks](#benchmarks)  
   - Knowledge & Coding  
   - Reasoning & Math  
   - Agentic  
4. [Inference](#inference)  
   - Hugging Face  
   - [vLLM](https://github.com/vllm-project/vllm)
   - [SGLang](https://github.com/sgl-project/sglang)
5. [Footnote](#footnote)  
6. [Citation](#citation)  

## Introduction

**Sarvam-105B** is an advanced Mixture-of-Experts (MoE) model with 10.3B active parameters, designed for superior performance across a wide range of complex tasks. It is highly optimized for complex reasoning, with particular strength in agentic tasks, mathematics, and coding.

Sarvam-105B is a top-tier performer, consistently matching or surpassing several major closed-source models and staying within a narrow margin of frontier models across diverse reasoning and agentic benchmarks. It demonstrates exceptional agentic and reasoning capabilities in real-world applications such as web search and technical troubleshooting.

A major focus during training was the Indian context and languages, resulting in **state-of-the-art performance across 22 Indian languages** for its model size.

Sarvam-105B is open-sourced under the **Apache License**. For more details, see our [blog](https://www.sarvam.ai/blogs/sarvam-30b-105b).

## Architecture

The 105B model adopts an MLA-style attention stack with decoupled QK head dimensions (`q_head_dim=192` split into RoPE and noPE components, `v_head_dim=128`) and a large head_dim of 576, enabling higher representational bandwidth per head while keeping the hidden size at 4096. This approach improves attention expressivity and long-context extrapolation (via YaRN scaling with a factor of 40 and 128K context). It has an `intermediate_size` (16384) and `moe_intermediate_size` (2048), combined with top-8 routing over 128 experts, which increases per-token active capacity while keeping activation cost manageable. The model has one shared expert, a routed scaling factor of 2.5, and auxiliary-loss-free router balancing.

## Benchmarks

<details>
  <summary>Knowledge & Coding</summary>

| Benchmark | Sarvam-105B | GLM-4.5-Air | GPT-OSS-120B | Qwen3-Next-80B-A3B-Thinking |
|---|---|---|---|---|
| Math500 | 98.6 | 97.2 | 97.0 | 98.2 |
| Live Code Bench v6 | 71.7 | 59.5 | 72.3 | 68.7 |
| MMLU | 90.6 | 87.3 | 90.0 | 90.0 |
| MMLU Pro | 81.7 | 81.4 | 80.8 | 82.7 |
| Writing Bench | 80.5 | 83.8 | 86.5 | 84.6 |
| Arena Hard v2 | 71.0 | 68.1 | 88.5 | 68.2 |
| IF Eval | 84.8 | 83.5 | 85.4 | 88.9 |

</details>

<details>
  <summary>Reasoning & Math</summary>

| Benchmark | Sarvam-105B | GLM-4.5-Air | GPT-OSS-120B | Qwen3-Next-80B-A3B-Thinking |
|---|---|---|---|---|
| GPQA Diamond | 78.7 | 75.0 | 80.1 | 77.2 |
| AIME 25 (w/ Tools) | 88.3 (96.7) | 83.3 | 90.0 | 87.8 |
| Beyond AIME | 69.1 | 61.5 | 51.0 | 68.0 |
| HMMT (Feb 25) | 85.8 | 69.2 | 90.0 | 73.9 |
| HMMT (Nov 25) | 85.8 | 75.0 | 90.0 | 80.0 |

</details>

<details>
  <summary>Agentic</summary>

| Benchmark | Sarvam-105B | GLM-4.5-Air | GPT-OSS-120B | Qwen3-Next-80B-A3B-Thinking |
|---|---|---|---|---|
| BrowseComp | 49.5 | 21.3 | - | 38.0 |
| SWE Bench Verified (SWE-Agent Harness) | 45.0 | 57.6 | 50.6 | 60.9 |
| τ² Bench (avg.) | 68.3 | 53.2 | 65.8 | 55.0 |

> See footnote for evaluation details.

</details>

## Inference

<details>
  <summary>Huggingface</summary>

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

model_name = "sarvamai/sarvam-105b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, device_map="auto")

def generate_text(
    prompt: str,
    max_new_tokens: int = 2048,
    temperature: float = 0.8,
    top_p: float = 0.95,
    repetition_penalty: float = 1.0,
) -> None:
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")

    generation_config = GenerationConfig(
        max_new_tokens=max_new_tokens,
        repetition_penalty=repetition_penalty,
        temperature=temperature,
        top_p=top_p,
        do_sample=True,
    )

    with torch.no_grad():
        output_ids = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            generation_config=generation_config,
        )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

prompts = [
    "Which country won the FIFA World Cup in 2012?",
]

for prompt in prompts:
    templated_prompt = tokenizer.apply_chat_template(
      [{"role": "user", "content": prompt}],
      tokenize=False,
      add_generation_prompt=True,
      enable_thinking=True
    )
    output = generate_text(templated_prompt, max_new_tokens=512)
    print("Prompt: ", prompt)
    print("Generated text: ", output)
    print("=" * 100)
```
</details>

<details>
  <summary>SGLang</summary>

**Install latest SGLang from source**

```bash
git clone https://github.com/sgl-project/sglang.git
cd sglang
pip install -e "python[all]"
```

**Instantiate model and Run**

```python
import sglang as sgl
from transformers import AutoTokenizer

model_path = "sarvamai/sarvam-105b"
engine = sgl.Engine(
    model_path=model_path,
    tp_size=4,
    mem_fraction_static=0.70,
    trust_remote_code=True,
    dtype="bfloat16",
    moe_runner_backend="flashinfer_cutedsl",
    prefill_attention_backend="fa3",
    decode_attention_backend="flashmla",
    disable_radix_cache=False,
)

sampling_params = {
    "temperature": 0.8,
    "max_new_tokens": 2048,
    "repetition_penalty": 1.0,
}

prompts = [
    "Which band released the album Dark Side of the Moon in 1973?",
]

outputs = engine.generate([
    tokenizer.apply_chat_template([
        {"role": "user", "content": prompt}],
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=True)
        for prompt in prompts], 
    sampling_params)
for p, o in zip(prompts, outputs):
    print("Prompt: ", p)
    print("Generated text: ", o['text'])
    print("=" * 100)
```
</details>

<details>
  <summary>vLLM</summary>

Note: currently a PR is open for native support for the Sarvam models in vLLM ([link](https://github.com/vllm-project/vllm/pull/33942)). Therefore, we have 2 options here.

#### Option 1: install from source (hard)

* Use the custom fork here: [link](https://github.com/rahul-sarvam/vllm)
* Follow the instructions here to install from source: [link](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/index.html#build-wheel-from-source)

#### Option 2: hot-patch (easy)

* Run [hotpatch_vllm.py](./hotpatch_vllm.py)
* This will do the following:
  * install vllm=0.15.0
  * add 2 model entries to `registry.py`
  * download the model executors for `sarvam-105b` and `sarvam-30b`

Once this is done, you can run vLLM as usual

```python
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

model_path = "sarvamai/sarvam-105b"
tokenizer = AutoTokenizer.from_pretrained(model_path)
llm = LLM(model=model_path, 
            trust_remote_code=True, 
            max_model_len=2048, 
            tensor_parallel_size=8, 
            max_num_seqs=16,
        )
sampling_params = SamplingParams(
                    temperature=0.8, 
                    max_tokens=2048, 
                    repetition_penalty=1.0,
                    spaces_between_special_tokens=True
                )

prompts = [
    "Which artist painted The Persistence of Memory (the melting clocks)?",
]

outputs = llm.generate([
    tokenizer.apply_chat_template([
        {"role": "user", "content": prompt}],
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=True)
        for prompt in prompts], 
    sampling_params)
for p, o in zip(prompts, outputs):
    print("Prompt: ", p)
    print("Generated text: ", o.outputs[0].text)
    print("=" * 100)
```
</details>

## Footnote

* **General settings**: All benchmarks are evaluated with a maximum context length of 65,536 tokens.
* **Reasoning & Math benchmarks** (Math500, MMLU, MMLU Pro, GPQA Diamond, AIME 25, Beyond AIME, HMMT): Evaluated with `temperature=1.0, top_p=1.0, max_new_tokens=65536`.
* **Coding & Knowledge benchmarks** (Live Code Bench v6, Arena Hard v2, IF Eval):
  Evaluated with `temperature=1.0, top_p=1.0, max_new_tokens=65536`.
* **Writing Bench**:
  Responses generated using official Writing-Bench parameters:
  `temperature=0.7, top_p=0.8, top_k=20, max_length=16000`.
  Scoring performed using the official Writing-Bench critic model with:
  `temperature=1.0, top_p=0.95, max_length=2048`.
* **Agentic benchmarks** (BrowseComp, SWE Bench Verified, τ² Bench): Evaluated with `temperature=0.5, top_p=1.0, max_new_tokens=32768`.

## Citation
```
@misc{sarvam_sovereign_models,
  title        = {Introducing Sarvam's Sovereign Models},
  author       = {{Sarvam Foundation Models Team}},
  year         = {2026},
  howpublished = {\url{https://www.sarvam.ai/blogs/sarvam-30b-105b}},
  note         = {Accessed: 2026-03-03}
}
```