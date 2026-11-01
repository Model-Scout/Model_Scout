---
pretty_name: "Is K-Fashion Visually Distinct? Brand Selection & Analysis"
license: cc-by-4.0
language:
  - ko
  - en
tags:
  - fashion
  - vision-language
  - fashion-clip
  - cultural-analytics
  - k-fashion
  - reproducibility
size_categories:
  - 10K<n<100K
---

# Is "K-Fashion" Visually Distinct? — Brand Selection & Analysis Procedure
### 'K-패션'은 시각적으로 구별되는가 — 브랜드 선정 및 분석 절차 공개

A reproducible release for a study asking whether Korean fashion brands are
*visually distinguishable* from global brands under a fashion-specialized
vision model (**Fashion-CLIP**). **Original product images are NOT redistributed**
(copyright); we share **derived embeddings, metadata, the brand-selection record,
results, and all code** so the analysis is fully reproducible.

> 한국 브랜드 옷이 글로벌 브랜드 옷과 *시각적으로 구별되는가*를 패션 특화 AI(Fashion-CLIP)로
> 검증한 연구의 재현용 공개 자료입니다. **원본 이미지는 저작권상 비공개**, 대신 **임베딩·메타데이터·
> 브랜드 선정기록·결과·코드 전체**를 공개합니다.

---

## TL;DR — Findings
- Korean vs global brands are **not visually separable**: origin silhouette ≈ **0.02**
  (0 = fully mixed, 1 = fully separated); **not statistically significant** under a
  brand-level permutation test, with or without photo-format control, at every price tier.
- Clothes cluster by **individual brand**, not by nation.
- A first, dramatic "Korean brands don't use models" signal turned out to be a
  **sampling artifact** (4-brand sample); it vanished with a properly selected
  18-brand sample (both origins ~73% flat-lay).

## Research design
- **Origin × price-tier grid**: KR / GLOBAL × {SPA, Contemporary, Designer}, 3 brands per cell → **18 brands**.
- **~600 product images per brand** from Naver Shopping search API, 6 garment categories each (balanced).
- Total: **10,640 images** (KR 5,236 / GLOBAL 5,404).

### Brands (18)
| Tier | Korea (KR) | Global |
|---|---|---|
| SPA | 탑텐 TOPTEN, 스파오 SPAO, 에잇세컨즈 8seconds | 유니클로 UNIQLO, 자라 ZARA, H&M |
| Contemporary | 마뗑킴 MATIN KIM, 마르디메크르디 MARDI MERCREDI, 앤더슨벨 Andersson Bell | 코스 COS, 아크네스튜디오 Acne Studios, 아미 AMI Paris |
| Designer | 우영미 WOOYOUNGMI, 준지 JUUN.J, 아더에러 ADER ERROR | 메종마르지엘라 Maison Margiela, 꼼데가르송 Comme des Garçons, 질샌더 Jil Sander |

## Brand-selection procedure (LLM-assisted, reproducible)
The brand set was chosen with a transparent, bias-reducing pipeline (recorded in
`data/brand_selection_candidates.csv` and `brand_selection_final.csv`):
1. **Criteria fixed first** (before any LLM): origin definition; price-tier strata
   (to avoid confounding origin with segment); single brand (no multi-brand retailers);
   must be collectable on Naver (≥150 products).
2. **Independent LLM proposers (×3)** with different perspectives — *market share*,
   *editorial/critical*, *online/Gen-Z* — each proposed 4–5 brands per cell.
3. **Consensus** by vote count (brands proposed by multiple agents preferred).
4. **Verification**: factual existence / origin / single-brand checks, and
   **collectability** via Naver API product counts; ambiguous or low-yield brands dropped.
5. **Finalize** balanced 18, equal N per brand; full record kept for the appendix.

## Analysis pipeline
1. **Embed** each image with Fashion-CLIP (`patrickjohncyh/fashion-clip`, 512-d, L2-normalized, cosine).
2. **Photo-format control**: zero-shot classify *model* vs *flat-lay* product shots.
3. **Origin separability**: silhouette (cosine), nearest-neighbor cross-origin rate, centroid distance.
4. **Segment control**: repeat within each price tier.
5. **Significance**: bootstrap 95% CI + **brand-level permutation test** (shuffles which
   *brands* are KR/GLOBAL — the honest unit, since images within a brand are not independent).

## Files
- `data/brand_embeddings.parquet` — 10,640 × (brand, origin, tier, shot_type, e0…e511). **Reproduce all analysis from this; no images needed.**
- `data/brand_product_metadata.csv` — per-product metadata (image **URL**, category, price, mall, productId). *Control variables; images not included.*
- `data/brand_selection_candidates.csv` / `brand_selection_final.csv` — selection record (votes, Naver counts).
- `results/*.csv` — format-control, tier-control, significance summaries.
- `figures/*.png` — column/paper figures.
- `code/*.py` — collection + analysis scripts (Naver API key NOT included).

## Reproduce
```python
import pandas as pd, numpy as np
from sklearn.metrics import silhouette_score
df = pd.read_parquet("data/brand_embeddings.parquet")
X = df[[f"e{i}" for i in range(512)]].values
print(silhouette_score(X, df["origin"], metric="cosine"))  # ≈ 0.02
```
Full pipeline: see `code/` (collect → crop → embed/classify → tier → significance).

## License & ethics
- **Code**: MIT. **Derived data (embeddings, results, metadata)**: CC-BY-4.0.
- **Original images are NOT included/redistributed** (Naver listing copyright); only
  image URLs and derived 512-d vectors are shared. Data collected via the official
  Naver Shopping Search API for non-commercial research.
- Model: Fashion-CLIP (`patrickjohncyh/fashion-clip`).

## Limitations
- Single embedding model (Fashion-CLIP); cross-model + human-rater validation recommended.
- Images from a marketplace (resellers), not official brand channels.
- The "Hallyu halo / spillover" reading is an interpretation/hypothesis, not tested here.

## Sources & attribution (출처 표기)
- **Model — Fashion-CLIP**: Chia, P. J., et al. (2022). "Contrastive language and vision
  learning of general fashion concepts." *Scientific Reports*, 12, 18958.
  Model weights: [`patrickjohncyh/fashion-clip`](https://huggingface.co/patrickjohncyh/fashion-clip).
  Used as-is (no fine-tuning by us).
- **Data, brand study (this release)**: collected via the **Naver Shopping Search Open API**
  (search.naver.com), June 2026, for non-commercial research. Only image URLs + derived
  embeddings are shared; original images are **not** redistributed.
- **Data, style study (companion, NOT in this release)**: AI-Hub 'K-Fashion 이미지' dataset,
  built with support of the Ministry of Science and ICT & NIA, Korea (aihub.or.kr).
  본 연구는 과학기술정보통신부·한국지능정보사회진흥원(NIA)의 지원으로 구축된 'K-Fashion 이미지'
  데이터(AI-Hub)를 활용하였다.

## Citation
```
Kim, Habin (2026). Is "K-Fashion" Visually Distinct? Brand Selection & Analysis.
Hugging Face dataset. (column: 「김하빈의 스몰데이터」)

Model: Chia, P.J., et al. (2022). Contrastive language and vision learning of
general fashion concepts. Scientific Reports, 12, 18958.
```
