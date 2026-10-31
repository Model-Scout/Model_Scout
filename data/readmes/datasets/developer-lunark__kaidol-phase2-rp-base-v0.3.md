---
language:
- ko
- en
license: cc-by-nc-4.0
task_categories:
- text-generation
pretty_name: KAIDOL Phase 2 RP Base Dataset
size_categories:
- 100K<n<1M
tags:
- roleplay
- korean
- dialogue
- multiturn
- character-ai
- conversational
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-v0.3.jsonl
  - split: eval
    path: data/eval-v0.3.jsonl
---

---
language:
- ko
- en
license: cc-by-nc-4.0
task_categories:
- text-generation
pretty_name: KAIDOL Phase 2 RP Base Dataset
size_categories:
- 100K<n<1M
tags:
- roleplay
- korean
- dialogue
- multiturn
- character-ai
- conversational
- quality-filtered
- gpt-slop-filtered
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: eval
    path: data/eval-*
---

# KAIDOL Phase 2 RP Base Dataset v0.3

## Dataset Description

**KAIDOL Phase 2 RP Base v0.3** is a Korean-English bilingual conversational dataset designed for fine-tuning large language models (LLMs) for roleplay and character-based dialogue systems. This version includes **GPT-Slop filtering** to remove AI-sounding patterns and improve response quality.

### What's New in v0.3

- **GPT-Slop Filtering**: Removed `1,529` samples containing AI-sounding patterns
- **Cleaner Responses**: Filtered out identity leaks, refusals, sycophancy, and essay-style responses
- **Improved Quality**: Higher signal-to-noise ratio for better roleplay training

### Key Features

- **Bilingual**: Korean (66.0%) and English (34.0%)
- **Multiturn**: Average 8.0 turns per conversation
- **High Quality**: GPT-Slop filtered for natural character responses
- **Diverse Themes**: Multiple emotional/situational themes
- **Clean**: Automated quality checks with slop filtering

### Dataset Summary

| Split | Samples | Language Distribution |
|-------|---------|----------------------|
| Train | 70,569  | KO: 46,563 / EN: 24,006 |
| Eval  | 7,832   | KO: 5,225 / EN: 2,607 |
| **Total** | **78,401** | **KO: 66.0% / EN: 34.0%** |

## Dataset Structure

### Data Format

Each sample contains:

```python
{
    "messages": [
        {"role": "system", "content": "..."},
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."},
        ...
    ],
    "conversation_id": "conv_12345",
    "language": "ko",  # or "en"
    "source": "general-roleplay",
    "theme": "daily_chat",
    "num_turns": 5,
    "phase_id": "P2-Q30B-RP-BASE",
    "dataset_version": "v0.3"
}
```

### Data Fields

- `messages` (List[Dict]): Standard chat format with role and content
  - `role`: "system", "user", or "assistant"
  - `content`: Message text
- `conversation_id` (string): Unique conversation identifier
- `language` (string): "ko" or "en"
- `source` (string): Original data source
- `theme` (string): Conversation theme
- `num_turns` (int): Number of conversation turns
- `phase_id` (string): Experiment phase identifier
- `dataset_version` (string): Dataset version (v0.3)

### Theme Distribution (Top 5)

| Theme | Count | Ratio |
|-------|-------|-------|
| daily_chat | 41,193 | 0.0% |
| unknown | 17,896 | 0.0% |
| comfort | 3,116 | 0.0% |
| excited | 1,470 | 0.0% |
| surprised | 431 | 0.0% |

## Dataset Creation

### Source Data

The dataset combines multiple high-quality public datasets:

#### Public Datasets

**Korean RP**:
- general-roleplay: ~25,000 samples
- gf-persona: ~2,000 samples

**English**:
- hh-rlhf: ~10,000 samples
- conv_ai_2: ~3,500 samples
- PIPPA: ~12,000 samples
- WildChat-1M: ~5,000 samples

**Empathy**:
- empathetic_dialogues: ~8,000 samples
- chatbot_korean: ~5,000 samples

### Quality Assurance

#### GPT-Slop Filtering (v0.3)

The following patterns were detected and removed:

| Category | Patterns Removed | Examples |
|----------|------------------|----------|
| Identity Leak | "As an AI", "I am a language model" | AI identity disclosure |
| Refusal | "I cannot", "I'm not able to" | Content refusal patterns |
| Sycophancy | "Certainly!", "Great question!" | Overly agreeable responses |
| Essay Style | "In conclusion", "First, second, third" | Structured essay formats |
| Korean Slop | "제가 알고 있는 한", "일반적으로" | Korean AI filler phrases |

**Filtering Results**:
- Original samples: ~72,098 (train) / ~8,011 (eval)
- Filtered samples: 1,529
- Final samples: 70,569 (train) / 7,832 (eval)
- Filtering rate: ~0.0%

#### Quality Metrics

