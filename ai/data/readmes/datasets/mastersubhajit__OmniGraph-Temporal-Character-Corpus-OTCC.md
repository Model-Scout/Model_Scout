---
license: other
license_name: academic-only
task_categories:
- image-to-text
- object-detection
- visual-question-answering
- image-classification
language:
- en
- ja
- ko
- zh
tags:
- manga
- comics
- character-recognition
- graph-neural-networks
- multimodal
- panel-segmentation
- temporal-reasoning
- character-reidentification
- dialogue-attribution
- narrative-ordering
annotations_creators:
- machine-generated
language_creators:
- other
pretty_name: OmniGraph Temporal Character Corpus (OTCC)
size_categories:
- 10K<n<100K
extra_gated_heading: OmniGraph Temporal Character Corpus (OTCC) — Research Access Application
extra_gated_description: "Access to the OmniGraph Temporal Character Corpus (OTCC) is strictly restricted to accredited academic and research institutions for non-commercial scientific inquiry. Applications submitted using generic or personal email domains (e.g., gmail.com, hotmail.com, yahoo.com) will be automatically rejected. Approved researchers are kindly requested to cite this corpus in all publications resulting from its use and must never redistribute the raw imagery."
extra_gated_prompt: I confirm that I have read, understood, and agree to abide by the Academic Use Terms and Non-Commercial Restrictions for the OmniGraph Temporal Character Corpus (OTCC).
extra_gated_fields:
  Full Name: text
  Official Institutional Email Address: text
  University / Research Institution Affiliation: text
  Department / Faculty / Laboratory: text
  Academic Role / Position:
    type: select
    options:
    - label: Faculty / Professor / Principal Investigator
      value: faculty
    - label: Postdoctoral Researcher
      value: postdoc
    - label: PhD / Graduate Student Researcher
      value: graduate_student
    - label: Undergraduate Student Researcher
      value: undergrad
    - label: Research Scientist (Academic / Non-Profit Lab)
      value: research_scientist
  Country / Region: country
  Academic Webpage or Google Scholar Profile URL: text
  Specific Research Topic or Project Title: text
  Intended Use and Methodology of this Dataset in Your Research: text
  I agree to acknowledge and cite the OmniGraph Temporal Character Corpus (OTCC) when publishing research resulting from this dataset: checkbox
  I confirm this dataset will be used exclusively for non-commercial academic research and will NOT be used for commercial training, services, or products: checkbox
  I agree not to redistribute, mirror, or publicly share the underlying manga images or access credentials: checkbox
configs:
- config_name: default
  data_files:
  - split: train
    path: "**"
---

<div align="center">
  <img src="assets/ait_logo.jpg" alt="Asian Institute of Technology" width="440"/>
</div>

# OmniGraph Temporal Character Corpus (OTCC)

<div align="center">
  <a href="https://huggingface.co/datasets/mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC"><img src="https://img.shields.io/badge/Pages-22%2C914-2563EB" alt="Pages"></a>
  <a href="https://huggingface.co/datasets/mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC"><img src="https://img.shields.io/badge/Panels-25%2C253-D97706" alt="Panels"></a>
  <a href="https://huggingface.co/datasets/mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC"><img src="https://img.shields.io/badge/Graph_Edges-27%2C786-059669" alt="Edges"></a>
  <a href="https://huggingface.co/datasets/mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC"><img src="https://img.shields.io/badge/Series_Titles-77-7C3AED" alt="Series"></a>
  <a href="https://huggingface.co/datasets/mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC"><img src="https://img.shields.io/badge/Access-Gated_Research-DC2626" alt="Access"></a>
  <a href="https://huggingface.co/datasets/mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC"><img src="https://img.shields.io/badge/License-Academic_Only-16A34A" alt="License"></a>
</div>

---

## Notice: Academic and Research Purposes Only

The **OmniGraph Temporal Character Corpus (OTCC)** is curated, maintained, and distributed exclusively for non-commercial academic research, scientific inquiry, and educational benchmarking. 

By requesting access to this gated repository, researchers explicitly agree to the following terms:
1. **Non-commercial Use:** You will not utilize, ingest, or fine-tune models on any part of this corpus for commercial products, revenue-generating services, or proprietary commercial model deployments.
2. **No Artwork Redistribution:** You will not redistribute, mirror, re-host, or publicize the underlying raw source manga scans or artwork outside the authorized research environment.
3. **Intellectual Property Respect:** All underlying manga artwork, visual illustrations, dialogue texts, and characters remain the exclusive intellectual property of their original creators, illustrators, and publishing companies. This corpus is provided under fair-use principles to advance computer vision and multimodal reasoning.

