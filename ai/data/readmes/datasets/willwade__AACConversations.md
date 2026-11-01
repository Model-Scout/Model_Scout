---
language:
- en
- fr
- de
- es
- it
- nl
- el
- ru
- he
- ar
- pt
- cy
- ja
- zh
- ko
- nb
- sv
- da
- fi
- cs
- sk
- pl
- hu
- sl
- hr
- uk
- eu
- ca
- fo
- af
license: cc-by-4.0
multilinguality: multilingual
size_categories:
- 10K<n<100K
task_categories:
- text-generation
- text-classification
task_ids:
- language-modeling
- sentiment-analysis
- text-simplification
pretty_name: AAC Conversations Dataset (2024)
tags:
- aac
- augmentative-alternative-communication
- assistive-technology
- conversation
- multilingual
- text-correction
- text-generation
---

# AAC Conversations Dataset

## Dataset Description

The AAC Conversations Dataset is a collection of simulated conversations involving Augmentative and Alternative Communication (AAC) users across multiple languages. This dataset is designed to help researchers and developers build better assistive technologies for people who use AAC devices.

### Dataset Summary

This dataset contains conversations between AAC users and communication partners in various scenarios. Each conversation includes both the original utterances and various augmented versions that simulate different types of typing errors that commonly occur when using AAC devices. The dataset supports multiple languages, making it valuable for developing multilingual assistive technologies.

## Dataset Structure

### Data Instances

Each instance in the dataset represents a single utterance from an AAC user, along with context from the conversation and various augmented versions of the utterance.

Example:
```json
{
  "conversation_id": 42,
  "turn_number": 2,
  "language_code": "en-GB",
  "scene": "At a doctor's appointment",
  "context_speakers": ["Doctor", "Patient (AAC)"],
  "context_utterances": ["How have you been feeling lately?", "Not great"],
  "speaker": "Patient (AAC)",
  "utterance": "I've been having trouble sleeping",
  "utterance_intended": "I've been having trouble sleeping",
  "next_turn_speaker": "Doctor",
  "next_turn_utterance": "How long has this been going on?",
  "model": "gpt-4o-mini",
  "provider": "openai",
  "batch_id": "batch_682477c828bc81909f580a018af3a06c",
  "batch_number": 3,
  "noisy_qwerty_minimal": "I've been having troubke sleeping",
  "noisy_qwerty_light": "I've been havng troble sleepng",
  "noisy_qwerty_moderate": "I've ben havin troble sleping",
  "noisy_qwerty_severe": "Ive ben havin trble slping",
  "noisy_abc_minimal": "I've been having troubke sleeping",
  "noisy_abc_light": "I've been havng troble sleepng",
  "noisy_abc_moderate": "I've ben havin troble sleping",
  "noisy_abc_severe": "Ive ben havin trble slping",
  "noisy_frequency_minimal": "I've been having troubke sleeping",
  "noisy_frequency_light": "I've been havng troble sleepng",
  "noisy_frequency_moderate": "I've ben havin troble sleping",
  "noisy_frequency_severe": "Ive ben havin trble slping",
  "minimally_corrected": "I've been having trouble sleeping.",
  "fully_corrected": "I've been having trouble sleeping."
}
```

### Data Fields

#### Conversation Structure Fields
- `conversation_id`: Unique identifier for each conversation
- `turn_number`: The position of this utterance in the conversation
- `language_code`: The language code of the conversation (e.g., "en-GB", "fr-FR")
- `scene`: Description of the conversation setting
- `model`: The model used to generate the conversation (e.g., "gpt-4o-mini", "gpt-4.1-mini-2025-04-14")
- `provider`: The provider of the model (e.g., "openai", "unknown")
- `batch_id`: Identifier for the batch of data (e.g., "v1" for older data, specific batch IDs for newer data)
- `batch_number`: Batch number (0 for v1 dataset, 1-3 for newer batches)

#### Speaker and Utterance Fields
- `speaker`: The speaker of the current utterance
- `utterance`: The original utterance as typed by the AAC user
- `utterance_intended`: The intended utterance (what the user meant to type)

