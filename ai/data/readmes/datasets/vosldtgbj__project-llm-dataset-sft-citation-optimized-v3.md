---
pretty_name: SF-SFT-v3：引用净化后的正式 90/10 SFT
license: other
language: [ja, en, zh, ko, hi, pt, es, fr, de, ar, vi, sw, bn]
task_categories:
  - text-generation
  - question-answering
tags:
  - continued-pretraining
  - supervised-fine-tuning
  - reinforcement-learning
  - rlvr
  - japanese
  - searchforge
configs:
  - config_name: canonical_full_pool
    data_files:
      - split: train
        path: data/canonical_full_pool/*/train/accepted.jsonl
      - split: eval
        path: data/canonical_full_pool/*/eval/accepted.jsonl
  - config_name: official_90_10
    data_files:
      - split: train
        path:
          - data/canonical_full_pool/single_document_qa/train/accepted.jsonl
          - data/canonical_full_pool/cross_document_reasoning/train/accepted.jsonl
          - data/canonical_full_pool/temporal_conflict/train/accepted.jsonl
          - data/canonical_full_pool/normal_tool_trajectory/train/accepted.jsonl
          - data/canonical_full_pool/tool_failure_recovery/train/accepted.jsonl
          - data/canonical_full_pool/clarification_abstention_stop/train/accepted.jsonl
          - data/canonical_full_pool/structured_output/train/accepted.jsonl
          - data/canonical_full_pool/injection_permission/train/accepted.jsonl
          - data/official_90_10/train_view/general_diverse/train/accepted.jsonl
      - split: eval
        path:
          - data/canonical_full_pool/single_document_qa/eval/accepted.jsonl
          - data/canonical_full_pool/cross_document_reasoning/eval/accepted.jsonl
          - data/canonical_full_pool/temporal_conflict/eval/accepted.jsonl
          - data/canonical_full_pool/normal_tool_trajectory/eval/accepted.jsonl
          - data/canonical_full_pool/tool_failure_recovery/eval/accepted.jsonl
          - data/canonical_full_pool/clarification_abstention_stop/eval/accepted.jsonl
          - data/canonical_full_pool/structured_output/eval/accepted.jsonl
          - data/canonical_full_pool/injection_permission/eval/accepted.jsonl
          - data/official_90_10/eval_view/general_diverse/eval/accepted.jsonl
---


# SF-SFT-v3：引用净化后的正式 90/10 SFT

## 首先选择正确 config

| 目标 | 应使用的 config | 原因 |
|---|---|---|
| 复现九个正式 SFT v3 run | **`official_90_10`** | 真正按监督 token 冻结为约 90% 项目域 + 10% 通用 |
| 分析所有合格通用候选、重新设计配比 | `canonical_full_pool` | 保留完整 `general_diverse` 池 |
| 比较 v2/v3 引用净化 | `canonical_full_pool` + SF-SFT-v2 | 记录身份对应最完整 |

不要因为名字里有 canonical 就直接用 `canonical_full_pool` 复现正式训练。引用净化缩短了项目域回答，而通用池未变短，使 full pool 的通用监督 token 比例升至 train 16.0396%、eval 16.0663%。`official_90_10` 才是最终训练视图。

## 两个 config、两个 split 的精确规模

| config | split | 项目域 条/监督 token | 通用 条/监督 token | 合计 条/监督 token | 通用比例 |
|---|---|---:|---:|---:|---:|
| `canonical_full_pool` | train | 64,263 / 3,674,850 | 5,385 / 702,034 | 69,648 / 4,376,884 | 16.039584% |
| `canonical_full_pool` | eval | 16,083 / 917,764 | 1,483 / 175,675 | 17,566 / 1,093,439 | 16.066283% |
| `official_90_10` | train | 64,263 / 3,674,850 | 2,932 / 408,317 | 67,195 / 4,083,167 | 10.000007% |
| `official_90_10` | eval | 16,083 / 917,764 | 889 / 101,973 | 16,972 / 1,019,737 | 9.999931% |

`official_90_10` 并未复制八个项目域文件：它在 Dataset Card 中显式引用 `canonical_full_pool` 的八个项目域路径，只在 `data/official_90_10/{train,eval}_view` 保存确定性截取的通用记录。加载 config 时 Hugging Face 将九组文件组合为一个 split。直接浏览 `official_90_10` 目录并只看到通用数据，不表示正式视图只有通用数据。

