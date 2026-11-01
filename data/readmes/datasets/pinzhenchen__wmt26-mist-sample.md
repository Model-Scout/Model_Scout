---
license: unknown
task_categories:
- question-answering
- summarization
language:
- ru
- ku
- en
- te
- ht
- ja
- es
- fi
- zh
- fa
- fr
- hi
- yo
- th
- vi
- tr
- cs
- id
- ko
- de
- pt
- mr
- it
- sw
- sk
- bn
- ar
---

# Update Log

- 22 June 2026 (**latest**) - we updated our data mix because some BELEBELE samples did not have the context. If you downloaded data before 22 June, please download the new version.
- 16 June 2026 - first version

# Summary
The `wmt26-mist-sample` is a multilingual mix provided by the **WMT26 MIST shared task** organizers as a starting point for fine-tuning multilingual LLMs. It contains three types of tasks, to cover same-language and cross-lingual comprehension and generation: **context-based QA, open-ended QA, and (mono- and cross-lingual) summarization**. You are also welcome to construct your own training data.

For more information regarding the shared task, such as timeline, system constraints, languages, and tasks, please visit the [shared task homepage](https://www2.statmt.org/wmt26/multilingual-instruction.html).

# Fields:
- `task`: the task, either `qa` or `sum`.
- `lang_code`: language code of the output in the format of `lang_Script`
- `source`: the origin of the instance
- `input`: the input. Note that the input is self-contained, which includes the task prompt, context, etc.
- `output`: the expected output

# Usage
This dataset is intended to be seed data to get started. You can split it however you like into train, dev, etc.

To load this dataset, you need the `datasets` library (`pip install datasets --upgrade`) and then run the following code:

```python
from datasets import load_dataset

# Load the annotations dataset
mist26_sample_data = load_dataset("pinzhenchen/wmt26-mist-sample")
```

# Data Breakdown and Stats
The table below details the number of samples per dataset and language. For the cross-lingual CrossSum, the data is organized by the output language. For any output language, the source texts were sampled from the other languages.

<div style="font-size: 12px;">
<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">Question Answering</th>
      <th colspan="3">Summarization</th>
    </tr>
    <tr>
      <th></th>
      <th>MCIF-QA</th>
      <th>TyDi QA</th>
      <th>Aya Dataset</th>
      <th>BELEBELE</th>
      <th>WMT25-MIST-OEG</th>
      <th>CrossSum</th>
      <th>MCIF-Sum</th>
      <th>Wikilingua</th>
    </tr>
  </thead>
    <tbody>
    <tr>
      <td>arb_Arab</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
      <td>46</td>
      <td>374</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>ben_Beng</td>
      <td>-</td>
      <td>112</td>
      <td>-</td>
      <td>-</td>
      <td>46</td>
      <td>347</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>ces_Latn</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>46</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>ckb_Arab</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>deu_Latn</td>
      <td>220</td>
      <td>-</td>
      <td>241</td>
      <td>300</td>
      <td>46</td>
      <td>-</td>
      <td>100</td>
      <td>100</td>
    </tr>
    <tr>
      <td>eng_Latn</td>
      <td>220</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>46</td>
      <td>376</td>
      <td>100</td>
      <td>-</td>
    </tr>
    <tr>
      <td>fin_Latn</td>
      <td>-</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>fra_Latn</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>-</td>
      <td>351</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>hat_Latn</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>hin_Deva</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>46</td>
      <td>372</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>ind_Latn</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
      <td>46</td>
      <td>373</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>ita_Latn</td>
      <td>220</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>100</td>
      <td>100</td>
    </tr>
    <tr>
      <td>jpn_Jpan</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
      <td>46</td>
      <td>353</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>kor_Hang</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
      <td>-</td>
      <td>333</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>mar_Deva</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>-</td>
      <td>331</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>pes_Arab</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>-</td>
      <td>369</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>por_Latn</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>-</td>
      <td>369</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>rus_Cyrl</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
      <td>46</td>
      <td>371</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>slk_Latn</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>spa_Latn</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>-</td>
      <td>370</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>swh_Latn</td>
      <td>-</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>355</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>tel_Telu</td>
      <td>-</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>354</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>tha_Thai</td>
      <td>-</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>322</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>tur_Latn</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>-</td>
      <td>366</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>vie_Latn</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>-</td>
      <td>364</td>
      <td>-</td>
      <td>100</td>
    </tr>
    <tr>
      <td>yor_Latn</td>
      <td>-</td>
      <td>-</td>
      <td>300</td>
      <td>-</td>
      <td>-</td>
      <td>217</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>zho_Hans</td>
      <td>220</td>
      <td>-</td>
      <td>300</td>
      <td>300</td>
      <td>46</td>
      <td>359</td>
      <td>100</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
</div>

# Data Origin and Licence
We collected samples from the datasets below to create this mix. Each subset, denoted by the `source` field, is re-distributed under its original licence:
- [CohereLabs/aya_dataset](https://huggingface.co/datasets/CohereLabs/aya_dataset): Apache 2.0
- [google-research-datasets/tydiqa](https://github.com/google-research-datasets/tydiqa): Apache 2.0
- [facebook/belebele](https://huggingface.co/datasets/facebook/belebele): CC BY-SA 4.0
- [wmt25-mist-oeg-gpt-4.1](https://github.com/wmt-conference/wmt-mist/blob/main/data/submissions/GPT-4.1.json): TBD
- [FBK-MT/MCIF](https://huggingface.co/datasets/FBK-MT/MCIF): CC BY 4.0
- [csebuetnlp/CrossSum](https://huggingface.co/datasets/csebuetnlp/CrossSum): CC BY-NC-SA 4.0
- [esdurmus/Wikilingua](https://github.com/esdurmus/Wikilingua) / [GEM/wiki_lingua](https://huggingface.co/datasets/GEM/wiki_lingua): CC BY-NC-SA 3.0