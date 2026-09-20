---
license: cc-by-4.0
base_model: nvidia/canary-1b-v2
base_model_relation: quantized
library_name: transcribe.cpp
pipeline_tag: automatic-speech-recognition
language:
  - bg
  - hr
  - cs
  - da
  - nl
  - en
  - et
  - fi
  - fr
  - de
  - el
  - hu
  - it
  - lv
  - lt
  - mt
  - pl
  - pt
  - ro
  - sk
  - sl
  - es
  - sv
  - ru
  - uk
tags:
  - gguf
  - transcribe.cpp
  - asr
  - speech-to-text
  - canary
  - multitask-aed
  - encoder-decoder
  - multilingual
  - translation
transcribe_cpp:
  schema_version: 2
  wer_fleurs_bg:
    q8_0: 9.22
  wer_fleurs_cs:
    q8_0: 8.56
  wer_fleurs_da:
    q8_0: 11.34
  wer_fleurs_de:
    q8_0: 4.46
  wer_fleurs_el:
    q8_0: 26.02
  wer_fleurs_en:
    q8_0: 4.47
  wer_fleurs_es:
    q8_0: 3.1
  wer_fleurs_et:
    q8_0: 12.72
  wer_fleurs_fi:
    q8_0: 8.86
  wer_fleurs_fr:
    q8_0: 5.09
  wer_fleurs_hr:
    q8_0: 8.4
  wer_fleurs_hu:
    q8_0: 13.06
  wer_fleurs_it:
    q8_0: 3.1
  wer_fleurs_lt:
    q8_0: 13.45
  wer_fleurs_lv:
    q8_0: 10.41
  wer_fleurs_mt:
    q8_0: 19.75
  wer_fleurs_nl:
    q8_0: 6.28
  wer_fleurs_pl:
    q8_0: 6.88
  wer_fleurs_pt:
    q8_0: 4.5
  wer_fleurs_ro:
    q8_0: 6.87
  wer_fleurs_ru:
    q8_0: 7.83
  wer_fleurs_sk:
    q8_0: 6.84
  wer_fleurs_sl:
    q8_0: 12.76
  wer_fleurs_sv:
    q8_0: 9.74
  wer_fleurs_uk:
    q8_0: 10.58
  wer_librispeech_test_clean:
    f32: 1.92
    f16: 1.92
    q8_0: 1.91
    q6_k: 1.94
    q5_k_m: 1.93
    q4_k_m: 1.91
  rtf_m4_max:
    cpu: 25.08
    metal: 98.25
  rtf_ryzen_4750u:
    cpu: 8.32
    vulkan: 14.13
  streaming: false
  translate: true
  lang_detect: false
  timestamps: none
---

# canary-1b-v2: transcribe.cpp GGUF

