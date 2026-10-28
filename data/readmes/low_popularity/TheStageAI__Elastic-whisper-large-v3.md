---
base_model:
- openai/whisper-large-v3
base_model_relation: quantized
license: other
license_name: thestageai-elastic
pipeline_tag: automatic-speech-recognition
tags:
- audio
- automatic-speech-recognition
- speech-recognition
- whisper
- annthem
- qlip
- thestage
language:
- en
- zh
- de
- es
- ru
- ko
- fr
- ja
- pt
- tr
- pl
- ca
- nl
- ar
- sv
- it
- id
- hi
- fi
- vi
- he
- uk
- el
- ms
- cs
- ro
- da
- hu
- ta
- no
- th
- ur
- hr
- bg
- lt
- la
- mi
- ml
- cy
- sk
- te
- fa
- lv
- bn
- sr
- az
- sl
- kn
- et
- mk
- br
- eu
- is
- hy
- ne
- mn
- bs
- kk
- sq
- sw
- gl
- mr
- pa
- si
- km
- sn
- yo
- so
- af
- oc
- ka
- be
- tg
- sd
- gu
- am
- yi
- lo
- uz
- fo
- ht
- ps
- tk
- nn
- mt
- sa
- lb
- my
- bo
- tl
- mg
- as
- tt
- haw
- ln
- ha
- ba
- jw
- su
- yue
---

# Elastic model: whisper-large-v3

## Overview

---

ElasticModels are the models produced by TheStage AI ANNA: Automated Neural Networks Accelerator. ANNA allows you to control model size, latency and quality with a simple slider movement, routing different compression algorithms to different layers. For each model, we have produced a series of optimized models:

- **XL**: Mathematically equivalent neural network, optimized with our DNN compiler.
- **L**: Near lossless model, with less than 1% degradation obtained on corresponding benchmarks.
- **M**: Faster model, with accuracy degradation less than 1.5%.
- **S**: The fastest model, with accuracy degradation less than 2%.

Models can be accessed via TheStage AI Python SDK: ElasticModels, or deployed as Docker containers with REST API endpoints (see Deploy section).

## System Requirements

---

| **Property**| **Value** |
 | ---  | ---  |
| **GPU** | L40s, RTX 4090, RTX 5090, H100 |
| **Python Version** | 3.10-3.12 |
| **CPU** | Intel/AMD x86_64 |
| **CUDA Version** | 12.8+ |


## TheStage AI Access Token Setup

---

Install TheStage AI CLI and setup API token:

```bash
pip install thestage
thestage config set --access-token <YOUR_ACCESS_TOKEN>
```

## ElasticModels

---

Elastic Models provides the same interface as HuggingFace Transformers. Here is an example of how to use the whisper-large-v3 model.

### Installation

```bash
pip install 'thestage-elastic-models[nvidia]' \
    --extra-index-url https://thestage.jfrog.io/artifactory/api/pypi/pypi-thestage-ai-production/simple
pip install datasets==3.6.0 librosa soundfile  # only needed to load audio for the example below
```

### Usage

```python
import torch
from elastic_models.transformers import AutoModelForSpeechSeq2Seq
from transformers import AutoProcessor

model_name = "openai/whisper-large-v3"
hf_token = ''
device = torch.device("cuda")

processor = AutoProcessor.from_pretrained(
    model_name, token=hf_token
)
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_name,
    token=hf_token,
    torch_dtype=torch.float16,
    mode='S'
).to(device)

# Load audio file
from datasets import load_dataset
dataset = load_dataset(
    "hf-internal-testing/librispeech_asr_dummy",
    "clean", split="validation"
)
audio_sample = dataset[0]["audio"]

# Process audio
input_features = processor(
    audio_sample["array"],
    sampling_rate=audio_sample["sampling_rate"],
    return_tensors="pt"
).input_features.to(device, dtype=torch.float16)

# Generate transcription
with torch.inference_mode():
    predicted_ids = model.generate(input_features)

transcription = processor.batch_decode(
    predicted_ids, skip_special_tokens=True
)[0]

print(f"Transcription: {transcription}")
```


## Quality Benchmarks

---

We have evaluated the models using the Hugging Face Open ASR Leaderboard methodology. For each model size (S, M, L, XL), we report Word Error Rate (WER) on standard English and multilingual speech recognition benchmarks.

