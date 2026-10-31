---
license: cc-by-sa-4.0
language:
  - ko
pretty_name: Korean Handwriting Strokes (hangul.ink)
tags:
  - handwriting
  - online-handwriting
  - hangul
  - korean
  - pen-strokes
  - handwriting-synthesis
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files: data/recordings.parquet
  - config_name: sentences
    data_files: data/sentences.parquet
---

# Korean Handwriting Strokes

4,568 lines of Korean handwriting captured as **pen strokes** (not
images) with a Neo Smartpen: x/y position, pen-tip force, timing, and pen tilt
for every sample, grouped into strokes. This is the training data behind
[hangul.ink](https://hangul.ink), a browser-side recurrent network that writes Hangul by
hand, released for Hangul Day 2026. Code for collection, training, and the demo
is at [github.com/Hilokal/korean-handwriting](https://github.com/Hilokal/korean-handwriting).

| | |
|---|---|
| Recordings (lines) | 4,568 |
| Distinct sentences | 2,594 |
| Strokes | 250,517 |
| Pen samples | 2,952,498 |
| Recording time | 29.5 h |
| Writers | 1 |

All recordings are by a single writer, **Jo YW**, a native Korean
speaker who wrote every line for this project with a Neo Smartpen on Ncode paper. The pen streams at roughly
50 samples per second.

## Format

`data/recordings.parquet` has one row per recording. Long sentences were
written as several lines; `chunk_index` orders the chunks of one
`sentence_text`, and `text` is what this particular recording says.

| column | type | meaning |
|---|---|---|
| `recording_id` | int | unique id |
| `sentence_id` | int | joins to `sentences` |
| `writer_id` | int | always 1 in this release |
| `text` | string | the transcript of this line |
| `sentence_text` | string | the full sentence the line belongs to |
| `chunk_index` | int | 0-based position of this line within the sentence |
| `text_source` | string | `wikipedia` or `synthetic` (see Licensing) |
| `source` | string | Korean Wikipedia article title, or the synthetic batch name |
| `recorded_at` | string | UTC timestamp of the recording |
| `duration_ms` | int | time from first to last pen sample |
| `num_strokes`, `num_points` | int | sizes of `strokes` |
| `strokes` | list of struct | one struct per pen-down..pen-up stroke, each holding parallel arrays `x`, `y` (Ncode paper coordinates, float), `force` (pen-tip pressure, raw 0..~1000), `t_ms` (ms since the recording's first sample), `tilt_x`, `tilt_y`, `twist` (pen orientation, degrees) |

`x`/`y` are absolute positions on the page in Ncode units (the paper's dot
grid, about 2.4 mm per unit). A written line is roughly 2.5 units tall.
Recordings are not registered to a common origin; models typically consume
deltas between consecutive points.

`data/sentences.parquet` lists each sentence once with its provenance and how
many recordings exist for it.

```python
from datasets import load_dataset

ds = load_dataset("jbaudanza/korean-handwriting-strokes", split="train")
row = ds[0]
print(row["text"], row["num_strokes"])
first = row["strokes"][0]
xy = list(zip(first["x"], first["y"]))
```

## Known noise

Points are published exactly as the pen reported them. Two artefacts are
worth handling:

- **Ncode misreads**: occasionally a single move sample lands far off the
  line (a spike). The training loader drops move points more than a few units
  from the line's median y, and skips any step whose delta is implausibly large.
- **Early recordings without force**: all rows in this release carry force.

The reference loader (`handwriting_dataset.py` in the repository) shows the
exact cleaning used to train the released model.

## How the text was chosen

The first 1,271 sentences are from Korean Wikipedia (dictionary-form prose).
A model trained on those alone had holes: for example, it had almost never
seen the polite spoken ending 요 at the end of a line. The remaining sentences
were generated synthetically with Claude in targeted batches to fill such
gaps:

  - `synthetic-audit-holes`
  - `synthetic-noun-final`
  - `synthetic-thin-syllables`
  - `synthetic-받침`
  - `synthetic-받침-saturation`
  - `synthetic-해요체`

## Licensing and attribution

The dataset is released under **CC BY-SA 4.0**.

- Sentences with `text_source = wikipedia` are quoted from the Korean
  Wikipedia article named in `source`, which is itself
  [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Credit
  Korean Wikipedia and the article when redistributing those transcripts.
- Sentences with `text_source = synthetic` and all stroke data are original to
  this project.

Please attribute as: *Korean Handwriting Strokes by Jonathan Baudanza
(hangul.ink), handwriting by Jo YW, CC BY-SA 4.0; transcripts partly
from Korean Wikipedia (CC BY-SA 4.0).*

Use for education, art, research, and products is welcome. Jo YW
agreed to this public release and to being credited by name.
