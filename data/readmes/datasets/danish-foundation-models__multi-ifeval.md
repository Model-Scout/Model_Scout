---
language:
- ab
- ace
- ady
- af
- alt
- am
- ami
- an
- ang
- anp
- ar
- arc
- ary
- arz
- as
- ast
- atj
- av
- avk
- awa
- ay
- az
- azb
- ba
- ban
- bar
- bcl
- be
- bg
- bi
- bjn
- blk
- bm
- bn
- bo
- bpy
- br
- bs
- bug
- bxr
- ca
- cdo
- ce
- ceb
- ch
- chr
- chy
- ckb
- co
- cr
- crh
- cs
- csb
- cu
- cv
- cy
- da
- dag
- de
- din
- diq
- dsb
- dty
- dv
- dz
- ee
- el
- en
- eo
- es
- et
- eu
- ext
- fa
- fat
- ff
- fi
- fj
- fo
- fon
- fr
- frp
- frr
- fur
- fy
- ga
- gag
- gan
- gcr
- gd
- gl
- glk
- gn
- gom
- gor
- got
- gpe
- gu
- guc
- gur
- guw
- gv
- ha
- hak
- haw
- he
- hi
- hif
- hr
- hsb
- ht
- hu
- hy
- hyw
- ia
- id
- ie
- ig
- ik
- ilo
- inh
- io
- is
- it
- iu
- ja
- jam
- jbo
- ka
- kaa
- kab
- kbd
- kbp
- kcg
- kg
- ki
- kk
- kl
- km
- kn
- ko
- koi
- krc
- ks
- ku
- kv
- kw
- ky
- la
- lad
- lb
- lbe
- lez
- lfn
- lg
- li
- lij
- lld
- lmo
- ln
- lo
- lt
- ltg
- lv
- mad
- mai
- mdf
- mg
- mhr
- mi
- min
- mk
- ml
- mn
- mni
- mnw
- mr
- mrj
- ms
- mt
- mwl
- my
- myv
- mzn
- nap
- nds
- ne
- new
- nia
- nl
- nn
- 'no'
- nov
- nqo
- nso
- nv
- ny
- oc
- olo
- om
- or
- os
- pa
- pag
- pam
- pap
- pcd
- pcm
- pdc
- pfl
- pi
- pl
- pms
- pnb
- pnt
- ps
- pt
- pwn
- qu
- rm
- rmy
- rn
- ro
- ru
- rue
- rw
- sa
- sah
- sat
- sc
- scn
- sco
- sd
- se
- sg
- shi
- shn
- si
- sk
- skr
- sl
- sm
- smn
- sn
- so
- sq
- sr
- srn
- ss
- st
- stq
- su
- sv
- sw
- szl
- szy
- ta
- tay
- tcy
- te
- tet
- tg
- th
- ti
- tk
- tl
- tly
- tn
- to
- tpi
- tr
- trv
- ts
- tt
- tum
- ty
- tyv
- udm
- ug
- uk
- ur
- uz
- ve
- vec
- vep
- vi
- vls
- vo
- wa
- war
- wo
- wuu
- xal
- xh
- xmf
- yi
- yo
- yue
- za
- zea
- zu
language_bcp47:
- pt-br
- pt-pt
- zh-cn
- zh-tw
license: cc-by-nc-sa-4.0
dataset_info:
- config_name: ab
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 380501
    num_examples: 524
  download_size: 138693
  dataset_size: 380501
- config_name: ace
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 304834
    num_examples: 524
  download_size: 109454
  dataset_size: 304834
- config_name: ady
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 386288
    num_examples: 523
  download_size: 139815
  dataset_size: 386288
- config_name: af
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 284934
    num_examples: 524
  download_size: 96634
  dataset_size: 284934
- config_name: alt
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 389382
    num_examples: 524
  download_size: 140381
  dataset_size: 389382
- config_name: am
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 380636
    num_examples: 524
  download_size: 137089
  dataset_size: 380636
- config_name: ami
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 311536
    num_examples: 524
  download_size: 115430
  dataset_size: 311536
- config_name: an
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 289655
    num_examples: 524
  download_size: 100993
  dataset_size: 289655
- config_name: ang
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290054
    num_examples: 524
  download_size: 109873
  dataset_size: 290054
- config_name: anp
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 478632
    num_examples: 524
  download_size: 153610
  dataset_size: 478632
- config_name: ar
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 344464
    num_examples: 523
  download_size: 121117
  dataset_size: 344464
- config_name: arc
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 329200
    num_examples: 524
  download_size: 114112
  dataset_size: 329200
- config_name: ary
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 349590
    num_examples: 523
  download_size: 123917
  dataset_size: 349590
- config_name: arz
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 332337
    num_examples: 524
  download_size: 115387
  dataset_size: 332337
- config_name: as
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 489450
    num_examples: 524
  download_size: 156513
  dataset_size: 489450
- config_name: ast
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 289817
    num_examples: 523
  download_size: 100596
  dataset_size: 289817
- config_name: atj
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 298405
    num_examples: 512
  download_size: 103623
  dataset_size: 298405
- config_name: av
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 420966
    num_examples: 523
  download_size: 150768
  dataset_size: 420966
- config_name: avk
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 263067
    num_examples: 520
  download_size: 96479
  dataset_size: 263067
- config_name: awa
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 462935
    num_examples: 524
  download_size: 149932
  dataset_size: 462935
- config_name: ay
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 299483
    num_examples: 523
  download_size: 108400
  dataset_size: 299483
- config_name: az
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 304890
    num_examples: 523
  download_size: 104713
  dataset_size: 304890
- config_name: azb
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 391386
    num_examples: 524
  download_size: 136879
  dataset_size: 391386
- config_name: ba
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 385438
    num_examples: 524
  download_size: 132361
  dataset_size: 385438
- config_name: ban
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 301947
    num_examples: 523
  download_size: 105191
  dataset_size: 301947
- config_name: bar
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 286077
    num_examples: 524
  download_size: 107559
  dataset_size: 286077
- config_name: bcl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 307215
    num_examples: 523
  download_size: 106180
  dataset_size: 307215
- config_name: be
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 387682
    num_examples: 524
  download_size: 175279
  dataset_size: 387682
- config_name: bg
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 343567
    num_examples: 478
  download_size: 155946
  dataset_size: 343567
- config_name: bi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290791
    num_examples: 524
  download_size: 94655
  dataset_size: 290791
- config_name: bjn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 300459
    num_examples: 524
  download_size: 138678
  dataset_size: 300459
- config_name: blk
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 611668
    num_examples: 523
  download_size: 189964
  dataset_size: 611668
- config_name: bm
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 298415
    num_examples: 520
  download_size: 104862
  dataset_size: 298415
- config_name: bn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 502160
    num_examples: 522
  download_size: 155243
  dataset_size: 502160
- config_name: bo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 586181
    num_examples: 524
  download_size: 167739
  dataset_size: 586181
- config_name: bpy
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 491717
    num_examples: 523
  download_size: 157038
  dataset_size: 491717
- config_name: br
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 289259
    num_examples: 524
  download_size: 97706
  dataset_size: 289259
- config_name: bs
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 253077
    num_examples: 477
  download_size: 122870
  dataset_size: 253077
- config_name: bug
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 300688
    num_examples: 523
  download_size: 146540
  dataset_size: 300688
- config_name: bxr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 400587
    num_examples: 524
  download_size: 139687
  dataset_size: 400587
- config_name: ca
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 261419
    num_examples: 478
  download_size: 123116
  dataset_size: 261419
- config_name: cdo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 306792
    num_examples: 522
  download_size: 120228
  dataset_size: 306792
