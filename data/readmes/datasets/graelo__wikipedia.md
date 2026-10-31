---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
pretty_name: Wikipedia
paperswithcode_id: null
license:
- cc-by-sa-3.0
- gfdl
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
source_datasets:
- original
multilinguality:
- multilingual
size_categories:
- n<1K
- 1K<n<10K
- 10K<n<100K
- 100K<n<1M
- 1M<n<10M
language:
# - aa  - closed and no dump
- ab
- ace
- ady
- af
- ak
- als
- alt
- am
- ami
- an
- ang
- anp
- ar
- arc
- ary
- arz
- as
- ast
- atj
- av
- avk
- awa
- ay
- az
- azb
- ba
- ban
- bar
# - bat-smg - see bcp47 below
- bcl
# - be-x-old - see bcp47 below
- be
- bg
- bh
- bi
- bjn
- blk
- bm
- bn
- bo
- bpy
- br
- bs
- bug
- bxr
- ca
# - cbk-zam - see bcp47 below
- cdo
- ce
- ceb
- ch
- cho  # closed
- chr
- chy
- ckb
- co
- cr
- crh
- cs
- csb
- cu
- cv
- cy
- da
- dag
- de
- din
- diq
- dsb
- dty
- dv
- dz
- ee
- el
- eml
- eo
- es
- et
- eu
- ext
- fa
- fat
- ff
- fi
# - fiu-vro - see bcp47 below
- fj
- fo
- fr
- frp
- frr
- fur
- fy
- ga
- gag
- gan
- gcr
- gd
- gl
- glk
- gn
- gom
- gor
- got
- gu
- guc
- gur
- guw
- gv
- ha
- hak
- haw
- he
- hi
- hif
- ho  # closed
- hr
- hsb
- ht
- hu
- hy
- hyw
# - hz  - closed and no dump
- ia
- id
- ie
- ig
- ii  # closed
- ik
- ilo
- inh
- io
- is
- it
- iu
- ja
- jam
- jbo
- jv
- ka
- kaa
- kab
- kbd
- kbp
- kcg
- kg
- ki
- kj  # closed
- kk
- kl
- km
- kn
- ko
- koi
# - kr - closed and no dump
- krc
- ks
- ksh
- ku
- kv
- kw
- ky
- la
- lad
- lb
- lbe
- lez
- lfn
- lg
- li
- lij
- lld
- lmo
- ln
- lo
- lrc  # closed
- lt
- ltg
- lv
- mad
- mai
# - map-bms - see bcp47 below
- mdf
- mg
- mh
- mhr
- mi
- min
- mk
- ml
- mn
- mni
- mnw
- mr
- mrj
- ms
- mt
- mus  # closed
- mwl
- my
- myv
- mzn
# - na - closed and no dump
- nah
- nap
# - nds-nl - see bcp47 below
- nds
- ne
- new
- ng  # closed
- nia
- nl
- nn
- no
- nov
- nqo
- nrm
- nso
- nv
- ny
- oc
- olo
- om
- or
- os
- pa
- pag
- pam
- pap
- pcd
- pcm
- pdc
- pfl
- pi
- pih
- pl
- pms
- pnb
- pnt
- ps
- pt
- pwn
- qu
- rm
- rmy
- rn
- ro
# - roa-rup - see bcp47 below
# - roa-tara - see bcp47 below
- ru
- rue
- rw
- sa
- sah
- sat
- sc
- scn
- sco
- sd
- se
- sg
- sh
- shi
- shn
- si
# - simple - see bcp47 below
- sk
- skr
- sl
- sm
- smn
- sn
- so
- sq
- sr
- srn
- ss
- st
- stq
- su
- sv
- sw
- szl
- szy
- ta
- tay
- tcy
- te
- tet
- tg
- th
- ti
- tk
- tl
- tn
- to
- tpi
- tr
- trv
- ts
- tt
- tum
- tw
- ty
- tyv
- udm
- ug
- uk
- ur
- uz
- ve
- vec
- vep
- vi
- vls
- vo
- wa
- war
- wo
- wuu
- xal
- xh
- xmf
- yi
- yo
- za
- zea
- zh
# - zh-classical - see bcp47 below
# - zh-min-nan - see bcp47 below
# - zh-yue - see bcp47 below
- zu
language_bcp47:
- bat-smg
- be-x-old
- cbk-zam
- fiu-vro
- map-bms
- nds-nl
- roa-rup
- roa-tara
- simple
- zh-classical
- zh-min-nan
- zh-yue
dataset_info:
- config_name: 20230601.ab
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4183525
    num_examples: 6114
  download_size: 1172328
  dataset_size: 4183525
- config_name: 20230601.ace
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4887561
    num_examples: 12839
  download_size: 1473823
  dataset_size: 4887561
- config_name: 20230601.ady
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 613082
    num_examples: 609
  download_size: 280249
  dataset_size: 613082
- config_name: 20230601.af
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 220678901
    num_examples: 108170
  download_size: 121238071
  dataset_size: 220678901
- config_name: 20230601.ak
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 189
    num_examples: 1
  download_size: 3045
  dataset_size: 189
- config_name: 20230601.als
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 80615079
    num_examples: 29804
  download_size: 48883379
  dataset_size: 80615079
- config_name: 20230601.alt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5786027
    num_examples: 1082
  download_size: 2401701
  dataset_size: 5786027
- config_name: 20230601.am
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 24009050
    num_examples: 13839
  download_size: 10615909
  dataset_size: 24009050
- config_name: 20230601.ami
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3865236
    num_examples: 1570
  download_size: 2006639
  dataset_size: 3865236
- config_name: 20230601.an
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 56295233
    num_examples: 43744
  download_size: 29055888
  dataset_size: 56295233
- config_name: 20230601.ang
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2854073
    num_examples: 4019
  download_size: 1756372
  dataset_size: 2854073
- config_name: 20230601.anp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9055032
    num_examples: 2736
  download_size: 3270423
  dataset_size: 9055032
- config_name: 20230601.ar
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3052201469
    num_examples: 1205403
  download_size: 1319905253
  dataset_size: 3052201469
- config_name: 20230601.arc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 830073
    num_examples: 1925
  download_size: 360590
  dataset_size: 830073
- config_name: 20230601.ary
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10007364
    num_examples: 6703
  download_size: 4094420
  dataset_size: 10007364
- config_name: 20230601.arz
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1364641408
    num_examples: 1617770
  download_size: 306336320
  dataset_size: 1364641408
- config_name: 20230601.as
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 86645223
    num_examples: 11988
  download_size: 33149841
  dataset_size: 86645223
- config_name: 20230601.ast
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 470349731
    num_examples: 132550
  download_size: 271011784
  dataset_size: 470349731
- config_name: 20230601.atj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 993287
    num_examples: 1965
  download_size: 502890
  dataset_size: 993287
- config_name: 20230601.av
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5996158
    num_examples: 3392
  download_size: 2514243
  dataset_size: 5996158
- config_name: 20230601.avk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 31189461
    num_examples: 27493
  download_size: 7729144
  dataset_size: 31189461
- config_name: 20230601.awa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3588050
    num_examples: 3701
  download_size: 1230725
  dataset_size: 3588050
- config_name: 20230601.ay
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4357283
    num_examples: 5287
  download_size: 1736571
  dataset_size: 4357283
- config_name: 20230601.az
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 425710145
    num_examples: 194486
  download_size: 225589717
  dataset_size: 425710145
- config_name: 20230601.azb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 186034971
    num_examples: 243041
  download_size: 46251265
  dataset_size: 186034971
- config_name: 20230601.ba
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 293142247
    num_examples: 62907
  download_size: 120320323
  dataset_size: 293142247
- config_name: 20230601.ban
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16509353
    num_examples: 19293
  download_size: 6302437
  dataset_size: 16509353
- config_name: 20230601.bar
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36001708
    num_examples: 26978
  download_size: 21611902
  dataset_size: 36001708
- config_name: 20230601.bat-smg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7536614
    num_examples: 17181
  download_size: 3411835
  dataset_size: 7536614
- config_name: 20230601.be-x-old
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 244894736
    num_examples: 82917
  download_size: 110733701
  dataset_size: 244894736
- config_name: 20230601.bcl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 18259970
    num_examples: 13934
  download_size: 10086356
  dataset_size: 18259970
- config_name: 20230601.be
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 606416485
    num_examples: 231617
  download_size: 280474552
  dataset_size: 606416485
- config_name: 20230601.bg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1080390968
    num_examples: 291361
  download_size: 506945262
  dataset_size: 1080390968
- config_name: 20230601.bh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16078510
    num_examples: 8446
  download_size: 5648960
  dataset_size: 16078510
- config_name: 20230601.bi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 398357
    num_examples: 1539
  download_size: 200277
  dataset_size: 398357
- config_name: 20230601.bjn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6755874
    num_examples: 10379
  download_size: 3265979
  dataset_size: 6755874
- config_name: 20230601.blk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 24413622
    num_examples: 2725
  download_size: 7356285
  dataset_size: 24413622
- config_name: 20230601.bm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 473185
    num_examples: 1221
  download_size: 261438
  dataset_size: 473185
- config_name: 20230601.bn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 913676298
    num_examples: 138515
  download_size: 330147337
  dataset_size: 913676298
- config_name: 20230601.bo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 132034426
    num_examples: 12434
  download_size: 38687191
  dataset_size: 132034426
- config_name: 20230601.bpy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 42862119
    num_examples: 25167
  download_size: 6532133
  dataset_size: 42862119
- config_name: 20230601.br
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 84044684
    num_examples: 79959
  download_size: 48952223
  dataset_size: 84044684
- config_name: 20230601.bs
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 190816695
    num_examples: 92065
  download_size: 106053913
  dataset_size: 190816695
- config_name: 20230601.bug
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3433134
    num_examples: 15873
  download_size: 815878
  dataset_size: 3433134
- config_name: 20230601.bxr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6695205
    num_examples: 2791
  download_size: 3078381
  dataset_size: 6695205
- config_name: 20230601.ca
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1918941844
    num_examples: 728483
  download_size: 1113762234
  dataset_size: 1918941844
- config_name: 20230601.cbk-zam
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2808337
    num_examples: 3307
  download_size: 1261855
  dataset_size: 2808337
- config_name: 20230601.cdo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5010639
    num_examples: 16234
  download_size: 1949302
  dataset_size: 5010639
- config_name: 20230601.ce
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 726468413
    num_examples: 599863
  download_size: 86627608
  dataset_size: 726468413
- config_name: 20230601.ceb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4569352784
    num_examples: 6124009
  download_size: 926156250
  dataset_size: 4569352784
- config_name: 20230601.ch
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 187255
    num_examples: 573
  download_size: 96403
  dataset_size: 187255
- config_name: 20230601.cho
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7974
    num_examples: 14
  download_size: 9782
  dataset_size: 7974
- config_name: 20230601.chr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 764388
    num_examples: 1113
  download_size: 341232
  dataset_size: 764388
- config_name: 20230601.chy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 149009
    num_examples: 801
  download_size: 76580
  dataset_size: 149009
- config_name: 20230601.ckb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 101248717
    num_examples: 49928
  download_size: 40379289
  dataset_size: 101248717
- config_name: 20230601.co
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8069524
    num_examples: 6565
  download_size: 4650142
  dataset_size: 8069524
