---
license: apache-2.0
datasets:
- maywell/korean_textbooks
language:
- ko
pipeline_tag: text-generation
tags:
- mamba
---
# **Mamba-ko-2.8B🐍**
![Mamba-ko-2.8B](./Seagull-mamba.png)
**Mamba-ko-2.8B** is the state space model, further pretrained(or continous trained) with synthetically generated dataset - [**korean_textbooks**](https://huggingface.co/datasets/maywell/korean_textbooks).

> If you're interested in building large-scale language models to solve a wide variety of problems in a wide variety of domains, you should consider joining [Allganize](https://allganize.career.greetinghr.com/o/65146).
For a coffee chat or if you have any questions, please do not hesitate to contact me as well! - kuotient.dev@gmail.com

I would like to thank Allganize Korea for their generosity in providing resources for this personal project. This project is not directly related to the company's goals or research.
## TODO
- 🟢 Training with korean_textbooks dataset - DONE

- More training with publicly available Korean corpora
- 🟡 Instruct tuning
## **What is Mamba?**
Mamba is a new state space model architecture showing promising performance on information-dense data such as language modeling, where previous subquadratic models fall short of Transformers. It is based on the line of progress on structured state space models, with an efficient hardware-aware design and implementation in the spirit of FlashAttention.
## **License**
Apache 2.0
## **Model Details**
#### **Developed by**
Jisoo Kim(kuotient)
#### **Base Model**  
[state-spaces/mamba-2.8b-slimpj](https://huggingface.co/state-spaces/mamba-2.8b-slimpj)  
## **Model Benchmark**
### KoBEST
| Model | boolq | copa | hellaswag | sentineg |
| --- | --- | --- | --- | --- |
| kuotient/mamba-ko-2.8b | 0.6213 | 0.6150 | 0.4014 | 0.3383 |
| state_spaces/mamba-2.8b-slimpj | 0.3343 | 0.4867 | 0.3452 | 0.3547 |
| kuotient/mamba-ko-2.8b-old (2B trained only) | 0.4236 | 0.5896 | 0.4012 | 0.4348 |
| kuotient/mamba-ko-2.8b-old-instruct | 0.4041 | 0.6505 | 0.4906 | 0.3348 |
| EleutherAI/polyglot-ko-1.3b | 0.3552 | 0.7196 | 0.5247 | 0.6790 |
| maywell/TinyWand-SFT | 0.3455 | 0.6142 | 0.3944 | N/A |
| microsoft/phi-2 | 0.3343 | 0.4792 | 0.3235 | N/A |
| TinyLlama/TinyLlama-1.1B | 0.3343 | 0.4784 | 0.3396 | N/A |
### Thanks
한국어 LLM 커뮤니티에 많은 기여와 동기부여를 해주고 계신 [maywell](https://huggingface.co/maywell)님 감사드립니다.
## Usage
```sh
pip install causal_conv1d>=1.1.0 mamba-ssm==1.1.1
```
```py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel

device = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "kuotient/mamba-ko-2.8b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = MambaLMHeadModel.from_pretrained(
        model_name, device=device, dtype=torch.float16)

prompt = "아이들한테 제공할 영양가 있는 음식 5가지의 예시는 다음과 같다."

tokens = tokenizer(prompt, return_tensors='pt')
input_ids = tokens.input_ids.to(device)
streamer = TextStreamer(tokenizer)

out = model.generate(
    input_ids=input_ids,
    streamer=streamer,
    max_length=2000,
    temperature=0.7,
    top_p=0.7,
    eos_token_id=tokenizer.eos_token_id,
)
```