- config_name: ce
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 373207
    num_examples: 519
  download_size: 132976
  dataset_size: 373207
- config_name: ceb
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 306948
    num_examples: 524
  download_size: 102116
  dataset_size: 306948
- config_name: ch
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 298144
    num_examples: 524
  download_size: 105653
  dataset_size: 298144
- config_name: chr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 367568
    num_examples: 512
  download_size: 123202
  dataset_size: 367568
- config_name: chy
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 243377
    num_examples: 399
  download_size: 83363
  dataset_size: 243377
- config_name: ckb
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 388490
    num_examples: 524
  download_size: 134584
  dataset_size: 388490
- config_name: cn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 276586
    num_examples: 524
  download_size: 101679
  dataset_size: 276586
- config_name: co
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 291941
    num_examples: 524
  download_size: 101634
  dataset_size: 291941
- config_name: cr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 386603
    num_examples: 515
  download_size: 141024
  dataset_size: 386603
- config_name: crh
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 299414
    num_examples: 524
  download_size: 106426
  dataset_size: 299414
- config_name: cs
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290239
    num_examples: 523
  download_size: 140741
  dataset_size: 290239
- config_name: csb
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 301458
    num_examples: 524
  download_size: 149189
  dataset_size: 301458
- config_name: cu
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 376234
    num_examples: 523
  download_size: 145282
  dataset_size: 376234
- config_name: cv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 375863
    num_examples: 524
  download_size: 171872
  dataset_size: 375863
- config_name: cy
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 288019
    num_examples: 524
  download_size: 133051
  dataset_size: 288019
- config_name: da
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 279903
    num_examples: 524
  download_size: 132672
  dataset_size: 279903
- config_name: dag
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 301478
    num_examples: 522
  download_size: 109247
  dataset_size: 301478
- config_name: de
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 303862
    num_examples: 524
  download_size: 144405
  dataset_size: 303862
- config_name: din
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 299912
    num_examples: 521
  download_size: 106908
  dataset_size: 299912
- config_name: diq
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 298623
    num_examples: 524
  download_size: 114588
  dataset_size: 298623
- config_name: dsb
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 293412
    num_examples: 524
  download_size: 143638
  dataset_size: 293412
- config_name: dty
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 480994
    num_examples: 522
  download_size: 157457
  dataset_size: 480994
- config_name: dv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 452121
    num_examples: 524
  download_size: 154202
  dataset_size: 452121
- config_name: dz
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 581311
    num_examples: 524
  download_size: 221257
  dataset_size: 581311
- config_name: ee
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 295742
    num_examples: 524
  download_size: 103021
  dataset_size: 295742
- config_name: el
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 417815
    num_examples: 521
  download_size: 186881
  dataset_size: 417815
- config_name: en
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 307669
    num_examples: 522
  download_size: 149646
  dataset_size: 307669
- config_name: eo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 279025
    num_examples: 524
  download_size: 95145
  dataset_size: 279025
- config_name: es
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 294194
    num_examples: 524
  download_size: 137460
  dataset_size: 294194
- config_name: et
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 279547
    num_examples: 524
  download_size: 134653
  dataset_size: 279547
- config_name: eu
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 288630
    num_examples: 524
  download_size: 133833
  dataset_size: 288630
- config_name: ext
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 293213
    num_examples: 524
  download_size: 140705
  dataset_size: 293213
- config_name: fa
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 374703
    num_examples: 523
  download_size: 128293
  dataset_size: 374703
- config_name: fat
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 299166
    num_examples: 524
  download_size: 107520
  dataset_size: 299166
- config_name: ff
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 295131
    num_examples: 522
  download_size: 111433
  dataset_size: 295131
- config_name: fi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290796
    num_examples: 524
  download_size: 139287
  dataset_size: 290796
- config_name: fj
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 316250
    num_examples: 520
  download_size: 106830
  dataset_size: 316250
- config_name: fo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 259385
    num_examples: 477
  download_size: 125967
  dataset_size: 259385
- config_name: fon
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 318962
    num_examples: 523
  download_size: 116670
  dataset_size: 318962
- config_name: fr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 301377
    num_examples: 524
  download_size: 141544
  dataset_size: 301377
- config_name: frp
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 299583
    num_examples: 524
  download_size: 110324
  dataset_size: 299583
- config_name: frr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 285802
    num_examples: 524
  download_size: 108844
  dataset_size: 285802
- config_name: fur
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290753
    num_examples: 524
  download_size: 102670
  dataset_size: 290753
- config_name: fy
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 289936
    num_examples: 524
  download_size: 134433
  dataset_size: 289936
- config_name: ga
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 301831
    num_examples: 524
  download_size: 104905
  dataset_size: 301831
- config_name: gag
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 288057
    num_examples: 523
  download_size: 105128
  dataset_size: 288057
- config_name: gan
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 275870
    num_examples: 524
  download_size: 102180
  dataset_size: 275870
- config_name: gcr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 281850
    num_examples: 524
  download_size: 96466
  dataset_size: 281850
- config_name: gd
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 311460
    num_examples: 524
  download_size: 106488
  dataset_size: 311460
- config_name: gl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 289444
    num_examples: 524
  download_size: 98469
  dataset_size: 289444
- config_name: glk
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 369598
    num_examples: 524
  download_size: 141623
  dataset_size: 369598
- config_name: gn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 300600
    num_examples: 524
  download_size: 104667
  dataset_size: 300600
- config_name: gom
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 456127
    num_examples: 524
  download_size: 202514
  dataset_size: 456127
- config_name: gor
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 296445
    num_examples: 523
  download_size: 140606
  dataset_size: 296445
- config_name: got
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 551084
    num_examples: 513
  download_size: 234512
  dataset_size: 551084
- config_name: gpe
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 279445
    num_examples: 524
  download_size: 93565
  dataset_size: 279445
- config_name: gu
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 471708
    num_examples: 521
  download_size: 150367
  dataset_size: 471708
- config_name: guc
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 325409
    num_examples: 521
  download_size: 110075
  dataset_size: 325409
- config_name: gur
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 302312
    num_examples: 520
  download_size: 106620
  dataset_size: 302312
- config_name: guw
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 320044
    num_examples: 523
  download_size: 111640
  dataset_size: 320044
- config_name: gv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 291206
    num_examples: 524
  download_size: 104171
  dataset_size: 291206
- config_name: ha
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 298139
    num_examples: 523
  download_size: 104796
  dataset_size: 298139
- config_name: hak
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 330234
    num_examples: 524
  download_size: 128728
  dataset_size: 330234
- config_name: haw
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 315433
    num_examples: 523
  download_size: 105024
  dataset_size: 315433
- config_name: he
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 325300
    num_examples: 520
  download_size: 112306
  dataset_size: 325300
- config_name: hi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 488584
    num_examples: 522
  download_size: 153269
  dataset_size: 488584
- config_name: hif
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 291736
    num_examples: 524
  download_size: 102081
  dataset_size: 291736
- config_name: hr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 254991
    num_examples: 478
  download_size: 123149
  dataset_size: 254991
- config_name: hsb
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290466
    num_examples: 524
  download_size: 107643
  dataset_size: 290466
- config_name: ht
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 275161
    num_examples: 524
  download_size: 91595
  dataset_size: 275161
- config_name: hu
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 264993
    num_examples: 475
  download_size: 128018
  dataset_size: 264993
- config_name: hy
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 389476
    num_examples: 519
  download_size: 134898
  dataset_size: 389476
- config_name: hyw
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 400772
    num_examples: 521
  download_size: 143192
  dataset_size: 400772
- config_name: ia
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 284581
    num_examples: 522
  download_size: 97166
  dataset_size: 284581
