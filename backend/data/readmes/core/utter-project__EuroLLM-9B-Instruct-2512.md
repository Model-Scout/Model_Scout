---
license: apache-2.0
language:
- en
- de
- es
- fr
- it
- pt
- pl
- nl
- tr
- sv
- cs
- el
- hu
- ro
- fi
- uk
- sl
- sk
- da
- lt
- lv
- et
- bg
- 'no'
- ca
- hr
- ga
- mt
- gl
- zh
- ru
- ko
- ja
- ar
- hi
library_name: transformers
base_model:
- utter-project/EuroLLM-9B-2512
---

# Model Card for EuroLLM-9B-Instruct-2512

This is the model card for EuroLLM-9B-Instruct-2512, an improved version of [utter-project/EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct).
In comparison with the previous version, this version includes the long-context extension phase and the revamped post-training recipe from [utter-project/EuroLLM-22B-Instruct](https://huggingface.co/utter-project/EuroLLM-22B-Instruct-2512).

- **Developed by:** Instituto Superior Técnico - University of Lisbon, Instituto de Telecomunicações, University of Edinburgh, Aveni, Unbabel, University of Paris-Saclay, Artefact Research Center, University of Amsterdam, Naver Labs, Sorbonne Université.
- **Funded by:** European Union.
- **Model type:** A 9B parameter multilingual transfomer LLM.
- **Language(s) (NLP):** Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, and Ukrainian. 
- **License:** Apache License 2.0.

[<img src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/axolotl-ai-cloud/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.12.2`
```yaml
auto_resume_from_checkpoints: true
use_tensorboard: true

base_model: utter-project/EuroLLM-9B-2512
model_type: AutoModelForCausalLM
tokenizer_type: AutoTokenizer

load_in_8bit: false
load_in_4bit: false
strict: false

dataset_processes: 64
datasets:
  - path: utter-project/EuroBlocks-SFT-2512
    type: chat_template
    split: train
    conversation: chatml
    field_messages: conversations
    message_field_role: role
    message_field_content: content
    roles_to_train: ["assistant"]
    train_on_eos: all


chat_template_jinja: "{% for message in messages %}{% if message['role'] == 'assistant' %}{% set role = 'assistant' %}{% else %}{% set role = message['role'] %}{% endif %}<|im_start|>{{ role }}\n{{ message['content'] | trim }}<|im_end|>\n{% endfor %}{% if add_generation_prompt %}{{'<|im_start|>assistant\n'}}{% endif %}"
 
output_dir: checkpoints
val_set_size: 0

sequence_len: 32768
sample_packing: true
pad_to_sequence_len: true

# sequence_parallel_degree: 4
# heads_k_stride: 1
# ring_attn_func:

plugins:
  - axolotl.integrations.liger.LigerPlugin
liger_rope: true
liger_rms_norm: true
liger_glu_activation: true
liger_layer_norm: true
liger_fused_linear_cross_entropy: true

# N_GPUS * GRAD_ACC_STEPS * MICRO_BATCH_SIZE * SEQ_LEN = tokens/step ->
# Assuming 32 gpus (32 * 2 * 2 * 32k = 4 096 000 tokens/step)
gradient_accumulation_steps: 2
micro_batch_size: 2

eval_batch_size: 1
num_epochs: 5
optimizer: adamw_torch
lr_scheduler: cosine
learning_rate: 1e-5

train_on_inputs: false
group_by_length: false
bf16: true
fp16: false
tf32: false

gradient_checkpointing: true
logging_steps: 1
flash_attention: true
flash_attn_cross_entropy: false
flash_attn_rms_norm: false
flash_attn_fuse_qkv: false
flash_attn_fuse_mlp: false

warmup_steps: 125
eval_sample_packing: False
save_steps: 500
save_total_limit: 2
deepspeed: deepspeed_configs/zero3_bf16.json
weight_decay: 0.01

special_tokens:
  eos_token: "<|im_end|>"

```
</details><br>

## Run the model
    
    from transformers import AutoModelForCausalLM, AutoTokenizer
    
    model_id = "utter-project/EuroLLM-9B-Instruct-2512"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)

    messages = [
        {
            "role": "system",
            "content": "You are EuroLLM --- an AI assistant specialized in European languages that provides safe, educational and helpful answers.",
        },
        {
            "role": "user", "content": "What is the capital of Portugal? How would you describe it?"
        },
        ]

    inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
    outputs = model.generate(inputs, max_new_tokens=1024)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

## Bias, Risks, and Limitations

EuroLLM-9B has not been aligned to human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful content, or false statements).

## Citation
If you use our work, please cite:
```
@misc{ramos2026eurollm22btechnicalreport,
      title={EuroLLM-22B: Technical Report}, 
      author={Miguel Moura Ramos and Duarte M. Alves and Hippolyte Gisserot-Boukhlef and João Alves and Pedro Henrique Martins and Patrick Fernandes and José Pombal and Nuno M. Guerreiro and Ricardo Rei and Nicolas Boizard and Amin Farajian and Mateusz Klimaszewski and José G. C. de Souza and Barry Haddow and François Yvon and Pierre Colombo and Alexandra Birch and André F. T. Martins},
      year={2026},
      eprint={2602.05879},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.05879}, 
}
```