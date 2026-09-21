---
language:
- en
- ko
license: mit
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- email-search
- bge
- embeddings
- multilingual
- email-retrieval
datasets:
- doubleyyh/mixed-email-dataset
model-index:
- name: email-tuned-bge-m3
  results:
  - task:
      type: Retrieval
      name: Email Content Retrieval
    metrics:
      - type: mrr
        value: 0.85
        name: MRR@10
      - type: ndcg
        value: 0.82
        name: NDCG@10
      - type: recall
        value: 0.88
        name: Recall@10
---

# Email-tuned BGE-M3

This is a fine-tuned version of [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) optimized for email content retrieval. The model was trained on a mixed-language (English/Korean) email dataset to improve retrieval performance for various email-related queries.

## Model Description

- **Model Type:** Embedding model (encoder-only)
- **Base Model:** BAAI/bge-m3
- **Languages:** English, Korean
- **Domain:** Email content, business communication
- **Training Data:** Mixed-language email dataset with various types of queries (metadata, long-form, short-form, yes/no questions)

## Quickstart

```python
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

# Initialize the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="doubleyyh/email-tuned-bge-m3",
    model_kwargs={'device': 'cuda'},
    encode_kwargs={'normalize_embeddings': True}
)

# Example emails
emails = [
    {
        "subject": "회의 일정 변경 안내",
        "from": [["김철수", "kim@company.com"]],
        "to": [["이영희", "lee@company.com"]],
        "cc": [["박지원", "park@company.com"]],
        "date": "2024-03-26T10:00:00",
        "text_body": "안녕하세요, 내일 예정된 프로젝트 미팅을 오후 2시로 변경하고자 합니다."
    },
    {
        "subject": "Project Timeline Update",
        "from": [["John Smith", "john@company.com"]],
        "to": [["Team", "team@company.com"]],
        "cc": [],
        "date": "2024-03-26T11:30:00",
        "text_body": "Hi team, I'm writing to update you on the Q2 project milestones."
    }
]

# Format emails into documents
docs = []
for email in emails:
    # Format email content
    content = "\n".join([f"{k}: {v}" for k, v in email.items()])
    docs.append(Document(page_content=content))

# Create FAISS index
db = FAISS.from_documents(docs, embeddings)

# Query examples (supports both Korean and English)
queries = [
    "회의 시간이 언제로 변경되었나요?",
    "When is the meeting rescheduled?",
    "프로젝트 일정",
    "Q2 milestones"
]

# Perform similarity search
for query in queries:
    print(f"\nQuery: {query}")
    results = db.similarity_search(query, k=1)
    print(f"Most relevant email:\n{results[0].page_content[:200]}...")
```


## Intended Use & Limitations

### Intended Use
- Email content retrieval
- Similar document search in email corpora
- Question answering over email content
- Multi-language email search systems

### Limitations
- Performance may vary for domains outside of email content
- Best suited for business communication context
- While supporting both English and Korean, performance might vary between languages

## Citation

```bibtex
@misc{email-tuned-bge-m3,
  author = {doubleyyh},
  title = {Email-tuned BGE-M3: Fine-tuned Embedding Model for Email Content},
  year = {2024},
  publisher = {HuggingFace}
}
```

## License

This model follows the same license as the base model (bge-m3).

## Contact

For questions or feedback, please use the GitHub repository issues section or contact through HuggingFace.