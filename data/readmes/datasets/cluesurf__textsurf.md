---
license: other
license_name: mixed
license_link: LICENSE.md
language:
  - abc
  - ae
  - ahr
  - akk
  - alw
  - am
  - amo
  - ang
  - aqk
  - ar
  - arc
  - arp
  - as
  - asj
  - awa
  - awk
  - ban
  - bdv
  - be
  - bea
  - beo
  - bfz
  - bgc
  - bhi
  - bhu
  - bkw
  - bn
  - bo
  - bou
  - bpx
  - br
  - bra
  - bsj
  - bsw
  - bvw
  - bwc
  - bwo
  - ca
  - cak
  - cdz
  - ceb
  - cek
  - cfm
  - ch
  - chr
  - ckb
  - cop
  - cs
  - csy
  - cth
  - cu
  - cy
  - da
  - de
  - dhn
  - dji
  - dne
  - dnv
  - dov
  - dwr
  - ee
  - eka
  - ekk
  - el
  - en
  - ena
  - enm
  - eo
  - es
  - eu
  - fa
  - ff
  - fi
  - fr
  - fro
  - gaq
  - gax
  - gaz
  - gbl
  - gdf
  - gel
  - gez
  - ghn
  - glw
  - gmv
  - gof
  - goj
  - gok
  - grc
  - gu
  - gux
  - gv
  - gyl
  - gyz
  - ha
  - hav
  - haw
  - he
  - hi
  - hil
  - hit
  - hlb
  - hlt
  - hne
  - hr
  - hre
  - hru
  - hu
  - hwo
  - hy
  - id
  - idc
  - ig
  - ikz
  - is
  - isn
  - it
  - iyx
  - ja
  - jid
  - jni
  - jnj
  - jum
  - juy
  - ka
  - kbq
  - kdl
  - kfc
  - kff
  - khj
  - ki
  - kiz
  - kky
  - klg
  - kn
  - ko
  - kos
  - krh
  - kxv
  - la
  - lbm
  - ldb
  - lg
  - lga
  - ln
  - lt
  - lth
  - luo
  - mbu
  - mey
  - mfm
  - mfo
  - mfx
  - mgj
  - mgv
  - mi
  - mkw
  - ml
  - mnk
  - moh
  - mpa
  - mr
  - my
  - mzq
  - nag
  - nb
  - nce
  - ncr
  - ndg
  - nit
  - njd
  - nkn
  - nl
  - 'no'
  - non
  - npi
  - nv
  - nww
  - ny
  - omb
  - ono
  - ory
  - oui
  - oyd
  - pa
  - pdo
  - peg
  - pes
  - pga
  - pi
  - pl
  - pll
  - plq
  - pon
  - pt
  - pub
  - puu
  - pwr
  - qok
  - quc
  - reg
  - rei
  - rhg
  - rki
  - rmn
  - rmy
  - ro
  - row
  - ru
  - rup
  - sa
  - sbk
  - sby
  - sch
  - shr
  - six
  - sk
  - skr
  - sle
  - sn
  - sr
  - stw
  - sur
  - sux
  - sv
  - swh
  - syc
  - ta
  - tap
  - tbx
  - tcn
  - tcz
  - tdx
  - te
  - th
  - thd
  - thr
  - tl
  - tn
  - to
  - tr
  - tsw
  - tvn
  - tw
  - tyx
  - ug
  - uga
  - uk
  - ulk
  - unx
  - ur
  - utr
  - vaa
  - vgr
  - vi
  - wbi
  - wbq
  - wja
  - wlo
  - wo
  - wro
  - xhm
  - xht
  - xhu
  - xnj
  - xsn
  - xur
  - yaf
  - yao
  - ydd
  - yer
  - ymp
  - yns
  - yo
  - yom
  - yua
  - zaj
  - zak
  - zbu
  - zga
  - zh
  - zin
  - ztp
pretty_name: text.surf texts
tags:
  - text.surf
size_categories:
  - 10M<n<100M
