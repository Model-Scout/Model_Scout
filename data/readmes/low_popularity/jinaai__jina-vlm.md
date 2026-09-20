---
library_name: transformers
pipeline_tag: image-text-to-text
license: cc-by-nc-4.0
tags:
- multimodal
- multilingual
- vlm
- vision-language
- qwen3
- siglip2
language:
- en
- zh
- ar
- pt
- ru
- tr
- de
- es
- fr
- it
- ja
- ko
- vi
- th
- id
- hi
- bn
- nl
- pl
- sv
- fi
- da
- "no"
- cs
- el
- he
- uk
- ro
- hu
- multilingual
base_model:
- Qwen/Qwen3-1.7B-Base
- google/siglip2-so400m-patch14-384
inference: false
---

<p align="center">
<img src="https://huggingface.co/datasets/jinaai/documentation-images/resolve/main/logo.webp" alt="Jina AI: Your Search Foundation, Supercharged!" width="150px">
</p>

# jina-vlm: Small Multilingual Vision Language Model

[Blog](https://jina.ai/news/jina-vlm-small-multilingual-vision-language-model/) | API | AWS | Azure | GCP | [Arxiv](https://arxiv.org/abs/2512.04032)

`jina-vlm` is a token-efficient 2.4B parameter vision-language model that achieves state-of-the-art multilingual VQA performance among open 2B-scale VLMs. The model couples a SigLIP2 vision encoder with a Qwen3 language decoder and makes use of image tiling and attention-pooling for token-efficient processing of arbitrary-resolution images.

![jina-vlm architecture](./assets/jvlm_architecture.png)

Built on [Qwen3-1.7B-Base](https://huggingface.co/Qwen/Qwen3-1.7B-Base) with [SigLIP2-So400M](https://huggingface.co/google/siglip2-so400m-patch14-384), it processes images via overlapping tiling with attention-based token pooling that reduces visual tokens by 4x while preserving spatial information. The model achieves the highest average score (72.3) across eight VQA benchmarks while leading on multilingual multimodal understanding (MMMB: 78.8, Multilingual MMBench: 74.3).

| Model | Params | VQA Avg | MMMB | MM-Bench | RealWorld QA |
|-------|--------|---------|------|----------|--------------|
| **jina-vlm** | 2.4B | **72.3** | **78.8** | **74.3** | **68.2** |
| Qwen2-VL-2B | 2.2B | 66.4 | 71.3 | 69.4 | 62.9 |
| Qwen3-VL-2B | 2.2B | 71.6 | 75.0 | 72.3 | 63.9 |
| InternVL3-2B | 2.2B | 69.2 | 73.6 | 71.9 | 64.3 |
| InternVL3.5-2B | 2.2B | 71.6 | 74.6 | 70.9 | 62.0 |


## Via Jina API

We provide an OpenAI-compatible API at `https://api-beta-vlm.jina.ai`. All requests require a Jina API key in the Authorization header, get your API key at [jina.ai](https://jina.ai).


### Image from URL

| Format | Example |
|--------|---------|
| HTTP/HTTPS URL | `https://example.com/image.jpg` |
| Base64 data URI | `data:image/jpeg;base64,/9j/4AAQ...` |

```bash
curl https://api-beta-vlm.jina.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -d '{
    "model": "jina-vlm",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "Describe this image"},
        {"type": "image_url", "image_url": {"url": "https://example.com/photo.jpg"}}
      ]
    }]
  }'
```


### Local image (base64)

```bash
curl https://api-beta-vlm.jina.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -d '{
    "model": "jina-vlm",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "What is in this image?"},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,'$(base64 -i image.jpg)'"}}
      ]
    }]
  }'
```


### Text-only query

```bash
curl https://api-beta-vlm.jina.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -d '{
    "model": "jina-vlm",
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
  }'
```

### Streaming response

Add `"stream": true` to receive tokens as they're generated:

```bash
curl https://api-beta-vlm.jina.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -d '{
    "model": "jina-vlm",
    "stream": true,
    "messages": [{"role": "user", "content": "Write a haiku about coding"}]
  }'
```

When the service is cold starting, you'll receive:

```json
{
  "error": {
    "message": "Model is loading, please retry in 30-60 seconds. Cold start takes ~30s after the service scales up.",
    "code": 503
  }
}
```

Simply retry your request after waiting.


## Local Installation

```bash
uv sync
```

For CUDA users with FlashAttention2 support:
```bash
uv sync --extra flash-attn
```

### Using the CLI

You can directly chat with `jina-vlm` using the `infer.py` CLI:

```bash
# Single image
python infer.py -i image.jpg -p "What's in this image?"

# Streaming output
python infer.py -i image.jpg -p "Describe this image" --stream

# Multiple images
python infer.py -i img1.jpg -i img2.jpg -p "Compare these images"

# Text-only
python infer.py -p "What is the capital of France?"
```

**Options:**
- `-m, --model`: Model path. Auto-detects local repo (if `config.json` exists) or falls back to `jinaai/jina-vlm` from HuggingFace.
- `-i, --image`: Image path, URL, or glob pattern (can specify multiple times).
- `-p, --prompt`: Text prompt (can specify multiple times).
- `--max-crops`: Maximum crops (default: 12).
- `--max-tokens`: Maximum output tokens (default: 1024).
- `--max-pixels`: Max pixels per image, larger images are resized preserving aspect ratio.
- `--stream`: Enable streaming output.

**Example:**

```bash
python infer.py -i assets/the_persistence_of_memory.jpg -p "Describe this picture"
```

<table>
<tr>
<td width="40%"><b>Input</b></td>
<td width="60%"><b>Output</b></td>
</tr>
<tr>
<td><img src="./assets/the_persistence_of_memory.jpg" width="100%"></td>
<td>

```
* Conversation 1/1
├── 🖼️Images: ['the_persistence_of_memory.jpg']
├── 📜Prompt: Describe this picture
└── 🧠Response: This image is a surreal painting
by Salvador Dalí, titled "The Persistence of
Memory." It features a dreamlike landscape with
a variety of melting clocks and other objects.
The central focus is a melting clock with a blue
face and yellow hands, which is hanging from a
branch...

Token usage: 1753 tokens (4.3%)
Generated in 8.68s | 20.04 tok/s
```

</td>
</tr>
</table>

### Using Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig

processor = AutoProcessor.from_pretrained(
    'jinaai/jina-vlm', use_fast=False, trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    'jinaai/jina-vlm',
    device_map='auto',
    trust_remote_code=True
)

image = 'https://picsum.photos/800/600'
conversation = [
    {
        'role': 'user',
        'content': [
            {'type': 'image', 'image': image},
            {'type': 'text', 'text': 'Describe this image'},
        ],
    }
]

text = processor.apply_chat_template(conversation, add_generation_prompt=True)
inputs = processor(text=[text], images=[image], padding='longest', return_tensors='pt')
inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

output = model.generate(
    **inputs,
    generation_config=GenerationConfig(max_new_tokens=512, do_sample=False),
    return_dict_in_generate=True,
    use_model_defaults=True,
)

response = processor.tokenizer.decode(
    output.sequences[0][inputs['input_ids'].shape[-1]:],
    skip_special_tokens=True
)
print(response)
```

<details>
<summary>Multi-image inference</summary>

```python
images = ['https://picsum.photos/id/1/800/600', 'https://picsum.photos/id/2/800/600']
conversation = [
    {
        'role': 'user',
        'content': [
            {'type': 'image', 'image': images[0]},
            {'type': 'image', 'image': images[1]},
            {'type': 'text', 'text': 'What is the difference between these images?'},
        ],
    }
]
text = processor.apply_chat_template(conversation, add_generation_prompt=True)
inputs = processor(text=[text], images=images, padding='longest', return_tensors='pt')
inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

output = model.generate(
    **inputs,
    generation_config=GenerationConfig(max_new_tokens=512, do_sample=False),
    return_dict_in_generate=True,
    use_model_defaults=True,
)
response = processor.tokenizer.decode(
    output.sequences[0][inputs['input_ids'].shape[-1]:],
    skip_special_tokens=True
)
print(response)
```

</details>

<details>
<summary>Text-only inference</summary>

```python
conversation = [
    {
        'role': 'user',
        'content': [
            {'type': 'text', 'text': 'Explain quantum computing in simple terms'},
        ],
    }
]
text = processor.apply_chat_template(conversation, add_generation_prompt=True)
inputs = processor(text=[text], padding='longest', return_tensors='pt')
inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

output = model.generate(
    **inputs,
    generation_config=GenerationConfig(max_new_tokens=512, do_sample=False),
    return_dict_in_generate=True,
    use_model_defaults=True,
)
response = processor.tokenizer.decode(
    output.sequences[0][inputs['input_ids'].shape[-1]:],
    skip_special_tokens=True
)
print(response)
```

</details>

<details>
<summary>Batch inference</summary>

```python
import torch
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig

processor = AutoProcessor.from_pretrained(
    'jinaai/jina-vlm', use_fast=False, trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    'jinaai/jina-vlm',
    device_map='auto',
    torch_dtype=torch.bfloat16,
    attn_implementation='flash_attention_2',
    trust_remote_code=True
)

images = [
    'https://picsum.photos/id/22/800/600',
    'https://picsum.photos/id/49/800/600'
]
conversations = [
    [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': images[0]},
                {'type': 'text', 'text': 'What is the man doing in this image?'},
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': images[1]},
                {'type': 'text', 'text': 'What country\'s flag is in this image?'},
            ],
        }
    ],
]

texts = processor.apply_chat_template(conversations, add_generation_prompt=True)
inputs = processor(text=texts, images=images, padding='longest', return_tensors='pt')
inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

output = model.generate(
    **inputs,
    generation_config=GenerationConfig(max_new_tokens=512, do_sample=False),
    return_dict_in_generate=True,
    use_model_defaults=True,
)

for idx in range(len(output.sequences)):
    gen_ids = output.sequences[idx][inputs['input_ids'].shape[-1]:]
    response = processor.tokenizer.decode(gen_ids, skip_special_tokens=True)
    print(f"Response {idx+1}: {response}")
```

</details>

<details>
<summary>Batch inference with mixed examples</summary>

```python
import torch
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig

processor = AutoProcessor.from_pretrained(
    'jinaai/jina-vlm', use_fast=False, trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    'jinaai/jina-vlm',
    device_map='auto',
    torch_dtype=torch.bfloat16,
    attn_implementation='flash_attention_2',
    trust_remote_code=True
)

images = [
    ['https://picsum.photos/id/22/800/600'],
    ['https://picsum.photos/id/49/800/600'],
    ['https://picsum.photos/id/0/800/600', 'https://picsum.photos/id/2/800/600'],
    [],
]
conversations = [
    [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': images[0][0]},
                {'type': 'text', 'text': 'What is the man doing in this image?'},
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': images[1][0]},
                {'type': 'text', 'text': 'What country\'s flag is in this image?'},
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': images[2][0]},
                {'type': 'image', 'image': images[2][1]},
                {'type': 'text', 'text': 'What is the difference between these two images?'},
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'Describe the concept of polymorphism in Computer Science'},
            ],
        }
    ],
]

