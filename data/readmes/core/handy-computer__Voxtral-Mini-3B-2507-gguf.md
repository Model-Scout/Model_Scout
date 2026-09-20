---
license: apache-2.0
base_model: mistralai/Voxtral-Mini-3B-2507
base_model_relation: quantized
library_name: transcribe.cpp
pipeline_tag: automatic-speech-recognition
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - nl
  - hi
tags:
  - gguf
  - transcribe.cpp
  - asr
  - speech-to-text
  - voxtral
  - audio-llm
  - multilingual
transcribe_cpp:
  schema_version: 2
  wer_fleurs_de:
    q8_0: 4.71
  wer_fleurs_en:
    q8_0: 3.89
  wer_fleurs_es:
    q8_0: 3.52
  wer_fleurs_fr:
    q8_0: 4.51
  wer_fleurs_hi:
    q8_0: 8.93
  wer_fleurs_it:
    q8_0: 2.56
  wer_fleurs_nl:
    q8_0: 6.57
  wer_fleurs_pt:
    q8_0: 3.84
  wer_librispeech_test_clean:
    bf16: 1.88
    f16: 1.89
    q8_0: 1.87
    q6_k: 1.87
    q5_k_m: 1.91
    q4_k_m: 1.94
  rtf_m4_max:
    cpu: 2.12
    metal: 13.42
  rtf_ryzen_4750u:
    cpu: 0.56
    vulkan: 1.08
  streaming: false
  translate: true
  lang_detect: true
  timestamps: none
---

# Voxtral-Mini-3B-2507: transcribe.cpp GGUF

GGUF conversions of [mistralai/Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) for use
with [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp).