extra_gated_heading: Agree to the TextSurf Terms of Use to download
extra_gated_prompt: Downloading these files means you agree to the [TextSurf Terms of Use](https://text.surf/terms/use). Each text keeps its own license, listed in `LICENSE.md`. Where a text's license is NonCommercial, do not use it commercially.
extra_gated_fields:
  I agree to the TextSurf Terms of Use: checkbox
extra_gated_button_content: Agree and download
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/*/*/*.parquet
  - config_name: abureni
    data_files:
      - split: train
        path: data/abureni/*/*.parquet
  - config_name: ahirani
    data_files:
      - split: train
        path: data/ahirani/*/*.parquet
  - config_name: ainu
    data_files:
      - split: train
        path: data/ainu/*/*.parquet
  - config_name: akkadian
    data_files:
      - split: train
        path: data/akkadian/*/*.parquet
  - config_name: alaba-kabeena
    data_files:
      - split: train
        path: data/alaba-kabeena/*/*.parquet
  - config_name: ambala-ayta
    data_files:
      - split: train
        path: data/ambala-ayta/*/*.parquet
  - config_name: amharic
    data_files:
      - split: train
        path: data/amharic/*/*.parquet
  - config_name: amo
    data_files:
      - split: train
        path: data/amo/*/*.parquet
  - config_name: aninka
    data_files:
      - split: train
        path: data/aninka/*/*.parquet
  - config_name: apali
    data_files:
      - split: train
        path: data/apali/*/*.parquet
  - config_name: arabic
    data_files:
      - split: train
        path: data/arabic/*/*.parquet
  - config_name: aramaic
    data_files:
      - split: train
        path: data/aramaic/*/*.parquet
  - config_name: arapaho
    data_files:
      - split: train
        path: data/arapaho/*/*.parquet
  - config_name: ardhamagadhi
    data_files:
      - split: train
        path: data/ardhamagadhi/*/*.parquet
  - config_name: armenian
    data_files:
      - split: train
        path: data/armenian/*/*.parquet
  - config_name: aromanian
    data_files:
      - split: train
        path: data/aromanian/*/*.parquet
  - config_name: assamese
    data_files:
      - split: train
        path: data/assamese/*/*.parquet
  - config_name: avestan
    data_files:
      - split: train
        path: data/avestan/*/*.parquet
  - config_name: awabakal
    data_files:
      - split: train
        path: data/awabakal/*/*.parquet
  - config_name: awadhi
    data_files:
      - split: train
        path: data/awadhi/*/*.parquet
  - config_name: baiso
    data_files:
      - split: train
        path: data/baiso/*/*.parquet
  - config_name: balinese
    data_files:
      - split: train
        path: data/balinese/*/*.parquet
  - config_name: balkan-romani
    data_files:
      - split: train
        path: data/balkan-romani/*/*.parquet
  - config_name: bangwinji
    data_files:
      - split: train
        path: data/bangwinji/*/*.parquet
  - config_name: basque
    data_files:
      - split: train
        path: data/basque/*/*.parquet
  - config_name: beami
    data_files:
      - split: train
        path: data/beami/*/*.parquet
  - config_name: beaver
    data_files:
      - split: train
        path: data/beaver/*/*.parquet
  - config_name: bekwil
    data_files:
      - split: train
        path: data/bekwil/*/*.parquet
  - config_name: belarusian
    data_files:
      - split: train
        path: data/belarusian/*/*.parquet
  - config_name: bengali
    data_files:
      - split: train
        path: data/bengali/*/*.parquet
  - config_name: bhadarwahi
    data_files:
      - split: train
        path: data/bhadarwahi/*/*.parquet
  - config_name: bhateali
    data_files:
      - split: train
        path: data/bhateali/*/*.parquet
  - config_name: bhilali
    data_files:
      - split: train
        path: data/bhilali/*/*.parquet
  - config_name: bhunjia
    data_files:
      - split: train
        path: data/bhunjia/*/*.parquet
  - config_name: blackfoot
    data_files:
      - split: train
        path: data/blackfoot/*/*.parquet
  - config_name: bodo-parja
    data_files:
      - split: train
        path: data/bodo-parja/*/*.parquet
  - config_name: boga
    data_files:
      - split: train
        path: data/boga/*/*.parquet
  - config_name: bondei
    data_files:
      - split: train
        path: data/bondei/*/*.parquet
  - config_name: borana-arsi-guji-oromo
    data_files:
      - split: train
        path: data/borana-arsi-guji-oromo/*/*.parquet
  - config_name: boro-ethiopia
    data_files:
      - split: train
        path: data/boro-ethiopia/*/*.parquet
  - config_name: braj
    data_files:
      - split: train
        path: data/braj/*/*.parquet
  - config_name: breton
    data_files:
      - split: train
        path: data/breton/*/*.parquet
  - config_name: bu-zaranda
    data_files:
      - split: train
        path: data/bu-zaranda/*/*.parquet
  - config_name: bu
    data_files:
      - split: train
        path: data/bu/*/*.parquet
  - config_name: burmese
    data_files:
      - split: train
        path: data/burmese/*/*.parquet
  - config_name: bwile
    data_files:
      - split: train
        path: data/bwile/*/*.parquet
  - config_name: catalan
    data_files:
      - split: train
        path: data/catalan/*/*.parquet
  - config_name: cebuano
    data_files:
      - split: train
        path: data/cebuano/*/*.parquet
  - config_name: central-kurdish
    data_files:
      - split: train
        path: data/central-kurdish/*/*.parquet
  - config_name: chamorro
    data_files:
      - split: train
        path: data/chamorro/*/*.parquet
  - config_name: cherokee
    data_files:
      - split: train
        path: data/cherokee/*/*.parquet
  - config_name: chhattisgarhi
    data_files:
      - split: train
        path: data/chhattisgarhi/*/*.parquet
  - config_name: chinese
    data_files:
      - split: train
        path: data/chinese/*/*.parquet
  - config_name: church-slavonic
    data_files:
      - split: train
        path: data/church-slavonic/*/*.parquet
  - config_name: cishingini-western-kambari
    data_files:
      - split: train
        path: data/cishingini-western-kambari/*/*.parquet
  - config_name: coptic
    data_files:
      - split: train
        path: data/coptic/*/*.parquet
  - config_name: creole-haitian
    data_files:
      - split: train
        path: data/creole-haitian/*/*.parquet
  - config_name: croatian-standard
    data_files:
      - split: train
        path: data/croatian-standard/*/*.parquet
  - config_name: cung
    data_files:
      - split: train
        path: data/cung/*/*.parquet
  - config_name: czech
    data_files:
      - split: train
        path: data/czech/*/*.parquet
  - config_name: danish
    data_files:
      - split: train
        path: data/danish/*/*.parquet
  - config_name: danu
    data_files:
      - split: train
        path: data/danu/*/*.parquet
  - config_name: dawro
    data_files:
      - split: train
        path: data/dawro/*/*.parquet
  - config_name: dela-oenale
    data_files:
      - split: train
        path: data/dela-oenale/*/*.parquet
  - config_name: desia
    data_files:
      - split: train
        path: data/desia/*/*.parquet
  - config_name: dhanki
    data_files:
      - split: train
        path: data/dhanki/*/*.parquet
  - config_name: diyari
    data_files:
      - split: train
        path: data/diyari/*/*.parquet
  - config_name: djinang
    data_files:
      - split: train
        path: data/djinang/*/*.parquet
  - config_name: dutch
    data_files:
      - split: train
        path: data/dutch/*/*.parquet
  - config_name: duya
    data_files:
      - split: train
        path: data/duya/*/*.parquet
  - config_name: early-modern-korean
    data_files:
      - split: train
        path: data/early-modern-korean/*/*.parquet
  - config_name: east-ambae
    data_files:
      - split: train
        path: data/east-ambae/*/*.parquet
  - config_name: eastern-khumi-chin
    data_files:
      - split: train
        path: data/eastern-khumi-chin/*/*.parquet
  - config_name: eastern-panjabi
    data_files:
      - split: train
        path: data/eastern-panjabi/*/*.parquet
  - config_name: eastern-yiddish
    data_files:
      - split: train
        path: data/eastern-yiddish/*/*.parquet
  - config_name: egyptian
    data_files:
      - split: train
        path: data/egyptian/*/*.parquet
  - config_name: ekajuk
    data_files:
      - split: train
        path: data/ekajuk/*/*.parquet
  - config_name: english
    data_files:
      - split: train
        path: data/english/*/*.parquet
  - config_name: esperanto
    data_files:
      - split: train
        path: data/esperanto/*/*.parquet
  - config_name: estonian
    data_files:
      - split: train
        path: data/estonian/*/*.parquet
  - config_name: etulo
    data_files:
      - split: train
        path: data/etulo/*/*.parquet
  - config_name: ewe
    data_files:
      - split: train
        path: data/ewe/*/*.parquet
  - config_name: falam-chin
    data_files:
      - split: train
        path: data/falam-chin/*/*.parquet
  - config_name: finnish
    data_files:
      - split: train
        path: data/finnish/*/*.parquet
  - config_name: french
    data_files:
      - split: train
        path: data/french/*/*.parquet
  - config_name: fula
    data_files:
      - split: train
        path: data/fula/*/*.parquet
  - config_name: gamit
    data_files:
      - split: train
        path: data/gamit/*/*.parquet
  - config_name: gamo
    data_files:
      - split: train
        path: data/gamo/*/*.parquet
  - config_name: ganda
    data_files:
      - split: train
        path: data/ganda/*/*.parquet
  - config_name: gata
    data_files:
      - split: train
        path: data/gata/*/*.parquet
  - config_name: gayil
    data_files:
      - split: train
        path: data/gayil/*/*.parquet
  - config_name: geez
    data_files:
      - split: train
        path: data/geez/*/*.parquet
  - config_name: georgian
    data_files:
      - split: train
        path: data/georgian/*/*.parquet
  - config_name: german
    data_files:
      - split: train
        path: data/german/*/*.parquet
  - config_name: ghanongga
    data_files:
      - split: train
        path: data/ghanongga/*/*.parquet
  - config_name: glavda
    data_files:
      - split: train
        path: data/glavda/*/*.parquet
  - config_name: gofa
    data_files:
      - split: train
        path: data/gofa/*/*.parquet
  - config_name: gourmanchema
    data_files:
      - split: train
        path: data/gourmanchema/*/*.parquet
  - config_name: gowlan
    data_files:
      - split: train
        path: data/gowlan/*/*.parquet
  - config_name: gowli
    data_files:
      - split: train
        path: data/gowli/*/*.parquet
  - config_name: greek
    data_files:
      - split: train
        path: data/greek/*/*.parquet
  - config_name: guduf-gava
    data_files:
      - split: train
        path: data/guduf-gava/*/*.parquet
  - config_name: gujarati
    data_files:
      - split: train
        path: data/gujarati/*/*.parquet
  - config_name: guugu-yimidhirr
    data_files:
      - split: train
        path: data/guugu-yimidhirr/*/*.parquet
  - config_name: gyaazi
    data_files:
      - split: train
        path: data/gyaazi/*/*.parquet
  - config_name: halbi
    data_files:
      - split: train
        path: data/halbi/*/*.parquet
  - config_name: haryanvi
    data_files:
      - split: train
        path: data/haryanvi/*/*.parquet
  - config_name: hassaniyya
    data_files:
      - split: train
        path: data/hassaniyya/*/*.parquet
  - config_name: hattic
    data_files:
      - split: train
        path: data/hattic/*/*.parquet
  - config_name: hausa
    data_files:
      - split: train
        path: data/hausa/*/*.parquet
  - config_name: havu
    data_files:
      - split: train
        path: data/havu/*/*.parquet
  - config_name: hawaiian
    data_files:
      - split: train
        path: data/hawaiian/*/*.parquet
  - config_name: hebrew
    data_files:
      - split: train
        path: data/hebrew/*/*.parquet
  - config_name: hiligaynon
    data_files:
      - split: train
        path: data/hiligaynon/*/*.parquet
  - config_name: hindi
    data_files:
      - split: train
        path: data/hindi/*/*.parquet
  - config_name: hittite
    data_files:
      - split: train
        path: data/hittite/*/*.parquet
  - config_name: hre
    data_files:
      - split: train
        path: data/hre/*/*.parquet
  - config_name: hruso
    data_files:
      - split: train
        path: data/hruso/*/*.parquet
  - config_name: hungarian
    data_files:
      - split: train
        path: data/hungarian/*/*.parquet
  - config_name: hurrian
    data_files:
      - split: train
        path: data/hurrian/*/*.parquet
  - config_name: hwana
    data_files:
      - split: train
        path: data/hwana/*/*.parquet
  - config_name: icelandic
    data_files:
      - split: train
        path: data/icelandic/*/*.parquet
  - config_name: idon
    data_files:
      - split: train
        path: data/idon/*/*.parquet
  - config_name: igbo
    data_files:
      - split: train
        path: data/igbo/*/*.parquet
  - config_name: ikizu
    data_files:
      - split: train
        path: data/ikizu/*/*.parquet
  - config_name: ilocano
    data_files:
      - split: train
        path: data/ilocano/*/*.parquet
  - config_name: isanzu
    data_files:
      - split: train
        path: data/isanzu/*/*.parquet
  - config_name: italian
    data_files:
      - split: train
        path: data/italian/*/*.parquet
  - config_name: jain-maharashtri
    data_files:
      - split: train
        path: data/jain-maharashtri/*/*.parquet
  - config_name: janji
    data_files:
      - split: train
        path: data/janji/*/*.parquet
  - config_name: japanese
    data_files:
      - split: train
        path: data/japanese/*/*.parquet
  - config_name: jumjum
    data_files:
      - split: train
        path: data/jumjum/*/*.parquet
  - config_name: juray
    data_files:
      - split: train
        path: data/juray/*/*.parquet
  - config_name: kamano
    data_files:
      - split: train
        path: data/kamano/*/*.parquet
  - config_name: kannada
    data_files:
      - split: train
        path: data/kannada/*/*.parquet
  - config_name: kapin
    data_files:
      - split: train
        path: data/kapin/*/*.parquet
  - config_name: kaqchikel
    data_files:
      - split: train
        path: data/kaqchikel/*/*.parquet
  - config_name: kara-tanzania
    data_files:
      - split: train
        path: data/kara-tanzania/*/*.parquet
  - config_name: kiche
    data_files:
      - split: train
        path: data/kiche/*/*.parquet
  - config_name: kikuyu
    data_files:
      - split: train
        path: data/kikuyu/*/*.parquet
  - config_name: kinga
    data_files:
      - split: train
        path: data/kinga/*/*.parquet
  - config_name: kinshasa-lingala
    data_files:
      - split: train
        path: data/kinshasa-lingala/*/*.parquet
  - config_name: kisi
    data_files:
      - split: train
        path: data/kisi/*/*.parquet
  - config_name: kituba-congo
    data_files:
      - split: train
        path: data/kituba-congo/*/*.parquet
  - config_name: koda
    data_files:
      - split: train
        path: data/koda/*/*.parquet
  - config_name: konda-dora
    data_files:
      - split: train
        path: data/konda-dora/*/*.parquet
  - config_name: korean
    data_files:
      - split: train
        path: data/korean/*/*.parquet
  - config_name: koromba
    data_files:
      - split: train
        path: data/koromba/*/*.parquet
  - config_name: kosraean
    data_files:
      - split: train
        path: data/kosraean/*/*.parquet
  - config_name: koya
    data_files:
      - split: train
        path: data/koya/*/*.parquet
  - config_name: kuhane
    data_files:
      - split: train
        path: data/kuhane/*/*.parquet
  - config_name: kurama
    data_files:
      - split: train
        path: data/kurama/*/*.parquet
  - config_name: kuturmi
    data_files:
      - split: train
        path: data/kuturmi/*/*.parquet
  - config_name: kuvi
    data_files:
      - split: train
        path: data/kuvi/*/*.parquet
  - config_name: labwor
    data_files:
      - split: train
        path: data/labwor/*/*.parquet
  - config_name: latin
    data_files:
      - split: train
        path: data/latin/*/*.parquet
  - config_name: lithuanian
    data_files:
      - split: train
        path: data/lithuanian/*/*.parquet
  - config_name: lodhi
    data_files:
      - split: train
        path: data/lodhi/*/*.parquet
  - config_name: loxicha-zapotec
    data_files:
      - split: train
        path: data/loxicha-zapotec/*/*.parquet
  - config_name: lungga
    data_files:
      - split: train
        path: data/lungga/*/*.parquet
  - config_name: luo-kenya-and-tanzania
    data_files:
      - split: train
        path: data/luo-kenya-and-tanzania/*/*.parquet
  - config_name: luwian
    data_files:
      - split: train
        path: data/luwian/*/*.parquet
  - config_name: luyana
    data_files:
      - split: train
        path: data/luyana/*/*.parquet
  - config_name: mahasu-pahari
    data_files:
      - split: train
        path: data/mahasu-pahari/*/*.parquet
  - config_name: malayalam
    data_files:
      - split: train
        path: data/malayalam/*/*.parquet
  - config_name: mandaic
    data_files:
      - split: train
        path: data/mandaic/*/*.parquet
  - config_name: mandinka
    data_files:
      - split: train
        path: data/mandinka/*/*.parquet
  - config_name: manx
    data_files:
      - split: train
        path: data/manx/*/*.parquet
  - config_name: maori
    data_files:
      - split: train
        path: data/maori/*/*.parquet
  - config_name: marathi
    data_files:
      - split: train
        path: data/marathi/*/*.parquet
  - config_name: marghi-south
    data_files:
      - split: train
        path: data/marghi-south/*/*.parquet
  - config_name: matengo
    data_files:
      - split: train
        path: data/matengo/*/*.parquet
  - config_name: mbe
    data_files:
      - split: train
        path: data/mbe/*/*.parquet
  - config_name: mbula-bwazza
    data_files:
      - split: train
        path: data/mbula-bwazza/*/*.parquet
  - config_name: melo
    data_files:
      - split: train
        path: data/melo/*/*.parquet
  - config_name: meriam
    data_files:
      - split: train
        path: data/meriam/*/*.parquet
  - config_name: middle-english
    data_files:
      - split: train
        path: data/middle-english/*/*.parquet
  - config_name: middle-khmer
    data_files:
      - split: train
        path: data/middle-khmer/*/*.parquet
  - config_name: middle-korean
    data_files:
      - split: train
        path: data/middle-korean/*/*.parquet
  - config_name: middle-persian
    data_files:
      - split: train
        path: data/middle-persian/*/*.parquet
  - config_name: modern-greek
    data_files:
      - split: train
        path: data/modern-greek/*/*.parquet
  - config_name: mohawk
    data_files:
      - split: train
        path: data/mohawk/*/*.parquet
  - config_name: mori-atas
    data_files:
      - split: train
        path: data/mori-atas/*/*.parquet
  - config_name: mpoto
    data_files:
      - split: train
        path: data/mpoto/*/*.parquet
  - config_name: munda
    data_files:
      - split: train
        path: data/munda/*/*.parquet
  - config_name: mwaghavul
    data_files:
      - split: train
        path: data/mwaghavul/*/*.parquet
  - config_name: naga-pidgin
    data_files:
      - split: train
        path: data/naga-pidgin/*/*.parquet
  - config_name: nahuatl-huasteca
    data_files:
      - split: train
        path: data/nahuatl-huasteca/*/*.parquet
  - config_name: nahuatl
    data_files:
      - split: train
        path: data/nahuatl/*/*.parquet
  - config_name: navajo
    data_files:
      - split: train
        path: data/navajo/*/*.parquet
  - config_name: ncane-mungong
    data_files:
      - split: train
        path: data/ncane-mungong/*/*.parquet
  - config_name: ndendeule
    data_files:
      - split: train
        path: data/ndendeule/*/*.parquet
  - config_name: ndengereko
    data_files:
      - split: train
        path: data/ndengereko/*/*.parquet
  - config_name: ndonde-hamba
    data_files:
      - split: train
        path: data/ndonde-hamba/*/*.parquet
  - config_name: ndwewe
    data_files:
      - split: train
        path: data/ndwewe/*/*.parquet
  - config_name: nepali
    data_files:
      - split: train
        path: data/nepali/*/*.parquet
  - config_name: nga-la
    data_files:
      - split: train
        path: data/nga-la/*/*.parquet
  - config_name: ngarrindjeri
    data_files:
      - split: train
        path: data/ngarrindjeri/*/*.parquet
  - config_name: nkangala
    data_files:
      - split: train
        path: data/nkangala/*/*.parquet
  - config_name: norwegian-bokmal
    data_files:
      - split: train
        path: data/norwegian-bokmal/*/*.parquet
  - config_name: norwegian
    data_files:
      - split: train
        path: data/norwegian/*/*.parquet
  - config_name: nsari
    data_files:
      - split: train
        path: data/nsari/*/*.parquet
  - config_name: nyanja
    data_files:
      - split: train
        path: data/nyanja/*/*.parquet
  - config_name: odia
    data_files:
      - split: train
        path: data/odia/*/*.parquet
  - config_name: old-anatolian-turkish
    data_files:
      - split: train
        path: data/old-anatolian-turkish/*/*.parquet
  - config_name: old-cham
    data_files:
      - split: train
        path: data/old-cham/*/*.parquet
  - config_name: old-church-slavonic
    data_files:
      - split: train
        path: data/old-church-slavonic/*/*.parquet
  - config_name: old-east-slavic
    data_files:
      - split: train
        path: data/old-east-slavic/*/*.parquet
  - config_name: old-english
    data_files:
      - split: train
        path: data/old-english/*/*.parquet
  - config_name: old-french
    data_files:
      - split: train
        path: data/old-french/*/*.parquet
  - config_name: old-javanese
    data_files:
      - split: train
        path: data/old-javanese/*/*.parquet
  - config_name: old-khmer
    data_files:
      - split: train
        path: data/old-khmer/*/*.parquet
  - config_name: old-korean
    data_files:
      - split: train
        path: data/old-korean/*/*.parquet
  - config_name: old-malay
    data_files:
      - split: train
        path: data/old-malay/*/*.parquet
  - config_name: old-norse
    data_files:
      - split: train
        path: data/old-norse/*/*.parquet
  - config_name: old-turkic
    data_files:
      - split: train
        path: data/old-turkic/*/*.parquet
  - config_name: onondaga
    data_files:
      - split: train
        path: data/onondaga/*/*.parquet
  - config_name: oyda
    data_files:
      - split: train
        path: data/oyda/*/*.parquet
  - config_name: padoe
    data_files:
      - split: train
        path: data/padoe/*/*.parquet
  - config_name: palaic
    data_files:
      - split: train
        path: data/palaic/*/*.parquet
  - config_name: pali
    data_files:
      - split: train
        path: data/pali/*/*.parquet
  - config_name: palya-bareli
    data_files:
      - split: train
        path: data/palya-bareli/*/*.parquet
  - config_name: pengo
    data_files:
      - split: train
        path: data/pengo/*/*.parquet
  - config_name: persian
    data_files:
      - split: train
        path: data/persian/*/*.parquet
  - config_name: pohnpeian
    data_files:
      - split: train
        path: data/pohnpeian/*/*.parquet
  - config_name: polci
    data_files:
      - split: train
        path: data/polci/*/*.parquet
  - config_name: polish
    data_files:
      - split: train
        path: data/polish/*/*.parquet
  - config_name: portuguese
    data_files:
      - split: train
        path: data/portuguese/*/*.parquet
  - config_name: powari
    data_files:
      - split: train
        path: data/powari/*/*.parquet
  - config_name: prakrit
    data_files:
      - split: train
        path: data/prakrit/*/*.parquet
  - config_name: punjabi
    data_files:
      - split: train
        path: data/punjabi/*/*.parquet
  - config_name: punu
    data_files:
      - split: train
        path: data/punu/*/*.parquet
  - config_name: purum
    data_files:
      - split: train
        path: data/purum/*/*.parquet
  - config_name: rakhine
    data_files:
      - split: train
        path: data/rakhine/*/*.parquet
  - config_name: rana-tharu
    data_files:
      - split: train
        path: data/rana-tharu/*/*.parquet
  - config_name: rangi
    data_files:
      - split: train
        path: data/rangi/*/*.parquet
  - config_name: reli
    data_files:
      - split: train
        path: data/reli/*/*.parquet
  - config_name: rohingya
    data_files:
      - split: train
        path: data/rohingya/*/*.parquet
  - config_name: romanian
    data_files:
      - split: train
        path: data/romanian/*/*.parquet
  - config_name: russian
    data_files:
      - split: train
        path: data/russian/*/*.parquet
  - config_name: ruthenian
    data_files:
      - split: train
        path: data/ruthenian/*/*.parquet
  - config_name: safen
    data_files:
      - split: train
        path: data/safen/*/*.parquet
  - config_name: safwa
    data_files:
      - split: train
        path: data/safwa/*/*.parquet
  - config_name: sakachep-chorei
    data_files:
      - split: train
        path: data/sakachep-chorei/*/*.parquet
  - config_name: salka-tsishingini
    data_files:
      - split: train
        path: data/salka-tsishingini/*/*.parquet
  - config_name: sanga-nigeria
    data_files:
      - split: train
        path: data/sanga-nigeria/*/*.parquet
  - config_name: sanskrit
    data_files:
      - split: train
        path: data/sanskrit/*/*.parquet
  - config_name: santa
    data_files:
      - split: train
        path: data/santa/*/*.parquet
  - config_name: saraiki
    data_files:
      - split: train
        path: data/saraiki/*/*.parquet
  - config_name: satawalese
    data_files:
      - split: train
        path: data/satawalese/*/*.parquet
  - config_name: serbian-standard
    data_files:
      - split: train
        path: data/serbian-standard/*/*.parquet
  - config_name: serbian
    data_files:
      - split: train
        path: data/serbian/*/*.parquet
  - config_name: shi
    data_files:
      - split: train
        path: data/shi/*/*.parquet
  - config_name: sholaga
    data_files:
      - split: train
        path: data/sholaga/*/*.parquet
  - config_name: shona
    data_files:
      - split: train
        path: data/shona/*/*.parquet
  - config_name: shwe-palaung
    data_files:
      - split: train
        path: data/shwe-palaung/*/*.parquet
  - config_name: sizang-chin
    data_files:
      - split: train
        path: data/sizang-chin/*/*.parquet
  - config_name: slovak
    data_files:
      - split: train
        path: data/slovak/*/*.parquet
  - config_name: soli
    data_files:
      - split: train
        path: data/soli/*/*.parquet
  - config_name: south-sudanese-creole-arabic
    data_files:
      - split: train
        path: data/south-sudanese-creole-arabic/*/*.parquet
  - config_name: southeastern-kolami
    data_files:
      - split: train
        path: data/southeastern-kolami/*/*.parquet
  - config_name: spanish
    data_files:
      - split: train
        path: data/spanish/*/*.parquet
  - config_name: standard-indonesian
    data_files:
      - split: train
        path: data/standard-indonesian/*/*.parquet
  - config_name: sumau
    data_files:
      - split: train
        path: data/sumau/*/*.parquet
  - config_name: sumerian
    data_files:
      - split: train
        path: data/sumerian/*/*.parquet
  - config_name: swahili
    data_files:
      - split: train
        path: data/swahili/*/*.parquet
  - config_name: swedish
    data_files:
      - split: train
        path: data/swedish/*/*.parquet
  - config_name: syriac
    data_files:
      - split: train
        path: data/syriac/*/*.parquet
  - config_name: taabwa
    data_files:
      - split: train
        path: data/taabwa/*/*.parquet
  - config_name: tagakaulu-kalagan
    data_files:
      - split: train
        path: data/tagakaulu-kalagan/*/*.parquet
  - config_name: tagalog
    data_files:
      - split: train
        path: data/tagalog/*/*.parquet
  - config_name: tamil
    data_files:
      - split: train
        path: data/tamil/*/*.parquet
  - config_name: tandroy-malagasy
    data_files:
      - split: train
        path: data/tandroy-malagasy/*/*.parquet
  - config_name: tanzanian-ngoni
    data_files:
      - split: train
        path: data/tanzanian-ngoni/*/*.parquet
  - config_name: tarok
    data_files:
      - split: train
        path: data/tarok/*/*.parquet
  - config_name: tavoyan
    data_files:
      - split: train
        path: data/tavoyan/*/*.parquet
  - config_name: teke-tyee
    data_files:
      - split: train
        path: data/teke-tyee/*/*.parquet
  - config_name: telugu
    data_files:
      - split: train
        path: data/telugu/*/*.parquet
  - config_name: thado-chin
    data_files:
      - split: train
        path: data/thado-chin/*/*.parquet
  - config_name: thai
    data_files:
      - split: train
        path: data/thai/*/*.parquet
  - config_name: thaipum-chin
    data_files:
      - split: train
        path: data/thaipum-chin/*/*.parquet
  - config_name: thayore
    data_files:
      - split: train
        path: data/thayore/*/*.parquet
  - config_name: tibetan
    data_files:
      - split: train
        path: data/tibetan/*/*.parquet
  - config_name: tichurong
    data_files:
      - split: train
        path: data/tichurong/*/*.parquet
  - config_name: toka-leya-dombe
    data_files:
      - split: train
        path: data/toka-leya-dombe/*/*.parquet
  - config_name: tonga-tonga-islands
    data_files:
      - split: train
        path: data/tonga-tonga-islands/*/*.parquet
  - config_name: tsikimba
    data_files:
      - split: train
        path: data/tsikimba/*/*.parquet
  - config_name: tswana
    data_files:
      - split: train
        path: data/tswana/*/*.parquet
  - config_name: turkish
    data_files:
      - split: train
        path: data/turkish/*/*.parquet
  - config_name: twi
    data_files:
      - split: train
        path: data/twi/*/*.parquet
  - config_name: ugaritic
    data_files:
      - split: train
        path: data/ugaritic/*/*.parquet
  - config_name: uighur
    data_files:
      - split: train
        path: data/uighur/*/*.parquet
  - config_name: ukrainian
    data_files:
      - split: train
        path: data/ukrainian/*/*.parquet
  - config_name: urartian
    data_files:
      - split: train
        path: data/urartian/*/*.parquet
  - config_name: urdu
    data_files:
      - split: train
        path: data/urdu/*/*.parquet
  - config_name: ut-main
    data_files:
      - split: train
        path: data/ut-main/*/*.parquet
  - config_name: vaagri-booli
    data_files:
      - split: train
        path: data/vaagri-booli/*/*.parquet
  - config_name: vaghri
    data_files:
      - split: train
        path: data/vaghri/*/*.parquet
  - config_name: vietnamese
    data_files:
      - split: train
        path: data/vietnamese/*/*.parquet
  - config_name: vlax-romani
    data_files:
      - split: train
        path: data/vlax-romani/*/*.parquet
  - config_name: vwanji
    data_files:
      - split: train
        path: data/vwanji/*/*.parquet
  - config_name: waddar
    data_files:
      - split: train
        path: data/waddar/*/*.parquet
  - config_name: waja
    data_files:
      - split: train
        path: data/waja/*/*.parquet
  - config_name: welsh
    data_files:
      - split: train
        path: data/welsh/*/*.parquet
  - config_name: west-central-oromo
    data_files:
      - split: train
        path: data/west-central-oromo/*/*.parquet
  - config_name: western-farsi
    data_files:
      - split: train
        path: data/western-farsi/*/*.parquet
  - config_name: wolio
    data_files:
      - split: train
        path: data/wolio/*/*.parquet
  - config_name: wolof
    data_files:
      - split: train
        path: data/wolof/*/*.parquet
  - config_name: worrorra
    data_files:
      - split: train
        path: data/worrorra/*/*.parquet
  - config_name: yaka-congo
    data_files:
      - split: train
        path: data/yaka-congo/*/*.parquet
  - config_name: yaka-pelende-lonzo
    data_files:
      - split: train
        path: data/yaka-pelende-lonzo/*/*.parquet
  - config_name: yale
    data_files:
      - split: train
        path: data/yale/*/*.parquet
  - config_name: yamap
    data_files:
      - split: train
        path: data/yamap/*/*.parquet
  - config_name: yansi
    data_files:
      - split: train
        path: data/yansi/*/*.parquet
  - config_name: yao
    data_files:
      - split: train
        path: data/yao/*/*.parquet
  - config_name: yemsa
    data_files:
      - split: train
        path: data/yemsa/*/*.parquet
  - config_name: yiddish
    data_files:
      - split: train
        path: data/yiddish/*/*.parquet
  - config_name: yinjibarndi
    data_files:
      - split: train
        path: data/yinjibarndi/*/*.parquet
  - config_name: yombe
    data_files:
      - split: train
        path: data/yombe/*/*.parquet
  - config_name: yoruba
    data_files:
      - split: train
        path: data/yoruba/*/*.parquet
  - config_name: yucatec-maya
    data_files:
      - split: train
        path: data/yucatec-maya/*/*.parquet
  - config_name: zanaki
    data_files:
      - split: train
        path: data/zanaki/*/*.parquet
  - config_name: zaramo
    data_files:
      - split: train
        path: data/zaramo/*/*.parquet
  - config_name: zinza
    data_files:
      - split: train
        path: data/zinza/*/*.parquet
---

# text.surf texts

21318 editions of 19204 works in 324 languages from the text.surf archive, release 000006: 22380444 passages, one row each. Each edition keeps its own license (`LICENSE.md`).

Licenses: CC BY 3.0, CC BY 4.0, CC BY-NC 4.0, CC BY-NC-SA 3.0, CC BY-NC-SA 4.0, CC BY-SA 3.0, CC BY-SA 4.0, CC0 1.0, MIT, BAdW terms, non-commercial, Bahá'í International Community terms of use, Public domain. Each MIT edition's copyright line and the MIT permission notice are in `LICENSE.md`, and a copy of an MIT edition keeps both.

One Parquet file per edition, `data/<language>/<work>/<edition>.parquet`, every file with the columns below. `load_dataset` reads every language as one `train` split; name a language as the config (`load_dataset("<repo>", "sanskrit")`) to read that language alone. To take a single edition, load its file alone (`LICENSE.md` names each).

| column | holds |
| --- | --- |
| `work` | the work's key |
| `edition` | `<language>.<script>.<version>` |
| `passage` | the place within the work, such as `1/1`; null for an edition with no places |
| `language`, `script` | the edition's |
| `text` | the passage, exactly as the edition has it (never Unicode-normalized) |
| `license` | the edition's license |
| `source` | the source the edition cites, or null |
| `sha256` | the archive object the row came from |

| config | code | editions | works | passages |
| --- | --- | --- | --- | --- |
| abureni | mgj | 1 | 1 | 3892 |
| ahirani | ahr | 1 | 1 | 14539 |
| ainu |  | 1 | 1 | 1334 |
| akkadian | akk | 162 | 142 | 188334 |
| alaba-kabeena | alw | 1 | 1 | 7917 |
| ambala-ayta | abc | 1 | 1 | 1084 |
| amharic | am | 20 | 18 | 78 |
| amo | amo | 1 | 1 | 7954 |
| aninka | aqk | 1 | 1 | 1151 |
| apali | ena | 1 | 1 | 10218 |
| arabic | ar | 77 | 74 | 771639 |
| aramaic | arc | 5 | 5 | 11987 |
| arapaho | arp | 1 | 1 | 1151 |
| ardhamagadhi |  | 2 | 2 | 742 |
| armenian | hy | 13 | 13 | 20678 |
| aromanian | rup | 1 | 1 | 2174 |
| assamese | as | 1 | 1 | 31124 |
| avestan | ae | 13 | 8 | 4106 |
| awabakal | awk | 1 | 1 | 1136 |
| awadhi | awa | 3 | 3 | 91 |
| baiso | bsw | 2 | 1 | 14576 |
| balinese | ban | 2 | 2 | 768 |
| balkan-romani | rmn | 1 | 1 | 7956 |
| bangwinji | bsj | 1 | 1 | 7187 |
| basque | eu | 1 | 1 | 7952 |
| beami | beo | 1 | 1 | 30059 |
| beaver | bea | 1 | 1 | 678 |
| bekwil | bkw | 1 | 1 | 7950 |
| belarusian | be | 2 | 1 | 44324 |
| bengali | bn | 2 | 1 | 62450 |
| bhadarwahi |  | 1 | 1 | 7938 |
| bhateali |  | 1 | 1 | 7888 |
| bhilali | bhi | 1 | 1 | 7957 |
| bhunjia | bhu | 1 | 1 | 7956 |
| blackfoot |  | 1 | 1 | 1071 |
| bodo-parja | bdv | 1 | 1 | 7959 |
| boga | bvw | 1 | 1 | 2122 |
| bondei | bou | 1 | 1 | 3779 |
| borana-arsi-guji-oromo | gax | 1 | 1 | 31069 |
| boro-ethiopia | bwo | 1 | 1 | 7947 |
| braj | bra | 4 | 4 | 2344 |
| breton | br | 3 | 2 | 56821 |
| bu-zaranda | zbu | 1 | 1 | 1793 |
| bu | jid | 1 | 1 | 7953 |
| burmese | my | 2 | 1 | 60697 |
| bwile | bwc | 1 | 1 | 1226 |
| catalan | ca | 1 | 1 | 366 |
| cebuano | ceb | 3 | 1 | 92829 |
| central-kurdish | ckb | 1 | 1 | 31218 |
| chamorro | ch | 1 | 1 | 7245 |
| cherokee | chr | 2 | 2 | 8086 |
| chhattisgarhi | hne | 1 | 1 | 31220 |
| chinese | zh | 4077 | 3924 | 4000301 |
| church-slavonic |  | 29 | 27 | 145613 |
| cishingini-western-kambari |  | 1 | 1 | 19305 |
| coptic | cop | 91 | 90 | 63366 |
| creole-haitian |  | 2 | 1 | 62342 |
| croatian-standard | hr | 2 | 1 | 43395 |
| cung |  | 1 | 1 | 7950 |
| czech | cs | 3 | 2 | 39166 |
| danish | da | 2 | 2 | 343 |
| danu | dnv | 1 | 1 | 7924 |
| dawro | dwr | 1 | 1 | 30930 |
| dela-oenale | row | 1 | 1 | 9084 |
| desia |  | 1 | 1 | 7958 |
| dhanki | dhn | 1 | 1 | 14540 |
| diyari |  | 1 | 1 | 7959 |
| djinang | dji | 1 | 1 | 911 |
| dutch | nl | 7 | 4 | 109804 |
| duya | ldb | 1 | 1 | 7940 |
| early-modern-korean |  | 3 | 3 | 350 |
| east-ambae | omb | 1 | 1 | 1231 |
| eastern-khumi-chin | cek | 1 | 1 | 31191 |
| eastern-panjabi | pa | 1 | 1 | 31220 |
| eastern-yiddish | ydd | 1 | 1 | 7957 |
| egyptian |  | 107 | 74 | 51013 |
| ekajuk | eka | 1 | 1 | 15890 |
| english | en | 3671 | 3249 | 2895954 |
| esperanto | eo | 1 | 1 | 31102 |
| estonian | ekk | 4 | 3 | 16263 |
| etulo | utr | 1 | 1 | 7959 |
| ewe | ee | 1 | 1 | 31220 |
| falam-chin | cfm | 1 | 1 | 675 |
| finnish | fi | 4 | 4 | 19848 |
| french | fr | 97 | 85 | 272674 |
| fula | ff | 16 | 16 | 2743 |
| gamit | gbl | 1 | 1 | 7923 |
| gamo | gmv | 3 | 1 | 69628 |
| ganda | lg | 1 | 1 | 31223 |
| gata | gaq | 1 | 1 | 7959 |
| gayil | gyl | 1 | 1 | 7953 |
| geez | gez | 1221 | 1175 | 43603 |
| georgian | ka | 1 | 1 | 72 |
| german | de | 153 | 144 | 493109 |
| ghanongga | ghn | 1 | 1 | 7948 |
| glavda | glw | 1 | 1 | 3997 |
| gofa | gof | 3 | 1 | 70119 |
| gourmanchema | gux | 2 | 1 | 15899 |
| gowlan | goj | 1 | 1 | 7959 |
| gowli | gok | 1 | 1 | 7945 |
| greek | grc | 1328 | 1293 | 1013488 |
| guduf-gava | gdf | 1 | 1 | 1749 |
| gujarati | gu | 1 | 1 | 31240 |
| guugu-yimidhirr | kky | 1 | 1 | 9 |
| gyaazi | gyz | 1 | 1 | 5742 |
| halbi | hlb | 1 | 1 | 7959 |
| haryanvi | bgc | 1 | 1 | 7918 |
| hassaniyya | mey | 1 | 1 | 693 |
| hattic | xht | 2 | 1 | 28186 |
| hausa | ha | 15 | 14 | 39841 |
| havu | hav | 1 | 1 | 2155 |
| hawaiian | haw | 2 | 2 | 46613 |
| hebrew | he | 1561 | 1279 | 2404300 |
| hiligaynon | hil | 1 | 1 | 30451 |
| hindi | hi | 2 | 1 | 62446 |
| hittite | hit | 65 | 23 | 29955 |
| hre | hre | 1 | 1 | 11533 |
| hruso | hru | 1 | 1 | 1176 |
| hungarian | hu | 3 | 2 | 39413 |
| hurrian | xhu | 2 | 1 | 36689 |
| hwana | hwo | 1 | 1 | 7953 |
| icelandic | is | 2 | 1 | 10580 |
| idon | idc | 1 | 1 | 3778 |
| igbo | ig | 1 | 1 | 31220 |
| ikizu | ikz | 1 | 1 | 7957 |
| ilocano |  | 1 | 1 | 31090 |
| isanzu | isn | 1 | 1 | 7952 |
| italian | it | 15 | 9 | 107520 |
| jain-maharashtri |  | 1 | 1 | 484 |
| janji | jni | 1 | 1 | 7949 |
| japanese | ja | 38 | 33 | 199960 |
| jumjum | jum | 1 | 1 | 2601 |
| juray | juy | 1 | 1 | 7959 |
| kamano | kbq | 1 | 1 | 31092 |
| kannada | kn | 4 | 2 | 73125 |
| kapin | tbx | 1 | 1 | 5185 |
| kaqchikel | cak | 1 | 1 | 267 |
| kara-tanzania | reg | 1 | 1 | 7951 |
| kiche | quc | 3 | 3 | 9021 |
| kikuyu | ki | 1 | 1 | 31209 |
| kinga | zga | 1 | 1 | 7907 |
| kinshasa-lingala | ln | 1 | 1 | 31168 |
| kisi | kiz | 1 | 1 | 7940 |
| kituba-congo | mkw | 1 | 1 | 31161 |
| koda | cdz | 1 | 1 | 3799 |
| konda-dora | kfc | 1 | 1 | 7897 |
| korean | ko | 10 | 8 | 63386 |
| koromba |  | 1 | 1 | 1071 |
| kosraean | kos | 1 | 1 | 31049 |
| koya | kff | 1 | 1 | 7959 |
| kuhane |  | 1 | 1 | 7929 |
| kurama | krh | 1 | 1 | 710 |
| kuturmi | khj | 1 | 1 | 1151 |
| kuvi | kxv | 1 | 1 | 7870 |
| labwor | lth | 1 | 1 | 8410 |
| latin | la | 746 | 718 | 670027 |
| lithuanian | lt | 3 | 2 | 11127 |
| lodhi | lbm | 1 | 1 | 14434 |
| loxicha-zapotec | ztp | 1 | 1 | 7959 |
| lungga | lga | 1 | 1 | 9614 |
| luo-kenya-and-tanzania | luo | 1 | 1 | 31219 |
| luwian |  | 2 | 1 | 17539 |
| luyana |  | 1 | 1 | 7959 |
| mahasu-pahari | bfz | 1 | 1 | 7954 |
| malayalam | ml | 3 | 1 | 93491 |
| mandaic |  | 1 | 1 | 5189 |
| mandinka | mnk | 13 | 13 | 1124 |
| manx | gv | 1 | 1 | 3994 |
| maori | mi | 2 | 1 | 39176 |
| marathi | mr | 2 | 1 | 62380 |
| marghi-south | mfm | 1 | 1 | 5840 |
| matengo | mgv | 1 | 1 | 7959 |
| mbe | mfo | 1 | 1 | 8106 |
| mbula-bwazza | mbu | 1 | 1 | 16540 |
| melo | mfx | 2 | 1 | 15876 |
| meriam | ulk | 1 | 1 | 3779 |
| middle-english | enm | 5 | 5 | 18645 |
| middle-khmer | xhm | 1 | 1 | 1283 |
| middle-korean |  | 7 | 7 | 581 |
| middle-persian |  | 1 | 1 | 1294 |
| modern-greek | el | 1 | 1 | 31102 |
| mohawk | moh | 1 | 1 | 107 |
| mori-atas | mzq | 1 | 1 | 1152 |
| mpoto | mpa | 1 | 1 | 7959 |
| munda | unx | 1 | 1 | 7958 |
| mwaghavul | sur | 1 | 1 | 3796 |
| naga-pidgin | nag | 1 | 1 | 7959 |
| nahuatl-huasteca |  | 1 | 1 | 100 |
| nahuatl |  | 2 | 2 | 436 |
| navajo | nv | 1 | 1 | 230 |
| ncane-mungong | ncr | 1 | 1 | 7950 |
| ndendeule | dne | 1 | 1 | 7959 |
| ndengereko | ndg | 1 | 1 | 7939 |
| ndonde-hamba | njd | 1 | 1 | 1071 |
| ndwewe | nww | 1 | 1 | 7959 |
| nepali | npi | 2 | 1 | 62313 |
| nga-la | hlt | 3 | 1 | 80335 |
| ngarrindjeri |  | 1 | 1 | 390 |
| nkangala | nkn | 1 | 1 | 6794 |
| norwegian-bokmal | nb | 1 | 1 | 7748 |
| norwegian | no | 3 | 3 | 28517 |
| nsari | asj | 1 | 1 | 7950 |
| nyanja | ny | 1 | 1 | 31220 |
| odia | ory | 1 | 1 | 31242 |
| old-anatolian-turkish |  | 1 | 1 | 1041 |
| old-cham |  | 1 | 1 | 1620 |
| old-church-slavonic | cu | 13 | 9 | 66080 |
| old-east-slavic |  | 4 | 4 | 7674 |
| old-english | ang | 3 | 3 | 7233 |
| old-french | fro | 3 | 3 | 13170 |
| old-javanese |  | 2 | 2 | 5940 |
| old-khmer | qok | 1 | 1 | 18534 |
| old-korean |  | 3 | 3 | 239 |
| old-malay |  | 1 | 1 | 191 |
| old-norse | non | 89 | 59 | 47065 |
| old-turkic | oui | 3 | 3 | 212 |
| onondaga | ono | 1 | 1 | 13 |
| oyda | oyd | 2 | 1 | 15862 |
| padoe | pdo | 1 | 1 | 1150 |
| palaic | plq | 2 | 1 | 3532 |
| pali | pi | 57 | 29 | 663617 |
| palya-bareli | bpx | 1 | 1 | 1071 |
| pengo | peg | 1 | 1 | 7829 |
| persian | fa | 73 | 73 | 730411 |
| pohnpeian | pon | 2 | 1 | 20830 |
| polci |  | 1 | 1 | 6193 |
| polish | pl | 1 | 1 | 7915 |
| portuguese | pt | 8 | 5 | 88618 |
| powari | pwr | 1 | 1 | 5656 |
| prakrit |  | 15 | 15 | 12736 |
| punjabi | pa | 6 | 6 | 11807 |
| punu | puu | 1 | 1 | 2263 |
| purum | pub | 1 | 1 | 672 |
| rakhine | rki | 1 | 1 | 7923 |
| rana-tharu | thr | 1 | 1 | 7959 |
| rangi |  | 1 | 1 | 7957 |
| reli | rei | 1 | 1 | 3534 |
| rohingya | rhg | 1 | 1 | 5683 |
| romanian | ro | 6 | 2 | 72393 |
| russian | ru | 6 | 6 | 39066 |
| ruthenian |  | 1 | 1 | 673 |
| safen |  | 1 | 1 | 10672 |
| safwa | sbk | 1 | 1 | 7951 |
| sakachep-chorei | sch | 1 | 1 | 7912 |
| salka-tsishingini | tsw | 1 | 1 | 1929 |
| sanga-nigeria | xsn | 1 | 1 | 2222 |
| sanskrit | sa | 1672 | 826 | 1574058 |
| santa |  | 1 | 1 | 7920 |
| saraiki | skr | 2 | 2 | 4006 |
| satawalese | stw | 1 | 1 | 3770 |
| serbian-standard | sr | 4 | 1 | 124910 |
| serbian |  | 2 | 2 | 17160 |
| shi | shr | 1 | 1 | 35457 |
| sholaga | sle | 1 | 1 | 7957 |
| shona | sn | 1 | 1 | 31219 |
| shwe-palaung | pll | 1 | 1 | 675 |
| sizang-chin | csy | 1 | 1 | 7959 |
| slovak | sk | 1 | 1 | 7955 |
| soli | sby | 1 | 1 | 7959 |
| south-sudanese-creole-arabic | pga | 1 | 1 | 375 |
| southeastern-kolami | nit | 1 | 1 | 7933 |
| spanish | es | 14 | 8 | 232424 |
| standard-indonesian | id | 2 | 1 | 28590 |
| sumau | six | 1 | 1 | 2932 |
| sumerian | sux | 443 | 439 | 57206 |
| swahili | swh | 4 | 1 | 101393 |
| swedish | sv | 1 | 1 | 31150 |
| syriac | syc | 54 | 53 | 67007 |
| taabwa | tap | 1 | 1 | 5061 |
| tagakaulu-kalagan | klg | 1 | 1 | 7937 |
| tagalog | tl | 2 | 1 | 62207 |
| tamil | ta | 33 | 31 | 132802 |
| tandroy-malagasy | tdx | 1 | 1 | 31075 |
| tanzanian-ngoni | xnj | 1 | 1 | 7959 |
| tarok | yer | 1 | 1 | 10499 |
| tavoyan | tvn | 1 | 1 | 7941 |
| teke-tyee | tyx | 1 | 1 | 7957 |
| telugu | te | 3 | 2 | 63304 |
| thado-chin | tcz | 1 | 1 | 31063 |
| thai | th | 1 | 1 | 28439 |
| thaipum-chin | cth | 1 | 1 | 31275 |
| thayore | thd | 1 | 1 | 170 |
| tibetan | bo | 4732 | 4728 | 433317 |
| tichurong | tcn | 1 | 1 | 1886 |
| toka-leya-dombe | dov | 1 | 1 | 7954 |
| tonga-tonga-islands | to | 1 | 1 | 31218 |
| tsikimba | kdl | 1 | 1 | 1149 |
| tswana | tn | 1 | 1 | 7586 |
| turkish | tr | 8 | 8 | 12608 |
| twi | tw | 2 | 1 | 62543 |
| ugaritic | uga | 18 | 9 | 15232 |
| uighur | ug | 4 | 1 | 123300 |
| ukrainian | uk | 3 | 1 | 49516 |
| urartian | xur | 2 | 2 | 6979 |
| urdu | ur | 2 | 1 | 62341 |
| ut-main | gel | 1 | 1 | 5255 |
| vaagri-booli | vaa | 1 | 1 | 7936 |
| vaghri | vgr | 1 | 1 | 7949 |
| vietnamese | vi | 3 | 2 | 64114 |
| vlax-romani | rmy | 6 | 1 | 26362 |
| vwanji | wbi | 1 | 1 | 7948 |
| waddar | wbq | 1 | 1 | 3793 |
| waja | wja | 1 | 1 | 1764 |
| welsh | cy | 112 | 112 | 8712 |
| west-central-oromo | gaz | 2 | 1 | 62438 |
| western-farsi | pes | 2 | 1 | 60788 |
| wolio | wlo | 1 | 1 | 12471 |
| wolof | wo | 14 | 14 | 3953 |
| worrorra | wro | 1 | 1 | 1829 |
| yaka-congo | iyx | 1 | 1 | 7947 |
| yaka-pelende-lonzo | yaf | 1 | 1 | 7106 |
| yale | nce | 1 | 1 | 3513 |
| yamap | ymp | 1 | 1 | 2856 |
| yansi | yns | 1 | 1 | 7958 |
| yao | yao | 1 | 1 | 7959 |
| yemsa | jnj | 2 | 1 | 15848 |
| yiddish |  | 1 | 1 | 11633 |
| yinjibarndi |  | 1 | 1 | 16 |
| yombe | yom | 1 | 1 | 10530 |
| yoruba | yo | 1 | 1 | 31203 |
| yucatec-maya | yua | 1 | 1 | 338 |
| zanaki | zak | 1 | 1 | 7937 |
| zaramo | zaj | 1 | 1 | 10700 |
| zinza | zin | 1 | 1 | 7945 |

Verify: `manifest.json` is the signed release (Ed25519 key `fa60df0234a34132` in `publisher.json`, signature `manifest.json.sig`, sha256 `de5c1dff45cfdd46191536f34280a6edceb171b0913a7221ac985d49fb08d7c7`); every `sha256` above is an object it lists. Format textsurf-archive/1.

The names text.surf and ClueSurf are trademarks. A copy may say it derives from text.surf and may not be called text.surf.