- config_name: id
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 295900
    num_examples: 524
  download_size: 97659
  dataset_size: 295900
- config_name: ie
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 279966
    num_examples: 524
  download_size: 97752
  dataset_size: 279966
- config_name: ig
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 315068
    num_examples: 524
  download_size: 142379
  dataset_size: 315068
- config_name: ik
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 278029
    num_examples: 515
  download_size: 101013
  dataset_size: 278029
- config_name: ilo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 314625
    num_examples: 524
  download_size: 107506
  dataset_size: 314625
- config_name: inh
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 377939
    num_examples: 523
  download_size: 134078
  dataset_size: 377939
- config_name: io
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 275188
    num_examples: 523
  download_size: 94346
  dataset_size: 275188
- config_name: is
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 262465
    num_examples: 478
  download_size: 125861
  dataset_size: 262465
- config_name: it
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292322
    num_examples: 524
  download_size: 137802
  dataset_size: 292322
- config_name: iu
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 415634
    num_examples: 523
  download_size: 142996
  dataset_size: 415634
- config_name: ja
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 338618
    num_examples: 524
  download_size: 113673
  dataset_size: 338618
- config_name: jam
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 274547
    num_examples: 524
  download_size: 134674
  dataset_size: 274547
- config_name: jbo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 286674
    num_examples: 511
  download_size: 131742
  dataset_size: 286674
- config_name: ka
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 502101
    num_examples: 524
  download_size: 151786
  dataset_size: 502101
- config_name: kaa
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 302261
    num_examples: 522
  download_size: 107533
  dataset_size: 302261
- config_name: kab
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 297756
    num_examples: 524
  download_size: 111347
  dataset_size: 297756
- config_name: kbd
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 388961
    num_examples: 524
  download_size: 139467
  dataset_size: 388961
- config_name: kbp
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 327540
    num_examples: 519
  download_size: 118379
  dataset_size: 327540
- config_name: kcg
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 314335
    num_examples: 506
  download_size: 108195
  dataset_size: 314335
- config_name: kg
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 300990
    num_examples: 522
  download_size: 100959
  dataset_size: 300990
- config_name: ki
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 320498
    num_examples: 523
  download_size: 116637
  dataset_size: 320498
- config_name: kk
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 385220
    num_examples: 524
  download_size: 132059
  dataset_size: 385220
- config_name: kl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 303307
    num_examples: 524
  download_size: 110761
  dataset_size: 303307
- config_name: km
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 535857
    num_examples: 523
  download_size: 168566
  dataset_size: 535857
- config_name: kn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 521530
    num_examples: 520
  download_size: 160325
  dataset_size: 521530
- config_name: ko
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 318567
    num_examples: 524
  download_size: 110021
  dataset_size: 318567
- config_name: koi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 370800
    num_examples: 523
  download_size: 172941
  dataset_size: 370800
- config_name: krc
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 398268
    num_examples: 524
  download_size: 138282
  dataset_size: 398268
- config_name: ks
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 419479
    num_examples: 523
  download_size: 155941
  dataset_size: 419479
- config_name: ku
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 300961
    num_examples: 524
  download_size: 107928
  dataset_size: 300961
- config_name: kv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 366959
    num_examples: 524
  download_size: 130094
  dataset_size: 366959
- config_name: kw
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 279019
    num_examples: 523
  download_size: 100689
  dataset_size: 279019
- config_name: ky
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 391574
    num_examples: 523
  download_size: 135443
  dataset_size: 391574
- config_name: la
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 282161
    num_examples: 524
  download_size: 103110
  dataset_size: 282161
- config_name: lad
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290400
    num_examples: 524
  download_size: 104982
  dataset_size: 290400
- config_name: lb
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 293970
    num_examples: 524
  download_size: 103555
  dataset_size: 293970
- config_name: lbe
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 410001
    num_examples: 523
  download_size: 146381
  dataset_size: 410001
- config_name: lez
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 391484
    num_examples: 524
  download_size: 139572
  dataset_size: 391484
- config_name: lfn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 282190
    num_examples: 524
  download_size: 130437
  dataset_size: 282190
- config_name: lg
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 309988
    num_examples: 524
  download_size: 147960
  dataset_size: 309988
- config_name: li
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290560
    num_examples: 524
  download_size: 139819
  dataset_size: 290560
- config_name: lij
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 296876
    num_examples: 524
  download_size: 114235
  dataset_size: 296876
- config_name: lld
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 283334
    num_examples: 524
  download_size: 106806
  dataset_size: 283334
- config_name: lmo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292494
    num_examples: 524
  download_size: 110097
  dataset_size: 292494
- config_name: ln
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 300820
    num_examples: 516
  download_size: 105205
  dataset_size: 300820
- config_name: lo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 484601
    num_examples: 523
  download_size: 154914
  dataset_size: 484601
- config_name: lt
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 264886
    num_examples: 478
  download_size: 128275
  dataset_size: 264886
- config_name: ltg
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 289889
    num_examples: 524
  download_size: 143693
  dataset_size: 289889
- config_name: lv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 258513
    num_examples: 478
  download_size: 125891
  dataset_size: 258513
- config_name: mad
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 311194
    num_examples: 522
  download_size: 113975
  dataset_size: 311194
- config_name: mai
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 475170
    num_examples: 524
  download_size: 151387
  dataset_size: 475170
- config_name: mdf
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 379615
    num_examples: 523
  download_size: 136779
  dataset_size: 379615
- config_name: mg
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 315729
    num_examples: 523
  download_size: 143044
  dataset_size: 315729
- config_name: mhr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 370300
    num_examples: 521
  download_size: 128821
  dataset_size: 370300
- config_name: mi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 304443
    num_examples: 524
  download_size: 101446
  dataset_size: 304443
- config_name: min
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 294623
    num_examples: 524
  download_size: 100369
  dataset_size: 294623
- config_name: mk
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 383533
    num_examples: 522
  download_size: 132248
  dataset_size: 383533
- config_name: ml
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 564536
    num_examples: 522
  download_size: 220043
  dataset_size: 564536
- config_name: mn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 394538
    num_examples: 524
  download_size: 135581
  dataset_size: 394538
- config_name: mni
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 487098
    num_examples: 519
  download_size: 155619
  dataset_size: 487098
- config_name: mnw
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 524336
    num_examples: 523
  download_size: 167447
  dataset_size: 524336
- config_name: mr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 489316
    num_examples: 524
  download_size: 153974
  dataset_size: 489316
- config_name: mrj
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 376941
    num_examples: 522
  download_size: 135321
  dataset_size: 376941
- config_name: ms
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 301389
    num_examples: 524
  download_size: 99931
  dataset_size: 301389
- config_name: mt
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290428
    num_examples: 524
  download_size: 99447
  dataset_size: 290428
- config_name: mwl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 289733
    num_examples: 523
  download_size: 101922
  dataset_size: 289733
- config_name: my
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 594034
    num_examples: 523
  download_size: 181112
  dataset_size: 594034
- config_name: myv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 390124
    num_examples: 524
  download_size: 138799
  dataset_size: 390124
- config_name: mzn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 367861
    num_examples: 524
  download_size: 129727
  dataset_size: 367861
- config_name: nap
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292762
    num_examples: 524
  download_size: 106917
  dataset_size: 292762
- config_name: nds
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292574
    num_examples: 524
  download_size: 139057
  dataset_size: 292574
- config_name: ne
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 515654
    num_examples: 522
  download_size: 155027
  dataset_size: 515654
- config_name: new
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 479594
    num_examples: 524
  download_size: 152459
  dataset_size: 479594
- config_name: nia
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 304659
    num_examples: 524
  download_size: 108662
  dataset_size: 304659
