---
language:
  - ko
license: cc-by-nc-4.0
task_categories:
  - text-generation
size_categories:
  - 10K<n<100K
configs:
  - config_name: alpaca
    data_files: train_alpaca.jsonl
  - config_name: chatml
    data_files: train_chatml.jsonl
dataset_info:
  features:
    - name: instruction
      dtype: string
      description: 사용자의 운세 요청 또는 질문
    - name: input
      dtype: string
      description: 추가 맥락 정보 (대부분 비어있음)
    - name: output
      dtype: string
      description: AI 생성 운세 해석 및 조언
    - name: domain
      dtype: string
      description: 운세 도메인 (astrology, bazi, tarot, hwatu)
    - name: source
      dtype: string
      description: 데이터 출처
  splits:
    - name: train
      num_examples: 31625
---

# Yeji Fortune-Telling Korean SFT Dataset v9

## Dataset Summary

**Yeji-fortune-telling-ko-v9** is a comprehensive supervised fine-tuning (SFT) dataset for training Korean language models on fortune-telling and divination tasks. It contains 31,625 high-quality instruction-output pairs across four divination domains: Astrology, Bazi, Tarot, and Hwatu.

## Dataset Statistics

### Total Records: 31,625

| Domain | Records | Percentage |
|--------|---------|-----------|
| Astrology (점성술) | 10,000 | 31.6% |
| Bazi (사주) | 8,423 | 26.6% |
| Tarot (타로) | 6,621 | 20.9% |
| Hwatu (화투) | 6,581 | 20.8% |

### Data Distribution by Source

| Source | Records | Percentage |
|--------|---------|-----------|
| horoscope_saved | 9,844 | 31.1% |
| gpt5mini_synthesized | 8,423 | 26.6% |
| gemini-3-flash | 6,621 | 20.9% |
| hwatu_synthesized | 6,581 | 20.8% |
| horoscope_saved_gpt5mini_fixed | 156 | 0.5% |

## File Descriptions

### 1. train_alpaca.jsonl

**Format:** Alpaca instruction-following format

Each line contains:
- `instruction`: User's fortune-telling question or request
- `input`: Additional context (mostly empty)
- `output`: Expert-level divination interpretation and advice
- `domain`: Divination type (astrology, bazi, tarot, hwatu)
- `source`: Data origin

**Best For:** Traditional instruction-tuning, models expecting instruction/input/output structure

### 2. train_chatml.jsonl

**Format:** ChatML conversation format (Qwen, Llama Chat compatible)

Each line contains:
- `messages`: List of user and assistant turn messages
- `domain`: Divination type

**Best For:** Multi-turn conversation fine-tuning, chat-based applications

### 3. yeji_v9_train.jsonl

Legacy format (Alpaca-based). Use `train_alpaca.jsonl` for new projects.

## Domains

**Astrology (점성술)** - 10,000 records
- Western zodiac horoscope readings
- Personality, relationships, career, health predictions
- Astrological aspects and planetary influences

**Bazi (사주)** - 8,423 records
- Chinese Four Pillars of Destiny analysis
- Fortune based on birth time and date
- Career, relationships, personality insights

**Tarot (타로)** - 6,621 records
- Celtic Cross and other spread interpretations
- Card meanings and combined symbolism
- Life guidance and decision-making support

**Hwatu (화투)** - 6,581 records (NEW in v9)
- Traditional Korean card divination
- Card-based decision-making guidance
- Yes/No and choice-based fortunes

## Usage Examples

### Loading with HuggingFace Datasets

```python
from datasets import load_dataset

dataset = load_dataset("json", data_files="train_alpaca.jsonl", split="train")
print(f"Total records: {len(dataset)}")
print(dataset[0])
```

### Filtering by Domain

```python
import json

tarot_records = [
    json.loads(line) for line in open("train_alpaca.jsonl")
    if json.loads(line)["domain"] == "tarot"
]
print(f"Tarot records: {len(tarot_records)}")
```

### Fine-tuning with LoRA

```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model

dataset = load_dataset("json", data_files="train_alpaca.jsonl", split="train")

def format_alpaca(example):
    return {
        "text": f"[INST] {example['instruction']} [/INST] {example['output']}"
    }

dataset = dataset.map(format_alpaca)

model_name = "Qwen/Qwen2-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    lora_dropout=0.05,
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, lora_config)

args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=4,
)

trainer = Trainer(model=model, args=args, train_dataset=dataset)
trainer.train()
```

## Dataset Characteristics

### Quality Assurance

All records validated for:
- JSON integrity and valid parsing
- Required fields present (instruction, output, domain, source)
- Proper domain categorization
- Native Korean language quality
- Semantic coherence of instruction-output pairs
- Duplication removal

### Quality Features

- Professional expertise in divination domains
- Cultural authenticity and sensitivity
- Balanced compassionate and practical tone
- Detailed, long-form interpretations
- Multi-perspective divination approaches

## Version History

### v9 (2026-02-05) - Current Release

**New:**
- Added Hwatu (화투) domain: 6,581 records
- Total expansion: 25,044 → 31,625 records
- Both Alpaca and ChatML formats
- Enhanced validation pipeline

**Composition:**
- Astrology: 10,000 records
- Bazi: 8,423 records
- Tarot: 6,621 records
- Hwatu: 6,581 records (NEW)

### v8 (Previous)

- 25,044 records
- Three domains: Astrology, Bazi, Tarot
- Alpaca format only

## License & Citation

**License:** CC-BY-NC-4.0 (Creative Commons Attribution-NonCommercial 4.0)

Non-commercial use only. Attribution required.

**Citation:**

```bibtex
@dataset{yeji_fortune_telling_v9_2026,
  title={Yeji Fortune-Telling Korean SFT Dataset v9},
  author={SSAFY Fortune-Telling Project},
  year={2026},
  month={February},
  publisher={HuggingFace Datasets},
  url={https://huggingface.co/datasets/tellang/yeji-fortune-telling-ko-v9},
  note={31,625 Korean fortune-telling instruction-output pairs}
}
```

## Tags

- **Language:** Korean (한국어)
- **Tasks:** text-generation, instruction-following, conversation, fine-tuning
- **Domains:** divination, fortune-telling, astrology, bazi, tarot, hwatu, culture
- **Models:** qwen, llama, causal-lm, sft

## Important Considerations

### Content Notes
- Traditional divination content (not scientific)
- For cultural and entertainment purposes
- Responses are interpretive, not factual predictions
- Not for medical, financial, or critical decision-making

### Recommendations
1. Cross-validate outputs with domain experts
2. Consider domain-specific LoRA adapters
3. Implement safety filters for factual claims
4. Be aware of cultural assumptions

## Metadata

| Property | Value |
|----------|-------|
| Dataset Size | 115 MB (combined JSONLs) |
| Total Examples | 31,625 |
| Language | Korean (ko) |
| License | CC-BY-NC-4.0 |
| Last Updated | 2026-02-05 |
| Status | Active |

---

**Identifier:** tellang/yeji-fortune-telling-ko-v9  
**Release Date:** February 5, 2026  
**Card Version:** 1.0

