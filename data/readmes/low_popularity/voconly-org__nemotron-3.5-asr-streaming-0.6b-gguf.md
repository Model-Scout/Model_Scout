---
license: openmdw-1.1
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
- ru
- tr
- hi
- vi
- uk
- pl
- sv
- cs
- nb
- da
- bg
- fi
- hr
- sk
- hu
- ro
- et
tags:
- asr
- automatic-speech-recognition
- nvidia
- nemotron
- gguf
- streaming
- multilingual
- speech-to-text
base_model:
- nvidia/nemotron-3.5-asr-streaming-0.6b
---

# Nemotron 3.5 ASR Streaming 0.6B GGUF

NVIDIA 推出的轻量级流式多语言语音识别模型，支持32种语言，专为实时转录场景优化。

## 模型简介

NVIDIA Nemotron 3.5 ASR Streaming 是专为实时流式处理设计的多语言语音识别模型：

- **参数量**：0.6B (600M)
- **语言支持**：32种语言（含中英日韩及欧洲主要语言）
- **量化格式**：GGUF (llama.cpp 兼容)
- **特点**：流式处理、低延迟、轻量级、多语言
- **适用场景**：实时字幕、直播转写、语音助手、会议实时记录

## 支持语言 (32种)

| 语言 | 代码 | 语言 | 代码 | 语言 | 代码 |
|------|------|------|------|------|------|
| 英语(美) | en-US | 英语(英) | en-GB | 中文 | zh-CN |
| 日语 | ja-JP | 韩语 | ko-KR | 阿拉伯语 | ar-AR |
| 德语 | de-DE | 法语(法) | fr-FR | 法语(加) | fr-CA |
| 西班牙语(美) | es-US | 西班牙语(西) | es-ES | 意大利语 | it-IT |
| 葡萄牙语(巴) | pt-BR | 葡萄牙语(葡) | pt-PT | 荷兰语 | nl-NL |
| 土耳其语 | tr-TR | 俄语 | ru-RU | 印地语 | hi-IN |
| 越南语 | vi-VN | 乌克兰语 | uk-UA | 波兰语 | pl-PL |
| 瑞典语 | sv-SE | 捷克语 | cs-CZ | 挪威语 | nb-NO |
| 丹麦语 | da-DK | 保加利亚语 | bg-BG | 芬兰语 | fi-FI |
| 克罗地亚语 | hr-HR | 斯洛伐克语 | sk-SK | 匈牙利语 | hu-HU |
| 罗马尼亚语 | ro-RO | 爱沙尼亚语 | et-EE | - | - |

## 可用量化版本

| 文件名 | 量化类型 | 文件大小 | 说明 |
|--------|----------|----------|------|
| nemotron-3.5-asr-streaming-0.6b-Q4_K_M.gguf | Q4_K_M | ~最小 | 推荐实时应用 |
| nemotron-3.5-asr-streaming-0.6b-Q5_K_M.gguf | Q5_K_M | ~小 | 平衡选择 |
| nemotron-3.5-asr-streaming-0.6b-Q6_K.gguf | Q6_K | ~中 | 更高精度 |
| nemotron-3.5-asr-streaming-0.6b-Q8_0.gguf | Q8_0 | ~中高 | 最高量化精度 |

> 注意：F16/F32 版本已排除，推荐使用量化版本以获得最佳流式性能。

## 使用方法

### 实时流式转录

```python
from llama_cpp import Llama
import sounddevice as sd
import numpy as np

llm = Llama(
    model_path="nemotron-3.5-asr-streaming-0.6b-Q4_K_M.gguf",
    n_gpu_layers=-1,
)

# 实时录音转写
def callback(indata, frames, time, status):
    # 流式处理音频
    result = llm.transcribe_buffer(indata)
    if result["text"]:
        print(result["text"], end="", flush=True)

with sd.InputStream(callback=callback):
    input("按 Enter 停止...")
```

### 离线批处理

```bash
./main -m nemotron-3.5-asr-streaming-0.6b-Q4_K_M.gguf -f audio.wav --output-txt
```

## 性能特点

- **低延迟**：专为实时处理优化，延迟极低
- **轻量级**：模型小巧，资源占用少
- **多语言**：支持32种语言，覆盖全球主要语种
- **流式友好**：支持音频流逐步输入
- **边缘部署**：适合在边缘设备上运行

## 技术规格

- **架构**：基于 Transformer 的流式编码器
- **采样率**：16kHz
- **延迟**：<100ms (取决于硬件)
- **内存占用**：最低约 500MB (Q4_K_M)

## 应用场景

1. **实时字幕**：直播、视频会议实时字幕
2. **语音助手**：智能家居、车载系统
3. **客服系统**：实时通话转写
4. **无障碍辅助**：听力障碍辅助工具

## 许可证

CC BY 4.0 License

## 致谢

- 原始模型：[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)
- GGUF转换：由 voconly 团队完成