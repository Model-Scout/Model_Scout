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
  - jami
  - ziwei
  - consultation
size_categories:
  - 1K<n<10K
---

<div align="center">

```
     ██╗ █████╗ ███╗   ███╗██╗    ███████╗██╗██╗    ██╗███████╗██╗
     ██║██╔══██╗████╗ ████║██║    ╚══███╔╝██║██║    ██║██╔════╝██║
     ██║███████║██╔████╔██║██║      ███╔╝ ██║██║ █╗ ██║█████╗  ██║
██   ██║██╔══██║██║╚██╔╝██║██║     ███╔╝  ██║██║███╗██║██╔══╝  ██║
╚█████╔╝██║  ██║██║ ╚═╝ ██║██║    ███████╗██║╚███╔███╔╝███████╗██║
 ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝    ╚══════╝╚═╝ ╚══╝╚══╝ ╚══════╝╚═╝
```

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=35&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=600&lines=SYSTEM%3A+JAMI+ZIWEI;SAMPLES%3A+7%2C983;STAR+CHARTS" alt="Matrix Typing"/>

</div>

---

<div align="center">

## ⚡ PURPLE STAR ASTROLOGY ⚡

</div>

<img align="right" alt="Jami GIF" width="300" src="https://huggingface.co/datasets/tellang/yeji-jami-consultation/resolve/main/assets/jami-h.gif">

```bash
> ACCESS GRANTED: JAMI CONSULTATION
> TYPE: Ziwei Doushu Q&A Dataset
> CLEARANCE LEVEL: PUBLIC
> SAMPLES: 7,983
> DOMAIN: Purple Star Astrology
> STATUS: ACTIVE
```

**🔬 MISSION:**  
자미두수 (紫微斗數) 상담 Q&A 데이터

**🧠 COVERAGE:**  
명반 해석, 대한 분석, 인생 조언

**⚡ CAPTCHA:**  
<a href="https://huggingface.co/spaces/tellang/yeji-captcha">
<img src="https://img.shields.io/badge/%5B%20%5D%20YES%2C%20I%27M%20A%20ROBOT-VERIFY-00FF41?style=for-the-badge&logo=robot&logoColor=white"/>
</a>

<br clear="right"/>

---

<div align="center">

## 📊 STAR CHART SYSTEM 📊

<img src="https://huggingface.co/datasets/tellang/yeji-jami-consultation/resolve/main/assets/jami-s.gif" width="100">

</div>

```yaml
JAMI_SYSTEM_紫微斗數:

  MAIN_STARS_主星:
    - 紫微: "Emperor Star"
    - 天機: "Heavenly Secret"
    - 太陽: "Sun Star"
    - 武曲: "Military Star"
    - 天同: "Heavenly Unity"
    - 廉貞: "Chaste Star"
    
  PALACES_十二宮:
    - 命宮: "Life Palace"
    - 兄弟宮: "Siblings Palace"
    - 夫妻宮: "Marriage Palace"
    - 子女宮: "Children Palace"
    - 財帛宮: "Wealth Palace"
    - 疾厄宮: "Health Palace"
    
  CONTENT_TYPES:
    consultation_qa: "상담 Q&A 대화"
    chart_analysis: "명반 분석"
    life_guidance: "인생 조언"
    timing_advice: "시기 판단"
```

<div align="center">

### ⚡ CELESTIAL DATA ⚡

<img src="https://img.shields.io/badge/SAMPLES-7,983-00FFFF?style=for-the-badge&logo=stars&logoColor=black"/>
<img src="https://img.shields.io/badge/DOMAIN-ZIWEI-FF0080?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/PALACES-12-00FF41?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/STARS-108-FFFF00?style=for-the-badge&logoColor=black"/>

</div>

---

<div align="center">

## 💻 QUICK START 💻

</div>

```python
from datasets import load_dataset

# 자미두수 상담 데이터 로드
ds = load_dataset("tellang/yeji-jami-consultation")
print(f"Loaded: {len(ds['train']):,} samples")  # 7,983

# 상담 Q&A 샘플
sample = ds['train'][0]
print(f"Question: {sample['instruction']}")
print(f"Analysis: {sample['output']}")

# 자미두수 AI 학습에 활용
# - 명반 해석 패턴 학습
# - 12궁 분석 능력 향상
# - 상담 스타일 습득
```

---

<div align="center">

## 🔗 12 PALACES 🔗

</div>

<table>
<tr>
<td width="25%" align="center">

#### 命宮
Life Palace

</td>
<td width="25%" align="center">

#### 財帛宮
Wealth Palace

</td>
<td width="25%" align="center">

#### 官祿宮
Career Palace

</td>
<td width="25%" align="center">

#### 夫妻宮
Marriage Palace

</td>
</tr>
<tr>
<td width="25%" align="center">

#### 遷移宮
Travel Palace

</td>
<td width="25%" align="center">

#### 福德宮
Fortune Palace

</td>
<td width="25%" align="center">

#### 田宅宮
Property Palace

</td>
<td width="25%" align="center">

#### 子女宮
Children Palace

</td>
</tr>
</table>

---

<div align="center">

## 🌐 NETWORK CONNECTIONS 🌐

<img src="https://huggingface.co/datasets/tellang/yeji-jami-consultation/resolve/main/assets/jami-f.gif" width="100">

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
@misc{yeji-jami2026,
  title   = {YEJI Jami: Ziwei Doushu Consultation Dataset},
  author  = {tellang},
  year    = {2026},
  publisher = {Hugging Face},
  url     = {https://huggingface.co/datasets/tellang/yeji-jami-consultation}
}
```

---

<div align="center">

### ⚡ SYSTEM MONITORING ⚡

```
> STATUS: STAR CHARTS LOADED
> SAMPLES: 7,983 CONSULTATIONS
> NEXT_MISSION: CELESTIAL AI TRAINING
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