- config_name: 20230601.cr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 50625
    num_examples: 182
  download_size: 26509
  dataset_size: 50625
- config_name: 20230601.crh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9056373
    num_examples: 25642
  download_size: 3453399
  dataset_size: 9056373
- config_name: 20230601.cs
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1529727976
    num_examples: 525205
  download_size: 966856046
  dataset_size: 1529727976
- config_name: 20230601.csb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3739371
    num_examples: 5478
  download_size: 2049003
  dataset_size: 3739371
- config_name: 20230601.cu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 975765
    num_examples: 1221
  download_size: 395563
  dataset_size: 975765
- config_name: 20230601.cv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 81019358
    num_examples: 51407
  download_size: 29189010
  dataset_size: 81019358
- config_name: 20230601.cy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 304314230
    num_examples: 278927
  download_size: 111093453
  dataset_size: 304314230
- config_name: 20230601.da
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 540186121
    num_examples: 291721
  download_size: 326825586
  dataset_size: 540186121
- config_name: 20230601.dag
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8116697
    num_examples: 8850
  download_size: 3469680
  dataset_size: 8116697
- config_name: 20230601.de
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9446726072
    num_examples: 2801769
  download_size: 5752429951
  dataset_size: 9446726072
- config_name: 20230601.din
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 554422
    num_examples: 506
  download_size: 334229
  dataset_size: 554422
- config_name: 20230601.diq
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19300910
    num_examples: 40589
  download_size: 7469118
  dataset_size: 19300910
- config_name: 20230601.dsb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3303132
    num_examples: 3357
  download_size: 1923763
  dataset_size: 3303132
- config_name: 20230601.dty
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6972841
    num_examples: 3625
  download_size: 2497168
  dataset_size: 6972841
- config_name: 20230601.dv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13916007
    num_examples: 4344
  download_size: 5255070
  dataset_size: 13916007
- config_name: 20230601.dz
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8517069
    num_examples: 777
  download_size: 2474869
  dataset_size: 8517069
- config_name: 20230601.ee
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 844062
    num_examples: 1164
  download_size: 464418
  dataset_size: 844062
- config_name: 20230601.el
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1314451459
    num_examples: 222598
  download_size: 627997252
  dataset_size: 1314451459
- config_name: 20230601.eml
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3605037
    num_examples: 12945
  download_size: 1681847
  dataset_size: 3605037
- config_name: 20230601.en
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21325670826
    num_examples: 6660918
  download_size: 12512970849
  dataset_size: 21325670826
- config_name: 20230601.eo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 508055613
    num_examples: 337291
  download_size: 294377264
  dataset_size: 508055613
- config_name: 20230601.es
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5889963046
    num_examples: 1805012
  download_size: 3477902737
  dataset_size: 5889963046
- config_name: 20230601.eu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 547125100
    num_examples: 405840
  download_size: 264099434
  dataset_size: 547125100
- config_name: 20230601.ext
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4182030
    num_examples: 3636
  download_size: 2631658
  dataset_size: 4182030
- config_name: 20230601.fa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1851617207
    num_examples: 964236
  download_size: 759372155
  dataset_size: 1851617207
- config_name: 20230601.fat
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1933259
    num_examples: 1046
  download_size: 1067434
  dataset_size: 1933259
- config_name: 20230601.ff
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1401981
    num_examples: 1484
  download_size: 824781
  dataset_size: 1401981
- config_name: 20230601.fi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1125659121
    num_examples: 553519
  download_size: 678674705
  dataset_size: 1125659121
- config_name: 20230601.fiu-vro
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4773469
    num_examples: 6559
  download_size: 2464729
  dataset_size: 4773469
- config_name: 20230601.fj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 593373
    num_examples: 1283
  download_size: 323108
  dataset_size: 593373
- config_name: 20230601.fo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 15058635
    num_examples: 13954
  download_size: 8633381
  dataset_size: 15058635
- config_name: 20230601.fr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7910192478
    num_examples: 2525926
  download_size: 4618774275
  dataset_size: 7910192478
- config_name: 20230601.frp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3517265
    num_examples: 5689
  download_size: 1847765
  dataset_size: 3517265
- config_name: 20230601.frr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10292357
    num_examples: 17260
  download_size: 5084999
  dataset_size: 10292357
- config_name: 20230601.fur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4062291
    num_examples: 3967
  download_size: 2401534
  dataset_size: 4062291
- config_name: 20230601.fy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 130189677
    num_examples: 51506
  download_size: 73624821
  dataset_size: 130189677
- config_name: 20230601.ga
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 59266973
    num_examples: 58579
  download_size: 33377343
  dataset_size: 59266973
- config_name: 20230601.gag
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2405210
    num_examples: 2966
  download_size: 1319553
  dataset_size: 2405210
- config_name: 20230601.gan
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2878337
    num_examples: 6691
  download_size: 1485195
  dataset_size: 2878337
- config_name: 20230601.gcr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2335924
    num_examples: 2397
  download_size: 1344338
  dataset_size: 2335924
- config_name: 20230601.gd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14026914
    num_examples: 16018
  download_size: 7175920
  dataset_size: 14026914
- config_name: 20230601.gl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 483432936
    num_examples: 196473
  download_size: 287329100
  dataset_size: 483432936
- config_name: 20230601.glk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6067898
    num_examples: 7035
  download_size: 2372761
  dataset_size: 6067898
- config_name: 20230601.gn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6754303
    num_examples: 5298
  download_size: 3702975
  dataset_size: 6754303
- config_name: 20230601.gom
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 30830020
    num_examples: 4250
  download_size: 11258918
  dataset_size: 30830020
- config_name: 20230601.gor
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6111487
    num_examples: 14556
  download_size: 2036928
  dataset_size: 6111487
- config_name: 20230601.got
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1518930
    num_examples: 1005
  download_size: 626840
  dataset_size: 1518930
- config_name: 20230601.gu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 120869564
    num_examples: 30357
  download_size: 39339802
  dataset_size: 120869564
- config_name: 20230601.guc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 916033
    num_examples: 578
  download_size: 547551
  dataset_size: 916033
- config_name: 20230601.gur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1414225
    num_examples: 954
  download_size: 753483
  dataset_size: 1414225
- config_name: 20230601.guw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1894278
    num_examples: 1301
  download_size: 1027313
  dataset_size: 1894278
- config_name: 20230601.gv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5969707
    num_examples: 5954
  download_size: 3155779
  dataset_size: 5969707
- config_name: 20230601.ha
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 62945985
    num_examples: 27905
  download_size: 35159511
  dataset_size: 62945985
- config_name: 20230601.hak
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4493017
    num_examples: 10183
  download_size: 1875697
  dataset_size: 4493017
- config_name: 20230601.haw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1648045
    num_examples: 2580
  download_size: 681202
  dataset_size: 1648045
- config_name: 20230601.he
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1890961532
    num_examples: 325534
  download_size: 955373507
  dataset_size: 1890961532
- config_name: 20230601.hi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 652930384
    num_examples: 160068
  download_size: 230339569
  dataset_size: 652930384
- config_name: 20230601.hif
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5670768
    num_examples: 10975
  download_size: 2708959
  dataset_size: 5670768
- config_name: 20230601.ho
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3450
    num_examples: 3
  download_size: 7714
  dataset_size: 3450
- config_name: 20230601.hsb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 15650862
    num_examples: 13929
  download_size: 7422054
  dataset_size: 15650862
- config_name: 20230601.ht
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 54468681
    num_examples: 69778
  download_size: 21591458
  dataset_size: 54468681
- config_name: 20230601.hu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1490296647
    num_examples: 526030
  download_size: 904279478
  dataset_size: 1490296647
- config_name: 20230601.hy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1142467643
    num_examples: 297933
  download_size: 477398053
  dataset_size: 1142467643
- config_name: 20230601.hyw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 57478946
    num_examples: 10933
  download_size: 26499417
  dataset_size: 57478946
- config_name: 20230601.ia
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16183963
    num_examples: 27939
  download_size: 8108662
  dataset_size: 16183963
- config_name: 20230601.id
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1086885042
    num_examples: 648383
  download_size: 575124507
  dataset_size: 1086885042
- config_name: 20230601.ie
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6482834
    num_examples: 11705
  download_size: 2881031
  dataset_size: 6482834
- config_name: 20230601.ig
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 45043729
    num_examples: 16970
  download_size: 23565907
  dataset_size: 45043729
- config_name: 20230601.ii
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8921
    num_examples: 14
  download_size: 14936
  dataset_size: 8921
- config_name: 20230601.ik
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 190236
    num_examples: 823
  download_size: 109460
  dataset_size: 190236
- config_name: 20230601.ilo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16860855
    num_examples: 15379
  download_size: 7350161
  dataset_size: 16860855
- config_name: 20230601.inh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2697943
    num_examples: 2108
  download_size: 1257824
  dataset_size: 2697943
- config_name: 20230601.io
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 37291268
    num_examples: 38155
  download_size: 16629067
  dataset_size: 37291268
- config_name: 20230601.is
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 86487184
    num_examples: 56795
  download_size: 51372350
  dataset_size: 86487184
- config_name: 20230601.it
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4826403309
    num_examples: 1812514
  download_size: 2926177870
  dataset_size: 4826403309
- config_name: 20230601.iu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 284349
    num_examples: 564
  download_size: 132368
  dataset_size: 284349
- config_name: 20230601.ja
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6913216645
    num_examples: 1373311
  download_size: 3923535785
  dataset_size: 6913216645
- config_name: 20230601.jam
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1140551
    num_examples: 1771
  download_size: 700995
  dataset_size: 1140551
- config_name: 20230601.jbo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2521508
    num_examples: 1390
  download_size: 888087
  dataset_size: 2521508
- config_name: 20230601.jv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 70703094
    num_examples: 73024
  download_size: 36199167
  dataset_size: 70703094
- config_name: 20230601.ka
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 693108151
    num_examples: 168185
  download_size: 237719175
  dataset_size: 693108151
- config_name: 20230601.kaa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4584133
    num_examples: 3560
  download_size: 2620141
  dataset_size: 4584133
- config_name: 20230601.kab
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4374017
    num_examples: 5800
  download_size: 2570505
  dataset_size: 4374017
- config_name: 20230601.kbd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3034249
    num_examples: 1637
  download_size: 1317388
  dataset_size: 3034249
- config_name: 20230601.kbp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3571606
    num_examples: 1918
  download_size: 1794790
  dataset_size: 3571606
- config_name: 20230601.kcg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 663326
    num_examples: 825
  download_size: 350587
  dataset_size: 663326
- config_name: 20230601.kg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 463083
    num_examples: 1333
  download_size: 240321
  dataset_size: 463083
- config_name: 20230601.ki
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 453178
    num_examples: 1635
  download_size: 243544
  dataset_size: 453178
- config_name: 20230601.kj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5190
    num_examples: 5
  download_size: 10453
  dataset_size: 5190
- config_name: 20230601.kk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 488955469
    num_examples: 237304
  download_size: 176872369
  dataset_size: 488955469
- config_name: 20230601.kl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 312839
    num_examples: 298
  download_size: 193192
  dataset_size: 312839
- config_name: 20230601.km
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 102051337
    num_examples: 11784
  download_size: 35067125
  dataset_size: 102051337
