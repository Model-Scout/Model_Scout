---
viewer: true
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- abq
- ab
- af
- akk
- aqz
- sq
- gsw
- am
- grc
- hbo
- apu
- ar
- hy
- as
- aii
- az
- bm
- eu
- bar
- bej
- be
- bn
- bho
- sab
- bor
- brh
- br
- bg
- bxr
- yue
- cpg
- ca
- ceb
- ckb
- zh
- ctn
- ckt
- xcl
- lzh
- cop
- hr
- cs
- da
- nl
- egy
- en
- myv
- eo
- et
- fo
- fi
- fr
- qfn
- gl
- ka
- de
- aln
- gor
- got
- el
- gub
- gn
- gu
- gwi
- ht
- ha
- he
- azz
- hi
- hit
- hu
- is
- arh
- id
- ga
- it
- ja
- jv
- urb
- kbc
- xnr
- krl
- arr
- kk
- naq
- quc
- koi
- kpv
- ko
- ky
- ltg
- la
- lv
- lij
- lt
- olo
- nds
- lb
- mk
- jaa
- qaf
- mpu
- ml
- mt
- gv
- mr
- gun
- axm
- frm
- mdf
- myu
- nmf
- pcm
- nap
- yrk
- ne
- yrl
- sme
- kmr
- gya
- 'no'
- oc
- or
- cu
- orv
- ang
- fro
- oge
- sga
- pro
- otk
- ota
- ps
- pad
- fa
- pay
- xpg
- pl
- qpm
- pt
- pa
- ro
- ru
- ruc
- sa
- gd
- sr
- wuu
- scn
- sd
- si
- sms
- sk
- sl
- ajp
- sdh
- es
- ssp
- sv
- swl
- tl
- ta
- tt
- eme
- te
- qte
- th
- tn
- tpn
- tr
- qti
- qtd
- uk
- xum
- hsb
- ur
- ug
- uz
- vep
- vi
- wbp
- cy
- hyw
- nhi
- wo
- xav
- sjo
- sah
- yi
- yo
- ess
- say
- zza
license: other
multilinguality:
- multilingual
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- parsing
- part-of-speech
- lemmatization
paperswithcode_id: universal-dependencies
pretty_name: Universal Dependencies Treebank
tags:
- text
- dependency-parsing
- part-of-speech-tagging

configs:
- config_name: abq_atb
  data_files:
  - split: test
    path: parquet/abq_atb/test.parquet
- config_name: ab_abnc
  data_files:
  - split: test
    path: parquet/ab_abnc/test.parquet
- config_name: af_afribooms
  data_files:
  - split: dev
    path: parquet/af_afribooms/dev.parquet
  - split: test
    path: parquet/af_afribooms/test.parquet
  - split: train
    path: parquet/af_afribooms/train.parquet
- config_name: akk_pisandub
  data_files:
  - split: test
    path: parquet/akk_pisandub/test.parquet
- config_name: akk_riao
  data_files:
  - split: test
    path: parquet/akk_riao/test.parquet
- config_name: aqz_tudet
  data_files:
  - split: test
    path: parquet/aqz_tudet/test.parquet
- config_name: sq_staf
  data_files:
  - split: dev
    path: parquet/sq_staf/dev.parquet
  - split: test
    path: parquet/sq_staf/test.parquet
  - split: train
    path: parquet/sq_staf/train.parquet
- config_name: sq_tsa
  data_files:
  - split: test
    path: parquet/sq_tsa/test.parquet
- config_name: gsw_divital
  data_files:
  - split: test
    path: parquet/gsw_divital/test.parquet
- config_name: gsw_uzh
  data_files:
  - split: test
    path: parquet/gsw_uzh/test.parquet
- config_name: am_att
  data_files:
  - split: test
    path: parquet/am_att/test.parquet
- config_name: grc_perseus
  data_files:
  - split: dev
    path: parquet/grc_perseus/dev.parquet
  - split: test
    path: parquet/grc_perseus/test.parquet
  - split: train
    path: parquet/grc_perseus/train.parquet
- config_name: grc_proiel
  data_files:
  - split: dev
    path: parquet/grc_proiel/dev.parquet
  - split: test
    path: parquet/grc_proiel/test.parquet
  - split: train
    path: parquet/grc_proiel/train.parquet
- config_name: grc_ptnk
  data_files:
  - split: dev
    path: parquet/grc_ptnk/dev.parquet
  - split: test
    path: parquet/grc_ptnk/test.parquet
  - split: train
    path: parquet/grc_ptnk/train.parquet
- config_name: hbo_ptnk
  data_files:
  - split: dev
    path: parquet/hbo_ptnk/dev.parquet
  - split: test
    path: parquet/hbo_ptnk/test.parquet
  - split: train
    path: parquet/hbo_ptnk/train.parquet
- config_name: apu_ufpa
  data_files:
  - split: test
    path: parquet/apu_ufpa/test.parquet
- config_name: ar_padt
  data_files:
  - split: dev
    path: parquet/ar_padt/dev.parquet
  - split: test
    path: parquet/ar_padt/test.parquet
  - split: train
    path: parquet/ar_padt/train.parquet
- config_name: ar_pud
  data_files:
  - split: test
    path: parquet/ar_pud/test.parquet
- config_name: hy_armtdp
  data_files:
  - split: dev
    path: parquet/hy_armtdp/dev.parquet
  - split: test
    path: parquet/hy_armtdp/test.parquet
  - split: train
    path: parquet/hy_armtdp/train.parquet
- config_name: hy_bsut
  data_files:
  - split: dev
    path: parquet/hy_bsut/dev.parquet
  - split: test
    path: parquet/hy_bsut/test.parquet
  - split: train
    path: parquet/hy_bsut/train.parquet
- config_name: as_aiw
  data_files:
  - split: dev
    path: parquet/as_aiw/dev.parquet
  - split: test
    path: parquet/as_aiw/test.parquet
  - split: train
    path: parquet/as_aiw/train.parquet
- config_name: aii_as
  data_files:
  - split: test
    path: parquet/aii_as/test.parquet
- config_name: az_tuecl
  data_files:
  - split: test
    path: parquet/az_tuecl/test.parquet
- config_name: bm_crb
  data_files:
  - split: test
    path: parquet/bm_crb/test.parquet
- config_name: eu_bdt
  data_files:
  - split: dev
    path: parquet/eu_bdt/dev.parquet
  - split: test
    path: parquet/eu_bdt/test.parquet
  - split: train
    path: parquet/eu_bdt/train.parquet
- config_name: bar_maibaam
  data_files:
  - split: test
    path: parquet/bar_maibaam/test.parquet
- config_name: bej_autogramm
  data_files:
  - split: test
    path: parquet/bej_autogramm/test.parquet
- config_name: be_hse
  data_files:
  - split: dev
    path: parquet/be_hse/dev.parquet
  - split: test
    path: parquet/be_hse/test.parquet
  - split: train
    path: parquet/be_hse/train.parquet
- config_name: bn_bru
  data_files:
  - split: test
    path: parquet/bn_bru/test.parquet
- config_name: bho_bhtb
  data_files:
  - split: test
    path: parquet/bho_bhtb/test.parquet
- config_name: sab_chibergis
  data_files:
  - split: test
    path: parquet/sab_chibergis/test.parquet
- config_name: bor_bdt
  data_files:
  - split: dev
    path: parquet/bor_bdt/dev.parquet
  - split: test
    path: parquet/bor_bdt/test.parquet
  - split: train
    path: parquet/bor_bdt/train.parquet
- config_name: brh_kholum
  data_files:
  - split: test
    path: parquet/brh_kholum/test.parquet
- config_name: br_keb
  data_files:
  - split: test
    path: parquet/br_keb/test.parquet
- config_name: bg_btb
  data_files:
  - split: dev
    path: parquet/bg_btb/dev.parquet
  - split: test
    path: parquet/bg_btb/test.parquet
  - split: train
    path: parquet/bg_btb/train.parquet
- config_name: bxr_bdt
  data_files:
  - split: test
    path: parquet/bxr_bdt/test.parquet
  - split: train
    path: parquet/bxr_bdt/train.parquet
- config_name: yue_hk
  data_files:
  - split: test
    path: parquet/yue_hk/test.parquet
- config_name: cpg_amgic
  data_files:
  - split: test
    path: parquet/cpg_amgic/test.parquet
- config_name: cpg_tuecl
  data_files:
  - split: test
    path: parquet/cpg_tuecl/test.parquet
- config_name: ca_ancora
  data_files:
  - split: dev
    path: parquet/ca_ancora/dev.parquet
  - split: test
    path: parquet/ca_ancora/test.parquet
  - split: train
    path: parquet/ca_ancora/train.parquet
- config_name: ceb_gja
  data_files:
  - split: test
    path: parquet/ceb_gja/test.parquet
- config_name: ckb_mukri
  data_files:
  - split: dev
    path: parquet/ckb_mukri/dev.parquet
  - split: test
    path: parquet/ckb_mukri/test.parquet
  - split: train
    path: parquet/ckb_mukri/train.parquet
- config_name: zh_beginner
  data_files:
  - split: test
    path: parquet/zh_beginner/test.parquet
- config_name: zh_cfl
  data_files:
  - split: test
    path: parquet/zh_cfl/test.parquet
- config_name: zh_gsd
  data_files:
  - split: dev
    path: parquet/zh_gsd/dev.parquet
  - split: test
    path: parquet/zh_gsd/test.parquet
  - split: train
    path: parquet/zh_gsd/train.parquet
- config_name: zh_gsdsimp
  data_files:
  - split: dev
    path: parquet/zh_gsdsimp/dev.parquet
  - split: test
    path: parquet/zh_gsdsimp/test.parquet
  - split: train
    path: parquet/zh_gsdsimp/train.parquet
- config_name: zh_hk
  data_files:
  - split: test
    path: parquet/zh_hk/test.parquet
- config_name: zh_patentchar
  data_files:
  - split: test
    path: parquet/zh_patentchar/test.parquet
- config_name: zh_pud
  data_files:
  - split: test
    path: parquet/zh_pud/test.parquet
- config_name: ctn_ctntb
  data_files:
  - split: test
    path: parquet/ctn_ctntb/test.parquet
- config_name: ckt_hse
  data_files:
  - split: test
    path: parquet/ckt_hse/test.parquet
- config_name: xcl_caval
  data_files:
  - split: dev
    path: parquet/xcl_caval/dev.parquet
  - split: test
    path: parquet/xcl_caval/test.parquet
  - split: train
    path: parquet/xcl_caval/train.parquet
- config_name: lzh_kyoto
  data_files:
  - split: dev
    path: parquet/lzh_kyoto/dev.parquet
  - split: test
    path: parquet/lzh_kyoto/test.parquet
  - split: train
    path: parquet/lzh_kyoto/train.parquet
- config_name: lzh_tuecl
  data_files:
  - split: test
    path: parquet/lzh_tuecl/test.parquet
- config_name: cop_bohairic
  data_files:
  - split: dev
    path: parquet/cop_bohairic/dev.parquet
  - split: test
    path: parquet/cop_bohairic/test.parquet
  - split: train
    path: parquet/cop_bohairic/train.parquet
- config_name: cop_scriptorium
  data_files:
  - split: dev
    path: parquet/cop_scriptorium/dev.parquet
  - split: test
    path: parquet/cop_scriptorium/test.parquet
  - split: train
    path: parquet/cop_scriptorium/train.parquet
- config_name: hr_set
  data_files:
  - split: dev
    path: parquet/hr_set/dev.parquet
  - split: test
    path: parquet/hr_set/test.parquet
  - split: train
    path: parquet/hr_set/train.parquet
- config_name: cs_cac
  data_files:
  - split: dev
    path: parquet/cs_cac/dev.parquet
  - split: test
    path: parquet/cs_cac/test.parquet
  - split: train
    path: parquet/cs_cac/train.parquet
- config_name: cs_cltt
  data_files:
  - split: dev
    path: parquet/cs_cltt/dev.parquet
  - split: test
    path: parquet/cs_cltt/test.parquet
  - split: train
    path: parquet/cs_cltt/train.parquet
- config_name: cs_fictree
  data_files:
  - split: dev
    path: parquet/cs_fictree/dev.parquet
  - split: test
    path: parquet/cs_fictree/test.parquet
  - split: train
    path: parquet/cs_fictree/train.parquet
- config_name: cs_pdtc
  data_files:
  - split: dev
    path: parquet/cs_pdtc/dev.parquet
  - split: test
    path: parquet/cs_pdtc/test.parquet
  - split: train
    path: parquet/cs_pdtc/train.parquet
- config_name: cs_poetry
  data_files:
  - split: test
    path: parquet/cs_poetry/test.parquet
- config_name: cs_pud
  data_files:
  - split: test
    path: parquet/cs_pud/test.parquet
- config_name: da_ddt
  data_files:
  - split: dev
    path: parquet/da_ddt/dev.parquet
  - split: test
    path: parquet/da_ddt/test.parquet
  - split: train
    path: parquet/da_ddt/train.parquet
- config_name: nl_alpino
  data_files:
  - split: dev
    path: parquet/nl_alpino/dev.parquet
  - split: test
    path: parquet/nl_alpino/test.parquet
  - split: train
    path: parquet/nl_alpino/train.parquet
