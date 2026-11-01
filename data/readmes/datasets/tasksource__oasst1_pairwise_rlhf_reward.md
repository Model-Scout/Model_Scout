---
dataset_info:
  features:
  - name: lang
    dtype: string
  - name: parent_id
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 40736437
    num_examples: 17966
  - name: validation
    num_bytes: 2152443
    num_examples: 952
  download_size: 22371458
  dataset_size: 42888880
language:
- en
- es
- ru
- de
- pl
- th
- vi
- sv
- bn
- da
- he
- it
- fa
- sk
- id
- nb
- el
- nl
- hu
- eu
- zh
- eo
- ja
- ca
- cs
- bg
- fi
- pt
- tr
- ro
- ar
- uk
- gl
- fr
- ko
---
# Dataset Card for "oasst1_pairwise_rlhf_reward"


[OASST1 dataset](https://huggingface.co/datasets/OpenAssistant/oasst1) preprocessed for reward modeling:


```python
import pandas as pd
from datasets import load_dataset,concatenate_datasets, Dataset, DatasetDict
import numpy as np

dataset = load_dataset("OpenAssistant/oasst1")

df=concatenate_datasets(list(dataset.values())).to_pandas()
m2t=df.set_index("message_id")['text'].to_dict()
m2r=df.set_index("message_id")['role'].to_dict()
m2p=df.set_index('message_id')['parent_id'].to_dict()

m2history=dict() # message id to unrolled history
for k,v in m2p.items():
    history=[k]
    while history[-1] in m2p:
        history+=[m2p[history[-1]]]
    m2history[k]="\n".join([f"{m2r[m]}: {m2t[m]}" for m in history[::-1] if m])
        
d=dict()
for split in "train","validation":
    df=dataset[split].to_pandas()   
    df['prompt']=df.parent_id.map(lambda x: m2history.get(x,''))
    df=df[~df['rank'].isna()]
    
    def agg(x):
        x=list(x)
        return [x[0],x[-1]]
    df=df.groupby(['prompt',"parent_id",'lang'])[['text','rank']].agg(agg).reset_index()
    df=df[df['rank'].map(lambda x:len(set(x))>1)]
    df['chosen']   = df.apply(lambda x:x['text'][np.argmin(x['rank'])],axis=1)
    df['rejected'] = df.apply(lambda x:x['text'][np.argmax(x['rank'])],axis=1)
    d[split]=Dataset.from_pandas(df[['lang','parent_id','prompt','chosen','rejected']],preserve_index=False)

DatasetDict(d).push_to_hub('tasksource/oasst1_pairwise_rlhf_reward')
```