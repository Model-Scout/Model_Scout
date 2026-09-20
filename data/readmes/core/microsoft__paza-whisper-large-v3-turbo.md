---
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
- kik
- luo
- mas
- som
- kln
tags:
- audio
- automatic-speech-recognition
pipeline_tag: automatic-speech-recognition
license: mit
base_model:
- openai/whisper-large-v3-turbo
library_name: transformers
---

# paza-whisper-large-v3-turbo
## Model Details

This model is a fine-tuned version of the [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) model finetuned for automatic speech recognition (ASR) in several Kenyan languages, including **Swahili, Kalenjin, Kikuyu, Luo, Maasai and Somali**. Whisper is a transformer-based encoder-decoder model that converts raw audio into text. The encoder processes audio inputs as log-Mel spectrograms, capturing acoustic and linguistic features, while the decoder generates text tokens in an autoregressive manner. This design allows the model to handle diverse languages, accents, and noise conditions with strong generalization. 

Fine-tuning was performed on the entire unified multilingual ASR dataset, which includes the mentioned six languages, to encourage cross-lingual generalization. The fine-tuning process involved continued supervised training on labeled audio-text pairs, adjusting all the model’s parameters to better capture the phonetic and linguistic patterns unique to them. As a result, this model provides improved transcription accuracy for low-resource speech recognition tasks while maintaining Whisper’s robustness and efficiency. 

## Alignment approach 

<details>
  <summary>Click to view details</summary>

Traditional alignment measures are not applicable for this model because it does not generate new content; its primary function is to transcribe speech to text. In this context, alignment is best approximated by accuracy—the degree to which the transcription reflects the original spoken input. 

Generative risks such as hallucination, harmful content are not applicable because the model does not create novel text or interpret meaning beyond transcription. 

The post-training alignment process for this model focused on ensuring that transcriptions are reliable, consistent, and safe for downstream use in the specific language context. Supervised fine-tuning was performed on a multi-domain dataset of speech-text pairs in the mentioned languages, covering conversational, instructional, and broadcast speech to enhance robustness to diverse accents, noise conditions, and domains. No additional filtering for harmful or offensive content was applied during data preparation, because the focus was on capturing the full range of natural language use in a low-resource setting. 

To align the model to the target ASR task, the training strategy included standard supervised learning with cross-entropy loss on the token level, followed by iterative validation monitoring using Word Error Rate (WER) and Character Error Rate (CER) metrics. 

