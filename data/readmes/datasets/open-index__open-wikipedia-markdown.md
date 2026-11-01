---
language:
  - bh
  - ho
  - kge
  - mwl
  - tcy
  - za
  - zea
  - fa
  - no
  - tw
  - mi
  - pdc
  - rm
  - bg
  - knc
  - zu
  - am
  - bar
  - bxr
  - fat
  - hy
  - it
  - mk
  - nso
  - ak
  - jv
  - kw
  - mdf
  - pag
  - rw
  - ve
  - blk
  - kn
  - sh
  - ch
  - crh
  - si
  - ur
  - wuu
  - cdo
  - cu
  - iu
  - ky
  - or
  - pap
  - ba
  - dty
  - haw
  - tet
  - ts
  - arc
  - bdr
  - be
  - la
  - mhr
  - new
  - pwn
  - sw
  - cs
  - fo
  - gl
  - gpe
  - hr
  - my
  - ro
  - frp
  - pcm
  - tly
  - tum
  - ceb
  - dtp
  - tn
  - bjn
  - bpy
  - ce
  - ja
  - mad
  - ms
  - ace
  - arz
  - diq
  - kg
  - mg
  - nv
  - rue
  - stq
  - ty
  - as
  - fy
  - nah
  - nn
  - nrm
  - sco
  - skr
  - tt
  - ab
  - alt
  - dga
  - en
  - ik
  - sg
  - vo
  - co
  - lg
  - pa
  - chr
  - mus
  - ng
  - vi
  - lv
  - awa
  - cy
  - ht
  - ki
  - nl
  - st
  - syl
  - bn
  - dz
  - kaa
  - krc
  - ln
  - mrj
  - tg
  - zh
  - als
  - az
  - bcl
  - ny
  - tpi
  - ann
  - avk
  - kk
  - ks
  - lad
  - mt
  - sn
  - uk
  - dsb
  - es
  - guw
  - ku
  - olo
  - uz
  - bi
  - gan
  - ha
  - sr
  - av
  - et
  - tyv
  - bs
  - dag
  - gom
  - hif
  - mn
  - nds
  - ug
  - lez
  - om
  - wa
  - zgh
  - btm
  - io
  - rmy
  - pam
  - rn
  - te
  - tr
  - vec
  - azb
  - is
  - kus
  - mni
  - pms
  - ss
  - ban
  - dv
  - el
  - kcg
  - kv
  - srn
  - vep
  - fon
  - kab
  - ksh
  - lij
  - ml
  - ps
  - pt
  - sl
  - gur
  - nap
  - nia
  - tok
  - yo
  - bm
  - csb
  - fr
  - ie
  - mzn
  - sah
  - sd
  - shn
  - cv
  - de
  - hi
  - nov
  - trv
  - vls
  - ady
  - gd
  - inh
  - jbo
  - koi
  - os
  - sq
  - ast
  - lt
  - sk
  - so
  - tay
  - frr
  - ia
  - mh
  - mnw
  - nr
  - yi
  - anp
  - fur
  - ka
  - mos
  - sv
  - wo
  - bew
  - oc
  - udm
  - kj
  - km
  - ru
  - chy
  - cr
  - mr
  - qu
  - rki
  - eo
  - glk
  - hu
  - ig
  - sat
  - sc
  - se
  - cho
  - gcr
  - smn
  - to
  - war
  - ary
  - hak
  - ltg
  - pcd
  - igl
  - kl
  - ilo
  - mai
  - pnb
  - sa
  - tig
  - pnt
  - ang
  - lld
  - ppl
  - szy
  - ne
  - tk
  - myv
  - bbc
  - ext
  - kaj
  - ti
  - ami
  - da
  - hsb
  - kbd
  - pl
  - rsk
  - tl
  - an
  - kbp
  - lbe
  - pfl
  - got
  - guc
  - gv
  - ta
  - xh
  - gu
  - kai
  - nqo
  - su
  - szl
  - ar
  - eml
  - pi
  - scn
  - shi
  - sm
  - bo
  - li
  - lo
  - min
  - th
  - atj
  - ay
  - bug
  - ca
  - ckb
  - eu
  - fi
  - hyw
  - ee
  - gor
  - he
  - id
  - ii
  - jam
  - lmo
  - lb
  - br
  - din
  - ff
  - ga
  - iba
  - ko
  - lfn
  - tdd
  - af
  - fj
  - gag
  - gn
  - nup
  - pih
  - xal
  - xmf
  - aa
  - hz
  - kr
  - lrc
  - na
language_bcp47:
  - nds-nl
  - cbk-zam
  - roa-tara
  - zh-yue
  - roa-rup
  - zh-classical
  - fiu-vro
  - map-bms
  - be-x-old
  - zh-min-nan
  - bat-smg
license: cc-by-sa-4.0
task_categories:
  - text-generation
  - feature-extraction
  - text-classification
  - question-answering
  - summarization
  - translation
pretty_name: Open Wikipedia (Markdown)
tags:
  - wikipedia
  - encyclopedia
  - knowledge
  - markdown
  - multilingual
  - wikimedia
  - open-data
size_categories:
  - 10M<n<100M
