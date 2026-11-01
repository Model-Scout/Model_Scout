---
license: apache-2.0
language:
- en
- fr
- zh
- ko
- ja
- vi
- th
- ru
- ar
- pt
- es
- de
tags:
- RAG
- DSE
- cooking
- recipes
- culinary
- retrieval
task_categories:
- visual-document-retrieval
- text-retrieval
configs:
- config_name: train
  data_files: "train-*.parquet"
- config_name: filtered
  data_files: "filtered-*.parquet"
---

# VDR_Cooking_Recipes - Overview

## Dataset Summary

**VDR_Cooking_Recipes is a curated multimodal dataset focused on cooking recipe documents, culinary guides, and food preparation instructions. It combines text and image data extracted from real culinary PDFs to support tasks such as RAG DSE, question answering, document search, and vision-language model training.**

## Dataset Details

### Dataset Creation

This dataset was created using our open-source tool [VDR_pdf-to-parquet](https://github.com/RacineAIOS/VDR_pdf-to-parquet).

Cooking recipe PDFs were collected from public online sources, focusing primarily on cookbooks, culinary guides, and recipe collections from various cuisines and cooking traditions. Each document underwent **manual cleaning and curation** before processing, including the removal of blank pages, title pages, table of contents, and other out-of-topic content to ensure optimal dataset quality.

The cleaned documents were then processed page-by-page to extract text, convert pages into high-resolution images, and generate synthetic culinary queries with corresponding answers.

We used Google's **Gemini 2.5 Flash** model in a custom pipeline to generate diverse, expert-level questions and comprehensive answers that align with the content of each page.

### Data Fields

Each entry in the dataset contains:

- **`id`** (string): A unique identifier for the sample
- **`query`** (string): A synthetic culinary question generated from that page
- **`answer`** (string): A comprehensive answer to the corresponding query
- **`image`** (PIL.Image): A visual rendering of a PDF page    
- **`language`** (string): The detected language of the query  

### Data Generation

Each page produces 4 unique entries: a main culinary query, a secondary one, a visual-based question, and a multimodal semantic query, all with their corresponding answers.

## Supported Tasks

This dataset is designed to support:

- **Question Answering**: Training and evaluating models on culinary and recipe content
- **Visual Question Answering**: Multimodal understanding of recipe documents
- **Document Retrieval**: Developing search systems for culinary and recipe documents
- **Text Generation**: Automated question-answer generation from culinary sources
- **Domain-Specific Applications**: Recipe analysis, cooking assistance, and culinary knowledge understanding

## Dataset Use Cases

- Training and evaluating vision-language models on culinary and recipe content
- Developing multimodal search or retrieval systems for cooking and recipe documents
- Research in automated question-answer generation from culinary and recipe sources  
- Enhancing tools for recipe analysis, cooking assistance, and culinary knowledge understanding
- Supporting culinary education and cooking assistant applications

## Dataset Curators

- **Yumeng Ye**
- **Léo Appourchaux**