---
task_categories:
- question-answering
- text-generation
language:
- ko
tags:
- legal
size_categories:
- 1K<n<10K
pretty_name: easylaw_kr — Korean everyday-law Q&A instruction pairs
---

# easylaw_kr — Korean everyday-law Q&A instruction pairs

**2,195 instruction pairs** built from the Korean government's plain-language legal guidance for ordinary people: deposits not returned, wages paid late, contracts, traffic fines, family matters. Released July 4, 2023 as the training data of **LAW-Alpaca**, a Korean legal-advice LLM project.

- **Source.** The "100 questions, 100 answers" guidance posts on 생활법령정보 (easylaw.go.kr), run by the Ministry of Government Legislation of Korea. Each post's question became `instruction`, its answer became `output`; `input` is empty. Collected in spring 2023. Source text is public government guidance; see the site's [copyright policy](https://www.easylaw.go.kr/CSP/InfoCopyright.laf).
- **Format.** Alpaca-style columns `instruction` / `input` / `output`, one split (`train`, 2,195 rows), Korean only.
- **Author.** Jiwoo Chris Jung ([@jiwoochris](https://huggingface.co/jiwoochris), formerly `juicyjung`), with teammates on the LAW-Alpaca project. Code and notes: [github.com/jiwoochris/LAW-Alpaca](https://github.com/jiwoochris/LAW-Alpaca).

## Models trained on this data

- [jiwoochris/ko_law_alpaca-12.8b](https://huggingface.co/jiwoochris/ko_law_alpaca-12.8b) — LoRA adapter on [beomi/KoAlpaca-Polyglot-12.8B](https://huggingface.co/beomi/KoAlpaca-Polyglot-12.8B), released with this dataset (July 2023).
- [jiwoochris/Law-alpaca-lora-7b](https://huggingface.co/jiwoochris/Law-alpaca-lora-7b) — earlier LoRA adapter on LLaMA-7B (May 2023).

## Used in

- *Chamain: Harmonizing Character Persona Integrity with Domain-Adaptive Knowledge in Dialogue Generation* (Yang, Lee, and Cho), NLP4ConvAI workshop at ACL 2024 — used as the legal-domain Alpaca-style training data and as the input questions for its long-form legal QA evaluation ("the easylaw dataset"). [aclanthology.org/2024.nlp4convai-1.7](https://aclanthology.org/2024.nlp4convai-1.7/)

## Usage

```python
from datasets import load_dataset
ds = load_dataset("jiwoochris/easylaw_kr")["train"]
print(ds[0]["instruction"], ds[0]["output"])
```

## Limitations

- The answers are the government's general guidance as of 2023. Laws change; the dataset is not updated and is not legal advice.
- A model fine-tuned on this data answers fluently even when a question falls outside the guidance. For checkable answers, keep the posts as retrievable text and show the source passage instead of relying on memorized weights; see the notes in the LAW-Alpaca repository.

## Citation

```bibtex
@misc{jung2023easylaw_kr,
  title  = {easylaw\_kr: Korean everyday-law Q\&A instruction pairs},
  author = {Jung, Jiwoo Chris},
  year   = {2023},
  url    = {https://huggingface.co/datasets/jiwoochris/easylaw_kr}
}
```
