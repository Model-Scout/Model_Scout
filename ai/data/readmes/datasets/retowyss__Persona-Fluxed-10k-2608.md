---
license: cc-by-4.0
language:
- en
- ja
- ko
- hi
- pt
- es
- vi
- nl
- fr
- de
tags:
- personas
- flux-2-klein
- synthetic
- portrait
task_categories:
- text-to-image
- image-to-text
pretty_name: Persona Fluxed 10k 2608
size_categories:
- 10K<n<100K
---

# Persona Fluxed 10k

Synthetic persona portraits rendered with **FLUX.2-klein-4b** (8-step, 1024x1024) from the NVIDIA `Nemotron-Personas-*` datasets. 
Each persona is grounded in real-world demographic, geographic and
personality-trait distributions for its country (CC BY 4.0 source; no real people).

Currently Nemotron-Personas exist for:

- **USA** — English
- **Japan** — Japanese
- **India** — English, Hindi
- **Brazil** — Portuguese
- **Singapore** — English
- **France** — French
- **Korea** — Korean
- **El Salvador** — Spanish
- **Vietnam** — Vietnamese
- **Belgium** — Dutch, French, German, English

## Structure
One subset per country (10), each with a single `train` split:
PNG files + a `metadata.csv` in the same directory.

## Columns
| column | meaning |
|---|---|
| `file_name` | image file in the same directory |
| `uuid` | source persona id (stable across the 6 fields of one person) |
| `field` | persona facet: professional / sports / arts / travel / culinary / plain |
| `persona_text` | raw source description (native language) |
| `prompt` | exact prompt sent to the model (`"A  photo of: "` + persona_text) |
| `style` | VLM-classified visual style: Photo / Photo-Collage / Digital Art / Other |
| `country` | config slug: usa, japan, india, brazil, singapore, france, korea, el-salvador, vietnam, belgium |
| `source_dataset` | originating `nvidia/Nemotron-Personas-*` repo id |
| `country_meta` | source's native country label |
| `age`, `sex`, `marital_status`, `education_level`, `occupation` | demographic attributes (native-language values, empty where absent) |

## Notes
- ~10k portraits (10 countries x 167 personas x 6 fields).
- `travel` personas frequently render as multi-panel collages; `arts` personas
  drift toward stylized art most often. Filter on `style` as needed.
- Same `uuid` appears up to 6 times (once per facet) — join on `uuid` to group
  the facets of one person.

## License

Both Nemotron and FLUX.2-klein-4b have permissive licenses. 

- The docs and metadata of this dataset shall be considered CC BY 4.0
- No claims or guarantees are made in regards to images - provided as is.