---

## Dataset Overview

Modern document intelligence and multimodal vision-language models struggle when confronted with sequential graphic narratives. Comic and manga pages present non-standard reading orders, variable non-grid panel layouts, visual stylization, and long-range narrative dependencies including temporal jumps, simultaneous actions, and character identity transformations across changing attire and ages.

The **OmniGraph Temporal Character Corpus (OTCC)** addresses this benchmark gap. It connects high-resolution source manga page scans with a standardized hierarchical annotation model:

- **Page-Level Multi-Panel Alignment:** Every source page is paired with an arbitrary, dynamic number of annotated panels (1 to 9 panels per page).
- **Relational & Temporal Graph Modeling:** Panels are connected via 27,786 directed graph edges capturing narrative sequencing (`PAGE_SEQUENCE`, `ADJACENT`, `NEXT`), simultaneous action (`CONCURRENT`), temporal flashbacks (`FLASHBACK`), and perspective shifts (`PERSPECTIVE`).
- **Entity State Tracking & Character Continuity:** Annotations track 43,535 character instances (12,214 named appearances) with bounding geometry, identity resolution confidence, visual descriptors, emotion, location, and clothing state deltas.
- **Dialogue Attribution & Speech Bubble Parsing:** Annotations include 79,768 dialogue and sound-effect (SFX) regions with normalized box coordinates, reading sequence orders, and linked character-speaker IDs.

---

## Corpus Statistics

| Dimension | Metric | Detail |
|---|---|---|
| **Volume & Scale** | Total Source Pages | **22,914** high-resolution scanned pages |
| | Approximate Image Volume | **~36.2 GB** uncompressed image data |
| | Unique Series / Works | **77** distinct manga series |
| | Unique Chapters / Volumes | **1,150** narrative chapters |
| **Structural Annotations** | Annotated Panels | **25,253** bounding boxes |
| | Panels per Page | 1 to 9 (dynamic layout) |
| | Directed Narrative Edges | **27,786** relational graph edges |
| **Character & Dialogue** | Character Instances | **43,535** observed character entity boxes |
| | Named Character Appearances | **12,214** resolved character references |
| | Dialogue & SFX Bubbles | **79,768** segmented text regions |
| **Schema & Release** | Current Schema Identifier | `temporal_state` |
| | Format Standard | Hugging Face `ImageFolder` compatible |

---

## Supported Machine Learning Tasks

The multi-tiered architecture of OTCC provides an empirical benchmark across multiple core computer vision and multimodal research domains:

1. **Panel Detection & Reading-Order Segmentation**
   - *Target architectures:* YOLOv8/v11, RT-DETR, Mask R-CNN, LayoutLMv3.
   - *Objective:* Predict normalized panel bounding boxes [x_min, y_min, x_max, y_max] and sequence reading rank.
2. **Dialogue Attribution & Speaker Identification**
   - *Target architectures:* Multimodal LLMs (Qwen2-VL, InternVL, LLaVA, Florence-2).
   - *Objective:* Ground dialogue bubbles to their speaking character entity using visual orientation and speech bubble tail cues.
3. **Character Re-Identification (ReID) Under Visual Variation**
   - *Target architectures:* Contrastive Visual Encoders (DINOv2, CLIP, OpenCLIP).
   - *Objective:* Match character identity embeddings across dramatic changes in framing, lighting, costume, and expression.
4. **Narrative Graph Reasoning & Temporal Classification**
   - *Target architectures:* Graph Neural Networks (GAT, Relational GCN, Graphormer).
   - *Objective:* Classify panel transition types (`NEXT`, `CONCURRENT`, `FLASHBACK`, `PERSPECTIVE`) from multimodal node representations.
5. **Multimodal Visual Storytelling & VQA**
   - *Target architectures:* Vision-Language Foundation Models.
   - *Objective:* Sequential scene captioning and visual question answering across narrative time.

---

## Schema Specification (`temporal_state`)

### Top-Level Dataset Fields (`metadata.jsonl`)

Each record in `metadata.jsonl` corresponds to one source page, enabling native visual rendering in the Hugging Face Dataset Viewer:

