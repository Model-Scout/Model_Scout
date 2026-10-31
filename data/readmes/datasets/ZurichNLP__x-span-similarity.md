---
license: cc-by-sa-4.0
language:
- ar
- bg
- bho
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
- fil
- fr
- grc
- gu
- he
- hi
- hr
- hu
- id
- is
- it
- ja
- kn
- ko
- lt
- lv
- mas
- ml
- mr
- nb
- nl
- pa
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
- zu
pretty_name: X-Span-Similarity (Cross-Lingual SSD)
tags:
- cross-lingual
- span-similarity
- semantic-similarity
- machine-translation
- natural-language-inference
task_categories:
- text-classification
- token-classification
configs:
- config_name: ar_eg
  data_files:
  - split: train
    path: ssd_train_ar_eg.jsonl
  - split: test
    path: ssd_test_ar_eg.jsonl
- config_name: ar_sa
  data_files:
  - split: train
    path: ssd_train_ar_sa.jsonl
  - split: test
    path: ssd_test_ar_sa.jsonl
- config_name: bg_bg
  data_files:
  - split: train
    path: ssd_train_bg_bg.jsonl
  - split: test
    path: ssd_test_bg_bg.jsonl
- config_name: bho_in
  data_files:
  - split: train
    path: ssd_train_bho_in.jsonl
  - split: test
    path: ssd_test_bho_in.jsonl
- config_name: bn_in
  data_files:
  - split: train
    path: ssd_train_bn_in.jsonl
  - split: test
    path: ssd_test_bn_in.jsonl
- config_name: ca_es
  data_files:
  - split: train
    path: ssd_train_ca_es.jsonl
  - split: test
    path: ssd_test_ca_es.jsonl
- config_name: cs_cz
  data_files:
  - split: train
    path: ssd_train_cs_cz.jsonl
  - split: test
    path: ssd_test_cs_cz.jsonl
- config_name: da_dk
  data_files:
  - split: train
    path: ssd_train_da_dk.jsonl
  - split: test
    path: ssd_test_da_dk.jsonl
- config_name: de_de
  data_files:
  - split: train
    path: ssd_train_de_de.jsonl
  - split: test
    path: ssd_test_de_de.jsonl
- config_name: el_gr
  data_files:
  - split: train
    path: ssd_train_el_gr.jsonl
  - split: test
    path: ssd_test_el_gr.jsonl
- config_name: es_mx
  data_files:
  - split: train
    path: ssd_train_es_mx.jsonl
  - split: test
    path: ssd_test_es_mx.jsonl
- config_name: et_ee
  data_files:
  - split: train
    path: ssd_train_et_ee.jsonl
  - split: test
    path: ssd_test_et_ee.jsonl
- config_name: fa_ir
  data_files:
  - split: train
    path: ssd_train_fa_ir.jsonl
  - split: test
    path: ssd_test_fa_ir.jsonl
- config_name: fi_fi
  data_files:
  - split: train
    path: ssd_train_fi_fi.jsonl
  - split: test
    path: ssd_test_fi_fi.jsonl
- config_name: fil_ph
  data_files:
  - split: train
    path: ssd_train_fil_ph.jsonl
  - split: test
    path: ssd_test_fil_ph.jsonl
- config_name: fr_fr
  data_files:
  - split: train
    path: ssd_train_fr_fr.jsonl
  - split: test
    path: ssd_test_fr_fr.jsonl
- config_name: gu_in
  data_files:
  - split: train
    path: ssd_train_gu_in.jsonl
  - split: test
    path: ssd_test_gu_in.jsonl
- config_name: he_il
  data_files:
  - split: train
    path: ssd_train_he_il.jsonl
  - split: test
    path: ssd_test_he_il.jsonl
- config_name: hi_in
  data_files:
  - split: train
    path: ssd_train_hi_in.jsonl
  - split: test
    path: ssd_test_hi_in.jsonl
- config_name: hr_hr
  data_files:
  - split: train
    path: ssd_train_hr_hr.jsonl
  - split: test
    path: ssd_test_hr_hr.jsonl
