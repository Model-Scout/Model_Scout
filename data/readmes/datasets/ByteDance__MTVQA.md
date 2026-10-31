---
language:
- multilingual
- ar
- de
- vi
- ja
- ko
- fr
- ru
- it
- th
license: cc-by-nc-4.0
size_categories:
- 10K<n<100K
task_categories:
- visual-question-answering
- image-to-text
tags:
- multilingual
- text-centric
- vqa
dataset_info:
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: qa_pairs
    dtype: string
  - name: lang
    dtype: string
  splits:
  - name: train
    num_bytes: 3078399368.832
    num_examples: 6678
  - name: test
    num_bytes: 1052451409.396
    num_examples: 2116
  download_size: 4239693120
  dataset_size: 4130850778.2279997
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

# Dataset Card
The dataset is oriented toward visual question answering of multilingual text scenes in nine languages, including Korean, Japanese, Italian, Russian, Deutsch, French, Thai, Arabic, and Vietnamese. The question-answer pairs are labeled by native annotators following a series of rules. A comprehensive description of the dataset can be found in the paper [MTVQA](https://arxiv.org/pdf/2405.11985).

## - Image Distribution

<table style="width:60%;">
    <tr>
        <td></td>
        <td><b>KO</b></td>
        <td><b>JA</b></td>
        <td><b>IT</b></td>
        <td><b>RU</b></td>
        <td><b>DE</b></td>
        <td><b>FR</b></td>
        <td><b>TH</b></td>
        <td><b>AR</b></td>
        <td><b>VI</b></td>
        <td><b>Total</b> </td>
    </tr>
    <tr>
        <td><b>Train Images</b></td>
        <td>580</td>
        <td>1039</td>
        <td>622</td>
        <td>635</td>
        <td>984</td>
        <td>792</td>
        <td>319</td>
        <td>568</td>
        <td>1139</td>
        <td>6678 </td>
    </tr>
    <tr>
        <td><b>Test Images</b></td>
        <td>250</td>
        <td>250</td>
        <td>250</td>
        <td>250</td>
        <td>250</td>
        <td>250</td>
        <td>116</td>
        <td>250</td>
        <td>250</td>
        <td>2116 </td>
    </tr>
    <tr>
        <td><b>Train QA</b></td>
        <td>1280</td>
        <td>3332</td>
        <td>2168</td>
        <td>1835</td>
        <td>4238</td>
        <td>2743</td>
        <td>625</td>
        <td>1597</td>
        <td>4011</td>
        <td>21829 </td>
    </tr>
    <tr>
        <td><b>Test QA</b></td>
        <td>558</td>
        <td>828</td>
        <td>884</td>
        <td>756</td>
        <td>1048</td>
        <td>886</td>
        <td>231</td>
        <td>703</td>
        <td>884</td>
        <td>6778</td>
    </tr>
</table>

## - LeaderBoard
<table style="width:75%;">
    <tr>
        <th>Models</th>
        <td><b>AR</b></td>
        <td><b><b>DE</b></td>
        <td><b>FR</b></td>
        <td><b>IT</b></td>
        <td><b>JA</b></td>
        <td><b>KO</b></td>
        <td><b>RU</b></td>
        <td><b>TH</b></td>
        <td><b>VI</b></td>
        <td><b>Average</b> </td>
    </tr>
    <tr>
        <th align="left">GPT-4O</th>
        <td>20.2 </td>
        <td>34.2 </td>
        <td>41.2 </td>
        <td>32.7 </td>
        <td>20.0 </td>
        <td>33.9 </td>
        <td>11.5 </td>
        <td>22.5 </td>
        <td>34.2 </td>
        <td>27.8 </td>
    </tr>
    <tr>
        <th align="left">Claude3 Opus</th>
        <td>15.1 </td>
        <td>33.4 </td>
        <td>40.6 </td>
        <td>34.4 </td>
        <td>19.4 </td>
        <td>27.2 </td>
        <td>13.0 </td>
        <td>19.5 </td>
        <td>29.1 </td>
        <td>25.7  </td>
    </tr>
    <tr>
        <th align="left">Gemini Ultra</th>
        <td>14.7 </td>
        <td>32.3 </td>
        <td>40.0 </td>
        <td>31.8 </td>
        <td>12.3 </td>
        <td>17.2 </td>
        <td>11.8 </td>
        <td>20.3 </td>
        <td>28.6 </td>
        <td>23.2  </td>
    </tr>
    <tr>
        <th align="left">GPT-4V</th>
        <td>11.5 </td>
        <td>31.5 </td>
        <td>40.4 </td>
        <td>32.3 </td>
        <td>11.5 </td>
        <td>16.7 </td>
        <td>10.3 </td>
        <td>15.0 </td>
        <td>28.9 </td>
        <td>22.0  </td>
    </tr>
    <tr>
        <th align="left">QwenVL Max</th>
        <td>7.7 </td>
        <td>31.4 </td>
        <td>37.6 </td>
        <td>30.2 </td>
        <td>18.6 </td>
        <td>25.4 </td>
        <td>10.4 </td>
        <td>4.8 </td>
        <td>23.5 </td>
        <td>21.1  </td>
    </tr>
    <tr>
        <th align="left">Claude3 Sonnet</th>
        <td>10.5 </td>
        <td>28.9 </td>
        <td>35.6 </td>
        <td>31.8 </td>
        <td>13.9 </td>
        <td>22.2 </td>
        <td>11.0 </td>
        <td>15.2 </td>
        <td>20.8 </td>
        <td>21.1  </td>
    </tr>
    <tr>
        <th align="left">QwenVL Plus</th>
        <td>4.8 </td>
        <td>28.8 </td>
        <td>33.7 </td>
        <td>27.1 </td>
        <td>12.8 </td>
        <td>19.9 </td>
        <td>9.4 </td>
        <td>5.6 </td>
        <td>18.1 </td>
        <td>17.8  </td>
    </tr>
    <tr>
        <th align="left">MiniCPM-Llama3-V-2_5</th>
        <td>6.1 </td>
        <td>29.6 </td>
        <td>35.7 </td>
        <td>26.0 </td>
        <td>12.1 </td>
        <td>13.1 </td>
        <td>5.7 </td>
        <td>12.6 </td>
        <td>15.3 </td>
        <td>17.3  </td>
    </tr>
    <tr>
        <th align="left">InternVL-V1.5</th>
        <td>3.4 </td>
        <td>27.1 </td>
        <td>31.4 </td>
        <td>27.1 </td>
        <td>9.9 </td>
        <td>9.0 </td>
        <td>4.9 </td>
        <td>8.7 </td>
        <td>12.4 </td>
        <td>14.9  </td>
    </tr>
    <tr>
        <th align="left">GLM4V</th>
        <td>0.3 </td>
        <td>30.0 </td>
        <td>34.1 </td>
        <td>30.1 </td>
        <td>3.4 </td>
        <td>5.7 </td>
        <td>3.0 </td>
        <td>3.5 </td>
        <td>12.3 </td>
        <td>13.6  </td>
    </tr>
    <tr>
        <th align="left">TextSquare</th>
        <td>3.7 </td>
        <td>27.0 </td>
        <td>30.8 </td>
        <td>26.7 </td>
        <td>3.2 </td>
        <td>7.2 </td>
        <td>6.7 </td>
        <td>5.2 </td>
        <td>12.4 </td>
        <td>13.6  </td>
    </tr>
    <tr>
        <th align="left">Mini-Gemini-HD-34B</th>
        <td>2.2 </td>
        <td>25.0 </td>
        <td>29.2 </td>
        <td>25.5 </td>
        <td>6.1 </td>
        <td>8.6 </td>
        <td>4.1 </td>
        <td>4.3 </td>
        <td>11.8 </td>
        <td>13.0  </td>
    </tr>
    <tr>
        <th align="left">InternLM-Xcomposer2-4KHD</th>
        <td>2.0 </td>
        <td>20.6 </td>
        <td>23.2 </td>
        <td>21.6 </td>
        <td>5.6 </td>
        <td>7.7 </td>
        <td>4.1 </td>
        <td>6.1 </td>
        <td>10.1 </td>
        <td>11.2  </td>
    </tr>
    <tr>
        <th align="left">Llava-Next-34B</th>
        <td>3.3 </td>
        <td>24.0 </td>
        <td>28.0 </td>
        <td>22.3 </td>
        <td>3.6 </td>
        <td>6.1 </td>
        <td>2.6 </td>
        <td>0.4 </td>
        <td>9.8 </td>
        <td>11.1  </td>
    </tr>
    <tr>
        <th align="left">TextMonkey</th>
        <td>2.0 </td>
        <td>18.1 </td>
        <td>19.9 </td>
        <td>22.1 </td>
        <td>4.6 </td>
        <td>7.2 </td>
        <td>3.2 </td>
        <td>0.9 </td>
        <td>11.1 </td>
        <td>9.9  </td>
    </tr>
    <tr>
        <th align="left">MiniCPM-V-2</th>
        <td>1.3 </td>
        <td>12.7 </td>
        <td>14.9 </td>
        <td>17.0 </td>
        <td>3.7 </td>
        <td>5.6 </td>
        <td>2.2 </td>
        <td>2.2 </td>
        <td>6.8 </td>
        <td>7.4  </td>
    </tr>
    <tr>
        <th align="left">mPLUG-DocOwl 1.5</th>
        <td>1.0 </td>
        <td>13.9 </td>
        <td>14.9 </td>
        <td>18.2 </td>
        <td>2.9 </td>
        <td>5.0 </td>
        <td>2.0 </td>
        <td>0.9 </td>
        <td>6.4 </td>
        <td>7.2  </td>
    </tr>
    <tr>
        <th align="left">YI-VL-34B</th>
        <td>1.7 </td>
        <td>13.5 </td>
        <td>15.7 </td>
        <td>12.1 </td>
        <td>4.8 </td>
        <td>5.2 </td>
        <td>0.8 </td>
        <td>3.5 </td>
        <td>4.1 </td>
        <td>6.8  </td>
    </tr>
    <tr>
        <th align="left">DeepSeek-VL</th>
        <td>0.6 </td>
        <td>14.2 </td>
        <td>15.3 </td>
        <td>15.2 </td>
        <td>2.9 </td>
        <td>3.8 </td>
        <td>1.6 </td>
        <td>0.9 </td>
        <td>5.2 </td>
        <td>6.6 </td>
    </tr>
</table>


## - Direct usage
The data is designed to evaluate and enhance the multilingual textual vqa capabilities of multimodal models in the hope of facilitating the understanding of multilingual images, enabling AI to reach more people in the world.

### -- Huggingface dataloader
```
from datasets import load_dataset
dataset = load_dataset("ByteDance/MTVQA")
```

## - Out-of-Scope usage
Academic use only, not supported for commercial usage.

## - Ethics Assessment
Both GPT4V and manual assessment are employed to filter out unethical question and answer pairs.

## - Bias, Risks, and Limitations
Your access to and use of this dataset are at your own risk. We do not guarantee the accuracy of this dataset. The dataset is provided “as is” and we make no warranty or representation to you with respect to it and we expressly disclaim, and hereby expressly waive, all warranties, express, implied, statutory or otherwise. This includes, without limitation, warranties of quality, performance, merchantability or fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. In no event will we be liable to you on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this public license or use of the licensed material. The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.


## - Citation
```
@misc{tang2024mtvqa,
      title={MTVQA: Benchmarking Multilingual Text-Centric Visual Question Answering}, 
      author={Jingqun Tang and Qi Liu and Yongjie Ye and Jinghui Lu and Shu Wei and Chunhui Lin and Wanqing Li and Mohamad Fitri Faiz Bin Mahmood and Hao Feng and Zhen Zhao and Yanjie Wang and Yuliang Liu and Hao Liu and Xiang Bai and Can Huang},
      year={2024},
      eprint={2405.11985},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

