---
license: cc0-1.0
task_categories:
  - text-to-speech
language:
  - ab
  - af
  - am
  - ar
  - as
  - ast
  - az
  - ba
  - bas
  - be
  - bg
  - bn
  - br
  - ca
  - ckb
  - cnh
  - cs
  - cv
  - cy
  - da
  - dav
  - de
  - dv
  - dyu
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gl
  - gn
  - ha
  - he
  - hi
  - hsb
  - ht
  - hu
  - hy
  - ia
  - id
  - ig
  - is
  - it
  - ja
  - ka
  - kab
  - kk
  - kln
  - kmr
  - ko
  - ky
  - lg
  - lij
  - lo
  - lt
  - ltg
  - luo
  - lv
  - mdf
  - mhr
  - mk
  - ml
  - mn
  - mr
  - mrj
  - mt
  - myv
  - nan
  - nb
  - ne
  - nhi
  - nl
  - nn
  - nr
  - nso
  - oc
  - or
  - os
  - pa
  - pl
  - ps
  - pt
  - quy
  - rm
  - ro
  - ru
  - rup
  - rw
  - sah
  - sat
  - sc
  - sd
  - sk
  - skr
  - sl
  - sq
  - sr
  - st
  - sv
  - sw
  - ta
  - te
  - tg
  - th
  - ti
  - tig
  - tk
  - tn
  - tok
  - tr
  - ts
  - tt
  - tw
  - ug
  - uk
  - ur
  - uz
  - ve
  - vi
  - vot
  - xh
  - yi
  - yo
  - yue
  - zgh
  - zh
  - zu
  - zza
language_bcp47:
  - fy-NL
  - ga-IE
  - hy-AM
  - nan-TW
  - nb-NO
  - ne-NP
  - nn-NO
  - pa-IN
  - rm-sursilv
  - rm-vallader
  - sv-SE
  - zh-CN
  - zh-HK
  - zh-TW
extra_gated_prompt: >-
  You agree to not attempt to determine the identity of speakers in the Common Voice dataset.
tags:
  - speech
  - common-voice
  - sidon
size_categories:
  - 1M<n<10M