- config_name: 20230601.kn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 394061570
    num_examples: 30793
  download_size: 143867617
  dataset_size: 394061570
- config_name: 20230601.ko
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1374136790
    num_examples: 635278
  download_size: 777760206
  dataset_size: 1374136790
- config_name: 20230601.koi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5077608
    num_examples: 3487
  download_size: 1880469
  dataset_size: 5077608
- config_name: 20230601.krc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4592333
    num_examples: 2098
  download_size: 2019043
  dataset_size: 4592333
- config_name: 20230601.ks
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2380920
    num_examples: 4060
  download_size: 849849
  dataset_size: 2380920
- config_name: 20230601.ksh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3110398
    num_examples: 2945
  download_size: 2004743
  dataset_size: 3110398
- config_name: 20230601.ku
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 42327613
    num_examples: 59529
  download_size: 21970440
  dataset_size: 42327613
- config_name: 20230601.kv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9221030
    num_examples: 5589
  download_size: 3676356
  dataset_size: 9221030
- config_name: 20230601.kw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4653320
    num_examples: 7070
  download_size: 2695687
  dataset_size: 4653320
- config_name: 20230601.ky
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 168214006
    num_examples: 80594
  download_size: 64353836
  dataset_size: 168214006
- config_name: 20230601.la
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 139977277
    num_examples: 137851
  download_size: 75850224
  dataset_size: 139977277
- config_name: 20230601.lad
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4820385
    num_examples: 3638
  download_size: 2703040
  dataset_size: 4820385
- config_name: 20230601.lb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 87567860
    num_examples: 61757
  download_size: 49791518
  dataset_size: 87567860
- config_name: 20230601.lbe
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 698292
    num_examples: 1276
  download_size: 282486
  dataset_size: 698292
- config_name: 20230601.lez
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9785097
    num_examples: 4256
  download_size: 3849506
  dataset_size: 9785097
- config_name: 20230601.lfn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8850905
    num_examples: 4805
  download_size: 5189938
  dataset_size: 8850905
- config_name: 20230601.lg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6771716
    num_examples: 4016
  download_size: 3634293
  dataset_size: 6771716
- config_name: 20230601.li
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 29183994
    num_examples: 14308
  download_size: 17566220
  dataset_size: 29183994
- config_name: 20230601.lij
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11088927
    num_examples: 11132
  download_size: 6042920
  dataset_size: 11088927
- config_name: 20230601.lld
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 45325217
    num_examples: 158242
  download_size: 12436563
  dataset_size: 45325217
- config_name: 20230601.lmo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 42267433
    num_examples: 71061
  download_size: 18724770
  dataset_size: 42267433
- config_name: 20230601.ln
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2024697
    num_examples: 3515
  download_size: 1115171
  dataset_size: 2024697
- config_name: 20230601.lo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14729412
    num_examples: 4928
  download_size: 5382036
  dataset_size: 14729412
- config_name: 20230601.lrc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 144
    num_examples: 1
  download_size: 2723
  dataset_size: 144
- config_name: 20230601.lt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 331252602
    num_examples: 208114
  download_size: 191925990
  dataset_size: 331252602
- config_name: 20230601.ltg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 901980
    num_examples: 1044
  download_size: 522213
  dataset_size: 901980
- config_name: 20230601.lv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 220969643
    num_examples: 120295
  download_size: 126161867
  dataset_size: 220969643
- config_name: 20230601.mad
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1325061
    num_examples: 1103
  download_size: 764579
  dataset_size: 1325061
- config_name: 20230601.mai
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21215977
    num_examples: 14622
  download_size: 6041134
  dataset_size: 21215977
- config_name: 20230601.map-bms
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5400186
    num_examples: 13554
  download_size: 2420169
  dataset_size: 5400186
- config_name: 20230601.mdf
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4033455
    num_examples: 3473
  download_size: 1513534
  dataset_size: 4033455
- config_name: 20230601.mg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 71936817
    num_examples: 95675
  download_size: 21206762
  dataset_size: 71936817
- config_name: 20230601.mh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11524
    num_examples: 8
  download_size: 16877
  dataset_size: 11524
- config_name: 20230601.mhr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19030836
    num_examples: 11016
  download_size: 6821706
  dataset_size: 19030836
- config_name: 20230601.mi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4120867
    num_examples: 7855
  download_size: 1016905
  dataset_size: 4120867
- config_name: 20230601.min
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 118484114
    num_examples: 226953
  download_size: 25401691
  dataset_size: 118484114
- config_name: 20230601.mk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 633734922
    num_examples: 136723
  download_size: 263383509
  dataset_size: 633734922
- config_name: 20230601.ml
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 485143578
    num_examples: 84794
  download_size: 179727029
  dataset_size: 485143578
- config_name: 20230601.mn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 88813927
    num_examples: 23385
  download_size: 40026827
  dataset_size: 88813927
- config_name: 20230601.mni
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9790220
    num_examples: 10877
  download_size: 2193774
  dataset_size: 9790220
- config_name: 20230601.mnw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 45579901
    num_examples: 3184
  download_size: 13207357
  dataset_size: 45579901
- config_name: 20230601.mr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 254646708
    num_examples: 92898
  download_size: 79982313
  dataset_size: 254646708
- config_name: 20230601.mrj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8729899
    num_examples: 10542
  download_size: 3278742
  dataset_size: 8729899
- config_name: 20230601.ms
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 410354637
    num_examples: 365491
  download_size: 206610861
  dataset_size: 410354637
- config_name: 20230601.mt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 26613613
    num_examples: 5369
  download_size: 15563924
  dataset_size: 26613613
- config_name: 20230601.mus
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 922
    num_examples: 2
  download_size: 5286
  dataset_size: 922
- config_name: 20230601.mwl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19284605
    num_examples: 4474
  download_size: 11469001
  dataset_size: 19284605
- config_name: 20230601.my
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 310836677
    num_examples: 108750
  download_size: 84350660
  dataset_size: 310836677
- config_name: 20230601.myv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11073788
    num_examples: 7910
  download_size: 4560227
  dataset_size: 11073788
- config_name: 20230601.mzn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14682517
    num_examples: 15995
  download_size: 4856126
  dataset_size: 14682517
- config_name: 20230601.nah
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2843124
    num_examples: 6654
  download_size: 1347633
  dataset_size: 2843124
- config_name: 20230601.nap
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6365024
    num_examples: 14849
  download_size: 3169570
  dataset_size: 6365024
- config_name: 20230601.nds
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 92743798
    num_examples: 84225
  download_size: 47925882
  dataset_size: 92743798
- config_name: 20230601.nds-nl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13432115
    num_examples: 7669
  download_size: 8207550
  dataset_size: 13432115
- config_name: 20230601.ne
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 105562688
    num_examples: 32084
  download_size: 36335987
  dataset_size: 105562688
- config_name: 20230601.new
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 159067466
    num_examples: 73004
  download_size: 20472096
  dataset_size: 159067466
- config_name: 20230601.ng
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 68090
    num_examples: 21
  download_size: 52355
  dataset_size: 68090
- config_name: 20230601.nia
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1793045
    num_examples: 1638
  download_size: 908004
  dataset_size: 1793045
- config_name: 20230601.nl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2607286503
    num_examples: 2123556
  download_size: 1451716829
  dataset_size: 2607286503
- config_name: 20230601.nn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 233905017
    num_examples: 165610
  download_size: 132674509
  dataset_size: 233905017
- config_name: 20230601.no
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1018553680
    num_examples: 611542
  download_size: 594771430
  dataset_size: 1018553680
- config_name: 20230601.nov
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 912652
    num_examples: 1626
  download_size: 466451
  dataset_size: 912652
- config_name: 20230601.nqo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8295905
    num_examples: 1577
  download_size: 3503359
  dataset_size: 8295905
- config_name: 20230601.nrm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3212495
    num_examples: 4887
  download_size: 1504411
  dataset_size: 3212495
- config_name: 20230601.nso
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2753446
    num_examples: 8617
  download_size: 912548
  dataset_size: 2753446
- config_name: 20230601.nv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16785014
    num_examples: 22189
  download_size: 3271175
  dataset_size: 16785014
- config_name: 20230601.ny
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1693443
    num_examples: 1133
  download_size: 937213
  dataset_size: 1693443
- config_name: 20230601.oc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 117818984
    num_examples: 88886
  download_size: 62764519
  dataset_size: 117818984
- config_name: 20230601.olo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3122448
    num_examples: 4514
  download_size: 1707016
  dataset_size: 3122448
- config_name: 20230601.om
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3057811
    num_examples: 1574
  download_size: 1720686
  dataset_size: 3057811
- config_name: 20230601.or
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 71342568
    num_examples: 16793
  download_size: 25347488
  dataset_size: 71342568
- config_name: 20230601.os
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12975022
    num_examples: 17066
  download_size: 5519425
  dataset_size: 12975022
- config_name: 20230601.pa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 205173613
    num_examples: 49955
  download_size: 78370120
  dataset_size: 205173613
- config_name: 20230601.pag
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1336264
    num_examples: 2638
  download_size: 417192
  dataset_size: 1336264
- config_name: 20230601.pam
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8241795
    num_examples: 8935
  download_size: 4231831
  dataset_size: 8241795
- config_name: 20230601.pap
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3662048
    num_examples: 3237
  download_size: 2098802
  dataset_size: 3662048
- config_name: 20230601.pcd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5622299
    num_examples: 5639
  download_size: 3094652
  dataset_size: 5622299
- config_name: 20230601.pcm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1531576
    num_examples: 954
  download_size: 937573
  dataset_size: 1531576
- config_name: 20230601.pdc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1196915
    num_examples: 2162
  download_size: 688667
  dataset_size: 1196915
- config_name: 20230601.pfl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3682829
    num_examples: 2756
  download_size: 1962515
  dataset_size: 3682829
- config_name: 20230601.pi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1134003
    num_examples: 3056
  download_size: 196632
  dataset_size: 1134003
- config_name: 20230601.pih
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 378374
    num_examples: 930
  download_size: 236668
  dataset_size: 378374
- config_name: 20230601.pl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2904184909
    num_examples: 1569515
  download_size: 1787531053
  dataset_size: 2904184909
- config_name: 20230601.pms
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 34301415
    num_examples: 67899
  download_size: 11986805
  dataset_size: 34301415
- config_name: 20230601.pnb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 298316454
    num_examples: 70562
  download_size: 130650981
  dataset_size: 298316454
- config_name: 20230601.pnt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 675000
    num_examples: 535
  download_size: 298222
  dataset_size: 675000
- config_name: 20230601.ps
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 104012780
    num_examples: 19565
  download_size: 48710783
  dataset_size: 104012780
- config_name: 20230601.pt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2693736720
    num_examples: 1103446
  download_size: 1571347957
  dataset_size: 2693736720
- config_name: 20230601.pwn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 800565
    num_examples: 380
  download_size: 446595
  dataset_size: 800565
- config_name: 20230601.qu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16631588
    num_examples: 23909
  download_size: 7575996
  dataset_size: 16631588
- config_name: 20230601.rm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 17822525
    num_examples: 3815
  download_size: 10339459
  dataset_size: 17822525
