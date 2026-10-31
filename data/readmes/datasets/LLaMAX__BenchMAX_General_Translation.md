---
license: cc-by-4.0
task_categories:
- translation
language:
- en
- zh
- es
- fr
- de
- ru
- ja
- th
- sw
- te
- bn
- ar
- ko
- vi
- cs
- hu
- sr
multilinguality:
- multilingual
dataset_info:
- config_name: flores_en
  features:
  - name: text
    dtype: string
- config_name: ted_en
  features:
  - name: id
    dtype: int32
  - name: text
    dtype: string
  - name: talk_name
    dtype: string
  - name: lang
    dtype: string
configs:
- config_name: flores_en
  data_files: flores200/flores_200_en.jsonl
- config_name: flores_zh
  data_files: flores200/flores_200_zh.jsonl
- config_name: flores_es
  data_files: flores200/flores_200_es.jsonl
- config_name: flores_fr
  data_files: flores200/flores_200_fr.jsonl
- config_name: flores_de
  data_files: flores200/flores_200_de.jsonl
- config_name: flores_ru
  data_files: flores200/flores_200_ru.jsonl
- config_name: flores_ja
  data_files: flores200/flores_200_ja.jsonl
- config_name: flores_th
  data_files: flores200/flores_200_th.jsonl
- config_name: flores_bn
  data_files: flores200/flores_200_bn.jsonl
- config_name: flores_sw
  data_files: flores200/flores_200_sw.jsonl
- config_name: flores_te
  data_files: flores200/flores_200_te.jsonl
- config_name: flores_ar
  data_files: flores200/flores_200_ar.jsonl
- config_name: flores_ko
  data_files: flores200/flores_200_ko.jsonl
- config_name: flores_vi
  data_files: flores200/flores_200_vi.jsonl
- config_name: flores_cs
  data_files: flores200/flores_200_cs.jsonl
- config_name: flores_hu
  data_files: flores200/flores_200_hu.jsonl
- config_name: flores_sr
  data_files: flores200/flores_200_sr.jsonl
- config_name: ted_en
  data_files: ted/test.en.jsonl
- config_name: ted_zh
  data_files: ted/test.zh.jsonl
- config_name: ted_es
  data_files: ted/test.es.jsonl
- config_name: ted_fr
  data_files: ted/test.fr.jsonl
- config_name: ted_de
  data_files: ted/test.de.jsonl
- config_name: ted_ru
  data_files: ted/test.ru.jsonl
- config_name: ted_ja
  data_files: ted/test.ja.jsonl
- config_name: ted_th
  data_files: ted/test.th.jsonl
- config_name: ted_bn
  data_files: ted/test.bn.jsonl
- config_name: ted_ar
  data_files: ted/test.ar.jsonl
- config_name: ted_ko
  data_files: ted/test.ko.jsonl
- config_name: ted_vi
  data_files: ted/test.vi.jsonl
- config_name: ted_cs
  data_files: ted/test.cs.jsonl
- config_name: ted_hu
  data_files: ted/test.hu.jsonl
- config_name: ted_sr
  data_files: ted/test.sr.jsonl
- config_name: wmt24_en-zh_en
  data_files: wmt24/wmt24.en-zh.en.jsonl
- config_name: wmt24_en-zh_zh
  data_files: wmt24/wmt24.en-zh.zh.jsonl
- config_name: wmt24_en-es_en
  data_files: wmt24/wmt24.en-es.en.jsonl
- config_name: wmt24_en-es_es
  data_files: wmt24/wmt24.en-es.es.jsonl
- config_name: wmt24_en-de_en
  data_files: wmt24/wmt24.en-de.en.jsonl
- config_name: wmt24_en-de_de
  data_files: wmt24/wmt24.en-de.de.jsonl
- config_name: wmt24_en-cs_en
  data_files: wmt24/wmt24.en-cs.en.jsonl
- config_name: wmt24_en-cs_cs
  data_files: wmt24/wmt24.en-cs.cs.jsonl
- config_name: wmt24_en-ja_en
  data_files: wmt24/wmt24.en-ja.en.jsonl
- config_name: wmt24_en-ja_ja
  data_files: wmt24/wmt24.en-ja.ja.jsonl
- config_name: wmt24_en-ru_en
  data_files: wmt24/wmt24.en-ru.en.jsonl
- config_name: wmt24_en-ru_ru
  data_files: wmt24/wmt24.en-ru.ru.jsonl
- config_name: flores_af
  data_files: flores200/flores_200_af.jsonl
- config_name: flores_am
  data_files: flores200/flores_200_am.jsonl
- config_name: flores_as
  data_files: flores200/flores_200_as.jsonl
- config_name: flores_ast
  data_files: flores200/flores_200_ast.jsonl
- config_name: flores_az
  data_files: flores200/flores_200_az.jsonl
- config_name: flores_be
  data_files: flores200/flores_200_be.jsonl
- config_name: flores_bs
  data_files: flores200/flores_200_bs.jsonl