- config_name: nl_lassysmall
  data_files:
  - split: dev
    path: parquet/nl_lassysmall/dev.parquet
  - split: test
    path: parquet/nl_lassysmall/test.parquet
  - split: train
    path: parquet/nl_lassysmall/train.parquet
- config_name: egy_pc
  data_files:
  - split: dev
    path: parquet/egy_pc/dev.parquet
  - split: test
    path: parquet/egy_pc/test.parquet
  - split: train
    path: parquet/egy_pc/train.parquet
- config_name: en_atis
  data_files:
  - split: dev
    path: parquet/en_atis/dev.parquet
  - split: test
    path: parquet/en_atis/test.parquet
  - split: train
    path: parquet/en_atis/train.parquet
- config_name: en_childes
  data_files:
  - split: dev
    path: parquet/en_childes/dev.parquet
  - split: test
    path: parquet/en_childes/test.parquet
  - split: train
    path: parquet/en_childes/train.parquet
- config_name: en_ctetex
  data_files:
  - split: test
    path: parquet/en_ctetex/test.parquet
- config_name: en_eslspok
  data_files:
  - split: dev
    path: parquet/en_eslspok/dev.parquet
  - split: test
    path: parquet/en_eslspok/test.parquet
  - split: train
    path: parquet/en_eslspok/train.parquet
- config_name: en_ewt
  data_files:
  - split: dev
    path: parquet/en_ewt/dev.parquet
  - split: test
    path: parquet/en_ewt/test.parquet
  - split: train
    path: parquet/en_ewt/train.parquet
  default: true
- config_name: en_gentle
  data_files:
  - split: test
    path: parquet/en_gentle/test.parquet
- config_name: en_gum
  data_files:
  - split: dev
    path: parquet/en_gum/dev.parquet
  - split: test
    path: parquet/en_gum/test.parquet
  - split: train
    path: parquet/en_gum/train.parquet
- config_name: en_gumreddit
  data_files:
  - split: dev
    path: parquet/en_gumreddit/dev.parquet
  - split: test
    path: parquet/en_gumreddit/test.parquet
  - split: train
    path: parquet/en_gumreddit/train.parquet
- config_name: en_lines
  data_files:
  - split: dev
    path: parquet/en_lines/dev.parquet
  - split: test
    path: parquet/en_lines/test.parquet
  - split: train
    path: parquet/en_lines/train.parquet
- config_name: en_littleprince
  data_files:
  - split: test
    path: parquet/en_littleprince/test.parquet
- config_name: en_partut
  data_files:
  - split: dev
    path: parquet/en_partut/dev.parquet
  - split: test
    path: parquet/en_partut/test.parquet
  - split: train
    path: parquet/en_partut/train.parquet
- config_name: en_pronouns
  data_files:
  - split: test
    path: parquet/en_pronouns/test.parquet
- config_name: en_pud
  data_files:
  - split: test
    path: parquet/en_pud/test.parquet
- config_name: myv_jr
  data_files:
  - split: test
    path: parquet/myv_jr/test.parquet
  - split: train
    path: parquet/myv_jr/train.parquet
- config_name: eo_cairo
  data_files:
  - split: test
    path: parquet/eo_cairo/test.parquet
- config_name: eo_prago
  data_files:
  - split: test
    path: parquet/eo_prago/test.parquet
- config_name: et_edt
  data_files:
  - split: dev
    path: parquet/et_edt/dev.parquet
  - split: test
    path: parquet/et_edt/test.parquet
  - split: train
    path: parquet/et_edt/train.parquet
- config_name: et_ewt
  data_files:
  - split: dev
    path: parquet/et_ewt/dev.parquet
  - split: test
    path: parquet/et_ewt/test.parquet
  - split: train
    path: parquet/et_ewt/train.parquet
- config_name: fo_farpahc
  data_files:
  - split: dev
    path: parquet/fo_farpahc/dev.parquet
  - split: test
    path: parquet/fo_farpahc/test.parquet
  - split: train
    path: parquet/fo_farpahc/train.parquet
- config_name: fo_oft
  data_files:
  - split: test
    path: parquet/fo_oft/test.parquet
- config_name: fi_ftb
  data_files:
  - split: dev
    path: parquet/fi_ftb/dev.parquet
  - split: test
    path: parquet/fi_ftb/test.parquet
  - split: train
    path: parquet/fi_ftb/train.parquet
- config_name: fi_ood
  data_files:
  - split: test
    path: parquet/fi_ood/test.parquet
- config_name: fi_pud
  data_files:
  - split: test
    path: parquet/fi_pud/test.parquet
- config_name: fi_tdt
  data_files:
  - split: dev
    path: parquet/fi_tdt/dev.parquet
  - split: test
    path: parquet/fi_tdt/test.parquet
  - split: train
    path: parquet/fi_tdt/train.parquet
- config_name: fr_alts
  data_files:
  - split: dev
    path: parquet/fr_alts/dev.parquet
  - split: test
    path: parquet/fr_alts/test.parquet
  - split: train
    path: parquet/fr_alts/train.parquet
- config_name: fr_fqb
  data_files:
  - split: test
    path: parquet/fr_fqb/test.parquet
- config_name: fr_gsd
  data_files:
  - split: dev
    path: parquet/fr_gsd/dev.parquet
  - split: test
    path: parquet/fr_gsd/test.parquet
  - split: train
    path: parquet/fr_gsd/train.parquet
- config_name: fr_parisstories
  data_files:
  - split: dev
    path: parquet/fr_parisstories/dev.parquet
  - split: test
    path: parquet/fr_parisstories/test.parquet
  - split: train
    path: parquet/fr_parisstories/train.parquet
- config_name: fr_partut
  data_files:
  - split: dev
    path: parquet/fr_partut/dev.parquet
  - split: test
    path: parquet/fr_partut/test.parquet
  - split: train
    path: parquet/fr_partut/train.parquet
- config_name: fr_poitevindivital
  data_files:
  - split: test
    path: parquet/fr_poitevindivital/test.parquet
- config_name: fr_pud
  data_files:
  - split: test
    path: parquet/fr_pud/test.parquet
- config_name: fr_rhapsodie
  data_files:
  - split: dev
    path: parquet/fr_rhapsodie/dev.parquet
  - split: test
    path: parquet/fr_rhapsodie/test.parquet
  - split: train
    path: parquet/fr_rhapsodie/train.parquet
- config_name: fr_sequoia
  data_files:
  - split: dev
    path: parquet/fr_sequoia/dev.parquet
  - split: test
    path: parquet/fr_sequoia/test.parquet
  - split: train
    path: parquet/fr_sequoia/train.parquet
- config_name: qfn_fame
  data_files:
  - split: test
    path: parquet/qfn_fame/test.parquet
- config_name: gl_ctg
  data_files:
  - split: dev
    path: parquet/gl_ctg/dev.parquet
  - split: test
    path: parquet/gl_ctg/test.parquet
  - split: train
    path: parquet/gl_ctg/train.parquet
- config_name: gl_pud
  data_files:
  - split: test
    path: parquet/gl_pud/test.parquet
- config_name: gl_treegal
  data_files:
  - split: test
    path: parquet/gl_treegal/test.parquet
  - split: train
    path: parquet/gl_treegal/train.parquet
- config_name: ka_glc
  data_files:
  - split: dev
    path: parquet/ka_glc/dev.parquet
  - split: test
    path: parquet/ka_glc/test.parquet
  - split: train
    path: parquet/ka_glc/train.parquet
- config_name: ka_gnc
  data_files:
  - split: dev
    path: parquet/ka_gnc/dev.parquet
  - split: test
    path: parquet/ka_gnc/test.parquet
  - split: train
    path: parquet/ka_gnc/train.parquet
- config_name: de_gsd
  data_files:
  - split: dev
    path: parquet/de_gsd/dev.parquet
  - split: test
    path: parquet/de_gsd/test.parquet
  - split: train
    path: parquet/de_gsd/train.parquet
- config_name: de_hdt
  data_files:
  - split: dev
    path: parquet/de_hdt/dev.parquet
  - split: test
    path: parquet/de_hdt/test.parquet
  - split: train
    path: parquet/de_hdt/train.parquet
- config_name: de_lit
  data_files:
  - split: test
    path: parquet/de_lit/test.parquet
- config_name: de_pud
  data_files:
  - split: test
    path: parquet/de_pud/test.parquet
- config_name: aln_gps
  data_files:
  - split: test
    path: parquet/aln_gps/test.parquet
- config_name: gor_bungololombi
  data_files:
  - split: test
    path: parquet/gor_bungololombi/test.parquet
- config_name: got_proiel
  data_files:
  - split: dev
    path: parquet/got_proiel/dev.parquet
  - split: test
    path: parquet/got_proiel/test.parquet
  - split: train
    path: parquet/got_proiel/train.parquet
- config_name: el_cretan
  data_files:
  - split: dev
    path: parquet/el_cretan/dev.parquet
  - split: test
    path: parquet/el_cretan/test.parquet
  - split: train
    path: parquet/el_cretan/train.parquet
- config_name: el_gdt
  data_files:
  - split: dev
    path: parquet/el_gdt/dev.parquet
  - split: test
    path: parquet/el_gdt/test.parquet
  - split: train
    path: parquet/el_gdt/train.parquet
- config_name: el_glcii
  data_files:
  - split: test
    path: parquet/el_glcii/test.parquet
- config_name: el_gud
  data_files:
  - split: test
    path: parquet/el_gud/test.parquet
  - split: train
    path: parquet/el_gud/train.parquet
- config_name: el_lesbian
  data_files:
  - split: test
    path: parquet/el_lesbian/test.parquet
- config_name: el_messinian
  data_files:
  - split: dev
    path: parquet/el_messinian/dev.parquet
  - split: test
    path: parquet/el_messinian/test.parquet
  - split: train
    path: parquet/el_messinian/train.parquet
- config_name: gub_tudet
  data_files:
  - split: test
    path: parquet/gub_tudet/test.parquet
- config_name: gn_oldtudet
  data_files:
  - split: test
    path: parquet/gn_oldtudet/test.parquet
- config_name: gu_gujtb
  data_files:
  - split: test
    path: parquet/gu_gujtb/test.parquet
- config_name: gwi_tuecl
  data_files:
  - split: test
    path: parquet/gwi_tuecl/test.parquet
- config_name: ht_adolphe
  data_files:
  - split: dev
    path: parquet/ht_adolphe/dev.parquet
  - split: test
    path: parquet/ht_adolphe/test.parquet
  - split: train
    path: parquet/ht_adolphe/train.parquet
- config_name: ht_autogramm
  data_files:
  - split: test
    path: parquet/ht_autogramm/test.parquet
- config_name: ha_easternautogramm
  data_files:
  - split: test
    path: parquet/ha_easternautogramm/test.parquet
- config_name: ha_northernautogramm
  data_files:
  - split: test
    path: parquet/ha_northernautogramm/test.parquet
- config_name: ha_southernautogramm
  data_files:
  - split: test
    path: parquet/ha_southernautogramm/test.parquet
- config_name: ha_westernautogramm
  data_files:
  - split: test
    path: parquet/ha_westernautogramm/test.parquet
- config_name: he_htb
  data_files:
  - split: dev
    path: parquet/he_htb/dev.parquet
  - split: test
    path: parquet/he_htb/test.parquet
  - split: train
    path: parquet/he_htb/train.parquet
- config_name: he_iahltknesset
  data_files:
  - split: dev
    path: parquet/he_iahltknesset/dev.parquet
  - split: test
    path: parquet/he_iahltknesset/test.parquet
  - split: train
    path: parquet/he_iahltknesset/train.parquet
- config_name: he_iahltwiki
  data_files:
  - split: dev
    path: parquet/he_iahltwiki/dev.parquet
  - split: test
    path: parquet/he_iahltwiki/test.parquet
  - split: train
    path: parquet/he_iahltwiki/train.parquet
- config_name: he_postrab
  data_files:
  - split: test
    path: parquet/he_postrab/test.parquet
- config_name: azz_itml
  data_files:
  - split: test
    path: parquet/azz_itml/test.parquet
- config_name: hi_hdtb
  data_files:
  - split: dev
    path: parquet/hi_hdtb/dev.parquet
  - split: test
    path: parquet/hi_hdtb/test.parquet
  - split: train
    path: parquet/hi_hdtb/train.parquet
- config_name: hi_pud
  data_files:
  - split: test
    path: parquet/hi_pud/test.parquet
- config_name: hit_hittb
  data_files:
  - split: test
    path: parquet/hit_hittb/test.parquet
- config_name: hu_szeged
  data_files:
  - split: dev
    path: parquet/hu_szeged/dev.parquet
  - split: test
    path: parquet/hu_szeged/test.parquet
  - split: train
    path: parquet/hu_szeged/train.parquet
- config_name: is_gc
  data_files:
  - split: dev
    path: parquet/is_gc/dev.parquet
  - split: test
    path: parquet/is_gc/test.parquet
  - split: train
    path: parquet/is_gc/train.parquet
