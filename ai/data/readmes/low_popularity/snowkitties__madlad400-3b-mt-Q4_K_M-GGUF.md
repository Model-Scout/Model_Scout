---
license: apache-2.0
language:
- multilingual
- en
- ru
- es
- fr
- de
- it
- pt
- pl
- nl
- vi
- tr
- sv
- id
- ro
- cs
- zh
- hu
- ja
- th
- fi
- fa
- uk
- da
- el
- 'no'
- bg
- sk
- ko
- ar
- lt
- ca
- sl
- he
- et
- lv
- hi
- sq
- ms
- az
- sr
- ta
- hr
- kk
- is
- ml
- mr
- te
- af
- gl
- fil
- be
- mk
- eu
- bn
- ka
- mn
- bs
- uz
- ur
- sw
- yue
- ne
- kn
- kaa
- gu
- si
- cy
- eo
- la
- hy
- ky
- tg
- ga
- mt
- my
- km
- tt
- so
- ku
- ps
- pa
- rw
- lo
- ha
- dv
- fy
- lb
- ckb
- mg
- gd
- am
- ug
- ht
- grc
- hmn
- sd
- jv
- mi
- tk
- ceb
- yi
- ba
- fo
- or
- xh
- su
- kl
- ny
- sm
- sn
- co
- zu
- ig
- yo
- pap
- st
- haw
- as
- oc
- cv
- lus
- tet
- gsw
- sah
- br
- rm
- sa
- bo
- om
- se
- ce
- cnh
- ilo
- hil
- udm
- os
- lg
- ti
- vec
- ts
- tyv
- kbd
- ee
- iba
- av
- kha
- to
- tn
- nso
- fj
- zza
- ak
- ada
- otq
- dz
- bua
- cfm
- ln
- chm
- gn
- krc
- wa
- hif
- yua
- srn
- war
- rom
- bik
- pam
- sg
- lu
- ady
- kbp
- syr
- ltg
- myv
- iso
- kac
- bho
- ay
- kum
- qu
- za
- pag
- ngu
- ve
- pck
- zap
- tyz
- hui
- bbc
- tzo
- tiv
- ksd
- gom
- min
- ang
- nhe
- bgp
- nzi
- nnb
- nv
- zxx
- bci
- kv
- new
- mps
- alt
- meu
- bew
- fon
- iu
- abt
- mgh
- mnw
- tvl
- dov
- tlh
- ho
- kw
- mrj
- meo
- crh
- mbt
- emp
- ace
- ium
- mam
- gym
- mai
- crs
- pon
- ubu
- fip
- quc
- gv
- kj
- btx
- ape
- chk
- rcf
- shn
- tzh
- mdf
- ppk
- ss
- gag
- cab
- kri
- seh
- ibb
- tbz
- bru
- enq
- ach
- cuk
- kmb
- wo
- kek
- qub
- tab
- bts
- kos
- rwo
- cak
- tuc
- bum
- cjk
- gil
- stq
- tsg
- quh
- mak
- arn
- ban
- jiv
- sja
- yap
- tcy
- toj
- twu
- xal
- amu
- rmc
- hus
- nia
- kjh
- bm
- guh
- mas
- acf
- dtp
- ksw
- bzj
- din
- zne
- mad
- msi
- mag
- mkn
- kg
- lhu
- ch
- qvi
- mh
- djk
- sus
- mfe
- srm
- dyu
- ctu
- gui
- pau
- inb
- bi
- mni
- guc
- jam
- wal
- jac
- bas
- gor
- skr
- nyu
- noa
- sda
- gub
- nog
- cni
- teo
- tdx
- sxn
- rki
- nr
- frp
- alz
- taj
- lrc
- cce
- rn
- jvn
- hvn
- nij
- dwr
- izz
- msm
- bus
- ktu
- chr
- maz
- tzj
- suz
- knj
- bim
- gvl
- bqc
- tca
- pis
- prk
- laj
- mel
- qxr
- niq
- ahk
- shp
- hne
- spp
- koi
- krj
- quf
- luz
- agr
- tsc
- mqy
- gof
- gbm
- miq
- dje
- awa
- bjj
- qvz
- sjp
- tll
- raj
- kjg
- bgz
- quy
- cbk
- akb
- oj
- ify
- mey
- ks
- cac
- brx
- qup
- syl
- jax
- ff
- ber
- tks
- trp
- mrw
- adh
- smt
- srr
- ffm
- qvc
- mtr
- ann
- kaa
- aa
- noe
- nut
- gyn
- kwi
- xmm
- msb
library_name: transformers
tags:
- text2text-generation
- text-generation-inference
- llama-cpp
- gguf-my-repo
datasets:
- allenai/MADLAD-400
pipeline_tag: translation
widget:
- text: <2en> Como vai, amigo?
  example_title: Translation to English
- text: <2de> Do you speak German?
  example_title: Translation to German
base_model: google/madlad400-3b-mt
---

# snowkitties/madlad400-3b-mt-Q4_K_M-GGUF
This model was converted to GGUF format from [`google/madlad400-3b-mt`](https://huggingface.co/google/madlad400-3b-mt) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/google/madlad400-3b-mt) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo snowkitties/madlad400-3b-mt-Q4_K_M-GGUF --hf-file madlad400-3b-mt-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo snowkitties/madlad400-3b-mt-Q4_K_M-GGUF --hf-file madlad400-3b-mt-q4_k_m.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

Step 1: Clone llama.cpp from GitHub.
```
git clone https://github.com/ggerganov/llama.cpp
```

Step 2: Move into the llama.cpp folder and build it with `LLAMA_CURL=1` flag along with other hardware-specific flags (for ex: LLAMA_CUDA=1 for Nvidia GPUs on Linux).
```
cd llama.cpp && LLAMA_CURL=1 make
```

Step 3: Run inference through the main binary.
```
./llama-cli --hf-repo snowkitties/madlad400-3b-mt-Q4_K_M-GGUF --hf-file madlad400-3b-mt-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo snowkitties/madlad400-3b-mt-Q4_K_M-GGUF --hf-file madlad400-3b-mt-q4_k_m.gguf -c 2048
```
