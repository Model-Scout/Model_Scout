---
license: cc-by-4.0
language:
- am
- hy
- zh
- ka
- ja
- km
- lo
- my
- te
- ta
- ml
- he
- hi
- ko
- kn
- or
- bn
- el
- gu
- la
- ru
- si
- th
- uk
- ar
- bo
size_categories:
- 100K<n<1M
tags:
- Cherokee
- Hanunoo
- Kaithi
- Lisu
- Miao
- Osage
- Sharada
- Siddham
- Soyombo
- TaiTham
- TaiViet
- Takri
- Thaana
- Tirhuta
- Tifinagh
- soyombo
- siddham
- sharada
- osage
- miao
- lisu
- kaithi
- Ethiopian
- Adlam
---


# 🌍 Tiny Multilingual CAPTCHA Library

**Repository:** `remiai3/tiny-captcha-library`  
A multilingual dataset of **synthetic 4-character CAPTCHA images** designed for **OCR, multilingual vision models, and script recognition research**.
This dataset spans **44 world writing systems** and is especially useful for **low-resource script OCR training**.

## 📌 Dataset Summary

Each script includes **10,000 unique CAPTCHA images**.  
The dataset is provided in **two parallel formats**:

- **CSV version** (standard ML workflows)
- **Parquet version** (faster loading for large-scale pipelines)

⚠️ The images inside both folders are **identical** — only the label file format differs.
So per language:
- 10,000 unique images  
- 10,000 duplicate copies (same images, different label format)  

## 🗂 Dataset Structure

tiny-captcha-library/
│
├── 4char/
│ ├── <Language_Name>/
│ │ ├── images.zip
│ │ └── labels.csv
│ └── ...
│
├── 4char_parquet/
│ ├── <Language_Name>/
│ │ ├── images.zip
│ │ └── labels.parquet
│ └── ...
│
├── Amharic.png
├── Armenian.png
└── ...

