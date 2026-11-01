---
license: mit
task_categories:
- tabular-classification
- text-retrieval
language:
- en
- zh
- ja
- de
- fr
- es
- it
- pt
- ko
- ar
- hi
tags:
- legal
- corporate-law
- compliance
- cross-border
- taxation
pretty_name: GO2ABROAD Registry Data Core
size_categories:
- 10K<n<100K
---

<div align="center">

# GO2ABROAD Registry Data Core

**Global Statutory Intelligence Engine & Cross-Border Corporate Compliance Dataset**

[![Zenodo DOI](https://img.shields.io/badge/Zenodo%20DOI-10.5281%2Fzenodo.23493470-blue.svg)](https://doi.org/10.5281/zenodo.23493470)
[![Figshare DOI](https://img.shields.io/badge/Figshare%20DOI-10.6084%2Fm9.figshare.34711899-brightgreen.svg)](https://doi.org/10.6084/m9.figshare.34711899)
[![Harvard Dataverse](https://img.shields.io/badge/Dataverse%20DOI-10.7910%2FDVN%2FXUWOHL-orange.svg)](https://doi.org/10.7910/DVN/XUWOHL)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Official Live Portal](https://registry.go2abroad.space) | [GitHub Master Repo](https://github.com/go2abroad-registry/go2abroad-registry-data) | [Gitee](https://gitee.com/go2abroad-registry) | [GitCode](https://gitcode.com/go2abroad-registry)

</div>

---

## 🌐 Overview
The **GO2ABROAD Registry Data Core** is an open-access statutory dataset and corporate compliance catalog systematizing cross-border corporate formation, multi-tier taxation, and commercial banking rails across **80+ jurisdictions worldwide**.

Built upon **23,795 structured statutory baseline dossiers** (expanded into **261,492 multilingual assets across 11 languages**), the dataset benchmarks the complete enterprise lifecycle across 6 critical statutory stages:
1. **Stage 1: Pre-Incorporation & UBO Transparency Protocol**: Beneficial ownership disclosure thresholds, restricted name registries, and initial formation budgets.
2. **Stage 2: Statutory Formation & Pro-Forma Governance**: Articles of Incorporation, official state filing fees, pro-forma board resolutions, and governing law citations.
3. **Stage 3: Tax Identity & Indirect Tax Nexus**: Tax identification protocols (EIN, VAT, TRN), pass-through check-the-box elections, and cross-border indirect sales tax thresholds.
4. **Stage 4: Banking Settlement Rails & EMI Whitelists**: Onboarding defense matrices, Fintech EMI whitelists (Mercury, Airwallex, Wise), and AML risk profiling.
5. **Stage 5: Annual Governance & Mandatory Audit Thresholds**: Mandatory annual filings, statutory registered agent retention, and compulsory audit revenue/asset thresholds.
6. **Stage 6: Corporate Income Tax (CIT) & International Reporting**: Statutory CIT rates, cross-border tax return forms, transfer pricing rules, and director liability penalties.

---

## 💻 How to Load with Python

```python
import pandas as pd

# Load master indexing catalogue
data_url = "[https://huggingface.co/datasets/go2abroad-registry/corporate-compliance-catalog/raw/main/dossier_catalog_merged.csv](https://huggingface.co/datasets/go2abroad-registry/corporate-compliance-catalog/raw/main/dossier_catalog_merged.csv)"
try:
    df = pd.read_csv(data_url)
    print(f"✅ Successfully loaded {len(df)} compliance dossiers.")
except Exception:
    print("Files currently uploading. Please check the 'Files and versions' tab.")
```

## 🏛️ Academic Citations & Persistent DOIs
If you utilize this statutory dataset in empirical research, machine learning benchmarks, or automated compliance tooling, please cite our permanent identifiers:

代码段
@dataset{go2abroad_registry_core_2026,
  author       = {GO2ABROAD Registry Working Group},
  title        = {GO2ABROAD Registry Data Core: Global Statutory Intelligence & Corporate Compliance Infrastructure},
  year         = 2026,
  publisher    = {Hugging Face / Zenodo / Figshare / Harvard Dataverse},
  doi          = {10.5281/zenodo.23493470},
  url          = {[https://registry.go2abroad.space](https://registry.go2abroad.space)}
}

## 📬 Ecosystem & Contact
Official Live Portal: https://registry.go2abroad.space

GitHub Organization: https://github.com/go2abroad-registry

General Inquiries: contact@go2abroad.space