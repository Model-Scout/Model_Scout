---
license: cc-by-nc-4.0
task_categories:
- automatic-speech-recognition
- text-to-speech
- audio-classification
language:
- af
- am
- ar
- az
- be
- bn
- ca
- ckb
- cnr
- crs
- cs
- de
- dv
- el
- en
- eo
- es
- fa
- fr
- ga
- grc
- ha
- he
- hi
- hu
- hy
- id
- ig
- iu
- ja
- ka
- kk
- km
- ko
- la
- lb
- lo
- mfe
- mi
- ml
- mn
- mr
- ms
- my
- ne
- nl
- nr
- nso
- om
- pa
- pl
- pt
- rm
- ro
- ru
- rw
- si
- sm
- sn
- sq
- ss
- st
- sv
- sw
- ta
- th
- ti
- tl
- tn
- tr
- ts
- ug
- uz
- ve
- vi
- xh
- yue
- zh
- zu
size_categories:
- 10M<n<100M
pretty_name: WorldSpeech
tags:
- speech
- multilingual
- low-resource
- parliamentary
- asr
- tts
- audio
configs:
- config_name: af_za
  data_files:
  - split: train
    path: data/af_za/*train-*.parquet
  - split: test
    path: data/af_za/*test-*.parquet
- config_name: am_et
  data_files:
  - split: train
    path: data/am_et/*train-*.parquet
  - split: test
    path: data/am_et/*test-*.parquet
- config_name: ar_bh
  data_files:
  - split: train
    path: data/ar_bh/*train-*.parquet
  - split: test
    path: data/ar_bh/*test-*.parquet
- config_name: ar_dz
  data_files:
  - split: train
    path: data/ar_dz/*train-*.parquet
  - split: test
    path: data/ar_dz/*test-*.parquet
- config_name: ar_eg
  data_files:
  - split: train
    path: data/ar_eg/*train-*.parquet
  - split: test
    path: data/ar_eg/*test-*.parquet
- config_name: ar_iq
  data_files:
  - split: train
    path: data/ar_iq/*train-*.parquet
  - split: test
    path: data/ar_iq/*test-*.parquet
- config_name: ar_kw
  data_files:
  - split: train
    path: data/ar_kw/*train-*.parquet
  - split: test
    path: data/ar_kw/*test-*.parquet
- config_name: ar_ma
  data_files:
  - split: train
    path: data/ar_ma/*train-*.parquet
  - split: test
    path: data/ar_ma/*test-*.parquet
- config_name: ar_sa
  data_files:
  - split: train
    path: data/ar_sa/*train-*.parquet
  - split: test
    path: data/ar_sa/*test-*.parquet
- config_name: ar_tn
  data_files:
  - split: train
    path: data/ar_tn/*train-*.parquet
  - split: test
    path: data/ar_tn/*test-*.parquet
- config_name: ar_un
  data_files:
  - split: train
    path: data/ar_un/*train-*.parquet
  - split: test
    path: data/ar_un/*test-*.parquet
- config_name: as_in
  data_files:
  - split: train
    path: data/as_in/in_as_air-train-*.parquet
  - split: test
    path: data/as_in/in_as_air-test-*.parquet
- config_name: az_az
  data_files:
  - split: train
    path: data/az_az/*train-*.parquet
  - split: test
    path: data/az_az/*test-*.parquet
- config_name: be_by
  data_files:
  - split: train
    path: data/be_by/*train-*.parquet
  - split: test
    path: data/be_by/*test-*.parquet
- config_name: bn_bd
  data_files:
  - split: train
    path: data/bn_bd/*train-*.parquet
  - split: test
    path: data/bn_bd/*test-*.parquet
- config_name: bn_in
  data_files:
  - split: train
    path: data/bn_in/in_bn_air-train-*.parquet
  - split: test
    path: data/bn_in/in_bn_air-test-*.parquet
- config_name: ca_es
  data_files:
  - split: train
    path: data/ca_es/*train-*.parquet
  - split: test
    path: data/ca_es/*test-*.parquet
- config_name: ca_fr
  default: true
  data_files:
  - split: train
    path: data/ca_fr/train-*.parquet
  - split: test
    path: data/ca_fr/test-*.parquet
- config_name: ckb_iq
  data_files:
  - split: train
    path: data/ckb_iq/*train-*.parquet
  - split: test
    path: data/ckb_iq/*test-*.parquet
- config_name: cn_ug
  data_files:
  - split: train
    path: data/cn_ug/*train-*.parquet
  - split: test
    path: data/cn_ug/*test-*.parquet
- config_name: cnr_me
  data_files:
  - split: train
    path: data/cnr_me/*train-*.parquet
  - split: test
    path: data/cnr_me/*test-*.parquet
- config_name: crs_sc
  data_files:
  - split: train
    path: data/crs_sc/*train-*.parquet
  - split: test
    path: data/crs_sc/*test-*.parquet
- config_name: cs_cz
  data_files:
  - split: train
    path:
    - data/cs_cz/*train-*.parquet
    - data/cz_cs/*train-*.parquet
  - split: test
    path:
    - data/cs_cz/*test-*.parquet
    - data/cz_cs/*test-*.parquet
- config_name: de_at
  data_files:
  - split: train
    path: data/de_at/*train-*.parquet
  - split: test
    path: data/de_at/*test-*.parquet
- config_name: de_li
  data_files:
  - split: train
    path: data/de_li/train-*.parquet
  - split: test
    path: data/de_li/test-*.parquet
- config_name: dgo_in
  data_files:
  - split: train
    path: data/dgo_in/in_dgo_air-train-*.parquet
  - split: test
    path: data/dgo_in/in_dgo_air-test-*.parquet
- config_name: dv_mv
  data_files:
  - split: train
    path: data/dv_mv/*train-*.parquet
  - split: test
    path: data/dv_mv/*test-*.parquet
- config_name: el_cy
  data_files:
  - split: train
    path: data/el_cy/*train-*.parquet
  - split: test
    path: data/el_cy/*test-*.parquet
- config_name: el_gr
  data_files:
  - split: train
    path: data/el_gr/*train-*.parquet
  - split: test
    path: data/el_gr/*test-*.parquet
- config_name: en_au
  data_files:
  - split: train
    path: data/en_au/*train-*.parquet
  - split: test
    path: data/en_au/*test-*.parquet
- config_name: en_jm
  data_files:
  - split: train
    path: data/en_jm/*train-*.parquet
  - split: test
    path: data/en_jm/*test-*.parquet
- config_name: en_ke
  data_files:
  - split: train
    path: data/en_ke/*train-*.parquet
  - split: test
    path: data/en_ke/*test-*.parquet
- config_name: en_nz
  data_files:
  - split: train
    path: data/en_nz/*train-*.parquet
  - split: test
    path: data/en_nz/*test-*.parquet
- config_name: en_pk
  data_files:
  - split: train
    path: data/en_pk/train-*.parquet
  - split: test
    path: data/en_pk/test-*.parquet
- config_name: en_sl
  data_files:
  - split: train
    path: data/en_sl/*train-*.parquet
  - split: test
    path: data/en_sl/*test-*.parquet
- config_name: en_us
  data_files:
  - split: train
    path: data/en_us/*train-*.parquet
  - split: test
    path: data/en_us/*test-*.parquet
- config_name: en_zm
  data_files:
  - split: train
    path: data/en_zm/*train-*.parquet
  - split: test
    path: data/en_zm/*test-*.parquet
- config_name: eo
  data_files:
  - split: train
    path: data/eo/*train-*.parquet
  - split: test
    path: data/eo/*test-*.parquet
- config_name: es_ar
  data_files:
  - split: train
    path: data/es_ar/*train-*.parquet
  - split: test
    path: data/es_ar/*test-*.parquet
- config_name: es_cl
  data_files:
  - split: train
    path: data/es_cl/*train-*.parquet
  - split: test
    path: data/es_cl/*test-*.parquet
- config_name: es_co
  data_files:
  - split: train
    path: data/es_co/*train-*.parquet
  - split: test
    path: data/es_co/*test-*.parquet
- config_name: es_es
  data_files:
  - split: train
    path: data/es_es/*train-*.parquet
  - split: test
    path: data/es_es/*test-*.parquet
- config_name: es_mx
  data_files:
  - split: train
    path: data/es_mx/*train-*.parquet
  - split: test
    path: data/es_mx/*test-*.parquet
- config_name: es_pe
  data_files:
  - split: train
    path: data/es_pe/*train-*.parquet
  - split: test
    path: data/es_pe/*test-*.parquet
- config_name: es_pr
  data_files:
  - split: train
    path: data/es_pr/*train-*.parquet
  - split: test
    path: data/es_pr/*test-*.parquet
- config_name: es_py
  data_files:
  - split: train
    path: data/es_py/*train-*.parquet
  - split: test
    path: data/es_py/*test-*.parquet
- config_name: es_uy
  data_files:
  - split: train
    path: data/es_uy/*train-*.parquet
  - split: test
    path: data/es_uy/*test-*.parquet
- config_name: fa_ir
  data_files:
  - split: train
    path: data/fa_ir/*train-*.parquet
  - split: test
    path: data/fa_ir/*test-*.parquet
- config_name: fr_ca
  data_files:
  - split: train
    path: data/fr_ca/*train-*.parquet
  - split: test
    path: data/fr_ca/*test-*.parquet
- config_name: fr_cd
  data_files:
  - split: train
    path: data/fr_cd/*train-*.parquet
  - split: test
    path: data/fr_cd/*test-*.parquet
- config_name: fr_ci
  data_files:
  - split: train
    path: data/fr_ci/*train-*.parquet
  - split: test
    path: data/fr_ci/*test-*.parquet
- config_name: grc_gr
  data_files:
  - split: train
    path: data/grc_gr/*train-*.parquet
  - split: test
    path: data/grc_gr/*test-*.parquet
- config_name: gu_in
  data_files:
  - split: train
    path: data/gu_in/in_gu_air-train-*.parquet
  - split: test
    path: data/gu_in/in_gu_air-test-*.parquet
- config_name: ha_ng
  data_files:
  - split: train
    path: data/ha_ng/*train-*.parquet
  - split: test
    path: data/ha_ng/*test-*.parquet
- config_name: ha_td
  data_files:
  - split: train
    path: data/ha_td/*train-*.parquet
  - split: test
    path: data/ha_td/*test-*.parquet
- config_name: he_il
  data_files:
  - split: train
    path: data/he_il/*train-*.parquet
  - split: test
    path: data/he_il/*test-*.parquet
- config_name: hi_in
  data_files:
  - split: train
    path:
    - data/hi_in/train-*.parquet
    - data/hi_in/in_hi_bh-train-*.parquet
    - data/hi_in/in_hi_mkb-train-*.parquet
    - data/hi_in/in_hi_rj-train-*.parquet
    - data/hi_in/in_hi_air-train-*.parquet
    - data/hi_in/in_hi_rs-train-*.parquet
  - split: test
    path:
    - data/hi_in/test-*.parquet
    - data/hi_in/in_hi_bh-test-*.parquet
    - data/hi_in/in_hi_mkb-test-*.parquet
    - data/hi_in/in_hi_rj-test-*.parquet
    - data/hi_in/in_hi_air-test-*.parquet
    - data/hi_in/in_hi_rs-test-*.parquet
- config_name: hu_hu
  data_files:
  - split: train
    path: data/hu_hu/*train-*.parquet
  - split: test
    path: data/hu_hu/*test-*.parquet
- config_name: hy_am
  data_files:
  - split: train
    path: data/hy_am/*train-*.parquet
  - split: test
    path: data/hy_am/*test-*.parquet
- config_name: id_id
  data_files:
  - split: train
    path: data/id_id/*train-*.parquet
  - split: test
    path: data/id_id/*test-*.parquet
- config_name: ig_ng
  data_files:
  - split: train
    path: data/ig_ng/*train-*.parquet
  - split: test
    path: data/ig_ng/*test-*.parquet
- config_name: ja_jp
  data_files:
  - split: train
    path: data/ja_jp/*train-*.parquet
  - split: test
    path: data/ja_jp/*test-*.parquet
- config_name: ka_ge
  data_files:
  - split: train
    path: data/ka_ge/*train-*.parquet
  - split: test
    path: data/ka_ge/*test-*.parquet
- config_name: kh_km
  data_files:
  - split: train
    path: data/kh_km/*train-*.parquet
  - split: test
    path: data/kh_km/*test-*.parquet
- config_name: kk_kz
  data_files:
  - split: train
    path: data/kk_kz/*train-*.parquet
  - split: test
    path: data/kk_kz/*test-*.parquet
- config_name: kn_in
  data_files:
  - split: train
    path: data/kn_in/in_kn_air-train-*.parquet
  - split: test
    path: data/kn_in/in_kn_air-test-*.parquet
- config_name: ko_kr
  data_files:
  - split: train
    path: data/ko_kr/*train-*.parquet
  - split: test
    path: data/ko_kr/*test-*.parquet
- config_name: kok_in
  data_files:
  - split: train
    path: data/kok_in/in_kok_air-train-*.parquet
  - split: test
    path: data/kok_in/in_kok_air-test-*.parquet
- config_name: la_lo
  data_files:
  - split: train
    path: data/la_lo/*train-*.parquet
  - split: test
    path: data/la_lo/*test-*.parquet
- config_name: la_va
  data_files:
  - split: train
    path: data/la_va/*train-*.parquet
  - split: test
    path: data/la_va/*test-*.parquet
- config_name: lb_lu
  data_files:
  - split: train
    path: data/lb_lu/*train-*.parquet
  - split: test
    path: data/lb_lu/*test-*.parquet
- config_name: mai_in
  data_files:
  - split: train
    path: data/mai_in/in_mai_air-train-*.parquet
  - split: test
    path: data/mai_in/in_mai_air-test-*.parquet
- config_name: mfe_mu
  data_files:
  - split: train
    path: data/mfe_mu/*train-*.parquet
  - split: test
    path: data/mfe_mu/*test-*.parquet
- config_name: mi_nz
  data_files:
  - split: train
    path: data/mi_nz/*train-*.parquet
  - split: test
    path: data/mi_nz/*test-*.parquet
- config_name: ml_in
  data_files:
  - split: train
    path:
    - data/ml_in/*train-*.parquet
    - data/ml_in/in_ml_air-train-*.parquet
  - split: test
    path:
    - data/ml_in/*test-*.parquet
    - data/ml_in/in_ml_air-test-*.parquet
- config_name: mm_my
  data_files:
  - split: train
    path: data/mm_my/*train-*.parquet
  - split: test
    path: data/mm_my/*test-*.parquet
- config_name: mn_mn
  data_files:
  - split: train
    path: data/mn_mn/*train-*.parquet
  - split: test
    path: data/mn_mn/*test-*.parquet
- config_name: mr_in
  data_files:
  - split: train
    path:
    - data/mr_in/*train-*.parquet
    - data/mr_in/in_mr_air-train-*.parquet
  - split: test
    path:
    - data/mr_in/*test-*.parquet
    - data/mr_in/in_mr_air-test-*.parquet
- config_name: ms_my
  data_files:
  - split: train
    path: data/ms_my/*train-*.parquet
  - split: test
    path: data/ms_my/*test-*.parquet
- config_name: ne_in
  data_files:
  - split: train
    path: data/ne_in/in_ne_air-train-*.parquet
  - split: test
    path: data/ne_in/in_ne_air-test-*.parquet
- config_name: ne_np
  data_files:
  - split: train
    path: data/ne_np/*train-*.parquet
  - split: test
    path: data/ne_np/*test-*.parquet
- config_name: nl_be
  data_files:
  - split: train
    path: data/nl_be/*train-*.parquet
  - split: test
    path: data/nl_be/*test-*.parquet
- config_name: nl_nl
  data_files:
  - split: train
    path: data/nl_nl/*train-*.parquet
  - split: test
    path: data/nl_nl/*test-*.parquet
- config_name: nr_za
  data_files:
  - split: train
    path: data/nr_za/*train-*.parquet
  - split: test
    path: data/nr_za/*test-*.parquet
- config_name: nso_za
  data_files:
  - split: train
    path: data/nso_za/*train-*.parquet
  - split: test
    path: data/nso_za/*test-*.parquet
- config_name: om_et
  data_files:
  - split: train
    path: data/om_et/*train-*.parquet
  - split: test
    path: data/om_et/*test-*.parquet
- config_name: or_in
  data_files:
  - split: train
    path: data/or_in/in_or_air-train-*.parquet
  - split: test
    path: data/or_in/in_or_air-test-*.parquet
- config_name: pa_in
  data_files:
  - split: train
    path:
    - data/pa_in/*train-*.parquet
    - data/pa_in/in_pa_air-train-*.parquet
  - split: test
    path:
    - data/pa_in/*test-*.parquet
    - data/pa_in/in_pa_air-test-*.parquet
- config_name: pl_pl
  data_files:
  - split: train
    path: data/pl_pl/*train-*.parquet
  - split: test
    path: data/pl_pl/*test-*.parquet
- config_name: pt_br
  data_files:
  - split: train
    path: data/pt_br/*train-*.parquet
  - split: test
    path: data/pt_br/*test-*.parquet
- config_name: rm_ch
  data_files:
  - split: train
    path: data/rm_ch/*train-*.parquet
  - split: test
    path: data/rm_ch/*test-*.parquet
- config_name: ro_md
  data_files:
  - split: train
    path: data/ro_md/*train-*.parquet
  - split: test
    path: data/ro_md/*test-*.parquet
- config_name: ro_ro
  data_files:
  - split: train
    path: data/ro_ro/*train-*.parquet
  - split: test
    path: data/ro_ro/*test-*.parquet
- config_name: ru_by
  data_files:
  - split: train
    path: data/ru_by/*train-*.parquet
  - split: test
    path: data/ru_by/*test-*.parquet
- config_name: ru_ru
  data_files:
  - split: train
    path: data/ru_ru/*train-*.parquet
  - split: test
    path: data/ru_ru/*test-*.parquet
- config_name: rw_rw
  data_files:
  - split: train
    path: data/rw_rw/*train-*.parquet
  - split: test
    path: data/rw_rw/*test-*.parquet
- config_name: si_lk
  data_files:
  - split: train
    path: data/si_lk/*train-*.parquet
  - split: test
    path: data/si_lk/*test-*.parquet
- config_name: sm_ws
  data_files:
  - split: train
    path: data/sm_ws/*train-*.parquet
  - split: test
    path: data/sm_ws/*test-*.parquet
- config_name: sn_zw
  data_files:
  - split: train
    path: data/sn_zw/*train-*.parquet
  - split: test
    path: data/sn_zw/*test-*.parquet
- config_name: sq_al
  data_files:
  - split: train
    path: data/sq_al/*train-*.parquet
  - split: test
    path: data/sq_al/*test-*.parquet
- config_name: sq_xk
  data_files:
  - split: train
    path: data/sq_xk/*train-*.parquet
  - split: test
    path: data/sq_xk/*test-*.parquet
- config_name: ss_za
  data_files:
  - split: train
    path: data/ss_za/*train-*.parquet
  - split: test
    path: data/ss_za/*test-*.parquet
- config_name: st_za
  data_files:
  - split: train
    path: data/st_za/*train-*.parquet
  - split: test
    path: data/st_za/*test-*.parquet
- config_name: sv_ax
  data_files:
  - split: train
    path: data/sv_ax/*train-*.parquet
  - split: test
    path: data/sv_ax/*test-*.parquet
- config_name: sw_ke
  data_files:
  - split: train
    path: data/sw_ke/*train-*.parquet
  - split: test
    path: data/sw_ke/*test-*.parquet
- config_name: sw_tz
  data_files:
  - split: train
    path:
    - data/sw_tz/tz_sw_znz-train-*.parquet
    - data/sw_tz/tz_sw_bunge-train-*.parquet
  - split: test
    path:
    - data/sw_tz/tz_sw_znz-test-*.parquet
    - data/sw_tz/tz_sw_bunge-test-*.parquet
- config_name: ta_in
  data_files:
  - split: train
    path: data/ta_in/in_ta_air-train-*.parquet
  - split: test
    path: data/ta_in/in_ta_air-test-*.parquet
- config_name: ta_lk
  data_files:
  - split: train
    path: data/ta_lk/*train-*.parquet
  - split: test
    path: data/ta_lk/*test-*.parquet
- config_name: te_in
  data_files:
  - split: train
    path: data/te_in/in_te_air-train-*.parquet
  - split: test
    path: data/te_in/in_te_air-test-*.parquet
- config_name: th_th
  data_files:
  - split: train
    path: data/th_th/*train-*.parquet
  - split: test
    path: data/th_th/*test-*.parquet
- config_name: ti_et
  data_files:
  - split: train
    path: data/ti_et/*train-*.parquet
  - split: test
    path: data/ti_et/*test-*.parquet
- config_name: tl_ph
  data_files:
  - split: train
    path: data/tl_ph/*train-*.parquet
  - split: test
    path: data/tl_ph/*test-*.parquet
- config_name: tn_bw
  data_files:
  - split: train
    path: data/tn_bw/*train-*.parquet
  - split: test
    path: data/tn_bw/*test-*.parquet
- config_name: tn_za
  data_files:
  - split: train
    path: data/tn_za/*train-*.parquet
  - split: test
    path: data/tn_za/*test-*.parquet
- config_name: tr_tr
  data_files:
  - split: train
    path: data/tr_tr/*train-*.parquet
  - split: test
    path: data/tr_tr/*test-*.parquet
- config_name: ts_za
  data_files:
  - split: train
    path: data/ts_za/*train-*.parquet
  - split: test
    path: data/ts_za/*test-*.parquet
- config_name: ur_in
  data_files:
  - split: train
    path: data/ur_in/in_ur_air-train-*.parquet
  - split: test
    path: data/ur_in/in_ur_air-test-*.parquet
- config_name: ur_pk
  data_files:
  - split: train
    path: data/ur_pk/train-*.parquet
  - split: test
    path: data/ur_pk/test-*.parquet
- config_name: uz_uz
  data_files:
  - split: train
    path: data/uz_uz/*train-*.parquet
  - split: test
    path: data/uz_uz/*test-*.parquet
- config_name: ve_za
  data_files:
  - split: train
    path: data/ve_za/*train-*.parquet
- config_name: vn_vi
  data_files:
  - split: train
    path: data/vn_vi/*train-*.parquet
  - split: test
    path: data/vn_vi/*test-*.parquet
- config_name: xh_za
  data_files:
  - split: train
    path: data/xh_za/*train-*.parquet
  - split: test
    path: data/xh_za/*test-*.parquet
- config_name: yue_hk
  data_files:
  - split: train
    path: data/yue_hk/*train-*.parquet
  - split: test
    path: data/yue_hk/*test-*.parquet
- config_name: zh_tw
  data_files:
  - split: train
    path: data/zh_tw/*train-*.parquet
  - split: test
    path: data/zh_tw/*test-*.parquet
- config_name: zu_za
  data_files:
  - split: train
    path: data/zu_za/*train-*.parquet
  - split: test
    path: data/zu_za/*test-*.parquet
---

# WorldSpeech

A multilingual ASR dataset containing over 65k hours of human transcribed speech across 127 language-region variants, drawn from national parliaments, public broadcasters, public-domain audiobooks, and international institutions. Rows consist of 24 kHz speech utterances paired with a human-provided transcript, an aligned ASR transcript, character error rate (CER) between the two, a WADA-SNR estimate, and four DNSMOS-P.835 quality scores.

## Dataset Overview


| Metric | Value |
| :--- | :--- |
| Total hours | 65,072 |
| Distinct languages | 88 (76 above 10 hours) |
| Language variations | 127 |
| Languages ≥ 1,000 h | 24 |
| Languages ≥ 500 h | 28 |
| Languages ≥ 200 h | 37 |
| Languages ≥ 50 h | 53 |
| Avg DNSMOS-P.835 OVR | 2.83 |
| Sample rate | 24 kHz |


## How to use

```python
from datasets import load_dataset

ds = load_dataset("disco-eth/WorldSpeech", "nl_nl", split="train")

row = ds[0]
wav    = row["audio"]["array"]         
sr     = row["audio"]["sampling_rate"]
text   = row["human_transcript"]
snr    = row["snr"]
dnsmos = row["dnsmos_ovr"]
```

### Streaming

```python
from datasets import load_dataset

ds = load_dataset("disco-eth/WorldSpeech", "nl_nl", split="train", streaming=True)

for row in ds:
    wav = row["audio"]["array"]
    break
```


## Schema

| Field | Description |
|---|---|
| `audio` | OGG Opus decoded to `{"array": np.float32[N], "sampling_rate": 24000}` |
| `human_transcript` | Human-provided transcript |
| `asr_transcript` | ASR output used for alignment and CER computation |
| `cer` | Character error rate between `asr_transcript` and `human_transcript` |
| `snr` | WADA-SNR estimate, dB |
| `dnsmos_sig` | DNSMOS-P.835 signal quality |
| `dnsmos_bak` | DNSMOS-P.835 background noise |
| `dnsmos_ovr` | DNSMOS-P.835 overall MOS |
| `dnsmos_p808` | DNSMOS-P.808 MOS |
| `duration` | Segment duration in seconds |
| `source` | Source identifier (e.g. `parliament_nl`, `librivox`, `voa_hausa`) |
| `source_url` | URL to the original recording |
| `source_start_s` | Start offset within the source recording (seconds) |
| `source_end_s` | End offset within the source recording (seconds) |
| `session_date` | ISO-8601 date of the original recording |
| `segment_id` | Unique identifier for this segment |
| `language` | BCP-47 language tag |
| `country` | ISO 3166-1 alpha-2 country code (`un` / `va` for international) |


## Language Coverage

| Config | Country | Language | Hours | DNSMOS OVR |
|---|---|---|---|---|
| `af_za` | South Africa | Afrikaans | 20.2 | 2.79 |
| `am_et` | Ethiopia | Amharic | 39.6 | 3.11 |
| `ar_bh` | Bahrain | Arabic | 272.5 | 2.72 |
| `ar_dz` | Algeria | Arabic | 92.9 | 2.66 |
| `ar_eg` | Egypt | Arabic | 22.0 | 2.86 |
| `ar_iq` | Iraq | Arabic | 291.9 | 2.94 |
| `ar_kw` | Kuwait | Arabic | 175.5 | 2.82 |
| `ar_ma` | Morocco | Arabic | 78.3 | 2.68 |
| `ar_sa` | Saudi Arabia | Arabic | 6.1 | 2.01 |
| `ar_tn` | Tunisia | Arabic | 50.9 | 2.74 |
| `ar_un` | United Nations | Arabic | 11.1 | 3.03 |
| `as_in` | India | Assamese | 54.5 | 3.06 |
| `az_az` | Azerbaijan | Azerbaijani | 305.4 | 2.76 |
| `be_by` | Belarus | Belarusian | 24.2 | 3.10 |
| `bn_bd` | Bangladesh | Bengali | 46.1 | 3.03 |
| `bn_in` | India | Bengali | 26.7 | 2.83 |
| `ca_es` | Spain | Catalan | 1,171.0 | 2.99 |
| `ckb_iq` | Iraq | Sorani Kurdish | 35.3 | 2.93 |
| `cn_ug` | China | Uyghur | 200.0 | 2.86 |
| `cnr_me` | Montenegro | Montenegrin | 47.9 | 2.98 |
| `crs_sc` | Seychelles | Kreol Seselwa | 1,602.3 | 3.15 |
| `cs_cz` | Czech Republic | Czech | 3,717.4 | 2.86 |
| `de_at` | Austria | German | 1,077.5 | 2.93 |
| `de_li` | Liechtenstein | German | 829.7 | 2.79 |
| `dgo_in` | India | Dogri | 34.5 | 3.17 |
| `dv_mv` | Maldives | Dhivehi | 20.0 | 2.92 |
| `el_cy` | Cyprus | Greek | 394.4 | 2.90 |
| `el_gr` | Greece | Greek | 35.9 | 3.37 |
| `en_au` | Australia | English | 568.4 | 3.02 |
| `en_jm` | Jamaica | English | 9.6 | 2.52 |
| `en_ke` | Kenya | English | 170.0 | 2.97 |
| `en_nz` | New Zealand | English | 435.7 | 2.68 |
| `en_pk` | Pakistan | English | 8.5 | 2.28 |
| `en_sl` | Sierra Leone | English | 102.4 | 2.70 |
| `en_us` | USA | English | 3,725.9 | 2.85 |
| `en_zm` | Zambia | English | 291.6 | 2.70 |
| `eo` | (international) | Esperanto | 15.0 | 3.27 |
| `es_ar` | Argentina | Spanish | 251.7 | 2.78 |
| `es_cl` | Chile | Spanish | 1,740.5 | 2.94 |
| `es_co` | Colombia | Spanish | 156.8 | 2.75 |
| `es_es` | Spain | Spanish | 2,097.4 | 2.52 |
| `es_mx` | Mexico | Spanish | 901.6 | 2.63 |
| `es_pe` | Peru | Spanish | 387.4 | 2.63 |
| `es_pr` | Puerto Rico | Spanish | 228.6 | 2.73 |
| `es_py` | Paraguay | Spanish | 133.2 | 3.14 |
| `es_uy` | Uruguay | Spanish | 894.4 | 2.94 |
| `fa_ir` | Iran | Persian | 27.6 | 2.94 |
| `ca_fr` | Canada | French | 5,989.3 | 2.88 |
| `fr_cd` | DR Congo | French | 28.0 | 3.00 |
| `fr_ci` | Côte d'Ivoire | French | 11.9 | 2.97 |
| `ga_ie` | Ireland | Irish | 60.6 | 3.00 |
| `grc_gr` | Greece | Ancient Greek | 1.3 | 3.25 |
| `gu_in` | India | Gujarati | 27.2 | 3.09 |
| `ha_ng` | Nigeria | Hausa | 54.9 | 2.88 |
| `ha_td` | Chad | Hausa | 71.5 | 2.87 |
| `he_il` | Israel | Hebrew | 41.8 | 3.21 |
| `hi_in` | India | Hindi | 1,706.7 | 2.68 |
| `hu_hu` | Hungary | Hungarian | 1,350.1 | 2.96 |
| `hy_am` | Armenia | Armenian | 1,138.9 | 2.59 |
| `id_id` | Indonesia | Indonesian | 340.0 | 2.95 |
| `ig_ng` | Nigeria | Igbo | 40.7 | 3.31 |
| `iu_ca` | Canada | Inuktitut | 33.8 | 2.81 |
| `ja_jp` | Japan | Japanese | 1,387.2 | 2.86 |
| `ka_ge` | Georgia | Georgian | 206.4 | 2.37 |
| `kh_km` | Cambodia | Khmer | 1,323.0 | 2.85 |
| `kk_kz` | Kazakhstan | Kazakh | 179.0 | 2.84 |
| `kn_in` | India | Kannada | 30.2 | 3.19 |
| `ko_kr` | South Korea | Korean | 1,454.1 | 3.07 |
| `kok_in` | India | Konkani | 0.7 | 3.19 |
| `la_lo` | Laos | Lao | 827.0 | 2.82 |
| `la_va` | Vatican | Latin | 34.8 | 3.37 |
| `lb_lu` | Luxembourg | Luxembourgish | 1,805.3 | 2.87 |
| `mai_in` | India | Maithili | 9.6 | 3.19 |
| `mfe_mu` | Mauritius | Mauritian Creole | 44.3 | 3.45 |
| `mi_nz` | New Zealand | Māori | 1.6 | 2.85 |
| `ml_in` | India | Malayalam | 56.7 | 3.10 |
| `mm_my` | Myanmar | Burmese | 865.0 | 2.88 |
| `mn_mn` | Mongolia | Mongolian | 181.0 | 2.80 |
| `mr_in` | India | Marathi | 114.3 | 3.17 |
| `ms_my` | Malaysia | Malay | 432.0 | 2.91 |
| `ne_in` | India | Nepali | 5.7 | 2.94 |
| `ne_np` | Nepal | Nepali | 58.0 | 2.79 |
| `nl_be` | Belgium | Dutch (Flemish) | 960.5 | 2.59 |
| `nl_nl` | Netherlands | Dutch | 4,497.6 | 3.00 |
| `nr_za` | South Africa | Southern Ndebele | 0.2 | 2.60 |
| `nso_za` | South Africa | Northern Sotho | 0.7 | 2.70 |
| `om_et` | Ethiopia | Oromo | 16.3 | 3.06 |
| `or_in` | India | Odia | 57.8 | 3.05 |
| `pa_in` | India | Punjabi | 4.0 | 2.61 |
| `pl_pl` | Poland | Polish | 2,731.9 | 2.70 |
| `pt_br` | Brazil | Portuguese | 1,763.5 | 2.68 |
| `rm_ch` | Switzerland | Romansh | 163.1 | 3.14 |
| `ro_md` | Moldova | Romanian | 1,059.5 | 2.66 |
| `ro_ro` | Romania | Romanian | 686.3 | 2.75 |
| `ru_by` | Belarus | Russian | 2.9 | 2.79 |
| `ru_ru` | Russia | Russian | 1,534.2 | 3.03 |
| `rw_rw` | Rwanda | Kinyarwanda | 17.6 | 2.63 |
| `rw_voa` | Rwanda | Kinyarwanda (VOA) | 14.5 | 2.77 |
| `si_lk` | Sri Lanka | Sinhala | 154.0 | 2.40 |
| `sm_ws` | Samoa | Samoan | 55.9 | 2.79 |
| `sn_zw` | Zimbabwe | Shona | 18.2 | 2.88 |
| `sq_al` | Albania | Albanian | 257.4 | 2.69 |
| `sq_xk` | Kosovo | Albanian | 176.6 | 2.69 |
| `ss_za` | South Africa | Swati | 0.1 | 2.84 |
| `st_za` | South Africa | Sesotho | 0.4 | 2.67 |
| `sv_ax` | Åland Islands | Swedish | 66.0 | 2.73 |
| `sw_ke` | Kenya | Swahili | 257.4 | 2.93 |
| `sw_tz` | Tanzania | Swahili | 748.8 | 2.33 |
| `ta_in` | India | Tamil | 36.1 | 3.06 |
| `ta_lk` | Sri Lanka | Tamil | 204.0 | 2.80 |
| `te_in` | India | Telugu | 77.0 | 3.13 |
| `th_th` | Thailand | Thai | 1,175.6 | 3.23 |
| `ti_et` | Ethiopia | Tigrinya | 14.0 | 3.10 |
| `tl_ph` | Philippines | Tagalog | 219.0 | 2.88 |
| `tn_bw` | Botswana | Tswana | 49.7 | 2.88 |
| `tn_za` | South Africa | Tswana | 0.9 | 2.69 |
| `tr_tr` | Turkey | Turkish | 1,007.6 | 2.22 |
| `ts_za` | South Africa | Tsonga | 0.2 | 2.75 |
| `ur_in` | India | Urdu | 12.6 | 3.01 |
| `ur_pk` | Pakistan | Urdu | 73.1 | 2.44 |
| `uz_uz` | Uzbekistan | Uzbek | 33.7 | 2.84 |
| `ve_za` | South Africa | Venda | 0.1 | 2.72 |
| `vn_vi` | Vietnam | Vietnamese | 726.0 | 2.90 |
| `xh_za` | South Africa | Xhosa | 10.1 | 2.74 |
| `yue_hk` | Hong Kong | Cantonese | 1,943.5 | 3.02 |
| `zh_tw` | Taiwan | Mandarin | 1,482.1 | 2.47 |
| `zu_za` | South Africa | Zulu | 19.0 | 2.71 |
| **Total** | — | — | **65,072.4** | **2.83** |

⚠️ Five configs (`kh_km` Khmer, `la_lo` Lao, `mm_my` Burmese, `vn_vi` Vietnamese, `cn_ug` Uyghur, sourced from Radio Free Asia include only metadata, transcripts, and source URLs. Audio must be downloaded separately from `source_url`.


## Citation

If you use WorldSpeech in your research, please cite:

```bibtex
@misc{asonitis2026worldspeechmultilingualspeechcorpus,
      title={WorldSpeech: A Multilingual Speech Corpus from Around the World}, 
      author={Antonis Asonitis and Luca A. Lanzendörfer and Frédéric Berdoz and Roger Wattenhofer},
      year={2026},
      eprint={2605.09167},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.09167}, 
}
```


## Dataset License

WorldSpeech is released under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Individual source licenses apply per config and are listed in the [Licenses](#licenses) section. Where a source license is more restrictive than CC BY-NC 4.0, the more restrictive terms govern that config.

## Licenses

| Config | Country / Language | License | Notes |
|---|---|---|---|
| `af_za` | South Africa / Afrikaans | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |
| `am_et` | Ethiopia / Amharic | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `ar_bh` | Bahrain / Arabic | [Parliamentary Proceedings](https://www.nuwab.bh/) |  |
| `ar_dz` | Algeria / Arabic | [Parliamentary Proceedings](https://www.apn.dz/) |  |
| `ar_eg` | Egypt / Arabic | [Parliamentary Proceedings](https://www.parliament.gov.eg/) |  |
| `ar_iq` | Iraq / Arabic | [Parliamentary Proceedings](https://parliament.iq/) |  |
| `ar_kw` | Kuwait / Arabic | [Parliamentary Proceedings](https://www.kna.kw/) |  |
| `ar_ma` | Morocco / Arabic | [Parliamentary Proceedings](https://www.parlement.ma/) |  |
| `ar_sa` | Saudi Arabia / Arabic | [Government Archive (Public Record)](https://www.gph.gov.sa/) |  |
| `ar_tn` | Tunisia / Arabic | [Parliamentary Proceedings](https://www.parliament.tn/) |  |
| `ar_un` | United Nations / Arabic | [UN Official Records](https://www.un.org/en/about-us/copyright) | UN official records; non-commercial/research use per UN terms. Contact permissions@un.org for commercial use. |
| `as_in` | India / Assamese | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `az_az` | Azerbaijan / Azerbaijani | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `be_by` | Belarus / Belarusian | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |  |
| `bn_bd` | Bangladesh / Bengali | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `bn_in` | India / Bengali | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `ckb_iq` | Iraq / Sorani Kurdish | [Parliamentary Proceedings](https://parliament.iq/) |  |
| `cn_ug` | China / Uyghur | [RFA Terms of Use (non-commercial)](https://www.rfa.org/english/about/terms-of-use/) | Metadata only — audio not embedded. Download audio from `source_url`. Non-commercial research use; see RFA terms. |
| `cnr_me` | Montenegro / Montenegrin | [Parliamentary Proceedings](https://www.skupstina.me/) |  |
| `crs_sc` | Seychelles / Kreol Seselwa | [Parliamentary Proceedings](https://www.nationalassembly.sc/) |  |
| `cs_cz` | Czech Republic / Czech | [Parliamentary Proceedings](https://www.psp.cz/) |  |
| `cz_cs` | Czech Republic / Czech | [Parliamentary Proceedings](https://www.senat.cz/) | Czech Senate (Senát Parlamentu ČR). |
| `de_at` | Austria / German | [Parliamentary Proceedings](https://www.parlament.gv.at/rechtliches) |  |
| `de_li` | Liechtenstein / German | [Parliamentary Proceedings](https://www.landtag.li/) |  |
| `dgo_in` | India / Dogri | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `dv_mv` | Maldives / Dhivehi | [Parliamentary Proceedings](https://majlis.gov.mv/) |  |
| `el_cy` | Cyprus / Greek | [Parliamentary Proceedings](https://www.parliament.cy/) |  |
| `el_gr` | Greece / Greek | [Parliamentary Proceedings](https://www.hellenicparliament.gr/) |  |
| `en_au` | Australia / English | [Parliamentary Proceedings](https://www.aph.gov.au/Help/Disclaimer_Privacy_Copyright) |  |
| `en_jm` | Jamaica / English | [Parliamentary Proceedings](https://www.japarliament.gov.jm/) |  |
| `en_ke` | Kenya / English | [Parliamentary Proceedings](https://www.parliament.go.ke/) |  |
| `en_nz` | New Zealand / English | [Parliamentary Proceedings](https://www.parliament.nz/en/footer/copyright/) |  |
| `en_sl` | Sierra Leone / English | [Parliamentary Proceedings](https://www.parliament.gov.sl/) |  |
| `en_us` | USA / English | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal proceedings (Congress.gov / C-SPAN public domain content). |
| `en_zm` | Zambia / English | [Parliamentary Proceedings](https://www.parliament.gov.zm/) |  |
| `eo` | (international) / Esperanto | [CC0 1.0 (Public Domain)](https://librivox.org/pages/public-domain/) |  |
| `es_ar` | Argentina / Spanish | [Parliamentary Proceedings](https://www.hcdn.gob.ar/) |  |
| `es_cl` | Chile / Spanish | [Parliamentary Proceedings](https://www.camara.cl/) |  |
| `es_co` | Colombia / Spanish | [Parliamentary Proceedings](https://www.camara.gov.co/) |  |
| `es_es` | Spain / Spanish | [Parliamentary Proceedings](https://www.congreso.es/) |  |
| `es_mx` | Mexico / Spanish | [Parliamentary Proceedings](https://www.congreso.gob.mx/) |  |
| `es_pe` | Peru / Spanish | [Parliamentary Proceedings](https://www.congreso.gob.pe/) |  |
| `es_pr` | Puerto Rico / Spanish | [Parliamentary Proceedings](https://www.camaraderepresentantes.org/) |  |
| `es_py` | Paraguay / Spanish | [Parliamentary Proceedings](https://www.congreso.gov.py/) |  |
| `es_uy` | Uruguay / Spanish | [Parliamentary Proceedings](https://parlamento.gub.uy/) |  |
| `fa_ir` | Iran / Persian | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `ca_fr` | Canada / French | [Parliamentary Proceedings](https://www.assnat.qc.ca/) |  |
| `fr_cd` | DR Congo / French | [ICC Court Records](https://www.icc-cpi.int/disclaimer) | Public judicial proceedings of an international court; non-commercial/educational use per ICC terms. |
| `fr_ci` | Cote d'Ivoire / French | [ICC Court Records](https://www.icc-cpi.int/disclaimer) | Public judicial proceedings of an international court; non-commercial/educational use per ICC terms. |
| `ga_ie` | Ireland / Irish | [CC BY 4.0 (Oireachtas PSI Licence)](https://www.oireachtas.ie/en/open-data/license/) |  |
| `grc_gr` | Greece / Ancient Greek | [CC0 1.0 (Public Domain)](https://librivox.org/pages/public-domain/) |  |
| `gu_in` | India / Gujarati | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `ha_ng` | Nigeria / Hausa | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `ha_td` | Chad | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `he_il` | Israel / Hebrew | [CC0 1.0 (Public Domain)](https://librivox.org/pages/public-domain/) | LibriVox recordings (CC0) + Ben-Yehuda Project texts (public domain per Israeli copyright law). |
| `hi_in` | India / Hindi | [Parliamentary Proceedings](https://sansad.in/) |  |
| `hu_hu` | Hungary / Hungarian | [Parliamentary Proceedings](https://www.parlament.hu/) |  |
| `hy_am` | Armenia / Armenian | [Parliamentary Proceedings](https://www.parliament.am/) |  |
| `id_id` | Indonesia / Indonesian | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `ig_ng` | Nigeria / Igbo | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `iu_ca` | Canada / Inuktitut | [Parliamentary Proceedings](https://www.assembly.nu.ca/) |  |
| `ja_jp` | Japan / Japanese | [CC0 1.0 (Public Domain)](https://librivox.org/pages/public-domain/) | LibriVox recordings (CC0) + Aozora Bunko texts (public domain, 50yr Japanese law). |
| `ka_ge` | Georgia / Georgian | [Parliamentary Proceedings](https://parliament.ge/) |  |
| `kh_km` | Cambodia / Khmer | [RFA Terms of Use (non-commercial)](https://www.rfa.org/english/about/terms-of-use/) | Metadata only — audio not embedded. Download audio from `source_url`. Non-commercial research use; see RFA terms. |
| `kk_kz` | Kazakhstan / Kazakh | [Parliamentary Proceedings](https://www.parlam.kz/) |  |
| `kn_in` | India / Kannada | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `ko_kr` | South Korea / Korean | [Parliamentary Proceedings](https://www.assembly.go.kr/) |  |
| `kok_in` | India / Konkani | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `la_lo` | Laos / Lao | [RFA Terms of Use (non-commercial)](https://www.rfa.org/english/about/terms-of-use/) | Metadata only — audio not embedded. Download audio from `source_url`. Non-commercial research use; see RFA terms. |
| `la_va` | Vatican / Latin | [Vatican Radio Archive](https://www.vaticannews.va/en/others/terms-and-conditions.html) | Vatican Radio historical archive; contact Vatican Media for commercial use. |
| `lb_lu` | Luxembourg / Luxembourgish | [Parliamentary Proceedings](https://www.chd.lu/) |  |
| `mai_in` | India / Maithili | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `mfe_mu` | Mauritius / Mauritian Creole | [Parliamentary Proceedings](https://govmu.org/) |  |
| `mi_nz` | New Zealand / Maori | [Parliamentary Proceedings](https://www.parliament.nz/en/footer/copyright/) |  |
| `ml_in` | India / Malayalam | [Parliamentary Proceedings](https://niyamasabha.org/) |  |
| `mm_my` | Myanmar / Burmese | [RFA Terms of Use (non-commercial)](https://www.rfa.org/english/about/terms-of-use/) | Metadata only — audio not embedded. Download audio from `source_url`. Non-commercial research use; see RFA terms. |
| `mn_mn` | Mongolia / Mongolian | [Parliamentary Proceedings / CC0](https://www.parliament.mn/) | Parliament sessions (public record) + Latter-day Saints addresses (CC0 per lds.org). |
| `mr_in` | India / Marathi | [Parliamentary Proceedings](https://www.vidhan.maharashtra.gov.in/) |  |
| `ms_my` | Malaysia / Malay | [Parliamentary Proceedings](https://www.parlimen.gov.my/) |  |
| `ne_in` | India / Nepali | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `ne_np` | Nepal / Nepali | [Parliamentary Proceedings](https://www.parliament.gov.np/) |  |
| `nl_be` | Belgium / Dutch | [Parliamentary Proceedings](https://www.vlaamsparlement.be/) |  |
| `nl_nl` | Netherlands / Dutch | [Parliamentary Proceedings](https://www.tweedekamer.nl/) |  |
| `nr_za` | South Africa / Southern Ndebele | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |
| `nso_za` | South Africa / Northern Sotho | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |
| `om_et` | Ethiopia / Oromo | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `or_in` | India / Odia | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `pa_in` | India / Punjabi | [Parliamentary Proceedings](https://vidhanpb.gov.in/) |  |
| `pl_pl` | Poland / Polish | [Parliamentary Proceedings](https://www.sejm.gov.pl/) |  |
| `pt_br` | Brazil / Portuguese | [Parliamentary Proceedings](https://www.senado.leg.br/) |  |
| `rm_ch` | Switzerland / Romansh | [SRG SSR Terms of Use](https://www.srgssr.ch/en/who-we-are/public-service/) | Corpus compiled from publicly broadcast RTR programming; contact SRG SSR for commercial use. |
| `ro_md` | Moldova / Romanian | [Parliamentary Proceedings](https://www.parlament.md/) |  |
| `ro_ro` | Romania / Romanian | [Parliamentary Proceedings](https://www.senat.ro/) |  |
| `ru_by` | Belarus / Russian | [Government Publication (Public Record)](https://president.gov.by/) |  |
| `ru_ru` | Russia / Russian | [Parliamentary Proceedings](https://duma.gov.ru/) |  |
| `rw_rw` | Rwanda / Kinyarwanda | [Parliamentary Proceedings](https://www.parliament.gov.rw/) |  |
| `si_lk` | Sri Lanka / Sinhala | [Parliamentary Proceedings](https://www.parliament.lk/) |  |
| `sm_ws` | Samoa / Samoan | [Parliamentary Proceedings](https://parliament.ws/) |  |
| `sn_zw` | Zimbabwe / Shona | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `sq_al` | Albania / Albanian | [Parliamentary Proceedings](https://www.parlament.al/) |  |
| `sq_xk` | Kosovo / Albanian | [Parliamentary Proceedings](https://www.assembly-kosova.org/) |  |
| `ss_za` | South Africa / Swati | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |
| `st_za` | South Africa / Sesotho | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |
| `sv_ax` | Aland Islands / Swedish | [Parliamentary Proceedings](https://www.lagting.ax/) |  |
| `sw_ke` | Kenya / Swahili | [Parliamentary Proceedings](https://www.parliament.go.ke/) |  |
| `sw_tz` | Tanzania / Swahili | [Parliamentary Proceedings](https://www.bunge.go.tz/) |  |
| `ta_in` | India / Tamil | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `ta_lk` | Sri Lanka / Tamil | [Parliamentary Proceedings](https://www.parliament.lk/) |  |
| `te_in` | India / Telugu | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `th_th` | Thailand / Thai | [Parliamentary Proceedings](https://www.parliament.go.th/) |  |
| `ti_et` | Ethiopia / Tigrinya | [Public Domain (17 USC §105)](https://www.law.cornell.edu/uscode/text/17/105) | US federal agency content (VOA). |
| `tl_ph` | Philippines / Tagalog | [Parliamentary Proceedings](https://www.congress.gov.ph/) |  |
| `tn_bw` | Botswana / Tswana | [Parliamentary Proceedings](https://www.parliament.gov.bw/) |  |
| `tn_za` | South Africa / Tswana | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |
| `tr_tr` | Turkey / Turkish | [Parliamentary Proceedings](https://www.tbmm.gov.tr/) |  |
| `ts_za` | South Africa / Tsonga | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |
| `ur_in` | India / Urdu | [All India Radio Archive (Prasar Bharati)](https://newsonair.gov.in/) | Prasar Bharati public broadcaster archive. |
| `uz_uz` | Uzbekistan / Uzbek | [RFE/RL Terms of Use (non-commercial)](https://about.rferl.org/use-our-content/) | US government-funded broadcaster; non-commercial research use. Original Ozodlik (RFE/RL Uzbek) content. |
| `ve_za` | South Africa / Venda | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |
| `vn_vi` | Vietnam / Vietnamese | [RFA Terms of Use (non-commercial)](https://www.rfa.org/english/about/terms-of-use/) | Metadata only — audio not embedded. Download audio from `source_url`. Non-commercial research use; see RFA terms. |
| `xh_za` | South Africa / Xhosa | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |
| `yue_hk` | Hong Kong / Cantonese | [Parliamentary Proceedings](https://www.legco.gov.hk/en/general/disclaimer.html) |  |
| `zh_tw` | Taiwan / Chinese (Mandarin) | [Parliamentary Proceedings](https://www.ly.gov.tw/) |  |
| `zu_za` | South Africa / Zulu | [Parliamentary Proceedings](https://www.parliament.gov.za/legal) |  |