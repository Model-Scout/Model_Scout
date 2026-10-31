---
language: [ar, bg, bn, ca, cs, da, de, el, en, es, fa, fi, fil, fr, he, hi, hu, id, is, it, ja, ko, lt, lv, mk, ms, nb, nl, pl, pt, ro, ru, sh, sk, sl, sv, ta, tr, uk, ur, vi, zh]
license: mit
multilinguality: multilingual
pretty_name: Word Embeddings for 1.67M Words in 42 Languages / 42 语 167 万词向量
size_categories:
- 1M<n<10M
source_datasets:
- vocabradar/wordfreq
tags:
- embeddings
- word-embeddings
- int8
- quantization
- multilingual
- llama.cpp
---

# Word Embeddings — 1,672,738 words in 42 languages

One 384-dimensional vector for **every word** in
[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq):
**42 languages, 1,672,738 words**. The word lists and the vector matrices are
row-for-row aligned, so a word's line number in the list is also its row in the
matrix and its frequency rank.

Vectors come from
[`hotchpotch/bekko-embedding-v1-a25m`](https://huggingface.co/hotchpotch/bekko-embedding-v1-a25m)
— a 24.9M-parameter multilingual ModernBERT encoder (MIT), mean pooling,
L2-normalized, 384 dimensions (Matryoshka 256 / 128 / 64). Inference runs on
llama.cpp with the official BF16 GGUF (`--embedding --pooling mean
--embd-normalize 2`, Vulkan GPU offload). Each normalized vector is then
quantized to **int8 with scale 127**, which keeps the whole dataset at about
612 MiB while preserving cosine similarity to within ~0.001.

> 中文版请见下方：[中文版说明](#zh)

## Files

```
WordEmbedding/
├── README.md                  # this card, bilingual
├── meta.json                  # model, format, per-language counts
├── files.json                 # size + SHA-256 of every data file
├── tools/
│   ├── build_dataset.py       # embed (llama.cpp) + finalize (meta/files)
│   ├── gen_readme.py          # regenerate the generated tables below
│   └── verify.py              # re-check sizes, SHA-256, row alignment
└── data/
    ├── <lang>.words.txt       # UTF-8 words, one per line, frequency order
    └── <lang>.int8.vector    # int8 vectors, row-major, N × 384
```

One pair of files per language (`en`, `zh`, `ar`, … — 42 in total).

## Data format

For a language `xx`:

- `<xx>.words.txt` — plain UTF-8, **one word per line**, in cleaned
  wordfreq order (descending frequency). Line `i` (0-based) has frequency rank
  `i + 1`.
- `<xx>.int8.vector` — raw **int8**, **row-major**, shape `N × 384`, no header.
  Row `i` is the vector of line `i` in the words file.
- `N = file size / 384`.
- Dequantize with `v = int8 / 127.0`. Rows were L2-normalized *before*
  quantization, so the result is close to unit length.
- Cosine similarity: `dot(a, b) / 127²` after casting to `float32` or `int32`.
  Do **not** call `numpy.dot` directly on two `int8` arrays — the accumulator
  overflows for 384 dimensions.

## Quick start

```python
import numpy as np

words = open("data/en.words.txt", encoding="utf-8").read().splitlines()
vec = np.memmap("data/en.int8.vector", dtype=np.int8, mode="r").reshape(-1, 384)
q = vec.astype(np.float32) / 127.0          # N × 384, approximately unit length

i = words.index("apple")
sims = q @ q[i]                            # cosine similarities
for j in np.argsort(-sims)[1:11]:
    print(f"{words[j]:20s} {sims[j]:.4f}")
```

The same matrix works across languages: `apple` is close to `苹果`, `pomme`,
`Apfel`, and so on, because bekko is a multilingual model.

## Precision

int8 quantization was measured on 1,000 English words:

| metric | value |
|--------|-------|
| cosine (float32 ↔ int8), min / mean | 0.99885 / 0.99902 |
| top-10 neighbour overlap (200 queries) | 98.3% |

That is well below the semantic spacing between unrelated words and is the
reason the dataset can ship at 384 bytes per word. If you need higher fidelity,
rebuild with a different `SCALE`/dtype in `tools/build_dataset.py`.

`meta.json → languages.<code>.zero_vectors` records how many rows are all zero
(words that produced no model tokens); see the per-language entries.

## Model and build

| item | value |
|------|-------|
| base model | `hotchpotch/bekko-embedding-v1-a25m` (MIT) |
| GGUF | `hotchpotch/bekko-embedding-v1-a25m-GGUF`, `BF16`, 252,522,944 bytes, SHA-256 `f85eda97…93d559` |
| architecture | ModernBERT, 24.9M active parameters |
| output | 384 dimensions, mean pooling, L2-normalized |
| context | 8192 tokens (words are far shorter) |
| runtime | llama.cpp `llama-server --embedding` (Vulkan GPU offload) |

```bash
# 1) place the GGUF in work/models/ (auto-downloaded from hf-mirror if absent)
# 2) point at your llama.cpp build if it is not BrowserExtention/backend/bin/llamacpp
python tools/build_dataset.py all
# or a subset / a re-run
python tools/build_dataset.py embed --langs en zh --force
python tools/build_dataset.py finalize
```

`build_dataset.py` starts (or reuses) a local `llama-server`, posts batches of
2048 words to `/v1/embeddings` (base64 float32 responses), and **fsyncs every
batch** to `data/<lang>.int8.vector.part`, with progress in `work/parts/<lang>.json`. An
interrupted run resumes at the last durable batch instead of redoing the whole
language; the `.part` is renamed to `<lang>.int8.vector` only after the final batch.
On a Vulkan GPU this sustains roughly 700–1,200 words/s, so the full 42-language
run takes tens of minutes, not hours. Exact provenance (model hash, llama.cpp
build, per-language backend) is recorded in `meta.json`.

Two disjoint language sets can run as separate tasks on different ports, for
example a GPU worker and a CPU worker:

```bash
python tools/build_dataset.py embed --langs ta ru sk --port 18083 --gpu-layers 99
python tools/build_dataset.py embed --langs lt tr fi --port 18085 --gpu-layers 0 --threads 8
```

## Languages

<!-- BEGIN GENERATED LANGUAGE TABLE -->
| code | language | native name | words | vectors (MiB) |
|------|----------|-------------|------:|--------------:|
| ar | Arabic | العربية | 55,611 | 20.37 |
| bg | Bulgarian | български | 35,848 | 13.13 |
| bn | Bengali | বাংলা | 33,062 | 12.11 |
| ca | Catalan | català | 27,028 | 9.90 |
| cs | Czech | čeština | 51,744 | 18.95 |
| da | Danish | dansk | 29,321 | 10.74 |
| de | German | Deutsch | 38,989 | 14.28 |
| el | Greek | Ελληνικά | 43,191 | 15.82 |
| en | English | English | 28,223 | 10.34 |
| es | Spanish | español | 34,740 | 12.72 |
| fa | Persian | فارسی | 30,108 | 11.03 |
| fi | Finnish | suomi | 59,143 | 21.66 |
| fil | Filipino | Filipino | 30,098 | 11.02 |
| fr | French | français | 31,203 | 11.43 |
| he | Hebrew | עברית | 57,405 | 21.02 |
| hi | Hindi | हिन्दी | 24,031 | 8.80 |
| hu | Hungarian | magyar | 46,525 | 17.04 |
| id | Indonesian | Bahasa Indonesia | 30,967 | 11.34 |
| is | Icelandic | íslenska | 42,207 | 15.46 |
| it | Italian | italiano | 35,954 | 13.17 |
| ja | Japanese | 日本語 | 27,856 | 10.20 |
| ko | Korean | 한국어 | 26,807 | 9.82 |
| lt | Lithuanian | lietuvių | 63,973 | 23.43 |
| lv | Latvian | latviešu | 45,464 | 16.65 |
| mk | Macedonian | македонски | 32,925 | 12.06 |
| ms | Malay | Bahasa Melayu | 28,571 | 10.46 |
| nb | Norwegian Bokmål | norsk bokmål | 25,994 | 9.52 |
| nl | Dutch | Nederlands | 28,715 | 10.52 |
| pl | Polish | polski | 49,664 | 18.19 |
| pt | Portuguese | português | 33,123 | 12.13 |
| ro | Romanian | română | 43,279 | 15.85 |
| ru | Russian | русский | 59,604 | 21.83 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | 54,698 | 20.03 |
| sk | Slovak | slovenčina | 59,414 | 21.76 |
| sl | Slovenian | slovenščina | 53,882 | 19.73 |
| sv | Swedish | svenska | 30,515 | 11.17 |
| ta | Tamil | தமிழ் | 64,756 | 23.71 |
| tr | Turkish | Türkçe | 63,130 | 23.12 |
| uk | Ukrainian | українська | 46,286 | 16.95 |
| ur | Urdu | اردو | 22,442 | 8.22 |
| vi | Vietnamese | Tiếng Việt | 10,519 | 3.85 |
| zh | Chinese | 中文 | 35,723 | 13.08 |
| **total** | 42 languages | — | 1,672,738 | 612.57 |
<!-- END GENERATED LANGUAGE TABLE -->

*words* is the number of vectors in that language; *vectors* is the size of the
`.int8.vector` file. The total row sums both columns.

## Licence and citation

The embedding model is MIT-licensed. The word lists are derived from
[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq)
(MIT metadata; upstream wordfreq 3.0.2). If you use this dataset, cite the
model and the word list:

```bibtex
@misc{bekko_embedding_v1_a25m,
  title  = {bekko-embedding-v1-a25m},
  author = {hotchpotch},
  year   = {2026},
  url    = {https://huggingface.co/hotchpotch/bekko-embedding-v1-a25m}
}
@misc{vocabradar_wordfreq,
  title  = {Cleaned Word Frequency Lists (42 languages)},
  author = {VocabRadar},
  year   = {2026},
  url    = {https://huggingface.co/datasets/vocabradar/wordfreq}
}
```

## About VocabRadar

This dataset is a **VocabRadar** project: it gives every word of
[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq) a vector, so
the vocabulary radar can place a word in semantic space as soon as it meets it.

The [VocabRadar browser extension](https://vocabradar.com) marks up the words you do not
know yet while you watch videos or browse the web: definitions in place, translation,
bilingual subtitles and annotated subtitles. Whatever you looked up can go on to
[vocabradar.com](https://vocabradar.com), which turns it into related exercises and games
so the words actually stick.

---

<a id="zh"></a>

# 42 语 167 万词向量

为 [vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq)
清洗词表中的**每一个词**提供一个 384 维向量：**42 种语言、1,672,738 个词**。
词表与向量矩阵逐行对齐——词在词表中的行号就是它在矩阵中的行号，也是它的词频排名。

向量由
[`hotchpotch/bekko-embedding-v1-a25m`](https://huggingface.co/hotchpotch/bekko-embedding-v1-a25m)
生成——2490 万激活参数的多语言 ModernBERT（MIT），mean pooling、L2 归一化、384 维
（Matryoshka 可截断到 256 / 128 / 64）。推理走 llama.cpp 官方 BF16 GGUF
（`--embedding --pooling mean --embd-normalize 2`，Vulkan GPU 卸载），随后把每条归一化向量
**按 127 的比例量化为 int8**：全量约 612 MiB，余弦相似度误差约 0.001。

## 文件

```
WordEmbedding/
├── README.md                  # 本数据卡（中英双语）
├── meta.json                  # 模型、格式、逐语言统计
├── files.json                 # 每个数据文件的大小与 SHA-256
├── tools/
│   ├── build_dataset.py       # 推理（llama.cpp）+ 收尾（meta/files）
│   ├── gen_readme.py          # 重生成下方语言表
│   └── verify.py              # 复核大小、SHA-256、词表与矩阵对齐
└── data/
    ├── <lang>.words.txt       # UTF-8 词表，一行一词，按词频降序
    └── <lang>.int8.vector    # int8 向量，行优先，N × 384
```

每种语言一对文件（`en`、`zh`、`ar`……共 42 种）。

## 数据格式

以语言 `xx` 为例：

- `<xx>.words.txt` —— 明文 UTF-8，**一行一词**，沿用清洗版 wordfreq 的词频降序；
  第 `i` 行（从 0 起）的词频排名为 `i + 1`。
- `<xx>.int8.vector` —— 裸 **int8**、**行优先**、形状 `N × 384`、无文件头；
  第 `i` 行对应词表第 `i` 行的词。
- `N = 文件字节数 / 384`。
- 反量化：`v = int8 / 127.0`。量化前每行已做 L2 归一化，因此反量化后近似单位长度。
- 余弦相似度：转成 `float32` 或 `int32` 后 `dot(a, b) / 127²`。
  **不要**直接对两个 `int8` 数组做 `numpy.dot`——384 维累加会溢出。

## 快速开始

```python
import numpy as np

words = open("data/zh.words.txt", encoding="utf-8").read().splitlines()
vec = np.memmap("data/zh.int8.vector", dtype=np.int8, mode="r").reshape(-1, 384)
q = vec.astype(np.float32) / 127.0          # N × 384，近似单位长度

i = words.index("苹果")
sims = q @ q[i]
for j in np.argsort(-sims)[1:11]:
    print(f"{words[j]:10s} {sims[j]:.4f}")
```

同一套矩阵天然跨语言：`苹果` 会靠近 `apple`、`pomme`、`Apfel` 等——bekko 是多语言模型。

## 精度

在 1000 个英文词上实测 int8 量化：

| 指标 | 数值 |
|------|------|
| float32 ↔ int8 余弦，最小 / 平均 | 0.99885 / 0.99902 |
| Top-10 邻居重合率（200 次查询） | 98.3% |

误差远小于无关词之间的语义间距，这也是每个词只占 384 字节仍可用的原因。
若需要更高保真度，可在 `tools/build_dataset.py` 中调整 `SCALE` 或改用更高精度重建。

`meta.json → languages.<code>.zero_vectors` 记录全零行数（分词后没有 token 的词）；
逐语言数值见该字段。

## 模型与构建

| 项目 | 值 |
|------|----|
| 基座模型 | `hotchpotch/bekko-embedding-v1-a25m`（MIT） |
| GGUF | `hotchpotch/bekko-embedding-v1-a25m-GGUF`，`BF16`，252,522,944 字节，SHA-256 `f85eda97…93d559` |
| 架构 | ModernBERT，2490 万激活参数 |
| 输出 | 384 维，mean pooling，L2 归一化 |
| 上下文 | 8192 token（单词远短于此） |
| 运行时 | llama.cpp `llama-server --embedding`（Vulkan GPU 卸载） |

```bash
# 1) 把 GGUF 放到 work/models/（缺失时会自动从 hf-mirror 下载）
# 2) 若 llama.cpp 不在 BrowserExtention/backend/bin/llamacpp，用参数指定
python tools/build_dataset.py all
# 只跑部分语言 / 强制重跑
python tools/build_dataset.py embed --langs en zh --force
python tools/build_dataset.py finalize
```

`build_dataset.py` 会启动（或复用）本地 `llama-server`，每批 2048 词 POST 到
`/v1/embeddings`（base64 float32 回包），**每批 fsync 落盘**到
`data/<lang>.int8.vector.part`，进度记在 `work/parts/<lang>.json`。中断后从最后一批
续跑，不重做整种语言；最后一批完成后才把 `.part` 改名为 `<lang>.int8.vector`。
Vulkan GPU 上约 700–1,200 词/秒，全量 42 语是几十分钟级。模型哈希、llama.cpp
版本与逐语言后端写入 `meta.json`。

两个任务可在不同端口上跑互不相交的语言集，例如一个 GPU 任务加一个 CPU 任务：

```bash
python tools/build_dataset.py embed --langs ta ru sk --port 18083 --gpu-layers 99
python tools/build_dataset.py embed --langs lt tr fi --port 18085 --gpu-layers 0 --threads 8
```

## 语言表

<!-- BEGIN GENERATED LANGUAGE TABLE -->
| 代码 | 语言 | 本地名 | 词数 | 向量体积 (MiB) |
|------|------|--------|------:|---------------:|
| ar | Arabic | العربية | 55,611 | 20.37 |
| bg | Bulgarian | български | 35,848 | 13.13 |
| bn | Bengali | বাংলা | 33,062 | 12.11 |
| ca | Catalan | català | 27,028 | 9.90 |
| cs | Czech | čeština | 51,744 | 18.95 |
| da | Danish | dansk | 29,321 | 10.74 |
| de | German | Deutsch | 38,989 | 14.28 |
| el | Greek | Ελληνικά | 43,191 | 15.82 |
| en | English | English | 28,223 | 10.34 |
| es | Spanish | español | 34,740 | 12.72 |
| fa | Persian | فارسی | 30,108 | 11.03 |
| fi | Finnish | suomi | 59,143 | 21.66 |
| fil | Filipino | Filipino | 30,098 | 11.02 |
| fr | French | français | 31,203 | 11.43 |
| he | Hebrew | עברית | 57,405 | 21.02 |
| hi | Hindi | हिन्दी | 24,031 | 8.80 |
| hu | Hungarian | magyar | 46,525 | 17.04 |
| id | Indonesian | Bahasa Indonesia | 30,967 | 11.34 |
| is | Icelandic | íslenska | 42,207 | 15.46 |
| it | Italian | italiano | 35,954 | 13.17 |
| ja | Japanese | 日本語 | 27,856 | 10.20 |
| ko | Korean | 한국어 | 26,807 | 9.82 |
| lt | Lithuanian | lietuvių | 63,973 | 23.43 |
| lv | Latvian | latviešu | 45,464 | 16.65 |
| mk | Macedonian | македонски | 32,925 | 12.06 |
| ms | Malay | Bahasa Melayu | 28,571 | 10.46 |
| nb | Norwegian Bokmål | norsk bokmål | 25,994 | 9.52 |
| nl | Dutch | Nederlands | 28,715 | 10.52 |
| pl | Polish | polski | 49,664 | 18.19 |
| pt | Portuguese | português | 33,123 | 12.13 |
| ro | Romanian | română | 43,279 | 15.85 |
| ru | Russian | русский | 59,604 | 21.83 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | 54,698 | 20.03 |
| sk | Slovak | slovenčina | 59,414 | 21.76 |
| sl | Slovenian | slovenščina | 53,882 | 19.73 |
| sv | Swedish | svenska | 30,515 | 11.17 |
| ta | Tamil | தமிழ் | 64,756 | 23.71 |
| tr | Turkish | Türkçe | 63,130 | 23.12 |
| uk | Ukrainian | українська | 46,286 | 16.95 |
| ur | Urdu | اردو | 22,442 | 8.22 |
| vi | Vietnamese | Tiếng Việt | 10,519 | 3.85 |
| zh | Chinese | 中文 | 35,723 | 13.08 |
| **合计** | 42 种语言 | — | 1,672,738 | 612.57 |
<!-- END GENERATED LANGUAGE TABLE -->

*词数* 为该语言的向量条数，*向量体积* 为 `.int8.vector` 文件大小；合计行只对这两列求和。

## 许可与引用

向量模型为 MIT 许可；词表来自
[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq)
（元数据 MIT；上游 wordfreq 3.0.2）。使用本数据集请同时引用模型与词表：

```bibtex
@misc{bekko_embedding_v1_a25m,
  title  = {bekko-embedding-v1-a25m},
  author = {hotchpotch},
  year   = {2026},
  url    = {https://huggingface.co/hotchpotch/bekko-embedding-v1-a25m}
}
@misc{vocabradar_wordfreq,
  title  = {Cleaned Word Frequency Lists (42 languages)},
  author = {VocabRadar},
  year   = {2026},
  url    = {https://huggingface.co/datasets/vocabradar/wordfreq}
}
```

## 关于 VocabRadar

这项工作是 **VocabRadar**（词汇雷达）的工作：为
[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq) 的每个词给出一个向量，
让词汇雷达一见到某个词就能把它放进语义空间。

[VocabRadar 浏览器扩展](https://vocabradar.com) 让你在看视频、刷网页时把还不认识的生词就地标注出来
—— 释义、翻译、双语字幕、注释字幕；查过的词还能送到 [vocabradar.com](https://vocabradar.com)，
自动生成相关习题与游戏，把词真正记住。
