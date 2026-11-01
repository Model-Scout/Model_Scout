---
library_name: transformers
license: apache-2.0
basemodel: meta-llama/Meta-Llama-3-8B-Instruct
datasets:
- Saxo/total_ko_train_set_1_without_wiki_with_orca
language:
- ko
- en
pipeline_tag: text-generation
---

# Model Card for Model ID

<div align="center">
<img src="http://www.linkbricks.com/wp-content/uploads/2024/11/fulllogo.png" />
</div>


AI 와 빅데이터 분석 전문 기업인 Linkbricks의 데이터사이언티스트인 지윤성(Saxo) 이사가 meta-llama/Meta-Llama-3-8B를 베이스모델로 GCP상의 H100-80G 8개를 통해 SFT-DPO 훈련을 한(8000 Tokens) 한글 기반 모델.
토크나이저는 라마3랑 동일하며 한글 VOCA 확장은 하지 않은 버전 입니다. 한글이 20만개 이상 포함된 한글전용 토크나이저 모델은 별도 연락 주시기 바랍니다.

Dr. Yunsung Ji (Saxo), a data scientist at Linkbricks, a company specializing in AI and big data analytics, trained the meta-llama/Meta-Llama-3-8B base model on 8 H100-60Gs on GCP for 4 hours of instructional training (8000 Tokens).
Accelerate, Deepspeed Zero-3 libraries were used. 

www.linkbricks.com, www.linkbricks.vc

## Configuration including BitsandBytes
---
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=False,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch_dtype
)


args = TrainingArguments(
    output_dir=project_name,
    run_name=run_name_str,
    overwrite_output_dir=True,
    num_train_epochs=20,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4, #1
    gradient_checkpointing=True,
    optim="paged_adamw_32bit",
    #optim="adamw_8bit",
    logging_steps=10,
    save_steps=100,
    save_strategy="epoch",
    learning_rate=2e-4, #2e-4
    weight_decay=0.01,
    max_grad_norm=1, #0.3
    max_steps=-1,
    warmup_ratio=0.1,
    group_by_length=False,
    fp16 = not torch.cuda.is_bf16_supported(),
    bf16 = torch.cuda.is_bf16_supported(),
    #fp16 = True, 
    lr_scheduler_type="cosine", #"constant",
    disable_tqdm=False,
    report_to='wandb',
    push_to_hub=False
)