configs:
  - config_name: bh
    data_files:
      - split: train
        path: data/bh/*.parquet
  - config_name: ho
    data_files:
      - split: train
        path: data/ho/*.parquet
  - config_name: kge
    data_files:
      - split: train
        path: data/kge/*.parquet
  - config_name: mwl
    data_files:
      - split: train
        path: data/mwl/*.parquet
  - config_name: tcy
    data_files:
      - split: train
        path: data/tcy/*.parquet
  - config_name: wikifunctions
    data_files:
      - split: train
        path: data/wikifunctions/*.parquet
  - config_name: za
    data_files:
      - split: train
        path: data/za/*.parquet
  - config_name: zea
    data_files:
      - split: train
        path: data/zea/*.parquet
  - config_name: fa
    data_files:
      - split: train
        path: data/fa/*.parquet
  - config_name: no
    data_files:
      - split: train
        path: data/no/*.parquet
  - config_name: tw
    data_files:
      - split: train
        path: data/tw/*.parquet
  - config_name: mi
    data_files:
      - split: train
        path: data/mi/*.parquet
  - config_name: pdc
    data_files:
      - split: train
        path: data/pdc/*.parquet
  - config_name: rm
    data_files:
      - split: train
        path: data/rm/*.parquet
  - config_name: testcommons
    data_files:
      - split: train
        path: data/testcommons/*.parquet
  - config_name: bg
    data_files:
      - split: train
        path: data/bg/*.parquet
  - config_name: knc
    data_files:
      - split: train
        path: data/knc/*.parquet
  - config_name: zu
    data_files:
      - split: train
        path: data/zu/*.parquet
  - config_name: am
    data_files:
      - split: train
        path: data/am/*.parquet
  - config_name: bar
    data_files:
      - split: train
        path: data/bar/*.parquet
  - config_name: bxr
    data_files:
      - split: train
        path: data/bxr/*.parquet
  - config_name: fat
    data_files:
      - split: train
        path: data/fat/*.parquet
  - config_name: hy
    data_files:
      - split: train
        path: data/hy/*.parquet
  - config_name: it
    data_files:
      - split: train
        path: data/it/*.parquet
  - config_name: mk
    data_files:
      - split: train
        path: data/mk/*.parquet
  - config_name: nso
    data_files:
      - split: train
        path: data/nso/*.parquet
  - config_name: ak
    data_files:
      - split: train
        path: data/ak/*.parquet
  - config_name: jv
    data_files:
      - split: train
        path: data/jv/*.parquet
  - config_name: kw
    data_files:
      - split: train
        path: data/kw/*.parquet
  - config_name: mdf
    data_files:
      - split: train
        path: data/mdf/*.parquet
  - config_name: pag
    data_files:
      - split: train
        path: data/pag/*.parquet
  - config_name: rw
    data_files:
      - split: train
        path: data/rw/*.parquet
  - config_name: ve
    data_files:
      - split: train
        path: data/ve/*.parquet
  - config_name: blk
    data_files:
      - split: train
        path: data/blk/*.parquet
  - config_name: kn
    data_files:
      - split: train
        path: data/kn/*.parquet
  - config_name: sh
    data_files:
      - split: train
        path: data/sh/*.parquet
  - config_name: ch
    data_files:
      - split: train
        path: data/ch/*.parquet
  - config_name: crh
    data_files:
      - split: train
        path: data/crh/*.parquet
  - config_name: si
    data_files:
      - split: train
        path: data/si/*.parquet
  - config_name: testwikidata
    data_files:
      - split: train
        path: data/testwikidata/*.parquet
  - config_name: ur
    data_files:
      - split: train
        path: data/ur/*.parquet
  - config_name: wuu
    data_files:
      - split: train
        path: data/wuu/*.parquet
  - config_name: cdo
    data_files:
      - split: train
        path: data/cdo/*.parquet
  - config_name: cu
    data_files:
      - split: train
        path: data/cu/*.parquet
  - config_name: iu
    data_files:
      - split: train
        path: data/iu/*.parquet
  - config_name: ky
    data_files:
      - split: train
        path: data/ky/*.parquet
  - config_name: or
    data_files:
      - split: train
        path: data/or/*.parquet
  - config_name: pap
    data_files:
      - split: train
        path: data/pap/*.parquet
  - config_name: ba
    data_files:
      - split: train
        path: data/ba/*.parquet
  - config_name: dty
    data_files:
      - split: train
        path: data/dty/*.parquet
  - config_name: haw
    data_files:
      - split: train
        path: data/haw/*.parquet
  - config_name: tet
    data_files:
      - split: train
        path: data/tet/*.parquet
  - config_name: ts
    data_files:
      - split: train
        path: data/ts/*.parquet
  - config_name: arc
    data_files:
      - split: train
        path: data/arc/*.parquet
  - config_name: bdr
    data_files:
      - split: train
        path: data/bdr/*.parquet
  - config_name: be
    data_files:
      - split: train
        path: data/be/*.parquet
  - config_name: la
    data_files:
      - split: train
        path: data/la/*.parquet
  - config_name: mhr
    data_files:
      - split: train
        path: data/mhr/*.parquet
  - config_name: new
    data_files:
      - split: train
        path: data/new/*.parquet
  - config_name: pwn
    data_files:
      - split: train
        path: data/pwn/*.parquet
  - config_name: sw
    data_files:
      - split: train
        path: data/sw/*.parquet
  - config_name: cs
    data_files:
      - split: train
        path: data/cs/*.parquet
  - config_name: fo
    data_files:
      - split: train
        path: data/fo/*.parquet
  - config_name: gl
    data_files:
      - split: train
        path: data/gl/*.parquet
  - config_name: gpe
    data_files:
      - split: train
        path: data/gpe/*.parquet
  - config_name: hr
    data_files:
      - split: train
        path: data/hr/*.parquet
  - config_name: my
    data_files:
      - split: train
        path: data/my/*.parquet
  - config_name: nds_nl
    data_files:
      - split: train
        path: data/nds_nl/*.parquet
  - config_name: ro
    data_files:
      - split: train
        path: data/ro/*.parquet
  - config_name: frp
    data_files:
      - split: train
        path: data/frp/*.parquet
  - config_name: pcm
    data_files:
      - split: train
        path: data/pcm/*.parquet
  - config_name: tly
    data_files:
      - split: train
        path: data/tly/*.parquet
  - config_name: tum
    data_files:
      - split: train
        path: data/tum/*.parquet
  - config_name: ceb
    data_files:
      - split: train
        path: data/ceb/*.parquet
  - config_name: dtp
    data_files:
      - split: train
        path: data/dtp/*.parquet
  - config_name: tn
    data_files:
      - split: train
        path: data/tn/*.parquet
  - config_name: bjn
    data_files:
      - split: train
        path: data/bjn/*.parquet
  - config_name: bpy
    data_files:
      - split: train
        path: data/bpy/*.parquet
  - config_name: cbk_zam
    data_files:
      - split: train
        path: data/cbk_zam/*.parquet
  - config_name: ce
    data_files:
      - split: train
        path: data/ce/*.parquet
  - config_name: ja
    data_files:
      - split: train
        path: data/ja/*.parquet
  - config_name: mad
    data_files:
      - split: train
        path: data/mad/*.parquet
  - config_name: ms
    data_files:
      - split: train
        path: data/ms/*.parquet
  - config_name: simple
    data_files:
      - split: train
        path: data/simple/*.parquet
  - config_name: ace
    data_files:
      - split: train
        path: data/ace/*.parquet
  - config_name: arz
    data_files:
      - split: train
        path: data/arz/*.parquet
  - config_name: diq
    data_files:
      - split: train
        path: data/diq/*.parquet
  - config_name: kg
    data_files:
      - split: train
        path: data/kg/*.parquet
  - config_name: mg
    data_files:
      - split: train
        path: data/mg/*.parquet
  - config_name: nv
    data_files:
      - split: train
        path: data/nv/*.parquet
  - config_name: rue
    data_files:
      - split: train
        path: data/rue/*.parquet
  - config_name: vote
    data_files:
      - split: train
        path: data/vote/*.parquet
  - config_name: stq
    data_files:
      - split: train
        path: data/stq/*.parquet
  - config_name: ty
    data_files:
      - split: train
        path: data/ty/*.parquet
  - config_name: as
    data_files:
      - split: train
        path: data/as/*.parquet
  - config_name: fy
    data_files:
      - split: train
        path: data/fy/*.parquet
  - config_name: nah
    data_files:
      - split: train
        path: data/nah/*.parquet
  - config_name: nn
    data_files:
      - split: train
        path: data/nn/*.parquet
  - config_name: nrm
    data_files:
      - split: train
        path: data/nrm/*.parquet
  - config_name: sco
    data_files:
      - split: train
        path: data/sco/*.parquet
  - config_name: skr
    data_files:
      - split: train
        path: data/skr/*.parquet
  - config_name: tt
    data_files:
      - split: train
        path: data/tt/*.parquet
  - config_name: ab
    data_files:
      - split: train
        path: data/ab/*.parquet
  - config_name: alt
    data_files:
      - split: train
        path: data/alt/*.parquet
  - config_name: dga
    data_files:
      - split: train
        path: data/dga/*.parquet
  - config_name: en
    data_files:
      - split: train
        path: data/en/*.parquet
    default: true
  - config_name: ik
    data_files:
      - split: train
        path: data/ik/*.parquet
  - config_name: sg
    data_files:
      - split: train
        path: data/sg/*.parquet
  - config_name: vo
    data_files:
      - split: train
        path: data/vo/*.parquet
  - config_name: co
    data_files:
      - split: train
        path: data/co/*.parquet
  - config_name: lg
    data_files:
      - split: train
        path: data/lg/*.parquet
  - config_name: pa
    data_files:
      - split: train
        path: data/pa/*.parquet
  - config_name: chr
    data_files:
      - split: train
        path: data/chr/*.parquet
  - config_name: mus
    data_files:
      - split: train
        path: data/mus/*.parquet
  - config_name: ng
    data_files:
      - split: train
        path: data/ng/*.parquet
  - config_name: vi
    data_files:
      - split: train
        path: data/vi/*.parquet
  - config_name: lv
    data_files:
      - split: train
        path: data/lv/*.parquet
  - config_name: awa
    data_files:
      - split: train
        path: data/awa/*.parquet
  - config_name: cy
    data_files:
      - split: train
        path: data/cy/*.parquet
  - config_name: ht
    data_files:
      - split: train
        path: data/ht/*.parquet
  - config_name: ki
    data_files:
      - split: train
        path: data/ki/*.parquet
  - config_name: nl
    data_files:
      - split: train
        path: data/nl/*.parquet
  - config_name: st
    data_files:
      - split: train
        path: data/st/*.parquet
  - config_name: syl
    data_files:
      - split: train
        path: data/syl/*.parquet
  - config_name: bn
    data_files:
      - split: train
        path: data/bn/*.parquet
  - config_name: dz
    data_files:
      - split: train
        path: data/dz/*.parquet
  - config_name: kaa
    data_files:
      - split: train
        path: data/kaa/*.parquet
  - config_name: krc
    data_files:
      - split: train
        path: data/krc/*.parquet
  - config_name: ln
    data_files:
      - split: train
        path: data/ln/*.parquet
  - config_name: mrj
    data_files:
      - split: train
        path: data/mrj/*.parquet
  - config_name: tg
    data_files:
      - split: train
        path: data/tg/*.parquet
  - config_name: zh
    data_files:
      - split: train
        path: data/zh/*.parquet
  - config_name: als
    data_files:
      - split: train
        path: data/als/*.parquet
  - config_name: az
    data_files:
      - split: train
        path: data/az/*.parquet
  - config_name: bcl
    data_files:
      - split: train
        path: data/bcl/*.parquet
  - config_name: ny
    data_files:
      - split: train
        path: data/ny/*.parquet
  - config_name: tpi
    data_files:
      - split: train
        path: data/tpi/*.parquet
  - config_name: ann
    data_files:
      - split: train
        path: data/ann/*.parquet
  - config_name: avk
    data_files:
      - split: train
        path: data/avk/*.parquet
  - config_name: kk
    data_files:
      - split: train
        path: data/kk/*.parquet
  - config_name: ks
    data_files:
      - split: train
        path: data/ks/*.parquet
  - config_name: lad
    data_files:
      - split: train
        path: data/lad/*.parquet
  - config_name: mt
    data_files:
      - split: train
        path: data/mt/*.parquet
  - config_name: sn
    data_files:
      - split: train
        path: data/sn/*.parquet
  - config_name: uk
    data_files:
      - split: train
        path: data/uk/*.parquet
  - config_name: dsb
    data_files:
      - split: train
        path: data/dsb/*.parquet
  - config_name: es
    data_files:
      - split: train
        path: data/es/*.parquet
  - config_name: guw
    data_files:
      - split: train
        path: data/guw/*.parquet
  - config_name: ku
    data_files:
      - split: train
        path: data/ku/*.parquet
  - config_name: olo
    data_files:
      - split: train
        path: data/olo/*.parquet
  - config_name: uz
    data_files:
      - split: train
        path: data/uz/*.parquet
  - config_name: bi
    data_files:
      - split: train
        path: data/bi/*.parquet
  - config_name: gan
    data_files:
      - split: train
        path: data/gan/*.parquet
  - config_name: ha
    data_files:
      - split: train
        path: data/ha/*.parquet
  - config_name: sr
    data_files:
      - split: train
        path: data/sr/*.parquet
  - config_name: av
    data_files:
      - split: train
        path: data/av/*.parquet
  - config_name: et
    data_files:
      - split: train
        path: data/et/*.parquet
  - config_name: tyv
    data_files:
      - split: train
        path: data/tyv/*.parquet
  - config_name: bs
    data_files:
      - split: train
        path: data/bs/*.parquet
  - config_name: dag
    data_files:
      - split: train
        path: data/dag/*.parquet
  - config_name: gom
    data_files:
      - split: train
        path: data/gom/*.parquet
  - config_name: hif
    data_files:
      - split: train
        path: data/hif/*.parquet
  - config_name: mn
    data_files:
      - split: train
        path: data/mn/*.parquet
  - config_name: nds
    data_files:
      - split: train
        path: data/nds/*.parquet
  - config_name: ug
    data_files:
      - split: train
        path: data/ug/*.parquet
  - config_name: lez
    data_files:
      - split: train
        path: data/lez/*.parquet
  - config_name: om
    data_files:
      - split: train
        path: data/om/*.parquet
  - config_name: wa
    data_files:
      - split: train
        path: data/wa/*.parquet
  - config_name: zgh
    data_files:
      - split: train
        path: data/zgh/*.parquet
  - config_name: btm
    data_files:
      - split: train
        path: data/btm/*.parquet
  - config_name: io
    data_files:
      - split: train
        path: data/io/*.parquet
  - config_name: rmy
    data_files:
      - split: train
        path: data/rmy/*.parquet
  - config_name: roa_tara
    data_files:
      - split: train
        path: data/roa_tara/*.parquet
  - config_name: zh_yue
    data_files:
      - split: train
        path: data/zh_yue/*.parquet
  - config_name: pam
    data_files:
      - split: train
        path: data/pam/*.parquet
  - config_name: rn
    data_files:
      - split: train
        path: data/rn/*.parquet
  - config_name: te
    data_files:
      - split: train
        path: data/te/*.parquet
  - config_name: tr
    data_files:
      - split: train
        path: data/tr/*.parquet
  - config_name: vec
    data_files:
      - split: train
        path: data/vec/*.parquet
  - config_name: azb
    data_files:
      - split: train
        path: data/azb/*.parquet
  - config_name: is
    data_files:
      - split: train
        path: data/is/*.parquet
  - config_name: kus
    data_files:
      - split: train
        path: data/kus/*.parquet
  - config_name: mni
    data_files:
      - split: train
        path: data/mni/*.parquet
  - config_name: pms
    data_files:
      - split: train
        path: data/pms/*.parquet
  - config_name: ss
    data_files:
      - split: train
        path: data/ss/*.parquet
  - config_name: ban
    data_files:
      - split: train
        path: data/ban/*.parquet
  - config_name: dv
    data_files:
      - split: train
        path: data/dv/*.parquet
  - config_name: el
    data_files:
      - split: train
        path: data/el/*.parquet
  - config_name: kcg
    data_files:
      - split: train
        path: data/kcg/*.parquet
  - config_name: kv
    data_files:
      - split: train
        path: data/kv/*.parquet
  - config_name: srn
    data_files:
      - split: train
        path: data/srn/*.parquet
  - config_name: thankyou
    data_files:
      - split: train
        path: data/thankyou/*.parquet
  - config_name: vep
    data_files:
      - split: train
        path: data/vep/*.parquet
  - config_name: fon
    data_files:
      - split: train
        path: data/fon/*.parquet
  - config_name: kab
    data_files:
      - split: train
        path: data/kab/*.parquet
  - config_name: ksh
    data_files:
      - split: train
        path: data/ksh/*.parquet
  - config_name: lij
    data_files:
      - split: train
        path: data/lij/*.parquet
  - config_name: ml
    data_files:
      - split: train
        path: data/ml/*.parquet
  - config_name: ps
    data_files:
      - split: train
        path: data/ps/*.parquet
  - config_name: pt
    data_files:
      - split: train
        path: data/pt/*.parquet
  - config_name: sl
    data_files:
      - split: train
        path: data/sl/*.parquet
  - config_name: gur
    data_files:
      - split: train
        path: data/gur/*.parquet
  - config_name: nap
    data_files:
      - split: train
        path: data/nap/*.parquet
  - config_name: nia
    data_files:
      - split: train
        path: data/nia/*.parquet
  - config_name: tok
    data_files:
      - split: train
        path: data/tok/*.parquet
  - config_name: yo
    data_files:
      - split: train
        path: data/yo/*.parquet
  - config_name: bm
    data_files:
      - split: train
        path: data/bm/*.parquet
  - config_name: csb
    data_files:
      - split: train
        path: data/csb/*.parquet
  - config_name: fr
    data_files:
      - split: train
        path: data/fr/*.parquet
  - config_name: ie
    data_files:
      - split: train
        path: data/ie/*.parquet
  - config_name: mzn
    data_files:
      - split: train
        path: data/mzn/*.parquet
  - config_name: sah
    data_files:
      - split: train
        path: data/sah/*.parquet
  - config_name: sd
    data_files:
      - split: train
        path: data/sd/*.parquet
  - config_name: shn
    data_files:
      - split: train
        path: data/shn/*.parquet
  - config_name: cv
    data_files:
      - split: train
        path: data/cv/*.parquet
  - config_name: de
    data_files:
      - split: train
        path: data/de/*.parquet
  - config_name: hi
    data_files:
      - split: train
        path: data/hi/*.parquet
  - config_name: nov
    data_files:
      - split: train
        path: data/nov/*.parquet
  - config_name: trv
    data_files:
      - split: train
        path: data/trv/*.parquet
  - config_name: vls
    data_files:
      - split: train
        path: data/vls/*.parquet
  - config_name: ady
    data_files:
      - split: train
        path: data/ady/*.parquet
  - config_name: gd
    data_files:
      - split: train
        path: data/gd/*.parquet
  - config_name: inh
    data_files:
      - split: train
        path: data/inh/*.parquet
  - config_name: jbo
    data_files:
      - split: train
        path: data/jbo/*.parquet
  - config_name: koi
    data_files:
      - split: train
        path: data/koi/*.parquet
  - config_name: os
    data_files:
      - split: train
        path: data/os/*.parquet
  - config_name: roa_rup
    data_files:
      - split: train
        path: data/roa_rup/*.parquet
  - config_name: sq
    data_files:
      - split: train
        path: data/sq/*.parquet
  - config_name: ast
    data_files:
      - split: train
        path: data/ast/*.parquet
  - config_name: lt
    data_files:
      - split: train
        path: data/lt/*.parquet
  - config_name: sk
    data_files:
      - split: train
        path: data/sk/*.parquet
  - config_name: so
    data_files:
      - split: train
        path: data/so/*.parquet
  - config_name: tay
    data_files:
      - split: train
        path: data/tay/*.parquet
  - config_name: ten
    data_files:
      - split: train
        path: data/ten/*.parquet
  - config_name: frr
    data_files:
      - split: train
        path: data/frr/*.parquet
  - config_name: ia
    data_files:
      - split: train
        path: data/ia/*.parquet
  - config_name: mh
    data_files:
      - split: train
        path: data/mh/*.parquet
  - config_name: mnw
    data_files:
      - split: train
        path: data/mnw/*.parquet
  - config_name: nr
    data_files:
      - split: train
        path: data/nr/*.parquet
  - config_name: yi
    data_files:
      - split: train
        path: data/yi/*.parquet
  - config_name: anp
    data_files:
      - split: train
        path: data/anp/*.parquet
  - config_name: fur
    data_files:
      - split: train
        path: data/fur/*.parquet
  - config_name: ka
    data_files:
      - split: train
        path: data/ka/*.parquet
  - config_name: mos
    data_files:
      - split: train
        path: data/mos/*.parquet
  - config_name: sv
    data_files:
      - split: train
        path: data/sv/*.parquet
  - config_name: wo
    data_files:
      - split: train
        path: data/wo/*.parquet
  - config_name: bew
    data_files:
      - split: train
        path: data/bew/*.parquet
  - config_name: oc
    data_files:
      - split: train
        path: data/oc/*.parquet
  - config_name: udm
    data_files:
      - split: train
        path: data/udm/*.parquet
  - config_name: kj
    data_files:
      - split: train
        path: data/kj/*.parquet
  - config_name: km
    data_files:
      - split: train
        path: data/km/*.parquet
  - config_name: ru
    data_files:
      - split: train
        path: data/ru/*.parquet
  - config_name: chy
    data_files:
      - split: train
        path: data/chy/*.parquet
  - config_name: cr
    data_files:
      - split: train
        path: data/cr/*.parquet
  - config_name: mr
    data_files:
      - split: train
        path: data/mr/*.parquet
  - config_name: qu
    data_files:
      - split: train
        path: data/qu/*.parquet
  - config_name: rki
    data_files:
      - split: train
        path: data/rki/*.parquet
  - config_name: zh_classical
    data_files:
      - split: train
        path: data/zh_classical/*.parquet
  - config_name: eo
    data_files:
      - split: train
        path: data/eo/*.parquet
  - config_name: fiu_vro
    data_files:
      - split: train
        path: data/fiu_vro/*.parquet
  - config_name: glk
    data_files:
      - split: train
        path: data/glk/*.parquet
  - config_name: hu
    data_files:
      - split: train
        path: data/hu/*.parquet
  - config_name: ig
    data_files:
      - split: train
        path: data/ig/*.parquet
  - config_name: sat
    data_files:
      - split: train
        path: data/sat/*.parquet
  - config_name: sc
    data_files:
      - split: train
        path: data/sc/*.parquet
  - config_name: se
    data_files:
      - split: train
        path: data/se/*.parquet
  - config_name: cho
    data_files:
      - split: train
        path: data/cho/*.parquet
  - config_name: gcr
    data_files:
      - split: train
        path: data/gcr/*.parquet
  - config_name: smn
    data_files:
      - split: train
        path: data/smn/*.parquet
  - config_name: to
    data_files:
      - split: train
        path: data/to/*.parquet
  - config_name: war
    data_files:
      - split: train
        path: data/war/*.parquet
  - config_name: ary
    data_files:
      - split: train
        path: data/ary/*.parquet
  - config_name: hak
    data_files:
      - split: train
        path: data/hak/*.parquet
  - config_name: ltg
    data_files:
      - split: train
        path: data/ltg/*.parquet
  - config_name: pcd
    data_files:
      - split: train
        path: data/pcd/*.parquet
  - config_name: igl
    data_files:
      - split: train
        path: data/igl/*.parquet
  - config_name: kl
    data_files:
      - split: train
        path: data/kl/*.parquet
  - config_name: ilo
    data_files:
      - split: train
        path: data/ilo/*.parquet
  - config_name: mai
    data_files:
      - split: train
        path: data/mai/*.parquet
  - config_name: map_bms
    data_files:
      - split: train
        path: data/map_bms/*.parquet
  - config_name: pnb
    data_files:
      - split: train
        path: data/pnb/*.parquet
  - config_name: sa
    data_files:
      - split: train
        path: data/sa/*.parquet
  - config_name: tig
    data_files:
      - split: train
        path: data/tig/*.parquet
  - config_name: pnt
    data_files:
      - split: train
        path: data/pnt/*.parquet
  - config_name: ang
    data_files:
      - split: train
        path: data/ang/*.parquet
  - config_name: lld
    data_files:
      - split: train
        path: data/lld/*.parquet
  - config_name: ppl
    data_files:
      - split: train
        path: data/ppl/*.parquet
  - config_name: szy
    data_files:
      - split: train
        path: data/szy/*.parquet
  - config_name: ne
    data_files:
      - split: train
        path: data/ne/*.parquet
  - config_name: tk
    data_files:
      - split: train
        path: data/tk/*.parquet
  - config_name: myv
    data_files:
      - split: train
        path: data/myv/*.parquet
  - config_name: bbc
    data_files:
      - split: train
        path: data/bbc/*.parquet
  - config_name: be_x_old
    data_files:
      - split: train
        path: data/be_x_old/*.parquet
  - config_name: ext
    data_files:
      - split: train
        path: data/ext/*.parquet
  - config_name: kaj
    data_files:
      - split: train
        path: data/kaj/*.parquet
  - config_name: ti
    data_files:
      - split: train
        path: data/ti/*.parquet
  - config_name: ami
    data_files:
      - split: train
        path: data/ami/*.parquet
  - config_name: da
    data_files:
      - split: train
        path: data/da/*.parquet
  - config_name: hsb
    data_files:
      - split: train
        path: data/hsb/*.parquet
  - config_name: kbd
    data_files:
      - split: train
        path: data/kbd/*.parquet
  - config_name: pl
    data_files:
      - split: train
        path: data/pl/*.parquet
  - config_name: rsk
    data_files:
      - split: train
        path: data/rsk/*.parquet
  - config_name: tl
    data_files:
      - split: train
        path: data/tl/*.parquet
  - config_name: zh_min_nan
    data_files:
      - split: train
        path: data/zh_min_nan/*.parquet
  - config_name: an
    data_files:
      - split: train
        path: data/an/*.parquet
  - config_name: kbp
    data_files:
      - split: train
        path: data/kbp/*.parquet
  - config_name: lbe
    data_files:
      - split: train
        path: data/lbe/*.parquet
  - config_name: pfl
    data_files:
      - split: train
        path: data/pfl/*.parquet
  - config_name: got
    data_files:
      - split: train
        path: data/got/*.parquet
  - config_name: guc
    data_files:
      - split: train
        path: data/guc/*.parquet
  - config_name: gv
    data_files:
      - split: train
        path: data/gv/*.parquet
  - config_name: ta
    data_files:
      - split: train
        path: data/ta/*.parquet
  - config_name: xh
    data_files:
      - split: train
        path: data/xh/*.parquet
  - config_name: bat_smg
    data_files:
      - split: train
        path: data/bat_smg/*.parquet
  - config_name: gu
    data_files:
      - split: train
        path: data/gu/*.parquet
  - config_name: kai
    data_files:
      - split: train
        path: data/kai/*.parquet
  - config_name: nqo
    data_files:
      - split: train
        path: data/nqo/*.parquet
  - config_name: su
    data_files:
      - split: train
        path: data/su/*.parquet
  - config_name: szl
    data_files:
      - split: train
        path: data/szl/*.parquet
  - config_name: ar
    data_files:
      - split: train
        path: data/ar/*.parquet
  - config_name: eml
    data_files:
      - split: train
        path: data/eml/*.parquet
  - config_name: pi
    data_files:
      - split: train
        path: data/pi/*.parquet
  - config_name: scn
    data_files:
      - split: train
        path: data/scn/*.parquet
  - config_name: shi
    data_files:
      - split: train
        path: data/shi/*.parquet
  - config_name: sm
    data_files:
      - split: train
        path: data/sm/*.parquet
  - config_name: bo
    data_files:
      - split: train
        path: data/bo/*.parquet
  - config_name: li
    data_files:
      - split: train
        path: data/li/*.parquet
  - config_name: lo
    data_files:
      - split: train
        path: data/lo/*.parquet
  - config_name: min
    data_files:
      - split: train
        path: data/min/*.parquet
  - config_name: th
    data_files:
      - split: train
        path: data/th/*.parquet
  - config_name: atj
    data_files:
      - split: train
        path: data/atj/*.parquet
  - config_name: ay
    data_files:
      - split: train
        path: data/ay/*.parquet
  - config_name: bug
    data_files:
      - split: train
        path: data/bug/*.parquet
  - config_name: ca
    data_files:
      - split: train
        path: data/ca/*.parquet
  - config_name: ckb
    data_files:
      - split: train
        path: data/ckb/*.parquet
  - config_name: eu
    data_files:
      - split: train
        path: data/eu/*.parquet
  - config_name: fi
    data_files:
      - split: train
        path: data/fi/*.parquet
  - config_name: hyw
    data_files:
      - split: train
        path: data/hyw/*.parquet
  - config_name: ee
    data_files:
      - split: train
        path: data/ee/*.parquet
  - config_name: gor
    data_files:
      - split: train
        path: data/gor/*.parquet
  - config_name: he
    data_files:
      - split: train
        path: data/he/*.parquet
  - config_name: id
    data_files:
      - split: train
        path: data/id/*.parquet
  - config_name: ii
    data_files:
      - split: train
        path: data/ii/*.parquet
  - config_name: jam
    data_files:
      - split: train
        path: data/jam/*.parquet
  - config_name: lmo
    data_files:
      - split: train
        path: data/lmo/*.parquet
  - config_name: lb
    data_files:
      - split: train
        path: data/lb/*.parquet
  - config_name: br
    data_files:
      - split: train
        path: data/br/*.parquet
  - config_name: din
    data_files:
      - split: train
        path: data/din/*.parquet
  - config_name: ff
    data_files:
      - split: train
        path: data/ff/*.parquet
  - config_name: ga
    data_files:
      - split: train
        path: data/ga/*.parquet
  - config_name: iba
    data_files:
      - split: train
        path: data/iba/*.parquet
  - config_name: ko
    data_files:
      - split: train
        path: data/ko/*.parquet
  - config_name: lfn
    data_files:
      - split: train
        path: data/lfn/*.parquet
  - config_name: tdd
    data_files:
      - split: train
        path: data/tdd/*.parquet
  - config_name: af
    data_files:
      - split: train
        path: data/af/*.parquet
  - config_name: fj
    data_files:
      - split: train
        path: data/fj/*.parquet
  - config_name: gag
    data_files:
      - split: train
        path: data/gag/*.parquet
  - config_name: gn
    data_files:
      - split: train
        path: data/gn/*.parquet
  - config_name: nup
    data_files:
      - split: train
        path: data/nup/*.parquet
  - config_name: pih
    data_files:
      - split: train
        path: data/pih/*.parquet
  - config_name: xal
    data_files:
      - split: train
        path: data/xal/*.parquet
  - config_name: xmf
    data_files:
      - split: train
        path: data/xmf/*.parquet
  - config_name: aa
    data_files:
      - split: train
        path: data/aa/*.parquet
  - config_name: hz
    data_files:
      - split: train
        path: data/hz/*.parquet
  - config_name: kr
    data_files:
      - split: train
        path: data/kr/*.parquet
  - config_name: lrc
    data_files:
      - split: train
        path: data/lrc/*.parquet
  - config_name: na
    data_files:
      - split: train
        path: data/na/*.parquet
dataset_info:
  - config_name: bh
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 8978
  - config_name: ho
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2
  - config_name: kge
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1833
  - config_name: mwl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4398
  - config_name: tcy
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3677
  - config_name: wikifunctions
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 23896
  - config_name: za
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1668
  - config_name: zea
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6834
  - config_name: fa
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1072305
  - config_name: no
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 672745
  - config_name: tw
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4996
  - config_name: mi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7680
  - config_name: pdc
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1739
  - config_name: rm
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3056
  - config_name: testcommons
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1
  - config_name: bg
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 308436
  - config_name: knc
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2197
  - config_name: zu
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5013
  - config_name: am
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 14012
  - config_name: bar
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 24707
  - config_name: bxr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2830
  - config_name: fat
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2102
  - config_name: hy
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 325435
  - config_name: it
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1913308
  - config_name: mk
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 159986
  - config_name: nso
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 8336
  - config_name: ak
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1
  - config_name: jv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 64686
  - config_name: kw
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5531
  - config_name: mdf
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7694
  - config_name: pag
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2360
  - config_name: rw
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 11229
  - config_name: ve
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 964
  - config_name: blk
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3269
  - config_name: kn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 35135
  - config_name: sh
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 445038
  - config_name: ch
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 466
  - config_name: crh
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 26443
  - config_name: si
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 27179
  - config_name: testwikidata
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 131022
  - config_name: ur
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 250695
  - config_name: wuu
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 47625
  - config_name: cdo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 8828
  - config_name: cu
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1359
  - config_name: iu
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 510
  - config_name: ky
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 76543
  - config_name: or
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 20818
  - config_name: pap
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5169
  - config_name: ba
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 63892
  - config_name: dty
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3935
  - config_name: haw
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2297
  - config_name: tet
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1276
  - config_name: ts
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1027
  - config_name: arc
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1624
  - config_name: bdr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 425
  - config_name: be
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 261618
  - config_name: la
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 139421
  - config_name: mhr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 10973
  - config_name: new
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 72602
  - config_name: pwn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 444
  - config_name: sw
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 106958
  - config_name: cs
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 588490
  - config_name: fo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 12283
  - config_name: gl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 229542
  - config_name: gpe
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5077
  - config_name: hr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 210243
  - config_name: my
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 98206
  - config_name: nds_nl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7119
  - config_name: ro
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 510832
  - config_name: frp
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5424
  - config_name: pcm
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1738
  - config_name: tly
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6757
  - config_name: tum
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 12875
  - config_name: ceb
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6111012
  - config_name: dtp
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1979
  - config_name: tn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4817
  - config_name: bjn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 11376
  - config_name: bpy
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 25168
  - config_name: cbk_zam
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3111
  - config_name: ce
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 846576
  - config_name: ja
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1490683
  - config_name: mad
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6643
  - config_name: ms
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 383478
  - config_name: simple
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 261460
  - config_name: ace
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 11749
  - config_name: arz
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1630858
  - config_name: diq
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 36818
  - config_name: kg
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1283
  - config_name: mg
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 99518
  - config_name: nv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 22402
  - config_name: rue
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 8603
  - config_name: vote
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7
  - config_name: stq
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3806
  - config_name: ty
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 275
  - config_name: as
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 24223
  - config_name: fy
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 57044
  - config_name: nah
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3702
  - config_name: nn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 174762
  - config_name: nrm
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4537
  - config_name: sco
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 32236
  - config_name: skr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 24312
  - config_name: tt
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 613866
  - config_name: ab
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6153
  - config_name: alt
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1105
  - config_name: dga
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3966
  - config_name: en
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7096118
  - config_name: ik
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 338
  - config_name: sg
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 213
  - config_name: vo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 47262
  - config_name: co
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7738
  - config_name: lg
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5322
  - config_name: pa
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 59690
  - config_name: chr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 690
  - config_name: mus
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2
  - config_name: ng
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 17
  - config_name: vi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1275578
  - config_name: lv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 139534
  - config_name: awa
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3759
  - config_name: cy
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 283552
  - config_name: ht
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 66130
  - config_name: ki
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1341
  - config_name: nl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2176652
  - config_name: st
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1785
  - config_name: syl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 955
  - config_name: bn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 186902
  - config_name: dz
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1252
  - config_name: kaa
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 9819
  - config_name: krc
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2107
  - config_name: ln
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4309
  - config_name: mrj
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 8490
  - config_name: tg
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 115689
  - config_name: zh
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1502996
  - config_name: als
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 31579
  - config_name: az
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 206877
  - config_name: bcl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 19994
  - config_name: ny
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 930
  - config_name: tpi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 666
  - config_name: ann
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 454
  - config_name: avk
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 27550
  - config_name: kk
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 246048
  - config_name: ks
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 9271
  - config_name: lad
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3947
  - config_name: mt
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7728
  - config_name: sn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 11059
  - config_name: uk
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1413984
  - config_name: dsb
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3233
  - config_name: es
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2033924
  - config_name: guw
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1756
  - config_name: ku
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 87435
  - config_name: olo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4611
  - config_name: uz
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 310488
  - config_name: bi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 778
  - config_name: gan
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3780
  - config_name: ha
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 95990
  - config_name: sr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 708077
  - config_name: av
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3824
  - config_name: et
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 253688
  - config_name: tyv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4185
  - config_name: bs
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 96745
  - config_name: dag
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 14291
  - config_name: gom
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4280
  - config_name: hif
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 9620
  - config_name: mn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 30196
  - config_name: nds
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 84724
  - config_name: ug
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 9973
  - config_name: lez
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4306
  - config_name: om
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2073
  - config_name: wa
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 12075
  - config_name: zgh
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 12058
  - config_name: btm
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1187
  - config_name: io
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 57030
  - config_name: rmy
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 613
  - config_name: roa_tara
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1801
  - config_name: zh_yue
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 123506
  - config_name: pam
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 9761
  - config_name: rn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 566
  - config_name: te
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 122265
  - config_name: tr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 631148
  - config_name: vec
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 66789
  - config_name: azb
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 244369
  - config_name: is
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 57643
  - config_name: kus
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1586
  - config_name: mni
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 10545
  - config_name: pms
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 70819
  - config_name: ss
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1316
  - config_name: ban
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 36142
  - config_name: dv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4374
  - config_name: el
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 267528
  - config_name: kcg
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1737
  - config_name: kv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5702
  - config_name: srn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1010
  - config_name: thankyou
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3
  - config_name: vep
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7037
  - config_name: fon
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3764
  - config_name: kab
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5479
  - config_name: ksh
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2728
  - config_name: lij
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 10470
  - config_name: ml
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 88739
  - config_name: ps
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 22415
  - config_name: pt
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1133459
  - config_name: sl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 190678
  - config_name: gur
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1641
  - config_name: nap
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5876
  - config_name: nia
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1809
  - config_name: tok
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3075
  - config_name: yo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 32013
  - config_name: bm
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 594
  - config_name: csb
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5480
  - config_name: fr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2735281
  - config_name: ie
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 13173
  - config_name: mzn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 64080
  - config_name: sah
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 17332
  - config_name: sd
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 21263
  - config_name: shn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 15046
  - config_name: cv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 57566
  - config_name: de
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3096176
  - config_name: hi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 171640
  - config_name: nov
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1634
  - config_name: trv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1887
  - config_name: vls
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 8139
  - config_name: ady
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 720
  - config_name: gd
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 14998
  - config_name: inh
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2156
  - config_name: jbo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1306
  - config_name: koi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3328
  - config_name: os
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 19084
  - config_name: roa_rup
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1239
  - config_name: sq
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 105670
  - config_name: ast
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 132347
  - config_name: lt
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 218089
  - config_name: sk
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 248687
  - config_name: so
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 11001
  - config_name: tay
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2769
  - config_name: ten
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 534
  - config_name: frr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 19559
  - config_name: ia
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 26984
  - config_name: mh
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7
  - config_name: mnw
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3768
  - config_name: nr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 551
  - config_name: yi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 15064
  - config_name: anp
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3150
  - config_name: fur
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4677
  - config_name: ka
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 192557
  - config_name: mos
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1587
  - config_name: sv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2610508
  - config_name: wo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1319
  - config_name: bew
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3364
  - config_name: oc
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 85732
  - config_name: udm
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5491
  - config_name: kj
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 3
  - config_name: km
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 13436
  - config_name: ru
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2092524
  - config_name: chy
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 469
  - config_name: cr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1
  - config_name: mr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 101268
  - config_name: qu
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 23791
  - config_name: rki
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1708
  - config_name: zh_classical
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 13115
  - config_name: eo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 382460
  - config_name: fiu_vro
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6479
  - config_name: glk
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 48477
  - config_name: hu
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 563268
  - config_name: ig
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 53265
  - config_name: sat
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 15550
  - config_name: sc
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7153
  - config_name: se
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5194
  - config_name: cho
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6
  - config_name: gcr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2378
  - config_name: smn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6269
  - config_name: to
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1603
  - config_name: war
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1214798
  - config_name: ary
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 13593
  - config_name: hak
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 8734
  - config_name: ltg
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1039
  - config_name: pcd
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5798
  - config_name: igl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1206
  - config_name: kl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1
  - config_name: ilo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 15269
  - config_name: mai
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 15010
  - config_name: map_bms
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5532
  - config_name: pnb
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 66592
  - config_name: sa
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 12781
  - config_name: tig
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 359
  - config_name: pnt
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 578
  - config_name: ang
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4260
  - config_name: lld
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 147949
  - config_name: ppl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 872
  - config_name: szy
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4636
  - config_name: ne
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 30088
  - config_name: tk
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6767
  - config_name: myv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 7497
  - config_name: bbc
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1337
  - config_name: be_x_old
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 89981
  - config_name: ext
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4219
  - config_name: kaj
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 986
  - config_name: ti
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 418
  - config_name: ami
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1804
  - config_name: da
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 309642
  - config_name: hsb
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 14170
  - config_name: kbd
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1666
  - config_name: pl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1645827
  - config_name: rsk
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1227
  - config_name: tl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 48302
  - config_name: zh_min_nan
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 418035
  - config_name: an
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 62145
  - config_name: kbp
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1966
  - config_name: lbe
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 919
  - config_name: pfl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2852
  - config_name: got
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1132
  - config_name: guc
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 893
  - config_name: gv
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 6568
  - config_name: ta
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 183948
  - config_name: xh
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2506
  - config_name: bat_smg
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 17095
  - config_name: gu
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 30920
  - config_name: kai
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 671
  - config_name: nqo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1619
  - config_name: su
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 60612
  - config_name: szl
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 55719
  - config_name: ar
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1285887
  - config_name: eml
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2121
  - config_name: pi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 123
  - config_name: scn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 23334
  - config_name: shi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 10829
  - config_name: sm
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1033
  - config_name: bo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 14785
  - config_name: li
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 15035
  - config_name: lo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5987
  - config_name: min
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 226531
  - config_name: th
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 181169
  - config_name: atj
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2003
  - config_name: ay
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4735
  - config_name: bug
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 10591
  - config_name: ca
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 787820
  - config_name: ckb
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 80784
  - config_name: eu
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 466375
  - config_name: fi
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 613451
  - config_name: hyw
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 13681
  - config_name: ee
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1067
  - config_name: gor
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 15440
  - config_name: he
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 374996
  - config_name: id
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 749574
  - config_name: ii
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2
  - config_name: jam
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1493
  - config_name: lmo
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 75533
  - config_name: lb
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 62932
  - config_name: br
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 77520
  - config_name: din
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 324
  - config_name: ff
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 27199
  - config_name: ga
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 58554
  - config_name: iba
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2392
  - config_name: ko
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 738854
  - config_name: lfn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 4870
  - config_name: tdd
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 541
  - config_name: af
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 126861
  - config_name: fj
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1113
  - config_name: gag
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 2166
  - config_name: gn
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 5711
  - config_name: nup
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1334
  - config_name: pih
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1
  - config_name: xal
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 1257
  - config_name: xmf
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 19563
  - config_name: aa
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 0
  - config_name: hz
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 0
  - config_name: kr
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 0
  - config_name: lrc
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 0
  - config_name: na
    features:
      - name: id
        dtype: int64
      - name: title
        dtype: string
      - name: markdown
        dtype: string
      - name: url
        dtype: string
      - name: lang
        dtype: string
      - name: length
        dtype: int32
      - name: timestamp
        dtype: string
    splits:
      - name: train
        num_examples: 0
---

# Open Wikipedia (Markdown)

> Every Wikipedia article converted to clean Markdown, organized by language and updated from the latest Wikimedia dumps

## What is it?

This dataset contains every article from every language edition of [Wikipedia](https://www.wikipedia.org/), converted from raw MediaWiki markup into clean, readable **Markdown**. Headings, bold, italic, code blocks, and internal links are all preserved as proper Markdown syntax, while templates, infoboxes, references, tables, categories, and other noise are stripped away.

The dataset currently contains **65.9M articles** across **367 languages**, sourced from the official [Wikimedia database dumps](https://dumps.wikimedia.org/). Each language's full XML export is streamed, parsed, and converted article by article. The results are stored as sharded Apache Parquet files with Zstandard compression, organized by language. Each language gets its own directory under `data/`, and each shard holds up to 500,000 articles.

This is the Markdown variant of the Open Wikipedia collection. If you need plain text with all formatting removed, see [](https://huggingface.co/datasets/). If you need the original MediaWiki source markup, see [](https://huggingface.co/datasets/).

## What is being released?

The dataset is organized as one directory per language, with sharded Parquet files inside each:

```
data/
  en/en-00000.parquet      English, shard 0
     en-00001.parquet      English, shard 1
     ...
  de/de-00000.parquet      German
  fr/fr-00000.parquet      French
  es/es-00000.parquet      Spanish
  ja/ja-00000.parquet      Japanese
  ...
  la/la-00000.parquet      Latin
```

Each Parquet file contains up to 500,000 rows. Languages with fewer articles than that fit in a single shard. Larger languages like English, German, and French are split across multiple shards. All files use Zstandard compression.

## How to download and use this dataset

### Using DuckDB

DuckDB can read Parquet files directly from Hugging Face without downloading anything first. This is the fastest way to explore the data.

```sql
-- Count articles per language
SELECT lang, COUNT(*) as articles
FROM read_parquet('hf://datasets/open-index/open-wikipedia-markdown/data/*/*.parquet')
GROUP BY lang
ORDER BY articles DESC;
```

```sql
-- Search for articles about a topic across all languages
SELECT title, lang, length, url
FROM read_parquet('hf://datasets/open-index/open-wikipedia-markdown/data/*/*.parquet')
WHERE markdown ILIKE '%machine learning%'
ORDER BY length DESC
LIMIT 20;
```

```sql
-- Article length distribution for English Wikipedia
SELECT
    percentile_disc(0.25) WITHIN GROUP (ORDER BY length) AS p25,
    percentile_disc(0.50) WITHIN GROUP (ORDER BY length) AS p50,
    percentile_disc(0.75) WITHIN GROUP (ORDER BY length) AS p75,
    percentile_disc(0.90) WITHIN GROUP (ORDER BY length) AS p90,
    percentile_disc(0.99) WITHIN GROUP (ORDER BY length) AS p99,
    AVG(length)::INT AS avg_length,
    MAX(length) AS max_length
