---
license: other
license_name: deepreviewer-license
base_model: microsoft/phi-4
language:
- en
- zh
- ja
- ko
- fr
- de
metrics:
- accuracy
extra_gated_prompt: "You agree to not use the model for official peer reviews in any capacity."
extra_gated_fields:
  First Name: text
  Last Name: text
  Country: country
  Affiliation: text
  I want to use this model for:
    type: select
    options: 
      - Paper Improvement
      - Writing Practice
      - Self-assessment Tool
      - Learning Aid
      - Feedback Simulation
      - Revision Guide
      - Concept Validator
      - Reward Model
      - Educational Resource
      - Research Assistant
      - Supplementary Tool
      - label: Other
        value: other
  I agree to DO NOT use this model for Official Reviews and Publication Decisions: checkbox
extra_gated_button_content: Submit
library_name: transformers
---

## Model Info

**Homepage & Demo:** http://ai-researcher.net


DeepReviewer is a set of generative large language models that have undergone additional supervised training for academic paper review, with sizes of 7B and 14B. Both models are pure text language models based on the Phi-4 pre-trained language model. They utilize a multi-stage reasoning framework to generate in-depth, structured reviews of academic papers.

DeepReviewer offers three review modes to balance between depth and efficiency:
- **Fast Mode**: Quick reviews with summary, scores, and key points
- **Standard Mode**: Simulated multiple reviewer perspectives with verification
- **Best Mode**: Most comprehensive reviews with detailed analysis across all dimensions

According to our license, **all models created/trained/distributed/replicated based on these cannot be used for any formal review work**. 


DeepReviewer is an LLM capable of automatically evaluating the quality of a paper based on given paper content. It provides a near-human level paper review with comprehensive analysis, strengths, weaknesses, and suggestions. The Standard and Best modes can generate simulations of multiple reviewers and a Meta-Reviewer to provide diverse expert-level opinions.

The main purposes of DeepReviewer are:

- To promote iterative self-improvement in scientific research by providing structured feedback for paper revision
- To advance research on automated academic evaluation and peer review assistance
- To serve as a reward model for reinforcement learning systems designed to improve scientific research

**Model Release Date** Mar. 2025

**Model Knowledge Cutoff Date** Jan. 2025

## Model Specifications

