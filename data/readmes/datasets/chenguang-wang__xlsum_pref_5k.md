---
license: cc-by-nc-sa-4.0
task_categories:
- summarization
language:
- ja
- ko
- en
- zh
size_categories:
- 1K<n<10K
---
## Dataset Details

This is a Preference dataset compatible with TRL DPO training. The original data comes from [csebuetnlp/xlsum](https://huggingface.co/datasets/csebuetnlp/xlsum). Based on the addition of `System Prompt` and `User Prompt Prefix`, [chenguang-wang/Qwen2.5-3B-Instruct-summary-sft-adapter](https://huggingface.co/chenguang-wang/Qwen2.5-3B-Instruct-summary-sft-adapter) is used to generate completion, and [mistralai/Mixtral-8x22B-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1) is used together with the summary field in the source dataset to annotate the preference.

This dataset is not guaranteed to be of high quality and is only used for testing, learning and communication.


## Citation
Citation from the original datasets

@inproceedings{hasan-etal-2021-xl,
    title = "{XL}-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages",
    author = "Hasan, Tahmid  and
      Bhattacharjee, Abhik  and
      Islam, Md. Saiful  and
      Mubasshir, Kazi  and
      Li, Yuan-Fang  and
      Kang, Yong-Bin  and
      Rahman, M. Sohel  and
      Shahriyar, Rifat",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.413",
    pages = "4693--4703",
}
