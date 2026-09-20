---
language:
  - en
  - ru
  - uk
  - de
  - es
  - am
  - zh
  - ar
  - hi
  - it
  - fr
  - he
  - ja
  - tt
license: openrail++
library_name: transformers
base_model:
  - prajjwal1/bert-small
datasets:
- gravitee-io/textdetox-multilingual-toxicity-dataset
pipeline_tag: text-classification
tags:
  - toxicity
  - bert-small
  - gravitee-io
  - ai-gateway
---
# bert-small-toxicity

This is a toxicity classifier fine-tuned using the [gravitee-io/textdetox-multilingual-toxicity-dataset](https://huggingface.co/datasets/gravitee-io/textdetox-multilingual-toxicity-dataset). The model supports a wide range of languages and is trained for toxicity classification ("not-toxic", "toxic").

We perform an 85/15 train-test split per language based on the `textdetox` dataset. All credits go to the authors of the original corpora.

## Performance Overview

While the model performance differs from [gravitee-io/distilbert-multilingual-toxicity-classifier](https://huggingface.co/gravitee-io/distilbert-multilingual-toxicity-classifier)
Some languages still make the cut, even with the base model being lightweight and trained on English as per the model card. 

### Original model

| Language | eval F1  | train F1 | Δ F1      |
|----------|----------|----------|-----------|
| en       | 0.962567 | 0.992951 | -0.030384 |
| fr       | 0.907895 | 0.988053 | -0.080159 |
| ru       | 0.904891 | 0.939517 | -0.034626 |
| hi       | 0.887978 | 0.942063 | -0.054085 |
| de       | 0.886792 | 0.972123 | -0.085330 |
| uk       | 0.880000 | 0.929799 | -0.049799 |
| tt       | 0.836763 | 0.898663 | -0.061901 |
| it       | 0.824742 | 0.940903 | -0.116160 |
| es       | 0.817708 | 0.941259 | -0.123551 |
| ja       | 0.730458 | 0.795933 | -0.065475 |
| hin      | 0.723944 | 0.867925 | -0.143981 |
| ar       | 0.688396 | 0.755972 | -0.067576 |
| am       | 0.626697 | 0.679577 | -0.052881 |
| he       | 0.570093 | 0.680567 | -0.110474 |
| zh       | 0.615169 | 0.648622 | -0.033454 |


### Quantized model (ONNX)

| Language | eval F1  | train F1 | Δ F1      |
|----------|----------|----------|-----------|
| en       | 0.960864 | 0.993184 | -0.032321 |
| fr       | 0.911958 | 0.988037 | -0.076079 |
| ru       | 0.895890 | 0.938834 | -0.042944 |
| hi       | 0.886486 | 0.939657 | -0.053171 |
| de       | 0.882038 | 0.970994 | -0.088956 |
| uk       | 0.879892 | 0.924596 | -0.044704 |
| tt       | 0.828532 | 0.898537 | -0.070004 |
| it       | 0.826255 | 0.937281 | -0.111027 |
| es       | 0.821990 | 0.940571 | -0.118581 |
| ja       | 0.716459 | 0.791557 | -0.075098 |
| hin      | 0.718750 | 0.866036 | -0.147286 |
| ar       | 0.671916 | 0.752080 | -0.080164 |
| am       | 0.630045 | 0.681464 | -0.051419 |
| he       | 0.563107 | 0.680237 | -0.117131 |
| zh       | 0.610795 | 0.635040 | -0.024245 |


## 🤗 Usage

```python
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification
import numpy as np
# Load model and tokenizer using optimum
model = ORTModelForSequenceClassification.from_pretrained(
 "gravitee-io/bert-small-toxicity",
 file_name="model.quant.onnx"
)
tokenizer = AutoTokenizer.from_pretrained("gravitee-io/bert-small-toxicity")
# Tokenize input
text = "Your text here"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
# Run inference
outputs = model(**inputs)
logits = outputs.logits
# Optional: convert to probabilities
probs = 1 / (1 + np.exp(-logits))
print(probs)
```

## Github Repository

You can check details on how the model was fine-tuned and evaluated on the [Github Repository](https://github.com/gravitee-io-labs/gravitee-distilbert-multilingual-toxicity-classifier)

## License

This model is licensed under [OpenRAIL++](LICENSE)

## Citation

```bibtex
@misc{bhargava2021generalization,
      title={Generalization in NLI: Ways (Not) To Go Beyond Simple Heuristics}, 
      author={Prajjwal Bhargava and Aleksandr Drozd and Anna Rogers},
      year={2021},
      eprint={2110.01518},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

@article{DBLP:journals/corr/abs-1908-08962,
  author    = {Iulia Turc and
               Ming{-}Wei Chang and
               Kenton Lee and
               Kristina Toutanova},
  title     = {Well-Read Students Learn Better: The Impact of Student Initialization
               on Knowledge Distillation},
  journal   = {CoRR},
  volume    = {abs/1908.08962},
  year      = {2019},
  url       = {http://arxiv.org/abs/1908.08962},
  eprinttype = {arXiv},
  eprint    = {1908.08962},
  timestamp = {Thu, 29 Aug 2019 16:32:34 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1908-08962.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

```bibtex
@inproceedings{dementieva2024overview,
  title={Overview of the Multilingual Text Detoxification Task at PAN 2024},
  author={Dementieva, Daryna and Moskovskiy, Daniil and Babakov, Nikolay and Ayele, Abinew Ali and Rizwan, Naquee and Schneider, Frolian and Wang, Xintog and Yimam, Seid Muhie and Ustalov, Dmitry and Stakovskii, Elisei and Smirnova, Alisa and Elnagar, Ashraf and Mukherjee, Animesh and Panchenko, Alexander},
  booktitle={Working Notes of CLEF 2024 - Conference and Labs of the Evaluation Forum},
  editor={Guglielmo Faggioli and Nicola Ferro and Petra Galu{{s}}{{c}}{'a}kov{'a} and Alba Garc{'i}a Seco de Herrera},
  year={2024},
  organization={CEUR-WS.org}
}
@inproceedings{dementieva
-etal-2024-toxicity,
  title = "Toxicity Classification in {U}krainian",
  author = "Dementieva, Daryna and Khylenko, Valeriia and Babakov, Nikolay and Groh, Georg",
  booktitle = "Proceedings of the 8th Workshop on Online Abuse and Harms (WOAH 2024)",
  month = jun,
  year = "2024",
  address = "Mexico City, Mexico",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2024.woah-1.19/",
  doi = "10.18653/v1/2024.woah-1.19",
  pages = "244--255"
}
@inproceedings{DBLP:conf/ecir/BevendorffCCDEFFKMMPPRRSSSTUWZ24,
  author = {Janek Bevendorff and et al.},
  title = {Overview of {PAN} 2024: Multi-author Writing Style Analysis, Multilingual Text Detoxification, Oppositional Thinking Analysis, and Generative {AI} Authorship Verification - Extended Abstract},
  booktitle = {ECIR 2024, Glasgow, UK, March 24-28, 2024, Proceedings, Part {VI}},
  series = {Lecture Notes in Computer Science},
  volume = {14613},
  pages = {3--10},
  publisher = {Springer},
  year = {2024},
  doi = {10.1007/978-3-031-56072-9_1}
}
```
