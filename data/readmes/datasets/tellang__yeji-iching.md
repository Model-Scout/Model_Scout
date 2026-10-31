---
license: mit
task_categories:
  - text-generation
language:
  - ko
  - zh
tags:
  - fortune-telling
  - iching
  - divination
  - hexagrams
size_categories:
  - n<1K
---

<div align="center">

```
██╗ ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗      ██████╗ ██╗  ██╗
██║██╔════╝██║  ██║██║████╗  ██║██╔════╝     ██╔════╝ ██║  ██║
██║██║     ███████║██║██╔██╗ ██║██║  ███╗    ███████╗ ███████║
██║██║     ██╔══██║██║██║╚██╗██║██║   ██║    ██╔═══██╗╚════██║
██║╚██████╗██║  ██║██║██║ ╚████║╚██████╔╝    ╚██████╔╝     ██║
╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝      ╚═╝
```

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=35&duration=3000&pause=1000&color=FFFF00&center=true&vCenter=true&width=600&lines=SYSTEM%3A+I+CHING;HEXAGRAMS%3A+64;ANCIENT+WISDOM" alt="Matrix Typing"/>

</div>

---

<div align="center">

## ⚡ 64 HEXAGRAMS DECODED ⚡

</div>

<img align="right" alt="I Ching GIF" width="300" src="https://huggingface.co/datasets/tellang/yeji-iching/resolve/main/assets/ichi-h.gif">

```bash
> ACCESS GRANTED: YEJI I CHING
> TYPE: Hexagram Reference System
> CLEARANCE LEVEL: PUBLIC
> HEXAGRAMS: 64 (Complete Set)
> TRADITION: 周易 (Zhou Yi)
> STATUS: COMPLETE
```

**🔬 MISSION:**  
주역 64괘 완전 해설 레퍼런스

**🧠 COVERAGE:**  
괘상, 괘사, 효사, 현대 해석

**⚡ CAPTCHA:**  
<a href="https://huggingface.co/spaces/tellang/yeji-captcha">
<img src="https://img.shields.io/badge/%5B%20%5D%20YES%2C%20I%27M%20A%20ROBOT-VERIFY-00FF41?style=for-the-badge&logo=robot&logoColor=white"/>
</a>

<br clear="right"/>

---

<div align="center">

## 📊 HEXAGRAM STRUCTURE 📊

<img src="https://huggingface.co/datasets/tellang/yeji-iching/resolve/main/assets/ichi-s.gif" width="100">

</div>

```yaml
HEXAGRAM_SYSTEM:

  TRIGRAMS_八卦:
    乾_천: "☰ Heaven (Creative)"
    坤_지: "☷ Earth (Receptive)"
    震_뇌: "☳ Thunder (Arousing)"
    巽_풍: "☴ Wind (Gentle)"
    坎_수: "☵ Water (Abysmal)"
    離_화: "☲ Fire (Clinging)"
    艮_산: "☶ Mountain (Keeping Still)"
    兌_택: "☱ Lake (Joyous)"
    
  HEXAGRAMS_64卦:
    total: 64
    combinations: "8 × 8 trigrams"
    lines_per_hexagram: 6
    
  CONTENT_PER_HEXAGRAM:
    괘명: "Hexagram name (Korean/Chinese)"
    괘상: "Hexagram symbol"
    괘사: "Judgment text"
    효사: "Line texts (6 lines)"
    해석: "Modern interpretation"
```

<div align="center">

### ⚡ ANCIENT WISDOM ⚡

<img src="https://img.shields.io/badge/HEXAGRAMS-64-FFFF00?style=for-the-badge&logo=yin-yang&logoColor=black"/>
<img src="https://img.shields.io/badge/TRIGRAMS-8-00FFFF?style=for-the-badge&logoColor=black"/>
<img src="https://img.shields.io/badge/TRADITION-3000+_YEARS-00FF41?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/STATUS-COMPLETE-FF6600?style=for-the-badge&logoColor=white"/>

</div>

---

<div align="center">

## 💻 QUICK START 💻

</div>

```python
from datasets import load_dataset

# 64괘 데이터 로드
ds = load_dataset("tellang/yeji-iching")

# 특정 괘 조회
hexagram_1 = ds['train'][0]  # 乾卦 (건괘)
print(f"괘명: {hexagram_1['name']}")
print(f"괘상: {hexagram_1['symbol']}")
print(f"괘사: {hexagram_1['judgment']}")

# RAG 시스템용 레퍼런스로 활용
# - 괘 해석 검색
# - 상황별 조언 매칭
# - 점술 AI 지식 베이스
```

---

<div align="center">

## 🔗 SAMPLE HEXAGRAMS 🔗

</div>

<table>
<tr>
<td width="33%" align="center">

#### ☰ 乾 (건)
```
═══
═══
═══
```
**Heaven / Creative**
원형이정 (元亨利貞)

</td>
<td width="33%" align="center">

#### ☷ 坤 (곤)
```
= =
= =
= =
```
**Earth / Receptive**
이빈마지정 (利牝馬之貞)

</td>
<td width="33%" align="center">

#### ☵ 坎 (감)
```
= =
═══
= =
```
**Water / Abysmal**
습감유부 (習坎有孚)

</td>
</tr>
</table>

---

<div align="center">

## 🌐 NETWORK CONNECTIONS 🌐

<img src="https://huggingface.co/datasets/tellang/yeji-iching/resolve/main/assets/ichi-f.gif" width="100">

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
@misc{yeji-iching2026,
  title   = {YEJI I Ching: Complete 64 Hexagrams Reference},
  author  = {tellang},
  year    = {2026},
  publisher = {Hugging Face},
  url     = {https://huggingface.co/datasets/tellang/yeji-iching}
}
```

---

<div align="center">

### ⚡ SYSTEM MONITORING ⚡

```
> STATUS: ANCIENT WISDOM DIGITIZED
> HEXAGRAMS: ALL 64 COMPLETE
> NEXT_MISSION: DIVINATION AI REFERENCE
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
