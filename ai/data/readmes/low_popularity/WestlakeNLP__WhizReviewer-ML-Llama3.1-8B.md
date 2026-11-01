---
license: other
license_name: whizreviewer-llama-3.1-license
license_link: LICENSE
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
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
  Specific date: date_picker
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
  geo: ip_location
  I agree to DO NOT use this model for Official Reviews and Publication Decisions: checkbox
extra_gated_button_content: Submit
library_name: transformers
---



# WhizReviewer-ML-Llama3.1-8B



#### Model Info

The WhizReviewer is a set of generative large language models that have undergone additional supervised training, with sizes of 8B, 70B, and 123B respectively. All models are pure text language models, with the 8B and 70B derived from the Llama3.1 pre-trained language model, and the 123B from the Mistral-Large-2 model. They all use the Transformer architecture.

All models have undergone extensive supervised training on a dataset of paper-review comments in the field of **machine learning (including CV, NLP, MM)**, aimed at providing expert-level review comments. According to our license, **all models created/trained/distributed/replicated based on these cannot be used for any formal review work**. We also provide code based on [FastDetectGPT](https://github.com/baoguangsheng/fast-detect-gpt) to detect misuse of this series of models in formal settings.

![info](./image/info.png)

WhizReviewer-ML is an LLM capable of automatically evaluating the quality of a paper based on given paper content. It can provide a near-human level paper review opinion and evaluation score. Specifically, WhizReviewer-ML will generate simulations of multiple members in a paper program committee, including a group of Reviewers (we recommend 4) and a Meta-Reviewer to provide expert-level opinions. Please note that WhizReviewer-ML is trained to generate ICLR or NeurIPS level review comments, so the Meta Reviewer it generates may require relatively high quality to generate an "Accept".

The main purposes of the WhizReviewer-ML series models are the following two:

- To promote iterative self-improvement in human scientific research. Given the long review cycle for papers, WhizReviewer-ML can enable rapid iteration and refinement of papers.
- To promote Auto-Research. This model can serve as a Reward Model to assist in the Research capabilities of artificial intelligence models.

**Model Release Date** August 16, 2024

**Model Knowledge Cutoff Date** January 2024

#### Model Specifications

|            Model Name             |                 Pre-training Language Model                  |                           HF Link                            |  MS Link   |
| :-------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :--------: |
|    WhizReviewer-ML-Llama3.1-8B    | [Llama3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) | [🤗 link](https://huggingface.co/WestlakeNLP/WhizReviewer-ML-Llama3.1-8B) | [🤖 TODO]() |
|   WhizReviewer-ML-Llama3.1-70B    | [Llama3.1-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) | [🤗 link](https://huggingface.co/WestlakeNLP/WhizReviewer-ML-Llama3.1-70B) | [🤖 TODO]() |
|     WhizReviewer-ML-Pro-123B      | [Mistral-Large-2](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407) | [🤗 link](https://huggingface.co/WestlakeNLP/WhizReviewer-ML-Pro-123B) | [🤖 TODO]() |
| WhizReviewer-Science-Llama3.1-8B  | [Llama3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) |                          [🤗 TODO]()                          | [🤖 TODO]() |
| WhizReviewer-Science-Llama3.1-70B | [Llama3.1-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) |                          [🤗 TODO]()                          | [🤖 TODO]() |
|   WhizReviewer-Science-Pro-123B   | [Mistral-Large-2](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407) |                          [🤗 TODO]()                          | [🤖 TODO]() |

#### Open Source License

The code in this repository is open-sourced under the Apache-2.0 license. The model weights are open-sourced under the WhizReviewer License, which introduces additional content based on the **Llama 3.1 Community License** to ensure the model is not misused.




#### Model Performance

We used 784 papers and their review comments from ICLR 2024 as test data, which were not included in the training dataset.



| Metric                        | [WhizReviewer-ML-Llama3.1-8B](https://huggingface.co/WestlakeNLP/WhizReviewer-ML-Llama3.1-8B) | [WhizReviewer-ML-Llama3.1-70B](https://huggingface.co/WestlakeNLP/WhizReviewer-ML-Llama3.1-70B) | [WhizReviewer-ML-Pro-123B](https://huggingface.co/WestlakeNLP/WhizReviewer-ML-Pro-123B) |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Decisions (Accept/Reject) Acc | 59.41%                                                       | 61.58%                                                       | **74.55%**                                                   |
| Score Avg Abs                 | 1.24                                                         | 1.28                                                         | **1.05**                                                     |
| Score Min Abs                 | 1.31                                                         | **1.18**                                                     | 1.45                                                         |
| Score Max Abs                 | 1.73                                                         | 1.71                                                         | **1.01**                                                     |
| Score Perfect Match           | 3.23%                                                        | 1.47%                                                        | **3.65%**                                                       |
| Score Avg Acc                 | 7.93%                                                        | 6.83%                                                        | **10.94%**                                                   |
| Score Min Acc                 | 36.96%                                                       | **42.70%**                                                   | 31.77%                                                       |
| Score Max Acc                 | 24.73%                                                       | 23.69%                                                       | **49.09%**                                                   |

We instruct the WhizReviewer-ML model to simulate reviewers from low-scoring to high-scoring, generating review comments and final scores in sequence. After collecting all review comments, a Meta-Reviewer is generated, which can predict the final acceptance result. In the evaluation results, Decisions Acc represents the accuracy of predicting the correct outcome given a paper, while Score Avg Abs represents the absolute difference between the average predicted score and the original score.

#### How to use

The models included in this repository can be used with the `transformers` or `vllm` code libraries.

To generate Review comments, we need a long context (**14000 tokens for Input and 5000 tokens for Output**), please ensure you have enough GPU memory. Here are our recommended configurations:

|          Model Name          | Recommended Config (bs>=5) |          Minimum Config (bs=1)          |
| :--------------------------: | :------------------------: | :-------------------------------------: |
| WhizReviewer-ML-Llama3.1-8B  |    2 x A100/H100 (bf16)    | 1 x A100/H100 (int8) / 1 x A6000 (int4) |
| WhizReviewer-ML-Llama3.1-70B |    8 x A100/H100 (bf16)    |          2 x A100/H100 (bf16) / 1 x A100/H100 (int4)           |
|   WhizReviewer-ML-Pro-123B   |    8 x A100/H100 (bf16)    |          2 x A100/H100 (bf16) / 1 x A100/H100 (int4)            |

##### Getting Your Paper Text

If you can provide the original Latex version or Markdown version of your paper, that would be ideal, and you can skip this step.

If you only have the PDF version of the paper, you need to convert it to Markdown or Latex format first. We recommend using one of the following two methods for conversion:

**Online** You don't need to download any models, just register and get free tokens from [doc2x](https://doc2x.noedgeai.com/?inviteCode=WE5L94), then make sure your `pdfdeal` is the latest version: `pip install --upgrade pdfdeal`

```python
from pdfdeal import Doc2X
from pdfdeal import get_files
client = Doc2X(apikey='xxx') # apikey from doc2x
file_list, rename = get_files(path=r"path/PDF", mode="pdf", out="md")
success, failed, flag = client.pdfdeal(
    pdf_file=file_list,
    output_path=r"OutputPath/PDF",
    output_format='md',
    output_names=rename,
)
print(success)
print(failed)
print(flag)
```

At this point, you will be able to view the markdown format of the paper.

**Offline** If you need to run locally, we recommend using [MagicPDF](https://github.com/magicpdf/Magic-Doc). First, please follow the relevant guide to install it, then you will be able to use the code below to convert PDF paper files to markdown format:

```python
from magic_doc.docconv import DocConverter, S3Config
converter = DocConverter(s3_config=None)
markdown_cotent, time_cost = converter.convert("path/PDF", conv_timeout=300)
```

##### Using with transformers

Starting from `transformers >= 4.44.0`, first make sure your `transformers` is updated: `pip install -U transformers`

```python
import transformers
import torch
import re

def process_text(text, skip_appendix=True):
    pattern = re.compile(r"Under review as a conference paper at ICLR 2024", re.IGNORECASE)
    text = pattern.sub("", text)

    pattern = re.compile(r"Published as a conference paper at ICLR 2024", re.IGNORECASE)
    text = pattern.sub("", text)
    
    if skip_appendix:
        match = re.search(r"REFERENCES", text, re.IGNORECASE)

        if match:
            # Truncate the text at "REFERENCES"
            text = text[:match.start()]

    match = re.search(r"ABSTRACT", text, re.IGNORECASE)

    if match:
        text = text[match.start():]

    return text.strip()
    
model_id = "WestlakeNLP/WhizReviewer-ML-Llama-3.1-8B"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

system_prompt = \
"""You are an expert academic reviewer tasked with providing a thorough and balanced evaluation of research papers. For each paper submitted, conduct a comprehensive review addressing the following aspects:

1. Summary: Briefly outline main points and objectives.
2. Soundness: Assess methodology and logical consistency.
3. Presentation: Evaluate clarity, organization, and visual aids.
4. Contribution: Analyze significance and novelty in the field.
5. Strengths: Identify the paper's strongest aspects.
6. Weaknesses: Point out areas for improvement.
7. Questions: Pose questions for the authors.
8. Rating: Score 1-10, justify your rating.
9. Meta Review: Provide overall assessment and recommendation (Accept/Reject).

Maintain objectivity and provide specific examples from the paper to support your evaluation.

You need to fill out **4** review opinions."""


markdown_context = "xxxxxxx" # Your paper's context
markdown_context = process_text(markdown_context, skip_appendix=True) # We suggest to skip appendix.

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": markdown_context},
]

outputs = pipeline(
    messages,
    max_new_tokens=4096,
)
print(outputs[0]["generated_text"][-1])
```

##### Using with vllm

Compared to `transformers`, we more strongly recommend using `vllm` for fast text generation. Usually, it can complete generation within 2 minutes: `pip install -U vllm`.

```python
from vllm import LLM, SamplingParams
import torch
import re

def process_text(text, skip_appendix=True):
    pattern = re.compile(r"Under review as a conference paper at ICLR 2024", re.IGNORECASE)
    text = pattern.sub("", text)

    pattern = re.compile(r"Published as a conference paper at ICLR 2024", re.IGNORECASE)
    text = pattern.sub("", text)
    
    if skip_appendix:
        match = re.search(r"REFERENCES", text, re.IGNORECASE)
    
        if match:
            # Truncate the text at "REFERENCES"
            text = text[:match.start()]
    
    match = re.search(r"ABSTRACT", text, re.IGNORECASE)
    
    if match:
        text = text[match.start():]
    
    return text.strip()

model_id = "WestlakeNLP/WhizReviewer-ML-Llama-3.1-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
llm = LLM(
        model=model_name,
        tensor_parallel_size=8,
        max_model_len=15000,
        gpu_memory_utilization=0.95,
    )

system_prompt = \
"""You are an expert academic reviewer tasked with providing a thorough and balanced evaluation of research papers. For each paper submitted, conduct a comprehensive review addressing the following aspects:

1. Summary: Briefly outline main points and objectives.
2. Soundness: Assess methodology and logical consistency.
3. Presentation: Evaluate clarity, organization, and visual aids.
4. Contribution: Analyze significance and novelty in the field.
5. Strengths: Identify the paper's strongest aspects.
6. Weaknesses: Point out areas for improvement.
7. Questions: Pose questions for the authors.
8. Rating: Score 1-10, justify your rating.
9. Meta Review: Provide overall assessment and recommendation (Accept/Reject).

Maintain objectivity and provide specific examples from the paper to support your evaluation.

You need to fill out **4** review opinions."""


markdown_context = "xxxxxxx" # Your paper's context
markdown_context = process_text(markdown_context, skip_appendix=True) # We suggest to skip appendix.

sampling_params = SamplingParams(temperature=0.4, top_p=0.95, max_tokens=4096)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": markdown_context},
]

input_ids = tokenizer.apply_chat_template(messages+[{'role':'assistant','content':'\n\n## Reviewer\n'}], tokenize=False,add_generation_prompt=True)[:-4]
outputs = llm.generate([input_ids], sampling_params)
```

For more usage methods, please refer to the [vLLM](https://docs.vllm.ai/en/latest/) documentation.

#### Harmlessness and Safety

The fine-tuning of language models can compromise their harmlessness, which leads to the possibility of them being used for illegal purposes. We value the harmlessness settings of language models and hope that the WhizReviewer model can ensure safe deployment for anyone. Therefore, before the model's release, we have added extra safety restrictions to the weights through the SafetyLock method. SafetyLock can mitigate the inherent safety risks of the model while balancing practicality and safety.



#### Ethical Considerations

Academic Integrity: Although the WhizReviewer model is designed to assist researchers in improving paper quality, it should not be used to replace the real peer review process. We strongly recommend users to use this tool only as an auxiliary means for self-improvement and learning.

Fairness: The model may have biases, especially when evaluating interdisciplinary or emerging field research. The current model is only suitable for the machine learning field. Users should be aware of this and be cautious about the model's feedback.

Responsible Use: We call on users to use this model responsibly, and require users not to use it to produce false review opinions or manipulate the academic evaluation process according to our agreement.

Transparency: When using content generated by this model in any public setting, the WhizReviewer source should be clearly stated to maintain transparency and honesty in academia.

#### Limitations

Knowledge Cutoff Date: The model's knowledge is cut off in January 2024, so it may lack understanding of new technologies, methods, or research trends that emerged after this date. This may lead to undervaluation of some highly innovative research.

Pure Text Limitations: As a pure text model, WhizReviewer-ML-Llama-3.1-8B cannot directly parse or evaluate images, charts, or complex formulas in papers. This may affect the comprehensive assessment of papers that heavily rely on visual elements.

Depth in Specialized Fields: Although the model has been specially trained in the field of machine learning, its evaluation may not be as accurate as human experts in the field for very specialized or cutting-edge sub-fields.

Lack of Real-time Information: The model cannot access real-time academic databases or the latest published papers, which may lead to bias in assessing research novelty.

Disciplinary Bias: Due to limitations in training data, the model may have preferences for certain disciplines or research methods. Users should be aware of this and combine it with other opinions.

Language and Cultural Limitations: The model may perform poorly in handling non-English papers or cross-cultural research, requiring users to be extra cautious in these cases.

Scoring Consistency: The model's scoring may have some inconsistencies, especially when dealing with borderline cases or interdisciplinary research.

#### Detecting Misuse of WhizReviewer-ML

We use Fast-Detect-GPT to avoid misuse of WhizReviewer. The table below shows the detection performance of Fast-Detect-GPT, which can to some extent prevent WhizReviewer-ML from being used in unauthorized places.

| Model                        | Detect Acc |
| ---------------------------- | ---------- |
| WhizReviewer-ML-Llama3.1-8B  | 98.43      |
| WhizReviewer-ML-Llama3.1-70B | 99.47      |
| WhizReviewer-ML-Pro-123B     | 95.14      |

We mixed three hundred review comment samples from ICLR2024 and generated samples from WhizReviewer-ML as the evaluated dataset, with Llama-3.1-8B as the reference model. Detect Acc indicates the accuracy of being correctly detected by Fast-Detect-GPT.

#### Intended Uses

**Expected Use Cases** The WhizReviewer series models are suitable for research purposes in multiple languages. This includes but is not limited to the following objectives:

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

**Out of Scope** We do not allow this model to be misused to influence the academic environment. In addition to what is not allowed under the Llama License and Mistral License, the following are also not permitted by us:

1. Official Reviews: The WhizReviewer-ML explicitly prohibits use for official peer reviews in any capacity.
2. Legal or Ethical Decisions: Not designed to make judgments on research ethics or legal compliance.
3. Factual Verification: While it can offer feedback, it should not be the sole source for fact-checking or verifying scientific claims.
4. Plagiarism Detection: Not equipped to serve as a plagiarism detection tool.
5. Publication Decisions: Cannot be used to make final decisions on whether a paper should be published.
6. Expert Consultation: Not a replacement for expert consultation in specialized fields.

**If you are unsure whether you meet our License requirements, please send your relevant application to zhuminjun@westlake.edu.cn for further inquiry**


#### Case Study

We take a (Poster Paper) from ICLR 2024 titled "Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks" as an example to showcase WhizReviewer-ML's review suggestions. Please refer to [Openreview](https://openreview.net/forum?id=9nsNyN0vox) for the original reviews. The human review scores were *[5,6,6,8]*. The following content is from the output of WhizReviewer-ML-Llama3.1-8B:



```
## Reviewer

### Summary

This paper proposes a framework called Neural Comprehension to integrate compiled neural networks (CoNNs) into the standard transformer architecture. CoNNs are designed to explicitly encode rules through artificially generated attention weights. The authors demonstrate the effectiveness of their approach in various symbolic tasks and arithmetic reasoning tasks.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to understand.
- The method is general and can be applied to LLMs of different scales.

### Weaknesses

- The method seems to be a straightforward combination of CoNNs and LLMs, which makes me question the novelty of the proposed method.
- The experimental results are not strong enough to support the claim that the proposed method can improve the performance of LLMs on symbolic tasks.
- The paper lacks a thorough analysis of the limitations of the proposed method.

### Questions

- The method seems to be a straightforward combination of CoNNs and LLMs, which makes me question the novelty of the proposed method. Can the authors provide more insight into the novelty of the proposed method?
- The experimental results are not strong enough to support the claim that the proposed method can improve the performance of LLMs on symbolic tasks. For example, in Figure 4, the performance of Neural Comprehension is not significantly better than that of GPT-3.5 in most cases. Can the authors provide more convincing evidence to support their claim?
- The paper lacks a thorough analysis of the limitations of the proposed method. For example, the proposed method may not be suitable for tasks that require more complex reasoning, such as logical reasoning. Can the authors discuss the limitations of the proposed method and provide more insights into its potential applications?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a new method called Neural Comprehension, which integrates compiled neural networks (CoNNs) into the standard transformer architecture to improve the performance of language models on symbolic tasks. CoNNs are designed to explicitly encode rules through artificially generated attention weights. The authors demonstrate the effectiveness of their approach in various symbolic tasks and arithmetic reasoning tasks.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The method is general and can be applied to LLMs of different scales.

### Weaknesses

1. The paper lacks a thorough analysis of the limitations of the proposed method. For example, the proposed method may not be suitable for tasks that require more complex reasoning, such as logical reasoning. Can the authors discuss the limitations of the proposed method and provide more insights into its potential applications?
2. The experimental results are not strong enough to support the claim that the proposed method can improve the performance of LLMs on symbolic tasks. For example, in Figure 4, the performance of Neural Comprehension is not significantly better than that of GPT-3.5 in most cases. Can the authors provide more convincing evidence to support their claim?
3. The paper lacks a thorough analysis of the limitations of the proposed method. For example, the proposed method may not be suitable for tasks that require more complex reasoning, such as logical reasoning. Can the authors discuss the limitations of the proposed method and provide more insights into its potential applications?

### Questions

1. The paper lacks a thorough analysis of the limitations of the proposed method. For example, the proposed method may not be suitable for tasks that require more complex reasoning, such as logical reasoning. Can the authors discuss the limitations of the proposed method and provide more insights into its potential applications?
2. The experimental results are not strong enough to support the claim that the proposed method can improve the performance of LLMs on symbolic tasks. For example, in Figure 4, the performance of Neural Comprehension is not significantly better than that of GPT-3.5 in most cases. Can the authors provide more convincing evidence to support their claim?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

This paper proposes a method called Neural Comprehension to integrate compiled neural networks (CoNNs) into the standard transformer architecture to improve the performance of language models on symbolic tasks. CoNNs are designed to explicitly encode rules through artificially generated attention weights. The authors demonstrate the effectiveness of their approach in various symbolic tasks and arithmetic reasoning tasks.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The method is general and can be applied to LLMs of different scales.

### Weaknesses

1. The paper lacks a thorough analysis of the limitations of the proposed method. For example, the proposed method may not be suitable for tasks that require more complex reasoning, such as logical reasoning. Can the authors discuss the limitations of the proposed method and provide more insights into its potential applications?
2. The experimental results are not strong enough to support the claim that the proposed method can improve the performance of LLMs on symbolic tasks. For example, in Figure 4, the performance of Neural Comprehension is not significantly better than that of GPT-3.5 in most cases. Can the authors provide more convincing evidence to support their claim?
3. The paper lacks a thorough analysis of the limitations of the proposed method. For example, the proposed method may not be suitable for tasks that require more complex reasoning, such as logical reasoning. Can the authors discuss the limitations of the proposed method and provide more insights into its potential applications?

### Questions

1. The paper lacks a thorough analysis of the limitations of the proposed method. For example, the proposed method may not be suitable for tasks that require more complex reasoning, such as logical reasoning. Can the authors discuss the limitations of the proposed method and provide more insights into its potential applications?
2. The experimental results are not strong enough to support the claim that the proposed method can improve the performance of LLMs on symbolic tasks. For example, in Figure 4, the performance of Neural Comprehension is not significantly better than that of GPT-3.5 in most cases. Can the authors provide more convincing evidence to support their claim?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Reviewer

### Summary

The paper proposes a framework that integrates compiled neural networks (CoNNs) into the standard transformer architecture to improve the performance of language models on symbolic tasks. The authors demonstrate the effectiveness of their approach in various symbolic tasks and arithmetic reasoning tasks.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow.

### Weaknesses

The paper lacks a thorough analysis of the limitations of the proposed method. For example, the proposed method may not be suitable for tasks that require more complex reasoning, such as logical reasoning. Can the authors discuss the limitations of the proposed method and provide more insights into its potential applications?

### Questions

The paper lacks a thorough analysis of the limitations of the proposed method. For example, the proposed method may not be suitable for tasks that require more complex reasoning, such as logical reasoning. Can the authors discuss the limitations of the proposed method and provide more insights into its potential applications?

### Flag For Ethics Review

No ethics review needed.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

## Meta Review

This paper proposes a framework called Neural Comprehension to integrate compiled neural networks (CoNNs) into the standard transformer architecture to improve the performance of language models on symbolic tasks. CoNNs are designed to explicitly encode rules through artificially generated attention weights. The authors demonstrate the effectiveness of their approach in various symbolic tasks and arithmetic reasoning tasks.

The reviewers raised several concerns about the novelty of the proposed method, the experimental results, and the analysis of the limitations of the proposed method. The authors did not provide any rebuttal.

### justification_for_why_not_higher_score

The reviewers raised several concerns about the novelty of the proposed method, the experimental results, and the analysis of the limitations of the proposed method. The authors did not provide any rebuttal.

### justification_for_why_not_lower_score

N/A

**********

## Paper Decision

Reject (not good enough)
```
