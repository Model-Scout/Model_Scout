---
license: mit
language:
- multilingual
- ar
- zh
- cs
- da
- nl
- en
- fi
- fr
- de
- he
- hu
- it
- ja
- ko
- no
- pl
- pt
- ru
- es
- sv
- th
- tr
- uk
- kik
- sw
- kln
- mas
- som 
- luo
pipeline_tag: automatic-speech-recognition
tags:
- nlp
- code
- audio
- automatic-speech-recognition
- speech-summarization
- speech-translation
- visual-question-answering
- phi-4-multimodal
- phi
- phi-4-mini

base_model:
- microsoft/Phi-4-multimodal-instruct
library_name: transformers
---
# paza-Phi-4-multimodal-instruct 

## Model Overview
This is a fine-tuned version of [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) for automatic speech recognition (ASR) in **Swahili, Kalenjin, Kikuyu, Luo, Maasai and Somali**. The model retains the base model’s transformer-based architecture but is optimized for audio transcription.  

Fine-tuning was performed on the entire unified multilingual ASR dataset, comprising the mentioned six languages, to encourage cross-lingual generalization. During fine-tuning, only the audio-specific components: audio embedding module, audio encoder, and audio projection layers, were unfrozen and set as trainable, while the rest of the model parameters remained frozen to preserve pretrained language capabilities. Dropout was applied to both the audio encoder and projection layers to regularize training. The model leverages a multimodal processor that handles text tokenization and audio feature extraction, allowing seamless integration of audio inputs into the transformer architecture. 


## Alignment approach 

<details>
  <summary>Click to view details</summary>

Traditional alignment measures are not the focus for this model, the fine tuning for this model is focused on transcription of speech to text. In this context, alignment is best approximated by accuracy—the degree to which the transcription reflects the original spoken input. 

The model’s alignment strategy focused on producing accurate and reliable transcriptions of speech. Post-training alignment was performed using supervised fine-tuning on speech-text pairs in the target language. Datasets included multi-domain recordings and publicly available speech corpora, without additional filtering for content. Techniques such as instruction tuning and selective unfreezing of audio-related model components were applied to encourage consistent and precise outputs. The model’s performance and alignment were evaluated using standard ASR metrics, including word error rate (WER) and character error rate (CER). Users should note that, while the model is optimized for the mentioned low-resource languages, transcription, it may still produce errors. 

