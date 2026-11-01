---
license: cc-by-4.0
task_categories:
- translation
pretty_name: Smol
size_categories:
- 10K<n<100K
language:
- aa
- ab
- abq
- ace
- ach
- ady
- aeb
- af
- ahr
- aii
- ak
- alz
- am
- apc
- apd
- ar
- arn
- arz
- as
- av
- awa
- ay
- ayl
- ba
- bal
- ban
- bbc
- bci
- bem
- ber
- bew
- bfq
- bfy
- bgq
- bho
- bik
- bjn
- bm
- bn
- bns
- bo
- br
- bra
- brh
- brx
- bts
- btx
- bua
- bug
- ccp
- ce
- cgg
- ch
- chk
- mhr
- ckb
- cnh
- crh
- crs
- ctg
- cv
- dhd
- din
- dje
- doi
- dov
- dv
- dyu
- dz
- ee
- efi
- en
- es
- fa
- ff
- fil
- fj
- fo
- fon
- fr
- fuc
- fur
- gaa
- glk
- gn
- gom
- grt
- gu
- gv
- ha
- hac
- hi
- hil
- hne
- hoc
- hrx
- iba
- id
- ig
- ilo
- is
- iso
- iu
- ja
- jam
- jdt
- kaa
- kac
- kbd
- kek
- kfy
- kg
- kha
- ki
- kjh
- kl
- km
- kn
- ko
- kr
- kri
- kru
- ks
- ktu
- kv
- lep
- lg
- li
- lif
- lij
- lmo
- ln
- ltg
- lu
- lua
- luo
- lus
- mad
- mag
- mai
- mak
- mam
- meo
- mfe
- mg
- mh
- min
- mjl
- ml
- mni
- mos
- mr
- ms
- mtr
- mwr
- my
- nd
- ndc
- ne
- new
- nhe
- noe
- nr
- nso
- nus
- nv
- ny
- oc
- om
- os
- pa
- pag
- pam
- pap
- pcm
- ps
- pt
- qu
- quc
- rhg
- rn
- rom
- ru
- rw
- sa
- sah
- sat
- scn
- sd
- se
- sg
- sgj
- shn
- si
- sjp
- skr
- sn
- so
- spv
- ss
- st
- sus
- sw
- syl
- szl
- ta
- tcy
- te
- tet
- th
- ti
- tig
- tiv
- tn
- to
- tpi
- trp
- ts
- tum
- ty
- tyv
- udm
- unr
- ur
- ve
- vec
- war
- wbr
- wo
- xh
- xnr
- xsr
- yo
- yua
- yue
- zap
- zh
- zu
- zza

