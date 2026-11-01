---
license: gpl-2.0
task_categories:
- text-classification
language:
- en
- ko
pretty_name: BlendX
size_categories:
- 10M<n<100M
---

# BlendX : Complex Multi-Intent Detection with Blended Patterns
#### Official Repository for "BlendX : Complex Multi-Intent Detection with Blended Patterns." [[Paper(ACL Anthology)]](https://aclanthology.org/2024.lrec-main.218/) [[Paper(arXiv)]](https://arxiv.org/abs/2403.18277)
##### Yejin Yoon, Jungyeon Lee, Kangsan Kim, Chanhee Park and Taeuk Kim. *Accepted to LREC-COLING2024 long paper*.

## Dataset Structure
```
./
├── v1.0/
│   ├── BlendX/
│   │   ├── BlendATIS/
│   │   ├── BlendBanking77/
│   │   ├── BlendCLINC150/
│   │   └── BlendSNIPS/
│   └── MixX/
│       ├── MixATIS/
│       ├── MixBanking77/
│       ├── MixCLINC150/
│       └── MixSNIPS/
├── v2.0/
    ├── KoBlendX/
    │   ├── KoBlendATIS/
    │   ├── KoBlendBanking/
    │   └── KoBlendCLINC/
    └── KoMixX/
        ├── KoMixATIS/
        ├── KoMixBanking/
        └── KoMixCLINC/
```
BlendX is a collection of multi-intent detection datasets constructed by blending or mixing existing domain-specific corpora such as ATIS, Banking77, CLINC150, and SNIPS. The dataset is available in both English (`v1.0`) and Korean (`v2.0`) versions, supporting multilingual research and cross-domain generalization.

- `BlendX/` - Our enhanced multi-intent dataset, BlendX, created by concatenating these single-intent utterance data sources:
    - SNIPS: [paper](https://arxiv.org/abs/1805.10190v3), [dataset](https://github.com/sonos/nlu-benchmark)
    - ATIS: [paper](https://aclanthology.org/H90-1021/), [dataset](https://github.com/Microsoft/CNTK/tree/master/Examples/LanguageUnderstanding/ATIS/Data)
    - Banking77: [paper](https://aclanthology.org/2020.nlp4convai-1.5/), [dataset](https://github.com/PolyAI-LDN/task-specific-datasets/tree/master/banking_data)
    - CLINC150: [paper](https://aclanthology.org/D19-1131/), [dataset](https://github.com/clinc/oos-eval)
- `MixX/` - Our version of MixX, incorporating a concatenation strategy from this [paper](https://aclanthology.org/2020.findings-emnlp.163/) and including [datasets](https://github.com/LooperXX/AGIF), also includes datasets such as *Banking77* and *CLINC150*. Our version is tailored specifically for intent detection, maintaining the integrity of the original datasets.
- `KoBlendX` / `KoMixX`: Korean versions with equivalent structures.

## Usage
You can easily load the dataset using HF `datasets` library: 

```python
from datasets import load_dataset

dataset = load_dataset("HYU-NLP/BlendX", data_dir="v1.0/BlendX/BlendATIS")
print(dataset["test"][0])
```

## Citation
```{bibtex}
@inproceedings{yoon-etal-2024-blendx-complex,
    title = "{B}lend{X}: Complex Multi-Intent Detection with Blended Patterns",
    author = "Yoon, Yejin  and
      Lee, Jungyeon  and
      Kim, Kangsan  and
      Park, Chanhee  and
      Kim, Taeuk",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.218",
    pages = "2428--2439",
    abstract = "Task-oriented dialogue (TOD) systems are commonly designed with the presumption that each utterance represents a single intent. However, this assumption may not accurately reflect real-world situations, where users frequently express multiple intents within a single utterance. While there is an emerging interest in multi-intent detection (MID), existing in-domain datasets such as MixATIS and MixSNIPS have limitations in their formulation. To address these issues, we present BlendX, a suite of refined datasets featuring more diverse patterns than their predecessors, elevating both its complexity and diversity. For dataset construction, we utilize both rule-based heuristics as well as a generative tool{---}OpenAI{'}s ChatGPT{---}which is augmented with a similarity-driven strategy for utterance selection. To ensure the quality of the proposed datasets, we also introduce three novel metrics that assess the statistical properties of an utterance related to word count, conjunction use, and pronoun usage. Extensive experiments on BlendX reveal that state-of-the-art MID models struggle with the challenges posed by the new datasets, highlighting the need to reexamine the current state of the MID field. The dataset is available at \url{https://github.com/HYU-NLP/BlendX}.",
}
```
```
Yejin Yoon, Jungyeon Lee, Kangsan Kim, Chanhee Park, and Taeuk Kim. 2024. BlendX: Complex Multi-Intent Detection with Blended Patterns. In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 2428–2439, Torino, Italia. ELRA and ICCL.
```

## More Details

For detailed dataset construction, statistics, and usage examples, please refer to:
- [ACL Anthology Paper](https://aclanthology.org/2024.lrec-main.218/)
- [arXiv Version](https://arxiv.org/abs/2403.18277)
- [Official GitHub Repository](https://github.com/HYU-NLP/BlendX)

## License

This repository and its contents are licensed under the **GNU General Public License v2.0**. By using, distributing, or contributing to this repository, you agree to the terms and conditions outlined in the LICENSE file.