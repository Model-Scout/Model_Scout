---
license: mit
task_categories:
- text-classification
- translation
language:
- de
- es
- fr
- ja
- ko
- zh
tags:
- paws-x
- multilingual
- paraphrase-detection
- text-similarity
- machine-translation
size_categories:
- 100K<n<1M
---

# PAWS-X Multilingual Triplet Dataset

This dataset contains PAWS-X (Paraphrase Adversaries from Word Scrambling) data organized by translation models for paraphrase detection and text similarity tasks.

## Dataset Structure

Each sample contains the following fields:
- `id`: Unique identifier for the text pair
- `text1`: First sentence (originally sentence1)
- `text2`: Second sentence (originally sentence2)  
- `label`: Binary label (1 for paraphrase, 0 for non-paraphrase)
- `model`: Translation model used to generate the text

## Available Splits

This dataset contains **36 splits** organized by translation model:

### Individual Model Splits:
- `nllb_200_distilled_600M`
- `nllb_200_distilled_1_3B`
- `nllb_200_1_3B`
- `nllb_200_3_3B`
- `xglm_564M`
- `xglm_1_7B`
- `xglm_2_9B`
- `xglm_4_5B`
- `xglm_7_5B`
- `bloom_560m`
- `bloom_1b1`
- `bloom_1b7`
- `bloom_3b`
- `bloom_7b1`
- `llama_7B`
- `llama_13B`
- `llama_30B`
- `RedPajama_INCITE_Base_3B_v1`
- `RedPajama_INCITE_7B_Base`
- `open_llama_3b`
- `open_llama_7b`
- `open_llama_13b`
- `open_llama_3b_v2`
- `open_llama_7b_v2`
- `falcon_7b`
- `xgen_7b_4k_base`
- `xgen_7b_8k_base`
- `xgen_7b_8k_inst`
- `polylm_1_7b`
- `polylm_13b`
- `polylm_multialpaca_13b`
- `Llama_2_7b_hf`
- `Llama_2_13b_hf`
- `Llama_2_7b_chat_hf`
- `Llama_2_13b_chat_hf`

### Combined Split:
- `combined`: All models combined

## Usage

### Load a Specific Model Split

```python
from datasets import load_dataset

# Load a specific model (e.g., NLLB 200 distilled 600M)
dataset = load_dataset("patrickamadeus/pawsx_mt_triplets", split="nllb_200_distilled_600M")

# Load combined dataset
dataset = load_dataset("patrickamadeus/pawsx_mt_triplets", split="combined")
```

### Load All Available Splits

```python
from datasets import load_dataset

# Load the entire dataset (all splits)
full_dataset = load_dataset("patrickamadeus/pawsx_mt_triplets")

# Access specific splits
nllb_600m = full_dataset["nllb_200_distilled_600M"]
combined = full_dataset["combined"]
```

### Iterate Through Data

```python
# Load a specific split
dataset = load_dataset("patrickamadeus/pawsx_mt_triplets", split="nllb_200_distilled_600M")

# Iterate through samples
for example in dataset:
    print(f"ID: {example['id']}")
    print(f"Text1: {example['text1']}")
    print(f"Text2: {example['text2']}")
    print(f"Label: {example['label']}")
    print(f"Model: {example['model']}")
    break
```

### Use with PyTorch DataLoader

```python
from datasets import load_dataset
from torch.utils.data import DataLoader

# Load dataset
dataset = load_dataset("patrickamadeus/pawsx_mt_triplets", split="nllb_200_distilled_600M")

# Convert to PyTorch format
dataset.set_format("torch")

# Create DataLoader
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Iterate through batches
for batch in dataloader:
    print(f"Batch size: {len(batch['text1'])}")
    print(f"Text1: {batch['text1'][0]}")
    print(f"Text2: {batch['text2'][0]}")
    print(f"Labels: {batch['label']}")
    break
```

## Model Information

The dataset includes translations from the following models:

### NLLB Models:
- `nllb_200_distilled_600M`: NLLB-200 distilled 600M
- `nllb_200_distilled_1_3B`: NLLB-200 distilled 1.3B
- `nllb_200_1_3B`: NLLB-200 1.3B
- `nllb_200_3_3B`: NLLB-200 3.3B

### XGLM Models:
- `xglm_564M`: XGLM 564M
- `xglm_1_7B`: XGLM 1.7B
- `xglm_2_9B`: XGLM 2.9B
- `xglm_4_5B`: XGLM 4.5B
- `xglm_7_5B`: XGLM 7.5B

### BLOOM Models:
- `bloom_560m`: BLOOM 560M
- `bloom_1b1`: BLOOM 1B1
- `bloom_1b7`: BLOOM 1B7
- `bloom_3b`: BLOOM 3B
- `bloom_7b1`: BLOOM 7B1

### LLaMA Models:
- `llama_7B`: LLaMA 7B
- `llama_13B`: LLaMA 13B
- `llama_30B`: LLaMA 30B

### Other Models:
- `RedPajama_INCITE_Base_3B_v1`: RedPajama INCITE Base 3B v1
- `RedPajama_INCITE_7B_Base`: RedPajama INCITE 7B Base
- `open_llama_3b`: Open LLaMA 3B
- `open_llama_7b`: Open LLaMA 7B
- `open_llama_13b`: Open LLaMA 13B
- `open_llama_3b_v2`: Open LLaMA 3B v2
- `open_llama_7b_v2`: Open LLaMA 7B v2
- `falcon_7b`: Falcon 7B
- `xgen_7b_4k_base`: XGen 7B 4K Base
- `xgen_7b_8k_base`: XGen 7B 8K Base
- `xgen_7b_8k_inst`: XGen 7B 8K Instruction
- `polylm_1_7b`: PolyLM 1.7B
- `polylm_13b`: PolyLM 13B
- `polylm_multialpaca_13b`: PolyLM MultiAlpaca 13B
- `Llama_2_7b_hf`: LLaMA 2 7B HF
- `Llama_2_13b_hf`: LLaMA 2 13B HF
- `Llama_2_7b_chat_hf`: LLaMA 2 7B Chat HF
- `Llama_2_13b_chat_hf`: LLaMA 2 13B Chat HF

## Languages

The dataset covers 6 languages:
- German (de)
- Spanish (es)
- French (fr)
- Japanese (ja)
- Korean (ko)
- Chinese (zh)

## Dataset Statistics

- **Total Models**: 35
- **Total Languages**: 6
- **Total Samples per Model**: ~12,000 (2,000 per language × 6 languages)
- **Total Samples (Combined)**: ~420,000

## Citation

If you use this dataset, please cite the original PAWS-X paper:

```bibtex
@inproceedings{yang2019pawsx,
  title={PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification},
  author={Yang, Yinfei and Zhang, Yuan and Tar, Chris and Baldridge, Jason},
  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
  year={2019}
}
```

## License

This dataset is released under the MIT License. The original PAWS-X dataset may be freely used for any purpose, although acknowledgement of Google LLC ("Google") as the data source would be appreciated.
