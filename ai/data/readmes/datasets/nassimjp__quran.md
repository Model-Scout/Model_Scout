---
license: other
license_name: mixed-per-config
pretty_name: "QuranLab — Verse-Aligned Multilingual Quran Corpus"
language:
  - ar
  - aa
  - ace
  - af
  - am
  - as
  - az
  - bg
  - bm
  - bn
  - bs
  - dag
  - de
  - dv
  - en
  - es
  - fa
  - ff
  - fil
  - fr
  - gu
  - ha
  - he
  - hi
  - hu
  - id
  - ilp
  - it
  - ja
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - ln
  - luy
  - mk
  - ml
  - mr
  - mrw
  - ms
  - mt
  - my
  - ne
  - nl
  - ny
  - om
  - prs
  - ps
  - pt
  - ru
  - run
  - rw
  - sd
  - si
  - sn
  - so
  - sq
  - sr
  - st
  - sw
  - ta
  - te
  - tg
  - th
  - tr
  - tt
  - tw
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yo
  - yuw
  - zh
  - zu
task_categories:
  - text-generation
  - translation
  - text-retrieval
  - question-answering
annotations_creators:
  - expert-generated
language_creators:
  - expert-generated
  - found
multilinguality:
  - multilingual
source_datasets:
  - original
size_categories:
  - 1M<n<10M
tags:
  - quran
  - islam
  - arabic
  - multilingual
  - religious-text
  - ahl-sunnah
  - verse-aligned
  - parallel-corpus
  - tafsir
  - morphology
  - low-resource-languages
  - text
  - datasets
  - pandas
  - dask
  - mlcroissant
