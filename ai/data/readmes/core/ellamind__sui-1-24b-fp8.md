---
license: apache-2.0
base_model:
- ellamind/sui-1-24b
tags:
- summarization
- long-context
- grounded-generation
- citation
- xml-tagging
language:
- en
- de
- es
- fr
- it
- pt
- nl
- pl
- zh
- ja
- ko
- ru
- ar
- tr
- vi
- id
- hi
- sv
- uk
- ro
- cs
- el
- hu
- th
pipeline_tag: text-generation
library_name: transformers
---

<div align="center">
  <img src="images/sui_icon.jpeg" alt="SUI Icon" width="200">
  <h3>sui-1</h3>
</div>

**sui-1** (Summarization with Unique Identifiers) is a specialized model for high-quality summarization of very long texts with built-in source grounding. Every claim in the summary can be traced back to its source sentence, enabling verification and reducing hallucination risk.

## Key Features

- **Very Long Document Processing**: Handles up to 128k tokens natively, with a two-step iterative approach for documents up to 2 million tokens
- **Single GPU Deployment**: The FP8 variant runs on a single A100 40GB or A6000 48GB GPU; the iterative approach enables deployment on even more modest hardware
- **Competitive Performance**: Significantly outperforms all tested open-weight baselines, including models with 3x more parameters
- **Multilingual Support**: Fine-tuned for English, German, Spanish, French, and Italian; inherits 20+ additional languages from Mistral Small 3.2
- **High-Quality Training Data**: Built using a sophisticated data generation pipeline that produced 22,000+ training examples from parliamentary documents, web sources, and Wikipedia using chain-of-thought reasoning with multi-stage verification
- **Verifiable Outputs**: Built-in citation mechanism links each claim to its source sentence for full traceability

## Quick Start

