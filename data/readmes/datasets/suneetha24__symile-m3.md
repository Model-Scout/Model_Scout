---
license: cc-by-nc-sa-4.0
task_categories:
- zero-shot-classification
- zero-shot-image-classification
language:
- ar
- el
- en
- hi
- ja
- ko
- te
- th
- uk
- zh
tags:
- multimodal
- representation learning
- multilingual
pretty_name: Symile-M3
size_categories:
- 10M<n<100M
configs:
- config_name: symile-m3-10-l
  data_files:
  - split: train
    path: symile-m3-10-l/train-*
  - split: val
    path: symile-m3-10-l/val-*
  - split: test
    path: symile-m3-10-l/test-*
- config_name: symile-m3-10-m
  data_files:
  - split: train
    path: symile-m3-10-m/train-*
  - split: val
    path: symile-m3-10-m/val-*
  - split: test
    path: symile-m3-10-m/test-*
- config_name: symile-m3-10-s
  data_files:
  - split: train
    path: symile-m3-10-s/train-*
  - split: val
    path: symile-m3-10-s/val-*
  - split: test
    path: symile-m3-10-s/test-*
- config_name: symile-m3-10-xs
  data_files:
  - split: train
    path: symile-m3-10-xs/train-*
  - split: val
    path: symile-m3-10-xs/val-*
  - split: test
    path: symile-m3-10-xs/test-*
- config_name: symile-m3-2-l
  data_files:
  - split: train
    path: symile-m3-2-l/train-*
  - split: val
    path: symile-m3-2-l/val-*
  - split: test
    path: symile-m3-2-l/test-*
- config_name: symile-m3-2-m
  data_files:
  - split: train
    path: symile-m3-2-m/train-*
  - split: val
    path: symile-m3-2-m/val-*
  - split: test
    path: symile-m3-2-m/test-*
- config_name: symile-m3-2-s
  data_files:
  - split: train
    path: symile-m3-2-s/train-*
  - split: val
    path: symile-m3-2-s/val-*
  - split: test
    path: symile-m3-2-s/test-*
- config_name: symile-m3-2-xs
  data_files:
  - split: train
    path: symile-m3-2-xs/train-*
  - split: val
    path: symile-m3-2-xs/val-*
  - split: test
    path: symile-m3-2-xs/test-*
- config_name: symile-m3-5-l
  data_files:
  - split: train
    path: symile-m3-5-l/train-*
  - split: val
    path: symile-m3-5-l/val-*
  - split: test
    path: symile-m3-5-l/test-*
- config_name: symile-m3-5-m
  data_files:
  - split: train
    path: symile-m3-5-m/train-*
  - split: val
    path: symile-m3-5-m/val-*
  - split: test
    path: symile-m3-5-m/test-*
- config_name: symile-m3-5-s
  data_files:
  - split: train
    path: symile-m3-5-s/train-*
  - split: val
    path: symile-m3-5-s/val-*
  - split: test
    path: symile-m3-5-s/test-*
- config_name: symile-m3-5-xs
  data_files:
  - split: train
    path: symile-m3-5-xs/train-*
  - split: val
    path: symile-m3-5-xs/val-*
  - split: test
    path: symile-m3-5-xs/test-*
dataset_info:
- config_name: symile-m3-10-l
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 1446543825495.0
    num_examples: 10000000
  - name: val
    num_bytes: 72759133130.0
    num_examples: 500000
  - name: test
    num_bytes: 73115450770.0
    num_examples: 500000
  download_size: 1581842669512
  dataset_size: 1592418409395.0
- config_name: symile-m3-10-m
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 730037036870.0
    num_examples: 5000000
  - name: val
    num_bytes: 34629271677.0
    num_examples: 250000
  - name: test
    num_bytes: 36151216283.0
    num_examples: 250000
  download_size: 791259211281
  dataset_size: 800817524830.0
- config_name: symile-m3-10-s
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 146524378048.0
    num_examples: 1000000
  - name: val
    num_bytes: 7080058097.0
    num_examples: 50000
  - name: test
    num_bytes: 7190117140.0
    num_examples: 50000
  download_size: 158201715556
  dataset_size: 160794553285.0
- config_name: symile-m3-10-xs
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 73256371802.0
    num_examples: 500000
  - name: val
    num_bytes: 3427110860.0
    num_examples: 25000
  - name: test
    num_bytes: 3659094119.0
    num_examples: 25000
  download_size: 79070541672
  dataset_size: 80342576781.0
- config_name: symile-m3-2-l
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 1505566993378.0
    num_examples: 10000000
  - name: val
    num_bytes: 72552235656.0
    num_examples: 500000
  - name: test
    num_bytes: 74556954653.0
    num_examples: 500000
  download_size: 1614310359255
  dataset_size: 1652676183687.0
- config_name: symile-m3-2-m
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 705910308274.0
    num_examples: 5000000
  - name: val
    num_bytes: 36243856806.0
    num_examples: 250000
  - name: test
    num_bytes: 36343275454.0
    num_examples: 250000
  download_size: 807287520293
  dataset_size: 778497440534.0
