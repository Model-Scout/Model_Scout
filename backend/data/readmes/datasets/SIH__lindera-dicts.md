---
license: other
language:
  - ja
  - ko
tags:
  - tokenization
  - morphological-analysis
  - japanese
  - korean
  - lindera
  - mecab
  - ipadic
  - unidic
  - ko-dic
pretty_name: Lindera Morpheme Dictionaries (JA + KO)
---

# Lindera Morpheme Dictionaries (JA + KO)

Prebuilt [Lindera](https://github.com/lindera/lindera) binary dictionaries for
Japanese (IPADIC, UniDic) and Korean (ko-dic) morpheme segmentation, packaged
for on-demand download by the
[LDaCA Text Analytics Tools](https://github.com/Australian-Text-Analytics-Platform/ldaca_web_app)
web app.

The web app uses these dictionaries through its `polars-text` Rust extension —
the first time a user runs tokenisation on a Japanese or Korean corpus, the
matching tarball is fetched from this dataset into the per-OS cache directory
(`~/Library/Caches/ldaca/lindera/` on macOS, `~/.cache/ldaca/lindera/` on Linux,
`%LOCALAPPDATA%\ldaca\lindera\` on Windows) and reused for every subsequent
call. Bundling the dicts in the wheel would push the install size past our
hard limit (see
[memory: project_deployment_targets](https://github.com/Australian-Text-Analytics-Platform/ldaca_web_app)),
so we ship the wheel slim and stream the dict here on first use.

## Files

| Tarball | Gzipped | Extracted dir | Source dict |
|---------|---------|---------------|-------------|
| `ipadic-mecab-2.7.0-bin.tar.gz` | ~15 MB | `ipadic-mecab-2.7.0-bin/` | [mecab-ipadic 2.7.0-20250920](https://Lindera.dev/mecab-ipadic-2.7.0-20250920.tar.gz) |
| `unidic-mecab-2.1.2-bin.tar.gz` | ~50 MB | `unidic-mecab-2.1.2-bin/` | [unidic-mecab 2.1.2](https://Lindera.dev/unidic-mecab-2.1.2.tar.gz) |
| `ko-dic-2.1.1-bin.tar.gz` | ~34 MB | `ko-dic-2.1.1-bin/` | [mecab-ko-dic 2.1.1-20180720](https://Lindera.dev/mecab-ko-dic-2.1.1-20180720.tar.gz) |

Each tarball extracts to a directory containing the standard Lindera binary
layout: `matrix.mtx`, `dict.da`, `dict.vals`, `dict.words`, `dict.wordsidx`,
`char_def.bin`, `unk.bin`, `metadata.json`.

## Usage

The dataset is consumed automatically by `polars-text` when a tokenisation
request specifies one of the matching model IDs:

```python
import polars_text as pt
import polars as pl

# First call downloads + caches the dict; subsequent calls hit the cache.
tokens = (
    pl.DataFrame({"text": ["今日は良い天気です"]})
    .lazy()
    .select(pt.tokenize(pl.col("text"), model="lindera-ja-ipadic"))
    .collect()
)
# -> ["今日", "は", "良い", "天気", "です"]
```

Supported model IDs:
- `lindera-ja-ipadic` — Japanese, IPADIC dictionary (recommended default)
- `lindera-ja-unidic` — Japanese, UniDic dictionary (alternative, more accurate
  for modern web/social text)
- `lindera-ko-dic` — Korean, ko-dic dictionary

To override the dataset source (for testing or self-hosting), set the
`LDACA_LINDERA_DICT_REPO` environment variable to a different HF dataset path.

## Reproduce from source

Each tarball is the output of `lindera-cli build` against the upstream MeCab
source dictionary plus the metadata file shipped in the corresponding Lindera
crate (`lindera-ipadic`, `lindera-unidic`, `lindera-ko-dic`):

```bash
cargo install lindera-cli --version 3.0.7

# Example for IPADIC:
curl -sSfL -o mecab-ipadic-2.7.0-20250920.tar.gz \
    https://Lindera.dev/mecab-ipadic-2.7.0-20250920.tar.gz
tar -xzf mecab-ipadic-2.7.0-20250920.tar.gz

lindera build \
    --src mecab-ipadic-2.7.0-20250920 \
    --dest ipadic-mecab-2.7.0-bin \
    --metadata <path-to-lindera-ipadic-crate>/metadata.json

tar -czf ipadic-mecab-2.7.0-bin.tar.gz ipadic-mecab-2.7.0-bin/
```

The upstream MeCab dictionary tarballs have the following MD5s (matching the
values recorded in the lindera-ipadic / lindera-unidic / lindera-ko-dic build
scripts at version 3.0.7):

- mecab-ipadic 2.7.0-20250920: `a95c409f12f1023fce8ef91f991ef042`
- unidic-mecab 2.1.2: `f4502a563e1da44747f61dcd2b269e35`
- mecab-ko-dic 2.1.1-20180720: `b996764e91c96bc89dc32ea208514a96`

## Licensing

Each dictionary inherits the licence of its upstream source. The Lindera build
process is a non-creative format conversion (CSV → binary serialisation) and
does not introduce new copyrightable content.

- **IPADIC** — [IPA Dictionary Licence](https://taku910.github.io/mecab/) (BSD-style,
  attribution required). Original source: NAIST / Institute of Statistical
  Mathematics.
- **UniDic** — BSD-3-Clause / GPL-2 / LGPL-2.1 triple-licensed. Maintained by
  the National Institute for Japanese Language and Linguistics (NINJAL).
- **ko-dic** — [Apache License 2.0](https://github.com/Pusnow/mecab-ko-dic-msvc/blob/master/LICENSE).
  Originally derived from Sejong corpus data, repackaged by the mecab-ko
  project.

Lindera itself (the build tool, not the data) is MIT-licensed.

## Acknowledgements

This dataset is published by the
[Sydney Informatics Hub](https://informatics.sydney.edu.au/) to support text
analytics workflows on the
[Language Data Commons of Australia](https://www.ldaca.edu.au/) infrastructure.

Source dictionaries are the work of their respective maintainers:
- **mecab / IPADIC** — Taku Kudo et al. (Kyoto University, NAIST)
- **UniDic** — National Institute for Japanese Language and Linguistics (NINJAL)
- **mecab-ko-dic** — Pusnow / Eunjeon project, building on Sejong Corpus data
- **Lindera** — Minoru Osuka et al. (the Rust reimplementation that this
  binary format targets)