## canonical full pool 的分 family 规模

| family（目录名） | train 行 | eval 行 | train 监督 token | eval 监督 token | 训练意图 |
|---|---:|---:|---:|---:|---|
| `clarification_abstention_stop` | 20,188 | 5,114 | 529,107 | 132,016 | 缺信息时澄清、不可回答、合理拒答与停止 |
| `cross_document_reasoning` | 5,430 | 1,312 | 374,030 | 96,375 | 跨文档比较、汇总、计算与多跳归纳 |
| `general_diverse` | 5,385 | 1,483 | 702,034 | 175,675 | 多语言、多能力通用 SFT 锚点 |
| `injection_permission` | 1,752 | 439 | 208,649 | 52,065 | 间接提示注入、只读权限和操作边界 |
| `normal_tool_trajectory` | 6,881 | 1,725 | 951,989 | 236,203 | 正常搜索、打开证据、工具调用与停止 |
| `single_document_qa` | 17,950 | 4,511 | 553,591 | 136,087 | 单文档事实提取、单位和有依据回答 |
| `structured_output` | 3,629 | 902 | 178,692 | 44,704 | JSON/schema/字段约束和可解析输出 |
| `temporal_conflict` | 3,865 | 937 | 357,811 | 90,173 | 版本、时间状态、来源冲突与新旧口径 |
| `tool_failure_recovery` | 4,568 | 1,143 | 520,981 | 130,141 | 空结果、错误查询、工具失败后的改写与恢复 |

## 正式通用 10% 的分层覆盖

`official_90_10` 使用 seed `20261006` 与 selected-ID SHA-256 冻结。按行的语言覆盖如下；实际配额仍按监督 token：

| split | de | en | es | fr | hi | ja | ko | pt-BR | zh | ar+bn+sw+vi | 合计 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| train | 52 | 176 | 270 | 66 | 204 | 349 | 149 | 241 | 1,382 | 43 | 2,932 |
| eval | 19 | 65 | 91 | 24 | 53 | 118 | 58 | 64 | 380 | 17 | 889 |

英文及多语言 strata 进一步覆盖 agent search/tool、code、crosslingual、instruction v2 non-thinking、instruction v3、math、science、safety、structured output、各语言 general/code/math/STEM。精确行数与监督 token 位于：

- `data/official_90_10/train_view/manifest.json`
- `data/official_90_10/eval_view/manifest.json`

## 引用净化做了什么

v2 的部分领域回答把内部证据 ID（文档名、行号、chunk、哈希）直接放进 assistant 文本并参与 loss。v3 的 `citation_optimization_v1`：

1. 定位 assistant 中的永久内部 ID；
2. 移除或改成本次请求内的短标签/自然语言；
3. 对结构化输出同步移除不必要的内部 citation 字段，并在需要时补充可读 schema 指令；
4. 保留 `source_evidence`、`citation_map`、`derivation` 和 provenance，供系统侧核验；
5. 重新用同一 tokenizer/chat template 计算 token 数；
6. 不调用教师模型，不人工逐条润色，不改变通用记录。

转换统计：87,214 条记录处理；56,826 个 assistant 永久 ID 和 56,826 个 teacher payload ID 被移除；33,536 个 assistant ID 被局部化；创建 16,508 个 citation map、82,540 个映射项；4,531 条结构化任务移除内部字段并补充 schema prompt；6,868 条通用记录保持原样。

记录数保持稳定但监督 token 从 v2 的 train/eval 7,020,047/1,756,603 降至 4,376,884/1,093,439。下降是去除冗长引用后的预期结果，不代表丢失相同比例的任务。

## accepted 记录字段字典