configs:
  - config_name: ab
    data_files:
      - split: invalidated
        path: ab/invalidated-*.tar.gz
      - split: other
        path: ab/other-*.tar.gz
      - split: test
        path: ab/test-*.tar.gz
      - split: train
        path: ab/train-*.tar.gz
      - split: validation
        path: ab/validation-*.tar.gz
  - config_name: af
    data_files:
      - split: invalidated
        path: af/invalidated-*.tar.gz
      - split: other
        path: af/other-*.tar.gz
      - split: test
        path: af/test-*.tar.gz
      - split: train
        path: af/train-*.tar.gz
      - split: validation
        path: af/validation-*.tar.gz
  - config_name: am
    data_files:
      - split: invalidated
        path: am/invalidated-*.tar.gz
      - split: other
        path: am/other-*.tar.gz
      - split: test
        path: am/test-*.tar.gz
      - split: train
        path: am/train-*.tar.gz
      - split: validation
        path: am/validation-*.tar.gz
  - config_name: ar
    data_files:
      - split: invalidated
        path: ar/invalidated-*.tar.gz
      - split: other
        path: ar/other-*.tar.gz
      - split: test
        path: ar/test-*.tar.gz
      - split: train
        path: ar/train-*.tar.gz
      - split: validation
        path: ar/validation-*.tar.gz
  - config_name: as
    data_files:
      - split: invalidated
        path: as/invalidated-*.tar.gz
      - split: other
        path: as/other-*.tar.gz
      - split: test
        path: as/test-*.tar.gz
      - split: train
        path: as/train-*.tar.gz
      - split: validation
        path: as/validation-*.tar.gz
  - config_name: ast
    data_files:
      - split: invalidated
        path: ast/invalidated-*.tar.gz
      - split: other
        path: ast/other-*.tar.gz
      - split: test
        path: ast/test-*.tar.gz
      - split: train
        path: ast/train-*.tar.gz
      - split: validation
        path: ast/validation-*.tar.gz
  - config_name: az
    data_files:
      - split: invalidated
        path: az/invalidated-*.tar.gz
      - split: other
        path: az/other-*.tar.gz
      - split: test
        path: az/test-*.tar.gz
      - split: train
        path: az/train-*.tar.gz
      - split: validation
        path: az/validation-*.tar.gz
  - config_name: ba
    data_files:
      - split: invalidated
        path: ba/invalidated-*.tar.gz
      - split: other
        path: ba/other-*.tar.gz
      - split: test
        path: ba/test-*.tar.gz
      - split: train
        path: ba/train-*.tar.gz
      - split: validation
        path: ba/validation-*.tar.gz
  - config_name: bas
    data_files:
      - split: invalidated
        path: bas/invalidated-*.tar.gz
      - split: other
        path: bas/other-*.tar.gz
      - split: test
        path: bas/test-*.tar.gz
      - split: train
        path: bas/train-*.tar.gz
      - split: validation
        path: bas/validation-*.tar.gz
  - config_name: be
    data_files:
      - split: invalidated
        path: be/invalidated-*.tar.gz
      - split: other
        path: be/other-*.tar.gz
      - split: test
        path: be/test-*.tar.gz
      - split: train
        path: be/train-*.tar.gz
      - split: validation
        path: be/validation-*.tar.gz
  - config_name: bg
    data_files:
      - split: invalidated
        path: bg/invalidated-*.tar.gz
      - split: other
        path: bg/other-*.tar.gz
      - split: test
        path: bg/test-*.tar.gz
      - split: train
        path: bg/train-*.tar.gz
      - split: validation
        path: bg/validation-*.tar.gz
  - config_name: bn
    data_files:
      - split: invalidated
        path: bn/invalidated-*.tar.gz
      - split: other
        path: bn/other-*.tar.gz
      - split: test
        path: bn/test-*.tar.gz
      - split: train
        path: bn/train-*.tar.gz
      - split: validation
        path: bn/validation-*.tar.gz
  - config_name: br
    data_files:
      - split: invalidated
        path: br/invalidated-*.tar.gz
      - split: other
        path: br/other-*.tar.gz
      - split: test
        path: br/test-*.tar.gz
      - split: train
        path: br/train-*.tar.gz
      - split: validation
        path: br/validation-*.tar.gz
  - config_name: ca
    data_files:
      - split: invalidated
        path: ca/invalidated-*.tar.gz
      - split: other
        path: ca/other-*.tar.gz
      - split: test
        path: ca/test-*.tar.gz
      - split: train
        path: ca/train-*.tar.gz
      - split: validation
        path: ca/validation-*.tar.gz
  - config_name: ckb
    data_files:
      - split: invalidated
        path: ckb/invalidated-*.tar.gz
      - split: other
        path: ckb/other-*.tar.gz
      - split: test
        path: ckb/test-*.tar.gz
      - split: train
        path: ckb/train-*.tar.gz
      - split: validation
        path: ckb/validation-*.tar.gz
  - config_name: cnh
    data_files:
      - split: invalidated
        path: cnh/invalidated-*.tar.gz
      - split: other
        path: cnh/other-*.tar.gz
      - split: test
        path: cnh/test-*.tar.gz
      - split: train
        path: cnh/train-*.tar.gz
      - split: validation
        path: cnh/validation-*.tar.gz
  - config_name: cs
    data_files:
      - split: invalidated
        path: cs/invalidated-*.tar.gz
      - split: other
        path: cs/other-*.tar.gz
      - split: test
        path: cs/test-*.tar.gz
      - split: train
        path: cs/train-*.tar.gz
      - split: validation
        path: cs/validation-*.tar.gz
  - config_name: cv
    data_files:
      - split: invalidated
        path: cv/invalidated-*.tar.gz
      - split: other
        path: cv/other-*.tar.gz
      - split: test
        path: cv/test-*.tar.gz
      - split: train
        path: cv/train-*.tar.gz
      - split: validation
        path: cv/validation-*.tar.gz
  - config_name: cy
    data_files:
      - split: invalidated
        path: cy/invalidated-*.tar.gz
      - split: other
        path: cy/other-*.tar.gz
      - split: test
        path: cy/test-*.tar.gz
      - split: train
        path: cy/train-*.tar.gz
      - split: validation
        path: cy/validation-*.tar.gz
  - config_name: da
    data_files:
      - split: invalidated
        path: da/invalidated-*.tar.gz
      - split: other
        path: da/other-*.tar.gz
      - split: test
        path: da/test-*.tar.gz
      - split: train
        path: da/train-*.tar.gz
      - split: validation
        path: da/validation-*.tar.gz
  - config_name: dav
    data_files:
      - split: invalidated
        path: dav/invalidated-*.tar.gz
      - split: other
        path: dav/other-*.tar.gz
      - split: test
        path: dav/test-*.tar.gz
      - split: train
        path: dav/train-*.tar.gz
      - split: validation
        path: dav/validation-*.tar.gz
  - config_name: de
    data_files:
      - split: invalidated
        path: de/invalidated-*.tar.gz
      - split: other
        path: de/other-*.tar.gz
      - split: test
        path: de/test-*.tar.gz
      - split: train
        path: de/train-*.tar.gz
      - split: validation
        path: de/validation-*.tar.gz
  - config_name: dv
    data_files:
      - split: invalidated
        path: dv/invalidated-*.tar.gz
      - split: other
        path: dv/other-*.tar.gz
      - split: test
        path: dv/test-*.tar.gz
      - split: train
        path: dv/train-*.tar.gz
      - split: validation
        path: dv/validation-*.tar.gz
  - config_name: dyu
    data_files:
      - split: invalidated
        path: dyu/invalidated-*.tar.gz
      - split: other
        path: dyu/other-*.tar.gz
      - split: test
        path: dyu/test-*.tar.gz
      - split: train
        path: dyu/train-*.tar.gz
      - split: validation
        path: dyu/validation-*.tar.gz
  - config_name: el
    data_files:
      - split: invalidated
        path: el/invalidated-*.tar.gz
      - split: other
        path: el/other-*.tar.gz
      - split: test
        path: el/test-*.tar.gz
      - split: train
        path: el/train-*.tar.gz
      - split: validation
        path: el/validation-*.tar.gz
  - config_name: en
    data_files:
      - split: invalidated
        path: en/invalidated-*.tar.gz
      - split: other
        path: en/other-*.tar.gz
      - split: test
        path: en/test-*.tar.gz
      - split: train
        path: en/train-*.tar.gz
      - split: validation
        path: en/validation-*.tar.gz
  - config_name: eo
    data_files:
      - split: invalidated
        path: eo/invalidated-*.tar.gz
      - split: other
        path: eo/other-*.tar.gz
      - split: test
        path: eo/test-*.tar.gz
      - split: train
        path: eo/train-*.tar.gz
      - split: validation
        path: eo/validation-*.tar.gz
  - config_name: es
    data_files:
      - split: invalidated
        path: es/invalidated-*.tar.gz
      - split: other
        path: es/other-*.tar.gz
      - split: test
        path: es/test-*.tar.gz
      - split: train
        path: es/train-*.tar.gz
      - split: validation
        path: es/validation-*.tar.gz
  - config_name: et
    data_files:
      - split: invalidated
        path: et/invalidated-*.tar.gz
      - split: other
        path: et/other-*.tar.gz
      - split: test
        path: et/test-*.tar.gz
      - split: train
        path: et/train-*.tar.gz
      - split: validation
        path: et/validation-*.tar.gz
  - config_name: eu
    data_files:
      - split: invalidated
        path: eu/invalidated-*.tar.gz
      - split: other
        path: eu/other-*.tar.gz
      - split: test
        path: eu/test-*.tar.gz
      - split: train
        path: eu/train-*.tar.gz
      - split: validation
        path: eu/validation-*.tar.gz
  - config_name: fa
    data_files:
      - split: invalidated
        path: fa/invalidated-*.tar.gz
      - split: other
        path: fa/other-*.tar.gz
      - split: test
        path: fa/test-*.tar.gz
      - split: train
        path: fa/train-*.tar.gz
      - split: validation
        path: fa/validation-*.tar.gz
  - config_name: fi
    data_files:
      - split: invalidated
        path: fi/invalidated-*.tar.gz
      - split: other
        path: fi/other-*.tar.gz
      - split: test
        path: fi/test-*.tar.gz
      - split: train
        path: fi/train-*.tar.gz
      - split: validation
        path: fi/validation-*.tar.gz
  - config_name: fr
    data_files:
      - split: invalidated
        path: fr/invalidated-*.tar.gz
      - split: other
        path: fr/other-*.tar.gz
      - split: test
        path: fr/test-*.tar.gz
      - split: train
        path: fr/train-*.tar.gz
      - split: validation
        path: fr/validation-*.tar.gz
  - config_name: fy-NL
    data_files:
      - split: invalidated
        path: fy-NL/invalidated-*.tar.gz
      - split: other
        path: fy-NL/other-*.tar.gz
      - split: test
        path: fy-NL/test-*.tar.gz
      - split: train
        path: fy-NL/train-*.tar.gz
      - split: validation
        path: fy-NL/validation-*.tar.gz
  - config_name: ga-IE
    data_files:
      - split: invalidated
        path: ga-IE/invalidated-*.tar.gz
      - split: other
        path: ga-IE/other-*.tar.gz
      - split: test
        path: ga-IE/test-*.tar.gz
      - split: train
        path: ga-IE/train-*.tar.gz
      - split: validation
        path: ga-IE/validation-*.tar.gz
  - config_name: gl
    data_files:
      - split: invalidated
        path: gl/invalidated-*.tar.gz
      - split: other
        path: gl/other-*.tar.gz
      - split: test
        path: gl/test-*.tar.gz
      - split: train
        path: gl/train-*.tar.gz
      - split: validation
        path: gl/validation-*.tar.gz
  - config_name: gn
    data_files:
      - split: invalidated
        path: gn/invalidated-*.tar.gz
      - split: other
        path: gn/other-*.tar.gz
      - split: test
        path: gn/test-*.tar.gz
      - split: train
        path: gn/train-*.tar.gz
      - split: validation
        path: gn/validation-*.tar.gz
  - config_name: ha
    data_files:
      - split: invalidated
        path: ha/invalidated-*.tar.gz
      - split: other
        path: ha/other-*.tar.gz
      - split: test
        path: ha/test-*.tar.gz
      - split: train
        path: ha/train-*.tar.gz
      - split: validation
        path: ha/validation-*.tar.gz
  - config_name: he
    data_files:
      - split: invalidated
        path: he/invalidated-*.tar.gz
      - split: other
        path: he/other-*.tar.gz
      - split: test
        path: he/test-*.tar.gz
      - split: train
        path: he/train-*.tar.gz
      - split: validation
        path: he/validation-*.tar.gz
  - config_name: hi
    data_files:
      - split: invalidated
        path: hi/invalidated-*.tar.gz
      - split: other
        path: hi/other-*.tar.gz
      - split: test
        path: hi/test-*.tar.gz
      - split: train
        path: hi/train-*.tar.gz
      - split: validation
        path: hi/validation-*.tar.gz
  - config_name: hsb
    data_files:
      - split: invalidated
        path: hsb/invalidated-*.tar.gz
      - split: other
        path: hsb/other-*.tar.gz
      - split: test
        path: hsb/test-*.tar.gz
      - split: train
        path: hsb/train-*.tar.gz
      - split: validation
        path: hsb/validation-*.tar.gz
  - config_name: ht
    data_files:
      - split: other
        path: ht/other-*.tar.gz
      - split: test
        path: ht/test-*.tar.gz
      - split: train
        path: ht/train-*.tar.gz
      - split: validation
        path: ht/validation-*.tar.gz
  - config_name: hu
    data_files:
      - split: invalidated
        path: hu/invalidated-*.tar.gz
      - split: other
        path: hu/other-*.tar.gz
      - split: test
        path: hu/test-*.tar.gz
      - split: train
        path: hu/train-*.tar.gz
      - split: validation
        path: hu/validation-*.tar.gz
  - config_name: hy-AM
    data_files:
      - split: invalidated
        path: hy-AM/invalidated-*.tar.gz
      - split: other
        path: hy-AM/other-*.tar.gz
      - split: test
        path: hy-AM/test-*.tar.gz
      - split: train
        path: hy-AM/train-*.tar.gz
      - split: validation
        path: hy-AM/validation-*.tar.gz
  - config_name: ia
    data_files:
      - split: invalidated
        path: ia/invalidated-*.tar.gz
      - split: other
        path: ia/other-*.tar.gz
      - split: test
        path: ia/test-*.tar.gz
      - split: train
        path: ia/train-*.tar.gz
      - split: validation
        path: ia/validation-*.tar.gz
  - config_name: id
    data_files:
      - split: invalidated
        path: id/invalidated-*.tar.gz
      - split: other
        path: id/other-*.tar.gz
      - split: test
        path: id/test-*.tar.gz
      - split: train
        path: id/train-*.tar.gz
      - split: validation
        path: id/validation-*.tar.gz
  - config_name: ig
    data_files:
      - split: invalidated
        path: ig/invalidated-*.tar.gz
      - split: other
        path: ig/other-*.tar.gz
      - split: test
        path: ig/test-*.tar.gz
      - split: train
        path: ig/train-*.tar.gz
      - split: validation
        path: ig/validation-*.tar.gz
  - config_name: is
    data_files:
      - split: invalidated
        path: is/invalidated-*.tar.gz
      - split: other
        path: is/other-*.tar.gz
      - split: test
        path: is/test-*.tar.gz
      - split: train
        path: is/train-*.tar.gz
      - split: validation
        path: is/validation-*.tar.gz
  - config_name: it
    data_files:
      - split: invalidated
        path: it/invalidated-*.tar.gz
      - split: other
        path: it/other-*.tar.gz
      - split: test
        path: it/test-*.tar.gz
      - split: train
        path: it/train-*.tar.gz
      - split: validation
        path: it/validation-*.tar.gz
  - config_name: ja
    data_files:
      - split: invalidated
        path: ja/invalidated-*.tar.gz
      - split: other
        path: ja/other-*.tar.gz
      - split: test
        path: ja/test-*.tar.gz
      - split: train
        path: ja/train-*.tar.gz
      - split: validation
        path: ja/validation-*.tar.gz
  - config_name: ka
    data_files:
      - split: invalidated
        path: ka/invalidated-*.tar.gz
      - split: other
        path: ka/other-*.tar.gz
      - split: test
        path: ka/test-*.tar.gz
      - split: train
        path: ka/train-*.tar.gz
      - split: validation
        path: ka/validation-*.tar.gz
  - config_name: kab
    data_files:
      - split: invalidated
        path: kab/invalidated-*.tar.gz
      - split: other
        path: kab/other-*.tar.gz
      - split: test
        path: kab/test-*.tar.gz
      - split: train
        path: kab/train-*.tar.gz
      - split: validation
        path: kab/validation-*.tar.gz
  - config_name: kk
    data_files:
      - split: invalidated
        path: kk/invalidated-*.tar.gz
      - split: other
        path: kk/other-*.tar.gz
      - split: test
        path: kk/test-*.tar.gz
      - split: train
        path: kk/train-*.tar.gz
      - split: validation
        path: kk/validation-*.tar.gz
  - config_name: kln
    data_files:
      - split: invalidated
        path: kln/invalidated-*.tar.gz
      - split: other
        path: kln/other-*.tar.gz
      - split: test
        path: kln/test-*.tar.gz
      - split: train
        path: kln/train-*.tar.gz
      - split: validation
        path: kln/validation-*.tar.gz
  - config_name: kmr
    data_files:
      - split: invalidated
        path: kmr/invalidated-*.tar.gz
      - split: other
        path: kmr/other-*.tar.gz
      - split: test
        path: kmr/test-*.tar.gz
      - split: train
        path: kmr/train-*.tar.gz
      - split: validation
        path: kmr/validation-*.tar.gz
  - config_name: ko
    data_files:
      - split: invalidated
        path: ko/invalidated-*.tar.gz
      - split: other
        path: ko/other-*.tar.gz
      - split: test
        path: ko/test-*.tar.gz
      - split: train
        path: ko/train-*.tar.gz
      - split: validation
        path: ko/validation-*.tar.gz
  - config_name: ky
    data_files:
      - split: invalidated
        path: ky/invalidated-*.tar.gz
      - split: other
        path: ky/other-*.tar.gz
      - split: test
        path: ky/test-*.tar.gz
      - split: train
        path: ky/train-*.tar.gz
      - split: validation
        path: ky/validation-*.tar.gz
  - config_name: lg
    data_files:
      - split: invalidated
        path: lg/invalidated-*.tar.gz
      - split: other
        path: lg/other-*.tar.gz
      - split: test
        path: lg/test-*.tar.gz
      - split: train
        path: lg/train-*.tar.gz
      - split: validation
        path: lg/validation-*.tar.gz
  - config_name: lij
    data_files:
      - split: invalidated
        path: lij/invalidated-*.tar.gz
      - split: test
        path: lij/test-*.tar.gz
      - split: train
        path: lij/train-*.tar.gz
      - split: validation
        path: lij/validation-*.tar.gz
  - config_name: lo
    data_files:
      - split: invalidated
        path: lo/invalidated-*.tar.gz
      - split: other
        path: lo/other-*.tar.gz
      - split: test
        path: lo/test-*.tar.gz
      - split: train
        path: lo/train-*.tar.gz
      - split: validation
        path: lo/validation-*.tar.gz
  - config_name: lt
    data_files:
      - split: invalidated
        path: lt/invalidated-*.tar.gz
      - split: other
        path: lt/other-*.tar.gz
      - split: test
        path: lt/test-*.tar.gz
      - split: train
        path: lt/train-*.tar.gz
      - split: validation
        path: lt/validation-*.tar.gz
  - config_name: ltg
    data_files:
      - split: invalidated
        path: ltg/invalidated-*.tar.gz
      - split: other
        path: ltg/other-*.tar.gz
      - split: test
        path: ltg/test-*.tar.gz
      - split: train
        path: ltg/train-*.tar.gz
      - split: validation
        path: ltg/validation-*.tar.gz
  - config_name: luo
    data_files:
      - split: invalidated
        path: luo/invalidated-*.tar.gz
      - split: other
        path: luo/other-*.tar.gz
      - split: test
        path: luo/test-*.tar.gz
      - split: train
        path: luo/train-*.tar.gz
      - split: validation
        path: luo/validation-*.tar.gz
  - config_name: lv
    data_files:
      - split: invalidated
        path: lv/invalidated-*.tar.gz
      - split: other
        path: lv/other-*.tar.gz
      - split: test
        path: lv/test-*.tar.gz
      - split: train
        path: lv/train-*.tar.gz
      - split: validation
        path: lv/validation-*.tar.gz
  - config_name: mdf
    data_files:
      - split: invalidated
        path: mdf/invalidated-*.tar.gz
      - split: test
        path: mdf/test-*.tar.gz
      - split: train
        path: mdf/train-*.tar.gz
      - split: validation
        path: mdf/validation-*.tar.gz
  - config_name: mhr
    data_files:
      - split: invalidated
        path: mhr/invalidated-*.tar.gz
      - split: other
        path: mhr/other-*.tar.gz
      - split: test
        path: mhr/test-*.tar.gz
      - split: train
        path: mhr/train-*.tar.gz
      - split: validation
        path: mhr/validation-*.tar.gz
  - config_name: mk
    data_files:
      - split: invalidated
        path: mk/invalidated-*.tar.gz
      - split: other
        path: mk/other-*.tar.gz
      - split: test
        path: mk/test-*.tar.gz
      - split: train
        path: mk/train-*.tar.gz
      - split: validation
        path: mk/validation-*.tar.gz
  - config_name: ml
    data_files:
      - split: invalidated
        path: ml/invalidated-*.tar.gz
      - split: other
        path: ml/other-*.tar.gz
      - split: test
        path: ml/test-*.tar.gz
      - split: train
        path: ml/train-*.tar.gz
      - split: validation
        path: ml/validation-*.tar.gz
  - config_name: mn
    data_files:
      - split: invalidated
        path: mn/invalidated-*.tar.gz
      - split: other
        path: mn/other-*.tar.gz
      - split: test
        path: mn/test-*.tar.gz
      - split: train
        path: mn/train-*.tar.gz
      - split: validation
        path: mn/validation-*.tar.gz
  - config_name: mr
    data_files:
      - split: invalidated
        path: mr/invalidated-*.tar.gz
      - split: other
        path: mr/other-*.tar.gz
      - split: test
        path: mr/test-*.tar.gz
      - split: train
        path: mr/train-*.tar.gz
      - split: validation
        path: mr/validation-*.tar.gz
  - config_name: mrj
    data_files:
      - split: invalidated
        path: mrj/invalidated-*.tar.gz
      - split: other
        path: mrj/other-*.tar.gz
      - split: test
        path: mrj/test-*.tar.gz
      - split: train
        path: mrj/train-*.tar.gz
      - split: validation
        path: mrj/validation-*.tar.gz
  - config_name: mt
    data_files:
      - split: invalidated
        path: mt/invalidated-*.tar.gz
      - split: other
        path: mt/other-*.tar.gz
      - split: test
        path: mt/test-*.tar.gz
      - split: train
        path: mt/train-*.tar.gz
      - split: validation
        path: mt/validation-*.tar.gz
  - config_name: myv
    data_files:
      - split: invalidated
        path: myv/invalidated-*.tar.gz
      - split: test
        path: myv/test-*.tar.gz
      - split: train
        path: myv/train-*.tar.gz
      - split: validation
        path: myv/validation-*.tar.gz
  - config_name: nan-tw
    data_files:
      - split: invalidated
        path: nan-tw/invalidated-*.tar.gz
      - split: other
        path: nan-tw/other-*.tar.gz
      - split: test
        path: nan-tw/test-*.tar.gz
      - split: train
        path: nan-tw/train-*.tar.gz
      - split: validation
        path: nan-tw/validation-*.tar.gz
  - config_name: nb-NO
    data_files:
      - split: invalidated
        path: nb-NO/invalidated-*.tar.gz
      - split: other
        path: nb-NO/other-*.tar.gz
      - split: test
        path: nb-NO/test-*.tar.gz
      - split: train
        path: nb-NO/train-*.tar.gz
      - split: validation
        path: nb-NO/validation-*.tar.gz
  - config_name: ne-NP
    data_files:
      - split: invalidated
        path: ne-NP/invalidated-*.tar.gz
      - split: other
        path: ne-NP/other-*.tar.gz
      - split: test
        path: ne-NP/test-*.tar.gz
      - split: train
        path: ne-NP/train-*.tar.gz
      - split: validation
        path: ne-NP/validation-*.tar.gz
  - config_name: nhi
    data_files:
      - split: other
        path: nhi/other-*.tar.gz
      - split: test
        path: nhi/test-*.tar.gz
      - split: train
        path: nhi/train-*.tar.gz
      - split: validation
        path: nhi/validation-*.tar.gz
  - config_name: nl
    data_files:
      - split: invalidated
        path: nl/invalidated-*.tar.gz
      - split: other
        path: nl/other-*.tar.gz
      - split: test
        path: nl/test-*.tar.gz
      - split: train
        path: nl/train-*.tar.gz
      - split: validation
        path: nl/validation-*.tar.gz
  - config_name: nn-NO
    data_files:
      - split: invalidated
        path: nn-NO/invalidated-*.tar.gz
      - split: other
        path: nn-NO/other-*.tar.gz
      - split: test
        path: nn-NO/test-*.tar.gz
      - split: train
        path: nn-NO/train-*.tar.gz
      - split: validation
        path: nn-NO/validation-*.tar.gz
  - config_name: nr
    data_files:
      - split: other
        path: nr/other-*.tar.gz
  - config_name: nso
    data_files:
      - split: other
        path: nso/other-*.tar.gz
      - split: train
        path: nso/train-*.tar.gz
  - config_name: oc
    data_files:
      - split: invalidated
        path: oc/invalidated-*.tar.gz
      - split: other
        path: oc/other-*.tar.gz
      - split: test
        path: oc/test-*.tar.gz
      - split: train
        path: oc/train-*.tar.gz
      - split: validation
        path: oc/validation-*.tar.gz
  - config_name: or
    data_files:
      - split: invalidated
        path: or/invalidated-*.tar.gz
      - split: other
        path: or/other-*.tar.gz
      - split: test
        path: or/test-*.tar.gz
      - split: train
        path: or/train-*.tar.gz
      - split: validation
        path: or/validation-*.tar.gz
  - config_name: os
    data_files:
      - split: invalidated
        path: os/invalidated-*.tar.gz
      - split: test
        path: os/test-*.tar.gz
      - split: train
        path: os/train-*.tar.gz
      - split: validation
        path: os/validation-*.tar.gz
  - config_name: pa-IN
    data_files:
      - split: invalidated
        path: pa-IN/invalidated-*.tar.gz
      - split: other
        path: pa-IN/other-*.tar.gz
      - split: test
        path: pa-IN/test-*.tar.gz
      - split: train
        path: pa-IN/train-*.tar.gz
      - split: validation
        path: pa-IN/validation-*.tar.gz
  - config_name: pl
    data_files:
      - split: invalidated
        path: pl/invalidated-*.tar.gz
      - split: other
        path: pl/other-*.tar.gz
      - split: test
        path: pl/test-*.tar.gz
      - split: train
        path: pl/train-*.tar.gz
      - split: validation
        path: pl/validation-*.tar.gz
  - config_name: ps
    data_files:
      - split: invalidated
        path: ps/invalidated-*.tar.gz
      - split: other
        path: ps/other-*.tar.gz
      - split: test
        path: ps/test-*.tar.gz
      - split: train
        path: ps/train-*.tar.gz
      - split: validation
        path: ps/validation-*.tar.gz
  - config_name: pt
    data_files:
      - split: invalidated
        path: pt/invalidated-*.tar.gz
      - split: other
        path: pt/other-*.tar.gz
      - split: test
        path: pt/test-*.tar.gz
      - split: train
        path: pt/train-*.tar.gz
      - split: validation
        path: pt/validation-*.tar.gz
  - config_name: quy
    data_files:
      - split: invalidated
        path: quy/invalidated-*.tar.gz
      - split: other
        path: quy/other-*.tar.gz
      - split: test
        path: quy/test-*.tar.gz
      - split: train
        path: quy/train-*.tar.gz
  - config_name: rm-sursilv
    data_files:
      - split: invalidated
        path: rm-sursilv/invalidated-*.tar.gz
      - split: other
        path: rm-sursilv/other-*.tar.gz
      - split: test
        path: rm-sursilv/test-*.tar.gz
      - split: train
        path: rm-sursilv/train-*.tar.gz
      - split: validation
        path: rm-sursilv/validation-*.tar.gz
  - config_name: rm-vallader
    data_files:
      - split: invalidated
        path: rm-vallader/invalidated-*.tar.gz
      - split: other
        path: rm-vallader/other-*.tar.gz
      - split: test
        path: rm-vallader/test-*.tar.gz
      - split: train
        path: rm-vallader/train-*.tar.gz
      - split: validation
        path: rm-vallader/validation-*.tar.gz
  - config_name: ro
    data_files:
      - split: invalidated
        path: ro/invalidated-*.tar.gz
      - split: other
        path: ro/other-*.tar.gz
      - split: test
        path: ro/test-*.tar.gz
      - split: train
        path: ro/train-*.tar.gz
      - split: validation
        path: ro/validation-*.tar.gz
  - config_name: ru
    data_files:
      - split: invalidated
        path: ru/invalidated-*.tar.gz
      - split: other
        path: ru/other-*.tar.gz
      - split: test
        path: ru/test-*.tar.gz
      - split: train
        path: ru/train-*.tar.gz
      - split: validation
        path: ru/validation-*.tar.gz
  - config_name: rup
    data_files:
      - split: other
        path: rup/other-*.tar.gz
  - config_name: rw
    data_files:
      - split: invalidated
        path: rw/invalidated-*.tar.gz
      - split: other
        path: rw/other-*.tar.gz
      - split: test
        path: rw/test-*.tar.gz
      - split: train
        path: rw/train-*.tar.gz
      - split: validation
        path: rw/validation-*.tar.gz
  - config_name: sah
    data_files:
      - split: invalidated
        path: sah/invalidated-*.tar.gz
      - split: other
        path: sah/other-*.tar.gz
      - split: test
        path: sah/test-*.tar.gz
      - split: train
        path: sah/train-*.tar.gz
      - split: validation
        path: sah/validation-*.tar.gz
  - config_name: sat
    data_files:
      - split: invalidated
        path: sat/invalidated-*.tar.gz
      - split: other
        path: sat/other-*.tar.gz
      - split: test
        path: sat/test-*.tar.gz
      - split: train
        path: sat/train-*.tar.gz
      - split: validation
        path: sat/validation-*.tar.gz
  - config_name: sc
    data_files:
      - split: invalidated
        path: sc/invalidated-*.tar.gz
      - split: other
        path: sc/other-*.tar.gz
      - split: test
        path: sc/test-*.tar.gz
      - split: train
        path: sc/train-*.tar.gz
      - split: validation
        path: sc/validation-*.tar.gz
  - config_name: sd
    data_files:
      - split: invalidated
        path: sd/invalidated-*.tar.gz
      - split: other
        path: sd/other-*.tar.gz
      - split: test
        path: sd/test-*.tar.gz
      - split: train
        path: sd/train-*.tar.gz
  - config_name: sk
    data_files:
      - split: invalidated
        path: sk/invalidated-*.tar.gz
      - split: other
        path: sk/other-*.tar.gz
      - split: test
        path: sk/test-*.tar.gz
      - split: train
        path: sk/train-*.tar.gz
      - split: validation
        path: sk/validation-*.tar.gz
  - config_name: skr
    data_files:
      - split: invalidated
        path: skr/invalidated-*.tar.gz
      - split: other
        path: skr/other-*.tar.gz
      - split: test
        path: skr/test-*.tar.gz
      - split: train
        path: skr/train-*.tar.gz
      - split: validation
        path: skr/validation-*.tar.gz
  - config_name: sl
    data_files:
      - split: invalidated
        path: sl/invalidated-*.tar.gz
      - split: other
        path: sl/other-*.tar.gz
      - split: test
        path: sl/test-*.tar.gz
      - split: train
        path: sl/train-*.tar.gz
      - split: validation
        path: sl/validation-*.tar.gz
  - config_name: sq
    data_files:
      - split: invalidated
        path: sq/invalidated-*.tar.gz
      - split: test
        path: sq/test-*.tar.gz
      - split: train
        path: sq/train-*.tar.gz
      - split: validation
        path: sq/validation-*.tar.gz
  - config_name: sr
    data_files:
      - split: invalidated
        path: sr/invalidated-*.tar.gz
      - split: other
        path: sr/other-*.tar.gz
      - split: test
        path: sr/test-*.tar.gz
      - split: train
        path: sr/train-*.tar.gz
      - split: validation
        path: sr/validation-*.tar.gz
  - config_name: st
    data_files:
      - split: other
        path: st/other-*.tar.gz
  - config_name: sv-SE
    data_files:
      - split: invalidated
        path: sv-SE/invalidated-*.tar.gz
      - split: other
        path: sv-SE/other-*.tar.gz
      - split: test
        path: sv-SE/test-*.tar.gz
      - split: train
        path: sv-SE/train-*.tar.gz
      - split: validation
        path: sv-SE/validation-*.tar.gz
  - config_name: sw
    data_files:
      - split: invalidated
        path: sw/invalidated-*.tar.gz
      - split: other
        path: sw/other-*.tar.gz
      - split: test
        path: sw/test-*.tar.gz
      - split: train
        path: sw/train-*.tar.gz
      - split: validation
        path: sw/validation-*.tar.gz
  - config_name: ta
    data_files:
      - split: invalidated
        path: ta/invalidated-*.tar.gz
      - split: other
        path: ta/other-*.tar.gz
      - split: test
        path: ta/test-*.tar.gz
      - split: train
        path: ta/train-*.tar.gz
      - split: validation
        path: ta/validation-*.tar.gz
  - config_name: te
    data_files:
      - split: invalidated
        path: te/invalidated-*.tar.gz
      - split: other
        path: te/other-*.tar.gz
      - split: test
        path: te/test-*.tar.gz
      - split: train
        path: te/train-*.tar.gz
      - split: validation
        path: te/validation-*.tar.gz
  - config_name: tg
    data_files:
      - split: invalidated
        path: tg/invalidated-*.tar.gz
      - split: test
        path: tg/test-*.tar.gz
      - split: train
        path: tg/train-*.tar.gz
      - split: validation
        path: tg/validation-*.tar.gz
  - config_name: th
    data_files:
      - split: invalidated
        path: th/invalidated-*.tar.gz
      - split: other
        path: th/other-*.tar.gz
      - split: test
        path: th/test-*.tar.gz
      - split: train
        path: th/train-*.tar.gz
      - split: validation
        path: th/validation-*.tar.gz
  - config_name: ti
    data_files:
      - split: invalidated
        path: ti/invalidated-*.tar.gz
      - split: other
        path: ti/other-*.tar.gz
      - split: test
        path: ti/test-*.tar.gz
      - split: train
        path: ti/train-*.tar.gz
      - split: validation
        path: ti/validation-*.tar.gz
  - config_name: tig
    data_files:
      - split: invalidated
        path: tig/invalidated-*.tar.gz
      - split: other
        path: tig/other-*.tar.gz
      - split: test
        path: tig/test-*.tar.gz
      - split: train
        path: tig/train-*.tar.gz
      - split: validation
        path: tig/validation-*.tar.gz
  - config_name: tk
    data_files:
      - split: invalidated
        path: tk/invalidated-*.tar.gz
      - split: other
        path: tk/other-*.tar.gz
      - split: test
        path: tk/test-*.tar.gz
      - split: train
        path: tk/train-*.tar.gz
      - split: validation
        path: tk/validation-*.tar.gz
  - config_name: tn
    data_files:
      - split: invalidated
        path: tn/invalidated-*.tar.gz
      - split: other
        path: tn/other-*.tar.gz
      - split: test
        path: tn/test-*.tar.gz
      - split: train
        path: tn/train-*.tar.gz
      - split: validation
        path: tn/validation-*.tar.gz
  - config_name: tok
    data_files:
      - split: invalidated
        path: tok/invalidated-*.tar.gz
      - split: other
        path: tok/other-*.tar.gz
      - split: test
        path: tok/test-*.tar.gz
      - split: train
        path: tok/train-*.tar.gz
      - split: validation
        path: tok/validation-*.tar.gz
  - config_name: tr
    data_files:
      - split: invalidated
        path: tr/invalidated-*.tar.gz
      - split: other
        path: tr/other-*.tar.gz
      - split: test
        path: tr/test-*.tar.gz
      - split: train
        path: tr/train-*.tar.gz
      - split: validation
        path: tr/validation-*.tar.gz
  - config_name: ts
    data_files:
      - split: invalidated
        path: ts/invalidated-*.tar.gz
  - config_name: tt
    data_files:
      - split: invalidated
        path: tt/invalidated-*.tar.gz
      - split: other
        path: tt/other-*.tar.gz
      - split: test
        path: tt/test-*.tar.gz
      - split: train
        path: tt/train-*.tar.gz
      - split: validation
        path: tt/validation-*.tar.gz
  - config_name: tw
    data_files:
      - split: invalidated
        path: tw/invalidated-*.tar.gz
      - split: other
        path: tw/other-*.tar.gz
      - split: test
        path: tw/test-*.tar.gz
      - split: train
        path: tw/train-*.tar.gz
  - config_name: ug
    data_files:
      - split: invalidated
        path: ug/invalidated-*.tar.gz
      - split: other
        path: ug/other-*.tar.gz
      - split: test
        path: ug/test-*.tar.gz
      - split: train
        path: ug/train-*.tar.gz
      - split: validation
        path: ug/validation-*.tar.gz
  - config_name: uk
    data_files:
      - split: invalidated
        path: uk/invalidated-*.tar.gz
      - split: other
        path: uk/other-*.tar.gz
      - split: test
        path: uk/test-*.tar.gz
      - split: train
        path: uk/train-*.tar.gz
      - split: validation
        path: uk/validation-*.tar.gz
  - config_name: ur
    data_files:
      - split: invalidated
        path: ur/invalidated-*.tar.gz
      - split: other
        path: ur/other-*.tar.gz
      - split: test
        path: ur/test-*.tar.gz
      - split: train
        path: ur/train-*.tar.gz
      - split: validation
        path: ur/validation-*.tar.gz
  - config_name: uz
    data_files:
      - split: invalidated
        path: uz/invalidated-*.tar.gz
      - split: other
        path: uz/other-*.tar.gz
      - split: test
        path: uz/test-*.tar.gz
      - split: train
        path: uz/train-*.tar.gz
      - split: validation
        path: uz/validation-*.tar.gz
  - config_name: ve
    data_files:
      - split: other
        path: ve/other-*.tar.gz
  - config_name: vi
    data_files:
      - split: invalidated
        path: vi/invalidated-*.tar.gz
      - split: other
        path: vi/other-*.tar.gz
      - split: test
        path: vi/test-*.tar.gz
      - split: train
        path: vi/train-*.tar.gz
      - split: validation
        path: vi/validation-*.tar.gz
  - config_name: vot
    data_files:
      - split: invalidated
        path: vot/invalidated-*.tar.gz
      - split: test
        path: vot/test-*.tar.gz
      - split: train
        path: vot/train-*.tar.gz
  - config_name: xh
    data_files:
      - split: other
        path: xh/other-*.tar.gz
      - split: train
        path: xh/train-*.tar.gz
  - config_name: yi
    data_files:
      - split: invalidated
        path: yi/invalidated-*.tar.gz
      - split: other
        path: yi/other-*.tar.gz
      - split: test
        path: yi/test-*.tar.gz
      - split: train
        path: yi/train-*.tar.gz
      - split: validation
        path: yi/validation-*.tar.gz
  - config_name: yo
    data_files:
      - split: invalidated
        path: yo/invalidated-*.tar.gz
      - split: other
        path: yo/other-*.tar.gz
      - split: test
        path: yo/test-*.tar.gz
      - split: train
        path: yo/train-*.tar.gz
      - split: validation
        path: yo/validation-*.tar.gz
  - config_name: yue
    data_files:
      - split: invalidated
        path: yue/invalidated-*.tar.gz
      - split: other
        path: yue/other-*.tar.gz
      - split: test
        path: yue/test-*.tar.gz
      - split: train
        path: yue/train-*.tar.gz
      - split: validation
        path: yue/validation-*.tar.gz
  - config_name: zgh
    data_files:
      - split: invalidated
        path: zgh/invalidated-*.tar.gz
      - split: other
        path: zgh/other-*.tar.gz
      - split: test
        path: zgh/test-*.tar.gz
      - split: train
        path: zgh/train-*.tar.gz
      - split: validation
        path: zgh/validation-*.tar.gz
  - config_name: zh-CN
    data_files:
      - split: invalidated
        path: zh-CN/invalidated-*.tar.gz
      - split: other
        path: zh-CN/other-*.tar.gz
      - split: test
        path: zh-CN/test-*.tar.gz
      - split: train
        path: zh-CN/train-*.tar.gz
      - split: validation
        path: zh-CN/validation-*.tar.gz
  - config_name: zh-HK
    data_files:
      - split: invalidated
        path: zh-HK/invalidated-*.tar.gz
      - split: other
        path: zh-HK/other-*.tar.gz
      - split: test
        path: zh-HK/test-*.tar.gz
      - split: train
        path: zh-HK/train-*.tar.gz
      - split: validation
        path: zh-HK/validation-*.tar.gz
  - config_name: zh-TW
    data_files:
      - split: invalidated
        path: zh-TW/invalidated-*.tar.gz
      - split: other
        path: zh-TW/other-*.tar.gz
      - split: test
        path: zh-TW/test-*.tar.gz
      - split: train
        path: zh-TW/train-*.tar.gz
      - split: validation
        path: zh-TW/validation-*.tar.gz
  - config_name: zu
    data_files:
      - split: invalidated
        path: zu/invalidated-*.tar.gz
      - split: other
        path: zu/other-*.tar.gz
      - split: test
        path: zu/test-*.tar.gz
      - split: train
        path: zu/train-*.tar.gz
  - config_name: zza
    data_files:
      - split: invalidated
        path: zza/invalidated-*.tar.gz
      - split: other
        path: zza/other-*.tar.gz
      - split: test
        path: zza/test-*.tar.gz
      - split: train
        path: zza/train-*.tar.gz
      - split: validation
        path: zza/validation-*.tar.gz
