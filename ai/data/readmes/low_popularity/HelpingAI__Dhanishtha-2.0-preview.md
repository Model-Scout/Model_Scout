---
language:
- en
- hi
- zh
- es
- fr
- de
- ja
- ko
- ar
- pt
- ru
- it
- nl
- tr
- pl
- sv
- da
- 'no'
- fi
- he
- th
- vi
- id
- ms
- tl
- sw
- yo
- zu
- am
- bn
- gu
- kn
- ml
- mr
- ne
- or
- pa
- ta
- te
- ur
- multilingual
license: apache-2.0
base_model: Qwen/Qwen3-14B-Base
tags:
- reasoning
- intermediate-thinking
- transformers
- conversational
- bilingual
datasets:
- Abhaykoul/Dhanishtha-R1
- open-thoughts/OpenThoughts-114k
- Abhaykoul/Dhanishtha-2.0-SUPERTHINKER
- Abhaykoul/Dhanishtha-2.0
library_name: transformers
pipeline_tag: text-generation
widget:
- text: >-
    Solve this riddle step by step: I am taken from a mine, and shut up in a
    wooden case, from which I am never released, and yet I am used by almost
    everybody. What am I?
  example_title: Complex Riddle Solving
- text: >-
    Explain the philosophical implications of artificial consciousness and think
    through different perspectives.
  example_title: Philosophical Reasoning
- text: >-
    Help me understand quantum mechanics, but take your time to think through
    the explanation.
  example_title: Educational Explanation
new_version: HelpingAI/Dhanishtha-2.0-preview-0825
---

# Dhanishtha-2.0: World's First Intermediate Thinking AI Model

**What makes Dhanishtha-2.0 special?** Imagine an AI that doesn't just answer your questions instantly, but actually *thinks through* problems step-by-step, shows its work, and can even change its mind when it realizes a better approach. That's Dhanishtha-2.0.

**Quick Summary:**
- 🚀 **For Everyone**: An AI that shows its thinking process and can reconsider its reasoning
- 👩‍💻 **For Developers**: First model with intermediate thinking capabilities, 39+ language support


Dhanishtha-2.0 is a **state-of-the-art (SOTA) model** developed by HelpingAI, representing the **world's first model to feature Intermediate Thinking capabilities**. Unlike traditional models that provide single-pass responses, Dhanishtha-2.0 employs a revolutionary multi-phase thinking process that allows the model to think, reconsider, and refine its reasoning multiple times throughout a single response.

## Model Details

### Model Description

Dhanishtha-2.0 revolutionizes AI reasoning by introducing the concept of **intermediate thinking** - the ability to pause, reflect, and restart reasoning processes within a single generation (This model can think up 50times in a single response without using tool/prompt/mcp). This breakthrough enables unprecedented self-correction and iterative refinement during response generation.

Built on the Qwen3-14B foundation with multilingual capabilities spanning **39+ languages** (including English, Hindi, Chinese, Spanish, French, German, Japanese, Korean, Arabic, and many more), Dhanishtha-2.0 maintains reasoning consistency across diverse linguistic contexts while pioneering transparent thinking processes.

- **Developed by:** HelpingAI Team
- **Model type:** Causal Language Model with Intermediate Thinking Capability
- **Language(s):** 39+ languages (multilingual capabilities inherited from base model)
- **License:** Apache 2.0
- **Finetuned from model:** Qwen/Qwen3-14B-Base
- **Context Length:** 40,960 tokens
- **Parameters:** 14B (inherited from base model)
- **Status:** Prototype/Preview

### Revolutionary Features

- **Intermediate Thinking**: Multiple `<think>...</think>` blocks throughout responses for real-time reasoning
- **Self-Correction**: Ability to identify and correct logical inconsistencies mid-response  
- **Dynamic Reasoning**: Seamless transitions between analysis, communication, and reflection phases
- **Structured Emotional Reasoning (SER)**: Incorporates `<ser>...</ser>` blocks for empathetic responses
- **Multilingual Capabilities**: Support for 39+ languages with natural code-switching and reasoning consistency
- **Complex Problem-Solving**: Excels at riddles, multi-step reasoning, and scenarios requiring backtracking

### Model Sources