configs:
  - config_name: arabic-uthmani
    default: true
    data_files:
      - split: train
        path: "arabic-uthmani/train-*.parquet"
  - config_name: arabic-simple-clean
    data_files:
      - split: train
        path: "arabic-simple-clean/train-*.parquet"
  - config_name: en-pickthall
    data_files:
      - split: train
        path: "en-pickthall/train-*.parquet"
  - config_name: en-yusufali
    data_files:
      - split: train
        path: "en-yusufali/train-*.parquet"
  - config_name: tr-elmalili
    data_files:
      - split: train
        path: "tr-elmalili/train-*.parquet"
  - config_name: aa-sheikhmahmoudab
    data_files:
      - split: train
        path: "aa-sheikhmahmoudab/train-*.parquet"
  - config_name: ace-tgkhmahjiddinju
    data_files:
      - split: train
        path: "ace-tgkhmahjiddinju/train-*.parquet"
  - config_name: af-imammabaker
    data_files:
      - split: train
        path: "af-imammabaker/train-*.parquet"
  - config_name: am-muhammedsadiqan
    data_files:
      - split: train
        path: "am-muhammedsadiqan/train-*.parquet"
  - config_name: as-shaykhrafeequli
    data_files:
      - split: train
        path: "as-shaykhrafeequli/train-*.parquet"
  - config_name: az-alikhanmusayev
    data_files:
      - split: train
        path: "az-alikhanmusayev/train-*.parquet"
  - config_name: az-khanmusayev
    data_files:
      - split: train
        path: "az-khanmusayev/train-*.parquet"
  - config_name: az-vasimmammadaliy
    data_files:
      - split: train
        path: "az-vasimmammadaliy/train-*.parquet"
  - config_name: bg-tzvetantheophan
    data_files:
      - split: train
        path: "bg-tzvetantheophan/train-*.parquet"
  - config_name: bm-fodisulimankant
    data_files:
      - split: train
        path: "bm-fodisulimankant/train-*.parquet"
  - config_name: bm-karamobabamamad
    data_files:
      - split: train
        path: "bm-karamobabamamad/train-*.parquet"
  - config_name: bn-abubakrzakaria
    data_files:
      - split: train
        path: "bn-abubakrzakaria/train-*.parquet"
  - config_name: bn-muhiuddinkhan
    data_files:
      - split: train
        path: "bn-muhiuddinkhan/train-*.parquet"
  - config_name: bs-besimkorkut
    data_files:
      - split: train
        path: "bs-besimkorkut/train-*.parquet"
  - config_name: bs-korkut
    data_files:
      - split: train
        path: "bs-korkut/train-*.parquet"
  - config_name: bs-muhamedmehanovi
    data_files:
      - split: train
        path: "bs-muhamedmehanovi/train-*.parquet"
  - config_name: bs-wwwislamhouseco
    data_files:
      - split: train
        path: "bs-wwwislamhouseco/train-*.parquet"
  - config_name: dag-muhammadbabaght
    data_files:
      - split: train
        path: "dag-muhammadbabaght/train-*.parquet"
  - config_name: de-aburidamuhammad
    data_files:
      - split: train
        path: "de-aburidamuhammad/train-*.parquet"
  - config_name: de-amirzaidan
    data_files:
      - split: train
        path: "de-amirzaidan/train-*.parquet"
  - config_name: de-asfbubenheimand
    data_files:
      - split: train
        path: "de-asfbubenheimand/train-*.parquet"
  - config_name: de-frankbubenheima
    data_files:
      - split: train
        path: "de-frankbubenheima/train-*.parquet"
  - config_name: dv-officeofthepres
    data_files:
      - split: train
        path: "dv-officeofthepres/train-*.parquet"
  - config_name: en-abdelhaleem
    data_files:
      - split: train
        path: "en-abdelhaleem/train-*.parquet"
  - config_name: en-abdulhye
    data_files:
      - split: train
        path: "en-abdulhye/train-*.parquet"
  - config_name: en-almuntakhabfita
    data_files:
      - split: train
        path: "en-almuntakhabfita/train-*.parquet"
  - config_name: en-bewley
    data_files:
      - split: train
        path: "en-bewley/train-*.parquet"
  - config_name: en-clearquran
    data_files:
      - split: train
        path: "en-clearquran/train-*.parquet"
  - config_name: en-clearquran-god
    data_files:
      - split: train
        path: "en-clearquran-god/train-*.parquet"
  - config_name: en-daryabadi
    data_files:
      - split: train
        path: "en-daryabadi/train-*.parquet"
  - config_name: en-farookmalik
    data_files:
      - split: train
        path: "en-farookmalik/train-*.parquet"
  - config_name: en-hilali-khan
    data_files:
      - split: train
        path: "en-hilali-khan/train-*.parquet"
  - config_name: en-maududi
    data_files:
      - split: train
        path: "en-maududi/train-*.parquet"
  - config_name: en-miraneesuddin
    data_files:
      - split: train
        path: "en-miraneesuddin/train-*.parquet"
  - config_name: en-mohammadshafi
    data_files:
      - split: train
        path: "en-mohammadshafi/train-*.parquet"
  - config_name: en-mubarakpuri
    data_files:
      - split: train
        path: "en-mubarakpuri/train-*.parquet"
  - config_name: en-muhammadmahmoud
    data_files:
      - split: train
        path: "en-muhammadmahmoud/train-*.parquet"
  - config_name: en-rowwadtranslati
    data_files:
      - split: train
        path: "en-rowwadtranslati/train-*.parquet"
  - config_name: en-safikaskas
    data_files:
      - split: train
        path: "en-safikaskas/train-*.parquet"
  - config_name: en-saheeh
    data_files:
      - split: train
        path: "en-saheeh/train-*.parquet"
  - config_name: en-syedvickarahame
    data_files:
      - split: train
        path: "en-syedvickarahame/train-*.parquet"
  - config_name: en-tbirving
    data_files:
      - split: train
        path: "en-tbirving/train-*.parquet"
  - config_name: en-ummmuhammad
    data_files:
      - split: train
        path: "en-ummmuhammad/train-*.parquet"
  - config_name: en-usmani
    data_files:
      - split: train
        path: "en-usmani/train-*.parquet"
  - config_name: es-abdulqadermouhe
    data_files:
      - split: train
        path: "es-abdulqadermouhe/train-*.parquet"
  - config_name: es-islamicfoundati
    data_files:
      - split: train
        path: "es-islamicfoundati/train-*.parquet"
  - config_name: es-islamicfoundati1
    data_files:
      - split: train
        path: "es-islamicfoundati1/train-*.parquet"
  - config_name: es-muhammadisagarc
    data_files:
      - split: train
        path: "es-muhammadisagarc/train-*.parquet"
  - config_name: fa-drhussientagi
    data_files:
      - split: train
        path: "fa-drhussientagi/train-*.parquet"
  - config_name: fa-islamhousecompe
    data_files:
      - split: train
        path: "fa-islamhousecompe/train-*.parquet"
  - config_name: fa-mostafakhorramd
    data_files:
      - split: train
        path: "fa-mostafakhorramd/train-*.parquet"
  - config_name: ff-rowadtranslatio
    data_files:
      - split: train
        path: "ff-rowadtranslatio/train-*.parquet"
  - config_name: fil-abdullatifeduar
    data_files:
      - split: train
        path: "fil-abdullatifeduar/train-*.parquet"
  - config_name: fil-wwwislamhouseco
    data_files:
      - split: train
        path: "fil-wwwislamhouseco/train-*.parquet"
  - config_name: fr-islamicfoundati
    data_files:
      - split: train
        path: "fr-islamicfoundati/train-*.parquet"
  - config_name: fr-muhammadhameedu
    data_files:
      - split: train
        path: "fr-muhammadhameedu/train-*.parquet"
  - config_name: fr-muhammadhamidul
    data_files:
      - split: train
        path: "fr-muhammadhamidul/train-*.parquet"
  - config_name: fr-rashidmaash
    data_files:
      - split: train
        path: "fr-rashidmaash/train-*.parquet"
  - config_name: gu-rabilaalomari
    data_files:
      - split: train
        path: "gu-rabilaalomari/train-*.parquet"
  - config_name: ha-abubakarmahmood
    data_files:
      - split: train
        path: "ha-abubakarmahmood/train-*.parquet"
  - config_name: ha-abubakarmahmoud
    data_files:
      - split: train
        path: "ha-abubakarmahmoud/train-*.parquet"
  - config_name: he-darusalamhousei
    data_files:
      - split: train
        path: "he-darusalamhousei/train-*.parquet"
  - config_name: hi-maulanaazizulha
    data_files:
      - split: train
        path: "hi-maulanaazizulha/train-*.parquet"
  - config_name: hi-muhammadfarooqk
    data_files:
      - split: train
        path: "hi-muhammadfarooqk/train-*.parquet"
  - config_name: hi-suhelfarooqkhan
    data_files:
      - split: train
        path: "hi-suhelfarooqkhan/train-*.parquet"
  - config_name: hu-drahmedabdelrah
    data_files:
      - split: train
        path: "hu-drahmedabdelrah/train-*.parquet"
  - config_name: id-indonesianislam
    data_files:
      - split: train
        path: "id-indonesianislam/train-*.parquet"
  - config_name: id-jalaladdinalmah
    data_files:
      - split: train
        path: "id-jalaladdinalmah/train-*.parquet"
  - config_name: id-kingfahdcomplex
    data_files:
      - split: train
        path: "id-kingfahdcomplex/train-*.parquet"
  - config_name: id-muhammadquraish
    data_files:
      - split: train
        path: "id-muhammadquraish/train-*.parquet"
  - config_name: id-thesabiqcompany
    data_files:
      - split: train
        path: "id-thesabiqcompany/train-*.parquet"
  - config_name: ilp-abdulazizgroaal
    data_files:
      - split: train
        path: "ilp-abdulazizgroaal/train-*.parquet"
  - config_name: it-hamzarobertopic
    data_files:
      - split: train
        path: "it-hamzarobertopic/train-*.parquet"
  - config_name: ja-ryoichimita
    data_files:
      - split: train
        path: "ja-ryoichimita/train-*.parquet"
  - config_name: kk-khalifahaltai
    data_files:
      - split: train
        path: "kk-khalifahaltai/train-*.parquet"
  - config_name: kk-khalifahaltaich
    data_files:
      - split: train
        path: "kk-khalifahaltaich/train-*.parquet"
  - config_name: km-cambodianmuslim
    data_files:
      - split: train
        path: "km-cambodianmuslim/train-*.parquet"
  - config_name: kn-abdussalamputhi
    data_files:
      - split: train
        path: "kn-abdussalamputhi/train-*.parquet"
  - config_name: ko-hamidchoi
    data_files:
      - split: train
        path: "ko-hamidchoi/train-*.parquet"
  - config_name: ko-unknown
    data_files:
      - split: train
        path: "ko-unknown/train-*.parquet"
  - config_name: ku-burhanmuhammada
    data_files:
      - split: train
        path: "ku-burhanmuhammada/train-*.parquet"
  - config_name: ku-muhammadsalehba
    data_files:
      - split: train
        path: "ku-muhammadsalehba/train-*.parquet"
  - config_name: ky-shamsaldinhakim
    data_files:
      - split: train
        path: "ky-shamsaldinhakim/train-*.parquet"
  - config_name: ln-zakariyamuhamme
    data_files:
      - split: train
        path: "ln-zakariyamuhamme/train-*.parquet"
  - config_name: luy-mohammadramadha
    data_files:
      - split: train
        path: "luy-mohammadramadha/train-*.parquet"
  - config_name: mk-macedonianschol
    data_files:
      - split: train
        path: "mk-macedonianschol/train-*.parquet"
  - config_name: mk-sheikhhassangil
    data_files:
      - split: train
        path: "mk-sheikhhassangil/train-*.parquet"
  - config_name: ml-abdulhameedmada
    data_files:
      - split: train
        path: "ml-abdulhameedmada/train-*.parquet"
  - config_name: ml-cheriyamundamab
    data_files:
      - split: train
        path: "ml-cheriyamundamab/train-*.parquet"
  - config_name: ml-muhammadkarakun
    data_files:
      - split: train
        path: "ml-muhammadkarakun/train-*.parquet"
  - config_name: mr-muhammadshafiia
    data_files:
      - split: train
        path: "mr-muhammadshafiia/train-*.parquet"
  - config_name: mrw-guroalimsaroman
    data_files:
      - split: train
        path: "mrw-guroalimsaroman/train-*.parquet"
  - config_name: ms-abdullahmuhamma
    data_files:
      - split: train
        path: "ms-abdullahmuhamma/train-*.parquet"
  - config_name: mt-martinrzammitmu
    data_files:
      - split: train
        path: "mt-martinrzammitmu/train-*.parquet"
  - config_name: my-basein
    data_files:
      - split: train
        path: "my-basein/train-*.parquet"
  - config_name: my-ghazimohammadha
    data_files:
      - split: train
        path: "my-ghazimohammadha/train-*.parquet"
  - config_name: my-hashimtinmyint
    data_files:
      - split: train
        path: "my-hashimtinmyint/train-*.parquet"
  - config_name: ne-ahlalhadithcent
    data_files:
      - split: train
        path: "ne-ahlalhadithcent/train-*.parquet"
  - config_name: nl-sofianssiregar
    data_files:
      - split: train
        path: "nl-sofianssiregar/train-*.parquet"
  - config_name: ny-alhajiyusufmuha
    data_files:
      - split: train
        path: "ny-alhajiyusufmuha/train-*.parquet"
  - config_name: ny-khaledibrahimbe
    data_files:
      - split: train
        path: "ny-khaledibrahimbe/train-*.parquet"
  - config_name: om-ghaliapapurapag
    data_files:
      - split: train
        path: "om-ghaliapapurapag/train-*.parquet"
  - config_name: prs-mawlawimuhammad
    data_files:
      - split: train
        path: "prs-mawlawimuhammad/train-*.parquet"
  - config_name: ps-abdulwalikhan
    data_files:
      - split: train
        path: "ps-abdulwalikhan/train-*.parquet"
  - config_name: ps-zakariaabulsala
    data_files:
      - split: train
        path: "ps-zakariaabulsala/train-*.parquet"
  - config_name: pt-helminasr
    data_files:
      - split: train
        path: "pt-helminasr/train-*.parquet"
  - config_name: pt-samirelhayek
    data_files:
      - split: train
        path: "pt-samirelhayek/train-*.parquet"
  - config_name: ru-abuadel
    data_files:
      - split: train
        path: "ru-abuadel/train-*.parquet"
  - config_name: ru-elmirkuliev
    data_files:
      - split: train
        path: "ru-elmirkuliev/train-*.parquet"
  - config_name: ru-ministryofawqaf
    data_files:
      - split: train
        path: "ru-ministryofawqaf/train-*.parquet"
  - config_name: run-sheikhamissirad
    data_files:
      - split: train
        path: "run-sheikhamissirad/train-*.parquet"
  - config_name: rw-rmcrwanda
    data_files:
      - split: train
        path: "rw-rmcrwanda/train-*.parquet"
  - config_name: rw-rwandamuslimsas
    data_files:
      - split: train
        path: "rw-rwandamuslimsas/train-*.parquet"
  - config_name: sd-tajmehmoodamrot
    data_files:
      - split: train
        path: "sd-tajmehmoodamrot/train-*.parquet"
  - config_name: si-naseemismailand
    data_files:
      - split: train
        path: "si-naseemismailand/train-*.parquet"
  - config_name: si-wwwislamhouseco
    data_files:
      - split: train
        path: "si-wwwislamhouseco/train-*.parquet"
  - config_name: sn-abdullahjmadini
    data_files:
      - split: train
        path: "sn-abdullahjmadini/train-*.parquet"
  - config_name: so-abdullahhasanja
    data_files:
      - split: train
        path: "so-abdullahhasanja/train-*.parquet"
  - config_name: so-mahmudmuhammada
    data_files:
      - split: train
        path: "so-mahmudmuhammada/train-*.parquet"
  - config_name: so-shaykhmahmoodmu
    data_files:
      - split: train
        path: "so-shaykhmahmoodmu/train-*.parquet"
  - config_name: sq-fetimehdiu
    data_files:
      - split: train
        path: "sq-fetimehdiu/train-*.parquet"
  - config_name: sq-hasanefendinahi
    data_files:
      - split: train
        path: "sq-hasanefendinahi/train-*.parquet"
  - config_name: sq-hassannahi
    data_files:
      - split: train
        path: "sq-hassannahi/train-*.parquet"
  - config_name: sq-sherifahmeti
    data_files:
      - split: train
        path: "sq-sherifahmeti/train-*.parquet"
  - config_name: sr-rowwadtranslati
    data_files:
      - split: train
        path: "sr-rowwadtranslati/train-*.parquet"
  - config_name: st-sheikheliaskeke
    data_files:
      - split: train
        path: "st-sheikheliaskeke/train-*.parquet"
  - config_name: sw-abdullahmuhamma
    data_files:
      - split: train
        path: "sw-abdullahmuhamma/train-*.parquet"
  - config_name: ta-abdulhameedbaqa
    data_files:
      - split: train
        path: "ta-abdulhameedbaqa/train-*.parquet"
  - config_name: ta-janturstfoundat
    data_files:
      - split: train
        path: "ta-janturstfoundat/train-*.parquet"
  - config_name: te-abdulraheemmoha
    data_files:
      - split: train
        path: "te-abdulraheemmoha/train-*.parquet"
  - config_name: te-muhammadazizurr
    data_files:
      - split: train
        path: "te-muhammadazizurr/train-*.parquet"
  - config_name: tg-khojamirov
    data_files:
      - split: train
        path: "tg-khojamirov/train-*.parquet"
  - config_name: tg-wwwislamhouseco
    data_files:
      - split: train
        path: "tg-wwwislamhouseco/train-*.parquet"
  - config_name: th-groupfromthesoc
    data_files:
      - split: train
        path: "th-groupfromthesoc/train-*.parquet"
  - config_name: th-kingfahadquranc
    data_files:
      - split: train
        path: "th-kingfahadquranc/train-*.parquet"
  - config_name: tr-ademugur
    data_files:
      - split: train
        path: "tr-ademugur/train-*.parquet"
  - config_name: tr-alibulac
    data_files:
      - split: train
        path: "tr-alibulac/train-*.parquet"
  - config_name: tr-alifikriyavuz
    data_files:
      - split: train
        path: "tr-alifikriyavuz/train-*.parquet"
  - config_name: tr-cantay
    data_files:
      - split: train
        path: "tr-cantay/train-*.parquet"
  - config_name: tr-celalyildirim
    data_files:
      - split: train
        path: "tr-celalyildirim/train-*.parquet"
  - config_name: tr-diyanet
    data_files:
      - split: train
        path: "tr-diyanet/train-*.parquet"
  - config_name: tr-diyanet-eski
    data_files:
      - split: train
        path: "tr-diyanet-eski/train-*.parquet"
  - config_name: tr-elmalili-sade
    data_files:
      - split: train
        path: "tr-elmalili-sade/train-*.parquet"
  - config_name: tr-elmalili-sade2
    data_files:
      - split: train
        path: "tr-elmalili-sade2/train-*.parquet"
  - config_name: tr-fizilal
    data_files:
      - split: train
        path: "tr-fizilal/train-*.parquet"
  - config_name: tr-ibnkesir
    data_files:
      - split: train
        path: "tr-ibnkesir/train-*.parquet"
  - config_name: tr-islamhouse
    data_files:
      - split: train
        path: "tr-islamhouse/train-*.parquet"
  - config_name: tr-muhammetabay
    data_files:
      - split: train
        path: "tr-muhammetabay/train-*.parquet"
  - config_name: tr-muslumsahin
    data_files:
      - split: train
        path: "tr-muslumsahin/train-*.parquet"
  - config_name: tr-sabanbritch
    data_files:
      - split: train
        path: "tr-sabanbritch/train-*.parquet"
  - config_name: tr-sabanpiris
    data_files:
      - split: train
        path: "tr-sabanpiris/train-*.parquet"
  - config_name: tr-tdv
    data_files:
      - split: train
        path: "tr-tdv/train-*.parquet"
  - config_name: tr-tefhim
    data_files:
      - split: train
        path: "tr-tefhim/train-*.parquet"
  - config_name: tt-yakubibnnugman
    data_files:
      - split: train
        path: "tt-yakubibnnugman/train-*.parquet"
  - config_name: tw-sheikhharounism
    data_files:
      - split: train
        path: "tw-sheikhharounism/train-*.parquet"
  - config_name: ug-muhammadsaleh
    data_files:
      - split: train
        path: "ug-muhammadsaleh/train-*.parquet"
  - config_name: ug-shaykhmuhammads
    data_files:
      - split: train
        path: "ug-shaykhmuhammads/train-*.parquet"
  - config_name: uk-drmikhailoyaqub
    data_files:
      - split: train
        path: "uk-drmikhailoyaqub/train-*.parquet"
  - config_name: uk-mykhayloyakubov
    data_files:
      - split: train
        path: "uk-mykhayloyakubov/train-*.parquet"
  - config_name: uk-yakubovych
    data_files:
      - split: train
        path: "uk-yakubovych/train-*.parquet"
  - config_name: ur-abulaalamaududi
    data_files:
      - split: train
        path: "ur-abulaalamaududi/train-*.parquet"
  - config_name: ur-fatehmuhammadja
    data_files:
      - split: train
        path: "ur-fatehmuhammadja/train-*.parquet"
  - config_name: ur-mahmoodulhassan
    data_files:
      - split: train
        path: "ur-mahmoodulhassan/train-*.parquet"
  - config_name: ur-muhammadjunagar
    data_files:
      - split: train
        path: "ur-muhammadjunagar/train-*.parquet"
  - config_name: ur-muhammadjunagar1
    data_files:
      - split: train
        path: "ur-muhammadjunagar1/train-*.parquet"
  - config_name: ur-muhammadkaramsh
    data_files:
      - split: train
        path: "ur-muhammadkaramsh/train-*.parquet"
  - config_name: ur-muhammadtaqiusm
    data_files:
      - split: train
        path: "ur-muhammadtaqiusm/train-*.parquet"
  - config_name: uz-alaaudeenmansou
    data_files:
      - split: train
        path: "uz-alaaudeenmansou/train-*.parquet"
  - config_name: uz-alauddinmansour
    data_files:
      - split: train
        path: "uz-alauddinmansour/train-*.parquet"
  - config_name: uz-muhammadsodikmu
    data_files:
      - split: train
        path: "uz-muhammadsodikmu/train-*.parquet"
  - config_name: vi-hassanabdulkari
    data_files:
      - split: train
        path: "vi-hassanabdulkari/train-*.parquet"
  - config_name: vi-rowwadtranslati
    data_files:
      - split: train
        path: "vi-rowwadtranslati/train-*.parquet"
  - config_name: xh-imaamismaaeelng
    data_files:
      - split: train
        path: "xh-imaamismaaeelng/train-*.parquet"
  - config_name: yo-shaykhaburahima
    data_files:
      - split: train
        path: "yo-shaykhaburahima/train-*.parquet"
  - config_name: yuw-muhammadbinabdu
    data_files:
      - split: train
        path: "yuw-muhammadbinabdu/train-*.parquet"
  - config_name: zh-anonymousgroupo
    data_files:
      - split: train
        path: "zh-anonymousgroupo/train-*.parquet"
  - config_name: zh-majian
    data_files:
      - split: train
        path: "zh-majian/train-*.parquet"
  - config_name: zh-majian1
    data_files:
      - split: train
        path: "zh-majian1/train-*.parquet"
  - config_name: zh-mazhonggang
    data_files:
      - split: train
        path: "zh-mazhonggang/train-*.parquet"
  - config_name: zh-muhammadmakin
    data_files:
      - split: train
        path: "zh-muhammadmakin/train-*.parquet"
  - config_name: zu-iqembulezifundi
    data_files:
      - split: train
        path: "zu-iqembulezifundi/train-*.parquet"
  - config_name: tr-kuranyolu
    data_files:
      - split: train
        path: "tr-kuranyolu/train-*.parquet"
  - config_name: tafsir-kuranyolu-tr
    data_files:
      - split: train
        path: "tafsir-kuranyolu-tr/train-*.parquet"
  - config_name: tafsir-kuranyolu-tr-verses
    data_files:
      - split: train
        path: "tafsir-kuranyolu-tr-verses/train-*.parquet"
  - config_name: tafsir-ibnkathir-ar
    data_files:
      - split: train
        path: "tafsir-ibnkathir-ar/train-*.parquet"
  - config_name: tafsir-tabari-ar
    data_files:
      - split: train
        path: "tafsir-tabari-ar/train-*.parquet"
  - config_name: tafsir-qurtubi-ar
    data_files:
      - split: train
        path: "tafsir-qurtubi-ar/train-*.parquet"
  - config_name: tafsir-baghawi-ar
    data_files:
      - split: train
        path: "tafsir-baghawi-ar/train-*.parquet"
  - config_name: tafsir-nasafi-ar
    data_files:
      - split: train
        path: "tafsir-nasafi-ar/train-*.parquet"
  - config_name: tafsir-jalalayn-ar
    data_files:
      - split: train
        path: "tafsir-jalalayn-ar/train-*.parquet"
  - config_name: tafsir-ibnatiyya-ar
    data_files:
      - split: train
        path: "tafsir-ibnatiyya-ar/train-*.parquet"
  - config_name: tafsir-ibnaljawzi-ar
    data_files:
      - split: train
        path: "tafsir-ibnaljawzi-ar/train-*.parquet"
  - config_name: tafsir-abussuud-ar
    data_files:
      - split: train
        path: "tafsir-abussuud-ar/train-*.parquet"
  - config_name: tafsir-razi-ar
    data_files:
      - split: train
        path: "tafsir-razi-ar/train-*.parquet"
  - config_name: tafsir-bahrmuhit-ar
    data_files:
      - split: train
        path: "tafsir-bahrmuhit-ar/train-*.parquet"
  - config_name: tafsir-alusi-ar
    data_files:
      - split: train
        path: "tafsir-alusi-ar/train-*.parquet"
  - config_name: tafsir-biqai-ar
    data_files:
      - split: train
        path: "tafsir-biqai-ar/train-*.parquet"
  - config_name: tafsir-samani-ar
    data_files:
      - split: train
        path: "tafsir-samani-ar/train-*.parquet"
  - config_name: tafsir-ibnjuzay-ar
    data_files:
      - split: train
        path: "tafsir-ibnjuzay-ar/train-*.parquet"
  - config_name: tafsir-durrmanthur-ar
    data_files:
      - split: train
        path: "tafsir-durrmanthur-ar/train-*.parquet"
  - config_name: tafsir-ibnabizamanin-ar
    data_files:
      - split: train
        path: "tafsir-ibnabizamanin-ar/train-*.parquet"
  - config_name: tafsir-mawardi-ar
    data_files:
      - split: train
        path: "tafsir-mawardi-ar/train-*.parquet"
  - config_name: tafsir-semerkandi-ar
    data_files:
      - split: train
        path: "tafsir-semerkandi-ar/train-*.parquet"
  - config_name: tafsir-ibnadil-ar
    data_files:
      - split: train
        path: "tafsir-ibnadil-ar/train-*.parquet"
  - config_name: tafsir-qasimi-ar
    data_files:
      - split: train
        path: "tafsir-qasimi-ar/train-*.parquet"
  - config_name: tafsir-sealibi-ar
    data_files:
      - split: train
        path: "tafsir-sealibi-ar/train-*.parquet"
  - config_name: tafsir-makki-ar
    data_files:
      - split: train
        path: "tafsir-makki-ar/train-*.parquet"
  - config_name: tafsir-iji-ar
    data_files:
      - split: train
        path: "tafsir-iji-ar/train-*.parquet"
  - config_name: tafsir-thalabi-ar
    data_files:
      - split: train
        path: "tafsir-thalabi-ar/train-*.parquet"
  - config_name: tafsir-shawkani-ar
    data_files:
      - split: train
        path: "tafsir-shawkani-ar/train-*.parquet"
  - config_name: tafsir-qanuji-ar
    data_files:
      - split: train
        path: "tafsir-qanuji-ar/train-*.parquet"
  - config_name: tafsir-wajiz-wahidi-ar
    data_files:
      - split: train
        path: "tafsir-wajiz-wahidi-ar/train-*.parquet"
  - config_name: tafsir-basit-wahidi-ar
    data_files:
      - split: train
        path: "tafsir-basit-wahidi-ar/train-*.parquet"
  - config_name: tafsir-durrmasun-ar
    data_files:
      - split: train
        path: "tafsir-durrmasun-ar/train-*.parquet"
  - config_name: tafsir-baydawi-ar
    data_files:
      - split: train
        path: "tafsir-baydawi-ar/train-*.parquet"
  - config_name: tafsir-ibnabihatim-ar
    data_files:
      - split: train
        path: "tafsir-ibnabihatim-ar/train-*.parquet"
  - config_name: tafsir-saadi-ar
    data_files:
      - split: train
        path: "tafsir-saadi-ar/train-*.parquet"
  - config_name: tafsir-muyassar-ar
    data_files:
      - split: train
        path: "tafsir-muyassar-ar/train-*.parquet"
  - config_name: tafsir-mukhtasar-en
    data_files:
      - split: train
        path: "tafsir-mukhtasar-en/train-*.parquet"
  - config_name: morphology-ar
    data_files:
      - split: train
        path: "morphology-ar/train-*.parquet"
  - config_name: tafsir-yahya-ibn-sallam-ar
    data_files:
      - split: train
        path: "tafsir-yahya-ibn-sallam-ar/train-*.parquet"
  - config_name: tafsir-ibn-mundhir-ar
    data_files:
      - split: train
        path: "tafsir-ibn-mundhir-ar/train-*.parquet"
  - config_name: tafsir-ijaz-bayan-ar
    data_files:
      - split: train
        path: "tafsir-ijaz-bayan-ar/train-*.parquet"
  - config_name: tafsir-taysir-nasafi-ar
    data_files:
      - split: train
        path: "tafsir-taysir-nasafi-ar/train-*.parquet"
  - config_name: tafsir-uleymi-ar
    data_files:
      - split: train
        path: "tafsir-uleymi-ar/train-*.parquet"
  - config_name: tafsir-abd-al-razzaq-ar
    data_files:
      - split: train
        path: "tafsir-abd-al-razzaq-ar/train-*.parquet"
  - config_name: tafsir-jahdami-ahkam-ar
    data_files:
      - split: train
        path: "tafsir-jahdami-ahkam-ar/train-*.parquet"
  - config_name: tafsir-tahawi-ar
    data_files:
      - split: train
        path: "tafsir-tahawi-ar/train-*.parquet"
  - config_name: tafsir-maturidi-ar
    data_files:
      - split: train
        path: "tafsir-maturidi-ar/train-*.parquet"
  - config_name: tafsir-qushayri-ar
    data_files:
      - split: train
        path: "tafsir-qushayri-ar/train-*.parquet"
  - config_name: tafsir-izz-abdussalam-ar
    data_files:
      - split: train
        path: "tafsir-izz-abdussalam-ar/train-*.parquet"
  - config_name: tafsir-khazin-ar
    data_files:
      - split: train
        path: "tafsir-khazin-ar/train-*.parquet"
  - config_name: tafsir-sufyan-thawri-ar
    data_files:
      - split: train
        path: "tafsir-sufyan-thawri-ar/train-*.parquet"
  - config_name: tafsir-nasai-ar
    data_files:
      - split: train
        path: "tafsir-nasai-ar/train-*.parquet"
  - config_name: tafsir-nizam-naysaburi-ar
    data_files:
      - split: train
        path: "tafsir-nizam-naysaburi-ar/train-*.parquet"
  - config_name: tafsir-ibn-arafa-ar
    data_files:
      - split: train
        path: "tafsir-ibn-arafa-ar/train-*.parquet"
  - config_name: tafsir-tabarani-ar
    data_files:
      - split: train
        path: "tafsir-tabarani-ar/train-*.parquet"
  - config_name: tafsir-nahrmadd-ar
    data_files:
      - split: train
        path: "tafsir-nahrmadd-ar/train-*.parquet"
  - config_name: tafsir-sawi-ar
    data_files:
      - split: train
        path: "tafsir-sawi-ar/train-*.parquet"
  - config_name: tafsir-shafii-ahkam-ar
    data_files:
      - split: train
        path: "tafsir-shafii-ahkam-ar/train-*.parquet"
  - config_name: tafsir-asbab-wahidi-ar
    data_files:
      - split: train
        path: "tafsir-asbab-wahidi-ar/train-*.parquet"
  - config_name: tafsir-kiya-harrasi-ahkam-ar
    data_files:
      - split: train
        path: "tafsir-kiya-harrasi-ahkam-ar/train-*.parquet"
  - config_name: tafsir-ibn-al-arabi-ahkam-ar
    data_files:
      - split: train
        path: "tafsir-ibn-al-arabi-ahkam-ar/train-*.parquet"
  - config_name: tafsir-ibn-faras-ar
    data_files:
      - split: train
        path: "tafsir-ibn-faras-ar/train-*.parquet"
  - config_name: tafsir-wasit-wahidi-ar
    data_files:
      - split: train
        path: "tafsir-wasit-wahidi-ar/train-*.parquet"
  - config_name: tafsir-mazhari-ar
    data_files:
      - split: train
        path: "tafsir-mazhari-ar/train-*.parquet"
  - config_name: tafsir-marah-labid-ar
    data_files:
      - split: train
        path: "tafsir-marah-labid-ar/train-*.parquet"
  - config_name: tafsir-siraj-munir-ar
    data_files:
      - split: train
        path: "tafsir-siraj-munir-ar/train-*.parquet"
  - config_name: tafsir-ibn-hajar-cujab-ar
    data_files:
      - split: train
        path: "tafsir-ibn-hajar-cujab-ar/train-*.parquet"
  - config_name: tafsir-ibn-furak-ar
    data_files:
      - split: train
        path: "tafsir-ibn-furak-ar/train-*.parquet"
  - config_name: tafsir-lubab-nuqul-suyuti-ar
    data_files:
      - split: train
        path: "tafsir-lubab-nuqul-suyuti-ar/train-*.parquet"
  - config_name: tafsir-mukhtasar-ar
    data_files:
      - split: train
        path: "tafsir-mukhtasar-ar/train-*.parquet"
  - config_name: tafsir-mukhtasar-as
    data_files:
      - split: train
        path: "tafsir-mukhtasar-as/train-*.parquet"
  - config_name: tafsir-mukhtasar-az
    data_files:
      - split: train
        path: "tafsir-mukhtasar-az/train-*.parquet"
  - config_name: tafsir-mukhtasar-bn
    data_files:
      - split: train
        path: "tafsir-mukhtasar-bn/train-*.parquet"
  - config_name: tafsir-mukhtasar-bs
    data_files:
      - split: train
        path: "tafsir-mukhtasar-bs/train-*.parquet"
  - config_name: tafsir-mukhtasar-zh
    data_files:
      - split: train
        path: "tafsir-mukhtasar-zh/train-*.parquet"
  - config_name: tafsir-mukhtasar-fr
    data_files:
      - split: train
        path: "tafsir-mukhtasar-fr/train-*.parquet"
  - config_name: tafsir-mukhtasar-ff
    data_files:
      - split: train
        path: "tafsir-mukhtasar-ff/train-*.parquet"
  - config_name: tafsir-mukhtasar-hi
    data_files:
      - split: train
        path: "tafsir-mukhtasar-hi/train-*.parquet"
  - config_name: tafsir-mukhtasar-id
    data_files:
      - split: train
        path: "tafsir-mukhtasar-id/train-*.parquet"
  - config_name: tafsir-mukhtasar-it
    data_files:
      - split: train
        path: "tafsir-mukhtasar-it/train-*.parquet"
  - config_name: tafsir-mukhtasar-ja
    data_files:
      - split: train
        path: "tafsir-mukhtasar-ja/train-*.parquet"
  - config_name: tafsir-mukhtasar-km
    data_files:
      - split: train
        path: "tafsir-mukhtasar-km/train-*.parquet"
  - config_name: tafsir-mukhtasar-ku
    data_files:
      - split: train
        path: "tafsir-mukhtasar-ku/train-*.parquet"
  - config_name: tafsir-mukhtasar-ky
    data_files:
      - split: train
        path: "tafsir-mukhtasar-ky/train-*.parquet"
  - config_name: tafsir-mukhtasar-ml
    data_files:
      - split: train
        path: "tafsir-mukhtasar-ml/train-*.parquet"
  - config_name: tafsir-mukhtasar-ps
    data_files:
      - split: train
        path: "tafsir-mukhtasar-ps/train-*.parquet"
  - config_name: tafsir-mukhtasar-fa
    data_files:
      - split: train
        path: "tafsir-mukhtasar-fa/train-*.parquet"
  - config_name: tafsir-mukhtasar-sr
    data_files:
      - split: train
        path: "tafsir-mukhtasar-sr/train-*.parquet"
  - config_name: tafsir-mukhtasar-si
    data_files:
      - split: train
        path: "tafsir-mukhtasar-si/train-*.parquet"
  - config_name: tafsir-mukhtasar-es
    data_files:
      - split: train
        path: "tafsir-mukhtasar-es/train-*.parquet"
  - config_name: tafsir-mukhtasar-fil
    data_files:
      - split: train
        path: "tafsir-mukhtasar-fil/train-*.parquet"
  - config_name: tafsir-mukhtasar-ta
    data_files:
      - split: train
        path: "tafsir-mukhtasar-ta/train-*.parquet"
  - config_name: tafsir-mukhtasar-te
    data_files:
      - split: train
        path: "tafsir-mukhtasar-te/train-*.parquet"
  - config_name: tafsir-mukhtasar-th
    data_files:
      - split: train
        path: "tafsir-mukhtasar-th/train-*.parquet"
  - config_name: tafsir-mukhtasar-tr
    data_files:
      - split: train
        path: "tafsir-mukhtasar-tr/train-*.parquet"
  - config_name: tafsir-mukhtasar-ug
    data_files:
      - split: train
        path: "tafsir-mukhtasar-ug/train-*.parquet"
  - config_name: tafsir-mukhtasar-uz
    data_files:
      - split: train
        path: "tafsir-mukhtasar-uz/train-*.parquet"
  - config_name: tafsir-mukhtasar-vi
    data_files:
      - split: train
        path: "tafsir-mukhtasar-vi/train-*.parquet"
  - config_name: tafsir-yaseer-ar
    data_files:
      - split: train
        path: "tafsir-yaseer-ar/train-*.parquet"
  - config_name: tafsir-nafahat-ar
    data_files:
      - split: train
        path: "tafsir-nafahat-ar/train-*.parquet"
  - config_name: tafsir-muyassar-ar-quranenc
    data_files:
      - split: train
        path: "tafsir-muyassar-ar-quranenc/train-*.parquet"
  - config_name: tafsir-saadi-fa
    data_files:
      - split: train
        path: "tafsir-saadi-fa/train-*.parquet"
  - config_name: tafsir-saadi-tr
    data_files:
      - split: train
        path: "tafsir-saadi-tr/train-*.parquet"
  - config_name: tafsir-saadi-ru
    data_files:
      - split: train
        path: "tafsir-saadi-ru/train-*.parquet"
  - config_name: tafsir-saadi-id
    data_files:
      - split: train
        path: "tafsir-saadi-id/train-*.parquet"
  - config_name: tafsir-saadi-ur
    data_files:
      - split: train
        path: "tafsir-saadi-ur/train-*.parquet"
  - config_name: tafsir-saadi-sw
    data_files:
      - split: train
        path: "tafsir-saadi-sw/train-*.parquet"
  - config_name: tafsir-zakaria-bn
    data_files:
      - split: train
        path: "tafsir-zakaria-bn/train-*.parquet"
  - config_name: tafsir-rowwad-annotated-en
    data_files:
      - split: train
        path: "tafsir-rowwad-annotated-en/train-*.parquet"
  - config_name: tafsir-noor-annotated-en
    data_files:
      - split: train
        path: "tafsir-noor-annotated-en/train-*.parquet"
  - config_name: tafsir-hilali-khan-annotated-en
    data_files:
      - split: train
        path: "tafsir-hilali-khan-annotated-en/train-*.parquet"
  - config_name: tafsir-muyassar-uz
    data_files:
      - split: train
        path: "tafsir-muyassar-uz/train-*.parquet"
  - config_name: parallel
    data_files:
      - split: train
        path: "parallel/train-*.parquet"