#### Context Fields (Flattened for Better Usability)
- `context_speakers`: List of speakers for the previous turns (up to 3)
- `context_utterances`: List of utterances for the previous turns (up to 3)
- `next_turn_speaker`: Speaker of the next turn in the conversation
- `next_turn_utterance`: Utterance of the next turn in the conversation

#### Augmented Utterance Fields
- `noisy_qwerty_minimal`: Utterance with minimal typing errors based on QWERTY keyboard layout
- `noisy_qwerty_light`: Utterance with light typing errors based on QWERTY keyboard layout
- `noisy_qwerty_moderate`: Utterance with moderate typing errors based on QWERTY keyboard layout
- `noisy_qwerty_severe`: Utterance with severe typing errors based on QWERTY keyboard layout
- `noisy_abc_minimal`: Utterance with minimal typing errors based on ABC keyboard layout
- `noisy_abc_light`: Utterance with light typing errors based on ABC keyboard layout
- `noisy_abc_moderate`: Utterance with moderate typing errors based on ABC keyboard layout
- `noisy_abc_severe`: Utterance with severe typing errors based on ABC keyboard layout
- `noisy_frequency_minimal`: Utterance with minimal typing errors based on frequency keyboard layout
- `noisy_frequency_light`: Utterance with light typing errors based on frequency keyboard layout
- `noisy_frequency_moderate`: Utterance with moderate typing errors based on frequency keyboard layout
- `noisy_frequency_severe`: Utterance with severe typing errors based on frequency keyboard layout
- `minimally_corrected`: Minimally corrected version of the utterance
- `fully_corrected`: Fully corrected version of the utterance

### Languages

The dataset includes conversations in 39 languages:

**European Languages**
- English (en-GB, en-US, en-CA, en-AU, en-NZ, en-ZA)
- French (fr-FR, fr-CA)
- German (de-DE, de-AT)
- Spanish (es-ES, es-US)
- Italian (it-IT)
- Dutch (nl-NL, nl-BE)
- Greek (el-GR)
- Russian (ru-RU)
- Portuguese (pt-PT, pt-BR)
- Welsh (cy-GB)
- Irish (ga-IE)
- Norwegian (nb-NO)
- Swedish (sv-SE)
- Danish (da-DK)
- Finnish (fi-FI)
- Czech (cs-CZ)
- Slovak (sk-SK)
- Polish (pl-PL)
- Hungarian (hu-HU)
- Slovenian (sl-SI)
- Croatian (hr-HR)
- Ukrainian (uk-UA)
- Basque (eu-ES)
- Catalan (ca-ES)
- Faroese (fo-FO)
- Afrikaans (af-ZA)

**Middle Eastern & Asian Languages**
- Hebrew (he-IL)
- Arabic (ar-SA)
- Japanese (ja-JP)
- Chinese (zh-CN)
- Korean (ko-KR)

### Dataset Statistics

The dataset contains:
- Over 86,000 examples across train and test splits
- 39 languages represented
- Approximately 300 conversations per language
- Multiple batches of data (v1 and batches 1-3)

The dataset is split into:
- Train split: ~68,800 examples
- Test split: ~17,200 examples

**MLU**: Mean Length of Utterance (average number of words per utterance)

## Dataset Creation

### Curation Rationale

AAC users often experience challenges with text entry that can lead to typing errors. This dataset was created to help develop and evaluate technologies that can assist AAC users by correcting typing errors, predicting text, and improving communication efficiency across multiple languages.

### Source Data

The conversations in this dataset are simulated based on common scenarios that AAC users might encounter in daily life, including medical appointments, social interactions, educational settings, and more.
You can see the code to make it at https://github.com/willwade/AACDataSet


### Generation Process

The dataset was created through a multi-step process:

1. **Template Creation**: Conversation templates were created with diverse scenarios relevant to AAC users
2. **Generation**: Conversations were generated using OpenAI's GPT-4o-mini model to create realistic AAC interactions
3. **Transformation**: Raw outputs were transformed into a structured format
4. **Augmentation**: AAC utterances were augmented with various noise levels and keyboard layouts
5. **Correction**: Both minimal and full corrections were added to each AAC utterance
6. **Multilingual Expansion**: Templates were translated and adapted for 39 languages

Each conversation in the dataset includes metadata about which model and provider were used to generate it (model="gpt-4o-mini", provider="openai" for most conversations, with some older conversations using different models), as well as batch information that allows tracking the dataset version.

