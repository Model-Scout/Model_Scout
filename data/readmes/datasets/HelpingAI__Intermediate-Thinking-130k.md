---
license: apache-2.0
task_categories:
- text-generation
language:
- af
- ar
- bn
- bg
- ca
- zh
- cs
- da
- nl
- en
- et
- fi
- fr
- de
- el
- he
- hi
- hu
- id
- it
- ja
- ko
- mr
- no
- fa
- pl
- pt
- ro
- ru
- so
- es
- sw
- sv
- tl
- ta
- te
- th
- tr
- uk
- ur
- vi
- cy
tags:
- intermediate-thinking
- mathematical-reasoning
- logical-reasoning
- self-correction
- structured-thinking
pretty_name: Intermediate Thinking Dataset
extra_gated_prompt: >-
  Thank you for your interest in accessing **Intermediate-Thinking-130k**, a dataset by HelpingAI Labs.  
  To ensure responsible and fair usage, please confirm the following before access:

  - I will use this dataset only for legitimate research / education / evaluation / development purposes.  
  
  - I understand that HelpingAI prioritizes user privacy and data protection.  
  
  - I agree not to re-sell, redistribute, or commercialize this dataset without explicit permission. 
  
  - I commit to citing HelpingAI appropriately in any work produced using this dataset.  
  
  - I will not use the dataset for creating harmful, discriminatory, or unethical content.

extra_gated_fields:
  First Name: text
  Last Name: text
  Email: text
  Affiliation: text
  Country: country
  Intended Use:
    type: select
    options:
      - Research
      - Model Development
      - Benchmarking
      - Teaching / Education
      - Other
  Project Description: text
  Agree to Access Terms: checkbox
  geo: ip_location

extra_gated_description: >-
  Access to **Intermediate-Thinking-130k** is gated to promote ethical use. The information you provide is used to ensure the dataset is used in line with HelpingAI’s values of empathy, openness, and responsibility.

extra_gated_button_content: Request Access

---

# Intermediate-Thinking-130k

A comprehensive dataset of 135,000 high-quality samples designed to advance language model reasoning capabilities through structured intermediate thinking processes. This dataset enables training and evaluation of models with sophisticated self-correction and iterative reasoning abilities across 42 languages.

## Overview

Intermediate-Thinking-130k addresses a fundamental limitation in current language models: their inability to pause, reflect, and refine reasoning during response generation. Traditional models produce responses in a single pass, often leading to incomplete or incorrect reasoning. This dataset provides examples of **Intermediate Thinking**—a cognitive approach that mirrors human reasoning processes through iterative refinement and self-correction.

### Key Innovations

- **Multi-Phase Reasoning**: Structured thinking blocks that demonstrate iterative problem-solving
- **Self-Correction Mechanisms**: Examples of error identification and mid-process refinement
- **Emotional Context Awareness**: Optional structured emotional reasoning (`<ser>`) blocks
- **Multilingual Support**: Coverage across 42 languages for global applicability
- **Human-Like Cognition**: Patterns that mirror natural human reasoning processes

## Dataset Structure

### Format

Each example follows a standardized JSON structure:

```json
{
  "instruction": "What is the direction of the gravitational force exerted by the Moon on an object at the Earth's equator?",
  "input": "",
  "output": "<think>\nThis is a physics question about gravitational forces. The Moon exerts a gravitational pull on objects on Earth. The direction of this force would be along the line connecting the object at the equator to the center of the Moon.\n</think>\n\nThe direction of the gravitational force is along the line connecting the object to the Moon.\n\n<think>\nWait, I should clarify that gravitational force follows Newton's law of universal gravitation. The direction is not static—it varies depending on the Moon's position relative to Earth.\n</think>\n\nSo, to be more precise, the gravitational force from the Moon on an object at the equator points directly toward the Moon's position in the sky at that time. As the Earth rotates and the Moon orbits, the direction of this force constantly shifts.\n\n<think>\nMaybe I should connect this to real-world effects like ocean tides.\n</think>\n\nThis changing gravitational pull is what drives ocean tides. When the Moon is overhead, the pull is upward; when it's on the horizon, the pull is nearly horizontal."
}
```

### Reasoning Architecture

The dataset implements a three-tier thinking framework:

#### 1. Initial Thinking (`<think>`)
- **Purpose**: First-pass problem analysis and approach formulation
- **Characteristics**: Basic understanding, initial strategy development
- **Frequency**: Present in every example

#### 2. Intermediate Thinking (`<think>`)
- **Purpose**: Self-correction and iterative refinement
- **Characteristics**: Error identification, approach adjustment, deeper exploration
- **Frequency**: Present in every example (1-17 blocks per example)

#### 3. End Thinking (`<think>`)
- **Purpose**: Final reflection for complex scenarios
- **Characteristics**: Human-like reasoning steps, comprehensive synthesis
- **Frequency**: Rare, only for complex challenges

### Emotional Context Awareness

Optional `<ser>` blocks encode contextual awareness:

```xml
<ser>
Emotion ==> curiosity
Cause ==> ambiguous mathematical structure
Mind ==> analytical but cautious
Growth ==> refining symbolic manipulation
</ser>
```

## Comparison with Traditional Approaches