- config_name: hu_hu
  data_files:
  - split: train
    path: ssd_train_hu_hu.jsonl
  - split: test
    path: ssd_test_hu_hu.jsonl
- config_name: id_id
  data_files:
  - split: train
    path: ssd_train_id_id.jsonl
  - split: test
    path: ssd_test_id_id.jsonl
- config_name: is_is
  data_files:
  - split: train
    path: ssd_train_is_is.jsonl
  - split: test
    path: ssd_test_is_is.jsonl
- config_name: it_it
  data_files:
  - split: train
    path: ssd_train_it_it.jsonl
  - split: test
    path: ssd_test_it_it.jsonl
- config_name: ja_jp
  data_files:
  - split: train
    path: ssd_train_ja_jp.jsonl
  - split: test
    path: ssd_test_ja_jp.jsonl
- config_name: kn_in
  data_files:
  - split: train
    path: ssd_train_kn_in.jsonl
  - split: test
    path: ssd_test_kn_in.jsonl
- config_name: ko_kr
  data_files:
  - split: train
    path: ssd_train_ko_kr.jsonl
  - split: test
    path: ssd_test_ko_kr.jsonl
- config_name: lt_lt
  data_files:
  - split: train
    path: ssd_train_lt_lt.jsonl
  - split: test
    path: ssd_test_lt_lt.jsonl
- config_name: lv_lv
  data_files:
  - split: train
    path: ssd_train_lv_lv.jsonl
  - split: test
    path: ssd_test_lv_lv.jsonl
- config_name: mas_ke
  data_files:
  - split: train
    path: ssd_train_mas_ke.jsonl
  - split: test
    path: ssd_test_mas_ke.jsonl
- config_name: ml_in
  data_files:
  - split: train
    path: ssd_train_ml_in.jsonl
  - split: test
    path: ssd_test_ml_in.jsonl
- config_name: mr_in
  data_files:
  - split: train
    path: ssd_train_mr_in.jsonl
  - split: test
    path: ssd_test_mr_in.jsonl
- config_name: nb_no
  data_files:
  - split: train
    path: ssd_train_nb_no.jsonl
  - split: test
    path: ssd_test_nb_no.jsonl
- config_name: nl_nl
  data_files:
  - split: train
    path: ssd_train_nl_nl.jsonl
  - split: test
    path: ssd_test_nl_nl.jsonl
- config_name: pa_in
  data_files:
  - split: train
    path: ssd_train_pa_in.jsonl
  - split: test
    path: ssd_test_pa_in.jsonl
- config_name: pl_pl
  data_files:
  - split: train
    path: ssd_train_pl_pl.jsonl
  - split: test
    path: ssd_test_pl_pl.jsonl
- config_name: pt_pt
  data_files:
  - split: train
    path: ssd_train_pt_pt.jsonl
  - split: test
    path: ssd_test_pt_pt.jsonl
- config_name: ro_ro
  data_files:
  - split: train
    path: ssd_train_ro_ro.jsonl
  - split: test
    path: ssd_test_ro_ro.jsonl
- config_name: ru_ru
  data_files:
  - split: train
    path: ssd_train_ru_ru.jsonl
  - split: test
    path: ssd_test_ru_ru.jsonl
- config_name: sk_sk
  data_files:
  - split: train
    path: ssd_train_sk_sk.jsonl
  - split: test
    path: ssd_test_sk_sk.jsonl
- config_name: sl_si
  data_files:
  - split: train
    path: ssd_train_sl_si.jsonl
  - split: test
    path: ssd_test_sl_si.jsonl
- config_name: sr_cyrl_rs
  data_files:
  - split: train
    path: ssd_train_sr_cyrl_rs.jsonl
  - split: test
    path: ssd_test_sr_cyrl_rs.jsonl
- config_name: sr_latn_rs
  data_files:
  - split: train
    path: ssd_train_sr_latn_rs.jsonl
  - split: test
    path: ssd_test_sr_latn_rs.jsonl
