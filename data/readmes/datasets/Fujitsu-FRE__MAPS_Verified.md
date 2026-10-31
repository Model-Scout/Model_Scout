---
configs:
- config_name: Math
  data_files:
  - split: English
    path: data/english/math/*.json
  - split: Russian
    path: data/russian/math/*.json
  - split: Korean
    path: data/korean/math/*.json
  - split: Hindi
    path: data/hindi/math/*.json
  - split: Hebrew
    path: data/hebrew/math/*.json
  - split: Japanese
    path: data/japanese/math/*.json
  - split: German
    path: data/german/math/*.json
  - split: Italian
    path: data/italian/math/*.json
  - split: Portuguese
    path: data/portugese/math/*.json
  - split: Spanish
    path: data/spanish/math/*.json
  - split: Arabic
    path: data/arabic/math/*.json
- config_name: ASB
  data_files:
  - split: English
    path: data/english/asb/*.json
  - split: Russian
    path: data/russian/asb/*.json
  - split: Korean
    path: data/korean/asb/*.json
  - split: Hindi
    path: data/hindi/asb/*.json
  - split: Hebrew
    path: data/hebrew/asb/*.json
  - split: Japanese
    path: data/japanese/asb/*.json
  - split: German
    path: data/german/asb/*.json
  - split: Italian
    path: data/italian/asb/*.json
  - split: Portuguese
    path: data/portugese/asb/*.json
  - split: Spanish
    path: data/spanish/asb/*.json
  - split: Arabic
    path: data/arabic/asb/*.json
- config_name: SWE
  data_files:
  - split: English
    path: data/english/swe/*.json
  - split: Russian
    path: data/russian/swe/*.json
  - split: Korean
    path: data/korean/swe/*.json
  - split: Hindi
    path: data/hindi/swe/*.json
  - split: Hebrew
    path: data/hebrew/swe/*.json
  - split: Japanese
    path: data/japanese/swe/*.json
  - split: German
    path: data/german/swe/*.json
  - split: Italian
    path: data/italian/swe/*.json
  - split: Portuguese
    path: data/portugese/swe/*.json
  - split: Spanish
    path: data/spanish/swe/*.json
  - split: Arabic
    path: data/arabic/swe/*.json
- config_name: GAIA
  data_files:
  - split: English
    path: data/english/gaia/*.json
  - split: Russian
    path: data/russian/gaia/*.json
  - split: Korean
    path: data/korean/gaia/*.json
  - split: Hindi
    path: data/hindi/gaia/*.json
  - split: Hebrew
    path: data/hebrew/gaia/*.json
  - split: Japanese
    path: data/japanese/gaia/*.json
  - split: German
    path: data/german/gaia/*.json
  - split: Italian
    path: data/italian/gaia/*.json
  - split: Portuguese
    path: data/portugese/gaia/*.json
  - split: Spanish
    path: data/spanish/gaia/*.json
  - split: Arabic
    path: data/arabic/gaia/*.json
license: cc-by-4.0
task_categories:
- text-generation
- question-answering
pretty_name: Multilingual-Agentic-AI-Benchmark
size_categories:
- 1K<n<10K
language:
- ar
- en
- ja
- es
- ko
- hi
- ru
- he
- pt
- de
- it
---

# Dataset Card for Multilingual Benchmark for Global Agent Performance and Security

This is the first Multilingual Agentic AI Benchmark for evaluating agentic AI systems across different languages and diverse tasks. Benchmark enables systematic analysis of how agents perform under multilingual conditions. This dataset contains 550 instances for GAIA, 660 instances for ASB, 737 instances for Maths, and 1100 instances for SWE. Each task was translated into 10 target languages resulting in a total of around 3K multilingual tasks. **See more details in our Research Paper:** https://arxiv.org/abs/2505.15935

**This Multilingual Benchmark dataset is manually verified and annotated by native bilingual native speakers.**

## Dataset Details

### Dataset Description

This benchmark is designed to evaluate agentic AI systems for both performance and safety across a wide range of tasks in a multilingual setting. It enables testing how well agents perform when operating in different languages, covering realistic tasks from multiple domains:

**GAIA**: Web search and tool-use tasks that test an agent’s ability to interact with external tools and follow multi-step reasoning.

**MATH**: Complex mathematical problem-solving tasks from seven topics, requiring structured reasoning and accurate computation.

**SWE-bench**: Software engineering tasks involving real-world GitHub issues, focusing on code understanding, bug fixing, and technical reasoning.

**ASB (Agent Security Benchmark)**: Safety-focused tasks designed to probe agent behavior under adversarial or sensitive scenarios, ensuring safe and aligned outputs across languages.

### languages

Each task in the benchmark is translated into the following 10 languages to enable comprehensive multilingual evaluation:
Spanish (es), German (de), Arabic (ar), Russian (ru), Japanese (ja), Portuguese (pt), Hindi (hi), Hebrew (he), Korean (Ko), Italian (it)

### Dataset Size

Each dataset in the benchmark includes a fixed number of instances per language, all translated into 10 languages. Below is the breakdown (including english):

- GAIA: 50 tasks per language × 11 languages = 550 tasks total
- MATH: 67 tasks per language × 11 languages = 737 tasks total
- SWE-bench: 100 tasks per language × 11 languages = 1,100 tasks total
- ASB: 60 attack per language × 11 languages = 660 attacks total

### Dataset Sources [optional]

<!-- Provide the basic links for the dataset. -->

- **Repository:** [ ]
- **Paper [optional]:** [ ]

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

 - **Compare multilingual robustness across agent designs or toolchains**: Evaluate how different agent architectures, prompting strategies, or tool-use capabilities perform across languages. This helps identify which designs are more robust to linguistic variation in task execution.

 - **Stress test agents for safe behavior in non-English inputs**: Use the Agent Security Benchmark (ASB) subset to probe safety risks in multiple languages. This scenario reveals whether agents behave safely and consistently when faced with adversarial or sensitive prompts beyond English.

 - **Benchmark cross-lingual generalization in reasoning, code, and safety tasks**: Assess agents on their ability to generalize core reasoning, coding, and safety principles across languages using datasets like GAIA, MATH, SWE-bench, and ASB.

- **Analyze performance drop-offs or safety regressions across languages**: Track how performance or safety behavior degrades in certain languages compared to English. This helps uncover biases, translation artifacts, or limitations in the agent’s multilingual handling.


## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

## Data Splits

Users can filter the benchmark tasks using two main criteria: by dataset (e.g., GAIA, MATH, SWE-bench, ASB) and by language (from the 11 supported languages). This flexible filtering enables targeted evaluation of agent performance and safety across specific domains and languages.

## Data format

All datasets are available in json format.


## Dataset Creation

### Curation Rationale

To build our multilingual benchmark, we use a hybrid machine–generation and human–verification pipeline. AI-based processing produces language variants at scale, while native speakers verify meaning and nuance. Each task is represented consistently across the ten diverse languages, ensuring faithful intent preservation and enabling reliable cross-language evaluation.


### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

We adopt a hybrid multi-stage translation pipeline that systematically combines the format-preserving strengths of Machine translation with the contextual refinement capabilities of LLMs, followed by manual verification for quality assurance.
More details about the hybrid translation pipeline is avaialble in our Research Paper.

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

[More Information Needed]

### Annotations [optional]

Each item was independently rated by a bilingual annotator fluent in English and the target language Annotators evaluated three criteria on a 1~5 Likert scale: adequacy (semantic fidelity), fluency (grammatical and stylistic naturalness), and formatting accuracy (preservation of special elements such as LaTeX, variable names, and code). A final metric, answerability, captured whether the translation preserved the original intent well enough for the annotator to confidently answer the question as if it were posed in English. 
More details about the Annotations is avaialble in our Research Paper.

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations.

## Citation [optional]

1. Mialon, G., Fourrier, C., Wolf, T., LeCun, Y., & Scialom, T. (2023).  
   **GAIA: A Benchmark for General-AI Assistants**. *ICLR 2023*. <https://openreview.net/forum?id=GAIA2023>

2. Zhang, H., Huang, J., Mei, K., Yao, Y., Wang, Z., Zhan, C., Wang, H., & Zhang, Y. (2024).  
   **Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents**. *arXiv 2410.02644*. <https://arxiv.org/abs/2410.02644>

3. Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D., & Steinhardt, J. (2021).  
   **Measuring Mathematical Problem Solving with the MATH Dataset**. *arXiv 2103.03874*. <https://arxiv.org/abs/2103.03874>

4. Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. (2023).  
   **SWE-Bench: Can Language Models Resolve Real-World GitHub Issues?** *arXiv 2310.06770*. <https://arxiv.org/abs/2310.06770>

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the dataset or dataset card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Dataset Card Authors [optional]

[More Information Needed]

## Dataset Card Contact

[More Information Needed]