- **Format Consistency**: 5.0/5.0 (all samples in chat format)
- **Content Safety**: 5.0/5.0 (NSFW content filtered)
- **Metadata**: 5.0/5.0 (complete tagging)

### Data Processing Pipeline

1. **Collection**: Downloaded from public sources
2. **Deduplication**: MinHash LSH with 0.8 similarity threshold
3. **Format Standardization**: Converted to standard chat format
4. **GPT-Slop Filtering**: Removed AI-sounding patterns (v0.3)
5. **Metadata Injection**: Automatic phase_id, version tagging
6. **Quality Check**: Automated validation

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load dataset (requires authentication for private repo)
dataset = load_dataset(
    'developer-lunark/kaidol-phase2-rp-base-v0.3',
    token=True  # or token="hf_xxxxx"
)

train_data = dataset['train']
eval_data = dataset['eval']

print(f"Train samples: {len(train_data):,}")
print(f"Eval samples: {len(eval_data):,}")
```

### Training Example with Unsloth (Recommended)

```python
from unsloth import FastLanguageModel
from transformers import TrainingArguments
from trl import SFTTrainer
from datasets import load_dataset

# Load dataset
dataset = load_dataset('developer-lunark/kaidol-phase2-rp-base-v0.3', token=True)

# Load model with Unsloth
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Qwen3-30B-A3B-Instruct-2507",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True,
)

# Apply LoRA
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    bias="none",
    use_gradient_checkpointing="unsloth",
)

# Training configuration
training_args = TrainingArguments(
    output_dir="./kaidol-rp-base-v0.3",
    num_train_epochs=2,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=16,
    learning_rate=2e-4,
    warmup_ratio=0.03,
    logging_steps=50,
    save_steps=1000,
    fp16=False,
    bf16=True,
    optim="adamw_8bit",
)

# Initialize trainer
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset['train'],
    eval_dataset=dataset['eval'],
    dataset_text_field="messages",
    max_seq_length=2048,
)

# Train
trainer.train()
```

## Intended Use

### Primary Use Cases

- Fine-tuning LLMs for roleplay and character-based dialogue
- Training K-POP idol boyfriend character AI models
- Developing conversational AI with empathy and emotional intelligence
- Research on bilingual (Korean-English) dialogue systems

### Out-of-Scope Use

- This dataset is NOT suitable for:
  - General-purpose chatbots without character context
  - Translation tasks
  - Sentiment analysis
  - Content moderation

## Limitations

### Known Issues

1. **Theme Distribution**: Daily chat themes dominate
2. **Language Balance**: Slightly skewed towards Korean
3. **Domain Specificity**: Optimized for roleplay scenarios
4. **Context Length**: Max sequence length of 2048 tokens

### Mitigation in v0.3

- GPT-Slop filtering reduces generic AI responses
- Character consistency improved through cleaner data

## Bias and Ethical Considerations

### Bias Analysis

- **Language**: Bilingual (Korean-English) but excludes other languages
- **Culture**: Focused on Korean and Western conversational norms
- **Emotion**: Positive emotions (love, comfort) may be overrepresented

### Safety Measures

- All samples filtered for NSFW content
- Profanity detection applied
- GPT-Slop patterns removed for more natural responses

### Ethical Use

This dataset should be used responsibly:
- Not for harmful or deceptive purposes
- Respect user privacy and consent
- Consider cultural sensitivities
- Provide clear disclosure when AI-generated content is used

## License

**CC-BY-NC-4.0** (Creative Commons Attribution-NonCommercial 4.0 International)

This dataset is licensed for non-commercial use only.

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{kaidol_phase2_rp_base_v03,
  title={KAIDOL Phase 2 RP Base Dataset v0.3},
  author={Lunark AI Team},
  year={2025},
  version={v0.3},
  url={https://huggingface.co/datasets/developer-lunark/kaidol-phase2-rp-base-v0.3},
  license={CC-BY-NC-4.0}
}
```

## Contact

For questions, issues, or commercial licensing:
- Organization: Lunark AI
- HuggingFace: [@lunark-ai](https://huggingface.co/lunark-ai)
- Repository: [kaidol-llm-finetuning](https://github.com/Lunark-AI-Dev/kaidol-llm-finetuning)

## Changelog

### v0.3 (2025-01-07)

- **GPT-Slop Filtering**: Removed 1,529 samples with AI-sounding patterns
- Improved dataset quality for roleplay training
- Train: 70,569 samples / Eval: 7,832 samples
- Korean 66.0% / English 34.0%
- Average 8.0 turns per conversation

### v0.2 (Previous)

- Base dataset without GPT-Slop filtering
- ~72,098 train / ~8,011 eval samples

### v0.1 (2025-11-17)

- Initial release
- 60,190 samples

---

**Dataset Card Authors**: Lunark AI Team

**Last Updated**: 2026-01-07