- config_name: 20230601.rmy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 491195
    num_examples: 930
  download_size: 285442
  dataset_size: 491195
- config_name: 20230601.rn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 522745
    num_examples: 805
  download_size: 295575
  dataset_size: 522745
- config_name: 20230601.ro
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 834681972
    num_examples: 440015
  download_size: 466488330
  dataset_size: 834681972
- config_name: 20230601.roa-rup
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1713384
    num_examples: 1409
  download_size: 955926
  dataset_size: 1713384
- config_name: 20230601.roa-tara
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7418561
    num_examples: 9337
  download_size: 3970663
  dataset_size: 7418561
- config_name: 20230601.ru
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10097718899
    num_examples: 1918942
  download_size: 4880008552
  dataset_size: 10097718899
- config_name: 20230601.rue
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12975836
    num_examples: 8703
  download_size: 6269020
  dataset_size: 12975836
- config_name: 20230601.rw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10794817
    num_examples: 7425
  download_size: 6009979
  dataset_size: 10794817
- config_name: 20230601.sa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 69233233
    num_examples: 12101
  download_size: 23590461
  dataset_size: 69233233
- config_name: 20230601.sah
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 47530889
    num_examples: 16598
  download_size: 21213858
  dataset_size: 47530889
- config_name: 20230601.sat
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 35005528
    num_examples: 8264
  download_size: 12124520
  dataset_size: 35005528
- config_name: 20230601.sc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12683528
    num_examples: 7540
  download_size: 7650423
  dataset_size: 12683528
- config_name: 20230601.scn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 17672274
    num_examples: 26507
  download_size: 10210177
  dataset_size: 17672274
- config_name: 20230601.sco
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 43796852
    num_examples: 36206
  download_size: 24764727
  dataset_size: 43796852
- config_name: 20230601.sd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36672141
    num_examples: 16882
  download_size: 17409382
  dataset_size: 36672141
- config_name: 20230601.se
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3600247
    num_examples: 8040
  download_size: 1814982
  dataset_size: 3600247
- config_name: 20230601.sg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 127791
    num_examples: 548
  download_size: 63800
  dataset_size: 127791
- config_name: 20230601.sh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 569915575
    num_examples: 458272
  download_size: 270502498
  dataset_size: 569915575
- config_name: 20230601.shi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2195129
    num_examples: 1544
  download_size: 1311300
  dataset_size: 2195129
- config_name: 20230601.shn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 33233508
    num_examples: 13706
  download_size: 8107005
  dataset_size: 33233508
- config_name: 20230601.si
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 135560965
    num_examples: 22574
  download_size: 52870973
  dataset_size: 135560965
- config_name: 20230601.sk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 410287543
    num_examples: 240597
  download_size: 237984111
  dataset_size: 410287543
- config_name: 20230601.skr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 22294235
    num_examples: 5739
  download_size: 9744982
  dataset_size: 22294235
- config_name: 20230601.sl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 444732062
    num_examples: 181212
  download_size: 263697513
  dataset_size: 444732062
- config_name: 20230601.sm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 891597
    num_examples: 1143
  download_size: 485815
  dataset_size: 891597
- config_name: 20230601.smn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5526668
    num_examples: 5094
  download_size: 2710998
  dataset_size: 5526668
- config_name: 20230601.sn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9252554
    num_examples: 10917
  download_size: 4738498
  dataset_size: 9252554
- config_name: 20230601.so
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14893759
    num_examples: 10812
  download_size: 8617659
  dataset_size: 14893759
- config_name: 20230601.sq
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 197206847
    num_examples: 100423
  download_size: 110414776
  dataset_size: 197206847
- config_name: 20230601.sr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1690745100
    num_examples: 671352
  download_size: 695586988
  dataset_size: 1690745100
- config_name: 20230601.srn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 649044
    num_examples: 1218
  download_size: 214987
  dataset_size: 649044
- config_name: 20230601.ss
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 861417
    num_examples: 720
  download_size: 489383
  dataset_size: 861417
- config_name: 20230601.st
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 934954
    num_examples: 1073
  download_size: 517491
  dataset_size: 934954
- config_name: 20230601.stq
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4929355
    num_examples: 4129
  download_size: 2878034
  dataset_size: 4929355
- config_name: 20230601.su
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 47909002
    num_examples: 61490
  download_size: 19683635
  dataset_size: 47909002
- config_name: 20230601.sv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2133848723
    num_examples: 2564263
  download_size: 1002020509
  dataset_size: 2133848723
- config_name: 20230601.sw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 71857907
    num_examples: 77334
  download_size: 35252918
  dataset_size: 71857907
- config_name: 20230601.szl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21335080
    num_examples: 56652
  download_size: 7284436
  dataset_size: 21335080
- config_name: 20230601.szy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10412319
    num_examples: 4709
  download_size: 5572825
  dataset_size: 10412319
- config_name: 20230601.tay
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2779734
    num_examples: 2595
  download_size: 1147869
  dataset_size: 2779734
- config_name: 20230601.tcy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11968976
    num_examples: 2173
  download_size: 4524692
  dataset_size: 11968976
- config_name: 20230601.te
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 705766405
    num_examples: 83107
  download_size: 206360536
  dataset_size: 705766405
- config_name: 20230601.tet
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1457614
    num_examples: 1460
  download_size: 739227
  dataset_size: 1457614
- config_name: 20230601.tg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 145506377
    num_examples: 109839
  download_size: 48637192
  dataset_size: 145506377
- config_name: 20230601.th
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 987873133
    num_examples: 156445
  download_size: 365894157
  dataset_size: 987873133
- config_name: 20230601.ti
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 665363
    num_examples: 433
  download_size: 328037
  dataset_size: 665363
- config_name: 20230601.tk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12580480
    num_examples: 7836
  download_size: 6951103
  dataset_size: 12580480
- config_name: 20230601.tl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 82731267
    num_examples: 44797
  download_size: 44058126
  dataset_size: 82731267
- config_name: 20230601.tn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3562981
    num_examples: 1162
  download_size: 1244173
  dataset_size: 3562981
- config_name: 20230601.to
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1074947
    num_examples: 1848
  download_size: 510687
  dataset_size: 1074947
- config_name: 20230601.tpi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 450891
    num_examples: 1390
  download_size: 236441
  dataset_size: 450891
- config_name: 20230601.tr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 965186144
    num_examples: 524184
  download_size: 543958666
  dataset_size: 965186144
- config_name: 20230601.trv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4873244
    num_examples: 1809
  download_size: 2635461
  dataset_size: 4873244
- config_name: 20230601.ts
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 841497
    num_examples: 769
  download_size: 451958
  dataset_size: 841497
- config_name: 20230601.tt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 679276199
    num_examples: 500608
  download_size: 128386602
  dataset_size: 679276199
- config_name: 20230601.tum
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8395079
    num_examples: 14169
  download_size: 3225881
  dataset_size: 8395079
- config_name: 20230601.tw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6562128
    num_examples: 3608
  download_size: 3389042
  dataset_size: 6562128
- config_name: 20230601.ty
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 324678
    num_examples: 1348
  download_size: 145184
  dataset_size: 324678
- config_name: 20230601.tyv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14032235
    num_examples: 3459
  download_size: 6378954
  dataset_size: 14032235
- config_name: 20230601.udm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6918258
    num_examples: 5586
  download_size: 2937644
  dataset_size: 6918258
- config_name: 20230601.ug
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 41939834
    num_examples: 8557
  download_size: 17588763
  dataset_size: 41939834
- config_name: 20230601.uk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4815765166
    num_examples: 1266287
  download_size: 2257591520
  dataset_size: 4815765166
- config_name: 20230601.ur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 394375073
    num_examples: 194435
  download_size: 160552761
  dataset_size: 394375073
- config_name: 20230601.uz
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 372775375
    num_examples: 241353
  download_size: 196367714
  dataset_size: 372775375
- config_name: 20230601.ve
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 347015
    num_examples: 836
  download_size: 159547
  dataset_size: 347015
- config_name: 20230601.vec
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 37671800
    num_examples: 69181
  download_size: 16029908
  dataset_size: 37671800
- config_name: 20230601.vep
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11259222
    num_examples: 6851
  download_size: 6196150
  dataset_size: 11259222
- config_name: 20230601.vi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1584847634
    num_examples: 1283785
  download_size: 731354374
  dataset_size: 1584847634
- config_name: 20230601.vls
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11296047
    num_examples: 7824
  download_size: 6952370
  dataset_size: 11296047
- config_name: 20230601.vo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 18943004
    num_examples: 33641
  download_size: 6379410
  dataset_size: 18943004
- config_name: 20230601.wa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11990482
    num_examples: 11858
  download_size: 7144929
  dataset_size: 11990482
- config_name: 20230601.war
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 468715357
    num_examples: 1266238
  download_size: 109807953
  dataset_size: 468715357
- config_name: 20230601.wo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3498671
    num_examples: 1719
  download_size: 2076485
  dataset_size: 3498671
- config_name: 20230601.wuu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 24986530
    num_examples: 42950
  download_size: 15960262
  dataset_size: 24986530
- config_name: 20230601.xal
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1386014
    num_examples: 2307
  download_size: 508481
  dataset_size: 1386014
- config_name: 20230601.xh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2320277
    num_examples: 1601
  download_size: 1444732
  dataset_size: 2320277
- config_name: 20230601.xmf
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36557690
    num_examples: 17705
  download_size: 12535173
  dataset_size: 36557690
- config_name: 20230601.yi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36031133
    num_examples: 15297
  download_size: 16153644
  dataset_size: 36031133
- config_name: 20230601.yo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 18018480
    num_examples: 33179
  download_size: 8274108
  dataset_size: 18018480
- config_name: 20230601.za
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1276590
    num_examples: 2722
  download_size: 642448
  dataset_size: 1276590
- config_name: 20230601.zea
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5059421
    num_examples: 5756
  download_size: 2547904
  dataset_size: 5059421
- config_name: 20230601.zh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2720688196
    num_examples: 1357881
  download_size: 1718953037
  dataset_size: 2720688196
- config_name: 20230601.zh-classical
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14617535
    num_examples: 12513
  download_size: 9882532
  dataset_size: 14617535
- config_name: 20230601.zh-min-nan
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 159218053
    num_examples: 432531
  download_size: 37371610
  dataset_size: 159218053
- config_name: 20230601.zh-yue
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 107325669
    num_examples: 131542
  download_size: 63294114
  dataset_size: 107325669
- config_name: 20230601.zu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6915666
    num_examples: 11381
  download_size: 3683813
  dataset_size: 6915666
- config_name: 20230601.hr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 438311404
    num_examples: 200747
  download_size: 275098294
  dataset_size: 438311404
- config_name: 20230601.simple
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 282844880
    num_examples: 231233
  download_size: 154520600
  dataset_size: 282844880
- config_name: 20230601.ta
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 789472198
    num_examples: 156273
  download_size: 258263767
  dataset_size: 789472198
- config_name: 20230901.ab
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4257828
    num_examples: 6135
  download_size: 1204070
  dataset_size: 4257828
- config_name: 20230901.ace
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4988748
    num_examples: 12932
  download_size: 1532859
  dataset_size: 4988748
- config_name: 20230901.ady
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 732900
    num_examples: 656
  download_size: 334202
  dataset_size: 732900