configs:
  - config_name: smolsent__ru_kjh
    data_files:
      - split: train
        path: smolsent/ru_kjh.jsonl
  - config_name: smoldoc__ru_kjh
    data_files:
      - split: train
        path: smoldoc/ru_kjh.jsonl
  - config_name: gatitos__en_tig
    data_files:
      - split: train
        path: gatitos/en_tig.jsonl
  - config_name: smolsent__en_tig
    data_files:
      - split: train
        path: smolsent/en_tig.jsonl
  - config_name: smoldoc__en_tig
    data_files:
      - split: train
        path: smoldoc/en_tig.jsonl        
  - config_name: smolsent__en_chn
    data_files:
      - split: train
        path: smolsent/en_chm.jsonl
  - config_name: smolsent__ru_ce
    data_files:
      - split: train
        path: smolsent/ru_ce.jsonl
  - config_name: smolsent__en_es
    data_files:
      - split: train
        path: smolsent/en_es.jsonl
  - config_name: smolsent__en_dje
    data_files:
      - split: train
        path: smolsent/en_dje.jsonl
  - config_name: smolsent__en_hac
    data_files:
      - split: train
        path: smolsent/en_hac.jsonl
  - config_name: smolsent__en_glk
    data_files:
      - split: train
        path: smolsent/en_glk.jsonl
  - config_name: smolsent__en_ckb
    data_files:
      - split: train
        path: smolsent/en_ckb.jsonl
  - config_name: smolsent__en_is
    data_files:
      - split: train
        path: smolsent/en_is.jsonl
  - config_name: smolsent__en_qu
    data_files:
      - split: train
        path: smolsent/en_qu.jsonl
  - config_name: smolsent__en_lij
    data_files:
      - split: train
        path: smolsent/en_lij.jsonl
  - config_name: smolsent__en_ay
    data_files:
      - split: train
        path: smolsent/en_ay.jsonl
  - config_name: smolsent__en_gn
    data_files:
      - split: train
        path: smolsent/en_gn.jsonl
  - config_name: smolsent__en_bo
    data_files:
      - split: train
        path: smolsent/en_bo.jsonl
  - config_name: smolsent__en_brx
    data_files:
      - split: train
        path: smolsent/en_brx.jsonl
  - config_name: smolsent__en_pa-Arab
    data_files:
      - split: train
        path: smolsent/en_pa-Arab.jsonl
  - config_name: smolsent__en_sat
    data_files:
      - split: train
        path: smolsent/en_sat.jsonl
  - config_name: smolsent__en_sat-Latn
    data_files:
      - split: train
        path: smolsent/en_sat-Latn.jsonl
  - config_name: smolsent__en_fuc
    data_files:
      - split: train
        path: smolsent/en_fuc.jsonl
  - config_name: smolsent__en_ff
    data_files:
      - split: train
        path: smolsent/en_ff.jsonl
  - config_name: smolsent__en_sa
    data_files:
      - split: train
        path: smolsent/en_sa.jsonl
  - config_name: smolsent__en_ks
    data_files:
      - split: train
        path: smolsent/en_ks.jsonl
  - config_name: smolsent__en_ks-Deva
    data_files:
      - split: train
        path: smolsent/en_ks-Deva.jsonl
  - config_name: smolsent__en_yue
    data_files:
      - split: train
        path: smolsent/en_yue.jsonl
  - config_name: smolsent__en_lus
    data_files:
      - split: train
        path: smolsent/en_lus.jsonl
  - config_name: smolsent__en_kl
    data_files:
      - split: train
        path: smolsent/en_kl.jsonl
  - config_name: smolsent__en_mni-Mtei
    data_files:
      - split: train
        path: smolsent/en_mni-Mtei.jsonl
  - config_name: smolsent__en_af
    data_files:
      - split: train
        path: smolsent/en_af.jsonl
  - config_name: smolsent__en_am
    data_files:
      - split: train
        path: smolsent/en_am.jsonl
  - config_name: smolsent__en_ny
    data_files:
      - split: train
        path: smolsent/en_ny.jsonl
  - config_name: smolsent__en_ha
    data_files:
      - split: train
        path: smolsent/en_ha.jsonl
  - config_name: smolsent__en_ig
    data_files:
      - split: train
        path: smolsent/en_ig.jsonl
  - config_name: smolsent__en_rw
    data_files:
      - split: train
        path: smolsent/en_rw.jsonl
  - config_name: smolsent__en_ln
    data_files:
      - split: train
        path: smolsent/en_ln.jsonl
  - config_name: smolsent__en_luo
    data_files:
      - split: train
        path: smolsent/en_luo.jsonl
  - config_name: smolsent__en_pcm
    data_files:
      - split: train
        path: smolsent/en_pcm.jsonl
  - config_name: smolsent__en_om
    data_files:
      - split: train
        path: smolsent/en_om.jsonl
  - config_name: smolsent__en_nso
    data_files:
      - split: train
        path: smolsent/en_nso.jsonl
  - config_name: smolsent__en_st
    data_files:
      - split: train
        path: smolsent/en_st.jsonl
  - config_name: smolsent__en_sn
    data_files:
      - split: train
        path: smolsent/en_sn.jsonl
  - config_name: smolsent__en_sw
    data_files:
      - split: train
        path: smolsent/en_sw.jsonl
  - config_name: smolsent__en_ber-Latn
    data_files:
      - split: train
        path: smolsent/en_ber-Latn.jsonl
  - config_name: smolsent__en_ak
    data_files:
      - split: train
        path: smolsent/en_ak.jsonl
  - config_name: smolsent__en_zu
    data_files:
      - split: train
        path: smolsent/en_zu.jsonl
  - config_name: smolsent__en_wo
    data_files:
      - split: train
        path: smolsent/en_wo.jsonl
  - config_name: smolsent__en_so
    data_files:
      - split: train
        path: smolsent/en_so.jsonl
  - config_name: smolsent__en_nd
    data_files:
      - split: train
        path: smolsent/en_nd.jsonl
  - config_name: smolsent__en_mg
    data_files:
      - split: train
        path: smolsent/en_mg.jsonl
  - config_name: smolsent__en_din
    data_files:
      - split: train
        path: smolsent/en_din.jsonl
  - config_name: smolsent__en_gaa
    data_files:
      - split: train
        path: smolsent/en_gaa.jsonl
  - config_name: smolsent__en_xh
    data_files:
      - split: train
        path: smolsent/en_xh.jsonl
  - config_name: smolsent__en_ts
    data_files:
      - split: train
        path: smolsent/en_ts.jsonl
  - config_name: smolsent__en_lg
    data_files:
      - split: train
        path: smolsent/en_lg.jsonl
  - config_name: smolsent__en_bm
    data_files:
      - split: train
        path: smolsent/en_bm.jsonl
  - config_name: smolsent__en_ve
    data_files:
      - split: train
        path: smolsent/en_ve.jsonl
  - config_name: smolsent__en_efi
    data_files:
      - split: train
        path: smolsent/en_efi.jsonl
  - config_name: smolsent__en_dyu
    data_files:
      - split: train
        path: smolsent/en_dyu.jsonl
  - config_name: smolsent__en_tn
    data_files:
      - split: train
        path: smolsent/en_tn.jsonl
  - config_name: smolsent__en_rn
    data_files:
      - split: train
        path: smolsent/en_rn.jsonl
  - config_name: smolsent__en_tiv
    data_files:
      - split: train
        path: smolsent/en_tiv.jsonl
  - config_name: smolsent__en_mfe
    data_files:
      - split: train
        path: smolsent/en_mfe.jsonl
  - config_name: smolsent__en_ti
    data_files:
      - split: train
        path: smolsent/en_ti.jsonl
  - config_name: smolsent__en_sus
    data_files:
      - split: train
        path: smolsent/en_sus.jsonl
  - config_name: smolsent__en_ndc
    data_files:
      - split: train
        path: smolsent/en_ndc.jsonl
  - config_name: smolsent__en_ki
    data_files:
      - split: train
        path: smolsent/en_ki.jsonl
  - config_name: smolsent__en_cgg
    data_files:
      - split: train
        path: smolsent/en_cgg.jsonl
  - config_name: smolsent__en_bem
    data_files:
      - split: train
        path: smolsent/en_bem.jsonl
  - config_name: smolsent__en_tum
    data_files:
      - split: train
        path: smolsent/en_tum.jsonl
  - config_name: smolsent__en_arz
    data_files:
      - split: train
        path: smolsent/en_arz.jsonl
  - config_name: smolsent__en_nr
    data_files:
      - split: train
        path: smolsent/en_nr.jsonl
  - config_name: smolsent__en_kr
    data_files:
      - split: train
        path: smolsent/en_kr.jsonl
  - config_name: smolsent__en_fon
    data_files:
      - split: train
        path: smolsent/en_fon.jsonl
  - config_name: smolsent__en_yo
    data_files:
      - split: train
        path: smolsent/en_yo.jsonl
  - config_name: smolsent__en_ee
    data_files:
      - split: train
        path: smolsent/en_ee.jsonl
  - config_name: smolsent__en_ar-MA
    data_files:
      - split: train
        path: smolsent/en_ar-MA.jsonl
  - config_name: smolsent__en_apd
    data_files:
      - split: train
        path: smolsent/en_apd.jsonl
  - config_name: smolsent__en_ss
    data_files:
      - split: train
        path: smolsent/en_ss.jsonl
  - config_name: smolsent__en_ayl
    data_files:
      - split: train
        path: smolsent/en_ayl.jsonl
  - config_name: smolsent__en_ktu
    data_files:
      - split: train
        path: smolsent/en_ktu.jsonl
  - config_name: smolsent__en_aeb
    data_files:
      - split: train
        path: smolsent/en_aeb.jsonl
  - config_name: smolsent__en_aa
    data_files:
      - split: train
        path: smolsent/en_aa.jsonl
  - config_name: smolsent__en_lu
    data_files:
      - split: train
        path: smolsent/en_lu.jsonl
  - config_name: smolsent__en_ach
    data_files:
      - split: train
        path: smolsent/en_ach.jsonl
  - config_name: smolsent__en_alz
    data_files:
      - split: train
        path: smolsent/en_alz.jsonl
  - config_name: smolsent__en_bci
    data_files:
      - split: train
        path: smolsent/en_bci.jsonl
  - config_name: smolsent__en_dov
    data_files:
      - split: train
        path: smolsent/en_dov.jsonl
  - config_name: smolsent__en_kg
    data_files:
      - split: train
        path: smolsent/en_kg.jsonl
  - config_name: smolsent__en_mos
    data_files:
      - split: train
        path: smolsent/en_mos.jsonl
  - config_name: smolsent__en_nqo
    data_files:
      - split: train
        path: smolsent/en_nqo.jsonl
  - config_name: smolsent__en_ber
    data_files:
      - split: train
        path: smolsent/en_ber.jsonl
  - config_name: smolsent__en_kri
    data_files:
      - split: train
        path: smolsent/en_kri.jsonl
  - config_name: smolsent__en_fil
    data_files:
      - split: train
        path: smolsent/en_fil.jsonl
  - config_name: smolsent__en_fa
    data_files:
      - split: train
        path: smolsent/en_fa.jsonl
  - config_name: smolsent__en_bn
    data_files:
      - split: train
        path: smolsent/en_bn.jsonl
  - config_name: smolsent__en_te
    data_files:
      - split: train
        path: smolsent/en_te.jsonl
  - config_name: smolsent__en_ta
    data_files:
      - split: train
        path: smolsent/en_ta.jsonl
  - config_name: smolsent__en_kn
    data_files:
      - split: train
        path: smolsent/en_kn.jsonl
  - config_name: smolsent__en_ml
    data_files:
      - split: train
        path: smolsent/en_ml.jsonl
  - config_name: smolsent__en_gu
    data_files:
      - split: train
        path: smolsent/en_gu.jsonl
  - config_name: smolsent__en_pa
    data_files:
      - split: train
        path: smolsent/en_pa.jsonl
  - config_name: smolsent__en_ur
    data_files:
      - split: train
        path: smolsent/en_ur.jsonl
  - config_name: smolsent__en_hi
    data_files:
      - split: train
        path: smolsent/en_hi.jsonl
  - config_name: smolsent__en_mr
    data_files:
      - split: train
        path: smolsent/en_mr.jsonl
  - config_name: smolsent__en_my
    data_files:
      - split: train
        path: smolsent/en_my.jsonl
  - config_name: smolsent__en_km
    data_files:
      - split: train
        path: smolsent/en_km.jsonl
  - config_name: smolsent__en_th
    data_files:
      - split: train
        path: smolsent/en_th.jsonl
  - config_name: smolsent__en_ja
    data_files:
      - split: train
        path: smolsent/en_ja.jsonl
  - config_name: smolsent__en_ko
    data_files:
      - split: train
        path: smolsent/en_ko.jsonl
  - config_name: smolsent__en_id
    data_files:
      - split: train
        path: smolsent/en_id.jsonl
  - config_name: smolsent__en_si
    data_files:
      - split: train
        path: smolsent/en_si.jsonl
  - config_name: smolsent__en_tyv
    data_files:
      - split: train
        path: smolsent/en_tyv.jsonl
  - config_name: smolsent__en_ne
    data_files:
      - split: train
        path: smolsent/en_ne.jsonl
  - config_name: smolsent__en_brh
    data_files:
      - split: train
        path: smolsent/en_brh.jsonl
  - config_name: smolsent__ru_jdt
    data_files:
      - split: train
        path: smolsent/ru_jdt.jsonl
  - config_name: smolsent__ru_abq
    data_files:
      - split: train
        path: smolsent/ru_abq.jsonl
  - config_name: smoldoc__en_dje
    data_files:
      - split: train
        path: smoldoc/en_dje.jsonl
  - config_name: smoldoc__ru_ce
    data_files:
      - split: train
        path: smoldoc/ru_ce.jsonl
  - config_name: smoldoc__en_fil
    data_files:
      - split: train
        path: smoldoc/en_fil.jsonl
  - config_name: smoldoc__en_ki
    data_files:
      - split: train
        path: smoldoc/en_ki.jsonl
  - config_name: smoldoc__en_ach
    data_files:
      - split: train
        path: smoldoc/en_ach.jsonl
  - config_name: smoldoc__en_aa
    data_files:
      - split: train
        path: smoldoc/en_aa.jsonl
  - config_name: smoldoc__en_lij
    data_files:
      - split: train
        path: smoldoc/en_lij.jsonl
  - config_name: smoldoc__en_bem
    data_files:
      - split: train
        path: smoldoc/en_bem.jsonl
  - config_name: smoldoc__en_cgg
    data_files:
      - split: train
        path: smoldoc/en_cgg.jsonl
  - config_name: smoldoc__en_din
    data_files:
      - split: train
        path: smoldoc/en_din.jsonl
  - config_name: smoldoc__en_fon
    data_files:
      - split: train
        path: smoldoc/en_fon.jsonl
  - config_name: smoldoc__en_gaa
    data_files:
      - split: train
        path: smoldoc/en_gaa.jsonl
  - config_name: smoldoc__en_kr
    data_files:
      - split: train
        path: smoldoc/en_kr.jsonl
  - config_name: smoldoc__en_lu
    data_files:
      - split: train
        path: smoldoc/en_lu.jsonl
  - config_name: smoldoc__en_mfe
    data_files:
      - split: train
        path: smoldoc/en_mfe.jsonl
  - config_name: smoldoc__en_rn
    data_files:
      - split: train
        path: smoldoc/en_rn.jsonl
  - config_name: smoldoc__en_nr
    data_files:
      - split: train
        path: smoldoc/en_nr.jsonl
  - config_name: smoldoc__en_ts
    data_files:
      - split: train
        path: smoldoc/en_ts.jsonl
  - config_name: smoldoc__en_tn
    data_files:
      - split: train
        path: smoldoc/en_tn.jsonl
  - config_name: smoldoc__en_aeb
    data_files:
      - split: train
        path: smoldoc/en_aeb.jsonl
  - config_name: smoldoc__en_ve
    data_files:
      - split: train
        path: smoldoc/en_ve.jsonl
  - config_name: smoldoc__en_alz
    data_files:
      - split: train
        path: smoldoc/en_alz.jsonl
  - config_name: smoldoc__en_dov
    data_files:
      - split: train
        path: smoldoc/en_dov.jsonl
  - config_name: smoldoc__en_dyu
    data_files:
      - split: train
        path: smoldoc/en_dyu.jsonl
  - config_name: smoldoc__en_ayl
    data_files:
      - split: train
        path: smoldoc/en_ayl.jsonl
  - config_name: smoldoc__en_ndc
    data_files:
      - split: train
        path: smoldoc/en_ndc.jsonl
  - config_name: smoldoc__en_nd
    data_files:
      - split: train
        path: smoldoc/en_nd.jsonl
  - config_name: smoldoc__en_tum
    data_files:
      - split: train
        path: smoldoc/en_tum.jsonl
  - config_name: smoldoc__en_bci
    data_files:
      - split: train
        path: smoldoc/en_bci.jsonl
  - config_name: smoldoc__en_ktu
    data_files:
      - split: train
        path: smoldoc/en_ktu.jsonl
  - config_name: smoldoc__en_kg
    data_files:
      - split: train
        path: smoldoc/en_kg.jsonl
  - config_name: smoldoc__en_apd
    data_files:
      - split: train
        path: smoldoc/en_apd.jsonl
  - config_name: smoldoc__en_ss
    data_files:
      - split: train
        path: smoldoc/en_ss.jsonl
  - config_name: smoldoc__en_efi
    data_files:
      - split: train
        path: smoldoc/en_efi.jsonl
  - config_name: smoldoc__en_tiv
    data_files:
      - split: train
        path: smoldoc/en_tiv.jsonl
  - config_name: smoldoc__en_mos
    data_files:
      - split: train
        path: smoldoc/en_mos.jsonl
  - config_name: smoldoc__en_sus
    data_files:
      - split: train
        path: smoldoc/en_sus.jsonl
  - config_name: smoldoc__en_nqo
    data_files:
      - split: train
        path: smoldoc/en_nqo.jsonl
  - config_name: smoldoc__en_am
    data_files:
      - split: train
        path: smoldoc/en_am.jsonl
  - config_name: smoldoc__en_sw
    data_files:
      - split: train
        path: smoldoc/en_sw.jsonl
  - config_name: smoldoc__en_yo
    data_files:
      - split: train
        path: smoldoc/en_yo.jsonl
  - config_name: smoldoc__en_ha
    data_files:
      - split: train
        path: smoldoc/en_ha.jsonl
  - config_name: smoldoc__en_yue
    data_files:
      - split: train
        path: smoldoc/en_yue.jsonl
  - config_name: smoldoc__en_ig
    data_files:
      - split: train
        path: smoldoc/en_ig.jsonl
  - config_name: smoldoc__en_mg
    data_files:
      - split: train
        path: smoldoc/en_mg.jsonl
  - config_name: smoldoc__en_om
    data_files:
      - split: train
        path: smoldoc/en_om.jsonl
  - config_name: smoldoc__en_xh
    data_files:
      - split: train
        path: smoldoc/en_xh.jsonl
  - config_name: smoldoc__en_ny
    data_files:
      - split: train
        path: smoldoc/en_ny.jsonl
  - config_name: smoldoc__en_ln
    data_files:
      - split: train
        path: smoldoc/en_ln.jsonl
  - config_name: smoldoc__en_wo
    data_files:
      - split: train
        path: smoldoc/en_wo.jsonl
  - config_name: smoldoc__en_sn
    data_files:
      - split: train
        path: smoldoc/en_sn.jsonl
  - config_name: smoldoc__en_rw
    data_files:
      - split: train
        path: smoldoc/en_rw.jsonl
  - config_name: smoldoc__en_st
    data_files:
      - split: train
        path: smoldoc/en_st.jsonl
  - config_name: smoldoc__en_ff
    data_files:
      - split: train
        path: smoldoc/en_ff.jsonl
  - config_name: smoldoc__en_lg
    data_files:
      - split: train
        path: smoldoc/en_lg.jsonl
  - config_name: smoldoc__en_luo
    data_files:
      - split: train
        path: smoldoc/en_luo.jsonl
  - config_name: smoldoc__en_scn
    data_files:
      - split: train
        path: smoldoc/en_scn.jsonl
  - config_name: smoldoc__en_ar-MA
    data_files:
      - split: train
        path: smoldoc/en_ar-MA.jsonl
  - config_name: smoldoc__en_ti
    data_files:
      - split: train
        path: smoldoc/en_ti.jsonl
  - config_name: smoldoc__en_zu
    data_files:
      - split: train
        path: smoldoc/en_zu.jsonl
  - config_name: smoldoc__en_ak
    data_files:
      - split: train
        path: smoldoc/en_ak.jsonl
  - config_name: smoldoc__en_arz
    data_files:
      - split: train
        path: smoldoc/en_arz.jsonl
  - config_name: smoldoc__en_bm
    data_files:
      - split: train
        path: smoldoc/en_bm.jsonl
  - config_name: smoldoc__en_so
    data_files:
      - split: train
        path: smoldoc/en_so.jsonl
  - config_name: smoldoc__en_pcm
    data_files:
      - split: train
        path: smoldoc/en_pcm.jsonl
  - config_name: smoldoc__en_nso
    data_files:
      - split: train
        path: smoldoc/en_nso.jsonl
  - config_name: smoldoc__en_af
    data_files:
      - split: train
        path: smoldoc/en_af.jsonl
  - config_name: smoldoc__en_ee
    data_files:
      - split: train
        path: smoldoc/en_ee.jsonl
  - config_name: smoldoc__en_kri
    data_files:
      - split: train
        path: smoldoc/en_kri.jsonl
  - config_name: smoldoc__en_ber-Latn
    data_files:
      - split: train
        path: smoldoc/en_ber-Latn.jsonl
  - config_name: smoldoc__en_ber
    data_files:
      - split: train
        path: smoldoc/en_ber.jsonl
  - config_name: smoldoc__en_kru
    data_files:
      - split: train
        path: smoldoc/en_kru.jsonl
  - config_name: smoldoc__en_hoc-Wara
    data_files:
      - split: train
        path: smoldoc/en_hoc-Wara.jsonl
  - config_name: smoldoc__en_bra
    data_files:
      - split: train
        path: smoldoc/en_bra.jsonl
  - config_name: smoldoc__en_bgq
    data_files:
      - split: train
        path: smoldoc/en_bgq.jsonl
  - config_name: smoldoc__en_trp
    data_files:
      - split: train
        path: smoldoc/en_trp.jsonl
  - config_name: smoldoc__en_xsr-Tibt
    data_files:
      - split: train
        path: smoldoc/en_xsr-Tibt.jsonl
  - config_name: smoldoc__en_grt-Latn
    data_files:
      - split: train
        path: smoldoc/en_grt-Latn.jsonl
  - config_name: smoldoc__en_bfq
    data_files:
      - split: train
        path: smoldoc/en_bfq.jsonl
  - config_name: smoldoc__en_ahr
    data_files:
      - split: train
        path: smoldoc/en_ahr.jsonl
  - config_name: smoldoc__en_ccp-Latn
    data_files:
      - split: train
        path: smoldoc/en_ccp-Latn.jsonl
  - config_name: smoldoc__en_xnr
    data_files:
      - split: train
        path: smoldoc/en_xnr.jsonl
  - config_name: smoldoc__en_lep
    data_files:
      - split: train
        path: smoldoc/en_lep.jsonl
  - config_name: smoldoc__en_kfy
    data_files:
      - split: train
        path: smoldoc/en_kfy.jsonl
  - config_name: smoldoc__en_lif-Limb
    data_files:
      - split: train
        path: smoldoc/en_lif-Limb.jsonl
  - config_name: smoldoc__en_mjl
    data_files:
      - split: train
        path: smoldoc/en_mjl.jsonl
  - config_name: smoldoc__en_ps
    data_files:
      - split: train
        path: smoldoc/en_ps.jsonl
  - config_name: smoldoc__en_unr-Deva
    data_files:
      - split: train
        path: smoldoc/en_unr-Deva.jsonl
  - config_name: smoldoc__en_tcy
    data_files:
      - split: train
        path: smoldoc/en_tcy.jsonl
  - config_name: smoldoc__en_sd-Deva
    data_files:
      - split: train
        path: smoldoc/en_sd-Deva.jsonl
  - config_name: smoldoc__en_bns
    data_files:
      - split: train
        path: smoldoc/en_bns.jsonl
  - config_name: smoldoc__en_wbr
    data_files:
      - split: train
        path: smoldoc/en_wbr.jsonl
  - config_name: smoldoc__en_mtr
    data_files:
      - split: train
        path: smoldoc/en_mtr.jsonl
  - config_name: smoldoc__en_sjp
    data_files:
      - split: train
        path: smoldoc/en_sjp.jsonl
  - config_name: smoldoc__en_spv
    data_files:
      - split: train
        path: smoldoc/en_spv.jsonl
  - config_name: smoldoc__en_mag
    data_files:
      - split: train
        path: smoldoc/en_mag.jsonl
  - config_name: smoldoc__en_sgj
    data_files:
      - split: train
        path: smoldoc/en_sgj.jsonl
  - config_name: smoldoc__en_noe
    data_files:
      - split: train
        path: smoldoc/en_noe.jsonl
  - config_name: smoldoc__en_doi
    data_files:
      - split: train
        path: smoldoc/en_doi.jsonl
  - config_name: smoldoc__en_dhd
    data_files:
      - split: train
        path: smoldoc/en_dhd.jsonl
  - config_name: smoldoc__en_bfy
    data_files:
      - split: train
        path: smoldoc/en_bfy.jsonl
  - config_name: smoldoc__zh_am
    data_files:
      - split: train
        path: smoldoc/zh_am.jsonl
  - config_name: smoldoc__ar_am
    data_files:
      - split: train
        path: smoldoc/ar_am.jsonl
  - config_name: smoldoc__zh_sw
    data_files:
      - split: train
        path: smoldoc/zh_sw.jsonl
  - config_name: smoldoc__ar_sw
    data_files:
      - split: train
        path: smoldoc/ar_sw.jsonl
  - config_name: smoldoc__en_ru
    data_files:
      - split: train
        path: smoldoc/en_ru.jsonl
  - config_name: smoldoc__en_fa
    data_files:
      - split: train
        path: smoldoc/en_fa.jsonl
  - config_name: smoldoc__en_bn
    data_files:
      - split: train
        path: smoldoc/en_bn.jsonl
  - config_name: smoldoc__en_gu
    data_files:
      - split: train
        path: smoldoc/en_gu.jsonl
  - config_name: smoldoc__en_hi
    data_files:
      - split: train
        path: smoldoc/en_hi.jsonl
  - config_name: smoldoc__en_kn
    data_files:
      - split: train
        path: smoldoc/en_kn.jsonl
  - config_name: smoldoc__en_ml
    data_files:
      - split: train
        path: smoldoc/en_ml.jsonl
  - config_name: smoldoc__en_mr
    data_files:
      - split: train
        path: smoldoc/en_mr.jsonl
  - config_name: smoldoc__en_pa
    data_files:
      - split: train
        path: smoldoc/en_pa.jsonl
  - config_name: smoldoc__en_ta
    data_files:
      - split: train
        path: smoldoc/en_ta.jsonl
  - config_name: smoldoc__en_te
    data_files:
      - split: train
        path: smoldoc/en_te.jsonl
  - config_name: smoldoc__en_ur
    data_files:
      - split: train
        path: smoldoc/en_ur.jsonl
  - config_name: smoldoc__en_my
    data_files:
      - split: train
        path: smoldoc/en_my.jsonl
  - config_name: smoldoc__en_id
    data_files:
      - split: train
        path: smoldoc/en_id.jsonl
  - config_name: smoldoc__en_th
    data_files:
      - split: train
        path: smoldoc/en_th.jsonl
  - config_name: smoldoc__en_ja
    data_files:
      - split: train
        path: smoldoc/en_ja.jsonl
  - config_name: smoldoc__en_km
    data_files:
      - split: train
        path: smoldoc/en_km.jsonl
  - config_name: smoldoc__en_ko
    data_files:
      - split: train
        path: smoldoc/en_ko.jsonl
  - config_name: smoldoc__en_si
    data_files:
      - split: train
        path: smoldoc/en_si.jsonl
  - config_name: smoldoc__en_chm
    data_files:
      - split: train
        path: smoldoc/en_chm.jsonl
  - config_name: smoldoc__en_tyv
    data_files:
      - split: train
        path: smoldoc/en_tyv.jsonl
  - config_name: smoldoc__ru_jdt
    data_files:
      - split: train
        path: smoldoc/ru_jdt.jsonl
  - config_name: smoldoc__en_ne
    data_files:
      - split: train
        path: smoldoc/en_ne.jsonl
  - config_name: smoldoc__en_brh
    data_files:
      - split: train
        path: smoldoc/en_brh.jsonl
  - config_name: smoldoc__ru_abq
    data_files:
      - split: train
        path: smoldoc/ru_abq.jsonl
  - config_name: gatitos__en_dje
    data_files:
      - split: train
        path: gatitos/en_dje.jsonl
  - config_name: gatitos__en_fr-CA
    data_files:
      - split: train
        path: gatitos/en_fr-CA.jsonl
  - config_name: gatitos__en_is
    data_files:
      - split: train
        path: gatitos/en_is.jsonl
  - config_name: gatitos__en_iu-Latn
    data_files:
      - split: train
        path: gatitos/en_iu-Latn.jsonl
  - config_name: gatitos__en_pt-PT
    data_files:
      - split: train
        path: gatitos/en_pt-PT.jsonl
  - config_name: gatitos__en_nhe
    data_files:
      - split: train
        path: gatitos/en_nhe.jsonl
  - config_name: gatitos__en_aii
    data_files:
      - split: train
        path: gatitos/en_aii.jsonl
  - config_name: gatitos__en_bjn
    data_files:
      - split: train
        path: gatitos/en_bjn.jsonl
  - config_name: gatitos__en_bjn-Arab
    data_files:
      - split: train
        path: gatitos/en_bjn-Arab.jsonl
  - config_name: gatitos__en_bci
    data_files:
      - split: train
        path: gatitos/en_bci.jsonl
  - config_name: gatitos__en_bem
    data_files:
      - split: train
        path: gatitos/en_bem.jsonl
  - config_name: gatitos__en_bua
    data_files:
      - split: train
        path: gatitos/en_bua.jsonl
  - config_name: gatitos__en_dov
    data_files:
      - split: train
        path: gatitos/en_dov.jsonl
  - config_name: gatitos__en_fur
    data_files:
      - split: train
        path: gatitos/en_fur.jsonl
  - config_name: gatitos__en_hrx
    data_files:
      - split: train
        path: gatitos/en_hrx.jsonl
  - config_name: gatitos__en_kr
    data_files:
      - split: train
        path: gatitos/en_kr.jsonl
  - config_name: gatitos__en_alz
    data_files:
      - split: train
        path: gatitos/en_alz.jsonl
  - config_name: gatitos__en_luo
    data_files:
      - split: train
        path: gatitos/en_luo.jsonl
  - config_name: gatitos__en_pap
    data_files:
      - split: train
        path: gatitos/en_pap.jsonl
  - config_name: gatitos__en_sg
    data_files:
      - split: train
        path: gatitos/en_sg.jsonl
  - config_name: gatitos__en_sus
    data_files:
      - split: train
        path: gatitos/en_sus.jsonl
  - config_name: gatitos__en_ty
    data_files:
      - split: train
        path: gatitos/en_ty.jsonl
  - config_name: gatitos__en_ab
    data_files:
      - split: train
        path: gatitos/en_ab.jsonl
  - config_name: gatitos__en_nqo
    data_files:
      - split: train
        path: gatitos/en_nqo.jsonl
  - config_name: gatitos__en_hne
    data_files:
      - split: train
        path: gatitos/en_hne.jsonl
  - config_name: gatitos__en_cgg
    data_files:
      - split: train
        path: gatitos/en_cgg.jsonl
  - config_name: gatitos__en_kv
    data_files:
      - split: train
        path: gatitos/en_kv.jsonl
  - config_name: gatitos__en_kg
    data_files:
      - split: train
        path: gatitos/en_kg.jsonl
  - config_name: gatitos__en_lij
    data_files:
      - split: train
        path: gatitos/en_lij.jsonl
  - config_name: gatitos__en_li
    data_files:
      - split: train
        path: gatitos/en_li.jsonl
  - config_name: gatitos__en_lmo
    data_files:
      - split: train
        path: gatitos/en_lmo.jsonl
  - config_name: gatitos__en_mos
    data_files:
      - split: train
        path: gatitos/en_mos.jsonl
  - config_name: gatitos__en_szl
    data_files:
      - split: train
        path: gatitos/en_szl.jsonl
  - config_name: gatitos__en_ss
    data_files:
      - split: train
        path: gatitos/en_ss.jsonl
  - config_name: gatitos__en_tiv
    data_files:
      - split: train
        path: gatitos/en_tiv.jsonl
  - config_name: gatitos__en_btx
    data_files:
      - split: train
        path: gatitos/en_btx.jsonl
  - config_name: gatitos__en_fj
    data_files:
      - split: train
        path: gatitos/en_fj.jsonl
  - config_name: gatitos__en_iso
    data_files:
      - split: train
        path: gatitos/en_iso.jsonl
  - config_name: gatitos__en_ltg
    data_files:
      - split: train
        path: gatitos/en_ltg.jsonl
  - config_name: gatitos__en_lua
    data_files:
      - split: train
        path: gatitos/en_lua.jsonl
  - config_name: gatitos__en_pag
    data_files:
      - split: train
        path: gatitos/en_pag.jsonl
  - config_name: gatitos__en_rn
    data_files:
      - split: train
        path: gatitos/en_rn.jsonl
  - config_name: gatitos__en_sat-Latn
    data_files:
      - split: train
        path: gatitos/en_sat-Latn.jsonl
  - config_name: gatitos__en_sat
    data_files:
      - split: train
        path: gatitos/en_sat.jsonl
  - config_name: gatitos__en_ch
    data_files:
      - split: train
        path: gatitos/en_ch.jsonl
  - config_name: gatitos__en_crh
    data_files:
      - split: train
        path: gatitos/en_crh.jsonl
  - config_name: gatitos__en_efi
    data_files:
      - split: train
        path: gatitos/en_efi.jsonl
  - config_name: gatitos__en_ki
    data_files:
      - split: train
        path: gatitos/en_ki.jsonl
  - config_name: gatitos__en_trp
    data_files:
      - split: train
        path: gatitos/en_trp.jsonl
  - config_name: gatitos__en_mam
    data_files:
      - split: train
        path: gatitos/en_mam.jsonl
  - config_name: gatitos__en_tyv
    data_files:
      - split: train
        path: gatitos/en_tyv.jsonl
  - config_name: gatitos__en_tum
    data_files:
      - split: train
        path: gatitos/en_tum.jsonl
  - config_name: gatitos__en_din
    data_files:
      - split: train
        path: gatitos/en_din.jsonl
  - config_name: gatitos__en_ks
    data_files:
      - split: train
        path: gatitos/en_ks.jsonl
  - config_name: gatitos__en_ndc
    data_files:
      - split: train
        path: gatitos/en_ndc.jsonl
  - config_name: gatitos__en_ban
    data_files:
      - split: train
        path: gatitos/en_ban.jsonl
  - config_name: gatitos__en_bal
    data_files:
      - split: train
        path: gatitos/en_bal.jsonl
  - config_name: gatitos__en_ba
    data_files:
      - split: train
        path: gatitos/en_ba.jsonl
  - config_name: gatitos__en_bts
    data_files:
      - split: train
        path: gatitos/en_bts.jsonl
  - config_name: gatitos__en_bbc
    data_files:
      - split: train
        path: gatitos/en_bbc.jsonl
  - config_name: gatitos__en_bew
    data_files:
      - split: train
        path: gatitos/en_bew.jsonl
  - config_name: gatitos__en_br
    data_files:
      - split: train
        path: gatitos/en_br.jsonl
  - config_name: gatitos__en_bik
    data_files:
      - split: train
        path: gatitos/en_bik.jsonl
  - config_name: gatitos__en_ctg
    data_files:
      - split: train
        path: gatitos/en_ctg.jsonl
  - config_name: gatitos__en_chk
    data_files:
      - split: train
        path: gatitos/en_chk.jsonl
  - config_name: gatitos__en_fo
    data_files:
      - split: train
        path: gatitos/en_fo.jsonl
  - config_name: gatitos__en_dz
    data_files:
      - split: train
        path: gatitos/en_dz.jsonl
  - config_name: gatitos__en_gaa
    data_files:
      - split: train
        path: gatitos/en_gaa.jsonl
  - config_name: gatitos__en_quc
    data_files:
      - split: train
        path: gatitos/en_quc.jsonl
  - config_name: gatitos__en_kbd
    data_files:
      - split: train
        path: gatitos/en_kbd.jsonl
  - config_name: gatitos__en_kaa
    data_files:
      - split: train
        path: gatitos/en_kaa.jsonl
  - config_name: gatitos__en_meo
    data_files:
      - split: train
        path: gatitos/en_meo.jsonl
  - config_name: gatitos__en_ktu
    data_files:
      - split: train
        path: gatitos/en_ktu.jsonl
  - config_name: gatitos__en_chm
    data_files:
      - split: train
        path: gatitos/en_chm.jsonl
  - config_name: gatitos__en_mfe
    data_files:
      - split: train
        path: gatitos/en_mfe.jsonl
  - config_name: gatitos__en_pcm
    data_files:
      - split: train
        path: gatitos/en_pcm.jsonl
  - config_name: gatitos__en_nd
    data_files:
      - split: train
        path: gatitos/en_nd.jsonl
  - config_name: gatitos__en_se
    data_files:
      - split: train
        path: gatitos/en_se.jsonl
  - config_name: gatitos__en_oc
    data_files:
      - split: train
        path: gatitos/en_oc.jsonl
  - config_name: gatitos__en_os
    data_files:
      - split: train
        path: gatitos/en_os.jsonl
  - config_name: gatitos__en_rhg-Latn
    data_files:
      - split: train
        path: gatitos/en_rhg-Latn.jsonl
  - config_name: gatitos__en_rom
    data_files:
      - split: train
        path: gatitos/en_rom.jsonl
  - config_name: gatitos__en_skr
    data_files:
      - split: train
        path: gatitos/en_skr.jsonl
  - config_name: gatitos__en_shn
    data_files:
      - split: train
        path: gatitos/en_shn.jsonl
  - config_name: gatitos__en_ber-Latn
    data_files:
      - split: train
        path: gatitos/en_ber-Latn.jsonl
  - config_name: gatitos__en_ber
    data_files:
      - split: train
        path: gatitos/en_ber.jsonl
  - config_name: gatitos__en_tet
    data_files:
      - split: train
        path: gatitos/en_tet.jsonl
  - config_name: gatitos__en_bo
    data_files:
      - split: train
        path: gatitos/en_bo.jsonl
  - config_name: gatitos__en_tpi
    data_files:
      - split: train
        path: gatitos/en_tpi.jsonl
  - config_name: gatitos__en_to
    data_files:
      - split: train
        path: gatitos/en_to.jsonl
  - config_name: gatitos__en_tn
    data_files:
      - split: train
        path: gatitos/en_tn.jsonl
  - config_name: gatitos__en_aeb
    data_files:
      - split: train
        path: gatitos/en_aeb.jsonl
  - config_name: gatitos__en_udm
    data_files:
      - split: train
        path: gatitos/en_udm.jsonl
  - config_name: gatitos__en_ve
    data_files:
      - split: train
        path: gatitos/en_ve.jsonl
  - config_name: gatitos__en_vec
    data_files:
      - split: train
        path: gatitos/en_vec.jsonl
  - config_name: gatitos__en_sah
    data_files:
      - split: train
        path: gatitos/en_sah.jsonl
  - config_name: gatitos__en_yua
    data_files:
      - split: train
        path: gatitos/en_yua.jsonl
  - config_name: gatitos__en_zza
    data_files:
      - split: train
        path: gatitos/en_zza.jsonl
  - config_name: gatitos__en_ace
    data_files:
      - split: train
        path: gatitos/en_ace.jsonl
  - config_name: gatitos__en_ach
    data_files:
      - split: train
        path: gatitos/en_ach.jsonl
  - config_name: gatitos__en_ady
    data_files:
      - split: train
        path: gatitos/en_ady.jsonl
  - config_name: gatitos__en_aa
    data_files:
      - split: train
        path: gatitos/en_aa.jsonl
  - config_name: gatitos__en_awa
    data_files:
      - split: train
        path: gatitos/en_awa.jsonl
  - config_name: gatitos__en_bug
    data_files:
      - split: train
        path: gatitos/en_bug.jsonl
  - config_name: gatitos__en_ce
    data_files:
      - split: train
        path: gatitos/en_ce.jsonl
  - config_name: gatitos__en_cv
    data_files:
      - split: train
        path: gatitos/en_cv.jsonl
  - config_name: gatitos__en_fa-AF
    data_files:
      - split: train
        path: gatitos/en_fa-AF.jsonl
  - config_name: gatitos__en_dyu
    data_files:
      - split: train
        path: gatitos/en_dyu.jsonl
  - config_name: gatitos__en_yue
    data_files:
      - split: train
        path: gatitos/en_yue.jsonl
  - config_name: gatitos__en_arz
    data_files:
      - split: train
        path: gatitos/en_arz.jsonl
  - config_name: gatitos__en_cnh
    data_files:
      - split: train
        path: gatitos/en_cnh.jsonl
  - config_name: gatitos__en_hil
    data_files:
      - split: train
        path: gatitos/en_hil.jsonl
  - config_name: gatitos__en_iba
    data_files:
      - split: train
        path: gatitos/en_iba.jsonl
  - config_name: gatitos__en_iu
    data_files:
      - split: train
        path: gatitos/en_iu.jsonl
  - config_name: gatitos__en_kac
    data_files:
      - split: train
        path: gatitos/en_kac.jsonl
  - config_name: gatitos__en_pa-Arab
    data_files:
      - split: train
        path: gatitos/en_pa-Arab.jsonl
  - config_name: gatitos__en_ayl
    data_files:
      - split: train
        path: gatitos/en_ayl.jsonl
  - config_name: gatitos__en_mad
    data_files:
      - split: train
        path: gatitos/en_mad.jsonl
  - config_name: gatitos__en_mak
    data_files:
      - split: train
        path: gatitos/en_mak.jsonl
  - config_name: gatitos__en_ms-Arab
    data_files:
      - split: train
        path: gatitos/en_ms-Arab.jsonl
  - config_name: gatitos__en_arn
    data_files:
      - split: train
        path: gatitos/en_arn.jsonl
  - config_name: gatitos__en_mwr
    data_files:
      - split: train
        path: gatitos/en_mwr.jsonl
  - config_name: gatitos__en_min
    data_files:
      - split: train
        path: gatitos/en_min.jsonl
  - config_name: gatitos__en_nv
    data_files:
      - split: train
        path: gatitos/en_nv.jsonl
  - config_name: gatitos__en_nr
    data_files:
      - split: train
        path: gatitos/en_nr.jsonl
  - config_name: gatitos__en_apd
    data_files:
      - split: train
        path: gatitos/en_apd.jsonl
  - config_name: gatitos__en_tcy
    data_files:
      - split: train
        path: gatitos/en_tcy.jsonl
  - config_name: gatitos__en_scn
    data_files:
      - split: train
        path: gatitos/en_scn.jsonl
  - config_name: gatitos__en_war
    data_files:
      - split: train
        path: gatitos/en_war.jsonl
  - config_name: gatitos__en_mh
    data_files:
      - split: train
        path: gatitos/en_mh.jsonl
  - config_name: gatitos__en_crs
    data_files:
      - split: train
        path: gatitos/en_crs.jsonl
  - config_name: gatitos__en_jam
    data_files:
      - split: train
        path: gatitos/en_jam.jsonl
  - config_name: gatitos__en_brx
    data_files:
      - split: train
        path: gatitos/en_brx.jsonl
  - config_name: gatitos__en_fon
    data_files:
      - split: train
        path: gatitos/en_fon.jsonl
  - config_name: gatitos__en_wo
    data_files:
      - split: train
        path: gatitos/en_wo.jsonl
  - config_name: gatitos__en_kha
    data_files:
      - split: train
        path: gatitos/en_kha.jsonl
  - config_name: gatitos__en_pam
    data_files:
      - split: train
        path: gatitos/en_pam.jsonl
  - config_name: gatitos__en_zap
    data_files:
      - split: train
        path: gatitos/en_zap.jsonl
  - config_name: gatitos__en_av
    data_files:
      - split: train
        path: gatitos/en_av.jsonl
  - config_name: gatitos__en_ar-MA
    data_files:
      - split: train
        path: gatitos/en_ar-MA.jsonl
  - config_name: gatitos__en_gv
    data_files:
      - split: train
        path: gatitos/en_gv.jsonl
  - config_name: gatitos__en_mag
    data_files:
      - split: train
        path: gatitos/en_mag.jsonl
  - config_name: gatitos__en_crh-Latn
    data_files:
      - split: train
        path: gatitos/en_crh-Latn.jsonl
  - config_name: gatitos__en_kek
    data_files:
      - split: train
        path: gatitos/en_kek.jsonl
  - config_name: gatitos__en_apc
    data_files:
      - split: train
        path: gatitos/en_apc.jsonl
  - config_name: gatitos__en_syl
    data_files:
      - split: train
        path: gatitos/en_syl.jsonl
  - config_name: gatitos__en_nus
    data_files:
      - split: train
        path: gatitos/en_nus.jsonl
  - config_name: gatitos__en_ks-Deva
    data_files:
      - split: train
        path: gatitos/en_ks-Deva.jsonl
  - config_name: gatitos__en_new
    data_files:
      - split: train
        path: gatitos/en_new.jsonl
  - config_name: gatitos__en_lg
    data_files:
      - split: train
        path: gatitos/en_lg.jsonl
  - config_name: gatitos__en_ay
    data_files:
      - split: train
        path: gatitos/en_ay.jsonl
  - config_name: gatitos__en_es
    data_files:
      - split: train
        path: gatitos/en_es.jsonl
  - config_name: gatitos__en_as
    data_files:
      - split: train
        path: gatitos/en_as.jsonl
  - config_name: gatitos__en_doi
    data_files:
      - split: train
        path: gatitos/en_doi.jsonl
  - config_name: gatitos__en_ckb
    data_files:
      - split: train
        path: gatitos/en_ckb.jsonl
  - config_name: gatitos__en_ee
    data_files:
      - split: train
        path: gatitos/en_ee.jsonl
  - config_name: gatitos__en_gn
    data_files:
      - split: train
        path: gatitos/en_gn.jsonl
  - config_name: gatitos__en_qu
    data_files:
      - split: train
        path: gatitos/en_qu.jsonl
  - config_name: gatitos__en_gom
    data_files:
      - split: train
        path: gatitos/en_gom.jsonl
  - config_name: gatitos__en_ilo
    data_files:
      - split: train
        path: gatitos/en_ilo.jsonl
  - config_name: gatitos__en_kri
    data_files:
      - split: train
        path: gatitos/en_kri.jsonl
  - config_name: gatitos__en_kl
    data_files:
      - split: train
        path: gatitos/en_kl.jsonl
  - config_name: gatitos__en_lus
    data_files:
      - split: train
        path: gatitos/en_lus.jsonl
  - config_name: gatitos__en_fr
    data_files:
      - split: train
        path: gatitos/en_fr.jsonl
  - config_name: gatitos__en_ts
    data_files:
      - split: train
        path: gatitos/en_ts.jsonl
  - config_name: gatitos__en_ln
    data_files:
      - split: train
        path: gatitos/en_ln.jsonl
  - config_name: gatitos__en_sa
    data_files:
      - split: train
        path: gatitos/en_sa.jsonl
  - config_name: gatitos__en_hi
    data_files:
      - split: train
        path: gatitos/en_hi.jsonl
  - config_name: gatitos__en_nso
    data_files:
      - split: train
        path: gatitos/en_nso.jsonl
  - config_name: gatitos__en_ak
    data_files:
      - split: train
        path: gatitos/en_ak.jsonl
  - config_name: gatitos__en_ff
    data_files:
      - split: train
        path: gatitos/en_ff.jsonl
  - config_name: gatitos__en_om
    data_files:
      - split: train
        path: gatitos/en_om.jsonl
  - config_name: gatitos__en_bho
    data_files:
      - split: train
        path: gatitos/en_bho.jsonl
  - config_name: gatitos__en_mai
    data_files:
      - split: train
        path: gatitos/en_mai.jsonl
  - config_name: gatitos__en_bm
    data_files:
      - split: train
        path: gatitos/en_bm.jsonl
  - config_name: gatitos__en_ti
    data_files:
      - split: train
        path: gatitos/en_ti.jsonl
  - config_name: gatitos__en_dv
    data_files:
      - split: train
        path: gatitos/en_dv.jsonl
  - config_name: gatitos__en_mni-Mtei
    data_files:
      - split: train
        path: gatitos/en_mni-Mtei.jsonl
  - config_name: gatitos__ru_jdt
    data_files:
      - split: train
        path: gatitos/ru_jdt.jsonl
