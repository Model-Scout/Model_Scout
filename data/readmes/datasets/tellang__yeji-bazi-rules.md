---
license: mit
task_categories:
  - text-generation
language:
  - ko
  - zh
tags:
  - fortune-telling
  - bazi
  - rules
  - rag
size_categories:
  - n<1K
---

<div align="center">

```
██████╗  █████╗ ███████╗██╗    ██████╗ ██╗   ██╗██╗     ███████╗███████╗
██╔══██╗██╔══██╗╚══███╔╝██║    ██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
██████╔╝███████║  ███╔╝ ██║    ██████╔╝██║   ██║██║     █████╗  ███████╗
██╔══██╗██╔══██║ ███╔╝  ██║    ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║
██████╔╝██║  ██║███████╗██║    ██║  ██║╚██████╔╝███████╗███████╗███████║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
```

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=35&duration=3000&pause=1000&color=FF6600&center=true&vCenter=true&width=600&lines=SYSTEM%3A+BAZI+RULES;DOCS%3A+51%2B;RAG+READY" alt="Matrix Typing"/>

</div>

---

<div align="center">

## ⚡ INTERPRETATION RULEBOOK ⚡

</div>

<img align="right" alt="Rules GIF" width="300" src="https://huggingface.co/datasets/tellang/yeji-bazi-rules/resolve/main/assets/rule-h.gif">

```bash
> ACCESS GRANTED: BAZI RULES
> TYPE: Interpretation Guidelines
> CLEARANCE LEVEL: PUBLIC
> DOCUMENTS: 51+
> USE CASE: RAG System
> STATUS: DEPLOYED
```

**🔬 MISSION:**  
사주팔자 해석 규칙 및 가이드라인

**🧠 COVERAGE:**  
십신, 용신, 격국, 대운 해석 규칙

**⚡ CAPTCHA:**  
<a href="https://huggingface.co/spaces/tellang/yeji-captcha">
<img src="https://img.shields.io/badge/%5B%20%5D%20YES%2C%20I%27M%20A%20ROBOT-VERIFY-00FF41?style=for-the-badge&logo=robot&logoColor=white"/>
</a>

<br clear="right"/>

---

<div align="center">

## 📊 RULE CATEGORIES 📊

<img src="https://huggingface.co/datasets/tellang/yeji-bazi-rules/resolve/main/assets/rule-s.gif" width="100">

</div>

```yaml
RULE_CATEGORIES:

  BASIC_CONCEPTS_기초:
    천간_지지: "Ten Stems & Twelve Branches"
    음양_오행: "Yin-Yang & Five Elements"
    합충형파: "Combinations & Clashes"
    
  INTERPRETATION_해석:
    십신_해석: "Ten Gods interpretation"
    용신_선정: "Favorable element selection"
    격국_분석: "Pattern classification"
    
  TIMING_시기:
    대운_분석: "Major luck cycles (10-year)"
    세운_분석: "Annual luck cycles"
    월운_분석: "Monthly influences"
    
  SPECIALIZED_전문:
    직업_적성: "Career aptitude"
    건강_운세: "Health patterns"
    인간_관계: "Relationship dynamics"
    재물_운세: "Wealth patterns"
```

<div align="center">

### ⚡ RAG SYSTEM READY ⚡

<img src="https://img.shields.io/badge/DOCUMENTS-51+-FF6600?style=for-the-badge&logo=bookstack&logoColor=white"/>
<img src="https://img.shields.io/badge/USE_CASE-RAG-00FFFF?style=for-the-badge&logoColor=black"/>
<img src="https://img.shields.io/badge/DOMAIN-BAZI-00FF41?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/FORMAT-MARKDOWN-FF0080?style=for-the-badge&logoColor=white"/>

</div>

---

<div align="center">

## 💻 QUICK START 💻

</div>

```python
from datasets import load_dataset

# 규칙 문서 로드
ds = load_dataset("tellang/yeji-bazi-rules")

# RAG 시스템에 임베딩
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# 문서 청킹 및 벡터화
texts = [doc['content'] for doc in ds['train']]
vectorstore = FAISS.from_texts(texts, OpenAIEmbeddings())

# 관련 규칙 검색
query = "식신이 많으면 어떤 성격인가요?"
relevant_rules = vectorstore.similarity_search(query, k=3)
```

---

<div align="center">

## 🔗 RULE EXAMPLES 🔗

</div>

<table>
<tr>
<td width="50%">

#### 📖 십신 해석 규칙
```
비겁(比劫): 자아, 경쟁
식상(食傷): 표현, 창의
재성(財星): 재물, 욕망
관성(官星): 직업, 규율
인성(印星): 학문, 보호
```

</td>
<td width="50%">

#### 📖 오행 상생상극
```
상생: 木→火→土→金→水→木
상극: 木→土→水→火→金→木
```

</td>
</tr>
</table>

---

<div align="center">

## 🌐 NETWORK CONNECTIONS 🌐

<img src="https://huggingface.co/datasets/tellang/yeji-bazi-rules/resolve/main/assets/rule-f.gif" width="100">

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
@misc{yeji-bazi-rules2026,
  title   = {YEJI BaZi Rules: Interpretation Guidelines for RAG},
  author  = {tellang},
  year    = {2026},
  publisher = {Hugging Face},
  url     = {https://huggingface.co/datasets/tellang/yeji-bazi-rules}
}
```

---

<div align="center">

### ⚡ SYSTEM MONITORING ⚡

```
> STATUS: RULES DOCUMENTED
> DOCUMENTS: 51+ GUIDELINES
> NEXT_MISSION: RAG INTEGRATION
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