texts = processor.apply_chat_template(conversations, add_generation_prompt=True)
inputs = processor(text=texts, images=images, padding='longest', return_tensors='pt')
inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

output = model.generate(
    **inputs,
    generation_config=GenerationConfig(max_new_tokens=512, do_sample=False),
    return_dict_in_generate=True,
    use_model_defaults=True,
)

for idx in range(len(output.sequences)):
    gen_ids = output.sequences[idx][inputs['input_ids'].shape[-1]:]
    response = processor.tokenizer.decode(gen_ids, skip_special_tokens=True)
    print(f"Response {idx+1}: {response}")
```

</details>

<details>
<summary>Feature extraction</summary>

```python
import torch
from transformers import AutoModel, AutoProcessor

processor = AutoProcessor.from_pretrained(
    'jinaai/jina-vlm', use_fast=False, trust_remote_code=True
)
model = AutoModel.from_pretrained(
    'jinaai/jina-vlm',
    device_map='auto',
    torch_dtype=torch.bfloat16,
    attn_implementation='flash_attention_2',
    trust_remote_code=True
)

images = [
    ['https://picsum.photos/id/22/800/600'],
    ['https://picsum.photos/id/49/800/600'],
    ['https://picsum.photos/id/0/800/600', 'https://picsum.photos/id/2/800/600'],
    [],
]
conversations = [
    [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': images[0][0]},
                {'type': 'text', 'text': 'What is the man doing in this image?'},
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': images[1][0]},
                {'type': 'text', 'text': 'What country\'s flag is in this image?'},
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': images[2][0]},
                {'type': 'image', 'image': images[2][1]},
                {'type': 'text', 'text': 'What is the difference between these two images?'},
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'Describe the concept of polymorphism in Computer Science'},
            ],
        }
    ],
]

