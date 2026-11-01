---
language_creators:
- expert-generated
# All ISO 639-3 and BCP-47 codes for the 278 languoids in question
language: ['aa', 'aar', 'abl', 'af', 'afr', 'agr', 'aiq', 'als', 'am', 'amh', 'ami', 'ane', 'apc', 'arh', 'arn', 'arz', 'as', 'asm', 'ayr', 'ayz', 'azb', 'azj', 'azm', 'azz', 'ba', 'bak', 'bam', 'bas', 'bba', 'be', 'bel', 'ben', 'bft', 'bg', 'bhb', 'bho', 'bm', 'bn', 'bo', 'bod', 'bos', 'br', 'bre', 'brh', 'brx', 'bs', 'bsh', 'bsk', 'bul', 'ca', 'cak', 'cat', 'ce', 'ceb', 'ces', 'che', 'chr', 'chv', 'cja', 'cjk', 'ckb', 'ckl', 'cmn', 'crk', 'cs', 'cux', 'cv', 'cy', 'cym', 'da', 'dan', 'daq', 'de', 'deu', 'dgo', 'dik', 'diq', 'div', 'djc', 'dje', 'dtm', 'dts', 'dua', 'dv', 'dz', 'dzo', 'ekk', 'el', 'ell', 'en', 'enb', 'eng', 'enl', 'es', 'eto', 'eu', 'eus', 'ewo', 'fao', 'fi', 'fia', 'fin', 'fo', 'fr', 'fra', 'fry', 'fuc', 'fuv', 'fvr', 'fy', 'ga', 'gax', 'gaz', 'gd', 'gil', 'gkp', 'gl', 'gla', 'gle', 'glg', 'gom', 'gu', 'guc', 'gug', 'guj', 'guz', 'gxx', 'ha', 'hat', 'hau', 'he', 'heb', 'heh', 'hi', 'hin', 'hne', 'hr', 'hrv', 'ht', 'hu', 'hun', 'hve', 'hy', 'hye', 'ibo', 'id', 'ig', 'ijc', 'ilo', 'ind', 'irk', 'is', 'isl', 'it', 'ita', 'ja', 'jav', 'jmc', 'jnj', 'jpn', 'jv', 'ka', 'kaa', 'kac', 'kai', 'kal', 'kam', 'kan', 'kat', 'kaz', 'kea', 'kek', 'khk', 'khm', 'khq', 'khw', 'kin', 'kir', 'kjh', 'kk', 'kl', 'kls', 'km', 'kmb', 'kmr', 'kn', 'knc', 'knw', 'ko', 'kor', 'krt', 'kru', 'ksf', 'ktu', 'kuj', 'kwy', 'kxp', 'ky', 'lao', 'led', 'lg', 'lgg', 'li', 'lij', 'lim', 'lin', 'lir', 'lit', 'lld', 'ln', 'lo', 'loa', 'loh', 'lt', 'lug', 'luo', 'lvs', 'maf', 'mai', 'mal', 'mam', 'mar', 'mas', 'mey', 'mi', 'mie', 'min', 'miq', 'mk', 'mkd', 'ml', 'mlt', 'mos', 'mr', 'mri', 'mt', 'mtq', 'my', 'mya', 'mzl', 'naq', 'nhe', 'nl', 'nld', 'nlv', 'nn', 'nno', 'npi', 'nso', 'nus', 'ny', 'nya', 'ory', 'pa', 'pan', 'pbs', 'pbt', 'pcm', 'pes', 'pl', 'plt', 'pol', 'por', 'pt', 'quc', 'quh', 'quz', 'rm', 'ro', 'rob', 'roh', 'ron', 'ru', 'rus', 'rw', 'sat', 'sba', 'scn', 'sd', 'se', 'sgc', 'shn', 'si', 'sif', 'sin', 'sk', 'skr', 'sl', 'slk', 'slv', 'sme', 'sn', 'sna', 'snd', 'so', 'som', 'sot', 'spa', 'sr', 'sro', 'srp', 'ss', 'ssw', 'st', 'su', 'sun', 'sv', 'swe', 'swh', 'szl', 'ta', 'tam', 'taq', 'tat', 'tda', 'te', 'tel', 'tg', 'tgk', 'tgl', 'th', 'tha', 'ti', 'tir', 'tl', 'tn', 'toc', 'tpi', 'tpl', 'tr', 'ts', 'tsg', 'tsn', 'tso', 'tsz', 'tt', 'tui', 'tur', 'tw', 'twi', 'tzh', 'tzm', 'ug', 'uig', 'uk', 'ukr', 'umb', 'ur', 'urd', 'uzn', 've', 'ven', 'vi', 'vie', 'vmw', 'war', 'wlv', 'wo', 'wol', 'wuu', 'xh', 'xho', 'xuu', 'ydd', 'ydg', 'yo', 'yor', 'yua', 'yue', 'zai', 'zne', 'zsm', 'zu', 'zul']
license: cc-by-4.0
task_categories:
- translation
size_categories:
- 1K<n<10K
configs:

# All languages put together

- config_name: default
  data_files:
  - split: dev
    path: "data/*_level/dev/*.parquet"
  - split: test
    path: "data/*_level/test/*.parquet"
- config_name: sentence_level
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/*.parquet"
  - split: test
    path: "data/sentence_level/**/test/*.parquet"
- config_name: paragraph_level
  data_files:
  - split: dev
    path: "data/paragraph_level/dev/*.parquet"
  - split: test
    path: "data/paragraph_level/test/*.parquet"
- config_name: benchmark
  data_files:
  - split: dev
    path: "benchmark_data/*_level/dev/*.parquet"
  - split: test
    path: "benchmark_data/*_level/test/*.parquet"
- config_name: benchmark_sentence_level
  data_files:
  - split: dev
    path: "benchmark_data/sentence_level/**/dev/*.parquet"
  - split: test
    path: "benchmark_data/sentence_level/**/test/*.parquet"
- config_name: benchmark_paragraph_level
  data_files:
  - split: dev
    path: "benchmark_data/paragraph_level/dev/*.parquet"
  - split: test
    path: "benchmark_data/paragraph_level/test/*.parquet"

# the subset of the languages contributed by Mozilla

- config_name: Mozilla
  data_files:
  - split: dev
    path: "data/*/Mozilla/dev/*.parquet"
  - split: test
    path: "data/*/Mozilla/test/*.parquet"
- config_name: Mozilla_sentence_level
  data_files:
  - split: dev
    path: "data/sentence_level/Mozilla/dev/*.parquet"
  - split: test
    path: "data/sentence_level/Mozilla/test/*.parquet"
- config_name: Mozilla_paragraph_level
  data_files:
  - split: dev
    path: "data/paragraph_level/Mozilla/dev/*.parquet"
  - split: test
    path: "data/paragraph_level/Mozilla/test/*.parquet"

# Language-specific configs

- config_name: aar_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/aar_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/aar_Latn.parquet"
- config_name: abl_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/abl_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/abl_Latn.parquet"
- config_name: afr_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/afr_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/afr_Latn.parquet"
- config_name: agr_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/agr_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/agr_Latn.parquet"
- config_name: aiq_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/aiq_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/aiq_Arab.parquet"
- config_name: als_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/als_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/als_Latn.parquet"
- config_name: amh_Ethi
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/amh_Ethi.parquet"
  - split: test
    path: "data/sentence_level/**/test/amh_Ethi.parquet"
- config_name: ami_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ami_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ami_Latn.parquet"
- config_name: ane_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ane_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ane_Latn.parquet"
- config_name: apc_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/apc_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/apc_Arab.parquet"
- config_name: arh_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/arh_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/arh_Latn.parquet"
- config_name: arn_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/arn_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/arn_Latn.parquet"
- config_name: arz_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/arz_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/arz_Arab.parquet"
- config_name: arz_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/arz_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/arz_Latn.parquet"
- config_name: asm_Beng
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/asm_Beng.parquet"
  - split: test
    path: "data/sentence_level/**/test/asm_Beng.parquet"
- config_name: ayr_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ayr_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ayr_Latn.parquet"
- config_name: ayz_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ayz_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ayz_Latn.parquet"
- config_name: azb_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/azb_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/azb_Arab.parquet"
- config_name: azj_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/azj_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/azj_Latn.parquet"
- config_name: azm_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/azm_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/azm_Latn.parquet"
- config_name: azz_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/azz_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/azz_Latn.parquet"
- config_name: bak_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bak_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/bak_Cyrl.parquet"
- config_name: bam_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bam_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/bam_Latn.parquet"
- config_name: bas_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bas_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/bas_Latn.parquet"
- config_name: bba_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bba_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/bba_Latn.parquet"
- config_name: bel_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bel_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/bel_Cyrl.parquet"
- config_name: ben_Beng
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ben_Beng.parquet"
  - split: test
    path: "data/sentence_level/**/test/ben_Beng.parquet"
- config_name: ben_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ben_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ben_Latn.parquet"
- config_name: bft_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bft_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/bft_Arab.parquet"
- config_name: bhb_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bhb_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/bhb_Deva.parquet"
- config_name: bho_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bho_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/bho_Deva.parquet"
- config_name: bod_Tibt
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bod_Tibt.parquet"
  - split: test
    path: "data/sentence_level/**/test/bod_Tibt.parquet"
