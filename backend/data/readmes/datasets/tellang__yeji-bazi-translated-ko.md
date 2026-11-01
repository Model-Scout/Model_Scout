---
license: mit
task_categories:
  - text-generation
  - translation
language:
  - ko
  - zh
tags:
  - fortune-telling
  - bazi
  - translation
  - chinese-to-korean
size_categories:
  - 100K<n<1M
---

<div align="center">

```
██████╗  █████╗ ███████╗██╗    ████████╗██████╗  █████╗ ███╗   ██╗███████╗
██╔══██╗██╔══██╗╚══███╔╝██║    ╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝
██████╔╝███████║  ███╔╝ ██║       ██║   ██████╔╝███████║██╔██╗ ██║███████╗
██╔══██╗██╔══██║ ███╔╝  ██║       ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║
██████╔╝██║  ██║███████╗██║       ██║   ██║  ██║██║  ██║██║ ╚████║███████║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
```

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=35&duration=3000&pause=1000&color=FF0080&center=true&vCenter=true&width=600&lines=SYSTEM%3A+BAZI+TRANSLATED;SAMPLES%3A+262%2C980;ZH+→+KO+TRANSLATION" alt="Matrix Typing"/>

</div>

---

<div align="center">

## ⚡ MASSIVE TRANSLATION CORPUS ⚡

</div>

<img align="right" alt="Translation GIF" width="300" src="https://huggingface.co/datasets/tellang/yeji-bazi-translated-ko/resolve/main/assets/bazi-h.gif">

```bash
> ACCESS GRANTED: BAZI TRANSLATED
> TYPE: ZH→KO Translation Dataset
> CLEARANCE LEVEL: PUBLIC
> TOTAL SAMPLES: 262,980
> LANGUAGE PAIR: Chinese → Korean
> STATUS: ACTIVE
```

**🔬 MISSION:**  
중국어 사주팔자 데이터의 한국어 번역

**🧠 COVERAGE:**  
명리학 전문 용어, 해석 패턴, 상담 대화

**⚡ CAPTCHA:**  
<a href="https://huggingface.co/spaces/tellang/yeji-captcha">
<img src="https://img.shields.io/badge/%5B%20%5D%20YES%2C%20I%27M%20A%20ROBOT-VERIFY-00FF41?style=for-the-badge&logo=robot&logoColor=white"/>
</a>

<br clear="right"/>

---

<div align="center">

## 📊 TRANSLATION STATS 📊

<img src="https://huggingface.co/datasets/tellang/yeji-bazi-translated-ko/resolve/main/assets/bazi-s.gif" width="100">

</div>

```yaml
TRANSLATION_ANALYSIS:

  TOTAL_SAMPLES: 262,980
  
  CONTENT_TYPES:
    명리_해석: "사주팔자 분석 및 해설"
    운세_예측: "시기별 운세 및 조언"
    상담_대화: "Q&A 형식 상담 내용"
    용어_설명: "명리학 전문 용어 해설"
    
  QUALITY_METRICS:
    translation_model: "Qwen 2.5"
    review_status: "Automated QA"
    terminology_consistency: "HIGH"
    
  SOURCE:
    original_language: "Chinese (Simplified)"
    target_language: "Korean"
    domain: "Traditional Fortune-Telling"
```

<div align="center">

### ⚡ DATA STATS ⚡

<img src="https://img.shields.io/badge/SAMPLES-262K+-FF0080?style=for-the-badge&logo=database&logoColor=white"/>
<img src="https://img.shields.io/badge/ZH→KO-TRANSLATION-00FFFF?style=for-the-badge&logoColor=black"/>
<img src="https://img.shields.io/badge/DOMAIN-BAZI-00FF41?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/QUALITY-VERIFIED-FF6600?style=for-the-badge&logoColor=white"/>

</div>

---

<div align="center">

## 💻 QUICK START 💻

</div>

```python
from datasets import load_dataset

# 번역 데이터 로드
ds = load_dataset("tellang/yeji-bazi-translated-ko")
print(f"Loaded: {len(ds['train']):,} samples")  # 262,980

# 샘플 확인 (중국어 원문 + 한국어 번역)
sample = ds['train'][0]
print(f"Chinese: {sample['instruction'][:100]}...")
print(f"Korean: {sample['output'][:100]}...")

# 한국어 사주 AI 학습에 활용
# - Fine-tuning용 instruction-output 페어
# - 명리학 전문 용어 학습
# - 해석 패턴 습득
```

---

<div align="center">

## 🔗 TRANSLATION PIPELINE 🔗

</div>

<table>
<tr>
<td width="33%" align="center">

#### 📥 SOURCE
```
Chinese BaZi Data
```
중국어 원본

</td>
<td width="33%" align="center">

#### ⚙️ PROCESS
```
Qwen 2.5 Translation
```
AI 번역 + QA

</td>
<td width="33%" align="center">

#### 📤 OUTPUT
```
Korean BaZi Data
```
한국어 번역본

</td>
</tr>
</table>

---

<div align="center">

## 🌐 NETWORK CONNECTIONS 🌐

<img src="https://huggingface.co/datasets/tellang/yeji-bazi-translated-ko/resolve/main/assets/bazi-f.gif" width="100">

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
@misc{yeji-bazi-translated2026,
  title   = {YEJI BaZi Translated: Chinese to Korean Fortune-Telling Corpus},
  author  = {tellang},
  year    = {2026},
  publisher = {Hugging Face},
  url     = {https://huggingface.co/datasets/tellang/yeji-bazi-translated-ko}
}
```

---

<div align="center">

### ⚡ SYSTEM MONITORING ⚡

```
> STATUS: TRANSLATION COMPLETE
> COVERAGE: 262,980 SAMPLES
> NEXT_MISSION: KOREAN AI TRAINING
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
