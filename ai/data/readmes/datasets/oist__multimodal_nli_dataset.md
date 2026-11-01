---
license: cc-by-nc-4.0
task_categories:
- sentence-similarity
language:
- ar
- fr
- en
- de 
- es
- it
- ja
- ko
- nl
- pl
- pt
- ru
- tr
- zh
- hi
pretty_name: Multimodal and Multilingual Natural Language Inference Dataset
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: premise_text
    dtype: string
  - name: premise_audio
    dtype: string
  - name: hypothesis_text
    dtype: string
  - name: hypothesis_audio
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': entailment
          '1': contradiction
          '2': neutral
  - name: premise_modality
    dtype: string
  - name: hypothesis_modality
    dtype: string
  - name: premise_language
    dtype: string
  - name: hypothesis_language
    dtype: string
  - name: premise_source
    dtype: string
  - name: hypothesis_source
    dtype: string
  splits:
  - name: train
    num_bytes: 254373188
    num_examples: 1181133
  - name: validation
    num_bytes: 24873676
    num_examples: 91010
  - name: test
    num_bytes: 40669962
    num_examples: 141806
  download_size: 163298146
  dataset_size: 319916826
---
---
# Dataset Card for Multimodal and Multilingual NLI Dataset

## Dataset Details

**Paper:** [Beyond Similarity Scoring: Detecting Entailment and Contradiction in Multilingual and Multimodal Contexts, Interspeech 2025](https://www.isca-archive.org/interspeech_2025/istaiteh25_interspeech.pdf)

### Dataset Description

The Multimodal and Multilingual NLI Dataset supports multilingual and multimodal Natural Language Inference (NLI). It enables classification of entailment, contradiction, and neutrality across four modality combinations:

- Text-Text (T-T)
- Text-Speech (T-S)
- Speech-Text (S-T)
- Speech-Speech (S-S)

The dataset covers text in multiple languages — Arabic, English, French, German, Spanish, Italian, Japanese, Korean, Dutch, Polish, Portuguese, Russian, Turkish, Chinese, Hindi, and Urdu — while speech data is available in Arabic, French, and English. It supports research beyond similarity scoring by detecting logical relationships in both text and speech across multilingual settings.

- Labels: 
  - 0 = Entailment
  - 1 = Contradiction
  - 2 = Neutral

- Number of splits: train, validation, test

- Multimodal fields: premise and hypothesis each contain:
  - "text": string or None
  - "audio": audio array loaded by Hugging Face `Audio` feature or None

## Associated Model

This dataset was used to train the **Multilingual & Multimodal NLI (MMNLI) model**, available here: [oist/multimodal_nli_model](https://huggingface.co/oist/multimodal_nli_model).

### Curated by

- Othman Istaiteh, Salima Mdhaffar, Yannick Estève  
- Affiliation: LIA Lab, Université d’Avignon, France

### Language(s)

- **Text:** Arabic (ar), English (en), French (fr), German (de), Spanish (es), Italian (it), Japanese (ja), Korean (ko), Dutch (nl), Polish (pl), Portuguese (pt), Russian (ru), Turkish (tr), Chinese (zh), Hindi (hi), Urdu (ur)  
- **Speech:** Arabic (ar), English (en), French (fr)

### License

- CC BY-NC 4.0 (dataset as a whole)
- Includes components licensed under:
  - SNLI: CC BY-SA 4.0
  - XNLI: CC BY-NC 4.0
  - FLEURS: CC BY 4.0

## Dataset Sources

- Repository: https://github.com/othman-istaiteh/multimodal-nli
- Paper: Istaiteh et al., Interspeech 2025
- Audio: FLEURS recordings, TTS-generated speech (Coqui TTS)


## Audio Download

The dataset includes audio from two sources. **You must download the audio files separately** because the Hugging Face dataset only stores paths to audio files to keep the repository small and avoid extremely large uploads.

- [FLEURS recordings (ZIP)](https://drive.google.com/file/d/1RdTbeLyYT6f7SzgEPMwRppX33L5GRfUa/view?usp=sharing)
- [TTS-generated speech (ZIP)](https://drive.google.com/file/d/17h5LUJ7FFnoQOt8GETMpUUytPjOB_tRA/view?usp=sharing)

## Sample Data

| premise_text | premise_audio | hypothesis_text | hypothesis_audio | label | premise_modality | hypothesis_modality | premise_language | hypothesis_language | premise_source | hypothesis_source |
|--------------|---------------|----------------|-----------------|-------|-----------------|-------------------|-----------------|-------------------|----------------|-----------------|
| "On stage, the innards of a piano are shown..." | None | "There are two men." | None | 0 | text | text | en | en | SNLI | SNLI |
| None | data/audio/fleures/file1.wav | "avec seulement dix-huit médailles disponibles..." | None | 0 | speech | text | fr | fr | FLEURS | FLEURS |
| "Mai umeed karta hun kai ap hamare contributor raho gai..." | None | None | data/audio/tts_generated/file1.wav | 2 | text | speech | ur | en | XNLI | TTS_generated |
| None | data/audio/fleures/file2.wav | None | data/audio/fleures/file3.wav | 1 | speech | speech | ar | en | FLEURS | FLEURS |

*Note*: For each row, the `premise` and `hypothesis` can independently be either text or speech.  
- `premise_text` / `hypothesis_text` contain text if that modality is present, otherwise `None`.  
- `premise_audio` / `hypothesis_audio` contain paths to audio files if that modality is present, otherwise `None`.  

This allows all modality combinations:  
- Text-Text (premise text, hypothesis text)  
- Text-Speech (premise text, hypothesis audio)  
- Speech-Text (premise audio, hypothesis text)  
- Speech-Speech (premise audio, hypothesis audio)  

In the table above, audio paths are shown for illustration. In the dataset, these paths can be loaded as audio arrays using the Hugging Face Audio feature after downloading and extracting the audio files.

## Uses

### Direct Use

- Training multimodal NLI models that handle text, speech, or both
- Research in multilingual reasoning, cross-lingual entailment, and speech-text NLI


## Dataset Structure

- Splits:  
  - train: pre-merged training split  
  - validation: validation set  
  - test: test set  

### Dataset Creation

#### Curation Rationale
This dataset was curated to provide a benchmark for multimodal and multilingual natural language inference. It supports research beyond similarity scoring by including both text and speech inputs across multiple languages, with labels for entailment, contradiction, and neutral.

#### Source Data
- **XNLI:** Human-annotated multilingual NLI text pairs  
- **SNLI:** English image-caption derived NLI pairs  
- **FLEURS:** Natural speech recordings in multiple languages  
- **TTS_generated:** Synthetic speech generated using Coqui TTS  
- **Mistral_generated:** NLI pairs generated by a fine-tuned Mistral 7B model  

#### Data Processing
- Audio paths are stored as strings; audio can be dynamically loaded using the Hugging Face `Audio` feature  
- Each example specifies the modality (text or speech) for both premise and hypothesis  
- Training, validation, and test splits are provided as separate sets within the dataset  
- Splits are pre-merged and ready to use; no further merging of files is required  

#### Annotations
- Labels (`0 = entailment`, `1 = contradiction`, `2 = neutral`) come from original datasets or were generated using a fine-tuned Mistral 7B model for synthetic data. 
- Each row may independently contain text, speech, or both for premise and hypothesis  

#### Personal and Sensitive Information
- Contains multilingual text and speech  
- No personally identifiable information beyond what may exist in source datasets  

## Bias, Risks, and Limitations

- Biases may exist due to source datasets (SNLI, XNLI, FLEURS)
- Limited speaker diversity in TTS-generated speech
- Non-commercial license limits downstream use


## Citation

### BibTeX
```bibtex
@inproceedings{istaiteh2025beyond,
  title={Beyond Similarity Scoring: Detecting Entailment and Contradiction in Multilingual and Multimodal Contexts},
  author={Istaiteh, Othman and Mdhaffar, Salima and Est{\`e}ve, Yannick},
  booktitle={Proc. Interspeech 2025},
  pages={286--290},
  year={2025}
}
```

APA:

Istaiteh, O., Mdhaffar, S., & Estève, Y. (2025). Beyond Similarity Scoring: Detecting Entailment and Contradiction in Multilingual and Multimodal Contexts. Interspeech 2025

## References

- Jiang, A. Q. et al. (2023). Mistral 7B. arXiv:2310.06825
- Conneau, A. et al. (2022). FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech. arXiv:2205.12446
- Conneau, A. et al. (2018). XNLI: Evaluating Cross-lingual Sentence Representations. EMNLP
- Bowman, S. R. et al. (2015). SNLI: A large annotated corpus for learning natural language inference. EMNLP
- Gölge, E., & Coqui TTS Team (2021). Coqui TTS. Zenodo


## Dataset Card Contact

- Email: othmanistaiteh@gmail.com