- config_name: bos_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bos_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/bos_Latn.parquet"
- config_name: bre_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bre_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/bre_Latn.parquet"
- config_name: brh_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/brh_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/brh_Arab.parquet"
- config_name: brx_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/brx_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/brx_Deva.parquet"
- config_name: bsh_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bsh_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/bsh_Arab.parquet"
- config_name: bsk_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bsk_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/bsk_Arab.parquet"
- config_name: bul_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/bul_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/bul_Cyrl.parquet"
- config_name: cak_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/cak_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/cak_Latn.parquet"
- config_name: cat_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/cat_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/cat_Latn.parquet"
- config_name: ceb_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ceb_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ceb_Latn.parquet"
- config_name: ces_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ces_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ces_Latn.parquet"
- config_name: che_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/che_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/che_Cyrl.parquet"
- config_name: chr_Cher
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/chr_Cher.parquet"
  - split: test
    path: "data/sentence_level/**/test/chr_Cher.parquet"
- config_name: chv_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/chv_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/chv_Cyrl.parquet"
- config_name: cja_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/cja_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/cja_Arab.parquet"
- config_name: cjk_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/cjk_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/cjk_Latn.parquet"
- config_name: ckb_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ckb_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/ckb_Arab.parquet"
- config_name: ckl_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ckl_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ckl_Latn.parquet"
- config_name: cmn_Hans
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/cmn_Hans.parquet"
  - split: test
    path: "data/sentence_level/**/test/cmn_Hans.parquet"
- config_name: cmn_Hant
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/cmn_Hant.parquet"
  - split: test
    path: "data/sentence_level/**/test/cmn_Hant.parquet"
- config_name: crk_Cans
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/crk_Cans.parquet"
  - split: test
    path: "data/sentence_level/**/test/crk_Cans.parquet"
- config_name: crk_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/crk_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/crk_Latn.parquet"
- config_name: cux_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/cux_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/cux_Latn.parquet"
- config_name: cym_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/cym_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/cym_Latn.parquet"
- config_name: dan_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/dan_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/dan_Latn.parquet"
- config_name: daq_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/daq_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/daq_Deva.parquet"
- config_name: deu_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/deu_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/deu_Latn.parquet"
- config_name: dgo_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/dgo_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/dgo_Deva.parquet"
- config_name: dik_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/dik_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/dik_Latn.parquet"
- config_name: diq_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/diq_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/diq_Latn.parquet"
- config_name: div_Thaa
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/div_Thaa.parquet"
  - split: test
    path: "data/sentence_level/**/test/div_Thaa.parquet"
- config_name: djc_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/djc_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/djc_Latn.parquet"
- config_name: dje_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/dje_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/dje_Latn.parquet"
- config_name: dtm_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/dtm_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/dtm_Latn.parquet"
- config_name: dts_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/dts_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/dts_Latn.parquet"
- config_name: dua_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/dua_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/dua_Latn.parquet"
- config_name: dzo_Tibt
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/dzo_Tibt.parquet"
  - split: test
    path: "data/sentence_level/**/test/dzo_Tibt.parquet"
- config_name: ekk_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ekk_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ekk_Latn.parquet"
- config_name: ell_Grek
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ell_Grek.parquet"
  - split: test
    path: "data/sentence_level/**/test/ell_Grek.parquet"
- config_name: enb_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/enb_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/enb_Latn.parquet"
- config_name: eng_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/eng_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/eng_Latn.parquet"
- config_name: enl_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/enl_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/enl_Latn.parquet"
- config_name: eto_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/eto_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/eto_Latn.parquet"
- config_name: eus_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/eus_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/eus_Latn.parquet"
- config_name: ewo_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ewo_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ewo_Latn.parquet"
- config_name: fao_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/fao_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/fao_Latn.parquet"
- config_name: fia_Copt
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/fia_Copt.parquet"
  - split: test
    path: "data/sentence_level/**/test/fia_Copt.parquet"
- config_name: fin_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/fin_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/fin_Latn.parquet"
- config_name: fra_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/fra_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/fra_Latn.parquet"
- config_name: fry_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/fry_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/fry_Latn.parquet"
- config_name: fuc_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/fuc_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/fuc_Latn.parquet"
- config_name: fuv_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/fuv_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/fuv_Latn.parquet"
- config_name: fvr_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/fvr_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/fvr_Latn.parquet"
- config_name: gax_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/gax_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/gax_Latn.parquet"
- config_name: gaz_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/gaz_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/gaz_Latn.parquet"
- config_name: gil_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/gil_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/gil_Latn.parquet"
- config_name: gkp_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/gkp_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/gkp_Latn.parquet"
- config_name: gla_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/gla_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/gla_Latn.parquet"
- config_name: gle_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/gle_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/gle_Latn.parquet"
- config_name: glg_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/glg_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/glg_Latn.parquet"
- config_name: gom_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/gom_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/gom_Deva.parquet"
- config_name: guc_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/guc_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/guc_Latn.parquet"
- config_name: gug_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/gug_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/gug_Latn.parquet"
- config_name: guj_Gujr
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/guj_Gujr.parquet"
  - split: test
    path: "data/sentence_level/**/test/guj_Gujr.parquet"
- config_name: guz_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/guz_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/guz_Latn.parquet"
- config_name: gxx_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/gxx_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/gxx_Latn.parquet"
- config_name: hat_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/hat_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/hat_Latn.parquet"
- config_name: hau_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/hau_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/hau_Latn.parquet"
- config_name: heb_Hebr
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/heb_Hebr.parquet"
  - split: test
    path: "data/sentence_level/**/test/heb_Hebr.parquet"
- config_name: heh_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/heh_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/heh_Latn.parquet"
- config_name: hin_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/hin_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/hin_Deva.parquet"
- config_name: hin_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/hin_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/hin_Latn.parquet"
- config_name: hne_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/hne_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/hne_Deva.parquet"
- config_name: hrv_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/hrv_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/hrv_Latn.parquet"
- config_name: hun_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/hun_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/hun_Latn.parquet"
- config_name: hve_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/hve_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/hve_Latn.parquet"
- config_name: hye_Armn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/hye_Armn.parquet"
  - split: test
    path: "data/sentence_level/**/test/hye_Armn.parquet"
- config_name: ibo_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ibo_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ibo_Latn.parquet"
- config_name: ijc_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ijc_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ijc_Latn.parquet"
- config_name: ilo_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ilo_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ilo_Latn.parquet"
- config_name: ind_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ind_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ind_Latn.parquet"
- config_name: irk_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/irk_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/irk_Latn.parquet"
- config_name: isl_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/isl_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/isl_Latn.parquet"
- config_name: ita_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ita_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ita_Latn.parquet"
- config_name: jav_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/jav_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/jav_Latn.parquet"
- config_name: jmc_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/jmc_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/jmc_Latn.parquet"
- config_name: jnj_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/jnj_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/jnj_Latn.parquet"
- config_name: jpn_Jpan
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/jpn_Jpan.parquet"
  - split: test
    path: "data/sentence_level/**/test/jpn_Jpan.parquet"
- config_name: kaa_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kaa_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/kaa_Cyrl.parquet"
- config_name: kac_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kac_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kac_Latn.parquet"
- config_name: kai_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kai_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kai_Latn.parquet"
- config_name: kal_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kal_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kal_Latn.parquet"
- config_name: kam_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kam_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kam_Latn.parquet"
- config_name: kan_Knda
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kan_Knda.parquet"
  - split: test
    path: "data/sentence_level/**/test/kan_Knda.parquet"
- config_name: kat_Geor
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kat_Geor.parquet"
  - split: test
    path: "data/sentence_level/**/test/kat_Geor.parquet"
- config_name: kaz_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kaz_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/kaz_Cyrl.parquet"
- config_name: kea_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kea_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kea_Latn.parquet"
- config_name: kek_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kek_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kek_Latn.parquet"
- config_name: khk_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/khk_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/khk_Cyrl.parquet"
- config_name: khm_Khmr
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/khm_Khmr.parquet"
  - split: test
    path: "data/sentence_level/**/test/khm_Khmr.parquet"
- config_name: khq_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/khq_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/khq_Latn.parquet"
- config_name: khw_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/khw_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/khw_Arab.parquet"
- config_name: kin_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kin_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kin_Latn.parquet"
- config_name: kir_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kir_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/kir_Cyrl.parquet"
- config_name: kjh_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kjh_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/kjh_Cyrl.parquet"
- config_name: kls_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kls_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/kls_Arab.parquet"
- config_name: kmb_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kmb_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kmb_Latn.parquet"
- config_name: kmr_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kmr_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kmr_Latn.parquet"
- config_name: knc_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/knc_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/knc_Arab.parquet"
- config_name: knw_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/knw_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/knw_Latn.parquet"
- config_name: kor_Kore
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kor_Kore.parquet"
  - split: test
    path: "data/sentence_level/**/test/kor_Kore.parquet"
- config_name: krt_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/krt_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/krt_Latn.parquet"
- config_name: kru_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kru_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/kru_Deva.parquet"
- config_name: ksf_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ksf_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ksf_Latn.parquet"
- config_name: ktu_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ktu_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ktu_Latn.parquet"
- config_name: kuj_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kuj_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kuj_Latn.parquet"
- config_name: kwy_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kwy_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/kwy_Latn.parquet"
- config_name: kxp_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/kxp_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/kxp_Arab.parquet"
- config_name: lao_Laoo
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lao_Laoo.parquet"
  - split: test
    path: "data/sentence_level/**/test/lao_Laoo.parquet"
