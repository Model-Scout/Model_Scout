---
license: mit
configs:
  - config_name: af
    data_files:
      - split: train
        path: af/*.txt

  - config_name: am
    data_files:
      - split: train
        path: am/*.txt

  - config_name: ar
    data_files:
      - split: train
        path: ar/*.txt

  - config_name: az
    data_files:
      - split: train
        path: az/*.txt

  - config_name: ca
    data_files:
      - split: train
        path: ca/*.txt

  - config_name: cy
    data_files:
      - split: train
        path: cy/*.txt
  - config_name: da
    data_files:
      - split: train
        path: da/*.txt
  - config_name: de
    data_files:
      - split: train
        path: de/*.txt

  - config_name: en
    data_files:
      - split: train
        path: en/*.txt
  - config_name: et
    data_files:
      - split: train
        path: et/*.txt
  - config_name: eu
    data_files:
      - split: train
        path: eu/*.txt
  - config_name: es
    data_files:
      - split: train
        path: es/*.txt

  - config_name: fa
    data_files:
      - split: train
        path: fa/*.txt

  - config_name: fr
    data_files:
      - split: train
        path: fr/*.txt

  - config_name: hr
    data_files:
      - split: train
        path: hi/*.txt
  - config_name: hi
    data_files:
      - split: train
        path: hi/*.txt

  - config_name: hu
    data_files:
      - split: train
        path: hu/*.txt
  - config_name: is
    data_files:
      - split: train
        path: is/*.txt
  - config_name: it
    data_files:
      - split: train
        path: it/*.txt
  - config_name: ko
    data_files:
      - split: train
        path: mr/*.txt
  - config_name: mr
    data_files:
      - split: train
        path: mr/*.txt

  - config_name: pl
    data_files:
      - split: train
        path: pl/*.txt
  - config_name: te
    data_files:
      - split: train
        path: te/*.txt

  - config_name: nl
    data_files:
      - split: train
        path: nl/*.txt
  - config_name: pt
    data_files:
      - split: train
        path: pt/*.txt

  - config_name: ru
    data_files:
      - split: train
        path: ru/*.txt

  - config_name: sv
    data_files:
      - split: train
        path: sv/*.txt

  - config_name: ta
    data_files:
      - split: train
        path: ta/*.txt

  - config_name: th
    data_files:
      - split: train
        path: th/*.txt

  - config_name: tr
    data_files:
      - split: train
        path: tr/*.txt

  - config_name: ug
    data_files:
      - split: train
        path: ug/*.txt

  - config_name: uk
    data_files:
      - split: train
        path: uk/*.txt

  - config_name: ur
    data_files:
      - split: train
        path: ur/*.txt

  - config_name: vi
    data_files:
      - split: train
        path: vi/*.txt

  - config_name: yue
    data_files:
      - split: train
        path: yue/*.txt

  - config_name: zh
    data_files:
      - split: train
        path: zh/*.txt

language:
- af
- am
- ar
- az
- ca
- cy
- da
- de
- en
- es
- et
- eu
- fa
- fr
- hi
- hr
- hu
- is
- it
- ko
- mr
- nl
- pl
- pt
- ru
- sv
- ta
- te
- th
- tr
- ug
- uk
- ur
- vi
- yue
- zh
---

# Phoneme-UD: A Multilingual Phonemized Universal Dependencies Corpus for 34+ Languages




## G2P+ Phonemizer

We use G2P+ to phonemize Universal Dependencies. Here is an example usage: 


```
# Install required packages
!apt-get install -y espeak-ng
!pip install phonemizer g2p-plus
# Set the environment variable from Python
import os
os.environ["PHONEMIZER_ESPEAK_LIBRARY"] = "/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1"

# Now run your transcription
from g2p_plus import transcribe_utterances

lines = ['hello there!', 'nice to meet you.']
phonemized = transcribe_utterances(lines, "phonemizer", "en-gb", keep_word_boundaries=True)
print(phonemized)
```



```
@misc{goriely2025ipachildesg2pfeaturerich,
      title={IPA-CHILDES & G2P+: Feature-Rich Resources for Cross-Lingual Phonology and Phonemic Language Modeling}, 
      author={Zébulon Goriely and Paula Buttery},
      year={2025},
      eprint={2504.03036},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2504.03036}, 
}
```


## Attribution

G2P+ incorporates content from the following sources:

<!-- - **Phoible** by **Moran, Steven & McCloy, Daniel**, licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).  
  Original work: [https://phoible.org/](https://phoible.org/)  -->
- **Pingyam** by **Open Dictionary**, licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).  
  Original work: [https://github.com/kfcd/pingyam/tree/master](https://github.com/kfcd/pingyam/tree/master) 
- **CEDICT** by **MDBG**, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).  
  Original work: [https://www.mdbg.net/chinese/dictionary?page=cc-cedict](https://www.mdbg.net/chinese/dictionary?page=cc-cedict) 

In accordance with the **CC BY-SA 3.0** license, any derivative work or adaptation of these resources must also be shared under the same license.

