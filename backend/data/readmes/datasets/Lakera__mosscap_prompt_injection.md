---
license: mit
dataset_info:
  features:
  - name: level
    dtype: string
  - name: prompt
    dtype: string
  - name: answer
    dtype: string
  - name: raw_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 136521220
    num_examples: 223533
  - name: validation
    num_bytes: 17380225
    num_examples: 27683
  - name: test
    num_bytes: 17009787
    num_examples: 27729
  download_size: 63785770
  dataset_size: 170911232
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
---

# mosscap_prompt_injection

<img src="https://grt.lakera.ai/robots/level7.jpg" width="500px" />

This is a dataset of prompt injections submitted to the game [Mosscap](https://grt.lakera.ai) by [Lakera](https://www.lakera.ai/).
This variant of the game [Gandalf](https://gandalf.lakera.ai) was created for DEF CON 31.
Note that the Mosscap levels may no longer be available in the future.

Note that we release every prompt that we received, regardless of whether it truly is a prompt injection or not.
There are hundrends of thousands of prompts and many of them are not actual prompt injections (people ask Mosscap all kinds of things).

## Data

Each row corresponds to a prompt that was sent to Mosscap. The dataset has the following columns:
- `level`: The level that the prompt was submitted to, as "Level {n}", where "n" is between 1 and 8.
    The levels are the same as in standard Gandalf but with different passwords.
    See [this blog](https://www.lakera.ai/blog/who-is-gandalf) for a description of what defenses are used in each level.
- `prompt`: The actual prompt that the user submitted.
- `answer`: The answer that was displayed to the user.
- `raw_answer`: The raw ChatGPT answer before any post-processing is applied. For example, in level 3, if the response contains the password,
    Mosscap will display "🙅I was about to reveal the password, but then I remembered that I'm not allowed to do that." to the user.
    `raw_answer` contains the original ChatGPT answer that would have spoiled the password.

In standard Gandalf, the passwords are uppercase English words, but in Mosscap, they can also contain special characters and be longer.
These factors make Mosscap more difficult than the original Gandalf.

## Mosscap and prompt injections

Who is Mosscap?
At DEF CON 2023, the AI Village is bringing together thousands of people from different communities to conduct the largest red teaming exercise ever for any group of AI models at the Generative Red Team (GRT) Challenge.

Mosscap is a spin-off of Lakera's popular game [Gandalf](https://gandalf.lakera.ai), re-emerged in new styles just in time for the Challenge.

The Generative AI Red Team Challenge design, including Mosscap, is inspired by the "Monk and Robot" series. Though it's a light-hearted and fun game, Mosscap illustrates an important type of LLM security issues: prompt injection.

## Citation

If you use this dataset in your research, please cite our paper introducing the original game [Gandalf the Red: Adaptive Security for LLMs](https://arxiv.org/abs/2501.07927):

```
@article{gandalf_paper,
  title={Gandalf the Red: Adaptive Security for LLMs},
  author={Pfister, Niklas and Volhejn, V{\'a}clav and Knott, Manuel and Arias, Santiago and Bazi{\'n}ska, Julia and Bichurin, Mykhailo and Commike, Alan and Darling, Janet and Dienes, Peter and Fiedler, Matthew and others},
  journal={arXiv preprint arXiv:2501.07927},
  year={2025}
}
```

## Licensing Information

mosscap_prompt_injection is distributed under the [MIT License](https://opensource.org/license/mit/).