|       Model Name      |   Pre-training Language Model   |            HF Link           |
|:---------------------:|:-------------------------------:|:----------------------------:|
| DeepReviewer-7B       | Qwen/Qwen2.5-7B-Instruct                        | [🤗 link](https://huggingface.co/WestlakeNLP/DeepReviewer-7B) |
| DeepReviewer-14B      | microsoft/phi-4                       | [🤗 link](https://huggingface.co/WestlakeNLP/DeepReviewer-14B) |

## Open Source License

The code in this repository is open-sourced under the Apache-2.0 license. The model weights are open-sourced under the DeepReviewer License, which incorporates additional content to ensure the model is not misused.

## Model Performance

We evaluated DeepReviewer across different metrics using test data from ICLR conference papers. The table below shows the comparison with other leading models:

### ICLR 2024

| Metric | DeepReviewer-7B | DeepReviewer-14B | CycleReviewer-70B | GPT-o1 | DeepSeek-R1 | Gemini-2.0-Flash-Thinking |
|--------------------------|-----------------|------------------|------------------|--------|-------------|---------------------------|
| Rating MSE↓             | 1.8262          | **1.3137**         | 2.4870           | 4.3414 | 4.1648      | 4.9297                    |
| Rating MAE↓             | 1.0870          | **0.9102**         | 1.2514           | 1.7294 | 1.6526      | 1.8711                    |
| Decision Accuracy$\uparrow$   | 0.5975          | **0.6406**         | 0.6304           | 0.4500 | 0.5248      | 0.5743                    |
| Decision F1$\uparrow$       | 0.5428          | **0.6307**         | 0.5696           | 0.4424 | 0.4988      | 0.5197                    |
| Rating Spearman$\uparrow$     | 0.2126          | **0.3559**         | 0.3356           | 0.2621 | 0.3256      | 0.0745                    |
| Pairwise Rating Acc$\uparrow$ | 0.5749          | **0.6242**         | 0.6160           | 0.5881 | 0.6206      | 0.5343                    |

### ICLR 2025

| Metric | DeepReviewer-7B | DeepReviewer-14B | CycleReviewer-70B | GPT-o1 | DeepSeek-R1 | Gemini-2.0-Flash-Thinking |
|--------------------------|-----------------|------------------|------------------|--------|-------------|---------------------------|
| Rating MSE↓             | 1.6730          | **1.3410**         | 2.4294           | 4.3072 | 4.7719      | 3.9232                    |
| Rating MAE↓             | 1.0379          | **0.9243**         | 1.2128           | 1.7917 | 1.8099      | 1.6470                    |
| Decision Accuracy$\uparrow$   | 0.6660          | **0.6878**         | 0.6782           | 0.4167 | 0.4259      | 0.6139                    |
| Decision F1$\uparrow$       | 0.5564          | **0.6227**         | 0.5737           | 0.4157 | 0.4161      | 0.4808                    |
| Rating Spearman$\uparrow$     | 0.2973          | **0.4047**         | 0.2674           | 0.2991 | 0.3237      | 0.2565                    |
| Pairwise Rating Acc$\uparrow$ | 0.6038          | **0.6402**         | 0.5928           | 0.6318 | 0.6289      | 0.6040                    |

DeepReviewer significantly outperforms other models on most metrics, despite its smaller parameter count. The 14B model achieves particularly strong results on Decision Accuracy and Score MSE, demonstrating its reliability in overall paper quality assessment.

## Intended Uses

**Expected Use Cases** DeepReviewer models are suitable for research purposes in multiple languages. This includes but is not limited to the following objectives:

1. Paper Improvement: Assist in enhancing the quality and clarity of academic papers.
2. Writing Practice: Provide a platform for users to practice and refine their academic writing skills.
3. Self-assessment Tool: Enable researchers to evaluate their own work before submission.
4. Learning Aid: Support students and researchers in understanding the peer review process.
5. Feedback Simulation: Offer simulated peer review feedback to prepare authors for actual reviews.
6. Revision Guide: Provide structured guidance for revising academic papers.
7. Concept Validator: Help researchers validate their ideas and hypotheses.
8. Reward Model: Serve as a component in machine learning systems for academic writing improvement.
9. Educational Resource: Act as a teaching tool for academic writing and peer review processes.
10. Research Assistant: Aid in literature reviews and research methodology refinement.
11. Supplementary Tool: Complement human review in informal, non-official settings.

**Out of Scope** We do not allow this model to be misused to influence the academic environment. The following are not permitted:

1. Official Reviews: DeepReviewer explicitly prohibits use for official peer reviews in any capacity.
2. Legal or Ethical Decisions: Not designed to make judgments on research ethics or legal compliance.
3. Factual Verification: While it can offer feedback, it should not be the sole source for fact-checking or verifying scientific claims.
4. Plagiarism Detection: Not equipped to serve as a plagiarism detection tool.
5. Publication Decisions: Cannot be used to make final decisions on whether a paper should be published.
6. Expert Consultation: Not a replacement for expert consultation in specialized fields.

**If you are unsure whether you meet our License requirements, please contact us for further inquiry**

## How to Use

The models included in this repository can be used with the `transformers` or `vllm` code libraries.

To generate review comments, we need a long context (**14000 tokens for Input and 5000 tokens for Output**), please ensure you have enough GPU memory. Here are our recommended configurations:

|     Model Name    | Recommended Config (bs>=5) |       Minimum Config (bs=1)      |
|:-----------------:|:--------------------------:|:--------------------------------:|
| DeepReviewer-7B   |    1 x RTX3090/4090/5090 (bf16)    | 1 x RTX 4070 (int8)              |
| DeepReviewer-14B  |    1 x A100 (bf16)    |  1 x RTX3090/4090/5090 (int8)             |

### Getting Your Paper Text

If you can provide the original Latex version or Markdown version of your paper, that would be ideal, and you can skip this step.

If you only have the PDF version of the paper, you need to convert it to Markdown or Latex format first. We recommend using tools like MagicPDF or other PDF-to-text converters.

### Using with vllm

```python
from ai_researcher.deep_reviewer import DeepReviewer
import torch

# Initialize DeepReviewer
reviewer = DeepReviewer(
    model_size="14B",  # Use "7B" for the smaller model
    device="cuda",
    tensor_parallel_size=1,  # Increase for multi-GPU setup
    gpu_memory_utilization=0.95
)

# Load paper content
paper_content = "Your paper content here"  # Replace with actual paper content

# Generate reviews in different modes
# Fast Mode for quick overview
fast_review = reviewer.evaluate([paper_content], mode="Fast Mode")

# Standard Mode with multiple reviewers
standard_review = reviewer.evaluate([paper_content], mode="Standard Mode", reviewer_num=3)


# Parse the review results
for result in standard_review:
    print("\n--- Meta-Review ---")
    print(f"Summary: {result['meta_review'].get('summary', 'N/A')}")
    print(f"Rating: {result['meta_review'].get('rating', 'N/A')}")
    print(f"Decision: {result['decision']}")
```


## Ethical Considerations

Academic Integrity: Although DeepReviewer is designed to assist researchers in improving paper quality, it should not be used to replace the real peer review process. We strongly recommend users to use this tool only as an auxiliary means for self-improvement and learning.

Fairness: The model may have biases, especially when evaluating interdisciplinary or emerging field research. Users should be aware of this and be cautious about the model's feedback.

Responsible Use: We call on users to use this model responsibly, and require users not to use it to produce false review opinions or manipulate the academic evaluation process according to our agreement.

Transparency: When using content generated by this model in any public setting, the DeepReviewer source should be clearly stated to maintain transparency and honesty in academia.

## Limitations

Knowledge Cutoff Date: The model's knowledge is cut off in October 2024, so it may lack understanding of new technologies, methods, or research trends that emerged after this date. This may lead to undervaluation of some highly innovative research.

Pure Text Limitations: As a pure text model, DeepReviewer cannot directly parse or evaluate images, charts, or complex formulas in papers. This may affect the comprehensive assessment of papers that heavily rely on visual elements.

Depth in Specialized Fields: Although the model has been trained across various domains, its evaluation may not be as accurate as human experts in very specialized or cutting-edge sub-fields.

Lack of Real-time Information: The model cannot access real-time academic databases or the latest published papers, which may lead to bias in assessing research novelty.

Disciplinary Bias: Due to limitations in training data, the model may have preferences for certain disciplines or research methods. Users should be aware of this and combine it with other opinions.

Language and Cultural Limitations: The model may perform poorly in handling papers with cultural nuances or field-specific terminology outside its training distribution.

## CITE

```
@inproceedings{
weng2025cycleresearcher,
title={CycleResearcher: Improving Automated Research via Automated Review},
author={Yixuan Weng and Minjun Zhu and Guangsheng Bao and Hongbo Zhang and Jindong Wang and Yue Zhang and Linyi Yang},
booktitle={The Thirteenth International Conference on Learning Representations},
year={2025},
url={https://openreview.net/forum?id=bjcsVLoHYs}
}
```