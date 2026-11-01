---
pretty_name: SF-SFT-v2：90% 项目域 + 10% 多语言多能力通用 SFT
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
  - config_name: canonical
    data_files:
      - split: train
        path: data/canonical/*/train/accepted.jsonl
      - split: eval
        path: data/canonical/*/eval/accepted.jsonl
---


# SF-SFT-v2：90% 项目域 + 10% 多语言多能力通用 SFT

## 一句话定位

v2 将 v1 的八类项目域 accepted 数据清理后，与真正多语言、多能力的公开通用 SFT 池组合。配额按 **assistant 监督 token** 计算，而非按条数；train/eval 分别达到约 90% 项目域 + 10% 通用。它是 v3 的直接父版本，也是引用净化前的 canonical 基线。

## config、family 目录与 split

唯一 config `canonical` 用 glob 合并九个 family 目录：八个项目域 family + `general_diverse`。它提供：

| split | 项目域 条/监督 token | 通用 条/监督 token | 合计 条/监督 token | 通用 token 比例 |
|---|---:|---:|---:|---:|
| `train` | 64,263 / 6,318,013 | 5,385 / 702,034 | 69,648 / 7,020,047 | 10.000417% |
| `eval` | 16,083 / 1,580,928 | 1,483 / 175,675 | 17,566 / 1,756,603 | 10.000837% |

family 目录不是 Hugging Face config；它们是同一 config 内可通过 `task_family` 分层过滤的来源文件。`eval` 与 train 按原有 split group/上游 ID 隔离，不应并入训练。

## 分 family 规模

| family（目录名） | train 行 | eval 行 | train 监督 token | eval 监督 token | 训练意图 |
|---|---:|---:|---:|---:|---|
| `clarification_abstention_stop` | 20,188 | 5,114 | 719,086 | 180,209 | 缺信息时澄清、不可回答、合理拒答与停止 |
| `cross_document_reasoning` | 5,430 | 1,312 | 789,804 | 197,394 | 跨文档比较、汇总、计算与多跳归纳 |
| `general_diverse` | 5,385 | 1,483 | 702,034 | 175,675 | 多语言、多能力通用 SFT 锚点 |
| `injection_permission` | 1,752 | 439 | 327,140 | 82,015 | 间接提示注入、只读权限和操作边界 |
| `normal_tool_trajectory` | 6,881 | 1,725 | 1,435,667 | 358,999 | 正常搜索、打开证据、工具调用与停止 |
| `single_document_qa` | 17,950 | 4,511 | 1,223,832 | 306,060 | 单文档事实提取、单位和有依据回答 |
| `structured_output` | 3,629 | 902 | 334,594 | 83,687 | JSON/schema/字段约束和可解析输出 |
| `temporal_conflict` | 3,865 | 937 | 655,541 | 163,787 | 版本、时间状态、来源冲突与新旧口径 |
| `tool_failure_recovery` | 4,568 | 1,143 | 832,349 | 208,777 | 空结果、错误查询、工具失败后的改写与恢复 |

## `general_diverse` 的来源与能力

公开池来自：

- `nvidia/Nemotron-SFT-Instruction-Following-Chat-v3`
- `nvidia/Nemotron-SFT-Instruction-Following-Chat-v2`
- `nvidia/Nemotron-SFT-Agentic-v2`
- `nvidia/Nemotron-SFT-Multilingual-v2`
- `nvidia/Nemotron-SFT-Safety-v2`
- `nvidia/Nemotron-SFT-Math-v4`
- `nvidia/Nemotron-SFT-Competitive-Programming-v2`
- `nvidia/Nemotron-SFT-Science-v2`
- `CohereLabs/aya_dataset`（锁定 revision `f9ea04583f02a8f86404ff6c58bf75fe637df8a2`）

能力 strata 包括英文普通/非思考指令、Agent tool/search、结构化输出、安全、数学、科学、代码、跨语言，以及日语/中文/韩语/印地语/葡萄牙语/西班牙语/法语/德语/阿拉伯语/越南语/斯瓦希里语/孟加拉语。这里的目标是防止纯日语领域 SFT 造成其他语言和通用能力明显回归。

### 完整通用池的语言行数

| split | de | en | es | fr | hi | ja | ko | pt-BR | zh | ar+bn+sw+vi | 合计 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| train | 94 | 325 | 564 | 117 | 388 | 653 | 273 | 446 | 2,440 | 85 | 5,385 |
| eval | 30 | 120 | 170 | 36 | 95 | 198 | 83 | 108 | 617 | 26 | 1,483 |

行数不能代替 token 比例：代码、数学和 Agent 样本通常远长于普通指令。配额与训练报告必须使用 `supervised_token_count`。

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


## provenance/config

- `general_mix_canonical_20261002.yaml`：语言、能力、来源和 token 目标。
- `source_lock.json`：上游 repo/revision 或本地快照绑定策略。
- 其他配置固定 acceptance、split、tokenizer/template 与抽样规则。

仓库内的 `upstream` 字段保存每个通用样本的 repo、source/variant/stratum 和原始 ID。项目域样本使用 `source_evidence`、`generation`、`environment_replay` 等字段。训练时二者统一为 messages/tools/loss mask，但 provenance 结构不必完全相同。

## 与 v1、v3 的差异

### 相对 v1

- 删除/修复少量不再满足门禁的领域记录；例如 clarification train 从 20,267 变为 20,188，eval 从 5,120 变为 5,114。
- `general_anchor` 被覆盖更广的 `general_diverse` 取代。
- 重新按固定 tokenizer/template 统计监督 token，并按 token 精确配比。

### 相对 v3

v2 的领域 assistant 输出仍可能包含类似 `【defense_2004:L...:hash】` 的永久内部定位串。v3 对其做确定性引用净化，记录数和 split 身份保持稳定，但监督 token 显著下降。若研究引用净化的效果，v2 是基线；若训练实际模型，优先 v3 `official_90_10`。

## 训练建议

1. 从 `messages` 和 `tools` 渲染模型原生 chat template。
2. 只对 `loss_mask_policy` 指定的 assistant/目标 span 计算 loss。
3. 以 `task_family` 做监控，不建议训练前再按行重新均匀采样。
4. 保留原 train/eval；公开 eval 仅用于复现，未来正式盲测另建私有集。
5. 若直接拼入更多通用数据，重新按监督 token计算比例并冻结新的 identity。
## 使用方法

推荐先使用 streaming 检查 schema，确认无误后再完整下载：

```python
from datasets import load_dataset
canonical_train = load_dataset("vosldtgbj/project-llm-dataset-sft-canonical-v2", "canonical", split="train", streaming=True)
print(next(iter(canonical_train)))
canonical_eval = load_dataset("vosldtgbj/project-llm-dataset-sft-canonical-v2", "canonical", split="eval", streaming=True)
print(next(iter(canonical_eval)))
```

固定 revision：

```python
ds = load_dataset(
    "vosldtgbj/project-llm-dataset-sft-canonical-v2",
    "canonical",
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