- config_name: 20230901.af
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 223836122
    num_examples: 110683
  download_size: 122868601
  dataset_size: 223836122
- config_name: 20230901.ak
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 189
    num_examples: 1
  download_size: 3045
  dataset_size: 189
- config_name: 20230901.als
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 81066470
    num_examples: 29914
  download_size: 49151942
  dataset_size: 81066470
- config_name: 20230901.alt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6370197
    num_examples: 1076
  download_size: 2683190
  dataset_size: 6370197
- config_name: 20230901.am
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 24108874
    num_examples: 13863
  download_size: 10659605
  dataset_size: 24108874
- config_name: 20230901.ami
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4376488
    num_examples: 1613
  download_size: 2207864
  dataset_size: 4376488
- config_name: 20230901.an
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 57157273
    num_examples: 44090
  download_size: 29392661
  dataset_size: 57157273
- config_name: 20230901.ang
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2899899
    num_examples: 4106
  download_size: 1782699
  dataset_size: 2899899
- config_name: 20230901.anp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9238243
    num_examples: 2753
  download_size: 3338080
  dataset_size: 9238243
- config_name: 20230901.ar
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3090850739
    num_examples: 1214692
  download_size: 1336764394
  dataset_size: 3090850739
- config_name: 20230901.arc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 837851
    num_examples: 1935
  download_size: 364313
  dataset_size: 837851
- config_name: 20230901.ary
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10716445
    num_examples: 7181
  download_size: 4413789
  dataset_size: 10716445
- config_name: 20230901.arz
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1371439747
    num_examples: 1619204
  download_size: 309552126
  dataset_size: 1371439747
- config_name: 20230901.as
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 88616101
    num_examples: 12209
  download_size: 33925273
  dataset_size: 88616101
- config_name: 20230901.ast
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 470680707
    num_examples: 133219
  download_size: 271143532
  dataset_size: 470680707
- config_name: 20230901.atj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1009452
    num_examples: 1967
  download_size: 512377
  dataset_size: 1009452
- config_name: 20230901.av
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6136668
    num_examples: 3420
  download_size: 2568423
  dataset_size: 6136668
- config_name: 20230901.avk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 31833142
    num_examples: 28141
  download_size: 7911635
  dataset_size: 31833142
- config_name: 20230901.awa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3591539
    num_examples: 3696
  download_size: 1233124
  dataset_size: 3591539
- config_name: 20230901.ay
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4378141
    num_examples: 5348
  download_size: 1748641
  dataset_size: 4378141
- config_name: 20230901.az
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 430470815
    num_examples: 195659
  download_size: 228140471
  dataset_size: 430470815
- config_name: 20230901.azb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 186776266
    num_examples: 243263
  download_size: 46619566
  dataset_size: 186776266
- config_name: 20230901.ba
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 296321332
    num_examples: 63134
  download_size: 121809783
  dataset_size: 296321332
- config_name: 20230901.ban
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 17383384
    num_examples: 20242
  download_size: 6524686
  dataset_size: 17383384
- config_name: 20230901.bar
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36251706
    num_examples: 27040
  download_size: 21762636
  dataset_size: 36251706
- config_name: 20230901.bat-smg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7584027
    num_examples: 17214
  download_size: 3437198
  dataset_size: 7584027
- config_name: 20230901.be-x-old
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 249911330
    num_examples: 83778
  download_size: 113105161
  dataset_size: 249911330
- config_name: 20230901.bcl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19285430
    num_examples: 14723
  download_size: 10682007
  dataset_size: 19285430
- config_name: 20230901.be
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 618711883
    num_examples: 234760
  download_size: 286395236
  dataset_size: 618711883
- config_name: 20230901.bg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1095408838
    num_examples: 293306
  download_size: 514238024
  dataset_size: 1095408838
- config_name: 20230901.bh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16433197
    num_examples: 8552
  download_size: 5775459
  dataset_size: 16433197
- config_name: 20230901.bi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 405238
    num_examples: 1544
  download_size: 204286
  dataset_size: 405238
- config_name: 20230901.bjn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6761698
    num_examples: 10460
  download_size: 3255595
  dataset_size: 6761698
- config_name: 20230901.blk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 25837114
    num_examples: 2923
  download_size: 7802724
  dataset_size: 25837114
- config_name: 20230901.bm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 591154
    num_examples: 1254
  download_size: 324954
  dataset_size: 591154
- config_name: 20230901.bn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 945095157
    num_examples: 141288
  download_size: 340510394
  dataset_size: 945095157
- config_name: 20230901.bo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 132468794
    num_examples: 12826
  download_size: 38750901
  dataset_size: 132468794
- config_name: 20230901.bpy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 42975074
    num_examples: 25165
  download_size: 6557544
  dataset_size: 42975074
- config_name: 20230901.br
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 84959382
    num_examples: 83342
  download_size: 49373423
  dataset_size: 84959382
- config_name: 20230901.bs
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 192322421
    num_examples: 92325
  download_size: 106973603
  dataset_size: 192322421
- config_name: 20230901.bug
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3433942
    num_examples: 15877
  download_size: 816476
  dataset_size: 3433942
- config_name: 20230901.bxr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6686504
    num_examples: 2791
  download_size: 3073419
  dataset_size: 6686504
- config_name: 20230901.ca
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1942397691
    num_examples: 733807
  download_size: 1127952357
  dataset_size: 1942397691
- config_name: 20230901.cbk-zam
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1997943
    num_examples: 3276
  download_size: 776590
  dataset_size: 1997943
- config_name: 20230901.cdo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5085776
    num_examples: 16406
  download_size: 1972779
  dataset_size: 5085776
- config_name: 20230901.ce
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 729121943
    num_examples: 600961
  download_size: 87442481
  dataset_size: 729121943
- config_name: 20230901.ceb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4568428530
    num_examples: 6122999
  download_size: 925715583
  dataset_size: 4568428530
- config_name: 20230901.ch
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 187141
    num_examples: 591
  download_size: 93248
  dataset_size: 187141
- config_name: 20230901.cho
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7974
    num_examples: 14
  download_size: 9782
  dataset_size: 7974
- config_name: 20230901.chr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 768617
    num_examples: 1121
  download_size: 343463
  dataset_size: 768617
- config_name: 20230901.chy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 145752
    num_examples: 800
  download_size: 74383
  dataset_size: 145752
- config_name: 20230901.ckb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 105393226
    num_examples: 51534
  download_size: 42196297
  dataset_size: 105393226
- config_name: 20230901.co
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9828777
    num_examples: 7286
  download_size: 5312668
  dataset_size: 9828777
- config_name: 20230901.cr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 54526
    num_examples: 176
  download_size: 34910
  dataset_size: 54526
- config_name: 20230901.crh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9450530
    num_examples: 26893
  download_size: 3578677
  dataset_size: 9450530
- config_name: 20230901.cs
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1552256812
    num_examples: 531017
  download_size: 981191812
  dataset_size: 1552256812
- config_name: 20230901.csb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3748403
    num_examples: 5480
  download_size: 2055688
  dataset_size: 3748403
- config_name: 20230901.cu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 981478
    num_examples: 1237
  download_size: 397764
  dataset_size: 981478
- config_name: 20230901.cv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 81463626
    num_examples: 51647
  download_size: 29416321
  dataset_size: 81463626
- config_name: 20230901.cy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 305551170
    num_examples: 279341
  download_size: 111947867
  dataset_size: 305551170
- config_name: 20230901.da
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 544417184
    num_examples: 294196
  download_size: 329369262
  dataset_size: 544417184
- config_name: 20230901.dag
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11405576
    num_examples: 9584
  download_size: 4905465
  dataset_size: 11405576
- config_name: 20230901.de
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9552907552
    num_examples: 2828561
  download_size: 5816126238
  dataset_size: 9552907552
- config_name: 20230901.din
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 562639
    num_examples: 511
  download_size: 339141
  dataset_size: 562639
- config_name: 20230901.diq
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19574906
    num_examples: 41541
  download_size: 7581584
  dataset_size: 19574906
- config_name: 20230901.dsb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3314217
    num_examples: 3376
  download_size: 1930644
  dataset_size: 3314217
- config_name: 20230901.dty
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6999985
    num_examples: 3629
  download_size: 2505457
  dataset_size: 6999985
- config_name: 20230901.dv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13919491
    num_examples: 4345
  download_size: 5255676
  dataset_size: 13919491
- config_name: 20230901.dz
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8837256
    num_examples: 787
  download_size: 2571127
  dataset_size: 8837256
- config_name: 20230901.ee
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 881798
    num_examples: 1172
  download_size: 482924
  dataset_size: 881798
- config_name: 20230901.el
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1335513979
    num_examples: 225623
  download_size: 637838917
  dataset_size: 1335513979
- config_name: 20230901.eml
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3620183
    num_examples: 12954
  download_size: 1687294
  dataset_size: 3620183
- config_name: 20230901.en
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21550145456
    num_examples: 6705754
  download_size: 12639246876
  dataset_size: 21550145456
- config_name: 20230901.eo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 517650573
    num_examples: 342419
  download_size: 299082818
  dataset_size: 517650573
- config_name: 20230901.es
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5977729133
    num_examples: 1826609
  download_size: 3528834297
  dataset_size: 5977729133
- config_name: 20230901.et
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 436983600
    num_examples: 239195
  download_size: 266302500
  dataset_size: 436983600
- config_name: 20230901.eu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 555867111
    num_examples: 408841
  download_size: 269449522
  dataset_size: 555867111
- config_name: 20230901.ext
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4334809
    num_examples: 3737
  download_size: 2724237
  dataset_size: 4334809
- config_name: 20230901.fa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1879857088
    num_examples: 972647
  download_size: 771735257
  dataset_size: 1879857088
- config_name: 20230901.fat
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2016722
    num_examples: 1113
  download_size: 1115327
  dataset_size: 2016722
- config_name: 20230901.ff
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1619659
    num_examples: 1929
  download_size: 951246
  dataset_size: 1619659
- config_name: 20230901.fi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1138299674
    num_examples: 558359
  download_size: 686112933
  dataset_size: 1138299674
- config_name: 20230901.fiu-vro
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4789834
    num_examples: 6572
  download_size: 2475758
  dataset_size: 4789834
- config_name: 20230901.fj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 600984
    num_examples: 1291
  download_size: 325888
  dataset_size: 600984
- config_name: 20230901.fo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 15387671
    num_examples: 14054
  download_size: 8835604
  dataset_size: 15387671
- config_name: 20230901.fr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8004882292
    num_examples: 2549364
  download_size: 4674130728
  dataset_size: 8004882292
- config_name: 20230901.frp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3646051
    num_examples: 5744
  download_size: 1899883
  dataset_size: 3646051
- config_name: 20230901.frr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10513932
    num_examples: 17708
  download_size: 5190719
  dataset_size: 10513932
- config_name: 20230901.fur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4073954
    num_examples: 3977
  download_size: 2408634
  dataset_size: 4073954
- config_name: 20230901.fy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 133127089
    num_examples: 52120
  download_size: 75305215
  dataset_size: 133127089
- config_name: 20230901.ga
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 60113068
    num_examples: 58940
  download_size: 33805587
  dataset_size: 60113068
- config_name: 20230901.gag
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2405444
    num_examples: 2967
  download_size: 1319216
  dataset_size: 2405444
