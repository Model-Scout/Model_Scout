---
language:
- lv
license: cc-by-sa-3.0
size_categories:
- 100K<n<1M
task_categories:
- question-answering
pretty_name: Latvian Wikipedia QA Synthetic Dataset
tags:
- latvian
- wikipedia
- qa
- conversational
- multi-turn
- synthetic
- gemma
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 306571250
    num_examples: 118507
  download_size: 162584473
  dataset_size: 306571250
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Latvian Wikipedia QA Synthetic Dataset

## Dataset Description

This dataset contains approximately **118,000 multi-turn conversations** with approximately **454,000 synthetic question-answer pairs** generated from Latvian Wikipedia articles using Gemma 3 27B.

### Dataset Summary

- **Language**: Latvian (lv)
- **Task**: Question Answering, Conversational AI
- **Format**: Multi-turn conversations with user-assistant exchanges
- **Total Conversations**: ~118,000
- **Total Q&A Pairs**: ~454,000
- **Avg Q&A per article**: 3.83
- **Avg messages per conversation**: 7.67

## Dataset Details

### Source Data

- **Base Content**: Latvian Wikipedia articles
- **Wikipedia Dump**: lvwiki-20241020-pages-articles-multistream.xml.bz2 (October 20, 2024)
- **Source License**: CC-BY-SA 3.0
- **Wikipedia URL**: https://lv.wikipedia.org/
- **Dump Download**: https://wikimedia.org/

### Synthetic Generation

- **Method**: LLM-generated question-answer pairs from Wikipedia article content
- **Model Used**: **Google Gemma 3 27B**
- **Process**: The model was prompted to generate relevant questions and comprehensive answers based on article content
- **Markers**: Generated Q&A pairs used JTJ: (Jautājums/Question) and ATB: (Atbilde/Answer) markers in Latvian

#### Prompt Template

The following prompt was used to generate Q&A pairs from Wikipedia articles:

```
Mani dati par {title}: {text} Manu datu beigas. Izveido pilnvērtīgus {num_questions} 
jautājumu un atbilžu pārus par šiem maniem datiem kā sarunu starp asistentu un lietotāju. 
Jautājumiem jābūt dažādiem, īsiem un kodolīgiem. Atbildēm jābūt izsmeļošām un garām, 
izstāstošām. Pirmais jautājums ir par datu galveno tēmu, tam ir jāsatur tēmas nosaukums, 
lai varētu saprat, par ko ir jautājums, neredzot datus. Atbilde gara un izstāstoša, tad 
katrs nākošais jautājums ir precizējošāks un atbildes īsākas. Svarīga ir kvalitatīva 
latviešu valodas izmantošana jautājumos un atbildēs bez kļūdām.

Piemērs:
JTJ: īss lietotāja jautājums, kas skaidri un nepārprotami ietver tēmas nosaukumu un ir 
     paskaidrojošs bez papildus datiem
ATB: gara un izstāstoša asistenta atbilde
JTJ: īss lietotāja jautājums
ATB: gara un izstāstoša asistenta atbilde
JTJ: īsāks lietotāja jautājums
ATB: izstāstoša asistenta atbilde
JTJ: īsāks lietotāja precizējošs jautājums
ATB: īsāka asistenta atbilde

Un tā tālāk. Pašā atbildē nav jānorāda, vai tā ir paskaidrojoša, precizējoša vai īsa.
Tas ir dzīvīgs dialogs starp asistentu un lietotāju.
Raksti tīru tekstu bez papildu formatējuma, piemēram, '**'.
Pārliecinies, ka izmantotie vārdi latviešu valodā pastāv un ir pareizi pielietoti. 
Jautājumus formulē vienkāršā valodā, kodolīgus un īsus.
```

**Key aspects of the prompt:**
- First question must be comprehensive and include the topic title
- Questions progressively become more specific
- Answers start long and detailed, then become shorter
- Emphasizes high-quality Latvian language usage
- Requires natural, conversational dialogue
- Plain text output without formatting markers

### Dataset Structure

Each example contains a single field with multi-turn conversations:

```python
{
  "messages": [
    {"role": "user", "content": "Kāda ir Edi Ramas politiskā karjera?"},
    {"role": "assistant", "content": "Edi Rama sāka savu politisko karjeru..."},
    {"role": "user", "content": "Kāda bija viņa loma Tirānā?"},
    {"role": "assistant", "content": "Rama kļuva par Tirānas mēru 2000. gadā..."},
    # ... more related Q&A pairs about the same topic
  ]
}
```

**Key Features:**
- All Q&A pairs from the same Wikipedia article are grouped into one conversation
- Preserves topical context across multiple question-answer exchanges
- Questions are in Latvian, answers are comprehensive and contextual

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("martinsu/latvian-wikipedia-qa-gemma3")

