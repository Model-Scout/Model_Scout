---
license: cc-by-4.0
base_model: nvidia/canary-180m-flash
base_model_relation: quantized
library_name: transcribe.cpp
pipeline_tag: automatic-speech-recognition
language:
  - en
  - de
  - es
  - fr
tags:
  - gguf
  - transcribe.cpp
  - asr
  - speech-to-text
  - canary
  - multitask-aed
  - encoder-decoder
  - translation
transcribe_cpp:
  schema_version: 2
  wer_fleurs_de:
    q8_0: 7.33
  wer_fleurs_en:
    q8_0: 5.98
  wer_fleurs_es:
    q8_0: 6.54
  wer_fleurs_fr:
    q8_0: 8.53
  wer_librispeech_test_clean:
    f32: 1.94
    f16: 1.94
    q8_0: 1.93
    q6_k: 1.93
    q5_k_m: 1.9
    q4_k_m: 1.93
  rtf_m4_max:
    cpu: 78.91
    metal: 153.46
  rtf_ryzen_4750u:
    cpu: 21.73
    vulkan: 33.09
  streaming: false
  translate: true
  lang_detect: false
  timestamps: none
---

# canary-180m-flash: transcribe.cpp GGUF

GGUF conversions of [nvidia/canary-180m-flash](https://huggingface.co/nvidia/canary-180m-flash) for use
with [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp).

Ported from upstream commit
[b12ab41](https://huggingface.co/nvidia/canary-180m-flash/commit/b12ab41),
pinned 2026-05-08.
Validated against the NeMo reference at transcribe.cpp commit
[db53eda](https://github.com/handy-computer/transcribe.cpp/tree/db53eda)
on 2026-05-08.

Offline multilingual speech-to-text and translation. A 182M-parameter
multitask AED with a 17-layer FastConformer encoder and a 4-layer
Transformer decoder. Supports automatic speech recognition in English,
German, Spanish, and French, and bidirectional EN↔{DE, ES, FR}
translation. Takes a
16 kHz mono WAV and produces a transcript. Not a streaming model;
word/segment timestamps are upstream-experimental and not exposed in
the v1 port.


## Downloads

| Quantization | Download | Size | WER (LibriSpeech test-clean) |
| --- | --- | ---: | ---: |
| F32 | [canary-180m-flash-F32.gguf](https://huggingface.co/handy-computer/canary-180m-flash-gguf/resolve/main/canary-180m-flash-F32.gguf) | 756 MB | 1.94% |
| F16 | [canary-180m-flash-F16.gguf](https://huggingface.co/handy-computer/canary-180m-flash-gguf/resolve/main/canary-180m-flash-F16.gguf) | 382 MB | 1.94% |
| Q8_0 | [canary-180m-flash-Q8_0.gguf](https://huggingface.co/handy-computer/canary-180m-flash-gguf/resolve/main/canary-180m-flash-Q8_0.gguf) | 218 MB | 1.93% |
| Q6_K | [canary-180m-flash-Q6_K.gguf](https://huggingface.co/handy-computer/canary-180m-flash-gguf/resolve/main/canary-180m-flash-Q6_K.gguf) | 176 MB | 1.93% |
| Q5_K_M | [canary-180m-flash-Q5_K_M.gguf](https://huggingface.co/handy-computer/canary-180m-flash-gguf/resolve/main/canary-180m-flash-Q5_K_M.gguf) | 159 MB | 1.90% |
| Q4_K_M | [canary-180m-flash-Q4_K_M.gguf](https://huggingface.co/handy-computer/canary-180m-flash-gguf/resolve/main/canary-180m-flash-Q4_K_M.gguf) | 139 MB | 1.93% |

WER on the full LibriSpeech test-clean split (2,620 utterances), batch size 1, timestamps none. Figures without a commit were published before provenance was recorded.

Greedy decoding, no external LM. F32 reference baseline: 1.94%. On the same wavs,
NeMo's reference run produces 1.93% (one substitution difference out of ~27k
reference words), so the F32 port matches the reference framework at the noise
floor. NVIDIA's self-reported number on the upstream model card is 1.87%.


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
  -m canary-180m-flash-Q8_0.gguf \
  input.wav
```

If your audio isn't already 16 kHz mono WAV, convert it first:

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

See the [transcribe.cpp model page](https://github.com/handy-computer/transcribe.cpp/blob/main/docs/models/canary-180m-flash.md) for performance
numbers, numerical validation, and reproduction steps.

## License

Inherited from the base model: **CC-BY-4.0**. See the
[upstream model card](https://huggingface.co/nvidia/canary-180m-flash) for full terms.

---

## Original Model Card

> The section below is reproduced from
> [nvidia/canary-180m-flash](https://huggingface.co/nvidia/canary-180m-flash) at commit
> `b12ab41` for offline reference. The upstream card is the
> authoritative source.

# Canary 180M Flash

<style>
img {
 display: inline;
}
</style>

## Description:
NVIDIA NeMo Canary Flash [1] is a family of multilingual multi-tasking models based on Canary architecture [2] that achieves state-of-the art performance on multiple speech benchmarks. With 182 million parameters and an inference speed of more than 1200 RTFx (on open-asr-leaderboard sets), canary-180m-flash supports automatic speech-to-text recognition (ASR) in 4 languages (English, German, French, Spanish) and translation from English to German/French/Spanish and from German/French/Spanish to English with or without punctuation and capitalization (PnC).
Additionally, canary-180m-flash offers an experimental feature for word-level and segment-level timestamps in English, German, French, and Spanish.
This model is released under the permissive CC-BY-4.0 license and is available for commercial use.


## Model Architecture:
Canary is an encoder-decoder model with FastConformer [3] Encoder and Transformer Decoder [4]. With audio features extracted from the encoder, task tokens such as \<target language\>, \<task\>, \<toggle timestamps\> and \<toggle PnC\> are fed into the Transformer Decoder to trigger the text generation process. Canary uses a concatenated tokenizer [5] from individual SentencePiece [6] tokenizers of each language, which makes it easy to scale up to more languages. The canary-180m-flash model has 17 encoder layers and 4 decoder layers, leading to a total of 182M parameters. For more details about the architecture, please refer to [1].

## NVIDIA NeMo

To train, fine-tune or transcribe with canary-180m-flash, you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo).

## How to Use this Model

The model is available for use in the NeMo framework [7], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

Please refer to [our tutorial](https://github.com/NVIDIA/NeMo/blob/main/tutorials/asr/Canary_Multitask_Speech_Model.ipynb) for more details.

A few inference examples listed below:

### Loading the Model

```python
from nemo.collections.asr.models import EncDecMultiTaskModel
# load model
canary_model = EncDecMultiTaskModel.from_pretrained('nvidia/canary-180m-flash')
# update decode params
decode_cfg = canary_model.cfg.decoding
decode_cfg.beam.beam_size = 1
canary_model.change_decoding_strategy(decode_cfg)
```

## Input: 
**Input Type(s):** Audio <br>
**Input Format(s):** .wav or .flac files<br>
**Input Parameters(s):** 1D <br>
**Other Properties Related to Input:** 16000 Hz Mono-channel Audio, Pre-Processing Not Needed <br>

Input to canary-180m-flash can be either a list of paths to audio files or a jsonl manifest file.

### Inference with canary-180m-flash:
If the input is a list of paths, canary-180m-flash assumes that the audio is English and transcribes it. I.e., canary-180m-flash default behavior is English ASR. 
```python
output = canary_model.transcribe(
    ['path1.wav', 'path2.wav'],
    batch_size=16,  # batch size to run the inference with
    pnc='True',        # generate output with Punctuation and Capitalization
)

predicted_text = output[0].text

```

canary-180m-flash can also predict word-level and segment-level timestamps
```python
output = canary_model.transcribe(
  ['filepath.wav'],
  timestamps=True,  # generate output with timestamps
)

predicted_text = output[0].text
word_level_timestamps = output[0].timestamp['word']
segment_level_timestamps = output[0].timestamp['segment']

```
To predict timestamps for audio files longer than 10 seconds, we recommend using the longform inference script (explained in the next section) with `chunk_len_in_secs=10.0`. 

To use canary-180m-flash for transcribing other supported languages or perform Speech-to-Text translation or provide word-level timestamps, specify the input as jsonl manifest file, where each line in the file is a dictionary containing the following fields: 

```yaml
# Example of a line in input_manifest.json
{
    "audio_filepath": "/path/to/audio.wav",  # path to the audio file
    "source_lang": "en",  # language of the audio input, set `source_lang`==`target_lang` for ASR, choices=['en','de','es','fr']
    "target_lang": "en",  # language of the text output, choices=['en','de','es','fr']
    "pnc": "yes",  # whether to have PnC output, choices=['yes', 'no']
    "timestamp": "yes", # whether to output word-level timestamps, choices=['yes', 'no']
}
```

and then use:
```python
output = canary_model.transcribe(
    "<path to input manifest file>",
    batch_size=16,  # batch size to run the inference with
)
```

### Longform inference with canary-180m-flash:
Canary models are designed to handle input audio smaller than 40 seconds. In order to handle longer audios, NeMo includes [speech_to_text_aed_chunked_infer.py](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/asr_chunked_inference/aed/speech_to_text_aed_chunked_infer.py) script that handles chunking, performs inference on the chunked files, and stitches the transcripts.

The script will perform inference on all `.wav` files in `audio_dir`. Alternatively you can also pass a path to a manifest file as shown above. The decoded output will be saved at `output_json_path`.

```
python scripts/speech_to_text_aed_chunked_infer.py \
    pretrained_name="nvidia/canary-180m-flash" \
    audio_dir=$audio_dir \
    output_filename=$output_json_path \
    chunk_len_in_secs=40.0 \
    batch_size=1 \
    decoding.beam.beam_size=1 \
    timestamps=False
```

**Note** that for longform inference with timestamps, it is recommended to use `chunk_len_in_secs` of 10 seconds.


## Output:
**Output Type(s):** Text <br>
**Output Format:** Text output as a string (w/ timestamps) depending on the task chosen for decoding <br> 
**Output Parameters:** 1-Dimensional text string <br>
**Other Properties Related to Output:** May Need Inverse Text Normalization; Does Not Handle Special Characters <br>


## Software Integration:
**Runtime Engine(s):** 
* NeMo - main <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* [NVIDIA Ampere] <br>
* [NVIDIA Blackwell] <br>
* [NVIDIA Jetson]  <br>
* [NVIDIA Hopper] <br>
* [NVIDIA Lovelace] <br>
* [NVIDIA Pascal] <br>
* [NVIDIA Turing] <br>
* [NVIDIA Volta] <br>

**[Preferred/Supported] Operating System(s):** <br>
* [Linux] <br>
* [Linux 4 Tegra] <br>
* [Windows] <br>

## Model Version(s): 
canary-180m-flash <br>


# Training and Evaluation Datasets: 

## Training Dataset:

The canary-180m-flash model is trained on a total of 85K hrs of speech data. It consists of 31K hrs of public data, 20K hrs collected by [Suno](https://suno.ai/), and 34K hrs of in-house data. 
The datasets below include conversations, videos from the web, and audiobook recordings.

**Data Collection Method:**
* Human <br>

**Labeling Method:**
* Hybrid: Human, Automated <br>

The constituents of public data are as follows. 

#### English (25.5k hours)
- Librispeech 960 hours
- Fisher Corpus
- Switchboard-1 Dataset
- WSJ-0 and WSJ-1
- National Speech Corpus (Part 1, Part 6)
- VCTK
- VoxPopuli (EN)
- Europarl-ASR (EN)
- Multilingual Librispeech (MLS EN) - 2,000 hour subset
- Mozilla Common Voice (v7.0)
- People's Speech - 12,000 hour subset
- Mozilla Common Voice (v11.0)  - 1,474 hour subset

#### German (2.5k hours)
- Mozilla Common Voice (v12.0)  - 800 hour subset
- Multilingual Librispeech (MLS DE) - 1,500 hour subset
- VoxPopuli (DE) - 200 hr subset

#### Spanish (1.4k hours)
- Mozilla Common Voice (v12.0)  - 395 hour subset
- Multilingual Librispeech (MLS ES) - 780 hour subset
- VoxPopuli (ES) - 108 hour subset
- Fisher  - 141 hour subset

#### French (1.8k hours)
- Mozilla Common Voice (v12.0)  - 708 hour subset
- Multilingual Librispeech (MLS FR) - 926 hour subset
- VoxPopuli (FR) - 165 hour subset


## Evaluation Dataset:

**Data Collection Method:** <br>
* Human <br>

**Labeling Method:** <br>
* Human <br>

Automatic Speech Recognition: 
* [HuggingFace OpenASR Leaderboard evaluation sets](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)
* [MLS](https://huggingface.co/datasets/facebook/multilingual_librispeech)
* [MCV] (https://commonvoice.mozilla.org/en/datasets)

Automatic Speech Translation:
* [FLEURS](https://huggingface.co/datasets/google/fleurs)
* [COVOST-v2](https://github.com/facebookresearch/covost)
* [mExpresso](https://huggingface.co/facebook/seamless-expressive#mexpresso-multilingual-expresso)

Timestamp Prediction:
* [Librispeech](https://www.openslr.org/12)

Hallucination Robustness:
* [MUSAN](https://www.openslr.org/17/) 48 hrs eval set

Noise Robustness:
* [Librispeech](https://www.openslr.org/12)

Model Fairness:
* [Casual Conversations Dataset](https://arxiv.org/pdf/2104.02821)

## Training

canary-180m-flash is trained using the NVIDIA NeMo framework [7] for a total of 219K steps with 2D bucketing [1] and optimal batch sizes set using OOMptimizer [8]. The model is trained on 32 NVIDIA A100 80GB GPUs. 
The model can be trained using this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/speech_multitask/speech_to_text_aed.py) and [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/speech_multitask/fast-conformer_aed.yaml).

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).

## Inference:
**Engine:** NVIDIA NeMo <br>
**Test Hardware :** <br>
* A6000 <br>
* A100 <br>
* V100 <br>

## Performance

For ASR and AST experiments, predictions were generated using greedy decoding. Note that utterances shorter than 1 second are symmetrically zero-padded upto 1 second during evaluation.

### English ASR Performance (w/o PnC) 

The ASR performance is measured with word error rate (WER), and we process the groundtruth and predicted text with [whisper-normalizer](https://pypi.org/project/whisper-normalizer/).

WER on [HuggingFace OpenASR leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) evaluated with a batch size of 128:

| **Version** | **Model**     | **RTFx**   | **AMI**   | **GigaSpeech**   | **LS Clean**   | **LS Other**   | **Earnings22**   | **SPGISpech**   | **Tedlium**   | **Voxpopuli**   |
|:---------:|:-----------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| main  | canary-180m-flash | 1233 | 14.86 | 10.51 | 1.87 | 3.83 | 13.33 | 2.26 | 3.98 | 6.35 |

#### Inference speed on different systems
We profiled inference speed on the OpenASR benchmark using the [real-time factor](https://github.com/NVIDIA/DeepLearningExamples/blob/master/Kaldi/SpeechRecognition/README.md#metrics) (RTFx) to quantify throughput. 

| **Version** | **Model**     | **System**   | **RTFx**   |
|:-----------:|:-------------:|:------------:|:----------:|
| main | canary-180m-flash | NVIDIA A100 | 1233 |
| main | canary-180m-flash | NVIDIA H100 | 2041 |



### Multilingual ASR Performance
WER on [MLS](https://huggingface.co/datasets/facebook/multilingual_librispeech) test set:

| **Version** | **Model**  | **De**   | **Es**   | **Fr**   |
|:---------:|:-----------:|:------:|:------:|:------:|
| main   | canary-180m-flash | 4.81 | 3.17 | 4.75 |


WER on [MCV-16.1](https://commonvoice.mozilla.org/en/datasets) test set:
| **Version** | **Model**  |  **En**   | **De**   | **Es**   | **Fr**   |
|:---------:|:-----------:|:------:|:------:|:------:|:------:|
| main   | canary-180m-flash | 9.53 | 5.94 | 4.90 | 8.19 |


More details on evaluation can be found at [HuggingFace ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)

### AST Performance

We evaluate AST performance with [BLEU score](https://lightning.ai/docs/torchmetrics/stable/text/sacre_bleu_score.html), and use native annotations with punctuation and capitalization in the datasets.

[FLEURS](https://huggingface.co/datasets/google/fleurs) test set:

BLEU score: 

| **Version** | **Model** | **En->De** | **En->Es** | **En->Fr** | **De->En** | **Es->En** | **Fr->En** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| main       | canary-180m-flash | 	28.18   |  20.47   |   36.66    |   32.08   |   20.09    |  29.75    |

COMET score:

| **Version** | **Model** | **En->De** | **En->Es** | **En->Fr** | **De->En** | **Es->En** | **Fr->En** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| main       | canary-180m-flash | 	77.56   |  78.10   |   78.53    |   83.03   |   81.48    |  82.28    |

[COVOST-v2](https://github.com/facebookresearch/covost) test set:
 
BLEU score:

| **Version** | **Model** | **De->En** | **Es->En** | **Fr->En** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|
| main       | canary-180m-flash |   35.61   |    39.84    |   38.57    |

COMET score:

| **Version** | **Model** | **De->En** | **Es->En** | **Fr->En** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|
| main       | canary-180m-flash |   80.94   |    84.54    |   82.50    |

[mExpresso](https://huggingface.co/facebook/seamless-expressive#mexpresso-multilingual-expresso) test set:

BLEU score:

| **Version** | **Model** | **En->De** | **En->Es** | **En->Fr** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|
| main       | canary-180m-flash |   21.60    |   33.45   |   25.96   |

COMET score:

| **Version** | **Model** | **En->De** | **En->Es** | **En->Fr** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|
| main       | canary-180m-flash |   77.71    |   80.87   |   77.82   |


### Timestamp Prediction
F1-score on [Librispeech Test sets](https://www.openslr.org/12) at collar value of 200ms

| **Version** | **Model** | **test-clean** | **test-other** |
|:-----------:|:---------:|:----------:|:----------:|
| main       | canary-180m-flash |   93.48    |   91.38   |


### Hallucination Robustness
Number of characters per minute on [MUSAN](https://www.openslr.org/17) 48 hrs eval set

| **Version** | **Model** | **# of character per minute** |
|:-----------:|:---------:|:----------:|
| main       | canary-180m-flash |   91.52   |

### Noise Robustness
WER on [Librispeech Test Clean](https://www.openslr.org/12) at different SNR (signal to noise ratio) levels of additive white noise

| **Version** | **Model** | **SNR 10** | **SNR 5** | **SNR 0** | **SNR -5** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|:----------:|
| main       | canary-180m-flash |    3.23   |   5.34   |   12.21   |    34.03  |

## Model Fairness Evaluation

As outlined in the paper "Towards Measuring Fairness in AI: the Casual Conversations Dataset" [9], we assessed the canary-180m-flash model for fairness. The model was evaluated on the CausalConversations-v1 dataset, and the results are reported as follows:

### Gender Bias:

| Gender | Male | Female | N/A | Other |
| :--- | :--- | :--- | :--- | :--- |
| Num utterances | 19325 | 24532 | 926 | 33 |
| % WER | 16.92 | 14.01 | 20.01 | 25.04 |

### Age Bias:

| Age Group | (18-30) | (31-45) | (46-85) | (1-100) |
| :--- | :--- | :--- | :--- | :--- |
| Num utterances | 15956 | 14585 | 13349 | 43890 |
| % WER | 14.95 | 15.36 | 15.65 | 15.29 |

(Error rates for fairness evaluation are determined by normalizing both the reference and predicted text, similar to the methods used in the evaluations found at https://github.com/huggingface/open_asr_leaderboard.)

## License/Terms of Use: 
canary-180m-flash is released under the CC-BY-4.0 license. By using this model, you are agreeing to the [terms and conditions](https://choosealicense.com/licenses/cc-by-4.0/) of the license. <br>

## References:

[1] [Training and Inference Efficiency of Encoder-Decoder Speech Models](https://arxiv.org/pdf/2503.05931)

[2] [Less is More: Accurate Speech Recognition & Translation without Web-Scale Data](https://www.isca-archive.org/interspeech_2024/puvvada24_interspeech.pdf) <br>

[3] [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10389701)

[4] [Attention is All You Need](https://arxiv.org/abs/1706.03762)

[5] [Unified Model for Code-Switching Speech Recognition and Language Identification Based on Concatenated Tokenizer](https://aclanthology.org/2023.calcs-1.7.pdf)

[6] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)

[7] [NVIDIA NeMo Framework](https://github.com/NVIDIA/NeMo)

[8] [EMMeTT: Efficient Multimodal Machine Translation Training](https://arxiv.org/abs/2409.13523)

[9] [Towards Measuring Fairness in AI: the Casual Conversations Dataset](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9634168)


## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  
Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).
