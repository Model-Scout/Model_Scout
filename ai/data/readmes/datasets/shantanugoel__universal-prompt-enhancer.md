---
pretty_name: Universal Prompt Enhancer training corpus
license: other
license_name: upe-mixed-component-terms
license_link: LICENSE.md
task_categories:
- text-generation
- image-text-to-text
language:
- en
- hi
- es
- fr
- ja
- zh
- ko
- ar
- de
- pt
size_categories:
- 10K<n<100K
tags:
- synthetic
- prompt-enhancement
- multimodal
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*.parquet
  - split: validation
    path: data/validation-*.parquet
  - split: test
    path: data/test-*.parquet
---

# Universal Prompt Enhancer corpus

**Built with Qwen. Improved using Qwen. Public release. Component-specific terms apply.**

The complete 44,184-record corpus used for the Universal Prompt Enhancer 0.8B
student, with original train/validation/test assignments. This is synthetic
teacher supervision for generative-media prompt rewriting; it is not human
ground truth. It covers t2i, edit, t2v, i2v, sound effects, and music, across
14 mode/target combinations. See `provenance/release_audit.json` for exact counts.

| Split | Records | Unique original IDs | Records with images |
|---|---|---|---|
| train | 39729 | 38695 | 12701 |
| validation | 2271 | 2211 | 750 |
| test | 2184 | 2123 | 688 |

## Loading

```python
from datasets import load_dataset
ds = load_dataset("shantanugoel/universal-prompt-enhancer")
row = ds["train"][0]
print(row["user_request"], row["assistant"])
# row["image"] is a PIL image or None; original_image_paths are historical only.
```

The Parquet shards embed source image bytes. A network connection to MagicBrush
or access to the training machine is not needed to decode these images. Only
source images used by this corpus are included, resized to a maximum 768×768
bounding box and reencoded as JPEG quality 90; audio and edited target images
are not included. `original_records/*.jsonl.gz` preserves the exact input records
for reproducibility, including historical local image paths. Prefer Parquet for use.

## Schema

- `release_row_id`: unique stable ID within this release, formed from split + row index.
- `id`, `row_id`, `concept_id`, `split_key`: original identifiers, **not necessarily unique**.
- `mode`, `target`, `user_request`, `assistant`: task, destination convention,
  rough request, and teacher-generated JSON target. The target keys are
  `rewritten_prompt`, `aspect_ratio`, `ratio_follow`, `duration_s`, `constraints`.
- `image`: optional embedded source image; `image_sha256`: JPEG content hash.
- `image_source_dataset`, `image_source_revision`, `image_source_id`,
  `image_source_split`, `image_license`: image attribution independent of request provenance.
- `source_dataset`, `source_id`: original request provenance; may be null even
  on image rows, so use the additional image attribution fields.
- `request_component_license`: CC-BY-SA-4.0 for MusicCaps-derived requests,
  CC-BY-4.0 for MagicBrush requests, otherwise project-original research terms.
- `teacher`, teacher revision/prompt hash fields, difficulty, language, seed,
  attempts, and license notes: original generation metadata where present.
- `original_image_paths`: original training-machine references, informational only.

`language` is an incomplete planning label, with missing values on many records;
it is not a language detector. The labeled languages are en, hi, es, fr, ja, zh,
ko, ar, de, pt. Output language depends on target conventions.

## Creation and splits

30,400 planned concepts expanded to target-specific requests; teachers generated
candidate rewrites, which were filtered with deterministic checks and retries.
The main qwen-image target buckets used Qwen-Image-2.1 PE-T2I/PE-I2I; other
groups and hard rows used Qwen3.8 Flash Next EXL3. See the linked model card and
verified provenance for teacher revisions and training settings.
The `constraints` target was filled by a deterministic lexical extractor rather
than a comprehensive semantic annotation. Upstream prompt sources and revisions
are recorded in historical provenance; upstream prompt files are not republished here.

Concept grouping keeps `split_key` disjoint between splits. **Original source
identity is not disjoint.** The release audit records shared request source IDs,
original image source IDs, image paths, and exact image hashes independently.
These overlaps can make evaluation optimistic. Repeated original IDs remain
within splits despite earlier claims that deduplication was complete. They are
retained because these are the records actually used for training/evaluation.
Do not use `id` alone as a dictionary key. A future cleaned corpus requires a
new version and reevaluation; this release does not silently change the splits.

## Rights and attribution

This dataset is a collection under **component-specific terms**, not a blanket
Apache-2.0 or uniformly non-commercial dataset. See [LICENSE.md](LICENSE.md),
[NOTICE](NOTICE), and `LICENSES/` for full copies and publication-review issues.

- MagicBrush instructions/images: authors Kai Zhang, Lingbo Mo, Wenhu Chen,
  Huan Sun, Yu Su; CC-BY-4.0; source revision
  `1d8d4629150d18ca50afab66391866f2085be989`. Image conversion changes are above.
- MusicCaps-derived requests: Google and contributors, CC-BY-SA-4.0; source
  revision `0a51889b340037bb75a9a0858af2e4ece21f7f89`. Requests were adapted from
  caption inspiration; source IDs preserve attribution. No source audio included.
- Original synthetic annotations: conservative research/evaluation release terms,
  with Qwen teacher notices and unresolved distillation/combination questions.
  A research-only blanket license must not override Creative Commons components.

## Limitations and sensitive content

Teacher hallucinations, mistranslations, added restrictions, and failures to
preserve exclusions exist. Automatic filtering does not certify correctness.
Images can contain people, including children, as in upstream MagicBrush; no
new consent, privacy clearance, or biometric annotation is asserted. No new
comprehensive sensitive-content audit was performed for this release. Do not
use the dataset as evidence of identities or factual descriptions of people.
Source licenses and attribution do not by themselves establish all other rights.

Related model: https://huggingface.co/shantanugoel/Universal-Prompt-Enhancer-0.8B.
Use the model card's citation for this corpus and retain upstream attributions.

## Release verification

Before publication, the release was downloaded into a separate cache and checked against
its SHA-256 manifests. Dataset records/images were checked, and downloaded
merged, adapter, and Q6_K models passed text/image inference smoke checks.
See [release_validation.json](release_validation.json) for pinned tested
revisions and outputs. These checks verify packaging and I/O, not prompt
quality, full benchmark reproduction, or public-release licensing clearance.
