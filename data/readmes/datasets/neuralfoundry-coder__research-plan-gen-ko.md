---
license: cc-by-nc-4.0
language:
- ko
- en
base_model: []
tags:
- research
- planning
- translation
- korean
- machine-learning
- scientific-writing
pretty_name: Research Plan Generation (Korean)
size_categories:
- 10K<n<100K
source_datasets:
- facebook/research-plan-gen
task_categories:
- text-generation
- text2text-generation
---

<!-- aegis-dataset-card -->

# research-plan-gen-ko

> **용도 기록 없음** · Research Plan Generation - Korean (research-plan-gen-ko)  
> 파일 7개 · 140.7 MB · 행 22,513 · revision `26e1e085a3` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
This dataset is a **Korean translation** of the [facebook/research-plan-gen](https://huggingface.co/datasets/facebook/research-plan-gen) dataset. It contains research goals, evaluation rubrics, and reference solutions translated from English to Korean while preserving technical terms, proper nouns, and original formatting.

## 이 데이터로 학습한 모델
이 데이터로 학습했다는 기록(학습 설정 · 모델 카드)을 찾지 못했다. 카탈로그의 '확인 필요' 목록에 있다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 4.7 KB | - |  |
| `data/arxiv/test.jsonl` | 9.6 MB | 1,496 |  |
| `data/arxiv/train.jsonl` | 41.7 MB | 6,573 |  |
| `data/ml/test.jsonl` | 4.5 MB | 685 |  |
| `data/ml/train.jsonl` | 43.3 MB | 6,872 |  |
| `data/pubmed/test.jsonl` | 2.8 MB | 464 |  |
| `data/pubmed/train.jsonl` | 38.8 MB | 6,423 |  |

## 필드 · 범주 분포
**`data/arxiv/test.jsonl`, `data/arxiv/train.jsonl`, `data/ml/test.jsonl`, `data/ml/train.jsonl`, `data/pubmed/test.jsonl`, `data/pubmed/train.jsonl`** (기준 `data/ml/train.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `Goal` | str | 100% |
| `Rubric` | list | 100% |
| `Reference solution` | str | 100% |
| `article_id` | str | 100% |
| `q_id` | str | 100% |
| `Subdomain` | str | 100% |
| `Category` | str | 100% |
| `Identifier` | str | 100% |

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/research-plan-gen-ko --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### Research Plan Generation - Korean (research-plan-gen-ko)

#### Dataset Description

This dataset is a **Korean translation** of the [facebook/research-plan-gen](https://huggingface.co/datasets/facebook/research-plan-gen) dataset. It contains research goals, evaluation rubrics, and reference solutions translated from English to Korean while preserving technical terms, proper nouns, and original formatting.

##### Source Dataset

- **Original Dataset**: [facebook/research-plan-gen](https://huggingface.co/datasets/facebook/research-plan-gen)
- **Original Authors**: Meta AI Research
- **Translation**: Machine translation with optimized prompts for academic/scientific content

##### Dataset Structure

The dataset follows the same structure as the original dataset with three configurations:
- `ml`: Machine Learning domain
- `arxiv`: ArXiv papers
- `pubmed`: PubMed medical literature

Each configuration contains `train` and `test` splits.

##### Fields

| Field | Description |
|-------|-------------|
| `Goal` | Research goal in Korean |
| `Rubric` | Evaluation criteria in Korean (list format) |
| `Reference solution` | Reference solution/methodology in Korean |
| `Goal_original` | Original English research goal |
| `Rubric_original` | Original English evaluation criteria |
| `Reference solution_original` | Original English reference solution |
| `article_id` | Article identifier |
| `q_id` | Question identifier |
| `Subdomain` | Research subdomain |
| `Category` | Category classification |
| `Identifier` | Unique identifier |
| `_idx` | Original dataset index |
| `_config` | Configuration name (ml/arxiv/pubmed) |
| `_split` | Split name (train/test) |

##### Translation Methodology

The translation was performed using an LLM-based translation pipeline with the following optimizations:
- Preservation of technical terms, proper nouns, and citations in original English
- Maintenance of original formatting (markdown, bullet points, numbering)
- Use of natural Korean academic writing style
- Retention of abbreviations and acronyms (e.g., ML, NLP, API)
- Low temperature (0.3) for translation consistency

#### License and Usage

##### License

This dataset inherits the license from the original dataset:
- **License**: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
- **Original License Reference**: Please refer to the [original dataset](https://huggingface.co/datasets/facebook/research-plan-gen) for complete license terms.

##### Attribution

When using this dataset, please cite both:
1. The original [facebook/research-plan-gen](https://huggingface.co/datasets/facebook/research-plan-gen) dataset
2. This Korean translation dataset

##### Disclaimer

**IMPORTANT: User Responsibility Notice**

- This dataset is provided "as-is" for research and educational purposes.
- **Users are solely responsible for any and all issues arising from the use of this dataset**, including but not limited to:
  - Translation errors or inaccuracies
  - Misinterpretation of translated content
  - Any consequences resulting from the use of this data in applications, models, or research
- The translators and distributors of this dataset make no warranties regarding the accuracy, completeness, or fitness for any particular purpose of the translations.
- Users should verify critical information with the original English source when accuracy is essential.
- By using this dataset, you agree to accept full responsibility for any outcomes resulting from its use.

#### Citation

If you use this dataset, please cite the original work:

```bibtex
@misc{research-plan-gen,
  title={Research Plan Generation Dataset},
  author={Meta AI Research},
  year={2024},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/facebook/research-plan-gen}}
}
```

And this Korean translation:

```bibtex
@misc{research-plan-gen-ko,
  title={Research Plan Generation Dataset - Korean Translation},
  author={neuralfoundry-coder},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/neuralfoundry-coder/research-plan-gen-ko}}
}
```

#### Contact

For issues related to:
- **Original dataset content**: Please refer to the [original dataset repository](https://huggingface.co/datasets/facebook/research-plan-gen)
- **Translation quality or this Korean version**: Open an issue on this dataset's repository
