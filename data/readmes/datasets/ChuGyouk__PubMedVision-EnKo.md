---
license: apache-2.0
task_categories:
  - question-answering
  - text-generation
language:
  - en
  - ko
tags:
  - Vision
  - medical
  - biology
size_categories:
  - 1M<n<10M
configs:
  - config_name: PubMedVision_Alignment_VQA
    data_files: PubMedVision_Alignment_VQA_trans.json
  - config_name: PubMedVision_InstructionTuning_VQA
    data_files: PubMedVision_InstructionTuning_VQA_trans.json
---

## Informations
- This is the Korean translation of [FreedomIntelligence/PubMedVision](https://huggingface.co/datasets/FreedomIntelligence/PubMedVision). The translation was primarily generated using the ['solar-pro-241126'](https://www.upstage.ai/blog/en/solar-pro) model, with occasional manual assistance from the 'Gemini 2.0 Flash Experimental' model and the 'Gemini experimental 1206' model.
- An evaluation of the translation quality ("llm-as-a-judge") will be coming soon.

## News
- [2024/07/01]: We add annotations for 'body_part' and 'modality' of images, utilizing the [HuatuoGPT-Vision-7B](https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B) model.

## PubMedVision
PubMedVision is a large-scale medical VQA dataset. We extracted high-quality image-text pairs from PubMed and used GPT-4V to reformat them to enhance their quality.

PubMedVision significantly improves the multimodal capabilities of MLLMs in the medical field. For more details, refer to our [paper](https://arxiv.org/abs/2406.19280) and [github](https://github.com/FreedomIntelligence/HuatuoGPT-Vision).

## Data Volume
PubMedVision contains 1.3 million medical VQAs, divided into Alignment VQA and Instruction Tuning VQA:
| Data                            | # Data     |
| ---------- | ---------- |
| PubMedVision_Alignment_VQA      | 647,031    |
| PubMedVision_InstructionTuning_VQA | 647,031    |
| **Total**                       | **1,294,062** |

## Image Data
`images_*.zip` contains the compressed image data. You can unzip these images using the following code:
```bash
for ((i=0; i<20; i++))
do
    unzip -j images_$i.zip -d images/ & # wait patiently, it takes a while...
done
```

## Citation

If you find our data useful, please consider citing our work! We are FreedomIntelligence from [Shenzhen Research Institute of Big Data](http://sribd.cn/en) and [The Chinese University of Hong Kong, Shenzhen](https://sds.cuhk.edu.cn/en)
```
@misc{chen2024huatuogptvisioninjectingmedicalvisual,
      title={HuatuoGPT-Vision, Towards Injecting Medical Visual Knowledge into Multimodal LLMs at Scale}, 
      author={Junying Chen and Ruyi Ouyang and Anningzhe Gao and Shunian Chen and Guiming Hardy Chen and Xidong Wang and Ruifei Zhang and Zhenyang Cai and Ke Ji and Guangjun Yu and Xiang Wan and Benyou Wang},
      year={2024},
      eprint={2406.19280},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2406.19280}, 
}
```
