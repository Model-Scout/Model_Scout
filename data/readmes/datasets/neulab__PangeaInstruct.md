---
license: apache-2.0
task_categories:
- visual-question-answering
- question-answering
language:
- am
- ar
- bg
- bn
- cs
- de
- el
- en
- es
- fa
- fr
- ga
- hi
- id
- ig
- it
- iw
- ja
- jv
- ko
- nl
- mn
- ms
- no
- pl
- pt
- ro
- ru
- si
- su
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
tags:
- multilingual
- multimodal
pretty_name: PangeaIns
size_categories:
- 1M<n<10M
viewer: false
---
# PangeaInstruct

[Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://neulab.github.io/Pangea/)

🇪🇹 🇸🇦 🇧🇬 🇧🇩 🇨🇿 🇩🇪 🇬🇷 🇬🇧 🇺🇸 🇪🇸 🇮🇷 🇫🇷 🇮🇪 🇮🇳 🇮🇩 🇳🇬 🇮🇹 🇮🇱 🇯🇵 🇮🇩 🇰🇷 🇳🇱 🇲🇳 🇲🇾 🇳🇴 🇵🇱 🇵🇹 🇧🇷 🇷🇴 🇷🇺 🇱🇰 🇮🇩 🇰🇪 🇹🇿 🇱🇰 🇮🇳 🇮🇳 🇹🇭 🇹🇷 🇺🇦 🇵🇰 🇮🇳 🇻🇳 🇨🇳 🇹🇼

[🏠 Homepage](https://neulab.github.io/Pangea/) | [🤖 Pangea-7B](https://huggingface.co/neulab/Pangea-7B) | [📊 PangeaIns](https://huggingface.co/datasets/neulab/PangeaInstruct) | [🧪 PangeaBench](https://huggingface.co/collections/neulab/pangea-6713c3b0d78a453906eb2ed8) | [💻 Github](https://github.com/neulab/Pangea/tree/main) | [📄 Arxiv](https://arxiv.org/abs/2410.16153) | [📕 PDF](https://arxiv.org/pdf/2410.16153) | [🖥️ Demo](https://huggingface.co/spaces/neulab/Pangea)


<img src="https://cdn-uploads.huggingface.co/production/uploads/6230d750d93e84e233882dbc/ZjVTKnIsyshWpo-PWg9gM.png" alt="description" style="width:300px;">

This README provides comprehensive details on the PangeaIns dataset, which was utilized during the instruction tuning phase for [Pangea-7B](https://huggingface.co/neulab/Pangea-7B).

## Description of PangeaIns

PangeaIns is a 6M multilingual multicultural multimodal instruction tuning dataset spanning 39 languages.

## PangeaIns Data Source
PangeaIns data path: PangeaIns.json (# samples: 6450624)
PangeaIns data source:
| Dataset Name                | Dataset Path                                                 | # Samples |
|-----------------------------|--------------------------------------------------------------|-----------|
| ALLAVA-4V                   | general/ALLAVA-4V/data.json                                  | 621327    |
| allava_vflan                | general/allava_vflan/data.json                               | 325122    |
| Cambrian737k                | general/cambrian/data.json                                   | 736934    |
| ChartQA                     | doc+chart/ChartQA/data.json                                  | 28299     |
| Code-Feedback               | text-only/Code-Feedback/data.json                            | 20000     |
| doc-vqa                     | doc+chart/doc-vqa/data.json                                  | 9665      |
| gpt4v-dataset               | caption/gpt4v-dataset/data.json                              | 10822     |
| GQA-ru                      | general/GQA-ru/data.json                                     | 40000     |
| laion-1M-qa                 | cultural/laion-multi-1M/captions-1M-generated-qas-llava.json | 1028791   |
| laion-300K-caption          | cultural/laion-multi-1M/laion-300K-caption-llava.json        | 300000    |
| llava-en-zh-300k            | general/llava-en-zh-300k/data.json                           | 50000     |
| LLaVA-Finetune              | cultural/laion-cultural-150k/laion-cultural-150k.json        | 151072    |
| Llava-JP-Instruct-108K      | general/LLaVA-JP-Instruct-108K/data.json                     | 108855    |
| llava-med-zh-instruct-60K   | general/llava-med-zh-instruct-60k/data.json                  | 56649     |
| LLaVA-NeXt                  | general/LLaVA-NeXt-Data/data.json                            | 119853    |
| LVIS-Instruct4V             | general/LVIS-Instruct4V/data.json                            | 222697    |
| MTVQA                       | general/MTVQA/data.json                                      | 6678      |
| nvlr2-llava                 | general/nvlr2-llava/data.json                                | 86373     |
| NuminaMath-CoT              | text-only/NuminaMath-CoT/data.json                           | 100000    |
| OpenHermes-2.5              | text-only/Openhermes-2.5/data.json                           | 399900    |
| palo_multilingual_dataset   | general/palo_multilingual_dataset/urdu-100k.json             | 99992     |
| ShareGPT-4o                 | general/ShareGPT-4o/data.json                                | 57289     |
| ShareGPT4V                  | general/ShareGPT4V/data.json                                 | 91021     |
| STAIR-Captions              | caption/STAIR-Captions/data.json                             | 82783     |
| table-vqa                   | doc+chart/table-vqa/data.json                                | 16408     |
| Viet-Doc-VQA                | doc+chart/Viet-Doc-VQA/data.json                             | 12000     |
| Viet-DOC-VQA-II             | doc+chart/Viet-DOC-VQA-II/data.json                          | 14998     |
| Viet-OCR-VQA                | doc+chart/Viet-OCR-VQA/data.json                             | 30000     |
| Viet-ShareGPT-4o-Text-VQA   | general/Viet-ShareGPT-4o-Text-VQA/data.json                  | 42678     |
| webui_multilingual_ocr      | ocr/webui_multilingual_ocr/data.json                             | 300000    |
| translation                 | translation/data.json                                        | 1280328   |


## Applications

PangeaIns was designed specifically for training the Pangea-7B model.

### Code Instructions

The dataset follows the LLaVA data format. To retrieve all files from PangeaIns, use the following script:

```python
from huggingface_hub import HfApi, hf_hub_download
import json

# Initialize the API client
api = HfApi()
dataset_name = "neulab/PangeaInstruct"

# Retrieve and download all files in the dataset
files = api.list_repo_files(repo_id=dataset_name, repo_type="dataset")

for file in files:
    hf_hub_download(repo_id=dataset_name, filename=file, repo_type="dataset")
    print(f"File downloaded: {file}")

# Load the complete PangeaIns dataset
with open('PangeaIns.json') as f:
  data = json.load(f)
```

Please note that image data is provided in compressed formats such as `.tar` or `.zip`. After downloading, you may need to extract these files to access the images.
For images.tar files, you could untar them by running 
```bash
tar -xvf images.tar
```

For images.zip files, you could unzip them by running 
```bash
unzip images.zip
```

For some large tar files, we uploaded tar files splitted using the split command, such as `split -n 4 -d images.tar part_`.
For example, in the `cultural/laion-multi-1M` subset, we splitted the images.tar file into 4 parts, `part_00`, `part_01`, `part_02`, and `part_03`.
In such cases, you would need to first combine the splits and then extract the tar file.

```bash
cat part_* > images.tar
tar -xvf images.tar
```

Each subset within the PangeaIns dataset (e.g., ChartQA) contains a `.json` file for metadata and a corresponding `.tar/.zip` file for the images.

## Citing the Dataset

**BibTeX Citation:**

```
@article{yue2024pangeafullyopenmultilingual,
  title={Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages},
  author={Xiang Yue and Yueqi Song and Akari Asai and Seungone Kim and Jean de Dieu Nyandwi and Simran Khanuja and Anjali Kantharuban and Lintang Sutawika and Sathyanarayanan Ramamoorthy and Graham Neubig},
  year={2024},
  journal={arXiv preprint arXiv:2410.16153},
  url={https://arxiv.org/abs/2410.16153}
}
```

## Contact

Corresponding to: {xyue2,yueqis,gneubig}@cs.cmu.edu