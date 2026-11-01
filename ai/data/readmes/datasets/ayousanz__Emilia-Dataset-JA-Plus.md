---
license: cc-by-nc-4.0
task_categories:
- text-to-speech
- automatic-speech-recognition
language:
- zh
- en
- ja
- fr
- de
- ko
pretty_name: Emilia
size_categories:
- 10M<n<100M
extra_gated_prompt: >-
  Terms of Access: The researcher has requested permission to use the Emilia
  dataset and the Emilia-Pipe preprocessing pipeline.  In exchange for such
  permission, the researcher hereby agrees to the following terms and
  conditions:

  1. The researcher shall use the dataset ONLY for non-commercial research and
  educational purposes.

  2. The authors make no representations or warranties regarding the dataset, 
    including but not limited to warranties of non-infringement or fitness for a particular purpose.

  3. The researcher accepts full responsibility for their use of the dataset and
  shall defend and indemnify the authors of Emilia, 
    including their employees, trustees, officers, and agents, against any and all claims arising from the researcher's use of the dataset, 
    including but not limited to the researcher's use of any copies of copyrighted content that they may create from the dataset.

  4. The researcher may provide research associates and colleagues with access
  to the dataset,
    provided that they first agree to be bound by these terms and conditions.
    
  5. The authors reserve the right to terminate the researcher's access to the
  dataset at any time.

  6. If the researcher is employed by a for-profit, commercial entity,  the
  researcher's employer shall also be bound by these terms and conditions,  and
  the researcher hereby represents that they are fully authorized to enter into
  this agreement on behalf of such employer.
extra_gated_fields:
  Name: text
  Email: text
  Affiliation: text
  Position: text
  Your Supervisor/manager/director: text
  I agree to the Terms of Access: checkbox
---