- config_name: nl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 289855
    num_examples: 524
  download_size: 98471
  dataset_size: 289855
- config_name: nn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 280507
    num_examples: 524
  download_size: 134022
  dataset_size: 280507
- config_name: 'no'
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 279311
    num_examples: 524
  download_size: 132378
  dataset_size: 279311
- config_name: nov
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 272879
    num_examples: 523
  download_size: 96367
  dataset_size: 272879
- config_name: nqo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 413112
    num_examples: 524
  download_size: 141153
  dataset_size: 413112
- config_name: nso
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 306127
    num_examples: 520
  download_size: 106856
  dataset_size: 306127
- config_name: nv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 355682
    num_examples: 523
  download_size: 125400
  dataset_size: 355682
- config_name: ny
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 305559
    num_examples: 522
  download_size: 105322
  dataset_size: 305559
- config_name: oc
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292291
    num_examples: 524
  download_size: 102063
  dataset_size: 292291
- config_name: olo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 285464
    num_examples: 524
  download_size: 140471
  dataset_size: 285464
- config_name: om
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 311529
    num_examples: 524
  download_size: 110853
  dataset_size: 311529
- config_name: or
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 518265
    num_examples: 524
  download_size: 160600
  dataset_size: 518265
- config_name: os
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 379176
    num_examples: 523
  download_size: 172191
  dataset_size: 379176
- config_name: pa
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 488347
    num_examples: 524
  download_size: 156501
  dataset_size: 488347
- config_name: pag
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 303422
    num_examples: 524
  download_size: 106246
  dataset_size: 303422
- config_name: pam
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 310159
    num_examples: 523
  download_size: 107680
  dataset_size: 310159
- config_name: pap
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 287336
    num_examples: 524
  download_size: 134529
  dataset_size: 287336
- config_name: pcd
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 297482
    num_examples: 524
  download_size: 111250
  dataset_size: 297482
- config_name: pcm
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 281953
    num_examples: 524
  download_size: 95915
  dataset_size: 281953
- config_name: pdc
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 286639
    num_examples: 524
  download_size: 104283
  dataset_size: 286639
- config_name: pfl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292149
    num_examples: 524
  download_size: 110215
  dataset_size: 292149
- config_name: pi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 439864
    num_examples: 524
  download_size: 149101
  dataset_size: 439864
- config_name: pl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 295651
    num_examples: 524
  download_size: 143223
  dataset_size: 295651
- config_name: pms
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290334
    num_examples: 524
  download_size: 104991
  dataset_size: 290334
- config_name: pnb
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 380188
    num_examples: 524
  download_size: 132142
  dataset_size: 380188
- config_name: pnt
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 400927
    num_examples: 524
  download_size: 140706
  dataset_size: 400927
- config_name: ps
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 379307
    num_examples: 524
  download_size: 171920
  dataset_size: 379307
- config_name: pt
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 291354
    num_examples: 523
  download_size: 100759
  dataset_size: 291354
- config_name: pt-pt
  features:
  - name: prompt
    dtype: string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 293819
    num_examples: 523
  download_size: 135298
  dataset_size: 293819
- config_name: pwn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 301850
    num_examples: 504
  download_size: 106038
  dataset_size: 301850
- config_name: qu
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 300481
    num_examples: 524
  download_size: 105908
  dataset_size: 300481
- config_name: rm
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290372
    num_examples: 524
  download_size: 103944
  dataset_size: 290372
- config_name: rmy
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290253
    num_examples: 523
  download_size: 110081
  dataset_size: 290253
- config_name: rn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 304071
    num_examples: 523
  download_size: 110753
  dataset_size: 304071
- config_name: ro
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 267673
    num_examples: 477
  download_size: 126799
  dataset_size: 267673
- config_name: ru
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 388558
    num_examples: 524
  download_size: 137605
  dataset_size: 388558
- config_name: rue
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 371589
    num_examples: 524
  download_size: 136388
  dataset_size: 371589
- config_name: rw
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 302258
    num_examples: 524
  download_size: 108462
  dataset_size: 302258
- config_name: sa
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 517723
    num_examples: 524
  download_size: 170672
  dataset_size: 517723
- config_name: sah
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 387280
    num_examples: 519
  download_size: 136337
  dataset_size: 387280
- config_name: sat
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 524708
    num_examples: 524
  download_size: 164709
  dataset_size: 524708
- config_name: sc
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 304462
    num_examples: 524
  download_size: 142981
  dataset_size: 304462
- config_name: scn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290210
    num_examples: 524
  download_size: 103649
  dataset_size: 290210
- config_name: sco
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 273633
    num_examples: 524
  download_size: 94373
  dataset_size: 273633
- config_name: sd
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 371254
    num_examples: 524
  download_size: 167357
  dataset_size: 371254
- config_name: se
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 290258
    num_examples: 520
  download_size: 134530
  dataset_size: 290258
- config_name: sg
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 310939
    num_examples: 521
  download_size: 107408
  dataset_size: 310939
- config_name: shi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 286503
    num_examples: 523
  download_size: 111370
  dataset_size: 286503
- config_name: shn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 594127
    num_examples: 524
  download_size: 243910
  dataset_size: 594127
- config_name: si
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 504120
    num_examples: 524
  download_size: 165471
  dataset_size: 504120
- config_name: sk
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 258967
    num_examples: 478
  download_size: 127362
  dataset_size: 258967
- config_name: skr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 381995
    num_examples: 524
  download_size: 135538
  dataset_size: 381995
- config_name: sl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 282192
    num_examples: 524
  download_size: 137802
  dataset_size: 282192
- config_name: sm
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 302526
    num_examples: 521
  download_size: 103321
  dataset_size: 302526
- config_name: smn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 294063
    num_examples: 523
  download_size: 108149
  dataset_size: 294063
- config_name: sn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 306465
    num_examples: 524
  download_size: 144060
  dataset_size: 306465
- config_name: so
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 303452
    num_examples: 524
  download_size: 110638
  dataset_size: 303452
- config_name: sq
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 274701
    num_examples: 478
  download_size: 128928
  dataset_size: 274701
- config_name: sr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 303067
    num_examples: 476
  download_size: 148821
  dataset_size: 303067
- config_name: srn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 282310
    num_examples: 523
  download_size: 129012
  dataset_size: 282310
- config_name: ss
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 304107
    num_examples: 520
  download_size: 110408
  dataset_size: 304107
- config_name: st
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292842
    num_examples: 513
  download_size: 103307
  dataset_size: 292842
- config_name: stq
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 291322
    num_examples: 524
  download_size: 106404
  dataset_size: 291322
- config_name: su
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 293825
    num_examples: 524
  download_size: 100131
  dataset_size: 293825
- config_name: sv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 279000
    num_examples: 524
  download_size: 95088
  dataset_size: 279000
- config_name: sw
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 286827
    num_examples: 523
  download_size: 97432
  dataset_size: 286827
- config_name: szl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 288392
    num_examples: 524
  download_size: 112648
  dataset_size: 288392
- config_name: szy
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 308513
    num_examples: 524
  download_size: 110994
  dataset_size: 308513
- config_name: ta
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 582388
    num_examples: 523
  download_size: 177509
  dataset_size: 582388
- config_name: tay
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 304097
    num_examples: 509
  download_size: 140209
  dataset_size: 304097
- config_name: tcy
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 500174
    num_examples: 524
  download_size: 157012
  dataset_size: 500174
- config_name: te
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 509480
    num_examples: 524
  download_size: 159871
  dataset_size: 509480
- config_name: tet
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292692
    num_examples: 524
  download_size: 97069
  dataset_size: 292692
