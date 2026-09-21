---
license: apache-2.0
base_model: tencent/Hy-MT2-1.8B
base_model_relation: quantized
pipeline_tag: translation
library_name: mlx
tags:
  - mlx
  - apple-silicon
  - quantized
  - ternary
  - sherry
  - stq1_0
  - hunyuan
  - machine-translation
language:
  - zh
  - en
  - ko
  - ja
  - fr
  - es
  - pt
  - de
  - it
  - ru
  - ar
  - th
  - vi
  - id
  - ms
  - tr
  - pl
  - cs
  - nl
  - uk
  - hi
---

# Hy-MT2-1.8B-1.25Bit-MLX

Hy-MT2 1.8B 翻译模型的 1.25-bit 极限量化 MLX 版本，带**重写的 Metal 解码内核**——
单文件权重仅 454 MB，Apple Silicon 上单流 ~112 tok/s、并发 4 聚合 ~216 tok/s
（M3 实测），支持 continuous batching。

- 量化格式：STQ 1.3125 bpw（llama.cpp STQ1_0 位布局，拆成 `qs` / `sign` /
  `scales` 三个 buffer），嵌入为 6-bit affine
- 解码：自定义 Metal GEMV（解析码本 + half4 LUT + 合并访存），batch 解码按
  8 行分块复用权重；prefill 走一次性反量化 + GEMM
- 模型定义内嵌在 `sherry_model.py`，`mlx-lm` 通过 `config.json` 的
  `model_file` 自动加载，无需额外安装

## 用法

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load("Sube126/Hy-MT2-1.8B-1.25Bit-MLX")

messages = [{"role": "user",
             "content": "把下面的文本翻译成英文。\n\n城市轨道交通网络的扩张使换乘站的客流压力日益集中。"}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
out = generate(model, tokenizer, prompt=prompt, max_tokens=256,
               sampler=make_sampler(temp=0.0))
```

OpenAI 兼容服务（continuous batching，支持流式）：

```bash
python -m mlx_lm.server --model Sube126/Hy-MT2-1.8B-1.25Bit-MLX --port 8899
```

## 性能（Apple M3 10-core GPU 实测）

| 场景 | 数值 |
|---|---|
| 单流 decode（短上下文） | ~112 tok/s |
| 单流 decode（600 token 上下文） | ~85 tok/s |
| prefill（>256 token，dense 路径） | ~700–760 tok/s |
| 并发 4（600 token 输入，端到端） | 聚合 ~216 tok/s |
| 并发 8 / 16 / 32（短输出，端到端） | ~157 / ~170 / ~182 tok/s |
| TTFT（~600 token prompt） | 单发 0.6s / 并发 4 均值 1.7s |

## 要求

- Apple Silicon macOS
- `mlx-lm >= 0.31`（在 0.31.3 上验证），依赖 `mlx.fast.metal_kernel`

## 文件

| 文件 | 说明 |
|---|---|
| `model.safetensors` | 454 MB，1.31 bpw 量化权重 |
| `sherry_model.py` | 模型定义 + Metal 内核（GEMV / batch GEMV / dequant） |
| `config.json` 等 | 标准 HF 配置，`model_file` 指向 sherry_model.py |

## 来源与许可

Apache-2.0，与上游各仓库一致。

- 本仓库修改自 [kuotient/Hy-MT2-1.8B-1.25Bit-MLX](https://huggingface.co/kuotient/Hy-MT2-1.8B-1.25Bit-MLX)：
  权重文件与其 bit 级一致（sha256 `20e835e3d231e7e96af87175249e528e6f2850fce63dc5042c7344111563aa16`），
  差异在 `sherry_model.py`——解码内核完全重写（batch 解码 8 行分块复用权重、
  解析码本 GEMV、continuous batching 路由），并发吞吐显著提升。
- 权重源头：[AngelSlim/Hy-MT2-1.8B-1.25Bit-GGUF](https://huggingface.co/AngelSlim/Hy-MT2-1.8B-1.25Bit-GGUF)
  （Sherry 官方 1.25-bit QAT checkpoint），由
  [hy-mt2-mlx](https://github.com/kuotient/hy-mt2-mlx) 无损转换为 MLX 布局。
- 模型与 Sherry 量化方案归 Tencent（Hunyuan / AngelSlim）：Sherry — arXiv
  2601.07892，Hy-MT2 — arXiv 2605.22064；STQ1_0 格式参考
  [llama.cpp PR #22836](https://github.com/ggml-org/llama.cpp/pull/22836)。
- 完整署名链见 [hy-mt2-mlx NOTICE](https://github.com/kuotient/hy-mt2-mlx)。
