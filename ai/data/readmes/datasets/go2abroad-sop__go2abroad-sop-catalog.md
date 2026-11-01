---
license: apache-2.0
task_categories:
- text-retrieval
- tabular-classification
language:
- en
- zh
- de
- ja
- fr
- es
- pt
- it
- ko
- ar
- hi
tags:
- manufacturing
- engineering
- compliance
- industry
- standard-operating-procedures
- isic-rev4
pretty_name: GO2ABROAD SOP - Global Industrial Intelligence Core
size_categories:
- 100K<n<1M
---

# GO2ABROAD SOP — Global Industrial Operating Procedures Core

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23767285.svg)](https://doi.org/10.5281/zenodo.23767285)
[![Verified SOPs](https://img.shields.io/badge/Verified%20SOPs-143%2C729-success.svg)](https://sop.go2abroad.space)
[![Jurisdictions](https://img.shields.io/badge/Jurisdictions-180%2B-orange.svg)](https://sop.go2abroad.space)
[![ISIC Sectors](https://img.shields.io/badge/ISIC%20Sectors-419-blueviolet.svg)](https://sop.go2abroad.space)

**GO2ABROAD SOP** is an open-access industrial compliance and technical intelligence repository covering **140,000+** verified Standard Operating Procedures across **180+** jurisdictions and **419** UN ISIC Rev.4 industrial classifications with full 11-language support.

---

### 🌐 Official Multilingual Portals & Field Execution Engines
* [English Portal](https://sop.go2abroad.space/en/)
* [简体中文官方门户](https://sop.go2abroad.space/zh/)
* [Deutscher Portal](https://sop.go2abroad.space/de/)
* [日本語ポータル](https://sop.go2abroad.space/ja/)
* [Portail Français](https://sop.go2abroad.space/fr/)
* [Portal Español](https://sop.go2abroad.space/es/)
* [Português](https://sop.go2abroad.space/pt/)
* [Italiano](https://sop.go2abroad.space/it/)
* [한국어](https://sop.go2abroad.space/ko/)
* [العربية](https://sop.go2abroad.space/ar/)
* [हिन्दी](https://sop.go2abroad.space/hi/)

---

### 📦 Open Data Assets & Repositories
* **Official SOP Interactive Portal & Field Execution Engine**: [https://sop.go2abroad.space](https://sop.go2abroad.space)
* **Company Registry Hub**: [https://registry.go2abroad.space](https://registry.go2abroad.space)
* **GitHub Repository**: [go2abroad-sop/go2abroad-sop-catalog](https://github.com/go2abroad-sop/go2abroad-sop-catalog)

---

### 📋 Dataset Summary & Schema
The dataset provides compact global metadata indexes, verified engineering tolerances, international compliance codes (ISO, DIN, OSHA, ASME, IEC), and direct operational URLs.

#### Data Fields:
* `sop_id` *(string)*: Unique identifier formatted as `{ISO3}-{ISIC}-{TRACK}-{TIER}-{SCENARIO}`.
* `country` *(string)*: ISO-3166 alpha-3 jurisdiction code (e.g., DEU, USA, CHN).
* `industry_isic` *(string)*: UN ISIC Rev.4 4-digit industrial classification code.
* `standards` *(list)*: Primary compliance standards governing the procedure.
* `roles` *(dict)*: Localized target job role across 11 languages.
* `scenarios` *(dict)*: Localized operational scenario and commissioning scope.
* `summaries` *(dict)*: Localized critical tolerance metrics and baseline checks.
* `urls` *(dict)*: Direct links to the official interactive field execution dossier.

---

### 💡 Notice
This open dataset repository provides high-level index metadata, quantitative tolerances, and regulatory codes. Full DAG workflow state machines, mandatory PPE configurations, and interactive field work order modes are accessible via the official portal at [https://sop.go2abroad.space](https://sop.go2abroad.space).

---

### ⚖️ License & Citation
Released under the [Apache-2.0 License](https://opensource.org/licenses/Apache-2.0).

```bibtex
@misc{go2abroad_sop_2026,
  author = {GO2ABROAD Industrial Intelligence Group},
  title  = {Global Industrial Standard Operating Procedures (SOP) Knowledge Core},
  year   = {2026},
  doi    = {10.5281/zenodo.23767285},
  url    = {[https://sop.go2abroad.space](https://sop.go2abroad.space)}
}