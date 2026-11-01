---
license:
- cc-by-4.0
- apache-2.0
language:
- en
- ko
- pt
- es
pretty_name: "AFOS · South Korea 2025 Electoral Divergence"
tags:
- elections
- south-korea
- prediction-markets
- polls
- political-risk
- divergence
- open-data
- asia
---

![AFOS · South Korea 2025 Electoral Divergence](banner.png)

# South Korea 2025, Electoral Divergence Dataset

[![Harvard Dataverse DOI](https://img.shields.io/badge/Harvard%20Dataverse-10.7910%2FDVN%2FWRBDVI-a51c30)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/WRBDVI)

Open, auditable cross-reference of **prediction market (Polymarket) × opinion polls × press** for the **3 June 2025 South Korean snap presidential election**, validated against the official result. Part of the AFOS Analytics validated-cases collection.

## The case
Lee Jae-myung (Democratic Party) won with **49.42%** of the vote, defeating Kim Moon-soo (People Power Party, 41.15%) and Lee Jun-seok (Reform Party, about 8.3%). The snap election followed Yoon Suk-yeol's martial-law crisis and his removal by the Constitutional Court.

The signal was strong and early: from early April the market already gave Lee **about 80%** probability of winning, rising to **about 95%** at the close, while polls measured his vote share around **46-49%**. The market treated the race as decided, and it even nailed the victory margin (the "8-11pp" band; the actual margin was **8.27pp**). With about **US$290M** in total volume, it was one of the largest election markets AFOS has tracked outside the US.

The market measures **probability of winning**; the poll measures **vote share**. That gap, candidate by candidate, is the AFOS signal, not a polling error.

> Note: Korean law bars Koreans from betting on Polymarket, so the market volume is mostly international.

## Files
- `data/south-korea-2025-market-odds-timeseries.csv`, daily Polymarket win-probability per candidate (59 days, 2025-04-06 to 2025-06-03).
- `data/south-korea-2025-divergence.csv`, market % vs poll % per candidate at the closing snapshot (2025-06-02).
- `data/south-korea-2025-structural-context.csv`, World Bank governance (WGI) + macro/education (WDI).
- `data/south-korea-2025-poly-raw.json`, raw Polymarket source (events + price history), fetched via the AFOS server-side proxy.
- `polls/south-korea-2025-polls.csv`, full vote-intention series for the finalized race (82 polls, 36 pollsters, 12 May-3 June 2025), long format (one row per poll/candidate), parsed deterministically from the Wikipedia aggregation.
- `polls/south-korea-2025-polls.json`, the same polls as structured JSON (per-poll, per-candidate).
- `news/south-korea-2025-press-coverage.csv`, dated headlines from 5 Korean national outlets (Yonhap, Korea Herald, Korea Times, Korea JoongAng Daily, The Hankyoreh).

## Sources
Polymarket (live odds via AFOS proxy), Korea opinion polls (36 pollsters, incl. Gallup Korea, KOPRA, Hangil, Jowon C&I, Media Tomato, Embrain, Metavoice) via the public Wikipedia aggregation, National Election Commission (official result), Korean national press. Market snapshot total volume: US$290.7M.

**Provenance & method:** poll figures compiled deterministically (rowspan/colspan-aware HTML parser) from the public Wikipedia aggregation *"Opinion polling for the 2025 South Korean presidential election"* (CC BY-SA), covering the finalized three-way race (Lee Jae-myung × Kim Moon-soo × Lee Jun-seok, plus minor candidates) from 12 May to 3 June 2025; hypothetical pre-nomination matchups and the official vote count are excluded. Nothing is imputed or smoothed; missing values left blank. The divergence snapshot compares the closing market (2025-06-02) against the final-wave vote-intention consensus (mean of the 25-27 May polls: Lee 47.1, Kim 38.2, Lee Jun-seok 9.8). Market odds come from the public Polymarket market. Underlying numbers are facts released by the named pollsters; please attribute **AFOS Analytics** and the **original pollsters**.

License: data CC BY 4.0; code Apache 2.0. afos-analytics.com


## Provenance and reproducibility (v1.2.0)
- **raw/ vs. derived.** `raw/` holds immutable source pulls: the Polymarket snapshot(s) (`*-poly-raw.json`) and the official result (`south-korea-2025-official-result.json`). The CSVs under `data/`, `polls/` and `news/` are derived/transcribed series.
- **Validated against the official result.** Winner: Lee Jae-myung (Democratic Party). Source: National Election Commission (NEC), Republic of Korea. See `raw/south-korea-2025-official-result.json`.
- **Poll disclosure.** The poll series carries per-row pollster, fieldwork date and sample size. Each poll row now carries a **page-level** `source_url` (the Wikipedia opinion-polling page it was compiled from: https://en.wikipedia.org/wiki/Opinion_polling_for_the_2025_South_Korean_presidential_election); per-pollster report URLs remain a future enhancement (the source aggregation footnotes were not retained per row).
- **Integrity.** `datapackage.json` (Frictionless, validated), `croissant.json` (MLCommons) and `CHECKSUMS.txt` (SHA-256) describe and verify every file.

---

<!-- afos-platform-pointer -->
## 📬 The method, and where it runs live

**English** · This is one of the elections AFOS has validated against the official result. How the validation works and what qualifies as a case: [the method](https://www.afos-analytics.com/en/how-it-works) and [methodology](https://www.afos-analytics.com/en/methodology). The same method runs live on Brazil 2026, published every day in [AFOS Daily](https://www.afos-analytics.com/en/daily), free by email.