# Emilia: An Extensive, Multilingual, and Diverse Speech Dataset for Large-Scale Speech Generation
<!-- [![arXiv](https://img.shields.io/badge/arXiv-Paper-COLOR.svg)](https://arxiv.org/abs/2407.05361)  [![hf](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Dataset-yellow)](https://huggingface.co/datasets/amphion/Emilia-Dataset)  [![OpenDataLab](https://img.shields.io/badge/OpenDataLab-Dataset-blue)](https://opendatalab.com/Amphion/Emilia)  [![GitHub](https://img.shields.io/badge/GitHub-Repo-green)](https://github.com/open-mmlab/Amphion/tree/main/preprocessors/Emilia)  [![demo](https://img.shields.io/badge/WebPage-Demo-red)](https://emilia-dataset.github.io/Emilia-Demo-Page/)
 -->
This is the official repository 👑 for the **Emilia** dataset and the source code for the **Emilia-Pipe** speech data preprocessing pipeline. 

<div align="center"><img width="500px" src="https://github.com/user-attachments/assets/b1c1a1f8-3149-4f96-8eb4-af470152a9b7" /></div>

## News 🔥
- **2024/08/28**: Welcome to join Amphion's [Discord channel](https://discord.com/invite/ZxxREr3Y) to stay connected and engage with our community!
- **2024/08/27**: *The Emilia dataset is now publicly available!* Discover the most extensive and diverse speech generation dataset with 101k hours of in-the-wild speech data now at [HuggingFace](https://huggingface.co/datasets/amphion/Emilia-Dataset) or [OpenDataLab](https://opendatalab.com/Amphion/Emilia)! 👑👑👑
- **2024/07/08**: Our preprint [paper](https://arxiv.org/abs/2407.05361) is now available! 🔥🔥🔥
- **2024/07/03**: We welcome everyone to check our [homepage](https://emilia-dataset.github.io/Emilia-Demo-Page/) for our brief introduction for Emilia dataset and our demos!
- **2024/07/01**: We release of Emilia and Emilia-Pipe! We welcome everyone to explore it on our [GitHub](https://github.com/open-mmlab/Amphion/tree/main/preprocessors/Emilia)! 🎉🎉🎉

## Emilia Overview ⭐️
The **Emilia** dataset is a comprehensive, multilingual dataset with the following features:
- containing over *101k* hours of speech data;
- covering six different languages: *English (En), Chinese (Zh), German (De), French (Fr), Japanese (Ja), and Korean (Ko)*;
- containing diverse speech data with *various speaking styles* from diverse video platforms and podcasts on the Internet, covering various content genres such as talk shows, interviews, debates, sports commentary, and audiobooks.

The table below provides the duration statistics for each language in the dataset.

|   Language  | Duration (hours) |
|:-----------:|:----------------:|
|   English   |     46,828       |
|   Chinese   |     49,922       |
|   German    |     1,590        |
|   French    |     1,381        |
|   Japanese  |     1,715        |
|   Korean    |      217         |


The **Emilia-Pipe** is the first open-source preprocessing pipeline designed to transform raw, in-the-wild speech data into high-quality training data with annotations for speech generation. This pipeline can process one hour of raw audio into model-ready data in just a few minutes, requiring only the raw speech data. 

Detailed descriptions for the Emilia and Emilia-Pipe can be found in our [paper](https://arxiv.org/abs/2407.05361).

## Emilia Dataset Usage 📖
Emilia is publicly available at [HuggingFace](https://huggingface.co/datasets/amphion/Emilia-Dataset).

If you are from mainland China or having a connecting issue with HuggingFace, you can also download Emilia from [OpenDataLab](https://opendatalab.com/Amphion/Emilia).

- To download from HuggingFace:

  1.  Gain access to the dataset and get the HF access token from: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
  2.  Install dependencies and login HF:
       - Install Python
       - Run `pip install librosa soundfile datasets huggingface_hub[cli]`
       - Login by `huggingface-cli login` and paste the HF access token. Check [here](https://huggingface.co/docs/huggingface_hub/guides/cli#huggingface-cli-login) for details.
  3.  Use following code to load Emilia:
    ```py
    from datasets import load_dataset
    dataset = load_dataset("amphion/Emilia-Dataset", streaming=True)
    print(dataset)
    print(next(iter(dataset['train'])))
    ```

- To download from OpenDataLab (i.e., OpenXLab), please follow the guidance [here](https://speechteam.feishu.cn/wiki/PC8Ew5igviqBiJkElMJcJxNonJc) to gain access.

**ENJOY USING EMILIA!!!** 🔥

### Use cases

If you want to load a subset of Emilia, e.g., only language `DE`, you can use the following code:

```py
from datasets import load_dataset
path = "DE/*.tar"
dataset = load_dataset("amphion/Emilia-Dataset", data_files={"de": path}, split="de", streaming=True)
print(dataset) # here should only shows 90 n_shards instead of 2360
print(next(iter(dataset['train'])))
```

If you want to download all files to your local before using Emilia, remove the `streaming=True` argument:

```py
from datasets import load_dataset
dataset = load_dataset("amphion/Emilia-Dataset") # prepare 2.4TB space to store Emilia
print(dataset)
```


### Re-build or Processing your own data

If you wish to re-build Emilia from scratch, you may download the raw audio files from the [provided URL list](https://huggingface.co/datasets/amphion/Emilia) and use our open-source [Emilia-Pipe](https://github.com/open-mmlab/Amphion/tree/main/preprocessors/Emilia) preprocessing pipeline to preprocess the raw data. Additionally, users can easily use Emilia-Pipe to preprocess their own raw speech data for custom needs. By open-sourcing the Emilia-Pipe code, we aim to enable the speech community to collaborate on large-scale speech generation research.

### Notes

*Please note that Emilia does not own the copyright to the audio files; the copyright remains with the original owners of the videos or audio. Users are permitted to use this dataset only for non-commercial purposes under the CC BY-NC-4.0 license.*

## Emilia Dataset Structure ⛪️

### Structure on HuggingFace

On HuggingFace, Emilia is now formatted as [WebDataset](https://github.com/webdataset/webdataset).

Each audio is tared with a corresponding JSON file (having the same prefix filename) within 2360 tar files.

By utilizing WebDataset, you can easily stream audio data, which is magnitude faster than reading separate data files one by one.

Read the *Emilia Dataset Usage 📖* part for a detailed usage guide.

Learn more about WebDataset [here](https://huggingface.co/docs/hub/datasets-webdataset).

*PS: If you want to download the `OpenDataLab` format from HuggingFace, you can specify the `revision` argument to `fc71e07e8572f5f3be1dbd02ed3172a4d298f152`, [which](https://huggingface.co/datasets/amphion/Emilia-Dataset/tree/fc71e07e8572f5f3be1dbd02ed3172a4d298f152) is the old format.*


### Structure on OpenDataLab
On OpenDataLab, Emilia is formatted using the following structure.

Structure example:
```
|-- openemilia_all.tar.gz (all .JSONL files are gzipped with directory structure in this file)
|-- EN (114 batches)
|   |-- EN_B00000.jsonl
|   |-- EN_B00000 (= EN_B00000.tar.gz)
|   |   |-- EN_B00000_S00000
|   |   |   `-- mp3
|   |   |       |-- EN_B00000_S00000_W000000.mp3
|   |   |       `-- EN_B00000_S00000_W000001.mp3
|   |   |-- ...
|   |-- ...
|   |-- EN_B00113.jsonl
|   `-- EN_B00113
|-- ZH (92 batches)
|-- DE (9 batches)
|-- FR (10 batches)
|-- JA (7 batches)
|-- KO (4 batches)

```

JSONL files example:
```
{"id": "EN_B00000_S00000_W000000", "wav": "EN_B00000/EN_B00000_S00000/mp3/EN_B00000_S00000_W000000.mp3", "text": " You can help my mother and you- No. You didn't leave a bad situation back home to get caught up in another one here. What happened to you, Los Angeles?", "duration": 6.264, "speaker": "EN_B00000_S00000", "language": "en", "dnsmos": 3.2927}
{"id": "EN_B00000_S00000_W000001", "wav": "EN_B00000/EN_B00000_S00000/mp3/EN_B00000_S00000_W000001.mp3", "text": " Honda's gone, 20 squads done. X is gonna split us up and put us on different squads. The team's come and go, but 20 squad, can't believe it's ending.", "duration": 8.031, "speaker": "EN_B00000_S00000", "language": "en", "dnsmos": 3.0442}
```

 
## Reference 📖
If you use the Emilia dataset or the Emilia-Pipe pipeline, please cite the following papers:
```bibtex
@inproceedings{emilia,
    author={He, Haorui and Shang, Zengqiang and Wang, Chaoren and Li, Xuyuan and Gu, Yicheng and Hua, Hua and Liu, Liwei and Yang, Chen and Li, Jiaqi and Shi, Peiyang and Wang, Yuancheng and Chen, Kai and Zhang, Pengyuan and Wu, Zhizheng},
    title={Emilia: An Extensive, Multilingual, and Diverse Speech Dataset for Large-Scale Speech Generation},
    booktitle={Proc.~of SLT},
    year={2024}
}
```
```bibtex
@inproceedings{amphion,
    author={Zhang, Xueyao and Xue, Liumeng and Gu, Yicheng and Wang, Yuancheng and Li, Jiaqi and He, Haorui and Wang, Chaoren and Song, Ting and Chen, Xi and Fang, Zihao and Chen, Haopeng and Zhang, Junan and Tang, Tze Ying and Zou, Lexiao and Wang, Mingxuan and Han, Jun and Chen, Kai and Li, Haizhou and Wu, Zhizheng},
    title={Amphion: An Open-Source Audio, Music and Speech Generation Toolkit},
    booktitle={Proc.~of SLT},
    year={2024}
}
```