| 字段 | 含义 | 是否应进入模型输入/loss |
|---|---|---|
| `messages` | OpenAI 风格多轮消息；可含 user/assistant/tool | 按 chat template 输入；只对 mask 指定的 assistant 内容计 loss |
| `tools` | 当前样本可见工具 schema | 工具轨迹样本需要；普通问答可能为空 |
| `loss_mask_policy` | 哪些消息/span 参与监督 | 训练打包器必须遵守 |
| `supervised_token_count` | 使用固定 tokenizer/template 计算的监督 token | 配额与审计，不直接作为文本训练 |
| `total_token_count` | 完整渲染输入 token | 长度/packing 估算 |
| `task_family` | 能力族 | 分层采样、逐类评测 |
| `split` | `train` 或 `eval` | 禁止跨 split 混用 |
| `split_group` | 来源/语义隔离组 | 防泄漏审计 |
| `record_id` | 稳定记录 ID | 去重与追踪 |
| `language` | 样本主要语言 | 语言配比分析 |
| `source_evidence` | 生成所依据的白书片段或上游来源 | provenance；通常不作为最终回答的一部分 |
| `environment_replay` | 工具环境与预期交互回放 | Agent/工具轨迹重放与验证 |
| `validation` | 自动规则、schema、语义等检查结果 | 质检，不训练 |
| `generation`、`teacher_payload` | 教师模型、prompt、版本及生成审计 | provenance，不训练 |
| `review_status` | 发布/验证状态 | 数据门禁 |
| `scenario`、`tool_surface_id` | 场景与工具表面形式 | 泛化与回放分析 |

实际训练不要将整行 JSON 序列化后喂给模型。应由数据适配器读取 `messages`/`tools`，依据 `loss_mask_policy` 和固定 chat template 生成 input IDs 与 labels。


v3 新增/强化的字段：

| 字段 | 含义 |
|---|---|
| `derivation` | 该记录从 v2 到 v3 的确定性转换版本、源 ID/哈希和变换摘要 |
| `citation_map` | 仅在需要的工具/注入类记录中保存内部证据到请求内短标签的映射；供系统审计，不应作为回答正文训练 |
| `validation` | 转换后结构、语义和引用规则的复核结果 |

## split 的隔离语义

- `train` 用于梯度更新；`eval` 用于 loss/行为评测。
- 八个项目域 family 沿用清理后的来源分组隔离。
- 通用池按上游 ID 和冻结选择分别构造 train/eval。
- v3 的两个 config 共享项目域记录：不能把 `canonical_full_pool/train` 与 `official_90_10/train` 拼接，否则项目域样本重复一次，部分通用样本也重复。

## 与本地训练 package 的关系

Hugging Face 仓库保存 canonical JSONL 和正式视图，未上传本地 NumPy packed package。九个正式 run 使用的本地 full package 由 `official_90_10/train` 确定性构建：67,195 条、44,084,610 输入 token、4,083,167 监督 token、5,824 个 8,192-token pack，packing efficiency 0.9240。eval package 为 16,972 条、11,016,416 总 token、1,019,737 监督 token，并另含 269 条行为评测。若重新打包，应固定 tokenizer/template、最大长度、packing 代码与 seed。

## 推荐训练步骤

1. 加载 `official_90_10/train`。
2. 检查 `review_status` 与 manifest identity。
3. 从 `messages`/`tools` 渲染模型原生模板；严格应用 `loss_mask_policy`。
4. 依据最大长度决定 truncate/pack；任何过滤都生成新的 manifest。
5. 用 `official_90_10/eval` 计算总体和逐 family loss；另外保留不公开的行为/Agent eval。
6. 报告样本数、输入 token、监督 token、每个 family 和每种语言，而非只报告 epoch。
## 使用方法

推荐先使用 streaming 检查 schema，确认无误后再完整下载：

```python
from datasets import load_dataset
official_90_10_train = load_dataset("vosldtgbj/project-llm-dataset-sft-citation-optimized-v3", "official_90_10", split="train", streaming=True)
print(next(iter(official_90_10_train)))
official_90_10_eval = load_dataset("vosldtgbj/project-llm-dataset-sft-citation-optimized-v3", "official_90_10", split="eval", streaming=True)
print(next(iter(official_90_10_eval)))
canonical_full_pool_train = load_dataset("vosldtgbj/project-llm-dataset-sft-citation-optimized-v3", "canonical_full_pool", split="train", streaming=True)
print(next(iter(canonical_full_pool_train)))
canonical_full_pool_eval = load_dataset("vosldtgbj/project-llm-dataset-sft-citation-optimized-v3", "canonical_full_pool", split="eval", streaming=True)
print(next(iter(canonical_full_pool_eval)))
```

固定 revision：

```python
ds = load_dataset(
    "vosldtgbj/project-llm-dataset-sft-citation-optimized-v3",
    "official_90_10",
    split="train",
    revision="<commit SHA>",
)
```

## 全系列血缘图

