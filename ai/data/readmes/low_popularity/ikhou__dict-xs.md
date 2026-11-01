---
license: apache-2.0
language:
- multilingual
- en
- de
- fr
- es
- it
- pt
- nl
- pl
- sv
- da
- no
- fi
- cs
- ro
- hu
- ca
- ru
- uk
- bg
- sr
- el
- zh
- ja
- ko
- hi
- bn
- ur
- ta
- te
- mr
- th
- vi
- id
- ms
- fil
- ar
- fa
- tr
- he
- sw
- am
- yo
- lt
- sl
- et
- lv
- sk
- hr
- az
- kk
- uz
library_name: transformers
tags:
- dictionary
- translation
- multilingual
- bilingual
- glossing
- vocabulary
base_model: Qwen/Qwen3-0.6B
datasets:
- HuggingFaceFW/fineweb
- HuggingFaceFW/fineweb-2
pipeline_tag: text-generation
---

# Ikhou Dictionary Model (dict-xs)

A lightweight multilingual dictionary model based on Qwen3-0.6B, fine-tuned on 1.7M dictionary-style glosses across 50+ languages.

## Model Description

This model provides short, dictionary-style translations and glosses for words and phrases in context. It's designed for:
- Quick word lookups in reading applications
- Vocabulary learning tools
- Translation assistance
- Language learning applications

**Key Features:**
- 🌍 **50+ languages** supported (see list below)
- 📖 **Dictionary-style glosses** with grammatical markers
- ⚡ **Fast inference** (596M parameters, bfloat16)
- 🎯 **Context-aware** translations

## Supported Languages (50)

### Major European Languages
English, German, French, Spanish, Italian, Portuguese, Dutch, Polish, Swedish, Danish, Norwegian Bokmål, Finnish, Czech, Romanian, Hungarian, Catalan, Greek

### Cyrillic Script
Russian, Ukrainian, Bulgarian, Serbian

### Asian Languages
Chinese (Mandarin), Japanese, Korean, Hindi, Bengali, Urdu, Tamil, Telugu, Marathi, Thai, Vietnamese, Indonesian, Malay, Filipino

### Middle Eastern
Arabic, Persian, Turkish, Hebrew

### African
Swahili, Amharic, Yoruba

### Other
Lithuanian, Slovenian, Estonian, Latvian, Slovak, Croatian, Azerbaijani, Kazakh, Uzbek

## Grammar Markers Explained

The model outputs grammatical information using standard linguistic abbreviations:

### Noun Markers (Gender-based Languages)
- **nm.** = Masculine noun (e.g., "nm. roi, monarque" = king, monarch in French)
- **nf.** = Feminine noun (e.g., "nf. maison, demeure" = house, dwelling in French)
- **nn.** = Neuter noun (German, Russian) (e.g., "nn. Haus, Gebäude" = house, building)

### Noun Markers (Non-gendered Languages)
- **n.** = Noun (e.g., "n. house, home" in English)

### Other Parts of Speech
- **adj.** = Adjective (e.g., "adj. rapide, vite" = fast, quick)
- **adv.** = Adverb (e.g., "adv. rapidement, vite" = quickly, fast)
- **pp** = Past participle (e.g., "mangé → eaten, consumed (pp)")

### Verb Forms
For conjugated verbs, the model provides:
- Translation(s)
- Tense/mood information in parentheses
- Example: "venait → came, was coming (imparfait, il)" = imperfect tense, he

## Usage

### Basic Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "ikhou/dict-xs",
    torch_dtype="bfloat16",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("ikhou/dict-xs")

# Example: Get a French→English gloss
messages = [
    {
        "role": "system",
        "content": "You are a bilingual dictionary. Given a word/phrase in context, output a short gloss.\n\nRules:\n- One line only, no labels\n- Use grammar markers: nm./nf./nn. for gendered nouns, n. for others, adj., adv., verbs with tense info\n- 1-4 short translations, comma-separated\n- Apply markers based on definition language"
    },
    {
        "role": "user",
        "content": 'Expression: "maison"\nContext: Il habite dans une petite 【maison】 près de la mer.\nSource language: fra (French)\nDefinition language: eng (English)\n\nReturn the single-line gloss now.'
    }
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(
    inputs,
    max_new_tokens=50,
    temperature=0.3,
    do_sample=True,
    top_p=0.9
)

response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
print(response)  # Output: "nf. house, home"
```

### Input Format

The model expects:
1. **Expression**: The word/phrase to define
2. **Context**: Sentence with the expression (use 【】 to highlight)
3. **Source language**: ISO 639-3 code (e.g., fra, eng, deu)
4. **Definition language**: ISO 639-3 code

### Output Format

The model returns a single line with:
- Grammar marker (nm./nf./nn./n./adj./adv./pp)
- 1-4 short translations/synonyms, comma-separated
- For verbs: glosses + grammatical info in parentheses

## Training Details

### Training Data
- **Dataset**: 1.7M synthetic dictionary entries
- **Sources**: FineWeb (English), FineWeb-2 (49 other languages)
- **Generation**: GPT-4-based teacher model for quality glosses
- **Filtering**: Proper noun filtering, quality scoring

### Training Configuration
- **Base Model**: Qwen/Qwen3-0.6B
- **Training Type**: Full fine-tuning (not LoRA)
- **Precision**: bfloat16
- **Batch Size**: 32 per device
- **Gradient Accumulation**: 8 steps
- **Total Steps**: 6,568
- **Learning Rate**: AdamW with cosine schedule
- **Hardware**: NVIDIA H100 (95GB)
- **Training Time**: ~6 hours

### Training Results
- **Final Loss**: 1.30
- **Eval Loss**: 1.34
- **Training thoroughly validated** - no zero loss issues

## Model Architecture

- **Architecture**: Qwen3ForCausalLM
- **Parameters**: 596M
- **Layers**: 28 transformer layers
- **Hidden Size**: 1024
- **Attention Heads**: 16 (8 KV heads)
- **Context Length**: 40,960 tokens (model max, trained on 512)
- **Vocabulary**: 151,936 tokens

## Limitations

- **Context**: Works best with clear, simple contexts
- **Proper nouns**: May struggle with names, places, brands
- **Rare languages**: Better performance on high-resource languages
- **Multi-word phrases**: Best for 1-6 token phrases
- **Ambiguity**: Provides common meanings, may miss context-specific nuances

## Ethical Considerations

- **Bias**: Trained on web data which may contain biases
- **Not for sensitive applications**: Dictionary glosses may have errors
- **Educational use**: Best for learning and reference, not authoritative translation

## License

Apache 2.0

## Citation

```bibtex
@misc{ikhou-dict-xs,
  author = {Ikhou},
  title = {Ikhou Dictionary Model (dict-xs)},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/ikhou/dict-xs}}
}
```

## Acknowledgments

- Based on [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) by Alibaba Cloud
- Training data sourced from [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) and [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2)
- Trained with [Hugging Face Transformers](https://github.com/huggingface/transformers)

## Contact

For issues or questions, please open an issue on the [model repository](https://huggingface.co/ikhou/dict-xs/discussions).
