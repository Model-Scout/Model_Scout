---
language:
- de
- ja
- tr
- en
- ko
- bn
license: cc-by-4.0
task_categories:
- visual-question-answering
pretty_name: ROLECUE-192
size_categories:
- n<1K
---

# ROLECUE-192

**Who did what to whom?**

ROLECUE is a controlled dataset for studying whether vision-language models can connect the roles they see in an image with the roles expressed in a sentence. It pairs two-person action scenes with sentences in six languages, including sentences where the person acted upon is mentioned first.

![Illustration of one person pushing another, with color bars representing word order](rolecue_cover.png)

*Cover illustration; the dataset itself contains the original generated image stimuli.*

## At a glance

| | |
| --- | --- |
| Images | 192 generated two-person scenes |
| Actions | 12 interpersonal actions |
| Languages | German, Japanese, Turkish, English, Korean, Bangla |
| Sentence order | Agent-first and patient-first |
| Tasks | Image-only role recognition, text-only role parsing, and joint image-sentence matching |
| Answer format | A/B choices with reversed answer mappings |

ROLECUE is designed as a diagnostic stress test. The separate tasks help distinguish visual and language errors from difficulties in joint matching; response preferences can also affect the results. See the [code and analysis repository](https://github.com/NiazTahi/ROLECUE) for the evaluation and scoring procedures.

## What's in the dataset

```text
data/
  manifests/
    rolecue192_image_gate.jsonl
    rolecue192_six_language_full.jsonl
    rolecue192_image_file_manifest.csv
    MANIFEST_SUMMARY.json
  processed/rolecue/
    rolecue_96/                 # original 96 PNGs
    rolecue_192_new_seeds/      # second 96 PNGs
```

`rolecue192_six_language_full.jsonl` has 18,816 prompt rows: 384 image-only, 9,216 text-only, and 9,216 joint. These are prompt rows, not independent images: the design repeats stimuli across language, order, sentence condition, and answer mapping. `rolecue192_image_gate.jsonl` contains the 384 image-only gate rows.

Each JSONL row contains a task, prompt, correct option, and option mapping. Image-based rows include `image_path`, relative to the dataset root. Sentence rows also include fields such as `language`, `order`, `sentence`, `sentence_agent_color`, and, for joint trials, `is_match`. The seed labels identify frozen visual stimuli; they are not analysis-time random draws.

The CSV records the original image paths and SHA-256 checksums. Its `review_jpeg` column refers to historical review copies, which are not included in this release. The PNGs here are the exact images used for inference, verified against those checksums.

## Download and inspect

Install the Hugging Face Hub client and Pillow, then download the dataset repository:

```bash
pip install huggingface_hub pillow
```

```python
import json
from pathlib import Path
from huggingface_hub import snapshot_download
from PIL import Image

root = Path(snapshot_download(repo_id="NiazTahi/ROLECUE-192", repo_type="dataset"))
manifest = root / "data/manifests/rolecue192_six_language_full.jsonl"
with manifest.open(encoding="utf-8") as f:
    example = next(json.loads(line) for line in f if json.loads(line)["task"] == "joint_match")

print(example["language"], example["order"], example["sentence"])
print(example["prompt"], "Correct option:", example["correct_option"])
image = Image.open(root / example["image_path"])
```

The evaluation pairs reversed A/B mappings before reporting semantic decisions. Treating each prompt row as an independent example will not reproduce the reported scores; refer to the [code repository](https://github.com/NiazTahi/ROLECUE) for analysis details.

## Validation and limitations

Human validators assessed visual role clarity and language templates. The first image wave has three recorded assessments per image. For the second wave, duplicated archived submissions mean the records do not establish two independent assessments. Language forms asked participants to assess their native language; the available records do not establish recruitment or validator independence.

The images are synthetic, color-coded, and depict male-presenting adults. The dataset covers 12 actions and does not represent the diversity of natural scenes or people. Static chasing scenes can be ambiguous, so the paper reports a no-chasing visual-control subset for affected models and a common-subset comparison. Instructions are in English even when the sentence is in another language. Results should not be interpreted as a general ranking of languages or cultures.

## Paper and license

ROLECUE: Diagnosing Cross-Lingual Role-Binding Failures in Vision-Language Models, by Niaz Mohaiman Abtahi and Evan Maksud. Accepted to WACV 2027, Evaluations and Datasets Track.

The dataset is released under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Code is available separately under the MIT license.