GGUF conversions of [nvidia/canary-1b-v2](https://huggingface.co/nvidia/canary-1b-v2) for use
with [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp).

Ported from upstream commit
[87bc526](https://huggingface.co/nvidia/canary-1b-v2/commit/87bc526),
pinned 2026-05-08.
Validated against the NeMo reference at transcribe.cpp commit
[db53eda](https://github.com/handy-computer/transcribe.cpp/tree/db53eda)
on 2026-05-08.

Offline multilingual speech-to-text and translation across 25 European
languages. A 978M-parameter multitask AED with a 32-layer FastConformer
encoder and an 8-layer Transformer decoder. Supports automatic speech
recognition for any of the 25 supported languages, plus translation
between supported language pairs (per the upstream model card). Takes
a 16 kHz mono WAV and produces a transcript. Not a streaming model;
word and segment timestamps from the upstream model are not exposed in
the v1 port.


## Downloads

| Quantization | Download | Size | WER (LibriSpeech test-clean) |
| --- | --- | ---: | ---: |
| F32 | [canary-1b-v2-F32.gguf](https://huggingface.co/handy-computer/canary-1b-v2-gguf/resolve/main/canary-1b-v2-F32.gguf) | 3.92 GB | 1.92% |
| F16 | [canary-1b-v2-F16.gguf](https://huggingface.co/handy-computer/canary-1b-v2-gguf/resolve/main/canary-1b-v2-F16.gguf) | 1.97 GB | 1.92% |
| Q8_0 | [canary-1b-v2-Q8_0.gguf](https://huggingface.co/handy-computer/canary-1b-v2-gguf/resolve/main/canary-1b-v2-Q8_0.gguf) | 1.14 GB | 1.91% |
| Q6_K | [canary-1b-v2-Q6_K.gguf](https://huggingface.co/handy-computer/canary-1b-v2-gguf/resolve/main/canary-1b-v2-Q6_K.gguf) | 932 MB | 1.94% |
| Q5_K_M | [canary-1b-v2-Q5_K_M.gguf](https://huggingface.co/handy-computer/canary-1b-v2-gguf/resolve/main/canary-1b-v2-Q5_K_M.gguf) | 837 MB | 1.93% |
| Q4_K_M | [canary-1b-v2-Q4_K_M.gguf](https://huggingface.co/handy-computer/canary-1b-v2-gguf/resolve/main/canary-1b-v2-Q4_K_M.gguf) | 735 MB | 1.91% |

WER on the full LibriSpeech test-clean split (2,620 utterances), batch size 1, timestamps none. Figures without a commit were published before provenance was recorded.

Greedy decoding, no external LM. F32 reference baseline: 1.92%. NVIDIA's
self-reported number on the upstream model card is 2.18%; our F32 port comes in
slightly under the upstream-reported number (Δ −0.26pp) and is likely down to
scoring differences.


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
  -m canary-1b-v2-Q8_0.gguf \
  input.wav
```

If your audio isn't already 16 kHz mono WAV, convert it first:

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

See the [transcribe.cpp model page](https://github.com/handy-computer/transcribe.cpp/blob/main/docs/models/canary-1b-v2.md) for performance
numbers, numerical validation, and reproduction steps.

## License

Inherited from the base model: **CC-BY-4.0**. See the
[upstream model card](https://huggingface.co/nvidia/canary-1b-v2) for full terms.

---

## Original Model Card

> The section below is reproduced from
> [nvidia/canary-1b-v2](https://huggingface.co/nvidia/canary-1b-v2) at commit
> `87bc526` for offline reference. The upstream card is the
> authoritative source.

## <span style="color:#ffb300;">🐤 Canary 1B v2: Multitask Speech Transcription and Translation Model </span>


**``Canary-1b-v2``** is a powerful 1-billion parameter model built for high-quality speech transcription and translation across 25 European languages.

It excels at both automatic speech recognition (ASR) and speech translation (AST), supporting:

* **Speech Transcription (ASR) for 25 languages**
* **Speech Translation (AST) from English → 24 languages**
* **Speech Translation (AST) from 24 languages → English**


**Supported Languages:**  
Bulgarian (**bg**), Croatian (**hr**), Czech (**cs**), Danish (**da**), Dutch (**nl**), English (**en**), Estonian (**et**), Finnish (**fi**), French (**fr**), German (**de**), Greek (**el**), Hungarian (**hu**), Italian (**it**), Latvian (**lv**), Lithuanian (**lt**), Maltese (**mt**), Polish (**pl**), Portuguese (**pt**), Romanian (**ro**), Slovak (**sk**), Slovenian (**sl**), Spanish (**es**), Swedish (**sv**), Russian (**ru**), Ukrainian (**uk**)

🗣️ **Experience `Canary-1b-v2` in action** at [Hugging Face Demo](https://huggingface.co/spaces/nvidia/canary-1b-v2)

`Canary-1b-v2` model is ready for commercial/non-commercial use.


## <span style="color:#b37800;">License/Terms of Use:</span>

GOVERNING TERMS: Use of this model is governed by the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) license.

## <span style="color:#b37800;"> Discover more from NVIDIA:</span>
For documentation, deployment guides, enterprise-ready APIs, and the latest open models—including Nemotron and other cutting-edge speech, translation, and generative AI—visit the NVIDIA Developer Portal at [developer.nvidia.com](https://developer.nvidia.com).
Join the community to access tools, support, and resources to accelerate your development with NVIDIA’s NeMo, Riva, NIM, and foundation models.<br>

### <span style="color:#b37800;">Explore more from NVIDIA: </span><br>
What is [Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)?<br>
NVIDIA Developer [Nemotron](https://developer.nvidia.com/nemotron)<br>
[NVIDIA Riva Speech](https://developer.nvidia.com/riva?sortBy=developer_learning_library%2Fsort%2Ffeatured_in.riva%3Adesc%2Ctitle%3Aasc#demos)<br>
[NeMo Documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html)<br>


## <span style="color:#b37800;">Key Features</span>

**`Canary-1b-v2`** is a scaled and enhanced version of the Canary model family, offering:

* Support for **25 European languages**, expanding from the **4 languages** in [canary-1b](https://huggingface.co/nvidia/canary-1b)/[canary-1b-flash](nvidia/canary-1b-flash) to **21 additional languages**
* **State-of-the-art performance** among models of similar size
* **Comparable quality to models 3× larger**, while being up to **10× faster**
* Automatic **punctuation** and **capitalization**
* Accurate **word-level** and **segment-level** timestamps
* Segment-level timestamps also available for **translated outputs**
* Released under a **permissive CC BY 4.0 license**

`Canary-1b-v2` model is the first model from NeMo team that leveraged full Nvidia's Granary dataset \[1] \[2], showcasing its multitask and multilingual capabilities.

For full details on the model architecture, training methodology, datasets, and evaluation results, check out the **[Canary-1b-v2 Technical Report](https://arxiv.org/abs/2509.14128)**.

For a deeper glimpse into the Canary family of models, explore this comprehensive [NeMo tutorial on multitask speech models](https://github.com/NVIDIA/NeMo/blob/main/tutorials/asr/Canary_Multitask_Speech_Model.ipynb).




### Automatic Speech Recognition (ASR)

![ASR WER Comparison](plots/asr.png)

*Figure 1: ASR WER comparison across different models. This does not include Punctuation and Capitalisation errors.*

---

### Speech Translation (AST)

#### X → English

![AST X-En Comparison](plots/x_en.png)

*Figure 2: AST X → En COMET scores comparison across different models*

#### English → X


![AST En-X Comparison](plots/en_x.png)

*Figure 3: AST En → X COMET scores comparison across different models*

---

### Evaluation Notes

**Note 1:** The above evaluations are conducted in two settings: (1) **All supported languages** (24 languages, excluding Latvian since `seamless-m4t-v2-large` and `seamless-m4t-medium` do not support it), and (2) **Common languages** (6 languages supported by all compared models: en, fr, de, it, pt, es).

**Note 2:** Performance differences may be partly attributed to Portuguese variant differences - our training data uses European Portuguese while most benchmarks use Brazilian Portuguese.

---


## <span style="color:#b37800;">Deployment Geography</span>

Global

## <span style="color:#b37800;">Use case</span>

This model serves developers, researchers, academics, and industries building applications that require speech-to-text capabilities, including but not limited to: conversational AI, voice assistants, transcription services, subtitle generation, and voice analytics platforms.

## <span style="color:#b37800;">Release Date</span>

Huggingface [08/14/2025](https://huggingface.co/nvidia/canary-1b-v2)

## <span style="color:#b37800;">Model Architecture</span>

`Canary-1b-v2` is an encoder-decoder architecture featuring a FastConformer Encoder \[3] and a Transformer Decoder \[4]. The model extracts audio features through the encoder and uses task-specific tokens—such as `<source language>` and `<target language>`—to guide the Transformer Decoder in generating text output.

It uses a unified SentencePiece Tokenizer \[5] with a vocabulary of **16,384 tokens**, optimized across all 25 supported languages. The architecture includes **32 encoder layers** and **8 decoder layers**, totaling **978 million parameters**.

For implementation details, see the [NeMo repository](https://github.com/NVIDIA/NeMo).


## <span style="color:#b37800;">Input</span>
- **Input Type(s):** 16kHz Audio
- **Input Format(s):** `.wav` and `.flac` audio formats
- **Input Parameters:** 1D (audio signal)
- **Other Properties Related to Input:**  Monochannel audio

## <span style="color:#b37800;">Output</span>
- **Output Type(s):**  Text
- **Output Format:**  String
- **Output Parameters:**  1D (text)
- **Other Properties Related to Output:** Punctuation and Capitalization included.

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. 

## <span style="color:#b37800;">How to Use This Model</span>


To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo) \[6]. We recommend you install it after you've installed latest PyTorch version.
```bash
pip install -U nemo_toolkit['asr']
```
The model is available for use in the NeMo toolkit [6], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

#### Automatically instantiate the model

```python
from nemo.collections.asr.models import ASRModel
asr_ast_model = ASRModel.from_pretrained(model_name="nvidia/canary-1b-v2")
```

#### Transcribing using Python
First, let's get a sample:
```bash
wget https://dldata-public.s3.us-east-2.amazonaws.com/2086-149220-0033.wav
```
Then simply do:
```python
output = asr_ast_model.transcribe(['2086-149220-0033.wav'], source_lang='en', target_lang='en')
print(output[0].text)
```

#### Translating using Python

Be sure to specify necessary `target_lang` for proper translation:

```python
output = asr_ast_model.transcribe(['2086-149220-0033.wav'], source_lang='en', target_lang='fr')
print(output[0].text)
```

#### Transcribing with timestamps

> **Note:** Use [main branch of NeMo](https://github.com/NVIDIA/NeMo/) to get timestamps until it is released in NeMo 2.5.

To transcribe with timestamps:
```python
output = asr_model.transcribe(['2086-149220-0033.wav'], source_lang='en', target_lang='en', timestamps=True)
# by default, timestamps are enabled for word and segment level
word_timestamps = output[0].timestamp['word'] # word level timestamps for first sample
segment_timestamps = output[0].timestamp['segment'] # segment level timestamps

for stamp in segment_timestamps:
    print(f"{stamp['start']}s - {stamp['end']}s : {stamp['segment']}")
```

#### Translating with timestamps

To translate with timestamps:
```python
output = asr_model.transcribe(['2086-149220-0033.wav'], source_lang='en', target_lang='fr', timestamps=True)

segment_timestamps = output[0].timestamp['segment'] # only supports segment level timestamps for translation

for stamp in segment_timestamps:
    print(f"{stamp['start']}s - {stamp['end']}s : {stamp['segment']}")
```

For translation task, please, refer to segment-level timestamps for getting intuitive and accurate alignment.

> **Note:** If timestamps are not required for your work, you can reduce memory usage by restoring only the `.nemo` file without the auxiliary CTC model. To do this, extract the `.nemo` file, remove any *timestamps_asr_model* files, then repackage it into a new `.nemo` file.


## <span style="color:#b37800;">Software Integration</span>

**Runtime Engine(s):**

* NeMo main branch (until it is released in NeMo 2.5)

**Supported Hardware Microarchitecture Compatibility:**

* NVIDIA Ampere
* NVIDIA Blackwell
* NVIDIA Hopper

**\[Preferred/Supported] Operating System(s):**

* Linux

**Hardware Specific Requirements:**
At least 6GB RAM for model to load.

#### Model Version

Current version: `Canary-1b-v2`. Previous versions can be [accessed](https://huggingface.co/collections/nvidia/canary-65c3b83ff19b126a3ca62926) here.



## <span style="color:#b37800;">Training and Evaluation Datasets</span>

### Training

The model was trained using the NeMo toolkit \[4], following a 3-stage training procedure:

* Initialized from a 4-language ASR model
* Stage 1: Trained for 150,000 steps on X→En and English ASR tasks using 64 A100 GPUs
* Stage 2: Trained for 115,000 additional steps on the full dataset (ASR, X→En, En→X)
* Stage 3: Fine-tuned for 10,000 steps on a language-balanced high-quality subset of Granary and NeMo ASR Set 3.0

For all the stages of training, both languages and corpora are weighted using temperature sampling (τ = 0.5).

Training script: [speech\_to\_text\_aed.py](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/speech_multitask/speech_to_text_aed.py)

Tokenizer script: [process\_asr\_text\_tokenizer.py](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py)

---

### Training Dataset

`Canary-1b-v2` was trained on a massive multilingual speech recognition and translation dataset combining Nvidia's newly published [Granary](https://huggingface.co/datasets/nvidia/Granary) and in-house dataset NeMo ASR Set 3.0. 

**Granary Dataset \[5] \[6] with improved pseudo-labels and efficiently filtered versions of the following corpora:**

* [YTC](https://huggingface.co/datasets/FBK-MT/mosel) \[7]
* [MOSEL](https://huggingface.co/datasets/FBK-MT/mosel) \[8]
* [YODAS](https://huggingface.co/datasets/espnet/yodas-granary) \[9]

Granary is now available on [Hugging Face](https://huggingface.co/datasets/nvidia/Granary).

To read more about the pseudo-labeling technique and [pipeline](https://github.com/NVIDIA/NeMo-speech-data-processor/tree/main/dataset_configs/multilingual/granary), please refer to the [Granary Paper](https://arxiv.org/abs/2505.13404).

**NeMo ASR Set 3.0 including human-labeled transcriptions from the following corpora:**

* Multilingual LibriSpeech (MLS)
* Mozilla Common Voice (v7.0)
* AMI (70 hrs)
* Fleurs
* LibriSpeech (960 hours)
* Fisher Corpus
* National Speech Corpus Part 1
* VCTK
* Europarl-ASR



**Total training hours:** 1.7M

* ASR: 660,000 hrs
* X→En: 360,000 hrs
* En→X: 690,000 hrs
* Non-speech: 36,000 hrs

All transcripts include punctuation and capitalization.


**Data Collection Method by dataset**

* Hybrid: Automated, Human 

**Labeling Method by dataset**

* Hybrid: Synthetic, Human


---

### Evaluation Dataset

* Fleurs \[10], MLS \[11], CoVoST \[12]
* Hugging Face Open ASR Leaderboard \[13]
* Earnings-22 \[14], This American Life \[15] (long-form)
* MUSAN \[16]

**Data Collection Method by dataset**

* Human

**Labeling Method by dataset**

* Human

## <span style="color:#b37800;">Benchmark Results</span>

This section reports the evaluation results of the ``Canary-1b-v2`` model across multiple tasks, including Automatic Speech Recognition (ASR), Speech Translation (AST), robustness to noise, and long-form transcription.

---

### Automatic Speech Recognition (ASR)

| **WER ↓**          | Fleurs-25 Langs       | CoVoST-13 Langs      | MLS - 6 Langs      |
| ---------------    | --------------------  | -------------------- | ------------------ |
| **`Canary-1b-v2`** | 8.40%                 | 8.85%                | 7.27%              |


**Note:** Presented WERs do not include Punctuation and Capitalization errors.

---

#### Hugging Face Open ASR Leaderboard

|  **WER ↓**   | **RTFx**   | **Mean**   | **AMI**   | **GigaSpeech**   | **LS Clean**   | **LS Other**   | **Earnings22**   | **SPGISpech**   | **Tedlium**   | **Voxpopuli**   |
|:-----------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| `Canary-1b-v2` | 749 | 7.15 | 16.01 | 10.82 | 2.18 | 3.56 | 11.79 | 2.28 | 4.29 | 6.25 |

More details on evaluation can be found at [HuggingFace ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)

---

### Speech Translation (AST)

#### X → English

|                    | **COMET ↑**     |                 | **BLEU ↑**      |                |
| ---------------    | --------------- | --------------- | --------------- | -------------- |
|                    | Fleurs-24 Langs | CoVoST-13 Langs | Fleurs-24 Langs | CoVoST-13 Langs|
| **`Canary-1b-v2`** | 79.30           | 77.48           | 29.08           | 40.48          |



#### English → X

|                    | **COMET ↑**     |                 | **BLEU ↑**      |                |
| ---------------    | -------------   | --------------- | --------------- | -------------- |
|                    | Fleurs-24 Langs | CoVoST-5 Langs  | Fleurs-24 Langs | CoVoST-5 Langs |
| **`Canary-1b-v2`** | 84.56           | 80.29           | 29.4            | 32.33          |

---


### Noise Robustness

Performance across different Signal-to-Noise Ratios (SNR) using MUSAN music and noise samples \[16] on the [LibriSpeech Clean test set](https://www.openslr.org/12).
**Metric**: Word Error Rate (**WER**)

| **SNR (dB)**       | 100      | 10    | 5     | 0     | -5     |
| ---------------    | -----    | ----- | ----- | ----- | -----  |
| **`Canary-1b-v2`** | 2.18% | 2.29% | 2.80% | 5.08% | 19.38% |


### Hallucination Robustness
Number of characters per minute on [MUSAN](https://www.openslr.org/17) \[16] 48 hrs eval set:
|  | **# of character per minute ↓** |
|:---------:|:----------:|
| **`Canary-1b-v2`** |   134.7   |


---

### Long-form Inference

`Canary-1b-v2` achieves strong performance on long-form transcription by using dynamic chunking with 1-second overlap between chunks, allowing for efficient parallel processing. This dynamic chunking feature is automatically enabled when calling `.transcribe()` on a single audio file, or when using `batch_size=1` with multiple audio files that are longer than 40 seconds.

| **Dataset**             | **WER ↓** |
| ----------------------- | --------- |
| Earnings-22             | 13.78%    |
| This American Life      | 9.87%     |

**Note:** Presented WERs do not include Punctuation and Capitalization errors.


---

## <span style="color:#b37800;">Inference</span>

**Engine**:

* NVIDIA NeMo

**Test Hardware**:

* NVIDIA A10
* NVIDIA A100
* NVIDIA A30
* NVIDIA A5000
* NVIDIA H100
* NVIDIA L4
* NVIDIA L40

---

## <span style="color:#b37800;">Ethical Considerations</span>

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards [here](https://developer.nvidia.com/blog/enhancing-ai-transparency-and-ethical-considerations-with-model-card/).

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## <span style="color:#b37800;">Bias:</span>

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------:
Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing  |  None
Measures taken to mitigate against unwanted bias                                                   |  None

## <span style="color:#b37800;">Explainability:</span>

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:
Intended Domain                                                                   |  Speech to Text Transcription and Translation
Model Type                                                                                            |  Attention Encoder-Decoder
Intended Users                                                                                        |  This model is intended for developers, researchers, academics, and industries building conversational based applications. 
Output                                                                                                |  Text 
Describe how the model works                                                                          |  Speech input is encoded into embeddings and passed into conformer-based model and output a text response.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of  |  Not Applicable
Technical Limitations & Mitigation                                                                    |  Transcripts and translations may be not 100% accurate. Accuracy varies based on source and target language and characteristics of input audio (Domain, Use Case, Accent, Noise, Speech Type, Context of speech, etc.)
Verified to have met prescribed NVIDIA quality standards  |  Yes
Performance Metrics                                                                                   | Word Error Rate (Speech Transcription) / BLEU score (Speech Translation) / COMET score (Speech Translation)
Potential Known Risks                                                                                 |  If a word is not trained in the language model and not presented in vocabulary, the word is not likely to be recognized. Not recommended for word-for-word/incomplete sentences as accuracy varies based on the context of input text
Licensing                                                                                             |  GOVERNING TERMS: Use of this model is governed by the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) license.

## <span style="color:#b37800;">Privacy:</span>

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------:
Generatable or reverse engineerable personal data?                                                     |  None
Personal data used to create this model?                                                                                       |  None
Is there provenance for all datasets used in training?                                                                                |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  No, not possible with externally-sourced data.
Applicable Privacy Policy        | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ 

## <span style="color:#b37800;">Safety:</span>

Field                                               |  Response
:---------------------------------------------------:|:----------------------------------
Model Application(s)                               |  Speech to Text Transcription
Describe the life critical impact   |  None
Use Case Restrictions                              | Abide by [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) License
Model and dataset restrictions            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.


## <span style="color:#b37800;">References</span>

\[1] [Granary: Speech Recognition and Translation Dataset in 25 European Languages](https://arxiv.org/abs/2505.13404)

\[2] [NVIDIA Granary Dataset Card](https://huggingface.co/datasets/nvidia/Granary)

\[3] [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084)

\[4] [Attention is All You Need](https://arxiv.org/abs/1706.03762)

\[5] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)

\[6] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

\[7] [Youtube-Commons](https://huggingface.co/datasets/PleIAs/YouTube-Commons)

\[8] [MOSEL: 950,000 Hours of Speech Data for Open-Source Speech Foundation Model Training on EU Languages](https://arxiv.org/abs/2410.01036)

\[9] [YODAS: Youtube-Oriented Dataset for Audio and Speech](https://arxiv.org/pdf/2406.00899)

\[10] [FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech](https://arxiv.org/abs/2205.12446)

\[11] [MLS: A Large-Scale Multilingual Dataset for Speech Research](https://arxiv.org/abs/2012.03411)

\[12] [CoVoST 2 and Massively Multilingual Speech-to-Text Translation](https://arxiv.org/abs/2007.10310)

\[13] [HuggingFace Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)

\[14] [Earnings-22 Benchmark](https://github.com/revdotcom/speech-datasets/tree/main/earnings22)

\[15] [Speech Recognition and Multi-Speaker Diarization of Long Conversations](https://arxiv.org/abs/2005.08072)

\[16] [MUSAN: A Music, Speech, and Noise Corpus](https://arxiv.org/abs/1510.08484)
