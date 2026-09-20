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

![image](https://cdn-uploads.huggingface.co/production/uploads/60270a7c32856987162c641a/SivoCJWJqex41oprnwyuK.png)

Want a bigger model? Download [Sarvam-105B](https://huggingface.co/sarvamai/sarvam-105b)!

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

**Sarvam-30B** is an advanced Mixture-of-Experts (MoE) model with 2.4B non-embedding active parameters, designed primarily for practical deployment. It combines strong reasoning, reliable coding ability, and best-in-class conversational quality across Indian languages. Sarvam-30B is built to run reliably in resource-constrained environments and can handle multilingual voice calls while performing tool calls.

A major focus during training was the Indian context and languages, resulting in **state-of-the-art performance across 22 Indian languages** for its model size.

Sarvam-30B is open-sourced under the **Apache License**. For more details, see our [blog](https://www.sarvam.ai/blogs/sarvam-30b-105b).

## Architecture

The 30B MoE model is designed for throughput and memory efficiency. It uses 19 layers, a dense FFN `intermediate_size` of 8192, `moe_intermediate_size` of 1024, top-6 routing, grouped KV heads (`num_key_value_heads=4`), and an extremely high rope_theta (`8e6`) for long-context stability without RoPE scaling. It has 128 experts with a shared expert, a routed scaling factor of 2.5, and auxiliary-loss-free router balancing. The 30B model focuses on throughput and memory efficiency through fewer layers, grouped KV attention, and smaller experts.

## Benchmarks

<details>
  <summary>Knowledge & Coding</summary>

| Benchmark | Sarvam-30B | Gemma 27B It | Mistral-3.2-24B | OLMo 3.1 32B Think | Nemotron-3-Nano-30B-A3B | Qwen3-30B-Thinking-2507 | GLM 4.7 Flash | GPT-OSS-20B |
|---|---|---|---|---|---|---|---|---|
| Math500 | 97.0 | 87.4 | 69.4 | 96.2 | 98.0 | 97.6 | 97.0 | 94.2 |
| HumanEval | 92.1 | 88.4 | 92.9 | 95.1 | 97.6 | 95.7 | 96.3 | 95.7 |
| MBPP | 92.7 | 81.8 | 78.3 | 58.7 | 91.9 | 94.3 | 91.8 | 95.3 |
| Live Code Bench v6 | 70.0 | 28.0 | 26.0 | 73.0 | 68.3 | 66.0 | 64.0 | 61.0 |
| MMLU | 85.1 | 81.2 | 80.5 | 86.4 | 84.0 | 88.4 | 86.9 | 85.3 |
| MMLU Pro | 80.0 | 68.1 | 69.1 | 72.0 | 78.3 | 80.9 | 73.6 | 75.0 |
| MILU | 76.8 | 69.2 | 67.9 | 69.9 | 64.8 | 82.6 | 75.6 | 73.7 |
| Arena Hard v2 | 49.0 | 50.1 | 43.1 | 42.0 | 67.7 | 72.1 | 58.1 | 62.9 |
| Writing Bench | 78.7 | 71.4 | 70.3 | 75.7 | 83.7 | 85.0 | 79.2 | 79.1 |

</details>

<details>
  <summary>Reasoning & Math</summary>

| Benchmark | Sarvam-30B | OLMo 3.1 32B | Nemotron-3-Nano-30B | Qwen3-30B-Thinking-2507 | GLM 4.7 Flash | GPT-OSS-20B |
|---|---|---|---|---|---|---|
| GPQA Diamond | 66.5 | 57.5 | 73.0 | 73.4 | 75.2 | 71.5 |
| AIME 25 (w/ Tools) | 88.3 (96.7) | 78.1 (81.7) | 89.1 (99.2) | 85.0 (-) | 91.6 (-) | 91.7 (98.7) |
| HMMT (Feb 25) | 73.3 | 51.7 | 85.0 | 71.4 | 85.0 | 76.7 |
| HMMT (Nov 25) | 74.2 | 58.3 | 75.0 | 73.3 | 81.7 | 68.3 |
| Beyond AIME | 58.3 | 48.5 | 64.0 | 61.0 | 60.0 | 46.0 |

</details>

<details>
  <summary>Agentic</summary>

| Benchmark | Sarvam-30B | Nemotron-3-Nano-30B | Qwen3-30B-Thinking-2507 | GLM 4.7 Flash | GPT-OSS-20B |
|---|---|---|---|---|---|
| BrowseComp | 35.5 | 23.8 | 2.9 | 42.8 | 28.3 |
| SWE Bench Verified | 34.0 | 38.8 | 22.0 | 59.2 | 34.0 |
| τ² Bench (avg.) | 45.7 | 49.0 | 47.7 | 79.5 | 48.7 |

> See footnote for evaluation details.

</details>

## Inference

<details>
  <summary>Huggingface</summary>
  
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

model_name = "sarvamai/sarvam-30b"
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
    "What is the capital city of New Zealand?",
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

model_path = "sarvamai/sarvam-30b"
engine = sgl.Engine(
    model_path=model_path,
    tp_size=2,
    mem_fraction_static=0.8,
    trust_remote_code=True,
    dtype="bfloat16",
    prefill_attention_backend="fa3",
    decode_attention_backend="fa3",
)

sampling_params = {
    "temperature": 0.8,
    "max_new_tokens": 2048,
    "repetition_penalty": 1.0,
}

prompts = [
    "Which treaty formally ended World War I and imposed heavy reparations on Germany?",
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

model_path = "sarvamai/sarvam-30b"
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
    "Who wrote The Picture of Dorian Gray?",
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

### Footnote

* **General settings**: All benchmarks are evaluated with a maximum context length of 65,536 tokens.
* **Reasoning & Math benchmarks** (Math500, MMLU, MMLU Pro, GPQA Diamond, AIME 25, Beyond AIME, HMMT, HumanEval, MBPP): Evaluated with `temperature=1.0, top_p=1.0, max_new_tokens=65536`.
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