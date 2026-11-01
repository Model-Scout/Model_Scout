---
library_name: transformers
license: cc-by-sa-3.0
datasets:
- wikimedia/wikipedia
- maywell/korean_textbooks
- nampdn-ai/tiny-codes
- Open-Orca/OpenOrca
language:
- ko
- en
inference: false
---

# phi-2-ko-v0.1

## Model Details
This model is a Korean-specific model trained in phi-2 by adding a Korean tokenizer and Korean data. (English is also available.)
Although phi-2 performs very well, it does not support the Korean language and does not have a tokenizer trained on Korean corpous, so tokenizing Korean text will use many times more tokens than English tokens.

To overcome these limitations, I trained the model using an open-license Korean corpus and some English corpus. 
The reasons for using the English corpus together are as follows:
    1. The goal is to preserve the excellent performance of the existing model by preventing catastrophic forgetting. 
    2. Mixing English and Korean prompts usually produces better results than using all prompts in Korean. 

Since my role is not as a working developer, but as an solutions architect helping customers with quick PoCs/prototypes, and I was limited by AWS GPU resources available, I only trained with 5GB of data instead of hundreds of GB of massive data.

### Vocab Expansion

| Model Name | Vocabulary Size | Description | 
| --- | --- | --- |
| Original phi-2 | 50,295 | BBPE (Byte-level BPE) |
| **phi-2-ko** | 66,676 | BBPE. Added Korean vocab and merges |

**Tokenizing "아마존 세이지메이커"**

| Model | # of tokens | Tokens |
| --- | --- | --- |
| Original phi-2 | 25 | `[168, 243, 226, 167, 100, 230, 168, 94, 112, 23821, 226, 116, 35975, 112, 168, 100, 222, 167, 102, 242, 35975, 112, 168, 119, 97]` |
| **phi-2-ko** |6| `[57974, 51299, 50617, 51005, 52027, 51446]` |

### Continued pre-training

The dataset used for training is as follows. To prevent catastrophic forgetting, I included some English corpus as training data.

- Wikipedia Korean dataset (https://huggingface.co/datasets/wikimedia/wikipedia) 
- Massive Korean synthetic dataset (https://huggingface.co/datasets/maywell/korean_textbooks)
- Tiny code dataset (https://huggingface.co/datasets/nampdn-ai/tiny-codes)
- OpenOrca dataset (https://huggingface.co/datasets/Open-Orca/OpenOrca)
- Using some of the various sentences I wrote (personal blog, chat, etc.)


Note that performance is not guaranteed since only a small number of datasets were used for the experiment. The number of samples for training set is just around 5 million after tokenization.
For distributed training, all weights were trained without adapter techniques, and sharding parallelization was performed with ZeRO-2. The presets are as follows.

Since this is a model that has not been fine-tuned, it is recommended to perform fine tuning such as instruction tuning/alignment tuning according to your use case.

```json
{
    "fp16": {
        "enabled": "auto",
        "loss_scale": 0,
        "loss_scale_window": 1000,
        "initial_scale_power": 16,
        "hysteresis": 2,
        "min_loss_scale": 1
    },
    
    "bf16": {
        "enabled": "auto"
    },    

    "optimizer": {
        "type": "AdamW",
        "params": {
            "lr": "auto",
            "betas": "auto",
            "eps": "auto",
            "weight_decay": "auto"
        }
    },

    "scheduler": {
        "type": "WarmupLR",
        "params": {
            "warmup_min_lr": "auto",
            "warmup_max_lr": "auto",
            "warmup_num_steps": "auto"
        }
    },

    "zero_optimization": {
        "stage": 2,
        "allgather_partitions": true,
        "allgather_bucket_size": 2e8,
        "overlap_comm": true,
        "reduce_scatter": true,
        "reduce_bucket_size": 2e8,
        "contiguous_gradients": true,
        "cpu_offload": true
    },

    "gradient_accumulation_steps": "auto",
    "gradient_clipping": "auto",
    "train_batch_size": "auto",
    "train_micro_batch_size_per_gpu": "auto"
}
```

Some hyperparameters are listed below.
```
batch_size: 2
num_epochs: 1
learning_rate: 3e-4
gradient_accumulation_steps: 8
lr_scheduler_type: "linear"
group_by_length: False
```

## How to Get Started with the Model
```python
import torch
from transformers import PhiForCausalLM, AutoModelForCausalLM, AutoTokenizer

torch.set_default_device("cuda")

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained("daekeun-ml/phi-2-ko-v0.1", torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained("daekeun-ml/phi-2-ko-v0.1", trust_remote_code=True)

# Korean 
inputs = tokenizer("머신러닝은 ", return_tensors="pt", return_attention_mask=False)

outputs = model.generate(**inputs, max_length=200)
text = tokenizer.batch_decode(outputs)[0]
print(text)

# English 
inputs = tokenizer('''def print_prime(n):
   """
   Print all primes between 1 and n
   """''', return_tensors="pt", return_attention_mask=False)

outputs = model.generate(**inputs, max_length=200)
text = tokenizer.batch_decode(outputs)[0]
print(text)
```

### References
- Base model: [microsoft/phi-2](https://huggingface.co/microsoft/phi-2)

## Notes 

### License

cc-by-sa 3.0; The license of phi-2 is MIT, but I considered the licensing of the dataset used for training.

### Caution
This model was created as a personal experiment, unrelated to the organization I work for. The model may not operate correctly because separate verification was not performed. Please be careful unless it is for personal experimentation or PoC (Proof of Concept)!