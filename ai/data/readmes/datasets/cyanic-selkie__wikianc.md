---
license: cc-by-sa-4.0
pretty_name: WikiAnc
annotations_creators:
- machine-generated
- crowdsourced
language_creators:
- machine-generated
- crowdsourced
task_categories:
- token-classification
multilinguality:
- multilingual
language:
- en
- ceb
- de
- sv
- fr
- nl
- ru
- es
- it
- arz
- pl
- ja
- zh
- vi
- uk
- war
- ar
- pt
- fa
- ca
- sr
- id
- ko
- 'no'
- ce
- fi
- cs
- tr
- hu
- tt
- sh
- ro
#- zh-min-nan
- eu
- ms
- eo
- he
- hy
- da
- bg
- cy
- sk
- azb
- uz
- et
#- simple
- be
- kk
- min
- el
- hr
- lt
- gl
- az
- ur
- sl
- lld
- ka
- nn
- hi
- th
- ta
- bn
- la
- mk
#- zh-yue
- ast
- lv
- af
- tg
- my
- mg
- mr
- sq
- bs
- oc
- te
- ml
- nds
- br
- ky
- sw
- jv
- lmo
- new
- pnb
- vec
- ht
- pms
- ba
- lb
- su
- ku
- ga
- szl
- is
- fy
- cv
- ckb
- pa
- tl
- an
- wuu
- diq
- io
- sco
- vo
- yo
- ne
- ia
- kn
- gu
- als
- ha
- avk
- bar
- crh
- scn
- bpy
- qu
- mn
- nv
- xmf
- ban
- si
- tum
- ps
- ig
- frr
- os
- mzn
#- bat-smg
- or
- sah
- cdo
- gd
- bug
- yi
- sd
- ilo
- am
- nap
- li
- bcl
- fo
- gor
- hsb
#- map-bms
- mai
- shn
- eml
- ace
#- zh-classical
- sa
- as
- wa
- ie
- hyw
- lij
- mhr
- zu
- sn
- hif
- mrj
- bjn
- km
- mni
- hak
#- roa-tara
- pam
- sat
- rue
- nso
- bh
- so
- mi
- se
- myv
- vls
#- nds-nl
- dag
- sc
- co
- ary
- kw
- bo
- vep
- glk
- tk
- kab
- gan
- rw
#- fiu-vro
- ab
- gv
- ug
- nah
- zea
- skr
- frp
- udm
- pcd
- mt
- kv
- csb
- gn
- smn
- ay
- nrm
- ks
- lez
- lfn
- olo
- mwl
- lo
- stq
- ang
- mdf
- fur
- rm
- lad
- kaa
- gom
- ext
- koi
- tyv
- pap
- av
- dsb
- ln
- dty
- tw
#- cbk-zam
- dv
- ksh
- za
- gag
- bxr
- pfl
- lg
- szy
- pag
- blk
- pi
- tay
- haw
- awa
- inh
- krc
- xal
- pdc
- to
- atj
- tcy
- arc
- mnw
- shi
- jam
- kbp
- wo
- anp
- kbd
- nia
- om
- nov
- ki
- nqo
- bi
- xh
- tpi
- ff
- tet
#- roa-rup
- jbo
- fj
- kg
- lbe
- ty
- cu
- guw
- trv
- ami
- srn
- sm
- mad
- alt
- ltg
- gcr
- chr
- tn
- ny
- st
- pih
- got
- rmy
- ee
- pcm
- bm
- ss
- gpe
- ts
- ve
- kcg
- chy
- rn
- ch
- gur
- ik
- ady
- fat
- pnt
- guc
- iu
- pwn
- sg
- din
- ti
- kl
- dz
- cr
tags:
- wikidata
- wikipedia
- wikification
- named-entity-linking
- nel
- entity-linking
- el
- named-entity-disambiguation
- ned
- entity-disambiguation
- ed
configs:
- config_name: ab
  data_files:
  - split: train
    path: "data/ab/train.parquet"
  - split: validation
    path: "data/ab/validation.parquet"
- config_name: ace
  data_files:
  - split: train
    path: "data/ace/train.parquet"
  - split: validation
    path: "data/ace/validation.parquet"
- config_name: ady
  data_files:
  - split: train
    path: "data/ady/train.parquet"
  - split: validation
    path: "data/ady/validation.parquet"
- config_name: af
  data_files:
  - split: train
    path: "data/af/train.parquet"
  - split: validation
    path: "data/af/validation.parquet"
- config_name: als
  data_files:
  - split: train
    path: "data/als/train.parquet"
  - split: validation
    path: "data/als/validation.parquet"
- config_name: alt
  data_files:
  - split: train
    path: "data/alt/train.parquet"
  - split: validation
    path: "data/alt/validation.parquet"
- config_name: am
  data_files:
  - split: train
    path: "data/am/train.parquet"
  - split: validation
    path: "data/am/validation.parquet"
- config_name: ami
  data_files:
  - split: train
    path: "data/ami/train.parquet"
  - split: validation
    path: "data/ami/validation.parquet"
- config_name: an
  data_files:
  - split: train
    path: "data/an/train.parquet"
  - split: validation
    path: "data/an/validation.parquet"
- config_name: ang
  data_files:
  - split: train
    path: "data/ang/train.parquet"
  - split: validation
    path: "data/ang/validation.parquet"
- config_name: anp
  data_files:
  - split: train
    path: "data/anp/train.parquet"
  - split: validation
    path: "data/anp/validation.parquet"
- config_name: ar
  data_files:
  - split: train
    path: "data/ar/train.parquet"
  - split: validation
    path: "data/ar/validation.parquet"
- config_name: arc
  data_files:
  - split: train
    path: "data/arc/train.parquet"
  - split: validation
    path: "data/arc/validation.parquet"
- config_name: ary
  data_files:
  - split: train
    path: "data/ary/train.parquet"
  - split: validation
    path: "data/ary/validation.parquet"
- config_name: arz
  data_files:
  - split: train
    path: "data/arz/train.parquet"
  - split: validation
    path: "data/arz/validation.parquet"
- config_name: as
  data_files:
  - split: train
    path: "data/as/train.parquet"
  - split: validation
    path: "data/as/validation.parquet"
- config_name: ast
  data_files:
  - split: train
    path: "data/ast/train.parquet"
  - split: validation
    path: "data/ast/validation.parquet"
- config_name: atj
  data_files:
  - split: train
    path: "data/atj/train.parquet"
  - split: validation
    path: "data/atj/validation.parquet"
- config_name: av
  data_files:
  - split: train
    path: "data/av/train.parquet"
  - split: validation
    path: "data/av/validation.parquet"
- config_name: avk
  data_files:
  - split: train
    path: "data/avk/train.parquet"
  - split: validation
    path: "data/avk/validation.parquet"
- config_name: awa
  data_files:
  - split: train
    path: "data/awa/train.parquet"
  - split: validation
    path: "data/awa/validation.parquet"
- config_name: ay
  data_files:
  - split: train
    path: "data/ay/train.parquet"
  - split: validation
    path: "data/ay/validation.parquet"
- config_name: az
  data_files:
  - split: train
    path: "data/az/train.parquet"
  - split: validation
    path: "data/az/validation.parquet"
- config_name: azb
  data_files:
  - split: train
    path: "data/azb/train.parquet"
  - split: validation
    path: "data/azb/validation.parquet"
- config_name: ba
  data_files:
  - split: train
    path: "data/ba/train.parquet"
  - split: validation
    path: "data/ba/validation.parquet"
- config_name: ban
  data_files:
  - split: train
    path: "data/ban/train.parquet"
  - split: validation
    path: "data/ban/validation.parquet"
- config_name: bar
  data_files:
  - split: train
    path: "data/bar/train.parquet"
  - split: validation
    path: "data/bar/validation.parquet"
- config_name: bat_smg
  data_files:
  - split: train
    path: "data/bat_smg/train.parquet"
  - split: validation
    path: "data/bat_smg/validation.parquet"
- config_name: bcl
  data_files:
  - split: train
    path: "data/bcl/train.parquet"
  - split: validation
    path: "data/bcl/validation.parquet"
- config_name: be
  data_files:
  - split: train
    path: "data/be/train.parquet"
  - split: validation
    path: "data/be/validation.parquet"
- config_name: bg
  data_files:
  - split: train
    path: "data/bg/train.parquet"
  - split: validation
    path: "data/bg/validation.parquet"
- config_name: bh
  data_files:
  - split: train
    path: "data/bh/train.parquet"
  - split: validation
    path: "data/bh/validation.parquet"
- config_name: bi
  data_files:
  - split: train
    path: "data/bi/train.parquet"
  - split: validation
    path: "data/bi/validation.parquet"
- config_name: bjn
  data_files:
  - split: train
    path: "data/bjn/train.parquet"
  - split: validation
    path: "data/bjn/validation.parquet"
- config_name: blk
  data_files:
  - split: train
    path: "data/blk/train.parquet"
  - split: validation
    path: "data/blk/validation.parquet"
- config_name: bm
  data_files:
  - split: train
    path: "data/bm/train.parquet"
  - split: validation
    path: "data/bm/validation.parquet"
- config_name: bn
  data_files:
  - split: train
    path: "data/bn/train.parquet"
  - split: validation
    path: "data/bn/validation.parquet"
- config_name: bo
  data_files:
  - split: train
    path: "data/bo/train.parquet"
  - split: validation
    path: "data/bo/validation.parquet"
- config_name: bpy
  data_files:
  - split: train
    path: "data/bpy/train.parquet"
  - split: validation
    path: "data/bpy/validation.parquet"
- config_name: br
  data_files:
  - split: train
    path: "data/br/train.parquet"
  - split: validation
    path: "data/br/validation.parquet"
- config_name: bs
  data_files:
  - split: train
    path: "data/bs/train.parquet"
  - split: validation
    path: "data/bs/validation.parquet"
- config_name: bug
  data_files:
  - split: train
    path: "data/bug/train.parquet"
  - split: validation
    path: "data/bug/validation.parquet"
- config_name: bxr
  data_files:
  - split: train
    path: "data/bxr/train.parquet"
  - split: validation
    path: "data/bxr/validation.parquet"
- config_name: ca
  data_files:
  - split: train
    path: "data/ca/train.parquet"
  - split: validation
    path: "data/ca/validation.parquet"
- config_name: cbk_zam
  data_files:
  - split: train
    path: "data/cbk_zam/train.parquet"
  - split: validation
    path: "data/cbk_zam/validation.parquet"
- config_name: cdo
  data_files:
  - split: train
    path: "data/cdo/train.parquet"
  - split: validation
    path: "data/cdo/validation.parquet"
- config_name: ce
  data_files:
  - split: train
    path: "data/ce/train.parquet"
  - split: validation
    path: "data/ce/validation.parquet"
- config_name: ceb
  data_files:
  - split: train
    path: "data/ceb/train.parquet"
  - split: validation
    path: "data/ceb/validation.parquet"
- config_name: ch
  data_files:
  - split: train
    path: "data/ch/train.parquet"
  - split: validation
    path: "data/ch/validation.parquet"
- config_name: chr
  data_files:
  - split: train
    path: "data/chr/train.parquet"
  - split: validation
    path: "data/chr/validation.parquet"
- config_name: chy
  data_files:
  - split: train
    path: "data/chy/train.parquet"
  - split: validation
    path: "data/chy/validation.parquet"
- config_name: ckb
  data_files:
  - split: train
    path: "data/ckb/train.parquet"
  - split: validation
    path: "data/ckb/validation.parquet"
- config_name: co
  data_files:
  - split: train
    path: "data/co/train.parquet"
  - split: validation
    path: "data/co/validation.parquet"
- config_name: cr
  data_files:
  - split: train
    path: "data/cr/train.parquet"
  - split: validation
    path: "data/cr/validation.parquet"
- config_name: crh
  data_files:
  - split: train
    path: "data/crh/train.parquet"
  - split: validation
    path: "data/crh/validation.parquet"
- config_name: cs
  data_files:
  - split: train
    path: "data/cs/train.parquet"
  - split: validation
    path: "data/cs/validation.parquet"
- config_name: csb
  data_files:
  - split: train
    path: "data/csb/train.parquet"
  - split: validation
    path: "data/csb/validation.parquet"
- config_name: cu
  data_files:
  - split: train
    path: "data/cu/train.parquet"
  - split: validation
    path: "data/cu/validation.parquet"
- config_name: cv
  data_files:
  - split: train
    path: "data/cv/train.parquet"
  - split: validation
    path: "data/cv/validation.parquet"
- config_name: cy
  data_files:
  - split: train
    path: "data/cy/train.parquet"
  - split: validation
    path: "data/cy/validation.parquet"
- config_name: da
  data_files:
  - split: train
    path: "data/da/train.parquet"
  - split: validation
    path: "data/da/validation.parquet"
- config_name: dag
  data_files:
  - split: train
    path: "data/dag/train.parquet"
  - split: validation
    path: "data/dag/validation.parquet"