texts = processor.apply_chat_template(conversations, add_generation_prompt=True)
inputs = processor(text=texts, images=images, padding='longest', return_tensors='pt')
inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

output = model(**inputs)
print(output)
```

</details>

### Using vLLM

The vLLM [project](https://github.com/vllm-project/vllm) and [documentation](https://docs.vllm.ai/en/latest/).

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model='jinaai/jina-vlm',
    runner='generate',
    trust_remote_code=True,
    dtype='bfloat16',  # or float16, float32
    hf_overrides={'_attn_implementation': 'flash_attention_2'},
)
conversations = [
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/800/600'
                    }
                },
                {'type': 'text', 'text': 'Describe this image'}
            ],
        }
    ]
]
response = llm.chat(
    messages=conversations,
    add_generation_prompt=True,
    chat_template_kwargs={
        'always_start_with_space': True,
        'image_prompt_token': '<|image|>',
    },
    sampling_params=SamplingParams(
        temperature=0.0,
        n=1,
        max_tokens=64,
        top_p=1.0,
        repetition_penalty=1.0,
        top_k=0,
    ),
)
print([r.outputs[0].text for r in response])
```

<details>
<summary>Multi-image inference</summary>

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model='jinaai/jina-vlm',
    runner='generate',
    trust_remote_code=True,
    dtype='bfloat16',  # or float16, float32
    hf_overrides={'_attn_implementation': 'flash_attention_2'},
)
conversations = [
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/1/800/600'
                    }
                },
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/2/800/600'
                    }
                },
                {'type': 'text', 'text': 'What is the difference between these images?'}
            ],
        }
    ]
]
response = llm.chat(
    messages=conversations,
    add_generation_prompt=True,
    chat_template_kwargs={
        'always_start_with_space': True,
        'image_prompt_token': '<|image|>',
    },
    sampling_params=SamplingParams(
        temperature=0.0,
        n=1,
        max_tokens=64,
        top_p=1.0,
        repetition_penalty=1.0,
        top_k=0,
    ),
)
print([r.outputs[0].text for r in response])
```

</details>

<details>
<summary>Text-only inference</summary>

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model='jinaai/jina-vlm',
    runner='generate',
    trust_remote_code=True,
    dtype='bfloat16',  # or float16, float32
    hf_overrides={'_attn_implementation': 'flash_attention_2'},
)
conversations = [
    [
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'Explain quantum computing in simple terms'}
            ],
        }
    ]
]
response = llm.chat(
    messages=conversations,
    add_generation_prompt=True,
    chat_template_kwargs={
        'always_start_with_space': True,
        'image_prompt_token': '<|image|>',
    },
    sampling_params=SamplingParams(
        temperature=0.0,
        n=1,
        max_tokens=64,
        top_p=1.0,
        repetition_penalty=1.0,
        top_k=0,
    ),
)
print([r.outputs[0].text for r in response])
```

