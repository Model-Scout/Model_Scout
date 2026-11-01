---
license: apache-2.0
task_categories:
- sentence-similarity
- feature-extraction
- text-retrieval
language:
- ko
tags:
- korean-medicine
- traditional-medicine
- embedding
- contrastive-learning
- retrieval
- ontology
- bge-m3
- hangeul-hanja
pretty_name: Korean Medicine Embedding Dataset
size_categories:
- 100K<n<1M
configs:
- config_name: default
  data_files:
  - split: train
    path: split_val/unified_train.jsonl
  - split: validation_hangeul_hanja
    path: split_val/val_both.jsonl
  - split: validation_hanja
    path: split_val/val_chinese.jsonl
  - split: validation_hangeul
    path: split_val/val_korean.jsonl
  - split: test_hangeul_hanja
    path: split_val/test_both.jsonl
  - split: test_hanja
    path: split_val/test_chinese.jsonl
  - split: test_hangeul
    path: split_val/test_korean.jsonl
---

# Korean Medicine Embedding Dataset (한의학 임베딩 데이터셋)

A contrastive-learning dataset for training and evaluating **domain-adapted text embedding models for Korean Medicine (KM, 한의학)**. Each example is a `query–positive–negatives` triplet built from KM terminology resources and a curated KM ontology, capturing semantic relations such as disease–symptom, disease–prescription, prescription–indication, prescription–herb, and herb–indication.