- config_name: symile-m3-2-s
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 146636122338.0
    num_examples: 1000000
  - name: val
    num_bytes: 6986579320.0
    num_examples: 50000
  - name: test
    num_bytes: 7092936758.0
    num_examples: 50000
  download_size: 161657435865
  dataset_size: 160715638416.0
- config_name: symile-m3-2-xs
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 71351902981.0
    num_examples: 500000
  - name: val
    num_bytes: 3538429599.0
    num_examples: 25000
  - name: test
    num_bytes: 3872603007.0
    num_examples: 25000
  download_size: 80789426573
  dataset_size: 78762935587.0
- config_name: symile-m3-5-l
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 1436698424427.0
    num_examples: 10000000
  - name: val
    num_bytes: 72348250632.0
    num_examples: 500000
  - name: test
    num_bytes: 73383131337.0
    num_examples: 500000
  download_size: 1596667549079
  dataset_size: 1582429806396.0
- config_name: symile-m3-5-m
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 725049451643.0
    num_examples: 5000000
  - name: val
    num_bytes: 35602464495.0
    num_examples: 250000
  - name: test
    num_bytes: 36207897705.0
    num_examples: 250000
  download_size: 798705714640
  dataset_size: 796859813843.0
- config_name: symile-m3-5-s
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 142185812397.0
    num_examples: 1000000
  - name: val
    num_bytes: 7217779117.0
    num_examples: 50000
  - name: test
    num_bytes: 7586183683.0
    num_examples: 50000
  download_size: 159628727029
  dataset_size: 156989775197.0
- config_name: symile-m3-5-xs
  features:
  - name: lang
    dtype: string
  - name: audio
    dtype: audio
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: cls
    dtype: string
  - name: cls_id
    dtype: int64
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 70410563197.0
    num_examples: 500000
  - name: val
    num_bytes: 3607295872.0
    num_examples: 25000
  - name: test
    num_bytes: 3624041386.0
    num_examples: 25000
  download_size: 80003029310
  dataset_size: 77641900455.0
---
# Dataset Card for Symile-M3
Symile-M3 is a multilingual dataset of (audio, image, text) samples. The dataset is specifically designed to test a model's ability to capture higher-order information between three distinct high-dimensional data types: by incorporating multiple languages, we construct a task where text and audio are both needed to predict the image, and where, importantly, neither text nor audio alone would suffice.
- Paper: https://arxiv.org/abs/2411.01053
- GitHub: https://github.com/rajesh-lab/symile
- Questions & Discussion: https://www.alphaxiv.org/abs/2411.01053v1

## Overview
![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/66d8e34b27d76ef6e481c2b5/mR0kJkgVyUK5rTNUOCOFx.jpeg)

