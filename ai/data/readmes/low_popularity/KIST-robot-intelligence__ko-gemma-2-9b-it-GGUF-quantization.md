---
license: gemma
library_name: transformers
pipeline_tag: text-generation
extra_gated_heading: Access Gemma on Hugging Face
extra_gated_prompt: >-
  To access Gemma on Hugging Face, you’re required to review and agree to
  Google’s usage license. To do this, please ensure you’re logged in to Hugging
  Face and click below. Requests are processed immediately.
extra_gated_button_content: Acknowledge license
tags:
- conversational
base_model:
- rtzr/ko-gemma-2-9b-it
language:
- ko
---

#KIST-robot-intelligence/ko-gemma-2-9b-it-GGUF
This is quantized version of [rtzr/ko-gemma-2-9b-it](https://huggingface.co/rtzr/ko-gemma-2-9b-it) created using llama.cpp

# Model Description

### Ko-Gemma-2-9B-IT

**[Ko-Gemma-2-9B-IT](https://huggingface.co/rtzr/ko-gemma-2-9b-it)** is a Korean-language conversational model that is part of the Gemma family of models. It is a text-to-text, decoder-only large language model, available in Korean. We fine-tuned this model on a carefully curated high-quality dataset using Supervised Fine-Tuning (SFT). And we use [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) training specifically for Human Feedback. The datasets include:

- [Orca-Math](https://huggingface.co/datasets/kuotient/orca-math-korean-dpo-pairs)
- [dpo-mix-7k](https://huggingface.co/datasets/argilla/dpo-mix-7k)

Some of these datasets were partially used and translated for training. In particular, a lot of repetition occurred during the translation process, so preprocessing was performed based on N-gram.

#### *Inputs and outputs*

- **Input:** Text string, such as a question, a prompt, or a document to be summarized.
- **Output:** Generated Korean-language text in response to the input, such as an answer to a question, or a summary of a document.

### Google Gemma 2

Gemma is a family of lightweight, state-of-the-art open models from Google,
built from the same research and technology used to create the Gemini models.
They are text-to-text, decoder-only large language models, available in English,
with open weights for both pre-trained variants and instruction-tuned variants.
Gemma models are well-suited for a variety of text generation tasks, including
question answering, summarization, and reasoning. Their relatively small size
makes it possible to deploy them in environments with limited resources such as
a laptop, desktop or your own cloud infrastructure, democratizing access to
state of the art AI models and helping foster innovation for everyone.

## Benchmark Scores

We evaluated it internally using [LogicKor](https://github.com/instructkr/LogicKor) code. While the public LogicKor code is assessed as GPT-4, our internal evaluation was conducted as GPT-4o. Public scores will be added as they are released. The scores below include only 0-shot evaluations.

| Model | Math | Reasoning | Writing | Coding | Understanding | Grammar | Single ALL | Multi ALL | Overall |
|:---------:|:-----:|:------:|:-----:|:-----:|:----:|:-----:|:-----:|:-----:|:----:|
| [rtzr/ko-gemma-2-9b-it](https://huggingface.co/rtzr/ko-gemma-2-9b-it) | 8.71 / 8.00  | 9.14 / 8.00 | 9.43 / 9.29 | 9.00 / 9.43 | 9.57 / 9.86 | 7.14 / 5.00 | 8.83 | 8.26 | 8.55  |
| [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it) | 8.57 / 7.71  | 8.86 / 7.00 | 9.29 / 9.29 | 9.29 / 9.57 | 8.57 / 8.29 | 6.86 / 3.86 | 8.57  | 7.62  | 8.10 |
| [MLP-KTLim/llama-3-Korean-Bllossom-8B](https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B) | 6.43 / 5.71  | 6.86 / 5.14 | 9.14 / 8.57 | 8.29 / 8.14 | 8.43 / 9.29  | 5.71 / 5.29 | 7.48 | 7.02 | 7.25 |
| [yanolja/EEVE-Korean-Instruct-10.8B-v1.0](https://huggingface.co/yanolja/EEVE-Korean-Instruct-10.8B-v1.0) | 5.57 / 4.29  | 8.14 / 5.14 | 8.29 / 6.29 | 6.43 / 7.86 | 9.29 / 8.57  | 6.57 / 3.71 | 7.38 | 5.98 | 6.68 |
| [allganize/Llama-3-Alpha-Ko-8B-Instruct](https://huggingface.co/allganize/Llama-3-Alpha-Ko-8B-Instruct) | 4.57 / 3.00  | 6.86 / 6.43 | 7.43 / 6.71 | 8.43 / 8.43| 7.71 / 8.71 | 6.71 / 4.43 | 6.95 | 6.29  | 6.62  |

## Usage

### Install Dependencies

You must install transformers >= 4.42.3 for gemma2 models.

```bash
pip install transformers==4.42.3 accelerate
```

### Python code with Pipeline

```python
import transformers
import torch


model_id = "rtzr/ko-gemma-2-9b-it"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

pipeline.model.eval()
instruction = "서울의 유명한 관광 코스를 만들어줄래?"

messages = [
    {"role": "user", "content": f"{instruction}"}
]

prompt = pipeline.tokenizer.apply_chat_template(
    messages, 
    tokenize=False, 
    add_generation_prompt=True
)

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<end_of_turn>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=2048,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)

print(outputs[0]["generated_text"][len(prompt):])
```

```markdown
서울은 역사, 문화, 현대성이 조화를 이룬 매력적인 도시입니다. 여기서 즐길 수 있는 다양한 관광지와 명소를 소개합니다. 다음은 서울의 유명한 관광 코스 3가지입니다.

**1. 역사와 문화를 둘러싼 한국관광코스**

1. **경복궁**: 조선 시대의 웅장한 왕궁을 만끽할 수 있는 곳입니다. 특히 매년 봄에 열리는 '춘추연회'는 경복궁의 아름다움을 더욱 돋보이게 합니다.
2. **북촌 한옥마을**: 고풍스러운 한옥이 모여있는 곳으로, 전통 문화 체험이 가능합니다. '북촌 한옥마을 문화체험관'에서는 한복 체험부터 종이만화, 한글 쓰기 등 다양한 프로그램이 준비되어 있습니다.
3. **인사동**: 서점, 미술관, 한식당이 많은 곳입니다. 특히 '인사동 문화관'에서는 서울의 역사와 문화를 이해하는 데 도움이 되는 전시를 볼 수 있습니다.
4. **광화문** 및 **명동**: 현대적인 쇼핑과 레스토랑이 즐비한 곳입니다. 광화문은 특히 젊은이들이 많은 곳으로, 스트리트 패션을 관찰하거나 밤거리에서 활기를 느낄 수 있습니다.

**2. 도시의 모습을 바라보는 뷰투어 코스**

1. **남산타워**: 서울의 상징적인 건물로, 꼭대기에서 펼쳐지는 360도의 경치가 압니다. 특히 밤이 되면 조명이 어우러져 더욱 아름다워집니다.
2. **서울타워**: 남산타워와 비슷한 위치로, 높이가 더 높기 때문에 더 넓은 전망을 볼 수 있습니다. 서울타워 내부에는 다양한 전시관과 레스토랑도 있습니다.
3. **북악산**: 서울의 중심부에 위치한 산으로, 서울의 경치를 조금 다른 관점에서 볼 수 있습니다. 특히 북악산 정상인 북악사에서도 좋은 전망을 볼 수 있습니다.
4. **서울숲**: 녹지 공간으로, 도시의 혼잡함에서 벗어날 수 있는 곳입니다. 또한, 서울숲 내부에는 '서울숲 아트프레젠트'라는 공간이 있어 예술과 자연을 함께 체험할 수 있습니다.

**3. 현대 문화를 만나는 코스**

1. **삼성동**: 현대 미술관이 많은 곳으로, '삼성 미술관', '아모리카나스 갤러리' 등이 있습니다. 또한, '코엑스'나 '아포카로포스' 등의 명소도 가까운 곳에 있습니다.
2. **이태원**: 외국인들이 많은 곳으로, 다양한 외국 음식을 즐길 수 있는 곳입니다. 또한, '이태원 글로컬문화센터'에서는 세계 각국의 문화 체험이 가능합니다.
3. **홍대**: 젊은이들의 문화가 넘치는 곳입니다. '홍대 롤링홀'은 특히 많은 사람들이 방문하는 곳입니다. 또한, '홍대 서점거리'에서는 독서와 문화를 만날 수 있습니다.
4. **강남**: 서울의 현대적 모습을 잘 보여주는 곳입니다. '강남역'을 중심으로 많은 고급 쇼핑몰과 레스토랑이 있습니다.

이러한 코스를 통해 서울의 다양한 모습을 한 번에 만나볼 수 있을 거예요. 각자의 취향에 맞춰 코스를 조절하시면 좋겠습니다. 즐거운 여행 되세요!
```

### Python code with AutoModel

```python
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


model_id = "rtzr/ko-gemma-2-9b-it"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

model.eval()
instruction = "서울의 유명한 관광 코스를 만들어줄래?"

messages = [
    {"role": "user", "content": f"{instruction}"}
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<end_of_turn>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=2048,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)

print(tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True))
```

```markdown
서울 관광 코스를 제안해드릴게요. 하루 종일 즐겁게 여행할 수 있는 루트로 구성했습니다.                                                    

### 1. 서울역사관 및 북촌한옥마을(오전)

- 서울역사관: 서울의 역사와 문화를 체험할 수 있는 곳입니다. 다양한 전시물과 상설전시를 통해 서울의 변화를 살펴볼 수 있습니다.
- 북촌한옥마을: 서울의 한옥을 보존하고 관리하는 곳입니다. 조선 시대의 분위기를 느낄 수 있으며, 한옥에서 문화 콘텐츠도 제공하는 곳도 많습니다.

### 2. 북악산 입장과 북악산 등산(오전)

- 북악산은 서울의 북쪽에 위치한 산으로, 서울 한복판에서도 자연을 만날 수 있는 곳입니다. 북악산 입구에서 등산을 시작하여, 북악산 정상까지 올라가면 서울의 전경을 볼 수 있습니다.

### 3. 종로 명동 쇼핑과 맛집 투어(낮)

- 명동: 다양한 쇼핑몰과 매장이 있는 곳입니다. 명동 쇼핑타운, 미스터트위스터, 미스터리마켓 등을 방문해보세요.
- 맛집 투어: 명동에는 다양한 지역 음식을 먹을 수 있는 곳이 많습니다. 떡볶이, 순대, 닭강정 등을 맛볼 수 있는 곳을 추천드립니다.

### 4. 서울시립미술관과 덕수궁(오후)

- 서울시립미술관: 현대미술을 전시하는 곳입니다. 특별전이 열린다면 방문해 볼 수 있습니다.
- 덕수궁: 조선시대의 궁궐입니다. 특히 봄에는 벚꽃이 아름답게 만발합니다.

### 5. 남산타워와 남산공원 산책(오후)

- 남산타워: 남산에 있는 관람대입니다. 남산타워에 올라가면 서울의 360도 전경을 볼 수 있습니다.
- 남산공원: 남산에 있는 공원입니다. 다양한 테마 공원과 조경이 잘 된 곳입니다. 남산공원을 산책하며 휴식을 취할 수 있습니다.

### 6. 명동 또는 이태원에서의 저녁 식사와 문화 활동(저녁)

- 명동: 다양한 전통적인 한국 음식을 먹을 수 있는 곳입니다. 또한, 명동은 밤에도 활기차게 활발한 문화 생활을 할 수 있는 곳입니다.
- 이태원: 외국인 관광객들이 많이 찾는 곳으로, 다양한 세계 음식을 먹을 수 있으며, 클럽이나 바가 많은 문화적 활동이 가능한 곳입니다.

이 코스는 하루 종일 활발하게 여행을 할 수 있도록 계획했습니다. 각 지역에 따라 이동 시간을 고려하시고, 개장 시간과 전시 일정 등을 미리 확인하시는 것이 좋습니다. 즐거운 여행 되세요!
```

### Quantized Versions through bitsandbytes

- *Using 8-bit precision*
- *Using 4-bit precision*

```python
# pip install bitsandbytes
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig


model_id = "rtzr/ko-gemma-2-9b-it"
quantization_config_8bit = BitsAndBytesConfig(load_in_8bit=True)
# quantization_config_4bit = BitsAndBytesConfig(load_in_4bit=True)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    quantization_config=quantization_config_8bit,
    # quantization_config=quantization_config_4bit,
    low_cpu_mem_usage=True,
)

model.eval()
instruction = "서울의 유명한 관광 코스를 만들어줄래?"

messages = [
    {"role": "user", "content": f"{instruction}"}
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<end_of_turn>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=2048,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)

print(tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True))
```

### VLLM Usage

When we use `vllm==0.5.1`, the gemma2 model cannot be loaded yet and the following [issue](https://github.com/vllm-project/vllm/issues/6237) occurs. So it is recommended to use `vllm/vllm-openai:latest` docker or [`vllm==0.5.0.post1`](https://github.com/vllm-project/vllm/releases/tag/v0.5.0.post1).

```bash
#!/bin/bash

VLLM_ATTENTION_BACKEND=FLASHINFER
MODEL_NAME="rtzr/ko-gemma-2-9b-it"

MODEL_PATH="YOUR_PATH/${MODEL_NAME}"
docker run --rm --gpus all   \
    -p 8000:8000  \
    --shm-size=12gb --ulimit memlock=-1 --ulimit stack=67108864 \
    -e VLLM_ATTENTION_BACKEND=${VLLM_ATTENTION_BACKEND} \
    -v $MODEL_PATH:/vllm-workspace/${MODEL_NAME} \
    vllm/vllm-openai:latest \
        --model ${MODEL_NAME} --dtype auto \
        --gpu-memory-utilization 0.8
```

## License

Gemma 2 License: <https://ai.google.dev/gemma/terms>

## Model Citation

```none
@article{RTZR,
  title={ko-gemma-2-9b-it},
  author={Return Zero Team},
  year={2024},
  url={https://huggingface.co/rtzr/ko-gemma-2-9b-it}
}
```

```none
@article{gemma_2024,
    title={Gemma},
    url={https://www.kaggle.com/m/3301},
    DOI={10.34740/KAGGLE/M/3301},
    publisher={Kaggle},
    author={Gemma Team},
    year={2024}
}
```
