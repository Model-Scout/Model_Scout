---
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: dataset
    dtype: string
  - name: language
    dtype: string
  - name: task
    dtype: string
  - name: ArmoRM-score
    dtype: float64
  - name: educational_score
    dtype: float64
  - name: category
    dtype: string
  - name: complexity
    dtype: float64
  - name: readability
    dtype: float64
  - name: langid
    dtype: string
  - name: messages
    dtype: float64
  - name: dedup_0.9
    dtype: bool
  - name: dedup_0.8
    dtype: bool
  splits:
  - name: train
    num_bytes: 857723304
    num_examples: 340286
  download_size: 389740376
  dataset_size: 857723304
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

![euroLLM logo](./eurollm_logo.jpeg)

# EuroLLM Synthetic SFT data:

Synthethic data used to train EuroLLM 9B Instruct. Note that different licenses and terms of use **might** apply to subsets of the data. While we made sure that all data comes from open-source commercial friendly models, those subsets might be subjected to different licenses and terms of use.

The datasets are split into the following subsets:

- **multilingual-synthetic-llama3.1-70B**: Data generated with Llama3.1-70B using filtered data from the annealing phase of EuroLLM as seed. This data is under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE).
- **multilingual-synthetic-ifeval-llama3.1-70B**: IFEval-like data generated with Llama3.1-70B using filtered data from the annealing phase of EuroLLM as seed. This data is under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE).
- **Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered**: [Magpie-Align/Magpie-Llama-3.1-Pro-300K](https://huggingface.co/datasets/Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered) further filtered. Also, under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE).
- **Magpie-Align/Magpie-Reasoning-150K**: [Magpie-Align/Magpie-Reasoning-150K](https://huggingface.co/datasets/Magpie-Align/Magpie-Reasoning-V1-150K) further filtered. Under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE) and [Qwen 2 License](https://github.com/QwenLM/Qwen/blob/main/Tongyi%20Qianwen%20LICENSE%20AGREEMENT).
- **Magpie-Align/Magpie-Qwen-Air-300K-Filtered**: [Magpie-Qwen-Air-300K-Filtered](https://huggingface.co/datasets/Magpie-Align/Magpie-Qwen-Air-300K-Filtered) further filtered. Under [Apache 2.0 License](https://huggingface.co/Qwen/Qwen2-7B-Instruct).
- **multilingual-synthetic-ifeval-llama3.1-405B**: IFEval-like data generated using filtered data from the annealing phase of EuroLLM as seed. This data is under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct/blob/main/LICENSE).
- **self-low-resource**: Data generated using an early checkpoint from EuroLLM 9B. Under [Apache 2.0](https://huggingface.co/utter-project/EuroLLM-9B-Instruct).
- **harmful-instruction-refusal**: Multilingual safety data covering some high resource languages and generated with Hermes 405 and 70B. The seed data comes from [HarmfulQA](https://huggingface.co/datasets/declare-lab/HarmfulQA) Under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE).
- **synthetic-ifeval-magpie**: IFEval like data taken from [Magpie-Align/Magpie-Llama-3.1-Pro-300K](https://huggingface.co/datasets/Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered). Under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE).
- **multilingual-synthetic-arc**: Multiple choice QA dataset created with Llama 3.1 70B. Under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE).
- **instruction-generation**: Data that teaches the model to generate an instruction given a seed document. These are a couple examples we took from the creation of **multilingual-synthetic-llama3.1-70B** with the goal of teaching early EuroLLM checkpoints to do the same. Under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE).
- **instruction-generation-ifeval**: Data that teaches the model to generate an IFEval-like instruction given a seed document. These are a couple examples we took from the creation of **multilingual-synthetic-llama3.1-70B** with the goal of teaching early EuroLLM checkpoints to do the same. Under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE).
- **synthetic-eurollm-9B**: Data generated with EuroLLM for some mid/low resource languages. Under [Apache 2.0](https://huggingface.co/utter-project/EuroLLM-9B-Instruct).
- **Magpie-Align/Magpie-Llama-3.1-Pro-DPO-100K-v0.1**: LLM-as-a-judge data where the model is presented with two answers and has to pick the best one. The original data comes from [Magpie-Align/Magpie-Llama-3.1-Pro-DPO-100K-v0.1](https://huggingface.co/datasets/Magpie-Align/Magpie-Llama-3.1-Pro-DPO-100K-v0.1). Under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE).
- **CohereForAI/aya_dataset**: Data from [CohereLabs Aya Dataset](https://huggingface.co/datasets/CohereLabs/aya_dataset). Under [Apache 2.0](https://huggingface.co/datasets/CohereLabs/aya_dataset)
- **multilingual-synthetic-mmlu**: Multiple choice QA dataset created with Llama 3.1 405B. Under [LLama 3.1 License](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct/blob/main/LICENSE).
- **eurollm-hardcoded**: Harcoded instructions created by us (authors). Under [Apache 2.0](https://huggingface.co/utter-project/EuroLLM-9B-Instruct).

## Dataset Structure:
- `conversations`: List with messages (from both user and assistant).
- `dataset`: Subset data.
- `language`: language of the instruction/answer. This might not be 100% correct specially in cases where there are multiple languages in the same conversation.
- `ArmoRM-score`: score of the last answer assigned by [ArmoRM Reward model](https://huggingface.co/RLHFlow/ArmoRM-Llama3-8B-v0.1). In theory, high scores indicate better answers BUT these scores are noisy. ArmoRM is build for ranking different answers and not for direct assessments (data filtering). Nonetheless we empirically observed that filtering with it helped improve the SFT dataset.
- `educational_score`: Educational score of the answer assigned by our quality filter [EuroFilter-v1](https://huggingface.co/utter-project/EuroFilter-v1). Not all answers have to be "educational" but good answers typically have high educational scores.
- `category`: A category assigned to the instruction.
- `complexity`: How difficult is to answer the instruction?
- `readability`: Is it easy to understand the user's instruction?
- `langid`: langid classification.
- `messages`: Number of messages in the conversation.
- `dedup_09` and `dedup_08`: Deduplication filter (these were computed using the entire SFT dataset).

## Citation
If you use our work, please cite:
```
@misc{martins2025eurollm9B,
      title={EuroLLM-9B: Technical Report}, 
      author={Pedro Henrique Martins and João Alves and Patrick Fernandes and and Nuno M. Guerreiro and Ricardo Rei and Amin Farajian and Mateusz Klimaszewski and Duarte M. Alves and José Pombal and Manuel Faysse and Pierre Colombo and François Yvon and Barry Haddow and José G. C. de Souza and Alexandra Birch and André F. T. Martins},
      year={2025},
      archivePrefix={arXiv},
      primaryClass={cs.CL}, 
}
```

# Funding Information

<img src="https://cdn-uploads.huggingface.co/production/uploads/62262e19d36494a6f743a28d/HbzC1C-uHe25ewTy2wyoK.png" width=7% height=7%> 
This is an output of the European Project UTTER (Unified Transcription and Translation for Extended Reality) funded by European Union’s Horizon Europe Research and Innovation programme under grant agreement number 101070631.

For more information please visit https://he-utter.eu/