- config_name: sv_se
  data_files:
  - split: train
    path: ssd_train_sv_se.jsonl
  - split: test
    path: ssd_test_sv_se.jsonl
- config_name: sw_ke
  data_files:
  - split: train
    path: ssd_train_sw_ke.jsonl
  - split: test
    path: ssd_test_sw_ke.jsonl
- config_name: ta_in
  data_files:
  - split: train
    path: ssd_train_ta_in.jsonl
  - split: test
    path: ssd_test_ta_in.jsonl
- config_name: te_in
  data_files:
  - split: train
    path: ssd_train_te_in.jsonl
  - split: test
    path: ssd_test_te_in.jsonl
- config_name: th_th
  data_files:
  - split: train
    path: ssd_train_th_th.jsonl
  - split: test
    path: ssd_test_th_th.jsonl
- config_name: tr_tr
  data_files:
  - split: train
    path: ssd_train_tr_tr.jsonl
  - split: test
    path: ssd_test_tr_tr.jsonl
- config_name: uk_ua
  data_files:
  - split: train
    path: ssd_train_uk_ua.jsonl
  - split: test
    path: ssd_test_uk_ua.jsonl
- config_name: ur_pk
  data_files:
  - split: train
    path: ssd_train_ur_pk.jsonl
  - split: test
    path: ssd_test_ur_pk.jsonl
- config_name: vi_vn
  data_files:
  - split: train
    path: ssd_train_vi_vn.jsonl
  - split: test
    path: ssd_test_vi_vn.jsonl
- config_name: zh_cn
  data_files:
  - split: train
    path: ssd_train_zh_cn.jsonl
  - split: test
    path: ssd_test_zh_cn.jsonl
- config_name: zu_za
  data_files:
  - split: train
    path: ssd_train_zu_za.jsonl
  - split: test
    path: ssd_test_zu_za.jsonl
dataset_info:
- config_name: ar_eg
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: ar_sa
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: bg_bg
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: bho_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: bn_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: ca_es
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: cs_cz
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: da_dk
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: de_de
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: el_gr
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: es_mx
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: et_ee
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: fa_ir
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: fi_fi
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: fil_ph
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: fr_fr
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: gu_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: he_il
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: hi_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: hr_hr
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: hu_hu
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: id_id
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: is_is
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: it_it
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: ja_jp
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: kn_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: ko_kr
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: lt_lt
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: lv_lv
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: mas_ke
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: ml_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: mr_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: nb_no
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: nl_nl
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: pa_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: pl_pl
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: pt_pt
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: ro_ro
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: ru_ru
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: sk_sk
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: sl_si
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: sr_cyrl_rs
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: sr_latn_rs
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: sv_se
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: sw_ke
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: ta_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: te_in
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: th_th
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: tr_tr
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: uk_ua
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: ur_pk
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: vi_vn
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: zh_cn
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
- config_name: zu_za
  features:
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: span_similarity
    sequence: int32
  - name: sentence_similarity
    dtype: int32
  - name: lang_premise
    dtype: string
  - name: lang_hypothesis
    dtype: string
  - name: locale
    dtype: string
  splits:
  - name: train
    num_examples: 1600
  - name: test
    num_examples: 400
---
# X-Span-Similarity (X-SSD)

Expanding Lozano et al.'s (2026) [Span Similarity Dataset (SSD)](https://huggingface.co/datasets/tum-nlp/span-similarity-dataset) into a cross-lingual setting, for Dissimilar/Difference Span Detection (DSD) across language pairs.

## Dataset summary

Each row is a `premise`/`hypothesis` sentence pair, one side in English and the other machine-translated into another target language, with span-level and sentence-level (dis)similarity labels carried over unchanged from the original English SSD annotation. Spans considered semantically dissimilar between `premise` and `hypothesis` are marked in the untranslated English side with `{{double curly braces}}`; `span_similarity` gives the label (`0` = dissimilar, `1` = similar) for each marked span in order, and `sentence_similarity` is a single binary label for the pair as a whole.

For every target language, both translation sides of the sentence pair are included: one row has the original English `premise` and a translated `hypothesis`, the next has a translated `premise` and the original English `hypothesis` — `lang_premise`/`lang_hypothesis` indicates which is which.