- config_name: is_icepahc
  data_files:
  - split: dev
    path: parquet/is_icepahc/dev.parquet
  - split: test
    path: parquet/is_icepahc/test.parquet
  - split: train
    path: parquet/is_icepahc/train.parquet
- config_name: is_modern
  data_files:
  - split: dev
    path: parquet/is_modern/dev.parquet
  - split: test
    path: parquet/is_modern/test.parquet
  - split: train
    path: parquet/is_modern/train.parquet
- config_name: is_pud
  data_files:
  - split: test
    path: parquet/is_pud/test.parquet
- config_name: arh_chibergis
  data_files:
  - split: test
    path: parquet/arh_chibergis/test.parquet
- config_name: id_csui
  data_files:
  - split: test
    path: parquet/id_csui/test.parquet
  - split: train
    path: parquet/id_csui/train.parquet
- config_name: id_gsd
  data_files:
  - split: dev
    path: parquet/id_gsd/dev.parquet
  - split: test
    path: parquet/id_gsd/test.parquet
  - split: train
    path: parquet/id_gsd/train.parquet
- config_name: id_pud
  data_files:
  - split: test
    path: parquet/id_pud/test.parquet
- config_name: ga_cadhan
  data_files:
  - split: test
    path: parquet/ga_cadhan/test.parquet
- config_name: ga_idt
  data_files:
  - split: dev
    path: parquet/ga_idt/dev.parquet
  - split: test
    path: parquet/ga_idt/test.parquet
  - split: train
    path: parquet/ga_idt/train.parquet
- config_name: ga_twittirish
  data_files:
  - split: dev
    path: parquet/ga_twittirish/dev.parquet
  - split: test
    path: parquet/ga_twittirish/test.parquet
  - split: train
    path: parquet/ga_twittirish/train.parquet
- config_name: it_isdt
  data_files:
  - split: dev
    path: parquet/it_isdt/dev.parquet
  - split: test
    path: parquet/it_isdt/test.parquet
  - split: train
    path: parquet/it_isdt/train.parquet
- config_name: it_kiparlaforest
  data_files:
  - split: test
    path: parquet/it_kiparlaforest/test.parquet
- config_name: it_markit
  data_files:
  - split: dev
    path: parquet/it_markit/dev.parquet
  - split: test
    path: parquet/it_markit/test.parquet
  - split: train
    path: parquet/it_markit/train.parquet
- config_name: it_old
  data_files:
  - split: dev
    path: parquet/it_old/dev.parquet
  - split: test
    path: parquet/it_old/test.parquet
  - split: train
    path: parquet/it_old/train.parquet
- config_name: it_parlamint
  data_files:
  - split: test
    path: parquet/it_parlamint/test.parquet
  - split: train
    path: parquet/it_parlamint/train.parquet
- config_name: it_partut
  data_files:
  - split: dev
    path: parquet/it_partut/dev.parquet
  - split: test
    path: parquet/it_partut/test.parquet
  - split: train
    path: parquet/it_partut/train.parquet
- config_name: it_postwita
  data_files:
  - split: dev
    path: parquet/it_postwita/dev.parquet
  - split: test
    path: parquet/it_postwita/test.parquet
  - split: train
    path: parquet/it_postwita/train.parquet
- config_name: it_pud
  data_files:
  - split: test
    path: parquet/it_pud/test.parquet
- config_name: it_twittiro
  data_files:
  - split: dev
    path: parquet/it_twittiro/dev.parquet
  - split: test
    path: parquet/it_twittiro/test.parquet
  - split: train
    path: parquet/it_twittiro/train.parquet
- config_name: it_valico
  data_files:
  - split: test
    path: parquet/it_valico/test.parquet
- config_name: it_vit
  data_files:
  - split: dev
    path: parquet/it_vit/dev.parquet
  - split: test
    path: parquet/it_vit/test.parquet
  - split: train
    path: parquet/it_vit/train.parquet
- config_name: ja_bccwjluw
  data_files:
  - split: dev
    path: parquet/ja_bccwjluw/dev.parquet
  - split: test
    path: parquet/ja_bccwjluw/test.parquet
  - split: train
    path: parquet/ja_bccwjluw/train.parquet
- config_name: ja_gsd
  data_files:
  - split: dev
    path: parquet/ja_gsd/dev.parquet
  - split: test
    path: parquet/ja_gsd/test.parquet
  - split: train
    path: parquet/ja_gsd/train.parquet
- config_name: ja_gsdluw
  data_files:
  - split: dev
    path: parquet/ja_gsdluw/dev.parquet
  - split: test
    path: parquet/ja_gsdluw/test.parquet
  - split: train
    path: parquet/ja_gsdluw/train.parquet
- config_name: ja_pud
  data_files:
  - split: test
    path: parquet/ja_pud/test.parquet
- config_name: ja_pudluw
  data_files:
  - split: test
    path: parquet/ja_pudluw/test.parquet
- config_name: jv_csui
  data_files:
  - split: test
    path: parquet/jv_csui/test.parquet
- config_name: urb_tudet
  data_files:
  - split: test
    path: parquet/urb_tudet/test.parquet
- config_name: kbc_unicamp
  data_files:
  - split: test
    path: parquet/kbc_unicamp/test.parquet
- config_name: xnr_kdtb
  data_files:
  - split: test
    path: parquet/xnr_kdtb/test.parquet
- config_name: krl_kkpp
  data_files:
  - split: test
    path: parquet/krl_kkpp/test.parquet
- config_name: arr_tudet
  data_files:
  - split: test
    path: parquet/arr_tudet/test.parquet
- config_name: kk_ktb
  data_files:
  - split: test
    path: parquet/kk_ktb/test.parquet
  - split: train
    path: parquet/kk_ktb/train.parquet
- config_name: naq_kdt
  data_files:
  - split: dev
    path: parquet/naq_kdt/dev.parquet
  - split: test
    path: parquet/naq_kdt/test.parquet
  - split: train
    path: parquet/naq_kdt/train.parquet
- config_name: quc_iu
  data_files:
  - split: test
    path: parquet/quc_iu/test.parquet
- config_name: koi_uh
  data_files:
  - split: test
    path: parquet/koi_uh/test.parquet
  - split: train
    path: parquet/koi_uh/train.parquet
- config_name: kpv_ikdp
  data_files:
  - split: test
    path: parquet/kpv_ikdp/test.parquet
- config_name: kpv_lattice
  data_files:
  - split: test
    path: parquet/kpv_lattice/test.parquet
  - split: train
    path: parquet/kpv_lattice/train.parquet
- config_name: ko_gsd
  data_files:
  - split: dev
    path: parquet/ko_gsd/dev.parquet
  - split: test
    path: parquet/ko_gsd/test.parquet
  - split: train
    path: parquet/ko_gsd/train.parquet
- config_name: ko_kaist
  data_files:
  - split: dev
    path: parquet/ko_kaist/dev.parquet
  - split: test
    path: parquet/ko_kaist/test.parquet
  - split: train
    path: parquet/ko_kaist/train.parquet
- config_name: ko_ksl
  data_files:
  - split: dev
    path: parquet/ko_ksl/dev.parquet
  - split: test
    path: parquet/ko_ksl/test.parquet
  - split: train
    path: parquet/ko_ksl/train.parquet
- config_name: ko_littleprince
  data_files:
  - split: test
    path: parquet/ko_littleprince/test.parquet
- config_name: ko_pud
  data_files:
  - split: test
    path: parquet/ko_pud/test.parquet
- config_name: ky_ktmu
  data_files:
  - split: test
    path: parquet/ky_ktmu/test.parquet
  - split: train
    path: parquet/ky_ktmu/train.parquet
- config_name: ky_tuecl
  data_files:
  - split: test
    path: parquet/ky_tuecl/test.parquet
- config_name: ltg_cairo
  data_files:
  - split: test
    path: parquet/ltg_cairo/test.parquet
- config_name: la_circse
  data_files:
  - split: dev
    path: parquet/la_circse/dev.parquet
  - split: test
    path: parquet/la_circse/test.parquet
  - split: train
    path: parquet/la_circse/train.parquet
- config_name: la_ittb
  data_files:
  - split: dev
    path: parquet/la_ittb/dev.parquet
  - split: test
    path: parquet/la_ittb/test.parquet
  - split: train
    path: parquet/la_ittb/train.parquet
- config_name: la_llct
  data_files:
  - split: dev
    path: parquet/la_llct/dev.parquet
  - split: test
    path: parquet/la_llct/test.parquet
  - split: train
    path: parquet/la_llct/train.parquet
- config_name: la_perseus
  data_files:
  - split: test
    path: parquet/la_perseus/test.parquet
  - split: train
    path: parquet/la_perseus/train.parquet
- config_name: la_proiel
  data_files:
  - split: dev
    path: parquet/la_proiel/dev.parquet
  - split: test
    path: parquet/la_proiel/test.parquet
  - split: train
    path: parquet/la_proiel/train.parquet
- config_name: la_udante
  data_files:
  - split: dev
    path: parquet/la_udante/dev.parquet
  - split: test
    path: parquet/la_udante/test.parquet
  - split: train
    path: parquet/la_udante/train.parquet
- config_name: lv_cairo
  data_files:
  - split: test
    path: parquet/lv_cairo/test.parquet
- config_name: lv_lvtb
  data_files:
  - split: dev
    path: parquet/lv_lvtb/dev.parquet
  - split: test
    path: parquet/lv_lvtb/test.parquet
  - split: train
    path: parquet/lv_lvtb/train.parquet
- config_name: lij_glt
  data_files:
  - split: test
    path: parquet/lij_glt/test.parquet
  - split: train
    path: parquet/lij_glt/train.parquet
- config_name: lt_alksnis
  data_files:
  - split: dev
    path: parquet/lt_alksnis/dev.parquet
  - split: test
    path: parquet/lt_alksnis/test.parquet
  - split: train
    path: parquet/lt_alksnis/train.parquet
- config_name: lt_hse
  data_files:
  - split: dev
    path: parquet/lt_hse/dev.parquet
  - split: test
    path: parquet/lt_hse/test.parquet
  - split: train
    path: parquet/lt_hse/train.parquet
- config_name: olo_kkpp
  data_files:
  - split: test
    path: parquet/olo_kkpp/test.parquet
  - split: train
    path: parquet/olo_kkpp/train.parquet
- config_name: nds_lsdc
  data_files:
  - split: test
    path: parquet/nds_lsdc/test.parquet
  - split: train
    path: parquet/nds_lsdc/train.parquet
- config_name: lb_luxbank
  data_files:
  - split: test
    path: parquet/lb_luxbank/test.parquet
- config_name: mk_mtb
  data_files:
  - split: test
    path: parquet/mk_mtb/test.parquet
- config_name: jaa_jarawara
  data_files:
  - split: test
    path: parquet/jaa_jarawara/test.parquet
- config_name: qaf_arabizi
  data_files:
  - split: dev
    path: parquet/qaf_arabizi/dev.parquet
  - split: test
    path: parquet/qaf_arabizi/test.parquet
  - split: train
    path: parquet/qaf_arabizi/train.parquet
- config_name: mpu_tudet
  data_files:
  - split: test
    path: parquet/mpu_tudet/test.parquet
- config_name: ml_ufal
  data_files:
  - split: test
    path: parquet/ml_ufal/test.parquet
- config_name: mt_mudt
  data_files:
  - split: dev
    path: parquet/mt_mudt/dev.parquet
  - split: test
    path: parquet/mt_mudt/test.parquet
  - split: train
    path: parquet/mt_mudt/train.parquet
- config_name: gv_cadhan
  data_files:
  - split: test
    path: parquet/gv_cadhan/test.parquet
  - split: train
    path: parquet/gv_cadhan/train.parquet
- config_name: mr_cmupan
  data_files:
  - split: dev
    path: parquet/mr_cmupan/dev.parquet
  - split: test
    path: parquet/mr_cmupan/test.parquet
  - split: train
    path: parquet/mr_cmupan/train.parquet
- config_name: mr_ufal
  data_files:
  - split: dev
    path: parquet/mr_ufal/dev.parquet
  - split: test
    path: parquet/mr_ufal/test.parquet
  - split: train
    path: parquet/mr_ufal/train.parquet
- config_name: gun_thomas
  data_files:
  - split: test
    path: parquet/gun_thomas/test.parquet
- config_name: axm_armtdp
  data_files:
  - split: test
    path: parquet/axm_armtdp/test.parquet
- config_name: frm_altm
  data_files:
  - split: test
    path: parquet/frm_altm/test.parquet
- config_name: frm_profiterole
  data_files:
  - split: dev
    path: parquet/frm_profiterole/dev.parquet
  - split: test
    path: parquet/frm_profiterole/test.parquet
  - split: train
    path: parquet/frm_profiterole/train.parquet
- config_name: mdf_jr
  data_files:
  - split: test
    path: parquet/mdf_jr/test.parquet
  - split: train
    path: parquet/mdf_jr/train.parquet
- config_name: myu_tudet
  data_files:
  - split: test
    path: parquet/myu_tudet/test.parquet
- config_name: nmf_suansu
  data_files:
  - split: test
    path: parquet/nmf_suansu/test.parquet
  - split: train
    path: parquet/nmf_suansu/train.parquet
