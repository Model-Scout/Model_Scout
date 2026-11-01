# medqa-4k

A Curated Multilingual Medical QA Dataset Featuring English, Chinese, and Korean

# MedQA-4K Dataset

This dataset is derived from the [MedQA](https://github.com/jind11/MedQA) dataset and includes a curated selection of multiple-choice medical questions. It is specifically designed for multilingual natural language processing and fine-tuning language models.

## Key Features:
1. **Language Distribution**:
   - The dataset contains **1,000 randomly sampled questions** for each of the following languages:
     - **English (American)**: Selected from the original dataset.
     - **Chinese (Simplified)**: Selected from the Mainland China subset.
     - **Chinese (Traditional)**: Selected from the Taiwan subset.

2. **Korean Language Addition**:
   - To extend the dataset's multilingual capabilities, **Korean translations** of the English questions and answers were added using Google Translator.

3. **Balanced and Random Sampling**:
   - For each language, questions were randomly sampled from their respective subsets to ensure diversity and fairness.

## Usage:
This dataset is suitable for:
- Training and fine-tuning multilingual language models.
- Exploring cross-lingual transfer learning in medical question-answering tasks.
- Evaluating the performance of language models on medical datasets.

## Dataset Structure:
- **Questions**: Multiple-choice medical questions covering various topics in medicine.
- **Answers**: Corresponding correct answers for each question.
- **Language**: A column indicating the language of each question and answer pair.

출처: Kaggle (seonokrkim/medqa-4k)
태그: health
라이선스: Unknown
수정일: 2025-01-14T18:38:37.910Z