This dataset accompanies the study *"A Domain-Adapted Embedding Model for Semantic Retrieval of Korean Medicine Knowledge"*, where it was used to domain-adapt [BGE-M3](https://huggingface.co/BAAI/bge-m3) with LoRA and ontology-guided negative sampling. To our knowledge, it is the first publicly released embedding dataset specifically targeting Korean traditional medicine.

## Why this dataset

General-purpose and biomedical embedding models do not capture the conceptual and linguistic structure of KM. KM interprets disease states in functional and relational terms and relies on symbolic concepts (e.g., 음양 *yin–yang*, 한열 *cold–heat*). It shares historical roots with Traditional Chinese Medicine but developed an independent theoretical system (e.g., *Donguibogam*, Sasang constitutional medicine). KM texts also mix **Hangeul (한글)**, **Hanja (한자)**, and **Hangeul–Hanja parallel notation**, where homophonous Sino-Korean terms can differ in meaning depending on the underlying characters. This dataset was constructed to inject that domain knowledge and these orthographic characteristics into embedding training.

## Dataset structure

### Data fields

Each line is a JSON object:

| Field | Type | Description |
|-------|------|-------------|
| `query` | `string` | A KM term or concept (term, disease, pattern identification, prescription, herb). |
| `pos` | `list[string]` | Semantically related positive text(s). |
| `neg` | `list[string]` | 10 negatives per query: **3 similarity-based hard negatives + 7 random negatives**. |

Example (Hangeul–Hanja format):

```json
{
  "query": "사군산(使君散)",
  "pos": ["사군자(使君子), 빈랑자(檳榔子), 웅황(雄黃)"],
  "neg": ["목통(木通), 청피(靑皮), 내복자(萊菔子), 회향(茴香), ...", "..."]
}
```

### Text representation formats

Every underlying semantic instance is provided in **three text representations**, applied identically to the `query`, `pos`, and `neg` fields:

| Format | File suffix | Example |
|--------|-------------|---------|
| Hangeul (한글 전용) | `korean` | `풍한해수` |
| Hanja (한자 전용) | `chinese` | `風寒咳嗽` |
| Hangeul–Hanja (병기) | `both` | `풍한해수(風寒咳嗽)` |

The three representation-specific datasets share **identical instance IDs**, so a given ID denotes the same query–positive relationship across all three.

### Splits

The dataset contains **113,299 underlying semantic instances**. To prevent different representations of the same instance from being distributed across partitions, **synchronized splitting was performed at the instance level**: the 113,299 instances were randomly divided **8:1:1** into train / validation / test, and the same partition assignment was applied to all three representation-specific datasets.

This yields **90,639 train / 11,330 validation / 11,330 test** instances per representation. The three training subsets were combined into a multi-representation training set of **271,917** instances.

| File | Split | Representation | Instances |
|------|-------|----------------|----------:|
| `split_val/unified_train.jsonl` | train | all three combined | **271,917** |
| `split_val/val_both.jsonl` | validation | Hangeul–Hanja | 11,330 |
| `split_val/val_chinese.jsonl` | validation | Hanja | 11,330 |
| `split_val/val_korean.jsonl` | validation | Hangeul | 11,330 |
| `split_val/test_both.jsonl` | test | Hangeul–Hanja | 11,330 |
| `split_val/test_chinese.jsonl` | test | Hanja | 11,330 |
| `split_val/test_korean.jsonl` | test | Hangeul | 11,330 |

The validation set was used for hyperparameter selection; the test set was held out for final evaluation.

Per-representation, unsplit versions of the full data are also provided under `transformed/`:

| File | Representation | Instances |
|------|----------------|----------:|
| `transformed/train_data_both.jsonl` | Hangeul–Hanja | 113,299 |
| `transformed/train_data_chinese.jsonl` | Hanja | 113,299 |
| `transformed/train_data_korean.jsonl` | Hangeul | 113,299 |

> Naming note: `both` = Hangeul–Hanja, `korean` = Hangeul, `chinese` = Hanja.

## Dataset composition

Positive pairs span **16 relation types** drawn from two source types:

| Data source | Query–Positive pair | Train | Validation | Test | Total |
|---|---|---:|---:|---:|---:|
| KM Terminology | Term–Definition | 23,379 | 2,974 | 2,925 | 29,278 (25.8%) |
| KM Terminology | Term–Synonym | 26,637 | 3,380 | 3,226 | 33,243 (29.3%) |
| KM Ontology | Disease–Disease | 2,637 | 304 | 325 | 3,266 (2.9%) |
| KM Ontology | Disease–Etiology | 498 | 55 | 64 | 617 (0.5%) |
| KM Ontology | Disease–Symptom | 5,155 | 606 | 613 | 6,374 (5.6%) |
| KM Ontology | Disease–Treatment Principle | 906 | 107 | 124 | 1,137 (1.0%) |
| KM Ontology | Disease–Prescription | 2,053 | 234 | 261 | 2,548 (2.2%) |
| KM Ontology | Disease–Pattern Identification | 540 | 65 | 60 | 665 (0.6%) |
| KM Ontology | Disease–Prognosis | 96 | 16 | 14 | 126 (0.1%) |
| KM Ontology | Prescription–Indication | 12,554 | 1,547 | 1,669 | 15,770 (13.9%) |
| KM Ontology | Prescription–Herb | 12,960 | 1,662 | 1,649 | 16,271 (14.4%) |
| KM Ontology | Prescription–Efficacy | 762 | 83 | 95 | 940 (0.8%) |
| KM Ontology | Herb–Alias | 1,097 | 121 | 140 | 1,358 (1.2%) |
| KM Ontology | Herb–Property | 450 | 61 | 54 | 565 (0.5%) |
| KM Ontology | Herb–Efficacy | 464 | 52 | 53 | 569 (0.5%) |
| KM Ontology | Herb–Indication | 451 | 63 | 58 | 572 (0.5%) |
| **Total** | | **90,639** | **11,330** | **11,330** | **113,299** |

## Construction pipeline

1. **Source curation.** Query–positive pairs were derived from KM terminology resources (term–definition, term–synonym) and a verified KM ontology covering diseases, pattern identifications, prescriptions, and herbs.
2. **Negative sampling (graph-based exclusion → similarity + random).** All elements of query–positive pairs were placed on a graph with bidirectional edges. Concept nodes (diseases, prescriptions, herbs) connect to other nodes; textual nodes (definitions, efficacies, indications) have no additional connections. Nodes within **2 hops** of a query were excluded from the negative candidate pool because of potential semantic relatedness. From the remaining candidates, **10 negatives** were selected per query: **3 similarity-based hard negatives** (cosine similarity 0.4–0.6 under BGE-M3) and **7 random negatives**.
3. **Multi-representation generation.** Each instance was rendered in Hangeul, Hanja, and Hangeul–Hanja, with the transformation applied consistently to query, positive, and negative texts.
4. **Synchronized splitting.** Instances were split 8:1:1 with partition assignments shared across all three representations; the training subsets were then unified.

## Reference results

The dataset was used to domain-adapt BGE-M3 (568M params) with LoRA (r=16, α=32, dropout=0.1) and MultipleNegativesRankingLoss. Selected configuration: batch size 32, learning rate 5×10⁻⁴, 20 epochs, max sequence length 256, BF16.

Two evaluation settings were used on the same held-out test partition:

- **Candidate-pool** — each query ranked against 11 candidates (1 positive + its 10 negatives).
- **Full-corpus** — each query searched against all unique candidate texts: **74,828** (Hangeul–Hanja), **74,134** (Hanja), **73,100** (Hangeul). Corpus sizes differ because distinct source texts can convert to identical representations. Self-matching queries were excluded.

Hangeul–Hanja representation:

| Setting | Metric | BGE-M3 (base) | BGE-M3 + LoRA |
|---|---|---:|---:|
| Candidate-pool | Recall@1 | 0.5583 | **0.8378** |
| Candidate-pool | MRR@10 | 0.6607 | **0.8953** |
| Candidate-pool | NDCG@10 | 0.7315 | **0.9206** |
| Full-corpus | Recall@1 | 0.0458 | **0.0829** |
| Full-corpus | Recall@10 | 0.1545 | **0.3286** |
| Full-corpus | Recall@100 | 0.3104 | **0.6385** |
| Full-corpus | MRR@10 | 0.0760 | **0.1483** |
| Full-corpus | NDCG@10 | 0.0945 | **0.1906** |
| Full-corpus | Median rank | 1,174 | **30** |

Full-corpus performance across representations (fine-tuned model): Hangeul–Hanja MRR@10 0.1483 > Hanja 0.1376 > Hangeul 0.1184.

Performance varied substantially by relation type — Herb–Alias was highest (MRR@10 0.4209, median rank 3), followed by Term–Synonym (0.2755) and Term–Definition (0.1852).

**SimGap** (mean cosine similarity of positive pairs minus that of negative pairs, computed over the 10 predefined negatives) rose from 0.1245 to 0.5134 for the Hangeul–Hanja representation after domain adaptation.

Ablation analyses reported in the paper found that the effects of similarity-based hard-negative sampling and graph-based filtering were small and **not consistent** across the three evaluation representations, and that the benefit of including the combined Hangeul–Hanja representation in training varied by evaluation format.

## Intended uses

- Training / fine-tuning **Korean Medicine–specific embedding models** for semantic retrieval.
- Building **RAG systems**, clinical decision support, and knowledge-retrieval pipelines over KM literature, guidelines, and ontology-based knowledge bases.
- Studying the effect of **Hangeul / Hanja / Hangeul–Hanja** representations on retrieval in Sino-Korean technical domains.

## Limitations

- Train, validation, and test partitions were derived from the **same** terminology and ontology resources via random splitting. Although splitting was synchronized at the instance level to prevent representation-level leakage, the same entity may still appear across partitions; generalization to fully unseen entities is not guaranteed.
- The data reflects terminology and ontology relations, **not** real clinical notes or prescription records, which use non-standardized, abbreviated, and varied expressions.
- Negatives were mined under BGE-M3 similarity, so their difficulty distribution is tied to that base model.
- The candidate-pool setting (1 positive + 10 negatives) saturates Recall@10; the full-corpus setting is the more informative evaluation.

## Citation

```bibtex
@article{kim2026km_embedding,
  title   = {A Domain-Adapted Embedding Model for Semantic Retrieval of Korean Medicine Knowledge},
  author  = {Kim, Young-Eun and Keum, Kimun and Kim, Sang-Kyun and Kim, Anna and Son, Mi Ju and Seo, SuMin and Jang, Yunji and Oh, Yongtaek and Yi, Mun Yong},
  year    = {2026},
  note    = {Dataset: https://huggingface.co/datasets/cnupo23/korean-medicine-embedding-dataset}
}
```

## License

Released under the **Apache License 2.0**. The underlying terminology and ontology resources are subject to their original terms; please verify source-specific conditions before use.