Ported from upstream commit
[3060fe3](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507/commit/3060fe3),
pinned 2026-06-06.
Validated against the Transformers reference at transcribe.cpp commit
[483c122](https://github.com/handy-computer/transcribe.cpp/tree/483c122)
on 2026-06-06.

Offline audio-LLM speech-to-text and speech translation. A Whisper-large-v3
bidirectional audio encoder feeds a 4-frame-group projector (375 audio tokens
per 30 s chunk) into a Ministral-3B causal LM (30 layers, GQA 32/8, NEOX RoPE,
SwiGLU) via audio-token injection. Takes a 16 kHz mono WAV and produces a
transcript via greedy decoding; speech translation runs through the
mistral-common instruct template. The smaller sibling of Voxtral Small 24B —
same encoder, projector, log-mel frontend, and tekken tokenizer, with a 3B
decoder in place of Mistral-Small-24B.


## Downloads

| Quantization | Download | Size | WER (LibriSpeech test-clean) |
| --- | --- | ---: | ---: |
| BF16 | [Voxtral-Mini-3B-2507-BF16.gguf](https://huggingface.co/handy-computer/Voxtral-Mini-3B-2507-gguf/resolve/main/Voxtral-Mini-3B-2507-BF16.gguf) | 9.37 GB | 1.88% |
| F16 | [Voxtral-Mini-3B-2507-F16.gguf](https://huggingface.co/handy-computer/Voxtral-Mini-3B-2507-gguf/resolve/main/Voxtral-Mini-3B-2507-F16.gguf) | 9.38 GB | 1.89% |
| Q8_0 | [Voxtral-Mini-3B-2507-Q8_0.gguf](https://huggingface.co/handy-computer/Voxtral-Mini-3B-2507-gguf/resolve/main/Voxtral-Mini-3B-2507-Q8_0.gguf) | 5.00 GB | 1.87% |
| Q6_K | [Voxtral-Mini-3B-2507-Q6_K.gguf](https://huggingface.co/handy-computer/Voxtral-Mini-3B-2507-gguf/resolve/main/Voxtral-Mini-3B-2507-Q6_K.gguf) | 3.87 GB | 1.87% |
| Q5_K_M | [Voxtral-Mini-3B-2507-Q5_K_M.gguf](https://huggingface.co/handy-computer/Voxtral-Mini-3B-2507-gguf/resolve/main/Voxtral-Mini-3B-2507-Q5_K_M.gguf) | 3.46 GB | 1.91% |
| Q4_K_M | [Voxtral-Mini-3B-2507-Q4_K_M.gguf](https://huggingface.co/handy-computer/Voxtral-Mini-3B-2507-gguf/resolve/main/Voxtral-Mini-3B-2507-Q4_K_M.gguf) | 2.98 GB | 1.94% |

WER on the full LibriSpeech test-clean split (2,620 utterances), batch size 8, timestamps none. Figures without a commit were published before provenance was recorded.

Scored with the Whisper English text normalizer on an NVIDIA L40S. Same-machine
HuggingFace transformers reference (VoxtralForConditionalGeneration, BF16,
attn_implementation=eager, greedy): 1.87%; the BF16 GGUF matches within rounding.
The BF16-vs-reference parity is the family's tensor-level numerical gate — 43
checkpointed tensors within tolerance, transcript byte-exact.


## Usage

Build transcribe.cpp from source:

```bash
git clone git@github.com:handy-computer/transcribe.cpp.git
cd transcribe.cpp
cmake -B build && cmake --build build
```

Run on a 16 kHz mono WAV:

```bash
build/bin/transcribe-cli \
  -m Voxtral-Mini-3B-2507-Q8_0.gguf \
  input.wav
```

If your audio isn't already 16 kHz mono WAV, convert it first:

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

See the [transcribe.cpp model page](https://github.com/handy-computer/transcribe.cpp/blob/main/docs/models/voxtral-mini-3b-2507.md) for performance
numbers, numerical validation, and reproduction steps.

## License

Inherited from the base model: **Apache-2.0**. See the
[upstream model card](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) for full terms.

---

## Original Model Card

> The section below is reproduced from
> [mistralai/Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) at commit
> `3060fe3` for offline reference. The upstream card is the
> authoritative source.

# Voxtral Mini 1.0 (3B) - 2507

Voxtral Mini is an enhancement of [Ministral 3B](https://mistral.ai/news/ministraux), incorporating state-of-the-art audio input capabilities while retaining best-in-class text performance. It excels at speech transcription, translation and audio understanding.

Learn more about Voxtral in our blog post [here](https://mistral.ai/news/voxtral) and our [research paper](https://arxiv.org/abs/2507.13264).

## Key Features

Voxtral builds upon Ministral-3B with powerful audio understanding capabilities.
- **Dedicated transcription mode**: Voxtral can operate in a pure speech transcription mode to maximize performance. By default, Voxtral automatically predicts the source audio language and transcribes the text accordingly
- **Long-form context**: With a 32k token context length, Voxtral handles audios up to 30 minutes for transcription, or 40 minutes for understanding
- **Built-in Q&A and summarization**: Supports asking questions directly through audio. Analyze audio and generate structured summaries without the need for separate ASR and language models
- **Natively multilingual**: Automatic language detection and state-of-the-art performance in the world’s most widely used languages (English, Spanish, French, Portuguese, Hindi, German, Dutch, Italian)
- **Function-calling straight from voice**: Enables direct triggering of backend functions, workflows, or API calls based on spoken user intents
- **Highly capable at text**: Retains the text understanding capabilities of its language model backbone, Ministral-3B

## Benchmark Results

### Audio

Average word error rate (WER) over the FLEURS, Mozilla Common Voice and Multilingual LibriSpeech benchmarks:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64161701107962562e9b1006/puASxtajF1lDeGYPrRK5y.png)

### Text

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5dfcb1aada6d0311fd3d5448/iH9V8JVtMoaGlqJd6FIri.png)

## Usage

The model can be used with the following frameworks;
- [`vllm (recommended)`](https://github.com/vllm-project/vllm): See [here](#vllm-recommended)
- [`Transformers` 🤗](https://github.com/huggingface/transformers): See [here](#transformers-🤗)

**Notes**:

- `temperature=0.2` and `top_p=0.95` for chat completion (*e.g. Audio Understanding*) and `temperature=0.0` for transcription
- Multiple audios per message and multiple user turns with audio are supported
- System prompts are not yet supported

### vLLM (recommended)

We recommend using this model with [vLLM](https://github.com/vllm-project/vllm).

#### Installation

Make sure to install vllm >= 0.10.0, we recommend using `uv`:

```
uv pip install -U "vllm[audio]" --system
```

Doing so should automatically install [`mistral_common >= 1.8.1`](https://github.com/mistralai/mistral-common/releases/tag/v1.8.1).

To check:
```
python -c "import mistral_common; print(mistral_common.__version__)"
```

#### Offline

You can test that your vLLM setup works as expected by cloning the vLLM repo:

```sh
git clone https://github.com/vllm-project/vllm && cd vllm
```

and then running:

```sh
python examples/offline_inference/audio_language.py --num-audios 2 --model-type voxtral
```

#### Serve

We recommend that you use Voxtral-Small-24B-2507 in a server/client setting. 

1. Spin up a server:

```
vllm serve mistralai/Voxtral-Mini-3B-2507 --tokenizer_mode mistral --config_format mistral --load_format mistral
```

**Note:** Running Voxtral-Mini-3B-2507 on GPU requires ~9.5 GB of GPU RAM in bf16 or fp16. 


2. To ping the client you can use a simple Python snippet. See the following examples.


### Audio Instruct

Leverage the audio capabilities of Voxtral-Mini-3B-2507 to chat.

Make sure that your client has `mistral-common` with audio installed:

```sh
pip install --upgrade mistral_common\[audio\]
```

<details>
  <summary>Python snippet</summary>

```py
from mistral_common.protocol.instruct.messages import TextChunk, AudioChunk, UserMessage, AssistantMessage, RawAudio
from mistral_common.audio import Audio
from huggingface_hub import hf_hub_download

from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://<your-server-host>:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id

obama_file = hf_hub_download("patrickvonplaten/audio_samples", "obama.mp3", repo_type="dataset")
bcn_file = hf_hub_download("patrickvonplaten/audio_samples", "bcn_weather.mp3", repo_type="dataset")

def file_to_chunk(file: str) -> AudioChunk:
    audio = Audio.from_file(file, strict=False)
    return AudioChunk.from_audio(audio)

text_chunk = TextChunk(text="Which speaker is more inspiring? Why? How are they different from each other?")
user_msg = UserMessage(content=[file_to_chunk(obama_file), file_to_chunk(bcn_file), text_chunk]).to_openai()

print(30 * "=" + "USER 1" + 30 * "=")
print(text_chunk.text)
print("\n\n")

response = client.chat.completions.create(
    model=model,
    messages=[user_msg],
    temperature=0.2,
    top_p=0.95,
)
content = response.choices[0].message.content

print(30 * "=" + "BOT 1" + 30 * "=")
print(content)
print("\n\n")
# The speaker who is more inspiring is the one who delivered the farewell address, as they express
# gratitude, optimism, and a strong commitment to the nation and its citizens. They emphasize the importance of
# self-government and active citizenship, encouraging everyone to participate in the democratic process. In contrast,
# the other speaker provides a factual update on the weather in Barcelona, which is less inspiring as it
# lacks the emotional and motivational content of the farewell address.

# **Differences:**
# - The farewell address speaker focuses on the values and responsibilities of citizenship, encouraging active participation in democracy.
# - The weather update speaker provides factual information about the temperature in Barcelona, without any emotional or motivational content.


messages = [
    user_msg,
    AssistantMessage(content=content).to_openai(),
    UserMessage(content="Ok, now please summarize the content of the first audio.").to_openai()
]
print(30 * "=" + "USER 2" + 30 * "=")
print(messages[-1]["content"])
print("\n\n")

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.2,
    top_p=0.95,
)
content = response.choices[0].message.content
print(30 * "=" + "BOT 2" + 30 * "=")
print(content)
```
</details>

#### Transcription

Voxtral-Mini-3B-2507 has powerful transcription capabilities! 

Make sure that your client has `mistral-common` with audio installed:

```sh
pip install --upgrade mistral_common\[audio\]
```

<details>
  <summary>Python snippet</summary>

```python
from mistral_common.protocol.transcription.request import TranscriptionRequest
from mistral_common.protocol.instruct.messages import RawAudio
from mistral_common.audio import Audio
from huggingface_hub import hf_hub_download

from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://<your-server-host>:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id

obama_file = hf_hub_download("patrickvonplaten/audio_samples", "obama.mp3", repo_type="dataset")
audio = Audio.from_file(obama_file, strict=False)

audio = RawAudio.from_audio(audio)
req = TranscriptionRequest(model=model, audio=audio, language="en", temperature=0.0).to_openai(exclude=("top_p", "seed"))

response = client.audio.transcriptions.create(**req)
print(response)
```
</details>

### Transformers 🤗

Starting with `transformers >= 4.54.0` and above, you can run Voxtral natively!

Install Transformers:
```bash
pip install -U transformers
```

Make sure to have `mistral-common >= 1.8.1` installed with audio dependencies:
```bash
pip install --upgrade "mistral-common[audio]"
```

#### Audio Instruct

<details>
  <summary>➡️ multi-audio + text instruction</summary>

```python
from transformers import VoxtralForConditionalGeneration, AutoProcessor
import torch

device = "cuda"
repo_id = "mistralai/Voxtral-Mini-3B-2507"

processor = AutoProcessor.from_pretrained(repo_id)
model = VoxtralForConditionalGeneration.from_pretrained(repo_id, torch_dtype=torch.bfloat16, device_map=device)

conversation = [
    {
        "role": "user",
        "content": [
            {
                "type": "audio",
                "path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/mary_had_lamb.mp3",
            },
            {
                "type": "audio",
                "path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/winning_call.mp3",
            },
            {"type": "text", "text": "What sport and what nursery rhyme are referenced?"},
        ],
    }
]

inputs = processor.apply_chat_template(conversation)
inputs = inputs.to(device, dtype=torch.bfloat16)

outputs = model.generate(**inputs, max_new_tokens=500)
decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)

print("\nGenerated response:")
print("=" * 80)
print(decoded_outputs[0])
print("=" * 80)
```
</details>


<details>
  <summary>➡️ multi-turn</summary>

```python
from transformers import VoxtralForConditionalGeneration, AutoProcessor
import torch

device = "cuda"
repo_id = "mistralai/Voxtral-Mini-3B-2507"

processor = AutoProcessor.from_pretrained(repo_id)
model = VoxtralForConditionalGeneration.from_pretrained(repo_id, torch_dtype=torch.bfloat16, device_map=device)

conversation = [
    {
        "role": "user",
        "content": [
            {
                "type": "audio",
                "path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/obama.mp3",
            },
            {
                "type": "audio",
                "path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/bcn_weather.mp3",
            },
            {"type": "text", "text": "Describe briefly what you can hear."},
        ],
    },
    {
        "role": "assistant",
        "content": "The audio begins with the speaker delivering a farewell address in Chicago, reflecting on his eight years as president and expressing gratitude to the American people. The audio then transitions to a weather report, stating that it was 35 degrees in Barcelona the previous day, but the temperature would drop to minus 20 degrees the following day.",
    },
    {
        "role": "user",
        "content": [
            {
                "type": "audio",
                "path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/winning_call.mp3",
            },
            {"type": "text", "text": "Ok, now compare this new audio with the previous one."},
        ],
    },
]

inputs = processor.apply_chat_template(conversation)
inputs = inputs.to(device, dtype=torch.bfloat16)

outputs = model.generate(**inputs, max_new_tokens=500)
decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)

print("\nGenerated response:")
print("=" * 80)
print(decoded_outputs[0])
print("=" * 80)
```
</details>


<details>
  <summary>➡️ text only</summary>

```python
from transformers import VoxtralForConditionalGeneration, AutoProcessor
import torch

device = "cuda"
repo_id = "mistralai/Voxtral-Mini-3B-2507"

processor = AutoProcessor.from_pretrained(repo_id)
model = VoxtralForConditionalGeneration.from_pretrained(repo_id, torch_dtype=torch.bfloat16, device_map=device)

conversation = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Why should AI models be open-sourced?",
            },
        ],
    }
]

inputs = processor.apply_chat_template(conversation)
inputs = inputs.to(device, dtype=torch.bfloat16)

outputs = model.generate(**inputs, max_new_tokens=500)
decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)

print("\nGenerated response:")
print("=" * 80)
print(decoded_outputs[0])
print("=" * 80)
```
</details>


<details>
  <summary>➡️ audio only</summary>

```python
from transformers import VoxtralForConditionalGeneration, AutoProcessor
import torch

device = "cuda"
repo_id = "mistralai/Voxtral-Mini-3B-2507"

processor = AutoProcessor.from_pretrained(repo_id)
model = VoxtralForConditionalGeneration.from_pretrained(repo_id, torch_dtype=torch.bfloat16, device_map=device)

conversation = [
    {
        "role": "user",
        "content": [
            {
                "type": "audio",
                "path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/winning_call.mp3",
            },
        ],
    }
]

inputs = processor.apply_chat_template(conversation)
inputs = inputs.to(device, dtype=torch.bfloat16)

outputs = model.generate(**inputs, max_new_tokens=500)
decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)

print("\nGenerated response:")
print("=" * 80)
print(decoded_outputs[0])
print("=" * 80)
```
</details>


<details>
  <summary>➡️ batched inference</summary>

```python
from transformers import VoxtralForConditionalGeneration, AutoProcessor
import torch

device = "cuda"
repo_id = "mistralai/Voxtral-Mini-3B-2507"

processor = AutoProcessor.from_pretrained(repo_id)
model = VoxtralForConditionalGeneration.from_pretrained(repo_id, torch_dtype=torch.bfloat16, device_map=device)

conversations = [
    [
        {
            "role": "user",
            "content": [
                {
                    "type": "audio",
                    "path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/obama.mp3",
                },
                {
                    "type": "audio",
                    "path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/bcn_weather.mp3",
                },
                {
                    "type": "text",
                    "text": "Who's speaking in the speach and what city's weather is being discussed?",
                },
            ],
        }
    ],
    [
        {
            "role": "user",
            "content": [
                {
                    "type": "audio",
                    "path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/winning_call.mp3",
                },
                {"type": "text", "text": "What can you tell me about this audio?"},
            ],
        }
    ],
]

inputs = processor.apply_chat_template(conversations)
inputs = inputs.to(device, dtype=torch.bfloat16)

outputs = model.generate(**inputs, max_new_tokens=500)
decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)

print("\nGenerated responses:")
print("=" * 80)
for decoded_output in decoded_outputs:
    print(decoded_output)
    print("=" * 80)
```
</details>

#### Transcription

<details>
  <summary>➡️ transcribe</summary>

```python
from transformers import VoxtralForConditionalGeneration, AutoProcessor
import torch

device = "cuda"
repo_id = "mistralai/Voxtral-Mini-3B-2507"

processor = AutoProcessor.from_pretrained(repo_id)
model = VoxtralForConditionalGeneration.from_pretrained(repo_id, torch_dtype=torch.bfloat16, device_map=device)

inputs = processor.apply_transcription_request(language="en", audio="https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/obama.mp3", model_id=repo_id)
inputs = inputs.to(device, dtype=torch.bfloat16)

outputs = model.generate(**inputs, max_new_tokens=500)
decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)

print("\nGenerated responses:")
print("=" * 80)
for decoded_output in decoded_outputs:
    print(decoded_output)
    print("=" * 80)
```
</details>