### Annotations

The dataset includes several types of augmented utterances that simulate typing errors:

- **Error Rates**:
  - Minimal: 5% errors - very mild typing issues
  - Light: 15% errors - noticeable but clearly readable
  - Moderate: 25% errors - challenging but comprehensible
  - Severe: 35% errors - significant difficulty

- **Keyboard Layouts**:
  - QWERTY: Standard keyboard layout
  - ABC: Alphabetical keyboard layout
  - Frequency: Layout based on letter frequency

Each language uses appropriate keyboard layouts and letter frequencies for that language.

### Personal and Sensitive Information

This dataset does not contain any personal or sensitive information. All conversations are simulated and do not represent real individuals.

## Potential Uses

This dataset can be used for a variety of NLP tasks related to AAC:

1. **AAC Utterance Correction**: Train models to correct noisy AAC input
2. **Telegraphic Speech Expansion**: Expand telegraphic AAC utterances into grammatically complete sentences
3. **AAC Response Prediction**: Predict appropriate responses to AAC utterances
4. **AAC Interface Optimization**: Study error patterns across different keyboard layouts
5. **Multilingual Assistive Technology**: Develop assistive technologies that work across multiple languages
6. **Cross-lingual Transfer Learning**: Explore how models trained on one language can be adapted to others

## Considerations for Using the Data

### Social Impact of Dataset

This dataset aims to improve assistive technologies for people who use AAC devices, potentially enhancing their communication abilities and quality of life across multiple languages and cultures.

### Discussion of Biases

The dataset attempts to represent diverse scenarios and contexts, but may not capture all the nuances of real AAC user experiences. Users of this dataset should be aware of potential biases in the simulated conversations.

### Other Known Limitations

- The typing errors are generated algorithmically and may not perfectly represent the patterns of errors that real AAC users make
- Some languages have more comprehensive support than others
- The dataset focuses primarily on text-based communication and does not include symbol-based AAC

## Additional Information

### Licensing Information

This dataset is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

### Citation Information

If you use this dataset in your research, please cite:

```
@dataset{aac_conversations_dataset,
  author = {Wade, Will},
  title = {AAC Conversations Dataset},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/willwade/AACConversations}
}
```

### Contributions

Thanks to all who contributed to the creation of this dataset! 
Note it was made as part of a collaboration between Smartbox Assistive Technology and Ace Centre


## How to Use

Here's a simple example of how to load and explore the dataset:

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("willwade/AACConversations")

# Access the train and test splits
train_data = dataset["train"]
test_data = dataset["test"]

# Print the first example
print(train_data[0])

# Filter examples by language
english_examples = train_data.filter(lambda example: example["language_code"] == "en-GB")
print(f"Number of English examples: {len(english_examples)}")

# Example of a task: AAC utterance correction
for example in train_data.select(range(5)):
    print(f"Original: {example['noisy_qwerty_moderate']}")
    print(f"Corrected: {example['fully_corrected']}")
    print()
```

### Retrieving Complete Conversations

To retrieve all utterances from a specific conversation, you can use the following function:

```python
def get_complete_conversation(dataset, conversation_id):
    """
    Retrieve all utterances from a specific conversation.

    Args:
        dataset: The Hugging Face dataset
        conversation_id: The ID of the conversation to retrieve

    Returns:
        A list of utterances in the conversation, sorted by turn_number
    """
    # Filter the dataset to get all utterances from the conversation
    conversation = dataset.filter(lambda example: example["conversation_id"] == conversation_id)

    # Convert to list and sort by turn_number
    conversation_list = sorted(
        list(conversation), key=lambda x: x["turn_number"]
    )

    return conversation_list

# Example usage
conversation_id = 1  # Replace with the desired conversation ID
conversation = get_complete_conversation(train_data, conversation_id)

# Print the conversation
print(f"Conversation {conversation_id}:")
for turn in conversation:
    speaker = turn["speaker"]
    utterance = turn["utterance"]
    print(f"{speaker}: {utterance}")
