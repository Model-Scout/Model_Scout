---
license: cc-by-nc-sa-4.0
library_name: transformers
# license: apache-2.0
# license_link: https://huggingface.co/OptAI/Opt.Gear-1B/blob/main/LICENSE
pipeline_tag: text-generation
language:
- en
- ko
base_model:
- OptAI/Opt.Gear-1B
---

# Opt.Gear-1B

<img width="1000px" src="./OptAIxHuggingFace01.png">

[![OptAI](https://img.shields.io/badge/%F0%9F%8F%A0%20OptAI-1a1a2e)](https://opt-ai.kr)
[![Opt.Gear](https://img.shields.io/badge/%F0%9F%8F%A0%20OptAI-1a1a2e)](https://www.opt.ai.kr/optgear/index.html)
[![Tech Report](https://img.shields.io/badge/%F0%9F%93%84%20Tech%20Report-5b4bcf)](https://huggingface.co/OptGear)

> [!Note]
> This repository contains model weights and configuration files for the post-trained (instruction-tuned) model in the Hugging Face Transformers format.
>
> These artifacts are compatible with Hugging Face Transformers, llama.cpp, ExecuTorch, and vLLM. Executable binaries optimized for NPU inference (Qualcomm Hexagon NPU, Apple ANE) are also provided.
>
> In light of its parameter scale and on-device design goals, the intended use cases are on-device text generation, Korean-English bilingual assistants, task-specific fine-tuning, and other research or development purposes.

Opt.Gear is the first generation of OptAI Foundation Models, designed for efficient on-device deployment, real-time inference, and strong task capability. Rather than simply shrinking a server-scale LLM, Gear jointly optimizes downstream quality, device-side latency, memory efficiency, long-context capability, and practical deployability under hardware constraints such as limited SRAM, memory bandwidth, and power.

## Opt.Gear Highlights

- **Data-efficient training**: Trained on a curated **0.5T-token** subset selected from a 2T-token candidate corpus, **without knowledge distillation** from a teacher model — the most data-efficient recipe among comparable open foundation models.

- **Hybrid architecture with ConvKV-Gated Mixer**: A small set of global GQA layers handles long-range routing, while **ConvKV-Gated Mixer** blocks replace many local attention layers with softmax-free, matrix-multiplication-free local mixing. The persistent local state scales with the convolution kernel (L_conv = 3) instead of the sliding window (W = 512), substantially reducing live decoding state and memory bandwidth.

- **NPU-friendly by design**: Dynamic QKV matrix multiplications and softmax normalization are replaced with static linear, convolution, and element-wise operations, delivering up to **×4.9 faster prefill and decoding on NPUs** compared to models of similar scale (7,042 tokens/s prefill on Snapdragon GEN5).

- **Korean-English bilingual**: Built on the KORMo tokenizer (125,184 vocab) with Korean-English pretraining, achieving distinct superiority on Korean benchmarks (KMMLU, KoBEST, CLIcK, HAERAE) against same-scale baselines.

- **64K context on device**: Hybrid attention layout with separate global/local RoPE frequencies supports long-context modeling up to 65,536 tokens while keeping the local cache footprint small.

For more details, please refer to our tech report and blog post. <!-- TODO: 링크 연결 -->

## Model Overview

- Type: Causal Language Model (hybrid attention + convolutional mixer)
- Training Stage: Pre-training (0.5T tokens) → Long-context extension (4K → 32K → 64K) → Two-stage SFT (general instruction → reasoning-oriented)
- Architecture
    - Number of Parameters: 1B
    - Hidden Dimension: 1,152
    - Number of Layers: 26
    - Hidden Layout: hybrid of Global GQA, Local (sliding-window) Attention, and ConvKV-Gated Mixer
    - Grouped-Query Attention:
        - Number of Attention Heads: 4 for Q and 1 for KV
        - Head Dimension: 256
        - Sliding-Window Size (local attention): 512
        - QK-Normalization: QK-LN
    - ConvKV-Gated Mixer:
        - Causal depthwise 1D convolution on key/value streams
        - Convolution Kernel Size: 3 (fixed-size persistent state, independent of context length)
    - Feed-Forward Network:
        - Type: GeGLU (gated dense MLP)
        - Intermediate Dimension: 6,912
    - Rotary Position Embedding: global theta 1,000,000 / local theta 10,000
    - Tokenizer: KORMo (byte-level BPE), vocabulary 125,184
    - Word Embedding: untied (separate input embedding and LM head)
- Context Length: 65,536 natively

> [!Important]
> Base and Instruction models share the same tokenizer, but use different end-of-generation tokens: the **Base model emits `<EOS>`** while the **Instruction model emits `<EOT>`**. When fine-tuning, make sure training examples terminate with the same convention used by the target runtime — malformed termination wastes decoding steps and increases latency on device.

## Benchmark Results

All results are obtained using the [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) and may differ from scores reported elsewhere. Perplexity-based evaluation is adopted for HellaSwag, PIQA, WinoGrande, MMLU, MMLU-Pro, GPQA, ARC, KMMLU, and KoBEST.

<div style="max-width:1000px;margin:0 auto;padding:16px 0">
<!-- <table style="border-collapse:collapse;font-size:13px;width:100%"> -->
<table style="border-collapse:collapse;font-size:15px">
<thead><tr>
<th style="padding:10px 7px;text-align:left;font-weight:600;border-bottom:2px solid #5b4bcf;color:#5b4bcf"></th>
<th style="padding:10px 7px;text-align:center;font-weight:600;border-bottom:2px solid #5b4bcf;color:#5b4bcf">Opt.Gear-1B</th>
<th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #5b4bcf;color:#5b4bcf">Gemma3-1B</th>
<th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #5b4bcf;color:#5b4bcf">Llama3.2-1B</th>
<th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #5b4bcf;color:#5b4bcf">EXAONE4-1.2B</th>
<th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #5b4bcf;color:#5b4bcf">LFM2.5-1.2B</th>
<th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #5b4bcf;color:#5b4bcf">Qwen3-1.7B</th>
</tr></thead>
<tbody>
<tr>
<td style="padding:7px;border-bottom:1px solid rgba(128,128,128,0.15)"># Trained Tokens</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">0.5T</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">2T</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">9T</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">12T</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">28T</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">36T</td>
</tr>
<tr>
<td style="padding:7px;border-bottom:1px solid rgba(128,128,128,0.15)">Distilled</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">✗</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">✓</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">✓</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">✓</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">✓</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">✓</td>
</tr>
<tr><td colspan="7" style="padding:8px 12px;font-weight:600;color:#5b4bcf;border-bottom:1px solid rgba(91,75,207,0.2);background:rgba(91,75,207,0.08)">English</td></tr>
<tr>
<td style="padding:7px;padding-left:20px;border-bottom:1px solid rgba(128,128,128,0.15)">MMLU</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">43.2</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">39.8</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">46.1</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">37.2</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">51.1</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">60.3</td>
</tr>
<tr>
<tr><td colspan="7" style="padding:8px 12px;font-weight:600;color:#5b4bcf;border-bottom:1px solid rgba(91,75,207,0.2);background:rgba(91,75,207,0.08)">Korean</td></tr>
<tr>
<td style="padding:7px;padding-left:20px;border-bottom:1px solid rgba(128,128,128,0.15)">KMMLU</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">36.0</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">30.7</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">29.9</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">32.6</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">29.2</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">41.6</td>
</tr>
<tr>
<td style="padding:7px;padding-left:20px;border-bottom:1px solid rgba(128,128,128,0.15)">KoBEST</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">60.3</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">59.5</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">51.8</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">50.7</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">59.1</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">62.8</td>
</tr>
<tr>
<td style="padding:7px;padding-left:20px;border-bottom:1px solid rgba(128,128,128,0.15)">CLIcK</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">39.7</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">37.8</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">30.6</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">32.9</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">38.3</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">49.4</td>
</tr>
<tr>
<td style="padding:7px;padding-left:20px;border-bottom:1px solid rgba(128,128,128,0.15)">HAERAE</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">44.2</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">35.3</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">32.6</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">30.2</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">33.9</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">52.0</td>
</tr>
</tbody>
</table>
<p style="margin-top:12px;font-size:11px;opacity:0.7">
* All results are obtained using LM Evaluation Harness and may differ from other reported scores.<br>
* While baselines are trained on 2T–36T tokens and frequently leverage knowledge distillation, Opt.Gear-1B is trained on only 0.5T tokens without any distillation.
</p>
</div>

### On-Device Inference Performance

Measured across hardware processors (CPU/GPU/NPU) and runtimes (Qualcomm AI Engine Direct, llama.cpp, CoreML) with W4A16 quantization; embedding and LM head kept in 16-bit. Numbers are Prefill / Decode (tokens/sec).

<div style="max-width:1000px;margin:0 auto;padding:16px 0">
<!-- <table style="table-layout: fixed; border-collapse:collapse;font-size:13px;width:100%"> -->
<table style="border-collapse:collapse;font-size:15px">
<thead><tr>
<th style="padding:10px 7px;text-align:left;font-weight:600;border-bottom:2px solid #5b4bcf;color:#5b4bcf">Model</th>
<th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #5b4bcf;color:#5b4bcf">Snapdragon GEN5 (NPU)</th>
<th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #5b4bcf;color:#5b4bcf">Snapdragon GEN4 (NPU)</th>
<th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #5b4bcf;color:#5b4bcf">iPhone 17 Pro (NPU)</th>
<th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #5b4bcf;color:#5b4bcf">iPhone 16 Pro (NPU)</th>
</tr></thead>
<tbody>
<tr>
<td style="padding:7px;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">Opt.Gear-1B</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">7042 / 86</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">5882 / 80</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">3085 / 97</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15);font-weight:600">2589 / 80</td>
</tr>
<tr>
<td style="padding:7px;border-bottom:1px solid rgba(128,128,128,0.15)">Llama3.2-1B</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">4481 / 65</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">3013 / 50</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">1073 / 34</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">696 / 25</td>
</tr>
<tr>
<td style="padding:7px;border-bottom:1px solid rgba(128,128,128,0.15)">Gemma3-1B</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">3226 / 61</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">2724 / 51</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">2380 / 90</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">1862 / 70</td>
</tr>
<tr>
<td style="padding:7px;border-bottom:1px solid rgba(128,128,128,0.15)">EXAONE4-1.2B</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">4386 / 57</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">3436 / 49</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">590 / 20</td>
<td style="padding:7px;text-align:center;border-bottom:1px solid rgba(128,128,128,0.15)">319 / 15</td>
</tr>
</tbody>
</table>
<p style="margin-top:12px;font-size:11px;opacity:0.7">
* Snapdragon: Qualcomm AI Runtime (QAIRT). iPhone: CoreML Runtime. Full CPU/GPU results and llama.cpp results are available in the tech report.<br>
* Note: the llama.cpp NPU backend does not allocate the sliding-window attention pattern to hardware accelerators, which degrades prefill performance in that specific combination. QAIRT is recommended for Snapdragon NPU deployment.
</p>
</div>

## Quickstart

### Hugging Face Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "OptAI/Opt.Gear-1B"  

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype="auto", device_map="auto")

messages = [
    {"role": "user", "content": "온디바이스 AI가 왜 중요한지 설명해줘."},
]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

### llama.cpp

```shell
llama-cli -m opt-gear-1b-w4.gguf -p "프랑스의 수도가 뭐야?"" -n 128
```

<!-- ### vLLM

```shell
# TODO: 실제 리포지토리 ID로 교체
vllm serve OptAI/Opt.Gear-1B --port 8000 --max-model-len 65536 -->
<!-- ``` -->

### On-Device Deployment

Executable binaries optimized for NPU inference are provided for:

- **Qualcomm Hexagon NPU** — via Qualcomm AI Engine Direct (QAIRT); recommended for Snapdragon devices
- **Apple ANE** — via CoreML Runtime
- **ExecuTorch** — for mobile/edge PyTorch deployment

<!-- TODO: 디바이스별 배포 가이드 링크 추가 -->

## Quantization

A QAT (Quantization-Aware Training) checkpoint is available at [OptAI/Opt.Gear-1B-QAT](https://huggingface.co/OptGear/Opt.Gear-1B-qat-int4-per-channel-unquantized). <!-- TODO: 리포지토리 ID 확인 -->

The QAT model uses group-size-32 symmetric INT4 weights (W4A16) with Hessian-based scale initialization and Learned Step Size Quantization. On six English/Korean benchmarks, the QAT model loses only ~1.0 point on average from the Base model, and remains stable even when re-quantized with other INT4 PTQ methods (RTN/AWQ/GPTQ) — see the tech report for details.

## Best Practices

1. **Termination tokens**: The Instruction model terminates generation with `<EOT>`, while the Base model uses `<EOS>`. When fine-tuning either variant, ensure training examples terminate with the matching token — this is particularly important for on-device inference, where malformed termination wastes decoding steps and increases latency.

2. **Runtime selection**:
   - Snapdragon NPU → **QAIRT** (Qualcomm AI Engine Direct). Avoid the llama.cpp NPU backend, which cannot hardware-accelerate the sliding-window attention pattern.
   - Apple devices → **CoreML** (best-in-class GPU/ANE throughput at this scale).
   - CPU/GPU → llama.cpp works well and delivers stable performance.

3. **Languages**: The model is trained primarily on English (~92%) and Korean (~6%) with mathematical text (~2%). It is best suited for Korean-English bilingual understanding, summarization, rewriting, and instruction following.

4. **Not intended for code generation**: The pre-training corpus deliberately excludes code data — models at the 270M–1B scale are not typically used for code generation tasks. Use a code-specialized model for such workloads.

5. **Long context**: The model natively supports 65,536 tokens. The hybrid ConvKV architecture keeps the local cache footprint fixed, so long-context decoding remains memory-efficient on device.

## Limitations

The constrained 0.5T-token training budget limits capabilities in complex reasoning and mathematical tasks that typically benefit from larger training corpora. The current results reflect both the capacity of the proposed architecture and the limitations of the available data and compute budget. See the tech report for a detailed discussion.

## Citation

If you find our work helpful, feel free to give us a cite.

```bibtex
@misc{optgear2026,
    title  = {{Opt-Gear} Technical Report},
    author = {{Opt.Gear Team}},
    year   = {2026},
    url    = {https://arxiv.org/abs/2608.01034}
}
```

---

Correspondence: [contact@opt-ai.kr](mailto:contact@opt-ai.kr) · Hugging Face: [huggingface.co/OptAI](https://huggingface.co/OptGear)
