---
language:
- ko
license: mit
task_categories:
- question-answering
- text-generation
dataset_info:
  features:
  - name: input
    dtype: string
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 93015065
    num_examples: 60061
  download_size: 48634325
  dataset_size: 93015065
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---



# MarkrAI/KOpen-HQ-Hermes-2.5-60K

<p align="center">
  <img src="./Kopen.webp" alt="img" width="300" height="300"/>
</p>

The **`KOpen-HQ-Hermes-2.5-60K`** dataset has been released!

Anyone can use it under the MIT license, so feel free to take advantage of this **high-quality dataset**.

In this dataset, we have focused on incorporating our knowledge rather than human effort as much as possible, so there may be some translation errors.

Please keep this in mind when you cooking with it.


## Dataset Info

- Creator: Markr AI
- Developer: Seungyoo Lee, Kyujin Han
- Data generation:

We used the Near Dedup algorithm on the [Open Hermes dataset](https://huggingface.co/datasets/teknium/OpenHermes-2.5) to remove highly similar data(criteria: **Jaccard Sim, `0.8 >=`**) and then performed translation tasks using the DeepL API with 8 multiprocessing threads.

Afterward, we used SOTA LLMs (GPT-4 Turbo, Gemini, Wizard LM, Llama 3.1 405B) to score the data with Alpaca form prompts. 
We then evaluated the appropriateness of these prompts and extracted and published the data with high scores.



## Dataset's purpose

Our Markr AI research guild aims to make a small contribution to the Korean open-source community.

Through this effort, we hope to invigorate the existing Korean LLM models and their ecosystem, fostering the growth of many excellent Korean language models within the expanding community.

The license for this work is the MIT license, and you are welcome to use it. However, our small wish is that instead of merely using and benefiting from this culture of community activation and sharing, all members contribute to its development and, in doing so, help it evolve further.

Lastly, if you start cooking using this dataset, please press the like button to show your support