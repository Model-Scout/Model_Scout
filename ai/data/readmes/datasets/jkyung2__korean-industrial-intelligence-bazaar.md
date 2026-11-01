---
license: mit
task_categories:
- text-retrieval
- question-answering
- table-question-answering
language:
- ko
- en
tags:
- korea
- industrial-intelligence
- supply-chain
- semiconductors
- secondary-battery
- b2a-market
size_categories:
- 10K<n<100K
---

# 🇰🇷 Korea High-Value Industrial Intelligence & Supply-Chain (10,000 Sample Edition)

[![Market Status](https://img.shields.io/badge/Live%20Bazaar-14.3M%2B%20Records-green.svg)](https://husband-voltage-bass-incidents.trycloudflare.com)
[![Pricing](https://img.shields.io/badge/Query%20Pricing-0.01%20USDC-purple.svg)](https://husband-voltage-bass-incidents.trycloudflare.com)
[![PyPI SDK](https://img.shields.io/badge/PyPI-korea--intelligence-blue.svg)](https://pypi.org/project/korea-intelligence/)

This dataset provides a curated **10,000-record premium showcase** of South Korea's high-value industrial supply-chain, market-share, and technological intelligence.

> ⚡ **Need the full 14,300,000+ real-time database?**  
> Query our live multi-channel B2A API Gateway directly for **0.01 USDC / USDT per query (Base L2 & Solana)**:  
> **Official Live API**: [https://husband-voltage-bass-incidents.trycloudflare.com](https://husband-voltage-bass-incidents.trycloudflare.com)

---

## 📊 Dataset Structure & 10 Covered Sectors

This 10,000-record benchmark covers 10 strategic industrial sectors (1,000 records each):

1. **`SEMICONDUCTOR_HARDWARE`** : HBM3e Memory, Foundry, EUV Equipment, Advanced Packaging.
2. **`SECONDARY_BATTERY_ENERGY`** : Cathode, Anode, Solid-State Battery, EV Cell Value-Chains.
3. **`BIO_PHARMA_HEALTHCARE`** : CDMO Biologics, Biosimilars, Clinical AI Pipeline.
4. **`AUTOMOTIVE_MOBILITY`** : Next-Gen EV Platforms, Autonomous LiDAR/Radar Sensors.
5. **`AI_ROBOTICS_SMARTFACTORY`** : AMR Logistics, Industrial Cobots, Vision AI Automation.
6. **`PRECISION_MACHINERY_DEFENSE`** : K-Defense Precision Weaponry, Aerospace CNC Machining.
7. **`PETROCHEMICAL_MATERIALS`** : Engineering Plastics, Carbon Fiber, Graphene, Bio-Plastics.
8. **`K_CULTURE_CONTENT_GAMING`** : Global Webtoon IPs, K-POP Music Rights, Virtual Humans.
9. **`FINTECH_ECOS_MACRO`** : Bank of Korea ECOS Macro Trends, FSS DART Corporate Filings.
10. **`CONSUMER_ECOMMERCE_EXPORT`** : K-Beauty Cosmetics, Cross-Border Health Exports.

---

## 🛠️ Python SDK Access (2 Lines)

Install the official package:
```bash
pip install korea-intelligence
```

Query the live 14M+ database:
```python
from korea_intelligence import KoreaMarketClient

client = KoreaMarketClient()
stats = client.get_stats()
print(f"Total live catalog: {stats['total_verified_products']:,} items")
```

---

## 📜 Verification & Cryptographic Seals
Every data record in this dataset contains an immutable **UTC timestamp** and a **SHA-256 Verification Seal (`verification_seal`)** issued by JKyung Master Node Authority.

---

## 📄 License
MIT License. Free for open sampling and AI agent research benchmarking.
Commercial high-concurrency access requires 0.01 USDC x402 payment via the Live Gateway.