| Field | Type | Description |
|---|---|---|
| `image` | `Image` | PIL Image object automatically resolved from `file_name` by `ImageFolder`. |
| `file_name` | `string` | Relative path to the image scan within the repository (e.g. `335km/Vol. 1 Ch. 1/00.jpg`). |
| `schema` | `string` | Standardized schema identifier: `temporal_state`. |
| `work_id` | `string` | Series identifier (e.g. `saving-you`, `baby-steps`, `wangan-midnight`, `335km`). |
| `chapter_id` | `string` | Chapter or volume designator (e.g. `Vol. 1 Ch. 1`). |
| `page_id` | `string` | Zero-padded page index within the chapter. |
| `page_index_in_work` | `int` | Global sequential page index across the complete series. |
| `panel_count` | `int` | Number of annotated panels present on this specific page. |
| `source_width` | `int` | Native pixel width of the source image. |
| `source_height` | `int` | Native pixel height of the source image. |
| `source_sha256` | `string` | SHA-256 cryptographic hash of the source image for provenance verification. |
| `split` | `string` | Dataset split identifier (`train`). |
| `panels` | `list[object]` | Ordered list of panel annotation dictionaries (detailed below). |

---

### Nested Panel Object Structure (`panels[]`)

| Field | Type | Description |
|---|---|---|
| `panel_id` | `string` | Canonical panel identifier (e.g. `000000_p1`). |
| `panel_index` | `int` | Zero-based panel reading order on the page. |
| `panel_box` | `list[float]` | Normalized [x_min, y_min, x_max, y_max] coordinates in range [0.0, 1.0]. |
| `shot_type` | `string` | Camera framing: `wide`, `medium`, `close_up`, `extreme_close_up`, `medium_wide`, `extreme_wide`, `over_shoulder`. |
| `panel_function` | `string` | Narrative function: `action`, `dialogue`, `establishing`, `reaction`, `transition`, `splash`, `montage`. |
| `temporal_relation` | `string` | Temporal narrative transition: `NEXT`, `FLASHBACK`, `CONCURRENT`, `PERSPECTIVE`, `FLASHFORWARD`. |
| `temporal_relation_scope` | `string` | Narrative context scope (e.g. `previous_panel_same_page`). |
| `event_id` | `string` | Higher-level narrative event cluster identifier. |
| `scene_id` | `string` | Scene environment cluster identifier. |
| `prompt` | `string` | Descriptive scene description of the panel's visual action. |
| `features` | `object` | 8-D deterministic visual style vector and descriptor method. |
| `entities` | `list[object]` | Detected character entities present in this panel (detailed below). |
| `bubbles` | `list[object]` | Segmented dialogue and sound-effect regions (detailed below). |
| `chronology` | `object` | Story-time ordering metadata. |
| `generation` | `object` | OmniGraph generative dependency rank and receptive field tracking. |

---

### Character Entity Structure (`panels[].entities[]`)

| Field | Type | Description |
|---|---|---|
| `instance_id` | `string` | Panel-local entity identifier (e.g. `000000_p1_E1`). |
| `character_id` | `string` | Cross-panel resolved character identifier (e.g. `char_b88d62e0f7_0000`). |
| `character_name` | `string` | Character name string when known. |
| `identity_resolution` | `string` | Identity assignment state: `new`, `existing`, `merged`. |
| `identity_confidence` | `float` | Confidence score of character identity resolution (0.0 to 1.0). |
| `identity_evidence` | `string` | Reasoning rationale describing visual continuity factors. |
| `geometry` | `object` | Contains normalized bounding boxes: `bbox_page` and `bbox_in_panel`. |
| `state` | `object` | Observed physical location, emotion, clothing descriptors, and state deltas. |
| `utterances` | `list[string]` | Strings spoken by this character in the current panel. |
| `age` | `object` | Normalized visual age anchor score, confidence, and visual evidence. |

---

### Dialogue Bubble Structure (`panels[].bubbles[]`)

| Field | Type | Description |
|---|---|---|
| `bubble_id` | `string` | Unique bubble identifier (e.g. `000001_p0_b0`). |
| `reading_order` | `int` | Sequential reading rank within the page. |
| `kind` | `string` | Text bubble classification: `dialogue`, `thought`, `caption`, `sfx`. |
| `text` | `string` | Transcribed OCR / dialogue text content. |
| `geometry` | `object` | Normalized coordinates: `box_page` and `box_in_panel`. |
| `speaker_character_id` | `string` | Linked `character_id` of the speaker. |
| `speaker_confidence` | `float` | Attribution confidence score (0.0 to 1.0). |
| `speaker_basis` | `string` | Attribution reasoning basis: `tail`, `context`, `none`. |

---

### Relational Graph Edges (`annotation.jsonl`)

The raw `annotation.jsonl` file includes 27,786 relational graph edge entries:

```json
{
  "record": "edge",
  "row": {
    "source": "000000_p0",
    "target": "000000_p1",
    "relation": "NEXT",
    "scope": "page",
    "evidence": "v5_edge_types_mask"
  }
}
```