FROM read_parquet('hf://datasets/open-index/open-wikipedia-markdown/data/en/*.parquet');
```

```sql
-- Find the longest articles in each language
SELECT lang, title, length, url
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY lang ORDER BY length DESC) AS rn
    FROM read_parquet('hf://datasets/open-index/open-wikipedia-markdown/data/*/*.parquet')
)
WHERE rn = 1
ORDER BY length DESC
LIMIT 20;
```

```sql
-- How many articles contain code blocks?
SELECT lang, COUNT(*) AS articles_with_code, COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS pct
FROM read_parquet('hf://datasets/open-index/open-wikipedia-markdown/data/*/*.parquet')
WHERE markdown LIKE '%```%'
GROUP BY lang
ORDER BY articles_with_code DESC
LIMIT 15;
```

### Using `datasets`

```python
from datasets import load_dataset

# Load English Wikipedia
ds = load_dataset("open-index/open-wikipedia-markdown", "en")
print(ds["train"][0]["title"])
print(ds["train"][0]["markdown"][:500])

# Stream the full dataset without downloading everything first
ds = load_dataset("open-index/open-wikipedia-markdown", "en", split="train", streaming=True)
for item in ds:
    print(item["title"], item["length"])

# Load a specific language
ds = load_dataset("open-index/open-wikipedia-markdown", "de")
print(f"German articles: {len(ds['train']):,}")
```

### Using `huggingface_hub`

```python
from huggingface_hub import snapshot_download

