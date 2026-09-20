---
license: apache-2.0
language:
- ar
- de
- el
- en
- es
- fr
- it
- ja
- ko
- nl
- pl
- pt
- vi
- zh
pipeline_tag: automatic-speech-recognition
tags:
- audio
- hf-asr-leaderboard
- speech-recognition
- transcription
base_model:
- CohereLabs/cohere-transcribe-03-2026
library_name: transformers.js
---

# Cohere Transcribe

Cohere Transcribe is an open source release of a 2B parameter dedicated audio-in, text-out, automatic speech recognition (ASR) model. The model supports 14 languages.

Developed by: [Cohere](https://cohere.com) and [Cohere Labs](https://cohere.com/research).

* Point of Contact: [Cohere Labs](https://cohere.com/research)
* License: Apache 2.0 without any addendums
* Model: `CohereLabs/cohere-transcribe-03-2026`
* Model Size: 2B


**Try Cohere Transcribe**

You can try out the model in our [Hugging Face Space](https://huggingface.co/spaces/CohereLabs/Cohere-Transcribe-WebGPU).

<video src="https://cdn-uploads.huggingface.co/production/uploads/61b253b7ac5ecaae3d1efe0c/K_MqlyC8a7O8huVujxV6x.mp4" autoplay controls loop></video>
  
## Model Details

**Input:** Audio waveform. Audio is automatically resampled to 16kHz if necessary during preprocessing. Similarly, multi-channel (stereo) inputs are averaged to produce a single channel signal.

**Output:** Text.

**Model Architecture:** Cohere Transcribe is built on a speech-optimized Transformer variant: a Conformer. Input audio waveforms are converted into a mel-spectrogram and then processed by a Conformer encoder that holds the majority of the model’s parameters. The encoder’s representations are then passed to a lightweight Transformer decoder that generates text tokens. Cohere Transcribe is trained using standard supervised cross-entropy.

**Languages covered:** The model supports 14 languages: English, German, French, Italian, Spanish, Portuguese, Greek, Dutch, Polish, Arabic, Vietnamese, Chinese (Mandarin), Japanese and Korean.

## Strengths and Limitations

Cohere Transcribe is a performant, dedicated ASR model intended for efficient speech transcription.

### Strengths

Cohere Transcribe demonstrates best-in-class transcription accuracy in 14 languages. As a dedicated speech recognition model, it is also efficient, benefitting from a real-time factor up to three times faster than that of other, dedicated ASR models in the same size range. The model was trained from scratch, and from the outset, we deliberately focused on maximizing transcription accuracy while keeping production readiness top-of-mind.

## Usage

### Transformers.js

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:

```sh
npm i @huggingface/transformers
```

**Example:** English audio transcription
```js
import { pipeline } from "@huggingface/transformers";

// Create automatic speech recognition pipeline
const transcriber = await pipeline(
  "automatic-speech-recognition",
  "onnx-community/cohere-transcribe-03-2026-ONNX",
  { dtype: "q4", device: "webgpu" },
);
const audio = "https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/cohere_asr-en.wav";
const output = await transcriber(audio, { max_new_tokens: 1024 });
console.log(output); // { text: "Insects were the first animals to take to the air. Their ability to fly helped them evade enemies more easily and find food and mates more efficiently." }
```

**Example:** French audio transcription

```js
import { pipeline } from "@huggingface/transformers";

// Create automatic speech recognition pipeline
const transcriber = await pipeline(
  "automatic-speech-recognition",
  "onnx-community/cohere-transcribe-03-2026-ONNX",
  { dtype: "q4", device: "webgpu" },
);
const audio = "https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/cohere_asr-fr.wav";
const output = await transcriber(audio, { max_new_tokens: 1024, language: "fr" });
console.log(output); // { text: "Les insectes ont été les premiers animaux à s’envoler. Leur capacité à voler leur a permis d’échapper plus facilement à leurs ennemis et de trouver plus efficacement de la nourriture et des compagnons." }
```

Here is the full list of supported languages: `"en"`, `"fr"`, `"de"`, `"es"`, `"it"`, `"pt"`, `"nl"`, `"pl"`, `"el"`, `"ar"`, `"ja"`, `"zh"`, `"vi"`, `"ko"`.

### Limitations

* **Single language.** The model performs best when remaining in-distribution of a single, pre-specified language amongst the 14 in the range it supports. It does not feature explicit, automatic language detection and exhibits inconsistent performance on code-switched audio.

* **Timestamps/Speaker diarization.** The model does not feature either of these.

* **Silence.** Like most AED speech models, Cohere Transcribe is eager to transcribe, even non-speech sounds. The model thus benefits from prepending a noise gate or VAD (voice activity detection) model in order to prevent low-volume, floor noise from turning into hallucinations.


### Model Card Contact
For errors or additional questions about details in this model card, contact [labs@cohere.com](mailto:labs@cohere.com) or raise an issue.


Terms of Use:
We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant 2 billion parameter model to researchers all over the world. This model is governed by an Apache 2.0 license.