- config_name: de
  data_files:
  - split: train
    path: "data/de/train.parquet"
  - split: validation
    path: "data/de/validation.parquet"
- config_name: din
  data_files:
  - split: train
    path: "data/din/train.parquet"
  - split: validation
    path: "data/din/validation.parquet"
- config_name: diq
  data_files:
  - split: train
    path: "data/diq/train.parquet"
  - split: validation
    path: "data/diq/validation.parquet"
- config_name: dsb
  data_files:
  - split: train
    path: "data/dsb/train.parquet"
  - split: validation
    path: "data/dsb/validation.parquet"
- config_name: dty
  data_files:
  - split: train
    path: "data/dty/train.parquet"
  - split: validation
    path: "data/dty/validation.parquet"
- config_name: dv
  data_files:
  - split: train
    path: "data/dv/train.parquet"
  - split: validation
    path: "data/dv/validation.parquet"
- config_name: dz
  data_files:
  - split: train
    path: "data/dz/train.parquet"
  - split: validation
    path: "data/dz/validation.parquet"
- config_name: ee
  data_files:
  - split: train
    path: "data/ee/train.parquet"
  - split: validation
    path: "data/ee/validation.parquet"
- config_name: el
  data_files:
  - split: train
    path: "data/el/train.parquet"
  - split: validation
    path: "data/el/validation.parquet"
- config_name: eml
  data_files:
  - split: train
    path: "data/eml/train.parquet"
  - split: validation
    path: "data/eml/validation.parquet"
- config_name: en
  data_files:
  - split: train
    path: "data/en/train.parquet"
  - split: validation
    path: "data/en/validation.parquet"
- config_name: eo
  data_files:
  - split: train
    path: "data/eo/train.parquet"
  - split: validation
    path: "data/eo/validation.parquet"
- config_name: es
  data_files:
  - split: train
    path: "data/es/train.parquet"
  - split: validation
    path: "data/es/validation.parquet"
- config_name: et
  data_files:
  - split: train
    path: "data/et/train.parquet"
  - split: validation
    path: "data/et/validation.parquet"
- config_name: eu
  data_files:
  - split: train
    path: "data/eu/train.parquet"
  - split: validation
    path: "data/eu/validation.parquet"
- config_name: ext
  data_files:
  - split: train
    path: "data/ext/train.parquet"
  - split: validation
    path: "data/ext/validation.parquet"
- config_name: fa
  data_files:
  - split: train
    path: "data/fa/train.parquet"
  - split: validation
    path: "data/fa/validation.parquet"
- config_name: fat
  data_files:
  - split: train
    path: "data/fat/train.parquet"
  - split: validation
    path: "data/fat/validation.parquet"
- config_name: ff
  data_files:
  - split: train
    path: "data/ff/train.parquet"
  - split: validation
    path: "data/ff/validation.parquet"
- config_name: fi
  data_files:
  - split: train
    path: "data/fi/train.parquet"
  - split: validation
    path: "data/fi/validation.parquet"
- config_name: fiu_vro
  data_files:
  - split: train
    path: "data/fiu_vro/train.parquet"
  - split: validation
    path: "data/fiu_vro/validation.parquet"
- config_name: fj
  data_files:
  - split: train
    path: "data/fj/train.parquet"
  - split: validation
    path: "data/fj/validation.parquet"
- config_name: fo
  data_files:
  - split: train
    path: "data/fo/train.parquet"
  - split: validation
    path: "data/fo/validation.parquet"
- config_name: fr
  data_files:
  - split: train
    path: "data/fr/train.parquet"
  - split: validation
    path: "data/fr/validation.parquet"
- config_name: frp
  data_files:
  - split: train
    path: "data/frp/train.parquet"
  - split: validation
    path: "data/frp/validation.parquet"
- config_name: frr
  data_files:
  - split: train
    path: "data/frr/train.parquet"
  - split: validation
    path: "data/frr/validation.parquet"
- config_name: fur
  data_files:
  - split: train
    path: "data/fur/train.parquet"
  - split: validation
    path: "data/fur/validation.parquet"
- config_name: fy
  data_files:
  - split: train
    path: "data/fy/train.parquet"
  - split: validation
    path: "data/fy/validation.parquet"
- config_name: ga
  data_files:
  - split: train
    path: "data/ga/train.parquet"
  - split: validation
    path: "data/ga/validation.parquet"
- config_name: gag
  data_files:
  - split: train
    path: "data/gag/train.parquet"
  - split: validation
    path: "data/gag/validation.parquet"
- config_name: gan
  data_files:
  - split: train
    path: "data/gan/train.parquet"
  - split: validation
    path: "data/gan/validation.parquet"
- config_name: gcr
  data_files:
  - split: train
    path: "data/gcr/train.parquet"
  - split: validation
    path: "data/gcr/validation.parquet"
- config_name: gd
  data_files:
  - split: train
    path: "data/gd/train.parquet"
  - split: validation
    path: "data/gd/validation.parquet"
- config_name: gl
  data_files:
  - split: train
    path: "data/gl/train.parquet"
  - split: validation
    path: "data/gl/validation.parquet"
- config_name: glk
  data_files:
  - split: train
    path: "data/glk/train.parquet"
  - split: validation
    path: "data/glk/validation.parquet"
- config_name: gn
  data_files:
  - split: train
    path: "data/gn/train.parquet"
  - split: validation
    path: "data/gn/validation.parquet"
- config_name: gom
  data_files:
  - split: train
    path: "data/gom/train.parquet"
  - split: validation
    path: "data/gom/validation.parquet"
- config_name: gor
  data_files:
  - split: train
    path: "data/gor/train.parquet"
  - split: validation
    path: "data/gor/validation.parquet"
- config_name: got
  data_files:
  - split: train
    path: "data/got/train.parquet"
  - split: validation
    path: "data/got/validation.parquet"
- config_name: gpe
  data_files:
  - split: train
    path: "data/gpe/train.parquet"
  - split: validation
    path: "data/gpe/validation.parquet"
- config_name: gu
  data_files:
  - split: train
    path: "data/gu/train.parquet"
  - split: validation
    path: "data/gu/validation.parquet"
- config_name: guc
  data_files:
  - split: train
    path: "data/guc/train.parquet"
  - split: validation
    path: "data/guc/validation.parquet"
- config_name: gur
  data_files:
  - split: train
    path: "data/gur/train.parquet"
  - split: validation
    path: "data/gur/validation.parquet"
- config_name: guw
  data_files:
  - split: train
    path: "data/guw/train.parquet"
  - split: validation
    path: "data/guw/validation.parquet"
- config_name: gv
  data_files:
  - split: train
    path: "data/gv/train.parquet"
  - split: validation
    path: "data/gv/validation.parquet"
- config_name: ha
  data_files:
  - split: train
    path: "data/ha/train.parquet"
  - split: validation
    path: "data/ha/validation.parquet"
- config_name: hak
  data_files:
  - split: train
    path: "data/hak/train.parquet"
  - split: validation
    path: "data/hak/validation.parquet"
- config_name: haw
  data_files:
  - split: train
    path: "data/haw/train.parquet"
  - split: validation
    path: "data/haw/validation.parquet"
- config_name: he
  data_files:
  - split: train
    path: "data/he/train.parquet"
  - split: validation
    path: "data/he/validation.parquet"
- config_name: hi
  data_files:
  - split: train
    path: "data/hi/train.parquet"
  - split: validation
    path: "data/hi/validation.parquet"
- config_name: hif
  data_files:
  - split: train
    path: "data/hif/train.parquet"
  - split: validation
    path: "data/hif/validation.parquet"
- config_name: hr
  data_files:
  - split: train
    path: "data/hr/train.parquet"
  - split: validation
    path: "data/hr/validation.parquet"
- config_name: hsb
  data_files:
  - split: train
    path: "data/hsb/train.parquet"
  - split: validation
    path: "data/hsb/validation.parquet"
- config_name: ht
  data_files:
  - split: train
    path: "data/ht/train.parquet"
  - split: validation
    path: "data/ht/validation.parquet"
- config_name: hu
  data_files:
  - split: train
    path: "data/hu/train.parquet"
  - split: validation
    path: "data/hu/validation.parquet"
- config_name: hy
  data_files:
  - split: train
    path: "data/hy/train.parquet"
  - split: validation
    path: "data/hy/validation.parquet"
- config_name: hyw
  data_files:
  - split: train
    path: "data/hyw/train.parquet"
  - split: validation
    path: "data/hyw/validation.parquet"
- config_name: ia
  data_files:
  - split: train
    path: "data/ia/train.parquet"
  - split: validation
    path: "data/ia/validation.parquet"
- config_name: id
  data_files:
  - split: train
    path: "data/id/train.parquet"
  - split: validation
    path: "data/id/validation.parquet"
- config_name: ie
  data_files:
  - split: train
    path: "data/ie/train.parquet"
  - split: validation
    path: "data/ie/validation.parquet"
- config_name: ig
  data_files:
  - split: train
    path: "data/ig/train.parquet"
  - split: validation
    path: "data/ig/validation.parquet"
- config_name: ik
  data_files:
  - split: train
    path: "data/ik/train.parquet"
  - split: validation
    path: "data/ik/validation.parquet"
- config_name: ilo
  data_files:
  - split: train
    path: "data/ilo/train.parquet"
  - split: validation
    path: "data/ilo/validation.parquet"
- config_name: inh
  data_files:
  - split: train
    path: "data/inh/train.parquet"
  - split: validation
    path: "data/inh/validation.parquet"
- config_name: io
  data_files:
  - split: train
    path: "data/io/train.parquet"
  - split: validation
    path: "data/io/validation.parquet"
- config_name: is
  data_files:
  - split: train
    path: "data/is/train.parquet"
  - split: validation
    path: "data/is/validation.parquet"
- config_name: it
  data_files:
  - split: train
    path: "data/it/train.parquet"
  - split: validation
    path: "data/it/validation.parquet"
- config_name: iu
  data_files:
  - split: train
    path: "data/iu/train.parquet"
  - split: validation
    path: "data/iu/validation.parquet"
- config_name: ja
  data_files:
  - split: train
    path: "data/ja/train.parquet"
  - split: validation
    path: "data/ja/validation.parquet"
- config_name: jam
  data_files:
  - split: train
    path: "data/jam/train.parquet"
  - split: validation
    path: "data/jam/validation.parquet"
- config_name: jbo
  data_files:
  - split: train
    path: "data/jbo/train.parquet"
  - split: validation
    path: "data/jbo/validation.parquet"
- config_name: jv
  data_files:
  - split: train
    path: "data/jv/train.parquet"
  - split: validation
    path: "data/jv/validation.parquet"
- config_name: ka
  data_files:
  - split: train
    path: "data/ka/train.parquet"
  - split: validation
    path: "data/ka/validation.parquet"
- config_name: kaa
  data_files:
  - split: train
    path: "data/kaa/train.parquet"
  - split: validation
    path: "data/kaa/validation.parquet"
- config_name: kab
  data_files:
  - split: train
    path: "data/kab/train.parquet"
  - split: validation
    path: "data/kab/validation.parquet"
- config_name: kbd
  data_files:
  - split: train
    path: "data/kbd/train.parquet"
  - split: validation
    path: "data/kbd/validation.parquet"
- config_name: kbp
  data_files:
  - split: train
    path: "data/kbp/train.parquet"
  - split: validation
    path: "data/kbp/validation.parquet"
- config_name: kcg
  data_files:
  - split: train
    path: "data/kcg/train.parquet"
  - split: validation
    path: "data/kcg/validation.parquet"
- config_name: kg
  data_files:
  - split: train
    path: "data/kg/train.parquet"
  - split: validation
    path: "data/kg/validation.parquet"
- config_name: ki
  data_files:
  - split: train
    path: "data/ki/train.parquet"
  - split: validation
    path: "data/ki/validation.parquet"
- config_name: kk
  data_files:
  - split: train
    path: "data/kk/train.parquet"
  - split: validation
    path: "data/kk/validation.parquet"
- config_name: kl
  data_files:
  - split: train
    path: "data/kl/train.parquet"
  - split: validation
    path: "data/kl/validation.parquet"
- config_name: km
  data_files:
  - split: train
    path: "data/km/train.parquet"
  - split: validation
    path: "data/km/validation.parquet"
- config_name: kn
  data_files:
  - split: train
    path: "data/kn/train.parquet"
  - split: validation
    path: "data/kn/validation.parquet"
- config_name: ko
  data_files:
  - split: train
    path: "data/ko/train.parquet"
  - split: validation
    path: "data/ko/validation.parquet"
- config_name: koi
  data_files:
  - split: train
    path: "data/koi/train.parquet"
  - split: validation
    path: "data/koi/validation.parquet"
- config_name: krc
  data_files:
  - split: train
    path: "data/krc/train.parquet"
  - split: validation
    path: "data/krc/validation.parquet"