# Download only English
snapshot_download(
    "open-index/open-wikipedia-markdown",
    repo_type="dataset",
    local_dir="./wiki-md/",
    allow_patterns="data/en/*",
)
```

For faster downloads, install `pip install huggingface_hub[hf_transfer]` and set `HF_HUB_ENABLE_HF_TRANSFER=1`.

### Using the CLI

```bash
# Download a single language
huggingface-cli download open-index/open-wikipedia-markdown \
    --include "data/la/*" \
    --repo-type dataset --local-dir ./wiki-md/
```

### Using Polars

```python
import polars as pl

df = pl.read_parquet("data/en/*.parquet")
print(f"English articles: {len(df):,}")
print(f"Total Markdown text: {df['length'].sum() / 1e9:.1f} GB")
print(df.select("title", "length").describe())
```

## Dataset statistics

You can query the per-language statistics directly from the `stats.csv` file included in the dataset:

```sql
SELECT * FROM read_csv_auto('hf://datasets/open-index/open-wikipedia-markdown/stats.csv')
ORDER BY articles DESC;
```

The `stats.csv` file tracks each committed language with the following columns:

| Column | Description |
|--------|-------------|
| `lang` | ISO 639 language code |
| `lang_name` | Human-readable language name |
| `articles` | Number of articles in this language |
| `md_shards` | Number of Markdown Parquet shards |
| `text_shards` | Number of plain text Parquet shards |
| `wikitext_shards` | Number of wikitext Parquet shards |
| `md_bytes`, `text_bytes`, `wikitext_bytes` | Parquet file sizes per variant |
| `dump_bytes` | Original Wikimedia dump size |
| `dur_s` | Processing duration in seconds |
| `committed_at` | ISO 8601 timestamp of when this language was committed |

### Languages

| Language | Code | Articles | Shards |
|----------|------|----------|--------|
| bh | `bh` | 9.0K | 1 |
| ho | `ho` | 2 | 1 |
| kge | `kge` | 1.8K | 1 |
| mwl | `mwl` | 4.4K | 1 |
| tcy | `tcy` | 3.7K | 1 |
| wikifunctions | `wikifunctions` | 23.9K | 1 |
| za | `za` | 1.7K | 1 |
| zea | `zea` | 6.8K | 1 |
| Persian | `fa` | 1.1M | 3 |
| Norwegian | `no` | 672.7K | 2 |
| tw | `tw` | 5.0K | 1 |
| mi | `mi` | 7.7K | 1 |
| pdc | `pdc` | 1.7K | 1 |
| rm | `rm` | 3.1K | 1 |
| testcommons | `testcommons` | 1 | 1 |
| Bulgarian | `bg` | 308.4K | 1 |
| knc | `knc` | 2.2K | 1 |
| zu | `zu` | 5.0K | 1 |
| am | `am` | 14.0K | 1 |
| bar | `bar` | 24.7K | 1 |
| bxr | `bxr` | 2.8K | 1 |
| fat | `fat` | 2.1K | 1 |
| Armenian | `hy` | 325.4K | 1 |
| Italian | `it` | 1.9M | 4 |
| Macedonian | `mk` | 160.0K | 1 |
| nso | `nso` | 8.3K | 1 |
| ak | `ak` | 1 | 1 |
| Javanese | `jv` | 64.7K | 1 |
| kw | `kw` | 5.5K | 1 |
| mdf | `mdf` | 7.7K | 1 |
| pag | `pag` | 2.4K | 1 |
| rw | `rw` | 11.2K | 1 |
| ve | `ve` | 964 | 1 |
| blk | `blk` | 3.3K | 1 |
| Kannada | `kn` | 35.1K | 1 |
| Serbo-Croatian | `sh` | 445.0K | 1 |
| ch | `ch` | 466 | 1 |
| crh | `crh` | 26.4K | 1 |
| Sinhala | `si` | 27.2K | 1 |
| testwikidata | `testwikidata` | 131.0K | 1 |
| Urdu | `ur` | 250.7K | 1 |
| wuu | `wuu` | 47.6K | 1 |
| cdo | `cdo` | 8.8K | 1 |
| cu | `cu` | 1.4K | 1 |
| iu | `iu` | 510 | 1 |
| ky | `ky` | 76.5K | 1 |
| Odia | `or` | 20.8K | 1 |
| pap | `pap` | 5.2K | 1 |
| ba | `ba` | 63.9K | 1 |
| dty | `dty` | 3.9K | 1 |
| haw | `haw` | 2.3K | 1 |
| tet | `tet` | 1.3K | 1 |
| ts | `ts` | 1.0K | 1 |
| arc | `arc` | 1.6K | 1 |
| bdr | `bdr` | 425 | 1 |
| Belarusian | `be` | 261.6K | 1 |
| Latin | `la` | 139.4K | 1 |
| mhr | `mhr` | 11.0K | 1 |
| new | `new` | 72.6K | 1 |
| pwn | `pwn` | 444 | 1 |
| Swahili | `sw` | 107.0K | 1 |
| Czech | `cs` | 588.5K | 2 |
| fo | `fo` | 12.3K | 1 |
| Galician | `gl` | 229.5K | 1 |
| gpe | `gpe` | 5.1K | 1 |
| Croatian | `hr` | 210.2K | 1 |
| Burmese | `my` | 98.2K | 1 |
| nds_nl | `nds_nl` | 7.1K | 1 |
| Romanian | `ro` | 510.8K | 2 |
| frp | `frp` | 5.4K | 1 |
| pcm | `pcm` | 1.7K | 1 |
| tly | `tly` | 6.8K | 1 |
| tum | `tum` | 12.9K | 1 |
| Cebuano | `ceb` | 6.1M | 13 |
| dtp | `dtp` | 2.0K | 1 |
| tn | `tn` | 4.8K | 1 |
| bjn | `bjn` | 11.4K | 1 |
| bpy | `bpy` | 25.2K | 1 |
| cbk_zam | `cbk_zam` | 3.1K | 1 |
| Chechen | `ce` | 846.6K | 2 |
| Japanese | `ja` | 1.5M | 3 |
| mad | `mad` | 6.6K | 1 |
| Malay | `ms` | 383.5K | 1 |
| Simple English | `simple` | 261.5K | 1 |
| ace | `ace` | 11.7K | 1 |
| Egyptian Arabic | `arz` | 1.6M | 4 |
| diq | `diq` | 36.8K | 1 |
| kg | `kg` | 1.3K | 1 |
| mg | `mg` | 99.5K | 1 |
| nv | `nv` | 22.4K | 1 |
| rue | `rue` | 8.6K | 1 |
| vote | `vote` | 7 | 1 |
| stq | `stq` | 3.8K | 1 |
| ty | `ty` | 275 | 1 |
| as | `as` | 24.2K | 1 |
| fy | `fy` | 57.0K | 1 |
| nah | `nah` | 3.7K | 1 |
| nn | `nn` | 174.8K | 1 |
| nrm | `nrm` | 4.5K | 1 |
| sco | `sco` | 32.2K | 1 |
| skr | `skr` | 24.3K | 1 |
| tt | `tt` | 613.9K | 2 |
| ab | `ab` | 6.2K | 1 |
| alt | `alt` | 1.1K | 1 |
| dga | `dga` | 4.0K | 1 |
| English | `en` | 7.1M | 15 |
| ik | `ik` | 338 | 1 |
| sg | `sg` | 213 | 1 |
| vo | `vo` | 47.3K | 1 |
| co | `co` | 7.7K | 1 |
| lg | `lg` | 5.3K | 1 |
| Punjabi | `pa` | 59.7K | 1 |
| chr | `chr` | 690 | 1 |
| mus | `mus` | 2 | 1 |
| ng | `ng` | 17 | 1 |
| Vietnamese | `vi` | 1.3M | 3 |
| Latvian | `lv` | 139.5K | 1 |
| awa | `awa` | 3.8K | 1 |
| Welsh | `cy` | 283.6K | 1 |
| ht | `ht` | 66.1K | 1 |
| ki | `ki` | 1.3K | 1 |
| Dutch | `nl` | 2.2M | 5 |
| st | `st` | 1.8K | 1 |
| syl | `syl` | 955 | 1 |
| Bengali | `bn` | 186.9K | 1 |
| dz | `dz` | 1.3K | 1 |
| kaa | `kaa` | 9.8K | 1 |
| krc | `krc` | 2.1K | 1 |
| ln | `ln` | 4.3K | 1 |
| mrj | `mrj` | 8.5K | 1 |
| tg | `tg` | 115.7K | 1 |
| Chinese | `zh` | 1.5M | 4 |
| als | `als` | 31.6K | 1 |
| Azerbaijani | `az` | 206.9K | 1 |
| bcl | `bcl` | 20.0K | 1 |
| ny | `ny` | 930 | 1 |
| tpi | `tpi` | 666 | 1 |
| ann | `ann` | 454 | 1 |
| avk | `avk` | 27.6K | 1 |
| Kazakh | `kk` | 246.0K | 1 |
| ks | `ks` | 9.3K | 1 |
| lad | `lad` | 3.9K | 1 |
| mt | `mt` | 7.7K | 1 |
| sn | `sn` | 11.1K | 1 |
| Ukrainian | `uk` | 1.4M | 3 |
| dsb | `dsb` | 3.2K | 1 |
| Spanish | `es` | 2.0M | 5 |
| guw | `guw` | 1.8K | 1 |
| ku | `ku` | 87.4K | 1 |
| olo | `olo` | 4.6K | 1 |
| Uzbek | `uz` | 310.5K | 1 |
| bi | `bi` | 778 | 1 |
| gan | `gan` | 3.8K | 1 |
| ha | `ha` | 96.0K | 1 |
| Serbian | `sr` | 708.1K | 2 |
| av | `av` | 3.8K | 1 |
| Estonian | `et` | 253.7K | 1 |
| tyv | `tyv` | 4.2K | 1 |
| Bosnian | `bs` | 96.7K | 1 |
| dag | `dag` | 14.3K | 1 |
| gom | `gom` | 4.3K | 1 |
| hif | `hif` | 9.6K | 1 |
| Mongolian | `mn` | 30.2K | 1 |
| nds | `nds` | 84.7K | 1 |
| ug | `ug` | 10.0K | 1 |
| lez | `lez` | 4.3K | 1 |
| om | `om` | 2.1K | 1 |
| wa | `wa` | 12.1K | 1 |
| zgh | `zgh` | 12.1K | 1 |
| btm | `btm` | 1.2K | 1 |
| io | `io` | 57.0K | 1 |
| rmy | `rmy` | 613 | 1 |
| roa_tara | `roa_tara` | 1.8K | 1 |
| zh_yue | `zh_yue` | 123.5K | 1 |
| pam | `pam` | 9.8K | 1 |
| rn | `rn` | 566 | 1 |
| Telugu | `te` | 122.3K | 1 |
| Turkish | `tr` | 631.1K | 2 |
| vec | `vec` | 66.8K | 1 |
| South Azerbaijani | `azb` | 244.4K | 1 |
| is | `is` | 57.6K | 1 |
| kus | `kus` | 1.6K | 1 |
| mni | `mni` | 10.5K | 1 |
| pms | `pms` | 70.8K | 1 |
| ss | `ss` | 1.3K | 1 |
| ban | `ban` | 36.1K | 1 |
| dv | `dv` | 4.4K | 1 |
| Greek | `el` | 267.5K | 1 |
| kcg | `kcg` | 1.7K | 1 |
| kv | `kv` | 5.7K | 1 |
| srn | `srn` | 1.0K | 1 |
| thankyou | `thankyou` | 3 | 1 |
| vep | `vep` | 7.0K | 1 |
| fon | `fon` | 3.8K | 1 |
| kab | `kab` | 5.5K | 1 |
| ksh | `ksh` | 2.7K | 1 |
| lij | `lij` | 10.5K | 1 |
| Malayalam | `ml` | 88.7K | 1 |
| ps | `ps` | 22.4K | 1 |
| Portuguese | `pt` | 1.1M | 3 |
| Slovenian | `sl` | 190.7K | 1 |
| gur | `gur` | 1.6K | 1 |
| nap | `nap` | 5.9K | 1 |
| nia | `nia` | 1.8K | 1 |
| tok | `tok` | 3.1K | 1 |
| yo | `yo` | 32.0K | 1 |
| bm | `bm` | 594 | 1 |
| csb | `csb` | 5.5K | 1 |
| French | `fr` | 2.7M | 6 |
| ie | `ie` | 13.2K | 1 |
| mzn | `mzn` | 64.1K | 1 |
| sah | `sah` | 17.3K | 1 |
| sd | `sd` | 21.3K | 1 |
| shn | `shn` | 15.0K | 1 |
| cv | `cv` | 57.6K | 1 |
| German | `de` | 3.1M | 7 |
| Hindi | `hi` | 171.6K | 1 |
| nov | `nov` | 1.6K | 1 |
| trv | `trv` | 1.9K | 1 |
| vls | `vls` | 8.1K | 1 |
| ady | `ady` | 720 | 1 |
| gd | `gd` | 15.0K | 1 |
| inh | `inh` | 2.2K | 1 |
| jbo | `jbo` | 1.3K | 1 |
| koi | `koi` | 3.3K | 1 |
| os | `os` | 19.1K | 1 |
| roa_rup | `roa_rup` | 1.2K | 1 |
| Albanian | `sq` | 105.7K | 1 |
| ast | `ast` | 132.3K | 1 |
| Lithuanian | `lt` | 218.1K | 1 |
| Slovak | `sk` | 248.7K | 1 |
| so | `so` | 11.0K | 1 |
| tay | `tay` | 2.8K | 1 |
| ten | `ten` | 534 | 1 |
| frr | `frr` | 19.6K | 1 |
| ia | `ia` | 27.0K | 1 |
| mh | `mh` | 7 | 1 |
| mnw | `mnw` | 3.8K | 1 |
| nr | `nr` | 551 | 1 |
| Yiddish | `yi` | 15.1K | 1 |
| anp | `anp` | 3.1K | 1 |
| fur | `fur` | 4.7K | 1 |
| Georgian | `ka` | 192.6K | 1 |
| mos | `mos` | 1.6K | 1 |
| Swedish | `sv` | 2.6M | 6 |
| wo | `wo` | 1.3K | 1 |
| bew | `bew` | 3.4K | 1 |
| oc | `oc` | 85.7K | 1 |
| udm | `udm` | 5.5K | 1 |
| kj | `kj` | 3 | 1 |
| Khmer | `km` | 13.4K | 1 |
| Russian | `ru` | 2.1M | 5 |
| chy | `chy` | 469 | 1 |
| cr | `cr` | 1 | 1 |
| Marathi | `mr` | 101.3K | 1 |
| qu | `qu` | 23.8K | 1 |
| rki | `rki` | 1.7K | 1 |
| zh_classical | `zh_classical` | 13.1K | 1 |
| Esperanto | `eo` | 382.5K | 1 |
| fiu_vro | `fiu_vro` | 6.5K | 1 |
| glk | `glk` | 48.5K | 1 |
| Hungarian | `hu` | 563.3K | 2 |
| ig | `ig` | 53.3K | 1 |
| sat | `sat` | 15.6K | 1 |
| sc | `sc` | 7.2K | 1 |
| se | `se` | 5.2K | 1 |
| cho | `cho` | 6 | 1 |
| gcr | `gcr` | 2.4K | 1 |
| smn | `smn` | 6.3K | 1 |
| to | `to` | 1.6K | 1 |
| Waray | `war` | 1.2M | 3 |
| ary | `ary` | 13.6K | 1 |
| hak | `hak` | 8.7K | 1 |
| ltg | `ltg` | 1.0K | 1 |
| pcd | `pcd` | 5.8K | 1 |
| igl | `igl` | 1.2K | 1 |
| kl | `kl` | 1 | 1 |
| ilo | `ilo` | 15.3K | 1 |
| mai | `mai` | 15.0K | 1 |
| map_bms | `map_bms` | 5.5K | 1 |
| pnb | `pnb` | 66.6K | 1 |
| Sanskrit | `sa` | 12.8K | 1 |
| tig | `tig` | 359 | 1 |
| pnt | `pnt` | 578 | 1 |
| ang | `ang` | 4.3K | 1 |
| lld | `lld` | 147.9K | 1 |
| ppl | `ppl` | 872 | 1 |
| szy | `szy` | 4.6K | 1 |
| Nepali | `ne` | 30.1K | 1 |
| tk | `tk` | 6.8K | 1 |
| myv | `myv` | 7.5K | 1 |
| bbc | `bbc` | 1.3K | 1 |
| be_x_old | `be_x_old` | 90.0K | 1 |
| ext | `ext` | 4.2K | 1 |
| kaj | `kaj` | 986 | 1 |
| ti | `ti` | 418 | 1 |
| ami | `ami` | 1.8K | 1 |
| Danish | `da` | 309.6K | 1 |
| hsb | `hsb` | 14.2K | 1 |
| kbd | `kbd` | 1.7K | 1 |
| Polish | `pl` | 1.6M | 4 |
| rsk | `rsk` | 1.2K | 1 |
| Tagalog | `tl` | 48.3K | 1 |
| zh_min_nan | `zh_min_nan` | 418.0K | 1 |
| an | `an` | 62.1K | 1 |
| kbp | `kbp` | 2.0K | 1 |
| lbe | `lbe` | 919 | 1 |
| pfl | `pfl` | 2.9K | 1 |
| got | `got` | 1.1K | 1 |
| guc | `guc` | 893 | 1 |
| gv | `gv` | 6.6K | 1 |
| Tamil | `ta` | 183.9K | 1 |
| xh | `xh` | 2.5K | 1 |
| bat_smg | `bat_smg` | 17.1K | 1 |
| Gujarati | `gu` | 30.9K | 1 |
| kai | `kai` | 671 | 1 |
| nqo | `nqo` | 1.6K | 1 |
| Sundanese | `su` | 60.6K | 1 |
| szl | `szl` | 55.7K | 1 |
| Arabic | `ar` | 1.3M | 3 |
| eml | `eml` | 2.1K | 1 |
| pi | `pi` | 123 | 1 |
| scn | `scn` | 23.3K | 1 |
| shi | `shi` | 10.8K | 1 |
| sm | `sm` | 1.0K | 1 |
| bo | `bo` | 14.8K | 1 |
| li | `li` | 15.0K | 1 |
| Lao | `lo` | 6.0K | 1 |
| Minangkabau | `min` | 226.5K | 1 |
| Thai | `th` | 181.2K | 1 |
| atj | `atj` | 2.0K | 1 |
| ay | `ay` | 4.7K | 1 |
| bug | `bug` | 10.6K | 1 |
| Catalan | `ca` | 787.8K | 2 |
| ckb | `ckb` | 80.8K | 1 |
| Basque | `eu` | 466.4K | 1 |
| Finnish | `fi` | 613.5K | 2 |
| hyw | `hyw` | 13.7K | 1 |
| ee | `ee` | 1.1K | 1 |
| gor | `gor` | 15.4K | 1 |
| Hebrew | `he` | 375.0K | 1 |
| Indonesian | `id` | 749.6K | 2 |
| ii | `ii` | 2 | 1 |
| jam | `jam` | 1.5K | 1 |
| lmo | `lmo` | 75.5K | 1 |
| lb | `lb` | 62.9K | 1 |
| br | `br` | 77.5K | 1 |
| din | `din` | 324 | 1 |
| ff | `ff` | 27.2K | 1 |
| ga | `ga` | 58.6K | 1 |
| iba | `iba` | 2.4K | 1 |
| Korean | `ko` | 738.9K | 2 |
| lfn | `lfn` | 4.9K | 1 |
| tdd | `tdd` | 541 | 1 |
| Afrikaans | `af` | 126.9K | 1 |
| fj | `fj` | 1.1K | 1 |
| gag | `gag` | 2.2K | 1 |
| gn | `gn` | 5.7K | 1 |
| nup | `nup` | 1.3K | 1 |
| pih | `pih` | 1 | 1 |
| xal | `xal` | 1.3K | 1 |
| xmf | `xmf` | 19.6K | 1 |
| aa | `aa` | 0 | 0 |
| hz | `hz` | 0 | 0 |
| kr | `kr` | 0 | 0 |
| lrc | `lrc` | 0 | 0 |
| na | `na` | 0 | 0 |

## Schema

Every Parquet file shares the same schema:

| Column | Type | Description |
|--------|------|-------------|
| `id` | `int64` | Wikipedia page ID, unique within each language edition |
| `title` | `string` | Article title as it appears on Wikipedia |
| `markdown` | `string` | Full article body converted from wikitext to Markdown |
| `url` | `string` | Direct URL to the Wikipedia article |
| `lang` | `string` | ISO 639 language code (e.g. `en`, `de`, `fr`, `ja`) |
| `length` | `int32` | Markdown body length in bytes |
| `timestamp` | `string` | Last revision timestamp in ISO 8601 format |

### Example instance

Here is an example row from the English partition, showing a converted article:

```json
{
  "id": 12,
  "title": "Anarchism",
  "markdown": "# Anarchism\n\n**Anarchism** is a political philosophy and movement that is against all forms of authority...",
  "url": "https://en.wikipedia.org/wiki/Anarchism",
  "lang": "en",
  "length": 87453,
  "timestamp": "2025-12-15T08:22:01Z"
}
```

The `markdown` field contains the full article text with Markdown formatting. Internal wiki links are converted to full Wikipedia URLs, so `[[United States|US]]` becomes `[US](https://en.wikipedia.org/wiki/United_States)`.

## Wikitext to Markdown conversion

The conversion handles the most common MediaWiki syntax elements and maps them to their Markdown equivalents:

| MediaWiki syntax | Markdown output |
|-----------------|-----------------|
| `== Heading ==` | `## Heading` |
| `=== Subheading ===` | `### Subheading` |
| `'''bold'''` | `**bold**` |
| `''italic''` | `*italic*` |
| `[[Page\|Text]]` | `[Text](https://lang.wikipedia.org/wiki/Page)` |
| `[https://example.com text]` | `[text](https://example.com)` |
| `<syntaxhighlight lang="python">` | ` ```python ``` ` |
| `<code>x</code>` | `` `x` `` |
| `<pre>block</pre>` | ` ```\nblock\n``` ` |

### What gets stripped

The following elements are removed during conversion to produce clean, readable text:

| Element | Handling |
|---------|----------|
| `{{templates}}` | Removed entirely, including Infobox, Navbox, Taxobox, and all other templates |
| `{{Infobox ...}}` | Removed, including nested template parameters |
| `{| tables |}` | Removed |
| `<ref>` citations | Removed, including named references |
| `[[File:]]` / `[[Image:]]` | Removed, including thumbnails and captions |
| `[[Category:]]` | Removed |
| `<!-- comments -->` | Removed |
| Interwiki links | Removed |
| Magic words | `__NOTOC__`, `__FORCETOC__`, and similar directives are removed |

The goal is to preserve the article's readable content and structure while removing everything that only makes sense in the context of the MediaWiki rendering engine.

## How it works

The pipeline processes Wikipedia language editions through the following steps:

1. **Download.** The latest `{lang}wiki-latest-pages-articles.xml.bz2` dump is streamed from [dumps.wikimedia.org](https://dumps.wikimedia.org/). Downloads support HTTP range resumption, so interrupted transfers pick up where they left off.

2. **Parse.** A streaming XML parser processes the bzip2-compressed dump without extracting it to disk. Only namespace-0 pages (articles) are kept. Redirects, talk pages, user pages, and all other namespaces are skipped.

3. **Convert.** Each article's wikitext is converted to Markdown through a series of regex-based transformations. Templates are stripped with up to 5 nesting passes to handle deeply nested constructs. Internal wiki links are resolved to full Wikipedia URLs for the appropriate language edition.

4. **Filter.** Articles shorter than 100 bytes after conversion are excluded. This removes stubs, disambiguation pages, and other pages with minimal content.

5. **Shard.** Articles are written to Zstandard-compressed Parquet files, approximately 500,000 rows per shard. Multiple languages are processed in parallel using a worker pool.

6. **Publish.** Each language's shards are committed to this Hugging Face repository as they complete. Commit messages include article counts, shard counts, and file sizes for auditability.

## Considerations

### Why Markdown instead of plain text?

Plain text is sufficient for many NLP tasks, but it loses document structure. Markdown preserves headings, bold, italic, code blocks, and links, which makes it better suited for:

- Language model training where the model should understand document structure
- Retrieval-augmented generation (RAG) where chunking by heading sections produces more coherent results
- Knowledge graph construction where preserved links encode relationships between concepts

If you do not need formatting, the [plain text variant](https://huggingface.co/datasets/) is smaller and simpler.

### Known limitations

- **Conversion is regex-based, not a full parser.** Some complex wikitext constructs (deeply nested tables inside templates, parser functions, Lua module output) may not convert perfectly. The vast majority of articles convert cleanly, but edge cases exist.
- **Templates are stripped, not expanded.** Infoboxes, navigation boxes, and other templates are removed entirely rather than expanded to their rendered output. This means some structured data that appears in rendered Wikipedia pages is not present in this dataset.
- **One snapshot in time.** This dataset represents a single snapshot of each language's dump. It does not track edit history or article revisions.
- **Dump availability varies.** Not all language editions have their dumps available at all times. Languages whose dumps fail to download are skipped and will be included in future updates.

## Related datasets

- [](https://huggingface.co/datasets/) - Same articles as pure plain text with all formatting removed. Smaller files, better for embeddings and classification.
- [](https://huggingface.co/datasets/) - Same articles in original MediaWiki wikitext markup. Use this if you need templates, tables, references, and other source elements.

## Thanks

The content in this dataset was written by millions of Wikipedia editors worldwide and is hosted by the [Wikimedia Foundation](https://www.wikimedia.org/). The raw data comes from the [Wikimedia database dumps](https://dumps.wikimedia.org/), which the Foundation makes freely available for download.

Wikipedia is one of humanity's greatest collaborative achievements. All credit for the content goes to the volunteer editors who write, review, and maintain it.

This dataset is an independent conversion and is not affiliated with or endorsed by the Wikimedia Foundation.

## Licensing

Wikipedia content is released under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0). This dataset inherits that license. If you redistribute or build upon this data, you must give appropriate credit and share your contributions under the same license.

## Citation

```bibtex
@dataset{open_wikipedia_markdown,
  title     = {Open Wikipedia (Markdown)},
  author    = {Open Index},
  year      = {2026},
  url       = {https://huggingface.co/datasets/open-index/open-wikipedia-markdown},
  license   = {CC BY-SA 4.0},
  publisher = {Hugging Face}
}
```

_Last updated: 2026-05-30_
