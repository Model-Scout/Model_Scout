---
language:
- ar
- bg
- bn
- ca
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fa
- fi
- fr
- ga
- gl
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- ka
- ko
- kw
- lb
- lt
- lv
- ml
- mn
- ms
- nb
- ne
- nl
- pa
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
license: apache-2.0
size_categories:
- 100K<n<1M
tags:
- voice
- intent-recognition
- nlp
- multilingual
- smart-home
- home-assistant
- openvoiceos
- ovos
- templates
- nlu
- speech-recognition
task_categories:
- text-classification
task_ids:
- intent-classification
- slot-filling
pretty_name: OVOS Hass Intent Templates
configs:
- config_name: ar
  data_files: ar/data.jsonl
- config_name: bg
  data_files: bg/data.jsonl
- config_name: bn
  data_files: bn/data.jsonl
- config_name: ca
  data_files: ca/data.jsonl
- config_name: cs
  data_files: cs/data.jsonl
- config_name: cy
  data_files: cy/data.jsonl
- config_name: da
  data_files: da/data.jsonl
- config_name: de
  data_files: de/data.jsonl
- config_name: de_CH
  data_files: de_CH/data.jsonl
- config_name: el
  data_files: el/data.jsonl
- config_name: en
  data_files: en/data.jsonl
- config_name: es
  data_files: es/data.jsonl
- config_name: et
  data_files: et/data.jsonl
- config_name: eu
  data_files: eu/data.jsonl
- config_name: fa
  data_files: fa/data.jsonl
- config_name: fi
  data_files: fi/data.jsonl
- config_name: fr
  data_files: fr/data.jsonl
- config_name: ga
  data_files: ga/data.jsonl
- config_name: gl
  data_files: gl/data.jsonl
- config_name: he
  data_files: he/data.jsonl
- config_name: hi
  data_files: hi/data.jsonl
- config_name: hr
  data_files: hr/data.jsonl
- config_name: hu
  data_files: hu/data.jsonl
- config_name: hy
  data_files: hy/data.jsonl
- config_name: id
  data_files: id/data.jsonl
- config_name: is
  data_files: is/data.jsonl
- config_name: it
  data_files: it/data.jsonl
- config_name: ja
  data_files: ja/data.jsonl
- config_name: ka
  data_files: ka/data.jsonl
- config_name: ko
  data_files: ko/data.jsonl
- config_name: kw
  data_files: kw/data.jsonl
- config_name: lb
  data_files: lb/data.jsonl
- config_name: lt
  data_files: lt/data.jsonl
- config_name: lv
  data_files: lv/data.jsonl
- config_name: ml
  data_files: ml/data.jsonl
- config_name: mn
  data_files: mn/data.jsonl
- config_name: ms
  data_files: ms/data.jsonl
- config_name: nb
  data_files: nb/data.jsonl
- config_name: ne
  data_files: ne/data.jsonl
- config_name: nl
  data_files: nl/data.jsonl
- config_name: pa
  data_files: pa/data.jsonl
- config_name: pl
  data_files: pl/data.jsonl
- config_name: pt
  data_files: pt/data.jsonl
- config_name: pt_BR
  data_files: pt_BR/data.jsonl
- config_name: ro
  data_files: ro/data.jsonl
- config_name: ru
  data_files: ru/data.jsonl
- config_name: sk
  data_files: sk/data.jsonl
- config_name: sl
  data_files: sl/data.jsonl
- config_name: sr
  data_files: sr/data.jsonl
- config_name: sr_Latn
  data_files: sr_Latn/data.jsonl
- config_name: sv
  data_files: sv/data.jsonl
- config_name: sw
  data_files: sw/data.jsonl
- config_name: ta
  data_files: ta/data.jsonl
- config_name: te
  data_files: te/data.jsonl
- config_name: th
  data_files: th/data.jsonl
- config_name: tr
  data_files: tr/data.jsonl
- config_name: uk
  data_files: uk/data.jsonl
- config_name: ur
  data_files: ur/data.jsonl
- config_name: vi
  data_files: vi/data.jsonl
- config_name: zh_CN
  data_files: zh_CN/data.jsonl
- config_name: zh_HK
  data_files: zh_HK/data.jsonl
- config_name: zh_TW
  data_files: zh_TW/data.jsonl
---

