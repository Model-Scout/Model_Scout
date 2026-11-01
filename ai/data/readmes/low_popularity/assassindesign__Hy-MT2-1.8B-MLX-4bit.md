---
library_name: mlx
pipeline_tag: translation
base_model: tencent/Hy-MT2-1.8B
base_model_relation: quantized
tags:
- translation
- mlx
- hunyuan
- quantized
- 4bit
language:
- zh
- en
- fr
- pt
- es
- ja
- tr
- ru
- ar
- ko
- th
- it
- de
- vi
- ms
- id
- tl
- hi
- pl
- cs
- nl
- km
- my
- fa
- gu
- ur
- te
- mr
- he
- bn
- ta
- uk
- bo
- kk
- mn
- ug
license: other
license_name: tencent-hunyuan-community
license_link: https://huggingface.co/tencent/Hy-MT2-1.8B/blob/main/LICENSE.txt
---

# Hy-MT2-1.8B-MLX-4bit

这是腾讯混元翻译模型 [**tencent/Hy-MT2-1.8B**](https://huggingface.co/tencent/Hy-MT2-1.8B)
的 **Apple MLX 4-bit 量化版本**，用于在 Apple Silicon（Mac / iPhone / iPad）上本地、离线运行。

> 本仓库仅做**格式转换 + 权重量化**，未改变模型能力。所有翻译能力、支持语言、版权与许可均继承自原始模型。

## 模型信息

| 项目 | 值 |
| --- | --- |
| 基础模型 | tencent/Hy-MT2-1.8B |
| 架构 | `hunyuan_v1_dense`（`HunYuanDenseV1ForCausalLM`） |
| 参数量 | 1.8B |
| 量化 | 4-bit，affine，group_size 64（约 4.5 bits/weight） |
| 体积 | 约 970 MB |
| 层数 / 隐藏维度 | 32 / 2048 |
| 注意力头 | 16（KV 头 4，GQA）/ head_dim 128 |
| 词表 | 120818 |
| 特性 | QK-Norm、Dynamic-NTK RoPE、tied embeddings |
| 支持语言 | 33 种语言互译（中英为主） |

## 转换方式

```bash
pip install -U mlx-lm
mlx_lm.convert \
  --hf-path tencent/Hy-MT2-1.8B \
  -q --q-bits 4 \
  --mlx-path Hy-MT2-1.8B-MLX-4bit
```

## 使用方法

### Python（mlx-lm）

```bash
pip install -U mlx-lm
```

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load("<your-username>/Hy-MT2-1.8B-MLX-4bit")

# 混元 MT 无 system prompt，用显式方向指令，模型只输出译文
instruction = "将下面的英文翻译成中文。只输出中文译文，不要输出其它语言，不要解释。\n\nHello, nice to meet you."
prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": instruction}],
    tokenize=False, add_generation_prompt=True,
)

sampler = make_sampler(temp=0.7, top_p=0.6)
text = generate(model, tokenizer, prompt=prompt, max_tokens=256, sampler=sampler, verbose=True)
print(text)  # 你好，很高兴认识你。
```

### 命令行

```bash
mlx_lm.generate --model <your-username>/Hy-MT2-1.8B-MLX-4bit \
  --prompt "将下面的中文翻译成英文。只输出英文译文，不要解释。\n\n很高兴认识你。" \
  --temp 0.7 --top-p 0.6 --max-tokens 256
```

### Swift（mlx-swift-lm）注意事项

⚠️ 截至 `mlx-swift-lm` 3.31.x，Swift 端**尚未内置** `hunyuan_v1_dense` 架构，
直接加载会报 `unsupported model type`。需在工程内自行实现并注册该架构。
移植时注意两点：**RoPE 为 Dynamic-NTK**（`base = rope_theta * alpha^(head_dim/(head_dim-2))`）、
**QK-Norm 在 RoPE 之后**（与 Qwen3 相反）。

## 推荐推理参数

官方推荐（1.8B / 7B）：`temperature 0.7`，`top_p 0.6`，`top_k 20`，`repetition_penalty 1.05`。

## 提示词模板

混元 MT 无默认 system prompt。中英互译建议用显式方向约束，避免短句跑偏到第三语言：

```
将下面的<源语言>翻译成<目标语言>。只输出<目标语言>译文，不要输出其它语言，不要解释。

<原文>
```

## 量化影响

4-bit 量化会带来轻微质量损失，但对中英日常翻译影响很小，实测短句/常用句翻译准确、干净。
追求最高质量可用原始 bf16 模型或更高位量化（如 8-bit）。

## 许可协议

本模型遵循 **腾讯混元社区许可协议（Tencent Hunyuan Community License Agreement）**，
与原始模型 [tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B) 一致。使用前请阅读随附的 `LICENSE.txt`。

关键条款（摘要，以原文为准）：
- ✅ 允许商业使用、修改、分发、创建衍生品；
- ⚠️ 月活用户（MAU）达 **1 亿** 需另行向腾讯申请商业许可；
- 🌍 授权区域**不含欧盟（EU）、英国（UK）、韩国**；
- 📝 分发须保留 `LICENSE.txt` 与 `Notice` 声明；
- 🚫 不得用模型输出训练其他 AI 模型，不得生成有害/虚假内容。

## 致谢

- 原始模型：腾讯混元团队 [Tencent-Hunyuan/Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2)
- 量化框架：[Apple MLX](https://github.com/ml-explore/mlx) / [mlx-lm](https://github.com/ml-explore/mlx-lm)
