---
license: cc-by-4.0
language:
- en
- fr
- pt
- es
- ar
- hi
- tr
- it
- pl
- de
- ru
- nl
- ko
tags:
- fact-checking
- information-retrieval
---

# Fact-Check Retrieval Dataset

This dataset is designed to support the development and evaluation of fact-check retrieval pipelines. It is structured to work with [FactCheckBureau](https://gitlab.inria.fr/cedar/factcheckbureau), a tool for designing and evaluating fact-check retrieval pipelines. The dataset comprises a list of claims, fact-check articles, and precomputed embeddings for English and French fact-checks.

## Dataset Structure

The dataset consists of the following files and directories:

- **`articles.csv`**: Contains titles and URLs of fact-check articles. *(Note: The `body` column is currently empty; users must scrape or collect the article content themselves using the provided URLs.)*
  
- **`claims.csv`**: Contains a list of claims that have been fact-checked.
  
- **`claim_reviews.csv`**: Contains (claim, fact-check-article) pairs, along with metadata such as review date, publisher, and rating.

- **`embeddings/`**: Directory containing precomputed embeddings for English and French fact-checks.
  - **`English.pt`**: Embeddings for English fact-checks, generated using the `sentence-transformers/all-mpnet-base-v2` model.
  - **`French.pt`**: Embeddings for French fact-checks, generated using the `sentence-transformers/paraphrase-multilingual-mpnet-base-v2` model.

- **`index/`**: Directory containing the IDs corresponding to English and French fact-checks.

- **`full_dataset/`**: Directory containing the full dataset that we have collected, which includes:
  - **`claims.csv`**: Complete list of claims that have been fact-checked.
  - **`articles.csv`**: Complete list of fact-check articles, containing titles and URLs. *(Note: The users will need to collect the article contents themselves.)*
  - **`claim_reviews.csv`**: Full set of (claim, fact-check-article) pairs, with a total of 230,000 pairs. This is the comprehensive Claim Reviews data that has been collected.

## Usage

The files outside of the `full_dataset/` directory are specifically curated for conducting experiments and developing the `FactCheckBureau` application. These files include the necessary embeddings and BM25 objects ([fact-check-bureau](https://huggingface.co/NaughtyConstrictor/fact-check-bureau)) to facilitate the development and evaluation of fact-check retrieval pipelines.

The `full_dataset/` directory contains the entire set of data collected, including all claims and fact-check articles. Users can utilize this larger dataset for extensive analysis, research, and further development.

---