### Folder Details
| Folder | Contains | Purpose |
|-------|----------|---------|
| **4char/** | Images + `labels.csv` | Standard format |
| **4char_parquet/** | Same images + `labels.parquet` | Efficient ML pipelines |
Each language folder includes:
- `images.zip` → CAPTCHA images  
- Label file mapping image filename → correct 4-character text  

## 🌐 Supported Scripts
Amharic, Armenian, Arabic, Bengali, Cherokee, Chinese, Georgian, Greek, Gujarati, Hebrew, Hindi, Hanunoo, Japanese, Kaithi, 
Kannada, Khmer, Lao, Latin, Lisu, Malayalam, Miao, Modi, Myanmar, Odia, Osage, Russian, Sharada, Siddham, Sinhala, Soyombo, 
Tai Tham, Tai Viet, Takri, Thaana, Tirhuta, Tamil, Telugu, Thai, Ukrainian, Tifinagh, Korean, Tibetan, Ethiopian, Adlam

## 🖼 Sample CAPTCHA Styles

<table align="center">
<tr>
<td align="center"><img src="./Amharic.png" width="110"/><br>Amharic</td>
<td align="center"><img src="./Arabic.png" width="110"/><br>Arabic</td>
<td align="center"><img src="./Armenian.png" width="110"/><br>Armenian</td>
<td align="center"><img src="./Bengali.png" width="110"/><br>Bengali</td>
<td align="center"><img src="./Cherokee.png" width="110"/><br>Cherokee</td>
<td align="center"><img src="./Chinese.png" width="110"/><br>Chinese</td>
</tr>

<tr>
<td align="center"><img src="./Georgian.png" width="110"/><br>Georgian</td>
<td align="center"><img src="./Greek.png" width="110"/><br>Greek</td>
<td align="center"><img src="./Gujarati.png" width="110"/><br>Gujarati</td>
<td align="center"><img src="./Hanunoo.png" width="110"/><br>Hanunoo</td>
<td align="center"><img src="./Hebrew.png" width="110"/><br>Hebrew</td>
<td align="center"><img src="./Hindi.png" width="110"/><br>Hindi</td>
</tr>

<tr>
<td align="center"><img src="./Japanese.png" width="110"/><br>Japanese</td>
<td align="center"><img src="./Kaithi.png" width="110"/><br>Kaithi</td>
<td align="center"><img src="./Kannada.png" width="110"/><br>Kannada</td>
<td align="center"><img src="./Khmer.png" width="110"/><br>Khmer</td>
<td align="center"><img src="./Lao.png" width="110"/><br>Lao</td>
<td align="center"><img src="./Latin.png" width="110"/><br>Latin</td>
</tr>

<tr>
<td align="center"><img src="./Lisu.png" width="110"/><br>Lisu</td>
<td align="center"><img src="./Malayalam.png" width="110"/><br>Malayalam</td>
<td align="center"><img src="./Miao.png" width="110"/><br>Miao</td>
<td align="center"><img src="./Modi.png" width="110"/><br>Modi</td>
<td align="center"><img src="./Myanmar.png" width="110"/><br>Myanmar</td>
<td align="center"><img src="./Odia.png" width="110"/><br>Odia</td>
</tr>

<tr>
<td align="center"><img src="./Osage.png" width="110"/><br>Osage</td>
<td align="center"><img src="./Russian.png" width="110"/><br>Russian</td>
<td align="center"><img src="./Sharada.png" width="110"/><br>Sharada</td>
<td align="center"><img src="./Siddham.png" width="110"/><br>Siddham</td>
<td align="center"><img src="./Sinhala.png" width="110"/><br>Sinhala</td>
<td align="center"><img src="./Soyombo.png" width="110"/><br>Soyombo</td>
</tr>

<tr>
<td align="center"><img src="./TaiTham.png" width="110"/><br>Tai Tham</td>
<td align="center"><img src="./TaiViet.png" width="110"/><br>Tai Viet</td>
<td align="center"><img src="./Takri.png" width="110"/><br>Takri</td>
<td align="center"><img src="./Tamil.png" width="110"/><br>Tamil</td>
<td align="center"><img src="./Telugu.png" width="110"/><br>Telugu</td>
<td align="center"><img src="./Thaana.png" width="110"/><br>Thaana</td>
</tr>

<tr>
<td align="center"><img src="./Thai.png" width="110"/><br>Thai</td>
<td align="center"><img src="./Tirhuta.png" width="110"/><br>Tirhuta</td>
<td align="center"><img src="./Ukrainian.png" width="110"/><br>Ukrainian</td>
<td align="center"><img src="./Tifinagh.png" width="110"/><br>Tifinagh</td>
<td align="center"><img src="./Korean.png" width="110"/><br>Korean</td>
<td align="center"><img src="./Tibetan.png" width="110"/><br>Tibetan</td>
</tr>
<tr>
<td align="center"><img src="./Ethiopian.png" width="110"/><br>Ethiopian</td>
<td align="center"><img src="./Adlam.png" width="110"/><br>Adlam</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

## 🏷 Label Format
### CSV
| filename | label |
|----------|-------|
| img_00001.png | text |
| img_00002.png | text |

### Parquet
Same structure as CSV but stored in columnar format.

## 📊 Dataset Statistics
| Metric | Value |
|-------|------|
| Total Scripts | 44 |
| Unique Images per Script | 10,000 |
| Total Unique Images | 440,000 |
| Images Including Duplicates | 880,000 |
| Characters per CAPTCHA | 4 |

## 🎯 Intended Use
This dataset is designed for:
- Multilingual OCR training  
- Vision-language model pretraining  
- Script recognition research  
- Robust text recognition under distortion  
🚫 Not intended for bypassing real-world CAPTCHA security systems.

## ⚙️ Example Loading

```python
import pandas as pd

df = pd.read_csv("labels.csv")
print(df.head())