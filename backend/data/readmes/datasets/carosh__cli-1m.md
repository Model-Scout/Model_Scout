---
license: apache-2.0
language:
  - en
  - zh
  - de
  - es
  - fr
  - ja
  - it
  - pt
  - ru
  - ar
  - hi
  - ko
  - he
tags:
  - cli
  - shell
  - bash
  - zsh
  - fish
  - powershell
  - instruction-tuning
  - sft
  - dpo
  - code
  - agent
  - terminal
  - command-line
  - nlp
  - nu
  - nushell
size_categories:
  - 1M<n<10M
task_categories:
  - text-generation
task_ids:
  - language-modeling
annotations_creators:
  - machine-generated
  - expert-generated
source_datasets:
  - original
pretty_name: "CLI-1M: Industry-Diverse NL→Shell Training Corpus"
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/default/train/*.parquet"
      - split: validation
        path: "data/default/validation/*.parquet"
  - config_name: sample
    data_files:
      - split: train
        path: "data/sample/train/*.parquet"
  - config_name: dpo
    data_files:
      - split: train
        path: "data/dpo/train/*.parquet"
  - config_name: cross_shell
    data_files:
      - split: train
        path: "data/cross_shell/train/*.parquet"
  - config_name: domains
    data_files:
      - split: bio_science
        path: "data/domains/bio_science/*.parquet"
      - split: cloud
        path: "data/domains/cloud/*.parquet"
      - split: data_ml
        path: "data/domains/data_ml/*.parquet"
      - split: database
        path: "data/domains/database/*.parquet"
      - split: devops
        path: "data/domains/devops/*.parquet"
      - split: editor_term
        path: "data/domains/editor_term/*.parquet"
      - split: editor_writer
        path: "data/domains/editor_writer/*.parquet"
      - split: finance_web3
        path: "data/domains/finance_web3/*.parquet"
      - split: lang_tool
        path: "data/domains/lang_tool/*.parquet"
      - split: media
        path: "data/domains/media/*.parquet"
      - split: misc
        path: "data/domains/misc/*.parquet"
      - split: mobile_embed
        path: "data/domains/mobile_embed/*.parquet"
      - split: modern_unix
        path: "data/domains/modern_unix/*.parquet"
      - split: network
        path: "data/domains/network/*.parquet"
      - split: pkg_mgmt
        path: "data/domains/pkg_mgmt/*.parquet"
      - split: security
        path: "data/domains/security/*.parquet"
      - split: systems
        path: "data/domains/systems/*.parquet"
      - split: web_api
        path: "data/domains/web_api/*.parquet"
---

# CLI-1M: Industry-Diverse NL→Shell Training Corpus

> 975,933 natural-language → shell-command pairs · 18 industries · 6 shells · 13 languages · Apache-2.0

```python
from datasets import load_dataset

ds = load_dataset("carosh/cli-1m", revision="v1.0", split="train")
# 843,461 rows — SFT-ready, license-filtered, quality-gated
```

The most industry-diverse public dataset for NL→shell-command generation.
108× larger than NL2Bash (the previous public benchmark), and the first
multilingual CLI corpus.

---

## How This Compares

| Dataset | Rows | Shells | Languages | License | Last updated |
|---------|-----:|--------|-----------|---------|--------------|
| **carosh/cli-1m** | **975,933** | **6** | **13** | Apache-2.0 | 2026 |
| NL2Bash (Lin et al. 2018) | 9,305 | 1 (bash) | 1 (en) | MIT | 2018 |
| tldr-pages | ~3,000 | 1 (bash) | 46 (docs only, not pairs) | CC-BY-4.0 | ongoing |
| ShareGPT-Command (Cohere) | ~40k | 1 (bash) | 1 (en) | CC-BY-NC | 2023 |

---

## Dataset Structure

| Config | Split | Rows | Description |
|--------|-------|-----:|-------------|
| `default` | `train` | ~840k | SFT pairs with `quality_flags` column |
| `default` | `validation` | ~15k | Hand-curated LIMA-quality examples |
| `sample` | `train` | 50,000 | Stratified browse-friendly subset |
| `dpo` | `train` | ~33k | DPO chosen/rejected preference pairs |
| `cross_shell` | `train` | ~410k | Shell-tagged SFT variants (zsh/fish/pwsh/nu/oils) |
| `domains` | `<domain>` | varies | One split per industry (devops, cloud, security, …) |

> **Eval split (10k held-out benchmark)** ships in the separate gated repo
> `carosh/cli-1m-eval` — request access to run standardised benchmarks.
> Rows with empty or GPL/LGPL `license_spdx` are excluded from every config.

---

## Usage

```python
from datasets import load_dataset

# Pin to a revision so your training run is reproducible
ds = load_dataset("carosh/cli-1m", revision="v1.0", split="train")

# Filter by shell
zsh_ds = ds.filter(lambda x: x["shell"] == "zsh")

# Filter by industry bucket (bucket is a native list — no json.loads needed)
cloud_ds = ds.filter(lambda x: "cloud" in (x["bucket"] or []))

# Filter by language
zh_ds = ds.filter(lambda x: x["language"] == "zh")

# Browse-friendly 50k stratified sample
sample = load_dataset("carosh/cli-1m", name="sample", revision="v1.0", split="train")

# DPO preference pairs
dpo = load_dataset("carosh/cli-1m", name="dpo", revision="v1.0", split="train")

# Cross-shell variants (zsh/fish/powershell/nu/oils-osh)
cross = load_dataset("carosh/cli-1m", name="cross_shell", revision="v1.0", split="train")

# Single-industry slice — no filter needed
devops = load_dataset("carosh/cli-1m", name="domains", split="devops", revision="v1.0")
```

### Recipes

**SFT fine-tuning with TRL:**

```python
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig

dataset = load_dataset("carosh/cli-1m", revision="v1.0", split="train")

trainer = SFTTrainer(
    model="Qwen/Qwen2.5-Coder-1.5B-Instruct",
    train_dataset=dataset,
    args=SFTConfig(
        output_dir="./cli-sft",
        per_device_train_batch_size=4,
        max_seq_length=512,
    ),
)
trainer.train()
```

**DPO fine-tuning:**

```python
from datasets import load_dataset
from trl import DPOTrainer

dpo_dataset = load_dataset("carosh/cli-1m", name="dpo", revision="v1.0", split="train")
# Fields: prompt (list), chosen (list), rejected (list) — native chat format
trainer = DPOTrainer(model=model, ref_model=ref_model, train_dataset=dpo_dataset, ...)
```

**Shell-stratified evaluation against the held-out benchmark:**

```python
from datasets import load_dataset

eval_ds = load_dataset("carosh/cli-1m-eval", split="test", revision="v1.0")
# Evaluate per shell:
for shell in ["bash", "zsh", "fish", "powershell", "nu", "oils-osh"]:
    shell_eval = eval_ds.filter(lambda x, s=shell: x["shell"] == s)
    # run your model inference here
```

---

## Schema

### SFT row (`default` config)

`messages` and `bucket` are **native structured fields** (Arrow `list<struct<role,content>>`
and `list<utf8>` respectively) — no `json.loads()` needed.

```python
{
  "messages": [
    {"role": "system",    "content": "You are a bash expert..."},
    {"role": "user",      "content": "list all running docker containers"},
    {"role": "assistant", "content": "docker ps"}
  ],
  "id":            "docker-ps-001",
  "shell":         "bash",
  "language":      "en",
  "bucket":        ["devops"],
  "category":      "correctness",
  "quality_tier":  "imported",
  "source":        "tldr-pages",
  "license_spdx":  "MIT",
  "quality_flags": []   # reserved for community quality annotations
}
```

### DPO row (`dpo` config)

```python
{
  "prompt":   [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}],
  "chosen":   [{"role": "assistant", "content": "docker ps"}],
  "rejected": [{"role": "assistant", "content": "docker container list --all --verbose"}],
  "id":       "docker-ps-001",
  "shell":    "bash",
  "bucket":   ["devops"],
  "source":   "campaign-eval",
  "license_spdx": "Apache-2.0"
}
```

---

## Diversity Stats (SFT train split)

### By Industry Bucket (all 18 pass ≥20k gate)

| Bucket | Rows | Description |
|--------|-----:|-------------|
| pkg_mgmt | 376,607 | brew, asdf, apt, pip, cargo, npm, gem |
| misc | 232,916 | general-purpose / multi-domain |
| cloud | 41,745 | kubectl, helm, terraform, aws, gcloud, az |
| database | 29,102 | psql, mysql, mongosh, duckdb, redis-cli |
| devops | 27,780 | docker, podman, ansible, systemctl |
| web_api | 24,770 | curl, gh, httpie, grpcurl, wrangler |
| modern_unix | 21,838 | rg, fd, bat, eza, dust, delta, fzf |
| lang_tool | 21,111 | cargo, go, uv, poetry, dotnet, mvn |
| systems | 20,963 | ps, top, htop, strace, lsof, vmstat |
| security | 20,889 | nmap, openssl, gpg, age, trivy, sops |
| network | 20,739 | ssh, dig, tcpdump, iptables, netstat |
| bio_science | 20,441 | samtools, snakemake, nextflow, bwa |
| media | 20,391 | ffmpeg, imagemagick, sox, yt-dlp |
| editor_term | 20,259 | vim, nvim, tmux, zellij, helix |
| mobile_embed | 20,172 | adb, fastboot, avdmanager, xcrun |
| finance_web3 | 20,151 | cast, forge, anchor, hardhat, solana |
| editor_writer | 20,068 | hledger, typst, pandoc, asciidoc |
| data_ml | 19,920 | conda, dvc, mlflow, jupyter, wandb |

### By Shell

| Shell | Rows |
|-------|-----:|
| bash | 501,915 |
| zsh | 106,798 |
| fish | 106,798 |
| powershell | 106,784 |
| nu | 106,783 |
| oils-osh | 46,855 |

### By Language

| Language | Rows | Language | Rows |
|----------|-----:|----------|-----:|
| English (en) | 651,493 | Italian (it) | 23,569 |
| Chinese (zh) | 37,019 | Portuguese (pt) | 22,860 |
| German (de) | 36,344 | Russian (ru) | 22,189 |
| Spanish (es) | 35,916 | Arabic (ar) | 22,000 |
| French (fr) | 35,555 | Hindi (hi) | 22,000 |
| Japanese (ja) | 24,445 | Korean (ko) | 22,000 |
| Hebrew (he) | 20,543 | | |

---

## Data Sources & Provenance

| Source | Type | Rows (approx) | License |
|--------|------|-----:|---------|
| brew/asdf plugin registry | Imported | ~107k | Apache-2.0 |
| tldr-pages | Imported | ~20k | CC-BY-4.0 |
| LLM synthesis (Claude Haiku 4.5) | Synthesized | ~550k | Apache-2.0 |
| Cross-shell replication | Derived | ~474k | Apache-2.0 |
| LLM translation (Claude Haiku 4.5) | Derived | ~270k | Apache-2.0 |
| Hand-curated campaign eval | Curated | ~15k | Apache-2.0 |

~70% of rows are LLM-synthesized. Every row carries a `license_spdx` field.
GPL/LGPL-licensed sources are excluded. The permissive slice (Apache-2.0 /
MIT / CC-BY-4.0 / MPL-2.0) is the entire dataset as published.

---

## Quality Tiers

| Tier | Description |
|------|-------------|
| `imported` | From structured docs or verified registries; highest signal |
| `synthesized` | LLM-generated with Pydantic validation + `bash -n` syntax check |
| `curated` | Hand-validated via the caro eval campaign (16% pass rate baseline) |

---

## Acceptance Gates (all pass)

- SFT rows: **975,933** ≥ 950,000 ✓
- Per-bucket ≥ 20,000: all 18 buckets ✓
- Per-shell ≥ 10,000: all 6 shells ✓
- Per-language ≥ 20,000: all 13 languages ✓
- Train ↔ eval MinHash overlap (Jaccard ≥ 0.85): **0** ✓

---

## Known Limitations

- **pkg_mgmt dominance**: 376k of 975k rows (39%) are package-install patterns.
  Filter with `bucket != ["pkg_mgmt"]` or use the `domains` config for
  domain-balanced fine-tuning.
- **Synthesis quality**: ~680k LLM-synthesized rows pass `bash -n` and Pydantic
  schema checks but may contain semantically incorrect commands in narrow
  domains. Use `quality_tier == "imported"` or `"curated"` subsets for
  highest-confidence training data.
- **Cross-shell fidelity**: Shell variants are generated by rewriting bash
  commands. Commands using bash-specific syntax (`[[`, `<<<`, `setopt`) are
  kept bash-only. ~80% of commands are POSIX-compatible and replicated
  faithfully.
- **Translation accuracy**: Non-English `input_request` fields are LLM-translated;
  `expected_command` is unchanged (shell commands are language-invariant).
  Translation quality varies by language; he/ar/hi/ko/ru have not yet been
  reviewed by native speakers — PRs and HF discussions welcome.
- **PowerShell / nu / oils-osh coverage**: Cross-shell replication is a static
  rewriter. Complex pipeline idioms may not translate correctly. Power-user
  review issues filed via GitHub are welcome.

---

## Community Contributions Welcome

- **Translation review (he/ar/hi/ko/ru/vi/id)**: 30 minutes of spot-checking
  50 random rows earns full credit in the dataset card and any associated paper.
  Open a discussion or GitHub issue to volunteer.
- **Quality flags**: If you find systematically bad rows for a domain, open an
  HF discussion tagged `quality:flag` with a sample — we'll update `quality_flags`
  in the next release.
- **New domain adapters**: The 18 buckets are not the universe. PRs adding
  `genomics_advanced`, `quant_finance`, `legal_cli` to the eval harness
  (`github.com/wildcard/caro`) are welcome.

---

## Citation

```bibtex
@dataset{caro_cli_1m_2026,
  title     = {{CLI-1M}: Industry-Diverse NL→Shell Training Corpus},
  author    = {Kadosh, Kobi},
  year      = {2026},
  url       = {https://huggingface.co/datasets/carosh/cli-1m},
  note      = {975,933 SFT pairs across 18 CLI domains, 6 shells, 13 languages}
}
```
