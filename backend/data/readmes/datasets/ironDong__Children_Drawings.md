---
language:
  - ko
  - en
license: apache-2.0
pretty_name: Children's Drawings Dataset
size_categories:
  - 10K<n<100K
tags:
  - art
  - children
  - psychology
  - drawing
  - art-therapy
task_categories:
  - image-classification
annotations_creators:
  - expert-generated
source_datasets:
  - original
paperswithcode_id: null
---

# Children's Drawings Dataset

This dataset contains children's drawings collected as part of a project conducted by the National Information Society Agency (NIA) of Korea.

## Dataset Structure

The dataset includes:
- Drawings of houses, trees, male figures, and female figures
- Both raw source images and labeled data
- Training and validation splits

### Categories
- 집 (House)
- 나무 (Tree)
- 남자사람 (Male figure)
- 여자사람 (Female figure)

### File Naming Convention
Files are named with the following pattern:
`[category]_[age]_[gender]_[id].jpg`

### Data Organization
```
01-1.정식개방데이터/
├── Training/
│   ├── 01.원천데이터/ (Source Data)
│   │   ├── TS_집/ (Houses)
│   │   ├── TS_나무/ (Trees)
│   │   ├── TS_남자사람/ (Male figures)
│   │   └── TS_여자사람/ (Female figures)
│   └── 02.라벨링데이터/ (Labeled Data)
│       ├── TL_집/ (Houses)
│       ├── TL_나무/ (Trees)
│       ├── TL_남자사람/ (Male figures)
│       └── TL_여자사람/ (Female figures)
└── Validation/
    ├── 01.원천데이터/ (Source Data)
    │   ├── VS_집/ (Houses)
    │   ├── VS_나무/ (Trees)
    │   ├── VS_남자사람/ (Male figures)
    │   └── VS_여자사람/ (Female figures)
    └── 02.라벨링데이터/ (Labeled Data)
        ├── VL_집/ (Houses)
        ├── VL_나무/ (Trees)
        ├── VL_남자사람/ (Male figures)
        └── VL_여자사람/ (Female figures)
```

## Potential Uses

This dataset can be used for:
- Art therapy research
- Child psychology studies
- Machine learning models for analyzing children's drawings
- Educational research on child development

## Source

This data is the result of a project conducted by the National Information Society Agency (NIA) of Korea.
