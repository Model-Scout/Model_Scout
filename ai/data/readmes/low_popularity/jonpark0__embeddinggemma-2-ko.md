---
license: apache-2.0
base_model: google/embeddinggemma-2
base_model_relation: finetune
pipeline_tag: sentence-similarity
library_name: sentence-transformers
language:
- ko
- en
- multilingual
tags:
- embedding
- sentence-transformers
- sentence-similarity
- feature-extraction
- multimodal-embedding
- visual-document-retrieval
- korean
- retrieval
- matryoshka
datasets:
- NomaDamas/ko-vdr-train-public
- miracl/miracl
- castorini/mr-tydi
- Shitao/MLDR
- nlpai-lab/miracl-multilingual-triplets
- klue/klue
- PaDaS-Lab/webfaq
- rajpurkar/squad
- wikimedia/wikipedia
- qwer90qwer/health
---

# EmbeddingGemma 2 — Korean text and document-image retrieval fine-tune (v0.3)

[`google/embeddinggemma-2`](https://huggingface.co/google/embeddinggemma-2) with its text transformer fine-tuned on Korean retrieval data, now including Korean document pages as images. After each round of training the weights are interpolated back toward the previous version, so that the other abilities of the model are kept. It is a drop-in replacement: same architecture, same prompts, same 768-d space (128/256/512 Matryoshka truncation), same image/audio/video inputs.

[한국어 안내는 아래에 있습니다.](#한국어)

**Status:** v0.3 adds Korean document-page images to the training data: about 46k queries over 7.1k pages of Korean public documents ([Ko-VDR-Train-Public v2](https://huggingface.co/datasets/NomaDamas/ko-vdr-train-public)), plus 30k text rows from the earlier training data so that text retrieval holds. Korean document-image retrieval rises from 0.341 to 0.406 nDCG@10 on KoViDoRe v2 (all four tasks up, 95% confidence intervals above zero) and from 0.424 to 0.508 on SDS-KoPub-VDR. Korean text retrieval is 0.729 (v0.2: 0.726), and no image, speech or English check drops by more than 0.5 points; one Korean clustering task drops (see Limitations). The interpolation weight was settled after one look at the evaluation sets; see [How β was chosen](#how-β-was-chosen). The previous version stays available at revision [`v0.2`](https://huggingface.co/jonpark0/embeddinggemma-2-ko/tree/v0.2).

## Results

All numbers come from our own runs of all models with the same code (mteb 2.24.12, 768-d, full 8K context, bf16). They are not copied from other model cards and may differ from leaderboard setups. Changes are paired bootstrap 95% confidence intervals over queries.

### Korean document images: KoViDoRe v2, nDCG@10

Queries are Korean text; documents are page images, passed to the model as images only (no text prompt).

| Task | Base | v0.1 | v0.2 | v0.3 | v0.3 − v0.2 |
|---|---|---|---|---|---|
| KoVidore2HrRetrieval (221 queries) | 0.230 | 0.237 | 0.242 | 0.293 | +0.051 (+0.036 to +0.068) |
| KoVidore2EnergyRetrieval (173) | 0.414 | 0.438 | 0.431 | 0.522 | +0.091 (+0.068 to +0.115) |
| KoVidore2EconomicRetrieval (163) | 0.181 | 0.184 | 0.191 | 0.216 | +0.024 (+0.005 to +0.044) |
| KoVidore2CybersecurityRetrieval (149) | 0.502 | 0.503 | 0.500 | 0.592 | +0.093 (+0.067 to +0.119) |
| **Average** | **0.331** | **0.341** | **0.341** | **0.406** | **+0.065** |

At 256 dimensions the average goes from 0.287 (base), 0.293 (v0.1) and 0.297 (v0.2) to 0.367 (v0.3).

### Korean text retrieval: MTEB(kor, v2) retrieval tasks, nDCG@10

| Task | Base | v0.1 | v0.2 | v0.3 | v0.3 − v0.2 |
|---|---|---|---|---|---|
| MIRACLRetrieval | 0.640 | 0.657 | 0.669 | 0.672 | +0.002 (−0.005 to +0.010) |
| Ko-StrategyQA | 0.803 | 0.805 | 0.804 | 0.802 | −0.002 (−0.005 to +0.001) |
| LawIRKo | 0.561 | 0.576 | 0.608 | 0.625 | +0.017 (+0.014 to +0.020) |
| SQuADKorV1Retrieval | 0.889 | 0.895 | 0.893 | 0.892 | −0.001 (−0.003 to +0.000) |
| AutoRAGRetrieval | 0.798 | 0.801 | 0.811 | 0.804 | −0.007 (−0.021 to +0.007) |
| PublicHealthQA | 0.794 | 0.804 | 0.804 | 0.806 | +0.002 (−0.005 to +0.009) |
| BelebeleRetrieval | 0.935 | 0.934 | 0.934 | 0.934 | +0.000 (−0.003 to +0.003) |
| MultiLongDocRetrieval | 0.423 | 0.443 | 0.443 | 0.447 | +0.004 (−0.003 to +0.011) |
| MrTidyRetrieval | 0.542 | 0.555 | 0.567 | 0.575 | +0.008 (+0.000 to +0.016) |
| **Average** | **0.709** | **0.719** | **0.726** | **0.729** | **+0.003** |

At 256 dimensions the average goes from 0.693 (base), 0.703 (v0.1) and 0.710 (v0.2) to 0.714 (v0.3).

### Other modalities and languages

| Check | Metric | Base | v0.1 | v0.2 | v0.3 |
|---|---|---|---|---|---|
| SDS-KoPub-VDR (Korean document images) | nDCG@10 | 0.404 | 0.424 | 0.424 | 0.508 |
| MIRACL-Vision, Korean | nDCG@5 | 0.595 | 0.600 | 0.610 | 0.605 |
| XM3600, Korean captions → photos | Recall@10 | 0.906 | 0.914 | 0.917 | 0.920 |
| WIT, Korean | nDCG@10 | 0.592 | 0.614 | 0.611 | 0.614 |
| FLEURS, Korean text → speech (399 pairs) | Recall@1 | 0.970 | 0.962 | 0.972 | 0.970 |
| GoogleSVQ, Korean speech | Hit rate@5 | 0.582 | 0.580 | 0.582 | 0.581 |
| Belebele, English passages | Recall@1 | 0.906 | 0.917 | 0.918 | 0.914 |
| MTEB(kor, v2) non-retrieval tasks (11) | average | 0.676 | 0.685 | 0.673 | 0.672 |

SDS-KoPub-VDR at 256 dimensions: 0.379 (base), 0.392 (v0.1), 0.396 (v0.2), 0.482 (v0.3).

The text transformer is shared by all modalities (image and audio soft tokens pass through the same 24 layers), so any fine-tuning moves every modality. The interpolation weight was chosen to keep these checks within tolerance.

Non-retrieval tasks one by one (base → v0.1 → v0.2 → v0.3): KLUE-TC 0.570 → 0.573 → 0.563 → 0.562, SIB200 clustering 0.429 → 0.454 → 0.438 → 0.451, KlueMrcDomainClustering 0.826 → 0.846 → 0.733 → 0.742, KlueYnatMrcCategoryClustering 0.629 → 0.693 → 0.677 → **0.658**, KLUE-NLI 0.669 → 0.667 → 0.669 → 0.668, KorNLI 0.762 → 0.756 → 0.755 → 0.752, PAWS-X 0.487 → 0.487 → 0.491 → 0.490, MIRACL reranking 0.609 → 0.612 → 0.618 → 0.615, KLUE-STS 0.848 → 0.849 → 0.853 → 0.854, KorSTS 0.800 → 0.796 → 0.797 → 0.795, STS17 0.810 → 0.805 → 0.806 → 0.803.

## Usage

Requires `sentence-transformers>=6.1` and `transformers>=5.18`. Use it exactly like the base model:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("jonpark0/embeddinggemma-2-ko")

query = "서울에서 가장 높은 산은?"
document = "북한산은 서울 북부에 있는 산으로, 가장 높은 봉우리는 백운대다."

query_emb = model.encode(query, prompt_name="SearchQuery")    # "task: search result | query: ..."
doc_emb = model.encode(document, prompt_name="Document")       # "title: none | text: ..."
print(model.similarity(query_emb, doc_emb))
```

Document pages as images (this is how the KoViDoRe v2 and SDS-KoPub-VDR numbers above were measured):

```python
from PIL import Image

page = Image.open("page_017.png").convert("RGB")
page_emb = model.encode([{"image": page}])                     # image only, no text prompt
query_emb = model.encode("2026년 공무원 교육 예산은?", prompt_name="SearchQuery")
print(model.similarity(query_emb, page_emb))
```

- Documents with a real title: `model.encode(f"title: {title} | text: {body}")`.
- Text only (saves memory): `SentenceTransformer("jonpark0/embeddinggemma-2-ko", config_kwargs={"vision_config": None, "audio_config": None})`.
- Shorter vectors: `model.encode(..., truncate_dim=256, normalize_embeddings=True)`.
- Run in `bfloat16` or `float32`, never `float16` (same as the base model).
- Audio and video work as in the base model; see the [base model card](https://huggingface.co/google/embeddinggemma-2).
- Previous versions: `SentenceTransformer("jonpark0/embeddinggemma-2-ko", revision="v0.2")` (or `"v0.1"`).

## Training

v0.3 continues from v0.2. The v0.1 and v0.2 training data and recipe are described in the [v0.2 card](https://huggingface.co/jonpark0/embeddinggemma-2-ko/blob/v0.2/README.md).

**Data** (publicly licensed only):

| Source | License | Rows |
|---|---|---|
| [Ko-VDR-Train-Public v2](https://huggingface.co/datasets/NomaDamas/ko-vdr-train-public) (revision `3f03235`): Korean queries → pages of 45 Korean public documents from [data.go.kr](https://www.data.go.kr) | queries: CC BY 4.0; documents: "No Restrictions" (36) or KOGL Type 1 (9), see [Attribution](#attribution) | 45,978 queries, 7,111 pages |
| Text replay: rows of the v0.1 and v0.2 training data (with their negatives), sampled in proportion to source, English SQuAD included | as in the v0.2 card | 30,000 |

- **Queries.** Ko-VDR's queries were written and filtered by an LLM (Upstage Solar Pro 3) with the [kovidore-data-generator](https://github.com/whybe-choi/kovidore-data-generator) pipeline plus rule-based filters; the dataset card describes no human review. A page has about 41 queries on average; we kept a query only while one of its positive pages had fewer than 12 kept queries, which leaves 45,978. All seven query types (multi-hop, compare-contrast, open-ended, boolean, extractive, numerical, enumerative) and three formats (question, keyword, instruction) are kept.
- **Held-out documents.** Four whole documents, one per KoViDoRe v2 domain (HR, energy, economy, cybersecurity), were removed from training and used only for choosing β (581 queries, 385 pages).
- **Decontamination.** Training pages were compared with all 6,729 KoViDoRe v2 pages and a 1-in-4 sample (about 10k pages) of SDS-KoPub-VDR with a 256-bit difference hash. The match threshold was set from comparisons between different training documents before looking at the evaluation pages, and a document is removed when two or more of its pages match. No document was removed; three single training pages fell within the threshold and stayed. No training query equals or nearly equals (5-gram Jaccard ≥ 0.8) a query of KoViDoRe v2, SDS-KoPub-VDR or MIRACL-Vision. 72 page images that appear byte-identical under two different document names were removed from training and from the held-out set.
- **Page inputs.** The vision encoder and its projection were frozen, so each page's soft tokens (at most 280 per page, 270 on average) were computed once and reused; they enter the text transformer through the same path as at inference (checked: cosine ≥ 0.9999 against the normal image input).
- **Hard negatives.** Mined with v0.2 over all 7,111 training pages (TopK-PercPos: 3 per query, scoring below 0.95 × the positive).
- **What was trained.** Only the text transformer (kept in fp32), starting from v0.2's fp32 weights; the token embedding table and the vision and audio encoders were frozen.
- **Objective.** As in v0.2: CachedMultipleNegativesRankingLoss inside MatryoshkaLoss (768/512/256/128), batch 128 drawn from one source at a time, sources sampled proportionally; 1 epoch (601 steps, 4.2 hours on one GPU slice), learning rate 2e-5 with 10% linear warm-up, bf16 autocast.
- **Interpolation.** Final weights = v0.2 + β × (fine-tuned − v0.2) with β = 0.1875.

### How β was chosen

We first compared β ∈ {0.25, 0.5, 0.75, 1.0} on development sets: the four held-out documents for document images, held-out Korean and English text queries, and 1,347 FLEURS Korean training-split recordings for speech. The rule, fixed before training: Korean text, English and speech may each drop by at most 0.01 against v0.2, and among the values that pass, take the best document-image score (within 0.003, the smaller β). Larger β kept raising the document-image score (0.49 at β = 0.25, 0.53 at β = 0.5) but failed the speech check, so the rule picked β = 0.25.

On the evaluation sets above, β = 0.25 reached 0.423 on KoViDoRe v2 and kept text retrieval, but FLEURS Korean text → speech Recall@1 fell by 4 of 399 queries against v0.2, one query more than the 0.01 tolerance allows. Under the rules that was a failure, and we did not release it. We then added β = 0.125 and 0.1875 to the grid and reran the same rules: the development sets still chose 0.25, and the retry rule fixed before training (take the largest passing β below the one that failed) gave 0.1875, which passed every check and is this release.

The two added values were chosen after seeing evaluation results, so the evaluation sets have been looked at twice and the pass/fail outcome is post hoc. The comparisons against v0.2 in the tables do not depend on it: every KoViDoRe v2 task is above v0.2 with a 95% interval above zero, and the β we released scores lower on KoViDoRe v2 than the one we rejected. The document-image target set before training (KoViDoRe v2 average ≥ 0.40) is met with a margin of 0.006.

## Limitations

- **Matched training data.** Ko-VDR-Train-Public v2 was built with the same generator as KoViDoRe v2 (Korean public PDFs, LLM-written queries), so part of the KoViDoRe v2 gain reflects matched domain and query style. SDS-KoPub-VDR, a benchmark of Korean government documents built separately by another group ([arXiv 2511.04910](https://arxiv.org/abs/2511.04910)), rose by a similar amount (+0.083).
- **Machine-written queries.** The new training queries are LLM-generated and may differ from how people actually search.
- **Weakest task.** The economy task remains the weakest (0.216).
- **Speech.** Against v0.2, one FLEURS query that was found at rank 1 no longer is, and none was gained; at β = 0.25 four were lost and none gained. Document-image training nudges Korean text → speech retrieval down as β grows. GoogleSVQ did not move (0.582 → 0.581).
- **Clustering.** KlueYnatMrcCategoryClustering fell from 0.677 to 0.658. At 256 dimensions it fell from 0.700 (v0.2; base 0.675) to 0.619, and KlueMrcDomainClustering from 0.858 (v0.2; base 0.832) to 0.804. These tasks move by up to 0.09 between neighbouring interpolation weights, so they are unstable, but if you cluster Korean text with truncated vectors, compare with v0.2.

## License

Apache 2.0, the same as the base model ([Gemma 4 license](https://ai.google.dev/gemma/docs/gemma_4_license)). Training data licenses are listed above and in the v0.2 card: Ko-VDR-Train-Public v2 queries, WebFAQ and qwer90qwer/health are CC BY 4.0; KLUE and SQuAD are CC BY-SA 4.0; Wikipedia is CC BY-SA 3.0 / GFDL. Please credit them when you build on this model.

### Attribution

The page images come from Korean public documents published by government agencies and public institutions (via [data.go.kr](https://www.data.go.kr), 공공데이터포털). The full list of 49 documents in Ko-VDR-Train-Public v2, with license, link and how each was used, is in [`training_documents.csv`](training_documents.csv). Eleven are released under KOGL Type 1 (공공누리 제1유형: 출처표시), which requires attribution. The table follows the attribution given in the [Ko-VDR-Train-Public v2 card](https://huggingface.co/datasets/NomaDamas/ko-vdr-train-public):

이 모델은 아래 기관이 표의 연도에 작성하여 공공누리 제1유형으로 개방한 저작물을 학습과 검증에 이용했으며, 각 저작물은 표의 출처에서 무료로 내려받을 수 있습니다.

| Work (기관, 연도, 저작물명) | Source | Used for |
|---|---|---|
| 과학기술정보통신부 국립전파연구원, 2024, 'ICT 융・복합 시설의 안전한 전자파 환경 기반 조성 연구' | [공공데이터포털](https://www.data.go.kr/data/15145080/fileData.do) | training |
| 과학기술정보통신부 국립전파연구원, 2024, '전자파 흡수전력 밀도 등 전자파 인체노출량 평가기술 연구' | [공공데이터포털](https://www.data.go.kr/data/15145081/fileData.do) | training |
| 과학기술정보통신부 중앙전파관리소, 2026, '2025년 4분기 위성전파 감시동향' | [중앙전파관리소 위성전파감시정보](https://www.srmc.go.kr/obser/obserInfoBBSList.do) | training |
| 해양수산부, 2021, '무인도서 백서' (무인도서 100선) | [해양수산부 무인도서종합정보시스템](http://uii.mof.go.kr) | training |
| 개인정보보호위원회, 2025, '합성데이터 생성·활용 안내서' | [개인정보보호위원회 발간자료](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10915) | training |
| 개인정보보호위원회, 2024, '생체정보 보호 안내서' | [개인정보보호위원회 발간자료](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10900) | training |
| 한국언론진흥재단, 2022, '광고요금제 도입을 앞둔 넷플릭스에 대한 인식 및 이용 조사' | [공공데이터포털](https://www.data.go.kr/data/15112345/fileData.do) | training |
| 한국언론진흥재단, 2022, '이대남 현상에 대한 인식' | [공공데이터포털](https://www.data.go.kr/data/15112343/fileData.do) | training |
| 한국언론진흥재단, 2020, '코로나19(COVID-19) 관련 정보 이용 및 인식 현황' | [공공데이터포털](https://www.data.go.kr/data/15086396/fileData.do) | training |
| 한국원자력환경공단, 2025, '방사성폐기물 처분시설 부지주변 방사선환경보고서' | [공공데이터포털](https://www.data.go.kr/data/15156699/fileData.do) | held out (choosing β only) |
| 개인정보보호위원회, 2024, '개인정보 유출 등 사고 대응 매뉴얼' | [개인정보보호위원회 발간자료](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10123) | held out (choosing β only) |

### Citation

Ko-VDR-Train-Public v2 and the KoViDoRe benchmark come from:

```bibtex
@inproceedings{choi-etal-2026-kovidore,
    title = "{KoViDoRe}: A Benchmark for {K}orean Visual Document Retrieval",
    author = "Choi, Yongbin and Song, Yongwoo and Sung, Mujeen",
    booktitle = "Proceedings of the 2nd Workshop on Multimodal Augmented Generation via Multimodal Retrieval (MAGMaR 2026)",
    year = "2026",
    doi = "10.18653/v1/2026.magmar-main.11",
    url = "https://aclanthology.org/2026.magmar-main.11/"
}
```

---

## 한국어

[`google/embeddinggemma-2`](https://huggingface.co/google/embeddinggemma-2)의 글 트랜스포머를 한국어 검색 데이터로 미세조정했습니다. v0.3부터는 한국어 문서 쪽 이미지도 학습에 넣었습니다. 학습할 때마다 이전 버전 쪽으로 되돌려 섞어 다른 기능을 지켰습니다. 구조, 접두어, 768차원 공간(128/256/512 축소 가능), 이미지·음성·영상 입력이 원래 모델과 같아 그대로 바꿔 쓸 수 있습니다.

- **v0.3에서 바뀐 점:** v0.2에 이어, 공공데이터포털 문서 45개의 쪽 7,111장과 질의 약 4.6만 개(Ko-VDR-Train-Public v2)로 학습했습니다. 텍스트 검색을 지키려고 이전 학습 데이터 3만 행을 함께 넣었습니다. 이전 버전은 `revision="v0.2"`로 쓸 수 있습니다.
- **결과:**
  - 한국어 문서 이미지 검색 KoViDoRe v2 nDCG@10이 v0.2 0.341에서 0.406으로 올랐습니다. 네 과제 모두 95% 신뢰구간이 0보다 큽니다.
  - 따로 만든 평가 세트인 SDS-KoPub-VDR도 0.424에서 0.508로 올랐습니다.
  - 텍스트 검색 9과제 평균은 0.729(v0.2 0.726)입니다.
  - 사진, 음성, 영어 점검은 0.5점 넘게 떨어진 것이 없습니다.
- **β를 정한 과정 (사후 결정):** 처음 정한 β 0.25는 평가 세트의 FLEURS 음성 검색에서 v0.2보다 399문항 중 4문항을 더 놓쳤습니다. 미리 정한 허용치(3문항)를 넘어 공개하지 않았습니다. 그 뒤 β 0.125와 0.1875를 후보에 더하고 같은 규칙을 다시 적용해 0.1875를 얻었고, 이 값은 모든 점검을 통과했습니다. 후보를 더한 것은 평가 결과를 본 뒤이므로 통과 여부는 사후 판정입니다. v0.2 대비 개선은 신뢰구간으로 따로 확인됩니다.
- **주의:**
  - 학습 데이터가 KoViDoRe v2와 같은 생성기(공공 PDF, LLM이 쓴 질의)로 만들어져 분야와 질의 모양이 맞춰져 있습니다.
  - 경제 과제는 여전히 가장 낮습니다(0.216).
  - FLEURS 음성 검색에서 1문항을 더 놓칩니다.
  - 256차원에서 한국어 군집화 두 과제가 떨어졌습니다(KlueYnat 0.700 → 0.619, KlueMrcDomain 0.858 → 0.804). 축소 벡터로 군집화한다면 v0.2와 비교해 보세요.
- **사용법:** 위 Usage와 같습니다.
  - 질의는 `prompt_name="SearchQuery"`, 글 문서는 `prompt_name="Document"`를 씁니다.
  - 문서 쪽 이미지는 접두어 없이 `model.encode([{"image": 그림}])`로 넣습니다.
  - float16은 쓰지 마세요.
- **라이선스:** 원래 모델과 같은 Apache 2.0입니다. 다음 출처를 함께 밝혀 주세요.
  - Ko-VDR-Train-Public v2(CC BY 4.0), 공공누리 제1유형 문서(위 Attribution 표)
  - KLUE·SQuAD(CC BY-SA 4.0), 위키백과(CC BY-SA 3.0/GFDL), WebFAQ·qwer90qwer/health(CC BY 4.0)
