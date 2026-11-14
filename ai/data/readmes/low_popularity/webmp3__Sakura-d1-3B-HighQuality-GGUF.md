---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/d1-3B
base_model_relation: quantized
library_name: gguf
pipeline_tag: image-text-to-text
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
tags:
- gguf
- llama.cpp
- liquid
- lfm2.5
- decision
- classification
- system-one
- imatrix
- mixed-precision
- quantized
---

# Sakura d1-3B HighQuality GGUF

> **Modified files.** These GGUF files are quantized, modified versions of [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B) (revision `da1fe36`, the weights Liquid published on 7 October 2026). The weights were converted and compressed; nothing was retrained. Community build, not from or endorsed by Liquid AI. Used under the LFM Open License v1.0, a copy is in `LICENSE`.

Four GGUF files of Liquid AI's decision model d1-3B from 1.56 to 2.35 GB. Each tensor group gets its own precision, chosen from a measurement of how much each group costs in decision quality. The importance matrix comes from decision prompts in 30 languages and code.

![Distance to BF16 against file size](assets/d1_size_vs_drift.png)

![Indexed to AtomicChat's file of the same class](assets/d1_indexed_bars.png)

## Pick a file

Measured on 1,285 decisions (yes/no, choice and score questions over held-out texts in 30 languages and code) against the BF16 model of the same revision, run through llama.cpp (upstream commit `9c2e0e4`, Vulkan). `changed answers` counts decisions where the top option differs from BF16. `option drift` is the mean total variation distance between the option probabilities (0 means identical); `KLD` is the mean KL divergence of the option distributions.

| File | Size | changed answers | same answer | option drift | KLD |
|---|---:|---:|---:|---:|---:|
| `d1-3B-Sakura-HQ-S.gguf` | 1,556 MB | 30 | 97.7% | 0.0143 | 0.00135 |
| `d1-3B-Sakura-HQ-Q4.gguf` | 1,650 MB | 23 | 98.2% | 0.0123 | 0.00102 |
| `d1-3B-Sakura-HQ-Q5.gguf` | 1,949 MB | 22 | 98.3% | 0.0068 | 0.00030 |
| `d1-3B-Sakura-HQ-Q6.gguf` | 2,348 MB | 11 | 99.1% | 0.0045 | 0.00015 |

Image decisions need a projector: `mmproj-d1-3B-Q8_0.gguf` (583 MB) or `mmproj-d1-3B-BF16.gguf` (856 MB). We did not measure image decisions; we only checked that an image question returns a sensible answer.

## Compared with the other published builds

AtomicChat published 1,285-decision numbers for their files in [`AtomicChat/d1-3B-GGUF`](https://huggingface.co/AtomicChat/d1-3B-GGUF). We measured our files with the same decision set and the same protocol (their evaluation scripts from [`AtomicChat/d1-3B-GGUF-metrics`](https://huggingface.co/datasets/AtomicChat/d1-3B-GGUF-metrics)); their numbers below are as they published them and were not re-measured by us. Their run used a CUDA GPU and their own BF16 conversion, ours a Vulkan GPU and a BF16 file converted with the d1 pull request of llama.cpp, so small differences are within what two setups can disagree on.

| Class | Ours | AtomicChat (as published) | Reading |
|---|---|---|---|
| ~1.56 GB | HQ-S: 1,556 MB, 30 changed, drift 0.0143 | AD-IQ4_XS: 1,570 MB, 57 changed, drift 0.0203 | 47% fewer changed answers, 30% lower drift, 1% smaller |
| ~1.65 GB | HQ-Q4: 1,650 MB, 23 changed, drift 0.0123 | AD-Q4_K_M: 1,658 MB, 37 changed, drift 0.0178 | 38% fewer changed answers, 31% lower drift, 0.5% smaller |
| ~1.95 GB | HQ-Q5: 1,949 MB, 22 changed, drift 0.0068 | AD-Q5_K_M: 1,953 MB, 25 changed, drift 0.0112 | 3 fewer changed answers, 39% lower drift |
| ~2.35 GB | HQ-Q6: 2,348 MB, 11 changed, drift 0.0045 | AD-Q6_K: 2,348 MB, 11 changed, drift 0.0053 | same changed answers, 15% lower drift |

Counts of changed answers move by a few between two runs of the same file, so read them together with the drift column. At Q6 the starting layout follows the per-tensor rules AtomicChat published in their metrics repository; at the other three classes the layouts are our own. All four files then go through the error-feedback step described below, which is where most of the gain over the earlier version of this repository comes from.

## How to run

The files carry the decision type `lfm2-d1`. Support was merged into llama.cpp on 7 October 2026 ([ggml-org/llama.cpp#30110](https://github.com/ggml-org/llama.cpp/pull/30110), first release tag `b11483`), so any current llama.cpp build runs them (checked with upstream commit `9c2e0e4`, Vulkan). Builds older than `b11483` do not know the type and refuse to load the files.

```bash
llama-server -m d1-3B-Sakura-HQ-Q5.gguf --mmproj mmproj-d1-3B-Q8_0.gguf -ngl 99 -c 8192
```

Then ask typed questions about a state:

```bash
curl http://127.0.0.1:8080/v1/systemone -H "Content-Type: application/json" -d '{
  "state": "I was charged twice this month, please refund one of them.",
  "questions": {
    "refund":  {"type": "noul", "instructions": "Is the customer asking for a refund?"},
    "team":    {"type": "choice", "instructions": "Which team should handle this?",
                "criteria": {"billing": "Charges, refunds, invoices", "technical": "App or site faults", "fraud": "Suspected unauthorised use"}},
    "urgency": {"type": "score", "instructions": "How urgent is this?", "criteria": ["Can wait", "Today", "Blocking the customer now"]}
  }
}'
```

For the original model with Transformers (`trust_remote_code=True`, `model.system_one(...)`), see the [Liquid model card](https://huggingface.co/LiquidAI/d1-3B).

## How these files were made

1. **BF16 base:** converted from LiquidAI/d1-3B revision `da1fe36` with llama.cpp's converter from the d1-3B pull request (#30110, now merged), and the projector with `--mmproj`. Liquid's earlier GGUFs were built from the previous weights and are not comparable.
2. **Importance matrix:** `llama-imatrix` on the BF16 file over 256 chunks of 2,048 tokens: decision prompts rendered with the model's own prompt code, built from public texts (Wikipedia in 30 languages, source code files, English and German question/answer data). It is included as `imatrix-sakura-d1-multilingual.gguf` and contains statistics only, no text.
3. **Measuring where bits matter:** with everything at Q8_0 we moved one tensor group at a time to Q4_K and measured the change on 400 decisions. Per megabyte saved, attention q/k/v is the most expensive group, then attention output, the token table and the conv projections; the FFN gate/up and down matrices are the cheapest, and the later blocks (18 to 29) cost far less than the early ones (0 to 9).
4. **Allocation:** bits were handed out greedily by that cost per saved megabyte (attention q/k/v at Q8_0, attention output at least Q6_K, token table at least Q6_K), then the plans were built with `llama-quantize --imatrix --tensor-type` and measured in full. HQ-S, HQ-Q4 and HQ-Q5 are the plans for 1.56, 1.65 and 1.95 GB.
5. **Error feedback:** the tensors are then re-quantized block by block (256 input columns, the unit of the K and IQ formats) with llama.cpp's own encoder, but after each block its rounding error is pushed onto the columns still to come, using second-order statistics (the Hessian of the layer inputs) from 160 real decision prompts. The result is an ordinary GGUF with the same tensor types and the same size; only the stored values differ. Under identical conditions (same decision set, same BF16 reference, same llama.cpp build) this changed the files as follows:

| Class | before: changed / drift / KLD | after (this repo): changed / drift / KLD |
|---|---|---|
| HQ-S | 34 / 0.0195 / 0.00240 | 30 / 0.0143 / 0.00135 |
| HQ-Q4 | 31 / 0.0151 / 0.00149 | 23 / 0.0123 / 0.00102 |
| HQ-Q5 | 21 / 0.0093 / 0.00057 | 22 / 0.0068 / 0.00030 |
| HQ-Q6 | 11 / 0.0052 / 0.00019 | 11 / 0.0045 / 0.00015 |

   One tensor of HQ-Q4 could not be handled (its inverse Hessian was numerically not positive definite) and keeps its plain quantization; every other tensor in the four files went through the step.
6. **Checks:** every file was measured on all 1,285 decisions and queried through `/v1/systemone` in llama.cpp (text); one image question with the projector was run on `HQ-Q5` (a bar-chart image: P("is a bar chart") = 0.92, picks "chart" with 0.96). Image decisions were not measured further.

## Overfitting checks

The error-feedback step fits the files to calibration prompts, so we checked that the gain is not an artifact:

- **Text overlap.** 13 of the 1,285 evaluation decisions share an 80-character span with the calibration texts (same Wikipedia articles). Leaving them out changes the results by at most one changed answer and 0.0001 of drift (for example HQ-Q4: 22 changed answers, drift 0.0122, instead of 23 and 0.0123).
- **Question templates.** Calibration and the main evaluation use the same 14 question templates. We built a second evaluation of 450 decisions over the same evaluation texts with nine templates that appear in neither (different wording, option counts 2 to 6), and measured the files before and after the error-feedback step on it:

| Class | before: changed / drift / KLD | after (this repo): changed / drift / KLD |
|---|---|---|
| HQ-S | 16 / 0.0248 / 0.00313 | 13 / 0.0216 / 0.00222 |
| HQ-Q4 | 14 / 0.0211 / 0.00215 | 11 / 0.0178 / 0.00154 |
| HQ-Q5 | 7 / 0.0123 / 0.00071 | 5 / 0.0084 / 0.00038 |
| HQ-Q6 | 6 / 0.0063 / 0.00021 | 3 / 0.0060 / 0.00018 |

The step improves all four classes on templates it never saw, with a smaller gain at Q6.

## Files

`SHA256SUMS` lists every file. Only the `general.*` name strings were set after quantization; tensor data was verified identical.

## License and credits

Base model: [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B) by Liquid AI, released under the LFM Open License v1.0 (`LICENSE`, included as required). The license limits commercial use by organizations above its revenue threshold; read it before using these files commercially. The files are modified from the original (quantized), as the license requires us to say. llama.cpp support for d1 is by Liquid AI and the llama.cpp contributors (pull request #30110). The evaluation protocol and decision set are by AtomicChat. Quantization, importance matrix, allocation and measurements by webmp3. Not endorsed by Liquid AI or AtomicChat.

---

<details><summary>中文说明 · 樱花 (Simplified Chinese)</summary>

> English above. 本节为上文的中文翻译(Sakura = 樱花 yīnghuā);完整的独立中文版见 [README_zh.md](README_zh.md)。

# Sakura d1-3B HighQuality GGUF

> **已修改的文件。** 这些 GGUF 文件是 [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B)(修订版本 `da1fe36`,即 Liquid 于 2026 年 10 月 7 日发布的权重)经过量化的修改版本。权重经过转换和压缩,没有进行任何再训练。这是社区构建版本,并非来自 Liquid AI,也未获得其认可。依据 LFM Open License v1.0 使用,许可证副本见 `LICENSE`。

Liquid AI 决策模型 d1-3B 的四个 GGUF 文件,大小从 1.56 到 2.35 GB。每个张量组使用各自的精度,该精度根据一项测量来选择:测量每个张量组对决策质量造成的损失。重要性矩阵来自 30 种语言和代码的决策提示。

![Distance to BF16 against file size](assets/d1_size_vs_drift.png)

![Indexed to AtomicChat's file of the same class](assets/d1_indexed_bars.png)

## 如何选择文件

在 1,285 个决策上测量(针对 30 种语言和代码的留出文本的是非题、选择题和打分题),以相同修订版本的 BF16 模型为参照,通过 llama.cpp(上游提交 `9c2e0e4`,Vulkan)运行。`changed answers` 统计首选选项与 BF16 不同的决策数。`option drift` 是各选项概率之间的平均总变差距离(0 表示完全相同);`KLD` 是选项分布的平均 KL 散度。

| 文件 | 大小 | changed answers | same answer | option drift | KLD |
|---|---:|---:|---:|---:|---:|
| `d1-3B-Sakura-HQ-S.gguf` | 1,556 MB | 30 | 97.7% | 0.0143 | 0.00135 |
| `d1-3B-Sakura-HQ-Q4.gguf` | 1,650 MB | 23 | 98.2% | 0.0123 | 0.00102 |
| `d1-3B-Sakura-HQ-Q5.gguf` | 1,949 MB | 22 | 98.3% | 0.0068 | 0.00030 |
| `d1-3B-Sakura-HQ-Q6.gguf` | 2,348 MB | 11 | 99.1% | 0.0045 | 0.00015 |

图像决策需要投影器(projector):`mmproj-d1-3B-Q8_0.gguf`(583 MB)或 `mmproj-d1-3B-BF16.gguf`(856 MB)。我们没有测量图像决策;只检查了针对图像的提问能返回合理的回答。

## 与其他已发布构建版本的比较

AtomicChat 在 [`AtomicChat/d1-3B-GGUF`](https://huggingface.co/AtomicChat/d1-3B-GGUF) 中发布了其文件在 1,285 个决策上的数据。我们使用相同的决策集和相同的协议(来自 [`AtomicChat/d1-3B-GGUF-metrics`](https://huggingface.co/datasets/AtomicChat/d1-3B-GGUF-metrics) 的评测脚本)测量了我们的文件;下表中他们的数据是其发布时的原样,我们没有重新测量。他们的运行使用 CUDA GPU 和他们自己的 BF16 转换,我们使用 Vulkan GPU 和用 llama.cpp 的 d1 拉取请求转换的 BF16 文件,因此两套环境之间的小幅差异属于正常范围。

| 级别 | 我们的文件 | AtomicChat(按其发布数据) | 解读 |
|---|---|---|---|
| ~1.56 GB | HQ-S: 1,556 MB, 30 changed, drift 0.0143 | AD-IQ4_XS: 1,570 MB, 57 changed, drift 0.0203 | changed answers 少 47%,drift 低 30%,文件小 1% |
| ~1.65 GB | HQ-Q4: 1,650 MB, 23 changed, drift 0.0123 | AD-Q4_K_M: 1,658 MB, 37 changed, drift 0.0178 | changed answers 少 38%,drift 低 31%,文件小 0.5% |
| ~1.95 GB | HQ-Q5: 1,949 MB, 22 changed, drift 0.0068 | AD-Q5_K_M: 1,953 MB, 25 changed, drift 0.0112 | changed answers 少 3 个,drift 低 39% |
| ~2.35 GB | HQ-Q6: 2,348 MB, 11 changed, drift 0.0045 | AD-Q6_K: 2,348 MB, 11 changed, drift 0.0053 | changed answers 相同,drift 低 15% |

同一个文件在两次运行之间,changed answers 的计数会有几个的波动,因此请结合 drift 一列来看。在 Q6 级别,起始布局遵循 AtomicChat 在其 metrics 仓库中发布的逐张量规则;其余三个级别的布局是我们自己的。随后,这四个文件都经过下文所述的误差反馈步骤,相对于本仓库早期版本的大部分提升来自这一步。

## 如何运行

这些文件带有决策类型 `lfm2-d1`。支持已于 2026 年 10 月 7 日合并进 llama.cpp([ggml-org/llama.cpp#30110](https://github.com/ggml-org/llama.cpp/pull/30110),首个发布标签为 `b11483`),因此任何较新的 llama.cpp 构建都可以运行它们(已用上游提交 `9c2e0e4`、Vulkan 检查)。早于 `b11483` 的构建不认识该类型,会拒绝加载这些文件。

```bash
llama-server -m d1-3B-Sakura-HQ-Q5.gguf --mmproj mmproj-d1-3B-Q8_0.gguf -ngl 99 -c 8192
```

然后针对某个状态提出带类型的问题:

```bash
curl http://127.0.0.1:8080/v1/systemone -H "Content-Type: application/json" -d '{
  "state": "I was charged twice this month, please refund one of them.",
  "questions": {
    "refund":  {"type": "noul", "instructions": "Is the customer asking for a refund?"},
    "team":    {"type": "choice", "instructions": "Which team should handle this?",
                "criteria": {"billing": "Charges, refunds, invoices", "technical": "App or site faults", "fraud": "Suspected unauthorised use"}},
    "urgency": {"type": "score", "instructions": "How urgent is this?", "criteria": ["Can wait", "Today", "Blocking the customer now"]}
  }
}'
```

若要用 Transformers 运行原始模型(`trust_remote_code=True`、`model.system_one(...)`),请参阅 [Liquid 模型卡](https://huggingface.co/LiquidAI/d1-3B)。

## 这些文件是如何制作的

1. **BF16 基础文件:** 使用 d1-3B 拉取请求(#30110,现已合并)中的 llama.cpp 转换器,从 LiquidAI/d1-3B 修订版本 `da1fe36` 转换而来;投影器通过 `--mmproj` 转换。Liquid 早先的 GGUF 是用之前的权重构建的,与本仓库不可比。
2. **重要性矩阵:** 在 BF16 文件上运行 `llama-imatrix`,共 256 个块,每块 2,048 个 token:决策提示由模型自带的提示代码渲染,取材于公开文本(30 种语言的维基百科、源代码文件、英文和德文问答数据)。矩阵以 `imatrix-sakura-d1-multilingual.gguf` 提供,只包含统计信息,不含任何文本。
3. **测量哪里的比特最重要:** 先将所有张量设为 Q8_0,再每次将一个张量组改为 Q4_K,并在 400 个决策上测量变化。按每节省一兆字节计算,注意力 q/k/v 是代价最高的组,其次是注意力输出、token 表和卷积投影;FFN 的 gate/up 和 down 矩阵代价最低,而靠后的块(18 至 29)的代价远低于靠前的块(0 至 9)。
4. **分配:** 按每节省一兆字节的代价,以贪心方式分配比特(注意力 q/k/v 使用 Q8_0,注意力输出至少 Q6_K,token 表至少 Q6_K),随后用 `llama-quantize --imatrix --tensor-type` 构建各方案,并完整测量。HQ-S、HQ-Q4 和 HQ-Q5 分别对应 1.56、1.65 和 1.95 GB 的方案。
5. **误差反馈:** 随后张量被逐块重新量化(每块 256 个输入列,即 K 和 IQ 格式的单位),使用 llama.cpp 自己的编码器,但每处理完一块后,会把它的舍入误差推给尚未处理的列,所用的二阶统计信息(各层输入的 Hessian)来自 160 个真实的决策提示。结果仍是普通的 GGUF,张量类型和大小都不变;只有存储的数值不同。在相同条件下(相同的决策集、相同的 BF16 参考、相同的 llama.cpp 构建),这一步使文件发生如下变化:

| 级别 | 之前:changed / drift / KLD | 之后(本仓库):changed / drift / KLD |
|---|---|---|
| HQ-S | 34 / 0.0195 / 0.00240 | 30 / 0.0143 / 0.00135 |
| HQ-Q4 | 31 / 0.0151 / 0.00149 | 23 / 0.0123 / 0.00102 |
| HQ-Q5 | 21 / 0.0093 / 0.00057 | 22 / 0.0068 / 0.00030 |
| HQ-Q6 | 11 / 0.0052 / 0.00019 | 11 / 0.0045 / 0.00015 |

   HQ-Q4 中有一个张量无法处理(其逆 Hessian 在数值上不是正定的),因此保持普通量化;这四个文件中的其他所有张量都经过了这一步。
6. **检查:** 每个文件都在全部 1,285 个决策上测量,并通过 llama.cpp 中的 `/v1/systemone` 进行了查询(文本);另在 `HQ-Q5` 上用投影器运行了一个图像问题(一张柱状图:P("is a bar chart") = 0.92,以 0.96 选择 "chart")。图像决策没有进一步测量。

## 过拟合检查

误差反馈步骤会让文件适配校准提示,因此我们检查了这一提升不是假象:

- **文本重叠。** 1,285 个评测决策中有 13 个与校准文本有 80 字符的重叠片段(相同的维基百科文章)。排除它们后,结果最多变化一个 changed answer 和 0.0001 的 drift(例如 HQ-Q4:22 个 changed answers、drift 0.0122,而不是 23 和 0.0123)。
- **问题模板。** 校准和主评测使用相同的 14 个问题模板。我们在相同的评测文本上,用两者都未出现过的九个模板(措辞不同,选项数 2 至 6)构建了第二套 450 个决策的评测,并在其上测量了误差反馈步骤前后的文件:

| 级别 | 之前:changed / drift / KLD | 之后(本仓库):changed / drift / KLD |
|---|---|---|
| HQ-S | 16 / 0.0248 / 0.00313 | 13 / 0.0216 / 0.00222 |
| HQ-Q4 | 14 / 0.0211 / 0.00215 | 11 / 0.0178 / 0.00154 |
| HQ-Q5 | 7 / 0.0123 / 0.00071 | 5 / 0.0084 / 0.00038 |
| HQ-Q6 | 6 / 0.0063 / 0.00021 | 3 / 0.0060 / 0.00018 |

该步骤在它从未见过的模板上改善了全部四个级别,其中 Q6 的提升较小。

## 文件

`SHA256SUMS` 列出了每个文件。量化之后只设置了 `general.*` 名称字符串;已核实张量数据一致。

## 许可证与致谢

基础模型:Liquid AI 的 [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B),以 LFM Open License v1.0 发布(`LICENSE`,按要求随附)。该许可证限制超过其营收门槛的组织的商业使用;商业使用这些文件之前请先阅读。这些文件相对于原始模型已被修改(量化),这是许可证要求我们说明的。llama.cpp 对 d1 的支持由 Liquid AI 和 llama.cpp 贡献者完成(拉取请求 #30110)。评测协议和决策集来自 AtomicChat。量化、重要性矩阵、分配和测量由 webmp3 完成。未获得 Liquid AI 或 AtomicChat 的认可。

</details>
