---
language:
  - zh
  - ko
  - en
  - multilingual
pretty_name: UniVerseBench
tags:
  - audio
  - music
  - folk-music
  - multimodal
  - audio-language
  - question-answering
  - benchmark
task_categories:
  - question-answering
  - audio-classification
size_categories:
  - 1K<n<10K
license: cc-by-nc-4.0
---

<p align="center">
  <img src="universe_logo.png" alt="UniVerse · 同谣" width="280"/>
</p>

# UniVerseBench

**The evaluation split of [UniVerse](https://huggingface.co/datasets/universe-team/universeset) (同谣).**  
Training data lives in **[UniVerseSet](https://huggingface.co/datasets/universe-team/universeset)**.

UniVerseBench is a multilingual folk-music understanding benchmark for large audio–language models (LALMs). It asks models to listen, not to guess from language priors.

> 「诗言志，歌永言，声依永，律和声。」—《尚书·舜典》

| | |
|--|--|
| **Sister dataset (training)** | [universe-team/universeset](https://huggingface.co/datasets/universe-team/universeset) |
| **Live museum demo** | [http://143.89.224.8:8790/](http://143.89.224.8:8790/) |

---

## What's here

Two views of the same benchmark:

| Subset | Rows | Contents |
|--------|------|----------|
| `material` | **372** exhibits | Audio clip + native / English notes + ABC score + titles (native / translation / transliteration) + language + source URL |
| `qa` | **5,042** items | Multiple-choice questions grounded in those recordings |

Exhibit mix: **102** Chinese folk, **90** Korean gugak, **180** world folk, spanning **38+** languages. Headline site stats: **1.4M** metadata tokens, **1,080** minutes of benchmark audio.

Most QA items use **one** clip; a subset uses **two or three** clips for comparison.

---

## Question types (`qa`)

| Code | Name |
|------|------|
| FE | Feature Extraction |
| CR | Causal Reasoning |
| PR | Music Pattern Recognition |
| CA | Comparison Analysis |
| ED | Error Detection |

Report accuracy by language group: Chinese (`zh`), Korean (`ko`), other (`L-oth.`).

Items were selected so strong LALMs cannot rely on surface cues: we keep questions models miss, ones flagged as misleading in optimization logs, and we enforce coverage per recording.

---

## How to load

```python
from datasets import load_dataset

bench = load_dataset("universe-team/universebench")
materials = bench["material"]   # 372 exhibits
qa = bench["qa"]                # 5,042 MCQs
```

---

## License & attribution

**Academic research only. Commercial use is prohibited.**

All materials in UniVerseBench — including `material` and `qa`, audio clips, native / English notes, ABC scores, this dataset card, and any derived annotations — are released **solely for non-commercial academic research**. You may not use the dataset, in whole or in part, to train, evaluate, or deploy models for commercial products, paid services, advertising, or other for-profit purposes.

Underlying folk recordings remain under their original copyrights, collection licenses, and platform terms. This repository does **not** grant rights to redistribute or commercially exploit the audio. Please credit archives, collectors, and performers when citing or presenting clips.

License on the Hub: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). If you use UniVerseBench in research, please cite the paper below.

---

## Citation

```bibtex
@article{universe2026,
  title   = {UniVerse: Benchmarking and Enhancing LALMs on Culturally Inclusive Low-resource Music Understanding},
  author  = {[TODO: authors]},
  journal = {arXiv preprint arXiv:[TODO]},
  year    = {2026}
}
```
