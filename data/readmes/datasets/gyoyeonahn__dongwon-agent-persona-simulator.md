---
pretty_name: "Dongwon Agent-based Persona Simulator"
tags:
  - marketing
  - simulation
  - persona
  - agent-based
  - demand-forecasting
  - time-series
  - competition
language:
  - ko
  - en
license: "cc-by-nc-nd-4.0"
task_categories:
  - tabular-classification
  - time-series-forecasting
---


# MiriMarket — LLM-based Consumer Persona Simulation  
Dongwon X KAIST AI Competition (Award-winning Project)

## 🔍 Overview
MiriMarket는 새로운 제품을 출시하기 전에  
실존 소비자들이 어떤 반응을 보일지 **LLM 기반 가상 소비자(Persona) 시뮬레이션**을 통해  
수요를 예측하는 시스템입니다.

Dongwon X KAIST AI Competition에서 개발되었으며,  
제품 기획 / 마케팅 / 타겟 세그먼트 전략 수립을 위해 설계되었습니다.

---

## ✨ Key Features
- LLM 기반 가상 소비자 생성 (Adult / Health-conscious / Convenience / B2B 등)
- Persona-specific 시장 반응(선호/구매의향/Flavor 선택) 시뮬레이션
- Monte Carlo 기반 다회 샘플링
- Bass Diffusion 기반 조기 수요 예측
- Streamlit 대시보드 가능 (선택)

---

## 🧠 System Architecture

```plaintext
Product Idea
│
├── PromptManager
│     ├─ segment-specific persona templates
│     └─ product briefing → persona reaction
│
├── Persona Generator (LLM)
│     └─ synthetic consumers (100~200 samples)
│
├── Persona Reaction Simulator
│     ├─ flavor preference
│     ├─ purchase intention
│     └─ NPS/emotional response
│
└── Market Forecast Engine
      ├─ Monte Carlo sampling
      └─ Bass diffusion (optional)
```

---

## 📊 Example Output
- Persona distribution  
- Flavor preference prediction  
- 시나리오별 수요 변화 그래프(옵션)  

---

## 📁 Repository Structure
```
/src
    /persona_generator
    /prompt_manager
    /simulator
/notebooks
    - analysis.ipynb
/data
    - sample_personas.json (경량 샘플)
/README.md
```

---

## 📌 License
**CC-BY-NC-4.0** (비영리 사용만 허용됩니다)

---

## 🏆 Awards
Dongwon X KAIST AI Competition — 장려상 수상  
팀장 역할 + 전체 파이프라인 제작
