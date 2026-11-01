---
license: apache-2.0
---

This is [Allen AI's open-instruct dataset.](https://github.com/allenai/open-instruct)

It is used to train the Tulu family of models.

- https://huggingface.co/allenai/tulu-7b
- https://huggingface.co/allenai/tulu-13b
- https://huggingface.co/allenai/tulu-30b
- https://huggingface.co/allenai/tulu-65b

I have done the following:

1) Download the open-instruct repo
2) Execute the scripts/prepare_train_data.sh modified to download the "unfiltered" version of sharegpt dataset
3) Merged data/processed/**/*.jsonl into a single "open-instruct.jsonl"
4) Executed my "remove_refusals.py" against that "open-instruct.jsonl" to produce a "open-instruct-uncensored.jsonl"

I am currently training this "open-instruct-uncensored.jsonl" to a new model series named ehartford/tulu-uncensored

More info to come.