---
# CV22-Sidon

## Overview
This dataset hosts a release of Mozilla Common Voice 22 restored with the Sidon speech restoration model. 

- **Source**: [Mozilla Common Voice 22.0](https://commonvoice.mozilla.org/)
- **Processing**: Sidon denoising (`sarulab-speech/sidon-v0.1`) with 21 s chunks and 48 kHz reconstruction
- **Format**: [WebDataset](https://github.com/webdataset/webdataset) shards (`.tar.gz`)
- **Manifest**: `paths.yaml` enumerates every shard path for Hugging Face–style loading
- **License**: Original Common Voice license ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/))

## Languages
137 language folders are available; the directory names mirror the Common Voice language identifiers.

```
ab af am ar as ast az ba bas be bg bn br ca ckb cnh cs cv cy da dav de dv dyu el en eo es et eu fa fi fr fy-NL ga-IE gl gn ha he hi hsb ht hu hy-AM ia id ig is it ja ka kab kk kln kmr ko ky lg lij lo lt ltg luo lv mdf mhr mk ml mn mr mrj mt myv nan-tw nb-NO ne-NP nhi nl nn-NO nr nso oc or os pa-IN pl ps pt quy rm-sursilv rm-vallader ro ru rup rw sah sat sc sd sk skr sl sq sr st sv-SE sw ta te tg th ti tig tk tn tok tr ts tt tw ug uk ur uz ve vi vot xh yi yo yue zgh zh-CN zh-HK zh-TW zu zza
```