---

# QuranLab — Verse-Aligned Multilingual Quran Corpus

A unified, **verse-aligned** multilingual Quran corpus spanning **79
languages** and **185 translations**. Every recension and translation is a
separate **config** (subset), all row-aligned on the canonical **6,236-ayah**
`verse_key` (Hafs ʿan ʿAsim reading, 114 surahs).

The corpus also contains **111 tafsir configs**: verse-grain classical
and openly licensed Arabic works, plus the native-passage and verse-expanded
views of Diyanet's Turkish *Kur'an Yolu* commentary.

> **⚠️ Scope — Ahl al-Sunnah only.** This corpus deliberately includes **only
> translations within mainstream Sunni orthodoxy (Ahl al-Sunnah wa'l-Jamāʿah)**.
> Translations that are Quranist/hadith-rejecting, Shīʿa, Aḥmadiyya, or otherwise
> outside Sunni orthodoxy are intentionally **excluded**. Theological
> classification is documented in `metadata/translations.csv`.

QuranLab is a volunteer effort. Our aim is to present these works carefully and at high quality, and to help them travel faithfully — in the spirit in which they were written — not to claim them as ours.

The text here reaches you through the work of Tanzil Project, fawazahmed0/quran-api, QuranEnc.com, Tafsir Center for Quranic Studies and Quranic Universal Library (QUL), among others. Who to thank, and what we consulted without ever quoting, is set out in [`SOURCES.md`](SOURCES.md).

## At a glance

| | |
|---|---|
| Configs | **300** — 185 translations · 111 tafsir · 2 Arabic recensions · 1 morphology · 1 parallel |
| Languages | **79** |
| Spine | 6,236 ayahs (Ḥafṣ ʿan ʿĀṣim, Kufan numbering), identical across every config |
| Join key | `verse_key` (`"surah:ayah"`, e.g. `2:255`) |
| Format | Parquet · split `train` · loads with `datasets`, `pandas`, `dask`, DuckDB |
| Scope | Ahl al-Sunnah wa'l-Jamāʿah |

## Usage

```python
from datasets import load_dataset

ar  = load_dataset("quranlab/quran")                              # default: arabic-uthmani
en  = load_dataset("quranlab/quran", "en-pickthall", split="train")
tr  = load_dataset("quranlab/quran", "tr-diyanet",   split="train")
par = load_dataset("quranlab/quran", "parallel",     split="train")  # PD/CC aligned
taf = load_dataset("quranlab/quran", "tafsir-kuranyolu-tr", split="train")  # Kur'an Yolu tafsir (passages)
```

## For agents and pipelines

Deterministic facts an automated consumer needs, so nothing has to be inferred
from a sample.

- **Config naming:** `{lang}-{translator}` for translations, `arabic-{recension}`, `tafsir-{work}-{lang}`, `morphology-ar`, `parallel`
- **Join key:** `verse_key` on every config; `morphology-ar` joins one ayah to many segment rows
- **Default config:** `arabic-uthmani`
- **Format:** Parquet, one directory per config, split `train`.
- **Terms and credit** are per config in `metadata/`, never per row — join on the
  config name when you need them.
- **Do not assume a config is complete.** Where a source lacks a verse the cell is empty on purpose; filter on it rather than treating it as a bug.
- The `parallel` config is the only pre-joined wide table and holds public-domain / CC editions only.

Inspect it without downloading the data:

```bash
# every config and split
curl https://datasets-server.huggingface.co/splits?dataset=quranlab/quran

# a first page of rows
curl "https://datasets-server.huggingface.co/first-rows?dataset=quranlab/quran&config=tr-diyanet&split=train"

# machine-readable schema and provenance (Croissant JSON-LD)
curl https://huggingface.co/api/datasets/quranlab/quran/croissant
```

Query it in place with SQL — no full download:

```bash
hf datasets sql quranlab/quran "SELECT * FROM 'tr-diyanet' LIMIT 5"
```

```python
import duckdb
duckdb.sql("SELECT count(*) FROM 'hf://datasets/quranlab/quran/tr-diyanet/*.parquet'")
```

## Schema (per translation/recension config)

`verse_key` (str, e.g. `"1:1"`) · `surah` · `ayah` · `ayah_global` (1–6236)
· `juz` · `hizb` · `hizb_quarter` · `page` · `ruku` · `manzil`
· `sajda` (bool) · `sajda_type` · `surah_name_ar` · `surah_name_en`
· `surah_name_en_translation` · `revelation_place` · `revelation_order`
· `text` · `lang` · `translation_id`

Per-edition credits and terms are not repeated on every row — they are in
`metadata/translations.csv` (one row per config) and `LICENSES.md`.

All configs share the same `verse_key` spine, so cross-language alignment is a
join on `verse_key`. The `parallel` config is a curated wide table of the
license-clean (PD/CC) editions only.

### Tafsir (passage-grouped) configs

The `tafsir-*` configs hold **passage-grouped** commentary (Diyanet **Kur'an
Yolu**) — one row per commentary passage spanning an **ayah range**, plus
per-sura intro blocks — so they do **not** use the 6,236-verse spine. Columns:
`passage_id` · `section` (`tefsir`/`intro`) · `title` · `surah` · `ayah_start`
· `ayah_end` · `n_ayahs` · `verse_key_start` · `verse_key_end` · `juz`
· `surah_name_ar`/`surah_name_en` · `revelation_place` · `volume` · `text`
· `text_html` · `lang` · `translation_id` · `kind`. Join back to any verse config on a `verse_key`
in `[verse_key_start .. verse_key_end]`. A **verse-expanded** convenience view
(`tafsir-kuranyolu-tr-verses`, one row per ayah with the passage text repeated
plus `verse_key_from`/`verse_key_to`) is also provided for plain verse joins.

### Word-by-word morphology (`morphology-ar`)

The `morphology-ar` config is **sub-verse**: one row per **morphological segment**
(~130k rows) from the **Quranic Arabic Corpus** (corpus.quran.com, GPL, kept
verbatim). Columns: `location` (`surah:ayah:word:segment`, unique) · `verse_key`
(join key) · `surah` · `ayah` · `word_index` · `segment_index` · `ayah_global`
· `form` (Arabic vocalized segment) · `tag` (coarse N/P/V) · `pos` (fine
part-of-speech) · `seg_type` (`STEM`/`PREF`/`SUF`) · `lemma` · `root` · `features`
(the raw QAC annotation, full fidelity). Join to any verse config on
`verse_key` (one ayah → many segment rows).

## Configs by language

### Arabic (`ar`) — 72 config(s)

| config | translator / edition | school |
|---|---|---|
| `arabic-simple-clean` | Tanzil Project — Simple-Clean v1.1 | canonical-hafs |
| `arabic-uthmani` | Tanzil Project — Uthmani v1.1 | canonical-hafs |
| `morphology-ar` | Quranic Arabic Corpus (Kais Dukes) — Quranic Arabic Corpus — morphological annotation (v0.4) | n/a (grammatical annotation of the Quranic text) |
| `tafsir-abd-al-razzaq-ar` | Ebû Bekir Abdürrezzâk b. Hemmâm es-San‘ânî (ö. 211/826-27) — Tefsîru ʿAbdirrezzâḳ eṣ-Ṣanʿânî | Ehl-i hadis (mezhep teşekkülü öncesi erken rivayet tefsiri) |
| `tafsir-abussuud-ar` | Ebüssuûd Efendi (Muhammed b. Muhammed el-İmâdî, ö. 982/1574) — İrşâdü'l-akli's-selîm ilâ mezâya'l-Kitâbi'l-Kerîm | Hanefî (Osmanlı Sünnî) |
| `tafsir-alusi-ar` | Şehâbeddin Mahmûd el-Âlûsî (ö. 1270/1854) — Rûhu'l-meânî | Hanefî (Selef ağırlıklı) |
| `tafsir-asbab-wahidi-ar` | Ebü’l-Hasan Ali b. Ahmed el-Vâhidî en-Nîsâbûrî eş-Şâfiî (ö. 468/1076) — Esbâbü nüzûli’l-Ḳurʾân | Şâfiî; Eş‘arî (rivayet ağırlıklı esbâb-ı nüzûl eseri) |
| `tafsir-baghawi-ar` | Bağavî (Ebû Muhammed el-Hüseyn b. Mes'ûd, ö. 516/1122) — Me'âlimü't-tenzîl | Şâfiî |
| `tafsir-bahrmuhit-ar` | Ebû Hayyân el-Endelüsî (Muhammed b. Yûsuf, ö. 745/1344) — el-Bahrü'l-muhît | Şâfiî (Mâlikî/Zâhirî geçmişi) |
| `tafsir-basit-wahidi-ar` | Ebü'l-Hasan Ali b. Ahmed el-Vâhidî en-Nîsâbûrî eş-Şâfiî (ö. 468/1076) — el-Basît fî tefsîri'l-Kur'ân | Eş'arî/Şâfiî (rivayet, dil ve nahiv; güçlü sıhhat uyarısı) |
| `tafsir-baydawi-ar` | Kādî Nâsırüddin Abdullah b. Ömer el-Beyzâvî (ö. 685/1286) — Envârü't-tenzîl ve esrârü't-teʾvîl | Eş'arî/Şâfiî (dirayet; zayıf rivayet/İsrâiliyat uyarısı) |
| `tafsir-biqai-ar` | Burhâneddin İbrâhim el-Bikāî (ö. 885/1480) — Nazmü'd-dürer fî tenâsübi'l-âyât ve's-süver | Şâfiî |
| `tafsir-durrmanthur-ar` | Celâleddin es-Süyûtî (Abdurrahman b. Ebû Bekir, ö. 911/1505) — ed-Dürrü'l-mensûr fi't-tefsîr bi'l-me'sûr | Şâfiî (Eş'arî) |
| `tafsir-durrmasun-ar` | Şihâbüddin Ahmed b. Yûsuf es-Semîn el-Halebî (ö. 756/1355) — ed-Dürrü'l-masûn fî ʿulûmi'l-kitâbi'l-meknûn | Şâfiî (nahiv, kıraat ve dil ağırlıklı dirayet tefsiri) |
| `tafsir-ibn-al-arabi-ahkam-ar` | Ebû Bekir Muhammed b. Abdullah İbnü’l-Arabî el-Meâfirî el-İşbîlî (ö. 543/1148) — Aḥkâmü’l-Ḳurʾân | Mâlikî; Eş‘arî (fıkhî/ahkâm tefsiri) |
| `tafsir-ibn-arafa-ar` | Ebû Abdillâh Muhammed b. Muhammed İbn Arafe el-Vergammî et-Tûnisî (ö. 803/1401) — Tefsîru İbn ʿArafe (talebe ders notları) | Eş‘arî/Mâlikî |
| `tafsir-ibn-faras-ar` | Ebû Muhammed Abdülmün‘im b. Muhammed b. Abdurrahîm el-Ensârî el-Hazrecî İbnü’l-Feres (ö. 597/1201) — Aḥkâmü’l-Ḳurʾân | Mâlikî (fıkhî/ahkâm tefsiri; kelâmda Ehl-i Sünnet) |
| `tafsir-ibn-furak-ar` | Ebû Bekir Muhammed b. el-Hasen İbn Fûrek el-İsfahânî en-Nîsâbûrî (ö. 406/1015) — Tefsîrü'l-Ḳurʾân / Meʿâni'l-Ḳurʾân (Mü'minûn-Gâfir ve Nûh-Nâs mevcut dijital bölümleri) | Şâfiî-Eşʿarî; Ehl-i sünnet dirayet-rivayet tefsiri |
| `tafsir-ibn-hajar-cujab-ar` | Şihâbüddîn Ebü'l-Fazl Ahmed b. Ali İbn Hacer el-Askalânî (ö. 852/1449) — el-ʿUcâb fî beyâni'l-esbâb (mevcut eksik nüsha: Bakara-Nisâ 4:78) | Şâfiî; Sünnî hadis ve esbâb-ı nüzûl tenkidi |
| `tafsir-ibn-mundhir-ar` | Ebû Bekir Muhammed b. İbrâhim İbnü’l-Münzir en-Nîsâbûrî (ö. 318/930 [?]) — Kitâbü Tefsîri’l-Ḳurʾân (günümüze ulaşan 2:272–4:92 parçası) | Bağımsız Sünnî mutlak müctehid; Şâfiî usulünü kullandı ve Şâfiî tabakatında sayıldı |
| `tafsir-ibnabihatim-ar` | Ebû Muhammed Abdurrahman b. Muhammed İbn Ebû Hâtim er-Râzî (ö. 327/938) — Tefsîrü'l-Kur'âni'l-azîm | Ehl-i hadis/Hanbelî (rivayet tefsiri; isnad uyarısı) |
| `tafsir-ibnabizamanin-ar` | İbn Ebû Zemenîn (Muhammed b. Abdillâh el-Mürrî, ö. 399/1008) — Muhtasaru Tefsîri Yahyâ b. Sellâm (Tefsîrü'l-Kur'ân) | Mâlikî (Selef akîdesi) |
| `tafsir-ibnadil-ar` | İbn Âdil ed-Dımaşkî (Ebü Hafs Sirâcüddîn Ömer b. Nûriddîn Ali, VIII./XIV. yüzyıl) — el-Lübâb fî ulûmi'l-Kitâb | Hanbelî |
| `tafsir-ibnaljawzi-ar` | İbnü'l-Cevzî (Ebü'l-Ferec Abdurrahman b. Ali, ö. 597/1201) — Zâdü'l-mesîr fî ilmi't-tefsîr | Hanbelî |
| `tafsir-ibnatiyya-ar` | İbn Atıyye el-Endelüsî (Abdülhak b. Gālib, ö. 541/1147) — el-Muharrerü'l-vecîz fî tefsîri'l-kitâbi'l-azîz | Mâlikî |
| `tafsir-ibnjuzay-ar` | İbn Cüzey el-Kelbî (Ebü'l-Kāsım Muhammed b. Ahmed, ö. 741/1340) — et-Teshîl li-ulûmi't-tenzîl | Mâlikî |
| `tafsir-ibnkathir-ar` | İbn Kesîr (Ebü'l-Fidâ İsmâil b. Ömer, ö. 774/1373) — Tefsîrü'l-Kur'âni'l-Azîm | Eserî (Şâfiî) |
| `tafsir-ijaz-bayan-ar` | Ebü’l-Kāsım Mahmûd b. Ebi’l-Hasen en-Nîsâbûrî (ö. 553/1158’den sonra) — Îcâzü’l-beyân ʿan meʿâni’l-Ḳurʾân | Hanefî; rivayet, dil, kıraat ve dirayet tefsiri |
| `tafsir-iji-ar` | Muînüddin Muhammed b. Abdurrahman el-Îcî eş-Şâfiî (ö. 905/1500) — Câmiu'l-beyân fî tefsîri'l-Kur'ân | Şâfiî |
| `tafsir-izz-abdussalam-ar` | İzzeddin Abdülazîz b. Abdüsselâm es-Sülemî ed-Dımaşkī (ö. 660/1262) — Tefsîrü’l-Kurʾân | Eş‘arî/Şâfiî |
| `tafsir-jahdami-ahkam-ar` | Ebû İshak İsmâil b. İshak el-Cehdamî (ö. 282/896) — Aḥkâmü’l-Ḳurʾân (günümüze ulaşan parça) | Mâlikî; muhaddis ve Mâlikî fıkıh otoritesi (fıkhî/ahkâm tefsiri) |
| `tafsir-jalalayn-ar` | Celâleddin el-Mahallî (ö. 864/1459) ve Celâleddin es-Süyûtî (ö. 911/1505) — Tefsîrü'l-Celâleyn | Şâfiî (Eş'arî) |
| `tafsir-khazin-ar` | Alâeddin Ali b. Muhammed el-Hâzin el-Bağdâdî (ö. 741/1341) — Lübâbü’t-teʾvîl fî meʿâni’t-tenzîl | Eş‘arî/Şâfiî (rivayet-dirayet; güçlü İsrâiliyat uyarısı) |
| `tafsir-kiya-harrasi-ahkam-ar` | Ebü’l-Hasan İmâdüddin Ali b. Muhammed el-Kiyâ el-Herrâsî et-Taberî (ö. 504/1110) — Aḥkâmü’l-Ḳurʾân | Şâfiî; Eş‘arî (fıkhî/ahkâm tefsiri) |
| `tafsir-lubab-nuqul-suyuti-ar` | Celâlüddîn Abdurrahman b. Ebû Bekir es-Süyûtî eş-Şâfiî (ö. 911/1505) — Lubâbü'n-nuḳūl fî esbâbi'n-nüzûl | Şâfiî; Eşʿarî, Sünnî esbâb-ı nüzûl rivayet derlemesi |
| `tafsir-makki-ar` | Mekkî b. Ebû Tâlib el-Kaysî (Ebû Muhammed Hammûş, ö. 437/1045) — el-Hidâye ilâ bulûgi'n-nihâye fî ilmi meâni'l-Kur'ân ve tefsîrihî ve ahkâmihî | Mâlikî (Selef akîdesi) |
| `tafsir-marah-labid-ar` | Şeyh Muhammed Nevavî el-Bentenî el-Câvî (ö. 1316/1897) — Marāḥ Labīd li-keşfi maʿne’l-Ḳurʾâni’l-mecîd (et-Tefsîrü’l-Münîr) | Şâfiî; Eş‘arî/Ehl-i sünnet, klasik rivayet-dirayet tefsiri ve Güneydoğu Asya medrese geleneği |
| `tafsir-maturidi-ar` | Ebû Mansûr Muhammed b. Muhammed el-Mâtürîdî (ö. 333/944) — Teʾvîlâtü’l-Kurʾân (Teʾvîlâtü Ehli’s-sünne) | Hanefî-Mâtürîdî (dirayet ve kelâm) |
| `tafsir-mawardi-ar` | Ebü'l-Hasen el-Mâverdî (Ali b. Muhammed, ö. 450/1058) — en-Nüket ve'l-uyûn | Şâfiî (kelâmî nisbeti hakkında tarihî ihtilâf) |
| `tafsir-mazhari-ar` | Kādî Muhammed Senâullah Pânîpetî el-Hanefî (ö. 1225/1810) — et-Tefsîrü’l-Maẓharî | Hanefî; Nakşibendî-Müceddidî (rivayet, dirayet, fıkıh ve tasavvuf boyutlarını birleştiren klasik Sünnî tefsir) |
| `tafsir-mukhtasar-ar` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Arabic edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `tafsir-muyassar-ar` | Tefsîrü'l-Müyesser ilim heyeti — et-Tefsîrü'l-Müyesser | Eserî (heyet) |
| `tafsir-muyassar-ar-quranenc` | At-Tafsir Al-Muyassar scholarly committee — At-Tafsir Al-Muyassar — current official QuranEnc digital edition — Arabic edition V1.0.0 | Eserî (heyet; güncel resmî dijital edisyon) |
| `tafsir-nafahat-ar` | Muhammad bin Salih bin Abdullah al-Shawi — Al-Nafahat al-Makkiyyah fi Tafsir Kitab Rabb al-Bariyyah — Arabic edition V1.0.0 | Ehl-i Sünnet (çağdaş; mezhep-özel nispeti doğrulanmadı) |
| `tafsir-nahrmadd-ar` | Ebû Hayyân el-Endelüsî (Muhammed b. Yûsuf, ö. 745/1344) — en-Nehrü’l-mâd mine’l-Baḥri’l-muḥîṭ | Şâfiî (Mâlikî/Zâhirî geçmişi; dil ve dirayet tefsiri muhtasarı) |
| `tafsir-nasafi-ar` | Ebü'l-Berekât en-Nesefî (Abdullah b. Ahmed, ö. 710/1310) — Medârikü't-tenzîl ve hakāiku't-te'vîl | Hanefî-Mâtürîdî |
| `tafsir-nasai-ar` | Ebû Abdirrahmân Ahmed b. Şuayb en-Nesâî (ö. 303/915) — Kitâbü’t-Tefsîr (es-Sünenü’l-kübrâ’nın 82. kitabı) | Ehl-i sünnet/Ehl-i hadis (Kütüb-i Sitte muhaddisi) |
| `tafsir-nizam-naysaburi-ar` | Nizâmüddîn Hasen b. Muhammed en-Nîsâbûrî (ö. 730/1329 [?]) — Ġarâʾibü’l-Ḳurʾân ve reġāʾibü’l-furḳān | Eş‘arî/Şâfiî (rivayet-dirayet; sınırlı işârî açıklamalar) |
| `tafsir-qanuji-ar` | Muhammed Sıddîk Hasan Han el-Kınnevci (ö. 1307/1890) — Fethu'l-beyân fî makāsıdi'l-Kur'ân | Ehl-i Hadis/Eserî (müstakil; dört mezhebe bağlı değil, mezhep karşıtı söylem uyarısı) |
| `tafsir-qasimi-ar` | Cemâleddin el-Kāsımî (Muhammed Cemâleddîn, ö. 1914) — Mehâsinü't-te'vîl | Selefî (Şâfiî çevre; dört mezhebi mukayeseli aktarır) |
| `tafsir-qurtubi-ar` | Kurtubî (Ebû Abdillâh Muhammed b. Ahmed, ö. 671/1273) — el-Câmi' li-ahkâmi'l-Kur'ân | Mâlikî |
| `tafsir-qushayri-ar` | Abdülkerîm b. Hevâzin el-Kuşeyrî (ö. 465/1072) — Leṭâʾifü’l-işârât | Eş‘arî/Şâfiî (Sünnî işârî tefsir; güçlü yöntem uyarısı) |
| `tafsir-razi-ar` | Fahreddin er-Râzî (Muhammed b. Ömer, ö. 606/1210) — Mefâtîhu'l-gayb (et-Tefsîrü'l-kebîr) | Şâfiî-Eş'arî |
| `tafsir-saadi-ar` | Abdurrahman b. Nâsır es-Sa‘dî (ö. 1376/1957) — Teysîrü'l-Kerîmi'r-Rahmân fî tefsîri kelâmi'l-Mennân | Eserî (Hanbelî) |
| `tafsir-samani-ar` | Ebü'l-Muzaffer es-Sem'ânî (Mansûr b. Muhammed, ö. 489/1096) — Tefsîrü'l-Kur'ân | Şâfiî (Selef akîdesi) |
| `tafsir-sawi-ar` | Ahmed b. Muhammed es-Sâvî el-Mâlikî el-Halvetî (ö. 1241/1825) — Ḥâşiyetü’ṣ-Ṣâvî ʿalâ Tefsîri’l-Celâleyn | Mâlikî; Halvetî (tasavvuf ağırlıklı Celâleyn hâşiyesi) |
| `tafsir-sealibi-ar` | Ebû Zeyd es-Seâlibî (Abdurrahman b. Muhammed, ö. 875/1471) — el-Cevâhirü'l-hisân fî tefsîri'l-Kur'ân | Mâlikî |
| `tafsir-semerkandi-ar` | Ebü'l-Leys es-Semerkandî (Nasr b. Muhammed, ö. 373/983) — Tefsîru Ebi'l-Leys es-Semerkandî | Hanefî (Mâtürîdî çizgi) |
| `tafsir-shafii-ahkam-ar` | İmam Muhammed b. İdrîs eş-Şâfiî'nin (ö. 204/820) görüşleri; derleyen Ebû Bekir Ahmed b. Hüseyin el-Beyhakî (ö. 458/1066) — Aḥkâmü'l-Ḳurʾân li'l-İmâm eş-Şâfiʿî (Beyhakî derlemesi) | Şâfiî; Ehl-i Sünnet (Beyhakî derlemesi; fıkhî/ahkâm tefsiri) |
| `tafsir-shawkani-ar` | Muhammed b. Ali eş-Şevkânî (Ebû Abdullah, ö. 1250/1834) — Fethu'l-kadîr el-câmiʿ beyne fenneyi'r-rivâye ve'd-dirâye min ʿilmi't-tefsîr | Ehl-i Sünnet (müstakil müctehid; rivayet/dirayet, dört mezhebe bağlı değil) |
| `tafsir-siraj-munir-ar` | Şemseddin Muhammed b. Ahmed el-Hatîb eş-Şirbînî (ö. 977/1570) — es-Sirâcü'l-münîr fî'l-iʿâne ʿalâ maʿrifeti baʿżı meʿânî kelâmi rabbine'l-hakîmi'l-habîr | Şâfiî; Ehl-i sünnet rivayet-dirayet tefsiri |
| `tafsir-sufyan-thawri-ar` | Ebû Abdillâh Süfyân b. Saîd es-Sevrî (ö. 161/778) — Tefsîru Süfyâni’s-Sevrî | Ehl-i hadis; müstakil Sevrî fıkıh mezhebi (erken rivayet tefsiri) |
| `tafsir-tabarani-ar` | Ebü’l-Kāsım Süleyman b. Ahmed et-Taberânî (ö. 360/971) — et-Tefsîrü’l-kebîr | Ehl-i hadis/Selef akîdesi; Hanbelî (rivayet tefsiri) |
| `tafsir-tabari-ar` | Taberî (Ebû Ca'fer Muhammed b. Cerîr, ö. 310/923) — Câmiu'l-beyân an te'vîli âyi'l-Kur'ân | Klasik Sünnî (müctehid) |
| `tafsir-tahawi-ar` | Ebû Ca‘fer Ahmed b. Muhammed et-Tahâvî (ö. 321/933) — Aḥkâmü’l-Ḳurʾân | Hanefî; Ehl-i Sünnet akîdesi (fıkhî/ahkâm tefsiri) |
| `tafsir-taysir-nasafi-ar` | Ebü’l-Hafs Necmeddin Ömer b. Muhammed en-Nesefî (ö. 537/1142) — et-Teysîr fi’t-tefsîr | Hanefî-Mâtürîdî; Ehl-i Sünnet kelâmı ile rivayet/dirayet tefsiri |
| `tafsir-thalabi-ar` | Ebû İshak es-Sa'lebî en-Nîsâbûrî (Ahmed b. Muhammed, ö. 427/1035) — el-Keşf ve'l-beyân an tefsîri'l-Kur'ân | Şâfiî (rivayet tefsiri; güçlü sıhhat uyarısı) |
| `tafsir-uleymi-ar` | Ebü’l-Yümn Mücîrüddin el-Uleymî el-Makdisî el-Hanbelî (ö. 928/1522) — Fetḥu’r-Raḥmân fî Tefsîri’l-Ḳurʾân | Hanbelî; Ehl-i hadis/selef akidesi, Ehl-i Sünnet ve’l-cemaat |
| `tafsir-wajiz-wahidi-ar` | Ebü'l-Hasan Ali b. Ahmed el-Vâhidî en-Nîsâbûrî eş-Şâfiî (ö. 468/1076) — el-Vecîz fî tefsîri'l-kitâbi'l-azîz | Şâfiî (klasik Sünnî; rivayet sıhhati uyarısı) |
| `tafsir-wasit-wahidi-ar` | Ebü’l-Hasan Ali b. Ahmed el-Vâhidî en-Nîsâbûrî eş-Şâfiî (ö. 468/1076) — el-Vasîṭ fî tefsîri’l-Ḳurʾâni’l-mecîd | Şâfiî; Eş‘arî (rivayet, dil ve dirayeti birleştiren klasik orta hacimli tefsir) |
| `tafsir-yahya-ibn-sallam-ar` | Ebû Zekeriyyâ Yahyâ b. Sellâm et-Teymî (ö. 200/815) — Tefsîru Yaḥyâ b. Sellâm (günümüze ulaşan Nahl-Sâffât parçaları) | Erken Sünnî rivayet-dirayet tefsiri (mezhep teşekkülü öncesi; Mâlik'ten ders aldı) |
| `tafsir-yaseer-ar` | Al-Yaseer in At-Tafseer editorial team (not named on the current official card) — Al-Yaseer in At-Tafseer — Arabic edition V1.0.19 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel nispeti doğrulanmadı) |

### English (`en`) — 27 config(s)

| config | translator / edition | school |
|---|---|---|
| `en-abdelhaleem` | M. A. S. Abdel Haleem — The Qur'an (Oxford World's Classics) | Sunni (Azharî) |
| `en-abdulhye` | Abdul Hye — Translation of the meanings of the Qur'an | Sunni |
| `en-almuntakhabfita` | Almuntakhab Fi Tafsir Alquran Alkarim — Translation of the meanings of the Qur'an | Sunni (Al-Azhar) |
| `en-bewley` | Abdalhaqq & Aisha Bewley — The Noble Qur'an: A New Rendering | Mâlikî-Eş'arî (Murabitun) |
| `en-clearquran` | Dr. Mustafa Khattab — The Clear Quran (Allah edition) | Sunni |
| `en-clearquran-god` | Dr. Mustafa Khattab — The Clear Quran (God edition) | Sunni |
| `en-daryabadi` | Abdul Majid Daryabadi — The Glorious Qur'an: Text, Translation & Commentary | Sunni (Deobandi-leaning) |
| `en-farookmalik` | Farook Malik — Translation of the meanings of the Qur'an | Sunni |
| `en-hilali-khan` | Muhammad Taqi-ud-Din al-Hilali & Muhammad Muhsin Khan — The Noble Qur'an | Salafi/Athari |
| `en-maududi` | Sayyid Abul A'la Maududi (tr. Z. I. Ansari) — Towards Understanding the Qur'an (Tafhim) | Sunni (Jamaat-e-Islami) |
| `en-miraneesuddin` | Mir Aneesuddin — Translation of the meanings of the Qur'an | Sunni |
| `en-mohammadshafi` | Mohammad Shafi — Translation of the meanings of the Qur'an | Deobandi (Hanafi) |
| `en-mubarakpuri` | Safi-ur-Rahman al-Mubarakpuri (team) — Tafsir Ibn Kathir (abridged) — translation | Salafi/Athari |
| `en-muhammadmahmoud` | Muhammad Mahmoud Ghali — Translation of the meanings of the Qur'an | Sunni (Al-Azhar) |
| `en-pickthall` | Marmaduke Pickthall — The Meaning of the Glorious Koran (1930) | sunni-mainstream |
| `en-rowwadtranslati` | Rowwad Translation Center — Translation of the meanings of the Qur'an | Salafi (da'wah) |
| `en-safikaskas` | Safi Kaskas — Translation of the meanings of the Qur'an | Sunni (contemporary) |
| `en-saheeh` | Saheeh International — The Qur'an — Saheeh International | Sunni (Athari) |
| `en-syedvickarahame` | Syed Vickar Ahamed — Translation of the meanings of the Qur'an | Sunni |
| `en-tbirving` | Tbirving — Translation of the meanings of the Qur'an | Sunni (convert) |
| `en-ummmuhammad` | Umm Muhammad — Translation of the meanings of the Qur'an | Salafi (Saheeh International) |
| `en-usmani` | Mufti Muhammad Taqi Usmani — The Noble Qur'an: Meaning with Explanatory Notes | Deobandi (Hanafî) |
| `en-yusufali` | Abdullah Yusuf Ali — The Holy Qur'an (original 1934-1938 edition, unrevised) | sunni-mainstream |
| `tafsir-hilali-khan-annotated-en` | Muhammad Taqi-ud-Din al-Hilali and Muhammad Muhsin Khan — English annotated translation with extended explanatory notes — Hilali and Khan — English edition V1.1.2 | Ehl-i Sünnet/Eserî (İngilizce açıklamalı meal ve tefsir notları) |
| `tafsir-mukhtasar-en` | Tafsir Center for Quranic Studies (editorial and English translation team) — Al-Mukhtasar in Interpreting the Noble Quran — English edition | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `tafsir-noor-annotated-en` | Noor International Center editorial and translation team — English annotated translation with explanatory Quranic notes — Noor International Center — English edition V1.1.2 | Ehl-i Sünnet (çağdaş heyet; İngilizce açıklamalı meal ve tefsir notları) |
| `tafsir-rowwad-annotated-en` | Rowwad Translation Center translation team — English annotated translation with explanatory Quranic notes — Rowwad Translation Center — English edition V1.0.19 | Ehl-i Sünnet (çağdaş heyet; İngilizce açıklamalı meal ve tefsir notları) |

### Turkish (`tr`) — 24 config(s)

| config | translator / edition | school |
|---|---|---|
| `tafsir-kuranyolu-tr` | Hayrettin Karaman, Mustafa Çağrıcı, İbrahim Kâfi Dönmez, Sadrettin Gümüş — Kur'an Yolu Türkçe Meâl ve Tefsir (DİB) — tefsir kısmı (5 cilt) | Hanafî-Mâtürîdî |
| `tafsir-kuranyolu-tr-verses` | Hayrettin Karaman, Mustafa Çağrıcı, İbrahim Kâfi Dönmez, Sadrettin Gümüş — Kur'an Yolu Tefsir — verse-expanded view (one row per ayah; passage text repeated) | Hanafî-Mâtürîdî |
| `tafsir-mukhtasar-tr` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Turkish edition V1.1.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `tafsir-saadi-tr` | Abd al-Rahman ibn Nasir al-Sa'di; Turkish translator not named on the current official card — Tafsir al-Sa'di — Turkish translation — Turkish edition V1.0.0 | Hanbelî/Eserî (Türkçe çeviri) |
| `tr-ademugur` | Adem Uğur — Kur'an-ı Kerim ve Türkçe Meâli | Hanafî-Mâtürîdî |
| `tr-alibulac` | Ali Bulaç — Kur'an-ı Kerim ve Türkçe Anlamı (Meal ve Sözlük) | Hanafî-Mâtürîdî |
| `tr-alifikriyavuz` | Ali Fikri Yavuz — Kur'an-ı Kerim ve İzahlı Meâl-i Âlisi | Hanafî-Mâtürîdî |
| `tr-cantay` | Hasan Basri Çantay — Kur'an-ı Hakîm ve Meâl-i Kerîm | Hanafî-Mâtürîdî |
| `tr-celalyildirim` | Celal Yıldırım — İlmin Işığında Asrın Kur'an Meâli | Hanafî-Mâtürîdî |
| `tr-diyanet` | Diyanet İşleri Başkanlığı (Halil Altuntaş, Muzaffer Şahin) — Kur'an-ı Kerim Meâli | Hanafî-Mâtürîdî |
| `tr-diyanet-eski` | Diyanet İşleri Başkanlığı (eski heyet meali) — Kur'an-ı Kerim ve Türkçe Anlamı (eski Diyanet meali) | Hanafî-Mâtürîdî |
| `tr-elmalili` | Elmalili Muhammed Hamdi Yazir — Hak Dini Kur'an Dili (original, non-simplified) | sunni-mainstream |
| `tr-elmalili-sade` | Elmalılı M. Hamdi Yazır (sadeleştirilmiş) — Hak Dini Kur'an Dili (sadeleştirilmiş) | Hanafî-Mâtürîdî |
| `tr-elmalili-sade2` | Elmalılı M. Hamdi Yazır (sadeleştirilmiş, 2. derleme) — Hak Dini Kur'an Dili (sadeleştirilmiş, alt derleme) | Hanafî-Mâtürîdî |
| `tr-fizilal` | Seyyid Kutub (Fî Zilâli'l-Kur'an) — Fî Zilâli'l-Kur'an (meal kısmı) | Sünnî (İhvân/Eş'arî) |
| `tr-ibnkesir` | Bekir Karlığa, Bedrettin Çetiner (İbn Kesir tefsiri esaslı meal) — Hadislerle Kur'an-ı Kerim Tefsiri (meal kısmı) | Selefî / Şâfiî (İbn Kesir) |
| `tr-islamhouse` | IslamHouse.com (Türkçe heyet) — Kur'an Meâli (IslamHouse/QuranEnc) | Selefî / da'vâ |
| `tr-kuranyolu` | Hayrettin Karaman, Mustafa Çağrıcı, İbrahim Kâfi Dönmez, Sadrettin Gümüş — Kur'an Yolu Türkçe Meâl ve Tefsir (DİB) — meâl kısmı | Hanafî-Mâtürîdî |
| `tr-muhammetabay` | Muhammet Abay (Mustafa Öztürk düzeltili akademik meal) — Kur'an Meâli | Sünnî (akademik) |
| `tr-muslumsahin` | Müslim Şahin — Kur'an-ı Kerim Meâli (QuranEnc/IslamHouse) | Sünnî (da'vâ) |
| `tr-sabanbritch` | Şaban Britch (heyet) — Kur'an-ı Kerim Meâli (Rowwad/QuranEnc) | Selefî / Rowwad da'vâ |
| `tr-sabanpiris` | Şaban Piriş — Kur'an-ı Kerim Türkçe Anlamı | Selefî-meşrep Sünnî |
| `tr-tdv` | Heyet (Hayrettin Karaman, Ali Özek, İbrahim Kâfi Dönmez, Mustafa Çağrıcı, Sadrettin Gümüş, Ali Turgut) — Kur'an-ı Kerim ve Açıklamalı Meâli | Hanafî-Mâtürîdî |
| `tr-tefhim` | Ebü'l-A'lâ el-Mevdûdî (Tefhîmü'l-Kur'an) — Tefhîmü'l-Kur'an — Kur'an'ın Anlamı ve Tefsiri | Sünnî (Cemaat-i İslâmî) |

### Achinese (`ace`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `ace-tgkhmahjiddinju` | Tgk. H. Mahjiddin Jusuf — Translation of the meanings of the Qur'an | Shafi'i |

### Afar (`aa`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `aa-sheikhmahmoudab` | Sheikh Mahmoud Abdel Qader Hamz And Group Of Scholars — Translation of the meanings of the Qur'an | Salafi |

### Afrikaans (`af`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `af-imammabaker` | Imam M. A. Baker — Translation of the meanings of the Qur'an | Sunni |

### Albanian (`sq`) — 4 config(s)

| config | translator / edition | school |
|---|---|---|
| `sq-fetimehdiu` | Feti Mehdiu — Translation of the meanings of the Qur'an | Hanafi-Maturidi |
| `sq-hasanefendinahi` | Hasan Efendi Nahi — Translation of the meanings of the Qur'an | Hanafi-Maturidi |
| `sq-hassannahi` | Hassan Nahi — Translation of the meanings of the Qur'an | Hanafi-Maturidi |
| `sq-sherifahmeti` | Sherif Ahmeti — Translation of the meanings of the Qur'an | Hanafi-Maturidi |

### Amharic (`am`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `am-muhammedsadiqan` | Muhammed Sadiq And Muhammed Sani Habib — Translation of the meanings of the Qur'an | Sunni |

### Assamese (`as`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `as-shaykhrafeequli` | Shaykh Rafeequl Islam Habibur Rahman — Translation of the meanings of the Qur'an | Salafi |
| `tafsir-mukhtasar-as` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Assamese edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Azerbaijani (`az`) — 4 config(s)

| config | translator / edition | school |
|---|---|---|
| `az-alikhanmusayev` | Alikhan Musayev — Translation of the meanings of the Qur'an | Athari/Salafi |
| `az-khanmusayev` | Khan Musayev — Translation of the meanings of the Qur'an | Athari/Salafi |
| `az-vasimmammadaliy` | Vasim Mammadaliyev And Ziya Bunyadov — Translation of the meanings of the Qur'an | Hanafi-Maturidi (academic) |
| `tafsir-mukhtasar-az` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Azerbaijani edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Bambara (`bm`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `bm-fodisulimankant` | Fodi Suliman Kanti — Translation of the meanings of the Qur'an | Sunni (KFC/Rowwad) |
| `bm-karamobabamamad` | Karamo Baba Mamadi Jani — Translation of the meanings of the Qur'an | Sunni (KFC/Rowwad) |

### Bengali (`bn`) — 4 config(s)

| config | translator / edition | school |
|---|---|---|
| `bn-abubakrzakaria` | Abu Bakr Zakaria — Translation of the meanings of the Qur'an | Salafi/Athari |
| `bn-muhiuddinkhan` | Muhiuddin Khan — Translation of the meanings of the Qur'an | Hanafi (Deobandi-leaning) |
| `tafsir-mukhtasar-bn` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Bengali edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `tafsir-zakaria-bn` | Dr. Abu Bakr Muhammad Zakaria — Bengali annotated translation with Quranic tafsir notes — Abu Bakr Zakaria — Bengali edition V1.1.1 | Ehl-i Sünnet/Eserî (Bengalce açıklamalı meal ve tefsir notları) |

### Bosnian (`bs`) — 5 config(s)

| config | translator / edition | school |
|---|---|---|
| `bs-besimkorkut` | Besim Korkut — Translation of the meanings of the Qur'an | Hanafi-Maturidi |
| `bs-korkut` | Korkut — Translation of the meanings of the Qur'an | Hanafi-Maturidi |
| `bs-muhamedmehanovi` | Muhamed Mehanovic — Translation of the meanings of the Qur'an | Athari/Salafi |
| `bs-wwwislamhouseco` | Www.islamhouse.com — Translation of the meanings of the Qur'an | Athari/Salafi |
| `tafsir-mukhtasar-bs` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Bosnian edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Bulgarian (`bg`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `bg-tzvetantheophan` | Tzvetan Theophanov — Translation of the meanings of the Qur'an | Sunni |

### Burmese (`my`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `my-basein` | Ba Sein — Translation of the meanings of the Qur'an | Hanafi |
| `my-ghazimohammadha` | Ghazi Mohammad Hashim — Translation of the meanings of the Qur'an | Hanafi |
| `my-hashimtinmyint` | Hashim Tin Myint — Translation of the meanings of the Qur'an | Hanafi |

### Chichewa (`ny`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `ny-alhajiyusufmuha` | Al Haji Yusuf Muhammad Kanyamula — Translation of the meanings of the Qur'an | Sunni |
| `ny-khaledibrahimbe` | Khaled Ibrahim Betala — Translation of the meanings of the Qur'an | Sunni |

### Chinese (`zh`) — 6 config(s)

| config | translator / edition | school |
|---|---|---|
| `tafsir-mukhtasar-zh` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Chinese edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `zh-anonymousgroupo` | Anonymous Group Of Translators — Translation of the meanings of the Qur'an | Sunni (Hui) |
| `zh-majian` | Ma Jian — Translation of the meanings of the Qur'an | Sunni (Hui) |
| `zh-majian1` | Ma Jian — Translation of the meanings of the Qur'an | Sunni (Hui) |
| `zh-mazhonggang` | Ma Zhong Gang — Translation of the meanings of the Qur'an | Sunni (Hui) |
| `zh-muhammadmakin` | Muhammad Makin — Translation of the meanings of the Qur'an | Sunni (Hui) |

### Dagbani (`dag`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `dag-muhammadbabaght` | Muhammad Baba Ghtobo — Translation of the meanings of the Qur'an | Sunni |

### Divehi (`dv`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `dv-officeofthepres` | Office Of The President Of Maldives — Translation of the meanings of the Qur'an | Shafi'i |

### Dutch (`nl`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `nl-sofianssiregar` | Sofian S. Siregar — Translation of the meanings of the Qur'an | Salafi-leaning Sunni |

### Filipino (`fil`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `fil-abdullatifeduar` | Abdullatif Eduardo M. Arceo — Translation of the meanings of the Qur'an | Sunni (orthodox) |
| `fil-wwwislamhouseco` | Www.islamhouse.com — Translation of the meanings of the Qur'an | Salafi |
| `tafsir-mukhtasar-fil` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Filipino edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### French (`fr`) — 5 config(s)

| config | translator / edition | school |
|---|---|---|
| `fr-islamicfoundati` | Islamic Foundation — Translation of the meanings of the Qur'an | Salafi |
| `fr-muhammadhameedu` | Muhammad Hameedullah — Translation of the meanings of the Qur'an | Hanafi |
| `fr-muhammadhamidul` | Muhammad Hamidullah — Translation of the meanings of the Qur'an | Hanafi |
| `fr-rashidmaash` | Rashid Maash — Translation of the meanings of the Qur'an | Salafi |
| `tafsir-mukhtasar-fr` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — French edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Fulah (`ff`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `ff-rowadtranslatio` | Rowad Translation Center And Islamhouse — Translation of the meanings of the Qur'an | Salafi |
| `tafsir-mukhtasar-ff` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Fulah edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### German (`de`) — 4 config(s)

| config | translator / edition | school |
|---|---|---|
| `de-aburidamuhammad` | Abu Rida Muhammad Ibn Ahmad Ibn Rassoul — Translation of the meanings of the Qur'an | Sunni (orthodox) |
| `de-amirzaidan` | Amir Zaidan — Translation of the meanings of the Qur'an | Sunni (classical/Azhari) |
| `de-asfbubenheimand` | A. S. F. Bubenheim And N. Elyas — Translation of the meanings of the Qur'an | Salafi |
| `de-frankbubenheima` | Frank Bubenheim And Nadeem Elyas — Translation of the meanings of the Qur'an | Salafi |

### Gujarati (`gu`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `gu-rabilaalomari` | Rabila Al Omari — Translation of the meanings of the Qur'an | Sunni |

### Hausa (`ha`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `ha-abubakarmahmood` | Abubakar Mahmood Jummi — Translation of the meanings of the Qur'an | Salafi |
| `ha-abubakarmahmoud` | Abubakar Mahmoud Gumi — Translation of the meanings of the Qur'an | Salafi |

### Hebrew (`he`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `he-darusalamhousei` | Darusalam House In Jerusalem — Translation of the meanings of the Qur'an | Salafi |

### Hindi (`hi`) — 4 config(s)

| config | translator / edition | school |
|---|---|---|
| `hi-maulanaazizulha` | Maulana Azizul Haque Al Umari — Translation of the meanings of the Qur'an | Salafi/Ahl-e-Hadith |
| `hi-muhammadfarooqk` | Muhammad Farooq Khan And Muhammad Ahmed — Translation of the meanings of the Qur'an | Jamaat-e-Islami (Maududi) |
| `hi-suhelfarooqkhan` | Suhel Farooq Khan And Saifur Rahman Nadwi — Translation of the meanings of the Qur'an | Sunni (Nadwatul Ulama) |
| `tafsir-mukhtasar-hi` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Hindi edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Hungarian (`hu`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `hu-drahmedabdelrah` | Dr. Ahmed Abdel Rahman Okfat Tashaab — Translation of the meanings of the Qur'an | Salafi |

### Indonesian (`id`) — 7 config(s)

| config | translator / edition | school |
|---|---|---|
| `id-indonesianislam` | Indonesian Islamic Affairs Ministry — Translation of the meanings of the Qur'an | Shafi'i-Ash'ari |
| `id-jalaladdinalmah` | Jalal Ad Din Al Mahalli And Jalal Ad Din As Suyuti — Translation of the meanings of the Qur'an | Shafi'i-Ash'ari |
| `id-kingfahdcomplex` | King Fahd Complex — Translation of the meanings of the Qur'an | Shafi'i-Ash'ari |
| `id-muhammadquraish` | Muhammad Quraish Shihab Et Al. — Translation of the meanings of the Qur'an | Shafi'i-Ash'ari |
| `id-thesabiqcompany` | The Sabiq Company — Translation of the meanings of the Qur'an | Athari/Salafi |
| `tafsir-mukhtasar-id` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Indonesian edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `tafsir-saadi-id` | Abd al-Rahman ibn Nasir al-Sa'di; Indonesian translator not named on the current official card — Tafsir al-Sa'di — Indonesian translation — Indonesian edition V1.0.0 | Hanbelî/Eserî (Endonezce çeviri) |

### Italian (`it`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `it-hamzarobertopic` | Hamza Roberto Piccardo — Translation of the meanings of the Qur'an | Sunni (Salafi-leaning) |
| `tafsir-mukhtasar-it` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Italian edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Japanese (`ja`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `ja-ryoichimita` | Ryoichi Mita — Translation of the meanings of the Qur'an | Sunni |
| `tafsir-mukhtasar-ja` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Japanese edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Kannada (`kn`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `kn-abdussalamputhi` | Abdussalam Puthige — Translation of the meanings of the Qur'an | Sunni |

### Kazakh (`kk`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `kk-khalifahaltai` | Khalifah Altai — Translation of the meanings of the Qur'an | Hanafi-Maturidi |
| `kk-khalifahaltaich` | Khalifah Altai Charity Foundation — Translation of the meanings of the Qur'an | Hanafi-Maturidi |

### Khmer (`km`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `km-cambodianmuslim` | Cambodian Muslim Community Development — Translation of the meanings of the Qur'an | Shafi'i |
| `tafsir-mukhtasar-km` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Khmer edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Kinyarwanda (`rw`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `rw-rmcrwanda` | R. M. C. Rwanda — Translation of the meanings of the Qur'an | Sunni |
| `rw-rwandamuslimsas` | Rwanda Muslims Association Team — Translation of the meanings of the Qur'an | Sunni |

### Korean (`ko`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `ko-hamidchoi` | Hamid Choi — Translation of the meanings of the Qur'an | Sunni |
| `ko-unknown` | Unknown — Translation of the meanings of the Qur'an | Sunni |

### Kurdish (`ku`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `ku-burhanmuhammada` | Burhan Muhammad Amin — Translation of the meanings of the Qur'an | Shafi'i |
| `ku-muhammadsalehba` | Muhammad Saleh Bamoki — Translation of the meanings of the Qur'an | Sunni |
| `tafsir-mukhtasar-ku` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Kurdish edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Kyrgyz (`ky`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `ky-shamsaldinhakim` | Shams Al Din Hakimov — Translation of the meanings of the Qur'an | Hanafi |
| `tafsir-mukhtasar-ky` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Kyrgyz edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Lingala (`ln`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `ln-zakariyamuhamme` | Zakariya Muhammed Balingongo — Translation of the meanings of the Qur'an | Salafi/da'wah |

### Macedonian (`mk`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `mk-macedonianschol` | Macedonian Scholars — Translation of the meanings of the Qur'an | Hanafi-Maturidi |
| `mk-sheikhhassangil` | Sheikh Hassan Gilo — Translation of the meanings of the Qur'an | Hanafi-Maturidi |

### Malay (`ms`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `ms-abdullahmuhamma` | Abdullah Muhammad Basmeih — Translation of the meanings of the Qur'an | Shafi'i-Ash'ari |

### Malayalam (`ml`) — 4 config(s)

| config | translator / edition | school |
|---|---|---|
| `ml-abdulhameedmada` | Abdul Hameed Madani And Kunhi Mohammed — Translation of the meanings of the Qur'an | Salafi (Mujahid/KNM) |
| `ml-cheriyamundamab` | Cheriyamundam Abdul Hameed And Kunhi Mohammed Parappoor — Translation of the meanings of the Qur'an | Salafi (Mujahid/KNM) |
| `ml-muhammadkarakun` | Muhammad Karakunnu And Vanidas Elayavoor — Translation of the meanings of the Qur'an | Jamaat-e-Islami (Maududi) |
| `tafsir-mukhtasar-ml` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Malayalam edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Maltese (`mt`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `mt-martinrzammitmu` | Martin R. Zammit, Muhammad El Sadi — Translation of the meanings of the Qur'an | Sunni da'wah |

### Marathi (`mr`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `mr-muhammadshafiia` | Muhammad Shafi I Ansari — Translation of the meanings of the Qur'an | Sunni |

### Nepali (`ne`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `ne-ahlalhadithcent` | Ahl Al Hadith Central Society Of Nepal — Translation of the meanings of the Qur'an | Salafi/Athari (Ahl-e-Hadith) |

### Oromo (`om`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `om-ghaliapapurapag` | Ghali Apapur Apaghuna — Translation of the meanings of the Qur'an | Sunni da'wah |

### Pashto (`ps`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `ps-abdulwalikhan` | Abdulwali Khan — Translation of the meanings of the Qur'an | Hanafi (Deobandi) |
| `ps-zakariaabulsala` | Zakaria Abulsalam — Translation of the meanings of the Qur'an | Sunni (Hanafi/da'wah) |
| `tafsir-mukhtasar-ps` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Pashto edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Persian (`fa`) — 5 config(s)

| config | translator / edition | school |
|---|---|---|
| `fa-drhussientagi` | Dr. Hussien Tagi — Translation of the meanings of the Qur'an | Salafi |
| `fa-islamhousecompe` | Islamhouse.com Persian Team — Translation of the meanings of the Qur'an | Salafi |
| `fa-mostafakhorramd` | Mostafa Khorramdel — Translation of the meanings of the Qur'an | Shafi'i |
| `tafsir-mukhtasar-fa` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Persian edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `tafsir-saadi-fa` | Abd al-Rahman ibn Nasir al-Sa'di; Persian translator not named on the current official card — Tafsir al-Sa'di — Persian translation — Persian edition V1.0.0 | Hanbelî/Eserî (Farsça çeviri) |

### Portuguese (`pt`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `pt-helminasr` | Helmi Nasr — Translation of the meanings of the Qur'an | Sunni (King Fahd Complex) |
| `pt-samirelhayek` | Samir El Hayek — Translation of the meanings of the Qur'an | Sunni (general) |

### Russian (`ru`) — 4 config(s)

| config | translator / edition | school |
|---|---|---|
| `ru-abuadel` | Abu Adel — Translation of the meanings of the Qur'an | Athari/Salafi |
| `ru-elmirkuliev` | Elmir Kuliev — Translation of the meanings of the Qur'an | Salafi |
| `ru-ministryofawqaf` | Ministry Of Awqaf, Egypt — Translation of the meanings of the Qur'an | Ash'ari (Azhari) |
| `tafsir-saadi-ru` | Abd al-Rahman ibn Nasir al-Sa'di; Russian translator not named on the current official card — Tafsir al-Sa'di — Russian translation — Russian edition V1.0.0 | Hanbelî/Eserî (Rusça çeviri) |

### Serbian (`sr`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `sr-rowwadtranslati` | Rowwad Translation Center Islamhouse — Translation of the meanings of the Qur'an | Salafi/da'wah |
| `tafsir-mukhtasar-sr` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Serbian edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Shona (`sn`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `sn-abdullahjmadini` | Abdullah J. M. Adini And Students — Translation of the meanings of the Qur'an | Sunni da'wah (Madinah-trained) |

### Sindhi (`sd`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `sd-tajmehmoodamrot` | Taj Mehmood Amroti — Translation of the meanings of the Qur'an | Deobandi-Hanafi |

### Sinhala (`si`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `si-naseemismailand` | Naseem Ismail And Masoor Maulana, Kaleel — Translation of the meanings of the Qur'an | Shafi'i (Sri Lankan Sunni) |
| `si-wwwislamhouseco` | Www.islamhouse.com — Translation of the meanings of the Qur'an | Salafi da'wah |
| `tafsir-mukhtasar-si` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Sinhala edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Somali (`so`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `so-abdullahhasanja` | Abdullah Hasan Jacob — Translation of the meanings of the Qur'an | Sunni (Shafi'i) |
| `so-mahmudmuhammada` | Mahmud Muhammad Abduh — Translation of the meanings of the Qur'an | Sunni (Shafi'i) |
| `so-shaykhmahmoodmu` | Shaykh Mahmood Muhammad Abdu — Translation of the meanings of the Qur'an | Sunni (Shafi'i) |

### Sotho (`st`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `st-sheikheliaskeke` | Sheikh Elias Keketso Lelia — Translation of the meanings of the Qur'an | Sunni da'wah |

### Spanish (`es`) — 5 config(s)

| config | translator / edition | school |
|---|---|---|
| `es-abdulqadermouhe` | Abdul Qader Mouheddine, Sirhan Ali Sanchez. — Translation of the meanings of the Qur'an | Salafi |
| `es-islamicfoundati` | Islamic Foundation — Translation of the meanings of the Qur'an | Salafi/Sunni |
| `es-islamicfoundati1` | Islamic Foundation — Translation of the meanings of the Qur'an | Salafi/Sunni |
| `es-muhammadisagarc` | Muhammad Isa Garcia — Translation of the meanings of the Qur'an | Salafi |
| `tafsir-mukhtasar-es` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Spanish edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Swahili (`sw`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `sw-abdullahmuhamma` | Abdullah Muhammad Abu Bakr — Translation of the meanings of the Qur'an | Salafi da'wah |
| `tafsir-saadi-sw` | Abd al-Rahman ibn Nasir al-Sa'di; Swahili translator not named on the current official card — Tafsir al-Sa'di — Swahili translation — Swahili edition V1.0.0 | Hanbelî/Eserî (Svahili çeviri) |

### Tajik (`tg`) — 2 config(s)

| config | translator / edition | school |
|---|---|---|
| `tg-khojamirov` | Khoja Mirov — Translation of the meanings of the Qur'an | Sunni (Hanafi) |
| `tg-wwwislamhouseco` | Www.islamhouse.com — Translation of the meanings of the Qur'an | Salafi |

### Tamil (`ta`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `ta-abdulhameedbaqa` | Abdulhameed Baqavi — Translation of the meanings of the Qur'an | Shafi'i (Baqavi/traditionalist Sunni) |
| `ta-janturstfoundat` | Jan Turst Foundation — Translation of the meanings of the Qur'an | Sunni (general) |
| `tafsir-mukhtasar-ta` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Tamil edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |

### Tatar (`tt`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `tt-yakubibnnugman` | Yakub Ibn Nugman — Translation of the meanings of the Qur'an | Hanafi-Maturidi |

### Telugu (`te`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `tafsir-mukhtasar-te` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Telugu edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `te-abdulraheemmoha` | Abdul Raheem Mohammad Moulana — Translation of the meanings of the Qur'an | Sunni (King Fahd Complex) |
| `te-muhammadazizurr` | Muhammad Aziz Ur Rehman — Translation of the meanings of the Qur'an | Hanafi (traditional Sunni) |

### Thai (`th`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `tafsir-mukhtasar-th` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Thai edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `th-groupfromthesoc` | Group From The Society Of Graduates Of Thai Universities And Institutes — Translation of the meanings of the Qur'an | Sunni (general) |
| `th-kingfahadquranc` | King Fahad Quran Complex — Translation of the meanings of the Qur'an | Sunni (King Fahd Complex) |

### Twi (`tw`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `tw-sheikhharounism` | Sheikh Haroun Ismaeel — Translation of the meanings of the Qur'an | Sunni da'wah |

### Ukrainian (`uk`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `uk-drmikhailoyaqub` | Dr. Mikhailo Yaqubovic — Translation of the meanings of the Qur'an | Sunni (KFC-published) |
| `uk-mykhayloyakubov` | Mykhaylo Yakubovych — Translation of the meanings of the Qur'an | Sunni (KFC-published) |
| `uk-yakubovych` | Yakubovych — Translation of the meanings of the Qur'an | Sunni (KFC-published) |

### Urdu (`ur`) — 8 config(s)

| config | translator / edition | school |
|---|---|---|
| `tafsir-saadi-ur` | Abd al-Rahman ibn Nasir al-Sa'di; Urdu translator not named on the current official card — Tafsir al-Sa'di — Urdu translation — Urdu edition V1.0.0 | Hanbelî/Eserî (Urduca çeviri) |
| `ur-abulaalamaududi` | Abul A Ala Maududi — Translation of the meanings of the Qur'an | Sunni-revivalist (Jamaat-e-Islami, Hanafi-leaning) |
| `ur-fatehmuhammadja` | Fateh Muhammad Jalandhry — Translation of the meanings of the Qur'an | Hanafi (mainstream Sunni) |
| `ur-mahmoodulhassan` | Mahmood Ul Hassan — Translation of the meanings of the Qur'an | Deobandi |
| `ur-muhammadjunagar` | Muhammad Junagarhi — Translation of the meanings of the Qur'an | Salafi / Ahl-e-Hadith |
| `ur-muhammadjunagar1` | Muhammad Junagarhi, Muhammad Kazim — Translation of the meanings of the Qur'an | Salafi / Ahl-e-Hadith |
| `ur-muhammadkaramsh` | Muhammad Karam Shah Al Azhari — Translation of the meanings of the Qur'an | Barelvi (orthodox-Sufi) |
| `ur-muhammadtaqiusm` | Muhammad Taqi Usmani — Translation of the meanings of the Qur'an | Deobandi |

### Uyghur (`ug`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `tafsir-mukhtasar-ug` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Uyghur edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `ug-muhammadsaleh` | Muhammad Saleh — Translation of the meanings of the Qur'an | Hanafi |
| `ug-shaykhmuhammads` | Shaykh Muhammad Saleh — Translation of the meanings of the Qur'an | Hanafi / da'wah |

### Uzbek (`uz`) — 5 config(s)

| config | translator / edition | school |
|---|---|---|
| `tafsir-mukhtasar-uz` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Uzbek edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `tafsir-muyassar-uz` | At-Tafsir Al-Muyassar committee; Uzbek translation by Ismail Yaqub; reviewed by Islamic Center IxlosOrg — At-Tafsir Al-Muyassar — Uzbek translation — Uzbek edition V1.0.0 | Eserî (heyet; Özbekçe çeviri) |
| `uz-alaaudeenmansou` | Alaaudeen Mansour — Translation of the meanings of the Qur'an | Hanafi-Maturidi |
| `uz-alauddinmansour` | Alauddin Mansour — Translation of the meanings of the Qur'an | Hanafi-Maturidi |
| `uz-muhammadsodikmu` | Muhammad Sodik Muhammad Yusuf — Translation of the meanings of the Qur'an | Hanafi-Maturidi |

### Vietnamese (`vi`) — 3 config(s)

| config | translator / edition | school |
|---|---|---|
| `tafsir-mukhtasar-vi` | Tafsir Center for Quranic Studies (editorial and translation team) — Al-Mukhtasar in Interpreting the Noble Quran — Vietnamese edition V1.0.0 | Ehl-i Sünnet (çağdaş heyet; mezhep-özel değil) |
| `vi-hassanabdulkari` | Hassan Abdulkarim — Translation of the meanings of the Qur'an | Sunni (general) |
| `vi-rowwadtranslati` | Rowwad Translation Center — Translation of the meanings of the Qur'an | Salafi da'wah |

### Xhosa (`xh`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `xh-imaamismaaeelng` | Imaam Ismaaeel Ngqoyiyana — Translation of the meanings of the Qur'an | Sunni da'wah |

### Yoruba (`yo`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `yo-shaykhaburahima` | Shaykh Abu Rahimah Mikael Aykyuni — Translation of the meanings of the Qur'an | Sunni da'wah |

### Zulu (`zu`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `zu-iqembulezifundi` | Iqembu Lezifundiswa, Mussa Muhammad Telela , Uthman Mfanafuthi Msomi, Moulana Abdur Rahman Chilipa, Haji Ibrahim Mondli Japhet Mthembu, Moulana Imran Ngcobo, Moulana Eshaaq Osman — Translation of the meanings of the Qur'an | Sunni da'wah |

### ilp (`ilp`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `ilp-abdulazizgroaal` | Abdul Aziz Gro Aalem Saromintang — Translation of the meanings of the Qur'an | Shafi'i |

### luy (`luy`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `luy-mohammadramadha` | Mohammad Ramadhan Sebwa, Ramadhan Hajj Ndeka, Ismail Were, Musa Murasi Salim Kukuya, Yusuf Shiundu Malala, Yahya Wafula Ojwang, Haroon Albert Msah — Translation of the meanings of the Qur'an | Shafi'i/Sunni da'wah |

### mrw (`mrw`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `mrw-guroalimsaroman` | Guro Alim Saromantang — Translation of the meanings of the Qur'an | Shafi'i/Sunni |

### prs (`prs`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `prs-mawlawimuhammad` | Mawlawi Muhammad Anwar Badkhashani — Translation of the meanings of the Qur'an | Hanafi (Afghan/Deobandi-leaning) |

### run (`run`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `run-sheikhamissirad` | Sheikh Amissi Radjabu Ntamba — Translation of the meanings of the Qur'an | Shafi'i/Sunni |

### yuw (`yuw`) — 1 config(s)

| config | translator / edition | school |
|---|---|---|
| `yuw-muhammadbinabdu` | Muhammad Bin Abdul Hamid Silika — Translation of the meanings of the Qur'an | Sunni da'wah |

## The QuranLab family

These datasets are built by the same volunteers and are meant to be used together; they join on
shared keys — `verse_key` on the Qur'an side, `hadith_key` on the Sunnah side.

| Dataset | What it holds |
|---|---|
| [`quranlab/quran`](https://huggingface.co/datasets/quranlab/quran) | Qur'an text, multilingual translations, tafsir, word-level morphology |
| [`quranlab/quran-tafsir`](https://huggingface.co/datasets/quranlab/quran-tafsir) | Viewer-friendly open-license Sunni tafsir collection |
| [`quranlab/quran-audio`](https://huggingface.co/datasets/quranlab/quran-audio) | Recitation reference manifest and CC-BY word timing (references only, no audio files) |
| [`quranlab/hadith`](https://huggingface.co/datasets/quranlab/hadith) | Nine Books Arabic matn, translations, and normalized authenticity grades |
| [`quranlab/islamic-corpus-graph`](https://huggingface.co/datasets/quranlab/islamic-corpus-graph) | The above linked into one structured graph, with retrieval passages and a held-out evaluation set |

You are reading the card for **`quranlab/quran`**. Corrections, additions, and removal requests are
welcome on any of them through the **Community** tab.

## Quality, and how to check it yourself

Nothing is released until the integrity gate passes. Every claim below is
something you can re-run rather than take on trust — here on the published data,
not in our build tree:

| What is guaranteed | Evidence |
|---|---|
| Verse-grain configs share one spine | the `verse_key` sequence is asserted identical across all 298 verse-grain configs, so cross-language joins cannot silently misalign; `morphology-ar` (sub-verse) and `tafsir-kuranyolu-tr` (passage) are the two deliberate exceptions and carry their own documented keys |
| Canonical structure is complete | 114 surahs · 6,236 ayahs · 30 juz · 60 hizb · 240 hizb-quarters · 604 pages · 7 manzils, checked per config |
| Arabic is verbatim | Tanzil Uthmani and Simple-Clean v1.1 kept byte-for-byte; no normalisation applied |
| Sajda and basmala rules hold | sajda count is 14 or 15; basmala present only at 1:1 and absent at 9:1 |
| No silent gaps | a config with missing or empty cells is dropped from the build rather than shipped partial; expected source gaps are hash-pinned in the registry |
| Only Ahl al-Sunnah sources | each edition carries a theological classification in `metadata/translations.csv`; the excluded list is enforced in code, not by convention |

```python
from datasets import load_dataset

ar = load_dataset("quranlab/quran", "arabic-uthmani", split="train")
tr = load_dataset("quranlab/quran", "tr-diyanet",     split="train")

assert ar["verse_key"] == tr["verse_key"]      # one spine, every config
assert len(ar) == 6236 and ar[0]["verse_key"] == "1:1"
assert ar[-1]["verse_key"] == "114:6"
```

Where a source is genuinely missing, the row is published **empty and labelled**
rather than filled by guessing from a neighbouring entry. Coverage numbers in
this card count only real content.

## How it was built

We assembled this corpus ourselves: each edition is the **work of its translator**,
aligned by hand-checked rules onto the canonical 6,236-ayah spine, then validated
(114 surahs · 6,236 ayahs · juz/hizb/page/ruku/manzil/sajda structure · identical
`verse_key` spine across every config · no empty cells) before release. The Arabic
is Tanzil's Uthmani and Simple-Clean text, kept **verbatim**. Per-edition details —
translator, edition, school, and terms — are in `metadata/translations.csv` and
`LICENSES.md`.

## Notes

Public-domain and CC texts are kept verbatim; everything else is included with
full credit to its author or publisher. If you hold rights to a work here and
would like it removed, open a discussion on the **Community** tab — we take it
down promptly, no questions asked.

## Citation

```bibtex
@misc{quranlab_quran_2026,
  title        = {QuranLab — Verse-Aligned Multilingual Quran Corpus},
  author       = {QuranLab},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/quranlab/quran}}
}
```