- config_name: ks
  data_files:
  - split: train
    path: "data/ks/train.parquet"
  - split: validation
    path: "data/ks/validation.parquet"
- config_name: ksh
  data_files:
  - split: train
    path: "data/ksh/train.parquet"
  - split: validation
    path: "data/ksh/validation.parquet"
- config_name: ku
  data_files:
  - split: train
    path: "data/ku/train.parquet"
  - split: validation
    path: "data/ku/validation.parquet"
- config_name: kv
  data_files:
  - split: train
    path: "data/kv/train.parquet"
  - split: validation
    path: "data/kv/validation.parquet"
- config_name: kw
  data_files:
  - split: train
    path: "data/kw/train.parquet"
  - split: validation
    path: "data/kw/validation.parquet"
- config_name: ky
  data_files:
  - split: train
    path: "data/ky/train.parquet"
  - split: validation
    path: "data/ky/validation.parquet"
- config_name: la
  data_files:
  - split: train
    path: "data/la/train.parquet"
  - split: validation
    path: "data/la/validation.parquet"
- config_name: lad
  data_files:
  - split: train
    path: "data/lad/train.parquet"
  - split: validation
    path: "data/lad/validation.parquet"
- config_name: lb
  data_files:
  - split: train
    path: "data/lb/train.parquet"
  - split: validation
    path: "data/lb/validation.parquet"
- config_name: lbe
  data_files:
  - split: train
    path: "data/lbe/train.parquet"
  - split: validation
    path: "data/lbe/validation.parquet"
- config_name: lez
  data_files:
  - split: train
    path: "data/lez/train.parquet"
  - split: validation
    path: "data/lez/validation.parquet"
- config_name: lfn
  data_files:
  - split: train
    path: "data/lfn/train.parquet"
  - split: validation
    path: "data/lfn/validation.parquet"
- config_name: lg
  data_files:
  - split: train
    path: "data/lg/train.parquet"
  - split: validation
    path: "data/lg/validation.parquet"
- config_name: li
  data_files:
  - split: train
    path: "data/li/train.parquet"
  - split: validation
    path: "data/li/validation.parquet"
- config_name: lij
  data_files:
  - split: train
    path: "data/lij/train.parquet"
  - split: validation
    path: "data/lij/validation.parquet"
- config_name: lld
  data_files:
  - split: train
    path: "data/lld/train.parquet"
  - split: validation
    path: "data/lld/validation.parquet"
- config_name: lmo
  data_files:
  - split: train
    path: "data/lmo/train.parquet"
  - split: validation
    path: "data/lmo/validation.parquet"
- config_name: ln
  data_files:
  - split: train
    path: "data/ln/train.parquet"
  - split: validation
    path: "data/ln/validation.parquet"
- config_name: lo
  data_files:
  - split: train
    path: "data/lo/train.parquet"
  - split: validation
    path: "data/lo/validation.parquet"
- config_name: lt
  data_files:
  - split: train
    path: "data/lt/train.parquet"
  - split: validation
    path: "data/lt/validation.parquet"
- config_name: ltg
  data_files:
  - split: train
    path: "data/ltg/train.parquet"
  - split: validation
    path: "data/ltg/validation.parquet"
- config_name: lv
  data_files:
  - split: train
    path: "data/lv/train.parquet"
  - split: validation
    path: "data/lv/validation.parquet"
- config_name: mad
  data_files:
  - split: train
    path: "data/mad/train.parquet"
  - split: validation
    path: "data/mad/validation.parquet"
- config_name: mai
  data_files:
  - split: train
    path: "data/mai/train.parquet"
  - split: validation
    path: "data/mai/validation.parquet"
- config_name: map_bms
  data_files:
  - split: train
    path: "data/map_bms/train.parquet"
  - split: validation
    path: "data/map_bms/validation.parquet"
- config_name: mdf
  data_files:
  - split: train
    path: "data/mdf/train.parquet"
  - split: validation
    path: "data/mdf/validation.parquet"
- config_name: mg
  data_files:
  - split: train
    path: "data/mg/train.parquet"
  - split: validation
    path: "data/mg/validation.parquet"
- config_name: mhr
  data_files:
  - split: train
    path: "data/mhr/train.parquet"
  - split: validation
    path: "data/mhr/validation.parquet"
- config_name: mi
  data_files:
  - split: train
    path: "data/mi/train.parquet"
  - split: validation
    path: "data/mi/validation.parquet"
- config_name: min
  data_files:
  - split: train
    path: "data/min/train.parquet"
  - split: validation
    path: "data/min/validation.parquet"
- config_name: mk
  data_files:
  - split: train
    path: "data/mk/train.parquet"
  - split: validation
    path: "data/mk/validation.parquet"
- config_name: ml
  data_files:
  - split: train
    path: "data/ml/train.parquet"
  - split: validation
    path: "data/ml/validation.parquet"
- config_name: mn
  data_files:
  - split: train
    path: "data/mn/train.parquet"
  - split: validation
    path: "data/mn/validation.parquet"
- config_name: mni
  data_files:
  - split: train
    path: "data/mni/train.parquet"
  - split: validation
    path: "data/mni/validation.parquet"
- config_name: mnw
  data_files:
  - split: train
    path: "data/mnw/train.parquet"
  - split: validation
    path: "data/mnw/validation.parquet"
- config_name: mr
  data_files:
  - split: train
    path: "data/mr/train.parquet"
  - split: validation
    path: "data/mr/validation.parquet"
- config_name: mrj
  data_files:
  - split: train
    path: "data/mrj/train.parquet"
  - split: validation
    path: "data/mrj/validation.parquet"
- config_name: ms
  data_files:
  - split: train
    path: "data/ms/train.parquet"
  - split: validation
    path: "data/ms/validation.parquet"
- config_name: mt
  data_files:
  - split: train
    path: "data/mt/train.parquet"
  - split: validation
    path: "data/mt/validation.parquet"
- config_name: mwl
  data_files:
  - split: train
    path: "data/mwl/train.parquet"
  - split: validation
    path: "data/mwl/validation.parquet"
- config_name: my
  data_files:
  - split: train
    path: "data/my/train.parquet"
  - split: validation
    path: "data/my/validation.parquet"
- config_name: myv
  data_files:
  - split: train
    path: "data/myv/train.parquet"
  - split: validation
    path: "data/myv/validation.parquet"
- config_name: mzn
  data_files:
  - split: train
    path: "data/mzn/train.parquet"
  - split: validation
    path: "data/mzn/validation.parquet"
- config_name: nah
  data_files:
  - split: train
    path: "data/nah/train.parquet"
  - split: validation
    path: "data/nah/validation.parquet"
- config_name: nap
  data_files:
  - split: train
    path: "data/nap/train.parquet"
  - split: validation
    path: "data/nap/validation.parquet"
- config_name: nds
  data_files:
  - split: train
    path: "data/nds/train.parquet"
  - split: validation
    path: "data/nds/validation.parquet"
- config_name: nds_nl
  data_files:
  - split: train
    path: "data/nds_nl/train.parquet"
  - split: validation
    path: "data/nds_nl/validation.parquet"
- config_name: ne
  data_files:
  - split: train
    path: "data/ne/train.parquet"
  - split: validation
    path: "data/ne/validation.parquet"
- config_name: new
  data_files:
  - split: train
    path: "data/new/train.parquet"
  - split: validation
    path: "data/new/validation.parquet"
- config_name: nia
  data_files:
  - split: train
    path: "data/nia/train.parquet"
  - split: validation
    path: "data/nia/validation.parquet"
- config_name: nl
  data_files:
  - split: train
    path: "data/nl/train.parquet"
  - split: validation
    path: "data/nl/validation.parquet"
- config_name: nn
  data_files:
  - split: train
    path: "data/nn/train.parquet"
  - split: validation
    path: "data/nn/validation.parquet"
- config_name: 'no'
  data_files:
  - split: train
    path: "data/no/train.parquet"
  - split: validation
    path: "data/no/validation.parquet"
- config_name: nov
  data_files:
  - split: train
    path: "data/nov/train.parquet"
  - split: validation
    path: "data/nov/validation.parquet"
- config_name: nqo
  data_files:
  - split: train
    path: "data/nqo/train.parquet"
  - split: validation
    path: "data/nqo/validation.parquet"
- config_name: nrm
  data_files:
  - split: train
    path: "data/nrm/train.parquet"
  - split: validation
    path: "data/nrm/validation.parquet"
- config_name: nso
  data_files:
  - split: train
    path: "data/nso/train.parquet"
  - split: validation
    path: "data/nso/validation.parquet"
- config_name: nv
  data_files:
  - split: train
    path: "data/nv/train.parquet"
  - split: validation
    path: "data/nv/validation.parquet"
- config_name: ny
  data_files:
  - split: train
    path: "data/ny/train.parquet"
  - split: validation
    path: "data/ny/validation.parquet"
- config_name: oc
  data_files:
  - split: train
    path: "data/oc/train.parquet"
  - split: validation
    path: "data/oc/validation.parquet"
- config_name: olo
  data_files:
  - split: train
    path: "data/olo/train.parquet"
  - split: validation
    path: "data/olo/validation.parquet"
- config_name: om
  data_files:
  - split: train
    path: "data/om/train.parquet"
  - split: validation
    path: "data/om/validation.parquet"
- config_name: or
  data_files:
  - split: train
    path: "data/or/train.parquet"
  - split: validation
    path: "data/or/validation.parquet"
- config_name: os
  data_files:
  - split: train
    path: "data/os/train.parquet"
  - split: validation
    path: "data/os/validation.parquet"
- config_name: pa
  data_files:
  - split: train
    path: "data/pa/train.parquet"
  - split: validation
    path: "data/pa/validation.parquet"
- config_name: pag
  data_files:
  - split: train
    path: "data/pag/train.parquet"
  - split: validation
    path: "data/pag/validation.parquet"
- config_name: pam
  data_files:
  - split: train
    path: "data/pam/train.parquet"
  - split: validation
    path: "data/pam/validation.parquet"
- config_name: pap
  data_files:
  - split: train
    path: "data/pap/train.parquet"
  - split: validation
    path: "data/pap/validation.parquet"
- config_name: pcd
  data_files:
  - split: train
    path: "data/pcd/train.parquet"
  - split: validation
    path: "data/pcd/validation.parquet"
- config_name: pcm
  data_files:
  - split: train
    path: "data/pcm/train.parquet"
  - split: validation
    path: "data/pcm/validation.parquet"
- config_name: pdc
  data_files:
  - split: train
    path: "data/pdc/train.parquet"
  - split: validation
    path: "data/pdc/validation.parquet"
- config_name: pfl
  data_files:
  - split: train
    path: "data/pfl/train.parquet"
  - split: validation
    path: "data/pfl/validation.parquet"
- config_name: pi
  data_files:
  - split: train
    path: "data/pi/train.parquet"
  - split: validation
    path: "data/pi/validation.parquet"
- config_name: pih
  data_files:
  - split: train
    path: "data/pih/train.parquet"
  - split: validation
    path: "data/pih/validation.parquet"
- config_name: pl
  data_files:
  - split: train
    path: "data/pl/train.parquet"
  - split: validation
    path: "data/pl/validation.parquet"
- config_name: pms
  data_files:
  - split: train
    path: "data/pms/train.parquet"
  - split: validation
    path: "data/pms/validation.parquet"
- config_name: pnb
  data_files:
  - split: train
    path: "data/pnb/train.parquet"
  - split: validation
    path: "data/pnb/validation.parquet"
- config_name: pnt
  data_files:
  - split: train
    path: "data/pnt/train.parquet"
  - split: validation
    path: "data/pnt/validation.parquet"
- config_name: ps
  data_files:
  - split: train
    path: "data/ps/train.parquet"
  - split: validation
    path: "data/ps/validation.parquet"
- config_name: pt
  data_files:
  - split: train
    path: "data/pt/train.parquet"
  - split: validation
    path: "data/pt/validation.parquet"
- config_name: pwn
  data_files:
  - split: train
    path: "data/pwn/train.parquet"
  - split: validation
    path: "data/pwn/validation.parquet"
- config_name: qu
  data_files:
  - split: train
    path: "data/qu/train.parquet"
  - split: validation
    path: "data/qu/validation.parquet"
- config_name: rm
  data_files:
  - split: train
    path: "data/rm/train.parquet"
  - split: validation
    path: "data/rm/validation.parquet"
- config_name: rmy
  data_files:
  - split: train
    path: "data/rmy/train.parquet"
  - split: validation
    path: "data/rmy/validation.parquet"
- config_name: rn
  data_files:
  - split: train
    path: "data/rn/train.parquet"
  - split: validation
    path: "data/rn/validation.parquet"
- config_name: ro
  data_files:
  - split: train
    path: "data/ro/train.parquet"
  - split: validation
    path: "data/ro/validation.parquet"
- config_name: roa_rup
  data_files:
  - split: train
    path: "data/roa_rup/train.parquet"
  - split: validation
    path: "data/roa_rup/validation.parquet"