For safety considerations, refer to the [Responsible AI section](#responsible-ai-considerations) below. Additional performance metrics and evaluation results are provided in the Evaluation section. 

</details>

## Usage 
<details>
  <summary>Click to view details</summary>

### Primary use cases 

This model is primarily fine-tuned for automatic speech recognition (ASR) of **Swahili, Kalenjin, Kikuyu, Luo, Maasai and Somali** in a research setting, providing accurate transcription of spoken audio across multiple domains, including conversational, instructional, and broadcast speech. In addition to ASR, the model retains the capabilities of Phi-4-multimodal-instruct base, allowing it to perform text generation and image understanding tasks. It is expected to perform as well as the base model on non-ASR tasks, though the fine-tuned model was not evaluated for non-ASR capabilities as part of this project. 

This model is being shared with the research community to facilitate reproduction of our results and foster further research in this area. 


### Out-of-scope use cases 

This model is not intended for generating or altering audio content, automated decision-making, or any use cases that require understanding beyond transcription, and care should be taken to avoid applications where misinterpretation of speech could have safety or legal consequences. 

This model is not specifically designed or evaluated for all downstream purposes and has not been evaluated on any other tasks besides speech recognition in the mentioned six languages.  

Developers should consider common limitations of language models and multimodal models, as well as performance difference across languages, as they select use cases, and evaluate and mitigate for accuracy, safety, and fairness before using within a specific downstream use case, particularly for high-risk scenarios.  

Developers should be aware of and adhere to applicable laws or regulations (including but not limited to privacy, trade compliance laws, etc.) that are relevant to their use case. 

We do not recommend using this model in commercial or real-world applications without further testing and development. It is being released for research purposes. 

</details>

## Data Overview 

### Training Data

The model was finetuned on the [Africa Next Voices Kenya](https://huggingface.co/datasets/MCAA1-MSU/anv_data_ke), [DigiGreen Kikuyu](https://huggingface.co/datasets/DigiGreen/KikuyuASR_trainingdataset), a proprietary Kikuyu dataset and the Swahili split of the [Mozilla Common Voice](https://datacollective.mozillafoundation.org/datasets/cmj8u3puq00qhnxxbg26y0owu) dataset.

Audio samples longer than 30 seconds were excluded, following the recommendations in the input formats [documentation](https://huggingface.co/microsoft/Phi-4-multimodal-instruct#input-formats).

#### Data distribution by language

![alt text](figures/language_distribution.png)
*Figure 1: Data distribution by language*

### Training Procedure
<details>
  <summary>Click to view details</summary>
The model was finetuned using supervised learning on the speech-text pairs of the mentioned low-resource languages, in full precision (FP32). Training was conducted on 4×A100 GPUs (80GB). A streaming data pipeline was used, and a custom trainer cycled through batches from different datasets, enabling language-mixed training (e.g., one batch Swahili, the next Kalenjin).

A weighted random sampler was applied within the dataset generator to maintain balance across languages. Multi-GPU training was orchestrated using `accelerate`.

</details>

### Training Hyperparameters

<details>
  <summary>Click to view details</summary>

| Hyperparameter                | Value       |
|-------------------------------|------------|
| Precision                     | fp32       |
| Optimizer                      | AdamW_torch|
| Learning Rate                  | 1e-4       |
| LR Scheduler                   | LinearLR   |
| Warmup Ratio                    | 0.2       |
| Weight Decay                   | 0.005      |
| Gradient Clipping               | 1.0        |
| Training Batch Size             | 8          |
| Gradient Accumulation Steps     | 2          |
| Effective Global Batch Size     | 16         |
| Number of Training Steps        | 145,000    |
| Eval Batch Size                 | 8          |
| Adam Beta1                      | 0.9        |
| Adam Beta2                      | 0.99       |
| Adam Epsilon                    | 1e-7       |

</details>

## Quality and performance evaluation 

These are the results from the `test` splits of all the datasets mentioned in the data distribution chart as of  December 08, 2025.
Because the training data is imbalanced across languages (see the [data distribution chart](#data-distribution-by-language)), gains correlate with data volume.

The fine-tuned model demonstrates significant improvements in both Word Error Rate (WER) and Character Error Rate (CER) across multiple languages compared to the base model. Overall, the fine-tuned model consistently outperforms the base across languages, with variance reflecting the underlying language distribution.

*Note: The Kikuyu evaluation results are computed using the test splits of all Kikuyu datasets listed above, including the proprietary dataset.*

### Character Error Rate Comparison Across languages 

![alt text](figures/phi_cer_comparison.png)
*Figure 2: Character Error Rate (CER) comparison across the six languages for the base model versus the finetuned model. Lower CER indicates better transcription performance.*

### Word Error Rate Comparison Across languages 
![alt text](figures/phi_wer_comparison.png)
*Figure 3: Word Error Rate (WER) comparison across the six languages for the base model versus the finetuned model. Lower WER indicates better transcription performance.*


### Comparison Across SOTA models

We benchmarked our fine-tuned models against 3 state-of-the-art models - Meta’s [facebook/omniASR-LLM-7B](https://huggingface.co/facebook/omniASR-LLM-7B), [facebook/mms-1b-all](https://huggingface.co/facebook/mms-1b-all) and OpenAI's [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo). This set provides a balanced comparison across large‑scale multi-lingual, low‑resource, and leading ASR models

![alt text](figures/overall_cer_grouped_sorted.png)
*Figure 4: Character Error Rate (CER) comparison across the Kenyan languages for several state‑of‑the‑art ASR models including the Paza models. Lower CER indicates better transcription performance.* 

![alt text](figures/overall_wer_grouped_sorted.png)
*Figure 5: Word Error Rate (WER) comparison across the Kenyan languages for several state‑of‑the‑art ASR models including the Paza models. Lower WER indicates better transcription performance.* 


## Technical requirements and integration guidance 

<details>
  <summary>Click to view details</summary>

### Requirements

Phi-4 family has been integrated in the `4.48.2` version of `transformers`. The current `transformers` version can be verified with: `pip list | grep transformers`.
We suggest to run with Python 3.10.
Examples of required packages:
```
flash_attn==2.7.4.post1
torch==2.6.0
transformers==4.48.2
accelerate==1.3.0
soundfile==0.13.1
pillow==11.1.0
scipy==1.15.2
torchvision==0.21.0
backoff==2.2.1
peft==0.13.2
```


### Tokenizer

Phi-4-multimodal-instruct supports a vocabulary size of up to `200064` tokens. The [tokenizer files](https://huggingface.co/microsoft/Phi-4-multimodal-instruct/blob/main/added_tokens.json) already provide placeholder tokens that can be used for downstream fine-tuning, but they can also be extended up to the model's vocabulary size.

### Input Formats

The model accepts audio clips together with a short text instruction in English describing the task to perform. For speech recognition, the instruction specifies that the audio should be transcribed and, where applicable, the target language. The model processes the instruction and the audio jointly and produces a text output.
Given the nature of its training data, the model is best used with a chat-style prompt format, as shown below.

#### Speech-Language Format

This format is used for various speech and audio tasks:

`
<|user|><|audio_1|>{task prompt}<|end|><|assistant|>
`

The task prompt can vary for different task.
Automatic Speech Recognition:

`
<|user|><|audio_1|>Transcribe the the audio to {lang}.<|end|><|assistant|>
`

**Example:** 

**Instruction:** “Transcribe the Kikuyu audio clip.” 

**Audio:** The actual speech recording in a standard audio format (like a waveform).

Any audio format that can be loaded by soundfile package should be supported.

To keep the satisfactory performance, maximum audio length is suggested to be 40 seconds.
  
### Loading the model locally
After obtaining the  model checkpoints, users can use this sample code for inference.

```python
import requests
import torch
import os
import io
from PIL import Image
import soundfile as sf
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
from urllib.request import urlopen
# Define model path
model_path = "microsoft/paza-Phi-4-multimodal-instruct"

# Load model and processor
processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path, 
    device_map="cuda", 
    torch_dtype="auto", 
    trust_remote_code=True,
    # if you do not use Ampere or later GPUs, change attention to "eager"
    _attn_implementation='flash_attention_2',
).cuda()
# Load generation config
generation_config = GenerationConfig.from_pretrained(model_path)
# Define prompt structure
user_prompt = '<|user|>'
assistant_prompt = '<|assistant|>'
prompt_suffix = '<|end|>'

# Part 2: Audio Processing
print("\n--- AUDIO PROCESSING ---")
audio = "sample_audio.wav"
speech_prompt = "Transcribe the audio to Swahili."
prompt = f'{user_prompt}<|audio_1|>{speech_prompt}{prompt_suffix}{assistant_prompt}'
print(f'>>> Prompt\n{prompt}')

# Process with the model
inputs = processor(text=prompt, audios=[(audio, samplerate)], return_tensors='pt').to('cuda:0')
generate_ids = model.generate(
    **inputs,
    max_new_tokens=64,
    generation_config=generation_config,
)
generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]
print(f'>>> Response\n{response}')
```

More inference examples can be found [**here**](https://huggingface.co/microsoft/Phi-4-multimodal-instruct/blob/main/sample_inference_phi4mm.py).

</details>


## Responsible AI considerations 

<details>
  <summary>Click to view details</summary>

As indicated in the [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct), this model is not specifically designed or evaluated for all downstream purposes.  

Developers should consider common limitations of language models and multimodal models, as well as performance difference across languages, as they select use cases, and evaluate and mitigate for accuracy, safety, and fairness before using within a specific downstream use case, particularly for high-risk scenarios.  

Developers should be aware of and adhere to applicable laws or regulations (including but not limited to privacy, trade compliance laws, etc.) that are relevant to their use case. 

Users are responsible for sourcing their audio inputs legally. This could include securing appropriate rights, ensuring consent for use of audio, and/or the anonymization of data prior to use in research. 

</details>

## Long Context 

<details>
  <summary>Click to view details</summary>

Phi-4-multimodal-instruct supports an extended context window of 128K tokens, enabling efficient handling of long text and multimodal sequences. This fine-tuned ASR model retains the base model’s original architecture and positional encoding without changes. 

No additional training was done on long-context datasets, so performance for very long inputs has not been optimized or evaluated. Users should refer to the base model's documentation for detailed expectations and validate performance for tasks requiring extended sequences. 

</details>


## Safety evaluation and red-teaming

<details>
  <summary>Click to view details</summary>

This model is a fine-tuned variant of Phi-4-multimodal-instruct, optimized exclusively for automatic speech recognition (ASR) in the mentioned six African languages. While the fine-tuning introduces domain-specific improvements for transcription accuracy, it does not alter the underlying generative capabilities of the base model. As such: 

### Underlying Capabilities Remain 
The base model retains its original functionality beyond ASR. However, the fine-tuning process was limited to ASR tasks and did not expand or modify generative behaviors. Therefore, the safety posture of the model is expected to remain consistent with that of the original base model and additional safety testing was not performed on generative capabilities for this fine-tuned version of the model. 

### Limited Impact of Fine-Tuning on Safety Risks 
Fine-tuning for ASR does not introduce new pathways for prompt-based exploitation or unsafe completions. The model’s generative features are unchanged, and the ASR-specific layers do not create novel content. 

### Risk Considerations 
Any harmful or biased language in transcriptions originates from the source audio, not from the ASR functionality. Mitigation of such risks should occur through downstream content moderation systems. 
 
For generative capabilities inherited from the base model, refer to the base model’s safety evaluation for applicable risks and mitigations. 

</details>

## Contact 

Requests for additional information may be directed to  

Authorized representative: Microsoft Ireland Operations Limited 70 Sir John Rogerson’s Quay, Dublin 2, D02 R296, Ireland   

MSFTAIActRequest@microsoft.com