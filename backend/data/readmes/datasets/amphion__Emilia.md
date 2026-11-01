---
license: cc-by-nc-4.0
task_categories:
- text-to-speech
language:
- zh
- en
- ja
- ko
- de
- fr
pretty_name: Emilia
extra_gated_prompt: >-
  Terms of Access: The researcher has requested permission to use the Emilia dataset and the Emilia-Pipe preprocessing pipeline. 
  In exchange for such permission, the researcher hereby agrees to the following terms and conditions:

  1. The researcher shall use the dataset ONLY for non-commercial research and educational purposes.

  2. The authors make no representations or warranties regarding the dataset, 
    including but not limited to warranties of non-infringement or fitness for a particular purpose.

  3. The researcher accepts full responsibility for their use of the dataset and shall defend and indemnify the authors of Emilia, 
    including their employees, trustees, officers, and agents, against any and all claims arising from the researcher's use of the dataset, 
    including but not limited to the researcher's use of any copies of copyrighted content that they may create from the dataset.

  4. The researcher may provide research associates and colleagues with access to the dataset,
    provided that they first agree to be bound by these terms and conditions.
    
  5. The authors reserve the right to terminate the researcher's access to the dataset at any time.

  6. If the researcher is employed by a for-profit, commercial entity, 
  the researcher's employer shall also be bound by these terms and conditions, 
  and the researcher hereby represents that they are fully authorized to enter into this agreement on behalf of such employer.
extra_gated_fields:
  Name: text
  Email: text
  Affiliation: text
  Position: text
---

# Emilia: An Extensive, Multilingual, and Diverse Speech Dataset for Large-Scale Speech Generation

The Emilia dataset is the first open-source, multilingual, in-the-wild dataset designed for speech generation. It offers over 101,000 hours of high-quality speech data across six languages: Chinese (zh), English (en), Japanese (ja), Korean (ko), German (de), and French (fr). The dataset includes various speaking styles and their corresponding transcriptions.

## README 🚧🚧🚧🚧🚧🚧

**This repository contains only the URLs for Emilia's data sources.**

**If you're interested in using the processed data—the Emilia Dataset itself—please visit [this link](https://huggingface.co/datasets/amphion/Emilia-Dataset).**

## Meta Info

<image style="width: 500px; height: 500px;" src="https://huggingface.co/datasets/amphion/Emilia/resolve/main/emilia_source_url_category_distribution.png"/>

## Dataset Usage

To reconstruct the Emilia dataset, you can download the raw audio files from the [provided URL list](https://huggingface.co/datasets/amphion/Emilia) and use our open-source [Emilia-Pipe](https://github.com/open-mmlab/Amphion/tree/main/preprocessors/Emilia) preprocessing pipeline to process the raw data and rebuild the dataset. Additionally, users can employ Emilia-Pipe to preprocess their own raw speech data to meet specific needs. By open-sourcing the Emilia-Pipe code, we aim to empower the speech community to collaborate on large-scale speech generation research.


*Please note that Emilia does not own the copyright to the audio files; the copyright remains with the original owners of the videos or audio. Users are permitted to use this dataset only for non-commercial purposes under the CC BY-NC-4.0 license.*


## Reference
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