- config_name: 20230901.gan
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2905828
    num_examples: 6739
  download_size: 1504592
  dataset_size: 2905828
- config_name: 20230901.gcr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2338042
    num_examples: 2398
  download_size: 1345374
  dataset_size: 2338042
- config_name: 20230901.gd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14057133
    num_examples: 16034
  download_size: 7199577
  dataset_size: 14057133
- config_name: 20230901.gl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 489325069
    num_examples: 198354
  download_size: 291176228
  dataset_size: 489325069
- config_name: 20230901.glk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6078167
    num_examples: 7046
  download_size: 2379845
  dataset_size: 6078167
- config_name: 20230901.gn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6869059
    num_examples: 5475
  download_size: 3777263
  dataset_size: 6869059
- config_name: 20230901.gom
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 30886509
    num_examples: 4257
  download_size: 11274837
  dataset_size: 30886509
- config_name: 20230901.gor
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6131050
    num_examples: 14572
  download_size: 2047896
  dataset_size: 6131050
- config_name: 20230901.got
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1533270
    num_examples: 1012
  download_size: 633392
  dataset_size: 1533270
- config_name: 20230901.gu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 121284600
    num_examples: 30413
  download_size: 39504567
  dataset_size: 121284600
- config_name: 20230901.guc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 939870
    num_examples: 618
  download_size: 556772
  dataset_size: 939870
- config_name: 20230901.gur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1620565
    num_examples: 1119
  download_size: 820347
  dataset_size: 1620565
- config_name: 20230901.guw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1900240
    num_examples: 1303
  download_size: 1030888
  dataset_size: 1900240
- config_name: 20230901.gv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6030196
    num_examples: 6009
  download_size: 3195985
  dataset_size: 6030196
- config_name: 20230901.ha
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 73654886
    num_examples: 33752
  download_size: 40714314
  dataset_size: 73654886
- config_name: 20230901.hak
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4509695
    num_examples: 10238
  download_size: 1879146
  dataset_size: 4509695
- config_name: 20230901.haw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1672431
    num_examples: 2615
  download_size: 694045
  dataset_size: 1672431
- config_name: 20230901.he
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1927823110
    num_examples: 330733
  download_size: 974031783
  dataset_size: 1927823110
- config_name: 20230901.hi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 667221249
    num_examples: 162285
  download_size: 235641052
  dataset_size: 667221249
- config_name: 20230901.hif
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5676100
    num_examples: 10981
  download_size: 2709810
  dataset_size: 5676100
- config_name: 20230901.ho
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3450
    num_examples: 3
  download_size: 7714
  dataset_size: 3450
- config_name: 20230901.hr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 441122356
    num_examples: 201819
  download_size: 276842760
  dataset_size: 441122356
- config_name: 20230901.hsb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 15657332
    num_examples: 13949
  download_size: 7427955
  dataset_size: 15657332
- config_name: 20230901.ht
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 54641623
    num_examples: 70002
  download_size: 21699003
  dataset_size: 54641623
- config_name: 20230901.hu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1505652559
    num_examples: 529609
  download_size: 913575039
  dataset_size: 1505652559
- config_name: 20230901.hy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1167174995
    num_examples: 301853
  download_size: 488665605
  dataset_size: 1167174995
- config_name: 20230901.hyw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 59286603
    num_examples: 11644
  download_size: 27305593
  dataset_size: 59286603
- config_name: 20230901.ia
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16319168
    num_examples: 28081
  download_size: 8200366
  dataset_size: 16319168
- config_name: 20230901.id
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1110116852
    num_examples: 657990
  download_size: 587862344
  dataset_size: 1110116852
- config_name: 20230901.ie
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6658278
    num_examples: 11811
  download_size: 2978290
  dataset_size: 6658278
- config_name: 20230901.ig
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 55435770
    num_examples: 19892
  download_size: 28977840
  dataset_size: 55435770
- config_name: 20230901.ii
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8921
    num_examples: 14
  download_size: 14936
  dataset_size: 8921
- config_name: 20230901.ik
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 192007
    num_examples: 831
  download_size: 110667
  dataset_size: 192007
- config_name: 20230901.ilo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16853115
    num_examples: 15369
  download_size: 7345494
  dataset_size: 16853115
- config_name: 20230901.inh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2722201
    num_examples: 2121
  download_size: 1273603
  dataset_size: 2722201
- config_name: 20230901.io
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 37616691
    num_examples: 38645
  download_size: 16826496
  dataset_size: 37616691
- config_name: 20230901.is
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 87138239
    num_examples: 57147
  download_size: 51826151
  dataset_size: 87138239
- config_name: 20230901.it
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4879369360
    num_examples: 1824508
  download_size: 2957576589
  dataset_size: 4879369360
- config_name: 20230901.iu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 289114
    num_examples: 561
  download_size: 136067
  dataset_size: 289114
- config_name: 20230901.ja
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6988535462
    num_examples: 1383531
  download_size: 3966219907
  dataset_size: 6988535462
- config_name: 20230901.jam
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1142809
    num_examples: 1775
  download_size: 702478
  dataset_size: 1142809
- config_name: 20230901.jbo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2522674
    num_examples: 1391
  download_size: 888919
  dataset_size: 2522674
- config_name: 20230901.jv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 71017946
    num_examples: 73150
  download_size: 36394809
  dataset_size: 71017946
- config_name: 20230901.ka
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 696934958
    num_examples: 169131
  download_size: 238964498
  dataset_size: 696934958
- config_name: 20230901.kaa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4754449
    num_examples: 3856
  download_size: 2682618
  dataset_size: 4754449
- config_name: 20230901.kab
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4388232
    num_examples: 5825
  download_size: 2578056
  dataset_size: 4388232
- config_name: 20230901.kbd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3040422
    num_examples: 1656
  download_size: 1319464
  dataset_size: 3040422
- config_name: 20230901.kbp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3579071
    num_examples: 1922
  download_size: 1795549
  dataset_size: 3579071
- config_name: 20230901.kcg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 728303
    num_examples: 913
  download_size: 382843
  dataset_size: 728303
- config_name: 20230901.kg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 386320
    num_examples: 1325
  download_size: 206106
  dataset_size: 386320
- config_name: 20230901.ki
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 731003
    num_examples: 1647
  download_size: 408805
  dataset_size: 731003
- config_name: 20230901.kj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5190
    num_examples: 5
  download_size: 10453
  dataset_size: 5190
- config_name: 20230901.kk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 494357868
    num_examples: 237902
  download_size: 179217175
  dataset_size: 494357868
- config_name: 20230901.kl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 313121
    num_examples: 298
  download_size: 193507
  dataset_size: 313121
- config_name: 20230901.km
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 102576754
    num_examples: 11874
  download_size: 35281246
  dataset_size: 102576754
- config_name: 20230901.kn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 399521127
    num_examples: 31136
  download_size: 145847507
  dataset_size: 399521127
- config_name: 20230901.ko
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1401002436
    num_examples: 643723
  download_size: 792232087
  dataset_size: 1401002436
- config_name: 20230901.koi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5102564
    num_examples: 3504
  download_size: 1887860
  dataset_size: 5102564
- config_name: 20230901.krc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4586443
    num_examples: 2098
  download_size: 2015581
  dataset_size: 4586443
- config_name: 20230901.ks
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2828813
    num_examples: 4278
  download_size: 1074931
  dataset_size: 2828813
- config_name: 20230901.ksh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3115805
    num_examples: 2944
  download_size: 2007139
  dataset_size: 3115805
- config_name: 20230901.ku
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 43200623
    num_examples: 59822
  download_size: 22481749
  dataset_size: 43200623
- config_name: 20230901.kv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9244682
    num_examples: 5603
  download_size: 3687481
  dataset_size: 9244682
- config_name: 20230901.kw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4675299
    num_examples: 7088
  download_size: 2703089
  dataset_size: 4675299
- config_name: 20230901.ky
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 168378862
    num_examples: 80665
  download_size: 64423485
  dataset_size: 168378862
- config_name: 20230901.la
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 140689294
    num_examples: 138140
  download_size: 76340691
  dataset_size: 140689294
- config_name: 20230901.lad
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4878588
    num_examples: 3648
  download_size: 2737222
  dataset_size: 4878588
- config_name: 20230901.lb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 88394374
    num_examples: 62131
  download_size: 50250905
  dataset_size: 88394374
- config_name: 20230901.lbe
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 744689
    num_examples: 1277
  download_size: 304111
  dataset_size: 744689
- config_name: 20230901.lez
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9793873
    num_examples: 4264
  download_size: 3852020
  dataset_size: 9793873
- config_name: 20230901.lfn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8912633
    num_examples: 4819
  download_size: 5206921
  dataset_size: 8912633
- config_name: 20230901.lg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6887606
    num_examples: 4041
  download_size: 3703329
  dataset_size: 6887606
- config_name: 20230901.li
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 29373978
    num_examples: 14526
  download_size: 17641752
  dataset_size: 29373978
- config_name: 20230901.lij
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11336209
    num_examples: 11184
  download_size: 6176932
  dataset_size: 11336209
- config_name: 20230901.lld
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 50110703
    num_examples: 180580
  download_size: 13839995
  dataset_size: 50110703
- config_name: 20230901.lmo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 43217251
    num_examples: 72899
  download_size: 19041052
  dataset_size: 43217251
- config_name: 20230901.ln
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2024359
    num_examples: 3531
  download_size: 1116032
  dataset_size: 2024359
- config_name: 20230901.lo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 15117598
    num_examples: 4995
  download_size: 5527479
  dataset_size: 15117598
- config_name: 20230901.lrc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 144
    num_examples: 1
  download_size: 2723
  dataset_size: 144
- config_name: 20230901.lt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 334697442
    num_examples: 210202
  download_size: 193837594
  dataset_size: 334697442
- config_name: 20230901.ltg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 915321
    num_examples: 1070
  download_size: 530333
  dataset_size: 915321
- config_name: 20230901.lv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 224476781
    num_examples: 122266
  download_size: 128157342
  dataset_size: 224476781
- config_name: 20230901.mad
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1504064
    num_examples: 1160
  download_size: 856724
  dataset_size: 1504064
- config_name: 20230901.mai
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21426268
    num_examples: 14673
  download_size: 6117668
  dataset_size: 21426268
- config_name: 20230901.map-bms
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5413521
    num_examples: 13574
  download_size: 2427039
  dataset_size: 5413521
- config_name: 20230901.mdf
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4558408
    num_examples: 4073
  download_size: 1688901
  dataset_size: 4558408
- config_name: 20230901.mg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 72920973
    num_examples: 96060
  download_size: 21675187
  dataset_size: 72920973
- config_name: 20230901.mh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11524
    num_examples: 8
  download_size: 16877
  dataset_size: 11524
- config_name: 20230901.mhr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19188080
    num_examples: 11246
  download_size: 6867184
  dataset_size: 19188080
- config_name: 20230901.mi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4159228
    num_examples: 7898
  download_size: 1039215
  dataset_size: 4159228
- config_name: 20230901.min
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 118651753
    num_examples: 227024
  download_size: 25511300
  dataset_size: 118651753
- config_name: 20230901.mk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 640596981
    num_examples: 138453
  download_size: 266334099
  dataset_size: 640596981