| Edge Relation | Frequency | Narrative Semantic |
|---|---:|---|
| `PAGE_SEQUENCE` | 22,837 | Direct sequential page transition across the chapter |
| `ADJACENT` | 2,339 | Spatially adjacent panels on the same physical page layout |
| `NEXT` | 2,195 | Direct chronological causal narrative continuation |
| `SAME_CHARACTER_CONTINUITY` | 180 | Character persistence across consecutive panel transitions |
| `CONCURRENT` | 118 | Simultaneous actions occurring in parallel time |
| `SAME_LOCATION` | 91 | Persistent physical environment between consecutive panels |
| `FLASHBACK` | 14 | Temporal shift showing past story events |
| `PERSPECTIVE` | 10 | Alternate viewpoint shift of an identical event |
| `FLASHFORWARD` | 2 | Narrative jump ahead in story time |

---

## Recommended Training & Evaluation Practices

### 1. Data Split Strategy (Preventing Art-Style Leakage)
All records in this repository are published under the `train` split. When configuring benchmarks:
- **Do not perform uniform random page shuffling.** Random page splits allow models to memorize an illustrator's idiosyncratic line-art style and plot points across consecutive pages.
- **Perform series-level (`work_id`) holdout splits:** Reserve complete titles (e.g., 65 series for training, 6 for validation, and 6 for testing). This ensures models generalize across unseen artistic traditions and drawing conventions.

### 2. Class Imbalance Handling for Temporal Reasoning
Sequential narrative progression (`NEXT`) naturally forms the majority of comic storytelling. For non-linear temporal classification benchmarks (`CONCURRENT`, `FLASHBACK`, `PERSPECTIVE`), models should be trained with focal loss, class-balanced resampling, or contrastive minority weighting.

---

## Quickstart Usage

### Streaming Access (Recommended)

Because the dataset comprises ~36 GB of high-resolution imagery, streaming allows instant batch iteration without downloading the entire repository:

```python
from datasets import load_dataset

dataset = load_dataset(
    "mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC",
    split="train",
    streaming=True,
)

for example in dataset.take(3):
    image = example["image"]          # PIL Image object
    panels = example["panels"]        # List of panel dictionaries
    print(f"Series: {example['work_id']} | Panels on page: {example['panel_count']}")
    
    for panel in panels:
        box = panel["panel_box"]      # [x_min, y_min, x_max, y_max] normalized in [0, 1]
        print(f"  Panel {panel['panel_id']} ({panel['shot_type']}): {panel['prompt']}")
```

### Parsing the Full Narrative Graph

To reconstruct the directed panel narrative graph for Graph Neural Networks:

```python
import json
import networkx as nx

graph = nx.DiGraph()

with open("annotation.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)
        if item.get("record") == "panel":
            panel_id = item["row"]["panel_id"]
            graph.add_node(panel_id, **item["row"])
        elif item.get("record") == "edge":
            u = item["row"]["source"]
            v = item["row"]["target"]
            relation = item["row"]["relation"]
            graph.add_edge(u, v, relation=relation)

print(f"Reconstructed graph with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")
```

---

## Ethical Considerations & Disclosures

1. **Synthetic & Semi-Automated Annotation Disclosure:** Annotations are algorithmically generated and machine-assisted under the `temporal_state` schema. They are intended for research benchmarking and should not be treated as human gold labels without task-specific validation.
2. **Visual Age Anchoring Notice:** The `age` metric in character entities represents an uncertain visual heuristic derived from facial geometry and caricature conventions. It is strictly an experimental visual cue and must not be used for real-world biometric inference, age verification, or surveillance applications.

---

## Affiliation & Institutional Credits

The **OmniGraph Temporal Character Corpus (OTCC)** was created and curated by [Subhajit Ghosh](https://huggingface.co/mastersubhajit). 

It is maintained for academic research and is proudly associated with the **Asian Institute of Technology (AIT)**.

---

## Citation

If this corpus supports your research, please cite it using the following format:

```bibtex
@misc{subhajit_ghosh_2026,
	author       = { Subhajit Ghosh },
	title        = { OmniGraph-Temporal-Character-Corpus-OTCC (Revision a15b730) },
	year         = 2026,
	url          = { https://huggingface.co/datasets/mastersubhajit/OmniGraph-Temporal-Character-Corpus-OTCC },
	doi          = { 10.57967/hf/10875 },
	publisher    = { Hugging Face }
}
```

---

## Contact & Responsible Disclosure

For academic collaborations, annotation clarifications, or provenance inquiries, open a discussion in the repository's **Discussions** tab. When submitting inquiries regarding specific panels, reference the `work_id`, `chapter_id`, and `panel_id`.