- config_name: flores_bg
  data_files: flores200/flores_200_bg.jsonl
- config_name: flores_ca
  data_files: flores200/flores_200_ca.jsonl
- config_name: flores_ceb
  data_files: flores200/flores_200_ceb.jsonl
- config_name: flores_ku
  data_files: flores200/flores_200_ku.jsonl
- config_name: flores_cy
  data_files: flores200/flores_200_cy.jsonl
- config_name: flores_da
  data_files: flores200/flores_200_da.jsonl
- config_name: flores_el
  data_files: flores200/flores_200_el.jsonl
- config_name: flores_et
  data_files: flores200/flores_200_et.jsonl
- config_name: flores_fa
  data_files: flores200/flores_200_fa.jsonl
- config_name: flores_fi
  data_files: flores200/flores_200_fi.jsonl
- config_name: flores_ff
  data_files: flores200/flores_200_ff.jsonl
- config_name: flores_ga
  data_files: flores200/flores_200_ga.jsonl
- config_name: flores_gl
  data_files: flores200/flores_200_gl.jsonl
- config_name: flores_gu
  data_files: flores200/flores_200_gu.jsonl
- config_name: flores_ha
  data_files: flores200/flores_200_ha.jsonl
- config_name: flores_he
  data_files: flores200/flores_200_he.jsonl
- config_name: flores_hi
  data_files: flores200/flores_200_hi.jsonl
- config_name: flores_hr
  data_files: flores200/flores_200_hr.jsonl
- config_name: flores_hy
  data_files: flores200/flores_200_hy.jsonl
- config_name: flores_ig
  data_files: flores200/flores_200_ig.jsonl
- config_name: flores_id
  data_files: flores200/flores_200_id.jsonl
- config_name: flores_is
  data_files: flores200/flores_200_is.jsonl
- config_name: flores_it
  data_files: flores200/flores_200_it.jsonl
- config_name: flores_jv
  data_files: flores200/flores_200_jv.jsonl
- config_name: flores_kam
  data_files: flores200/flores_200_kam.jsonl
- config_name: flores_kn
  data_files: flores200/flores_200_kn.jsonl
- config_name: flores_ka
  data_files: flores200/flores_200_ka.jsonl
- config_name: flores_kk
  data_files: flores200/flores_200_kk.jsonl
- config_name: flores_kea
  data_files: flores200/flores_200_kea.jsonl
- config_name: flores_km
  data_files: flores200/flores_200_km.jsonl
- config_name: flores_ky
  data_files: flores200/flores_200_ky.jsonl
- config_name: flores_lo
  data_files: flores200/flores_200_lo.jsonl
- config_name: flores_lv
  data_files: flores200/flores_200_lv.jsonl
- config_name: flores_ln
  data_files: flores200/flores_200_ln.jsonl
- config_name: flores_lt
  data_files: flores200/flores_200_lt.jsonl
- config_name: flores_lb
  data_files: flores200/flores_200_lb.jsonl
- config_name: flores_lg
  data_files: flores200/flores_200_lg.jsonl
- config_name: flores_luo
  data_files: flores200/flores_200_luo.jsonl
- config_name: flores_ml
  data_files: flores200/flores_200_ml.jsonl
- config_name: flores_mr
  data_files: flores200/flores_200_mr.jsonl
- config_name: flores_mk
  data_files: flores200/flores_200_mk.jsonl
- config_name: flores_mt
  data_files: flores200/flores_200_mt.jsonl
- config_name: flores_mn
  data_files: flores200/flores_200_mn.jsonl
- config_name: flores_mi
  data_files: flores200/flores_200_mi.jsonl
- config_name: flores_ms
  data_files: flores200/flores_200_ms.jsonl
- config_name: flores_my
  data_files: flores200/flores_200_my.jsonl
- config_name: flores_nl
  data_files: flores200/flores_200_nl.jsonl
- config_name: flores_no
  data_files: flores200/flores_200_no.jsonl
- config_name: flores_ne
  data_files: flores200/flores_200_ne.jsonl
- config_name: flores_ns
  data_files: flores200/flores_200_ns.jsonl
- config_name: flores_ny
  data_files: flores200/flores_200_ny.jsonl
- config_name: flores_oc
  data_files: flores200/flores_200_oc.jsonl
- config_name: flores_om
  data_files: flores200/flores_200_om.jsonl
- config_name: flores_or
  data_files: flores200/flores_200_or.jsonl
- config_name: flores_pa
  data_files: flores200/flores_200_pa.jsonl
- config_name: flores_pl
  data_files: flores200/flores_200_pl.jsonl
- config_name: flores_pt
  data_files: flores200/flores_200_pt.jsonl
- config_name: flores_ps
  data_files: flores200/flores_200_ps.jsonl
- config_name: flores_ro
  data_files: flores200/flores_200_ro.jsonl
- config_name: flores_sk
  data_files: flores200/flores_200_sk.jsonl
