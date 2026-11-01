---
license: apache-2.0
language:
- en
- zh
- ja
- ko
- ar
- de
- fr
- es
- it
- pt
- nl
- pl
- el
- vi
tags:
- asr
- automatic-speech-recognition
- cohere
- gguf
- multilingual
- speech-to-text
- transcription
base_model:
- CohereLabs/cohere-transcribe-03-2026
---

# Cohere Transcribe 03-2026 GGUF

Cohere 公司推出的多语言专业转录模型，支持14种语言。

## 模型简介

Cohere Transcribe 是 Cohere 公司的多语言语音转录模型：

- **发布时间**：2026年3月
- **语言支持**：14种语言（中英日韩法德西葡等主流语言）
- **量化格式**：GGUF (llama.cpp 兼容)
- **适用场景**：专业转录、客服记录、播客转写、会议纪要

## 支持语言 (14种)

| 语言 | 代码 | 语言 | 代码 | 语言 | 代码 |
|------|------|------|------|------|------|
| 英语 | en | 中文 | zh | 日语 | ja |
| 韩语 | ko | 阿拉伯语 | ar | 德语 | de |
| 法语 | fr | 西班牙语 | es | 意大利语 | it |
| 葡萄牙语 | pt | 荷兰语 | nl | 波兰语 | pl |
| 希腊语 | el | 越南语 | vi | - | - |

## 可用量化版本

| 文件名 | 量化类型 | 文件大小 | 说明 |
|--------|----------|----------|------|
| cohere-transcribe-03-2026-Q4_K_M.gguf | Q4_K_M | ~适中 | 推荐平衡精度与速度 |
| cohere-transcribe-03-2026-Q5_K_M.gguf | Q5_K_M | ~较大 | 更高精度 |
| cohere-transcribe-03-2026-Q6_K.gguf | Q6_K | ~大 | 高精度 |
| cohere-transcribe-03-2026-Q8_0.gguf | Q8_0 | ~更大 | 最高量化精度 |

> 注意：F16/BF16 版本已排除，推荐使用量化版本以获得更好的性能和存储效率。

## 使用方法

### llama.cpp 命令行

```bash
./main -m cohere-transcribe-03-2026-Q4_K_M.gguf -f audio.wav --output-txt
```

### Python (llama-cpp-python)

```python
from llama_cpp import Llama

# 加载模型
llm = Llama(
    model_path="cohere-transcribe-03-2026-Q4_K_M.gguf",
    n_gpu_layers=-1,
)

# 语音识别
result = llm.transcribe("audio.wav")
print(result["text"])
```

## 性能特点

- 多语言专业级转录准确率
- 支持中英日韩等14种主流语言
- 支持多种音频格式
- 对口音有一定适应性
- 适合长时间音频处理

## 技术规格

- **采样率**: 16kHz
- **输入格式**: WAV/PCM/MP3 等常见音频格式
- **输出格式**: 文本

## 许可证

Apache 2.0 License

## 致谢

- 原始模型：[CohereLabs/cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)
- GGUF转换：由 voconly 团队完成