For safety considerations, refer to the [Responsible AI section](#responsible-ai-considerations) below. Additional performance metrics and evaluation results are provided in the Evaluation section. 

</details>

## Usage

<details>
  <summary>Click to view details</summary>

### Primary Use Cases

This model is designed for automatic speech recognition (ASR) across a wide range of already supported languages plus software and audio conditions and with additional support for **Swahili, Kalenjin, Kikuyu, Luo, Maasai and Somali**. This model is being shared with the research community to facilitate reproduction of our results and foster further research in this area. 


### Out-of-Scope Use Cases

It is not intended for automated decision-making, or any use cases that require understanding beyond transcription, and care should be taken to avoid applications where misinterpretation of speech could have safety or legal consequences. 

This model is not specifically designed or evaluated for all downstream purposes and has not been evaluated on any other tasks besides speech recognition in the six languages mentioned above.  

Developers should consider common limitations of language models and multimodal models, as well as performance difference across languages, as they select use cases, and evaluate and mitigate for accuracy, safety, and fairness before using within a specific downstream use case, particularly for high-risk scenarios. Developers should be aware of and adhere to applicable laws or regulations (including but not limited to privacy, trade compliance laws, etc.) that are relevant to their use case. 

We do not recommend using this model in commercial or real-world applications without further testing and development. It is being released for research purposes. 

</details>


## Data overview 


### Training Data

The model was finetuned on the [Africa Next Voices Kenya](https://huggingface.co/datasets/MCAA1-MSU/anv_data_ke), [DigiGreen Kikuyu](https://huggingface.co/datasets/DigiGreen/KikuyuASR_trainingdataset), a proprietary Kikuyu dataset and the Swahili split of the [Mozilla Common Voice](https://datacollective.mozillafoundation.org/datasets/cmflnuzw7mjcay14kmowc4y96) dataset.

Due to the model’s maximum input length of 448 tokens, audio samples exceeding this limit were discarded during tokenization. Performance in each language correlates strongly with the amount of training data available for that language.

### Data distribution by language

![alt text](figures/language_distribution.png)
*Figure 1: Data distribution by language*

### Training Procedure
<details>
  <summary>Click to view details</summary>

The model was finetuned in a full-precision floating-point setup using a streaming data pipeline. A custom trainer was used to cycle through batches from different datasets, enabling mixed-language training (e.g., one batch Swahili, the next Kalenjin, etc.). A weighted random sampler was applied within the dataset generator to maintain language balance. Multi-GPU training was ochestrated using `accelerate` on 8×A100 (40GB) GPUs.
Data preprocessing followed the same steps outlined in the Whisper finetuning [guide](https://huggingface.co/blog/fine-tune-whisper).

Since the base Whisper model supports only one of the six languages, we extended the tokenizer to new language tokens and resized the input embeddings so the new tokens could be trained and used for inference.


```py
from transformers import WhisperTokenizer, WhisperForConditionalGeneration

# Load model + tokenizer
model_name = "openai/whisper-large-v3-turbo"
tokenizer = WhisperTokenizer.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)

# Prepare the new language token
lang_code = "unsupported-language-code"
lang_token = f"<|{lang_code}|>"

vocab_len_before = len(tokenizer)

# Add token only if it doesn't already exist
existing_vocab = tokenizer.get_vocab()
if lang_token not in existing_vocab:
    tokenizer.add_tokens([lang_token])
    token_id = tokenizer.convert_tokens_to_ids(lang_token)

    # Ensure it wasn't mapped to the unknown token
    if token_id == tokenizer.unk_token_id:
        raise ValueError(f"Failed to add language token {lang_token}")

    # Resize embeddings to match tokenizer size
    model.resize_token_embeddings(len(tokenizer))

vocab_len_after = len(tokenizer)
vocab_delta = vocab_len_after - vocab_len_before
print(f"Vocabulary size changed by +{vocab_delta} (from {vocab_len_before} to {vocab_len_after}).")

```
</details>

### Training Hyperparameters

<details>
  <summary>Click to view details</summary>

| Hyperparameter                | Value |
|------------------------------|-------|
| Precision                    | fp32  |
| Optimizer                    | AdamW |
| Learning Rate                | 1e-5  |
| LR Scheduler                 |LinearLR|
| Warmup Ratio                 |  0.2  |
| Weight Decay                 |  0.01 |
| Gradient Clipping            |  1.0  |
| Training Batch Size           |  4    |
| Gradient Accumulation Steps  |  2    |
| Effective Global Batch Size  |  64   |
| Number of Training Steps     | 40,000|

</details>



## Quality and performance evaluation 


These are the results from the `test` splits of all the datasets mentioned in the data distribution chart as of  December 08, 2025.
Because the training data is imbalanced across languages (see the [data distribution chart](#data-distribution-by-language)), gains correlate with data volume.

The fine-tuned model demonstrates significant improvements in both Word Error Rate (WER) and Character Error Rate (CER) across multiple languages compared to the base model. Overall, the fine-tuned model consistently outperforms the base across languages, with variance reflecting the underlying language distribution.


*Note: The Kikuyu evaluation results are computed using the test splits of all Kikuyu datasets listed above, including the proprietary dataset.*

### Character Error Rate Comparison Across languages 

![CER Comparison](figures/whisper_cer_comparison.png)
*Figure 3: Character Error Rate (CER) comparison across the six languages for the base model versus the finetuned model. Lower CER indicates better transcription performance.*

### Word Error Rate Comparison Across languages 

![WER Comparison](figures/whisper_wer_comparison.png)
*Figure 2: Word Error Rate (WER) comparison across the six languages for the base model versus the finetuned model. Lower CER indicates better transcription performance.*


### Comparison Across SOTA models

We benchmarked our fine-tuned models against 3 state-of-the-art models - Meta’s [facebook/omniASR-LLM-7B](https://huggingface.co/facebook/omniASR-LLM-7B), [facebook/mms-1b-all](https://huggingface.co/facebook/mms-1b-all) and OpenAI's [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo). This set provides a balanced comparison across large‑scale multi-lingual, low‑resource, and leading ASR models

![alt text](figures/overall_cer_grouped_sorted.png)
*Figure 4: Character Error Rate (CER) comparison across the Kenyan languages for several state‑of‑the‑art ASR models including the Paza models. Lower CER indicates better transcription performance.* 


![alt text](figures/overall_wer_grouped_sorted.png)
*Figure 5: Word Error Rate (WER) comparison across the Kenyan languages for several state‑of‑the‑art ASR models including the Paza models. Lower CER indicates better transcription performance.* 






## Technical requirements and integration guidance 

<details>
  <summary>Click to view details</summary>

To transcribe audio samples, the model has to be used alongside a [`WhisperProcessor`](https://huggingface.co/docs/transformers/model_doc/whisper#transformers.WhisperProcessor).

The `WhisperProcessor` is used to:
1. Pre-process the audio inputs (converting them to log-Mel spectrograms for the model)
2. Post-process the model outputs (converting them from tokens to text)

The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". These context tokens 
are a sequence of tokens that are given to the decoder at the start of the decoding process, and take the following order:
1. The transcription always starts with the `<|startoftranscript|>` token
2. The second token is the language token (e.g. `<|sw|>` for Swahili)
3. The third token is the "task token". It can take one of two values: `<|transcribe|>` for speech recognition or `<|translate|>` for speech translation, however, the translation capability was neither modified nor evaluated during fine-tuning.
4. The fourth token, a `<|notimestamps|>` token is added if the model should not include timestamp prediction
5. Finally, our customization, `<|endoftext|>` token to terminate generation.

Thus, a typical sequence of context tokens might look as follows:
```
<|startoftranscript|> <|kik|> <|transcribe|> <|notimestamps|> <|endoftext|>
```
Which tells the model to decode in Kikuyu, under the task of speech recognition, and not to predict timestamps.

### Post-processing: Hallucination Mitigation

To reduce occasional trailing hallucinations or repetitive loops observed with Whisper-style decoders, we apply a post-processing truncation technique that constrains output length based on audio duration:

- A words-per-second (WPS) ratio is calibrated per language/dataset via grid search (0.5–8.0 WPS), selecting the value that minimizes WER on labeled validation data.
- After inference completes, the predicted text is dynamically truncated at the word level using `max_words = audio_duration × WPS` - any words beyond this limit are removed.
- An optional repetition detection pass scans for repeated 5–8 word phrases and escalating repetition patterns. When high-confidence repetition is detected, truncation occurs earlier to remove likely hallucinations.

This approach is applied entirely at post-processing time without modifying the model weights or decoding parameters. In practice, it reduces hallucinated trailing text while preserving valid speech content.

### Input formats 

The model accepts audio inputs in common formats such as WAV, MP3, FLAC, and OGG. Inputs can be provided as raw bytes, file paths, or as Hugging Face datasets Audio features. The preferred sampling rate is 16 kHz, and mono-channel audio is recommended for best results. The model does not require structured prompts; it directly transcribes the provided audio into text, with a language selected or through automatic language recognition by the model.  

Example usage includes passing an audio file path or raw bytes, which the preprocessing function converts into a suitable numpy array and the model returns a text output in form of a transcription. 

### How to Get Started with the Model

Use the code below to get started with the model.

- The model is supported in **Hugging Face Transformers**. To run it, first install the Transformers library.
- For this example, we also install **Datasets** to load a toy audio dataset from the Hugging Face Hub.

```python
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor
from datasets import Audio, load_dataset

device = "cuda:0" if torch.cuda.is_available() else "cpu"

model_id = "microsoft/paza-whisper-large-v3-turbo"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id).to(device)

processor = AutoProcessor.from_pretrained(model_id)

dataset = load_dataset("google/fleurs", "luo_ke", split="train", streaming=True)
dataset = dataset.cast_column("audio", Audio(processor.feature_extractor.sampling_rate))

sample = next(iter(dataset))
audio = sample["audio"]

inputs = processor(
    audio["array"],
    sampling_rate=audio["sampling_rate"],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
)
inputs = inputs.to(device, dtype=dtype)

pred_ids = model.generate(**inputs)
pred_text = processor.batch_decode(
    pred_ids,
    skip_special_tokens=True,
    decode_with_timestamps=False,    
    language="luo",  # Language codes:
                        # Kikuyu = "kik", Dholuo = "luo", Kalenjin = "kln",
                        # Maasai = "mas", Somali = "som", Swahili = "sw"
    task="transcribe",
    suppress_tokens=[],
    length_penalty=0.8,
    early_stopping=True,
    num_beams=5
)

print(pred_text)
```
</details>

## Responsible AI considerations 
<details>
  <summary>Click to view details</summary>
While efforts have been made to optimize the ASR model’s performance through various techniques, it may still produce outputs that are unexpected, biased, or inaccurate. The ASR model may inherit biases, errors, or omissions present in its base model. See the Whisper model card for more details. 

Users are responsible for sourcing their audio inputs legally. This could include securing appropriate rights, ensuring consent for use of audio, and/or the anonymization of data prior to use in research. 

Developers should be aware of and adhere to applicable laws or regulations (including but not limited to privacy, trade compliance laws, etc.) that are relevant to their use case. 

</details>


## Long context 
<details>
  <summary>Click to view details</summary>

This model supports input sequences of up to 448 tokens. Audio inputs that exceed this token limit must be segmented into smaller chunks prior to transcription. Consequently, processing long-form audio requires a chunking or streaming pipeline, and the model is not suitable for single-pass transcription of inputs that exceed the maximum token length.
</details>



## Safety evaluation and red-teaming 

<details>
  <summary>Click to view details</summary>

Techniques, it may still produce outputs that are unexpected, biased, or inaccurate. The ASR model may inherits any biases, errors, or omissions present in its base model, Whisper. For details on any safety testing or guidance related to Whisper, please refer to its original model card: https://huggingface.co/openai/whisper-large-v2#broader-implications 

Whisper’s capabilities are limited to Automatic Speech Recognition (ASR) and translation. Our fine-tuning process was restricted to ASR functionality and did not modify or extend the translation capability. This model is designed exclusively for automatic speech recognition (ASR) and translation and it does not generate new content, respond to prompts, or exhibit autonomous decision-making. As such:  

### No Generative Capabilities  
Red teaming and safety evaluations are primarily intended for models that produce novel outputs (e.g., text generation, image synthesis), where risks include harmful, biased, or unsafe content. ASR and translation models do  not create net new content; they transcribe or translate existing speech verbatim.  

 
### Inappropriate language  
Any inappropriate or harmful language in the transcription originates from the source audio, not from the model. Mitigation of such risks falls under downstream content moderation systems, not ASR functionality.  

### No Adversarial Prompting Scenario  

Red teaming typically probes for vulnerabilities in prompt-based systems. ASR models do not accept prompts or instructions; therefore, adversarial testing for jailbreaks or unsafe completions is irrelevant.  

For these reasons, formal safety evaluation and red teaming are not applicable to this ASR model. Instead, quality assurance focuses on accuracy metrics (see [Quality and performance evaluation](#quality-and-performance-evaluation) section).  

</details>

## Contact 

Requests for additional information may be directed to  

Authorized representative: Microsoft Ireland Operations Limited 70 Sir John Rogerson’s Quay, Dublin 2, D02 R296, Ireland  

MSFTAIActRequest@microsoft.com