- config_name: 20230901.ml
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 490833742
    num_examples: 85451
  download_size: 181789443
  dataset_size: 490833742
- config_name: 20230901.mn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 90537032
    num_examples: 23797
  download_size: 40809884
  dataset_size: 90537032
- config_name: 20230901.mni
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9818372
    num_examples: 10892
  download_size: 2207828
  dataset_size: 9818372
- config_name: 20230901.mnw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 46788079
    num_examples: 3249
  download_size: 13588244
  dataset_size: 46788079
- config_name: 20230901.mr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 260342611
    num_examples: 93653
  download_size: 81397471
  dataset_size: 260342611
- config_name: 20230901.mrj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8731508
    num_examples: 10542
  download_size: 3279598
  dataset_size: 8731508
- config_name: 20230901.ms
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 419678289
    num_examples: 367463
  download_size: 211505058
  dataset_size: 419678289
- config_name: 20230901.mt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 30536771
    num_examples: 5598
  download_size: 17850471
  dataset_size: 30536771
- config_name: 20230901.mus
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 922
    num_examples: 2
  download_size: 5286
  dataset_size: 922
- config_name: 20230901.mwl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19321295
    num_examples: 4485
  download_size: 11488668
  dataset_size: 19321295
- config_name: 20230901.my
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 312482214
    num_examples: 109166
  download_size: 84914025
  dataset_size: 312482214
- config_name: 20230901.myv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11131103
    num_examples: 7947
  download_size: 4586300
  dataset_size: 11131103
- config_name: 20230901.mzn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 15830260
    num_examples: 17696
  download_size: 5258917
  dataset_size: 15830260
- config_name: 20230901.nah
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2494573
    num_examples: 6180
  download_size: 1188515
  dataset_size: 2494573
- config_name: 20230901.nap
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6377175
    num_examples: 14868
  download_size: 3176787
  dataset_size: 6377175
- config_name: 20230901.nds
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 92854034
    num_examples: 84258
  download_size: 48004103
  dataset_size: 92854034
- config_name: 20230901.nds-nl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13560241
    num_examples: 7707
  download_size: 8287716
  dataset_size: 13560241
- config_name: 20230901.ne
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 106930147
    num_examples: 32423
  download_size: 36867790
  dataset_size: 106930147
- config_name: 20230901.new
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 159078463
    num_examples: 73003
  download_size: 20468180
  dataset_size: 159078463
- config_name: 20230901.ng
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 68090
    num_examples: 21
  download_size: 52355
  dataset_size: 68090
- config_name: 20230901.nia
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1909528
    num_examples: 1651
  download_size: 970289
  dataset_size: 1909528
- config_name: 20230901.nl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2631597985
    num_examples: 2130944
  download_size: 1467451759
  dataset_size: 2631597985
- config_name: 20230901.nn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 236262183
    num_examples: 166642
  download_size: 134021748
  dataset_size: 236262183
- config_name: 20230901.no
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1027035487
    num_examples: 615107
  download_size: 599774543
  dataset_size: 1027035487
- config_name: 20230901.nov
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 917413
    num_examples: 1636
  download_size: 469305
  dataset_size: 917413
- config_name: 20230901.nqo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8219209
    num_examples: 1571
  download_size: 3478458
  dataset_size: 8219209
- config_name: 20230901.nrm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3215096
    num_examples: 4899
  download_size: 1505717
  dataset_size: 3215096
- config_name: 20230901.nso
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2789807
    num_examples: 8643
  download_size: 932635
  dataset_size: 2789807
- config_name: 20230901.nv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16886983
    num_examples: 22324
  download_size: 3288156
  dataset_size: 16886983
- config_name: 20230901.ny
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1695102
    num_examples: 1133
  download_size: 938716
  dataset_size: 1695102
- config_name: 20230901.oc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 119055715
    num_examples: 89270
  download_size: 63403412
  dataset_size: 119055715
- config_name: 20230901.olo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3152274
    num_examples: 4595
  download_size: 1716616
  dataset_size: 3152274
- config_name: 20230901.om
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3430032
    num_examples: 1911
  download_size: 1900253
  dataset_size: 3430032
- config_name: 20230901.or
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 72723705
    num_examples: 17166
  download_size: 25879025
  dataset_size: 72723705
- config_name: 20230901.os
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13112794
    num_examples: 17446
  download_size: 5554157
  dataset_size: 13112794
- config_name: 20230901.pa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 211148791
    num_examples: 51013
  download_size: 80668229
  dataset_size: 211148791
- config_name: 20230901.pag
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1384685
    num_examples: 2662
  download_size: 451639
  dataset_size: 1384685
- config_name: 20230901.pam
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8237319
    num_examples: 8951
  download_size: 4235968
  dataset_size: 8237319
- config_name: 20230901.pap
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4105109
    num_examples: 3427
  download_size: 2353692
  dataset_size: 4105109
- config_name: 20230901.pcd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5680386
    num_examples: 5692
  download_size: 3127716
  dataset_size: 5680386
- config_name: 20230901.pcm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1807444
    num_examples: 1069
  download_size: 1111719
  dataset_size: 1807444
- config_name: 20230901.pdc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1223268
    num_examples: 2182
  download_size: 696649
  dataset_size: 1223268
- config_name: 20230901.pfl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3688761
    num_examples: 2759
  download_size: 1963616
  dataset_size: 3688761
- config_name: 20230901.pi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1133972
    num_examples: 3056
  download_size: 196617
  dataset_size: 1133972
- config_name: 20230901.pih
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 381602
    num_examples: 933
  download_size: 238696
  dataset_size: 381602
- config_name: 20230901.pl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2929578273
    num_examples: 1579326
  download_size: 1803033674
  dataset_size: 2929578273
- config_name: 20230901.pms
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 34318527
    num_examples: 67935
  download_size: 11997737
  dataset_size: 34318527
- config_name: 20230901.pnb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 303876889
    num_examples: 72240
  download_size: 133093182
  dataset_size: 303876889
- config_name: 20230901.pnt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 630714
    num_examples: 533
  download_size: 275657
  dataset_size: 630714
- config_name: 20230901.ps
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 109664877
    num_examples: 20166
  download_size: 51380951
  dataset_size: 109664877
- config_name: 20230901.pt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2731435653
    num_examples: 1107946
  download_size: 1593477871
  dataset_size: 2731435653
- config_name: 20230901.pwn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 792234
    num_examples: 394
  download_size: 433617
  dataset_size: 792234
- config_name: 20230901.qu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16754330
    num_examples: 24096
  download_size: 7651901
  dataset_size: 16754330
- config_name: 20230901.rm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 18052223
    num_examples: 3821
  download_size: 10475947
  dataset_size: 18052223
- config_name: 20230901.rmy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 555208
    num_examples: 969
  download_size: 324565
  dataset_size: 555208
- config_name: 20230901.rn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 522604
    num_examples: 808
  download_size: 295315
  dataset_size: 522604
- config_name: 20230901.ro
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 842490285
    num_examples: 441538
  download_size: 471249050
  dataset_size: 842490285
- config_name: 20230901.roa-rup
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1691177
    num_examples: 1409
  download_size: 953023
  dataset_size: 1691177
- config_name: 20230901.roa-tara
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7435543
    num_examples: 9341
  download_size: 3982748
  dataset_size: 7435543
- config_name: 20230901.ru
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10213314874
    num_examples: 1935562
  download_size: 4935575161
  dataset_size: 10213314874
- config_name: 20230901.rue
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13110982
    num_examples: 8749
  download_size: 6335689
  dataset_size: 13110982
- config_name: 20230901.rw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11946518
    num_examples: 8044
  download_size: 6640582
  dataset_size: 11946518
- config_name: 20230901.sa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 69665685
    num_examples: 12143
  download_size: 23750145
  dataset_size: 69665685
- config_name: 20230901.sah
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 47816835
    num_examples: 16867
  download_size: 21350955
  dataset_size: 47816835
- config_name: 20230901.sat
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 40858282
    num_examples: 9029
  download_size: 13950418
  dataset_size: 40858282
- config_name: 20230901.sc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12732368
    num_examples: 7559
  download_size: 7682010
  dataset_size: 12732368
- config_name: 20230901.scn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 17667128
    num_examples: 26519
  download_size: 10212874
  dataset_size: 17667128
- config_name: 20230901.sco
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 43780491
    num_examples: 36169
  download_size: 24761453
  dataset_size: 43780491
- config_name: 20230901.sd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36726435
    num_examples: 16894
  download_size: 17439666
  dataset_size: 36726435
- config_name: 20230901.se
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3600162
    num_examples: 8042
  download_size: 1814812
  dataset_size: 3600162
- config_name: 20230901.sg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 130365
    num_examples: 553
  download_size: 65750
  dataset_size: 130365
- config_name: 20230901.sh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 569747500
    num_examples: 458212
  download_size: 270404350
  dataset_size: 569747500
- config_name: 20230901.shi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2348743
    num_examples: 1771
  download_size: 1347026
  dataset_size: 2348743
- config_name: 20230901.shn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 33479127
    num_examples: 13878
  download_size: 8148046
  dataset_size: 33479127
- config_name: 20230901.si
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 136810596
    num_examples: 22893
  download_size: 53392258
  dataset_size: 136810596
- config_name: 20230901.simple
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 287855540
    num_examples: 238150
  download_size: 157248327
  dataset_size: 287855540
- config_name: 20230901.sk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 414483614
    num_examples: 241614
  download_size: 240700453
  dataset_size: 414483614
- config_name: 20230901.skr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 22524450
    num_examples: 5768
  download_size: 9854778
  dataset_size: 22524450
- config_name: 20230901.sl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 451888560
    num_examples: 182364
  download_size: 268258798
  dataset_size: 451888560
- config_name: 20230901.sm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 904339
    num_examples: 1149
  download_size: 493408
  dataset_size: 904339
- config_name: 20230901.smn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5673858
    num_examples: 5333
  download_size: 2767537
  dataset_size: 5673858
- config_name: 20230901.sn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9587086
    num_examples: 11354
  download_size: 4889856
  dataset_size: 9587086
- config_name: 20230901.so
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13594918
    num_examples: 9003
  download_size: 7886560
  dataset_size: 13594918
- config_name: 20230901.sq
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 204838795
    num_examples: 103850
  download_size: 114648801
  dataset_size: 204838795
- config_name: 20230901.sr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1709332753
    num_examples: 673516
  download_size: 704099906
  dataset_size: 1709332753
- config_name: 20230901.srn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 649208
    num_examples: 1219
  download_size: 215087
  dataset_size: 649208
- config_name: 20230901.ss
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1024219
    num_examples: 890
  download_size: 574998
  dataset_size: 1024219
- config_name: 20230901.st
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 956079
    num_examples: 1094
  download_size: 523485
  dataset_size: 956079
- config_name: 20230901.stq
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4934155
    num_examples: 4132
  download_size: 2880185
  dataset_size: 4934155
- config_name: 20230901.su
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 48039769
    num_examples: 61557
  download_size: 19764523
  dataset_size: 48039769
- config_name: 20230901.sv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2146681766
    num_examples: 2570535
  download_size: 1009875904
  dataset_size: 2146681766
- config_name: 20230901.sw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 72884231
    num_examples: 78444
  download_size: 35798700
  dataset_size: 72884231
