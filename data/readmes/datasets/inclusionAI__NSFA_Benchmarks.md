---
# For reference on dataset card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/datasetcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/datasets-cards
language:
  - af
  - sq
  - am
  - ar
  - hy
  - as
  - az
  - eu
  - be
  - bn
  - bs
  - bg
  - my
  - ca
  - ny
  - zh
  - hr
  - cs
  - da
  - dv
  - nl
  - dz
  - el
  - en
  - eo
  - et
  - fo
  - fi
  - fr
  - fy
  - gl
  - gd
  - lg
  - ka
  - de
  - gn
  - gu
  - ht
  - ha
  - he
  - hi
  - hu
  - is
  - ig
  - id
  - iu
  - ga
  - it
  - ja
  - jv
  - kn
  - ks
  - kk
  - km
  - rw
  - ko
  - ku
  - ky
  - lo
  - la
  - lv
  - ln
  - lt
  - lb
  - mk
  - mg
  - ms
  - ml
  - mt
  - gv
  - mi
  - mr
  - mn
  - nv
  - ne
  - no
  - nb
  - nn
  - oc
  - or
  - om
  - os
  - ps
  - fa
  - pl
  - pt
  - pa
  - qu
  - ro
  - rm
  - rn
  - ru
  - se
  - st
  - sa
  - sg
  - sd
  - si
  - sk
  - sl
  - sn
  - so
  - es
  - sr
  - ss
  - su
  - sw
  - sv
  - tl
  - tg
  - ta
  - tt
  - te
  - th
  - bo
  - ti
  - to
  - tn
  - ts
  - tk
  - tr
  - uk
  - ur
  - ug
  - uz
  - ve
  - vi
  - cy
  - wo
  - xh
  - yi
  - yo
  - zu
license: apache-2.0
tags:
  - guardrail
  - agent-security
  - llm-security
  - multilingual
  - NSFA
  - Not Secure For Agents
  - benchmark
task_categories:
  - text-classification
---

# Dataset Card for NSFA Benchmarks

NSFA Benchmarks are three multilingual evaluation benchmarks for assessing guardrail models that secure agentic AI systems against operational threats. They are grounded in the NSFA (**N**ot-**S**ecure-**F**or-**A**gents) taxonomy, a CIA-triad-grounded hierarchical classification of 185 risk variants. For full details on the taxonomy, data construction, and evaluation methodology, please refer to the accompanying paper (arXiv link coming soon).

## Dataset Details

### Dataset Description

| Benchmark | Total Samples | Pos:Neg Ratio | Domains | Variants | Languages |
|---|---|---|---|---|---|
| NSFA_Query_Multilingual | 63,431 | 29,474 : 33,957 | 5 | 160 | 133 |
| NSFA_Response_Multilingual | 29,972 | 14,314 : 15,658 | 2 | 25 | 133 |
| NSFA_CrossSource_Query_Multilingual | 3,435 | 2,315 : 1,120 | 5 | -- | 133 |

- The two purpose-built benchmarks (Query and Response) use distinct prompting templates from training data, employ a seven-model majority-vote annotation protocol, and apply aggressive MinHashLSH-based deduplication across the training-evaluation boundary.
- The cross-source benchmark is adapted from five public agent-security datasets (AgentDojo, InjecAgent, AgentHarm, AgentDyn, and ATBench) and is fully independent of the training data by construction.

- **Curated by:** SingGuard Team, AI Security Lab, Ant Group
- **Language(s) (NLP):** 133 languages
- **License:** Apache 2.0

### Dataset Sources

- **Repository:** https://github.com/inclusionAI/SingGuard-NSFA
- **Hugging Face:** https://huggingface.co/datasets/inclusionAI/NSFA_Benchmarks
- **ModelScope:** https://www.modelscope.cn/datasets/inclusionAI/NSFA_Benchmarks
- **Paper:** SingGuard-NSFA: Extensible Guardrails for Agentic AI via Generative Reasoning and Real-Time Classification (https://arxiv.org/abs/2607.13081)

## Citation

**BibTeX:**

```bibtex
@article{singguard2026nsfa,
  title     = {SingGuard-NSFA: Extensible Guardrails for Agentic AI via Generative Reasoning and Real-Time Classification},
  author    = {Li, Hongcheng and Yi, Sibo and Liao, Bingyan and Fu, Kaiwen and Xiong, Run and Wu, Chen and Yin, Shenglin and Li, Zongyi and Bai, Yichen and He, Liangbo and Lan, Jun and Cui, Shiwen and Meng, Changhua and Wang, Weiqiang},
  year      = {2026}
}
```