# Check structure
print(f"Total conversations: {len(dataset)}")
print(f"Example: {dataset[0]}")

# Use with your training framework
for conversation in dataset:
    messages = conversation['messages']
    # Apply your model's chat template
    # formatted = tokenizer.apply_chat_template(messages)
```

## Dataset Generation

### Prompt Strategy

The generation process involved:
1. Feeding Wikipedia article content to Gemma 3 27B
2. Prompting the model to generate relevant questions (JTJ:) and detailed answers (ATB:)
3. Generating multiple Q&A pairs per article to cover different aspects
4. Ensuring answers are comprehensive and contextually grounded in the article

### Quality Control

- **Parsing**: Robust extraction handles variations in LLM output format
- **Grouping**: Q&A pairs from the same article kept together as conversations
- **Cleaning**: Removal of marker artifacts, normalization of whitespace
- **Validation**: Each conversation contains at least one valid Q&A pair

### Processing Pipeline

1. Source: Latvian Wikipedia articles
2. Generation: Gemma 3 27B produces Q&A pairs with JTJ:/ATB: markers
3. Parsing: Extract questions and answers using pattern matching with fallbacks
4. Grouping: All Q&A from same article combined into multi-turn conversation
5. Formatting: Converted to HuggingFace standard with user/assistant roles

## Statistics

- **Total Articles Processed**: 118,507
- **Total Q&A Pairs**: ~454,265
- **Total Conversations**: 118,507
- **Average Q&A per Article**: 3.83
- **Average Messages per Conversation**: 7.67

## Intended Use

### Primary Use Cases

- **Fine-tuning** Latvian language models for question answering
- **Instruction tuning** for Latvian LLMs
- **Training** conversational AI systems for Latvian
- **Research** on multi-turn dialogue systems
- **Evaluation** of Latvian language understanding

### Recommended Applications

- Educational Q&A systems
- Latvian language assistants
- Wikipedia-based chatbots
- Knowledge retrieval systems

### Out-of-Scope Use

This dataset is intended for research and educational purposes. It should **not** be used for:
- Making factual claims without verification against original sources
- Applications requiring 100% factual accuracy
- Safety-critical or high-stakes decision making
- Medical, legal, or financial advice

## Limitations

- **Synthetic Nature**: All Q&A pairs are LLM-generated and may contain hallucinations or inaccuracies
- **Model Dependence**: Quality depends on Gemma 3 27B's capabilities and potential biases
- **Source Limitations**: Inherits any biases or limitations present in Wikipedia content
- **Language**: Latvian only, may not generalize to other languages
- **Temporal**: Based on Wikipedia snapshot; information may be outdated
- **Coverage**: Limited to topics present in processed Wikipedia articles

### Known Issues

- Some generated questions may be repetitive or overly similar
- Answers may occasionally include information not explicitly in source article
- Complex or nuanced topics may have oversimplified answers
- Model may have difficulty with highly technical or specialized content

## Licenses

### Wikipedia Content
- **License**: [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
- **Attribution**: Content derived from Latvian Wikipedia (https://lv.wikipedia.org/)

### Synthetic Q&A Generation
- **License**: CC-BY-SA 3.0 (inherits from Wikipedia source material)
- **Model**: Generated using Google Gemma 3 27B

### Gemma Terms of Use
This dataset contains outputs generated using **Gemma 3 27B**, which is provided under the Gemma Terms of Use found at [ai.google.dev/gemma/terms](https://ai.google.dev/gemma/terms). By using this dataset, you agree to comply with the Gemma Terms of Use.

### Dataset License
The overall dataset is released under **CC-BY-SA 3.0** to maintain compatibility with Wikipedia's licensing requirements.

## Citation

If you use this dataset in your research or applications, please cite:

```bibtex
@dataset{latvian_wiki_qa_synthetic_2025,
  author = {Martins Udris},
  title = {Latvian Wikipedia QA Synthetic Dataset},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/martinsu/latvian-wikipedia-qa-gemma3}},
  note = {Generated using Google Gemma 3 27B from Latvian Wikipedia articles}
}
```

### Acknowledgments

- **Wikipedia**: Source content from Latvian Wikipedia contributors under CC-BY-SA 3.0
- **Google**: Gemma 3 27B model used for synthetic Q&A generation
- **Community**: Thanks to the open-source NLP community for tools and frameworks

## Contact

- **Creator**: Martins Udris
- **Issues**: Please open an issue on the dataset repository for questions or concerns
- **Contributions**: Suggestions for improvements are welcome

## Version History

- **v1.0** (2025): Initial release with 118,507 conversations
- **v1.1** (2025): Cleaned up few Q and A pairs after audit - repetition in text and answers like "Jā."
---

**Disclaimer**: This is a synthetic dataset generated by an AI model. While efforts have been made to ensure quality, users should verify information against authoritative sources for critical applications.