- config_name: led_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/led_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/led_Latn.parquet"
- config_name: lgg_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lgg_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/lgg_Latn.parquet"
- config_name: lij_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lij_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/lij_Latn.parquet"
- config_name: lim_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lim_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/lim_Latn.parquet"
- config_name: lin_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lin_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/lin_Latn.parquet"
- config_name: lir_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lir_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/lir_Latn.parquet"
- config_name: lld_Latn_badi1244
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lld_Latn_badi1244.parquet"
  - split: test
    path: "data/sentence_level/**/test/lld_Latn_badi1244.parquet"
- config_name: lld_Latn_gard1241
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lld_Latn_gard1241.parquet"
  - split: test
    path: "data/sentence_level/**/test/lld_Latn_gard1241.parquet"
- config_name: lit_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lit_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/lit_Latn.parquet"
- config_name: loa_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/loa_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/loa_Latn.parquet"
- config_name: loh_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/loh_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/loh_Latn.parquet"
- config_name: lug_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lug_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/lug_Latn.parquet"
- config_name: luo_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/luo_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/luo_Latn.parquet"
- config_name: lvs_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/lvs_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/lvs_Latn.parquet"
- config_name: maf_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/maf_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/maf_Latn.parquet"
- config_name: mai_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mai_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/mai_Deva.parquet"
- config_name: mal_Mlym
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mal_Mlym.parquet"
  - split: test
    path: "data/sentence_level/**/test/mal_Mlym.parquet"
- config_name: mam_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mam_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/mam_Latn.parquet"
- config_name: mar_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mar_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/mar_Deva.parquet"
- config_name: mas_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mas_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/mas_Latn.parquet"
- config_name: mey_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mey_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/mey_Latn.parquet"
- config_name: mie_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mie_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/mie_Latn.parquet"
- config_name: min_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/min_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/min_Arab.parquet"
- config_name: miq_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/miq_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/miq_Latn.parquet"
- config_name: mkd_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mkd_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/mkd_Cyrl.parquet"
- config_name: mlt_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mlt_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/mlt_Latn.parquet"
- config_name: mos_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mos_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/mos_Latn.parquet"
- config_name: mri_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mri_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/mri_Latn.parquet"
- config_name: mtq_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mtq_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/mtq_Latn.parquet"
- config_name: mya_Mymr
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mya_Mymr.parquet"
  - split: test
    path: "data/sentence_level/**/test/mya_Mymr.parquet"
- config_name: mzl_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/mzl_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/mzl_Latn.parquet"
- config_name: naq_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/naq_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/naq_Latn.parquet"
- config_name: nhe_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/nhe_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/nhe_Latn.parquet"
- config_name: nld_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/nld_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/nld_Latn.parquet"
- config_name: nlv_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/nlv_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/nlv_Latn.parquet"
- config_name: nno_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/nno_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/nno_Latn.parquet"
- config_name: npi_Deva
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/npi_Deva.parquet"
  - split: test
    path: "data/sentence_level/**/test/npi_Deva.parquet"
- config_name: nso_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/nso_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/nso_Latn.parquet"
- config_name: nus_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/nus_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/nus_Latn.parquet"
- config_name: nya_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/nya_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/nya_Latn.parquet"
- config_name: ory_Orya
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ory_Orya.parquet"
  - split: test
    path: "data/sentence_level/**/test/ory_Orya.parquet"
- config_name: pan_Guru
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/pan_Guru.parquet"
  - split: test
    path: "data/sentence_level/**/test/pan_Guru.parquet"
- config_name: pbs_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/pbs_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/pbs_Latn.parquet"
- config_name: pbt_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/pbt_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/pbt_Arab.parquet"
- config_name: pcm_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/pcm_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/pcm_Latn.parquet"
- config_name: pes_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/pes_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/pes_Arab.parquet"
- config_name: plt_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/plt_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/plt_Latn.parquet"
- config_name: pol_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/pol_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/pol_Latn.parquet"
- config_name: por_Latn_braz1246
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/por_Latn_braz1246.parquet"
  - split: test
    path: "data/sentence_level/**/test/por_Latn_braz1246.parquet"
- config_name: quc_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/quc_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/quc_Latn.parquet"
- config_name: quh_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/quh_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/quh_Latn.parquet"
- config_name: quz_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/quz_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/quz_Latn.parquet"
- config_name: rob_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/rob_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/rob_Latn.parquet"
- config_name: roh_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/roh_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/roh_Latn.parquet"
- config_name: ron_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ron_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ron_Latn.parquet"
- config_name: rus_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/rus_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/rus_Cyrl.parquet"
- config_name: sat_Olck
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sat_Olck.parquet"
  - split: test
    path: "data/sentence_level/**/test/sat_Olck.parquet"
- config_name: sba_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sba_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/sba_Latn.parquet"
- config_name: scn_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/scn_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/scn_Latn.parquet"
- config_name: sgc_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sgc_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/sgc_Latn.parquet"
- config_name: shn_Mymr
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/shn_Mymr.parquet"
  - split: test
    path: "data/sentence_level/**/test/shn_Mymr.parquet"
- config_name: sif_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sif_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/sif_Latn.parquet"
- config_name: sin_Sinh
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sin_Sinh.parquet"
  - split: test
    path: "data/sentence_level/**/test/sin_Sinh.parquet"
- config_name: skr_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/skr_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/skr_Arab.parquet"
- config_name: slk_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/slk_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/slk_Latn.parquet"
- config_name: slv_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/slv_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/slv_Latn.parquet"
- config_name: sme_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sme_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/sme_Latn.parquet"
- config_name: sna_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sna_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/sna_Latn.parquet"
- config_name: snd_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/snd_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/snd_Arab.parquet"
- config_name: som_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/som_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/som_Latn.parquet"
- config_name: sot_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sot_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/sot_Latn.parquet"
- config_name: spa_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/spa_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/spa_Latn.parquet"
- config_name: sro_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sro_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/sro_Latn.parquet"
- config_name: srp_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/srp_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/srp_Cyrl.parquet"
- config_name: ssw_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ssw_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ssw_Latn.parquet"
- config_name: sun_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/sun_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/sun_Latn.parquet"
- config_name: swe_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/swe_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/swe_Latn.parquet"
- config_name: swh_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/swh_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/swh_Latn.parquet"
- config_name: szl_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/szl_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/szl_Latn.parquet"
- config_name: tam_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tam_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tam_Latn.parquet"
- config_name: tam_Taml
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tam_Taml.parquet"
  - split: test
    path: "data/sentence_level/**/test/tam_Taml.parquet"
- config_name: taq_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/taq_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/taq_Latn.parquet"
- config_name: taq_Tfng
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/taq_Tfng.parquet"
  - split: test
    path: "data/sentence_level/**/test/taq_Tfng.parquet"
- config_name: tat_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tat_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/tat_Cyrl.parquet"
- config_name: tda_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tda_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tda_Latn.parquet"
- config_name: tel_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tel_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tel_Latn.parquet"
- config_name: tel_Telu
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tel_Telu.parquet"
  - split: test
    path: "data/sentence_level/**/test/tel_Telu.parquet"
- config_name: tgk_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tgk_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/tgk_Cyrl.parquet"
- config_name: tgl_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tgl_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tgl_Latn.parquet"
- config_name: tha_Thai
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tha_Thai.parquet"
  - split: test
    path: "data/sentence_level/**/test/tha_Thai.parquet"
- config_name: tir_Ethi
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tir_Ethi.parquet"
  - split: test
    path: "data/sentence_level/**/test/tir_Ethi.parquet"
- config_name: toc_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/toc_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/toc_Latn.parquet"
- config_name: tpi_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tpi_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tpi_Latn.parquet"
- config_name: tpl_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tpl_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tpl_Latn.parquet"
- config_name: tsg_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tsg_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tsg_Latn.parquet"
- config_name: tsn_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tsn_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tsn_Latn.parquet"
- config_name: tso_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tso_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tso_Latn.parquet"
- config_name: tsz_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tsz_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tsz_Latn.parquet"
- config_name: tui_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tui_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tui_Latn.parquet"
- config_name: tur_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tur_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tur_Latn.parquet"
- config_name: twi_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/twi_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/twi_Latn.parquet"
- config_name: tzh_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tzh_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/tzh_Latn.parquet"
- config_name: tzm_Tfng
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/tzm_Tfng.parquet"
  - split: test
    path: "data/sentence_level/**/test/tzm_Tfng.parquet"
- config_name: uig_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/uig_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/uig_Arab.parquet"
- config_name: ukr_Cyrl
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ukr_Cyrl.parquet"
  - split: test
    path: "data/sentence_level/**/test/ukr_Cyrl.parquet"
- config_name: umb_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/umb_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/umb_Latn.parquet"
- config_name: urd_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/urd_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/urd_Arab.parquet"
- config_name: urd_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/urd_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/urd_Latn.parquet"
- config_name: uzn_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/uzn_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/uzn_Latn.parquet"
- config_name: ven_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ven_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/ven_Latn.parquet"
- config_name: vie_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/vie_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/vie_Latn.parquet"
- config_name: vmw_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/vmw_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/vmw_Latn.parquet"
- config_name: war_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/war_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/war_Latn.parquet"
- config_name: wlv_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/wlv_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/wlv_Latn.parquet"
- config_name: wol_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/wol_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/wol_Latn.parquet"
- config_name: wuu_Hans
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/wuu_Hans.parquet"
  - split: test
    path: "data/sentence_level/**/test/wuu_Hans.parquet"
