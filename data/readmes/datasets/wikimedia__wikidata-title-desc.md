---
license: cc-by-sa-4.0
language:
  - ab
  - ace
  - ady
  - af
  - als
  - alt
  - am
  - ami
  - an
  - ann
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
  - bbc
  - bcl
  - bdr
  - be
  - bew
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
  - btm
  - bug
  - bxr
  - ca
  - cdo
  - ce
  - ch
  - chr
  - chy
  - ckb
  - co
  - crh
  - cs
  - csb
  - cu
  - cv
  - cy
  - da
  - dag
  - de
  - dga
  - din
  - diq
  - dsb
  - dtp
  - dty
  - dv
  - dz
  - ee
  - el
  - eml
  - en
  - eo
  - es
  - et
  - eu
  - ext
  - fa
  - fat
  - ff
  - fi
  - fj
  - fo
  - fon
  - fr
  - frp
  - frr
  - fur
  - fy
  - ga
  - gag
  - gan
  - gd
  - gl
  - glk
  - gn
  - gom
  - gor
  - got
  - gpe
  - gu
  - guc
  - gur
  - guw
  - gv
  - ha
  - haw
  - he
  - hi
  - hif
  - hr
  - hsb
  - ht
  - hu
  - hy
  - hyw
  - ia
  - iba
  - id
  - ie
  - ig
  - igl
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
  - kab
  - kaj
  - kbd
  - kbp
  - kcg
  - kg
  - kge
  - ki
  - kk
  - km
  - kn
  - knc
  - ko
  - koi
  - krc
  - ks
  - ksh
  - ku
  - kus
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
  - lt
  - ltg
  - lv
  - mad
  - mai
  - mdf
  - mg
  - mhr
  - mi
  - min
  - mk
  - ml
  - mn
  - mni
  - mnw
  - mos
  - mr
  - mrj
  - ms
  - mt
  - mwl
  - my
  - myv
  - mzn
  - nah
  - nap
  - nb
  - nds
  - ne
  - new
  - nia
  - nl
  - nn
  - nov
  - nqo
  - nr
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
  - pl
  - pms
  - pnb
  - pnt
  - ps
  - pt
  - pwn
  - qu
  - rki
  - rm
  - rmy
  - rn
  - ro
  - rsk
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
  - sk
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
  - syl
  - szl
  - szy
  - ta
  - tay
  - tcy
  - tdd
  - te
  - tet
  - tg
  - th
  - ti
  - tig
  - tk
  - tl
  - tly
  - tn
  - to
  - tok
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
  - wo
  - wuu
  - xal
  - xh
  - xmf
  - yi
  - yo
  - za
  - zea
  - zgh
  - zh
  - zu
language_bcp47:
  - simple

tags:
  - wikidata
  - wikipedia
  - multilingual
  - entity-descriptions
  - knowledge-base
  - nlp
pretty_name: Wikidata Title and Description
dataset_info:
  features:
    - name: qid
      dtype: string
    - name: lang
      dtype: string
    - name: title
      dtype: string
    - name: description
      dtype: string
    - name: snapshot
      dtype: string
