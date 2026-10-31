---
license: apache-2.0
language:
- ko
---
# CharacterRAG dataset



![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/673c0092a3892e8156aa8312/P3mhELmc05imGtfedn7Bq.jpeg)


## Overview
CharacterRAG is a high-quality dataset for RAG-based role-playing agents, which consists of persona documents for 15 distinct fictional characters totaling 976K written characters, and 450 question–answer pairs.

All external information about works featuring characters that could affect persona consistency has been manually removed by human annotators (e.g., character popularity poll).


## Dataset Structure

```

├── anya_forger
    ├── anya_forger.txt # persona document
    └── anya_forger.xlsx # QA pairs
├── chika_fujiwara
    ├── chika_fujiwara.txt
    └── chika_fujiwara.xlsx
├── edward_elric
    ├── edward_elric.txt
    └── edward_elric.xlsx
├── frieren
    ├── frieren.txt
    └── frieren.xlsx
├── hitori_gotoh
    ├── hitori_gotoh.txt
    └── hitori_gotoh.xlsx
├── light_yagami
    ├── light_yagami.txt
    └── light_yagami.xlsx
├── maomao
    ├── maomao.txt
    └── maomao.xlsx
├── megumin
    ├── megumin.txt
    └── megumin.xlsx
├── mikoto_misaka
    ├── mikoto_misaka.txt
    └── mikoto_misaka.xlsx
├── nina_iseri
    ├── nina_iseri.txt
    └── nina_iseri.xlsx
├── saitama
    ├── saitama.txt
    └── saitama.xlsx
├── son_goku
    ├── son_goku.txt
    └── son_goku.xlsx
├── tanjiro_kamado
    ├── tanjiro_kamado.txt
    └── tanjiro_kamado.xlsx
├── tobio_kageyama
    ├── tobio_kageyama.txt
    └── tobio_kageyama.xlsx
└── yui_hirasawa
    ├── yui_hirasawa.txt
    └── yui_hirasawa.xlsx
```



## Citation Information

```
@misc{park2025dynamiccontextadaptationconsistent,
      title={Dynamic Context Adaptation for Consistent Role-Playing Agents with Retrieval-Augmented Generations}, 
      author={Jeiyoon Park and Yongshin Han and Minseop Kim and Kisu Yang},
      year={2025},
      eprint={2508.02016},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2508.02016}, 
}
```