- config_name: tg
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 403280
    num_examples: 524
  download_size: 138386
  dataset_size: 403280
- config_name: th
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 495072
    num_examples: 524
  download_size: 157178
  dataset_size: 495072
- config_name: ti
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 381355
    num_examples: 524
  download_size: 139560
  dataset_size: 381355
- config_name: tk
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 299395
    num_examples: 524
  download_size: 105687
  dataset_size: 299395
- config_name: tl
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 305745
    num_examples: 523
  download_size: 102792
  dataset_size: 305745
- config_name: tly
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 314401
    num_examples: 520
  download_size: 155495
  dataset_size: 314401
- config_name: tn
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 306914
    num_examples: 520
  download_size: 107571
  dataset_size: 306914
- config_name: to
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 332481
    num_examples: 524
  download_size: 113493
  dataset_size: 332481
- config_name: tpi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 306128
    num_examples: 524
  download_size: 97381
  dataset_size: 306128
- config_name: tr
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 291971
    num_examples: 523
  download_size: 101271
  dataset_size: 291971
- config_name: trv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 282684
    num_examples: 521
  download_size: 99996
  dataset_size: 282684
- config_name: ts
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 310560
    num_examples: 521
  download_size: 109597
  dataset_size: 310560
- config_name: tt
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 378547
    num_examples: 524
  download_size: 129979
  dataset_size: 378547
- config_name: tum
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 308828
    num_examples: 522
  download_size: 111786
  dataset_size: 308828
- config_name: tw
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 303928
    num_examples: 524
  download_size: 140580
  dataset_size: 303928
- config_name: ty
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 338964
    num_examples: 524
  download_size: 154841
  dataset_size: 338964
- config_name: tyv
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 405198
    num_examples: 524
  download_size: 178430
  dataset_size: 405198
- config_name: udm
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 378448
    num_examples: 524
  download_size: 135501
  dataset_size: 378448
- config_name: ug
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 414879
    num_examples: 524
  download_size: 144095
  dataset_size: 414879
- config_name: uk
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 342913
    num_examples: 476
  download_size: 157669
  dataset_size: 342913
- config_name: ur
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 384032
    num_examples: 524
  download_size: 132533
  dataset_size: 384032
- config_name: uz
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 294857
    num_examples: 524
  download_size: 101839
  dataset_size: 294857
- config_name: ve
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 313231
    num_examples: 524
  download_size: 112459
  dataset_size: 313231
- config_name: vec
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292371
    num_examples: 524
  download_size: 106919
  dataset_size: 292371
- config_name: vep
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 286847
    num_examples: 523
  download_size: 136564
  dataset_size: 286847
- config_name: vi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 339545
    num_examples: 524
  download_size: 113337
  dataset_size: 339545
- config_name: vls
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 286218
    num_examples: 524
  download_size: 105375
  dataset_size: 286218
- config_name: wa
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292833
    num_examples: 524
  download_size: 107211
  dataset_size: 292833
- config_name: war
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 307556
    num_examples: 521
  download_size: 104570
  dataset_size: 307556
- config_name: wo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 292312
    num_examples: 524
  download_size: 142364
  dataset_size: 292312
- config_name: wuu
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 277771
    num_examples: 524
  download_size: 107391
  dataset_size: 277771
- config_name: xal
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 365042
    num_examples: 524
  download_size: 135260
  dataset_size: 365042
- config_name: xh
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 294523
    num_examples: 507
  download_size: 139522
  dataset_size: 294523
- config_name: xmf
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 485454
    num_examples: 524
  download_size: 153229
  dataset_size: 485454
- config_name: yi
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 387421
    num_examples: 524
  download_size: 137104
  dataset_size: 387421
- config_name: yo
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 347802
    num_examples: 524
  download_size: 157278
  dataset_size: 347802
- config_name: yue
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 276515
    num_examples: 523
  download_size: 101524
  dataset_size: 276515
- config_name: za
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 283117
    num_examples: 500
  download_size: 105567
  dataset_size: 283117
- config_name: zea
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 286117
    num_examples: 524
  download_size: 102667
  dataset_size: 286117
- config_name: zu
  features:
  - name: prompt
    dtype: large_string
  - name: instruction_id_list
    list: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      list: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keywords
      list: string
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: options
      list: string
    - name: postscript_marker
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
    - name: language
      dtype: string
  - name: key
    dtype: int64
  splits:
  - name: test
    num_bytes: 300350
    num_examples: 524
  download_size: 105269
  dataset_size: 300350