- config_name: xho_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/xho_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/xho_Latn.parquet"
- config_name: xuu_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/xuu_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/xuu_Latn.parquet"
- config_name: ydd_Hebr
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ydd_Hebr.parquet"
  - split: test
    path: "data/sentence_level/**/test/ydd_Hebr.parquet"
- config_name: ydg_Arab
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/ydg_Arab.parquet"
  - split: test
    path: "data/sentence_level/**/test/ydg_Arab.parquet"
- config_name: yor_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/yor_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/yor_Latn.parquet"
- config_name: yua_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/yua_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/yua_Latn.parquet"
- config_name: yue_Hant
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/yue_Hant.parquet"
  - split: test
    path: "data/sentence_level/**/test/yue_Hant.parquet"
- config_name: zai_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/zai_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/zai_Latn.parquet"
- config_name: zne_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/zne_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/zne_Latn.parquet"
- config_name: zsm_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/zsm_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/zsm_Latn.parquet"
- config_name: zul_Latn
  data_files:
  - split: dev
    path: "data/sentence_level/**/dev/zul_Latn.parquet"
  - split: test
    path: "data/sentence_level/**/test/zul_Latn.parquet"

# Met-Bouquet

- config_name: met_bouquet_xstsrp
  data_files:
  - split: dev
    path: "met_bouquet_data/XSTSRP_r*/dev/*.parquet"
  - split: test
    path: "met_bouquet_data/XSTSRP_r*/test/*.parquet"
- config_name: met_bouquet_xstsrp_r1
  data_files:
  - split: dev
    path: "met_bouquet_data/XSTSRP_r1/dev/*.parquet"
  - split: test
    path: "met_bouquet_data/XSTSRP_r1/test/*.parquet"
- config_name: met_bouquet_xstsrp_r2
  data_files:
  - split: test
    path: "met_bouquet_data/XSTSRP_r2/test/*.parquet"
- config_name: met_bouquet_xsts
  data_files:
  - split: dev
    path: "met_bouquet_data/XSTS/dev/*.parquet"
  - split: test
    path: "met_bouquet_data/XSTS/test/*.parquet"
- config_name: met_bouquet_rsqm
  data_files:
  - split: dev
    path: "met_bouquet_data/RSQM/dev/*.parquet"
  - split: test
    path: "met_bouquet_data/RSQM/test/*.parquet"
- config_name: met_bouquet_all_protocols
  data_files:
  - split: dev
    path: "met_bouquet_data/*/dev/*.parquet"
  - split: test
    path: "met_bouquet_data/*/test/*.parquet"


extra_gated_heading: Protecting the integrity of BOUQuET for evaluation
extra_gated_fields:
  "This data is for evaluation purposes only; You may not use any of this data or its derivatives for training machine learning / AI models": checkbox
  "You may only distribute, embed, or otherwise transfer this data or its derivatives via a mechanism that is either private or that implements protections against automated crawling (such as using a password-protected archive or a gating mechanism that requires users to accept these terms before accessing the dataset)": checkbox
  "Your distributions must retain these terms": checkbox
---


# BOUQuET 💐: Benchmark and Open initiative for Universal Quality Evaluation in Translation

BOUQuET is a multi-way parallel, multi-centric and multi-register/domain dataset and benchmark for machine translation quality.

The underlying texts have been handcrafted by linguists in 8 diverse languages (Egyptian Arabic, French, German, Hindi, Indonesian, Mandarin Chinese, Russian, and Spanish) and translated to English and 269 other languoids (language + script + dialect combinations). The dataset is intended to be extensible to virtually any other written language. Volunteers can contribute new translations via https://bouquet.metademolab.com.

BOUQuET includes Met-BOUQuET: a set of machine translations with human judgements of translation quality that can be used for developing or validating metrics for automated evaluation of translation.