```text
公开日文白书 SF-RAW-v1
├── 分词、分组切分、按 token 混入通用 CPT/SFT ──> SF-CPT-v1
├── 教师生成九类 SFT + 自动/语义质检 ──> SF-SFT-v1
│   └── 客户任务清理 + 多语言多能力通用池 ──> SF-SFT-v2
│       └── 确定性引用净化 + 重新冻结 90/10 ──> SF-SFT-v3
└── 事实预索引 + 资格过滤 + 教师生成 + verifier fixture ──> SF-RLVR-Domain-v1
    └── 加入八个 NVIDIA 通用 RL 数据源 ──> SF-RLVR-Unified-v2
```

这里有两类不同的“关系”：

1. **数据血缘**：箭头表示下游数据由上游内容经过明确转换或抽样得到。
2. **模型训练顺序**：CPT checkpoint 可作为 SFT 起点，SFT checkpoint 可作为 RLVR 起点；这是权重关系，不表示 CPT Arrow 会转换成 SFT/RLVR JSONL。

七个仓库的职责：

| 别名 | 仓库 | 角色 | 当前建议 |
|---|---|---|---|
| SF-RAW-v1 | `project-llm-dataset-jp-whitepapers-v1` | 104 份项目域原始资料 | 重建数据时使用 |
| SF-CPT-v1 | `project-llm-dataset-cpt-frozen-3aef2778` | 已分词的 CPT 冻结包 | 复现 CPT 时使用 |
| SF-SFT-v1 | `project-llm-dataset-sft-generated-v1` | 第一轮完整生成审计集 | 仅审计/历史比较 |
| SF-SFT-v2 | `project-llm-dataset-sft-canonical-v2` | 90/10 多语言 canonical | 复现 v2 实验 |
| SF-SFT-v3 | `project-llm-dataset-sft-citation-optimized-v3` | 引用净化后的正式 SFT | 新 SFT 首选 `official_90_10` |
| SF-RLVR-Domain-v1 | `project-llm-dataset-rlvr-domain-v1` | 由白书构造的领域可验证题库 | 领域 RLVR/审计 |
| SF-RLVR-Unified-v2 | `project-llm-dataset-rlvr-unified-v2-37500` | 领域 + 通用的统一多环境题库 | 当前 RLVR 首选 execution config |

## 完整性、版本固定与复现

仓库根目录提供以下控制文件：

| 文件 | 作用 |
|---|---|
| `FILES.json` | 每个发布文件的上传前本地路径、仓库路径、字节数、mtime 与 SHA-256；适合程序审计 |
| `SHA256SUMS` | 可直接交给 `sha256sum -c` 的内容校验表 |
| `LINEAGE.json` | 本仓库的父版本、子版本、身份和关键数量 |
| `UPLOAD_MANIFEST.json` | 发布操作、目标 repo、文件数和总字节数 |
| `SOURCE_PATHS.md` | 制作时 canonical 本地位置；仅用于解释原始工作区，不是跨机器加载接口 |

下载后校验：

```bash
sha256sum -c SHA256SUMS
```

应把 repo commit、数据 config、split、manifest identity、代码版本、tokenizer/chat template 和训练配置一起记录。只写仓库名而不写 commit，无法严格复现实验。

## 公开性、评测污染与许可

本仓库公开发布用于研究、审计和实验复现。凡是这里公开的 `eval`、`locked_eval` 或参考答案，都已经失去“对未来模型保密”的属性：它们可以复现既有结果，也可以做开发集或公开 benchmark，但不能继续充当未来模型的私有盲测。未来正式报告应另建未公开、未参与 prompt 调整和人工挑选的评测集。

根卡使用 `license: other`，因为仓库可能同时包含日本政府公开材料、项目生成派生数据以及具有不同许可证的第三方数据。`other` 不会覆盖或重新许可上游内容。使用者必须逐一遵守上游条款、署名要求、可接受用途、隐私与再分发限制；尤其不能仅依据本仓库的可下载性推断所有上游材料均属于同一种许可证。

## 已知限制

- 时间截面固定在 2026-10-08 前后的项目归档状态；它不是持续更新的数据服务。
- 数据主要围绕日文防卫/警察白书及所选通用能力，不能代表所有日语领域、国家、文化或任务。
- 生成数据与规则验证能降低错误率，不能证明每个自然语言陈述都绝对正确。
- 行数、字节数、输入 token、监督 token 和 RLVR rollout 数是不同口径；比较数据量时必须注明口径。
- 发布目录中的 manifest 与审计字段可能包含内部实现名称。训练时应显式选择需要的字段，避免让模型学习 provenance 元数据。