</details>

<details>
<summary>Batch inference</summary>

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model='jinaai/jina-vlm',
    runner='generate',
    trust_remote_code=True,
    dtype='bfloat16',  # or float16, float32
    hf_overrides={'_attn_implementation': 'flash_attention_2'},
)
conversations = [
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/22/800/600'
                    }
                },
                {'type': 'text', 'text': 'What is the man doing in this image?'}
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/49/800/600'
                    }
                },
                {'type': 'text', 'text': 'What country\'s flag is in this image?'}
            ],
        }
    ]
]
response = llm.chat(
    messages=conversations,
    add_generation_prompt=True,
    chat_template_kwargs={
        'always_start_with_space': True,
        'image_prompt_token': '<|image|>',
    },
    sampling_params=SamplingParams(
        temperature=0.0,
        n=1,
        max_tokens=64,
        top_p=1.0,
        repetition_penalty=1.0,
        top_k=0,
    ),
)
print([r.outputs[0].text for r in response])
```

</details>

<details>
<summary>Batch inference with mixed examples</summary>

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model='jinaai/jina-vlm',
    runner='generate',
    trust_remote_code=True,
    dtype='bfloat16',  # or float16, float32
    hf_overrides={'_attn_implementation': 'flash_attention_2'},
)
conversations = [
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/22/800/600'
                    }
                },
                {'type': 'text', 'text': 'What is the man doing in this image?'}
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/49/800/600'
                    }
                },
                {'type': 'text', 'text': 'What country\'s flag is in this image?'}
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/0/800/600'
                    }
                },
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/2/800/600'
                    }
                },
                {'type': 'text', 'text': 'What is the difference between these two images?'}
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'Describe the concept of polymorphism in Computer Science'}
            ],
        }
    ]
]
response = llm.chat(
    messages=conversations,
    add_generation_prompt=True,
    chat_template_kwargs={
        'always_start_with_space': True,
        'image_prompt_token': '<|image|>',
    },
    sampling_params=SamplingParams(
        temperature=0.0,
        n=1,
        max_tokens=64,
        top_p=1.0,
        repetition_penalty=1.0,
        top_k=0,
    ),
)
print([r.outputs[0].text for r in response])
```