BOUQuET has been originally described in the paper by [Omnilingual Team, 2025](https://arxiv.org/abs/2502.04314), and its extension to more languages and to quality estimation data was described in [Omnilingual Team, 2026](https://arxiv.org/abs/2603.16309).

Associated leaderboard: https://huggingface.co/spaces/facebook/bouquet

Code for evaluation: https://github.com/facebookresearch/bouquet


## Dataset Details

### Dataset Description

- **Language(s) (NLP):** multilingual (278 varieties)
- **Home:** https://bouquet.metademolab.com/
- **Paper:** https://arxiv.org/abs/2502.04314, https://arxiv.org/abs/2603.16309
- **Leaderboard:** https://huggingface.co/spaces/facebook/bouquet

## Uses

### Base BOUQuET
The dataset is intended for evaluation of machine translation quality.
By purpose, it is similar to [FLORES+](https://huggingface.co/datasets/openlanguagedata/flores_plus) or [WMT24++](https://huggingface.co/datasets/google/wmt24pp).
Unlike these datasets, BOUQuET focuses more on linguistic diversity, both across languages (including some extremely low-resourced languages) and within a language (covering different registers).

The base BOUQuET dataset is not intended as a training dataset, but the `dev` subset may be used for validation during model development.

As default evaluation metrics, we recommend [ChrF++](https://github.com/mjpost/sacrebleu)
and [MetricX](https://huggingface.co/google/metricx-24-hybrid-xl-v2p6). For difficult target languages, mode-based metrics like MetricX should be adjusted with LID scores (e.g. by [GlotLID](https://huggingface.co/cis-lmu/glotlid)) to penalize off-target translations. Our [evaluation codebase](https://github.com/facebookresearch/bouquet) contains the recommended implementations of evaluation metrics.

### Met-BOUQUET
Met-BOUQUET is intended for evaluating automatic metrics of metrics of machine translation quality. We allow the use of its `dev` subset for training discriminative (non-generative) models for quality estimation, but the `test` subset is still reserved exclusively for evaluation.

## Dataset Structure

### Composition
BOUQuET consists of short paragraphs, fully parallel in all languages at the sentence level.
The dataset is distributed both at the sentence level and at the paragraph level.
By default, data with both levels is loaded; the `paragraph_level` and `sentence_level` configs may be used to load the levels separately.

The public portion of the dataset contains two splits:
- `dev`: 504 unique sentences, 120 paragraphs
- `test`: 854 unique sentences, 198 paragraphs

An additional split made up of 632 unique sentences and 144 paragraphs is being held out for quality assurance purposes and is not distributed here.

Met-BOUQuET contains BOUQuET sentences on the source side and their machine translations on the target side. It consists of several partitions:
- `XSTS+R+P` annotations: sentences annotated with the main protocol, `XSTS+R+P`, which is a version of [XSTS](https://arxiv.org/abs/2205.08533) sensitive to register and paragraph context, including:
  - Round 1: sentences from the `dev` and `test` splits, translated in 102 directions (once per direction) with diversely sampled translation systems.
  - Round 2: sentences from the and `test` split, translated in 57 difficult directions, twice per direction: by an OMT system and a baseline system.
- `XSTS`: a subset of Round 1 translations (16 directions) annotated with the base [XSTS](https://arxiv.org/abs/2205.08533) protocol.
- `RSQM`: a subset of Round 1 translations (14 directions) annotated with the RSQM protocol (a simplified version of MQM).

### Data configs

There are two views of the base BOUQuET dataset:
- Default view (every language is represented on the source side and paired with English on the target side). Thus, there are 278 directions (every language paired with English, including English itself): this includes `default`, `paragraph_level`, and `sentence_level` configs, as well as language-specific configs.
- Benchmark view: every language is paired with English (both as source and target) and, in most cases, with one or more other languages (chosen based on several criteria, including regional proximity); currently, there are 1062 translation directions (all symmetric, with 548 English-centric and 514 non-English-centric directions); this includes the `benchmark`, `benchmark_sentence_level`, and `benchmark_paragraph_level` configs.

Despite being distributed in these (somehow arbitrarily chosen pairs), the dataset is actually fully multi-way parallel, so any language could be paired with any other to evaluate the directions that are of interest to the user.

As for Met-BOUQuET, the `XSTS+R+P`, `XSTS` and `RSQM` parts are accessible via the configs `met_bouquet_xstsrp`, `met_bouquet_xsts`, and `met_bouquet_rsqm`, respectively.
To download their union, `met_bouquet_all_protocols` config can be used.

### Mozilla contributions

A part of the BOUQuET dataset has been contributed by the [Mozilla Foundation](https://www.mozillafoundation.org).
This parts consist of translations into the following 16 language varieties: `azz_Latn`, `bas_Latn`, `bft_Arab`, `brh_Arab`, `bsh_Arab`, `cak_Latn`, `chv_Cyrl`, `cux_Latn`, `dua_Latn`, `eto_Latn`, `kls_Arab`, `ksf_Latn`, `kxp_Arab`, `skr_Arab`, `tui_Latn`, `ydg_Arab`.

To locate these contributions, you could do either of the following:

- Load the dataset with the designated data configs: `Mozilla_sentence_level` for the sentence-level translations (paired with English), `Mozilla_paragraph_level` for the paragraph-level ones, or simply `Mozilla`. For example, the code `datasets.load_dataset("facebook/bouquet", "Mozilla")` would do it. [Here](https://huggingface.co/datasets/facebook/bouquet/viewer/Mozilla) is the associated dataset viewer.
- Access the data directly from the filesystem, using the `data/sentence_level/Mozilla` and `data/paragraph_level/Mozilla` directories. [Here](https://huggingface.co/datasets/facebook/bouquet/tree/main/data/sentence_level/Mozilla) is an example path to the sentence-level files.

This subset of the data will additionally be available on the [Mozilla Data Collective](https://mozilladatacollective.com/) platform.

We are extremely grateful to our Mozilla Foundation partners for this collaboration!

### Columns

The base BOUQuET dataset contains the following fields:
```
 - level           # str, "sentence_level" or "paragraph_level"
 - split           # str, "dev" or "test"
 - uniq_id         # str, identifier of the dataset item (e.g. `P464-S1` for sentence-level, `P464` for paragraph-level data)
 - src_lang        # str, NLLB-compatible non-English language code (such as `hin_Deva`)
 - tgt_lang        # str, "eng_Latn"
 - src_text        # str, non-English text
 - tgt_text        # str, English text
 - orig_text       # str, the original text (sentence or paragraph), which sometimes corresponds to src_text
 - par_comment     # str, comment to the whole paragraph
 - newline_next    # bool, whether the sentence should be followed by a newline in the paragraph
 - par_id          # str, paragraph id (e.g. `P464`)
 - domain          # str, one of the 8 domains (see the paper for the list of domains)
 - register        # str, three-letter identifier of the register (see the paper for the explanation of their meaning)
 - tags            # str, comma-separated linguistic tags of a sentence (see the paper)
```

Met-BOUQuET dataset has a slightly different set of columns:
```
- src_lang                    # str, source language code, e.g `eng_Latn`
- tgt_lang                    # str, target language code
- uniq_id                     # str, identifier of the sentence (same as in the base BOUQuET, e.g. `P464-S1`)
- domain                      # str, one of the 8 domains
- register_label              # str, three-letter identifier of the register
- src_text                    # str, source text (from the base BOUQuET dataset)
- mt_text                     # str, machine translation
- consensus_score             # float, the single score of translation quality aggregated from the annotators' scores
- n_annotators                # int, number of the annotators for the given translation
- score_list                  # List[float], list of the individual quality scores provided by the annotators
- par_harmonic_mean_consensus # float, translation quality score aggregated for the current paragraph
- par_n_sentences             # int, number of sentences in the current paragraph
- protocol                    # str, annotation protocol: eithet `XSTS+R+P`, `XSTS` or `RSQM`
- ref_text                    # str, reference text (from the base BOUQuET dataset); might be empty if the target language does not have BOUQuET translations
- has_ref                     # bool, whether the reference text is non empty
- par_id                      # str, paragraph id (same as in the base BOUQuET, e.g. `P464`)
- system                      # str, identifier of the translation system
- system_group                # str, id of the group of the translation system (external or internal baseline, OMT, OMT+RAG, or LLaMA+RAG)
- round                       # int, round of the annotations: 1 or 2 (see above)
- split                       # str, split of the data (`dev` or `test` for Round 1, `test` for Round 2)
- direction                   # str, combination of the source and target language (e.g. `ami_Latn-cmn_Hant`)
```

### Languages

Currently, BOUQuET covers 278 language varieties (more will be added later): 8 source ("pivot") languages + English + 269 added languoids (including 5 donated by community).

<details>
    <summary>List of languages</summary>

| Code.  | ISO 639-3 | ISO 15924  | Language             | Family               | Comment                              |
|:---------|:--------|:-----------|:---------------------|:---------------------|:-------------------------------------|
aar_Latn   | aar | Latn | Afar                           | Afro-Asiatic         |
abl_Latn   | abl | Latn | Lampung Nyo                    | Austronesian         |
afr_Latn   | afr | Latn | Afrikaans                      | Indo-European        |
agr_Latn   | agr | Latn | Aguaruna                       | Chicham              |
aiq_Arab   | aiq | Arab | Aimaq                          | Indo-European        |
als_Latn   | als | Latn | Tosk Albanian                  | Indo-European        |
amh_Ethi   | amh | Ethi | Amharic                        | Afro-Asiatic         |
ami_Latn   | ami | Latn | Amis                           | Austronesian         |
ane_Latn   | ane | Latn | Xârâcùù                        | Austronesian         |
apc_Arab   | apc | Arab | Levantine Arabic               | Afro-Asiatic         |
arh_Latn   | arh | Latn | Arhuaco                        | Chibchan             |
arn_Latn   | arn | Latn | Mapudungun                     | Araucanian           |
arz_Arab   | arz | Arab | Egyptian Arabic                | Afro-Asiatic         | Code-switching with Modern Standard Arabic (arb_Arab)
arz_Latn   | arz | Latn | Egyptian Arabic (Romanized)    | Afro-Asiatic         | Code-switching with Modern Standard Arabic (arb_Latn)
asm_Beng   | asm | Beng | Assamese                       | Indo-European        |
ayr_Latn   | ayr | Latn | Central Aymara                 | Aymaran              |
ayz_Latn   | ayz | Latn | Mai Brat                       | Maybratic            |
azb_Arab   | azb | Arab | South Azerbaijani              | Turkic               |
azj_Latn   | azj | Latn | North Azerbaijani              | Turkic               |
azm_Latn   | azm | Latn | Ipalapa Amuzgo                 | Otomanguean          |
azz_Latn   | azz | Latn | Highland Puebla Nahuatl        | Uto-Aztecan          |
bak_Cyrl   | bak | Cyrl | Bashkir                        | Turkic               | Community-contributed
bam_Latn   | bam | Latn | Bambara                        | Mande                |
bas_Latn   | bas | Latn | Basaa                          | Atlantic-Congo       |
bba_Latn   | bba | Latn | Baatonum                       | Atlantic-Congo       |
bel_Cyrl   | bel | Cyrl | Belarusian                     | Indo-European        |
ben_Beng   | ben | Beng | Bengali                        | Indo-European        |
ben_Latn   | ben | Latn | Bengali (Romanized)            | Indo-European        |
bft_Arab   | bft | Arab | Balti                          | Sino-Tibetan         |
bhb_Deva   | bhb | Deva | Bhili                          | Indo-European        |
bho_Deva   | bho | Deva | Bhojpuri                       | Indo-European        |
bod_Tibt   | bod | Tibt | Tibetan                        | Sino-Tibetan         |
bos_Latn   | bos | Latn | Bosnian                        | Indo-European        |
bre_Latn   | bre | Latn | Breton                         | Indo-European        |
brh_Arab   | brh | Arab | Brahui                         | Dravidian            |
brx_Deva   | brx | Deva | Bodo (India)                   | Sino-Tibetan         |
bsh_Arab   | bsh | Arab | Kateviri                       | Indo-European        |
bsk_Arab   | bsk | Arab | Burushaski                     | Burushaski           |
bul_Cyrl   | bul | Cyrl | Bulgarian                      | Indo-European        |
cak_Latn   | cak | Latn | Kaqchikel                      | Mayan                |
cat_Latn   | cat | Latn | Catalan                        | Indo-European        |
ceb_Latn   | ceb | Latn | Cebuano                        | Austronesian         |
ces_Latn   | ces | Latn | Czech                          | Indo-European        |
che_Cyrl   | che | Cyrl | Chechen                        | Nakh-Daghestanian    | Community-contributed
chr_Cher   | chr | Cher | Cherokee                       | Iroquoian            |
chv_Cyrl   | chv | Cyrl | Chuvash                        | Turkic               |
cja_Arab   | cja | Arab | Western Cham                   | Austronesian         |
cjk_Latn   | cjk | Latn | Chokwe                         | Atlantic-Congo       |
ckb_Arab   | ckb | Arab | Sorani Kurdish                 | Indo-European        |
ckl_Latn   | ckl | Latn | Kibaku                         | Afro-Asiatic         |
cmn_Hans   | cmn | Hans | Mandarin (Simplified)          | Sino-Tibetan         |
cmn_Hant   | cmn | Hant | Mandarin (Traditional)         | Sino-Tibetan         |
crk_Cans   | crk | Cans | Plains Cree                    | Algic                |
crk_Latn   | crk | Latn | Plains Cree                    | Algic                |
cux_Latn   | cux | Latn | Tepeuxila Cuicatec             | Otomanguean          |
cym_Latn   | cym | Latn | Welsh                          | Indo-European        |
dan_Latn   | dan | Latn | Danish                         | Indo-European        |
daq_Deva   | daq | Deva | Dandami Maria                  | Dravidian            |
deu_Latn   | deu | Latn | German                         | Indo-European        |
dgo_Deva   | dgo | Deva | Dogri                          | Indo-European        |
dik_Latn   | dik | Latn | Southwestern Dinka             | Nilotic              |
diq_Latn   | diq | Latn | Zazaki - Southern Zaza         | Indo-European        |
div_Thaa   | div | Thaa | Dhivehi                        | Indo-European        |
djc_Latn   | djc | Latn | Dar Daju                       | Dajuic               |
dje_Latn   | dje | Latn | Zarma                          | Songhay              |
dtm_Latn   | dtm | Latn | Tomo Kan Dogon                 | Dogon                |
dts_Latn   | dts | Latn | Toro So Dogon                  | Dogon                |
dua_Latn   | dua | Latn | Duala                          | Atlantic-Congo       |
dzo_Tibt   | dzo | Tibt | Dzongkha                       | Sino-Tibetan         |
ekk_Latn   | ekk | Latn | Standard Estonian              | Uralic               |
ell_Grek   | ell | Grek | Modern Greek                   | Indo-European        |
enb_Latn   | enb | Latn | Markweeta                      | Nilotic              |
eng_Latn   | eng | Latn | English                        | Indo-European        |
enl_Latn   | enl | Latn | Enlhet                         | Lengua-Mascoy        |
eto_Latn   | eto | Latn | Eton                           | Atlantic-Congo       |
eus_Latn   | eus | Latn | Basque                         | Basque               |
ewo_Latn   | ewo | Latn | Ewondo                         | Atlantic-Congo       |
fao_Latn   | fao | Latn | Faroese                        | Indo-European        |
fia_Copt   | fia | Copt | Nobiin                         | Nubian               |
fin_Latn   | fin | Latn | Finnish                        | Uralic               |
fra_Latn   | fra | Latn | French                         | Indo-European        |
fry_Latn   | fry | Latn | Western Frisian                | Indo-European        |
fuc_Latn   | fuc | Latn | Pulaar                         | Atlantic-Congo       |
fuv_Latn   | fuv | Latn | Nigerian Fulfulde              | Atlantic-Congo       |
fvr_Latn   | fvr | Latn | Fur                            | Furan                |
gax_Latn   | gax | Latn | Borana-Arsi-Guji Oromo         | Afro-Asiatic         |
gaz_Latn   | gaz | Latn | West Central Oromo             | Afro-Asiatic         |
gil_Latn   | gil | Latn | Gilbertese                     | Austronesian         |
gkp_Latn   | gkp | Latn | Kpelle (Guinea)                | Mande                |
gla_Latn   | gla | Latn | Scottish Gaelic                | Indo-European        |
gle_Latn   | gle | Latn | Irish                          | Indo-European        |
glg_Latn   | glg | Latn | Galician                       | Indo-European        |
gom_Deva   | gom | Deva | Goan Konkani                   | Indo-European        |
guc_Latn   | guc | Latn | Wayuu                          | Arawakan             |
gug_Latn   | gug | Latn | Paraguayan Guarani             | Tupian               |
guj_Gujr   | guj | Gujr | Gujarati                       | Indo-European        |
guz_Latn   | guz | Latn | Gusii                          | Atlantic-Congo       |
gxx_Latn   | gxx | Latn | Southern Wè                    | Kru                  |
hat_Latn   | hat | Latn | Haitian Creole                 | Indo-European        |
hau_Latn   | hau | Latn | Hausa                          | Afro-Asiatic         |
heb_Hebr   | heb | Hebr | Hebrew                         | Afro-Asiatic         |
heh_Latn   | heh | Latn | Hehe                           | Atlantic-Congo       |
hin_Deva   | hin | Deva | Hindi                          | Indo-European        |
hin_Latn   | hin | Latn | Hindi (Romanized)              | Indo-European        |
hne_Deva   | hne | Deva | Chhattisgarhi                  | Indo-European        |
hrv_Latn   | hrv | Latn | Croatian                       | Indo-European        |
hun_Latn   | hun | Latn | Hungarian                      | Uralic               |
hve_Latn   | hve | Latn | San Dionisio del Mar Huave     | Huavean              |
hye_Armn   | hye | Armn | Armenian                       | Indo-European        |
ibo_Latn   | ibo | Latn | Igbo                           | Atlantic-Congo       |
ijc_Latn   | ijc | Latn | Izon                           | Ijoid                |
ilo_Latn   | ilo | Latn | Iloko                          | Austronesian         |
ind_Latn   | ind | Latn | Indonesian                     | Austronesian         |
irk_Latn   | irk | Latn | Iraqw                          | Afro-Asiatic         |
isl_Latn   | isl | Latn | Icelandic                      | Indo-European        |
ita_Latn   | ita | Latn | Italian                        | Indo-European        |
jav_Latn   | jav | Latn | Javanese                       | Austronesian         |
jmc_Latn   | jmc | Latn | Machame                        | Atlantic-Congo       |
jnj_Latn   | jnj | Latn | Yemsa                          | Ta-Ne-Omotic         |
jpn_Jpan   | jpn | Jpan | Japanese                       | Japonic              |
kaa_Cyrl   | kaa | Cyrl | Karakalpak                     | Turkic               |
kac_Latn   | kac | Latn | Kachin                         | Sino-Tibetan         |
kai_Latn   | kai | Latn | Karekare                       | Afro-Asiatic         |
kal_Latn   | kal | Latn | Kalaallisut                    | Eskimo-Aleut         |
kam_Latn   | kam | Latn | Kamba                          | Atlantic-Congo       |
kan_Knda   | kan | Knda | Kannada                        | Dravidian            |
kat_Geor   | kat | Geor | Georgian                       | Kartvelian           |
kaz_Cyrl   | kaz | Cyrl | Kazakh                         | Turkic               |
kea_Latn   | kea | Latn | Kabuverdianu                   | Indo-European        |
kek_Latn   | kek | Latn | Kekchí                         | Mayan                |
khk_Cyrl   | khk | Cyrl | Halh Mongolian                 | Mongolic-Khitan      |
khm_Khmr   | khm | Khmr | Central Khmer                  | Austroasiatic        |
khq_Latn   | khq | Latn | Koyra Chiini Songhay           | Songhay              |
khw_Arab   | khw | Arab | Khowar                         | Indo-European        |
kin_Latn   | kin | Latn | Kinyarwanda                    | Atlantic-Congo       |
kir_Cyrl   | kir | Cyrl | Kyrgyz                         | Turkic               |
kjh_Cyrl   | kjh | Cyrl | Khakas                         | Turkic               | Community-contributed
kls_Arab   | kls | Arab | Kalasha                        | Indo-European        |
kmb_Latn   | kmb | Latn | Kimbundu                       | Atlantic-Congo       |
kmr_Latn   | kmr | Latn | Kurmanji Kurdish               | Indo-European        |
knc_Arab   | knc | Arab | Central Kanuri                 | Saharan              |
knw_Latn   | knw | Latn | Kung-Ekoka                     | Kxa                  |
kor_Kore   | kor | Kore | Korean                         | Koreanic             |
krt_Latn   | krt | Latn | Tumari Kanuri                  | Saharan              |
kru_Deva   | kru | Deva | Kurukh                         | Dravidian            |
ksf_Latn   | ksf | Latn | Bafia                          | Atlantic-Congo       |
ktu_Latn   | ktu | Latn | Kituba                         | Atlantic-Congo       |
kuj_Latn   | kuj | Latn | Kuria                          | Atlantic-Congo       |
kwy_Latn   | kwy | Latn | San Salvador Kongo             | Atlantic-Congo       |
kxp_Arab   | kxp | Arab | Koli Wadiyari                  | Indo-European        |
lao_Laoo   | lao | Laoo | Lao                            | Tai-Kadai            |
led_Latn   | led | Latn | Lendu                          | Central Sudanic      |
lgg_Latn   | lgg | Latn | Lugbara                        | Central Sudanic      |
lij_Latn   | lij | Latn | Ligurian                       | Indo-European        |
lim_Latn   | lim | Latn | Limburgish                     | Indo-European        |
lin_Latn   | lin | Latn | Kinshasa Lingala               | Atlantic-Congo       |
lir_Latn   | lir | Latn | Liberian Kreyol                | Pidgin               |
lit_Latn   | lit | Latn | Lithuanian                     | Indo-European        |
lld_Latn_badi1244 | lld | Latn | Ladin (Val Badia dialect) | Indo-European        | Community-contributed
lld_Latn_gard1241 | lld | Latn | Ladin (Gherdëina dialect) | Indo-European        | Community-contributed
loa_Latn   | loa | Latn | Loloda                         | North Halmahera      |
loh_Latn   | loh | Latn | Narim                          | Surmic               |
lug_Latn   | lug | Latn | Ganda                          | Atlantic-Congo       |
luo_Latn   | luo | Latn | Luo                            | Nilotic              |
lvs_Latn   | lvs | Latn | Standard Latvian               | Indo-European        |
maf_Latn   | maf | Latn | Mafa                           | Afro-Asiatic         |
mai_Deva   | mai | Deva | Maithili                       | Indo-European        |
mal_Mlym   | mal | Mlym | Malayalam                      | Dravidian            |
mam_Latn   | mam | Latn | Mam                            | Mayan                |
mar_Deva   | mar | Deva | Marathi                        | Indo-European        |
mas_Latn   | mas | Latn | Masai                          | Nilotic              |
mey_Latn   | mey | Latn | Hassaniyya Arabic              | Afro-Asiatic         |
mie_Latn   | mie | Latn | Ocotepec Mixtec                | Otomanguean          |
min_Arab   | min | Arab | Minangkabau                    | Austronesian         |
miq_Latn   | miq | Latn | Miskito                        | Misumalpan           |
mkd_Cyrl   | mkd | Cyrl | Macedonian                     | Indo-European        |
mlt_Latn   | mlt | Latn | Maltese                        | Afro-Asiatic         |
mos_Latn   | mos | Latn | Mossi                          | Atlantic-Congo       |
mri_Latn   | mri | Latn | Māori                          | Austronesian         |
mtq_Latn   | mtq | Latn | Muong                          | Austroasiatic        |
mya_Mymr   | mya | Mymr | Burmese                        | Sino-Tibetan         |
mzl_Latn   | mzl | Latn | Mazatlán Mixe                  | Mixe-Zoque           |
naq_Latn   | naq | Latn | Nama                           | Khoe-Kwadi           |
nhe_Latn   | nhe | Latn | Eastern Huasteca Nahuatl       | Uto-Aztecan          |
nld_Latn   | nld | Latn | Standard Dutch                 | Indo-European        |
nlv_Latn   | nlv | Latn | Orizaba Nahuatl                | Uto-Aztecan          |
nno_Latn   | nno | Latn | Nynorsk                        | Indo-European        |
npi_Deva   | npi | Deva | Nepali                         | Indo-European        |
nso_Latn   | nso | Latn | Northern Sotho                 | Atlantic-Congo       |
nus_Latn   | nus | Latn | Nuer                           | Nilotic              |
nya_Latn   | nya | Latn | Nyanja                         | Atlantic-Congo       |
ory_Orya   | ory | Orya | Oriya                          | Indo-European        |
pbs_Latn   | pbs | Latn | Central Pame                   | Otomanguean          |
pbt_Arab   | pbt | Arab | Southern Pashto                | Indo-European        |
pcm_Latn   | pcm | Latn | Nigerian Pidgin                | Indo-European        |
pes_Arab   | pes | Arab | Western Persian                | Indo-European        |
plt_Latn   | plt | Latn | Plateau Malagasy               | Austronesian         |
pnb_Guru   | pnb | Guru | Western Punjabi                | Indo-European        |
pol_Latn   | pol | Latn | Polish                         | Indo-European        |
por_Latn   | por | Latn | Brazilian Portuguese           | Indo-European        |
quc_Latn   | quc | Latn | K'iche'                        | Mayan                |
quh_Latn   | quh | Latn | South Bolivian Quechua         | Quechuan             |
quz_Latn   | quz | Latn | Cusco Quechua                  | Quechuan             |
rob_Latn   | rob | Latn | Tae’                           | Austronesian         |
roh_Latn   | roh | Latn | Romansh                        | Indo-European        |
ron_Latn   | ron | Latn | Romanian                       | Indo-European        |
rus_Cyrl   | rus | Cyrl | Russian                        | Indo-European        |
sat_Olck   | sat | Olck | Santali                        | Austroasiatic        |
sba_Latn   | sba | Latn | Ngambay                        | Central Sudanic      |
scn_Latn   | scn | Latn | Sicilian                       | Indo-European        |
sgc_Latn   | sgc | Latn | Kipsigis                       | Nilotic              |
shn_Mymr   | shn | Mymr | Shan                           | Tai-Kadai            |
sif_Latn   | sif | Latn | Siamou                         | Siamou               |
sin_Sinh   | sin | Sinh | Sinhala                        | Indo-European        |
skr_Arab   | skr | Arab | Saraiki                        | Indo-European        |
slk_Latn   | slk | Latn | Slovak                         | Indo-European        |
slv_Latn   | slv | Latn | Slovene                        | Indo-European        |
sme_Latn   | sme | Latn | Northern Sami                  | Uralic               |
sna_Latn   | sna | Latn | Shona                          | Atlantic-Congo       |
snd_Arab   | snd | Arab | Sindhi                         | Indo-European        |
som_Latn   | som | Latn | Somali                         | Afro-Asiatic         |
sot_Latn   | sot | Latn | Southern Sotho                 | Atlantic-Congo       |
spa_Latn   | spa | Latn | Spanish                        | Indo-European        |
sro_Latn   | sro | Latn | Sardinian Campidanese          | Indo-European        |
srp_Cyrl   | srp | Cyrl | Serbian                        | Indo-European        |
ssw_Latn   | ssw | Latn | Swati                          | Atlantic-Congo       |
sun_Latn   | sun | Latn | Sundanese                      | Austronesian         |
swe_Latn   | swe | Latn | Swedish                        | Indo-European        |
swh_Latn   | swh | Latn | Swahili                        | Atlantic-Congo       |
szl_Latn   | szl | Latn | Silesian                       | Indo-European        |
tam_Latn   | tam | Latn | Tamil (Romanized)              | Dravidian            |
tam_Taml   | tam | Taml | Tamil                          | Dravidian            |
taq_Latn   | taq | Latn | Tamashek (Romanized)           | Afro-Asiatic         |
taq_Tfng   | taq | Tfng | Tamashek                       | Afro-Asiatic         |
tat_Cyrl   | tat | Cyrl | Tatar                          | Turkic               |
tda_Latn   | tda | Latn | Tagdal                         | Songhay              |
tel_Latn   | tel | Latn | Telugu (Romanized)             | Dravidian            |
tel_Telu   | tel | Telu | Telugu                         | Dravidian            |
tgk_Cyrl   | tgk | Cyrl | Tajik                          | Indo-European        |
tgl_Latn   | tgl | Latn | Tagalog                        | Austronesian         |
tha_Thai   | tha | Thai | Thai                           | Tai-Kadai            |
tir_Ethi   | tir | Ethi | Tigrinya                       | Afro-Asiatic         |
toc_Latn   | toc | Latn | Coyutla Totonac                | Totonacan            |
tpi_Latn   | tpi | Latn | Tok Pisin                      | Indo-European        |
tpl_Latn   | tpl | Latn | Tlacoapa Me’phaa               | Otomanguean          |
tsg_Latn   | tsg | Latn | Tausug                         | Austronesian         |
tsn_Latn   | tsn | Latn | Tswana                         | Atlantic-Congo       |
tso_Latn   | tso | Latn | Tsonga                         | Atlantic-Congo       |
tsz_Latn   | tsz | Latn | Purepecha                      | Tarascan             |
tui_Latn   | tui | Latn | Tupuri                         | Atlantic-Congo       |
tur_Latn   | tur | Latn | Turkish                        | Turkic               |
twi_Latn   | twi | Latn | Twi                            | Atlantic-Congo       |
tzh_Latn   | tzh | Latn | Tzeltal                        | Mayan                |
tzm_Tfng   | tzm | Tfng | Central Atlas Tamazight        | Afro-Asiatic         |
uig_Arab   | uig | Arab | Uyghur                         | Turkic               |
ukr_Cyrl   | ukr | Cyrl | Ukrainian                      | Indo-European        |
umb_Latn   | umb | Latn | Umbundu                        | Atlantic-Congo       |
urd_Arab   | urd | Arab | Urdu                           | Indo-European        |
urd_Latn   | urd | Latn | Urdu (Romanized)               | Indo-European        |
uzn_Latn   | uzn | Latn | Northern Uzbek                 | Turkic               |
ven_Latn   | ven | Latn | Venda                          | Atlantic-Congo       |
vie_Latn   | vie | Latn | Vietnamese                     | Austroasiatic        |
vmw_Latn   | vmw | Latn | Makhuwa                        | Atlantic-Congo       |
war_Latn   | war | Latn | Waray                          | Austronesian         |
wlv_Latn   | wlv | Latn | Bermejo Wichí                  | Mataguayan           |
wol_Latn   | wol | Latn | Wolof                          | Atlantic-Congo       |
wuu_Hans   | wuu | Hans | Wu Chinese                     | Sino-Tibetan         |
xho_Latn   | xho | Latn | Xhosa                          | Atlantic-Congo       |
xuu_Latn   | xuu | Latn | Khwedam                        | Khoe-Kwadi           |
ydd_Hebr   | ydd | Hebr | Eastern Yiddish                | Indo-European        |
ydg_Arab   | ydg | Arab | Yadgha                         | Indo-European        |
yor_Latn   | yor | Latn | Yoruba                         | Atlantic-Congo       |
yua_Latn   | yua | Latn | Yucateco                       | Mayan                |
yue_Hant   | yue | Hant | Yue Chinese                    | Sino-Tibetan         |
zai_Latn   | zai | Latn | Isthmus Zapotec                | Otomanguean          |
zsm_Latn   | zsm | Latn | Colloquial Malay               | Austronesian         | Code-switching with Standard Malay (zlm_Latn)
zne_Latn   | zne | Latn | Zande                          | Atlantic-Congo       |
zul_Latn   | zul | Latn | Zulu                           | Atlantic-Congo       |

For some translation directions of the Round 2 Met-BOUQuET, there are currently no human translations of BOUQuET into the respective target language: `abz_Latn akb_Latn any_Latn awa_Deva bcc_Arab bem_Latn bsq_Latn dga_Latn kdj_Latn lua_Latn mad_Latn mim_Latn mni_Mtei osi_Latn tzo_Latn`. Therefore, these languages are represented in the dataset only as (very imperfect) machine translations, not as human translations.
</details>


Each language variety is characterized by an ISO 639-3 code for its language (sometimes several codes to emphasize code mixing, as in the case of Egyptian Arabic and Malay), an ISO 15924 code for the writing system, and, optionally, a Glottocode (currently, it is applied only to mark the Brazilian Portuguese as distinct from the European Portuguese).

To contribute translations for new languages, please use our crowdsourcing tool: https://bouquet.metademolab.com.

## Usage examples

The code below loads a pre-configured subset, French sentences paired with English, and selects the first instance
```Python
import datasets
data = datasets.load_dataset("facebook/bouquet", "fra_Latn", split="dev")

# to demonstrate an example, we select a single data instance
data[0]
# {'uniq_id': 'P037-S1',
#  'src_lang': 'fra_Latn',
#  'src_text': 'Tu as des mains en or, la nourriture est délicieuse.',
#  'tgt_lang': 'eng_Latn',
#  'domain': 'comments',
#  'tgt_text': 'Bless your hands, the food was very delicious. ',
#  'par_comment': 'possessive pronoun  "your" is 2nd person feminine',
#  'tags': 'second person, single tense (past)',
#  'register': 'mra',
#  'orig_text': 'تسلم ايديكي الاكل كان جميل جدًا',
#  'newline_next': True,
#  'level': 'sentence_level',
#  'split': 'dev',
#  'par_id': 'P037'}
```

Another example loads paragraph-level data paired with English, and then pairs Spanish sentences with their Russian translations:

```Python
import datasets
data = datasets.load_dataset("facebook/bouquet", "paragraph_level", split="dev").to_pandas()

spa2rus = pd.merge(
    data.loc[data["src_lang"].eq("spa_Latn")].drop(["tgt_lang", "tgt_text"], axis=1),
    data.loc[data["src_lang"].eq("rus_Cyrl"), ["src_lang", "src_text", "uniq_id"]].rename({"src_lang": "tgt_lang", "src_text": "tgt_text"}, axis=1),
    on="uniq_id",
)
```

The final example loads the XSTS+R+P part of the Met-BOUQuET dataset (dev split) and displays the first sample:

```Python
import datasets
data = datasets.load_dataset("facebook/bouquet",  "met_bouquet_xstsrp_r1", split="dev")

# to demonstrate an example, we select a single data instance
data[0]
# {'src_lang': 'aar_Latn',
#  'tgt_lang': 'arz_Arab',
#  'system': 'OMT-LLaMA-8B-experimental-3a921d66',
#  'uniq_id': 'P001-S1',
#  'domain': 'how-to | instructions',
#  'register_label': 'uca',
#  'src_text': 'Mahshi "dolmah" elle bicisan inni baaxook baaxol baxsale.',
#  'mt_text': 'المحشي "الدولمة" هو طبق يصنع من عجينة كبيرة تُشكل كأس.',
#  'consensus_score': 1.0,
#  'n_annotators': 3,
#  'score_list': [2.0, 1.0, 1.0],
#  'par_harmonic_mean_consensus': 1.2,
#  'par_n_sentences': 3,
#  'protocol': 'XSTS+R+P',
#  'ref_text': 'طريقة عمل المحشي بتختلف كتير من بلد لبلد',
#  'has_ref': True,
#  'par_id': 'P001',
#  'system_group': 'internal_baseline',
#  'round': 1,
#  'split': 'dev',
#  'direction': 'aar_Latn-arz_Arab'}
```

### Troubleshooting

- If you encounter an fsspec-related error when loading the dataset, please upgrade your dependencies: `pip install --upgrade datasets huggingface_hub fsspec`
- If you are getting a `GatedRepoError`, please make sure that you have:
  1. Logged into the HuggingFace website (this one);
  2. Accepted the terms of use of this dataset;
  3. Authenticated in your environment via a Huggingface token or the `login` method or `huggingface_hub`.
  See https://huggingface.co/docs/hub/en/datasets-gated for more detailed instructions.


## Dataset Creation

### Curation Rationale for base BOUQuET

The dataset has been created manually from scratch, by composing the source sentences that cover a variety of domains and registers in 8 diverse non-English languages: Egyptian Arabic (alternating with Modern Standard Arabic when appropriate), French, German, Hindi, Indonesian, Mandarin Chinese, Russian, and Spanish.

For each of the source languages, the sentences have been created in the following 8 domains:
1. How-to, written tutorials or instructions
2. Conversations (dialogues)
3. Narration (creative writing that doesn’t include dialogues)
4. Social media posts
5. Social media comments (reactive)
6. Other web content
7. Reflective piece
8. Miscellaneous (address to a nation, disaster response, etc.)

Apart from the domains, a variety of registers (contextual styles) were used. Each sentence is annotated with the register characterized by three features: connectedness, preparedness, and social differential.

The linguists who were creating the dataset were instructed to maintain the diversity of sentence lengths, word orders, sentence structures, and other linguistic characteristics.

Subsequently, the source sentences were translated from the 8 source languages into English, and then, into the other languages. We plan to extend the dataset "in width", by translating it into even more languages.

See the [paper](https://aclanthology.org/2025.emnlp-main.1400/) for more details.

### Curation Rationale for Met-BOUQuET

Met-BOUQuET has been built with several goals in mind:
- Provide quality judgements over translations that are diverse in terms of directions, systems, and quality levels. Targeted in Round 1 of XSTS+R+P annotation. For each sentence and direction, one translation system is selected, to maximize diversity.
- Compare the XSTS+R+P protocol with other human evaluation protocols. Targeted with the XSTS and RSQM annotations.
- Compare an OMT translation system with a strong open baseline for very chalenging translation directions. Targeted in Round 2 of XSTS+R+P annotation. For each sentence and direction, there are two translations.

All Met-BOUQuET data points are translations of BOUQuET sentences with either OMT models or open translation systems.

See the Section 8.2 of the [Omnilingual MT paper](https://arxiv.org/abs/2603.16309) for more details and discussion. See the file `XSTSRP_guidelines.md` file for the XSTS+R+P annnotation instructions.

## Contribution

To contribute to the dataset (adding translations for a new language, or verifying some of the existing translations), please use the web annotation tool at https://bouquet.metademolab.com.

## Citation


If you are referring to this dataset, please cite the [BOUQuET paper](https://aclanthology.org/2025.emnlp-main.1400/) and the [Omnilingual MT paper](TODO).

```bibtex
@inproceedings{andrews-etal-2025-bouquet,
    title = "{BOUQ}u{ET} : dataset, Benchmark and Open initiative for Universal Quality Evaluation in Translation",
    author = "Andrews, Pierre  and
      Artetxe, Mikel  and
      Meglioli, Mariano Coria  and
      Costa-juss{\`a}, Marta R.  and
      Chuang, Joe  and
      Dale, David  and
      Duppenthaler, Mark  and
      Ekberg, Nathanial Paul  and
      Gao, Cynthia  and
      Licht, Daniel Edward  and
      Maillard, Jean  and
      Mourachko, Alexandre  and
      Ropers, Christophe  and
      Saleem, Safiyyah  and
      S{\'a}nchez, Eduardo  and
      Tsiamas, Ioannis  and
      Turkatenko, Arina  and
      Ventayol-Boada, Albert  and
      Yates, Shireen",
    editor = "Christodoulopoulos, Christos  and
      Chakraborty, Tanmoy  and
      Rose, Carolyn  and
      Peng, Violet",
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.emnlp-main.1400/",
    doi = "10.18653/v1/2025.emnlp-main.1400",
    pages = "27515--27535",
    ISBN = "979-8-89176-332-6",
}

@misc{omnilingual2026,
    title={Omnilingual {MT}: Machine Translation for 1,600 Languages},
    author={The Omnilingual MT Team and Belen Alastruey and Niyati Bafna and Andrea Caciolai and Kevin Heffernan and Artyom Kozhevnikov and Christophe Ropers and Eduardo S{\'a}nchez and Charles-Eric Saint-James and Ioannis Tsiamas and Chierh Cheng and Joe Chuang and Paul-Ambroise Duquenne and Mark Duppenthaler and Nate Ekberg and Cynthia Gao and Pere Llu{\'i}s Huguet Cabot and Jo{\~a}o Maria Janeiro and Jean Maillard and Gabriel Mejia Gonzalez and Holger Schwenk and Edan Toledo and Arina Turkatenko and Albert Ventayol-Boada and Rashel Moritz and Alexandre Mourachko and Surya Parimi and Mary Williamson and Shireen Yates and David Dale and Marta R. Costa-juss{\`a}},
    year={2026},
    eprint={},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    url={https://arxiv.org/abs/2603.16309},
}
```

## License

This dataset is released under CC-BY-4.0.

## Glossary

- **Domain.** By the term *domain*, we mean different spaces in which language is produced in speech, sign, or writing (e.g., books, social media, news, Wikipedia, organization websites, official documents, direct messaging, texting). In this paper, we focus solely on the written modality.
- **Register.** We understand the term *register* as a functional variety of language that includes socio-semiotic properties, as expressed in [Halliday and Matthiessen (2004)], or more simply as a "contextual style", as presented in [Labov (1991), pp.79–99]. In that regard, a register is a specific variety of language used to best fit a specific communicative purpose in a specific situation.

## Changelog
- Oct 13, 2026: add two Ladin varieties (thanks to [Frontull et al, 2026](https://www2.statmt.org/wmt26/pdf/2026.wmt-1.193.pdf)) and Khakas (thanks to [@adeshkin](https://huggingface.co/adeshkin)) — for now, without updating the `benchmark` config
- Apr 21, 2026: update translation for 5 languages, add locator for Mozilla contributions
- Mar 17, 2026: extend to 275 language varieties in total, add Met-BOUQuET
- Nov 7, 2025: add 17 new languages, edit some translations
- Aug 1, 2025: add 28 new languages
- Jun 10, 2025: released the first version of the dataset (the 9 core languages)