- config_name: pcm_nsc
  data_files:
  - split: dev
    path: parquet/pcm_nsc/dev.parquet
  - split: test
    path: parquet/pcm_nsc/test.parquet
  - split: train
    path: parquet/pcm_nsc/train.parquet
- config_name: nap_rb
  data_files:
  - split: test
    path: parquet/nap_rb/test.parquet
- config_name: yrk_tundra
  data_files:
  - split: test
    path: parquet/yrk_tundra/test.parquet
- config_name: ne_bk
  data_files:
  - split: test
    path: parquet/ne_bk/test.parquet
- config_name: yrl_complin
  data_files:
  - split: test
    path: parquet/yrl_complin/test.parquet
  - split: train
    path: parquet/yrl_complin/train.parquet
- config_name: sme_giella
  data_files:
  - split: test
    path: parquet/sme_giella/test.parquet
  - split: train
    path: parquet/sme_giella/train.parquet
- config_name: kmr_kurmanji
  data_files:
  - split: test
    path: parquet/kmr_kurmanji/test.parquet
  - split: train
    path: parquet/kmr_kurmanji/train.parquet
- config_name: gya_autogramm
  data_files:
  - split: test
    path: parquet/gya_autogramm/test.parquet
- config_name: no_bokmaal
  data_files:
  - split: dev
    path: parquet/no_bokmaal/dev.parquet
  - split: test
    path: parquet/no_bokmaal/test.parquet
  - split: train
    path: parquet/no_bokmaal/train.parquet
- config_name: no_nynorsk
  data_files:
  - split: dev
    path: parquet/no_nynorsk/dev.parquet
  - split: test
    path: parquet/no_nynorsk/test.parquet
  - split: train
    path: parquet/no_nynorsk/train.parquet
- config_name: oc_ttb
  data_files:
  - split: dev
    path: parquet/oc_ttb/dev.parquet
  - split: test
    path: parquet/oc_ttb/test.parquet
  - split: train
    path: parquet/oc_ttb/train.parquet
- config_name: or_odtb
  data_files:
  - split: test
    path: parquet/or_odtb/test.parquet
- config_name: cu_proiel
  data_files:
  - split: dev
    path: parquet/cu_proiel/dev.parquet
  - split: test
    path: parquet/cu_proiel/test.parquet
  - split: train
    path: parquet/cu_proiel/train.parquet
- config_name: orv_birchbark
  data_files:
  - split: dev
    path: parquet/orv_birchbark/dev.parquet
  - split: test
    path: parquet/orv_birchbark/test.parquet
  - split: train
    path: parquet/orv_birchbark/train.parquet
- config_name: orv_rnc
  data_files:
  - split: dev
    path: parquet/orv_rnc/dev.parquet
  - split: test
    path: parquet/orv_rnc/test.parquet
  - split: train
    path: parquet/orv_rnc/train.parquet
- config_name: orv_ruthenian
  data_files:
  - split: dev
    path: parquet/orv_ruthenian/dev.parquet
  - split: test
    path: parquet/orv_ruthenian/test.parquet
  - split: train
    path: parquet/orv_ruthenian/train.parquet
- config_name: orv_torot
  data_files:
  - split: dev
    path: parquet/orv_torot/dev.parquet
  - split: test
    path: parquet/orv_torot/test.parquet
  - split: train
    path: parquet/orv_torot/train.parquet
- config_name: ang_cairo
  data_files:
  - split: test
    path: parquet/ang_cairo/test.parquet
- config_name: fro_altm
  data_files:
  - split: test
    path: parquet/fro_altm/test.parquet
- config_name: fro_profiterole
  data_files:
  - split: dev
    path: parquet/fro_profiterole/dev.parquet
  - split: test
    path: parquet/fro_profiterole/test.parquet
  - split: train
    path: parquet/fro_profiterole/train.parquet
- config_name: oge_glc
  data_files:
  - split: test
    path: parquet/oge_glc/test.parquet
- config_name: sga_dipsgg
  data_files:
  - split: test
    path: parquet/sga_dipsgg/test.parquet
- config_name: sga_dipwbg
  data_files:
  - split: test
    path: parquet/sga_dipwbg/test.parquet
- config_name: pro_corag
  data_files:
  - split: dev
    path: parquet/pro_corag/dev.parquet
  - split: test
    path: parquet/pro_corag/test.parquet
  - split: train
    path: parquet/pro_corag/train.parquet
- config_name: otk_clausal
  data_files:
  - split: test
    path: parquet/otk_clausal/test.parquet
- config_name: ota_boun
  data_files:
  - split: test
    path: parquet/ota_boun/test.parquet
  - split: train
    path: parquet/ota_boun/train.parquet
- config_name: ota_dudu
  data_files:
  - split: dev
    path: parquet/ota_dudu/dev.parquet
  - split: test
    path: parquet/ota_dudu/test.parquet
  - split: train
    path: parquet/ota_dudu/train.parquet
- config_name: ota_tuecl
  data_files:
  - split: test
    path: parquet/ota_tuecl/test.parquet
- config_name: ps_prince
  data_files:
  - split: test
    path: parquet/ps_prince/test.parquet
- config_name: ps_sikaram
  data_files:
  - split: test
    path: parquet/ps_sikaram/test.parquet
- config_name: pad_tuecl
  data_files:
  - split: test
    path: parquet/pad_tuecl/test.parquet
- config_name: fa_perdt
  data_files:
  - split: dev
    path: parquet/fa_perdt/dev.parquet
  - split: test
    path: parquet/fa_perdt/test.parquet
  - split: train
    path: parquet/fa_perdt/train.parquet
- config_name: fa_seraji
  data_files:
  - split: dev
    path: parquet/fa_seraji/dev.parquet
  - split: test
    path: parquet/fa_seraji/test.parquet
  - split: train
    path: parquet/fa_seraji/train.parquet
- config_name: pay_chibergis
  data_files:
  - split: test
    path: parquet/pay_chibergis/test.parquet
- config_name: xpg_kul
  data_files:
  - split: test
    path: parquet/xpg_kul/test.parquet
- config_name: pl_lfg
  data_files:
  - split: dev
    path: parquet/pl_lfg/dev.parquet
  - split: test
    path: parquet/pl_lfg/test.parquet
  - split: train
    path: parquet/pl_lfg/train.parquet
- config_name: pl_mpdt
  data_files:
  - split: dev
    path: parquet/pl_mpdt/dev.parquet
  - split: test
    path: parquet/pl_mpdt/test.parquet
  - split: train
    path: parquet/pl_mpdt/train.parquet
- config_name: pl_pdb
  data_files:
  - split: dev
    path: parquet/pl_pdb/dev.parquet
  - split: test
    path: parquet/pl_pdb/test.parquet
  - split: train
    path: parquet/pl_pdb/train.parquet
- config_name: pl_pud
  data_files:
  - split: test
    path: parquet/pl_pud/test.parquet
- config_name: qpm_philotis
  data_files:
  - split: dev
    path: parquet/qpm_philotis/dev.parquet
  - split: test
    path: parquet/qpm_philotis/test.parquet
  - split: train
    path: parquet/qpm_philotis/train.parquet
- config_name: pt_bosque
  data_files:
  - split: dev
    path: parquet/pt_bosque/dev.parquet
  - split: test
    path: parquet/pt_bosque/test.parquet
  - split: train
    path: parquet/pt_bosque/train.parquet
- config_name: pt_dantestocks
  data_files:
  - split: dev
    path: parquet/pt_dantestocks/dev.parquet
  - split: test
    path: parquet/pt_dantestocks/test.parquet
  - split: train
    path: parquet/pt_dantestocks/train.parquet
- config_name: pt_gsd
  data_files:
  - split: dev
    path: parquet/pt_gsd/dev.parquet
  - split: test
    path: parquet/pt_gsd/test.parquet
  - split: train
    path: parquet/pt_gsd/train.parquet
- config_name: pt_petrogold
  data_files:
  - split: dev
    path: parquet/pt_petrogold/dev.parquet
  - split: test
    path: parquet/pt_petrogold/test.parquet
  - split: train
    path: parquet/pt_petrogold/train.parquet
- config_name: pt_porttinari
  data_files:
  - split: dev
    path: parquet/pt_porttinari/dev.parquet
  - split: test
    path: parquet/pt_porttinari/test.parquet
  - split: train
    path: parquet/pt_porttinari/train.parquet
- config_name: pt_pud
  data_files:
  - split: test
    path: parquet/pt_pud/test.parquet
- config_name: pa_cs
  data_files:
  - split: dev
    path: parquet/pa_cs/dev.parquet
  - split: test
    path: parquet/pa_cs/test.parquet
  - split: train
    path: parquet/pa_cs/train.parquet
- config_name: pa_rang
  data_files:
  - split: dev
    path: parquet/pa_rang/dev.parquet
  - split: test
    path: parquet/pa_rang/test.parquet
  - split: train
    path: parquet/pa_rang/train.parquet
- config_name: ro_art
  data_files:
  - split: test
    path: parquet/ro_art/test.parquet
- config_name: ro_moldoro
  data_files:
  - split: test
    path: parquet/ro_moldoro/test.parquet
- config_name: ro_nonstandard
  data_files:
  - split: dev
    path: parquet/ro_nonstandard/dev.parquet
  - split: test
    path: parquet/ro_nonstandard/test.parquet
  - split: train
    path: parquet/ro_nonstandard/train.parquet
- config_name: ro_rrt
  data_files:
  - split: dev
    path: parquet/ro_rrt/dev.parquet
  - split: test
    path: parquet/ro_rrt/test.parquet
  - split: train
    path: parquet/ro_rrt/train.parquet
- config_name: ro_simonero
  data_files:
  - split: dev
    path: parquet/ro_simonero/dev.parquet
  - split: test
    path: parquet/ro_simonero/test.parquet
  - split: train
    path: parquet/ro_simonero/train.parquet
- config_name: ro_tuecl
  data_files:
  - split: test
    path: parquet/ro_tuecl/test.parquet
- config_name: ru_gsd
  data_files:
  - split: dev
    path: parquet/ru_gsd/dev.parquet
  - split: test
    path: parquet/ru_gsd/test.parquet
  - split: train
    path: parquet/ru_gsd/train.parquet
- config_name: ru_poetry
  data_files:
  - split: dev
    path: parquet/ru_poetry/dev.parquet
  - split: test
    path: parquet/ru_poetry/test.parquet
  - split: train
    path: parquet/ru_poetry/train.parquet
- config_name: ru_pud
  data_files:
  - split: test
    path: parquet/ru_pud/test.parquet
- config_name: ru_syntagrus
  data_files:
  - split: dev
    path: parquet/ru_syntagrus/dev.parquet
  - split: test
    path: parquet/ru_syntagrus/test.parquet
  - split: train
    path: parquet/ru_syntagrus/train.parquet
- config_name: ru_taiga
  data_files:
  - split: dev
    path: parquet/ru_taiga/dev.parquet
  - split: test
    path: parquet/ru_taiga/test.parquet
  - split: train
    path: parquet/ru_taiga/train.parquet
- config_name: ruc_rdt
  data_files:
  - split: test
    path: parquet/ruc_rdt/test.parquet
- config_name: sa_ufal
  data_files:
  - split: test
    path: parquet/sa_ufal/test.parquet
- config_name: sa_vedic
  data_files:
  - split: dev
    path: parquet/sa_vedic/dev.parquet
  - split: test
    path: parquet/sa_vedic/test.parquet
  - split: train
    path: parquet/sa_vedic/train.parquet
- config_name: gd_arcosg
  data_files:
  - split: dev
    path: parquet/gd_arcosg/dev.parquet
  - split: test
    path: parquet/gd_arcosg/test.parquet
  - split: train
    path: parquet/gd_arcosg/train.parquet
- config_name: sr_set
  data_files:
  - split: dev
    path: parquet/sr_set/dev.parquet
  - split: test
    path: parquet/sr_set/test.parquet
  - split: train
    path: parquet/sr_set/train.parquet
- config_name: wuu_shud
  data_files:
  - split: dev
    path: parquet/wuu_shud/dev.parquet
  - split: test
    path: parquet/wuu_shud/test.parquet
  - split: train
    path: parquet/wuu_shud/train.parquet
- config_name: scn_stb
  data_files:
  - split: test
    path: parquet/scn_stb/test.parquet
- config_name: sd_isra
  data_files:
  - split: dev
    path: parquet/sd_isra/dev.parquet
  - split: test
    path: parquet/sd_isra/test.parquet
  - split: train
    path: parquet/sd_isra/train.parquet
- config_name: si_appuwa
  data_files:
  - split: test
    path: parquet/si_appuwa/test.parquet
- config_name: si_stb
  data_files:
  - split: test
    path: parquet/si_stb/test.parquet
- config_name: sms_giellagas
  data_files:
  - split: test
    path: parquet/sms_giellagas/test.parquet
  - split: train
    path: parquet/sms_giellagas/train.parquet
- config_name: sk_snk
  data_files:
  - split: dev
    path: parquet/sk_snk/dev.parquet
  - split: test
    path: parquet/sk_snk/test.parquet
  - split: train
    path: parquet/sk_snk/train.parquet
