---
license: other
license_name: moonshine-community-license
license_link: https://github.com/moonshine-ai/moonshine/blob/main/LICENSE
base_model: UsefulSensors/moonshine-tiny-ko
base_model_relation: quantized
library_name: transcribe.cpp
pipeline_tag: automatic-speech-recognition
language:
  - ko
tags:
  - gguf
  - transcribe.cpp
  - asr
  - speech-to-text
  - moonshine
  - useful-sensors
  - encoder-decoder
transcribe_cpp:
  schema_version: 2
  cer_fleurs_ko:
    q8_0: 9.0
    f32: 8.97
    f16: 8.97
  rtf_m4_max:
    cpu: 89.48
    metal: 68.36
  rtf_ryzen_4750u:
    cpu: 20.5
    vulkan: 30.35
  streaming: false
  translate: false
  lang_detect: false
  timestamps: none
---

# moonshine-tiny-ko: transcribe.cpp GGUF

GGUF conversions of [UsefulSensors/moonshine-tiny-ko](https://huggingface.co/UsefulSensors/moonshine-tiny-ko) for use
with [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp).

Ported from upstream commit
[80995f0](https://huggingface.co/UsefulSensors/moonshine-tiny-ko/commit/80995f0),
pinned 2026-05-12.
Validated against the transformers reference at transcribe.cpp commit
[90bf720](https://github.com/handy-computer/transcribe.cpp/tree/90bf720)
on 2026-05-12.

UsefulSensors' Moonshine tiny fine-tuned on Korean. Same
encoder-decoder transformer architecture as moonshine-tiny (27M
parameters): consumes 16 kHz raw PCM via a three-layer Conv1d stem (no
STFT, no mel filterbank) and emits transcript-only output. Single-language
(ko); no translation, no language detection, no timestamps.


## Downloads

| Quantization | Download | Size | CER (FLEURS ko) |
| --- | --- | ---: | ---: |
| F32 | [moonshine-tiny-ko-F32.gguf](https://huggingface.co/handy-computer/moonshine-tiny-ko-gguf/resolve/main/moonshine-tiny-ko-F32.gguf) | 110 MB | 8.97% |
| F16 | [moonshine-tiny-ko-F16.gguf](https://huggingface.co/handy-computer/moonshine-tiny-ko-gguf/resolve/main/moonshine-tiny-ko-F16.gguf) | 59 MB | 8.97% |
| Q8_0 | [moonshine-tiny-ko-Q8_0.gguf](https://huggingface.co/handy-computer/moonshine-tiny-ko-gguf/resolve/main/moonshine-tiny-ko-Q8_0.gguf) | 35 MB | 9.00% |

CER on the full FLEURS ko split (382 utterances), batch sizes 1 and 8, timestamps none. Figures without a commit were published before provenance was recorded.

Decoded with the transcribe.cpp defaults (greedy, num_beams=1, max_length=192,
matching the upstream generation_config).

UsefulSensors does not publish a per-language CER number
for this variant. As a comparable baseline we ran the Transformers F32
reference (`MoonshineForConditionalGeneration`, fp32 on MPS) on the
same manifest: **8.99% CER**. The C++ F32/F16 numbers
above match the reference within bootstrap-CI noise; Q8_0 introduces
a small additional drift from F16 (typically within 0.1pp).


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
  -m moonshine-tiny-ko-Q8_0.gguf \
  input.wav
```

If your audio isn't already 16 kHz mono WAV, convert it first:

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

See the [transcribe.cpp model page](https://github.com/handy-computer/transcribe.cpp/blob/main/docs/models/moonshine.md) for performance
numbers, numerical validation, and reproduction steps.

## License

Inherited from the base model: **Moonshine AI Community License**. See the
[upstream model card](https://huggingface.co/UsefulSensors/moonshine-tiny-ko) for full terms.
This repository includes the license text
([`LICENSE`](https://huggingface.co/handy-computer/moonshine-tiny-ko-gguf/blob/main/LICENSE)) and a
[`NOTICE`](https://huggingface.co/handy-computer/moonshine-tiny-ko-gguf/blob/main/NOTICE) recording
how these files were derived from the original.

Free for research and non-commercial use. Commercial use requires
registering with Moonshine AI and is limited to organizations under
US$1M annual revenue; read the
[license](https://github.com/moonshine-ai/moonshine/blob/main/LICENSE)
before using it. Moonshine AI releases its English and streaming models
under MIT; only these legacy language fine-tunes carry this license.

Powered by Moonshine AI.

---

## Original Model Card

> The section below is reproduced from
> [UsefulSensors/moonshine-tiny-ko](https://huggingface.co/UsefulSensors/moonshine-tiny-ko) at commit
> `80995f0` for offline reference. The upstream card is the
> authoritative source.

# Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices

[[Paper]](https://huggingface.co/papers/2509.02523) [[Code]](https://github.com/moonshine-ai/moonshine) [[Installation]](https://github.com/usefulsensors/moonshine/blob/main/README.md)

This is the model card for running the automatic speech recognition (ASR) models (Moonshine models) trained and released by Moonshine AI (f.k.a Useful Sensors.) This model is part of the **Flavors of Moonshine** suite, tiny automatic speech recognition (ASR) models specialized for a range of underrepresented languages. Moonshine models are optimized for fast and accurate ASR on resource-constrained devices, outperforming comparably sized Whisper Tiny models.

Following [Model Cards for Model Reporting (Mitchell et al.)](https://arxiv.org/abs/1810.03993), we're providing some information about the automatic speech recognition model. More information on how these models were trained and evaluated can be found [in the paper](https://huggingface.co/papers/2509.02523). Note, a lot of the text has been copied verbatim from the [model card](https://github.com/openai/whisper/blob/main/model-card.md) for the Whisper model developed by OpenAI, because both models serve identical purposes, and carry identical risks.

## Usage

Moonshine is supported in Hugging Face 🤗 Transformers. To run the model, first install the Transformers library. For this example, we'll also install 🤗 Datasets to load toy audio dataset from the Hugging Face Hub, and 🤗 Accelerate to reduce the model loading time:

```bash
pip install --upgrade pip
pip install --upgrade transformers datasets[audio]
```

```python
from transformers import MoonshineForConditionalGeneration, AutoProcessor
from datasets import load_dataset, Audio
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model = MoonshineForConditionalGeneration.from_pretrained('UsefulSensors/moonshine-tiny-ko').to(device).to(torch_dtype)
processor = AutoProcessor.from_pretrained('UsefulSensors/moonshine-tiny-ko')

dataset = load_dataset('UsefulSensors/multilingual_examples', split='ko')
dataset = dataset.cast_column("audio", Audio(processor.feature_extractor.sampling_rate))
sample = dataset[0]["audio"]

inputs = processor(
    sample["array"], 
    return_tensors="pt",
    sampling_rate=processor.feature_extractor.sampling_rate
)
inputs = inputs.to(device, torch_dtype)

# to avoid hallucination loops, we limit the maximum length of the generated text based expected number of tokens per second
token_limit_factor = 13 / processor.feature_extractor.sampling_rate 
seq_lens = inputs.attention_mask.sum(dim=-1)
max_length = int((seq_lens * token_limit_factor).max().item())

generated_ids = model.generate(**inputs, max_length=max_length)
print(processor.decode(generated_ids[0], skip_special_tokens=True))
```

## Model Details

This Moonshine model is trained for the speech recognition task, capable of transcribing Korean speech audio into Korean text. Moonshine AI developed the models to support their business direction of developing real time speech transcription products based on low cost hardware. The following table shows comparisons of common ASR evaluations sets. For more information about evaluation, please refer to the paper.

| Size | Parameters | Fleurs (CER) ↓ | Common Voice 17 (CER) ↓ |
|:----:|:----------:|:------------------:|:------------------:|
| whisper tiny | 39 M       | 15.83                  | 37.27                    |
| whisper medium | 769 M       |  6.99                 | 9.38                 |
| moonshine tiny | 27 M       |          8.9        | 14.94                  |

### Release date

September 2025

### Model type

Sequence-to-sequence ASR (automatic speech recognition) and speech translation model

## Model Use

### Evaluated Use

The primary intended users of these models are AI developers that want to deploy Korean speech recognition systems in platforms that are severely constrained in memory capacity and computational resources. We recognize that once models are released, it is impossible to restrict access to only “intended” uses or to draw reasonable guidelines around what is or is not safe use.

The models are primarily trained and evaluated on Arabic ASR task. They may exhibit additional capabilities, particularly if fine-tuned on certain tasks like voice activity detection, speaker classification, or speaker diarization but have not been robustly evaluated in these areas. We strongly recommend that users perform robust evaluations of the models in a particular context and domain before deploying them.

In particular, we caution against using Moonshine models to transcribe recordings of individuals taken without their consent or purporting to use these models for any kind of subjective classification. We recommend against use in high-risk domains like decision-making contexts, where flaws in accuracy can lead to pronounced flaws in outcomes. The models are intended to transcribe Korean speech, use of the model for classification is not only not evaluated but also not appropriate, particularly to infer human attributes.

## Training Data

The models are trained on 72,000 hours of audio and the corresponding transcripts collected from the internet, as well as datasets openly available and accessible on HuggingFace. The open datasets used are listed in [the accompanying paper](https://huggingface.co/papers/2509.02523).

## Performance and Limitations

Our evaluations show that, the models exhibit greater accuracy on standard datasets over existing ASR systems of both similar and larger sizes. 

However, like any machine learning model, the predictions may include texts that are not actually spoken in the audio input (i.e. hallucination). We hypothesize that this happens because, given their general knowledge of language, the models combine trying to predict the next word in audio with trying to transcribe the audio itself.

In addition, the sequence-to-sequence architecture of the model makes it prone to generating repetitive texts, which can be mitigated to some degree by beam search and temperature scheduling but not perfectly. It is likely that this behavior and hallucinations may be worse for short audio segments, or segments where parts of words are cut off at the beginning or at the end of the segment.

## Broader Implications

We anticipate that Moonshine models’ transcription capabilities may be used for improving accessibility tools, especially for real-time transcription. The real value of beneficial applications built on top of Moonshine models suggests that the disparate performance of these models may have real economic implications.

There are also potential dual-use concerns that come with releasing Moonshine. While we hope the technology will be used primarily for beneficial purposes, making ASR technology more accessible could enable more actors to build capable surveillance technologies or scale up existing surveillance efforts, as the speed and accuracy allow for affordable automatic transcription and translation of large volumes of audio communication. Moreover, these models may have some capabilities to recognize specific individuals out of the box, which in turn presents safety concerns related both to dual use and disparate performance. In practice, we expect that the cost of transcription is not the limiting factor of scaling up surveillance projects.

## Project Page
Check out the blog post for more details: https://petewarden.com/2024/10/21/introducing-moonshine-the-new-state-of-the-art-for-speech-to-text/

## Citation
If you benefit from our work, please cite us:

```
@misc{king2025flavorsmoonshinetinyspecialized,
      title={Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices}, 
      author={Evan King and Adam Sabra and Manjunath Kudlur and James Wang and Pete Warden},
      year={2025},
      eprint={2509.02523},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://huggingface.co/papers/2509.02523}, 
}
```
