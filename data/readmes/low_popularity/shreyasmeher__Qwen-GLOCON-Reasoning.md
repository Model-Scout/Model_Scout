---
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
tags:
- unsloth
- text-classification
license: apache-2.0
library_name: transformers
base_model: Qwen/Qwen2.5-3B-Instruct
pipeline_tag: text-classification
---
# GLOCON-Reasoning: Qwen2.5-3B with GRPO Reinforcement Learning

[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-shreyasmeher%2FQwen--GLOCON--Reasoning-blue)](https://huggingface.co/shreyasmeher/Qwen-GLOCON-Reasoning)
[![Model](https://img.shields.io/badge/Base_Model-Qwen2.5--3B--Instruct-purple)](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
[![License](https://img.shields.io/badge/License-Apache_2.0-red)](https://www.apache.org/licenses/LICENSE-2.0)


## Important Usage Note

**Essential:** When using this model, you **must** set the prompt as described below to ensure the model follows the required structured reasoning format. Without explicitly setting the prompt, the model's outputs may not adhere to the expected XML structure and reasoning guidelines.

For instance, include the following prompt in your inference code:

```python
prompt = """
You are identifying conflict events and assigning them to one of five predefined categories. Think carefully and reason deeply, but when giving the final answer, provide only minimal, fixed-format outputs without any extra words.

Format your response:

<reasoning>
- Carefully analyze the text and explain:
  1. What action(s) triggered the event.
  2. Who are the participants or organizers.
  3. Where the event happened (city and country).
  4. Whether the event was violent or non-violent.
  5. Which of the five event categories fits best, and why.
</reasoning>

<answer>
1. Trigger: <exact phrase>
2. Participants: <actor1, actor2,...>
3. Location: <city, country>
4. Violence: <Violent / Non-violent>
5. Category: <one of: Demonstration / Armed Militancy / Group Clash / Industrial Action / Other>
</answer>
"""

```


## Reinforcement Learning Highlights
Unlike traditional supervised fine-tuning (used in ConflLlama), this model uses GRPO to:
1. **Optimize multiple reward signals** simultaneously
2. **Enforce structured reasoning format** through reinforcement signals
3. **Improve output consistency** with formatted XML responses
4. **Self-improve** through reinforcement rather than direct imitation



### Training Data
- **Dataset:** GLOCON event classification dataset
- **Time Period:** Contemporary civil conflict events
- **Format:** News articles with associated event categories
- **Labels:** Five main event categories:
  - Demonstration
  - Armed Militancy
  - Group Clash
  - Industrial Action
  - Other

### Data Processing
1. **Train/Test Split:**
   - 80% training, 20% testing
   - Consistent random seed (42) for reproducibility
2. **Format Standardization:**
   - System prompt with structured reasoning requirements
   - Consistent XML output format
3. **Answer Extraction:**
   - Specialized extraction from structured responses
   - Validation against known categories

### Training Format
- Input: News article describing potential conflict event
- Output: Structured XML with reasoning and final category


## Key Mathematical Concepts

### Policy Gradient with Multiple Rewards
The GRPO approach optimizes policy parameters using:

$$\nabla_\theta J(\theta) = \mathbb{E} \left[ \sum_{i=1}^{N} w_i R_i(x, y) \nabla_\theta \log \pi_\theta(y|x) \right]$$

### Reward Functions
Our implementation uses five specialized reward functions:

1. **Correctness Reward:** 2.0 points for accurate classification
2. **Category Format Reward:** 0.5 points for valid category selection
3. **Format Rewards:** Combined 1.0 points for proper XML structure
4. **XML Microrewards:** Small incentives for tag placement and structure

## Training Details
- **Framework:** Unsloth GRPO
- **Hardware:** Single NVIDIA GPU with vLLM acceleration
- **Training Configuration:**
  - Batch Size: 1 per device
  - Gradient Accumulation Steps: 4
  - Learning Rate: 5e-6
  - Max Steps: 1,000
  - Save Steps: 500
  - Logging Steps: 1
  - Samples per prompt: 6
  - Memory utilization: 60%

### LoRA Configuration
- **Rank:** 64 (significantly larger than ConflLlama's rank 8)
- **Target Modules:** q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- **Alpha Scaling:** 64
- **Quantization:** 4-bit training
- **Gradient Checkpointing:** Enabled ("unsloth" mode)

### Generation Parameters
- **Temperature:** 0.8
- **Top-p:** 0.95
- **Max tokens:** 256
- **Max prompt length:** 512

## Model Architecture
The training architecture combines reinforcement learning with efficient LLM fine-tuning. 

### Reinforcement Learning Benefits
This model demonstrates key advantages over supervised fine-tuning:

1. **Structured Output Enforcement**
   - Consistent XML formatting:
   ```
   <reasoning>
   1. Triggers detected: [...]
   2. Participants and organizers: [...]
   3. Location details: [...]
   4. Violence assessment: [...]
   5. Event category determination: [...]
   </reasoning>
   <answer>
   [Final category]
   </answer>
   ```

2. **Improved Reasoning Capability**
   - Explicit step-by-step reasoning before final classification
   - Consideration of multiple factors (violence, participants, location)
   - Transparent justification process

3. **Reward-Based Improvement**
   - Self-correcting behavior through multiple reward signals
   - Balance between format adherence and classification accuracy
   - Incentivizes proper structure without sacrificing correctness

### Implementation Details
The reward functions are implemented with efficient vectorized operations:

```python
def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]:
    responses = [completion[0]['content'] for completion in completions]
    extracted_responses = [extract_xml_answer(r) for r in responses]
    return [2.0 if r.strip() == a.strip() else 0.0 
            for r, a in zip(extracted_responses, answer)]
```


## Memory Optimizations
- Used 4-bit quantization
- Gradient accumulation steps: 4
- Memory-efficient gradient checkpointing
- Reduced maximum sequence length to 1024
- GPU memory utilization capped at 60%
- Fast inference with vLLM


## Intended Use
This model is designed for:
1. Classification of civil conflict events with reasoning
2. Academic research requiring transparent decision processes
3. Event analysis with structured outputs
4. Educational demonstration of RL-based classification

## Limitations
1. Fixed output structure may limit flexibility
2. Performance dependent on quality of reward functions
3. Maximum sequence length limited to 1024 tokens
4. Reinforcement may overoptimize for reward signals rather than true understanding
5. Limited to five predefined event categories
6. May not generalize well to conflict events outside training distribution

## Ethical Considerations
1. Model trained on conflict event data
2. Should be used responsibly for research purposes only
3. Not intended for operational security decisions
4. Results should be interpreted with appropriate context
5. May contain biases present in training data

## Citation
```bibtex
@misc{glocon-reasoning,
  author = {Meher, Shreyas},
  title = {GLOCON-Reasoning: Qwen2.5-3B with GRPO Reinforcement Learning},
  year = {2024},
  publisher = {HuggingFace},
  note = {Based on Qwen2.5-3B-Instruct and GRPO framework}
}
```

## Acknowledgments
- Unsloth for GRPO implementation and optimization framework
- Qwen team for the base model
- Hugging Face for transformers infrastructure
- vLLM team for fast inference capabilities
- This research was supported by NSF award 2311142

<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>