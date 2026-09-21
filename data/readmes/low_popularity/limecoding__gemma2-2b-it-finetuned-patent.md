---
base_model: fine-tuned-model
language:
- ko
license: apache-2.0
tags:
- text-generation-inference
- transformers
- unsloth
- gemma2
- trl
---

# Uploaded  model

- **Developed by:** limecoding
- **License:** apache-2.0
- **Finetuned from model :** fine-tuned-model

This gemma2 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

## Model Overview
This model is fine-tuned to assist with drafting patent specifications based on a general description of an invention.
The base model is unsloth/gemma-2-2b-it, and I used unsloth to merge the fine-tuned adapter.

## Dataset
The dataset used for fine-tuning includes a combination of research paper 
summary datasets from AI-Hub and patent claims data directly retrieved from KIPRIS 
(Korea Intellectual Property Rights Information Service).

Model Training
The model was trained using LoRA (Low-Rank Adaptation). The following code was used for training:
```
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)
```
```
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = train_data,
    max_seq_length = max_seq_length,
    formatting_func = generate_prompt,
    dataset_num_proc = 2,
    packing = False, # Can make training 5x faster for short sequences.
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        num_train_epochs = 1, # Set this for 1 full training run.
        # max_steps = 100,
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 10,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
    ),
)
```


## How to Use the Model

1. Install unsloth:
```
%%capture
!pip install unsloth
# Also get the latest nightly Unsloth!
!pip uninstall unsloth -y && pip install --upgrade --no-cache-dir "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"

# Install Flash Attention 2 for softcapping support
import torch
if torch.cuda.get_device_capability()[0] >= 8:
    !pip install --no-deps packaging ninja einops "flash-attn>=2.6.3"
```

2. Load the fine-tuned model and use it for inference:
```
from unsloth import FastLanguageModel
import torch
max_seq_length = 4096
dtype = None
load_in_4bit = True
token = "your-huggingface-token"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "limecoding/gemma2-2b-it-finetuned-patent",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
    token = token
)
```
3. Write a prompt and generate text:
```
input = """
상술한 과제를 해결하기 위하여, 본 고안은 내부에 보관할 물건을 넣을 수 있는 기본 내장 공간과 이를 둘러싼
외피를 포함하는 가방에 있어서, 상기 외피에는 열리고 닫히는 확장 외피 지퍼가 형성되어 있고, 상기 확장 외
피 지퍼의 내측에는 상기 확장 외피 지퍼가 열리는 경우 펼쳐지는 확장 내피를 더 포함하되, 상기 확장 내피의
내측으로 추가 공간이 형성되어 추가 수납공간을 구비토록 하는 것을 특징으로 하는 추가 수납공간이 구비된 가
방을 제공한다.
본 고안의 상기 확장 외피 지퍼는 상기 가방의 외주 전체를 감싸면서, 상기 확장 내피로 연장되어, 상기 확장
외피 지퍼를 전부 여는 경우 상기 외피가 상기 확장 내피로 연결되면서 분리되어 그 내부에 상기 추가 공간을
형성하는 것을 특징으로 할 수 있다.
본 고안의 상기 추가 공간은 상기 가방의 양측에 구비되는 것을 특징으로 할 수 있다.
상기 가방은 상기 기본 내장 공간이 확장될 수 있는 수단을 더 포함하되, 상기 기본 내장 공간이 확장될 수 있
는 수단은 상기 확장 외피 지퍼의 내측에 형성된 상기 추가 공간이 상기 기본 내장 공간과 통하여 상기 기본 내
장 공간이 확장되도록 하는 것을 특징으로 할 수 있다.
본 고안의 상기 기본 내장 공간과 상기 추가 공간 사이에는 격벽이 형성되어 별도의 추가 수납공간이 형성되는
것을 특징으로 할 수 있다.
본 고안의 상기 격벽은 상기 가방의 내측에서 탈착되는 것으로서, 필요에 따라 상기 기본 내장 공간과 상기 추
가 공간을 분리시키는 것을 특징으로 할 수 있다.
본 고안의 상기 기본 내장 공간의 내측에는 분리형 칸막이가 탈착 가능하게 부설되어 있는 것을 특징으로 할 수
있다.
본 고안의 상기 외피의 외측으로 보조포켓이 형성되어 별도의 수납공간이 형성되는 것을 특징으로 할 수 있다.
본 고안의 상기 보조포켓의 내부에는 탄력밴드가 부착되되 간격을 두고 그 일부가 부착됨으로써 부착되지 않는
공간으로 보관하는 물건을 끼워둘 수 있도록 하는 것을 특징으로 할 수 있다.
본 고안의 상기 확장 내피의 상부에는 내피 개폐 지퍼가 형성되어, 상기 추가 공간의 내부를 열고 닫을 수 있도
록 하는 것을 특징으로 할 수 있다.
본 고안의 상기 추가 공간에 형성된 상기 내피 개폐 지퍼의 양쪽부는 내부가 보이는 망사형 직물부로 형성하여
내장된 물품을 바로 확인할 수 있는 것을 특징으로 할 수 있다.
본 고안의 상기 가방은 가방 휴대자가 어깨에 멜 수 있도록 어깨용 끈 연결부가 형성되어 있는 것을 특징으로
할 수 있다.
본 고안의 상기 어깨용 끈 연결부에 양측 끝단이 고정되는 어깨용 끈을 더 포함하는 것을 특징으로 할 수 있다.
본 고안의 상기 가방의 외피에 부착되어 상기 가방을 들 수 있도록 형성되는 손잡이를 더 포함하는 것을 특징으
로 할 수 있다
"""

FastLanguageModel.for_inference(model)
inputs = tokenizer(
[
    r"""<bos><start_of_turn>user
다음 과제해결수단을 보고 발명의 명칭, 기술분야, 청구항을 뽑아주세요.: {}<end_of_turn>
<start_of_turn>model""".format(input)
], return_tensors = "pt").to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer)
_ = model.generate(**inputs, streamer = text_streamer, max_new_tokens = 1000)
```


## Model Results
The model was tested using the "Means to Solve the Problem" section from actual patent specifications. 
When compared with real patent documents, the model generated content that was relatively similar in 
structure and meaning.
```
[발명의 명칭]
가방


[기술분야]
본 발명은 가방에 관한 것으로, 보다 상세하게는 확장 가능한 가방에 관한 것이다.


[청구항]
내부에 보관할 물건을 넣을 수 있는 기본 내장 공간과 이를 둘러싼 외피를 포함하는 가방에 있어서,

상기 외피에는 열리고 닫히는 확장 외피 지퍼가 형성되어 있고,

상기 확장 외피 지퍼의 내측에는 상기 확장 외피 지퍼가 열리는 경우 펼쳐지는 확장 내피를 더 포함하되,

상기 확장 내피의 내측으로 추가 공간이 형성되어 추가 수납공간을 구비토록 하는 것을 특징으로 하는 추가 수납공간이 구비된 가방.<end_of_turn>
```