Each language directory contains Sidon-processed shards for the Common Voice splits that exist for that language (`train`, `validation`, `test`, `other`, and `invalidated`). 

Approximate shard counts across all languages:

- `train`: 1529 shards
- `validation`: 209 shards
- `test`: 219 shards
- `other`: 1384 shards
- `invalidated`: 418 shards

## Shard Contents
Every shard stores up to 5,000 utterances. Within a shard you will find records structured as:

```
123456.flac           # 48 kHz mono audio after Sidon restoration
123456.metadata.json  # Original Common Voice metadata (speaker info, split ids, transcript, etc.)
```


## Usage Examples

### Hugging Face Datasets (paths manifest)
```python
import datasets
from IPython.display import Audio
from huggingface_hub import hf_hub_download
import yaml
token="YOUR_HF_ACCESS_TOKEN"
base_url = "https://huggingface.co/datasets/sarulab-speech/commonvoice22_sidon/resolve/main/"
language = 'en'
split = 'train'
data_file_path = hf_hub_download(repo_id="sarulab-speech/commonvoice22_sidon", repo_type="dataset", filename="paths.yaml",token=token)
paths = yaml.load(open(data_file_path, "r"), Loader=yaml.FullLoader)

ds = datasets.load_dataset("webdataset", data_files=[base_url + p for p in paths[language][split]],streaming=True,token=token)['train']

sample = next(iter(ds))
audio = sample['flac']
print(sample['metadata.json'])
Audio(audio['array'], rate=audio['sampling_rate'])

```


