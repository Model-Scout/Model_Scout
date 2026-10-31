---
task_categories:
- text-generation
language:
- ko
size_categories:
- n<1K
license: cc-by-nc-4.0
tags:
- finance
---


## FinNewsBench

### 📌 Overview

**FinNewsBench** is a Korean financial news dataset composed of **synthetically generated financial news articles**.
The dataset is designed to support *multi-aspect structured information extraction* tasks, where models generate structured information from information-dense financial texts.

All news articles in FinNewsBench are **not real-world news**, but **synthetic data** created to mimic the style, structure, and informational characteristics of Korean financial news. Each article contains rich contextual descriptions involving companies, people, market themes, and sentiment, enabling practical extraction scenarios.

### 📚 Tasks

* **Structured Information Extraction**

  
  The task is formulated as a text-to-structured-output generation problem, where models generate structured fields directly from raw news text. Specifically, models are required to extract the following elements from each article:

  * Company entities
  * Person entities
  * Stock market themes
  * Keywords
  * Central company sentiment


### 🧪 Synthetic Data Generation

The dataset construction process follows these steps:

1. Synthetic financial news articles are generated using the Nine Memos service, which produces company-focused financial news describing market trends, industry issues, and policy-related topics.
2. Generated articles are selected and balanced across representative companies to form the FinNewsBench dataset.
3. Structured annotations are then produced through an LLM-based extraction process and further verified and refined by human annotators with financial domain knowledge to ensure consistency and accuracy.

Through this process, FinNewsBench provides synthetic financial news that preserves the realism and informational richness of real-world news articles, while avoiding copyright and licensing constraints associated with real news data.


### 📍 Key Features

* **Language:** Korean
* **Input Format:** Full-length synthetic news-style text
* **Annotations:** Multi-aspect structured labels combining automatic LLM extraction with expert human verification
* **Use Cases:**

  * Structured information extraction from financial news
  * Multi-entity extraction challenges
  * Sentiment and thematic analysis in finance texts

### 🛠️ Format

* Format: JSONL

| Key         | Type         | Description                                                                                            |
| ----------- | ------------ | ------------------------------------------------------------------------------------------------------ |
| `id`        | integer      | Unique identifier for each news article                                                                |
| `name`      | string       | Primary company associated with the article                                                            |
| `date`      | string       | Synthetic publication date of the article (`YYYY-MM-DD`)                                                         |
| `title`     | string       | Title of the financial news article                                                                    |
| `body`      | string       | Full text of the news article                                                                          |
| `company`   | list[object] | Companies mentioned in the article with relevance scores and evidence sentences                        |
| `people`    | list[object] | People mentioned in the article with relevance scores and evidence sentences                           |
| `theme`     | list[object] | Investment themes (e.g., theme stocks) used in the Korean stock market to categorize related companies |
| `keyword`   | list[object] | Key terms summarizing the article with relevance scores and evidence sentences                         |
| `sentiment` | list[object] | Sentiment annotations toward the central company with impact scores and evidence                       |

* Each object in `company`, `people`, `theme`, and `keyword` includes a name, a relevance weight, and an evidence sentence extracted from the article, along with the annotation source.
* Each object in `sentiment` includes a sentiment label, an impact score, and a supporting evidence sentence.