- config_name: roa_tara
  data_files:
  - split: train
    path: "data/roa_tara/train.parquet"
  - split: validation
    path: "data/roa_tara/validation.parquet"
- config_name: ru
  data_files:
  - split: train
    path: "data/ru/train.parquet"
  - split: validation
    path: "data/ru/validation.parquet"
- config_name: rue
  data_files:
  - split: train
    path: "data/rue/train.parquet"
  - split: validation
    path: "data/rue/validation.parquet"
- config_name: rw
  data_files:
  - split: train
    path: "data/rw/train.parquet"
  - split: validation
    path: "data/rw/validation.parquet"
- config_name: sa
  data_files:
  - split: train
    path: "data/sa/train.parquet"
  - split: validation
    path: "data/sa/validation.parquet"
- config_name: sah
  data_files:
  - split: train
    path: "data/sah/train.parquet"
  - split: validation
    path: "data/sah/validation.parquet"
- config_name: sat
  data_files:
  - split: train
    path: "data/sat/train.parquet"
  - split: validation
    path: "data/sat/validation.parquet"
- config_name: sc
  data_files:
  - split: train
    path: "data/sc/train.parquet"
  - split: validation
    path: "data/sc/validation.parquet"
- config_name: scn
  data_files:
  - split: train
    path: "data/scn/train.parquet"
  - split: validation
    path: "data/scn/validation.parquet"
- config_name: sco
  data_files:
  - split: train
    path: "data/sco/train.parquet"
  - split: validation
    path: "data/sco/validation.parquet"
- config_name: sd
  data_files:
  - split: train
    path: "data/sd/train.parquet"
  - split: validation
    path: "data/sd/validation.parquet"
- config_name: se
  data_files:
  - split: train
    path: "data/se/train.parquet"
  - split: validation
    path: "data/se/validation.parquet"
- config_name: sg
  data_files:
  - split: train
    path: "data/sg/train.parquet"
  - split: validation
    path: "data/sg/validation.parquet"
- config_name: sh
  data_files:
  - split: train
    path: "data/sh/train.parquet"
  - split: validation
    path: "data/sh/validation.parquet"
- config_name: shi
  data_files:
  - split: train
    path: "data/shi/train.parquet"
  - split: validation
    path: "data/shi/validation.parquet"
- config_name: shn
  data_files:
  - split: train
    path: "data/shn/train.parquet"
  - split: validation
    path: "data/shn/validation.parquet"
- config_name: si
  data_files:
  - split: train
    path: "data/si/train.parquet"
  - split: validation
    path: "data/si/validation.parquet"
- config_name: simple
  data_files:
  - split: train
    path: "data/simple/train.parquet"
  - split: validation
    path: "data/simple/validation.parquet"
- config_name: sk
  data_files:
  - split: train
    path: "data/sk/train.parquet"
  - split: validation
    path: "data/sk/validation.parquet"
- config_name: skr
  data_files:
  - split: train
    path: "data/skr/train.parquet"
  - split: validation
    path: "data/skr/validation.parquet"
- config_name: sl
  data_files:
  - split: train
    path: "data/sl/train.parquet"
  - split: validation
    path: "data/sl/validation.parquet"
- config_name: sm
  data_files:
  - split: train
    path: "data/sm/train.parquet"
  - split: validation
    path: "data/sm/validation.parquet"
- config_name: smn
  data_files:
  - split: train
    path: "data/smn/train.parquet"
  - split: validation
    path: "data/smn/validation.parquet"
- config_name: sn
  data_files:
  - split: train
    path: "data/sn/train.parquet"
  - split: validation
    path: "data/sn/validation.parquet"
- config_name: so
  data_files:
  - split: train
    path: "data/so/train.parquet"
  - split: validation
    path: "data/so/validation.parquet"
- config_name: sq
  data_files:
  - split: train
    path: "data/sq/train.parquet"
  - split: validation
    path: "data/sq/validation.parquet"
- config_name: sr
  data_files:
  - split: train
    path: "data/sr/train.parquet"
  - split: validation
    path: "data/sr/validation.parquet"
- config_name: srn
  data_files:
  - split: train
    path: "data/srn/train.parquet"
  - split: validation
    path: "data/srn/validation.parquet"
- config_name: ss
  data_files:
  - split: train
    path: "data/ss/train.parquet"
  - split: validation
    path: "data/ss/validation.parquet"
- config_name: st
  data_files:
  - split: train
    path: "data/st/train.parquet"
  - split: validation
    path: "data/st/validation.parquet"
- config_name: stq
  data_files:
  - split: train
    path: "data/stq/train.parquet"
  - split: validation
    path: "data/stq/validation.parquet"
- config_name: su
  data_files:
  - split: train
    path: "data/su/train.parquet"
  - split: validation
    path: "data/su/validation.parquet"
- config_name: sv
  data_files:
  - split: train
    path: "data/sv/train.parquet"
  - split: validation
    path: "data/sv/validation.parquet"
- config_name: sw
  data_files:
  - split: train
    path: "data/sw/train.parquet"
  - split: validation
    path: "data/sw/validation.parquet"
- config_name: szl
  data_files:
  - split: train
    path: "data/szl/train.parquet"
  - split: validation
    path: "data/szl/validation.parquet"
- config_name: szy
  data_files:
  - split: train
    path: "data/szy/train.parquet"
  - split: validation
    path: "data/szy/validation.parquet"
- config_name: ta
  data_files:
  - split: train
    path: "data/ta/train.parquet"
  - split: validation
    path: "data/ta/validation.parquet"
- config_name: tay
  data_files:
  - split: train
    path: "data/tay/train.parquet"
  - split: validation
    path: "data/tay/validation.parquet"
- config_name: tcy
  data_files:
  - split: train
    path: "data/tcy/train.parquet"
  - split: validation
    path: "data/tcy/validation.parquet"
- config_name: te
  data_files:
  - split: train
    path: "data/te/train.parquet"
  - split: validation
    path: "data/te/validation.parquet"
- config_name: tet
  data_files:
  - split: train
    path: "data/tet/train.parquet"
  - split: validation
    path: "data/tet/validation.parquet"
- config_name: tg
  data_files:
  - split: train
    path: "data/tg/train.parquet"
  - split: validation
    path: "data/tg/validation.parquet"
- config_name: th
  data_files:
  - split: train
    path: "data/th/train.parquet"
  - split: validation
    path: "data/th/validation.parquet"
- config_name: ti
  data_files:
  - split: train
    path: "data/ti/train.parquet"
  - split: validation
    path: "data/ti/validation.parquet"
- config_name: tk
  data_files:
  - split: train
    path: "data/tk/train.parquet"
  - split: validation
    path: "data/tk/validation.parquet"
- config_name: tl
  data_files:
  - split: train
    path: "data/tl/train.parquet"
  - split: validation
    path: "data/tl/validation.parquet"
- config_name: tn
  data_files:
  - split: train
    path: "data/tn/train.parquet"
  - split: validation
    path: "data/tn/validation.parquet"
- config_name: to
  data_files:
  - split: train
    path: "data/to/train.parquet"
  - split: validation
    path: "data/to/validation.parquet"
- config_name: tpi
  data_files:
  - split: train
    path: "data/tpi/train.parquet"
  - split: validation
    path: "data/tpi/validation.parquet"
- config_name: tr
  data_files:
  - split: train
    path: "data/tr/train.parquet"
  - split: validation
    path: "data/tr/validation.parquet"
- config_name: trv
  data_files:
  - split: train
    path: "data/trv/train.parquet"
  - split: validation
    path: "data/trv/validation.parquet"
- config_name: ts
  data_files:
  - split: train
    path: "data/ts/train.parquet"
  - split: validation
    path: "data/ts/validation.parquet"
- config_name: tt
  data_files:
  - split: train
    path: "data/tt/train.parquet"
  - split: validation
    path: "data/tt/validation.parquet"
- config_name: tum
  data_files:
  - split: train
    path: "data/tum/train.parquet"
  - split: validation
    path: "data/tum/validation.parquet"
- config_name: tw
  data_files:
  - split: train
    path: "data/tw/train.parquet"
  - split: validation
    path: "data/tw/validation.parquet"
- config_name: ty
  data_files:
  - split: train
    path: "data/ty/train.parquet"
  - split: validation
    path: "data/ty/validation.parquet"
- config_name: tyv
  data_files:
  - split: train
    path: "data/tyv/train.parquet"
  - split: validation
    path: "data/tyv/validation.parquet"
- config_name: udm
  data_files:
  - split: train
    path: "data/udm/train.parquet"
  - split: validation
    path: "data/udm/validation.parquet"
- config_name: ug
  data_files:
  - split: train
    path: "data/ug/train.parquet"
  - split: validation
    path: "data/ug/validation.parquet"
- config_name: uk
  data_files:
  - split: train
    path: "data/uk/train.parquet"
  - split: validation
    path: "data/uk/validation.parquet"
- config_name: ur
  data_files:
  - split: train
    path: "data/ur/train.parquet"
  - split: validation
    path: "data/ur/validation.parquet"
- config_name: uz
  data_files:
  - split: train
    path: "data/uz/train.parquet"
  - split: validation
    path: "data/uz/validation.parquet"
- config_name: ve
  data_files:
  - split: train
    path: "data/ve/train.parquet"
  - split: validation
    path: "data/ve/validation.parquet"
- config_name: vec
  data_files:
  - split: train
    path: "data/vec/train.parquet"
  - split: validation
    path: "data/vec/validation.parquet"
- config_name: vep
  data_files:
  - split: train
    path: "data/vep/train.parquet"
  - split: validation
    path: "data/vep/validation.parquet"
- config_name: vi
  data_files:
  - split: train
    path: "data/vi/train.parquet"
  - split: validation
    path: "data/vi/validation.parquet"
- config_name: vls
  data_files:
  - split: train
    path: "data/vls/train.parquet"
  - split: validation
    path: "data/vls/validation.parquet"
- config_name: vo
  data_files:
  - split: train
    path: "data/vo/train.parquet"
  - split: validation
    path: "data/vo/validation.parquet"
- config_name: wa
  data_files:
  - split: train
    path: "data/wa/train.parquet"
  - split: validation
    path: "data/wa/validation.parquet"
- config_name: war
  data_files:
  - split: train
    path: "data/war/train.parquet"
  - split: validation
    path: "data/war/validation.parquet"
- config_name: wo
  data_files:
  - split: train
    path: "data/wo/train.parquet"
  - split: validation
    path: "data/wo/validation.parquet"
- config_name: wuu
  data_files:
  - split: train
    path: "data/wuu/train.parquet"
  - split: validation
    path: "data/wuu/validation.parquet"
- config_name: xal
  data_files:
  - split: train
    path: "data/xal/train.parquet"
  - split: validation
    path: "data/xal/validation.parquet"
- config_name: xh
  data_files:
  - split: train
    path: "data/xh/train.parquet"
  - split: validation
    path: "data/xh/validation.parquet"
- config_name: xmf
  data_files:
  - split: train
    path: "data/xmf/train.parquet"
  - split: validation
    path: "data/xmf/validation.parquet"
- config_name: yi
  data_files:
  - split: train
    path: "data/yi/train.parquet"
  - split: validation
    path: "data/yi/validation.parquet"
- config_name: yo
  data_files:
  - split: train
    path: "data/yo/train.parquet"
  - split: validation
    path: "data/yo/validation.parquet"
- config_name: za
  data_files:
  - split: train
    path: "data/za/train.parquet"
  - split: validation
    path: "data/za/validation.parquet"
- config_name: zea
  data_files:
  - split: train
    path: "data/zea/train.parquet"
  - split: validation
    path: "data/zea/validation.parquet"
- config_name: zh
  data_files:
  - split: train
    path: "data/zh/train.parquet"
  - split: validation
    path: "data/zh/validation.parquet"
- config_name: zh_classical
  data_files:
  - split: train
    path: "data/zh_classical/train.parquet"
  - split: validation
    path: "data/zh_classical/validation.parquet"
- config_name: zh_min_nan
  data_files:
  - split: train
    path: "data/zh_min_nan/train.parquet"
  - split: validation
    path: "data/zh_min_nan/validation.parquet"
- config_name: zh_yue
  data_files:
  - split: train
    path: "data/zh_yue/train.parquet"
  - split: validation
    path: "data/zh_yue/validation.parquet"
- config_name: zu
  data_files:
  - split: train
    path: "data/zu/train.parquet"
  - split: validation
    path: "data/zu/validation.parquet"
---

# Dataset Card for WikiAnc

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)

## Dataset Description