## Notes
- Sidon resamples chunks to 16 kHz internally and writes 48 kHz FLAC output.
- Failed or skipped records are omitted, so counts can differ slightly from the raw Common Voice release.

## Citation
If you use this dataset, please cite Sidon and Mozilla Common Voice.

```
@misc{nakata2025sidonfastrobustopensource,
      title={Sidon: Fast and Robust Open-Source Multilingual Speech Restoration for Large-scale Dataset Cleansing},
      author={Nakata, Wataru and Saito, Yuki and Ueda, Yota and Saruwatari, Hiroshi},
      year={2025},
      eprint={2509.17052},
      archivePrefix={arXiv},
      primaryClass={cs.SD},
      url={https://arxiv.org/abs/2509.17052}
}
```

```
@article{ardila2020common,
  author    = {Ardila, Rosana and Branson, Megan and Davis, Kelly and Kohler, Michael and Meyer, Gabriela and Henretty, Reuben and Morais, Michael and Saunders, Lindsay and Tyers, Francis and Weber, Gregor},
  title     = {{Common Voice}: A Massively-Multilingual Speech Corpus},
  journal   = {Proceedings of the 12th Language Resources and Evaluation Conference (LREC)},
  year      = {2020}
}
```

## License
Derived from Mozilla Common Voice, this dataset remains available under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Please respect any additional requirements imposed by downstream usage (e.g., speaker consent in redistribution policies).

## Acknowledgements
- Mozilla and the Common Voice contributors for collecting and releasing the original data.
