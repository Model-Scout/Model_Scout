---
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
license: cc-by-nc-4.0
quantized_by: bartowski
pipeline_tag: text-generation
lm_studio:
  param_count: 35b
  use_case: general
  release_date: 11-03-2024
  model_creator: CohereForAI
  prompt_template: cohere_command_r
  system_prompt: none
  base_model: cohere
  original_repo: CohereForAI/c4ai-command-r-v01
---

## 💫 Community Model> C4AI Command-R 35B by Cohere For AI

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [Cohere For AI](https://huggingface.co/CohereForAI)<br>
**Original model**: [c4ai-command-r-v01](https://huggingface.co/CohereForAI/c4ai-command-r-v01)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b2536](https://github.com/ggerganov/llama.cpp/releases/tag/b2536)<br>

## Model Summary:

C4AI Command-R is a 35B parameter model released by Cohere For AI. Command-R is optimized for a variety of use cases including reasoning, summarization, and question answering. Command-R has the capability for multilingual generation evaluated in 10 languages and highly performant RAG capabilities.

## Prompt Template:

Choose the `Cohere Command R` preset in your LM Studio.

Under the hood, the model will see a prompt that's formatted like so:
```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
```

Note that this model does not support a System prompt.

## Use case and examples

Command-R is tuned for a broad range of uses such as reasoning, summarizing, general knowledge, and coding.

### Reasoning:

```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>
Statements:

All mathematicians are logical thinkers.
No logical thinker is irrational.
Some scientists are mathematicians.
Conclusions:

I. Some scientists are logical thinkers.
II. No mathematician is irrational.
III. Some scientists are irrational.

Analyze these statements and decide which conclusions are correct based on the logical relationships.<|END_OF_TURN_TOKEN|>
<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
The logical relationships between the statements and the correctness of each conclusion are as follows:

I. Some scientists are logical thinkers: This conclusion follows logically from the given statements. Since some scientists are mathematicians and all mathematicians are logical thinkers, it can be deduced that some scientists indeed exhibit logical thinking. This conclusion is correct.

II. No mathematician is irrational: This conclusion is a direct inference from the given statements. As no logical thinker is irrational, and all mathematicians are logical thinkers, it's reasonable to assume that no mathematician can be described as irrational. This conclusion is also correct.

III. Some scientists are irrational: This conclusion does not necessarily follow from the given statements. While it's true that not all scientists may be logical thinkers (as indicated in the second conclusion), it doesn't imply that they are irrational. The statement about scientists being irrational cannot be definitively concluded from the given information, so this conclusion is not correct. 

In summary, only I and II are correct conclusions based on the logical relationships within the statements provided.<|END_OF_TURN_TOKEN|>
```

### Coding:

```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>
Can you provide a merge sort implementation in python?<|END_OF_TURN_TOKEN|>
<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
Here's a merge sort implementation in Python:

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
    
            merge_sort(left)
            merge_sort(right)
    
            i = j = k = 0
    
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
    
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
    
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
    
    # Example usage
    my_list = [12, 11, 13, 5, 6, 7]
    merge_sort(my_list)
    print(my_list)


The `merge_sort` function takes a list `arr` as input and recursively divides it into two halves until each half contains a single element or is empty. It then merges the two sorted halves in a sorted manner. The example usage demonstrates how to use the function to sort a list.<|END_OF_TURN_TOKEN|>
```

## Technical Details

This model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety.

Multilingual capabilities: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, Simplified Chinese, and Arabic.

Pre-training data additionally included the following 13 languages: Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian.

Supports a context length of 128k.

For more information on prompting, you can reference the official documentation [here](https://docs.cohere.com/docs/prompting-command-r)

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.