> **Purpose.** This dataset was collected specifically for **intent-parser benchmarking**, *independently from any OVOS skill*. Skill-derived utterances tend to overfit the exact phrasings a plugin was tuned on; this data is drawn from a disjoint source so it measures whether an OVOS intent plugin **generalizes** rather than memorizes. It is part of the [OVOS intent-classification datasets](https://huggingface.co/collections/OpenVoiceOS/intent-classification-datasets) used by the [OVOS Plugin Arena](https://github.com/OpenVoiceOS/ovos-plugin-arena) intent benchmark.

## Funding

Developed by [TigreGotico](https://tigregotico.pt) for [OpenVoiceOS](https://openvoiceos.org) as part of **OpenVoiceOS — From Beta to Breakthrough**, funded through the [NGI0 Commons Fund](https://nlnet.nl/commonsfund/), a fund established by [NLnet](https://nlnet.nl) with financial support from the European Commission's [Next Generation Internet](https://ngi.eu) programme (grant agreement No 101135429).


# OVOS Hass Intent Templates

Multilingual voice-command intent templates derived from the Home Assistant
`hassil` grammar library, converted into the OpenVoiceOS **OVOS-INTENT-2**
locale format.

## What's inside

| Config | Rows | Description |
|--------|------|-------------|
| `ar`   | 2,038 | Arabic templates |
| `bg`   | 5,317 | Bulgarian templates |
| `bn`   | 4 | Bengali templates |
| `ca`   | 2,344 | Catalan templates |
| `cs`   | 2,270 | Czech templates |
| `cy`   | 679 | Welsh templates |
| `da`   | 18,384 | Danish templates |
| `de`   | 11,728 | German templates |
| `de_CH`| 1,902 | Swiss German templates |
| `el`   | 1,776 | Greek templates |
| `en`   | 3,804 | English templates |
| `es`   | 9,084 | Spanish templates |
| `et`   | 2 | Estonian templates |
| `eu`   | 430 | Basque templates |
| `fa`   | 3 | Persian templates |
| `fi`   | 8,030 | Finnish templates |
| `fr`   | 3,548 | French templates |
| `ga`   | 53 | Irish templates |
| `gl`   | 7,626 | Galician templates |
| `he`   | 1,674 | Hebrew templates |
| `hi`   | 54 | Hindi templates |
| `hr`   | 8,308 | Croatian templates |
| `hu`   | 2,445 | Hungarian templates |
| `hy`   | 1,223 | Armenian templates |
| `id`   | 34 | Indonesian templates |
| `is`   | 4,311 | Icelandic templates |
| `it`   | 4,175 | Italian templates |
| `ja`   | 93 | Japanese templates |
| `ka`   | 9 | Georgian templates |
| `ko`   | 821 | Korean templates |
| `kw`   | 24 | Cornish templates |
| `lb`   | 405 | Luxembourgish templates |
| `lt`   | 156 | Lithuanian templates |
| `lv`   | 4,233 | Latvian templates |
| `ml`   | 71 | Malayalam templates |
| `mn`   | 4 | Mongolian templates |
| `ms`   | 73 | Malay templates |
| `nb`   | 5,996 | Norwegian Bokmål templates |
| `ne`   | 3,544 | Nepali templates |
| `nl`   | 20,026 | Dutch templates |
| `pa`   | 2 | Punjabi templates |
| `pl`   | 1,893 | Polish templates |
| `pt`   | 2,559 | Portuguese templates |
| `pt_BR`| 3,522 | Brazilian Portuguese templates |
| `ro`   | 4,647 | Romanian templates |
| `ru`   | 4,195 | Russian templates |
| `sk`   | 4,437 | Slovak templates |
| `sl`   | 18,159 | Slovenian templates |
| `sr`   | 5,180 | Serbian templates |
| `sr_Latn`| 7,003 | Serbian (Latin) templates |
| `sv`   | 769 | Swedish templates |
| `sw`   | 4 | Swahili templates |
| `ta`   | 8 | Tamil templates |
| `te`   | 2 | Telugu templates |
| `th`   | 2,808 | Thai templates |
| `tr`   | 18 | Turkish templates |
| `uk`   | 186 | Ukrainian templates |
| `ur`   | 157 | Urdu templates |
| `vi`   | 21,281 | Vietnamese templates |
| `zh_CN`| 3,531 | Chinese (Simplified) templates |
| `zh_HK`| 2,340 | Chinese (Hong Kong) templates |
| `zh_TW`| 5,311 | Chinese (Traditional) templates |

**61 configs** · **~224k rows total**

## Format

One JSONL file per language config (e.g. `en/data.jsonl`, `ar/data.jsonl`). Each line:
```json
{
  "intent_id": "homeassistant:hass_turn_on",
  "domain": "homeassistant",
  "template": "<turn_on> [the|all] [the] {name} [in <the> {area}]",
  "slots": [
    {"name": "name", "examples": ["kitchen light", "living room lamp"]}
  ],
  "expansions": [
    {"keyword": "turn_on", "values": ["turn on", "switch on", "power on"]}
  ]
}
```

### Columns
- `intent_id` — full intent identifier (e.g. `homeassistant:hass_turn_on`)
- `domain` — Home Assistant domain
- `template` — OVOS-INTENT-2 grammar template
- `slots` — list of slots used in the template, with example values
- `expansions` — list of `{keyword, values}` structs for every `<keyword>` reference in the template (empty list if the template has no keyword refs)

## Conversion methodology

1. **Source**: `hassil` YAML grammar files from the Home Assistant
   `intents` repository (upstream community translations).
2. **Grammar rewrite**: `hassil` rules → OVOS-INTENT-2 `.intent` / `.voc` / `.entity`.
3. **Sample expansion**: A bounded depth-first traversal (≤ 20 000 paths) flattens
   the grammar into concrete test utterances; slot values are inlined from
   `.entity` files.
4. **Drops audited**: 2 279 rows were dropped during expansion—1 014 because
   all expansion paths were invalid, 756 due to cartesian explosion past the
   20 k cap, and 509 because the template contained Jinja response-only
   interpolations that cannot be statically flattened.

## Loading

```python
from datasets import load_dataset

# Load a specific language config
ds = load_dataset("OpenVoiceOS/hass-intent-templates", "en")
ds = load_dataset("OpenVoiceOS/hass-intent-templates", "ar")
ds = load_dataset("OpenVoiceOS/hass-intent-templates")
  url = {https://huggingface.co/datasets/OpenVoiceOS/hass-intent-templates}
}
```

## License

Same as upstream Home Assistant `intents` repository: Apache-2.0.
