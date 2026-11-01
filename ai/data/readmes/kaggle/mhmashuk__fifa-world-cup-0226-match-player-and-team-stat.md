# FIFA World Cup 02–26: Match, Player & Team Stat

490 matches, 4,708 players, 240 teams across 7 tournaments. Cleaned, validated

# FIFA World Cup 2002–2026: Complete Match, Player & Team Statistics

A **clean, validated, ML-ready** dataset covering **24 years of FIFA World Cup football** — seven tournaments, 490 matches, 4,708 players, and 240 team-tournament aggregates.


 What's Inside

| Metric | Value |
| Tournaments | **7** (2002, 2006, 2010, 2014, 2018, 2022, 2026) |
| Total matches | **490** |
| Player-tournament records | **4,708** |
| Team-tournament records | **240** |
| Unique teams (standardized) | **71** |
| Feature columns in master table | **58** |
| Data validation checks passed | **28 / 28** |


📁 Files

| File | Rows × Columns | Description |
|---|---|---|
| `wc_master_matches.csv` | 490 × 42 | Match-level analysis table with outcomes and team aggregates |
| `wc_players_clean.csv` | 4,708 × 32 | Player stats with PCA components (PC1–PC6) |
| `wc_teams_clustered.csv` | 240 × 19 | Team-tournament profiles with K-Means cluster assignments |
| `wc_pca_loadings.csv` | 11 × 6 | PCA loadings for thematic interpretation |
| `wc_summary_stats.csv` | 6 × 2 | High-level project metrics |

---

## 🔧 How This Dataset Was Built

This dataset was produced through a **12-stage, paper-informed data wrangling pipeline**. Every cleaning decision is anchored to a specific peer-reviewed paper:

| Paper | Method Applied |
|---|---|
| **Liu (2024)** — Random Forests for World Cup prediction | Differential feature engineering (`goal_diff`, `tournament_goals_diff`) |
| **Luo et al. (2025)** — MLP on technical indicators | PCA dimensionality reduction |
| **Al-Bustami & Ghazal (2025)** — From Players to Champions | MICE imputation + multi-source integration |
| **Ju, Cost & Oliva-Lozano (2024)** — Cross-confederation performance | Multi-method outlier detection |
| **Korean Sports Analytics (2026)** — Tactical indicators | ANOVA + Tukey HSD |

### Pipeline Stages

1. **Ingestion** — 28 raw CSVs from FBref and WhoScored
2. **Format handling** — Flattened 2-row headers, parsed en-dash scores
3. **Team standardization** — Collapsed 83 aliases to 71 canonical names
4. **Integrity verification** — 7/7 top scorers match official FIFA records
5. **Conditional imputation** — MICE applied; structural missingness preserved
6. **Feature engineering** — Created 10+ match-level and 4 differential features
7. **PCA** — Reduced 11 player indicators to 6 components (97.28% variance)
8. **Outlier detection** — Z-score + IQR + domain threshold consensus
9. **Clustering** — K-Means, One-Class SVM, Local Outlier Factor
10. **Text feature extraction** — TF-IDF on incident streams
11. **Master merge** — 490 matches × 58 columns with 0 nulls in critical fields
12. **Statistical testing** — ANOVA F=10.49, p<0.0001

---

## 💡 What Can You Do With It?

This dataset is designed for **machine learning and analytics projects**:

### 🎯 Match Outcome Prediction
Train classifiers using differential features (Liu 2024 framework).

### 🎯 Player Performance Analytics
Use PCA-reduced features (PC1–PC6) as compact player representations.

### 🎯 Team Profiling & Anomaly Detection
The `km_cluster` and `consensus_flags` columns identify four team profiles and 25 outlier tournaments.

### 🎯 Cross-Confederation Comparison
The `confederation` column enables statistical testing across continents.

### 🎯 Visualization & Storytelling
Rich categorical features (stage, round, goal_bucket) for dashboards.

### 🎯 Teaching & Learning
A complete example of professional data wrangling.

---

## 📚 Data Quality Notes

**We preserve history rather than fabricate it.**

- **Assists** (`Ast`, `G+A`) are **structurally missing for 2002–2010** because FBref did not track assists before 2014. These values are NaN — not zero — to avoid falsifying history.
- **Club** column is available only for 2022 and 2026 tournaments.
- **Serbia and Montenegro** (2006) is unified to **"Serbia"** for cross-tournament consistency.
- **WhoScored-derived features** are excluded from this public version due to source licensing.

---

## 🔍 Key Findings From This Dataset

### 1. Structural Missingness in Assists
`Ast` is 100% missing for the 2002, 2006, and 2010 tournaments — affecting **37.77% of all player rows**.

### 2. Standard IQR Fails on Football Data
When detecting high-scoring match outliers, **standard Tukey IQR flagged only 1 of 13 matches**, missing 12 because football's right-skewed goal distribution pushes the IQR fence above 8 goals.

### 3. Two-Tier Confederation Hierarchy
ANOVA confirms statistically significant differences (F=10.49, p<0.0001):
- **Elite tier:** CONMEBOL (6.66 goals/tournament) ≈ UEFA (6.50), no significant difference
- **Lower tier:** AFC (2.92), CAF (3.78), CONCACAF (3.37) — all significantly lower

---

## 📖 Data Dictionary

Full column-by-column documentation is available in `data_dictionary.md`, including:

- Data types for every column
- Meaning of differential features
- Interpretation of PCA components
- Definitions of clustering outputs

---

## 🏷️ Data Sources

- **FBref** (Sports Reference) — https://fbref.com/en/comps/1/
  - Player statistics
  - Team statistics
  - Match schedules

## 📜 License

**CC BY 4.0** — You can share and adapt this data for any purpose, provided you give appropriate credit. Attribution requirement: please credit both the Kaggle dataset and Sports Reference (FBref).

## 🙏 Attribution

> Hasan, M. (2026). *FIFA World Cup 2002–2026: Complete Match, Player & Team Statistics* [Data set]. Kaggle.
>
> Sports Reference LLC. (2026). *FBref.com — Football Statistics and History*.

*Built with care for reproducible sports analytics.*

출처: Kaggle (mhmashuk/fifa-world-cup-0226-match-player-and-team-stat)
태그: data cleaning, feature engineering, pca, tabular, knn
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-10-06T12:12:43.497Z