- config_name: flores_sl
  data_files: flores200/flores_200_sl.jsonl
- config_name: flores_sn
  data_files: flores200/flores_200_sn.jsonl
- config_name: flores_sd
  data_files: flores200/flores_200_sd.jsonl
- config_name: flores_so
  data_files: flores200/flores_200_so.jsonl
- config_name: flores_sv
  data_files: flores200/flores_200_sv.jsonl
- config_name: flores_ta
  data_files: flores200/flores_200_ta.jsonl
- config_name: flores_tg
  data_files: flores200/flores_200_tg.jsonl
- config_name: flores_tl
  data_files: flores200/flores_200_tl.jsonl
- config_name: flores_tr
  data_files: flores200/flores_200_tr.jsonl
- config_name: flores_uk
  data_files: flores200/flores_200_uk.jsonl
- config_name: flores_umb
  data_files: flores200/flores_200_umb.jsonl
- config_name: flores_ur
  data_files: flores200/flores_200_ur.jsonl
- config_name: flores_uz
  data_files: flores200/flores_200_uz.jsonl
- config_name: flores_wo
  data_files: flores200/flores_200_wo.jsonl
- config_name: flores_xh
  data_files: flores200/flores_200_xh.jsonl
- config_name: flores_yo
  data_files: flores200/flores_200_yo.jsonl
- config_name: flores_zho_trad
  data_files: flores200/flores_200_zho_trad.jsonl
- config_name: flores_zu
  data_files: flores200/flores_200_zu.jsonl
---
## Dataset Sources

- **Paper**: BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models
- **Link**: https://huggingface.co/papers/2502.07346
- **Repository**: https://github.com/CONE-MT/BenchMAX

## Dataset Description
BenchMAX_General_Translation is a dataset of [BenchMAX](https://arxiv.org/pdf/2502.07346), which evaluates the translation capability on the general domain.

We collect parallel test data from [Flore-200](https://github.com/facebookresearch/flores), [TED-talk](https://huggingface.co/datasets/IWSLT/ted_talks_iwslt), and [WMT24](https://www2.statmt.org/wmt24/).

## Usage

Run the following commands to generate translations and evaluate translations. Metrics now include spBLEU, BLEU, TER, and xCOMET.

```bash
git clone https://github.com/CONE-MT/BenchMAX.git
cd BenchMAX
pip install -r requirements.txt

cd tasks/translation
# generate general translations
# -s denotes source languages, -t denotes target languages
python generate_translation.py -s en -t zh,es,fr,de,ru,ja,th,sw,bn,te,ar,ko,vi,cs,hu,sr --task-name flores --model-name $model --infer-backend vllm --max-tokens 512
python generate_translation.py -s zh,es,fr,de,ru,ja,th,sw,bn,te,ar,ko,vi,cs,hu,sr -t en --task-name flores --model-name $model --infer-backend vllm --max-tokens 512
python generate_translation.py -s en -t zh,es,fr,de,ru,ja,th,bn,ar,ko,vi,cs,hu,sr --task-name ted --model-name $model --infer-backend vllm --max-tokens 512
python generate_translation.py -s zh,es,fr,de,ru,ja,th,bn,ar,ko,vi,cs,hu,sr -t en --task-name ted --model-name $model --infer-backend vllm --max-tokens 512
python generate_translation.py -s en -t cs,de,es,ja,ru,zh --task-name wmt24 --model-name $model --infer-backend vllm --max-tokens 1024

# evaluate general translations
python evaluate_translation.py -s en -t zh,es,fr,de,ru,ja,th,sw,bn,te,ar,ko,vi,cs,hu,sr --task-name flores --model-name $model --metrics spBLEU
python evaluate_translation.py -s zh,es,fr,de,ru,ja,th,sw,bn,te,ar,ko,vi,cs,hu,sr -t en --task-name flores --model-name $model --metrics spBLEU
python evaluate_translation.py -s en -t zh,es,fr,de,ru,ja,th,bn,ar,ko,vi,cs,hu,sr --task-name ted --model-name $model --metrics spBLEU
python evaluate_translation.py -s zh,es,fr,de,ru,ja,th,bn,ar,ko,vi,cs,hu,sr -t en --task-name ted --model-name $model --metrics spBLEU
python evaluate_translation.py -s en -t cs,de,es,ja,ru,zh --task-name wmt24 --model-name $model --metrics spBLEU

```

## Supported Languages
Arabic, Bengali, Chinese, Czech, English, French, German, Hungarian, Japanese, Korean, Serbian, Spanish, Swahili, Telugu, Thai, Russian, Vietnamese

## Citation
If you find our dataset helpful, please cite this paper:

```
@article{huang2025benchmax,
  title={BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models},
  author={Huang, Xu and Zhu, Wenhao and Hu, Hanxu and He, Conghui and Li, Lei and Huang, Shujian and Yuan, Fei},
  journal={arXiv preprint arXiv:2502.07346},
  year={2025}
}
```