## Dataset structure

### Configs

Each of the 54 target languages is exposed as its own config, matching the original `ssd_{split}_{locale}.jsonl` filenames. Load a single language (paired with English) with:

```python
from datasets import load_dataset

ds = load_dataset("ZurichNLP/x-span-similarity", "de_de")
ds["train"], ds["test"]
```

### Fields

| Field | Type | Description |
|---|---|---|
| `premise` | string | First sentence of the pair. |
| `hypothesis` | string | Second sentence of the pair. |
| `span_similarity` | list[int] | Per-span label (`0`/`1`) for each `{{...}}`-marked span, in order of appearance, on the untranslated side. |
| `sentence_similarity` | int | `0`/`1` label for whether the pair is semantically equivalent overall. |
| `lang_premise` | string | Locale of `premise` (e.g. `en_EN`, `de_DE`). |
| `lang_hypothesis` | string | Locale of `hypothesis`. |
| `locale` | string | The non-English locale for this config/row (redundant with the config name, provided for convenience when configs are concatenated). |

### Splits

`train` and `test` mirror the splits of the source SSD dataset. Sizes are 2x the source split size (one for each direction).


## Dataset creation

The source data is the English-only SSD (`tum-nlp/span-similarity-dataset`, Lozano et al. 2026). For each target locale, one side of every `premise`/`hypothesis` pair was machine-translated with Gemini (`gemini-3-flash-preview`), while span markers (`{{}}`) were stripped before translation and preserved on the untranslated side, since translation is not guaranteed to preserve exact span boundaries. Original `span_similarity`/`sentence_similarity` labels are carried over unchanged from the English source annotation. 


## Supported languages

| Locale | Language |
|---|---|
| `ar_eg` | Arabic (Egypt) |
| `ar_sa` | Arabic (Saudi Arabia) |
| `bg_bg` | Bulgarian |
| `bho_in` | Bhojpuri |
| `bn_in` | Bengali |
| `ca_es` | Catalan |
| `cs_cz` | Czech |
| `da_dk` | Danish |
| `de_de` | German |
| `el_gr` | Greek |
| `es_mx` | Spanish (Mexico) |
| `et_ee` | Estonian |
| `fa_ir` | Farsi |
| `fi_fi` | Finnish |
| `fil_ph` | Filipino |
| `fr_fr` | French (France) |
| `gu_in` | Gujarati |
| `he_il` | Hebrew |
| `hi_in` | Hindi |
| `hr_hr` | Croatian |
| `hu_hu` | Hungarian |
| `id_id` | Indonesian |
| `is_is` | Icelandic |
| `it_it` | Italian |
| `ja_jp` | Japanese |
| `kn_in` | Kannada |
| `ko_kr` | Korean |
| `lt_lt` | Lithuanian |
| `lv_lv` | Latvian |
| `mas_ke` | Masai |
| `ml_in` | Malayalam |
| `mr_in` | Marathi |
| `nb_no` | Norwegian |
| `nl_nl` | Dutch |
| `pa_in` | Punjabi |
| `pl_pl` | Polish |
| `pt_pt` | Portuguese (Portugal) |
| `ro_ro` | Romanian |
| `ru_ru` | Russian |
| `sk_sk` | Slovak |
| `sl_si` | Slovenian |
| `sr_cyrl_rs` | Serbian (Cyrillic) |
| `sr_latn_rs` | Serbian (Latin) |
| `sv_se` | Swedish |
| `sw_ke` | Swahili (Kenya) |
| `ta_in` | Tamil |
| `te_in` | Telugu |
| `th_th` | Thai |
| `tr_tr` | Turkish |
| `uk_ua` | Ukrainian |
| `ur_pk` | Urdu |
| `vi_vn` | Vietnamese |
| `zh_cn` | Chinese (Mandarin, China) |
| `zu_za` | Zulu |


## License

Released under **CC BY-SA 4.0**, matching the license of the source SSD dataset (Lozano et al. 2026). 


