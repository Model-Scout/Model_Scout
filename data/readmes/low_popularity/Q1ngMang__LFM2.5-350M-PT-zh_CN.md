---
library_name: transformers
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
base_model:
- LiquidAI/LFM2.5-350M
tags:
- liquid
- lfm2.5
- edge
datasets:
- 0xDing/wikipedia-cn-20230720-filtered
license: cc-by-sa-3.0
---

# LFM2.5-350M-PT-zh_CN
基于 [LiquidAI/LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M) 进行 Pre-Training 的模型。<br>
数据集 [0xDing/wikipedia-cn-20230720-filtered](https://huggingface.co/datasets/0xDing/wikipedia-cn-20230720-filtered)

## 协议冲突
LFM 1.0 规定年收入小于1000万美元的公司的免费商用，收入大于1000万美元**需要**向LiquidAI购买商业许可证，而 CC BY-SA 3.0 规定可以商用，因此存在冲突。<br>
该模型优先使用 CC BY-SA 3.0，但并**不代表**收入大于1000万美元**不需要**向LiquidAI购买商业许可证。

## 排泄环境
厕所：[LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory)<br>
马桶：[NVIDIA Tesla V100 SXM2 16GB](https://www.techpowerup.com/gpu-specs/tesla-v100-sxm2-16-gb.c3018)


### 肠道
| 项 | 值 |
| - | - |
| 微调方法 | LoRA |
| 量化等级 | 4 |
| 量化方法 | bnb |
| 对话模板 | lfm2 |
| 训练阶段 | Pre-Training |
| 学习率 | 4.5e-4 |
| 训练轮数 | 1.0 |
| 计算类型 | pure_bf16 |
| 截断长度 | 1968 |
| 批处理大小 | 4 |
| 梯度累积 | 256 |
| 验证集比例 | 0.05 |
| 序列打包 | True |
| 额外参数 | {"optim": "paged_adamw_8bit"} |
| LoRA秩 | 16 |
| LoRA缩放系数 | 32 |

### 排泄物
| 项 | 值 |
| - | - |
| 输入Token | 158,319,896 |
| 计算量 | 254,539,784GF |
| 训练损失 | 3.8676 |
| 训练耗时 | 9:52:32.56 |
| 每秒训练样本数 | 2.264 |
| 每秒训练步数 | 0.002 |
| 验证损失 | 3.5849 |
| 验证困惑度 | 36.0495 |
| 验证耗时 | 0:12:56.50 |
| 每秒验证样本数 | 5.525 |
| 每秒验证步数 | 1.382 |

### 排泄过程
![training_loss](https://cdn-uploads.huggingface.co/production/uploads/6a25efe68536ff11116416bf/qXbvIS_QwmxUzelMZIYfA.png)