- config_name: sl_ssj
  data_files:
  - split: dev
    path: parquet/sl_ssj/dev.parquet
  - split: test
    path: parquet/sl_ssj/test.parquet
  - split: train
    path: parquet/sl_ssj/train.parquet
- config_name: sl_sst
  data_files:
  - split: dev
    path: parquet/sl_sst/dev.parquet
  - split: test
    path: parquet/sl_sst/test.parquet
  - split: train
    path: parquet/sl_sst/train.parquet
- config_name: ajp_madar
  data_files:
  - split: test
    path: parquet/ajp_madar/test.parquet
- config_name: sdh_garrusi
  data_files:
  - split: dev
    path: parquet/sdh_garrusi/dev.parquet
  - split: test
    path: parquet/sdh_garrusi/test.parquet
  - split: train
    path: parquet/sdh_garrusi/train.parquet
- config_name: es_ancora
  data_files:
  - split: dev
    path: parquet/es_ancora/dev.parquet
  - split: test
    path: parquet/es_ancora/test.parquet
  - split: train
    path: parquet/es_ancora/train.parquet
- config_name: es_coser
  data_files:
  - split: test
    path: parquet/es_coser/test.parquet
- config_name: es_gsd
  data_files:
  - split: dev
    path: parquet/es_gsd/dev.parquet
  - split: test
    path: parquet/es_gsd/test.parquet
  - split: train
    path: parquet/es_gsd/train.parquet
- config_name: es_pud
  data_files:
  - split: test
    path: parquet/es_pud/test.parquet
- config_name: ssp_lse
  data_files:
  - split: test
    path: parquet/ssp_lse/test.parquet
- config_name: sv_lines
  data_files:
  - split: dev
    path: parquet/sv_lines/dev.parquet
  - split: test
    path: parquet/sv_lines/test.parquet
  - split: train
    path: parquet/sv_lines/train.parquet
- config_name: sv_old
  data_files:
  - split: test
    path: parquet/sv_old/test.parquet
- config_name: sv_pud
  data_files:
  - split: test
    path: parquet/sv_pud/test.parquet
- config_name: sv_swell
  data_files:
  - split: test
    path: parquet/sv_swell/test.parquet
- config_name: sv_talbanken
  data_files:
  - split: dev
    path: parquet/sv_talbanken/dev.parquet
  - split: test
    path: parquet/sv_talbanken/test.parquet
  - split: train
    path: parquet/sv_talbanken/train.parquet
- config_name: swl_sslc
  data_files:
  - split: test
    path: parquet/swl_sslc/test.parquet
- config_name: tl_trg
  data_files:
  - split: test
    path: parquet/tl_trg/test.parquet
- config_name: tl_ugnayan
  data_files:
  - split: test
    path: parquet/tl_ugnayan/test.parquet
- config_name: ta_mwtt
  data_files:
  - split: test
    path: parquet/ta_mwtt/test.parquet
- config_name: ta_ttb
  data_files:
  - split: dev
    path: parquet/ta_ttb/dev.parquet
  - split: test
    path: parquet/ta_ttb/test.parquet
  - split: train
    path: parquet/ta_ttb/train.parquet
- config_name: tt_nmctt
  data_files:
  - split: test
    path: parquet/tt_nmctt/test.parquet
- config_name: eme_tudet
  data_files:
  - split: test
    path: parquet/eme_tudet/test.parquet
- config_name: te_mtg
  data_files:
  - split: dev
    path: parquet/te_mtg/dev.parquet
  - split: test
    path: parquet/te_mtg/test.parquet
  - split: train
    path: parquet/te_mtg/train.parquet
- config_name: qte_tect
  data_files:
  - split: test
    path: parquet/qte_tect/test.parquet
  - split: train
    path: parquet/qte_tect/train.parquet
- config_name: th_pud
  data_files:
  - split: test
    path: parquet/th_pud/test.parquet
- config_name: th_tud
  data_files:
  - split: dev
    path: parquet/th_tud/dev.parquet
  - split: test
    path: parquet/th_tud/test.parquet
  - split: train
    path: parquet/th_tud/train.parquet
- config_name: tn_popapolelo
  data_files:
  - split: test
    path: parquet/tn_popapolelo/test.parquet
- config_name: tpn_tudet
  data_files:
  - split: test
    path: parquet/tpn_tudet/test.parquet
- config_name: tr_atis
  data_files:
  - split: dev
    path: parquet/tr_atis/dev.parquet
  - split: test
    path: parquet/tr_atis/test.parquet
  - split: train
    path: parquet/tr_atis/train.parquet
- config_name: tr_boun
  data_files:
  - split: dev
    path: parquet/tr_boun/dev.parquet
  - split: test
    path: parquet/tr_boun/test.parquet
  - split: train
    path: parquet/tr_boun/train.parquet
- config_name: tr_framenet
  data_files:
  - split: dev
    path: parquet/tr_framenet/dev.parquet
  - split: test
    path: parquet/tr_framenet/test.parquet
  - split: train
    path: parquet/tr_framenet/train.parquet
- config_name: tr_gb
  data_files:
  - split: test
    path: parquet/tr_gb/test.parquet
- config_name: tr_imst
  data_files:
  - split: dev
    path: parquet/tr_imst/dev.parquet
  - split: test
    path: parquet/tr_imst/test.parquet
  - split: train
    path: parquet/tr_imst/train.parquet
- config_name: tr_kenet
  data_files:
  - split: dev
    path: parquet/tr_kenet/dev.parquet
  - split: test
    path: parquet/tr_kenet/test.parquet
  - split: train
    path: parquet/tr_kenet/train.parquet
- config_name: tr_penn
  data_files:
  - split: dev
    path: parquet/tr_penn/dev.parquet
  - split: test
    path: parquet/tr_penn/test.parquet
  - split: train
    path: parquet/tr_penn/train.parquet
- config_name: tr_pud
  data_files:
  - split: test
    path: parquet/tr_pud/test.parquet
- config_name: tr_tourism
  data_files:
  - split: dev
    path: parquet/tr_tourism/dev.parquet
  - split: test
    path: parquet/tr_tourism/test.parquet
  - split: train
    path: parquet/tr_tourism/train.parquet
- config_name: tr_tuecl
  data_files:
  - split: test
    path: parquet/tr_tuecl/test.parquet
- config_name: qti_butr
  data_files:
  - split: test
    path: parquet/qti_butr/test.parquet
- config_name: qtd_sagt
  data_files:
  - split: dev
    path: parquet/qtd_sagt/dev.parquet
  - split: test
    path: parquet/qtd_sagt/test.parquet
  - split: train
    path: parquet/qtd_sagt/train.parquet
- config_name: uk_iu
  data_files:
  - split: dev
    path: parquet/uk_iu/dev.parquet
  - split: test
    path: parquet/uk_iu/test.parquet
  - split: train
    path: parquet/uk_iu/train.parquet
- config_name: uk_parlamint
  data_files:
  - split: dev
    path: parquet/uk_parlamint/dev.parquet
  - split: test
    path: parquet/uk_parlamint/test.parquet
  - split: train
    path: parquet/uk_parlamint/train.parquet
- config_name: xum_ikuvina
  data_files:
  - split: test
    path: parquet/xum_ikuvina/test.parquet
- config_name: hsb_ufal
  data_files:
  - split: test
    path: parquet/hsb_ufal/test.parquet
- config_name: ur_udtb
  data_files:
  - split: dev
    path: parquet/ur_udtb/dev.parquet
  - split: test
    path: parquet/ur_udtb/test.parquet
  - split: train
    path: parquet/ur_udtb/train.parquet
- config_name: ug_udt
  data_files:
  - split: dev
    path: parquet/ug_udt/dev.parquet
  - split: test
    path: parquet/ug_udt/test.parquet
  - split: train
    path: parquet/ug_udt/train.parquet
- config_name: uz_tuecl
  data_files:
  - split: test
    path: parquet/uz_tuecl/test.parquet
- config_name: uz_ut
  data_files:
  - split: test
    path: parquet/uz_ut/test.parquet
- config_name: uz_uzudt
  data_files:
  - split: test
    path: parquet/uz_uzudt/test.parquet
  - split: train
    path: parquet/uz_uzudt/train.parquet
- config_name: vep_vwt
  data_files:
  - split: test
    path: parquet/vep_vwt/test.parquet
- config_name: vi_tuecl
  data_files:
  - split: test
    path: parquet/vi_tuecl/test.parquet
- config_name: vi_vtb
  data_files:
  - split: dev
    path: parquet/vi_vtb/dev.parquet
  - split: test
    path: parquet/vi_vtb/test.parquet
  - split: train
    path: parquet/vi_vtb/train.parquet
- config_name: wbp_ufal
  data_files:
  - split: test
    path: parquet/wbp_ufal/test.parquet
- config_name: cy_ccg
  data_files:
  - split: dev
    path: parquet/cy_ccg/dev.parquet
  - split: test
    path: parquet/cy_ccg/test.parquet
  - split: train
    path: parquet/cy_ccg/train.parquet
- config_name: hyw_armtdp
  data_files:
  - split: dev
    path: parquet/hyw_armtdp/dev.parquet
  - split: test
    path: parquet/hyw_armtdp/test.parquet
  - split: train
    path: parquet/hyw_armtdp/train.parquet
- config_name: nhi_mesotree
  data_files:
  - split: test
    path: parquet/nhi_mesotree/test.parquet
- config_name: wo_wtb
  data_files:
  - split: dev
    path: parquet/wo_wtb/dev.parquet
  - split: test
    path: parquet/wo_wtb/test.parquet
  - split: train
    path: parquet/wo_wtb/train.parquet
- config_name: xav_xdt
  data_files:
  - split: test
    path: parquet/xav_xdt/test.parquet
- config_name: sjo_xdt
  data_files:
  - split: test
    path: parquet/sjo_xdt/test.parquet
- config_name: sah_yktdt
  data_files:
  - split: test
    path: parquet/sah_yktdt/test.parquet
- config_name: yi_yitb
  data_files:
  - split: dev
    path: parquet/yi_yitb/dev.parquet
  - split: test
    path: parquet/yi_yitb/test.parquet
  - split: train
    path: parquet/yi_yitb/train.parquet
- config_name: yo_ytb
  data_files:
  - split: test
    path: parquet/yo_ytb/test.parquet
- config_name: ess_sli
  data_files:
  - split: test
    path: parquet/ess_sli/test.parquet
- config_name: say_autogramm
  data_files:
  - split: test
    path: parquet/say_autogramm/test.parquet
  - split: train
    path: parquet/say_autogramm/train.parquet
- config_name: zza_zsd
  data_files:
  - split: dev
    path: parquet/zza_zsd/dev.parquet
  - split: test
    path: parquet/zza_zsd/test.parquet
  - split: train
    path: parquet/zza_zsd/train.parquet
---

## Dataset Card (v2.0) for Universal Dependencies Treebank

**Version 2.0.0** introduces significant improvements and breaking changes:
- **Parquet Format:** faster loading with HuggingFace datasets >=4.0.0
- **MWT Support:** New `mwt` field provides structured multi-word token information
- **Enhanced Security:** No more `trust_remote_code=True` required
- **Separate Versioning:** Loader version (2.0.0) distinct from UD data version (2.18)

**Breaking Changes:**
- Token sequences now exclude MWT surface forms (matches UD guidelines)
- Requires `datasets>=4.0.0` for Parquet support

- **Migration Guide:** See [MIGRATION.md](MIGRATION.md) for detailed upgrade instructions
- **Changelog:** See [CHANGELOG.md](CHANGELOG.md) for complete release notes


## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Data Quality & Fidelity](#data-quality--fidelity)
  - [Usage](#usage)
  - [Tasks](#tasks)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Repository History](#repository-history)

## Dataset Description

- **Homepage:** [Universal Dependencies](https://universaldependencies.org)
- **Repository:** [Universal Dependencies](https://github.com/UniversalDependencies)
- **Paper:** [Universal Dependencies v2: An Evergrowing Multilingual Treebank Collection](https://arxiv.org/abs/2004.10643)
- **Paper:** [From Treebank Metadata to Sentence-Level Genre in Universal Dependencies: A Reproducible, Versioned Resource](https://universaldependencies.org/udw26/papers/41_Paper.pdf)

### Dataset Summary

Universal Dependencies is a project that seeks to develop cross-linguistically consistent treebank annotation for many languages, with the goal of facilitating multilingual parser development, cross-lingual learning, and parsing research from a language typology perspective. The annotation scheme is based on (universal) Stanford dependencies (de Marneffe et al., 2006, 2008, 2014), Google universal part-of-speech tags (Petrov et al., 2012), and the Interset interlingua for morphosyntactic tagsets (Zeman, 2008).

This is the official Hugging Face Parquet distribution for Universal
Dependencies at
[`universal-dependencies/universal_dependencies`](https://huggingface.co/datasets/universal-dependencies/universal_dependencies).
The dataset was formerly maintained at `commul/universal_dependencies`.

### Data Quality & Fidelity

This dataset achieves **100% fidelity** for linguistic data (tokens,
annotations, dependencies) and **very high (~98%) fidelity** for metadata. The
Parquet files can be perfectly reconstructed back to the original CoNLL-U
format with:
- All linguistic annotations preserved exactly
- Multi-word tokens (MWTs) and empty nodes fully supported
- Duplicate metadata keys preserved (1,323 sentences across 14 treebanks)
- Enhanced dependencies and rare annotation edge cases handled correctly

Recent improvements include fixes for:
- Double equals parsing in FEATS/MISC fields (e.g., `Gloss==POSS`)
- Empty nodes with ID < 1 (e.g., `0.1` for pro-drop subjects)
- Empty metadata values and keys without values
- Raw field parsing to bypass library bugs

For technical details, see [CONLLU_PARSING.md](https://github.com/bot-zen/ud-hf-parquet-tools/blob/main/CONLLU_PARSING.md) in the ud-hf-parquet-tools repository.

### Usage

```python
from datasets import load_dataset

# Load a specific treebank
ds = load_dataset(
    "universal-dependencies/universal_dependencies",
    "en_ewt",
    revision="2.18",
    split="train",
)

# Access sentence data
sentence = ds[0]
print(f"Sentence ID: {sentence['sent_id']}")
print(f"Text: {sentence['text']}")
print(f"Tokens: {sentence['tokens']}")

# Parse optional fields using helper functions
from ud_hf_parquet_tools import parse_feats, parse_misc

for i, token in enumerate(sentence['tokens']):
    feats = parse_feats(sentence['feats'][i])  # Returns dict or {}
    misc = parse_misc(sentence['misc'][i])      # Returns dict or {}
    print(f"{token}: UPOS={sentence['upos'][i]}, feats={feats}, misc={misc}")

# Export back to CoNLL-U format
from ud_hf_parquet_tools import write_conllu

# Write to stdout
write_conllu(ds)

# Write to file
write_conllu(ds, "output.conllu")

# Write to buffer (for other libraries)
import io
buffer = io.StringIO()
write_conllu(ds, buffer)
conllu_text = buffer.getvalue()
```

### Tasks

This dataset supports dependency parsing, universal and language-specific
part-of-speech tagging, lemmatization, and morphology-oriented token
classification.

## Dataset Structure

All files use a revised version of [the CoNLL-X
format](http://anthology.aclweb.org/W/W06/W06-2920.pdf) called CoNLL-U.
Annotations are encoded in plain text files (UTF-8, [normalized to
NFC](http://unicode.org/reports/tr15/), using only the LF character as line
break, including an LF character at the end of file).

* [Revision (r2.18) specific documentation](https://github.com/UniversalDependencies/docs/blob/r2.18/format.md)
* [Latest UD CoNLL-U Format documentation](https://universaldependencies.org/format.html)

### Data Instances

This dataset has 353 configurations (treebanks).
```python
from datasets import get_dataset_config_names, load_dataset

# Get all available treebank configurations for revision="2.18"
configs = get_dataset_config_names("universal-dependencies/universal_dependencies", revision="2.18")
print(f"Available treebanks: {len(configs)}")

# Example configurations:
# ['af_afribooms',
#  'akk_pisandub',
#  'aqz_tudet',
#  'sq_tsa',
#  'gsw_uzh',
#  'am_att',
#   ...
# ]

# Get the latest configurations
get_dataset_config_names("universal-dependencies/universal_dependencies")

# Load a specific treebank
dataset = load_dataset("universal-dependencies/universal_dependencies", "en_ewt")
print(dataset)

# Output:
# DatasetDict({
#     train: Dataset({
#         features: ['sent_id', 'text', 'comments', 'tokens', 'lemmas', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc', 'mwt', 'empty_nodes'],
#         num_rows: 12544
#     })
#     dev: Dataset({
#         features: ['sent_id', 'text', 'comments', 'tokens', 'lemmas', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc', 'mwt', 'empty_nodes'],
#         num_rows: 2001
#     })
#     test: Dataset({
#         features: ['sent_id', 'text', 'comments', 'tokens', 'lemmas', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc', 'mwt', 'empty_nodes'],
#         num_rows: 2077
#     })
# })
```

### Data Fields

Each example in the dataset contains the following fields:

- **sent_id** (string): Sentence ID from the CoNLL-U file metadata
- **text** (string): Full sentence text (surface form)
- **tokens** (list of strings): Syntactic word forms (MWT surface forms excluded)
- **lemmas** (list of strings): Lemmas for each syntactic word
- **upos** (list of strings): Universal POS tags
- **xpos** (list of strings): Language-specific POS tags
- **feats** (list of strings): Morphological features in UD format
- **head** (list of integers): Head indices for dependency relations
- **deprel** (list of strings): Dependency relation labels
- **deps** (list of strings): Enhanced dependency graph
- **misc** (list of strings): Miscellaneous annotations
- **mwt** (list of dicts): Multi-Word Token information (NEW in v2.0)
  - **id** (string): Token range (e.g., "1-2")
  - **form** (string): Surface form (e.g., "don't")
  - **misc** (string): MWT-specific metadata
- **empty_nodes** (list of dicts): Empty Node Token information (NEW in v2.0)
- **comments** (list of strings): All comments including duplicates, empty values, and original ordering (NEW in v2.0)

**Example:**

```python
from datasets import load_dataset

dataset = load_dataset("universal-dependencies/universal_dependencies", "en_ewt", split="train")
print(dataset[0])

# Output:
{
    'sent_id': 'weblog-juancole.com_juancole_20051126063000_ENG_20051126_063000-0001',
    'text': 'Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the mosque in the town of Qaim, near the Syrian border.',
    'comments': [
        'newdoc id = weblog-juancole.com_juancole_20051126063000_ENG_20051126_063000',
        '__SENT_ID__',
        'newpar id = weblog-juancole.com_juancole_20051126063000_ENG_20051126_063000-p0001',
        '__TEXT__'
    ],
    'tokens': ['Al', '-', 'Zaman', ':', 'American', 'forces', 'killed', 'Shaikh', 'Abdullah', 'al', '-', 'Ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the', 'town', 'of', 'Qaim', ',', 'near', 'the', 'Syrian', 'border', '.'],
    'lemmas': ['Al', '-', 'Zaman', ':', 'American', 'force', 'kill', 'Shaikh', 'Abdullah', 'al', '-', 'Ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the', 'town', 'of', 'Qaim', ',', 'near', 'the', 'Syrian', 'border', '.'],
    'upos': ['PROPN', 'PUNCT', 'PROPN', 'PUNCT', 'ADJ', 'NOUN', 'VERB', ...],
    'xpos': ['NNP', 'HYPH', 'NNP', ':', 'JJ', 'NNS', 'VBD', 'NNP', 'NNP', 'NNP', 'HYPH', 'NNP', ',', 'DT', 'NN', 'IN', 'DT', 'NN', 'IN', 'DT', 'NN', 'IN', 'NNP', ',', 'IN', 'DT', 'JJ', 'NN', '.'],
    'feats': ['Number=Sing', None, 'Number=Sing', None, 'Degree=Pos', 'Number=Plur', 'Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin', 'Number=Sing', 'Number=Sing', 'Number=Sing', None, 'Number=Sing', None, 'Definite=Def|PronType=Art', 'Number=Sing', None, 'Definite=Def|PronType=Art', 'Number=Sing', None, 'Definite=Def|PronType=Art', 'Number=Sing', None, 'Number=Sing', None, None, 'Definite=Def|PronType=Art', 'Degree=Pos', 'Number=Sing', None], 
    'head': [0, 3, 1, 7, 6, 7, 1, ...],
    'deprel': ['root', 'punct', 'flat', 'punct', 'amod', 'nsubj', 'parataxis', 'obj', 'flat', 'flat', 'punct', 'flat', 'punct', 'det', 'appos', 'case', 'det', 'nmod', 'case', 'det', 'nmod', 'case', 'nmod', 'punct', 'case', 'det', 'amod', 'nmod', 'punct'], 
    'deps': ['0:root', '3:punct', '1:flat', '7:punct', '6:amod', '7:nsubj', '1:parataxis', '7:obj', '8:flat', '8:flat', '12:punct', '8:flat', '15:punct', '15:det', '8:appos', '18:case', '18:det', '15:nmod:at', '21:case', '21:det', '18:nmod:in', '23:case', '21:nmod:of', '28:punct', '28:case', '28:det', '28:amod', '21:nmod:near', '1:punct'], 
    'misc': ['SpaceAfter=No', 'SpaceAfter=No', None, None, None, None, None, None, None, 'SpaceAfter=No', 'SpaceAfter=No', 'SpaceAfter=No', None, None, None, None, None, None, None, None, None, None, 'SpaceAfter=No', None, None, None, None, 'SpaceAfter=No', None], 
    'mwt': [],
    'empty_nodes': []
}
```

*MWT Example (French):**

```python
dataset = load_dataset("universal-dependencies/universal_dependencies", "fr_gsd", split="train")
# Find sentence with MWT
example = [ex for ex in dataset if ex['mwt']][0]
print(example['mwt'])

# Output:
[{'id': '8-9', 'form': 'des', 'feats': None, 'misc': None}]
# This means example['tokens'][7:9] = ['de', 'les'] are combined as MWT surface form "des"
```

### Data Splits

The file `metadata.json` stores additional information about the data, for example, available splits:

```python
from huggingface_hub import hf_hub_download
import json

md = hf_hub_download(repo_id="universal-dependencies/universal_dependencies", filename="metadata.json", repo_type="dataset")

with open(md, "r", encoding="utf-8") as f:
    metadata = json.load(f)

[metadata[key]['splits'].keys() for key in metadata]
```

## Dataset Creation

### Curation Rationale

This Hugging Face distribution packages official Universal Dependencies release
snapshots as Parquet configurations, one configuration per treebank. The goal is
to make UD releases loadable with the standard `datasets` Parquet path, without
remote code, while preserving the original CoNLL-U linguistic annotations.

### Source Data

#### Initial Data Collection and Normalization

The source data is the official UD 2.18 release snapshot published via the
LINDAT/CLARIAH-CZ repository. During generation, the release archive is
downloaded unchanged, treebank metadata is extracted from the release files, and
CoNLL-U files are converted to Parquet. The conversion preserves regular tokens,
multi-word tokens, empty nodes, comments, and dependency annotations.

#### Who are the source language producers?

Source language producers vary by treebank and corpus. Individual treebanks may
contain material from published corpora, web text, Wikipedia-style text,
parallel corpora, spoken transcripts, learner data, historical texts, or other
language resources. Consult the corresponding upstream treebank README and
license information for provenance details.

### Annotations

#### Annotation process

Annotations are produced by the individual UD treebank teams according to the
Universal Dependencies guidelines. This repository does not revise the
linguistic annotation; it converts the released CoNLL-U files to Parquet and
validates token-level fidelity against the original release files.

#### Who are the annotators?

Annotators, maintainers, and contributors are specific to each treebank and are
listed in the corresponding upstream treebank README and release citation when
available. The aggregate UD release citation below lists contributors to the
release as a whole.

### Personal and Sensitive Information

Personal or sensitive information depends on the source corpora included by
individual treebanks. This Parquet distribution does not add new source text and
does not perform additional anonymization beyond what is present in the
official UD release. Users should review the upstream treebank documentation and
license terms for the subsets they use.

## Considerations for Using the Data

### Social Impact of Dataset

Universal Dependencies supports multilingual NLP research and tooling by
providing comparable morphosyntactic annotation across many languages. Coverage
is uneven across languages, domains, and varieties, so downstream systems should
not treat the dataset as a balanced representation of language use worldwide.

### Discussion of Biases

Biases reflect the source corpora and annotation histories of the individual
treebanks. Many languages, domains, genres, registers, and speaker communities
are underrepresented or absent. Annotation decisions are harmonized through UD
guidelines, but treebanks may still differ in source material, annotation
practice, and historical development.

### Other Known Limitations

This dataset is a release snapshot, not a live mirror of UD development
branches. Treebank contents, licenses, and annotation choices should be checked
against the corresponding upstream documentation when a project depends on a
specific language, corpus, or legal condition. The Parquet conversion preserves
the release data, but users needing byte-identical CoNLL-U files should use the
official UD release archives.

## Additional Information

### Dataset Curators

Universal Dependencies is maintained by the Universal Dependencies community.
This Hugging Face Parquet distribution is maintained under the official
`universal-dependencies` organization.

### Licensing Information
Universal Dependencies is a collection of linguistic data and tools. Each of
the treebanks has its own license terms and you (the "User") are responsible
for complying with the license terms applicable to those parts of UD which you
use.

Details about the License Terms:
* https://lindat.mff.cuni.cz/repository/xmlui/page/license-ud-2.18

The `./tools/` are licensed under the [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) license.

### Citation Information

Please cite the Universal Dependencies release used in your work. If you use a
specific treebank, find the corresponding upstream repository in the
[`UniversalDependencies`](https://github.com/UniversalDependencies)
organization and also cite the treebank-specific references listed in that
treebank's README when available. The `dirname` field in `metadata.json` gives
the upstream repository name, for example `UD_English-EWT`.

```bibtex
@misc{11234/1-6149,
   title = {Universal Dependencies 2.18},
   author = {Zeman, Daniel and Nivre, Joakim and Abid, Rimsha and Abrams, Mitchell and Ackermann, Elia and Adolphe, Jephtey and Aepli, No{\"e}mi and Afzal, Muhammad and Agi{\'c}, {\v Z}eljko and Ahrenberg, Lars and Ajede, Chika Kennedy and Akhundjanova, Arofat and Akkurt, Furkan and Albek, Orly and Aleksandravi{\v c}i{\=u}t{\.e}, Gabriel{\.e} and Alexandre, Dominick Maia and Alfina, Ika and Algom, Avner and Alnajjar, Khalid and Alzetta, Chiara and Anastasopoulos, Antonios and Andersen, Erik and Andrews, Kirk and Andrews, Matthew and Antonsen, Lene and Aoyama, Tatsuya and Aplonova, Katya and Aquino, Angelina and Aragon, Carolina and Aranes, Glyd and Aranzabe, Maria Jesus and Ar{\i}can, Bilge Nas and Arnard{\'o}ttir, {\t H}{\'o}runn and Aroonmanakun, Wirote and Arutie, Gashaw and Arwidarasti, Jessica Naraiswari and Asadpour, Hiwa and Asahara, Masayuki and {\'A}sgeirsd{\'o}ttir, Katla and Aslan, Deniz Baran and Asmazo{\u g}lu, Cengiz and Ateyah, Luma and Atmaca, Furkan and Attia, Mohammed and Atutxa, Aitziber and Augustinus, Liesbeth and Avel{\~a}s, Mariana and Aziz, Salwan and Badmaeva, Elena and Bajorat, Jana and Balasubramani, Keerthana and Ballesteros, Miguel and Banerjee, Esha and Bank, Sebastian and Barbosa, Bryan Khelven da Silva and Barbu Mititelu, Verginica and Barkarson, Starkaður and Basile, Rodolfo and Basmov, Victoria and Batchelor, Colin and Bauer, John and Bedir, Seyyit Talha and Begum, Zarina and Behzad, Shabnam and Beiner, Nathana{\"e}l and Belieni, Juan and B{\'e}mov{\'a}, Alevtina and Bengoetxea, Kepa and Benli, İbrahim and Ben Moshe, Yifat and Benzerrak, Marie and Berdicevskis, Aleksandrs and Berg, Ansu and Berk, G{\"o}zde and Bernhard, Delphine and Berntsson Ingelstam, Astrid and Bhat, Riyaz Ahmad and Biagetti, Erica and Bick, Eckhard and Bielinskien{\.e}, Agn{\.e} and Bilgin Ta{\c s}demir, Esma Fat{\i}ma and Binici, Helin and Bjarnad{\'o}ttir, Krist{\'{\i}}n and {BK}, Samuel and Blaschke, Verena and Blokland, Rogier and B{\"o}bel, Nina and Bobicev, Victoria and Boizou, Lo{\"{\i}}c and Bompolas, Stavros and Bona, Morgane and Bonilla, Johnatan and Borges V{\"o}lker, Emanuel and Borin, Lars and B{\"o}rstell, Carl and Bosco, Cristina and Bouma, Gosse and Bowman, Sam and Boyd, Adriane and Braggaar, Anouck and Branco, Ant{\'o}nio and Bras, Myriam and Brauner, Elisheva and Brillet, Th{\'e}o and Brokait{\.e}, Kristina and Bu, Lanni and Bur{\'a}{\v n}ov{\'a}, Eva and Burchardt, Aljoscha and Cabeza, Carmen and C{\'a}ceres Arandia, Natalia and Caftanatov, Olesea and Campos, Marisa and Candito, Marie and Cappello, Caterina Maria and Caron, Bernard and Caron, Gauthier and Carvalheiro, Catarina and Carvalho, Rita and Cassidy, Lauren and Castro, Maria Clara and Castro, S{\'e}rgio and Cavalcanti, Tatiana and Cebiro{\u g}lu Eryi{\u g}it, G{\"u}l{\c s}en and Cecchini, Flavio Massimiliano and Celano, Giuseppe G. A. and {\c C}epani, Anila and {\v C}{\'e}pl{\"o}, Slavom{\'{\i}}r and Cesur, Neslihan and Cetin, Savas and {\c C}etino{\u g}lu, {\"O}zlem and Chalub, Fabricio and Chamila, Liyanage and Chamoreau, Claudine and Chaudhary, Aditi and Chauhan, Shweta and Chen, Yifei and Chi, Ethan and Chika, Taishi and Cho, Yongseok and Choi, Jinho and Chontaeva, Bermet and Chun, Jayeol and Chung, Juyeon and Cignarella, Alessandra T. and Cinkov{\'a}, Silvie and Cocco, Esther and Collomb, Aur{\'e}lie and {\c C}{\"o}ltekin, {\c C}a{\u g}r{\i} and Connor, Miriam and Corbetta, Claudia and Corbetta, Daniela and Costa, Francisco and Courtin, Marine and Crabb{\'e}, Beno{\^{\i}}t and Cristescu, Mihaela and Cvetkoski, Vladimir and Dahan, Netanel and Dale, Ingerid L{\o}yning and D'Al{\`{\i}}, Sabrina and Daniel, Philemon and Danielyan, Anna S. and Daoudi, Khensa and Dash, Bijayalaxmi and Dash, Satya Ranjan and Davidson, Elizabeth and de Alencar, Leonel Figueiredo and Dehouck, Mathieu and de Laurentiis, Martina and de Marneffe, Marie-Catherine and Demir, Ahmet and de Paiva, Valeria and Derin, Mehmet Oguz and de Souza, Elvis and Diaz de Ilarraza, Arantza and D{\'{\i}}az Hern{\'a}ndez, Roberto Antonio and Dickerson, Carly and Di Felippo, Ariani and Dinakaramani, Arawinda and Di Nuovo, Elisa and Dione, Bamba and Dirix, Peter and Do, Hoa and Dobrovoljc, Kaja and Dogan, Mah{\^{\i}}r and D{\"o}hmer, Caroline and Doyle, Adrian and Dozat, Timothy and Droganova, Kira and Duran, Magali Sanches and Dwivedi, Puneet and Dyer, Andrew Thomas and Ebert, Christian and Eckhoff, Hanne and Eguchi, Masaki and Eiche, Sandra and Eiselen, Roald and Eli, Marhaba and Elkahky, Ali and Ephrem, Binyam and Erina, Olga and Erjavec, Toma{\v z} and Esher, Louise and Eslami, Soudabeh and Essaidi, Farah and Etienne, Aline and Evelyn, Wograine and Facundes, Sidney and Farkas, Rich{\'a}rd and Faryad, J{\'a}n and Favero, Federica and Ferdaousi, Jannatul and Fernanda, Mar{\'{\i}}lia and Fernandez Alcalde, Hector and Fethi, Amal and Foster, Jennifer and Francioni, Barbara and Fransen, Theodorus and Freitas, Cl{\'a}udia and Fuchs, Shlomit and Fujita, Kazunori and Gajdo{\v s}ov{\'a}, Katar{\'{\i}}na and Galbraith, Daniel and Galves, Charlotte Chambelland and Galy, Edith and Gamba, Federica and Garcia, Marcos and Garc{\'{\i}}a-Miguel, Jos{\'e} Mar{\'{\i}}a and G{\"a}rdenfors, Moa and Gaustad, Tanja and Gen{\c c}, Efe Eren and Gerardi, Fabr{\'{\i}}cio Ferraz and Gerdes, Kim and Gessler, Luke and Ginter, Filip and Godoy, Gustavo and Goenaga, Iakes and Gojenola, Koldo and G{\"o}k{\i}rmak, Memduh and Goldberg, Yoav and Goldin, Gili and G{\'o}mez Guinovart, Xavier and Gonz{\'a}lez Saavedra, Berta and Goux, Mathieu and Grand-Clement, Caroline and Grici{\=u}t{\.e}, Bernadeta and Grioni, Matias and Grobol, Lo{\"{\i}}c and Gr{\=u}z{\={\i}}tis, Normunds and Guglielmetti, Mario and Guillaume, Bruno and Guiller, Kirian and Guillot-Barbance, C{\'e}line and G{\"u}ng{\"o}r, Tunga and Gurevich, Vladimir and Habash, Nizar and Hafsteinsson, Hinrik and Hahn, Michael and Haji{\v c}, Jan and Haji{\v c} jr., Jan and Haji{\v c}ov{\'a}, Eva and H{\"a}m{\"a}l{\"a}inen, Mika and H{\`a} M{\~y}, Linh and Han, Na-Rae and Hanifmuti, Muhammad Yudistira and Harada, Takahiro and Hardwick, Sam and Harris, Kim and Hassert, Na{\"{\i}}ma and Haug, Dag and Havelka, Ji{\v r}{\'{\i}} and Heinecke, Johannes and Hellwig, Oliver and Hennig, Felix and Hladk{\'a}, Barbora and Hlav{\'a}{\v c}ov{\'a}, Jaroslava and Hociung, Florinel and Hoefels, Diana and Hoff, Barbara and Hohle, Petter and Howell, Nick and Huang, Yidi and Huerta Mendez, Marivel and Hwang, Jena and Ikeda, Takumi and Iliadou, Inessa and Ingason, Anton Karl and Ion, Radu and Irimia, Elena and Ishola, {\d O}l{\'a}j{\'{\i}}d{\'e} and Islamaj, Artan and Ito, Kaoru and Iurescia, Federica and Ivani, Jessica K. and Jagodzi{\'n}ska, Sandra and Jannat, Siratun and Jel{\'{\i}}nek, Tom{\'a}{\v s} and Jha, Apoorva and Jiamsundutsadee, Ratanon and Jiang, Katharine and Job, Sylvanus and Jobanputra, Mayank and Johannsen, Anders and J{\'o}nsd{\'o}ttir, Hildur and J{\o}rgensen, Fredrik and Ju, Zhuoxuan and Juarez Huerta, Mar{\'{\i}}a Ximena and Juutinen, Markus and Ka{\c s}{\i}kara, H{\"u}ner and Kabaeva, Nadezhda and Kahane, Sylvain and Kanayama, Hiroshi and Kanerva, Jenna and Kara, Neslihan and Karah{\'o}ǧa, Ritv{\'a}n and K{\'a}rn{\'{\i}}k, Ji{\v r}{\'{\i}} and K{\aa}sen, Andre and Kayadelen, Tolga and Kengatharaiyer, Sarveswaran and Kettnerov{\'a}, V{\'a}clava and Khan, Ali Haider and Kharatyan, Lilit and Kirchner, Jesse and Klementieva, Elena and Klironomou, Christina and Klyachko, Elena and Kocharov, Petr and K{\"o}hn, Arne and K{\"o}ksal, Abdullatif and Kol{\'a}{\v r}ov{\'a}, Veronika and Kopacewicz, Kamil and Korkiakangas, Timo and K{\"o}se, Mehmet and Koshevoy, Alexey and Kote, Nelda and Kotsyba, Natalia and Kova{\v c}i{\'c}, Barbara and Kovalevskait{\.e}, Jolanta and Kowner, Emmanuelle and Krek, Simon and Krishnamurthy, Parameswari and K{\"u}bler, Sandra and Ku{\v c}ov{\'a}, Lucie and Kuqi, Adrian and Kuriyozov, Elmurod and Kushare, Pranav and Kuyruk{\c c}u, O{\u g}uzhan and Kuzgun, Asl{\i} and Kwak, Sookyoung and Kyle, Kris and Laan, K{\"a}bi and Laippala, Veronika and Lambertino, Lorenzo and Landau, Israel and Lando, Tatiana and Larasati, Septina Dian and Larriv{\'e}e, Pierre and Lata, Kusum and Lavrentiev, Alexei and Lee, John and L{\^e} H{\`{\^o}}ng, Phương and Lenci, Alessandro and Leong, Wei Qi and Lertpradit, Saran and Leung, Herman and Levin, Lori and Levina, Maria and Levine, Lauren and Li, Cheuk Ying and Li, Josie and Li, Keying and Li, Yixuan and Li, Yuan and Lim, {KyungTae} and Lima Padovani, Bruna and Lin, Yi-Ju Jessica and Lind{\'e}n, Krister and Lindenbaum, Yitzchak and Liu, Yang Janet and Liu, Zoey and Ljube{\v s}i{\'c}, Nikola and Lobzhanidze, Irina and Loginova, Olga and Lopatkov{\'a}, Mark{\'e}ta and Lopes, Lucelene and Luftiu, Edita and Lukashevskyi, Arsenii and Lusito, Stefano and Lutgen, Anne-Marie and Luthfi, Andry and Luukko, Mikko and Lyashevskaya, Olga and Lynn, Teresa and Macketanz, Vivien and Mahamdi, Menel and Maillard, Jean and Maitreenukul, Punyanuch and Makarchuk, Ilya and Makazhanov, Aibek and Mambrini, Francesco and Mandl, Michael and Manning, Christopher and Manurung, Ruli and Mar{\c s}an, B{\"u}{\c s}ra and M{\u a}r{\u a}nduc, C{\u a}t{\u a}lina and Mare{\v c}ek, David and Marheinecke, Katrin and Markantonatou, Stella and M{\'a}rquez Hern{\'a}ndez, {\'A}ngeles and Mart{\'{\i}}nez Alonso, H{\'e}ctor and Mart{\'{\i}}n Rodr{\'{\i}}guez, Lorena and Martins, Andr{\'e} and Martins, Cl{\'a}udia and Masciolini, Arianna and Ma{\v s}ek, Jan and Matlatipov, Sanatbek and Matsuda, Hiroshi and Matsumoto, Yuji and Mauri, Caterina and Mazzei, Alessandro and {McDonald}, Ryan and {McGuinness}, Sarah and Mehta, Maitrey and Meiri, Ephraim and M{\'e}nard, Pierre Andr{\'e} and Mendon{\c c}a, Gustavo and Merhav, Hilla and Merzhevich, Tatiana and Meurer, Paul and Miekka, Niko and Mikulov{\'a}, Marie and Milano, Emilia and Mileti{\'c}, Aleksandra and Miller, Aaron and Min, Junghyun and Minerbi, Yael and M{\'{\i}}rovsk{\'y}, Ji{\v r}{\'{\i}} and Mischenkova, Karina and Missil{\"a}, Anna and Mititelu, C{\u a}t{\u a}lin and Mitrofan, Maria and Miyao, Yusuke and Mohapatra, Biswakalpita and Moln{\'a}r, Judit and Moloodi, Amirsaeid and Montemagni, Simonetta and More, Amir and Moreno Romero, Laura and Moretti, Giovanni and Mori, Shinsuke and Morioka, Tomohiko and Moro, Shigeki and Mortensen, Bjartur and Moskalevskyi, Bohdan and Mouzou, Katerina and Muischnek, Kadri and Munro, Robert and Murawaki, Yugo and Mus, Nikolett and M{\"u}{\"u}risep, Kaili and Nainwani, Pinkey and Nakhl{\'e}, Mariam and Nassajian, Minoo and Navarro Hor{\~n}iacek, Juan Ignacio and Nedoluzhko, Anna and Ne{\v s}pore-B{\=e}rzkalne, Gunta and Nevaci, Manuela and Nguy{\~{\^e}}n Th{\d i}, Lương and Nguy{\~{\^e}}n Th{\d i} Minh, Huy{\`{\^e}}n and Nikaido, Yoshihiro and Nikolaev, Vitaly and Nitisaroj, Rattima and Norrman, Victor and Nourian, Alireza and Nov{\'a}k, Michal and Nunes, Maria das Gra{\c c}as Volpe and Nurmi, Hanna and O'Brien, Colleen Alena and Ojala, Stina and Ojha, Atul Kr. and {\'O}lad{\'o}ttir, Hulda and Ol{\'u}{\`o}kun, Ad{\'e}day{\d o}̀ and Omura, Mai and Onwuegbuzia, Emeka and Ordan, Noam and Osenova, Petya and {\"O}stling, Robert and Ott, Annika and {\O}vrelid, Lilja and Oya, Masanori and {\"O}zate{\c s}, {\c S}aziye Bet{\"u}l and {\"O}z{\c c}elik, Merve and {\"O}zg{\"u}r, Arzucan and {\"O}zt{\"u}rk Ba{\c s}aran, Balk{\i}z and Paccosi, Teresa and Pajas, Petr and Palakapilly, Thomas and Palmero Aprosio, Alessio and Panevov{\'a}, Jarmila and Pannitto, Ludovica and Panova, Anastasia and Pardo, Thiago Alexandre Salgueiro and Parida, Shantipriya and Park, Hyunji Hayley and Partanen, Niko and Pascual, Elena and Pasparaki, Thelka and Passarotti, Marco and Patejuk, Agnieszka and Paulino-Passos, Guilherme and Pedonese, Giulia and Peeters, Oggi and Peljak-{\L}api{\'n}ska, Angelika and Peng, Siyao and Peng, Siyao Logan and Pereira, Rita and Pereira, S{\'{\i}}lvia and Perez, Cenel-Augusto and Perkova, Natalia and Perrier, Guy and Petrov, Slav and Petrova, Daria and Pettersson, Eva and Peverelli, Andrea and Phelan, Jason and Pierre-Louis, Claudel and Piitulainen, Jussi and Pinter, Yuval and Pinto, Clara and Pintucci, Rodrigo and Pirinen, Tommi A and Pitler, Emily and Plamada, Magdalena and Plank, Barbara and Plum, Alistair and Poibeau, Thierry and Polpanumas, Charin and Ponomareva, Larisa and Popel, Martin and Poujade, Clamen{\c c}a and Prangwedana, Rangga Prangwedana and Pretkalni{\c n}a, Lauma and Pretorius, Rigardt and Pr{\'e}vost, Sophie and Prokopidis, Prokopis and Przepi{\'o}rkowski, Adam and Pugh, Robert and Puolakainen, Tiina and Purschke, Christoph and Pyysalo, Sampo and Qi, Peng and Querido, Andreia and R{\"a}{\"a}bis, Andriela and Rabinovich, Ella and Rademaker, Alexandre and Rahman, Mutee-u and Rahoman, Mizanur and Rama, Taraka and Ramasamy, Loganathan and Ramisch, Carlos and Ramos, Joana and Rashel, Fam and Rasooli, Mohammad Sadegh and Ravishankar, Vinit and Real, Livy and Rebeja, Petru and Reddy, Siva and Regnault, Mathilde and Rehm, Georg and Riabi, Arij and Riabov, Ivan and Rie{\ss}ler, Michael and Rimkut{\.e}, Erika and Rinaldi, Larissa and Rituma, Laura and Rizqiyah, Putri and Rocha, Luisa and R{\"o}gnvaldsson, Eir{\'{\i}}kur and Roksandic, Ivan and Roman, Norton Trevisan and Romanenko, Mykhailo and Romanova, Natalia and Rosa, Rudolf and Roșca, Valentin and Roulon, Paulette and Rovati, Davide and Rozonoyer, Ben and Rudina, Olga and Rueter, Jack and Ruffolo, Paolo and R{\'u}narsson, Kristj{\'a}n and Rushiti, Rozana and Rutherford, Attapol T. and Sadde, Shoval and Safari, Pegah and Sahala, Aleksi and Sahoo, Kalyanamalini and Sahoo, Saraswati and Saleh, Shadi and Salomoni, Alessio and Samard{\v z}i{\'c}, Tanja and Sammani, Warangana and Sampanis, Konstantinos and Samson, Stephanie and S{\'a}nchez-Rodr{\'{\i}}guez, Xulia and Sandalo, Filomena Spatti and Sanguinetti, Manuela and San{\i}yar, Ezgi and S{\"a}rg, Dage and Sartor, Marta and Sarymsakova, Albina and Sasaki, Mitsuya and Saul{\={\i}}te, Baiba and Savary, Agata and Sawanakunanon, Yanin and Saxena, Shefali and Scannell, Kevin and Scarlata, Salvatore and Schang, Emmanuel and Schikowski, Robert and Schneider, Nathan and Schuster, Sebastian and Schwartz, Lane and Seddah, Djam{\'e} and Seeker, Wolfgang and Sellmer, Sven and Sengupta, Kaushik and Seraji, Mojgan and {\v S}ev{\v c}{\'{\i}}kov{\'a}, Magda and Sgall, Petr and Shahzadi, Syeda and Shen, Mo and Shimada, Atsuko and Shin, Gyu-Ho and Shirasu, Hiroyuki and Shishkina, Yana and Shmidman, Avi and Shohibussirri, Muh and Shvedova, Maria and Sibille, Jean and Siewert, Janine and Sigurðsson, Einar Freyr and Silva, Jo{\~a}o and Silveira, Aline and Silveira, Natalia and Silveira, Sara and Simi, Maria and Simionescu, Radu and Simk{\'o}, Katalin and {\v S}imkov{\'a}, M{\'a}ria and S{\'{\i}}monarson, Haukur Barri and Simov, Kiril and Sitchinava, Dmitri and Sither, Ted and Smith, Aaron and Soares-Bastos, Isabela and Solberg, Per Erik and Sollberger, Dolores and Sonnenhauser, Barbara and Sourov, Shafi and Speransky, Nina and Sprugnoli, Rachele and Sriwirote, Panyut and Stamou, Vivian and Steingr{\'{\i}}msson, Stein{\t h}{\'o}r and Stella, Antonio and {\v S}t{\v e}p{\'a}nek, Jan and {\v S}t{\v e}p{\'a}nkov{\'a}, Barbora and Stephen, Abishek and Straka, Milan and Strass, Omer and Strickland, Emmett and Strnadov{\'a}, Jana and Stymne, Sara and Suhr, Alane and Sulestio, Yogi Lesmana and Sulubacak, Umut and Sun, Jack and Sung, Hakyung and Suzuki, Shingo and Swanson, Daniel and Sz{\'a}nt{\'o}, Zsolt and Szawerna, Maria Irena and Taguchi, Chihiro and Taji, Dima and Tal, Rachel and Talamo, Luigi and Tamburini, Fabio and Tan, Mary Ann C. and Tanaka, Takaaki and Tanaya, Dipta and Tavoni, Mirko and Teker, Nursena and Tella, Samson and Tellier, Isabelle and Testori, Marinella and Thanyawong, Santhawat and Thomas, Guillaume and T{\i}ra{\c s}, Tar{\i}k Emre and Tjhi, William Chandra and Tollersrud, Thea and Tomaszek, Kamil and Tonelli, Sara and Torga, Liisi and Toribio, Lucas and Toska, Marsida and Trosterud, Trond and Trukhina, Anna and Tsarfaty, Reut and Tulchynska, Kira and T{\"u}rk, Utku and Tyers, Francis and {\t H}{\'o}rðarson, Sveinbj{\"o}rn and {\t H}orsteinsson, Vilhj{\'a}lmur and Uematsu, Sumire and Untilov, Roman and Ure{\v s}ov{\'a}, Zde{\v n}ka and Uria, Larraitz and Uszkoreit, Hans and Utka, Andrius and Vagnoni, Elena and Vajjala, Sowmya and Vak, Socrates and Vakirtzian, Socrates and van der Goot, Rob and Vanhove, Martine and van Niekerk, Daniel and van Noord, Gertjan and Varga, Viktor and Vaz, Helena and Vedenina, Uliana and Venturi, Giulia and Vergez-Couret, Marianne and Verkerk, Annemarie and Veronesi, Luiz and Veselovsky, Anna and Vidov{\'a} Hladk{\'a}, Barbora and Villemonte de la Clergerie, Eric and Vincze, Veronika and Vissamsetty, Anishka and Vlasova, Natalia and Vligouridou, Eleni and Vogel, Alan and Wakasa, Aya and Wallenberg, Joel C. and Wallin, Lars and Walsh, Abigail and Wang, John and Washington, Jonathan North and Weissweiler, Leonie and Wendt, Maximilan and Widmer, Paul and Wieczorek, Aleksandra and Wigderson, Shira and Wijono, Sri Hartati and Wille, Vanessa Berwanger and Williams, Seyi and Winkler, Miriam and Wintner, Shuly and Wir{\'e}n, Mats and Wittern, Christian and Witzlack-Makarevich, Alena and Woldemariam, Tsegay and Wong, Tak-sum and Wr{\'o}blewska, Alina and Wu, Qishen and Yako, Mary and Yamashita, Kayo and Yamazaki, Naoki and Yan, Chunxiao and Yang, Qizhen and Yang, Xiulin and Yasuoka, Koichi and Yavrumyan, Marat M. and Yenice, Arife Bet{\"u}l and Y{\i}landilo{\u g}lu, Enes and Y{\i}ld{\i}z, Olcay Taner and Yu, Zhuoran and Yuliawati, Arlisa and {\v Z}abokrtsk{\'y}, Zden{\v e}k and Zahra, Shorouq and Zeldes, Amir and Zhang, Annie and Zhang, Larry and Zhou, He and Zhu, Hanzhi and Zhu, Yilun and Zhuravleva, Anna and Ziane, Rayan and Znoti{\c n}{\v s}, Art{\=u}rs and Zucchini, Eleonora},
   url = {http://hdl.handle.net/11234/1-6149},
   note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL})},
   copyright = {Licence Universal Dependencies v2.18},
   year = {2026}
}
```

For general UD v2 background, cite:

```bibtex
@inproceedings{nivre-etal-2020-universal,
    title = "{U}niversal {D}ependencies v2: An Evergrowing Multilingual Treebank Collection",
    author = "Nivre, Joakim  and
      de Marneffe, Marie-Catherine  and
      Ginter, Filip  and
      Haji{\v{c}}, Jan  and
      Manning, Christopher D.  and
      Pyysalo, Sampo  and
      Schuster, Sebastian  and
      Tyers, Francis  and
      Zeman, Daniel",
    booktitle = "Proceedings of the Twelfth Language Resources and Evaluation Conference",
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2020.lrec-1.497/",
    pages = "4034--4043"
}
```

### Repository History

The v2.0 Parquet rewrite was originally authored by Egon W. Stemle. This
dataset was formerly hosted at `commul/universal_dependencies` and is now
maintained at the official
[`universal-dependencies/universal_dependencies`](https://huggingface.co/datasets/universal-dependencies/universal_dependencies)
location.
