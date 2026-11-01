---
license: cc0-1.0
language:
- bal
- bcc
- glk
- brh
- sdh
- kur
- hac
- kiu
- zza
- twi
- fat
- aka

configs:
- config_name: azb_Arab
  data_files: "azb_Arab/azb_Arab.csv"
- config_name: bal_Arab
  data_files: "bal_Arab/bal_Arab.csv"
- config_name: brh_Arab
  data_files: "brh_Arab/brh_Arab.csv"
- config_name: fat_Latn
  data_files: "fat_Latn/fat_Latn.csv"
- config_name: glk_Arab
  data_files: "glk_Arab/glk_Arab.csv"
- config_name: hac_Arab
  data_files: "hac_Arab/hac_Arab.csv"
- config_name: kiu_Latn
  data_files: "kiu_Latn/kiu_Latn.csv"
- config_name: sdh_Arab
  data_files: "sdh_Arab/sdh_Arab.csv"
- config_name: twi_Latn
  data_files: "twi_Latn/twi_Latn.csv"
- config_name: uzs_Arab
  data_files: "uzs_Arab/uzs_Arab.csv"

pretty_name: GlotSparse Corpus
---

# GlotSparse Corpus

Collection of news websites in low-resource languages.

- **Homepage:** [homepage](https://github.com/cisnlp/GlotSparse)
- **Repository:** [github](https://github.com/cisnlp/GlotSparse)
- **Paper:** [paper](https://arxiv.org/abs/2310.16248)
- **Point of Contact:** amir@cis.lmu.de

These languages are supported:

```
('azb_Arab', 'South-Azerbaijani_Arab')
('bal_Arab', 'Balochi_Arab')
('brh_Arab', 'Brahui_Arab')
('fat_Latn', 'Fanti_Latn') # aka
('glk_Arab', 'Gilaki_Arab')
('hac_Arab', 'Gurani_Arab')
('kiu_Latn', 'Kirmanjki_Latn') # zza
('sdh_Arab', 'Southern-Kurdish_Arab')
('twi_Latn', 'Twi_Latn') # aka
('uzs_Arab', 'Southern-Uzbek_Arab')
```

## Usage (HF Loader)
Replace `twi_Latn` with your specific language.
```python
from datasets import load_dataset
dataset = load_dataset('cis-lmu/GlotSparse', 'twi_Latn')
print(dataset['train'][0]) # First row of Twi_Latn
```

## Download
If you are not a fan of the HF dataloader or are just interested in a specific language, download it directly:
Replace `twi_Latn` with your specific language.

```python
! wget https://huggingface.co/datasets/cis-lmu/GlotSparse/resolve/main/twi_Latn/twi_Latn.csv
```


## Sources

- **Balochi (bal)**
  - News: https://sunnionline.us/balochi/
  - Stories: https://kissah.org/
  - Deiverse Contents such as poems, stories, posts, etc: https://baask.com/archive/category/balochi/

- **Gilaki (glk)**
  - Social Media: The original source of this content is Twitter, but Twitter typically doesn't support Gilaki as part of its language identifier due to gilaki is a low resource language. We obtained this content from a Telegram channel (https://t.me/gilaki_twitter) that re-posts Gilaki Twitter content. The admins of the channel are native Gilaki speakers, and after manual inspection, these tweets are selected. At present, there isn't a readily available mapping for Twitter IDs. The primary reason for reposting Twitter content on Telegram in Iran is the relative ease of access to Telegram compared to Twitter.

- **Brahui (brh)**
  - News: https://talarbrahui.com/category/news/ and https://talarbrahui.com/category/articles/

- **Southern-Kurdish (sdh)**
  - News: https://shafaq.com/ku/ (Feyli)

- **Gurani (hac)**
  - News: https://anfsorani.com/هۆرامی (Hawrami)

- **Kirmanjki (kiu)**
  - News: https://anfkirmancki.com/

- **Fanti (fat)**
  - News: https://akannews.com/fante/
 
- **Twi (twi)**
  - News: https://akannews.com/asante-twi/

- **South-Azerbaijani (azb)**
  - News: https://www.trt.net.tr/turki/
 
- **Southern Uzbek (uzs)**
  - News: https://www.trt.net.tr/afghaniuzbek/

## Tools

To compute the script of each text and removing unwanted langauges we used Glotscript ([code](https://github.com/cisnlp/GlotScript) and [paper](https://arxiv.org/abs/2309.13320)).


## License
We do not own any of the text from which these data has been extracted.
We license the actual packaging, the metadata and the annotations of these data under the cc0-1.0 (waiving all of the rights under copyright law).

If you are a website/dataset owner and do not want your data to be included in this corpra, please send us an email at amir@cis.lmu.de .


## Ethical Considerations

**1. Biases:** The text corpus may reflect the perspectives, opinions, or demographics of its sources or creators. It is important for users to critically evaluate the text in context especially for **news sources** and **social medias** (e.g., sunnionline, twitter, ...).

**2. Representativeness:** While we have aimed for diversity and inclusivity, the text corpus may not fully represent all native speakers. Users should be mindful of any potential underrepresentation.

**3. Ethics:** We acknowledge that the collection and use of text data can have ethical implications. We have strived to handle the data responsibly, but we encourage users to consider the broader ethical implications of their own research or applications.

**4. Robots.txt** We respect robots.txt, https://palewi.re/docs/news-homepages/openai-gptbot-robotstxt.html



## Github
We also host a GitHub version with representing similar metadata from other sources:
https://github.com/cisnlp/GlotSparse

## Citation
If you use any part of this code and data in your research, please cite it using the following BibTeX entry.
All the sources related to news, social media, and without mentioned datasets are crawled and compiled in this work.
This work is part of the [GlotLID](https://github.com/cisnlp/GlotLID) project.

```
@inproceedings{
  kargaran2023glotlid,
  title={{GlotLID}: Language Identification for Low-Resource Languages},
  author={Kargaran, Amir Hossein and Imani, Ayyoob and Yvon, Fran{\c{c}}ois and Sch{\"u}tze, Hinrich},
  booktitle={The 2023 Conference on Empirical Methods in Natural Language Processing},
  year={2023},
  url={https://openreview.net/forum?id=dl4e3EBz5j}
}

```