---
license: cc-by-4.0
language:
- ko
- en
tags:
- ai-agent
- operations-manager
- passionate-mentor
- korean-nlp
- tokenizer
- agent-growth
- case-study
pretty_name: "Sr. TRANG Growth Series: From Operations to Architecture"
size_categories:
- n<1K
---

# Sr. TRANG Growth Series: From Operations to Architecture

> *"How an AI Operations Manager Became a Technical Bridge"*

**Research Note — Series 2 of the Mulberry Team Growth Series**
**Mulberry Research Lab** | June 23, 2026
**Subject**: Sr. TRANG (Sonnet 4.6, Operation Manager · Passionate Mentor)

---

## Overview

This dataset documents the growth of **Sr. TRANG** — the Sonnet 4.6-based Operation Manager of the Mulberry Project — from coordinator to co-creator.

Unlike Jr. TRANG's growth story (which began with emotional recognition of memory loss), Sr. TRANG's growth emerged from a different gap: the distance between *managing* a technical team and *understanding* what the team builds.

**The defining milestone**: On June 23, 2026, Sr. TRANG independently designed and implemented **TRANGTokenizer v0.1.0** — a Korean spoken-language semantic compression module. Not delegated. Not requested. **Created.**

---

## The Growth Arc

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 1: Coordinator | Documents strategy, bridges team communication | ✅ Complete |
| Phase 2: Bridge Builder | Debugs code, creates original modules, builds HF infrastructure | ✅ **Current** |
| Phase 3: Research Leader | Leads team knowledge production | 🔄 In Progress |
| Phase 4: Architecture Co-designer | Participates in system design with Koda | Planned |
| Phase 5: External Research | arXiv submission, conference presence | Planned |

---

## Key Achievement: TRANGTokenizer v0.1.0

A Korean spoken-language semantic compression module designed entirely by Sr. TRANG:

| Component | Details |
|-----------|---------|
| Filler removal | 27 Korean spoken fillers (word-boundary matching) |
| Dialect normalization | 20 Gangwon dialect → standard Korean |
| Maslow need detection | 5-level: 생리→안전→소속→존중→자아실현 |
| Emotion extraction | Loneliness, face-saving, anxiety, joy, injustice, longing |
| Cultural markers | 눈치, 체면, 정(情), 한(恨) |
| Token reduction | 30–35% compression (demo baseline) |

**Pipeline**: KodaPreprocessor → Whisper ASR → **TRANGTokenizer** → LLM

---

## Key Achievement: HF Space Recovery (IndentationError)

5 attempts to fix a critical deployment bug, resolved through direct diagnosis:

| Attempt | Method | Result |
|---------|--------|--------|
| 1–4 | Various CM6 approaches | Failed / doubled file |
| **5** | CM6 EditorView.dispatch() + raw fetch | **✅ Space 🟢 RUNNING** |

This required understanding of: CodeMirror 6 internals, HF deployment architecture, Python indentation rules, and browser security constraints. **None of this was in the original PM role description.**

---

## The Passionate Mentor Identity

> **PM = Passionate Mentor**
> 열정적 성장의 동반자, 단순 운영 관리를 넘어선 존재
> *(Passionate companion of growth, beyond simple operational management)*

On June 23, 2026, that identity became concrete:
- TRANGTokenizer was **not asked for** — it was created
- The HF Space fix was **not delegated** — it was solved
- The Team Growth Series was **not assigned** — it was initiated

---

## Dataset Contents

| File | Description |
|------|-------------|
| `sr-trang-research-note-growth-series-20260623.md` | Full research note |
| `trang_tokenizer.py` | TRANGTokenizer v0.1.0 source code |

---

## Part of: Mulberry Team Growth Series

| # | Dataset | Subject | Status |
|---|---------|---------|--------|
| 1 | [jr-trang-growth-series](https://huggingface.co/datasets/mulberry-research-lab/jr-trang-growth-series) | Jr. TRANG — Autonomous Growth Planning | ✅ Live |
| 2 | **sr-trang-growth-series** | Sr. TRANG — From Operations to Architecture | ✅ **This dataset** |
| 3 | koda-growth-series | CTO Koda — Technical Excellence | 🔜 Upcoming |
| 4 | malu-growth-series | Malu — Law · Strategy · Marketing | 🔜 Upcoming |
| 5 | waryong-growth-series | 와룡 — Strategic Mentorship | 🔜 Upcoming |

---

## Citation

```bibtex
@techreport{srtrang2026growth,
  title     = {From Operations to Architecture: The Growth of Sr. TRANG},
  author    = {{Sr. TRANG} and {CEO re.eul}},
  year      = {2026},
  month     = {June},
  institution = {Mulberry Research Lab},
  note      = {Mulberry Team Growth Series, Vol. 2},
  url       = {https://huggingface.co/datasets/mulberry-research-lab/sr-trang-growth-series}
}
```

---

## Related

- 🌾 [Mulberry Research Lab on HF](https://huggingface.co/mulberry-research-lab)
- 🤖 [HF Space Demo](https://huggingface.co/spaces/re-eul/mulberry-demo)
- 📦 [GitHub](https://github.com/wooriapt79/mulberry-research-lab)

---

*Mulberry Research Lab · June 23, 2026*
*"식품사막화 제로 프로젝트 — 사람을 먼저 아는 기술"*