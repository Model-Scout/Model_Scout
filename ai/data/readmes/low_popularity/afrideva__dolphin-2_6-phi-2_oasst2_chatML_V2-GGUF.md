---
base_model: NickyNicky/dolphin-2_6-phi-2_oasst2_chatML_V2
inference: false
language:
- en
- es
- ru
- zh
- de
- fr
- th
- ca
- it
- ja
- pl
- eo
- eu
- vi
- fi
- hu
- ar
- nl
- da
- tr
- ko
- he
- id
- cs
- bn
- sv
model_creator: NickyNicky
model_name: dolphin-2_6-phi-2_oasst2_chatML_V2
pipeline_tag: text-generation
quantized_by: afrideva
tags:
- gguf
- ggml
- quantized
- q2_k
- q3_k_m
- q4_k_m
- q5_k_m
- q6_k
- q8_0
---
# NickyNicky/dolphin-2_6-phi-2_oasst2_chatML_V2-GGUF

Quantized GGUF model files for [dolphin-2_6-phi-2_oasst2_chatML_V2](https://huggingface.co/NickyNicky/dolphin-2_6-phi-2_oasst2_chatML_V2) from [NickyNicky](https://huggingface.co/NickyNicky)


| Name | Quant method | Size |
| ---- | ---- | ---- |
| [dolphin-2_6-phi-2_oasst2_chatml_v2.fp16.gguf](https://huggingface.co/afrideva/dolphin-2_6-phi-2_oasst2_chatML_V2-GGUF/resolve/main/dolphin-2_6-phi-2_oasst2_chatml_v2.fp16.gguf) | fp16 | 5.56 GB  |
| [dolphin-2_6-phi-2_oasst2_chatml_v2.q2_k.gguf](https://huggingface.co/afrideva/dolphin-2_6-phi-2_oasst2_chatML_V2-GGUF/resolve/main/dolphin-2_6-phi-2_oasst2_chatml_v2.q2_k.gguf) | q2_k | 1.09 GB  |
| [dolphin-2_6-phi-2_oasst2_chatml_v2.q3_k_m.gguf](https://huggingface.co/afrideva/dolphin-2_6-phi-2_oasst2_chatML_V2-GGUF/resolve/main/dolphin-2_6-phi-2_oasst2_chatml_v2.q3_k_m.gguf) | q3_k_m | 1.49 GB  |
| [dolphin-2_6-phi-2_oasst2_chatml_v2.q4_k_m.gguf](https://huggingface.co/afrideva/dolphin-2_6-phi-2_oasst2_chatML_V2-GGUF/resolve/main/dolphin-2_6-phi-2_oasst2_chatml_v2.q4_k_m.gguf) | q4_k_m | 1.79 GB  |
| [dolphin-2_6-phi-2_oasst2_chatml_v2.q5_k_m.gguf](https://huggingface.co/afrideva/dolphin-2_6-phi-2_oasst2_chatML_V2-GGUF/resolve/main/dolphin-2_6-phi-2_oasst2_chatml_v2.q5_k_m.gguf) | q5_k_m | 2.07 GB  |
| [dolphin-2_6-phi-2_oasst2_chatml_v2.q6_k.gguf](https://huggingface.co/afrideva/dolphin-2_6-phi-2_oasst2_chatML_V2-GGUF/resolve/main/dolphin-2_6-phi-2_oasst2_chatml_v2.q6_k.gguf) | q6_k | 2.29 GB  |
| [dolphin-2_6-phi-2_oasst2_chatml_v2.q8_0.gguf](https://huggingface.co/afrideva/dolphin-2_6-phi-2_oasst2_chatML_V2-GGUF/resolve/main/dolphin-2_6-phi-2_oasst2_chatml_v2.q8_0.gguf) | q8_0 | 2.96 GB  |



## Original Model Card:
```
  - model fine tune base: cognitivecomputations/dolphin-2_6-phi-2
  - sft
  - flash-attention 2
  - loss: 0.85
  - steps: 3000
  - max_length: 2028
  - neftune_noise_alpha: 5
```


![image/png](https://cdn-uploads.huggingface.co/production/uploads/641b435ba5f876fe30c5ae0a/wLDT0cPWHzFtv_HHigCH4.png)

Install packages
```Python
!python -m pip install --upgrade pip
!pip install -q datasets trl peft bitsandbytes sentencepiece wandb
!pip install -q accelerate safetensors deepspeed
!pip install -q scipy

!export CUDA_HOME=/usr/local/cuda-11.8
# !pip install ninja
!pip install ninja packaging --upgrade -qqq
!MAX_JOBS=4 pip install flash-attn --no-build-isolation -qqq
!pip install git+"https://github.com/HazyResearch/flash-attention.git#subdirectory=csrc/rotary" -qqq
!python -m pip install optimum -qqq
```

Ioad model and generate text
```Python

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
    GenerationConfig,
    TextIteratorStreamer,
)
# from attention_sinks import AutoModelForCausalLM

import torch

model_id = "NickyNicky/dolphin-2_6-phi-2_oasst2_chatML_V2"

model = AutoModelForCausalLM.from_pretrained(model_id,
                                             device_map="auto",
                                             trust_remote_code=True,
                                             torch_dtype=torch.bfloat16,
                                             load_in_4bit=True, 
                                             low_cpu_mem_usage= True,
                                             flash_attn=True,
                                             flash_rotary=True, 
                                             fused_dense=True,
                                             )
max_length=2028 
print("max_length",max_length)

tokenizer = AutoTokenizer.from_pretrained(model_id,
                                          use_fast = True,
                                          max_length=max_length,
                                          trust_remote_code=True,)

prompt= """<|im_start|>system
You are a helpful AI assistant.<|im_end|>
<|im_start|>user
tengo hambre que me recomiendas<|im_end|>
<|im_start|>assistant"""

inputs = tokenizer.encode(prompt,
                          return_tensors="pt",
                          add_special_tokens=False).cuda()#.to("cuda") # False # True

generation_config = GenerationConfig(
              max_new_tokens=700,
              temperature=0.5,
              top_p=0.9,
              top_k=45,
              repetition_penalty=1.15, #1.1, # 1.0 means no penalty, > 1.0 means penalty, 1.2 from CTRL paper
              do_sample=True,
              pad_token_id=tokenizer.eos_token_id,
              eos_token_id=tokenizer.eos_token_id,
              # bos_token_id=tokenizer.eos_token_id,
              #  use_cache=True,
              # stopping_criteria= StoppingCriteriaList([stopping_criteria]),
          )

outputs = model.generate(generation_config=generation_config,
                         input_ids=inputs,)
# tokenizer.decode(outputs[0], skip_special_tokens=False) #True
print(tokenizer.decode(outputs[0], skip_special_tokens=False))

'''OUTPUT:
<|im_start|>system
You are a helpful AI assistant.<|im_end|>
<|im_start|>user
tengo hambre que me recomiendas<|im_end|>
<|im_start|>assistant
Hay muchos tipos de alimentos que puedes probar si tienes hambre, pero aquí te muestro una lista ordenada por calor:

1- Frutas y verduras: Estas son buena opción para quitar hambre sin agotar tu cuerpo con grandes cantidades de carbohidratos. Algunas frutas y verduras que podrían ser suficientemente altas en calor durante el día incluyen tomates, plátanos, espinacas, papas, nueces, manzanas, limones, guisantes, cucumbers, zanahorias, etc.
2- Proteínas: Estas son importantes para mantener tu masa muscular y fuerzosa durante el día. Algunas proteínas que podrían ser útiles para quitar hambre durante el día incluyen carne, aceite de oliva, miel, yogur, leche fresca o sopa de gorditas, etc.
3- Carbohidratos: Estas son importantes para energizarte durante el día y mantenerte físico. Algunas frutas y verduras que podrían ser útiles para quitar hambre durante el día incluyen pan, tortillas, roti, arroz, pasta, rice, polenta, cereales, granola, etc.
4- Grains: Estas son importantes para mantenerte satiente durante el día y reducir la frecuencia de comidas rápida. Algunas gromas que podrían ser útiles para quitar hambre durante el día incluyen lentejas, farinas, tortilla, ensalada, etc.
5- Nuts y semolina: Estas son buenas opciones para quitar hambre durante el día sin agotar tu cuerpo con grandes cantidades de azúcar. Algunas frutas y verduras que podrían ser útiles para quitar hambre durante el día incluyen anacardios, almendras, macetas, bocaditos, panquesado, etc.
6- Papel picado: Esta es una opción deliciosa y económica que puedes preparar en caso de quitar hambre durante el día. Para hacer papel picado, primero cortezamos las frutas y verduras que deseas usarlas, y luego cortezamos las frutas y verduras que no deseas usarlas. A continuación, cortezamos las frutas y verduras que deseas usarlas más grandes y que estén más frescas, y luego cortezamos las frutas y verduras
'''
```