### Chain-of-Thought (CoT) Limitations
- **Linear reasoning**: Single-pass thinking process
- **No self-correction**: Once generated, thoughts remain static
- **Limited perspective**: Single approach to problem-solving
- **No iteration**: No refinement or improvement cycles

### Intermediate Thinking Advantages
- **Iterative refinement**: Multiple thinking cycles with self-correction
- **Self-evaluation**: Recognition and correction of logical errors
- **Adaptive reasoning**: Dynamic approach adjustment based on insights
- **Multi-perspective synthesis**: Integration of multiple viewpoints
- **Human-like cognition**: Natural reasoning patterns

## Dataset Statistics

| Metric | Value |
|--------|-------|
| **Total Examples** | 135,000 |
| **Languages Supported** | 42 languages |
| **Thinking Blocks per Example** | 1-17 |
| **Topics Covered** | Mathematics, Physics, Logic, Philosophy, Ethics |
| **Format** | JSON (auto-converted to Parquet) |
| **License** | Apache 2.0 |

## Use Cases

### Primary Applications
- **Model Training**: Fine-tuning language models for intermediate reasoning
- **Performance Evaluation**: Benchmarking reasoning capabilities
- **Research Development**: Advancing AI reasoning methodologies
- **Educational Applications**: Teaching structured problem-solving

### Research Areas
- Cognitive modeling and reasoning in AI systems
- Emotional intelligence and context awareness
- Multi-step problem solving evaluation
- Self-reflective AI capabilities assessment

## Quick Start

### Installation
```bash
pip install datasets pandas
```

### Basic Usage
```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("HelpingAI/Intermediate-Thinking-130k", split="train")

# Explore a sample
print(dataset[0]["instruction"])
print(dataset[0]["output"])

# Stream for large datasets
dataset_stream = load_dataset("HelpingAI/Intermediate-Thinking-130k", split="train", streaming=True)
for row in dataset_stream:
    print(row["instruction"])
    break
```

### Working with Thinking Blocks
```python
import re

def extract_thinking_blocks(text):
    """Extract all <think> blocks from a response"""
    think_pattern = r'<think>(.*?)</think>'
    return re.findall(think_pattern, text, re.DOTALL)

# Example usage
sample = dataset[0]
thinking_blocks = extract_thinking_blocks(sample["output"])
print(f"Found {len(thinking_blocks)} thinking blocks")
```

## Data Collection Methodology

### Source and Processing
- **Origin**: Synthetic generation with human curation
- **Regeneration**: Quality improvement through synthetic regeneration
- **Quality Control**: Manual review of reasoning structure
- **Validation**: Heuristic parsing for structural integrity
- **Deduplication**: Elimination of near-identical pairs

### Processing Pipeline
1. **Synthetic Generation**: Creation of multi-step reasoning examples
2. **Regeneration**: Quality enhancement through iterative refinement
3. **Filtering**: Structural integrity and quality validation
4. **Annotation**: Emotional context where applicable
5. **Validation**: Random sample review for quality assurance

## Limitations and Considerations

### Current Limitations
- **Synthetic Nature**: Primarily generated content, not all pedagogically verified
- **Language Distribution**: Multilingual support with English-dominant distribution
- **Reasoning Variation**: Styles may vary across different examples

### Best Practices
- **Training Focus**: Use for model training rather than direct inference
- **Complementary Datasets**: Combine with domain-specific datasets
- **Diverse Evaluation**: Test across various reasoning tasks
- **Capability Testing**: Thoroughly evaluate self-correction abilities

## Contributing

We welcome contributions from the research community to advance intermediate reasoning capabilities.

### Contribution Areas

**Dataset Improvements**
- Report data quality issues or inconsistencies
- Suggest new reasoning patterns or problem types
- Contribute validated examples following established format
- Help expand language coverage and improve multilingual examples

**Research and Evaluation**
- Share evaluation results and benchmarks
- Contribute to reasoning capability assessments
- Develop new metrics for intermediate thinking
- Publish research using this dataset

**Documentation and Resources**
- Improve dataset documentation and examples
- Create tutorials or educational materials
- Develop tools for working with reasoning blocks
- Contribute to the broader reasoning research ecosystem


## Citation

If you use this dataset in your research, please cite:

```bibtex
@misc{intermediate-thinking-130k,
  title        = {Intermediate-Thinking-130k: A Dataset for Multi-Step Mathematical and Logical Reasoning},
  author       = {HelpingAI},
  year         = {2025},
  publisher    = {HelpingAI},
  howpublished = {\url{https://huggingface.co/datasets/HelpingAI/Intermediate-Thinking-130k}},
  license      = {Apache 2.0}
}
```

## Contact and Support

- **Issues**: [Hugging Face Issues](https://huggingface.co/datasets/HelpingAI/Intermediate-Thinking-130k/issues)
- **Discussions**: [Hugging Face Discussions](https://huggingface.co/datasets/HelpingAI/Intermediate-Thinking-130k/discussions)
- **Email**: [team@helpingai.co](mailto:team@helpingai.co)

---

*Intermediate-Thinking-130k represents a significant advancement in AI reasoning research, providing the foundation for developing language models with sophisticated intermediate thinking capabilities that move beyond traditional single-pass reasoning toward more human-like cognitive processes.*