Let `w` represent the number of languages in the dataset (`w=2`, `w=5`, and `w=10` correspond to Symile-M3-2, Symile-M3-5, and Symile-M3-10, respectively). An (audio, image, text) sample is generated by first drawing a short one-sentence audio clip from [Common Voice](https://commonvoice.mozilla.org/en/datasets) spoken in one of `w` languages with equal probability. An image is drawn from [ImageNet](https://www.image-net.org/) that corresponds to one of 1,000 classes with equal probability. Finally, text containing exactly `w` words is generated based on the drawn audio and image: one of the `w` words in the text is the drawn image class name in the drawn audio language. The remaining `w-1` words are randomly chosen from the ImageNet class names and written in one of the `w` languages such that there is no overlap in language or class name across the `w` words in the text. The words are separated by underscores, and their order is randomized.

## Tasks
The dataset was designed to evaluate a model on the zero-shot retrieval task of finding an image of the appropriate class given the audio and text. The most probable image for a given query audio and text pair, selected from all possible candidate images in the test set, is that with the highest similarity score.

The dataset was designed to ensure that neither text nor audio alone would suffice to predict the image. Therefore, success on this zero-shot retrieval task hinges on a model's ability to capture joint information between the three modalities.

### Dataset Structure

Each sample in the dataset is a dictionary containing the following fields:

```python
{
    # language code of the audio clip
    'lang': 'ja',
    
    # audio data
    'audio': {
        'path': 'common_voice_ja_39019065.mp3',                 # Common Voice filename
        'array': array([0.00000000e+00, ..., 7.78421963e-06]),  # raw audio waveform
        'sampling_rate': 32000                                  # sampling rate in Hz
    },
    
    # image as a PIL Image object (RGB, size varies)
    'image': <PIL.JpegImageFile image mode=RGB size=500x375>,
    
    # text containing w words (one per language) separated by underscores
    'text': 'σπιτάκι πουλιών_ドーム_प्रयोगशाला कोट_мавпа-павук_gown',
    
    # target word class name in English (key in translations.json)
    'cls': 'dome',
    
    # class ID from translations.json (0 to 999)
    'cls_id': 538,
    
    # target word (class name in the language of the audio)
    'target_text': 'ドーム'
}
```

The dataset includes a `translations.json` file that maps ImageNet class names across all supported languages. Each entry contains:
- The English class name as the key
- Translations for all supported languages (`ar`, `el`, `en`, `hi`, `ja`, `ko`, `te`, `th`, `uk`, `zh-CN`)
- The ImageNet synset ID
- A unique class ID (0-999)

Example structure:
```json
{
    "tench": {
        "synset_id": "n01440764",
        "cls_id": 0,
        "ar": "سمك البنش",
        "el": "είδος κυπρίνου",
        "en": "tench",
        "hi": "टेंच",
        "ja": "テンチ",
        "ko": "텐치",
        "te": "టెంచ్",
        "th": "ปลาเทนช์",
        "uk": "линь",
        "zh-CN": "丁鱥"
    }
}
```

## Dataset Variants
We release three variants of the dataset:
- Symile-M3-2 with 2 languages: English (`en`) and Greek (`el`).
- Symile-M3-5 with 5 languages: English (`en`), Greek (`el`), Hindi (`hi`), Japanese (`ja`), and Ukrainian (`uk`).
- Symile-M3-10 with 10 languages: Arabic (`ar`), Greek (`el`), English (`en`), Hindi (`hi`), Japanese (`ja`), Korean (`ko`), Telugu (`te`), Thai (`th`), Ukrainian (`uk`), and Chinese (`zh-CN`).

Each variant is available in four sizes:
- Large (`l`): 10M training samples, 500K validation samples, 500K test samples
- Medium (`m`): 5M training samples, 250K validation samples, 250K test samples
- Small (`s`): 1M training samples, 50K validation samples, 50K test samples
- Extra Small (`xs`): 500K training samples, 25K validation samples, 25K test samples

## Usage

Before using the dataset, ensure you have the required audio and image processing libraries installed:
```bash
pip install librosa soundfile pillow
```

To load a specific version of Symile-M3, use a configuration name following the pattern `symile-m3-{num_langs}-{size}` where:
- `num_langs` is `2`, `5`, or `10`
- `size` is `xs`, `s`, `m`, or `l`

For example, to load the `xs` version of Symile-M3-5:

```python
from datasets import load_dataset

dataset = load_dataset("arsaporta/symile-m3", "symile-m3-5-xs")

print(dataset['train'][0])    # access first train sample
print(len(dataset['train']))  # get number of train samples
```

To process the dataset without loading it entirely into memory, use streaming mode to load samples one at a time:

```python
from datasets import load_dataset

dataset = load_dataset("arsaporta/symile-m3", "symile-m3-5-xs", streaming=True)

print(next(iter(dataset['train'])))
```

To download the dataset for offline use:

```python
import os
from datasets import load_dataset
from huggingface_hub import snapshot_download

local_dir = "./symile-m3-5-xs" # where to save

# download parquet files
snapshot_download(
    repo_id="arsaporta/symile-m3",
    repo_type="dataset",
    local_dir=local_dir,
    allow_patterns=["symile-m3-5-xs/*"]  # which configuration to download
)

# load the downloaded parquet files
dataset = load_dataset(
    "parquet",
    data_files={
        "train": os.path.join(data_dir, "train-*.parquet"),
        "validation": os.path.join(data_dir, "val-*.parquet"),
        "test": os.path.join(data_dir, "test-*.parquet")
    }
)
```

## Working with Raw Data

To work directly with the source images (jpeg) and audio (mp3):

1. Download the source data:
   - **ImageNet:** Get the training data from [Kaggle's ImageNet Challenge](https://www.kaggle.com/c/imagenet-object-localization-challenge/data?select=ILSVRC)
   - **Common Voice:** Download your needed languages from [Common Voice](https://commonvoice.mozilla.org/en/datasets):
     * All languages use Common Voice v16.0, except English which uses v14.0
     * Required languages vary by configuration:
       - Symile-M3-2: English (`en`), Greek (`el`)
       - Symile-M3-5: English, Greek, Hindi (`hi`), Japanese (`ja`), Ukrainian (`uk`)
       - Symile-M3-10: All of the above plus Arabic (`ar`), Korean (`ko`), Telugu (`te`), Thai (`th`), Chinese (`zh-CN`)

2. Access the dataset CSV files:
   - Find them in the `.csv_files` directory, organized by configuration (e.g., `symile-m3-2-xs`, `symile-m3-10-l`)
   - Each configuration contains `train.csv`, `val.csv`, and `test.csv`
   - CSV paths match the default extraction paths of ImageNet (`ILSVRC/Data/CLS-LOC/train/...`) and Common Voice (`cv/{lang}/clips/...`)

## Citation

```
@inproceedings{saporta2024symile,
  title = {Contrasting with Symile: Simple Model-Agnostic Representation Learning for Unlimited Modalities}
  author = {Saporta, Adriel and Puli, Aahlad and Goldstein, Mark and Ranganath, Rajesh}
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2024}
}
```