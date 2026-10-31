---
license: mit
task_categories:
  - text-generation
  - question-answering
language:
  - ko
  - zh
tags:
  - fortune-telling
  - bazi
  - astrology
  - tarot
  - divination
size_categories:
  - 10K<n<100K
---

<div align="center">

```
██████╗ ██████╗  ██████╗  ██████╗███████╗███████╗███████╗███████╗██████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║██║     █████╗  ███████╗███████╗█████╗  ██║  ██║
██╔═══╝ ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║╚════██║██╔══╝  ██║  ██║
██║     ██║  ██║╚██████╔╝╚██████╗███████╗███████║███████║███████╗██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚══════╝╚══════╝╚═════╝
```

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=35&duration=3000&pause=1000&color=00FF41&center=true&vCenter=true&width=600&lines=SYSTEM%3A+YEJI+PROCESSED;SAMPLES%3A+43%2C704;STATUS%3A+REFINED" alt="Matrix Typing"/>

</div>

---

<div align="center">

## ⚡ REFINED TRAINING DATA ⚡

</div>

<img align="right" alt="Processed GIF" width="300" src="https://huggingface.co/datasets/tellang/yeji-processed/resolve/main/assets/proc-h.gif">

```bash
> ACCESS GRANTED: YEJI PROCESSED
> TYPE: Refined Fortune-Telling Dataset
> CLEARANCE LEVEL: PUBLIC
> TOTAL SAMPLES: 43,704
> QUALITY: PRODUCTION READY
> STATUS: DEPLOYED
```

**🔬 MISSION:**  
점술 AI 파인튜닝을 위한 정제된 학습 데이터

**🧠 FEATURES:**  
중복 제거, 품질 검증, 포맷 통일

**⚡ CAPTCHA:**  
<a href="https://huggingface.co/spaces/tellang/yeji-captcha">
<img src="https://img.shields.io/badge/%5B%20%5D%20YES%2C%20I%27M%20A%20ROBOT-VERIFY-00FF41?style=for-the-badge&logo=robot&logoColor=white"/>
</a>

<br clear="right"/>

---

<div align="center">

## 📊 DATA COMPOSITION 📊

<img src="https://huggingface.co/datasets/tellang/yeji-processed/resolve/main/assets/proc-s.gif" width="100">

</div>

```yaml
DATA_COMPOSITION:

  BAZI_사주팔자:
    samples: 21,798
    coverage: "49.9%"
    format: "Q&A pairs"

  ASTROLOGY_점성술:
    samples: 13,120
    coverage: "30.0%"
    format: "Horoscope readings"

  TAROT_타로:
    samples: 5,847
    coverage: "13.4%"
    format: "Card interpretations"

  JAMI_자미두수:
    samples: 2,939
    coverage: "6.7%"
    format: "Consultation dialogs"
```

<div align="center">

### ⚡ PROCESSING STATS ⚡

<img src="https://img.shields.io/badge/TOTAL-43,704-00FF41?style=for-the-badge&logo=database&logoColor=white"/>
<img src="https://img.shields.io/badge/DOMAINS-4-FF0080?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/QUALITY-99%25-00FFFF?style=for-the-badge&logoColor=black"/>
<img src="https://img.shields.io/badge/DUPLICATES-REMOVED-FF6600?style=for-the-badge&logoColor=white"/>

</div>

---

<div align="center">

## 💻 QUICK START 💻

</div>

```python
from datasets import load_dataset

# 정제된 학습 데이터 로드
ds = load_dataset("tellang/yeji-processed")
print(f"Loaded: {len(ds['train']):,} samples")  # 43,704

# 샘플 확인
sample = ds['train'][0]
print(f"Question: {sample['instruction'][:100]}...")
print(f"Answer: {sample['output'][:100]}...")

# 도메인별 필터링
bazi_data = ds['train'].filter(lambda x: 'bazi' in x.get('domain', '').lower())
```

---

<div align="center">

## 🔗 RELATED DATASETS 🔗

</div>

<table>
<tr>
<td width="50%">

#### 📥 SOURCE
```
yeji-datasets (RAW)
```
원본 수집 데이터

[![SOURCE](https://img.shields.io/badge/DATASET-000000?style=for-the-badge&logo=huggingface&logoColor=FF0000)](https://huggingface.co/datasets/tellang/yeji-datasets)

</td>
<td width="50%">

#### 📤 EXTENDED
```
yeji-bazi-translated-ko
```
한국어 번역 확장 데이터

[![EXTENDED](https://img.shields.io/badge/DATASET-000000?style=for-the-badge&logo=huggingface&logoColor=FF0080)](https://huggingface.co/datasets/tellang/yeji-bazi-translated-ko)

</td>
</tr>
</table>

---

<div align="center">

## 🌐 NETWORK CONNECTIONS 🌐

<img src="https://huggingface.co/datasets/tellang/yeji-processed/resolve/main/assets/proc-f.gif" width="100">

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
@misc{yeji-processed2026,
  title   = {YEJI Processed: Refined Fortune-Telling Training Data},
  author  = {tellang},
  year    = {2026},
  publisher = {Hugging Face},
  url     = {https://huggingface.co/datasets/tellang/yeji-processed}
}
```

---

<div align="center">

### ⚡ SYSTEM MONITORING ⚡

```
> STATUS: DEPLOYED AND READY
> QUALITY: VERIFIED
> NEXT_MISSION: AI FINE-TUNING
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
