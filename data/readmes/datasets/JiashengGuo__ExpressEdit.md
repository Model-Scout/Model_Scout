---
license: cc-by-nc-sa-4.0
task_categories:
- image-text-to-image
- image-to-image
language:
- en
- zh
- ja
- ko
tags:
- art
pretty_name: ExpressEdit
size_categories:
- 10K<n<100K
viewer: false
---

# ExpressEdit: A Comprehensive Database for Stylized Facial Expression Editing

![diverse_page-0001](https://cdn-uploads.huggingface.co/production/uploads/698cc41c0eca9dd7d109f5a5/OzI0yHkFRj9SkCi1_NUcW.jpeg)

## 🚀 Interactive Demo

We provide a minimalist Retrieval-Augmented Generation (RAG) demo hosted on Hugging Face Spaces. You can input your own creative story snippet, and the system will retrieve the most matching expression tag from this database.

👉 **[Try the ExpressEdit RAG Demo Here](https://huggingface.co/spaces/JiashengGuo/ExpressEdit-RAG)**

## 📋 Dataset Summary

Facial expressions of characters are a vital component of visual storytelling. While current AI image editing models hold promise for assisting artists in the task of stylized expression editing, these models introduce global noise and pixel drift into the edited image, preventing the integration of these models into professional image editing software and workflows.

Furthermore, models primarily rely on textual prompts for image generation, which means users have to come up with detailed descriptions of expressions. This requirement on the prompt quality poses a cognitive burden for users and slows down the creation process.

**ExpressEdit** provides a solution by mapping free-form narrative intents to structured generation tags. To support the generation of diverse expressions according to different narrative needs, we compile a comprehensive expression database of 135 expression tags enriched with example stories and images designed for retrieval-augmented generation. This dataset accompanies the ExpressEdit Photoshop plugin, an open-source tool for fast and clean stylized expression editing.

## 🖼️ Dataset Composition

The dataset contains a rich combination of text, tags, and generated images:

### Expression Tags

* **Base Tags:** We obtained the expression tags from the Danbooru official website of face tags and eye tags. We manually choose the tags that can assist expression generation, filtering out explicit content, to obtain **135 expression tags**.
* **Definitions:** The definition for each expression tag was obtained from the official Danbooru website, specifying when the tag should and should not be applied.
* **Alternative Tags:** We also include alternative tags, which are Pixiv tags for each expression, or translations of the expression tag into Chinese, Japanese, or Korean. A total of **332 alternative tags** were obtained in this process.
* **Transformation-Free Flag:** Each tag is annotated with a flag indicating whether it can be reliably edited without applying Photoshop transformations such as Liquify. 100 out of 135 tags are transformation-free; the remaining 35 require quick manual operations.

### Example Stories

* To inspire users and facilitate the retrieval process, we generated 5 example stories for each tag with Gemini 3 Flash.
* The process is repeated for Chinese, English, Japanese, and Korean.
* The process results in **2,700 short stories** (135 tags × 5 stories × 4 languages).

### Example Images

* Example images were automatically generated based on 5 original character images.
* For each expression tag, we repeat the generation 5 times with different random seeds, resulting in **3,375 total edited images**.

## 🎯 Applications

There are two primary use cases for the ExpressEdit dataset:

### Retrieval-Augmented Generation (RAG)

Given the database, a user can conveniently use a VLM to retrieve the tag that is relevant to their stories, ideas, or specific editing instructions. By converting free-form user intent into structured expression tags, ExpressEdit refines the prompt into a format suitable for the image generation model, mitigating the prompt sensitivity of multi-modal generative models that potentially degrades image quality.

![pipeline_text (3)_page-0001](https://cdn-uploads.huggingface.co/production/uploads/698cc41c0eca9dd7d109f5a5/ZnL7Lz6fI2nP1p9tnTRhC.jpeg)

### Reference for Expression Stylization

The 3,375 image results can be used as a visual benchmark for how specific Danbooru tags influence the style, eye placement, and mouth shape of various 2D characters across different random seeds.

## 🏗️ Dataset Structure

The repository is organized into image folders and text-based JSONL files:

### Image Data

* **`results/` Directory:** Contains the 3,375 generated `.png` images. The files are named systematically as `c{character}_t{tag}_r{round}.png`, where `character` ranges from 1 to 5, `tag` is the zero-padded tag index from 001 to 135, and `round` is the random seed repetition from 1 to 5.

### Metadata & Text Files

* **`danbooru_expression_tags_full.jsonl`:** The core expression tag database. Each line is a JSON object with the following fields:
  * `tag_id`: Integer identifier from 1 to 135.
  * `tag`: The canonical Danbooru tag string (e.g., `+_+`, `averting_eyes`).
  * `definition`: Human-readable explanation of the expression, sourced from the Danbooru wiki.
  * `alternative_tags`: A list of Pixiv tags and translations into Chinese, Japanese, and Korean.
  * `wai_illustrious_sdxl_16_auto_edit`: Integer flag (1 = transformation-free; 0 = requires Photoshop transformations such as Liquify).

* **`*_stories.jsonl`:** Four separate files (`english_stories.jsonl`, `chinese_stories.jsonl`, `japanese_stories.jsonl`, `korean_stories.jsonl`) containing the narrative backgrounds. Each line mirrors the fields of the tag database and adds:
  * `responses`: A single string containing 5 numbered stories (prefixed `1.`, `2.`, ..., `5.`) separated by blank lines, which can be split on the numeric prefix to recover individual stories.

## 🚀 Usage

Download the full repository:

```bash
huggingface-cli download JiashengGuo/ExpressEdit --repo-type=dataset --local-dir ./ExpressEdit
```

Load the tag database and English stories in Python:

```python
import json

with open("danbooru_expression_tags_full.jsonl") as f:
    tags = [json.loads(line) for line in f]

with open("english_stories.jsonl") as f:
    stories = [json.loads(line) for line in f]

# Access the first tag
print(tags[0]["tag"], "-", tags[0]["definition"])
```

## 📜 Citation

If you find this dataset helpful in your research, please cite:

```bibtex
@article{tang2026expressedit,
  title={ExpressEdit: Fast Editing of Stylized Facial Expressions with Diffusion Models in Photoshop},
  author={Tang, Kenan and Guo, Jiasheng and Lin, Jeffrey and Qin, Yao},
  journal={arXiv preprint arXiv:2604.03448},
  year={2026}
}
```

## 🙏 Acknowledgements

The expression tags, definitions, and alternative tags are sourced from the [Danbooru](https://danbooru.donmai.us/) and [Pixiv Encyclopedia](https://dic.pixiv.net/en/) communities. The example stories were generated with Gemini 3 Flash.