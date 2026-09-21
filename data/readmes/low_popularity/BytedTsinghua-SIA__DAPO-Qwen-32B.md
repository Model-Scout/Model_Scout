---
license: apache-2.0
datasets:
- BytedTsinghua-SIA/DAPO-Math-17k
base_model:
- Qwen/Qwen2.5-32B
pipeline_tag: text-generation
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
---
# DAPO-Qwen-32B

## Introduction

This repository contains the **DAPO-Qwen-32B** model, which is trained based on Qwen2.5-32B using the **DAPO** algorithm.

## Inference

```python
import torch
from transformers import AutoTokenizer
from vllm import SamplingParams, LLM

examples = [
    {
        "question": "Solve the following math problem step by step. The last line of your response should be of the form Answer: $Answer (without quotes) where $Answer is the answer to the problem.\n\nFind the largest possible real part of \\[(75+117i)z+\\frac{96+144i}{z}\\]where $z$ is a complex number with $|z|=4$.\n\nRemember to put your answer on its own line after \"Answer:\".",
        "answer": "540"
    },
    {
        "question": "Solve the following math problem step by step. The last line of your response should be of the form Answer: $Answer (without quotes) where $Answer is the answer to the problem.\n\nEvery morning Aya goes for a $9$-kilometer-long walk and stops at a coffee shop afterwards. When she walks at a constant speed of $s$ kilometers per hour, the walk takes her 4 hours, including $t$ minutes spent in the coffee shop. When she walks $s+2$ kilometers per hour, the walk takes her 2 hours and 24 minutes, including $t$ minutes spent in the coffee shop. Suppose Aya walks at $s+\\frac{1}{2}$ kilometers per hour. Find the number of minutes the walk takes her, including the $t$ minutes spent in the coffee shop.\n\nRemember to put your answer on its own line after \"Answer:\".",
        "answer": "204"
    },
    {
        "question": "Solve the following math problem step by step. The last line of your response should be of the form Answer: $Answer (without quotes) where $Answer is the answer to the problem.\n\nLet $\\mathcal{B}$ be the set of rectangular boxes with surface area $54$ and volume $23$. Let $r$ be the radius of the smallest sphere that can contain each of the rectangular boxes that are elements of $\\mathcal{B}$. The value of $r^2$ can be written as $\\frac{p}{q}$, where $p$ and $q$ are relatively prime positive integers. Find $p+q$.\n\nRemember to put your answer on its own line after \"Answer:\".",
        "answer": "721"
    }
]


def main():
    model = "BytedTsinghua-SIA/DAPO-Qwen-32B"

    tokenzier = AutoTokenizer.from_pretrained(model)

    llm = LLM(
        model=model,
        dtype=torch.bfloat16,
        tensor_parallel_size=8,
        gpu_memory_utilization=0.95
    )

    sampling_params = SamplingParams(
        temperature=1.0,
        top_p=0.7,
        max_tokens=20480
    )

    for example in examples:
        question = example["question"]
        answer = example["answer"]
        output = llm.generate(
                    prompts=tokenzier.apply_chat_template(conversation=[{"content": question, "role": "user"}],
                                                          add_generation_prompt=True,
                                                          tokenize=False),
                    sampling_params=sampling_params
                )
        print(f"***QUESTION***:\n{question}\n***GROUND TRUTH***:\n{answer}\n***MODEL OUTPUT***:\n{output[0].outputs[0].text}\n")
        print("-"*100)

if __name__ == "__main__":
    main()
```

## Training & Performance
Please refer to the following resources for more information:

- [DAPO Paper](https://arxiv.org/abs/2503.14476).
- [DAPO Github Repository](https://github.com/BytedTsinghua-SIA/DAPO).
- [DAPO Blog](https://dapo-sia.github.io/).

## Citation

```
@misc{yu2025dapoopensourcellmreinforcement,
      title={DAPO: An Open-Source LLM Reinforcement Learning System at Scale}, 
      author={Qiying Yu and Zheng Zhang and Ruofei Zhu and Yufeng Yuan and Xiaochen Zuo and Yu Yue and Tiantian Fan and Gaohong Liu and Lingjun Liu and Xin Liu and Haibin Lin and Zhiqi Lin and Bole Ma and Guangming Sheng and Yuxuan Tong and Chi Zhang and Mofan Zhang and Wang Zhang and Hang Zhu and Jinhua Zhu and Jiaze Chen and Jiangjie Chen and Chengyi Wang and Hongli Yu and Weinan Dai and Yuxuan Song and Xiangpeng Wei and Hao Zhou and Jingjing Liu and Wei-Ying Ma and Ya-Qin Zhang and Lin Yan and Mu Qiao and Yonghui Wu and Mingxuan Wang},
      year={2025},
      eprint={2503.14476},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2503.14476}, 
}
```