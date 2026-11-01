---
language:
- en
- ko
license: cc-by-4.0
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: instruction
    dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 34213211
    num_examples: 24926
  download_size: 16662523
  dataset_size: 34213211
---

# KOpenPlatypus: Korean Translation dataset about Open-Platypus

## Korean Translation Method

I use [DeepL-pro-API](https://www.deepl.com/ko/pro/change-plan?cta=header-pro#single) and selenium. 
It takes about 140h times.  
+) 데이터셋 이용하셔서 모델이나 데이터셋을 만드실 때, 간단한 출처 표기를 해주신다면 연구에 큰 도움이 됩니다😭😭

## Korean Translation post-processing
![image](./typeA.png)
![image](./typeB.png)
![image](./typeE.png)
![image](./typeD.png)
![image](./typeC.png)

And also, applying post-processing. See below lists. (*약 2000개 이상의 코드 관련 데이터를 수작업으로 수정함)
1. 코드와 주석은 그대로 유지하고, 설명 부분만 한국어로 수정
2. 1번과 더불어서, Python, Java, Cpp, xml 등등 결과들은 전부 기존의 데이터 형태로 최대한 보존
3. 단일 숫자와 영어는 본래의 결과 그대로 가져옴
4. DeepL Pro 번역 결과 중 미완성 변역 결과 직접 수정(예를 들면, '[...]'가 포함되어 있음)
5. DeepL Pro 번역 결과가 본래의 데이터에 비해 글자수가 50% 이하로 낮으면, 번역 결과 수정
6. 번역하고자 하는 글자수가 1500자 이상일 경우, API로 변경해서 번역
7. `고유명사`는 최대한 유지함  

- 95% 이상의 번역 오류는 전부 고친 것으로 생각됨.   
- 약 144h 정도 번역 작업을 진행함. (72h/72h; Translation/Post-processing)  

## Introdcution

This dataset is focused on improving LLM logical reasoning skills and was used to train the Platypus2 models. It is comprised of the following datasets, which were filtered using keyword search and then Sentence Transformers to remove questions with a similarity above 80%:

| Dataset Name                                                 | License Type |
|--------------------------------------------------------------|--------------|
| [PRM800K](https://github.com/openai/prm800k)                 | MIT          |
| [ScienceQA](https://github.com/lupantech/ScienceQA) | [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)    |
| [SciBench](https://github.com/mandyyyyii/scibench)    | MIT      |
| [ReClor](https://whyu.me/reclor/)                            | Non-commercial      |
| [TheoremQA](https://huggingface.co/datasets/wenhu/TheoremQA) | MIT      |
| [`nuprl/leetcode-solutions-python-testgen-gpt4`](https://huggingface.co/datasets/nuprl/leetcode-solutions-python-testgen-gpt4/viewer/nuprl--leetcode-solutions-python-testgen-gpt4/train?p=1) | None listed |
| [`jondurbin/airoboros-gpt4-1.4.1`](https://huggingface.co/datasets/jondurbin/airoboros-gpt4-1.4.1) | other |
| [`TigerResearch/tigerbot-kaggle-leetcodesolutions-en-2k`](https://huggingface.co/datasets/TigerResearch/tigerbot-kaggle-leetcodesolutions-en-2k/viewer/TigerResearch--tigerbot-kaggle-leetcodesolutions-en-2k/train?p=2) | apache-2.0 |
| [openbookQA](https://huggingface.co/datasets/openbookqa/viewer/additional/train?row=35) | apache-2.0      |
| [ARB](https://arb.duckai.org)                                | MIT      |
| [`timdettmers/openassistant-guanaco`](https://huggingface.co/datasets/timdettmers/openassistant-guanaco)                                | apache-2.0      |

## Data Contamination Check

We've removed approximately 200 questions that appear in the Hugging Face benchmark test sets. Please see our [paper](https://arxiv.org/abs/2308.07317) and [project webpage](https://platypus-llm.github.io) for additional information. 

## Model Info

Please see models at [`garage-bAInd`](https://huggingface.co/garage-bAInd).

## Training and filtering code

Please see the [Platypus GitHub repo](https://github.com/arielnlee/Platypus).

## Citations
```bibtex
@article{platypus2023,
    title={Platypus: Quick, Cheap, and Powerful Refinement of LLMs}, 
    author={Ariel N. Lee and Cole J. Hunter and Nataniel Ruiz},
    booktitle={arXiv preprint arxiv:2308.07317},
    year={2023}
}
```
```bibtex
@article{lightman2023lets,
    title={Let's Verify Step by Step}, 
    author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
    journal={preprint arXiv:2305.20050},
    year={2023}
}
```
```bibtex
@inproceedings{lu2022learn,
    title={Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering},
    author={Lu, Pan and Mishra, Swaroop and Xia, Tony and Qiu, Liang and Chang, Kai-Wei and Zhu, Song-Chun and Tafjord, Oyvind and Clark, Peter and Ashwin Kalyan},
    booktitle={The 36th Conference on Neural Information Processing Systems (NeurIPS)},
    year={2022}
}
```
```bibtex
@misc{wang2023scibench,
    title={SciBench: Evaluating College-Level Scientific Problem-Solving Abilities of Large Language Models}, 
    author={Xiaoxuan Wang and Ziniu Hu and Pan Lu and Yanqiao Zhu and Jieyu Zhang and Satyen Subramaniam and Arjun R. Loomba and Shichang Zhang and Yizhou Sun and Wei Wang},
    year={2023},
    arXiv eprint 2307.10635
}
```
```bibtex
@inproceedings{yu2020reclor,
    author = {Yu, Weihao and Jiang, Zihang and Dong, Yanfei and Feng, Jiashi},
    title = {ReClor: A Reading Comprehension Dataset Requiring Logical Reasoning},
    booktitle = {International Conference on Learning Representations (ICLR)},
    month = {April},
    year = {2020}
}
```
```bibtex
@article{chen2023theoremqa,
    title={TheoremQA: A Theorem-driven Question Answering dataset},
    author={Chen, Wenhu and Ming Yin, Max Ku, Elaine Wan, Xueguang Ma, Jianyu Xu, Tony Xia, Xinyi Wang, Pan Lu},
    journal={preprint arXiv:2305.12524},
    year={2023}
}
```
```bibtex
@inproceedings{OpenBookQA2018,
     title={Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering},
     author={Todor Mihaylov and Peter Clark and Tushar Khot and Ashish Sabharwal},
     booktitle={EMNLP},
     year={2018}
}
```
```bibtex
@misc{sawada2023arb,
    title={ARB: Advanced Reasoning Benchmark for Large Language Models}, 
    author={Tomohiro Sawada and Daniel Paleka and Alexander Havrilla and Pranav Tadepalli and Paula Vidas and Alexander Kranias and John J. Nay and Kshitij Gupta and Aran Komatsuzaki},
    arXiv eprint 2307.13692,
    year={2023}
}
```