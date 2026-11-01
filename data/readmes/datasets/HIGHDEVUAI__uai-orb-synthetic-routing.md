---
license: apache-2.0
task_categories:
  - text-classification
language:
  - ko
  - en
---

# UAI Orb synthetic routing labels

Design-hypothesis labels (`SOLO` / `COUNCIL` / `RELAY`) for synthetic and golden eval prompts. **No user conversations.** Not a human gold set.

Live chat (2026-09-05) uses an explicit Orb menu including **RACE**. RACE is not a label in this dataset. Production routing is Cloudflare Workers AI incumbents (GLM-5.3-flash SOLO, GLM-5.3 agent, DeepSeek V4 Pro / Kimi K2.7 satellites). This classifier stays off (`FEATURE_ORB_ROUTER`).
