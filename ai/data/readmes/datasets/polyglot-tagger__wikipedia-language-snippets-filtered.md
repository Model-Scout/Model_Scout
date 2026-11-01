---
license: cc-by-sa-3.0
language:
- multilingual
- af
- am
- ar
- as
- ba
- be
- bg
- bn
- bo
- br
- bs
- ca
- ce
- ckb
- cs
- cy
- da
- de
- dv
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- ga
- gd
- gl
- gu
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lb
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- mt
- my
- ne
- nl
- no
- ny
- oc
- om
- or
- pa
- pl
- ps
- pt
- rm
- ro
- ru
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- tg
- th
- ti
- tl
- tr
- tt
- ug
- uk
- ur
- uz
- vi
- xh
- yo
- zh
- zu
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
size_categories:
- 1M<n<10M
---

# Wikipedia Snippets (Filtered)

Filtered sentence snippets in Wikipedia, by taking the first 60% of an article after filtering for stubs. Minor Latin groups are additionally filtered again for English leakage.
Sentences are mostly filtered out for non matching scripts, such as Arabic in a Cyrllic language.
## Files
Each file is in this format for languages in ISO 639 2-letter codes:
- `train/en/en.parquet`
- `train/es/es.parquet`


# From `wikimedia/wikipedia`

### Licensing Information

Copyright licensing information: https://dumps.wikimedia.org/legal.html

All original textual content is licensed under the [GNU Free Documentation License](https://www.gnu.org/licenses/fdl-1.3.html) (GFDL)
and the [Creative Commons Attribution-Share-Alike 3.0 License](https://creativecommons.org/licenses/by-sa/3.0/).
Some text may be available only under the Creative Commons license; see their [Terms of Use](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use) for details.
Text written by some authors may be released under additional licenses or into the public domain.

### Citation Information

```
@ONLINE{wikidump,
    author = "Wikimedia Foundation",
    title  = "Wikimedia Downloads",
    url    = "https://dumps.wikimedia.org"
}
```