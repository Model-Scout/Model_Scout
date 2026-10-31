---
dataset_info:
- config_name: ar
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 659105981
    num_examples: 499568
  - name: test
    num_bytes: 9015516
    num_examples: 4387
  - name: validation
    num_bytes: 7406509
    num_examples: 3783
  download_size: 3651950669
  dataset_size: 675528006
- config_name: ca
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 406179567
    num_examples: 294856
  - name: test
    num_bytes: 5378789
    num_examples: 2541
  - name: validation
    num_bytes: 3136722
    num_examples: 1532
  download_size: 1513026644
  dataset_size: 414695078
- config_name: de
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 1288274676
    num_examples: 1049967
  - name: test
    num_bytes: 10773087
    num_examples: 5649
  - name: validation
    num_bytes: 8955886
    num_examples: 4994
  download_size: 4521091910
  dataset_size: 1308003649
- config_name: el
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 133497910
    num_examples: 64221
  - name: test
    num_bytes: 2364826
    num_examples: 861
  - name: validation
    num_bytes: 1836092
    num_examples: 668
  download_size: 579372781
  dataset_size: 137698828
- config_name: en
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 3555107736
    num_examples: 2701389
  - name: test
    num_bytes: 13160183
    num_examples: 6685
  - name: validation
    num_bytes: 27692074
    num_examples: 13236
  download_size: 11914987368
  dataset_size: 3595959993
- config_name: es
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 888914515
    num_examples: 702785
  - name: test
    num_bytes: 16076382
    num_examples: 8561
  - name: validation
    num_bytes: 4621760
    num_examples: 2177
  download_size: 3570403740
  dataset_size: 909612657
- config_name: fr
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 768697146
    num_examples: 870448
  - name: test
    num_bytes: 5937745
    num_examples: 3883
  - name: validation
    num_bytes: 3233262
    num_examples: 2079
  download_size: 3269522484
  dataset_size: 777868153
- config_name: hi
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 96926984
    num_examples: 51900
  - name: test
    num_bytes: 1340091
    num_examples: 374
  - name: validation
    num_bytes: 1222098
    num_examples: 405
  download_size: 385810623
  dataset_size: 99489173
- config_name: it
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 436879977
    num_examples: 432076
  - name: test
    num_bytes: 3798221
    num_examples: 2175
  - name: validation
    num_bytes: 2230995
    num_examples: 1276
  download_size: 1685172398
  dataset_size: 442909193
- config_name: ja
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 708617436
    num_examples: 480785
  - name: test
    num_bytes: 7802066
    num_examples: 3392
  - name: validation
    num_bytes: 6990637
    num_examples: 3106
  download_size: 3186065351
  dataset_size: 723410139
- config_name: ko
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 266381416
    num_examples: 213659
  - name: test
    num_bytes: 1736809
    num_examples: 803
  - name: validation
    num_bytes: 1857229
    num_examples: 917
  download_size: 1119778167
  dataset_size: 269975454
- config_name: nl
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 695855128
    num_examples: 648029
  - name: test
    num_bytes: 5186584
    num_examples: 2715
  - name: validation
    num_bytes: 4188877
    num_examples: 2188
  download_size: 2591997126
  dataset_size: 705230589
- config_name: pl
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 877441685
    num_examples: 675688
  - name: test
    num_bytes: 11475559
    num_examples: 6376
  - name: validation
    num_bytes: 6618989
    num_examples: 3476
  download_size: 3365852789
  dataset_size: 895536233
- config_name: pt
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 584986936
    num_examples: 469347
  - name: test
    num_bytes: 8678707
    num_examples: 4313
  - name: validation
    num_bytes: 5807293
    num_examples: 2973
  download_size: 2347987926
  dataset_size: 599472936
- config_name: ru
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 604993210
    num_examples: 339697
  - name: test
    num_bytes: 5941158
    num_examples: 2296
  - name: validation
    num_bytes: 5352859
    num_examples: 2107
  download_size: 2754576893
  dataset_size: 616287227
- config_name: sv
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 1822863623
    num_examples: 1742082
  - name: test
    num_bytes: 13002356
    num_examples: 7531
  - name: validation
    num_bytes: 5136097
    num_examples: 2987
  download_size: 6790489020
  dataset_size: 1841002076
- config_name: vi
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 300641174
    num_examples: 260010
  - name: test
    num_bytes: 4304795
    num_examples: 1824
  - name: validation
    num_bytes: 3402120
    num_examples: 1461
  download_size: 1301938106
  dataset_size: 308348089
- config_name: zh
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 449085696
    num_examples: 369249
  - name: test
    num_bytes: 5260974
    num_examples: 2667
  - name: validation
    num_bytes: 3511103
    num_examples: 1816
  download_size: 2440525684
  dataset_size: 457857773
- config_name: all_languages
  features:
  - name: docid
    dtype: string
  - name: title
    dtype: string
  - name: uri
    dtype: string
  - name: lan
    dtype: string
  - name: text
    dtype: string
  - name: entities
    list:
    - name: uri
      dtype: string
    - name: surfaceform
      dtype: string
    - name: type
      dtype: string
    - name: start
      dtype: int32
    - name: end
      dtype: int32
  - name: relations
    list:
    - name: subject
      dtype: int32
    - name: predicate
      dtype: string
    - name: object
      dtype: int32
  splits:
  - name: train
    num_bytes: 14615645332
    num_examples: 11865756
  - name: test
    num_bytes: 131636046
    num_examples: 67033
  - name: validation
    num_bytes: 103507688
    num_examples: 51181
  download_size: 56989165879
  dataset_size: 14850789066
task_categories:
- token-classification
language:
- ar
- ca
- de
- el
- en
- es
- fr
- hi
- it
- ja
- ko
- nl
- pl
- pt
- ru
- sv
- vi
- zh
size_categories:
- 10M<n<100M
license: cc-by-sa-4.0
---
# RED<sup>FM</sup>: a Filtered and Multilingual Relation Extraction Dataset

This is the automatically-filtered dataset from the 2023 ACL paper [RED^{FM}: a Filtered and Multilingual Relation Extraction Dataset](https://arxiv.org/abs/2306.09802). If you use the model, please reference this work in your paper:

    @inproceedings{huguet-cabot-et-al-2023-redfm-dataset,
        title = "RED$^{\rm FM}$: a Filtered and Multilingual Relation Extraction Dataset",
        author = "Huguet Cabot, Pere-Llu{\'\i}s  and Tedeschi, Simone and Ngonga Ngomo, Axel-Cyrille and
          Navigli, Roberto",
        booktitle = "Proc. of the 61st Annual Meeting of the Association for Computational Linguistics: ACL 2023",
        month = jul,
        year = "2023",
        address = "Toronto, Canada",
        publisher = "Association for Computational Linguistics",
        url = "https://arxiv.org/abs/2306.09802",
    }


## License

SRED<sup>FM</sup> is licensed under the CC BY-SA 4.0 license. The text of the license can be found [here](https://creativecommons.org/licenses/by-sa/4.0/).