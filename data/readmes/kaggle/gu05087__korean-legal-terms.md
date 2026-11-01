# Korean_legal_terms

Korean Legal Terms Dataset in JSONL + CSV format (for RAG / Embedding / Chatbot

# Korean Legal Terms Dataset for LLMs (JSONL + CSV)

This dataset contains Korean legal terms, statutory descriptions, and detailed classifications  
based on actual legal use in Korea.  
It is refined into a JSONL format centered around `page_content` to optimize usage for large language models (LLMs),  
and a CSV version is included to support GUI applications and structured keyword-based search systems.

---

## File Structure

### `* korean_legal_terms.jsonl`

- **Format:** JSON Lines (`.jsonl`)
- **Description:** Each line is a JSON object representing a single legal term entry.
- **Main Fields:**
  - `page_content`: Main content intended for LLM training/inference
  - `metadata`: Additional data such as term, category, and full explanation

#### Example

```json
{
  "page_content": "용어: 폭력행위등처벌에관한법률위반(단체등의구성·활동)\n세부분류: 폭력범죄\n설명: 「폭력행위 등 처벌에 관한 법률」 제4조에 따라 폭력행위를 목적으로 하는 단체를 구성하거나 이에 가입하여 활동하는 행위를 의미합니다. 이는 폭력행위의 집단적·조직적 발생을 방지하기 위해 단체 자체의 구성 및 활동을 처벌 대상으로 규정한 것입니다.",
  "metadata": {
    "term": "폭력행위등처벌에관한법률위반(단체등의구성·활동)",
    "category": "형법",
    "subcategory": "폭력범죄",
    "description": "「폭력행위 등 처벌에 관한 법률」 제4조에 따라 폭력행위를 목적으로 하는 단체를 구성하거나 이에 가입하여 활동하는 행위를 의미합니다. 이는 폭력행위의 집단적·조직적 발생을 방지하기 위해 단체 자체의 구성 및 활동을 처벌 대상으로 규정한 것입니다."
  }
}
```

---

### `* legal_terms.csv` (Structured Legal Glossary)

- **Format:** CSV
- **Use Case:** GUI-based legal term search, filtering, and NLP-friendly preprocessing

<h3>Column Descriptions</h3>

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>category</td>
      <td>Main classification (e.g., Criminal Law, Civil Law)</td>
    </tr>
    <tr>
      <td>subcategory</td>
      <td>Sub-topic (e.g., Violent Crime, Compensation)</td>
    </tr>
    <tr>
      <td>term</td>
      <td>Legal term (e.g., 공소, 공탁, 개시표)</td>
    </tr>
    <tr>
      <td>description</td>
      <td>Full explanation or comparative definition of the term</td>
    </tr>
  </tbody>
</table>

---

## Category Distribution Visualization

This bar chart shows how many legal terms are included in each legal category.  
It helps users quickly understand which legal domains are most represented in the dataset.

<img src="https://github.com/ChloeLee01/lawmang_front/raw/main/src/assets/github/legal_category_chart_clean.png">

&gt; Categories are shown in English to avoid font rendering issues in Kaggle environments.

---

## Description Length Analysis

The following chart visualizes the distribution of character lengths for the `description` field.  
Most descriptions fall between **100 and 350 characters**,  
which makes the dataset suitable for tasks like LLM training, Q&A, embedding generation, and summarization.

<img src="https://github.com/ChloeLee01/lawmang_front/raw/main/src/assets/github/description_length_distribution.png">

&gt; The dataset contains text entries that are well-sized for various LLM applications.

---

## Use Cases

- Pretraining or fine-tuning LLMs on Korean legal domain
- Retrieval-Augmented Generation (RAG) system development
- Building legal chatbot knowledge bases
- Training embedding models and performing semantic search
- Legal document summarization and Q&A
- Designing GUI-based Korean legal glossaries

---

## Disclaimer

- This dataset is provided for research and development purposes only.
- It is not intended to replace legal advice or be used for actual legal decisions.
- All entries are based on public legal sources and manually created explanations.

---

## Contact

For questions or collaboration inquiries, please leave a comment on the Kaggle discussion page.


📌 File(s):  
- korean_legal_terms.jsonl  
- legal_terms_csv  
- README_ko.md  

This dataset was created by Chloe Lee, Seoyoung Cheon, hyeonji Hwang and is licensed under CC BY 4.0.  
A Korean version of the README is included in the dataset as `README_ko.md`.

---

📌 Source Reference:

Some legal term definitions in this dataset are partially based on the following source:

📘 *Legal Terminology Dictionary 2025*  
Author: 법전부 (Legislative Department)  
Publisher: 현암사 (Hyeonamsa Publishing)

출처: Kaggle (gu05087/korean-legal-terms)
태그: business, law, text, korean
라이선스: CC BY-SA 4.0
수정일: 2025-04-16T07:17:49.117Z