configs:
- config_name: ab
  data_files:
  - split: test
    path: ab/*.parquet
- config_name: ace
  data_files:
  - split: test
    path: ace/*.parquet
- config_name: ady
  data_files:
  - split: test
    path: ady/*.parquet
- config_name: af
  data_files:
  - split: test
    path: af/*.parquet
- config_name: alt
  data_files:
  - split: test
    path: alt/*.parquet
- config_name: am
  data_files:
  - split: test
    path: am/*.parquet
- config_name: ami
  data_files:
  - split: test
    path: ami/*.parquet
- config_name: an
  data_files:
  - split: test
    path: an/*.parquet
- config_name: ang
  data_files:
  - split: test
    path: ang/*.parquet
- config_name: anp
  data_files:
  - split: test
    path: anp/*.parquet
- config_name: ar
  data_files:
  - split: test
    path: ar/*.parquet
- config_name: arc
  data_files:
  - split: test
    path: arc/*.parquet
- config_name: ary
  data_files:
  - split: test
    path: ary/*.parquet
- config_name: arz
  data_files:
  - split: test
    path: arz/*.parquet
- config_name: as
  data_files:
  - split: test
    path: as/*.parquet
- config_name: ast
  data_files:
  - split: test
    path: ast/*.parquet
- config_name: atj
  data_files:
  - split: test
    path: atj/*.parquet
- config_name: av
  data_files:
  - split: test
    path: av/*.parquet
- config_name: avk
  data_files:
  - split: test
    path: avk/*.parquet
- config_name: awa
  data_files:
  - split: test
    path: awa/*.parquet
- config_name: ay
  data_files:
  - split: test
    path: ay/*.parquet
- config_name: az
  data_files:
  - split: test
    path: az/*.parquet
- config_name: azb
  data_files:
  - split: test
    path: azb/*.parquet
- config_name: ba
  data_files:
  - split: test
    path: ba/*.parquet
- config_name: ban
  data_files:
  - split: test
    path: ban/*.parquet
- config_name: bar
  data_files:
  - split: test
    path: bar/*.parquet
- config_name: bcl
  data_files:
  - split: test
    path: bcl/*.parquet
- config_name: be
  data_files:
  - split: test
    path: be/test-*
- config_name: bg
  data_files:
  - split: test
    path: bg/test-*
- config_name: bi
  data_files:
  - split: test
    path: bi/*.parquet
- config_name: bjn
  data_files:
  - split: test
    path: bjn/test-*
- config_name: blk
  data_files:
  - split: test
    path: blk/*.parquet
- config_name: bm
  data_files:
  - split: test
    path: bm/*.parquet
- config_name: bn
  data_files:
  - split: test
    path: bn/*.parquet
- config_name: bo
  data_files:
  - split: test
    path: bo/*.parquet
- config_name: bpy
  data_files:
  - split: test
    path: bpy/*.parquet
- config_name: br
  data_files:
  - split: test
    path: br/*.parquet
- config_name: bs
  data_files:
  - split: test
    path: bs/test-*
- config_name: bug
  data_files:
  - split: test
    path: bug/test-*
- config_name: bxr
  data_files:
  - split: test
    path: bxr/*.parquet
- config_name: ca
  data_files:
  - split: test
    path: ca/test-*
- config_name: cdo
  data_files:
  - split: test
    path: cdo/*.parquet
- config_name: ce
  data_files:
  - split: test
    path: ce/*.parquet
- config_name: ceb
  data_files:
  - split: test
    path: ceb/*.parquet
- config_name: ch
  data_files:
  - split: test
    path: ch/*.parquet
- config_name: chr
  data_files:
  - split: test
    path: chr/*.parquet
- config_name: chy
  data_files:
  - split: test
    path: chy/*.parquet
- config_name: ckb
  data_files:
  - split: test
    path: ckb/*.parquet
- config_name: co
  data_files:
  - split: test
    path: co/*.parquet
- config_name: cr
  data_files:
  - split: test
    path: cr/*.parquet
- config_name: crh
  data_files:
  - split: test
    path: crh/*.parquet
- config_name: cs
  data_files:
  - split: test
    path: cs/test-*
- config_name: csb
  data_files:
  - split: test
    path: csb/test-*
- config_name: cu
  data_files:
  - split: test
    path: cu/*.parquet
- config_name: cv
  data_files:
  - split: test
    path: cv/test-*
- config_name: cy
  data_files:
  - split: test
    path: cy/test-*
- config_name: da
  data_files:
  - split: test
    path: da/test-*
- config_name: dag
  data_files:
  - split: test
    path: dag/*.parquet
- config_name: de
  data_files:
  - split: test
    path: de/test-*
- config_name: din
  data_files:
  - split: test
    path: din/*.parquet
- config_name: diq
  data_files:
  - split: test
    path: diq/*.parquet
- config_name: dsb
  data_files:
  - split: test
    path: dsb/test-*
- config_name: dty
  data_files:
  - split: test
    path: dty/*.parquet
- config_name: dv
  data_files:
  - split: test
    path: dv/*.parquet
- config_name: dz
  data_files:
  - split: test
    path: dz/test-*
- config_name: ee
  data_files:
  - split: test
    path: ee/*.parquet
- config_name: el
  data_files:
  - split: test
    path: el/test-*
- config_name: en
  data_files:
  - split: test
    path: en/test-*
- config_name: eo
  data_files:
  - split: test
    path: eo/*.parquet
- config_name: es
  data_files:
  - split: test
    path: es/test-*
- config_name: et
  data_files:
  - split: test
    path: et/test-*
- config_name: eu
  data_files:
  - split: test
    path: eu/test-*
- config_name: ext
  data_files:
  - split: test
    path: ext/test-*
- config_name: fa
  data_files:
  - split: test
    path: fa/*.parquet
- config_name: fat
  data_files:
  - split: test
    path: fat/*.parquet
- config_name: ff
  data_files:
  - split: test
    path: ff/*.parquet
- config_name: fi
  data_files:
  - split: test
    path: fi/test-*
- config_name: fj
  data_files:
  - split: test
    path: fj/*.parquet
- config_name: fo
  data_files:
  - split: test
    path: fo/test-*
- config_name: fon
  data_files:
  - split: test
    path: fon/*.parquet
- config_name: fr
  data_files:
  - split: test
    path: fr/test-*
- config_name: frp
  data_files:
  - split: test
    path: frp/*.parquet
- config_name: frr
  data_files:
  - split: test
    path: frr/*.parquet
- config_name: fur
  data_files:
  - split: test
    path: fur/*.parquet
- config_name: fy
  data_files:
  - split: test
    path: fy/test-*
- config_name: ga
  data_files:
  - split: test
    path: ga/*.parquet
- config_name: gag
  data_files:
  - split: test
    path: gag/*.parquet
- config_name: gan
  data_files:
  - split: test
    path: gan/*.parquet
- config_name: gcr
  data_files:
  - split: test
    path: gcr/*.parquet
- config_name: gd
  data_files:
  - split: test
    path: gd/*.parquet
- config_name: gl
  data_files:
  - split: test
    path: gl/*.parquet
- config_name: glk
  data_files:
  - split: test
    path: glk/*.parquet
- config_name: gn
  data_files:
  - split: test
    path: gn/*.parquet
- config_name: gom
  data_files:
  - split: test
    path: gom/test-*
- config_name: gor
  data_files:
  - split: test
    path: gor/test-*
- config_name: got
  data_files:
  - split: test
    path: got/test-*
- config_name: gpe
  data_files:
  - split: test
    path: gpe/*.parquet
- config_name: gu
  data_files:
  - split: test
    path: gu/*.parquet
- config_name: guc
  data_files:
  - split: test
    path: guc/*.parquet
- config_name: gur
  data_files:
  - split: test
    path: gur/*.parquet
- config_name: guw
  data_files:
  - split: test
    path: guw/*.parquet
- config_name: gv
  data_files:
  - split: test
    path: gv/*.parquet
- config_name: ha
  data_files:
  - split: test
    path: ha/*.parquet
- config_name: hak
  data_files:
  - split: test
    path: hak/*.parquet
- config_name: haw
  data_files:
  - split: test
    path: haw/*.parquet
- config_name: he
  data_files:
  - split: test
    path: he/*.parquet
- config_name: hi
  data_files:
  - split: test
    path: hi/*.parquet
- config_name: hif
  data_files:
  - split: test
    path: hif/*.parquet
- config_name: hr
  data_files:
  - split: test
    path: hr/test-*
- config_name: hsb
  data_files:
  - split: test
    path: hsb/*.parquet
- config_name: ht
  data_files:
  - split: test
    path: ht/*.parquet
- config_name: hu
  data_files:
  - split: test
    path: hu/test-*
- config_name: hy
  data_files:
  - split: test
    path: hy/*.parquet
- config_name: hyw
  data_files:
  - split: test
    path: hyw/*.parquet
- config_name: ia
  data_files:
  - split: test
    path: ia/*.parquet
- config_name: id
  data_files:
  - split: test
    path: id/*.parquet
- config_name: ie
  data_files:
  - split: test
    path: ie/*.parquet
- config_name: ig
  data_files:
  - split: test
    path: ig/test-*
- config_name: ik
  data_files:
  - split: test
    path: ik/*.parquet
- config_name: ilo
  data_files:
  - split: test
    path: ilo/*.parquet
- config_name: inh
  data_files:
  - split: test
    path: inh/*.parquet
- config_name: io
  data_files:
  - split: test
    path: io/*.parquet
- config_name: is
  data_files:
  - split: test
    path: is/test-*
- config_name: it
  data_files:
  - split: test
    path: it/test-*
- config_name: iu
  data_files:
  - split: test
    path: iu/*.parquet
- config_name: ja
  data_files:
  - split: test
    path: ja/*.parquet
- config_name: jam
  data_files:
  - split: test
    path: jam/test-*
- config_name: jbo
  data_files:
  - split: test
    path: jbo/test-*
- config_name: ka
  data_files:
  - split: test
    path: ka/*.parquet
- config_name: kaa
  data_files:
  - split: test
    path: kaa/*.parquet
- config_name: kab
  data_files:
  - split: test
    path: kab/*.parquet
- config_name: kbd
  data_files:
  - split: test
    path: kbd/*.parquet
- config_name: kbp
  data_files:
  - split: test
    path: kbp/*.parquet
- config_name: kcg
  data_files:
  - split: test
    path: kcg/*.parquet
- config_name: kg
  data_files:
  - split: test
    path: kg/*.parquet
- config_name: ki
  data_files:
  - split: test
    path: ki/*.parquet
- config_name: kk
  data_files:
  - split: test
    path: kk/*.parquet
- config_name: kl
  data_files:
  - split: test
    path: kl/*.parquet
- config_name: km
  data_files:
  - split: test
    path: km/*.parquet
- config_name: kn
  data_files:
  - split: test
    path: kn/*.parquet
- config_name: ko
  data_files:
  - split: test
    path: ko/*.parquet
- config_name: koi
  data_files:
  - split: test
    path: koi/test-*
- config_name: krc
  data_files:
  - split: test
    path: krc/*.parquet
- config_name: ks
  data_files:
  - split: test
    path: ks/*.parquet
- config_name: ku
  data_files:
  - split: test
    path: ku/*.parquet
- config_name: kv
  data_files:
  - split: test
    path: kv/*.parquet
- config_name: kw
  data_files:
  - split: test
    path: kw/*.parquet
- config_name: ky
  data_files:
  - split: test
    path: ky/*.parquet
- config_name: la
  data_files:
  - split: test
    path: la/*.parquet
- config_name: lad
  data_files:
  - split: test
    path: lad/*.parquet
- config_name: lb
  data_files:
  - split: test
    path: lb/*.parquet
- config_name: lbe
  data_files:
  - split: test
    path: lbe/*.parquet
- config_name: lez
  data_files:
  - split: test
    path: lez/*.parquet
- config_name: lfn
  data_files:
  - split: test
    path: lfn/test-*
- config_name: lg
  data_files:
  - split: test
    path: lg/test-*
- config_name: li
  data_files:
  - split: test
    path: li/test-*
- config_name: lij
  data_files:
  - split: test
    path: lij/*.parquet
- config_name: lld
  data_files:
  - split: test
    path: lld/*.parquet
- config_name: lmo
  data_files:
  - split: test
    path: lmo/*.parquet
- config_name: ln
  data_files:
  - split: test
    path: ln/*.parquet
- config_name: lo
  data_files:
  - split: test
    path: lo/*.parquet
- config_name: lt
  data_files:
  - split: test
    path: lt/test-*
- config_name: ltg
  data_files:
  - split: test
    path: ltg/test-*
- config_name: lv
  data_files:
  - split: test
    path: lv/test-*
- config_name: mad
  data_files:
  - split: test
    path: mad/*.parquet
- config_name: mai
  data_files:
  - split: test
    path: mai/*.parquet
- config_name: mdf
  data_files:
  - split: test
    path: mdf/*.parquet
- config_name: mg
  data_files:
  - split: test
    path: mg/test-*
- config_name: mhr
  data_files:
  - split: test
    path: mhr/*.parquet
- config_name: mi
  data_files:
  - split: test
    path: mi/*.parquet
- config_name: min
  data_files:
  - split: test
    path: min/*.parquet
- config_name: mk
  data_files:
  - split: test
    path: mk/*.parquet
- config_name: ml
  data_files:
  - split: test
    path: ml/test-*
- config_name: mn
  data_files:
  - split: test
    path: mn/*.parquet
- config_name: mni
  data_files:
  - split: test
    path: mni/*.parquet
- config_name: mnw
  data_files:
  - split: test
    path: mnw/*.parquet
- config_name: mr
  data_files:
  - split: test
    path: mr/*.parquet
- config_name: mrj
  data_files:
  - split: test
    path: mrj/*.parquet
- config_name: ms
  data_files:
  - split: test
    path: ms/*.parquet
- config_name: mt
  data_files:
  - split: test
    path: mt/*.parquet
- config_name: mwl
  data_files:
  - split: test
    path: mwl/*.parquet
- config_name: my
  data_files:
  - split: test
    path: my/*.parquet
- config_name: myv
  data_files:
  - split: test
    path: myv/*.parquet
- config_name: mzn
  data_files:
  - split: test
    path: mzn/*.parquet
- config_name: nap
  data_files:
  - split: test
    path: nap/*.parquet
- config_name: nds
  data_files:
  - split: test
    path: nds/test-*
- config_name: ne
  data_files:
  - split: test
    path: ne/*.parquet
- config_name: new
  data_files:
  - split: test
    path: new/*.parquet
- config_name: nia
  data_files:
  - split: test
    path: nia/*.parquet
- config_name: nl
  data_files:
  - split: test
    path: nl/*.parquet
- config_name: nn
  data_files:
  - split: test
    path: nn/test-*
- config_name: 'no'
  data_files:
  - split: test
    path: no/test-*
- config_name: nov
  data_files:
  - split: test
    path: nov/*.parquet
- config_name: nqo
  data_files:
  - split: test
    path: nqo/*.parquet
- config_name: nso
  data_files:
  - split: test
    path: nso/*.parquet
- config_name: nv
  data_files:
  - split: test
    path: nv/*.parquet
- config_name: ny
  data_files:
  - split: test
    path: ny/*.parquet
- config_name: oc
  data_files:
  - split: test
    path: oc/*.parquet
- config_name: olo
  data_files:
  - split: test
    path: olo/test-*
- config_name: om
  data_files:
  - split: test
    path: om/*.parquet
- config_name: or
  data_files:
  - split: test
    path: or/*.parquet
- config_name: os
  data_files:
  - split: test
    path: os/test-*
- config_name: pa
  data_files:
  - split: test
    path: pa/*.parquet
- config_name: pag
  data_files:
  - split: test
    path: pag/*.parquet
- config_name: pam
  data_files:
  - split: test
    path: pam/*.parquet
- config_name: pap
  data_files:
  - split: test
    path: pap/test-*
- config_name: pcd
  data_files:
  - split: test
    path: pcd/*.parquet
- config_name: pcm
  data_files:
  - split: test
    path: pcm/*.parquet
- config_name: pdc
  data_files:
  - split: test
    path: pdc/*.parquet
- config_name: pfl
  data_files:
  - split: test
    path: pfl/*.parquet
- config_name: pi
  data_files:
  - split: test
    path: pi/*.parquet
- config_name: pl
  data_files:
  - split: test
    path: pl/test-*
- config_name: pms
  data_files:
  - split: test
    path: pms/*.parquet
- config_name: pnb
  data_files:
  - split: test
    path: pnb/*.parquet
- config_name: pnt
  data_files:
  - split: test
    path: pnt/*.parquet
- config_name: ps
  data_files:
  - split: test
    path: ps/test-*
- config_name: pt-br
  data_files:
  - split: test
    path: pt-br/*.parquet
- config_name: pt-pt
  data_files:
  - split: test
    path: pt-pt/test-*
- config_name: pwn
  data_files:
  - split: test
    path: pwn/*.parquet
- config_name: qu
  data_files:
  - split: test
    path: qu/*.parquet
- config_name: rm
  data_files:
  - split: test
    path: rm/*.parquet
- config_name: rmy
  data_files:
  - split: test
    path: rmy/*.parquet
- config_name: rn
  data_files:
  - split: test
    path: rn/*.parquet
- config_name: ro
  data_files:
  - split: test
    path: ro/test-*
- config_name: ru
  data_files:
  - split: test
    path: ru/*.parquet
- config_name: rue
  data_files:
  - split: test
    path: rue/*.parquet
- config_name: rw
  data_files:
  - split: test
    path: rw/*.parquet
- config_name: sa
  data_files:
  - split: test
    path: sa/*.parquet
- config_name: sah
  data_files:
  - split: test
    path: sah/*.parquet
- config_name: sat
  data_files:
  - split: test
    path: sat/*.parquet
- config_name: sc
  data_files:
  - split: test
    path: sc/test-*
- config_name: scn
  data_files:
  - split: test
    path: scn/*.parquet
- config_name: sco
  data_files:
  - split: test
    path: sco/*.parquet
- config_name: sd
  data_files:
  - split: test
    path: sd/test-*
- config_name: se
  data_files:
  - split: test
    path: se/test-*
- config_name: sg
  data_files:
  - split: test
    path: sg/*.parquet
- config_name: shi
  data_files:
  - split: test
    path: shi/*.parquet
- config_name: shn
  data_files:
  - split: test
    path: shn/test-*
- config_name: si
  data_files:
  - split: test
    path: si/*.parquet
- config_name: sk
  data_files:
  - split: test
    path: sk/test-*
- config_name: skr
  data_files:
  - split: test
    path: skr/*.parquet
- config_name: sl
  data_files:
  - split: test
    path: sl/test-*
- config_name: sm
  data_files:
  - split: test
    path: sm/*.parquet
- config_name: smn
  data_files:
  - split: test
    path: smn/*.parquet
- config_name: sn
  data_files:
  - split: test
    path: sn/test-*
- config_name: so
  data_files:
  - split: test
    path: so/*.parquet
- config_name: sq
  data_files:
  - split: test
    path: sq/test-*
- config_name: sr
  data_files:
  - split: test
    path: sr/test-*
- config_name: srn
  data_files:
  - split: test
    path: srn/test-*
- config_name: ss
  data_files:
  - split: test
    path: ss/*.parquet
- config_name: st
  data_files:
  - split: test
    path: st/*.parquet
- config_name: stq
  data_files:
  - split: test
    path: stq/*.parquet
- config_name: su
  data_files:
  - split: test
    path: su/*.parquet
- config_name: sv
  data_files:
  - split: test
    path: sv/*.parquet
- config_name: sw
  data_files:
  - split: test
    path: sw/*.parquet
- config_name: szl
  data_files:
  - split: test
    path: szl/*.parquet
- config_name: szy
  data_files:
  - split: test
    path: szy/*.parquet
- config_name: ta
  data_files:
  - split: test
    path: ta/*.parquet
- config_name: tay
  data_files:
  - split: test
    path: tay/test-*
- config_name: tcy
  data_files:
  - split: test
    path: tcy/*.parquet
- config_name: te
  data_files:
  - split: test
    path: te/*.parquet
- config_name: tet
  data_files:
  - split: test
    path: tet/*.parquet
- config_name: tg
  data_files:
  - split: test
    path: tg/*.parquet
- config_name: th
  data_files:
  - split: test
    path: th/*.parquet
- config_name: ti
  data_files:
  - split: test
    path: ti/*.parquet
- config_name: tk
  data_files:
  - split: test
    path: tk/*.parquet
- config_name: tl
  data_files:
  - split: test
    path: tl/*.parquet
- config_name: tly
  data_files:
  - split: test
    path: tly/test-*
- config_name: tn
  data_files:
  - split: test
    path: tn/*.parquet
- config_name: to
  data_files:
  - split: test
    path: to/*.parquet
- config_name: tpi
  data_files:
  - split: test
    path: tpi/*.parquet
- config_name: tr
  data_files:
  - split: test
    path: tr/*.parquet
- config_name: trv
  data_files:
  - split: test
    path: trv/*.parquet
- config_name: ts
  data_files:
  - split: test
    path: ts/*.parquet
- config_name: tt
  data_files:
  - split: test
    path: tt/*.parquet
- config_name: tum
  data_files:
  - split: test
    path: tum/*.parquet
- config_name: tw
  data_files:
  - split: test
    path: tw/test-*
- config_name: ty
  data_files:
  - split: test
    path: ty/test-*
- config_name: tyv
  data_files:
  - split: test
    path: tyv/test-*
- config_name: udm
  data_files:
  - split: test
    path: udm/*.parquet
- config_name: ug
  data_files:
  - split: test
    path: ug/*.parquet
- config_name: uk
  data_files:
  - split: test
    path: uk/test-*
- config_name: ur
  data_files:
  - split: test
    path: ur/*.parquet
- config_name: uz
  data_files:
  - split: test
    path: uz/*.parquet
- config_name: ve
  data_files:
  - split: test
    path: ve/*.parquet
- config_name: vec
  data_files:
  - split: test
    path: vec/*.parquet
- config_name: vep
  data_files:
  - split: test
    path: vep/test-*
- config_name: vi
  data_files:
  - split: test
    path: vi/*.parquet
- config_name: vls
  data_files:
  - split: test
    path: vls/*.parquet
- config_name: vo
  data_files:
  - split: test
    path: vo/*.parquet
- config_name: wa
  data_files:
  - split: test
    path: wa/*.parquet
- config_name: war
  data_files:
  - split: test
    path: war/*.parquet
- config_name: wo
  data_files:
  - split: test
    path: wo/test-*
- config_name: wuu
  data_files:
  - split: test
    path: wuu/*.parquet
- config_name: xal
  data_files:
  - split: test
    path: xal/*.parquet
- config_name: xh
  data_files:
  - split: test
    path: xh/test-*
- config_name: xmf
  data_files:
  - split: test
    path: xmf/*.parquet
- config_name: yi
  data_files:
  - split: test
    path: yi/*.parquet
- config_name: yo
  data_files:
  - split: test
    path: yo/test-*
- config_name: yue
  data_files:
  - split: test
    path: yue/*.parquet
- config_name: za
  data_files:
  - split: test
    path: za/*.parquet
- config_name: zea
  data_files:
  - split: test
    path: zea/*.parquet
- config_name: zh-cn
  data_files:
  - split: test
    path: zh-cn/*.parquet
- config_name: zh-tw
  data_files:
  - split: test
    path: zh-tw/*.parquet
- config_name: zu
  data_files:
  - split: test
    path: zu/*.parquet
---

# MultiIFEval

This dataset is an instruction-following dataset for 300+ languages, translated and localised from the [English IFEval dataset](https://doi.org/10.48550/arXiv.2311.07911).

## Dataset Details

### Dataset Description

All samples come from the [English IFEval dataset](https://doi.org/10.48550/arXiv.2311.07911), and we translate and localise with [Gemini-3-flash-preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview).

When translating and localising samples, we also include a random Wikipedia article in the target language, both to give some context for localisation, but also to increase the translation quality.

- **Created by:** Dan Saattrup Smart (dan.smart@alexandra.dk) from the [Alexandra Institute](https://alexandra.dk/).
- **Funded by:** The EU Horizon project [TrustLLM](https://trustllm.eu/) (grant agreement number 101135671) and the LLM generations were part of the [Google Cloud Research Credits Programme](https://edu.google.com/intl/ALL_us/programs/credits/research/).
- **License:** CC BY-NC-SA 4.0

### Dataset Sources

- **Repository:** [github.com/alexandrainst/multi_ifeval](https://github.com/alexandrainst/multi_ifeval)

## Uses

This dataset is designed to be used for evaluating models on the instruction-following task.

## Dataset Structure

The dataset contains the following features, which is the standard [IFEval](https://huggingface.co/datasets/google/IFEval) format:

- **key** (str): The ID of the sample.
- **prompt** (str): The prompt containing all the instructions that is to be followed.
- **instruction_id_list** (list of str): The IDs of the instructions that should be followed.
- **kwargs** (list of dict): The keyword arguments belonging to each instruction-checking function in `instruction_id_list` (so this has the same length as `instruction_id_list`). Most arguments are `null` - these can be ignored.

There's only a single split, the `test` split, which is intended to be for evaluation purposes.

## Citation

If you use MultiIFEval in your research, please cite our paper:

```bibtex
@article{smart2026multiifeval,
  title={MultiIFEval: An Instruction Following Benchmark in 300+ Languages},
  author={Smart, Dan Saattrup},
  journal={arXiv preprint arXiv:XXXX.XXXXX},
  url={https://arxiv.org/abs/XXXX.XXXXX},
  year={2026}
}
```