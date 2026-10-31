---
configs:
- config_name: all
  data_files:
  - path:
    - all.jsonl.zst
    split: train
  default: true
- config_name: ar
  data_files:
  - path:
    - ar.jsonl.zst
    split: train
- config_name: az
  data_files:
  - path:
    - az.jsonl.zst
    split: train
- config_name: bg
  data_files:
  - path:
    - bg.jsonl.zst
    split: train
- config_name: bn
  data_files:
  - path:
    - bn.jsonl.zst
    split: train
- config_name: ca
  data_files:
  - path:
    - ca.jsonl.zst
    split: train
- config_name: cs
  data_files:
  - path:
    - cs.jsonl.zst
    split: train
- config_name: da
  data_files:
  - path:
    - da.jsonl.zst
    split: train
- config_name: de
  data_files:
  - path:
    - de.jsonl.zst
    split: train
- config_name: el
  data_files:
  - path:
    - el.jsonl.zst
    split: train
- config_name: en
  data_files:
  - path:
    - en.jsonl.zst
    split: train
- config_name: es
  data_files:
  - path:
    - es.jsonl.zst
    split: train
- config_name: et
  data_files:
  - path:
    - et.jsonl.zst
    split: train
- config_name: fa
  data_files:
  - path:
    - fa.jsonl.zst
    split: train
- config_name: fi
  data_files:
  - path:
    - fi.jsonl.zst
    split: train
- config_name: fr
  data_files:
  - path:
    - fr.jsonl.zst
    split: train
- config_name: he
  data_files:
  - path:
    - he.jsonl.zst
    split: train
- config_name: hi
  data_files:
  - path:
    - hi.jsonl.zst
    split: train
- config_name: hu
  data_files:
  - path:
    - hu.jsonl.zst
    split: train
- config_name: hy
  data_files:
  - path:
    - hy.jsonl.zst
    split: train
- config_name: id
  data_files:
  - path:
    - id.jsonl.zst
    split: train
- config_name: is
  data_files:
  - path:
    - is.jsonl.zst
    split: train
- config_name: it
  data_files:
  - path:
    - it.jsonl.zst
    split: train
- config_name: ja
  data_files:
  - path:
    - ja.jsonl.zst
    split: train
- config_name: ka
  data_files:
  - path:
    - ka.jsonl.zst
    split: train
- config_name: kk
  data_files:
  - path:
    - kk.jsonl.zst
    split: train
- config_name: ko
  data_files:
  - path:
    - ko.jsonl.zst
    split: train
- config_name: lt
  data_files:
  - path:
    - lt.jsonl.zst
    split: train
- config_name: lv
  data_files:
  - path:
    - lv.jsonl.zst
    split: train
- config_name: mk
  data_files:
  - path:
    - mk.jsonl.zst
    split: train
- config_name: ml
  data_files:
  - path:
    - ml.jsonl.zst
    split: train
- config_name: mr
  data_files:
  - path:
    - mr.jsonl.zst
    split: train
- config_name: ne
  data_files:
  - path:
    - ne.jsonl.zst
    split: train
- config_name: nl
  data_files:
  - path:
    - nl.jsonl.zst
    split: train
- config_name: 'no'
  data_files:
  - path:
    - no.jsonl.zst
    split: train
- config_name: pl
  data_files:
  - path:
    - pl.jsonl.zst
    split: train
- config_name: pt
  data_files:
  - path:
    - pt.jsonl.zst
    split: train
- config_name: ro
  data_files:
  - path:
    - ro.jsonl.zst
    split: train
- config_name: ru
  data_files:
  - path:
    - ru.jsonl.zst
    split: train
- config_name: sk
  data_files:
  - path:
    - sk.jsonl.zst
    split: train
- config_name: sl
  data_files:
  - path:
    - sl.jsonl.zst
    split: train
- config_name: sq
  data_files:
  - path:
    - sq.jsonl.zst
    split: train
- config_name: sr
  data_files:
  - path:
    - sr.jsonl.zst
    split: train
- config_name: sv
  data_files:
  - path:
    - sv.jsonl.zst
    split: train
- config_name: ta
  data_files:
  - path:
    - ta.jsonl.zst
    split: train
- config_name: th
  data_files:
  - path:
    - th.jsonl.zst
    split: train
- config_name: tr
  data_files:
  - path:
    - tr.jsonl.zst
    split: train
- config_name: uk
  data_files:
  - path:
    - uk.jsonl.zst
    split: train
- config_name: ur
  data_files:
  - path:
    - ur.jsonl.zst
    split: train
- config_name: vi
  data_files:
  - path:
    - vi.jsonl.zst
    split: train
- config_name: zh
  data_files:
  - path:
    - zh.jsonl.zst
    split: train
language:
- multilingual
- ar
- az
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- et
- fa
- fi
- fr
- he
- hi
- hu
- hy
- id
- is
- it
- ja
- ka
- kk
- ko
- lt
- lv
- mk
- ml
- mr
- ne
- nl
- 'no'
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- ta
- th
- tr
- uk
- ur
- vi
- zh
task_categories:
- text-generation
- text-classification
- text-retrieval
size_categories:
- 100K<n<1M
---