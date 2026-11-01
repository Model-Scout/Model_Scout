---
license: apache-2.0
language:
- zh
- en
- yue
- ar
- de
- fr
- es
- pt
- id
- it
- ko
- ru
- th
- vi
- ja
- tr
- hi
- ms
- nl
- sv
- da
- fi
- pl
- cs
- fil
- fa
- el
- ro
- hu
- mk
tags:
- asr
- automatic-speech-recognition
- qwen
- gguf
- multilingual
- speech-to-text
base_model:
- Qwen/Qwen3-ASR-1.7B
---

# Qwen3-ASR-1.7B GGUF

阿里通义千问团队推出的多语言自动语音识别(ASR)模型，支持30种语言。

## 模型简介

Qwen3-ASR-1.7B 是阿里巴巴通义千问团队的语音识别模型，具有以下特点：

- **参数量**：1.7B
- **语言支持**：30种语言（中英日韩法德西葡俄阿拉伯语等）
- **量化格式**：GGUF (llama.cpp 兼容)
- **适用场景**：语音转文字、字幕生成、会议记录转写、多语言转录

## 支持语言 (30种)

| 语言 | 代码 | 语言 | 代码 | 语言 | 代码 |
|------|------|------|------|------|------|
| 中文 | zh | 英语 | en | 粤语 | yue |
| 日语 | ja | 韩语 | ko | 阿拉伯语 | ar |
| 德语 | de | 法语 | fr | 西班牙语 | es |
| 葡萄牙语 | pt | 意大利语 | it | 俄语 | ru |
| 泰语 | th | 越南语 | vi | 印地语 | hi |
| 土耳其语 | tr | 印尼语 | id | 马来语 | ms |
| 荷兰语 | nl | 瑞典语 | sv | 丹麦语 | da |
| 芬兰语 | fi | 波兰语 | pl | 捷克语 | cs |
| 菲律宾语 | fil | 波斯语 | fa | 希腊语 | el |
| 罗马尼亚语 | ro | 匈牙利语 | hu | 马其顿语 | mk |

## 可用量化版本

| 文件名 | 量化类型 | 文件大小 | 说明 |
|--------|----------|----------|------|
| Qwen3-ASR-1.7B-Q4_K_M.gguf | Q4_K_M | ~1.1 GB | 推荐平衡精度与速度 |
| Qwen3-ASR-1.7B-Q5_K_M.gguf | Q5_K_M | ~1.3 GB | 更高精度 |
| Qwen3-ASR-1.7B-Q6_K.gguf | Q6_K | ~1.5 GB | 高精度 |
| Qwen3-ASR-1.7B-Q8_0.gguf | Q8_0 | ~1.8 GB | 最高量化精度 |

## 使用方法

### llama.cpp 命令行

```bash
./main -m Qwen3-ASR-1.7B-Q4_K_M.gguf -f audio.wav --output-txt
```

### Python (llama-cpp-python)

```python
from llama_cpp import Llama

# 加载模型
llm = Llama(
    model_path="Qwen3-ASR-1.7B-Q4_K_M.gguf",
    n_gpu_layers=-1,  # 使用GPU加速
)

# 进行语音识别
result = llm.transcribe("audio.wav")
print(result["text"])
```

### whisper.cpp 风格调用

```cpp
whisper_context * ctx = whisper_init_from_file("Qwen3-ASR-1.7B-Q4_K_M.gguf");
whisper_full(ctx, wparams, samples, n_samples, nullptr, 0);
```

## 性能特点

- 多语言识别准确率高，支持30种语言
- 中文识别尤其优秀，支持普通话和粤语
- 对噪音有一定抗干扰能力
- 支持实时流式转写

## 技术规格

- **架构**: 基于 Transformer 的编码器-解码器结构
- **采样率**: 16kHz
- **输入格式**: WAV/PCM 音频
- **输出格式**: 文本

## 许可证

Apache 2.0 License

## 致谢

- 原始模型：[Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)
- GGUF转换：由 voconly 团队完成