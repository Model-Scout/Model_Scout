---
language:
  - ja
  - en
  - ko
  - zh
license: cc-by-nc-4.0
library_name: ctranslate2
tags:
  - translation
  - nllb
  - ctranslate2
  - japanese
  - korean
  - english
  - chinese
  - finance
  - oral
  - short-video
  - koubox
base_model: facebook/nllb-200-distilled-600M
pipeline_tag: translation
---

# Koubox NLLB-600M Multilang Oral Finance (CTranslate2 float16)

面向 **口播匣（Koubox）** 的本地翻译模型：在 `facebook/nllb-200-distilled-600M` 上做 **日语 / 英语 / 韩语 → 简体中文** 领域微调，并导出为 **CTranslate2 float16**，适合桌面端低显存、低延迟推理。

| 项目 | 内容 |
|------|------|
| 基座 | [`facebook/nllb-200-distilled-600M`](https://huggingface.co/facebook/nllb-200-distilled-600M) |
| 方向 | `jpn_Jpan` / `eng_Latn` / `kor_Hang` → `zho_Hans` |
| 领域 | 财经 / 科技供应链口播短视频字幕 |
| 格式 | CTranslate2 **float16**（约 1.2GB `model.bin`） |
| 显存 | 推理约 **1GB 量级**（随 batch/长度变化） |
| 评测 | Document-level holdout（禁止训测同源） |

---

## 亮点

1. **三语进、中文出口播**  
   同一套权重覆盖日/英/韩→简中，风格统一为财经博主口播：短、冲、术语稳。

2. **硬术语修好**  
   - `利益率` → **利润率**（不再误成「利率」；NLLB 词表无简体「润」，训练目标用词表内「利潤率」，解码再规范为「润」）  
   - `歩留まり` / yield → **良率**（避免「收益率」串扰）  
   - `精密ステージ` → **精密平台**；`テストソケット` → **测试插座**；`通信モジュール` → **通信模块**  
   - `1次資料` / primary sources → **一手资料**  
   - `PoC → 量産` → **PoC 转向量产**

3. **口播修辞与互动**  
   「不是单纯喊『支持AI』的口号」「给留言『779』的人」「就算…」「不只是市场的热度」等否定/互动句式明显好于基线。

4. **泛化评测纪律**  
   留出整篇文档 `文案_09` / `文案_10` 作 holdout，训练侧排除同原文，避免「同句刷分」。

5. **可上桌面**  
   CT2 float16 + 小显存，适合口播工作台本地跑，不依赖云端大模型在线翻译。

---

## 文件说明

```text
config.json                 # CTranslate2 配置
model.bin                   # CT2 float16 权重（主文件）
shared_vocabulary.json      # CT2 词表
tokenizer.json              # Hugging Face / SentencePiece 分词器
tokenizer_config.json
```

本仓库是 **CT2 推理包**，不是完整 Transformers `pytorch_model.bin`。请用 **CTranslate2** 加载。

---

## 快速使用（CTranslate2）

```python
import ctranslate2
from transformers import AutoTokenizer

repo = "xxliam/koubox-nllb-600m-ja-en-ko-zh-oral-ct2"
tokenizer = AutoTokenizer.from_pretrained(repo, src_lang="jpn_Jpan")
translator = ctranslate2.Translator(repo, device="cuda", compute_type="float16")

def translate(text: str, src_lang: str = "jpn_Jpan") -> str:
    tokenizer.src_lang = src_lang
    toks = tokenizer.convert_ids_to_tokens(tokenizer.encode(text, add_special_tokens=True))
    hyp = translator.translate_batch(
        [toks],
        target_prefix=[["zho_Hans"]],
        beam_size=4,
        max_decoding_length=128,
        repetition_penalty=1.2,
    )[0].hypotheses[0]
    body = hyp[1:] if hyp and hyp[0] == "zho_Hans" else hyp
    text_out = tokenizer.decode(tokenizer.convert_tokens_to_ids(body), skip_special_tokens=True).strip()
    # NLLB 词表无简体「润」：训练用「利潤」，展示时规范为简体
    return text_out.replace("潤", "润")

print(translate("製造ラインの稼働率と利益率に直結します。", "jpn_Jpan"))
# → 直接关系到产线的稼动率和利润率。
```

源语言代码：

| 源语言 | `src_lang` |
|--------|------------|
| 日语 | `jpn_Jpan` |
| 英语 | `eng_Latn` |
| 韩语 | `kor_Hang` |
| 目标简中 | `zho_Hans`（target_prefix） |

---

## 微调流程（完整）

### 1. 基座与目标

- Base: NLLB-200 Distilled **600M**
- PEFT LoRA（典型：`r=32`, `alpha=64`，目标模块 `q/k/v/out_proj/fc1/fc2`）
- 手写训练循环（预分词 + DataLoader），Windows 上 `num_workers=0`，bf16，甜点 batch≈16
- 多阶段续训后 **merge LoRA → Transformers**，再 `ct2-transformers-converter --quantization float16`

### 2. 教师数据（Teacher）

用 **SiliconFlow** 上的 DeepSeek 类聊天模型，对口播日语文案生成：

- SFT 平行句：`source` / `target`（日→中，后扩英/韩）
- DPO：`chosen`（教师佳译）vs `rejected`（基线或弱译）

环境变量示例（**勿把真实 Key 写进公开仓库**）：

```bash
SILICONFLOW_API=...
SILICONFLOW_MODEL=deepseek-ai/DeepSeek-V4-Flash
SILICONFLOW_BASEURL=https://api.siliconflow.cn/v1/chat/completions
```

### 3. 语种扩展

- 日语口播句 → 教师中文  
- 再生成 **英语 / 韩语** 平行句，组成 `sft_train_multilang` / `sft_holdout_multilang`  
- 训练三语均衡，避免「只会日→中」

### 4. 公开语料打底（HF Mix）

财经关键词召回的公开平行语料混合（约 **16 万** 量级，过滤英文照抄与脏 margin 句）：

| 来源 | 语向 | 用途 |
|------|------|------|
| WikiMatrix / CCMatrix | ja–zh | 日中财经/百科向打底 |
| OPUS-100 | en–zh | 英中打底 |
| AIHub 等 | ko–zh | 韩中打底 |

**刻意避免**：轻小说域合成数据（如 sakura 类），防止语域跑偏。

后期深度阶段会再抽数千～两万条 HF 做 **广度正则**，防止口播过拟合。

### 5. Document-level Holdout（硬规则）

| 集合 | 内容 |
|------|------|
| Holdout 文案 | `文案_09_半導体検査.txt`、`文案_10_低消費電力エッジAI.txt` |
| 训练 | 仅 01–08 等非留出文案 + 扩写 + HF |
| 评测 | 仅 holdout 多语抽样（约 36 句展示表） |

同原文不得进入训练集；评测禁止「训练集同句刷分」。

### 6. 阶段演进（摘要）

| 阶段 | 目的 |
|------|------|
| HF + 口播多语 + preference | 打底与偏好对齐 |
| 短句/术语加重 | 精密平台、良率等 |
| 防英文照抄 + HF 正则 | 抑制源语泄漏 |
| 术语回收 | 利润率/良率等 |
| 全弱点定向 | 修辞、779、信息完整 |
| 词表策略 | 简体「润」为 unk → 用「利潤率」+ 解码规范 |
| 超教师口播金标 | 比教师更冲的口播改写 |
| 深度持久（广度 1.5ep + 深度 2.5ep） | HF 正则 + 金标钉死 |
| 残差抛光 | 留言 779 等 |

最终导出为本仓库 CT2 float16。

### 7. 训练超参（典型）

- Optimizer: AdamW（fused）  
- LR: 早期偏高（~1e-4 量级打底），后期残差 **5e-6～1.5e-5**  
- Batch: 16；Max length: 96  
- Precision: bf16 训练 / float16 CT2 推理  
- Clip grad: 1.0  

---

## 数据清单（训练用过的完整类型）

> 下列为流水线中实际使用过的数据类型与规模量级；部分中间 jsonl 已在本地清理，公开侧以方法与规模说明为准。

### A. 自建口播平行

| 文件类型 | 规模量级 | 说明 |
|----------|----------|------|
| `sft.jsonl` / `sft_train.jsonl` | 数百句 | 日→中教师 SFT |
| `dpo.jsonl` / `dpo_train.jsonl` | 数百对 | chosen/rejected |
| `sft_train_multilang.jsonl` | ~900 | 日/英/韩→中训练（去 holdout） |
| `sft_holdout_multilang.jsonl` | ~200 | 仅评测 |
| `dpo_train_multilang.jsonl` | ~800+ | 多语 preference |
| `teacher_report.jsonl` | 教师生成日志 | 质检用 |

### B. Holdout 划分

| 文件 | 说明 |
|------|------|
| `SPLIT.json` | 记录 holdout 文案文件名 |
| holdout 源 | `文案_09_半導体検査`、`文案_10_低消費電力エッジAI` |

### C. 公开 HF 混集

| 文件 | 规模 | 说明 |
|------|------|------|
| `sft_hf_finance_mix.jsonl` | ~16.3 万 | ja/en/ko–zh 财经关键词召回；训练打底与深度广度阶段抽样 |

过滤要点：

- 去掉目标侧大量拉丁字母、几乎无汉字的「伪中文」  
- 跳过可能污染「利益率/利率」区分的脏句  
- 不做 holdout 原文泄漏  

### D. 定向强化（阶段构造，后已本地清理）

术语对比、口播修辞、779 互动、信息完整句、防过压缩、超教师 oralize 规则（`就算`/`不只是`/`一手资料`/`喊「支持AI」` 等）与 DPO chosen 加重。

---

## 评测结果（Holdout 粗判）

在 document-level holdout 多语抽样上（相对教师参考的启发式：术语 + 口播标记）：

- **胜 / 平 / 负 ≈ 11 / 25 / 0**（非人工终评）  
- 基线 NLLB 常见问题（速报→骗局、精密平台→精密阶段、利益率→利率、韩语乱译）在微调后明显改善  
- 部分句式可 **优于教师**（例如现场处理信息更完整、口播「光靠巨型数据中心，可能搞不定」等）

---

## 限制与注意

1. **词表**：简体「润」在原 NLLB SentencePiece 中为 `<unk>`；本模型用「利潤」训练，**推理后请 `replace("潤","润")`**。  
2. **语域**：针对财经/科技口播；文学、闲聊、法律长文未经专项优化。  
3. **长度**：训练 max length 96，超长请切句。  
4. **许可**：基座遵循 Meta NLLB / CC 相关条款；本微调权重建议 **非商业研究与个人桌面工具**（`cc-by-nc-4.0`）。若商用请自行评估基座与数据合规。  
5. **非投资建议**：口播财经文案翻译不构成荐股。

---

## 推荐环境

- GPU：NVIDIA，CUDA（CTranslate2 GPU 构建）  
- Python：`ctranslate2`、`transformers`、`sentencepiece`  
- 与 Koubox 桌面端搭配时，模型目录名可对应：  
  `nllb-200-distilled-600M-multilang-ft-ct2`

---

## 引用

```bibtex
@misc{koubox-nllb-oral-2026,
  title        = {Koubox NLLB-600M Multilang Oral Finance CT2},
  author       = {xxliam},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/xxliam/koubox-nllb-600m-ja-en-ko-zh-oral-ct2}},
  note         = {Fine-tuned from facebook/nllb-200-distilled-600M for JA/EN/KO to ZH oral finance subtitles}
}
```

基座：

```bibtex
@article{nllb2022,
  title  = {No Language Left Behind: Scaling Human-Centered Machine Translation},
  author = {NLLB Team},
  year   = {2022}
}
```

---

## 致谢

- Meta NLLB  
- CTranslate2  
- 公开平行语料：WikiMatrix / CCMatrix / OPUS / AIHub 等  
- 教师模型 API：SiliconFlow（DeepSeek 系列）  
- 产品：口播匣 Koubox
