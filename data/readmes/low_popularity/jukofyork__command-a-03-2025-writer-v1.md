---
inference: false
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
license: cc-by-nc-4.0
base_model:
- jukofyork/command-a-03-2025-uncut
datasets:
- jukofyork/books-fiction-paragraphs
- jukofyork/slop-fiction-paragraphs
---

![no_slop](https://cdn-uploads.huggingface.co/production/uploads/65995c45539c808e84c38bf1/4OL_E7DEPAL5VuLKPeGGc.png)

**NOTE**: Read the [Control Adapter documentation](https://github.com/jukofyork/qlora-pipe-lite/blob/main/docs/ControlAdapters.md) for implementation details.

---

Trained via [qlora-pipe-lite](https://github.com/jukofyork/qlora-pipe-lite):

```toml
# ==============================
# MODEL AND OUTPUT CONFIGURATION
# ==============================

model_dir = '/mnt/models/command-a-03-2025-uncut'
output_dir = '/mnt/fiction_finetunes/finetuned'

# ===========================
# TRAINING TYPE CONFIGURATION
# ===========================

use_control_adapters = true

load_in_4bit = true

# =============================
# CONTROL ADAPTER CONFIGURATION
# =============================

# ~20 tokens per trainable parameter (1e9/(64*64*(12288+1)))
lora_rank = 64

control_adapter_gamma = 0.1

# =======================
# OPTIMIZER CONFIGURATION
# =======================

lr = 1e-3

# ======================
# TRAINING CONFIGURATION
# ======================

sequence_len = 4096

pipeline_stages = 2

# 120 batch size (3*40) --> 480k tokens per step (4096*120)
gradient_accumulation_steps = 40

use_column_major_topology = true

# =====================
# DATASET CONFIGURATION
# =====================

sequence_prefix = 5                 # "<BOS_TOKEN>"

document_prefix = [255000, 255007]  # "<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>"
document_suffix = 255001            # "<|END_OF_TURN_TOKEN|>"

mask_tokens = true                  # Mask all special tokens

drop_tails = true

mix_datasets = true

# -------------------
# POSITIVE CLASS DATA
# -------------------

[[datasets]]
dataset_path = '/mnt/datasets/books-fiction-paragraphs/*.json'
control_class = 1

# -------------------
# NEGATIVE CLASS DATA
# -------------------

[[datasets]]
dataset_path = '/mnt/datasets/slop-fiction-paragraphs/*.json'
control_class = -1
```

using ~1B tokens (ie: ~500M positive and ~500M negative) from:

- [jukofyork/books-fiction-paragraphs](https://huggingface.co/datasets/jukofyork/books-fiction-paragraphs) (***NOTE***: *I have not uploaded this, but you can use my [jukofyork/gutenberg-fiction-paragraphs](https://huggingface.co/datasets/jukofyork/gutenberg-fiction-paragraphs) to get similar results...*)
- [jukofyork/slop-fiction-paragraphs](https://huggingface.co/datasets/jukofyork/slop-fiction-paragraphs)

taking around 15 days using 6x `RTX A6000` over 3 machines:

![image](https://cdn-uploads.huggingface.co/production/uploads/65995c45539c808e84c38bf1/hDJpVIDkDlnZ-zQRkHzFa.png)

![image](https://cdn-uploads.huggingface.co/production/uploads/65995c45539c808e84c38bf1/ANxxDtSFywi3BivFJVgoD.png)

![image](https://cdn-uploads.huggingface.co/production/uploads/65995c45539c808e84c38bf1/FiZGm-88v_Z-8OuV0-yED.png)

(hence the 120 batch size: `(num_gpus / pipeline_stages) * gradient_accumulation_steps = (6 / 2) * 40 = 120`)

***NOTE***: *Ignore the `22.69` days - it crashed whilst I was away from home and had to be restarted a week later...*

---

The control adapter was then converted to a LoRA using [control_adapter_to_lora.py](https://github.com/jukofyork/qlora-pipe-lite/blob/main/control_adapter_to_lora.py):

[command-a-03-2025-writer-v1-lora](https://huggingface.co/jukofyork/command-a-03-2025-writer-v1-lora)

and then merged using the [merge-lora](https://huggingface.co/spaces/jukofyork/merge-lora) space:

```
✓ Successfully merged and uploaded model!
Model URL: https://huggingface.co/jukofyork/command-a-03-2025-writer-v1
Scale factor: 1
Processed 49 shards
Merged 128 layers with LoRA weights
```

---

See [command-a-03-2025-writer-v1-lora-gguf](https://huggingface.co/jukofyork/command-a-03-2025-writer-v1-lora-gguf) for a LoRA in GGUF format that can be used with the `--lora` option on top of the base [command-a-03-2025-uncut](https://huggingface.co/jukofyork/command-a-03-2025-uncut) to get the same effect.