---

# SMOL

SMOL (Set for Maximal Overall Leverage) is a collection professional
translations into 221 Low-Resource Languages, for the purpose of training
translation models, and otherwise increasing the representations of said
languages in NLP and technology.

Please read the [SMOL Paper](https://arxiv.org/abs/2502.12301) and the
[GATITOS Paper](https://arxiv.org/abs/2303.15265) for a much more
thorough description!

There are four resources in this directory:


*   **SmolDoc:** document-level translations into 130 language pairs (129 unique languages)
*   **SmolSent:** sentence-level translations into 114 language pairs (116 unique languages)
*   **GATITOS:** token-level translations into 181 language pairs (183 unique languages)
*   **SmolDoc-factuality-annotations:** factuality annotations and rationales
    for 661 documents from `SmolDoc`
_If a dataset has `en_xx` and `xx_yy` language pairs, the language pairs are {`en_xx`, `xx_yy`} and the unique languages are  {`en`, `xx`, `yy`}_


## April 2026 Update

** More Volunteer translations:**
  * new volunteer SMOL translations for Abaza (`abq`), Brahui (`brh`), Chechen (`ce`), Juhuri (`jdt`), Meadow Mari (`mhr`), Russian (`ru`), and Tuvan (`tyv`)
  * 1000 Cantonese food dishes have been added to Gatitos!

** More Professional translations:** First, we have brought a bunch of languages from tier E to tier C, for a 5x increase in dataset size!
  * Affected languages: `aa din lu apd fon bem sus efi ktu dyu ach ki cgg nd bci mfe tiv rn ayl aeb tum dje gaa alz ndc-ZW dov mos kg ts tn ss kr ve nr gaa sus bci`
  * SMOL was also translated into Hindi, with a post-editing step by different translators to ensure highest quality

**MediSMOL Medical Translations:** For the slightly higher-resource languages, we added ~80 new docs apiece, focused on the medical domain. The English sides were generated in a similar way to SmolDoc, with a prompt lattice over a wide range of possible symptoms and modalities. Unlike SmolDoc, it is not multi-way parallel. It turns out that multi-way parallel data can actually be super dangerous for training!
  * Affected languages: `af ak am ar-MA arz ber ber-Latn bm ee ff ha ig kri lg ln luo mg nso ny om pcm rw sn so st sw ti wo xh yo zu`

**'sep' field:** We add a 'sep' field to SmolDoc. You can use this to join the sentences in SmolDoc together into a better-formatted whole!

**Renames**
  * `scl` appeared to be in Pashto, not Shina, as a result was renamed to `ps`
  * `ff` was renamed to `fuc` (Pulaar), and an alternate translation was provided for `ff`. Neither appear to be very high quality.

## Volunteer contributions

Although the first 113 SMOL languages were commissioned by professional
translation vendors, there have been many volunteer contributions since!

  * Cantonese (`yue`): Translations led by Mingfei Lau and Jonathan Eng; contribution by Tsz Yan Au, Emily Awesome, Jason Chan, Siu Man Chan, Vicky Chan, Yiwang Chen, Kinton Cheung, Mingo Choi, Andy Chow, Ashley Chow, Olivia Chow, Daniel (Ying Wai) Fan, Thomas Fung, Vikki Ha, Joshua Kwong, Liam Lee Pong Lam, Jonas Lau, Ying Tung (Grace) Law, Crystal Lee, Aki Leung, Derek Leung, Jackie Leung, Thomas Leung, Mu Li, Alicia Liu, Malena Loosli, Chui McConnell, Ken Ng, Nicholas Ng, Tonia Shen, Helen Shum, Franky Sze, Eric Tang, Tommy Tse, Daniel Wong, Danny Wong, Maggie Wong, Pinki Wong, Jeffrey Yu, Shanelle Yu, Shing Fung Yue, Miranda Zhang, and Willis Zhang
    * Cantonese food translation led by Olivia Tam
  * Abaza (`abq`): Translated by Georgy Konstantinovich Chekalov and Murat Sagidovich Gedugov, under the auspices of the Autonomous Non-Profit Organization [International Association for the Promotion of the Development of the Abaza-Abkhaz Ethnos 'Alashara'](https://alashara.org/en/) (President: Mussa Khabalevich Ekzekov)
  * Brahui (`brh`): Translated by Mohammad Jahangir
  * Chechen (`ce`): Translations by Abu-Viskhan Umishov, Vladislav Grigorian, and others.
  * Gilaki (`glk`): Translations led by Sina Ahmadi
  * Hawrami (`hac`): Translations led by Sina Ahmadi
  *  Tigre (`tig`): Translated by https://huggingface.co/BeitTigreAI
  * Indonesian (`id`): Post-edits by Muhammad Ravi Shulthan Habibi, David Anugraha, and Genta Indra Winata
  * Juhuri (`jdt`): Translations coordinated by Ariel  and translated by Нафталиев Мардахай Нафталиевич, Исаков Геник Банилович, Мардахаева Роза Эдуардовна, Ильягуева Салиха, Михайлов Виктор Сиюнович
  * Kokborok (`trp`): Translations led by Sudhamoy DebBarma
  * Ligurian (`lij`): Translations led by Alessandro Guasoni, Edoardo Ferrante, and the [Conseggio Ligure](https://conseggio-ligure.org/)
  * Meadow Mari (`mhr`): Translations led by Andrei Chemyshev, with the Mari Institute of Language, Literature and History
  * Mooré (mos): Post-edits/Translations by Clement Sampegbo (Ashesi University) and Tuwende Davy Donald Koumtoubre (Institut Burkinabe des Arts et Metiers)
  * NKo (`nqo`): Translations led by Baba Mamadi Diane, Koulako Moussa Doumbouya, Djibrila Diane Solo, anf Farabado Cissé
  * Russian (`ru`): Translations led by Ali Kuzhuget
  * Sorani (`ckb`): Translations led by Sina Ahmadi
  * Tumbuka (tum): Translations led by Anthony Munthali
  * Tuvan (`tyv`): Translations led by Ali Kuzhuget
  * Zarma (`dje`): Translated by Ismael Illa Salifou, Mariama Ibrahim Oumarou, Nafissatou Issa Oumarou, Christopher Homan, and Mamadou K. Keita.
  * Khakas (`kjh`): Translations led by Vasily Adeshkin; contribution by Mainagasheva Nina Semyonovna, Chebochakova Irina Maksimovna, Abdina Raisa Petrovna, Abumova Olga Dmitrievna, Kirginekov Roman Gennadievich, Kicheeva Kristina Vladimirovna, Kyzlasov Artyom Samuilovich, Subrakova Viya Vasilyevna, Shagdurova Olga Yurievna; [adeshkin/google-smol-en-ru-kjh](https://huggingface.co/datasets/adeshkin/google-smol-en-ru-kjh).

## Data schemata

The schemata are pretty straightforward. Source and Target language are
provided in `sl` and `tl` fields. The `is_src_orig` field has a value
of `true` if the source text was the original text, and the target field
was translated, and avalue of `false` if the data is back-translated.


### GATITOS

GATITOS has a one-to-many schema, with each source mapping to one or more targets:

```
{
 'sl': 'en',
 'tl': 'aa',
 'is_source_orig': True,
 'src': 'how are you',
 'trgs': ['mannah taniih?', 'anninnaay?']
}
```

### SmolSent

SmolSent's schema differs from SmolDoc's only in that `src` and `trg` are single strings, not lists:

```
{'id': 381,
 'sl': 'en',
 'tl': 'ber',
 'is_src_orig': True,
 'src': 'Rih, a deaf former soldier, plots rebellion while married to a queer, teenage god.',
 'trg': 'ⵔⵉⵀ, ⴷ ⴰⴷⴻⴼⵔⵉⵔ ⴰⵇⴱⵓⵔ ⴰⴻⵎⴻⵙⵍⵉ, ⵢⴻⵜⵜⵀⴻⴳⴳⵉ ⵜⴰⴴⴻⵡⵡⴰⵜ-ⵉⵙ, ⴴⴰⵙ ⴰⴽⴽⴻⵏ ⵢⴻⵣⵡⴻⴵ ⴷ ⵢⵉⵡⴻⵏ ⵢⵉⵍⵓ ⵉⵍⴻⵎⵥⵉ ⵉⵁⴻⵎⵎⵍⴻⵏ ⴰⵔⵔⴰⵛ.'
}
```

### SmolDoc

SmolDoc provides sentence-split and aligned translations through the `srcs` and `trgs` fields. These will always have the same length.

```
{
'id': 'topic_587__weyiwiniwaaotiwenwy',
 'sl': 'en',
 'tl': 'pcm',
 'is_src_orig': True,
 'factuality': 'ok',  # this is a story so there is no factual claim that could be wrong
 'srcs': ['"What the hell are you doing, you idiot?!"',
          '"Excuse me?"',
          '"You cut me off! You almost made me crash!"',
          '"I'm sorry, I didn't mean to. I was just trying to get around that slow-moving truck."',
          '"Well, you could have at least used your turn signal!"',
          '"I did use my turn signal!"',
          '"No, you didn't! You just pulled right out in front of me!"',
          '"I'm telling you, I used my turn signal!"',
          '"Whatever. You're still a terrible driver."',
          '"And you're a jerk!"',
          '"At least I know how to drive!"',
          '"Oh, yeah? Well, I'm a better writer than you are!"',
          '"That's debatable."',
          '"It's not debatable! I'm Ernest Hemingway!"',
          '"Who?"',
          '"Ernest Hemingway! The greatest writer of all time!"',
          '"Never heard of him."',
          '"Well, you've heard of me now!"',
          '"Yeah, I heard of you."'],
 'trgs': ['"Wetin di hell dey do, yu idiot?!"',
          '"Ekskuse mi?"',
          '"Yu komot mi! Yu almost make mi krash!"',
          '"I dey sorry, I nor wont do am. I just dey try get around dat truk wey slow."',
          '"Well, yu for don yus yor turn sign!"',
          '"I yus mai turn sign!"',
          '"No, yu nor turn am! Yu just turn rite in front of mi!"',
          '"I dey tell yu, I yus mai turn sign!"',
          '"Wateva. Yu still bi one tribol driva."',
          '"And yu bi jerk!"',
          '"At least I sabi hau to drive!"',
          '"Oh, yeah? Well, I bi ogbonge writa pass yu!"',
          '"Wi fit dibate dat."',
          '"nortin to dibate! I bi Ernest Hemingway!"',
          '"Who?"',
          '"Ernest Hemingway! De writa of all taim wey grate pass!"',
          '"Neva hear am."',
          '"Well, yu don hear mi nau!"',
          '"Na so, I don hear yu."'],
  'sep': ['
', '
', '
', '
', '
', '
', '
', '
', '
', '
', '
', '
', '
', '
', '
', '
', '
', '
', '']
}
```




### SmolDoc factuality

The factuality map contains the per-document ratings for each of the three
raters, for all documents in the SmolDoc data. The source text itself is not
included, but can be gotten by joining with SmolDoc on the `id` field. Example
datum:

```
  "topic_260__mtaftfttit": {
    "1": [
      "Minor Issue(s)",
      "This paragraph is mostly accurate, but there's an issue with the study mentioned. The study by the Geena Davis Institute found that only 36.3% of female characters had speaking roles, not 30% (source: https://geenadavisinstitute.org/wp-content/uploads/2024/01/see-jane-100-report-2017.pdf)."
    ],
    "2": [
      "Minor Issue(s)",
      "The claim regarding 12% of female characters working outside the home is not explicitly supported by Geena Davis Institute studies as seen in the article https://geenadavisinstitute.org/research/gender-bias-with-borders-an-investigation-of-female-characters-in-popular-films-across-11-countriesgender-bias-with-borders/"
    ],
    "3": [
      "Not Sure",
      "The claims are generally true. But I could not confirm that 12% of female characters were working outside the home according to this site. https://geenadavisinstitute.org/wp-content/uploads/2024/01/see-jane-100-report-2017.pdf"
    ]
  },
```


## Notes on the GATITOS multilingual Lexicon

The GATITOS (Google's Additional Translations Into Tail-languages: Often Short)
dataset is a high-quality, multi-way parallel dataset of tokens and short
phrases, intended for training and improving machine translation models.
Experiments on this dataset and Panlex focusing on unsupervised translation in
a 208-language model can be found in
the [GATITOS paper](https://arxiv.org/abs/2303.15265).

This dataset consists in 4,000 English segments (4,500 tokens) that have been
translated into each of 173 languages, and as a 4001st token, the endonym.
Of these, 170 are low-resource, and three
are mid-high resource (es, fr, hi). All translations were made
directly from English, with the exception of Aymara, which was translated from
the Spanish.

This dataset contains primarily short segments: 93% single tokens, and only 23
sentences (0.6%) have over 5 tokens. As such it is best thought of as a
multilingual lexicon, rather than a parallel training corpus. The source text is
frequent words in the English Language, along with some common phrases and short
sentences. Care has been taken to ensure that they include good coverage of
numbers, months, days of the week, swadesh words, and names of the languages
themselves (including the endonym).

Single tokens are remarkably fickle to translate because of the common issue of
polysemy. Some languages in this dataset only provide one translation per
source token; others provide multiple translations. When multiple translations
are given, they are broken up into multiple lines. Therefore, you can get the
average number of translations per token by looking at the number of lines in
the file versus the number of deduplicated English lines in the file. The three
languages with the most average translations per English token are Betawi,
Kachin, and Occitan, each with over 1.5 on average.

Sometimes translators have left annotations like "pike (verb)", "او (مونث)", "фамили(я)", "أسوأ(repeated)" etc..
Wolof is particularly noticeable in this regard, with notes like "xont (verb) which means to feed an animal". Several languages also give definitions instead of translations for some words, e.g. Tok Pisin translation of mole" to "wanpela liklik animal we i save stap long hol long graun".


## Per-language information

The following table only includes information for the
`source_lang_translated_lang` direction. However, data in this repo is released
in both directions, so e.g. this table lists only `en_ay`, but reversed `ay_en`
data is also released.

LP | Target Language Name | ISO 639-3  | ISO 15924 Script | Glottocode | Continent | Endonym | Alternate names |  N Smoldoc | N SmolSent | N Gatitos |
---|----------------------|------------------|-------------|-----------------|-----------|---------|-----------------|-----------|------------|-----------|
ar_am         | Amharic       | amh           | Ethi          | amha1245      | Africa        | አማርኛ          |               | 329  | 0  | 0  | 
ar_sw         | Swahili       | swa           | Latn          | swah1253      | Africa        | Kiswahili     | Kiswahili     | 330  | 0  | 0  | 
en_aa         | Afar          | aar           | Latn          | afar1241      | Africa        | Qafar         |               | 130  | 863  | 3990  | 
en_ab         | Abkhaz        | abk           | Cyrl          | abkh1244      | Asia          | Аҧсуа         | Abkhazian     | 0  | 0  | 3976  | 
en_abq        | Abaza         | abq           | Cyrl          | abaz1241      |               |               |               | 0  | 0  | 3999  | 
en_ace        | Acehnese      | ace           | Latn          | aceh1245      | Asia          | Aceh          | Achinese; Dayan; Aceh  | 0  | 0  | 4001  | 
en_ach        | Acholi        | ach           | Latn          | acol1240      | Africa        | Acholi        | Luo; Acoli    | 130  | 863  | 4001  | 
en_ady        | West Circassian  | ady           | Cyrl          | adyg1241      | Europe        | Черкес        | Adyghe        | 0  | 0  | 4001  | 
en_aeb        | Tunisian Arabic  | aeb           | Arab          | tuni1253      | Africa        | اللغة العربيّة التونسيّة  | Arabic (Tunisia); Tounsi  | 130  | 862  | 3998  | 
en_af         | Afrikaans     | afr           | Latn          | afri1274      | Africa        | Afrikaans     |               | 209  | 863  | 0  | 
en_ahr        | Ahirani       | ahr           | Deva          | ahir1247      | Asia          | खान्देशी, अहिराणी  |               | 457  | 0  | 0  | 
en_aii        | Assyrian Neo-Aramaic  | aii           | Syrc          | assy1244      | Asia          | ܣܘܪܝܬ         | Assyrian; Assyrian Neo–Aramaic; Sureth; Suret  | 0  | 0  | 3717  | 
en_ak         | Twi           | aka           | Latn          | akan1250      | Africa        | Twi           | Akan (includes Akuapem + Fante); Asante  | 347  | 863  | 4000  | 
en_alz        | Alur          | alz           | Latn          | alur1245      | Africa        | Lur           |               | 130  | 863  | 3992  | 
en_am         | Amharic       | amh           | Ethi          | amha1245      | Africa        | አማርኛ          |               | 663  | 863  | 0  | 
en_apc        | North Levantine Arabic  | apc           | Arab          | nort3190      | Asia          | شامي‎         |               | 0  | 0  | 3998  | 
en_apd        | Sudanese Arabic  | apd           | Arab          | suda1253      | Africa        | عربي سوداني   | Arabic (Sudan)  | 130  | 855  | 3995  | 
en_ar-MA      | Morrocan Arabic  | ara           | Arab          | stan1269      | Africa        | الدارجة       | Arabic (Morocco); Darija  | 343  | 863  | 3989  | 
en_arn        | Mapudungun    | arn           | Latn          | mapu1245      | Americas      | Mapudungun    | Mapuche       | 0  | 0  | 4001  | 
en_arz        | Egyptian Arabic  | arz           | Arab          | egyp1253      | Africa        | اللهجة المصرية  | Arabic (Egypt); Masri; Masry  | 344  | 863  | 4001  | 
en_as         | Assamese      | asm           | Beng          | assa1263      | Asia          | অসমীয়া       |               | 0  | 0  | 3975  | 
en_av         | Avar          | ava           | Cyrl          | avar1255      | Europe        | магӏарул мацӏ  | Avaric        | 0  | 0  | 4001  | 
en_awa        | Awadhi        | awa           | Deva          | awad1243      | Asia          | अवधी          | Audhi         | 0  | 0  | 3999  | 
en_ay         | Aymara        | aym           | Latn          | cent2131      | Americas      | Aymar aru     |               | 0  | 863  | 3990  | 
en_ayl        | Libyan Arabic  | ayl           | Arab          | liby1242      | Africa        | العربية الليبية  | Arabic (Libya); Sulaimitian Arabic  | 130  | 863  | 3999  | 
en_ba         | Bashkir       | bak           | Cyrl          | bash1264      | Europe        | Башҡорт       | Bashkort      | 0  | 0  | 3986  | 
en_bal        | Baluchi       | bal           | Arab          | balo1260      | Asia          | بلوچی         | Balochi       | 0  | 0  | 3994  | 
en_ban        | Balinese      | ban           | Latn          | bali1278      | Asia          | Basa Bali     |               | 0  | 0  | 3992  | 
en_bbc        | Batak Toba    | bbc           | Latn          | bata1315      | Asia          | Batak Toba    |               | 0  | 0  | 3993  | 
en_bci        | Baoulé        | bci           | Latn          | baou1244      | Africa        | wawle         | Baoule; Baule  | 130  | 863  | 3998  | 
en_bem        | Bemba (Zambia)  | bem           | Latn          | bemb1251      | Africa        | Ichibemba     | Bemba; chiBemba  | 130  | 863  | 3977  | 
en_ber        | Tamazight (Tifinagh Script)  | ber           | Tfng          | cent2136      | Africa        | ⵜⴰⵎⴰⵣⵉⵖⵜ      | Berber; Amazigh  | 213  | 862  | 4000  | 
en_ber-Latn   | Tamazight (Latin Script)  | ber           | Latn          | cent2136      | Africa        | Tamaziɣt      | Tamazight; Berber; Amazigh  | 208  | 862  | 4001  | 
en_bew        | Betawi        | bew           | Latn          | beta1263      | Asia          | Betawi        | Betawi Malay; Jakartan Malay; Batavian Malay  | 0  | 0  | 4001  | 
en_bfq        | Badaga        | bfq           | Taml          | bada1255      | Asia          | படக           |               | 457  | 0  | 0  | 
en_bfy        | Bagheli       | bfy           | Deva          | bagh1245      | Asia          | बघेली         |               | 457  | 0  | 0  | 
en_bgq        | Bagri         | bgq           | Deva          | bagr1244      | Asia          | बागड़ी        |               | 457  | 0  | 0  | 
en_bho        | Bhojpuri      | bho           | Deva          | bhoj1242      | Asia          | भोजपुरी       |               | 0  | 0  | 3991  | 
en_bik        | Bikol         | bcl           | Latn          | cent2238      | Asia          | Sentral Bikol  | Bicol; Bicolano  | 0  | 0  | 3993  | 
en_bjn        | Banjar        | bjn           | Latn          | banj1253      | Asia          | Banjar        | Banjarese     | 0  | 0  | 3996  | 
en_bjn-Arab   | Banjar (Arabic script)  | bjn           | Arab          | banj1253      | Asia          | بنجر; ڤندير بنجر  |               | 0  | 0  | 3999  | 
en_bm         | Bambara       | bam           | Latn          | bamb1269      | Africa        | Bámánánkán    |               | 340  | 863  | 4000  | 
en_bn         | Bengali       | ben           | Beng          | beng1280      | Asia          | বাংলা         |               | 253  | 562  | 0  | 
en_bns        | Bundeli       | bns           | Deva          | bund1257      | Asia          | बुन्देली      |               | 456  | 0  | 0  | 
en_bo         | Tibetan       | bod           | Tibt          | tibe1279      | Asia          | བོད་མི།; བོད་ཀྱི།; བོད་སྐད།; བོད་ཡིག།  | Lhasa Tibetan; Standard Tibetan; Baykha; Kham; Baykay  | 0  | 863  | 3994  | 
en_br         | Breton        | bre           | Latn          | bret1244      | Europe        | brezhoneg     | Brezhoneg     | 0  | 0  | 4001  | 
en_bra        | Braj          | bra           | Deva          | braj1239      | Asia          | ब्रजभाषा      |               | 457  | 0  | 0  | 
en_brh        | Brahui        | brh           | Arab          | brah1256      | Asia          | براہوئی‎      |               | 66  | 863  | 3935  | 
en_brx        | Bodo (India)  | brx           | Deva          | bodo1262      | Asia          | बोडो          | Bodo; Boro    | 0  | 863  | 3994  | 
en_bts        | Batak Simalungun  | bts           | Latn          | bata1312      | Asia          | Bahasa Simalungun  | Simalungun; Simalungunese  | 0  | 0  | 3999  | 
en_btx        | Batak Karo    | btx           | Latn          | bata1314      | Asia          | Batak Karo    | Karonese; Karo; Bahasa Karo  | 0  | 0  | 3997  | 
en_bua        | Buryat        | bua           | Cyrl          | bury1248      | Asia          | Буряад        |               | 0  | 0  | 3976  | 
en_bug        | Buginese      | bug           | Latn          | bugi1246      | Asia          | basa Ugi      |               | 0  | 0  | 3759  | 
en_ccp-Latn   | Chakma (Latin script)  | ccp           | Latn          | chak1271      | Asia          | Changhma Bhach  |               | 457  | 0  | 0  | 
en_ce         | Chechen       | che           | Cyrl          | chec1245      | Europe        | Нохчийн       |               | 0  | 0  | 3997  | 
en_cgg        | Kiga          | cgg           | Latn          | kiga1247      | Africa        | Kiga          | Chiga; Orukiga; Rukiga; Ruchiga  | 130  | 863  | 4001  | 
en_ch         | Chamorro      | cha           | Latn          | cham1313      | Oceania       | Finuʼ Chamoru  | CHamoru       | 0  | 0  | 4001  | 
en_chk        | Chuukese      | chk           | Latn          | chuu1241      | Oceania       | Trukese       | Trukese       | 0  | 0  | 3889  | 
en_ckb        | Kurdish (Sorani)  | ckb           | Arab          | cent2243      | Asia          | سۆرانی        | Central Kurdish; Sorani  | 0  | 863  | 3986  | 
en_cnh        | Hakha Chin    | cnh           | Latn          | hakh1239      | Asia          | Laica         | Zomi; Laiholh; Lai  | 0  | 0  | 3999  | 
en_crh        | Crimean Tatar (Cyrillic script)  | crh           | Cyrl          | crim1257      | Europe        | Крымскотатарский  | Crimean Tatar  | 0  | 0  | 3990  | 
en_crh-Latn   | Crimean Tatar (Latin script)  | crh           | Latn          | crim1257      | Europe        | qırımtatar tili  |               | 0  | 0  | 3990  | 
en_crs        | Seychellois Creole  | crs           | Latn          | seyc1242      | Africa        | kreol seselwa  | kreol; Seselwa Creole French  | 0  | 0  | 3989  | 
en_ctg        | Chittagonian  | ctg           | Beng          | chit1278      | Asia          | Chittagonian  |               | 0  | 0  | 3996  | 
en_cv         | Chuvash       | chv           | Cyrl          | chuv1255      | Europe        | Чăваш         |               | 0  | 0  | 3985  | 
en_dhd        | Dhundari      | dhd           | Deva          | dhun1238      | Asia          | ढूंढाड़ी      |               | 456  | 0  | 0  | 
en_din        | Dinka         | din           | Latn          | dink1262      | Africa        | Thuɔŋjäŋ      |               | 130  | 863  | 4001  | 
en_dje        | Zarma         | dje           | Latn          | zarm1239      | Africa        |               |               | 130  | 863  | 4001  | 
en_doi        | Dogri         | doi           | Deva          | dogr1251      | Asia          | डोगरी         |               | 454  | 0  | 3997  | 
en_dov        | Dombe         | dov           | Latn          | dovv1238      | Africa        | ChiDombe      | Chidombe; Zambezi; Tonga  | 130  | 863  | 3998  | 
en_dv         | Dhivehi       | div           | Thaa          | dive1238      | Asia          | ދިވެހި        | Maldivian, Divehi  | 0  | 0  | 3973  | 
en_dyu        | Dyula         | dyu           | Latn          | dyul1238      | Africa        | Julakan       | Dioula; Jula  | 130  | 863  | 3997  | 
en_dz         | Dzongkha      | dzo           | Tibt          | dzon1238      | Asia          | རྫོང་ཁ        | Bhutanese     | 0  | 0  | 3997  | 
en_ee         | Ewe           | ewe           | Latn          | ewee1241      | Africa        | Eʋegbe        |               | 212  | 863  | 3990  | 
en_efi        | Efik          | efi           | Latn          | efik1245      | Africa        | Usem mbom Efik; Ikɔ-efik  |               | 130  | 863  | 4001  | 
en_es         | Spanish       | spa           | Latn          | span1260      | Europe        | español, castellano  |               | 0  | 863  | 3991  | 
en_fa         | Persian       | fas           | Arab          | dari1249      | Asia          | فارسی         |               | 60  | 763  | 0  | 
en_fa-AF      | Dari          | fas           | Arab          | dari1249      | Asia          | دری           | Persian (Afghanistan)  | 0  | 0  | 4000  | 
en_ff         | Fulani        | ful           | Latn          | fula1264      | Africa        | Fulɓe; Fulfulde; Pular; Pulaar  | Fulfulde; Fula; Fulah; Pular; Pulaar; Peul (French)  | 340  | 862  | 3998  | 
en_fil        | Filipino      | fil           | Latn          | fili1244      | Asia          |               |               | 60  | 754  | 0  | 
en_fj         | Fijian        | fij           | Latn          | fiji1243      | Oceania       | Vosa Vaka-Viti  | Bauan         | 0  | 0  | 4001  | 
en_fo         | Faroese       | fao           | Latn          | faro1244      | Europe        | Føroysk       |               | 0  | 0  | 3999  | 
en_fon        | Fon           | fon           | Latn          | fonn1241      | Africa        | fɔ̀ngbè; fongbē  |               | 130  | 863  | 3998  | 
en_fr         | French        | fra           | Latn          | fren1241      | Europe        | français      |               | 0  | 0  | 3998  | 
en_fr-CA      | French (Canada)  | fra           | Latn          | fren1241      | Americas      | français canadien  |               | 0  | 0  | 4001  | 
en_fuc        | Pulaar        | fuc           | Latn          | pula1263      |               |               |               | 0  | 863  | 0  | 
en_fur        | Friulian      | fur           | Latn          | friu1241      | Europe        | Furlan        |               | 0  | 0  | 3985  | 
en_gaa        | Ga            | gaa           | Latn          | gaaa1245      | Africa        | Gã            |               | 130  | 863  | 4000  | 
en_glk        | Gilaki        | glk           | Arab          | gila1241      | Asia          | گيلکي         |               | 0  | 863  | 0  | 
en_gn         | Guarani       | grn           | Latn          | guar1295      | Americas      | avañeʼẽ       |               | 0  | 863  | 3991  | 
en_gom        | Goan Konkani  | gom           | Deva          | goan1237      | Asia          | कोंकणी        |               | 0  | 0  | 3999  | 
en_grt-Latn   | Garo (Latin script)  | grt           | Latn          | garo1249      | Asia          | A·chikku      |               | 457  | 0  | 0  | 
en_gu         | Gujarati      | guj           | Gujr          | guja1252      | Asia          | ગુજરાતી ભાષા  |               | 253  | 563  | 0  | 
en_gv         | Manx          | glv           | Latn          | manx1243      | Europe        | Gaelg         | Gaelic        | 0  | 0  | 3999  | 
en_ha         | Hausa         | hau           | Latn          | haus1257      | Africa        | Hausa         |               | 667  | 863  | 0  | 
en_hac        | Hawrami       | hac           | Arab          | hacr1238      | Asia          | ھەورامی       | Gurani        | 0  | 863  | 0  | 
en_hi         | Hindi         | hin           | Deva          | hind1269      | Asia          | हिन्दी        |               | 259  | 862  | 3984  | 
en_hil        | Hiligaynon    | hil           | Latn          | hili1241      | Asia          | Hiligaynon    | Ilonggo; Binisaya; Bisaya nga Hiniligaynon; Inilonggo  | 0  | 0  | 4001  | 
en_hne        | Chhattisgarhi  | hne           | Deva          | chha1248      | Asia          | छत्तीसगढ़ी    |               | 0  | 0  | 4000  | 
en_hoc-Wara   | Ho (Warang Chiti script)  | hoc           | Wara          | hooo1242      | Asia          | 𑢹𑣉𑣉 𑣎𑣋𑣜       |               | 457  | 0  | 0  | 
en_hrx        | Hunsrik       | hrx           | Latn          | huns1243      | Americas      | Hunsrik       | Riograndenser Hunsrik  | 0  | 0  | 3932  | 
en_iba        | Iban          | iba           | Latn          | iban1266      | Asia          | Iban          | Sea Dayak     | 0  | 0  | 3997  | 
en_id         | Indonesian    | ind           | Latn          | indo1316      | Asia          | Bahasa Indonesia  |               | 66  | 863  | 0  | 
en_ig         | Igbo          | ibo           | Latn          | igbo1258      | Africa        | Asụsụ Igbo    |               | 478  | 863  | 0  | 
en_ilo        | Ilocano       | ilo           | Latn          | iloc1242      | Asia          | Iloko         | Iloko; Ilokano  | 0  | 0  | 3993  | 
en_is         | Icelandic     | isl           | Latn          | icel1247      | Europe        | Íslenska      |               | 0  | 863  | 3995  | 
en_iso        | Isoko         | iso           | Latn          | isok1244      | Africa        | Isoko         |               | 0  | 0  | 4001  | 
en_iu         | Inuktut (Syllabics)  | iku           | Cans          | east2532      | Americas      | ᐃᓄᒃᑎᑐᑦ        | Inuktitut; Inuktut  | 0  | 0  | 3999  | 
en_iu-Latn    | Inuktut (Latin)  | iku           | Latn          | east2532      | Americas      | Inuktut       | Inuktitut; Inuktut  | 0  | 0  | 4001  | 
en_ja         | Japanese      | jpn           | Jpan          | nucl1643      | Asia          | 日本語           |               | 254  | 753  | 0  | 
en_jam        | Jamaican Patois  | jam           | Latn          | jama1263      | Americas      | Patwa         | Patois; Jamaican Creole English  | 0  | 0  | 3996  | 
en_kaa        | Karakalpak    | kaa           | Cyrl          | kara1499      | Asia          | Қарақалпақ; Қарақалпақша  | Kara-Kalpak; Qaraqalpaq  | 0  | 0  | 3970  | 
en_kac        | Jingpo        | kac           | Latn          | jing1258      | Asia          | Jinghpaw      | Kachin; Jingpho; Jingphaw; Wunpawng  | 0  | 0  | 3941  | 
en_kbd        | East Circassian  | kbd           | Cyrl          | kaba1278      | Europe        | Къэбэрдей; Адыгэ  | Kabardian     | 0  | 0  | 3976  | 
en_kek        | Q'eqchi'      | kek           | Latn          | qeqc1239      | Americas      | Qʼeqchiʼ      | Kekchi; Kekchi'; Kekchí  | 0  | 0  | 4001  | 
en_kfy        | Kumaoni       | kfy           | Deva          | kuma1271      | Asia          | कुमाऊँनी      |               | 457  | 0  | 0  | 
en_kg         | Kongo         | kon           | Latn          | kong1295      | Africa        | Kikongo       | Kikongo       | 130  | 863  | 3998  | 
en_kha        | Khasi         | kha           | Latn          | khas1265      | Asia          | khasi         | Khasian       | 0  | 0  | 4001  | 
en_ki         | Kikuyu        | kik           | Latn          | kiku1242      | Africa        | Gĩgĩkũyũ      | Gikuyu        | 130  | 863  | 3994  | 
en_kl         | Kalaallisut   | kal           | Latn          | kala1399      | Americas      | Kalaallisut   | Greenlandic   | 0  | 863  | 3943  | 
en_km         | Khmer         | khm           | Khmr          | cent2260      | Asia          | ភាសាខ្មែរ     |               | 254  | 763  | 0  | 
en_kn         | Kannada       | kan           | Knda          | kann1259      | Asia          | ಕನ್ನಡ         |               | 252  | 561  | 0  | 
en_ko         | Korean        | kor           | Kore          | kore1280      | Asia          | 한국어           |               | 254  | 753  | 0  | 
en_kr         | Kanuri        | kau           | Latn          | kanu1282      | Africa        | Kànùrí        |               | 130  | 863  | 4000  | 
en_kri        | Krio          | kri           | Latn          | krio1253      | Africa        | Krio          |               | 207  | 863  | 4020  | 
en_kru        | Kurukh        | kru           | Deva          | kuru1263      | Asia          | कुँड़ुख़      |               | 457  | 0  | 0  | 
en_ks         | Kashmiri      | kas           | Arab          | kash1277      | Asia          | كٲشُر         | Koshur        | 0  | 863  | 4001  | 
en_ks-Deva    | Kashmiri (Devanagari script)  | kas           | Deva          | kash1277      | Asia          | कॉशुर         | Koshur        | 0  | 863  | 4001  | 
en_ktu        | Kituba (DRC)  | ktu           | Latn          | kitu1242      | Africa        | Kituba        | Kituba        | 130  | 863  | 3999  | 
en_kv         | Komi          | kom           | Cyrl          | komi1269      | Asia          | Коми          | Zyryan; Komi-Zyryan  | 0  | 0  | 3980  | 
en_lep        | Lepcha        | lep           | Lepc          | lepc1242      | Asia          | ᰛᰩᰵᰛᰧᰵᰶ‎      |               | 456  | 0  | 0  | 
en_lg         | Luganda       | lug           | Latn          | gand1255      | Africa        | Oluganda      | Ganda         | 343  | 863  | 3998  | 
en_li         | Limburgish    | lim           | Latn          | limb1264      | Europe        | Limburgs      | Limburgian; Limburg; Limburgs  | 0  | 0  | 3999  | 
en_lif-Limb   | Limbu (Limbu script)  | lif           | Limb          | limb1265      | Asia          | ᤕᤠᤰᤌᤢᤱ ᤐᤠᤴ    |               | 457  | 0  | 0  | 
en_lij        | Ligurian      | lij           | Latn          | ligu1248      | Europe        | Ligure        | Genoese       | 66  | 863  | 4332  | 
en_lmo        | Lombard       | lmo           | Latn          | lomb1257      | Europe        | lombard       |               | 0  | 0  | 3983  | 
en_ln         | Lingala       | lin           | Latn          | ling1261      | Africa        | Lingála       | Ngala         | 343  | 863  | 3994  | 
en_ltg        | Latgalian     | ltg           | Latn          | latg1249      | Europe        | latgalīšu     |               | 0  | 0  | 3984  | 
en_lu         | Kiluba (Luba-Katanga)  | lub           | Latn          | luba1252      | Africa        | Kiluba        | Luba-Katanga; Luba; Tshiluba  | 130  | 863  | 0  | 
en_lua        | Tshiluba (Luba-Lulua)  | lua           | Latn          | luba1253      | Africa        | Tshiluba, Ciluba  | Luba-Kasai; Luba; Tshiluba; Cilubà; Tshilubà, Luba-Lulua  | 0  | 0  | 3998  | 
en_luo        | Luo           | luo           | Latn          | luoo1242      | Africa        | Luo           | Dholuo        | 342  | 863  | 3941  | 
en_lus        | Mizo          | lus           | Latn          | lush1249      | Asia          | Mizo ṭawng    |               | 0  | 863  | 3998  | 
en_mad        | Madurese      | mad           | Latn          | madu1252      | Asia          | Madurâ        |               | 0  | 0  | 3999  | 
en_mag        | Magahi        | mag           | Deva          | maga1259      | Asia          | मगही          |               | 456  | 0  | 3997  | 
en_mai        | Maithili      | mai           | Deva          | mait1250      | Asia          | मैथिली        | Maitili       | 0  | 0  | 3989  | 
en_mak        | Makassar      | mak           | Latn          | maka1312      | Asia          | Mangkasara    | Makasar; Makassarese; Mangkasara; Macassar  | 0  | 0  | 3994  | 
en_mam        | Mam           | mam           | Latn          | nort2932      | Americas      | Ta yol Mam    |               | 0  | 0  | 3902  | 
en_meo        | Kedah Malay   | meo           | Latn          | keda1251      | Asia          | Siti          | Malay (Kedah)  | 0  | 0  | 3995  | 
en_mfe        | Mauritian Creole  | mfe           | Latn          | maur1252      | Africa        | Morisien      | Morisien; Morisyen  | 130  | 863  | 3997  | 
en_mg         | Malagasy      | mlg           | Latn          | mala1288      | Africa        | Fiteny malagasy  |               | 474  | 863  | 0  | 
en_mh         | Marshallese   | mah           | Latn          | mars1254      | Oceania       | Majol         | Ebon          | 0  | 0  | 3977  | 
en_mhr        | Meadow Mari   | mhr           | Cyrl          | east2328      | Asia          | олык марий    | Eastern Mari  | 0  | 0  | 0  | 
en_min        | Minang        | min           | Latn          | mina1264      | Asia          | Minangkabau   | Minangkabau   | 0  | 0  | 3999  | 
en_mjl        | Mandeali      | mjl           | Deva          | mand1417      | Asia          | मण्डियाली     |               | 457  | 0  | 0  | 
en_ml         | Malayalam     | mal           | Mlym          | mala1464      | Asia          | മലയാളം        |               | 254  | 563  | 0  | 
en_mni-Mtei   | Meiteilon (Manipuri)  | mni           | Mtei          | mani1293      | Asia          | ꯃꯤꯇꯩꯂꯣꯟ       | Meitei, Meetei, Meitheilon, Meeteilon  | 0  | 863  | 3923  | 
en_mos        | Mooré         | mos           | Latn          | moor1244      | Africa        | Moaaga; Mòoré  | Mossi; Moore; More; Mõore; Mossé  | 130  | 863  | 4000  | 
en_mr         | Marathi       | mar           | Deva          | mara1378      | Asia          | मराठी         |               | 252  | 563  | 0  | 
en_ms-Arab    | Malay (Jawi Script)  | msa           | Arab          | stan1293      | Asia          | ملايو         |               | 0  | 0  | 4000  | 
en_mtr        | Mewari        | mtr           | Deva          | mewa1253      | Asia          | मेवाड़ी       |               | 457  | 0  | 0  | 
en_mwr        | Marwadi       | mwr           | Deva          | marw1261      | Asia          | मारवाड़ी      | Marwari; Rajasthani  | 0  | 0  | 3999  | 
en_my         | Myanmar (Burmese)  | mya           | Mymr          | burm1265      | Asia          | မြန်မာဘာသာစကား  |               | 251  | 763  | 0  | 
en_nd         | North Ndebele  | nde           | Latn          | nort2859      | Africa        | IsiNdebele    | Ndebele (North)  | 130  | 863  | 3694  | 
en_ndc        | Ndau          | ndc           | Latn          | ndau1241      | Africa        |               |               | 0  | 0  | 0  | 
en_ne         | Nepali        | nep           | Deva          | nepa1254      | Asia          | नेपाली        |               | 52  | 763  | 0  | 
en_new        | Nepalbhasa (Newari)  | new           | Deva          | newa1241      | Asia          | नेवाः         | Newari; Nepalbhasa; Nepal Bhasa; Newar  | 0  | 0  | 4001  | 
en_nhe        | Eastern Huasteca Nahuatl  | nhe           | Latn          | east2338      | Americas      | Nahuatlajtoli Kuextekan ikisayo  | Nahuatl (Eastern Huasteca)  | 0  | 0  | 4000  | 
en_noe        | Nimadi        | noe           | Deva          | nima1244      | Asia          | निमाड़ी       |               | 315  | 0  | 0  | 
en_nqo        | NKo           | bam           | Nkoo          | bamb1269      | Africa        | ߓߡߊߣߊ߲ߞߊ߲     | N'Ko          | 0  | 0  | 0  | 
en_nr         | South Ndebele  | nbl           | Latn          | sout2831      | Africa        | isiNdebele seSewula  | Ndebele (South); Transvaal Ndebele; Southern Ndebele  | 130  | 863  | 4001  | 
en_nso        | Sepedi        | nso           | Latn          | nort2827      | Africa        | Sepedi        | Northern Sotho; Pedi  | 213  | 863  | 3996  | 
en_nus        | Nuer          | nus           | Latn          | nuer1246      | Africa        | Thok Naath    |               | 0  | 0  | 4001  | 
en_nv         | Navajo        | nav           | Latn          | nava1247      | Americas      | Diné; Naabeehó  | Navaho; Diné  | 0  | 0  | 3992  | 
en_ny         | Chichewa      | nya           | Latn          | nyan1308      | Africa        | Chilankhulo cha Chichewa  |               | 354  | 863  | 0  | 
en_oc         | Occitan       | oci           | Latn          | occi1239      | Europe        | Occitan       | Provençal     | 0  | 0  | 3998  | 
en_om         | Oromo         | orm           | Latn          | orom1259      | Africa        | Afaan Oromoo  | Afaan Oromoo  | 477  | 863  | 3992  | 
en_os         | Ossetian      | oss           | Cyrl          | osse1243      | Europe        | Ирон          | Ossetic; Iron  | 0  | 0  | 3915  | 
en_pa         | Punjabi       | pan           | Guru          | panj1256      | Asia          | ਗੁਰਮੁਖੀ       | Punjabi (Gurumukhi); Punjabi (India)  | 252  | 563  | 0  | 
en_pa-Arab    | Lahnda Punjabi (Pakistan)  | pan           | Arab          | west2341      | Asia          | لہندا پنجابی  | Punjabi (Lahnda); Punjabi (Western); Punjabi (India); Punjabi (Shahmukhi)  | 0  | 863  | 4001  | 
en_pag        | Pangasinan    | pag           | Latn          | pang1290      | Asia          | Pangasinan    | Pangasinense  | 0  | 0  | 3994  | 
en_pam        | Kapampangan   | pam           | Latn          | pamp1243      | Asia          | Kapampangan   | Pampango; Capampáñgan  | 0  | 0  | 3993  | 
en_pap        | Papiamento    | pap           | Latn          | papi1254      | Americas      | Papiamento    | Papiamento in Aruba; Papiamentu in Bonaire and Curaçao  | 0  | 0  | 4001  | 
en_pcm        | Nigerian Pidgin  | pcm           | Latn          | nige1256      | Africa        | Naijá, Pidgin for Nigerian  | Naija; Naijá; Pijin; Brokun; Broken  | 213  | 863  | 4001  | 
en_ps         | Pashto        | pbu           | Arab          | nort2646      | Asia          | پښتو ژبه      |               | 457  | 0  | 0  | 
en_pt-PT      | Portuguese (Portugal)  | por           | Latn          | port1283      | Europe        | português     |               | 0  | 0  | 3995  | 
en_qu         | Quechua       | que           | Latn          | quec1387      | Americas      | Runa Simi     |               | 0  | 863  | 3861  | 
en_quc        | K'iche'       | quc           | Latn          | kich1262      | Americas      | K'iche'       | Quiche; Quiché  | 0  | 0  | 3992  | 
en_rhg-Latn   | Rohingya (Latin script)  | rhg           | Latn          | rohi1241      | Asia          | Ruháingga     | Rohingya      | 0  | 0  | 3999  | 
en_rn         | Rundi         | run           | Latn          | rund1242      | Africa        | Ikirundi      | Kirundi       | 130  | 863  | 3999  | 
en_rom        | Romani        | rmy           | Latn          | roma1271      | Europe        | Rromani ćhib  | Romany; Romanes; Roma  | 0  | 0  | 3988  | 
en_ru         | Russian       | rus           | Cyrl          | russ1263      | Europe        | русский язык‎  |               | 66  | 0  | 0  | 
en_rw         | Kinyarwanda   | kin           | Latn          | kiny1244      | Africa        | Ikinyarwanda  |               | 345  | 863  | 0  | 
en_sa         | Sanskrit      | san           | Deva          | sans1269      | Asia          | संस्कृतम्     | Samskrit; Samskrt; Samskritam  | 0  | 863  | 3998  | 
en_sah        | Yakut         | sah           | Cyrl          | sakc1242      | Europe        | Саха          | Sakha; Saxa; Saqa; Yakutian  | 0  | 0  | 3983  | 
en_sat        | Santali (Ol Chiki script)  | sat           | Olck          | sant1265      | Asia          | ᱥᱟᱱᱛᱟᱲᱤ       | Santali; Santhali; Hor  | 0  | 863  | 4001  | 
en_sat-Latn   | Santali (Latin Script)  | sat           | Latn          | sant1265      | Asia          | Santali       | Santali; Santhali; Hor  | 0  | 863  | 4000  | 
en_scn        | Sicilian      | scn           | Latn          | sici1248      | Europe        | Sicilianu     |               | 100  | 0  | 3997  | 
en_sd-Deva    | Sindhi (Devanagari script)  | snd           | Deva          | sind1279      | Asia          | सिन्धी        |               | 456  | 0  | 0  | 
en_se         | Northern Sami  | sme           | Latn          | nort2641      | Europe        | davvisámegiella  | North Saami; North Sámi; Sami (North)  | 0  | 0  | 3980  | 
en_sg         | Sango         | sag           | Latn          | sang1327      | Africa        | Sango         |               | 0  | 0  | 3994  | 
en_sgj        | Surgujia      | sgj           | Deva          | surg1242      | Asia          | सरगुजिया      |               | 356  | 0  | 0  | 
en_shn        | Shan          | shn           | Mymr          | shan1277      | Asia          | တႆး; လိၵ်ႈတႆး  | Tai longe     | 0  | 0  | 4001  | 
en_si         | Sinhala       | sin           | Sinh          | sinh1246      | Asia          | සිංහල භාෂාව   |               | 254  | 763  | 0  | 
en_sjp        | Surjapuri     | sjp           | Deva          | surj1242      | Asia          | सुरजापुरी‎    |               | 299  | 0  | 0  | 
en_skr        | Saraiki       | skr           | Arab          | sara1261      | Asia          | سرائیکی       | Multani       | 0  | 0  | 4001  | 
en_sn         | Shona         | sna           | Latn          | shon1249      | Africa        | ChiShona      |               | 345  | 863  | 0  | 
en_so         | Somali        | som           | Latn          | soma1255      | Africa        | Af-Soomaali   |               | 339  | 862  | 0  | 
en_spv        | Sambalpuri    | spv           | Orya          | samb1314      | Asia          | ସମ୍ବଲପୁରୀ     |               | 457  | 0  | 0  | 
en_ss         | Swati         | ssw           | Latn          | swat1253      | Africa        | Siswati       | siSwati       | 130  | 863  | 3924  | 
en_st         | Sesotho       | sot           | Latn          | sout2824      | Africa        | seSotho       |               | 341  | 863  | 0  | 
en_sus        | Susu          | sus           | Latn          | susu1255      | Africa        | Sosokhui      |               | 130  | 863  | 4000  | 
en_sw         | Swahili       | swa           | Latn          | swah1253      | Africa        | Kiswahili     | Kiswahili     | 664  | 863  | 0  | 
en_syl        | Sylheti       | syl           | Beng          | sylh1242      | Asia          | সিলেটি        | Siloti        | 0  | 0  | 4001  | 
en_szl        | Silesian      | szl           | Latn          | sile1255      | Europe        | Ślůnski       |               | 0  | 0  | 3997  | 
en_ta         | Tamil         | tam           | Taml          | tami1289      | Asia          | தமிழ்         |               | 253  | 563  | 0  | 
en_tcy        | Tulu          | tcy           | Knda          | tulu1257      | Asia          | ತುಳು          |               | 451  | 0  | 4000  | 
en_te         | Telugu        | tel           | Telu          | telu1262      | Asia          | తెలుగు        |               | 253  | 563  | 0  | 
en_tet        | Tetum         | tet           | Latn          | tetu1246      | Asia          | Tetun         | Tetun         | 0  | 0  | 4001  | 
en_th         | Thai          | tha           | Thai          | thai1240      | Asia          | ภาษาไทย       |               | 254  | 753  | 0  | 
en_ti         | Tigrinya      | tir           | Ethi          | tigr1271      | Africa        | ትግርኛ          | Tigrigna      | 339  | 863  | 4000  | 
en_tig        | Tigre         | tig           | Ethi          | tigr1270      | Africa        | ትግሬ           | Tigré         | 260 | 863 | 4000 |
en_tiv        | Tiv           | tiv           | Latn          | tivv1240      | Africa        | Tiv           |               | 130  | 863  | 4001  | 
en_tn         | Tswana        | tsn           | Latn          | tswa1253      | Africa        | Setswana      | Batswana; Setswana  | 130  | 863  | 3995  | 
en_to         | Tonga (Tonga Islands)  | ton           | Latn          | tong1325      | Oceania       | Tonga         | Tongan; Tonga; Lea Faka-Tonga  | 0  | 0  | 4001  | 
en_tpi        | Tok Pisin     | tpi           | Latn          | tokp1241      | Oceania       | Tok Pisin     | Papua New Guinea Pidgin  | 0  | 0  | 4001  | 
en_trp        | Kokborok      | trp           | Latn          | kokb1243      | Asia          | Kokborok; Kókborok  | Tripuri; Tiprakok; Kok Borok; Kókborok; Tripura, Tipra, Tippera; ককবরক‎; Kókborok  | 457  | 0  | 3997  | 
en_ts         | Tsonga        | tso           | Latn          | tson1249      | Africa        | Xitsonga      |               | 130  | 863  | 3994  | 
en_tum        | Tumbuka       | tum           | Latn          | tumb1254      | Africa        | Chitumbuka    |               | 130  | 863  | 3983  | 
en_ty         | Tahitian      | tah           | Latn          | tahi1242      | Oceania       | Reo Tahiti; Tahiti  |               | 0  | 0  | 4001  | 
en_tyv        | Tuvan         | tyv           | Cyrl          | tuvi1241      | Asia          | тувинский     | Tuvinian; Tyvan  | 66  | 863  | 3984  | 
en_udm        | Udmurt        | udm           | Cyrl          | udmu1245      | Europe        | Удмурт кыл    |               | 0  | 0  | 3992  | 
en_unr-Deva   | Mundari (Devanagari script)  | unr           | Deva          | mund1335      | Asia          | मुंडारी       |               | 457  | 0  | 0  | 
en_ur         | Urdu          | urd           | Arab          | urdu1245      | Asia          | اردو          |               | 253  | 563  | 0  | 
en_ve         | Venda         | ven           | Latn          | vend1247      | Africa        | Tshivenḓa     | Tshivenda; Luvenda; Bavenda  | 130  | 863  | 3984  | 
en_vec        | Venetian      | vec           | Latn          | vene1256      | Europe        | Veneto        | Vèneto        | 0  | 0  | 4000  | 
en_war        | Waray (Philippines)  | war           | Latn          | wara1293      | Asia          | Waray         | Waray; Waray-Waray  | 0  | 0  | 3963  | 
en_wbr        | Wagdi         | wbr           | Deva          | wagd1238      | Asia          | वाग्दी‎       |               | 455  | 0  | 0  | 
en_wo         | Wolof         | wol           | Latn          | wolo1247      | Africa        | Wolof         |               | 345  | 863  | 4001  | 
en_xh         | Xhosa         | xho           | Latn          | xhos1239      | Africa        | isiXhosa      |               | 344  | 863  | 0  | 
en_xnr        | Kangri        | xnr           | Deva          | kang1292      | Asia          | कांगड़ी       |               | 457  | 0  | 0  | 
en_xsr-Tibt   | Sherpa (Tibetan script)  | xsr           | Tibt          | sher1258      | Asia          | ཤར་པའི་སྐད་ཡིག  |               | 457  | 0  | 0  | 
en_yo         | Yoruba        | yor           | Latn          | yoru1245      | Africa        | Èdè Yorùbá    |               | 668  | 863  | 0  | 
en_yua        | Yucatec Maya  | yua           | Latn          | yuca1254      | Americas      | Maayat'aan    | Mayan; Yucateco  | 0  | 0  | 3959  | 
en_yue        | Cantonese     | yue           | Hant          | yuee1245      | Asia          | 廣東話; 粵語; 廣州話; 白話;   | Yue Chinese   | 584  | 863  | 5253  | 
en_zap        | Zapotec       | zap           | Latn          | zapo1270      | Americas      | Diidxazá      |               | 0  | 0  | 3777  | 
en_zu         | Zulu          | zul           | Latn          | zulu1248      | Africa        | isiZulu       |               | 339  | 863  | 0  | 
en_zza        | Zazaki        | diq           | Latn          | zaza1245      | Asia          | Zazakî        | Zaza; Kurdish (Zazaki); Dimli  | 0  | 0  | 3978  | 
ru_abq        | Abaza         | abq           | Cyrl          | abaz1241      |               |               |               | 66  | 863  | 0  | 
ru_ce         | Chechen       | che           | Cyrl          | chec1245      | Europe        | Нохчийн       |               | 66  | 863  | 0  | 
ru_jdt        | Juhuri        | jdt           | Cyrl          | jude1256      |               |               | Judeo-Tat     | 584  | 863  | 4000  |
ru_kjh        | Khakas                          | kjh       | Cyrl          | khak1248  | Asia      | Хакас         |        | 66  | 863  | 0  |
zh_am         | Amharic       | amh           | Ethi          | amha1245      | Africa        | አማርኛ          |               | 329  | 0  | 0  | 
zh_sw         | Swahili       | swa           | Latn          | swah1253      | Africa        | Kiswahili     | Kiswahili     | 330  | 0  | 0  | 

## Notes on language codes and names

We use the backwards-compatible BCP-47 language code convention. Several of
these languages have various alternate code also in use, including:

*   **ak** Twi also uses the code `tw`. Note that using the supercode for the
    most prevelent language variety is very common, e.g. `ku` for `kmr`, `zh`
    for `cmn`, etc.
*   **ber** The grouping of the Tamazight languages is a matter of debate. The
    variety in these data is probably close to `tzm`, though a language expert
    should opine
*   **qu** Another supercode issue. The Quechua variety this data is closest to
    is likely `quy`, though a language expert should opine
*   **pa-Arab** is also referred to as `lah`
*   **mhr**: the previous release used `chm` for Meadow Mari, although `chm` is properly the superset, and `mhr` is the individual code for Meadow Mari.
*   **rom**: Similarly, we use `rom` for all Romani dialects, `ak` for Twi (see note above), and `ff` for all Fulfulde dialects.
*   **fa-AF,ar-MA**: We use `fa-AF` and `ar-MA`  for Dari and Darija respectively. The specific codes `prs` and `ary` are probably more precise.


Please note that the language name can be a point of considerable tension, and
there is rarely a "right" name for a language! This said, here are some
non-exhaustive notes that went into the names in the second column above, based
on conversations with speakers. We welcome more comments from the community:

*   **ak:** Calling this language "Twi" instead of "Akan" here is reflective of
    the corresponding translation models active on Google Translate. These are
    likely to mix different Akan dialects, including Twi proper, Fante, Akuapem Twi, etc.. Therefore, from a linguistic perspective, one would call this "Akan" and use the corresponding code "ak". However, this is a more academic word for the language; according to native speaker consultants, "Akan" is usually used to describe the ethnic group rather than the language, so they suggested simply calling this "Twi", which is most likely accurate for the large majority of model outputs.
*   **ckb:** *Central Kurdish* is a more academic name that may not be as widely
    known to speakers of the language, so *Sorani* is preferred -- though they
    are both acceptable.
*   **dv:** There is not a consistent romanization of this language, and both
    *Divehi* and *Dhivehi* are common. The first consonant in this language is a
    dental, non-aspirated *d*. When transliterating Indian language names there is
    no standard about how to represent this sound. In the south, "dh" usually
    refers to the dental consonant; in the North, it just as often refers to the
    aspirated one. However, in both cases, it is common that "d" alone would
    represent the retroflex consonant, so it is possible that *Divehi* would be
    mispronounced more often.
*   **gom:** Technically, `gom` is the code for *Goan* Konkani only. Other
    varieties of Konkani, like Mangalore Konkani (which oddly enough does not
    have an ISO code), are mutually unintelligible! There is certainly dispute
    about whether to treat Konkani as one language or not.
*   **ilo:** Native speakers give a variety of different answers around the
    correct name. Some say that *Ilocano* is more formal, whereas *Ilokano* is
    more informal; some say that both of these actually refer to the people, and
    that *Iloko* is the only correct term for the language.
*   **lg:** Speakers usually refer to this language as "Luganda"; linguists sometimes call it
    "Ganda", but like Sepedi, this is not usually used by people
    familiar with the language.
*   **lus:** There is agreement that *Lushai* is an obsolete colonial name and
    should not be used. *Mizo* is the preferred name.
*   **mni-Mtei:** The conventional and most common name for this language is
    *Manipuri*. However, in reality, this is only the language of one of the
    many ethnicities in Manipur, so that name can be seen as offensive to some.
    Therefore, we use the endonym *Meiteilon*, with the conventional name
    (Manipuri) in parentheses.
*   **nso:** Although a linguist might say that Sepedi is a dialect of Northern
    Sotho, speakers often say that they call the whole language Sepedi, and that
    *Northern Sotho* has offensive colonial overtones. Others, however, may
    disagree with this. The endonym *Sesotho sa Leboa* is not uncommon. There is
    agreement that no-one uses *Pedi*.
*   **qu:** These translations are technically in *Southern* Quechua. However,
    this is a point of some contention. Some will opine that "Quechua" is not a
    language but a family of languages. Others, however, say that they all feel
    like one language, and that the regional differences are slight, and it's
    easy for Peruvians, Bolivians, and even Ecuadorians to understand each
    other. The majority opinion among the naive speakers we talked to seemed to
    be closer to the latter, so we have opted for the name "Quechua".
*   **ti:** In Tigray *Tigrigna* is the most common Romanization, and in Eritrea
    *Tigrinya* is.
*   **zap:** Linguists usually talk about the Zapotec *languages*, rather than
    considering Zapotec a single language. However, just as with Quechua above,
    conversations with a native speaker indicated that they perceived Zapotec
    as one language, with a variety of local variants that are all easy enough
    to understand (excepting one or two). A broader survey would help resolve this question.
*   Those languages in this dataset that are not on Google Translate have yet to
    undergo a more careful name review; if you see a name in the list above that
    you want to correct, please contact us!

Special note on Bantu languages: Bantu language names have a special noun-class
prefix for languages, like <i>xi</i>Tsonga, <i>se</i>Pedi, <i>ki</i>Swahili, <i>isi</i>Zulu,
<i>lu</i>Ganda, <i>si</i>Swati, <i>isi</i>Ndebele, <i>tshi</i>Venda, and so on. However, there is no
pattern as to whether this prefix is used in the conventional English form of
the name. For instance, Xhosa usually leaves off the <i>isi-</i> in English, whereas
Lingala almost never leaves off the <i>li-</i>. Others, like (xi)Tsonga, seem to be
frequently used in both forms. Linguistic resources occasionally strip the
prefixes, yielding names like "Ganda", "Pedi" and so on, perhaps out of a desire
for consistent handling of the noun class prefix. (Even the *ba* in *Bantu* is
such a prefix, so these languages are sometimes called the *Ntu* languages!)

For convenience, here is a mapping from codes used by Flores and SMOL:

```
flores2smol = {
'ace_Arab': 'ace-Arab', 'ace_Latn': 'ace', 'acm_Arab': 'acm', 'acq_Arab': 'acq', 'aeb_Arab': 'aeb', 'afr_Latn': 'af', 'ajp_Arab': 'ajp',
'aka_Latn': 'ak', 'als_Latn': 'sq', 'amh_Ethi': 'am', 'apc_Arab': 'apc', 'arb_Arab': 'ar', 'arb_Latn': 'ar-Latn', 'ars_Arab': 'ars',
'ary_Arab': 'ar-MA', 'arz_Arab': 'arz', 'asm_Beng': 'as', 'ast_Latn': 'ast', 'awa_Deva': 'awa', 'ayr_Latn': 'ay', 'azb_Arab': 'azb',
'azj_Latn': 'az', 'bak_Cyrl': 'ba', 'bam_Latn': 'bm', 'ban_Latn': 'ban', 'bel_Cyrl': 'be', 'bem_Latn': 'bem', 'ben_Beng': 'bn',
'bho_Deva': 'bho', 'bjn_Arab': 'bjn-Arab', 'bjn_Latn': 'bjn', 'bod_Tibt': 'bo', 'bos_Latn': 'bs', 'bug_Latn': 'bug', 'bul_Cyrl': 'bg',
'cat_Latn': 'ca', 'ceb_Latn': 'ceb', 'ces_Latn': 'cs', 'cjk_Latn': 'cjk', 'ckb_Arab': 'ckb', 'crh_Latn': 'crh-Latn', 'cym_Latn': 'cy',
'dan_Latn': 'da', 'deu_Latn': 'de', 'dik_Latn': 'din', 'dyu_Latn': 'dyu', 'dzo_Tibt': 'dz', 'ell_Grek': 'el', 'eng_Latn': 'en',
'epo_Latn': 'eo', 'est_Latn': 'et', 'eus_Latn': 'eu', 'ewe_Latn': 'ee', 'fao_Latn': 'fo', 'fij_Latn': 'fj', 'fin_Latn': 'fi',
'fon_Latn': 'fon', 'fra_Latn': 'fr', 'fur_Latn': 'fur', 'fuv_Latn': 'ff', 'gaz_Latn': 'om', 'gla_Latn': 'gd', 'gle_Latn': 'ga',
'glg_Latn': 'gl', 'grn_Latn': 'gn', 'guj_Gujr': 'gu', 'hat_Latn': 'ht', 'hau_Latn': 'ha', 'heb_Hebr': 'iw', 'hin_Deva': 'hi',
'hne_Deva': 'hne', 'hrv_Latn': 'hr', 'hun_Latn': 'hu', 'hye_Armn': 'hy', 'ibo_Latn': 'ig', 'ilo_Latn': 'ilo', 'ind_Latn': 'id',
'isl_Latn': 'is', 'ita_Latn': 'it', 'jav_Latn': 'jv', 'jpn_Jpan': 'ja', 'kab_Latn': 'kab', 'kac_Latn': 'kac', 'kam_Latn': 'kam',
'kan_Knda': 'kn', 'kas_Arab': 'ks', 'kas_Deva': 'ks-Deva', 'kat_Geor': 'ka', 'kaz_Cyrl': 'kk', 'kbp_Latn': 'kbp', 'kea_Latn': 'kea',
'khk_Cyrl': 'mn', 'khm_Khmr': 'km', 'kik_Latn': 'ki', 'kin_Latn': 'rw', 'kir_Cyrl': 'ky', 'kmb_Latn': 'kmb', 'kmr_Latn': 'ku',
'knc_Arab': 'kr-Arab', 'knc_Latn': 'kr', 'kon_Latn': 'kg', 'kor_Hang': 'ko', 'lao_Laoo': 'lo', 'lij_Latn': 'lij', 'lim_Latn': 'li',
'lin_Latn': 'ln', 'lit_Latn': 'lt', 'lmo_Latn': 'lmo', 'ltg_Latn': 'ltg', 'ltz_Latn': 'lb', 'lua_Latn': 'lua', 'lug_Latn': 'lg',
'luo_Latn': 'luo', 'lus_Latn': 'lus', 'lvs_Latn': 'lv', 'mag_Deva': 'mag', 'mai_Deva': 'mai', 'mal_Mlym': 'ml', 'mar_Deva': 'mr',
'min_Arab': 'min-Arab', 'min_Latn': 'min', 'mkd_Cyrl': 'mk', 'mlt_Latn': 'mt', 'mni_Beng': 'mni', 'mos_Latn': 'mos', 'mri_Latn': 'mi',
'mya_Mymr': 'my', 'nld_Latn': 'nl', 'nno_Latn': 'nn', 'nob_Latn': 'no', 'npi_Deva': 'ne', 'nso_Latn': 'nso', 'nus_Latn': 'nus',
'nya_Latn': 'ny', 'oci_Latn': 'oc', 'ory_Orya': 'or', 'pag_Latn': 'pag', 'pan_Guru': 'pa', 'pap_Latn': 'pap', 'pbt_Arab': 'ps',
'pes_Arab': 'fa', 'plt_Latn': 'mg', 'pol_Latn': 'pl', 'por_Latn': 'pt', 'prs_Arab': 'fa-AF', 'quy_Latn': 'quy', 'ron_Latn': 'ro',
'run_Latn': 'rn', 'rus_Cyrl': 'ru', 'sag_Latn': 'sg', 'san_Deva': 'sa', 'sat_Olck': 'sat', 'scn_Latn': 'scn', 'shn_Mymr': 'shn',
'sin_Sinh': 'si', 'slk_Latn': 'sk', 'slv_Latn': 'sl', 'smo_Latn': 'sm', 'sna_Latn': 'sn', 'snd_Arab': 'sd', 'som_Latn': 'so',
'sot_Latn': 'st', 'spa_Latn': 'es', 'srd_Latn': 'sc', 'srp_Cyrl': 'sr', 'ssw_Latn': 'ss', 'sun_Latn': 'su', 'swe_Latn': 'sv',
'swh_Latn': 'sw', 'szl_Latn': 'szl', 'tam_Taml': 'ta', 'taq_Latn': 'taq', 'taq_Tfng': 'taq-Tfng', 'tat_Cyrl': 'tt', 'tel_Telu': 'te',
'tgk_Cyrl': 'tg', 'tgl_Latn': 'fil', 'tha_Thai': 'th', 'tir_Ethi': 'ti', 'tpi_Latn': 'tpi', 'tsn_Latn': 'tn', 'tso_Latn': 'ts',
'tuk_Latn': 'tk', 'tum_Latn': 'tum', 'tur_Latn': 'tr', 'twi_Latn': 'ak', 'tzm_Tfng': 'ber', 'uig_Arab': 'ug', 'ukr_Cyrl': 'uk',
'umb_Latn': 'umb', 'urd_Arab': 'ur', 'uzn_Latn': 'uz', 'vec_Latn': 'vec', 'vie_Latn': 'vi', 'war_Latn': 'war', 'wol_Latn': 'wo',
'xho_Latn': 'xh', 'ydd_Hebr': 'yi', 'yor_Latn': 'yo', 'yue_Hant': 'yue', 'zho_Hans': 'zh', 'zho_Hant': 'zh-Hant', 'zsm_Latn': 'ms', 'zul_Latn': 'zu',}
```

## Known issues

There are several known issues of this dataset:

*   The translations into Kituba (`ktu`), Tulu (`tcy`), Nepali (`ne`), and
    Tibetan (`bo`) caused notable regressions in `ChrF`, suggesting that they
    are low-quality, though this could also be an issue with training or
    evaluation.
*   The Manx (`gv`) split of GATITOS that was originally released was spurious.
    It has been removed.





### Citations

To cite SMOL and GATITOS, please use the following:

```
@misc{caswell2025smol,
      title={{SMOL: Professionally translated parallel data for 115 under-represented languages}},
      author={Isaac Caswell and Elizabeth Nielsen and Jiaming Luo and Colin Cherry and Geza Kovacs and Hadar Shemtov and Partha Talukdar and Dinesh Tewari and Baba Mamadi Diane and Koulako Moussa Doumbouya and Djibrila Diane and Solo Farabado Cissé and Edoardo Ferrante and Alessandro Guasoni and Mamadou K. Keita and Sudhamoy DebBarma and Ali Kuzhuget and David Anugraha and Muhammad Ravi Shulthan Habibi and Sina Ahmadi and Mingfei Lau and Jonathan Eng},
      year={2025},
      eprint={2502.12301},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.12301},
}

@inproceedings{jones-etal-2023-gatitos,
    title = {{"GATITOS: Using a New Multilingual Lexicon for Low-resource Machine Translation"}},
    author = "Jones, Alexander  and
      Caswell, Isaac  and
      Firat, Orhan  and
      Saxena, Ishank",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.26/",
    doi = "10.18653/v1/2023.emnlp-main.26",
    pages = "371--405",
    abstract = "Modern machine translation models and language models are able to translate without having been trained on parallel data, greatly expanding the set of languages that they can serve. However, these models still struggle in a variety of predictable ways, a problem that cannot be overcome without at least some trusted bilingual data. This work expands on a cheap and abundant resource to combat this problem: bilingual lexica. We test the efficacy of bilingual lexica in a real-world set-up, on 200-language translation models trained on web-crawled text. We present several findings: (1) using lexical data augmentation, we demonstrate sizable performance gains for unsupervised translation; (2) we compare several families of data augmentation, demonstrating that they yield similar improvements, and can be combined for even greater improvements; (3) we demonstrate the importance of carefully curated lexica over larger, noisier ones, especially with larger models; and (4) we compare the efficacy of multilingual lexicon data versus human-translated parallel data. Based on results from (3), we develop and open-source GATITOS, a high-quality, curated dataset in 168 tail languages, one of the first human-translated resources to cover many of these languages."
}
```


### Contact

We welcome contributions, corrections, and suggestions, especially from speakers
of these languages. If you speak any of these languages and notice quality
issues, please file bugs on this repo or contact
{icaswell, eknielsen}꩜google.com. This
repository may be updated sporadically with corrections or additional
translations.


## License

This data is released under cc-by-4.0
