---
dataset_info:
  features:
  - name: Text
    dtype: string
  - name: Cluster
    dtype: int32
  - name: Polarity
    dtype: float64
  - name: count_word
    dtype: int64
  splits:
  - name: Cluster_1
    num_bytes: 11487341
    num_examples: 4797
  - name: Cluster_2
    num_bytes: 8423711
    num_examples: 4025
  - name: Cluster_3
    num_bytes: 16002250
    num_examples: 5026
  download_size: 18951480
  dataset_size: 35913302
configs:
- config_name: default
  data_files:
  - split: Cluster_1
    path: data/Cluster_1-*
  - split: Cluster_2
    path: data/Cluster_2-*
  - split: Cluster_3
    path: data/Cluster_3-*
language:
  - en
  - es
  - ru
  - zh
  - de
  - fr
  - th
  - ca
  - it
  - ja
  - pl
  - eo
  - eu
  - vi
  - fi
  - hu
  - ar
  - nl
  - da
  - tr
  - ko
  - he
  - id
  - cs
  - bn
  - sv
---


- max count_word cluster_1: 1722
- min count_word cluster_1: 11
- max count_word cluster_2: 2624
- min count_word cluster_2: 21
- max count_word cluster_3: 2370
- min count_word cluster_3: 31

```Python
DatasetDict({
    Cluster_1: Dataset({
        features: ['Text', 'Cluster', 'Polarity', 'count_word'],
        num_rows: 4797
    })
    Cluster_2: Dataset({
        features: ['Text', 'Cluster', 'Polarity', 'count_word'],
        num_rows: 4025
    })
    Cluster_3: Dataset({
        features: ['Text', 'Cluster', 'Polarity', 'count_word'],
        num_rows: 5026
    })
})
```

![image/png](https://cdn-uploads.huggingface.co/production/uploads/641b435ba5f876fe30c5ae0a/Ttmlj2f0dGArlmxDfcQMq.png)


![image/png](https://cdn-uploads.huggingface.co/production/uploads/641b435ba5f876fe30c5ae0a/rvDdQ10Ike-niaNBTV6Mp.png)