![Quality Benchmarking](https://cdn.thestage.ai/production/cms_file_upload/1773836677-0b071e8b-3253-42c9-95fc-acdf8f4096b6/Elastic_Whisper_Large_WER.png)

### Open ASR Leaderboard (English, WER %)

| **Dataset**| **S**| **M**| **L**| **XL**| **Original** |
 | ---  | ---  | ---  | ---  | ---  | ---  |
| **LibriSpeech Clean** | 1.89 | 1.88 | 1.87 | 1.88 | 1.88 |
| **LibriSpeech Other** | 3.71 | 3.69 | 3.69 | 3.69 | 3.68 |
| **SPGISpeech** | 2.92 | 2.9 | 2.91 | 2.95 | 2.95 |
| **TED-LIUM** | 3.81 | 3.77 | 3.8 | 3.85 | 3.84 |
| **VoxPopuli** | 8.33 | 8.45 | 8.41 | 9.28 | 9.17 |
| **GigaSpeech** | 9.97 | 10.01 | 10.01 | 10.01 | 10.01 |
| **Earnings-22** | 11.23 | 11.2 | 11.21 | 11.27 | 11.24 |
| **AMI** | 16.13 | 16.1 | 16.04 | 16.08 | 16.16 |
| **Mean WER** | 7.25 | 7.25 | 7.24 | 7.38 | 7.37 |


### Multilingual (WER %)

| **Dataset**| **S**| **M**| **L**| **XL**| **Original** |
 | ---  | ---  | ---  | ---  | ---  | ---  |
| **CoVoST2 DE** | 5.83 | 5.79 | 5.81 | 5.8 | 5.79 |
| **CoVoST2 ES** | 4.32 | 4.28 | 4.3 | 4.3 | 4.3 |
| **CoVoST2 FR** | 10.86 | 10.83 | 10.82 | 10.85 | 10.8 |
| **CoVoST2 IT** | 5.24 | 5.23 | 5.25 | 5.22 | 5.21 |
| **CoVoST2 PT** | 3.7 | 4.15 | 4.11 | 4.11 | 4.12 |
| **FLEURS DE** | 3.82 | 3.86 | 3.85 | 3.84 | 3.86 |
| **FLEURS ES** | 2.56 | 2.55 | 2.54 | 2.55 | 2.56 |
| **FLEURS FR** | 5.15 | 5.26 | 5.22 | 5.24 | 5.26 |
| **FLEURS IT** | 2.39 | 2.47 | 2.41 | 2.42 | 2.42 |
| **FLEURS PT** | 3.66 | 3.68 | 3.7 | 3.67 | 3.67 |
| **MLS French** | 4.69 | 4.68 | 4.7 | 4.68 | 4.68 |
| **MLS German** | 4.42 | 4.41 | 4.42 | 4.46 | 4.45 |
| **MLS Italian** | 8.95 | 8.94 | 8.92 | 8.92 | 8.94 |
| **MLS Portuguese** | 5.7 | 5.61 | 5.57 | 5.52 | 5.58 |
| **MLS Spanish** | 2.9 | 2.93 | 2.93 | 2.92 | 2.86 |
| **Mean WER** | 4.94 | 4.98 | 4.97 | 4.97 | 4.97 |


## Datasets

---

### English (Open ASR Leaderboard)

- **LibriSpeech Clean**: Read English speech from audiobooks, recorded in clean conditions. Tests baseline transcription accuracy on clear, well-articulated speech.
- **LibriSpeech Other**: Read English speech from audiobooks with more challenging acoustic conditions, including noisier recordings and less common speakers.
- **SPGISpeech**: Financial earnings calls and presentations, featuring domain-specific terminology, spontaneous speech, and diverse speaker accents.
- **TEDLium**: TED conference talks covering a wide range of topics, with diverse speakers, presentation styles, and varying audio quality.
- **VoxPopuli**: European Parliament event recordings in multiple languages, featuring political discourse, formal speech, and multilingual speakers.
- **GigaSpeech**: Large-scale multi-domain English speech corpus from audiobooks, podcasts, and YouTube, representing diverse acoustic conditions and speaking styles.
- **Earnings22**: Corporate earnings calls with financial terminology, multiple speakers, and telephone-quality audio.
- **AMI**: Meeting recordings with overlapping speech, distant microphones, and natural conversational dynamics.

### Multilingual

- **CoVoST2**: Common Voice Speech-To-Text 2. Built on Mozilla's Common Voice recordings, providing speech-to-text evaluation across 21 languages with diverse speakers, accents, and recording conditions.
- **FLEURS**: Few-shot Learning Evaluation of Universal Representations of Speech. Covers 102 languages with read speech from Wikipedia passages.
- **MLS**: Multilingual LibriSpeech. Derived from read audiobooks in 8 languages, providing large-scale multilingual ASR evaluation data.

## Metrics

---

- **WER (Word Error Rate)**: Measures the proportion of word-level errors (substitutions, insertions, deletions) in the transcription compared to the reference text. Lower values indicate better accuracy.


## Latency Benchmarks

---

We measured RTFx (Real-Time Factor) for each model size on various GPUs. RTFx indicates how many times faster than real-time the model transcribes audio. Higher RTFx is better.

![Latency Benchmarking](https://cdn.thestage.ai/production/cms_file_upload/1779128558-e11a4ca6-fc5b-4b7b-aeaf-7796436f0caf/Elastic_Whisper_Large_RTF_h100.png)

### RTFx, batch size 1

| **GPU/Model Size**| **S**| **M**| **L**| **XL**| **Original** |
 | ---  | ---  | ---  | ---  | ---  | ---  |
| **H100** | 68.9 | 68.4 | 64.3 | 63.8 | 26.1 |
| **L40s** | 59.4 | 59.4 | 58.3 | 54.6 | 18.1 |
| **GeForce RTX 5090** | 72 | 70 | 70 | 67 | 25 |
| **GeForce RTX 4090** | 69.3 | 67.9 | 67.2 | 64.3 | 38.5 |


### RTFx, batched

| **GPU/Model Size**| **S**| **M**| **L**| **XL**| **Original** |
 | ---  | ---  | ---  | ---  | ---  | ---  |
| **RTX 4090 (bs=24)** | 355 | 353 | 335 | 320 | 302 |
| **L40s (bs=32)** | 288 | 288 | 285 | 279 | 238 |
| **RTX 5090 (bs=32)** | 425 | 422 | 419 | 416 | 287 |
| **H100 (bs=64)** | 567 | 567 | 567 | 567 | 415 |


## Benchmarking Methodology

---

The benchmarking was performed on a single GPU using a 10-minute audio file resampled to 16kHz mono. RTFx (Real-Time Factor) is calculated as `audio_duration / transcription_time` — higher values mean faster-than-real-time transcription.

> **Algorithm summary:**
> 1. Load the whisper-large-v3 model with the specified size (S, M, L, XL, original).
> 2. Load a 10-minute audio file and resample to 16kHz mono.
> 3. Run a warm-up pass to initialize GPU caches.
> 4. Synchronize the GPU, record the start time.
> 5. Run the transcription pipeline with the specified batch size and chunk length.
> 6. Synchronize the GPU, record the end time.
> 7. Calculate RTFx as `audio_duration / time_taken`.


## Serving with Docker Image

---

For serving with Nvidia GPUs, we provide ready-to-go Docker containers with OpenAI-compatible API endpoints.
Using our containers you can set up an inference endpoint on any desired cloud/serverless providers as well as on-premise servers.
You can also use this container to run inference through TheStage AI platform.

### Prebuilt image from ECR

Pull docker image and start inference container. The container serves one model on one GPU; on a multi-GPU host `--gpus all` is fine, the model is placed on a single device:

```bash
docker pull public.ecr.aws/i3f7g5s7/thestage/elastic-models:0.2.4.post0-stt-streaming-v2-20261008-19026a9
```
```bash
docker run --rm -it \
  --name triton-stt \
  --gpus all \
  -p 127.0.0.1:<PORT>:<PORT> \
  -v "$HOME/.cache:/opt/project/.cache/" \
  -e MODEL_TYPE=<MODEL_TYPE> \
  -e PORT=<PORT> \
  -e AUTH_TOKEN=<AUTH_TOKEN> \
  -e MODEL_REPO=openai/whisper-large-v3 \
  -e MODEL_SIZE=<MODEL_SIZE> \
  -e MODEL_BATCH=<MODEL_BATCH> \
  -e PIPELINE_MAX_BATCH_SIZE=<PIPELINE_MAX_BATCH_SIZE> \
  -e CHUNK_LENGTH=<CHUNK_LENGTH> \
  -e PREPROCESSOR_WORKERS=<PREPROCESSOR_WORKERS> \
  -e MODEL_INSTANCES=<MODEL_INSTANCES> \
  -e PREPROCESSOR_QUEUE_DELAY=<PREPROCESSOR_QUEUE_DELAY> \
  -e MODEL_QUEUE_DELAY=<MODEL_QUEUE_DELAY> \
  -e ENSEMBLE_QUEUE_DELAY=<ENSEMBLE_QUEUE_DELAY> \
  -e HUGGINGFACE_ACCESS_TOKEN=<HUGGINGFACE_ACCESS_TOKEN> \
  -e THESTAGE_AUTH_TOKEN=<THESTAGE_ACCESS_TOKEN> \
  public.ecr.aws/i3f7g5s7/thestage/elastic-models:0.2.4.post0-stt-streaming-v2-20261008-19026a9
```

| **Parameter**              | **Description**                                                                                      |
|----------------------------|------------------------------------------------------------------------------------------------------|
| `<MODEL_TYPE>`             | `stt_streaming` for Whisper models. The image default is `stt_streaming_v2`, which serves Parakeet only. |
| `<PORT>`                   | Port the HTTP proxy listens on inside the container (default: 80).                                   |
| `<AUTH_TOKEN>`             | User-defined secret key to authenticate incoming requests.                                           |
| `<MODEL_SIZE>`             | Available: S, M, L, XL.                                                                              |
| `<MODEL_BATCH>`            | Maximum batch size for the model.                                                                    |
| `<PIPELINE_MAX_BATCH_SIZE>` | Maximum batch size for the ASR pipeline processing.                                                 |
| `<CHUNK_LENGTH>`           | Audio chunk length in seconds. 30 for any model; 10, 15, 20 only for `TheStageAI/thewhisper-large-v3(-turbo)` with a non-eager size. |
| `<PREPROCESSOR_WORKERS>`   | Number of preprocessor worker processes (e.g., 8).                                                   |
| `<MODEL_INSTANCES>`        | Number of Triton model instances (e.g., 1).                                                          |
| `<PREPROCESSOR_QUEUE_DELAY>` | Preprocessor dynamic-batching queue delay in microseconds (e.g., 10000).                           |
| `<MODEL_QUEUE_DELAY>`      | Model dynamic-batching queue delay in microseconds (e.g., 10000).                                    |
| `<ENSEMBLE_QUEUE_DELAY>`   | Ensemble dynamic-batching queue delay in microseconds (e.g., 10000).                                 |
| `<HUGGINGFACE_ACCESS_TOKEN>` | Hugging Face access token.                                                                         |
| `<THESTAGE_ACCESS_TOKEN>`  | TheStage token generated on the platform (Profile -> Access tokens).                                 |

## Invocation

---

### CLI

```bash
elastic-models-client client stt \
    --host 127.0.0.1 --port <PORT> --metadata-port <PORT> \
    --authorization <AUTH_TOKEN> \
    --sample sample.wav --lang-id en
```

### cURL

```bash
curl -X POST http://127.0.0.1:<PORT>/v1/audio/transcriptions \
    -H "Authorization: Bearer <AUTH_TOKEN>" \
    -F "file=@sample.wav" \
    -F "model=whisper-large-v3-<MODEL_SIZE_LOWER>-cl<CHUNK_LENGTH>-bs<MODEL_BATCH>" \
    -F "language=en"
```

## Endpoint Parameters

---

### Method

> **POST** `/v1/audio/transcriptions`

### Header Parameters

> `Authorization`: `string`
>
> Bearer token for authentication; it must match the container's `AUTH_TOKEN`.

### Input Body

All fields are sent as `multipart/form-data`.

> `file` : `binary`
>
> The audio file to transcribe.

> `model` : `string`
>
> Specifies the model to use for transcription. Format: `whisper-large-v3-<size>-cl<chunk_length>-bs<batch_size>`, where `<size>` is `MODEL_SIZE` lowercased (`s`, `m`, `l`, `xl`), `<chunk_length>` is `CHUNK_LENGTH`, and `<batch_size>` is `MODEL_BATCH`. Example: `whisper-large-v3-s-cl15-bs1`.

> `language` : `string`
>
> Language of the audio (e.g., "en", "es", "fr").


## Links

---

* __Platform__: [app.thestage.ai](https://app.thestage.ai)
* __Subscribe for updates__: [TheStageAI X](https://x.com/TheStageAI)
* __Contact email__: contact@thestage.ai