</details>

<details>
<summary>Feature extraction</summary>

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model='jinaai/jina-vlm',
    runner='pooling',
    trust_remote_code=True,
    dtype='bfloat16',  # or float16, float32
    hf_overrides={'_attn_implementation': 'flash_attention_2'},
)
conversations = [
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/22/800/600'
                    }
                },
                {'type': 'text', 'text': 'What is the man doing in this image?'}
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/49/800/600'
                    }
                },
                {'type': 'text', 'text': 'What country\'s flag is in this image?'}
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/0/800/600'
                    }
                },
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': 'https://picsum.photos/id/2/800/600'
                    }
                },
                {'type': 'text', 'text': 'What is the difference between these two images?'}
            ],
        }
    ],
    [
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'Describe the concept of polymorphism in Computer Science'}
            ],
        }
    ]
]
prompts = llm.preprocess_chat(
    messages=conversations,
    chat_template_kwargs={
        'always_start_with_space': True,
        'image_prompt_token': '<|image|>',
    },
)
output = llm.encode(prompts, pooling_task='token_embed')
print([out.outputs.data for out in output])
```

</details>

## Evaluation

### Multilingual Understanding

| Model | MMMB ar | MMMB cn | MMMB en | MMMB avg | MMBench avg | Overall |
|-------|---------|---------|---------|----------|-------------|---------|
| **jina-vlm** | **76.9** | **80.0** | **82.0** | **78.8** | **74.3** | **59.6** |
| Qwen2-VL-2B | 68.3 | 74.2 | 78.3 | 71.3 | 69.4 | 53.8 |
| Qwen3-VL-2B | 72.7 | 75.7 | 80.7 | 75.0 | 72.3 | 58.2 |
| InternVL3-2B | 68.6 | 78.3 | 81.9 | 73.6 | 71.9 | 57.4 |
| InternVL3.5-2B | 68.5 | 77.7 | 80.2 | 74.6 | 70.9 | 58.0 |

### General VQA Tasks

| Model | AI2D | ChartQA | TextVQA | DocVQA | InfoVQA | OCRBench | SEED-2+ | CharXiv | Avg |
|-------|------|---------|---------|--------|---------|----------|---------|---------|-----|
| **jina-vlm** | **82.0** | **81.9** | **83.2** | 90.6 | 71.6 | 778 | 67.2 | **32.3**/63.5 | **72.3** |
| Qwen2-VL-2B | 74.7 | 73.5 | 79.7 | 89.2 | 64.0 | 809 | 62.4 | 23.3/55.0 | 66.4 |
| Qwen3-VL-2B | 76.9 | 77.2 | 79.5 | **92.3** | **71.9** | **858** | 67.3 | 28.8/62.3 | 71.6 |
| InternVL3-2B | 78.6 | 80.2 | 77.0 | 87.4 | 67.1 | 835 | 64.6 | 28.3/54.7 | 69.2 |
| InternVL3.5-2B | 78.8 | 80.7 | 76.5 | 88.5 | 69.3 | 836 | **68.0** | 31.6/**65.0** | 71.6 |

### Text-Only Performance

| Model | MMLU | MMLU-Pro | GSM-8K | ARC-C | HellaSwag |
|-------|------|----------|--------|-------|-----------|
| **jina-vlm** | 56.1 | **30.3** | 71.3 | **77.3** | **59.4** |
| Qwen3-1.7B | **62.6** | 46.4 | **75.3** | 73.4 | 59.0 |

## Citation

If you find `jina-vlm` useful in your research, please cite our [technical report](https://arxiv.org/abs/2512.04032):

```bibtex
@misc{koukounas2025jinavlm,
    title={Jina-VLM: Small Multilingual Vision Language Model},
    author={Andreas Koukounas and Georgios Mastrapas and Florian Hönicke and Sedigheh Eslami and Guillaume Roncari and Scott Martens and Han Xiao},
    year={2025},
    eprint={2512.04032},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    url={https://arxiv.org/abs/2512.04032},
}
```

## License

`jina-vlm` is licensed under CC BY-NC 4.0. For commercial usage inquiries, feel free to [contact us](https://jina.ai/contact-sales/).