- **Repository:** [WikiAnc repository](https://github.com/cyanic-selkie/wikianc)

### Dataset Summary

The WikiAnc dataset is an automatically generated dataset from Wikipedia (all languages) and Wikidata dumps (August, 2023). 

The code for generating the dataset can be found [here](https://github.com/cyanic-selkie/wikianc).

### Supported Tasks

- `wikificiation`: The dataset can be used to train a model for Wikification.
- `named-entity-linking`: The dataset can be used to train a model for Named Entity Linking.

### Languages

The text in the dataset is in all 320 Wikipedia languages. The full list can be found in the table below.

## Dataset Structure

### Data Instances

A typical data point represents a paragraph in a Wikipedia article.

The `paragraph_text` field contains the original text in an NFC normalized, UTF-8 encoded string.

The `paragraph_anchors` field contains a list of anchors, each represented by a struct with the inclusive starting UTF-8 code point `start` field, exclusive ending UTF-8 code point `end` field, a nullable `qid` field, a nullable `pageid` field, and an NFC normalized, UTF-8 encoded `title` (Wikipedia) field.

Additionally, each paragraph has `article_title`, `article_pageid`, and (nullable) `article_qid` fields referring to the article the paragraph came from.

There is also a nullable, NFC normalized, UTF-8 encoded `section_heading` field, and an integer `section_level` field referring to the heading (if it exists) of the article section, and the level in the section hierarchy that the paragraph came from.

The `qid` fields refers to Wikidata's QID identifiers, while the `pageid` and `title` fields refer to Wikipedia's pageID and title identifiers (there is a one-to-one mapping between pageIDs and titles).

**NOTE:** An anchor will always have a `title`, but that doesn't mean it has to have a `pageid`. This is because Wikipedia allows defining anchors to nonexistent articles.

An example from the WikiAnc EN test set looks as follows:

```
{
  "uuid": "5f74e678-944f-4761-a5e0-b6426f6f61b8",
  "article_title": "Climatius",
  "article_pageid": 5394373,
  "article_qid": 867987,
  "section_heading": null,
  "section_level": 0,
  "paragraph_text": "It was a small fish, at 7.5 cm, and to discourage predators, Climatius sported fifteen sharp spines. There was one spine each on the paired pelvic and pectoral fins, and on the aingle anal and two dorsal fins, and a four pairs without fins on the fish's underside.",
  "paragraph_anchors": [
    {
      "start": 140,
      "end": 146,
      "qid": 3335089,
      "pageid": 56849833,
      "title": "Pelvic_fin"
    },
    {
      "start": 151,
      "end": 159,
      "qid": 4162555,
      "pageid": 331956,
      "title": "Pectoral_fin"
    },
    {
      "start": 184,
      "end": 188,
      "qid": 4162555,
      "pageid": 331958,
      "title": "Anal_fin"
    },
    {
      "start": 197,
      "end": 208,
      "qid": 1568355,
      "pageid": 294244,
      "title": "Dorsal_fin"
    }
  ]
}
```

### Data Fields

- `uuid`: a UTF-8 encoded string representing a v4 UUID that uniquely identifies the example
- `article_title`: an NFC normalized, UTF-8 encoded Wikipedia title of the article; spaces are replaced with underscores 
- `article_pageid`: an integer representing the Wikipedia pageID of the article
- `article_qid`: an integer representing the Wikidata QID this article refers to; it can be null if the entity didn't exist in Wikidata at the time of the creation of the original dataset
- `section_heading`: a nullable, NFC normalized, UTF-8 encoded string representing the section heading
- `section_level`: an integer representing the level of the section in the section hierarchy
- `paragraph_text`: an NFC normalized, UTF-8 encoded string representing the paragraph
- `paragraph_anchors`: a list of structs representing anchors, each anchor has:
  - `start`: an integer representing the inclusive starting UTF-8 code point of the anchors
  - `end`: an integer representing the exclusive ending UTF-8 code point of the anchor
  - `qid`: a nullable integer representing the Wikidata QID this anchor refers to; it can be null if the entity didn't exist in Wikidata at the time of the creation of the original dataset
  - `pageid`: a nullable integer representing the Wikipedia pageID of the anchor; it can be null if the article didn't exist in Wikipedia at the time of the creation of the original dataset
  - `title`: an NFC normalized, UTF-8 encoded string representing the Wikipedia title of the anchor; spaces are replaced with underscores; can refer to a nonexistent Wikipedia article 

### Data Splits

The data is split into training, validation and test sets; paragraphs belonging to the same article aren't necessarily in the same split. The final split sizes are as follows:

#### Train

| | Articles | Paragraphs | Anchors | Anchors with QIDs | Anchors with PageIDs | 
| :-- | --: | --: | --: | --: | --: |
| ab | 2378 | 5678 | 10515 | 3649 | 3650 |
| ace | 12591 | 23969 | 48638 | 25150 | 25175 |
| ady | 596 | 1662 | 2694 | 1593 | 1606 |
| af | 104470 | 399038 | 985640 | 900596 | 900967 |
| als | 27999 | 165085 | 402049 | 294742 | 294744 |
| alt | 1043 | 7468 | 9158 | 5446 | 5452 |
| am | 13576 | 46318 | 90051 | 51915 | 52173 |
| ami | 1582 | 12428 | 6080 | 1505 | 2579 |
| an | 40179 | 121367 | 669830 | 516248 | 516822 |
| ang | 3833 | 9664 | 24297 | 10189 | 10229 |
| anp | 2506 | 6865 | 14560 | 3825 | 5061 |
| ar | 1132271 | 3617491 | 11657228 | 11240112 | 11244160 |
| arc | 1844 | 3766 | 9232 | 5460 | 5545 |
| ary | 6736 | 17049 | 50185 | 34193 | 34227 |
| arz | 1579782 | 3693549 | 7879303 | 6906799 | 6917393 |
| as | 11947 | 77835 | 122760 | 67594 | 67720 |
| ast | 126992 | 877278 | 2952000 | 1775764 | 1777383 |
| atj | 1872 | 3820 | 6544 | 3247 | 3365 |
| av | 3048 | 8542 | 16115 | 8895 | 9000 |
| avk | 27577 | 85219 | 106100 | 32260 | 33491 |
| awa | 3396 | 5802 | 6617 | 1679 | 2370 |
| ay | 5102 | 15125 | 22802 | 13930 | 13933 |
| az | 180810 | 789902 | 1570889 | 1377797 | 1380325 |
| azb | 240990 | 585386 | 1241661 | 749575 | 753318 |
| ba | 62269 | 391926 | 625645 | 562730 | 563181 |
| ban | 18955 | 44138 | 86239 | 66213 | 66412 |
| bar | 26057 | 83298 | 185158 | 109082 | 109091 |
| bat_smg | 17013 | 41951 | 77417 | 51701 | 51733 |
| bcl | 13783 | 45457 | 78963 | 47819 | 47861 |
| be | 222883 | 821135 | 2499258 | 2204062 | 2204117 |
| bg | 285156 | 1336530 | 3967713 | 3618800 | 3627798 |
| bh | 7658 | 17052 | 29110 | 22157 | 22217 |
| bi | 1403 | 1712 | 3172 | 1991 | 1995 |
| bjn | 9672 | 19007 | 58660 | 32538 | 33071 |
| blk | 2786 | 11825 | 11341 | 5979 | 6129 |
| bm | 1111 | 2421 | 2451 | 1217 | 1218 |
| bn | 136921 | 736388 | 1530942 | 1161967 | 1162761 |
| bo | 11843 | 37121 | 8241 | 6265 | 6359 |
| bpy | 24742 | 115606 | 166906 | 86166 | 86170 |
| br | 78524 | 214128 | 657375 | 527295 | 527606 |
| bs | 86407 | 382114 | 1246030 | 965782 | 966511 |
| bug | 14231 | 14484 | 53879 | 14787 | 15146 |
| bxr | 2730 | 9571 | 27853 | 11560 | 11567 |
| ca | 691444 | 3596667 | 11359870 | 10236358 | 10237666 |
| cbk_zam | 2989 | 8322 | 9939 | 2790 | 2847 |
| cdo | 15922 | 30059 | 63474 | 29659 | 29705 |
| ce | 597137 | 2121587 | 3097393 | 1507129 | 1507806 |
| ceb | 5888811 | 11920613 | 37969424 | 33678489 | 33962205 |
| ch | 574 | 1166 | 2290 | 492 | 601 |
| chr | 980 | 1110 | 1311 | 779 | 790 |
| chy | 711 | 753 | 494 | 428 | 428 |
| ckb | 48903 | 163599 | 435662 | 224749 | 226749 |
| co | 6719 | 22954 | 46391 | 24149 | 24229 |
| cr | 158 | 216 | 209 | 94 | 94 |
| crh | 24117 | 29781 | 98534 | 70231 | 70235 |
| cs | 516037 | 2679537 | 9917806 | 8763103 | 8763291 |
| csb | 5315 | 14009 | 31294 | 16820 | 16820 |
| cu | 1171 | 2796 | 5283 | 2346 | 2349 |
| cv | 50525 | 157542 | 375399 | 166889 | 167497 |
| cy | 276031 | 992900 | 2011030 | 1613064 | 1620632 |
| da | 284765 | 1167917 | 4352733 | 3854239 | 3854549 |
| dag | 9248 | 29213 | 46084 | 10981 | 14213 |
| de | 2780056 | 16093948 | 52497421 | 50480495 | 50480548 |
| din | 485 | 1551 | 1096 | 197 | 197 |
| diq | 37565 | 70969 | 155656 | 141636 | 141695 |
| dsb | 3083 | 8760 | 19397 | 9652 | 9652 |
| dty | 3339 | 6219 | 7505 | 4417 | 4447 |
| dv | 4190 | 16809 | 7906 | 3612 | 3620 |
| dz | 652 | 2623 | 272 | 94 | 100 |
| ee | 1075 | 2326 | 1823 | 861 | 926 |
| el | 224207 | 1527561 | 4181433 | 3119952 | 3121967 |
| eml | 12169 | 53861 | 115729 | 65775 | 65940 |
| en | 6514924 | 40656507 | 109681826 | 107761324 | 107768438 |
| eo | 330486 | 1116191 | 4257655 | 3975927 | 3979379 |
| es | 1792062 | 10890435 | 33729712 | 31581851 | 31648945 |
| et | 233078 | 1110906 | 3558448 | 2879595 | 2886824 |
| eu | 386029 | 1405747 | 3398477 | 3025183 | 3030635 |
| ext | 3472 | 9626 | 20554 | 11966 | 11978 |
| fa | 901254 | 2357271 | 6189352 | 5862106 | 5870803 |
| fat | 1044 | 6092 | 1717 | 120 | 857 |
| ff | 1763 | 4103 | 3483 | 2304 | 2413 |
| fi | 373226 | 1667296 | 5221239 | 4658292 | 4663471 |
| fiu_vro | 6417 | 19897 | 40418 | 23563 | 23609 |
| fj | 1157 | 1782 | 4852 | 1910 | 1911 |
| fo | 11809 | 30828 | 119267 | 95117 | 95259 |
| fr | 2432972 | 15252697 | 43564517 | 42573624 | 42589064 |
| frp | 5341 | 10574 | 36358 | 24905 | 24926 |
| frr | 16038 | 30821 | 80265 | 68184 | 68315 |
| fur | 3665 | 10651 | 29516 | 16249 | 16278 |
| fy | 46011 | 206153 | 1271339 | 985227 | 985511 |
| ga | 52168 | 130535 | 347037 | 288261 | 288309 |
| gag | 2408 | 4844 | 8551 | 4520 | 4520 |
| gan | 4219 | 9689 | 18994 | 14119 | 14128 |
| gcr | 2227 | 5163 | 2763 | 1186 | 1186 |
| gd | 15850 | 48217 | 141290 | 95557 | 95562 |
| gl | 190419 | 910543 | 3674404 | 2937660 | 2938634 |
| glk | 6484 | 15344 | 32631 | 21395 | 21447 |
| gn | 5064 | 15481 | 40641 | 30389 | 30440 |
| gom | 4192 | 37508 | 14192 | 2369 | 2382 |
| gor | 14388 | 28133 | 107341 | 66191 | 67016 |
| got | 960 | 2186 | 4093 | 1404 | 1415 |
| gpe | 899 | 3383 | 1199 | 796 | 815 |
| gu | 30025 | 114805 | 459063 | 348651 | 348731 |
| guc | 546 | 2545 | 2300 | 1025 | 1138 |
| gur | 1010 | 5043 | 1761 | 227 | 244 |
| guw | 1263 | 3719 | 7474 | 3116 | 5375 |
| gv | 5036 | 12213 | 48801 | 19659 | 19663 |
| ha | 31977 | 149096 | 115029 | 97167 | 98184 |
| hak | 8694 | 11505 | 39744 | 28150 | 28152 |
| haw | 2470 | 5810 | 11169 | 5700 | 5705 |
| he | 323472 | 2648617 | 10904148 | 10367532 | 10379886 |
| hi | 150121 | 538451 | 964251 | 795726 | 798254 |
| hif | 10534 | 21169 | 43463 | 23970 | 24316 |
| hr | 189415 | 876107 | 3210326 | 2752205 | 2758602 |
| hsb | 13183 | 40760 | 91863 | 66632 | 66633 |
| ht | 64850 | 154160 | 201547 | 166206 | 167961 |
| hu | 346711 | 1859683 | 5267990 | 4707580 | 4710525 |
| hy | 298066 | 1542920 | 3767938 | 2689014 | 2690466 |
| hyw | 11358 | 83640 | 161227 | 82218 | 84817 |
| ia | 24581 | 43289 | 129914 | 96517 | 96595 |
| id | 620895 | 2138237 | 6589957 | 5629372 | 5644832 |
| ie | 11020 | 22342 | 60890 | 46054 | 46122 |
| ig | 19448 | 110907 | 57963 | 31022 | 31298 |
| ik | 737 | 1016 | 848 | 551 | 580 |
| ilo | 14135 | 74304 | 126533 | 75701 | 75705 |
| inh | 1754 | 4640 | 13284 | 5770 | 6011 |
| io | 36312 | 101555 | 303765 | 258933 | 259001 |
| is | 54348 | 170321 | 574897 | 436767 | 437784 |
| it | 1610989 | 8718610 | 27447754 | 26116131 | 26126157 |
| iu | 502 | 757 | 536 | 414 | 418 |
| ja | 1355269 | 9276459 | 29002111 | 27752954 | 27801000 |
| jam | 1571 | 2260 | 5887 | 3588 | 3590 |
| jbo | 1287 | 3088 | 5831 | 546 | 546 |
| jv | 66323 | 148710 | 547010 | 381682 | 382052 |
| ka | 167161 | 695865 | 2275552 | 422090 | 422095 |
| kaa | 3540 | 9814 | 12930 | 5312 | 5752 |
| kab | 5346 | 14709 | 36889 | 22000 | 22050 |
| kbd | 1549 | 6348 | 14594 | 5277 | 5280 |
| kbp | 1846 | 6005 | 7119 | 6875 | 6880 |
| kcg | 871 | 1839 | 2953 | 1857 | 1871 |
| kg | 1187 | 1933 | 3835 | 2292 | 2295 |
| ki | 1482 | 2899 | 2035 | 1386 | 1649 |
| kk | 235740 | 889990 | 1840304 | 1143049 | 1151399 |
| kl | 282 | 1024 | 1337 | 302 | 302 |
| km | 11422 | 84697 | 111378 | 40954 | 41529 |
| kn | 30729 | 261724 | 432994 | 188536 | 188807 |
| ko | 606386 | 2159706 | 6217786 | 5715559 | 5725614 |
| koi | 3260 | 9065 | 17068 | 10628 | 10628 |
| krc | 1465 | 6234 | 18092 | 7294 | 7311 |
| ks | 4176 | 9446 | 15252 | 5917 | 6226 |
| ksh | 2836 | 11043 | 26577 | 9484 | 9496 |
| ku | 55166 | 112840 | 269080 | 208679 | 210304 |
| kv | 5236 | 13396 | 32141 | 26727 | 26744 |
| kw | 6884 | 18901 | 49462 | 28074 | 28194 |
| ky | 75426 | 191772 | 271376 | 189656 | 190133 |
| la | 124150 | 240343 | 1456464 | 1283285 | 1283728 |
| lad | 3538 | 11910 | 37456 | 19124 | 19124 |
| lb | 57747 | 178507 | 573528 | 443583 | 444601 |
| lbe | 1205 | 2249 | 4470 | 2543 | 2543 |
| lez | 4067 | 16675 | 36970 | 25834 | 25842 |
| lfn | 4506 | 21746 | 29785 | 14554 | 14560 |
| lg | 3814 | 23386 | 15539 | 2088 | 2724 |
| li | 14134 | 58711 | 212772 | 137110 | 137367 |
| lij | 8092 | 23366 | 61410 | 34939 | 34940 |
| lld | 152613 | 158049 | 578033 | 443976 | 458150 |
| lmo | 67387 | 136650 | 373890 | 274174 | 274612 |
| ln | 3132 | 6066 | 11086 | 7838 | 7874 |
| lo | 4734 | 15005 | 27132 | 8562 | 8799 |
| lt | 204135 | 775863 | 2687983 | 2406710 | 2414909 |
| ltg | 1018 | 2979 | 5815 | 2190 | 2193 |
| lv | 118530 | 437086 | 1458341 | 1244609 | 1247181 |
| mad | 1113 | 3500 | 3762 | 1149 | 1157 |
| mai | 13285 | 22572 | 53246 | 38119 | 38128 |
| map_bms | 10875 | 16411 | 67964 | 51125 | 51137 |
| mdf | 4002 | 11043 | 21658 | 9178 | 9183 |
| mg | 92227 | 213580 | 328751 | 265931 | 267633 |
| mhr | 11010 | 33013 | 60771 | 38153 | 38220 |
| mi | 7274 | 10154 | 29052 | 24854 | 25216 |
| min | 223075 | 422381 | 1315030 | 513108 | 515548 |
| mk | 131522 | 695456 | 1984109 | 1639280 | 1640744 |
| ml | 84334 | 415940 | 797903 | 485482 | 486324 |
| mn | 23434 | 124485 | 295548 | 142014 | 142984 |
| mni | 10354 | 18872 | 29474 | 18810 | 19876 |
| mnw | 3136 | 34165 | 9342 | 1908 | 2387 |
| mr | 92464 | 326662 | 633452 | 383501 | 392709 |
| mrj | 10156 | 20132 | 48416 | 24098 | 24098 |
| ms | 344459 | 988647 | 2424535 | 1932685 | 1937647 |
| mt | 5381 | 49856 | 104636 | 51251 | 51278 |
| mwl | 4402 | 37271 | 127176 | 25729 | 26366 |
| my | 103938 | 334243 | 445026 | 300567 | 303288 |
| myv | 7515 | 21592 | 36762 | 26570 | 26591 |
| mzn | 17364 | 39937 | 89805 | 46962 | 47020 |
| nah | 5934 | 12478 | 30805 | 13093 | 14364 |
| nap | 11235 | 22336 | 41891 | 20798 | 20804 |
| nds | 79228 | 242004 | 583941 | 305374 | 305422 |
| nds_nl | 6484 | 28252 | 94875 | 51767 | 51785 |
| ne | 30359 | 91033 | 153937 | 124841 | 125078 |
| new | 71653 | 245033 | 454251 | 289444 | 289912 |
| nia | 1496 | 4047 | 4524 | 2258 | 2812 |
| nl | 1948842 | 5867108 | 17953497 | 16886996 | 16893078 |
| nn | 160106 | 549454 | 1751481 | 1375622 | 1376155 |
| no | 591000 | 2213493 | 7050421 | 6471776 | 6476157 |
| nov | 1341 | 3711 | 7466 | 3948 | 3955 |
| nqo | 1489 | 9858 | 23633 | 6056 | 6981 |
| nrm | 4571 | 14279 | 38935 | 33295 | 33321 |
| nso | 7618 | 9505 | 36826 | 35621 | 35623 |
| nv | 21911 | 57663 | 123762 | 107139 | 107139 |
| ny | 1060 | 3164 | 4750 | 1455 | 1490 |
| oc | 85099 | 303185 | 1035051 | 791403 | 792043 |
| olo | 4348 | 14334 | 18704 | 8634 | 8647 |
| om | 1710 | 7496 | 8222 | 4333 | 4416 |
| or | 17027 | 76677 | 137274 | 57023 | 57064 |
| os | 17468 | 40488 | 80943 | 48124 | 48414 |
| pa | 50421 | 226354 | 344239 | 197594 | 198080 |
| pag | 2533 | 41416 | 4150 | 2907 | 2907 |
| pam | 7816 | 16493 | 53785 | 29375 | 29715 |
| pap | 3153 | 12086 | 22157 | 18161 | 18233 |
| pcd | 5272 | 12203 | 15602 | 12319 | 12360 |
| pcm | 1019 | 4631 | 4161 | 1160 | 1261 |
| pdc | 2009 | 5406 | 8151 | 4122 | 4144 |
| pfl | 2717 | 14024 | 26150 | 10291 | 10294 |
| pi | 2972 | 5959 | 7773 | 201 | 201 |
| pih | 829 | 1065 | 2857 | 2016 | 2018 |
| pl | 1468194 | 5599437 | 19364191 | 18389560 | 18405120 |
| pms | 66552 | 170133 | 369956 | 308593 | 314917 |
| pnb | 67534 | 402101 | 937247 | 525105 | 533265 |
| pnt | 497 | 1467 | 3553 | 1715 | 1716 |
| ps | 19254 | 134868 | 72493 | 36348 | 36899 |
| pt | 1048823 | 5226543 | 16811382 | 15714686 | 15714890 |
| pwn | 328 | 1825 | 990 | 428 | 430 |
| qu | 22365 | 47078 | 133032 | 106686 | 106708 |
| rm | 3569 | 27345 | 47169 | 20460 | 20490 |
| rmy | 911 | 2221 | 4235 | 1854 | 1965 |
| rn | 726 | 1641 | 1436 | 594 | 601 |
| ro | 417630 | 1518438 | 4282072 | 3764830 | 3765626 |
| roa_rup | 1270 | 2751 | 4641 | 2527 | 2537 |
| roa_tara | 8407 | 18031 | 42040 | 14330 | 14331 |
| ru | 1889271 | 12344758 | 30796034 | 29268121 | 29288089 |
| rue | 7369 | 21429 | 61022 | 43241 | 43256 |
| rw | 7793 | 35619 | 38066 | 19821 | 20967 |
| sa | 12069 | 78188 | 104193 | 40307 | 41518 |
| sah | 16007 | 76450 | 82154 | 61041 | 61412 |
| sat | 8655 | 43624 | 57493 | 28497 | 28820 |
| sc | 6919 | 24434 | 66719 | 44707 | 44733 |
| scn | 21990 | 49686 | 132583 | 102735 | 102774 |
| sco | 34097 | 86464 | 301450 | 148184 | 148406 |
| sd | 16228 | 48679 | 79392 | 34572 | 35729 |
| se | 6101 | 10531 | 25844 | 17978 | 18010 |
| sg | 473 | 537 | 318 | 184 | 184 |
| sh | 445218 | 1213741 | 4337559 | 3858400 | 3860253 |
| shi | 1650 | 6036 | 10364 | 4715 | 4926 |
| shn | 10653 | 51542 | 46976 | 29925 | 29993 |
| si | 21959 | 132932 | 146935 | 55158 | 56422 |
| simple | 224811 | 618711 | 2014692 | 1689101 | 1689185 |
| sk | 230073 | 845501 | 2867955 | 2468707 | 2469129 |
| skr | 5505 | 62742 | 38412 | 15004 | 21015 |
| sl | 175804 | 810714 | 2597824 | 2067682 | 2068522 |
| sm | 995 | 1591 | 3838 | 2515 | 2523 |
| smn | 5004 | 12483 | 37008 | 22440 | 22492 |
| sn | 10159 | 19527 | 40437 | 31573 | 32763 |
| so | 8540 | 36173 | 53012 | 42913 | 43548 |
| sq | 94941 | 371562 | 699210 | 520709 | 522241 |
| sr | 657766 | 2331205 | 6562651 | 5257496 | 5264077 |
| srn | 1171 | 3050 | 6637 | 1752 | 1941 |
| ss | 783 | 2124 | 2382 | 1127 | 1139 |
| st | 982 | 1971 | 2510 | 1689 | 1701 |
| stq | 3648 | 10972 | 29713 | 15919 | 15920 |
| su | 57552 | 122590 | 496201 | 384518 | 384891 |
| sv | 2418380 | 5019466 | 22263222 | 21445193 | 21445441 |
| sw | 75109 | 218219 | 798980 | 688743 | 692052 |
| szl | 56229 | 109496 | 473528 | 129434 | 129479 |
| szy | 4628 | 49166 | 18867 | 2419 | 3187 |
| ta | 157642 | 780711 | 1642095 | 1141032 | 1142372 |
| tay | 2643 | 15831 | 10104 | 1496 | 5312 |
| tcy | 2135 | 9932 | 11073 | 4680 | 4745 |
| te | 83866 | 719826 | 822054 | 619184 | 622092 |
| tet | 1323 | 3797 | 8047 | 4093 | 4095 |
| tg | 108598 | 279635 | 761826 | 330974 | 331423 |
| th | 153075 | 715083 | 1723394 | 1395935 | 1398891 |
| ti | 388 | 987 | 1191 | 325 | 326 |
| tk | 4739 | 23629 | 18964 | 9717 | 9760 |
| tl | 43388 | 150141 | 447293 | 296084 | 296634 |
| tn | 1090 | 3960 | 3976 | 2008 | 2010 |
| to | 1512 | 2754 | 3542 | 2029 | 2080 |
| tpi | 1278 | 2055 | 3897 | 2193 | 2198 |
| tr | 500435 | 1806253 | 4476004 | 3964449 | 3965589 |
| trv | 1770 | 16650 | 3814 | 504 | 969 |
| ts | 674 | 1798 | 1557 | 903 | 909 |
| tt | 484761 | 1196573 | 2064576 | 1675637 | 1676579 |
| tum | 16778 | 31383 | 57382 | 28399 | 37107 |
| tw | 3568 | 16807 | 15312 | 10912 | 11495 |
| ty | 1175 | 1364 | 1563 | 1095 | 1095 |
| tyv | 3399 | 21968 | 21004 | 5535 | 5557 |
| udm | 5066 | 11432 | 24875 | 17709 | 17715 |
| ug | 8102 | 58982 | 23654 | 12671 | 12874 |
| uk | 522709 | 2867475 | 6800045 | 6445628 | 6451294 |
| ur | 194948 | 676227 | 1870488 | 910419 | 914840 |
| uz | 232879 | 859793 | 1344790 | 1073065 | 1084092 |
| ve | 764 | 1359 | 2524 | 2366 | 2366 |
| vec | 62729 | 98987 | 275972 | 194424 | 194447 |
| vep | 6853 | 43014 | 93864 | 39225 | 39228 |
| vi | 1300753 | 4103594 | 10852870 | 6884928 | 6892519 |
| vls | 7272 | 26374 | 61885 | 49639 | 49653 |
| vo | 32133 | 78015 | 125495 | 101612 | 101629 |
| wa | 11104 | 56305 | 116752 | 79686 | 80037 |
| war | 1158901 | 1342594 | 6654010 | 6009636 | 6009641 |
| wo | 1659 | 7693 | 10828 | 4057 | 4103 |
| wuu | 37170 | 58227 | 121928 | 82184 | 82237 |
| xal | 2008 | 4309 | 4582 | 2112 | 2113 |
| xh | 1502 | 4448 | 6733 | 2128 | 2186 |
| xmf | 19201 | 49944 | 179291 | 21189 | 22041 |
| yi | 14164 | 68937 | 172645 | 116102 | 116325 |
| yo | 29938 | 52231 | 85171 | 46928 | 47346 |
| za | 2388 | 3917 | 7463 | 4613 | 4665 |
| zea | 5445 | 16648 | 36161 | 23532 | 23578 |
| zh | 1310818 | 5501834 | 16397675 | 14380752 | 14421795 |
| zh_classical | 11775 | 44053 | 140340 | 71576 | 71692 |
| zh_min_nan | 425676 | 853753 | 2627115 | 2053956 | 2054838 |
| zh_yue | 121401 | 273459 | 844047 | 683130 | 683226 |
| zu | 10387 | 18211 | 22569 | 20193 | 20238 |

#### Validation

| | Articles | Paragraphs | Anchors | Anchors with QIDs | Anchors with PageIDs | 
| :-- | --: | --: | --: | --: | --: |
| ab | 475 | 601 | 1061 | 399 | 399 |
| ace | 2443 | 2668 | 5197 | 2583 | 2587 |
| ady | 142 | 183 | 248 | 150 | 151 |
| af | 27383 | 44157 | 109108 | 100078 | 100123 |
| als | 11998 | 18277 | 44634 | 32874 | 32874 |
| alt | 481 | 827 | 1020 | 621 | 621 |
| am | 3746 | 5234 | 10111 | 5731 | 5756 |
| ami | 749 | 1431 | 744 | 179 | 304 |
| an | 10526 | 13588 | 74808 | 58195 | 58259 |
| ang | 826 | 1099 | 2647 | 1099 | 1102 |
| anp | 504 | 751 | 1698 | 437 | 581 |
| ar | 265368 | 401215 | 1295968 | 1249666 | 1250103 |
| arc | 377 | 418 | 1061 | 610 | 617 |
| ary | 1447 | 1870 | 5702 | 3885 | 3887 |
| arz | 367206 | 410487 | 876531 | 767742 | 768942 |
| as | 5463 | 8589 | 13953 | 7719 | 7732 |
| ast | 48345 | 97904 | 329690 | 197832 | 198042 |
| atj | 399 | 440 | 774 | 406 | 416 |
| av | 719 | 961 | 1918 | 1043 | 1053 |
| avk | 8056 | 9538 | 11816 | 3633 | 3772 |
| awa | 515 | 645 | 721 | 213 | 287 |
| ay | 1391 | 1653 | 2616 | 1481 | 1483 |
| az | 57070 | 88136 | 177151 | 155596 | 155858 |
| azb | 57642 | 64997 | 137053 | 83336 | 83778 |
| ba | 25690 | 43460 | 69052 | 61624 | 61666 |
| ban | 4053 | 4840 | 9581 | 7374 | 7385 |
| bar | 6905 | 9377 | 20546 | 12164 | 12164 |
| bat_smg | 4149 | 4706 | 8787 | 5820 | 5823 |
| bcl | 3355 | 5058 | 8759 | 5080 | 5083 |
| be | 64203 | 91174 | 276525 | 244114 | 244122 |
| bg | 98148 | 148234 | 438687 | 400356 | 401330 |
| bh | 1535 | 1891 | 3464 | 2630 | 2635 |
| bi | 154 | 159 | 251 | 151 | 151 |
| bjn | 1764 | 2166 | 6458 | 3694 | 3775 |
| blk | 887 | 1374 | 1538 | 821 | 839 |
| bm | 196 | 272 | 317 | 146 | 146 |
| bn | 50495 | 81841 | 169097 | 128508 | 128609 |
| bo | 2198 | 4079 | 934 | 746 | 752 |
| bpy | 10057 | 12879 | 18710 | 9693 | 9693 |
| br | 18687 | 23734 | 73278 | 59024 | 59056 |
| bs | 28533 | 42574 | 138483 | 107760 | 107846 |
| bug | 1636 | 1655 | 6141 | 1682 | 1731 |
| bxr | 754 | 1003 | 2930 | 1211 | 1211 |
| ca | 251952 | 399403 | 1265187 | 1140208 | 1140359 |
| cbk_zam | 460 | 932 | 1040 | 268 | 272 |
| cdo | 2953 | 3237 | 6938 | 3273 | 3281 |
| ce | 197899 | 234617 | 341843 | 166126 | 166206 |
| ceb | 1221405 | 1324624 | 4218179 | 3742385 | 3773844 |
| ch | 123 | 131 | 239 | 64 | 73 |
| chr | 124 | 134 | 175 | 100 | 100 |
| chy | 67 | 67 | 47 | 42 | 42 |
| ckb | 13511 | 18279 | 48490 | 25365 | 25540 |
| co | 1723 | 2587 | 5286 | 2729 | 2737 |
| cr | 22 | 23 | 22 | 13 | 13 |
| crh | 2978 | 3246 | 11005 | 7899 | 7899 |
| cs | 189136 | 297000 | 1101343 | 974485 | 974505 |
| csb | 1307 | 1533 | 3341 | 1851 | 1851 |
| cu | 250 | 275 | 540 | 229 | 229 |
| cv | 14374 | 17462 | 42486 | 19049 | 19114 |
| cy | 89897 | 110225 | 222476 | 177842 | 178698 |
| da | 87765 | 129990 | 482701 | 427333 | 427374 |
| dag | 2215 | 3237 | 4935 | 1169 | 1498 |
| de | 1120553 | 1788057 | 5831103 | 5607963 | 5607963 |
| din | 149 | 177 | 128 | 15 | 15 |
| diq | 6660 | 7883 | 17684 | 15853 | 15861 |
| dsb | 781 | 1032 | 2476 | 1301 | 1301 |
| dty | 554 | 659 | 861 | 480 | 483 |
| dv | 1227 | 1898 | 870 | 406 | 406 |
| dz | 215 | 303 | 21 | 8 | 8 |
| ee | 203 | 242 | 183 | 66 | 74 |
| el | 99725 | 169395 | 461747 | 344216 | 344456 |
| eml | 4387 | 6114 | 13938 | 8193 | 8214 |
| en | 2503257 | 4516442 | 12185882 | 11974436 | 11975194 |
| eo | 90949 | 123848 | 474727 | 442357 | 442772 |
| es | 701171 | 1209944 | 3752765 | 3514968 | 3522213 |
| et | 80911 | 123354 | 395877 | 319773 | 320587 |
| eu | 104388 | 156552 | 378553 | 337331 | 337944 |
| ext | 804 | 1045 | 2269 | 1344 | 1345 |
| fa | 191532 | 262121 | 688824 | 652200 | 653219 |
| fat | 446 | 709 | 214 | 3 | 97 |
| ff | 361 | 459 | 378 | 222 | 234 |
| fi | 123327 | 184244 | 576163 | 514419 | 514915 |
| fiu_vro | 1738 | 2263 | 4622 | 2623 | 2628 |
| fj | 168 | 213 | 604 | 214 | 214 |
| fo | 2625 | 3398 | 13383 | 10599 | 10617 |
| fr | 954388 | 1695419 | 4847588 | 4738268 | 4740047 |
| frp | 1018 | 1181 | 4089 | 2862 | 2862 |
| frr | 2968 | 3419 | 9609 | 7996 | 8011 |
| fur | 884 | 1168 | 3225 | 1833 | 1839 |
| fy | 15980 | 22974 | 139530 | 108300 | 108337 |
| ga | 10781 | 14493 | 38848 | 32343 | 32352 |
| gag | 440 | 551 | 961 | 465 | 465 |
| gan | 731 | 1045 | 2071 | 1536 | 1537 |
| gcr | 480 | 567 | 297 | 122 | 122 |
| gd | 4393 | 5296 | 15544 | 10458 | 10458 |
| gl | 62030 | 101112 | 407821 | 325854 | 325960 |
| glk | 1383 | 1747 | 3723 | 2435 | 2443 |
| gn | 1164 | 1728 | 4751 | 3521 | 3528 |
| gom | 2106 | 4116 | 1511 | 251 | 251 |
| gor | 2844 | 3082 | 11826 | 7315 | 7411 |
| got | 216 | 245 | 514 | 190 | 190 |
| gpe | 265 | 355 | 93 | 71 | 73 |
| gu | 8437 | 13008 | 50956 | 38242 | 38251 |
| guc | 198 | 279 | 312 | 141 | 162 |
| gur | 369 | 565 | 145 | 25 | 27 |
| guw | 332 | 393 | 827 | 313 | 616 |
| gv | 957 | 1324 | 5652 | 2252 | 2253 |
| ha | 10666 | 16571 | 12853 | 10862 | 10993 |
| hak | 1179 | 1302 | 4628 | 3155 | 3155 |
| haw | 541 | 650 | 1238 | 616 | 618 |
| he | 165541 | 295188 | 1213939 | 1153986 | 1155384 |
| hi | 36229 | 60184 | 108382 | 89102 | 89340 |
| hif | 2107 | 2369 | 5015 | 2648 | 2680 |
| hr | 62673 | 97103 | 354392 | 304964 | 305664 |
| hsb | 3599 | 4379 | 10001 | 7239 | 7240 |
| ht | 14693 | 17294 | 23011 | 18721 | 18928 |
| hu | 125438 | 206546 | 586091 | 523501 | 523814 |
| hy | 113060 | 171415 | 418503 | 298111 | 298292 |
| hyw | 5310 | 9207 | 17616 | 8842 | 9168 |
| ia | 4021 | 4850 | 14972 | 11257 | 11263 |
| id | 158648 | 237793 | 734148 | 627764 | 629525 |
| ie | 2213 | 2523 | 6750 | 5036 | 5046 |
| ig | 7944 | 12354 | 6464 | 3466 | 3493 |
| ik | 100 | 118 | 120 | 64 | 71 |
| ilo | 4096 | 8297 | 14183 | 8609 | 8609 |
| inh | 399 | 494 | 1298 | 626 | 645 |
| io | 8868 | 11368 | 33682 | 28744 | 28748 |
| is | 13573 | 18566 | 62576 | 47263 | 47360 |
| it | 584902 | 968880 | 3050620 | 2902006 | 2903047 |
| iu | 61 | 62 | 48 | 29 | 29 |
| ja | 573457 | 1032568 | 3222875 | 3083301 | 3088604 |
| jam | 249 | 274 | 623 | 399 | 399 |
| jbo | 270 | 321 | 562 | 56 | 56 |
| jv | 13108 | 16457 | 60143 | 42112 | 42148 |
| ka | 53071 | 76961 | 252383 | 46974 | 46975 |
| kaa | 775 | 1071 | 1476 | 669 | 717 |
| kab | 1269 | 1685 | 4050 | 2397 | 2403 |
| kbd | 474 | 663 | 1482 | 537 | 537 |
| kbp | 535 | 656 | 835 | 810 | 811 |
| kcg | 190 | 223 | 311 | 196 | 197 |
| kg | 187 | 213 | 420 | 260 | 260 |
| ki | 273 | 333 | 248 | 169 | 206 |
| kk | 76635 | 99268 | 204324 | 126732 | 127677 |
| kl | 97 | 129 | 162 | 43 | 43 |
| km | 3844 | 9340 | 12192 | 4524 | 4583 |
| kn | 14217 | 29387 | 48402 | 20992 | 21022 |
| ko | 154713 | 239887 | 689906 | 633527 | 634725 |
| koi | 682 | 1010 | 1815 | 1144 | 1144 |
| krc | 423 | 698 | 2022 | 841 | 846 |
| ks | 888 | 1006 | 1692 | 645 | 670 |
| ksh | 918 | 1156 | 2951 | 1053 | 1055 |
| ku | 10060 | 12771 | 29766 | 23050 | 23232 |
| kv | 1105 | 1456 | 3365 | 2787 | 2787 |
| kw | 1820 | 2171 | 5570 | 3076 | 3082 |
| ky | 16655 | 21571 | 31213 | 21712 | 21757 |
| la | 22397 | 26732 | 161732 | 142447 | 142486 |
| lad | 961 | 1286 | 3984 | 2056 | 2056 |
| lb | 15385 | 19667 | 60568 | 46664 | 46730 |
| lbe | 207 | 232 | 488 | 290 | 290 |
| lez | 1184 | 1764 | 3829 | 2760 | 2760 |
| lfn | 1455 | 2435 | 3328 | 1602 | 1604 |
| lg | 1272 | 2650 | 1795 | 239 | 305 |
| li | 4501 | 6650 | 24213 | 15790 | 15826 |
| lij | 1781 | 2607 | 6658 | 3933 | 3933 |
| lld | 17293 | 17539 | 64059 | 49327 | 50864 |
| lmo | 12641 | 14976 | 40217 | 29874 | 29946 |
| ln | 585 | 692 | 1321 | 996 | 997 |
| lo | 1144 | 1680 | 3023 | 991 | 1013 |
| lt | 62652 | 85962 | 300456 | 269264 | 270227 |
| ltg | 289 | 341 | 686 | 285 | 285 |
| lv | 34742 | 48371 | 160433 | 136594 | 136873 |
| mad | 284 | 381 | 439 | 135 | 136 |
| mai | 2184 | 2499 | 5878 | 4209 | 4212 |
| map_bms | 1539 | 1847 | 7486 | 5705 | 5705 |
| mdf | 1086 | 1244 | 2512 | 1077 | 1077 |
| mg | 20361 | 23650 | 36313 | 29821 | 29974 |
| mhr | 2863 | 3594 | 6538 | 4114 | 4122 |
| mi | 1078 | 1154 | 3214 | 2743 | 2776 |
| min | 42987 | 46277 | 143692 | 55809 | 56077 |
| mk | 46235 | 76890 | 219310 | 180884 | 181042 |
| ml | 31116 | 46345 | 88976 | 53726 | 53818 |
| mn | 8485 | 13887 | 32271 | 15330 | 15455 |
| mni | 1843 | 2102 | 3418 | 2183 | 2325 |
| mnw | 1284 | 3750 | 897 | 202 | 224 |
| mr | 26803 | 36202 | 70510 | 43103 | 44352 |
| mrj | 2062 | 2297 | 5627 | 2888 | 2888 |
| ms | 75473 | 110077 | 270064 | 215280 | 215811 |
| mt | 2516 | 5510 | 11680 | 5760 | 5761 |
| mwl | 1828 | 4316 | 15365 | 3216 | 3287 |
| my | 24005 | 37165 | 49321 | 33223 | 33518 |
| myv | 1732 | 2327 | 4094 | 2923 | 2925 |
| mzn | 3784 | 4409 | 9938 | 5199 | 5205 |
| nah | 1128 | 1314 | 3316 | 1418 | 1556 |
| nap | 2047 | 2473 | 4579 | 2249 | 2249 |
| nds | 20646 | 26845 | 65355 | 34090 | 34094 |
| nds_nl | 2127 | 3063 | 10188 | 5585 | 5587 |
| ne | 6956 | 10087 | 16847 | 13502 | 13536 |
| new | 22645 | 27233 | 50860 | 32165 | 32217 |
| nia | 312 | 430 | 512 | 277 | 329 |
| nl | 490380 | 651743 | 1994062 | 1874588 | 1875259 |
| nn | 44180 | 60918 | 194747 | 153072 | 153140 |
| no | 172653 | 245377 | 779775 | 715618 | 716153 |
| nov | 339 | 410 | 861 | 452 | 452 |
| nqo | 583 | 1037 | 2598 | 704 | 813 |
| nrm | 1318 | 1600 | 4276 | 3734 | 3736 |
| nso | 960 | 1038 | 4242 | 4119 | 4119 |
| nv | 5649 | 6281 | 13652 | 11768 | 11768 |
| ny | 236 | 318 | 392 | 126 | 126 |
| oc | 23067 | 33775 | 115155 | 87980 | 88063 |
| olo | 1273 | 1598 | 2162 | 997 | 998 |
| om | 401 | 830 | 891 | 401 | 412 |
| or | 6261 | 8669 | 16120 | 6752 | 6757 |
| os | 3923 | 4535 | 9130 | 5470 | 5524 |
| pa | 17242 | 24844 | 37813 | 21759 | 21812 |
| pag | 1602 | 4519 | 404 | 300 | 300 |
| pam | 1509 | 1831 | 6019 | 3230 | 3272 |
| pap | 773 | 1376 | 2526 | 2042 | 2056 |
| pcd | 1089 | 1361 | 1803 | 1334 | 1338 |
| pcm | 353 | 542 | 409 | 128 | 139 |
| pdc | 370 | 565 | 839 | 424 | 429 |
| pfl | 1113 | 1500 | 2861 | 1070 | 1070 |
| pi | 578 | 682 | 881 | 26 | 26 |
| pih | 118 | 125 | 317 | 217 | 218 |
| pl | 444095 | 621669 | 2149058 | 2041686 | 2043400 |
| pms | 16530 | 19186 | 41547 | 34783 | 35474 |
| pnb | 21586 | 44654 | 103992 | 58461 | 59380 |
| pnt | 147 | 172 | 389 | 177 | 178 |
| ps | 7566 | 14922 | 8427 | 4108 | 4187 |
| pt | 349931 | 580790 | 1868210 | 1745832 | 1745858 |
| pwn | 103 | 166 | 85 | 31 | 31 |
| qu | 4540 | 5211 | 14781 | 11746 | 11750 |
| rm | 1076 | 3100 | 5539 | 2293 | 2298 |
| rmy | 214 | 235 | 446 | 176 | 184 |
| rn | 125 | 172 | 124 | 53 | 53 |
| ro | 106169 | 168972 | 473512 | 416263 | 416347 |
| roa_rup | 214 | 290 | 458 | 254 | 254 |
| roa_tara | 1278 | 1979 | 4455 | 1534 | 1534 |
| ru | 806592 | 1369860 | 3416036 | 3245837 | 3247963 |
| rue | 2022 | 2513 | 7023 | 5064 | 5066 |
| rw | 2577 | 3925 | 4139 | 2223 | 2349 |
| sa | 4344 | 8607 | 11313 | 4249 | 4391 |
| sah | 4729 | 8472 | 9040 | 6623 | 6660 |
| sat | 3485 | 4960 | 6473 | 3225 | 3278 |
| sc | 1900 | 2807 | 7641 | 5096 | 5098 |
| scn | 4263 | 5604 | 14333 | 11167 | 11171 |
| sco | 7382 | 9639 | 33771 | 16432 | 16453 |
| sd | 3970 | 5499 | 8879 | 3804 | 3925 |
| se | 982 | 1149 | 2841 | 1958 | 1958 |
| sg | 67 | 72 | 36 | 24 | 24 |
| sh | 103283 | 135121 | 484459 | 429555 | 429770 |
| shi | 477 | 679 | 1144 | 545 | 570 |
| shn | 3633 | 5630 | 5456 | 3627 | 3639 |
| si | 7672 | 14760 | 16443 | 6215 | 6346 |
| simple | 52503 | 68765 | 224811 | 187586 | 187598 |
| sk | 67520 | 93957 | 317232 | 272711 | 272779 |
| skr | 2090 | 6926 | 4136 | 1683 | 2359 |
| sl | 55621 | 89740 | 285769 | 228421 | 228530 |
| sm | 153 | 171 | 485 | 297 | 297 |
| smn | 1163 | 1420 | 4517 | 2681 | 2688 |
| sn | 1896 | 2139 | 4351 | 3384 | 3529 |
| so | 2358 | 4032 | 6064 | 5027 | 5083 |
| sq | 25223 | 41621 | 79295 | 59156 | 59350 |
| sr | 177997 | 258455 | 728755 | 584663 | 585394 |
| srn | 281 | 342 | 796 | 205 | 225 |
| ss | 188 | 259 | 265 | 125 | 125 |
| st | 157 | 198 | 248 | 164 | 166 |
| stq | 804 | 1162 | 3150 | 1816 | 1816 |
| su | 10348 | 13687 | 55055 | 42915 | 42944 |
| sv | 467467 | 558522 | 2473790 | 2382576 | 2382608 |
| sw | 18014 | 24348 | 90302 | 77817 | 78145 |
| szl | 11292 | 12173 | 52459 | 14419 | 14424 |
| szy | 2391 | 5418 | 2042 | 235 | 285 |
| ta | 59923 | 87114 | 183399 | 126977 | 127148 |
| tay | 1192 | 1757 | 1101 | 175 | 591 |
| tcy | 769 | 1077 | 1089 | 464 | 465 |
| te | 43790 | 79667 | 91327 | 69148 | 69484 |
| tet | 294 | 412 | 871 | 471 | 471 |
| tg | 27060 | 31599 | 86180 | 37522 | 37561 |
| th | 49169 | 78814 | 189768 | 154097 | 154453 |
| ti | 87 | 99 | 89 | 22 | 22 |
| tk | 1328 | 2612 | 2116 | 1056 | 1062 |
| tl | 11731 | 16623 | 49726 | 32858 | 32914 |
| tn | 296 | 424 | 477 | 278 | 278 |
| to | 254 | 277 | 393 | 230 | 233 |
| tpi | 180 | 207 | 394 | 216 | 217 |
| tr | 134938 | 200972 | 496960 | 440639 | 440790 |
| trv | 807 | 1814 | 400 | 53 | 98 |
| ts | 155 | 203 | 219 | 132 | 132 |
| tt | 113689 | 132676 | 228544 | 185563 | 185662 |
| tum | 2188 | 3516 | 6442 | 3105 | 4083 |
| tw | 1249 | 1885 | 1729 | 1217 | 1291 |
| ty | 162 | 167 | 215 | 143 | 143 |
| tyv | 1494 | 2486 | 2342 | 611 | 617 |
| udm | 1036 | 1240 | 2781 | 1957 | 1957 |
| ug | 2629 | 6556 | 2657 | 1479 | 1493 |
| uk | 203057 | 318240 | 758049 | 718278 | 718908 |
| ur | 54784 | 75152 | 206169 | 99493 | 100041 |
| uz | 65767 | 95465 | 149763 | 119192 | 120519 |
| ve | 128 | 148 | 256 | 229 | 229 |
| vec | 9463 | 11242 | 32188 | 22525 | 22531 |
| vep | 3225 | 4804 | 10375 | 4295 | 4295 |
| vi | 330763 | 455933 | 1211343 | 768936 | 769829 |
| vls | 2189 | 2904 | 7133 | 5776 | 5777 |
| vo | 7308 | 8647 | 13902 | 11270 | 11273 |
| wa | 4457 | 6269 | 12736 | 8751 | 8794 |
| war | 146537 | 149236 | 738087 | 666983 | 666983 |
| wo | 516 | 864 | 1083 | 404 | 414 |
| wuu | 5530 | 6448 | 13732 | 9168 | 9171 |
| xal | 407 | 449 | 549 | 308 | 308 |
| xh | 399 | 550 | 804 | 284 | 293 |
| xmf | 4516 | 5414 | 19437 | 2342 | 2447 |
| yi | 5260 | 7563 | 18821 | 12493 | 12510 |
| yo | 4431 | 5855 | 9761 | 5361 | 5410 |
| za | 335 | 414 | 777 | 457 | 458 |
| zea | 1470 | 1847 | 3682 | 2569 | 2574 |
| zh | 389361 | 611537 | 1817382 | 1592929 | 1597686 |
| zh_classical | 3601 | 4995 | 15834 | 8157 | 8170 |
| zh_min_nan | 87849 | 94529 | 291330 | 227978 | 228083 |
| zh_yue | 23579 | 30146 | 92720 | 75081 | 75096 |
| zu | 1646 | 2050 | 2518 | 2228 | 2234 |

**NOTE:** The number of articles in the tables above refers to the number of articles that have at least one paragraph belonging to the article appear in the split.

## Additional Information

### Licensing Information

The WikiAnc dataset is given under the [Creative Commons Attribution ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) license.  
