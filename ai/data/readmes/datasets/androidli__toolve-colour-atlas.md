---
license: other
license_name: mixed-cc-by-4.0-and-upstream
license_link: https://toolve.net/color-picker/
language:
- zh
- ja
- ko
- en
tags:
- color
- colour
- design
- palette
- traditional-colors
- cultural-heritage
- multilingual
pretty_name: Toolve Colour Atlas
size_categories:
- 1K<n<10K
---

# Toolve Colour Atlas — colour names, concept→colour, and cultural object palettes

A machine-readable colour atlas with three parts that are hard to find together:
**multilingual colour names** (Chinese / Japanese / Korean traditional vocabularies,
not just English), a **concept→colour** table (what colour a word like *生气* or
*侘寂* evokes), and **palettes extracted from public-domain museum objects**
together with their material and provenance metadata.

Live lookups (10 languages, in-browser): **https://toolve.net/color-picker/**

## What is inside

| file | rows | what it is |
|---|---|---|
| `data/colour-names-toolve.parquet` | 735 | Traditional Chinese / Japanese / Korean vocabularies + curated English names |
| `data/concepts-multilingual.parquet` | 1,618 | concept → colour (zh 1080, ja 370, en 168) |
| `data/cultural-objects.parquet` | 49 | museum objects + extracted palettes + material + provenance |
| `data/colour-names-meodai.parquet` | 1,380 | English colour names re-distributed under MIT |
| `data/colour-names-ntc.parquet` | 1,515 | English colour names re-distributed under CC BY 2.5 |

## Fields

**colour-names-\*.parquet** — `name`, `hex`, `hue`, `saturation`, `lightness`,
`culture` (`cn`/`jp`/`kr`/`en`), `source`, `licence`.

**concepts-multilingual.parquet** — `concept`, `lang`, `colour_name`, `hex`,
`hue`, `saturation`, `lightness`, `category`, `derivation`
(`curated` = written by hand, `llm-consensus` = two independent generations had to
agree within 25° hue before being kept), `model`, `note`, `licence`.

**cultural-objects.parquet** — `object_id`, `title`, `culture`, `culture_group`,
`date`, `object_type`, `medium`, `museum`, `licence`, `credit`, `source_url`,
`palette_hex` (space separated), `palette_names` (nearest traditional name per
colour, matched **within the object's own culture**), `palette_detail` (JSON with
share of pixels), `object_cover_ratio`, `image_file`.

## How to use

```python
from datasets import load_dataset

names = load_dataset("androidli/toolve-colour-atlas", data_files="data/colour-names-toolve.parquet", split="train")
concepts = load_dataset("androidli/toolve-colour-atlas", data_files="data/concepts-multilingual.parquet", split="train")
objects = load_dataset("androidli/toolve-colour-atlas", data_files="data/cultural-objects.parquet", split="train")

# every Chinese traditional colour
zh = names.filter(lambda r: r["culture"] == "cn")
# what colour does a word evoke?
print(concepts.filter(lambda r: r["concept"] == "生气"))
# palettes of Korean celadon
celadon = objects.filter(lambda r: "Goryeo" in r["culture"])
```

## How the palettes were made

1. Only **CC0 / public-domain** museum images are used; each row keeps the credit
   line and canonical URL.
2. The photographed background is masked out (border-connected regions of similar
   luminance) before clustering — otherwise studio backdrops dominate the result.
3. Remaining pixels are clustered in **OKLab** (perceptually uniform) with k-means++;
   near-duplicate clusters are merged and the palette is ordered by
   `share^0.4 × chroma` so distinctive colours come first.
4. Every colour is named with the closest entry of the atlas — but **within the
   object's own culture**, so a Japanese robe never gets Korean colour names.
5. Two sanity gates: at least one chromatic colour must exist, and the palette's mean
   luminance must match the object region, otherwise the object is dropped
   (under-exposed metalwork yields no palette rather than a wrong one).

## Limitations

- Concept→colour entries are **associative, not factual**: they model what a word
  evokes, and were filtered for agreement rather than verified.
- Museum photographs carry museum lighting. Extracted palettes describe *the
  photograph of the object*, not a colorimetric measurement of the surface.
- Object coverage is small and uneven (49 objects). It is an
  appendix to the name vocabulary, not a survey of world collections.
- Colour names are cultural artefacts: the same hexadecimal can legitimately carry
  different names in different traditions. We keep them separate on purpose.

## Licence

Mixed, by source — see **NOTICE.md** for per-source terms:

- our own additions (traditional vocabularies, curated names, concepts, palettes):
  **CC BY 4.0** — attribution "toolve colour atlas (https://toolve.net/color-picker/)"
- NTC subset: **CC BY 2.5** (Chirag Mehta)
- meodai subset: **MIT** (David Aerne)
- museum metadata/images: **CC0 1.0** (Cleveland Museum of Art, The Metropolitan Museum of Art)

## Citation

```
@misc{toolve_colour_atlas,
  title  = {Toolve Colour Atlas: multilingual colour names, concept-to-colour, and cultural object palettes},
  author = {toolve},
  year   = {2026},
  url    = {https://huggingface.co/datasets/androidli/toolve-colour-atlas}
}
```
