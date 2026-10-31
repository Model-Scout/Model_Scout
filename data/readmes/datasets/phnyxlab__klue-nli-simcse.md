---
dataset_info:
  features:
  - name: premise
    dtype: string
  - name: entailment
    dtype: string
  - name: contradiction
    dtype: string
  splits:
  - name: train
    num_bytes: 2022859.0657676577
    num_examples: 8142
  - name: validation
    num_bytes: 224844.9342323422
    num_examples: 905
  download_size: 1572558
  dataset_size: 2247704
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
language:
- ko
pretty_name: k
size_categories:
- 1K<n<10K
---
# KLUENLI for SimCSE Dataset

For a better dataset description, please visit: [LINK](https://klue-benchmark.com/) <br>
<br>
**This dataset was prepared by converting KLUENLI dataset** to use it for contrastive training (SimCSE). The code used to prepare the data is given below:

```py
import pandas as pd
from datasets import load_dataset, concatenate_datasets, Dataset
from torch.utils.data import random_split


class PrepTriplets:
    @staticmethod
    def make_dataset():
        train_dataset = load_dataset("klue", "nli", split="train")
        val_dataset = load_dataset("klue", "nli", split="validation")
        merged_dataset = concatenate_datasets([train_dataset, val_dataset])

        triplets_dataset = PrepTriplets._get_triplets(merged_dataset)

        # Split back into train and validation
        train_size = int(0.9 * len(triplets_dataset))
        val_size = len(triplets_dataset) - train_size
        train_subset, val_subset = random_split(
            triplets_dataset, [train_size, val_size]
        )

        # Convert Subset objects back to Dataset
        train_dataset = triplets_dataset.select(train_subset.indices)
        val_dataset = triplets_dataset.select(val_subset.indices)

        return train_dataset, val_dataset

    @staticmethod
    def _get_triplets(dataset):
        df = pd.DataFrame(dataset)

        entailments = df[df["label"] == 0]
        contradictions = df[df["label"] == 2]

        triplets = []

        for premise in df["premise"].unique():
            entailment_hypothesis = entailments[entailments["premise"] == premise][
                "hypothesis"
            ].tolist()
            contradiction_hypothesis = contradictions[
                contradictions["premise"] == premise
            ]["hypothesis"].tolist()

            if entailment_hypothesis and contradiction_hypothesis:
                triplets.append(
                    {
                        "premise": premise,
                        "entailment": entailment_hypothesis[0],
                        "contradiction": contradiction_hypothesis[0],
                    }
                )

        triplets_dataset = Dataset.from_pandas(pd.DataFrame(triplets))

        return triplets_dataset

# Example usage:
# PrepTriplets.make_dataset()
```

**How to download**

```
from datasets import load_dataset
data = load_dataset("phnyxlab/klue-nli-simcse")
```


**If you use this dataset for research, please cite this paper:**
```
@misc{park2021klue,
      title={KLUE: Korean Language Understanding Evaluation}, 
      author={Sungjoon Park and Jihyung Moon and Sungdong Kim and Won Ik Cho and Jiyoon Han and Jangwon Park and Chisung Song and Junseong Kim and Yongsook Song and Taehwan Oh and Joohong Lee and Juhyun Oh and Sungwon Lyu and Younghoon Jeong and Inkwon Lee and Sangwoo Seo and Dongjun Lee and Hyunwoo Kim and Myeonghwa Lee and Seongbo Jang and Seungwon Do and Sunkyoung Kim and Kyungtae Lim and Jongwon Lee and Kyumin Park and Jamin Shin and Seonghyun Kim and Lucy Park and Alice Oh and Jung-Woo Ha and Kyunghyun Cho},
      year={2021},
      eprint={2105.09680},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```