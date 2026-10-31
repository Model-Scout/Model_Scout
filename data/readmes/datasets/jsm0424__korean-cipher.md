---
license: cc-by-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: message
    dtype: string
  - name: ciphertext
    dtype: string
  splits:
  - name: train
    num_bytes: 60178
    num_examples: 196
  download_size: 44258
  dataset_size: 60178
language:
- ko
pretty_name: korean-cipher
size_categories:
- n<1K
---


# Korean-Cipher Dataset

## Overview  
This dataset was inspired by OpenAI's video, ["Korean Cipher with OpenAI o1"](https://www.youtube.com/watch?v=eZDmDn6Iq9Y).  
It is designed to evaluate the reasoning abilities of large language models (LLMs) in understanding and reconstructing distorted Korean text.  

### **Dataset Structure**  
Each sample in the dataset consists of the following fields:  

- **`id`**: A unique identifier for each sentence pair.  
- **`message`**: The original Korean sentence.  
- **`ciphertext`**: The distorted version of the original sentence, created by breaking linguistic rules and deviating from standard orthography.  

Native Korean speakers can recognize these distortions and intuitively reconstruct the correct sentences.  
This dataset serves as a benchmark to test whether LLMs possess similar reasoning capabilities in processing and restoring corrupted Korean text.  

## Future Plans  
In future research, we plan to experiment with reasoning-focused LLMs such as **OpenAI o1**, **OpenAI o3 mini** and **DeepSeek r1** using this dataset.  
We will analyze their performance and share the results with the community.  

## How to Use  
This dataset can be used for:  
✅ Evaluating LLMs' ability to reconstruct distorted Korean text  
✅ Training models to improve Korean text normalization and error correction  
✅ Studying how LLMs handle non-standard linguistic patterns  

## Citation  
If you use this dataset, please cite it as follows:  

```bibtex
@misc{korean_cipher,
  title={Korean Cipher Dataset},
  author={jsm0424},
  year={2025},
  url={https://huggingface.co/datasets/jsm0424/korean-cipher}
}