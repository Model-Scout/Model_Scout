---
license: apache-2.0
language:
- af
- am
- ar
- as
- az
- ba
- be
- bg
- bn
- bo
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fa
- fi
- fo
- fr
- gl
- gu
- haw
- ha
- he
- hi
- hr
- ht
- hu
- hy
- id
- is
- it
- ja
- jw
- ka
- kk
- km
- kn
- ko
- la
- lb
- ln
- lo
- lt
- lv
- mg
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- my
- ne
- nl
- nn
- no
- oc
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- sn
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- tg
- th
- tk
- tl
- tr
- tt
- uk
- ur
- uz
- vi
- yi
- yo
- yue
- zh
tags:
- asr
- automatic-speech-recognition
- openai
- whisper
- gguf
- multilingual
- speech-to-text
base_model:
- openai/whisper-large-v3-turbo
---

# Whisper Large v3 Turbo GGUF

OpenAI Whisper Large v3 的 Turbo 加速版本，支持100种语言的多语言语音识别标杆模型。

## 模型简介

Whisper Large v3 Turbo 是 OpenAI 推出的高效多语言语音识别模型：

- **基础版本**：Whisper Large v3
- **优化类型**：Turbo（速度优化版）
- **语言支持**：100种语言，覆盖全球绝大多数语种
- **量化格式**：GGUF (llama.cpp 兼容)
- **特点**：多语言支持、高准确率、速度快于原版
- **适用场景**：多语言转写、字幕生成、语音翻译

## 支持语言 (100种)

Whisper 支持的语言覆盖全球各大洲：

### 亚太语言
中文、粤语、日语、韩语、泰语、越南语、印尼语、马来语、菲律宾语、缅甸语、高棉语、老挝语、印地语、孟加拉语、乌尔都语、旁遮普语、古吉拉特语、泰卢固语、泰米尔语、卡纳达语、马拉雅拉姆语、僧伽罗语、尼泊尔语、藏语

### 欧洲语言
英语、德语、法语、西班牙语、葡萄牙语、意大利语、荷兰语、波兰语、俄语、乌克兰语、捷克语、斯洛伐克语、匈牙利语、罗马尼亚语、保加利亚语、塞尔维亚语、克罗地亚语、斯洛文尼亚语、希腊语、瑞典语、丹麦语、挪威语、芬兰语、爱尔兰语、威尔士语、巴斯克语、加泰罗尼亚语

### 中东和非洲语言
阿拉伯语、波斯语、土耳其语、希伯来语、阿姆哈拉语、斯瓦希里语、豪萨语、约鲁巴语、祖鲁语、南非荷兰语

### 其他语言
爪哇语、巽他语、阿塞拜疆语、哈萨克语、吉尔吉斯语、乌兹别克语、塔吉克语、土库曼语、格鲁吉亚语、亚美尼亚语

## 可用量化版本

| 文件名 | 量化类型 | 文件大小 | 说明 |
|--------|----------|----------|------|
| whisper-large-v3-turbo-Q4_K_M.gguf | Q4_K_M | ~最小 | 推荐日常使用 |
| whisper-large-v3-turbo-Q5_K_M.gguf | Q5_K_M | ~小 | 平衡精度 |
| whisper-large-v3-turbo-Q6_K.gguf | Q6_K | ~中 | 更高精度 |
| whisper-large-v3-turbo-Q8_0.gguf | Q8_0 | ~中高 | 最高量化精度 |

> 注意：F16 版本已排除，推荐使用量化版本。

## 使用方法

### llama.cpp 命令行

```bash
# 基础转写
./main -m whisper-large-v3-turbo-Q4_K_M.gguf -f audio.wav --output-txt

# 指定语言
./main -m whisper-large-v3-turbo-Q4_K_M.gguf -f audio.wav --language zh --output-txt
```

### Python (llama-cpp-python)

```python
from llama_cpp import Llama

llm = Llama(
    model_path="whisper-large-v3-turbo-Q4_K_M.gguf",
    n_gpu_layers=-1,
)

# 自动检测语言
result = llm.transcribe("audio.wav")
print(f"检测语言: {result['language']}")
print(f"转写文本: {result['text']}")

# 指定中文
result = llm.transcribe("audio.wav", language="zh")
```

### whisper.cpp 风格

```bash
whisper-cpp -m whisper-large-v3-turbo-Q4_K_M.gguf -f audio.mp3 --output-srt
```

## 模型特点

### 多语言支持

支持 99+ 种语言，包括但不限于：

| 语言 | 代码 | 性能 |
|------|------|------|
| 中文 | zh | 优秀 |
| 英语 | en | 优秀 |
| 日语 | ja | 优秀 |
| 韩语 | ko | 优秀 |
| 德语 | de | 优秀 |
| 法语 | fr | 优秀 |
| 西班牙语 | es | 优秀 |
| 俄语 | ru | 良好 |

### Turbo 优化

相比原始 Whisper Large v3：
- **速度提升**：约 2-3 倍
- **精度保持**：轻微下降但可接受
- **内存优化**：更好的内存效率

## 性能基准

| 测试集 | WER (英文) |
|--------|------------|
| LibriSpeech test-clean | ~2-3% |
| LibriSpeech test-other | ~5-6% |

## 技术规格

- **架构**：基于 Transformer 的编码器-解码器
- **采样率**：16kHz
- **最大音频长度**：30秒片段（可拼接处理长音频）
- **支持格式**：WAV、MP3、FLAC 等

## 许可证

MIT License

## 致谢

- 原始模型：[openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)
- GGUF转换：由 voconly 团队完成