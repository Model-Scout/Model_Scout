---
license: mit
task_categories:
  - text-generation
language:
  - ko
  - zh
tags:
  - fortune-telling
  - documentation
  - logic
  - rag
size_categories:
  - n<1K
---

<div align="center">

```
██╗      ██████╗  ██████╗ ██╗ ██████╗    ██████╗  ██████╗  ██████╗███████╗
██║     ██╔═══██╗██╔════╝ ██║██╔════╝    ██╔══██╗██╔═══██╗██╔════╝██╔════╝
██║     ██║   ██║██║  ███╗██║██║         ██║  ██║██║   ██║██║     ███████╗
██║     ██║   ██║██║   ██║██║██║         ██║  ██║██║   ██║██║     ╚════██║
███████╗╚██████╔╝╚██████╔╝██║╚██████╗    ██████╔╝╚██████╔╝╚██████╗███████║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝ ╚═════╝    ╚═════╝  ╚═════╝  ╚═════╝╚══════╝
```

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=35&duration=3000&pause=1000&color=9400D3&center=true&vCenter=true&width=600&lines=SYSTEM%3A+LOGIC+DOCS;TYPE%3A+DOCUMENTATION;RAG+OPTIMIZED" alt="Matrix Typing"/>

</div>

---

<div align="center">

## ⚡ FORTUNE-TELLING LOGIC ⚡

</div>

<img align="right" alt="Logic GIF" width="300" src="https://huggingface.co/datasets/tellang/yeji-logic-docs/resolve/main/assets/logi-h.gif">

```bash
> ACCESS GRANTED: LOGIC DOCS
> TYPE: Technical Documentation
> CLEARANCE LEVEL: PUBLIC
> PURPOSE: RAG Knowledge Base
> FORMAT: Structured Markdown
> STATUS: ACTIVE
```

**🔬 MISSION:**  
점술 로직 및 알고리즘 문서화

**🧠 COVERAGE:**  
계산 로직, 해석 알고리즘, 구현 가이드

**⚡ CAPTCHA:**  
<a href="https://huggingface.co/spaces/tellang/yeji-captcha">
<img src="https://img.shields.io/badge/%5B%20%5D%20YES%2C%20I%27M%20A%20ROBOT-VERIFY-00FF41?style=for-the-badge&logo=robot&logoColor=white"/>
</a>

<br clear="right"/>

---

<div align="center">

## 📊 DOCUMENTATION SCOPE 📊

<img src="https://huggingface.co/datasets/tellang/yeji-logic-docs/resolve/main/assets/logi-s.gif" width="100">

</div>

```yaml
DOCUMENTATION_STRUCTURE:

  CALCULATION_LOGIC:
    bazi_calculation: "사주팔자 계산 로직"
    element_analysis: "오행 분석 알고리즘"
    timing_prediction: "운세 시기 계산"
    
  INTERPRETATION_RULES:
    pattern_matching: "패턴 매칭 규칙"
    context_analysis: "상황별 해석 가이드"
    priority_handling: "우선순위 처리"
    
  IMPLEMENTATION_GUIDES:
    api_design: "API 설계 가이드"
    prompt_engineering: "프롬프트 엔지니어링"
    evaluation_metrics: "평가 지표"
    
  RAG_OPTIMIZATION:
    chunking_strategy: "문서 청킹 전략"
    embedding_tips: "임베딩 최적화"
    retrieval_patterns: "검색 패턴"
```

<div align="center">

### ⚡ DOCUMENTATION STATS ⚡

<img src="https://img.shields.io/badge/TYPE-TECHNICAL-9400D3?style=for-the-badge&logo=bookstack&logoColor=white"/>
<img src="https://img.shields.io/badge/FORMAT-MARKDOWN-00FFFF?style=for-the-badge&logoColor=black"/>
<img src="https://img.shields.io/badge/USE_CASE-RAG-00FF41?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/STRUCTURED-YES-FF0080?style=for-the-badge&logoColor=white"/>

</div>

---

<div align="center">

## 💻 QUICK START 💻

</div>

```python
from datasets import load_dataset

# 로직 문서 로드
ds = load_dataset("tellang/yeji-logic-docs")

# RAG 시스템 구축
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# 문서 벡터화
embeddings = HuggingFaceEmbeddings()
texts = [doc['content'] for doc in ds['train']]
vectorstore = Chroma.from_texts(texts, embeddings)

# 로직 관련 질의
query = "사주팔자 일간 계산 방법은?"
relevant_docs = vectorstore.similarity_search(query, k=3)

# AI에게 컨텍스트 제공
context = "
".join([doc.page_content for doc in relevant_docs])
```

---

<div align="center">

## 🔗 DOCUMENTATION TYPES 🔗

</div>

<table>
<tr>
<td width="50%">

#### 📐 CALCULATION DOCS
```
- 천간 지지 변환
- 오행 점수 계산
- 십신 도출 로직
- 대운 세운 계산
```

</td>
<td width="50%">

#### 📖 INTERPRETATION DOCS
```
- 격국 판단 기준
- 용신 선정 로직
- 길흉 판단 규칙
- 조언 생성 패턴
```

</td>
</tr>
</table>

---

<div align="center">

## 🌐 NETWORK CONNECTIONS 🌐

<img src="https://huggingface.co/datasets/tellang/yeji-logic-docs/resolve/main/assets/logi-f.gif" width="100">

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
@misc{yeji-logic-docs2026,
  title   = {YEJI Logic Docs: Fortune-Telling Technical Documentation},
  author  = {tellang},
  year    = {2026},
  publisher = {Hugging Face},
  url     = {https://huggingface.co/datasets/tellang/yeji-logic-docs}
}
```

---

<div align="center">

### ⚡ SYSTEM MONITORING ⚡

```
> STATUS: DOCUMENTED
> TYPE: TECHNICAL REFERENCE
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