configs:
  - config_name: all
    data_files: data/all/train.parquet
    default: true
  - config_name: ab
    data_files: data/ab/train.parquet
  - config_name: ace
    data_files: data/ace/train.parquet
  - config_name: ady
    data_files: data/ady/train.parquet
  - config_name: af
    data_files: data/af/train.parquet
  - config_name: als
    data_files: data/als/train.parquet
  - config_name: alt
    data_files: data/alt/train.parquet
  - config_name: am
    data_files: data/am/train.parquet
  - config_name: ami
    data_files: data/ami/train.parquet
  - config_name: an
    data_files: data/an/train.parquet
  - config_name: ann
    data_files: data/ann/train.parquet
  - config_name: anp
    data_files: data/anp/train.parquet
  - config_name: ar
    data_files: data/ar/train.parquet
  - config_name: arc
    data_files: data/arc/train.parquet
  - config_name: ary
    data_files: data/ary/train.parquet
  - config_name: arz
    data_files: data/arz/train.parquet
  - config_name: as
    data_files: data/as/train.parquet
  - config_name: ast
    data_files: data/ast/train.parquet
  - config_name: atj
    data_files: data/atj/train.parquet
  - config_name: av
    data_files: data/av/train.parquet
  - config_name: avk
    data_files: data/avk/train.parquet
  - config_name: awa
    data_files: data/awa/train.parquet
  - config_name: ay
    data_files: data/ay/train.parquet
  - config_name: az
    data_files: data/az/train.parquet
  - config_name: azb
    data_files: data/azb/train.parquet
  - config_name: ba
    data_files: data/ba/train.parquet
  - config_name: ban
    data_files: data/ban/train.parquet
  - config_name: bar
    data_files: data/bar/train.parquet
  - config_name: bbc
    data_files: data/bbc/train.parquet
  - config_name: bcl
    data_files: data/bcl/train.parquet
  - config_name: bdr
    data_files: data/bdr/train.parquet
  - config_name: be
    data_files: data/be/train.parquet
  - config_name: bew
    data_files: data/bew/train.parquet
  - config_name: bg
    data_files: data/bg/train.parquet
  - config_name: bh
    data_files: data/bh/train.parquet
  - config_name: bi
    data_files: data/bi/train.parquet
  - config_name: bjn
    data_files: data/bjn/train.parquet
  - config_name: blk
    data_files: data/blk/train.parquet
  - config_name: bm
    data_files: data/bm/train.parquet
  - config_name: bn
    data_files: data/bn/train.parquet
  - config_name: bo
    data_files: data/bo/train.parquet
  - config_name: bpy
    data_files: data/bpy/train.parquet
  - config_name: br
    data_files: data/br/train.parquet
  - config_name: bs
    data_files: data/bs/train.parquet
  - config_name: btm
    data_files: data/btm/train.parquet
  - config_name: bug
    data_files: data/bug/train.parquet
  - config_name: bxr
    data_files: data/bxr/train.parquet
  - config_name: ca
    data_files: data/ca/train.parquet
  - config_name: cdo
    data_files: data/cdo/train.parquet
  - config_name: ce
    data_files: data/ce/train.parquet
  - config_name: ch
    data_files: data/ch/train.parquet
  - config_name: chr
    data_files: data/chr/train.parquet
  - config_name: chy
    data_files: data/chy/train.parquet
  - config_name: ckb
    data_files: data/ckb/train.parquet
  - config_name: co
    data_files: data/co/train.parquet
  - config_name: crh
    data_files: data/crh/train.parquet
  - config_name: cs
    data_files: data/cs/train.parquet
  - config_name: csb
    data_files: data/csb/train.parquet
  - config_name: cu
    data_files: data/cu/train.parquet
  - config_name: cv
    data_files: data/cv/train.parquet
  - config_name: cy
    data_files: data/cy/train.parquet
  - config_name: da
    data_files: data/da/train.parquet
  - config_name: dag
    data_files: data/dag/train.parquet
  - config_name: de
    data_files: data/de/train.parquet
  - config_name: dga
    data_files: data/dga/train.parquet
  - config_name: din
    data_files: data/din/train.parquet
  - config_name: diq
    data_files: data/diq/train.parquet
  - config_name: dsb
    data_files: data/dsb/train.parquet
  - config_name: dtp
    data_files: data/dtp/train.parquet
  - config_name: dty
    data_files: data/dty/train.parquet
  - config_name: dv
    data_files: data/dv/train.parquet
  - config_name: dz
    data_files: data/dz/train.parquet
  - config_name: ee
    data_files: data/ee/train.parquet
  - config_name: el
    data_files: data/el/train.parquet
  - config_name: eml
    data_files: data/eml/train.parquet
  - config_name: en
    data_files: data/en/train.parquet
  - config_name: eo
    data_files: data/eo/train.parquet
  - config_name: es
    data_files: data/es/train.parquet
  - config_name: et
    data_files: data/et/train.parquet
  - config_name: eu
    data_files: data/eu/train.parquet
  - config_name: ext
    data_files: data/ext/train.parquet
  - config_name: fa
    data_files: data/fa/train.parquet
  - config_name: fat
    data_files: data/fat/train.parquet
  - config_name: ff
    data_files: data/ff/train.parquet
  - config_name: fi
    data_files: data/fi/train.parquet
  - config_name: fj
    data_files: data/fj/train.parquet
  - config_name: fo
    data_files: data/fo/train.parquet
  - config_name: fon
    data_files: data/fon/train.parquet
  - config_name: fr
    data_files: data/fr/train.parquet
  - config_name: frp
    data_files: data/frp/train.parquet
  - config_name: frr
    data_files: data/frr/train.parquet
  - config_name: fur
    data_files: data/fur/train.parquet
  - config_name: fy
    data_files: data/fy/train.parquet
  - config_name: ga
    data_files: data/ga/train.parquet
  - config_name: gag
    data_files: data/gag/train.parquet
  - config_name: gan
    data_files: data/gan/train.parquet
  - config_name: gd
    data_files: data/gd/train.parquet
  - config_name: gl
    data_files: data/gl/train.parquet
  - config_name: glk
    data_files: data/glk/train.parquet
  - config_name: gn
    data_files: data/gn/train.parquet
  - config_name: gom
    data_files: data/gom/train.parquet
  - config_name: gor
    data_files: data/gor/train.parquet
  - config_name: got
    data_files: data/got/train.parquet
  - config_name: gpe
    data_files: data/gpe/train.parquet
  - config_name: gu
    data_files: data/gu/train.parquet
  - config_name: guc
    data_files: data/guc/train.parquet
  - config_name: gur
    data_files: data/gur/train.parquet
  - config_name: guw
    data_files: data/guw/train.parquet
  - config_name: gv
    data_files: data/gv/train.parquet
  - config_name: ha
    data_files: data/ha/train.parquet
  - config_name: haw
    data_files: data/haw/train.parquet
  - config_name: he
    data_files: data/he/train.parquet
  - config_name: hi
    data_files: data/hi/train.parquet
  - config_name: hif
    data_files: data/hif/train.parquet
  - config_name: hr
    data_files: data/hr/train.parquet
  - config_name: hsb
    data_files: data/hsb/train.parquet
  - config_name: ht
    data_files: data/ht/train.parquet
  - config_name: hu
    data_files: data/hu/train.parquet
  - config_name: hy
    data_files: data/hy/train.parquet
  - config_name: hyw
    data_files: data/hyw/train.parquet
  - config_name: ia
    data_files: data/ia/train.parquet
  - config_name: iba
    data_files: data/iba/train.parquet
  - config_name: id
    data_files: data/id/train.parquet
  - config_name: ie
    data_files: data/ie/train.parquet
  - config_name: ig
    data_files: data/ig/train.parquet
  - config_name: igl
    data_files: data/igl/train.parquet
  - config_name: ik
    data_files: data/ik/train.parquet
  - config_name: ilo
    data_files: data/ilo/train.parquet
  - config_name: inh
    data_files: data/inh/train.parquet
  - config_name: io
    data_files: data/io/train.parquet
  - config_name: is
    data_files: data/is/train.parquet
  - config_name: it
    data_files: data/it/train.parquet
  - config_name: iu
    data_files: data/iu/train.parquet
  - config_name: ja
    data_files: data/ja/train.parquet
  - config_name: jam
    data_files: data/jam/train.parquet
  - config_name: jbo
    data_files: data/jbo/train.parquet
  - config_name: jv
    data_files: data/jv/train.parquet
  - config_name: ka
    data_files: data/ka/train.parquet
  - config_name: kab
    data_files: data/kab/train.parquet
  - config_name: kaj
    data_files: data/kaj/train.parquet
  - config_name: kbd
    data_files: data/kbd/train.parquet
  - config_name: kbp
    data_files: data/kbp/train.parquet
  - config_name: kcg
    data_files: data/kcg/train.parquet
  - config_name: kg
    data_files: data/kg/train.parquet
  - config_name: kge
    data_files: data/kge/train.parquet
  - config_name: ki
    data_files: data/ki/train.parquet
  - config_name: kk
    data_files: data/kk/train.parquet
  - config_name: km
    data_files: data/km/train.parquet
  - config_name: kn
    data_files: data/kn/train.parquet
  - config_name: knc
    data_files: data/knc/train.parquet
  - config_name: ko
    data_files: data/ko/train.parquet
  - config_name: koi
    data_files: data/koi/train.parquet
  - config_name: krc
    data_files: data/krc/train.parquet
  - config_name: ks
    data_files: data/ks/train.parquet
  - config_name: ksh
    data_files: data/ksh/train.parquet
  - config_name: ku
    data_files: data/ku/train.parquet
  - config_name: kus
    data_files: data/kus/train.parquet
  - config_name: kv
    data_files: data/kv/train.parquet
  - config_name: kw
    data_files: data/kw/train.parquet
  - config_name: ky
    data_files: data/ky/train.parquet
  - config_name: la
    data_files: data/la/train.parquet
  - config_name: lad
    data_files: data/lad/train.parquet
  - config_name: lb
    data_files: data/lb/train.parquet
  - config_name: lbe
    data_files: data/lbe/train.parquet
  - config_name: lez
    data_files: data/lez/train.parquet
  - config_name: lfn
    data_files: data/lfn/train.parquet
  - config_name: lg
    data_files: data/lg/train.parquet
  - config_name: li
    data_files: data/li/train.parquet
  - config_name: lij
    data_files: data/lij/train.parquet
  - config_name: lld
    data_files: data/lld/train.parquet
  - config_name: lmo
    data_files: data/lmo/train.parquet
  - config_name: ln
    data_files: data/ln/train.parquet
  - config_name: lo
    data_files: data/lo/train.parquet
  - config_name: lt
    data_files: data/lt/train.parquet
  - config_name: ltg
    data_files: data/ltg/train.parquet
  - config_name: lv
    data_files: data/lv/train.parquet
  - config_name: mad
    data_files: data/mad/train.parquet
  - config_name: mai
    data_files: data/mai/train.parquet
  - config_name: mdf
    data_files: data/mdf/train.parquet
  - config_name: mg
    data_files: data/mg/train.parquet
  - config_name: mhr
    data_files: data/mhr/train.parquet
  - config_name: mi
    data_files: data/mi/train.parquet
  - config_name: min
    data_files: data/min/train.parquet
  - config_name: mk
    data_files: data/mk/train.parquet
  - config_name: ml
    data_files: data/ml/train.parquet
  - config_name: mn
    data_files: data/mn/train.parquet
  - config_name: mni
    data_files: data/mni/train.parquet
  - config_name: mnw
    data_files: data/mnw/train.parquet
  - config_name: mos
    data_files: data/mos/train.parquet
  - config_name: mr
    data_files: data/mr/train.parquet
  - config_name: mrj
    data_files: data/mrj/train.parquet
  - config_name: ms
    data_files: data/ms/train.parquet
  - config_name: mt
    data_files: data/mt/train.parquet
  - config_name: mwl
    data_files: data/mwl/train.parquet
  - config_name: my
    data_files: data/my/train.parquet
  - config_name: myv
    data_files: data/myv/train.parquet
  - config_name: mzn
    data_files: data/mzn/train.parquet
  - config_name: nah
    data_files: data/nah/train.parquet
  - config_name: nap
    data_files: data/nap/train.parquet
  - config_name: nb
    data_files: data/nb/train.parquet
  - config_name: nds
    data_files: data/nds/train.parquet
  - config_name: ne
    data_files: data/ne/train.parquet
  - config_name: new
    data_files: data/new/train.parquet
  - config_name: nia
    data_files: data/nia/train.parquet
  - config_name: nl
    data_files: data/nl/train.parquet
  - config_name: nn
    data_files: data/nn/train.parquet
  - config_name: nov
    data_files: data/nov/train.parquet
  - config_name: nqo
    data_files: data/nqo/train.parquet
  - config_name: nr
    data_files: data/nr/train.parquet
  - config_name: nrm
    data_files: data/nrm/train.parquet
  - config_name: nso
    data_files: data/nso/train.parquet
  - config_name: nv
    data_files: data/nv/train.parquet
  - config_name: ny
    data_files: data/ny/train.parquet
  - config_name: oc
    data_files: data/oc/train.parquet
  - config_name: olo
    data_files: data/olo/train.parquet
  - config_name: om
    data_files: data/om/train.parquet
  - config_name: or
    data_files: data/or/train.parquet
  - config_name: os
    data_files: data/os/train.parquet
  - config_name: pa
    data_files: data/pa/train.parquet
  - config_name: pag
    data_files: data/pag/train.parquet
  - config_name: pam
    data_files: data/pam/train.parquet
  - config_name: pap
    data_files: data/pap/train.parquet
  - config_name: pcd
    data_files: data/pcd/train.parquet
  - config_name: pcm
    data_files: data/pcm/train.parquet
  - config_name: pdc
    data_files: data/pdc/train.parquet
  - config_name: pfl
    data_files: data/pfl/train.parquet
  - config_name: pi
    data_files: data/pi/train.parquet
  - config_name: pl
    data_files: data/pl/train.parquet
  - config_name: pms
    data_files: data/pms/train.parquet
  - config_name: pnb
    data_files: data/pnb/train.parquet
  - config_name: pnt
    data_files: data/pnt/train.parquet
  - config_name: ps
    data_files: data/ps/train.parquet
  - config_name: pt
    data_files: data/pt/train.parquet
  - config_name: pwn
    data_files: data/pwn/train.parquet
  - config_name: qu
    data_files: data/qu/train.parquet
  - config_name: rki
    data_files: data/rki/train.parquet
  - config_name: rm
    data_files: data/rm/train.parquet
  - config_name: rmy
    data_files: data/rmy/train.parquet
  - config_name: rn
    data_files: data/rn/train.parquet
  - config_name: ro
    data_files: data/ro/train.parquet
  - config_name: rsk
    data_files: data/rsk/train.parquet
  - config_name: ru
    data_files: data/ru/train.parquet
  - config_name: rue
    data_files: data/rue/train.parquet
  - config_name: rw
    data_files: data/rw/train.parquet
  - config_name: sa
    data_files: data/sa/train.parquet
  - config_name: sah
    data_files: data/sah/train.parquet
  - config_name: sat
    data_files: data/sat/train.parquet
  - config_name: sc
    data_files: data/sc/train.parquet
  - config_name: scn
    data_files: data/scn/train.parquet
  - config_name: sco
    data_files: data/sco/train.parquet
  - config_name: sd
    data_files: data/sd/train.parquet
  - config_name: se
    data_files: data/se/train.parquet
  - config_name: sg
    data_files: data/sg/train.parquet
  - config_name: sh
    data_files: data/sh/train.parquet
  - config_name: shi
    data_files: data/shi/train.parquet
  - config_name: shn
    data_files: data/shn/train.parquet
  - config_name: si
    data_files: data/si/train.parquet
  - config_name: simple
    data_files: data/simple/train.parquet
  - config_name: sk
    data_files: data/sk/train.parquet
  - config_name: sl
    data_files: data/sl/train.parquet
  - config_name: sm
    data_files: data/sm/train.parquet
  - config_name: smn
    data_files: data/smn/train.parquet
  - config_name: sn
    data_files: data/sn/train.parquet
  - config_name: so
    data_files: data/so/train.parquet
  - config_name: sq
    data_files: data/sq/train.parquet
  - config_name: sr
    data_files: data/sr/train.parquet
  - config_name: srn
    data_files: data/srn/train.parquet
  - config_name: ss
    data_files: data/ss/train.parquet
  - config_name: st
    data_files: data/st/train.parquet
  - config_name: stq
    data_files: data/stq/train.parquet
  - config_name: su
    data_files: data/su/train.parquet
  - config_name: sv
    data_files: data/sv/train.parquet
  - config_name: sw
    data_files: data/sw/train.parquet
  - config_name: syl
    data_files: data/syl/train.parquet
  - config_name: szl
    data_files: data/szl/train.parquet
  - config_name: szy
    data_files: data/szy/train.parquet
  - config_name: ta
    data_files: data/ta/train.parquet
  - config_name: tay
    data_files: data/tay/train.parquet
  - config_name: tcy
    data_files: data/tcy/train.parquet
  - config_name: tdd
    data_files: data/tdd/train.parquet
  - config_name: te
    data_files: data/te/train.parquet
  - config_name: tet
    data_files: data/tet/train.parquet
  - config_name: tg
    data_files: data/tg/train.parquet
  - config_name: th
    data_files: data/th/train.parquet
  - config_name: ti
    data_files: data/ti/train.parquet
  - config_name: tig
    data_files: data/tig/train.parquet
  - config_name: tk
    data_files: data/tk/train.parquet
  - config_name: tl
    data_files: data/tl/train.parquet
  - config_name: tly
    data_files: data/tly/train.parquet
  - config_name: tn
    data_files: data/tn/train.parquet
  - config_name: to
    data_files: data/to/train.parquet
  - config_name: tok
    data_files: data/tok/train.parquet
  - config_name: tpi
    data_files: data/tpi/train.parquet
  - config_name: tr
    data_files: data/tr/train.parquet
  - config_name: trv
    data_files: data/trv/train.parquet
  - config_name: ts
    data_files: data/ts/train.parquet
  - config_name: tt
    data_files: data/tt/train.parquet
  - config_name: tum
    data_files: data/tum/train.parquet
  - config_name: tw
    data_files: data/tw/train.parquet
  - config_name: ty
    data_files: data/ty/train.parquet
  - config_name: tyv
    data_files: data/tyv/train.parquet
  - config_name: udm
    data_files: data/udm/train.parquet
  - config_name: ug
    data_files: data/ug/train.parquet
  - config_name: uk
    data_files: data/uk/train.parquet
  - config_name: ur
    data_files: data/ur/train.parquet
  - config_name: uz
    data_files: data/uz/train.parquet
  - config_name: ve
    data_files: data/ve/train.parquet
  - config_name: vec
    data_files: data/vec/train.parquet
  - config_name: vep
    data_files: data/vep/train.parquet
  - config_name: vi
    data_files: data/vi/train.parquet
  - config_name: vls
    data_files: data/vls/train.parquet
  - config_name: vo
    data_files: data/vo/train.parquet
  - config_name: wa
    data_files: data/wa/train.parquet
  - config_name: wo
    data_files: data/wo/train.parquet
  - config_name: wuu
    data_files: data/wuu/train.parquet
  - config_name: xal
    data_files: data/xal/train.parquet
  - config_name: xh
    data_files: data/xh/train.parquet
  - config_name: xmf
    data_files: data/xmf/train.parquet
  - config_name: yi
    data_files: data/yi/train.parquet
  - config_name: yo
    data_files: data/yo/train.parquet
  - config_name: za
    data_files: data/za/train.parquet
  - config_name: zea
    data_files: data/zea/train.parquet
  - config_name: zgh
    data_files: data/zgh/train.parquet
  - config_name: zh
    data_files: data/zh/train.parquet
  - config_name: zu
    data_files: data/zu/train.parquet