Run the end-to-end [example.py](example.py) script (requires [uv](https://docs.astral.sh/uv/)):

```bash
# Summarize a document
uv run example.py document.txt

# Or with inline text
uv run example.py --text "Your long text here..." --words 300 --tags 8
```

The script handles everything: sentence tagging, model inference, and formatted output with source citations.

## Evaluation

We evaluate sui-1-24b using an **LLM-as-a-Judge** methodology, where a strong judge model evaluates summary quality across multiple criteria. This approach captures nuanced quality aspects that traditional metrics like ROUGE cannot measure.

### Overall Performance

![Overall Performance](images/overall_performance.png)

The chart shows the overall success rate across all evaluation criteria. sui-1-24b significantly outperforms its base model (Mistral-Small-3.2-24B) on the summarization task.

### Performance by Criteria

We evaluate summaries on five key dimensions:

| Criterion | Description |
|-----------|-------------|
| **Factual Accuracy** | Does the summary avoid introducing new facts, entities, numbers, or claims not supported by the source content? |
| **Coverage & Completeness**¹ | Does the summary cover the document's main points and key takeaways at appropriate granularity? |
| **Specificity & Informativeness** | Are claims specific and informative rather than generic filler (e.g., "there are several points")? |
| **Format Compliance** | Is the output compliant with formatting instructions including language consistency, semantic-aware planning, and paragraph structure? |
| **Custom Instruction**² | If a custom instruction is provided, is it followed appropriately? |

![Criteria Breakdown](images/criteria_breakdown.png)

The evaluation was conducted on 100 diverse test samples covering multiple languages (English, German, Spanish, French, Italian) and document types. Scoring uses binary pass/fail per criterion, aggregated to success rates.

*¹ Coverage scores are lower when samples require constrained formats (bullet points, short summaries) that inherently limit content coverage.*
*² Tests whether the model deviates from its default prose style when users request specific formats.*

### Grounding Metrics

In addition to LLM-as-a-Judge evaluation, we validate grounding quality using structural checks:

1. **Tag Uniqueness**: All referenced tags in `xml_tags` must be unique
2. **Tag Validity**: All referenced tags must exist in the input text
3. **Tag Usage**: All tags in `xml_tags` must appear in the summary

### Elluminate

The evaluation was performed using [Elluminate](https://elluminate.de), a collaborative evaluation platform for enterprise AI. Elluminate provides structured LLM-as-a-Judge workflows that enable teams to standardize quality metrics and systematically measure AI performance across defined criteria.

This model is a contribution by [ellamind](https://ellamind.ai) to the open-source community.

---

## Model Weights

We provide two variants:

| Variant | Description | Link |
|---------|-------------|------|
| **bfloat16** | Full precision (~48GB weights) | [ellamind/sui-1-24b](https://huggingface.co/ellamind/sui-1-24b) |
| **FP8** | Quantized (~24GB weights), lower VRAM | [ellamind/sui-1-24b-fp8](https://huggingface.co/ellamind/sui-1-24b-fp8) |

The FP8 version preserves high quality, scoring 81.05% overall on our benchmark—nearly identical to bfloat16.

---

## Hardware Requirements

We tested various GPU configurations using vLLM. The tables below show minimum requirements for different context lengths.

The bfloat16 variant requires **~55GB VRAM** for 8k context, scaling to **~76GB** for 128k. The FP8 variant requires **~38GB** for 8k and **~50GB** for 128k.

### bfloat16 (Full Precision)

| Setup | 8k | 32k | 64k | 128k |
|-------|:--:|:---:|:---:|:----:|
| 1× A100 80GB / H100 96GB| ✓ | ✓ | ✓ | ✓ |
| 2× RTX 5090 (32GB) | ✓ | ✓ | ✗ | ✗ |
| 2× A100 40GB / A6000 | ✓ | ✓ | ✓ | ✓ |
| 4× RTX 4090 (24GB) | ✓ | ✓ | ✓ | ✓ |

### FP8 Quantized (Recommended for Consumer GPUs)

| Setup | 8k | 32k | 64k | 128k |
|-------|:--:|:---:|:---:|:----:|
| 1× A100 40GB | ✓ | ✓ | ✗ | ✗ |
| 1× A6000 (48GB) | ✓ | ✓ | ✓ | ✗ |
| 1× A100 80GB / H100 96GB| ✓ | ✓ | ✓ | ✓ |
| 2× RTX 4090 (24GB) | ✓ | ✓ | ✓ | ✗ |
| 2× RTX 5090 (32GB) | ✓ | ✓ | ✓ | ✓ |
| 4× RTX 4090 (24GB) | ✓ | ✓ | ✓ | ✓ |

> **Tip**: The model supports both one-shot summarization (full document in context) and an iterative two-step approach for very long documents (see [Handling Very Long Contexts](#handling-very-long-contexts)). The 8k context configuration is sufficient to produce high-quality summaries using the iterative approach, making the model accessible on more modest hardware.

---

## How It Works

The model follows a three-phase approach:

1. **Planning Phase**: Analyzes the input and plans the summary structure
2. **Reference Selection**: Identifies the most important sentences to cite
3. **Grounded Generation**: Produces a summary with inline citations to source sentences

Citations use XML tags assigned during preprocessing, enabling deterministic verification of each claim.

---

## Input Format

The input text must be preprocessed with XML sentence tags. Each sentence is wrapped in a unique 8-character hexadecimal tag:

```
<a1b2c3d4>First sentence of the document.</a1b2c3d4><e5f6g7h8>Second sentence continues here.</e5f6g7h8>...
```

### Tag Format Requirements

- Tags must be **8 lowercase hexadecimal characters** (e.g., `a1b2c3d4`)
- Each tag must be **unique** within the document
- Tags wrap individual sentences: `<tag>sentence text</tag>`
- Tags should be contiguous (no whitespace between closing and opening tags)

### Preprocessing with spaCy (Recommended)

```python
import hashlib
import spacy

def generate_tag(index: int, sentence: str) -> str:
    """Generate unique 8-char hex tag from sentence."""
    return hashlib.md5(f"{index}_{sentence[:50]}".encode()).hexdigest()[:8]

def tag_text(text: str, language: str = "en") -> tuple[str, dict]:
    """
    Tag text with XML sentence markers.

    Args:
        text: Input text to tag
        language: Language code (en, de, es, fr, it)

    Returns:
        tuple: (tagged_text, tag_to_sentence_mapping)
    """
    # Load appropriate spaCy model
    models = {"en": "en_core_web_sm", "de": "de_core_news_sm",
              "es": "es_core_news_sm", "fr": "fr_core_news_sm", "it": "it_core_news_sm"}
    nlp = spacy.load(models.get(language, "en_core_web_sm"))

    doc = nlp(text)
    tagged_text = ""
    tag_mapping = {}

    for i, sent in enumerate(doc.sents):
        sentence = sent.text.strip()
        if sentence:
            tag = generate_tag(i, sentence)
            tag_mapping[tag] = sentence
            tagged_text += f"<{tag}>{sentence}</{tag}>"

    return tagged_text, tag_mapping

# Example usage
text = "This is the first sentence. Here is the second one. And a third."
tagged, mapping = tag_text(text)
print(tagged)
# Output: <a1b2c3d4>This is the first sentence.</a1b2c3d4><e5f67890>Here is the second one.</e5f67890>...
```

### Installation for Preprocessing

```bash
pip install spacy langdetect
python -m spacy download en_core_web_sm  # English
python -m spacy download de_core_news_sm  # German (optional)
```

To automatically detect the input language and select the appropriate spaCy model, you can use `langdetect`:

```python
from langdetect import detect

def detect_language(text: str) -> str:
    lang_code = detect(text[:1000])  # Sample first 1000 chars
    lang_map = {"de": "German", "en": "English", "es": "Spanish",
                "fr": "French", "it": "Italian"}
    return lang_map.get(lang_code, "English")  # Default to English
```

For non-enhanced languages, English-style sentence segmentation is used as fallback, which may be suboptimal for languages with different punctuation conventions (e.g., Chinese, Japanese).

---

## Output Format

The model outputs a JSON object with three keys:

```json
{
  "structure": "Planning text describing how the summary will be organized...",
  "xml_tags": ["<a1b2c3d4>", "<e5f67890>", "<12345678>"],
  "summary": "The document discusses... [<a1b2c3d4>]. Furthermore... [<e5f67890>]."
}
```

### Output Keys

| Key | Type | Description |
|-----|------|-------------|
| `structure` | string | Internal reasoning about the content and planned summary structure. Shows which topics will be covered and in what order. |
| `xml_tags` | array | List of XML tags that will be cited in the summary. Each tag corresponds to a source sentence. Tags are listed in the order they appear in the source. |
| `summary` | string | The actual summary with inline XML tag references in square brackets (e.g., `[<a1b2c3d4>]`). Each referenced tag must appear in the `xml_tags` list and exist in the input. |

### Reference Format in Summary

Citations appear inline immediately after the statement they support:

```
The report found significant budget overruns [<a1b2c3d4>]. This was attributed to
supply chain disruptions [<e5f67890>] and labor shortages [<12345678>].
```

<details>
<summary><b>Example Output (click to expand)</b></summary>

```json
{
  "structure": "This government report examines infrastructure spending over the past fiscal year. I will structure the summary as follows: 1) Executive overview with key findings, 2) Budget analysis section covering the main expenditures, 3) Regional breakdown of infrastructure projects, 4) Recommendations from the oversight committee. I will select 8 XML tags distributed across these sections to provide comprehensive source grounding.",
  "xml_tags": [
    "<9f2a1b3c>",
    "<d4e5f678>",
    "<90ab12cd>",
    "<ef345678>",
    "<9abc0def>",
    "<12345678>",
    "<abcdef90>",
    "<78901234>"
  ],
  "summary": "The Congressional Budget Office's annual infrastructure report reveals that federal infrastructure spending reached $284 billion in fiscal year 2024, representing a 12% increase from the previous year [<9f2a1b3c>]. The majority of funds were allocated to transportation projects, with highway maintenance and bridge repair accounting for 45% of total expenditures [<d4e5f678>].\n\nThe report identifies significant regional disparities in infrastructure investment. Northeastern states received disproportionately higher funding due to aging infrastructure requiring immediate attention [<90ab12cd>], while southern and western regions saw increased allocations for new construction projects [<ef345678>]. Rural communities continued to face challenges in securing adequate funding for basic infrastructure needs [<9abc0def>].\n\nThe oversight committee raised concerns about cost overruns in several major projects, with the average project exceeding initial estimates by 23% [<12345678>]. The committee recommends implementing stricter oversight mechanisms and requiring more detailed feasibility studies before project approval [<abcdef90>]. Additionally, the report suggests exploring public-private partnerships as a means to supplement federal funding and improve project efficiency [<78901234>]."
}
```

</details>

---

## Handling Very Long Contexts

The model supports a 128k token context window natively. For longer documents (tested up to 2 million tokens), use the iterative approach.

### Approach 1: Oneshot (Up to 128k tokens)

For documents within the context limit, use the standard prompt with `PROMPT_SUMMARY`:

```python
prompt = f"""You are a professional summarizer, following all given instructions with the utmost care.

<text>
{tagged_text}
</text>

# Output Format
The output must be in JSON format with the following structure:
1. A "structure" string containing your thoughts about the content and structure of the summary
2. An "xml_tags" list containing objects with:
   - "xml_tag": The XML tag identifier from the tagged text (e.g., "<a1b2c3d4>")
3. A "summary" string containing the actual summary with inline XML tag references

# Instructions
...

Parameters:
- Word count (excl. XML tags): {word_count}
- Number of XML tags: {number_of_xml_tags}
- Language: {language}
"""
```

**Output:** JSON with `structure`, `xml_tags`, and `summary`

---

### Approach 2: Iterative (128k+ tokens)

For documents exceeding the context limit, use a two-step iterative approach that preserves grounding quality:

#### Step 1: Partial Summaries (`PROMPT_SUMMARY_PARTIAL`)

Split the document into chunks and summarize each independently:

```python
prompt_partial = f"""You are a professional summarizer, following all given instructions with the utmost care.

This is a section of a larger document. Create a partial summary that will later be combined with other sections.

<text>
{chunk_tagged_text}
</text>

# Output Format
The output must be in JSON format with the following structure:
1. A "structure" string containing your thoughts about the content and structure of the summary
2. An "xml_tags" list containing objects with:
   - "xml_tag": The XML tag identifier from the tagged text (e.g., "<a1b2c3d4>")
3. A "summary" string containing the actual summary with inline XML tag references

# Instructions
1. Select {number_of_xml_tags} XML tags that capture the most significant data and facts.
2. Begin with a brief introduction of the section's main topics (no executive summary for partial summaries).
3. Structure the summary in coherent paragraphs with at least one XML tag reference each.
4. The summary should be 300-600 words long (without the XML tags).
5. Only include title/author if explicitly mentioned in this section.
...
"""
```

**Output per chunk:** JSON with `structure`, `xml_tags`, and `summary` (300-600 words each)

#### Step 2: Final Merge (`PROMPT_SUMMARY_PARTIAL_LAST`)

Combine all partial summaries into a coherent final summary:

```python
# Concatenate all partial summary outputs
partial_summaries_text = "\n\n".join([
    f"--- Section {i+1} ---\n{partial_output}"
    for i, partial_output in enumerate(partial_outputs)
])

prompt_final = f"""You are a professional summarizer, following all given instructions with the utmost care.

You are given partial summaries from a larger document. Combine them into a coherent final summary.

<partial_summaries>
{partial_summaries_text}
</partial_summaries>

# Output Format
The output must be in JSON format with the following structure:
1. A "structure" string containing your thoughts about the content and structure of the summary
2. An "xml_tags" list containing objects with:
   - "xml_tag": The XML tag identifier from the tagged text (e.g., "<a1b2c3d4>")
3. A "summary" string containing the actual summary with inline XML tag references

# Instructions
1. Select the {number_of_xml_tags} most significant XML tags from the partial summaries.
   Copy the XML tags verbatim, ensuring they represent key points from different sections.
2. Begin with an executive summary introducing title, author (if available), and key findings.
3. Structure the summary in coherent paragraphs following a coherent thread.
4. Each XML tag must appear exactly once. Use only XML tags from the partial summaries.
5. Don't repeat content that is very similar or identical in multiple partial summaries.
...
"""
```

**Final Output:** JSON with `structure`, `xml_tags`, and `summary`

#### How Grounding Quality is Maintained

The iterative approach preserves source grounding through careful XML tag propagation:

1. **Tag Extraction**: Each partial summary extracts XML tags from its chunk, linking claims to source sentences
2. **Tag Preservation**: The final merge prompt explicitly instructs to "copy XML tags verbatim" from partials
3. **No Hallucinated Tags**: The final summary can only reference tags that were already validated in partial summaries
4. **Distributed Coverage**: By selecting tags "from different sections," the final summary maintains broad source coverage

This ensures that even for 2M+ token documents, every claim in the final summary traces back to a specific source sentence.

### Recommended Parameters

| Summary Length | Word Count | XML Tags |
|---------------|------------|----------|
| Short | ~100 words | 3 tags |
| Medium | ~250 words | 6 tags |
| Long | ~500 words | 12 tags |

---

## Usage

For production use, we provide ready-to-use prompt templates in [`prompts.py`](prompts.py). This file contains:

- `PROMPT_SUMMARY`: Standard single-pass summarization prompt
- `PROMPT_SUMMARY_PARTIAL`: Prompt for creating partial summaries of document chunks
- `PROMPT_SUMMARY_PARTIAL_LAST`: Prompt for merging partial summaries into a final summary

**Resource-constrained environments:** The iterative two-step approach is not only useful for very long documents—it also enables deployment on hardware with limited VRAM. The model was trained on a broad range of chunk sizes, so partial summaries work reliably even with smaller context windows (e.g., 5k token chunks). This flexibility allows you to adjust chunk sizes to match your available GPU memory.

### With vLLM (Recommended for Production)

```python
from vllm import LLM, SamplingParams

# Load model
llm = LLM(
    model="ellamind/sui-1-24b-fp8",
    tensor_parallel_size=4,  # Adjust based on available GPUs
    dtype="bfloat16",
    tokenizer_mode="mistral",
    max_model_len=128000,
    trust_remote_code=True,
)

# Prepare prompt
prompt = f"""You are a professional summarizer, following all given instructions with the utmost care.

<text>
{tagged_text}
</text>

# Output Format
The output must be in JSON format with the following structure:
1. A "structure" string containing your thoughts about the content and structure of the summary
2. An "xml_tags" list containing the XML tag identifiers from the tagged text (e.g., "<a1b2c3d4>")
3. A "summary" string containing the actual summary with inline XML tag references

# Instructions
1. Start by thinking about and explaining the structure and content of your summary. Select {num_tags} XML tags from the tagged text that capture the most significant data and facts.
2. Begin with an executive summary introducing the title, author (if available), and key findings.
3. Structure the summary in coherent paragraphs. Every paragraph should contain at least one XML tag reference.
4. Reference XML tags inline in square brackets (e.g., [<a1b2c3d4>]) immediately after the statement they support.
5. Each XML tag must appear exactly once in the summary.
6. Avoid a concluding paragraph that merely restates points.
7. Do not use bullet points or headings unless explicitly requested.

# Custom Instruction
{custom_instruction}

Parameters:
- Word count (excl. XML tags): {word_count}
- Number of XML tags: {num_tags}
- Language: {language}
"""

# Generate
sampling_params = SamplingParams(max_tokens=8192, temperature=0.0)
outputs = llm.chat([[{"role": "user", "content": prompt}]], sampling_params)
result = outputs[0].outputs[0].text
```

### With Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "ellamind/sui-1-24b",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("ellamind/sui-1-24b")

messages = [{"role": "user", "content": prompt}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
outputs = model.generate(inputs, max_new_tokens=8192, temperature=0.0, do_sample=False)
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

---

## Language Support

### Enhanced Languages (Fine-tuned)

The model was fine-tuned with training data in these languages, providing optimal summarization quality:

| Language | Code | Tagging Support |
|----------|------|-----------------|
| English | `en` | `en_core_web_sm` |
| German | `de` | `de_core_news_sm` |
| Spanish | `es` | `es_core_news_sm` |
| French | `fr` | `fr_core_news_sm` |
| Italian | `it` | `it_core_news_sm` |

### Inherited Languages (Base Model)

The following languages are supported through the Mistral Small 3.2 base model. Summarization works but may have reduced quality compared to enhanced languages:

| Category | Languages |
|----------|-----------|
| European | Portuguese, Dutch, Polish, Russian, Swedish, Ukrainian, Romanian, Czech, Greek, Hungarian |
| Asian | Chinese, Japanese, Korean, Vietnamese, Indonesian, Thai, Hindi |
| Middle Eastern | Arabic, Turkish, Persian |

---

## Limitations

- Requires preprocessing of input text with XML tags
- Maximum single-pass context of 128k tokens
- JSON output parsing may occasionally fail; implement retry logic for production use

---

## Citation

```bibtex
@article{droste2025sui1,
  title={sui-1: Grounded and Verifiable Long-Form Summarization},
  author={Droste, Benedikt and Harries, Jan Philipp and Idahl, Maximilian and Pl{\"u}ster, Bj{\"o}rn},
  journal={arXiv preprint arXiv:2601.08472},
  year={2025}
}
```

---

## License

This model is released under the Apache 2.0 license, consistent with the base Mistral model.