```

If you're working with pandas DataFrames (e.g., when loading from CSV files locally), you can use:

```python
def get_complete_conversation_pandas(df, conversation_id):
    """Get all utterances from a specific conversation using pandas."""
    # Filter the dataframe to get all utterances from the conversation
    conversation = df[df["conversation_id"] == conversation_id]

    # Sort by turn_number
    conversation_sorted = conversation.sort_values(by="turn_number")

    return conversation_sorted

# Example usage with pandas
import pandas as pd
df = pd.read_csv("huggingface/data/aac_dataset_merged/train/dataset.csv")
conversation = get_complete_conversation_pandas(df, 114)

# Print the conversation
print(f"Conversation {conversation['conversation_id'].iloc[0]}")
print(f"Language: {conversation['language_code'].iloc[0]}")
print(f"Scene: {conversation['scene'].iloc[0]}")

for _, turn in conversation.iterrows():
    speaker = turn["speaker"]
    utterance = turn["utterance"]
    print(f"{speaker}: {utterance}")
```

### Filtering by Language, Model, Provider, or Batch

You can filter the dataset by language, model, provider, or batch ID:

```python
# Filter by language
english_examples = train_data.filter(lambda example: example["language_code"] == "en-GB")
print(f"Number of English examples: {len(english_examples)}")

# Filter by model
gpt4o_examples = train_data.filter(lambda example: example["model"] == "gpt-4o-mini")
print(f"Number of examples generated with GPT-4o-mini: {len(gpt4o_examples)}")

# Filter by provider
openai_examples = train_data.filter(lambda example: example["provider"] == "openai")
print(f"Number of examples from OpenAI: {len(openai_examples)}")

# Filter by batch
v1_examples = train_data.filter(lambda example: example["batch_id"] == "v1")
print(f"Number of examples from batch v1: {len(v1_examples)}")

# Combine filters
english_gpt4o_examples = train_data.filter(
    lambda example: example["language_code"] == "en-GB" and example["model"] == "gpt-4o-mini"
)
print(f"Number of English examples generated with GPT-4o-mini: {len(english_gpt4o_examples)}")
```

With pandas:

```python
import pandas as pd
df = pd.read_csv("huggingface/data/aac_dataset_merged/train/dataset.csv")

# Filter by language
english_examples = df[df["language_code"] == "en-GB"]
print(f"Number of English examples: {len(english_examples)}")

# Filter by model
gpt4o_examples = df[df["model"] == "gpt-4o-mini"]
print(f"Number of examples generated with GPT-4o-mini: {len(gpt4o_examples)}")

# Filter by provider
openai_examples = df[df["provider"] == "openai"]
print(f"Number of examples from OpenAI: {len(openai_examples)}")

# Filter by batch
v1_examples = df[df["batch_id"] == "v1"]
print(f"Number of examples from batch v1: {len(v1_examples)}")

# Combine filters
english_gpt4o_examples = df[
    (df["language_code"] == "en-GB") & (df["model"] == "gpt-4o-mini")
]
print(f"Number of English examples generated with GPT-4o-mini: {len(english_gpt4o_examples)}")
```

### Example Scripts

The repository includes example scripts in the `examples` directory that demonstrate how to work with the dataset:

1. `example_get_conversation.py`: Demonstrates how to retrieve and display a complete conversation
2. `example_filter_dataset.py`: Demonstrates how to filter the dataset by language, model, provider, and batch ID

You can download and run these scripts locally:

```bash
git clone https://huggingface.co/datasets/willwade/AACConversations
cd AACConversations/examples

# Run the example scripts
python example_get_conversation.py
python example_filter_dataset.py --language en-GB
```

See the README in the examples directory for more information.

### Accessing Raw Data

The raw data files used to create this dataset are included in the repository in the `batch_files` directory. Each language has its own subdirectory containing:

1. Original batch files: `batch_output_*.jsonl`
2. Transformed files: `*_transformed.jsonl`
3. Augmented files: `*_augmented.jsonl`

You can access these files directly from the repository or clone the repository to explore them locally:

```bash
git clone https://huggingface.co/datasets/willwade/AACConversations
cd AACConversations/batch_files
```

To explore a specific language's raw data:

```bash
cd batch_files/en-GB
ls -la
```

This will show you all the raw files for English (UK) conversations, including the original batch outputs, transformed files, and augmented files.