- config_name: 20230901.szl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21412618
    num_examples: 56961
  download_size: 7330797
  dataset_size: 21412618
- config_name: 20230901.szy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10793237
    num_examples: 4794
  download_size: 5811192
  dataset_size: 10793237
- config_name: 20230901.ta
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 801530157
    num_examples: 158664
  download_size: 262319221
  dataset_size: 801530157
- config_name: 20230901.tay
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2909279
    num_examples: 2715
  download_size: 1203598
  dataset_size: 2909279
- config_name: 20230901.tcy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12142146
    num_examples: 2195
  download_size: 4589253
  dataset_size: 12142146
- config_name: 20230901.te
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 719651788
    num_examples: 85840
  download_size: 211297920
  dataset_size: 719651788
- config_name: 20230901.tet
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1464393
    num_examples: 1465
  download_size: 743636
  dataset_size: 1464393
- config_name: 20230901.tg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 147555847
    num_examples: 110263
  download_size: 49551755
  dataset_size: 147555847
- config_name: 20230901.th
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1002621820
    num_examples: 158289
  download_size: 371401101
  dataset_size: 1002621820
- config_name: 20230901.ti
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 639136
    num_examples: 430
  download_size: 317759
  dataset_size: 639136
- config_name: 20230901.tk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13169481
    num_examples: 7898
  download_size: 7284367
  dataset_size: 13169481
- config_name: 20230901.tl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 84784414
    num_examples: 45155
  download_size: 45203377
  dataset_size: 84784414
- config_name: 20230901.tn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3561901
    num_examples: 1160
  download_size: 1245027
  dataset_size: 3561901
- config_name: 20230901.to
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1082372
    num_examples: 1866
  download_size: 515293
  dataset_size: 1082372
- config_name: 20230901.tpi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 457865
    num_examples: 1396
  download_size: 231303
  dataset_size: 457865
- config_name: 20230901.tr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 984939694
    num_examples: 530830
  download_size: 554907604
  dataset_size: 984939694
- config_name: 20230901.trv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4906787
    num_examples: 1835
  download_size: 2654525
  dataset_size: 4906787
- config_name: 20230901.ts
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 845256
    num_examples: 778
  download_size: 454559
  dataset_size: 845256
- config_name: 20230901.tt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 680656530
    num_examples: 501002
  download_size: 129123758
  dataset_size: 680656530
- config_name: 20230901.tum
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13199654
    num_examples: 18591
  download_size: 5352424
  dataset_size: 13199654
- config_name: 20230901.tw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7386605
    num_examples: 3717
  download_size: 3815538
  dataset_size: 7386605
- config_name: 20230901.ty
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 333733
    num_examples: 1355
  download_size: 149306
  dataset_size: 333733
- config_name: 20230901.tyv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14319641
    num_examples: 3481
  download_size: 6513101
  dataset_size: 14319641
- config_name: 20230901.udm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6975919
    num_examples: 5665
  download_size: 2952228
  dataset_size: 6975919
- config_name: 20230901.ug
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 42219904
    num_examples: 8621
  download_size: 17716007
  dataset_size: 42219904
- config_name: 20230901.uk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4910916097
    num_examples: 1285004
  download_size: 2303106335
  dataset_size: 4910916097
- config_name: 20230901.ur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 402322741
    num_examples: 197343
  download_size: 164074548
  dataset_size: 402322741
- config_name: 20230901.uz
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 385386661
    num_examples: 242726
  download_size: 203362895
  dataset_size: 385386661
- config_name: 20230901.ve
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 349857
    num_examples: 840
  download_size: 161562
  dataset_size: 349857
- config_name: 20230901.vec
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 37883286
    num_examples: 69250
  download_size: 16164035
  dataset_size: 37883286
- config_name: 20230901.vep
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11487509
    num_examples: 6918
  download_size: 6327017
  dataset_size: 11487509
- config_name: 20230901.vi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1606980713
    num_examples: 1287263
  download_size: 742700712
  dataset_size: 1606980713
- config_name: 20230901.vls
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11310015
    num_examples: 7839
  download_size: 6960289
  dataset_size: 11310015
- config_name: 20230901.vo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19274897
    num_examples: 34504
  download_size: 6491359
  dataset_size: 19274897
- config_name: 20230901.wa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12140372
    num_examples: 11955
  download_size: 7231141
  dataset_size: 12140372
- config_name: 20230901.war
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 467623925
    num_examples: 1266345
  download_size: 109503863
  dataset_size: 467623925
- config_name: 20230901.wo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3498562
    num_examples: 1718
  download_size: 2077375
  dataset_size: 3498562
- config_name: 20230901.wuu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 25005942
    num_examples: 42969
  download_size: 15994961
  dataset_size: 25005942
- config_name: 20230901.xal
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1390063
    num_examples: 2290
  download_size: 507117
  dataset_size: 1390063
- config_name: 20230901.xh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2415590
    num_examples: 1667
  download_size: 1503917
  dataset_size: 2415590
- config_name: 20230901.xmf
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 37262425
    num_examples: 17949
  download_size: 12771047
  dataset_size: 37262425
- config_name: 20230901.yi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36150608
    num_examples: 15329
  download_size: 16208341
  dataset_size: 36150608
- config_name: 20230901.yo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 18460117
    num_examples: 33495
  download_size: 8504564
  dataset_size: 18460117
- config_name: 20230901.za
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1359106
    num_examples: 2971
  download_size: 662982
  dataset_size: 1359106
- config_name: 20230901.zea
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5106625
    num_examples: 5834
  download_size: 2567716
  dataset_size: 5106625
- config_name: 20230901.zh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2766648619
    num_examples: 1375017
  download_size: 1748154636
  dataset_size: 2766648619
- config_name: 20230901.zh-classical
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14819164
    num_examples: 12615
  download_size: 10031693
  dataset_size: 14819164
- config_name: 20230901.zh-min-nan
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 159385896
    num_examples: 432644
  download_size: 37476665
  dataset_size: 159385896
- config_name: 20230901.zh-yue
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 108979942
    num_examples: 133155
  download_size: 64318527
  dataset_size: 108979942
- config_name: 20230901.zu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6925330
    num_examples: 11486
  download_size: 3690925
  dataset_size: 6925330
- config_name: 20230601.et
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 431680309
    num_examples: 236848
  download_size: 262989758
  dataset_size: 431680309
---

# Wikipedia

This Wikipedia dataset contains all available languages for recent dumps. It is
a refresh of the [20220301 wikipedia](https://hf.co/datasets/wikipedia) from
Huggingface, so it has the same license and dataset card details. The benefits
of this dataset are:

- more recent dumps (see table below)
- a few additional languages
- all available languages are preprocessed (including the largests: `en` and
  `ceb`)

| version | dump     | # available languages               | closed & dump                                   | closed & no dump  |
| -----   | ----     | -----                               | ------                                          | ---               |
| `1.0.0` | 20230601 | 328                                 | 9: ak (soon), cho, ho, ii, kj, lrc, mh, mus, ng | 4: aa, hz, kr, na |
| `1.1.0` | 20230601 | 329 (+et ~[az,ceb,ch,hr,ii,lrc,ta]) | 9: ak (soon), cho, ho, ii, kj, lrc, mh, mus, ng | 4: aa, hz, kr, na |
| `1.2.0` | 20230901 | idem                                | 9: ak , cho, ho, ii, kj, lrc, mh, mus, ng       | 4: aa, hz, kr, na |

Source: [List of Wikimedia
Languages](https://en.wikipedia.org/wiki/List_of_Wikipedias). A few (9)
Wikimedias are closed, meaning they won't have new pages, but the dumps are
still available. In addition, very few (4) Wikimedias are closed and don't
have dumps anymore.

## Release Notes

`1.2.0`

- **chore**: Update to 20230901

`1.1.0`

- **feat**: Add missing estonian (my bad), thanks Chris Ha
- **fix**: update category lists for az, ceb, ch, hr, ii, lrc, ta, which means
  they were all processed again.

`1.0.0`

- **chore**: File layout is now `data/{dump}/{lang}/{info.json,*.parquet}`.
  Sorry for the radical update, probably won't happen again.
- **chore**: Parquet files are now sharded (size < 200 MB), allowing parallel
  downloads and processing.
- **fix**: All languages were all processed again because of a bug in the media
  and category names, leading to some links not being extracted.
- **feat**: Add `en` and `ceb` which were too big for my Beam DirectRunner at
  the time.

## Usage

```python
from datasets import load_dataset

wikipedia_es = load_dataset("graelo/wikipedia", "20230601.es")
```

---

## Build instructions

Developer only. This dataset was preprocessed with a Beam DirectRunner as
follows.

### 1. Determine the date of the dump you are interested in

Choose one wikipedia dump, for instance <https://dumps.wikimedia.org/cewiki/>
and identify the date.

### 2. [Optional] Get a refreshed list of languages

This is optional because it not very likely that a new language will have
suddenly appeared since the last version _and_ have a significant dataset.

Navigate to <https://en.wikipedia.org/wiki/List_of_Wikipedias> and copy the
languages column from the "Detailed list" table (near the end of the page).

Copy that content in the form of a Python list into `lang_def.py` (at the top
of the repo) under a new date.

### 3. [Optional] Create Media and Category aliases

In order to properly extract links to images and media in all languages, we
must refresh the two corresponding files. To do so, from the root of the repo,
run

```sh
python -m prep.create_aliases
```

This will create or update these two files at the root of the repo:

- `media_aliases.py`
- `category_aliases.py`

These files are used in the final step

### 4. Build and prepare the datasets into sharded parquet files

Running this script downloads the wikipedia dumps for each language in
`lang_def.py` and shards each language dataset into the appropriate number of
shards (max size ~ 250MB).

```sh
python -m prep.build --date 20230601
```

There are other options:

```text
$ python -m prep.build --help
usage: Wikipedia Builder [-h] [--date DATE] [--language [LANG ...]] [--cache-dir DIR] [--mirror MIRROR]

Prepares the Wikipedia dataset for each language

optional arguments:
  -h, --help             show this help message and exit
  --date DATE            Wikipedia dump date (e.g. 20230601)
  --language [LANG ...]  Language code (e.g. en). If missing, all languages are processed
  --cache-dir DIR        Cache directory for 🤗 Datasets
  --mirror MIRROR        Mirror URL
```

For instance, for faster downloads of the dumps, use the mirror option:

```sh
python -m prep.build \
    --date 20230601 \
    --language bs \
    --mirror https://mirror.accum.se/mirror/wikimedia.org/dumps/
```

It will download the dumps at around 60MB/s instead of the capped speed
(~4MB/s) from <https://dumps.wikimedia.org>. The script will skip existing
directories, allowing you to run the script in several passes.

Notes:

- These instructions build upon the build process of the
  [Wikipedia](https://huggingface.co/datasets/wikipedia) 🤗 Dataset. HF did a
  fantastic job, I just pushed it a bit further.
- Be aware that not all mirrors contain all dumps. For instance mirror.accum.se
  does not contain dumps for languages such as be-x-old or cbk-zam. My own
  solution is to run a first pass using the aforementioned mirror, and a second
  pass with the official `https://dumps.wikimedia.org` site (omitting the
  `--mirror` parameter).