---

# Wikidata Title and Description

Wikidata entity titles and short descriptions for all 324 Wikipedia language editions,
extracted from the [Wikimedia Analytics wmf.wikidata_entity](https://wikitech.wikimedia.org/wiki/Analytics/Data_Lake/Edits/Wikidata_entity)
table. Each row links a Wikidata QID to the title and description as they
appear in a specific language edition of Wikipedia.

## Dataset Details

| Field | Value |
|---|---|
| Source | wmf.wikidata_entity (Wikidata + Wikipedia sitelinks) |
| Snapshot | 2026-03-30 |
| Languages | 324 |
| Total titles | 88,292,409 |
| Titles with description | 59,572,215 (67.5%) |
| License | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |

## Schema

| Column | Type | Description |
|---|---|---|
| `qid` | string | Wikidata entity ID, e.g. `Q42` |
| `lang` | string | BCP-47 language code, e.g. `en`, `ml`, `simple` |
| `title` | string | Wikipedia article title in that language |
| `description` | string | Short Wikidata description in that language (may be null) |
| `snapshot` | string | Wikidata dump snapshot date, e.g. `2026-03-30` |

## Usage

Load all languages:

```python
from datasets import load_dataset

ds = load_dataset("wikimedia/wikidata-title-desc")
```

Load a specific language:

```python
ds = load_dataset("wikimedia/wikidata-title-desc", "ml")   # Malayalam
ds = load_dataset("wikimedia/wikidata-title-desc", "en")   # English
ds = load_dataset("wikimedia/wikidata-title-desc", "simple")  # Simple English
```

Filter to rows that have a description:

```python
ds = load_dataset("wikimedia/wikidata-title-desc", "en")
ds_with_desc = ds.filter(lambda x: x["description"])
```

## Language Coverage

| lang | titles | with description | coverage % |
|------|-------:|-----------------:|-----------:|
| en | 20,455,894 | 19,605,584 | 95.8% |
| de | 3,762,818 | 3,499,833 | 93.0% |
| fr | 3,464,083 | 2,891,433 | 83.5% |
| sv | 3,046,107 | 1,812,981 | 59.5% |
| ru | 2,932,290 | 1,861,334 | 63.5% |
| es | 2,616,349 | 1,945,140 | 74.3% |
| it | 2,494,177 | 1,962,166 | 78.7% |
| ar | 2,440,054 | 2,064,603 | 84.6% |
| nl | 2,396,597 | 2,191,681 | 91.4% |
| zh | 2,142,635 | 1,130,871 | 52.8% |
| pl | 2,031,054 | 1,130,638 | 55.7% |
| uk | 1,878,743 | 1,336,790 | 71.2% |
| fa | 1,873,639 | 1,184,963 | 63.2% |
| ja | 1,851,700 | 1,101,244 | 59.5% |
| vi | 1,678,784 | 843,972 | 50.3% |
| pt | 1,671,063 | 1,000,568 | 59.9% |
| arz | 1,656,660 | 463,268 | 28.0% |
| ko | 1,177,597 | 697,372 | 59.2% |
| tr | 1,104,062 | 684,695 | 62.0% |
| ur | 986,702 | 629,209 | 63.8% |
| id | 971,329 | 599,232 | 61.7% |
| ca | 945,214 | 599,162 | 63.4% |
| sr | 926,851 | 340,140 | 36.7% |
| nb | 897,939 | 2,016 | 0.2% |
| ce | 877,790 | 61,920 | 7.1% |
| cs | 850,083 | 704,304 | 82.9% |
| ro | 746,894 | 512,778 | 68.7% |
| fi | 730,168 | 432,297 | 59.2% |
| hu | 669,948 | 575,865 | 86.0% |
| tt | 627,461 | 86,563 | 13.8% |
| eu | 586,153 | 219,647 | 37.5% |
| sh | 534,236 | 103,544 | 19.4% |
| he | 527,814 | 419,470 | 79.5% |
| eo | 513,773 | 336,701 | 65.5% |
| ms | 494,362 | 118,832 | 24.0% |
| hy | 480,443 | 268,195 | 55.8% |
| bn | 471,127 | 388,308 | 82.4% |
| bg | 409,379 | 225,708 | 55.1% |
| da | 407,869 | 226,980 | 55.7% |
| simple | 401,299 | 2,408 | 0.6% |
| be | 399,183 | 230,167 | 57.7% |
| uz | 380,176 | 64,725 | 17.0% |
| azb | 376,757 | 1,189 | 0.3% |
| az | 364,317 | 154,294 | 42.4% |
| sk | 363,912 | 243,081 | 66.8% |
| cy | 363,603 | 278,357 | 76.6% |
| el | 359,821 | 225,624 | 62.7% |
| gl | 323,588 | 234,987 | 72.6% |
| th | 302,687 | 150,979 | 49.9% |
| et | 294,685 | 115,400 | 39.2% |
| sl | 288,712 | 164,211 | 56.9% |
| kk | 287,130 | 10,434 | 3.6% |
| ka | 281,606 | 117,261 | 41.6% |
| ml | 273,444 | 150,714 | 55.1% |
| lt | 265,275 | 33,203 | 12.5% |
| nn | 263,592 | 128,100 | 48.6% |
| hr | 259,496 | 102,047 | 39.3% |
| mk | 256,519 | 137,201 | 53.5% |
| min | 231,997 | 52,069 | 22.4% |
| ta | 218,133 | 118,526 | 54.3% |
| hi | 215,785 | 115,503 | 53.5% |
| af | 198,138 | 113,827 | 57.4% |
| lv | 188,539 | 104,571 | 55.5% |
| la | 188,116 | 75,721 | 40.3% |
| lld | 181,962 | 93,251 | 51.2% |
| bs | 179,046 | 115,021 | 64.2% |
| ast | 173,815 | 117,307 | 67.5% |
| tg | 150,043 | 36,750 | 24.5% |
| sq | 141,179 | 77,700 | 55.0% |
| te | 140,845 | 65,863 | 46.8% |
| ckb | 133,072 | 61,131 | 45.9% |
| ku | 133,066 | 95,935 | 72.1% |
| sw | 124,084 | 34,795 | 28.0% |
| oc | 116,568 | 60,545 | 51.9% |
| br | 114,715 | 54,852 | 47.8% |
| ba | 113,241 | 58,644 | 51.8% |
| fy | 112,855 | 60,560 | 53.7% |
| mg | 105,642 | 1,613 | 1.5% |
| an | 104,952 | 49,472 | 47.1% |
| mr | 101,637 | 38,866 | 38.2% |
| jv | 100,608 | 48,449 | 48.2% |
| my | 100,041 | 30,225 | 30.2% |
| lb | 98,560 | 81,448 | 82.6% |
| ha | 96,670 | 9,177 | 9.5% |
| nds | 92,557 | 63,061 | 68.1% |
| lmo | 90,922 | 10,853 | 11.9% |
| tl | 90,461 | 34,439 | 38.1% |
| sco | 88,462 | 56,707 | 64.1% |
| cv | 87,933 | 6,094 | 6.9% |
| pnb | 87,169 | 2,121 | 2.4% |
| mn | 85,210 | 55,469 | 65.1% |
| ky | 84,055 | 10,947 | 13.0% |
| io | 82,816 | 8,544 | 10.3% |
| is | 81,810 | 32,279 | 39.5% |
| ga | 78,226 | 40,934 | 52.3% |
| vec | 78,203 | 40,038 | 51.2% |
| ht | 77,867 | 6,338 | 8.1% |
| new | 77,598 | 1,631 | 2.1% |
| pms | 76,862 | 363 | 0.5% |
| su | 74,132 | 31,444 | 42.4% |
| pa | 73,764 | 15,713 | 21.3% |
| mzn | 72,158 | 2,290 | 3.2% |
| szl | 66,669 | 1,226 | 1.8% |
| ban | 58,416 | 1,600 | 2.7% |
| wuu | 56,846 | 4,891 | 8.6% |
| vo | 55,657 | 3,725 | 6.7% |
| ig | 54,004 | 17,677 | 32.7% |
| diq | 49,660 | 7,671 | 15.4% |
| si | 48,913 | 18,800 | 38.4% |
| ary | 48,245 | 25,161 | 52.2% |
| glk | 47,264 | 368 | 0.8% |
| ne | 43,422 | 18,499 | 42.6% |
| als | 42,586 | 136 | 0.3% |
| yo | 42,217 | 9,628 | 22.8% |
| kn | 42,126 | 8,586 | 20.4% |
| bar | 39,723 | 17,041 | 42.9% |
| os | 37,651 | 1,482 | 3.9% |
| gu | 36,467 | 28,288 | 77.6% |
| sd | 35,451 | 14,915 | 42.1% |
| ia | 34,887 | 14,331 | 41.1% |
| crh | 33,537 | 287 | 0.9% |
| ilo | 33,427 | 31,723 | 94.9% |
| bpy | 33,236 | 7,469 | 22.5% |
| qu | 33,137 | 2,076 | 6.3% |
| as | 31,943 | 17,179 | 53.8% |
| gv | 31,379 | 26,119 | 83.2% |
| or | 30,671 | 22,022 | 71.8% |
| xmf | 30,297 | 2,733 | 9.0% |
| scn | 29,742 | 12,472 | 41.9% |
| avk | 28,236 | 1,225 | 4.3% |
| ab | 28,009 | 1,867 | 6.7% |
| frr | 27,690 | 9,216 | 33.3% |
| ps | 27,255 | 7,229 | 26.5% |
| cdo | 26,761 | 1,924 | 7.2% |
| shn | 26,284 | 6,724 | 25.6% |
| bh | 25,564 | 5 | 0.0% |
| sah | 25,277 | 2,391 | 9.5% |
| smn | 24,736 | 3,651 | 14.8% |
| hsb | 24,708 | 15,017 | 60.8% |
| nv | 24,325 | 10 | 0.0% |
| bcl | 24,263 | 2,713 | 11.2% |
| fo | 23,238 | 9,718 | 41.8% |
| sa | 22,350 | 10,902 | 48.8% |
| ff | 21,056 | 659 | 3.1% |
| yi | 20,400 | 7,719 | 37.8% |
| mai | 19,579 | 963 | 4.9% |
| li | 19,129 | 5,007 | 26.2% |
| gd | 18,733 | 3,416 | 18.2% |
| hyw | 18,231 | 1,614 | 8.9% |
| gor | 17,713 | 537 | 3.0% |
| sat | 17,447 | 7,644 | 43.8% |
| am | 17,366 | 1,971 | 11.3% |
| nap | 17,229 | 9,280 | 53.9% |
| mhr | 16,957 | 2,853 | 16.8% |
| km | 16,685 | 3,007 | 18.0% |
| bug | 16,517 | 709 | 4.3% |
| gan | 15,911 | 1,173 | 7.4% |
| vep | 15,503 | 577 | 3.7% |
| eml | 15,308 | 996 | 6.5% |
| lij | 15,129 | 11,680 | 77.2% |
| hif | 15,006 | 2,162 | 14.4% |
| ie | 14,746 | 334 | 2.3% |
| rue | 14,559 | 2,176 | 14.9% |
| ace | 14,525 | 8,852 | 60.9% |
| se | 14,469 | 8,111 | 56.1% |
| wa | 14,333 | 3,048 | 21.3% |
| mt | 14,127 | 5,386 | 38.1% |
| zu | 14,026 | 2,610 | 18.6% |
| bo | 13,929 | 285 | 2.0% |
| bjn | 13,920 | 3,703 | 26.6% |
| pam | 13,655 | 3,838 | 28.1% |
| mdf | 13,365 | 1,567 | 11.7% |
| myv | 13,167 | 1,215 | 9.2% |
| so | 13,035 | 3,674 | 28.2% |
| mrj | 12,519 | 55 | 0.4% |
| dag | 12,478 | 5,000 | 40.1% |
| zgh | 12,284 | 1,000 | 8.1% |
| vls | 12,056 | 423 | 3.5% |
| tly | 11,851 | 143 | 1.2% |
| tk | 11,114 | 1,394 | 12.5% |
| shi | 10,999 | 266 | 2.4% |
| co | 10,616 | 1,464 | 13.8% |
| ug | 10,436 | 508 | 4.9% |
| kw | 10,224 | 3,167 | 31.0% |
| sc | 10,155 | 1,235 | 12.2% |
| ks | 9,997 | 2,750 | 27.5% |
| kab | 9,473 | 367 | 3.9% |
| mi | 9,461 | 1,654 | 17.5% |
| nso | 9,418 | 408 | 4.3% |
| kv | 9,133 | 321 | 3.5% |
| sn | 8,977 | 200 | 2.2% |
| frp | 8,884 | 1,510 | 17.0% |
| zea | 8,721 | 1,727 | 19.8% |
| rw | 8,715 | 380 | 4.4% |
| udm | 8,671 | 277 | 3.2% |
| lo | 8,236 | 1,468 | 17.8% |
| dsb | 8,190 | 1,735 | 21.2% |
| mwl | 7,921 | 580 | 7.3% |
| gn | 7,894 | 2,481 | 31.4% |
| mni | 7,834 | 645 | 8.2% |
| av | 7,733 | 2,014 | 26.0% |
| lez | 7,553 | 160 | 2.1% |
| tum | 7,508 | 601 | 8.0% |
| pcd | 7,254 | 579 | 8.0% |
| mad | 7,073 | 564 | 8.0% |
| olo | 6,723 | 89 | 1.3% |
| pap | 6,702 | 3,541 | 52.8% |
| ln | 6,564 | 606 | 9.2% |
| csb | 6,508 | 731 | 11.2% |
| ay | 6,457 | 502 | 7.8% |
| lg | 6,367 | 2,363 | 37.1% |
| fur | 6,298 | 730 | 11.6% |
| krc | 6,255 | 338 | 5.4% |
| nrm | 6,051 | 152 | 2.5% |
| lfn | 6,026 | 421 | 7.0% |
| lad | 5,984 | 885 | 14.8% |
| bxr | 5,843 | 962 | 16.5% |
| gpe | 5,837 | 5,239 | 89.8% |
| nah | 5,577 | 44 | 0.8% |
| tyv | 5,567 | 85 | 1.5% |
| dv | 5,522 | 984 | 17.8% |
| inh | 5,403 | 187 | 3.5% |
| rm | 5,283 | 350 | 6.6% |
| stq | 5,247 | 1,370 | 26.1% |
| ext | 5,183 | 541 | 10.4% |
| dty | 5,025 | 548 | 10.9% |
| gom | 5,015 | 80 | 1.6% |
| koi | 4,701 | 320 | 6.8% |
| gag | 4,461 | 694 | 15.6% |
| iba | 4,409 | 199 | 4.5% |
| tw | 4,316 | 941 | 21.8% |
| ksh | 4,185 | 372 | 8.9% |
| kbd | 4,154 | 52 | 1.3% |
| tok | 4,074 | 855 | 21.0% |
| pfl | 4,064 | 63 | 1.6% |
| dtp | 4,059 | 164 | 4.0% |
| bew | 4,033 | 444 | 11.0% |
| haw | 3,974 | 264 | 6.6% |
| tn | 3,918 | 625 | 16.0% |
| tcy | 3,789 | 319 | 8.4% |
| kge | 3,788 | 183 | 4.8% |
| za | 3,705 | 190 | 5.1% |
| alt | 3,386 | 103 | 3.0% |
| nov | 3,376 | 291 | 8.6% |
| xh | 3,342 | 66 | 2.0% |
| pag | 3,326 | 1,862 | 56.0% |
| blk | 3,312 | 104 | 3.1% |
| pdc | 3,241 | 44 | 1.4% |
| awa | 3,176 | 151 | 4.8% |
| szy | 2,992 | 45 | 1.5% |
| wo | 2,867 | 124 | 4.3% |
| mnw | 2,789 | 100 | 3.6% |
| ki | 2,756 | 162 | 5.9% |
| fj | 2,750 | 214 | 7.8% |
| dga | 2,597 | 1,765 | 68.0% |
| om | 2,589 | 296 | 11.4% |
| cu | 2,562 | 484 | 18.9% |
| arc | 2,541 | 255 | 10.0% |
| to | 2,470 | 121 | 4.9% |
| tpi | 2,442 | 532 | 21.8% |
| st | 2,379 | 206 | 8.7% |
| kcg | 2,331 | 1,455 | 62.4% |
| jbo | 2,278 | 54 | 2.4% |
| kbp | 2,276 | 44 | 1.9% |
| fon | 2,250 | 1,238 | 55.0% |
| jam | 2,187 | 30 | 1.4% |
| xal | 2,181 | 179 | 8.2% |
| kg | 2,172 | 325 | 15.0% |
| knc | 2,112 | 170 | 8.0% |
| tay | 2,102 | 40 | 1.9% |
| guw | 2,079 | 77 | 3.7% |
| ltg | 2,071 | 86 | 4.2% |
| tet | 2,071 | 68 | 3.3% |
| anp | 2,004 | 86 | 4.3% |
| bi | 1,994 | 169 | 8.5% |
| ny | 1,993 | 112 | 5.6% |
| atj | 1,980 | 843 | 42.6% |
| ee | 1,954 | 244 | 12.5% |
| nia | 1,920 | 136 | 7.1% |
| pcm | 1,907 | 318 | 16.7% |
| syl | 1,882 | 309 | 16.4% |
| nqo | 1,787 | 1,049 | 58.7% |
| lbe | 1,718 | 98 | 5.7% |
| rki | 1,709 | 59 | 3.5% |
| ty | 1,686 | 81 | 4.8% |
| ts | 1,670 | 267 | 16.0% |
| got | 1,659 | 112 | 6.8% |
| ss | 1,626 | 22 | 1.4% |
| sm | 1,616 | 14 | 0.9% |
| mos | 1,587 | 815 | 51.4% |
| bbc | 1,573 | 87 | 5.5% |
| fat | 1,567 | 150 | 9.6% |
| chr | 1,562 | 175 | 11.2% |
| bm | 1,560 | 143 | 9.2% |
| srn | 1,535 | 329 | 21.4% |
| ami | 1,472 | 12 | 0.8% |
| rsk | 1,416 | 132 | 9.3% |
| rn | 1,402 | 49 | 3.5% |
| btm | 1,379 | 43 | 3.1% |
| ti | 1,323 | 119 | 9.0% |
| kus | 1,250 | 724 | 57.9% |
| pnt | 1,223 | 153 | 12.5% |
| gur | 1,221 | 722 | 59.1% |
| rmy | 1,190 | 394 | 33.1% |
| chy | 1,166 | 97 | 8.3% |
| ve | 1,162 | 105 | 9.0% |
| ik | 1,157 | 2 | 0.2% |
| igl | 1,123 | 52 | 4.6% |
| trv | 1,103 | 21 | 1.9% |
| dz | 1,015 | 24 | 2.4% |
| ady | 982 | 28 | 2.9% |
| tdd | 975 | 23 | 2.4% |
| ch | 936 | 205 | 21.9% |
| iu | 742 | 7 | 0.9% |
| sg | 729 | 74 | 10.2% |
| din | 717 | 20 | 2.8% |
| guc | 662 | 58 | 8.8% |
| pi | 658 | 112 | 17.0% |
| kaj | 502 | 14 | 2.8% |
| bdr | 477 | 35 | 7.3% |
| pwn | 461 | 85 | 18.4% |
| ann | 454 | 104 | 22.9% |
| nr | 322 | 40 | 12.4% |
| tig | 72 | 5 | 6.9% |
| **total** | **88,292,409** | **59,572,215** | **67.5%** |


## Notes

- Descriptions come from Wikidata and may be absent (`null` or empty string) for many articles,
  especially in smaller language editions.
- The `simple` config corresponds to Simple English Wikipedia (`simplewiki`), not a standard
  BCP-47 code.
- Rows with the same `qid` across different `lang` configs refer to the same Wikidata entity.

## Versioning

Each snapshot is tagged in the repository (e.g. `snapshot-2026-03-30`). To load data
from a specific snapshot:

```python
ds = load_dataset("wikimedia/wikidata-title-desc", revision="snapshot-2026-03-30")
```

## Source & Attribution

Data is derived from [Wikidata](https://www.wikidata.org/) and
[Wikipedia](https://www.wikipedia.org/), both licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Extracted using the [Wikimedia Analytics Data Lake](https://wikitech.wikimedia.org/wiki/Analytics/Data_Lake).