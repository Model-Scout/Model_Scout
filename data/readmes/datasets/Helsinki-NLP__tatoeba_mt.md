---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- afr
- ain
- ara
- asm
- avk
- awa
- aze
- bel
- ben
- ber
- bre
- bua
- bub
- bul
- bzt
- cat
- cbk
- ceb
- ces
- cha
- chm
- chv
- cor
- crh
- cym
- dan
- deu
- dsb
- dtp
- egl
- ell
- eng
- enm
- epo
- est
- eus
- fao
- fas
- fin
- fkv
- fra
- frr
- fry
- gcf
- gla
- gle
- glg
- gos
- got
- grc
- grn
- gsw
- hau
- hbs
- heb
- hin
- hoc
- hrx
- hsb
- hun
- hye
- ido
- ile
- ilo
- ina
- isl
- ita
- jav
- jbo
- jpn
- kab
- kat
- kaz
- kha
- khm
- kor
- kur
- kzj
- lad
- lao
- lat
- lav
- lfn
- lij
- lit
- ltz
- mal
- mar
- mkd
- mlt
- mon
- mri
- msa
- mya
- nds
- nld
- nor
- nov
- nst
- oci
- orv
- oss
- ota
- pam
- pcd
- pmn
- pms
- pol
- por
- prg
- que
- rom
- ron
- run
- rus
- sah
- sat
- slv
- spa
- sqi
- swa
- swe
- swg
- tam
- tat
- tel
- tgl
- tha
- tlh
- tok
- tuk
- tur
- tzl
- uig
- ukr
- urd
- uzb
- vie
- vol
- war
- xal
- xho
- yid
- zho
- zza
license:
- cc-by-2.0
multilinguality:
- translation
pretty_name: The Tatoeba Translation Challenge
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-generation
- translation
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test/*.tsv
  - split: dev
    path: data/dev/*.tsv
  sep: "\t"
  quoting: 3
- config_name: afr-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.afr-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: afr-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.afr-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.afr-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: afr-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.afr-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: afr-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.afr-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: afr-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.afr-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: afr-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.afr-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: ain-fin
  data_files:
  - split: test
    path: data/test/tatoeba-test.ain-fin.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-ber
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-ber.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ara-ber.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-deu.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ara-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-ell
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-ell.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ara-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-epo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ara-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ara-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-heb
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-heb.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ara-heb.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-kab
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-kab.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ara-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ara-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.ara-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ara-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: asm-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.asm-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.asm-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: avk-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.avk-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.avk-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: avk-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.avk-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: awa-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.awa-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: aze-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.aze-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.aze-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: aze-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.aze-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: aze-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.aze-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.aze-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.bel-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.bel-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.bel-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: bel-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.bel-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: ben-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.ben-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ben-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: ber-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.ber-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: ber-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.ber-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ber-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: ber-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.ber-epo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ber-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: ber-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.ber-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ber-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: ber-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.ber-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ber-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: bre-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.bre-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: bre-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.bre-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.bre-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: bua-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.bua-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: bub-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.bub-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-bul
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-bul.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.bul-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.bul-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.bul-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: bul-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.bul-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: cat-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.cat-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: cat-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.cat-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.cat-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: cat-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.cat-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: cat-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.cat-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: cat-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.cat-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: cat-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.cat-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: cat-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.cat-por.tsv
  sep: "\t"
  quoting: 3
- config_name: cat-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.cat-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.cat-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: cat-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.cat-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: cbk-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.cbk-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.cbk-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: ceb-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.ceb-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: ceb-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.ceb-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-deu.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ces-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ces-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-epo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ces-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-hun
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-hun.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ces-hun.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ces-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-slv
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-slv.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ces-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: ces-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.ces-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ces-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: cha-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.cha-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: chm-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.chm-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.chm-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: chv-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.chv-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: chv-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.chv-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: chv-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.chv-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: cor-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.cor-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: cor-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.cor-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.cor-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: cor-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.cor-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: cor-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.cor-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: cor-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.cor-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: cor-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.cor-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: cor-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.cor-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: crh-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.crh-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: cym-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.cym-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-dan
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-dan.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-deu.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-epo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-fin
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-fin.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-fin.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-hun
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-hun.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-nor.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-por.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dan-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: dan-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.dan-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-deu
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-deu.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-deu.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-dsb
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-dsb.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-ell
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-ell.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-ell.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-epo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-est
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-est.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-eus
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-eus.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-fas
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-fas.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-fas.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-fin
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-fin.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-fin.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-frr
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-frr.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-gos
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-gos.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-hbs
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-hbs.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-hbs.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-heb
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-heb.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-heb.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-hrx
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-hrx.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-hsb
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-hsb.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-hun
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-hun.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-hun.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-ido
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-ido.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-ido.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-ile
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-ile.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-ile.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-ina
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-ina.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-ina.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-isl
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-isl.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-jbo
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-jbo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-jbo.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-jpn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-kab
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-kab.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-kor
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-kor.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-kur
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-kur.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-lad
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-lad.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-lad.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-lat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-lav
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-lav.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-lfn
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-lfn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-lit
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-lit.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-lit.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-ltz
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-ltz.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-nds
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-nds.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-nds.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-nor.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-pol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-por.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-ron
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-ron.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-ron.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-run
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-run.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-run.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-slv
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-slv.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-swg
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-swg.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-swg.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-tat
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-tat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-tat.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-tgl
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-tgl.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-tlh.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-toki.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-tok.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-vol
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-vol.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.deu-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.deu-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: dsb-hsb
  data_files:
  - split: test
    path: data/test/tatoeba-test.dsb-hsb.tsv
  sep: "\t"
  quoting: 3
- config_name: dsb-slv
  data_files:
  - split: test
    path: data/test/tatoeba-test.dsb-slv.tsv
  sep: "\t"
  quoting: 3
- config_name: dtp-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.dtp-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.dtp-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: dtp-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.dtp-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: dtp-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.dtp-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: dtp-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.dtp-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: egl-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.egl-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-ell
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-ell.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ell-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ell-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ell-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ell-por.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ell-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ell-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: ell-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.ell-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ell-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-eng
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-eng.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-eng.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-epo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-est
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-est.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-est.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-eus
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-eus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-eus.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-fao
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-fao.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-fas
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-fas.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-fas.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-fin
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-fin.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-fin.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-fry
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-fry.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-gla
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-gla.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-gle
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-gle.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-gle.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-glg
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-glg.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-gos
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-gos.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-gos.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-got
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-got.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-grc
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-grc.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-gsw
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-gsw.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-hau
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-hau.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-hbs
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-hbs.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-hbs.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-heb
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-heb.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-heb.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-hin
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-hin.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-hin.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-hoc
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-hoc.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-hrx
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-hrx.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-hun
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-hun.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-hun.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-hye
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-hye.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-hye.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-ido
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-ido.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-ido.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-ile
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-ile.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-ile.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-ilo
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-ilo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-ilo.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-ina
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-ina.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-ina.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-isl
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-isl.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-isl.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-jav
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-jav.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-jbo
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-jbo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-jbo.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-jpn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-kab
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-kab.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-kab.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-kat
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-kat.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-kaz
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-kaz.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-kha
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-kha.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-kha.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-khm
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-khm.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-kor
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-kor.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-kor.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-kur
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-kur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-kur.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-kzj
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-kzj.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-lad
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-lad.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-lad.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-lat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-lav
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-lav.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-lav.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-lfn
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-lfn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-lit
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-lit.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-lit.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-ltz
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-ltz.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-mal
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-mal.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-mar
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-mar.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-mar.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-mkd
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-mkd.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-mkd.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-mlt
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-mlt.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-mon
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-mon.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-mon.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-mri
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-mri.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-msa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-mya
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-mya.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-nds
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-nds.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-nds.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-nor.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-nov
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-nov.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-nst
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-nst.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-oci
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-oci.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-orv
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-orv.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-ota
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-ota.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-pam
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-pam.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-pam.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-pmn
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-pmn.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-pms
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-pms.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-pol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-por.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-prg
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-prg.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-que
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-que.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-rom
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-rom.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-ron
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-ron.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-ron.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-run
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-run.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-slv
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-slv.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-slv.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-sqi
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-sqi.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-swa
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-swa.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tam
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tam.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tat
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-tat.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tel
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tel.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tgl
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tgl.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-tgl.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tha
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tha.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tlh.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-toki.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tok.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tuk
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tuk.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-tuk.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-tzl
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-tzl.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-tzl.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-uig
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-uig.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-uig.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-urd
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-urd.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-uzb
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-uzb.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-vie.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-vol
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-vol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-vol.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-war
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-war.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-war.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-xal
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-xal.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eng-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-zza
  data_files:
  - split: test
    path: data/test/tatoeba-test.eng-zza.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-epo
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-epo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-fas
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-fas.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-fas.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-fin
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-fin.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-fin.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-glg
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-glg.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-hbs
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-hbs.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-hbs.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-heb
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-heb.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-heb.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-hun
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-hun.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-hun.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-ido
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-ido.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-ido.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-ile
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-ile.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-ile.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-ina
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-ina.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-ina.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-isl
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-isl.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-jbo
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-jbo.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-jbo.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-jpn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-lad
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-lad.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-lad.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-lat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-lfn
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-lfn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-lit
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-lit.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-lit.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-nds
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-nds.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-nds.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-nor.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-oci
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-oci.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-pol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-por.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-ron
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-ron.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-ron.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-slv
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-slv.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-tgl
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-tgl.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-tgl.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-tlh.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-toki.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-tok.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-vol
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-vol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-vol.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: epo-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.epo-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.epo-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: est-fin
  data_files:
  - split: test
    path: data/test/tatoeba-test.est-fin.tsv
  sep: "\t"
  quoting: 3
- config_name: est-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.est-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: eus-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.eus-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: eus-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.eus-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: eus-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.eus-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.eus-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: fas-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.fas-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-fin
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-fin.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fin-fin.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-fkv
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-fkv.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fin-fkv.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fin-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-heb
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-heb.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-hun
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-hun.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fin-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-jpn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fin-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-kor
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-kor.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-kur
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-kur.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-nor.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fin-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-por.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fin-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fin-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fin-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: fin-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.fin-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-fra
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-fra.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-fra.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-gcf
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-gcf.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-hbs
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-hbs.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-heb
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-heb.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-heb.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-hun
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-hun.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-hun.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-ido
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-ido.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-ido.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-ile
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-ile.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-ina
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-ina.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-ina.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-jbo
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-jbo.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-jpn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-kab
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-kab.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-kab.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-kor
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-kor.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-lat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-lfn
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-lfn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-nds
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-nds.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-oci
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-oci.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-pcd
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-pcd.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-pol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-por.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-ron
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-ron.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-ron.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-run
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-run.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-slv
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-slv.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-tat
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-tat.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-tgl
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-tgl.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-toki.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-tok.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-uig
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-uig.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.fra-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.fra-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: fry-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.fry-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: gcf-gcf
  data_files:
  - split: test
    path: data/test/tatoeba-test.gcf-gcf.tsv
  sep: "\t"
  quoting: 3
- config_name: gla-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.gla-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: glg-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.glg-por.tsv
  sep: "\t"
  quoting: 3
- config_name: glg-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.glg-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.glg-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: gos-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.gos-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.gos-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: grn-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.grn-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.grn-por.tsv
  sep: "\t"
  quoting: 3
- config_name: grn-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.grn-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.grn-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: hbs-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.hbs-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: hbs-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.hbs-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: hbs-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.hbs-nor.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hbs-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: hbs-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.hbs-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: hbs-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.hbs-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hbs-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: hbs-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.hbs-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: hbs-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.hbs-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: hbs-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.hbs-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: hbs-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.hbs-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-heb
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-heb.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-heb.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-hun
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-hun.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-ina
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-ina.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-ina.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-lad
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-lad.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-lad.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-lat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-lfn
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-lfn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-pol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-por.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.heb-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: heb-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.heb-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: hin-mar
  data_files:
  - split: test
    path: data/test/tatoeba-test.hin-mar.tsv
  sep: "\t"
  quoting: 3
- config_name: hin-urd
  data_files:
  - split: test
    path: data/test/tatoeba-test.hin-urd.tsv
  sep: "\t"
  quoting: 3
- config_name: hin-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.hin-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: hoc-sat
  data_files:
  - split: test
    path: data/test/tatoeba-test.hoc-sat.tsv
  sep: "\t"
  quoting: 3
- config_name: hsb-slv
  data_files:
  - split: test
    path: data/test/tatoeba-test.hsb-slv.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-hun
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-hun.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hun-hun.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hun-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-jpn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hun-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-kor
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-kor.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hun-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-pol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hun-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hun-por.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hun-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hun-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.hun-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: hun-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.hun-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: hye-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.hye-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: ido-ina
  data_files:
  - split: test
    path: data/test/tatoeba-test.ido-ina.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ido-ina.tsv
  sep: "\t"
  quoting: 3
- config_name: ido-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.ido-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ido-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: ido-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.ido-lat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ido-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: ido-lfn
  data_files:
  - split: test
    path: data/test/tatoeba-test.ido-lfn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ido-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: ido-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.ido-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: ido-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.ido-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ido-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-lad
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-lad.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ina-lad.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-lat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ina-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-lfn
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-lfn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ina-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ina-por.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ina-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ina-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-tlh.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ina-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: ina-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.ina-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ina-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: isl-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.isl-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: isl-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.isl-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: isl-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.isl-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: isl-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.isl-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-ita
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-ita.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-ita.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-jpn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-lat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-lij
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-lij.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-lit
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-lit.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-nds
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-nds.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-pms
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-pms.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-pol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-por.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-ron
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-ron.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: ita-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.ita-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ita-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: jav-jav
  data_files:
  - split: test
    path: data/test/tatoeba-test.jav-jav.tsv
  sep: "\t"
  quoting: 3
- config_name: jav-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.jav-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: jbo-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.jbo-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: jbo-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.jbo-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: jbo-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.jbo-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: jbo-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.jbo-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: jbo-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.jbo-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jbo-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-jpn
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-jpn.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-kor
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-kor.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-lit
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-lit.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-mar
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-mar.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-msa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-nds
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-nds.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-nds.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-pol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-por.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-vie.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: jpn-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.jpn-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.jpn-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: kab-kab
  data_files:
  - split: test
    path: data/test/tatoeba-test.kab-kab.tsv
  - split: dev
    path: data/dev/tatoeba-dev.kab-kab.tsv
  sep: "\t"
  quoting: 3
- config_name: kab-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.kab-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: kab-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.kab-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.kab-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: kat-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.kat-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: kaz-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.kaz-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.kaz-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: khm-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.khm-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: kor-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.kor-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: kor-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.kor-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: kor-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.kor-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: kur-kur
  data_files:
  - split: test
    path: data/test/tatoeba-test.kur-kur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.kur-kur.tsv
  sep: "\t"
  quoting: 3
- config_name: kur-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.kur-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: kzj-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.kzj-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: lad-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.lad-lat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lad-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: lad-lfn
  data_files:
  - split: test
    path: data/test/tatoeba-test.lad-lfn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lad-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: lad-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.lad-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lad-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: lad-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.lad-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lad-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-lat
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-lat.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-lfn
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-lfn.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lat-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lat-por.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lat-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lat-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-tlh.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lat-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: lat-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.lat-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lat-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: lav-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.lav-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: lfn-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.lfn-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lfn-por.tsv
  sep: "\t"
  quoting: 3
- config_name: lfn-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.lfn-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lfn-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: lfn-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.lfn-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lfn-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: lfn-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.lfn-tlh.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lfn-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: lfn-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.lfn-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lfn-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: lfn-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.lfn-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lfn-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: lit-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.lit-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: lit-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.lit-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.lit-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: lit-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.lit-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: lit-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.lit-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: ltz-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.ltz-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: mkd-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.mkd-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: msa-msa
  data_files:
  - split: test
    path: data/test/tatoeba-test.msa-msa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.msa-msa.tsv
  sep: "\t"
  quoting: 3
- config_name: msa-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.msa-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: msa-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.msa-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: nds-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.nds-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nds-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: nds-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.nds-por.tsv
  sep: "\t"
  quoting: 3
- config_name: nds-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.nds-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nds-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: nds-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.nds-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-nld
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-nld.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-nld.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-pol.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-por.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-ron
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-ron.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-ron.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: nld-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.nld-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nld-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: nor-nor
  data_files:
  - split: test
    path: data/test/tatoeba-test.nor-nor.tsv
  - split: dev
    path: data/dev/tatoeba-dev.nor-nor.tsv
  sep: "\t"
  quoting: 3
- config_name: nor-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.nor-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: nor-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.nor-por.tsv
  sep: "\t"
  quoting: 3
- config_name: nor-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.nor-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: nor-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.nor-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: nor-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.nor-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: nor-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.nor-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: nor-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.nor-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: orv-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.orv-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: oss-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.oss-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: ota-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.ota-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ota-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-pol
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-pol.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-por.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-ron
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-ron.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.pol-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.pol-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.pol-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.pol-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: pol-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.pol-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: por-por
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-por.tsv
  - split: dev
    path: data/dev/tatoeba-dev.por-por.tsv
  sep: "\t"
  quoting: 3
- config_name: por-ron
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-ron.tsv
  - split: dev
    path: data/dev/tatoeba-dev.por-ron.tsv
  sep: "\t"
  quoting: 3
- config_name: por-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.por-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: por-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.por-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: por-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: por-tgl
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-tgl.tsv
  sep: "\t"
  quoting: 3
- config_name: por-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-toki.tsv
  - split: dev
    path: data/dev/tatoeba-dev.por-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: por-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-tok.tsv
  - split: dev
    path: data/dev/tatoeba-dev.por-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: por-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.por-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: por-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.por-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: por-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.por-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: por-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.por-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: ron-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.ron-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: ron-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.ron-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ron-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: ron-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.ron-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.ron-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: run-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.run-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: run-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.run-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-rus
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-rus.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-rus.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-sah
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-sah.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-slv
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-slv.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-slv.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-tat
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-tat.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-tat.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-toki.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-tok.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-uig
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-uig.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-xal
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-xal.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: rus-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.rus-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.rus-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: slv-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.slv-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.slv-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: slv-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.slv-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-spa
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-spa.tsv
  - split: dev
    path: data/dev/tatoeba-dev.spa-spa.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-swe.tsv
  - split: dev
    path: data/dev/tatoeba-dev.spa-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-tat
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-tat.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-tgl
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-tgl.tsv
  - split: dev
    path: data/dev/tatoeba-dev.spa-tgl.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-tlh
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-toki
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-toki.tsv
  - split: dev
    path: data/dev/tatoeba-dev.spa-toki.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-tok.tsv
  - split: dev
    path: data/dev/tatoeba-dev.spa-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.spa-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.spa-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.spa-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: spa-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.spa-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.spa-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: swe-swe
  data_files:
  - split: test
    path: data/test/tatoeba-test.swe-swe.tsv
  sep: "\t"
  quoting: 3
- config_name: swe-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.swe-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: swe-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.swe-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: tat-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.tat-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: tat-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.tat-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: tlh-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.tlh-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.tlh-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: tlh-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.tlh-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: tok-tok
  data_files:
  - split: test
    path: data/test/tatoeba-test.tok-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: tok-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.tok-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: tur-tur
  data_files:
  - split: test
    path: data/test/tatoeba-test.tur-tur.tsv
  - split: dev
    path: data/dev/tatoeba-dev.tur-tur.tsv
  sep: "\t"
  quoting: 3
- config_name: tur-uig
  data_files:
  - split: test
    path: data/test/tatoeba-test.tur-uig.tsv
  - split: dev
    path: data/dev/tatoeba-dev.tur-uig.tsv
  sep: "\t"
  quoting: 3
- config_name: tur-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.tur-ukr.tsv
  - split: dev
    path: data/dev/tatoeba-dev.tur-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: tur-uzb
  data_files:
  - split: test
    path: data/test/tatoeba-test.tur-uzb.tsv
  sep: "\t"
  quoting: 3
- config_name: tur-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.tur-yid.tsv
  - split: dev
    path: data/dev/tatoeba-dev.tur-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: tur-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.tur-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: uig-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.uig-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: ukr-ukr
  data_files:
  - split: test
    path: data/test/tatoeba-test.ukr-ukr.tsv
  sep: "\t"
  quoting: 3
- config_name: ukr-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.ukr-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: vie-vie
  data_files:
  - split: test
    path: data/test/tatoeba-test.vie-vie.tsv
  sep: "\t"
  quoting: 3
- config_name: vie-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.vie-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: yid-yid
  data_files:
  - split: test
    path: data/test/tatoeba-test.yid-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: zho-zho
  data_files:
  - split: test
    path: data/test/tatoeba-test.zho-zho.tsv
  - split: dev
    path: data/dev/tatoeba-dev.zho-zho.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-lad
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.ara-lad.tsv
  sep: "\t"
  quoting: 3
- config_name: ara-yid
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.ara-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: bzt-epo
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.bzt-epo.tsv
  sep: "\t"
  quoting: 3
- config_name: bzt-lfn
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.bzt-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: bzt-yid
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.bzt-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: deu-gsw
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.deu-gsw.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-grn
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.eng-grn.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-lao
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.eng-lao.tsv
  sep: "\t"
  quoting: 3
- config_name: eng-xho
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.eng-xho.tsv
  sep: "\t"
  quoting: 3
- config_name: enm-fin
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.enm-fin.tsv
  sep: "\t"
  quoting: 3
- config_name: fra-lad
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.fra-lad.tsv
  sep: "\t"
  quoting: 3
- config_name: ido-ile
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.ido-ile.tsv
  sep: "\t"
  quoting: 3
- config_name: ile-ina
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.ile-ina.tsv
  sep: "\t"
  quoting: 3
- config_name: ile-lfn
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.ile-lfn.tsv
  sep: "\t"
  quoting: 3
- config_name: ile-yid
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.ile-yid.tsv
  sep: "\t"
  quoting: 3
- config_name: lad-tlh
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.lad-tlh.tsv
  sep: "\t"
  quoting: 3
- config_name: lfn-tok
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.lfn-tok.tsv
  sep: "\t"
  quoting: 3
- config_name: lfn-toki
  data_files:
  - split: dev
    path: data/dev/tatoeba-dev.lfn-toki.tsv
  sep: "\t"
  quoting: 3
extra_gated_fields:
  This data is for evaluation purposes only; You may not use any of this data or its derivatives for training machine learning / AI models: checkbox
  You may only distribute, embed, or otherwise transfer this data or its derivatives via a mechanism that is either private or that implements protections against automated crawling (such as using a password-protected archive or a gating mechanism that requires users to accept these terms before accessing the dataset): checkbox
  Your distributions must retain these terms: checkbox
---

# Dataset Card for The Tatoeba Translation Challenge

**Please note that this dataset is intended strictly for evaluation and benchmarking purposes. Training models on this dataset, or including it in automatically collected web-scale training corpora, may lead to benchmark contamination and invalidate evaluation results.**

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
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
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/Helsinki-NLP/Tatoeba-Challenge/
- **Repository:** https://github.com/Helsinki-NLP/Tatoeba-Challenge/
- **Paper:** [The Tatoeba Translation Challenge – Realistic Data Sets for Low Resource and Multilingual MT](https://aclanthology.org/2020.wmt-1.139/)
- **Leaderboard:**
- **Point of Contact:** [Jörg Tiedemann](mailto:jorg.tiedemann@helsinki.fi)

### Dataset Summary

The Tatoeba Translation Challenge is a multilingual data set of machine translation benchmarks derived from user-contributed translations collected by [Tatoeba.org](https://tatoeba.org/) and provided as parallel corpus from [OPUS](https://opus.nlpl.eu/). This dataset includes test and development data sorted by language pair. It includes test sets for hundreds of language pairs and is continuously updated. Please, check the version number tag to refer to the release that your are using.

### Supported Tasks and Leaderboards

The translation task is described in detail in the [Tatoeba-Challenge repository](https://github.com/Helsinki-NLP/Tatoeba-Challenge) and covers various sub-tasks with different data coverage and resources. [Training data](https://github.com/Helsinki-NLP/Tatoeba-Challenge/blob/master/data/README.md) is also available from the same repository and [results](https://github.com/Helsinki-NLP/Tatoeba-Challenge/blob/master/results/tatoeba-results-all.md) are published and collected as well. [Models](https://github.com/Helsinki-NLP/Tatoeba-Challenge/blob/master/results/tatoeba-models-all.md) are also released for public use and are also partially available from the [huggingface model hub](https://huggingface.co/Helsinki-NLP).


### Languages

The data set covers hundreds of languages and language pairs and are organized by ISO-639-3 languages. The current release covers the following languages:
Afrikaans, Ainu (Japan), Arabic, Assamese, Kotava, Awadhi, Azerbaijani, Belarusian, Bengali, Berber languages, Breton, Buriat, Bua, Bulgarian, Brithenig, Catalan, Chavacano, Cebuano, Czech, Chamorro, Mari (Russia), Chuvash, Cornish, Crimean Tatar, Welsh, Danish, German, Lower Sorbian, Kadazan Dusun, Emilian, Modern Greek (1453-), English, Middle English (1100-1500), Esperanto, Estonian, Basque, Faroese, Persian, Finnish, Kven Finnish, French, Northern Frisian, Western Frisian, Guadeloupean Creole French, Scottish Gaelic, Irish, Galician, Gronings, Gothic, Ancient Greek (to 1453), Guarani, Swiss German, Hausa, Serbo-Croatian, Hebrew, Hindi, Ho, Hunsrik, Upper Sorbian, Hungarian, Armenian, Ido, Interlingue, Iloko, Interlingua (International Auxiliary Language Association), Icelandic, Italian, Javanese, Lojban, Japanese, Kabyle, Georgian, Kazakh, Khasi, Khmer, Korean, Kurdish, Coastal Kadazan, Ladino, Lao, Latin, Latvian, Lingua Franca Nova, Ligurian, Lithuanian, Luxembourgish, Malayalam, Marathi, Macedonian, Maltese, Mongolian, Maori, Malay (macrolanguage), Burmese, Low German, Dutch, Norwegian, Novial, Tase Naga, Occitan (post 1500), Old Russian, Ossetian, Ottoman Turkish (1500-1928), Pampanga, Picard, Pam, Piemontese, Polish, Portuguese, Prussian, Quechua, Romany, Romanian, Rundi, Russian, Yakut, Santali, Slovenian, Spanish, Albanian, Swahili (macrolanguage), Swedish, Swabian, Tamil, Tatar, Telugu, Tagalog, Thai, Klingon, Toki Pona, Turkmen, Turkish, Talossan, Uighur, Ukrainian, Urdu, Uzbek, Vietnamese, Volapük, Waray (Philippines), Kalmyk, Xhosa, Yiddish, Chinese, Zaza

## Dataset Structure

### Data Instances

Data instances are given as translation units in TAB-separated files with four columns: source and target language ISO-639-3 codes, source language text and target language text. Note that we do not imply a translation direction and consider the data set to be symmetric and to be used as a test set in both directions. Language-pair-specific subsets are only provided under the label of one direction using sorted ISO-639-3 language IDs.

Some subsets contain several sub-languages or language variants. They may refer to macro-languages such as Serbo-Croatian languages that are covered by the ISO code `hbs`. Language variants may also include different writing systems and in that case the ISO15924 script codes are attached to the language codes. Here are a few examples from the English to Serbo-Croation test set including examples for Bosnian, Croatian and Serbian in Cyrillic and in Latin scripts:

```
eng	bos_Latn	Children are the flowers of our lives.	Djeca su cvijeće našeg života.
eng	hrv	A bird was flying high up in the sky.	Ptica je visoko letjela nebom.
eng	srp_Cyrl	A bird in the hand is worth two in the bush.	Боље врабац у руци, него голуб на грани.
eng	srp_Latn	Canada is the motherland of ice hockey.	Kanada je zemlja-majka hokeja na ledu.
```

There are also data sets with sentence pairs in the same language. In most cases, those are variants with minor spelling differences but they also include rephrased sentences. Here are a few examples from the English test set:

```
eng     eng     All of us got into the car.     We all got in the car.
eng     eng     All of us hope that doesn't happen.     All of us hope that that doesn't happen.
eng     eng     All the seats are booked.       The seats are all sold out.
```


### Data Splits

Test and development data sets are disjoint with respect to sentence pairs but may include overlaps in individual source or target language sentences. Development data should not be used in training directly. The goal of the data splits is to create test sets of reasonable size with a large language coverage. Test sets include at most 10,000 instances. Development data do not exist for all language pairs.

To be comparable with other results, models should use the training data distributed from the [Tatoeba MT Challenge Repository](https://github.com/Helsinki-NLP/Tatoeba-Challenge/) including monolingual data sets also listed there.


## Dataset Creation

### Curation Rationale


The Tatoeba MT data set will be updated continuously and the data preparation procedures are also public and released on [github](https://github.com/Helsinki-NLP/Tatoeba-Challenge/). High language coverage is the main goal of the project and data sets are prepared to be consistent and systematic with standardized language labels and distribution formats.


### Source Data

#### Initial Data Collection and Normalization

The Tatoeba data sets are collected from user-contributed translations submitted to [Tatoeba.org](https://tatoeba.org/) and compiled into a multi-parallel corpus in [OPUS](https://opus.nlpl.eu/Tatoeba.php). The test and development sets are incrementally updated with new releases of the Tatoeba data collection at OPUS. New releases extend the existing data sets. Test sets should not overlap with any of the released development data sets.


#### Who are the source language producers?

The data sets come from [Tatoeba.org](https://tatoeba.org/), which provides a large database of sentences and their translations into a wide varity of languages. Its content is constantly growing as a result of voluntary contributions of thousands of users.
The original project was founded by Trang Ho in 2006, hosted on Sourceforge under the codename of multilangdict. 


### Annotations

#### Annotation process

Sentences are translated by volunteers and the Tatoeba database also provides additional metadata about each record including user ratings etc. However, the metadata is currently not used in any way for the compilation of the MT benchmark. Language skills of contributors naturally vary quite a bit and not all translations are done by native speakers of the target language. More information about the contributions can be found at [Tatoeba.org](https://tatoeba.org/).


#### Who are the annotators?

### Personal and Sensitive Information

For information about handling personal and sensitive information we refer to the [original provider](https://tatoeba.org/) of the data. This data set has not been processed in any way to detect or remove potentially sensitve or personal information.

## Considerations for Using the Data

### Social Impact of Dataset

The language coverage is high and with that it represents a highly valuable resource for machine translation development especially for lesser resourced languages and language pairs. The constantly growing database also represents a dynamic resource and its value will grow further.


### Discussion of Biases

The original source lives from its contributors and there interest and background will to certain subjective and cultural biases. Language coverage and translation quality is also biased by the skills of the contributors.


### Other Known Limitations

The sentences are typically quite short and, therefore, rather easy to translate. For high-resource languages, this leads to results that will be less useful than more challenging benchmarks. For lesser resource language pairs, the limited complexity of the examples is actually a good thing to measure progress even in very challenging setups.


## Additional Information

### Dataset Curators

The data set is curated by the University of Helsinki and its [language technology research group](https://blogs.helsinki.fi/language-technology/). Data and tools used for creating and using the resource are [open source](https://github.com/Helsinki-NLP/Tatoeba-Challenge/) and will be maintained as part of the [OPUS ecosystem](https://opus.nlpl.eu/) for parallel data and machine translation research.


### Licensing Information

The data sets are distributed under the same licence agreement as the original Tatoeba database using a
[CC-BY 2.0 license](https://creativecommons.org/licenses/by/2.0/fr/). More information about the terms of use of the original data sets is listed [here](https://tatoeba.org/eng/terms_of_use).


### Citation Information

If you use the data sets then, please, cite the following paper: [The Tatoeba Translation Challenge – Realistic Data Sets for Low Resource and Multilingual MT](https://aclanthology.org/2020.wmt-1.139/)

```
@inproceedings{tiedemann-2020-tatoeba,
    title = "The Tatoeba Translation Challenge {--} Realistic Data Sets for Low Resource and Multilingual {MT}",
    author = {Tiedemann, J{\"o}rg},
    booktitle = "Proceedings of the Fifth Conference on Machine Translation",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.wmt-1.139",
    pages = "1174--1182",
}
```

### Contributions

Thanks to [@jorgtied](https://github.com/jorgtied) and [@Helsinki-NLP](https://github.com/Helsinki-NLP) for adding this dataset.
Thanks also to [CSC Finland](https://www.csc.fi/en/solutions-for-research) for providing computational resources and storage space for the work on OPUS and other MT projects.
