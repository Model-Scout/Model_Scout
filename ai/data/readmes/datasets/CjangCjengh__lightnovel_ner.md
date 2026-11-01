---
license: mit
task_categories:
- translation
- text-classification
language:
- ja
- zh
- ko
- th
---

# 轻小说多语言NER翻译对数据集

本数据集包含从日文轻小说及其官方翻译中自动提取的**命名实体识别（NER）翻译对**，涵盖人名、地名、组织名和专有名词四类实体。

## 数据来源

原始平行语料来自轻小说的**官方翻译版本**：

| 语言对 | 目录 | 来源 |
|--------|------|------|
| 日文→繁体中文 | `ja-zh/` | 台版官方翻译 |
| 日文→韩文 | `ja-ko/` | 韩版官方翻译 |
| 日文→泰文 | `ja-th/` | 泰版官方翻译 |

## 数据统计

| 语言对 | 系列数 | 卷数 | NER条目数 | PER（人名） | LOC（地名） | ORG（组织） | TERM（术语） |
|--------|--------|------|-----------|-------------|-------------|-------------|--------------|
| ja-zh | 1,055 | 4,687 | 709,698 | 231,234 | 77,095 | 75,639 | 325,730 |
| ja-ko | 314 | 1,129 | 197,736 | 62,447 | 20,431 | 20,476 | 94,382 |
| ja-th | 215 | 1,049 | 29,163 | 10,823 | 3,279 | 3,263 | 11,798 |
| **合计** | **1,584** | **6,865** | **936,597** | **304,504** | **100,805** | **99,378** | **431,910** |

## 文件说明

本数据集以 Parquet 格式发布，包含以下文件：

| 文件 | 大小 | 说明 |
|------|------|------|
| `ner_translations.parquet` | ~16 MB | 主数据集：全部三个语言对的 NER 翻译对，韩文/泰文已应用振假名多译修正（仅保留意译） |
| `ner_translations_no_ruby_fix.parquet` | ~16 MB | 未修正版本：与主数据集相同，但保留了韩文/泰文中振假名标注产生的全部译法（含振假名音译） |
| `ruby_fixes.parquet` | ~70 KB | 振假名多译修正详情：记录了所有被识别为振假名多译的条目及其意译/振假名音译拆分（ja-ko + ja-th，共 2,248 条） |

## 数据格式

### Parquet 表结构

```python
# 使用 HuggingFace Datasets
from datasets import load_dataset
ds = load_dataset("parquet", data_files="ner_translations.parquet")

# 使用 pandas
import pandas as pd
df = pd.read_parquet("ner_translations.parquet")

# 按语言对筛选
df_zh = df[df["lang_pair"] == "ja-zh"]

# 按实体类型筛选
df_per = df[df["type"] == "PER"]

# 查看某个系列覆盖了哪些卷
series_vols = df[df["series"] == "ソードアート・オンライン"].iloc[0]["covered"]
```

| 列名 | 类型 | 说明 |
|------|------|------|
| `lang_pair` | string | 语言对（ja-zh / ja-ko / ja-th） |
| `series` | string | 作品系列名（日文原名） |
| `src` | string | 日文原文实体 |
| `tgt` | list\<string\> | 对应的译文实体列表（可能有多个译法） |
| `type` | string | 实体类型（PER / LOC / ORG / TERM） |
| `covered` | list\<string\> | 该系列中被处理的卷 |

### 实体类型

| 类型 | 全称 | 说明 | 示例 |
|------|------|------|------|
| `PER` | Person | 人物名 | 草薙護堂、エリオ |
| `LOC` | Location | 地名/场所 | 東京、冥界 |
| `ORG` | Organization | 组织/团体 | 魔術協会、騎士団 |
| `TERM` | Term | 专有名词/术语 | 魔弾、固有結界 |

### ruby_fixes.parquet 表结构

| 列名 | 类型 | 说明 |
|------|------|------|
| `lang_pair` | string | 语言对（ja-ko / ja-th） |
| `series` | string | 作品系列名（日文原名） |
| `src` | string | 日文原文实体 |
| `type` | string | 实体类型（PER / LOC / ORG / TERM） |
| `native_tgt` | string | 意译（被保留的译法） |
| `loan_tgt` | list\<string\> | 音译列表（被移除的译法） |

### 关于多译文

部分条目的 `tgt` 字段包含多个译文，这通常由以下原因导致：

- **同一实体的不同翻译策略**：译者在不同卷/章节中采用了不同的翻译方式
- **振假名标注导致的多译**（主要出现在韩文和泰文中）：日文轻小说常在汉字词上方用振假名标注英文/片假名读音（如在「魔弾」上标注「マジック・ミサイル」），韩文/泰文译者可能同时翻译了汉字部分（意译）和振假名标注部分（音译），产生两种译法

主数据集（`ner_translations.parquet`）中已使用 LLM 自动识别并修正了这类振假名多译，仅保留意译部分。如需保留原始的全部译法（含振假名音译），请使用 `ner_translations_no_ruby_fix.parquet`。修正详情见 `ruby_fixes.parquet`。

## 提取方法

本数据集通过以下流程自动提取：

1. 将日文原文与对应语言的官方翻译对齐为平行句对
2. 使用 LLM（Kimi K2.5）对平行句对进行命名实体识别，同时提取原文实体和译文实体
3. 对提取结果进行去括号、去重、清洗等后处理

## 许可说明

本数据集中的NER翻译对是从官方翻译文本中自动提取的实体名称映射，仅包含人名、地名、组织名、术语等短语级别的翻译对照信息，不包含任何原文的句子或段落内容。本数据集仅供学术研究使用。