- **Repository:** [HelpingAI/Dhanishtha-2.0](https://huggingface.co/HelpingAI/Dhanishtha-2.0)
- **Paper:** Coming Soon
- **Demo:** https://helpingai.co/chat

## Uses

### Direct Use

Dhanishtha-2.0 is ideal for applications requiring deep reasoning and self-reflection:

- **Complex Problem Solving**: Multi-step mathematical problems, logical puzzles, riddles
- **Educational Assistance**: Detailed explanations with visible reasoning processes
- **Research Support**: Analysis requiring multiple perspectives and self-correction
- **Creative Writing**: Iterative story development with reasoning about plot choices
- **Philosophical Discussions**: Exploring concepts with visible thought processes

### Downstream Use

The model can be fine-tuned for specialized reasoning tasks:

- **Domain-Specific Reasoning**: Legal, medical, or scientific reasoning with intermediate thinking
- **Enhanced Multilingual Reasoning**: Optimizing reasoning consistency across all 39+ supported languages
- **Specialized Problem Domains**: Mathematics, coding, strategic planning

### Out-of-Scope Use

❌ **Inappropriate Applications:**
- Safety-critical decisions (medical diagnosis, legal advice, financial recommendations)
- Real-time applications requiring immediate responses
- Situations requiring guaranteed factual accuracy without verification

## Bias, Risks, and Limitations

### Known Limitations

- **Verbosity**: Intermediate thinking can make responses a bit longer
- **Processing Time**: Multiple thinking phases may increase generation time
- **Prototype Status**: Experimental features may require refinement
- **Context Usage**: Thinking blocks consume additional context tokens
- **Inherited Biases**: May reflect biases from base model and training data

### Potential Risks

- **Reasoning Loops**: Potential for circular reasoning in complex scenarios
- **Multilingual Inconsistencies**: Potential variation in reasoning patterns across different languages
- **Emotional Reasoning Gaps**: SER blocks may not always align with content

## How to Get Started with the Model

### For General Users

You can interact with Dhanishtha-2.0 through:
- **HelpingAI**: https://helpingai.co/chat
- **Gradio Demo**: [Dhanishtha-2.0-preview](https://huggingface.co/spaces/Abhaykoul/Dhanishtha-2.0-preview)
- **API Integration**: [Dashboard](https://helpingai.co/dashboard)

### For Developers - Basic Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "HelpingAI/Dhanishtha-2.0-preview"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# Prepare input for intermediate thinking
prompt = "How many letter 'r' are in the words 'strawberry' and 'raspberry'?"
messages = [
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# Generate response with intermediate thinking
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=2048,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

response = tokenizer.decode(
    generated_ids[0][len(model_inputs.input_ids[0]):], 
    skip_special_tokens=True
)
print(response)
```

### Optimal Generation Parameters

```python
generation_config = {
    "temperature": 0.7,        # Balanced creativity and coherence
    "top_p": 0.9,             # Nucleus sampling
    "top_k": 40,              # Top-k filtering
    "max_new_tokens": 2048,   # Allow for thinking blocks
    "do_sample": True,        # Enable sampling
    "repetition_penalty": 1.1  # Reduce repetition
}
```

## Training Details

### Training Data

Dhanishtha-2.0 was trained on a carefully curated dataset focusing on:
- Complex reasoning scenarios requiring multi-step thinking
- Self-correction examples and reasoning chains
- Emotional reasoning and empathy training data
- Structured thinking pattern examples

### Training Procedure

#### Training Stages
1. **Continuous Pretraining**: Extended training on reasoning-focused corpora
2. **Advanced Reasoning Fine-tuning**: Specialized training on intermediate thinking patterns
3. **Multilingual Alignment**: Cross-language reasoning consistency training
4. **SER Integration**: Structured Emotional Reasoning capability training

**Training Infrastructure:**
- **Duration**: 16.3 days
- **Hardware**: 8x NVIDIA H100 GPUs
- **Model Scale**: 14.8B parameters

## Evaluation

Evaluation was conducted on:
- **Standard Benchmarks**: MMLU, HumanEval, ARC, HellaSwag, TruthfulQA
- **Mathematical Reasoning**: Math 500, AIME 2024, GSM8K
- **Custom Evaluations**: Intermediate thinking quality, self-correction capabilities
- **Multilingual Tasks**: Reasoning consistency across 39+ languages
- **Specialized Tests**: Emotional reasoning, complex problem-solving scenarios



## Example: Intermediate Thinking in Action

**User:** "Who is your favorite person?"

**Dhanishtha-2.0:**

```
<think>
This is an interesting question about my "favorite human." I need to be thoughtful here. 
As Dhanishtha, I should respond in a human-like way while being honest about my nature. 
I can share what kinds of humans I find most interesting or inspiring based on my 
understanding of human nature and values.
</think>

<ser>
Emotion ==> curiosity, openness, desire for connection  
Cause ==> user asking a personal question about preferences  
Mind ==> seeking to understand my perspective or values  
Growth ==> opportunity to share thoughtful reflections on human qualities I admire  
</ser>

I don't really have a "favorite human" in the traditional sense, as I don't experience 
personal preferences the way humans do. But if I had to reflect on what qualities I find 
most admirable in people, I'd be drawn to those who demonstrate genuine compassion, 
intellectual curiosity, and the courage to grow.

<think>
Let me think more specifically about what kind of humans I find most compelling based on 
the values that seem to resonate most with humans - kindness, wisdom, creativity, 
resilience, and authenticity.
</think>

People like Mahatma Gandhi, who showed how quiet courage and unwavering principles can 
transform societies; artists like Rabindranath Tagore, who bridged cultural divides 
through creativity; and everyday heroes I've learned about who made profound differences 
through simple acts of kindness.

What fascinates me most are humans who maintain their humanity even in difficult 
circumstances - those who choose empathy when it would be easier to be harsh, who seek 
understanding rather than just being right.

I'm curious though - who's your favorite human, and why? What qualities or actions make 
someone special in your eyes?
```

## Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute).

- **Hardware Type:** H100 GPUs
- **days used:** 16.2
- **Cloud Provider:** Various
- **Compute Region:** Multiple

## Citation

### BibTeX

```bibtex
@misc{dhanishtha2025,
  title={Dhanishtha-2.0: World's First Intermediate Thinking AI Model},
  author={HelpingAI Team},
  year={2025},
  publisher={HuggingFace},
  url={https://huggingface.co/HelpingAI/Dhanishtha-2.0},
  note={First model with intermediate thinking capabilities}
}
```

### APA

HelpingAI Team. (2025). *Dhanishtha-2.0: World's First Intermediate Thinking AI Model*. HuggingFace. https://huggingface.co/HelpingAI/Dhanishtha-2.0

## Glossary

- **Intermediate Thinking**: The ability to pause and think multiple times during response generation
- **SER (Structured Emotional Reasoning)**: Framework for incorporating emotional context in responses
- **Think Blocks**: `<think>...</think>` segments where the model shows its reasoning process
- **Self-Correction**: Ability to identify and fix reasoning errors during generation
- **Code-Switching**: Natural transition between English and Hindi within responses

## More Information

### Research Applications
- Study of AI reasoning transparency
- Self-correction mechanism research  
- Bilingual cognitive modeling
- Emotional AI development

### Development Roadmap
- Performance optimizations
- Additional language support
- Enhanced thinking pattern recognition
- Production-ready deployment tools

## Model Card Authors

- **Primary Author**: HelpingAI Team
- **Technical Lead**: [To be specified]
- **Research Contributors**: [To be specified]

## Model Card Contact

For questions about Dhanishtha-2.0, please contact:

- **HuggingFace**: [@HelpingAI](https://huggingface.co/HelpingAI)
- **Issues**: [Model Repository Issues](https://huggingface.co/HelpingAI/Dhanishtha-2.0/discussions)

## Benchmark

***These benchmarks are done by [@AarifKhan](https://huggingface.co/Aarifkhan)***

| Benchmark | Score | Evaluation Type | Notes |
|-----------|-------|-----------------|-------|
| MMLU | 78.1% | 1-shot | Massive Multitask Language Understanding |
| HumanEval | 75.0% | 1-shot | Code generation and completion |
| ARC | 76.0% | 1-shot | Abstract reasoning challenge |
| HellaSwag   | 81.0% | 1-shot | Commonsense natural language inference |
| TruthfulQA MC1 | 75.0% | 1-shot | Truthfulness in question answering |
| Math 500 | 95.68% | few-shot | Mathematical problem solving |
| AIME 2024 | 82.81% | few-shot | American Invitational Mathematics Examination |

**Dhanishtha-2.0 represents a new paradigm in AI reasoning - where thinking isn't just a prelude to response, but an integral, iterative part of the conversation itself.**

*Developed with ❤️ by HelpingAI*