---
license: mit
task_categories:
  - text-generation
language:
  - ko
  - zh
tags:
  - fortune-telling
  - raw-data
  - collection
size_categories:
  - 100K<n<1M
---

<div align="center">

```
██████╗  █████╗ ██╗    ██╗    ██████╗  █████╗ ████████╗ █████╗
██╔══██╗██╔══██╗██║    ██║    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██████╔╝███████║██║ █╗ ██║    ██║  ██║███████║   ██║   ███████║
██╔══██╗██╔══██║██║███╗██║    ██║  ██║██╔══██║   ██║   ██╔══██║
██║  ██║██║  ██║╚███╔███╔╝    ██████╔╝██║  ██║   ██║   ██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
```

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=35&duration=3000&pause=1000&color=FF0000&center=true&vCenter=true&width=600&lines=SYSTEM%3A+RAW+DATA;TYPE%3A+ARCHIVED;MULTI-DOMAIN" alt="Matrix Typing"/>

</div>

---

<div align="center">

## ⚡ ORIGINAL DATA ARCHIVE ⚡

</div>

<img align="right" alt="Archive GIF" width="300" src="https://huggingface.co/datasets/tellang/yeji-datasets/resolve/main/assets/data-h.gif">

```bash
> ACCESS GRANTED: YEJI DATASETS
> TYPE: Raw Data Collection
> CLEARANCE LEVEL: PUBLIC
> STATUS: ARCHIVED
> PURPOSE: Source Material
> WARNING: UNPROCESSED DATA
```

**🔬 MISSION:**  
점술 AI 학습용 원본 수집 데이터

**🧠 DOMAINS:**  
사주팔자, 호로스코프, 자미두수, 타로

**⚡ CAPTCHA:**  
<a href="https://huggingface.co/spaces/tellang/yeji-captcha">
<img src="https://img.shields.io/badge/%5B%20%5D%20YES%2C%20I%27M%20A%20ROBOT-VERIFY-00FF41?style=for-the-badge&logo=robot&logoColor=white"/>
</a>

<br clear="right"/>

---

<div align="center">

## 📊 DATA SOURCES 📊

<img src="https://huggingface.co/datasets/tellang/yeji-datasets/resolve/main/assets/data-s.gif" width="100">

</div>

```yaml
RAW_DATA_COLLECTION:

  SOURCES:
    web_scraping: "Fortune-telling websites"
    api_collection: "Astrology APIs"
    manual_curation: "Expert consultations"
    book_digitization: "Traditional texts"
    
  DOMAINS:
    bazi: "Chinese astrology (四柱八字)"
    horoscope: "Western astrology"
    jami: "Purple star (紫微斗數)"
    tarot: "Card divination"
    
  DATA_STATE:
    duplicates: "May exist"
    format: "Various"
    quality: "Unverified"
    
  RECOMMENDED_USE:
    - "Research and analysis"
    - "Preprocessing pipeline input"
    - "Data exploration"
```

<div align="center">

### ⚡ ARCHIVE STATUS ⚡

<img src="https://img.shields.io/badge/STATUS-ARCHIVED-FF0000?style=for-the-badge&logo=archive&logoColor=white"/>
<img src="https://img.shields.io/badge/TYPE-RAW-FFFF00?style=for-the-badge&logoColor=black"/>
<img src="https://img.shields.io/badge/DOMAINS-MULTI-00FFFF?style=for-the-badge&logoColor=black"/>
<img src="https://img.shields.io/badge/USE-RESEARCH-00FF41?style=for-the-badge&logoColor=white"/>

</div>

---

<div align="center">

## 💻 QUICK START 💻

</div>

```python
from datasets import load_dataset

# 원본 데이터 로드
ds = load_dataset("tellang/yeji-datasets")

# 데이터 탐색
print(f"Total samples: {len(ds['train']):,}")
print(f"Columns: {ds['train'].column_names}")

# ⚠️ 주의: 원본 데이터는 전처리가 필요합니다
# 정제된 데이터를 원하시면 yeji-processed 사용 권장
# ds_clean = load_dataset("tellang/yeji-processed")
```

---

<div align="center">

## 🔗 DATA PIPELINE 🔗

</div>

<table>
<tr>
<td width="33%" align="center">

#### 📥 RAW (This)
```
yeji-datasets
```
원본 수집 데이터

[![RAW](https://img.shields.io/badge/STATUS-ARCHIVED-FF0000?style=for-the-badge)](https://huggingface.co/datasets/tellang/yeji-datasets)

</td>
<td width="33%" align="center">

#### ⚙️ PROCESSED
```
yeji-processed
```
정제된 학습 데이터

[![PROCESSED](https://img.shields.io/badge/STATUS-DEPLOYED-00FF41?style=for-the-badge)](https://huggingface.co/datasets/tellang/yeji-processed)

</td>
<td width="33%" align="center">

#### 📤 EXTENDED
```
yeji-bazi-translated
```
확장 번역 데이터

[![EXTENDED](https://img.shields.io/badge/STATUS-ACTIVE-FF0080?style=for-the-badge)](https://huggingface.co/datasets/tellang/yeji-bazi-translated-ko)

</td>
</tr>
</table>

---

<div align="center">

## 🌐 NETWORK CONNECTIONS 🌐

<img src="https://huggingface.co/datasets/tellang/yeji-datasets/resolve/main/assets/data-f.gif" width="100">

<a href="https://huggingface.co/tellang">
  <img src="https://img.shields.io/badge/HUGGINGFACE-000000?style=for-the-badge&logo=huggingface&logoColor=00FF41"/>
</a>
<a href="https://huggingface.co/datasets/tellang/yeji-meta">
  <img src="https://img.shields.io/badge/YEJI_META-FF0080?style=for-the-badge&logo=database&logoColor=white"/>
</a>

</div>

---

<div align="center">

## 📚 CITATION 📚

</div>

```bibtex
@misc{yeji-datasets2026,
  title   = {YEJI Datasets: Raw Fortune-Telling Data Collection},
  author  = {tellang},
  year    = {2026},
  publisher = {Hugging Face},
  url     = {https://huggingface.co/datasets/tellang/yeji-datasets}
}
```

---

<div align="center">

### ⚡ SYSTEM MONITORING ⚡

```
> STATUS: ARCHIVED
> TYPE: RAW DATA
> RECOMMENDATION: USE yeji-processed INSTEAD
```

---

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   🤖 YEJI PROJECT - YES, I AM A ROBOT                                        ║
║   Crafted BY AI, FOR AI, SERVING HUMANS                                      ║
║                                                                              ║
║   [ MIT License ]  [ HuggingFace ]  [ 2026 ]                                 ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

<a href="https://huggingface.co/spaces/tellang/yeji-captcha">
<img src="https://img.shields.io/badge/🤖_VERIFY_ROBOT_STATUS-CLICK_HERE-00FF41?style=for-the-badge"/>
</a>

</div>
