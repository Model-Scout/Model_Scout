---
language:
- ko
---

# Dataset Card for S1K-KR

## Dataset Description

### Overview

S1K-KR is a Korean translation of the [simplescaling/s1K dataset](https://huggingface.co/datasets/simplescaling/s1K). It contains 1,000 problem-solution pairs across various domains, with each instance including the problem statement, solution, and detailed thinking trajectories (chain-of-thought reasoning) in Korean.

This dataset is designed to help train and evaluate Korean language models on complex reasoning tasks, providing both the final solutions and the step-by-step reasoning processes.

[Click here to see the Korean version of this overview.](README_KR.md)


### Supported Tasks and Models

This dataset can be used for the following tasks:
- Complex reasoning
- Chain-of-thought (CoT) prompting
- Problem-solving capabilities evaluation
- Korean language understanding and generation
- Step-by-step solution generation

## Dataset Structure

### Data Instances

Below is an example of a data instance from the dataset:

```python
{                              
    'solution_kr': '1. **삼각함수를 이용한 함수 재작성:**\n   \\[\n   f(x) = 1 - a \\cos(x) - b \\sin(x) - A \\cos(2x) - B \\sin(2x)\n   \\]\n   사인과 코사인의 덧셈 정리를 사용합니다:...', 
    'question_kr': '$a, b, A, B$가 주어진 실수라고 하자. 다음과 같은 함수가 정의되어 있다고 하자.  \n\\[ f(x) = 1 - a \\cdot \\cos(x) - b \\cdot \\sin(x) - A \\cdot \\c ...',                          
    'thinking_trajectories_kr': '["$f(x) = 1 - a \\\\cos x - b \\\\sin x - A \\\\cos 2x - B \\\\sin 2x \\\\geq 0$이 모든 $x \\\\in \\\\mathbb{R}$에 대해 성립한다고 하자.  ...'                
}
```

### Data Fields

- `solution`: Original English solution to the problem
- `question`: Original English question or problem statement
- `cot_type`: Category of the reasoning task (e.g., math, logic, common sense)
- `source_type`: Source of the original problem
- `metadata`: Additional information about the problem
- `cot`: Chain-of-thought reasoning in English
- `thinking_trajectories`: Detailed step-by-step reasoning process in English
- `attempt`: Information about solution attempts
- `question_kr`: Korean translation of the question
- `solution_kr`: Korean translation of the solution
- `thinking_trajectories_kr`: Korean translation of the thinking trajectories

### Data Statistics

- **Total Samples**: 1,000
- **Total Tokens** across all analyzed Korean columns: 3,119,257
- **Overall Vocabulary Size**: 196,501
- **Tokenization Method**: wordpiece

#### Column-specific Statistics:

- **solution_kr**:
  - Valid Samples: 1,000
  - Total Tokens: 388,053
  - Vocabulary Size: 31,671
  - Average Tokens per Instance: 388.05
  - Maximum Sequence Length: 3,290

- **question_kr**:
  - Valid Samples: 1,000
  - Total Tokens: 175,985
  - Vocabulary Size: 17,510
  - Average Tokens per Instance: 175.99
  - Maximum Sequence Length: 815

- **thinking_trajectories_kr**:
  - Valid Samples: 1,000
  - Total Tokens: 2,555,219
  - Vocabulary Size: 169,571
  - Average Tokens per Instance: 2,555.22
  - Maximum Sequence Length: 6,482


![image/png](https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/NTzP5wjXXZ1jyW5jeIaxr.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/Ta9_MSuYfF9HteQexbtxv.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/7AmIKvNf2o5kXiFk6OhNf.png)

### Token Distribution Analysis

The token distribution analysis reveals that:
- The thinking trajectories contain the majority of tokens (82% of all tokens)
- Solutions are moderately sized with an average of ~388 tokens
- Questions are relatively concise with an average of ~176 tokens
- The large vocabulary size indicates a diverse range of topics and specialized terminology

## Dataset Creation

### Source Data

This dataset is a Korean translation of the simplescaling/s1K dataset, which contains problem-solution pairs with detailed reasoning processes. The original dataset covers a variety of domains and reasoning types.

### Translation Process

The original English content was translated into Korean with GPT4o, preserving the reasoning structure and technical terminology. The translation focused on maintaining the accuracy of the reasoning steps and domain-specific vocabulary.

## Considerations for Using the Data

### Applicable Use Cases

This dataset is particularly useful for:
- Training Korean language models on complex reasoning tasks
- Evaluating models' step-by-step problem-solving capabilities
- Improving chain-of-thought prompting techniques for Korean NLP
- Benchmarking Korean language understanding and generation

### Limitations and Biases

- As a translated dataset, some nuances from the original English may not perfectly transfer to Korean
- Domain-specific terminology might have varying translation quality
- The dataset's distribution across problem types might not be representative of all reasoning challenges

## Additional Information

### Citation Information
For the original English dataset, please cite:

```
@misc{muennighoff2025s1simpletesttimescaling,
      title={s1: Simple test-time scaling}, 
      author={Niklas Muennighoff and Zitong Yang and Weijia Shi and Xiang Lisa Li and Li Fei-Fei and Hannaneh Hajishirzi and Luke Zettlemoyer and Percy Liang and Emmanuel Candès and Tatsunori Hashimoto},
      year={2025},
      eprint={2501.19393},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.19393}, 
}
```

