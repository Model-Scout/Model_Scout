---
license: apache-2.0
dataset_info:
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_examples: 403
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.json
task_categories:
- visual-question-answering
- question-answering
language:
- am
- ar
- bg
- bn
- cs
- de
- el
- en
- es
- fa
- fr
- ga
- hi
- id
- ig
- it
- iw
- ja
- jv
- ko
- nl
- mn
- ms
- no
- pl
- pt
- ro
- ru
- si
- su
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
tags:
- multilingual
- multimodal
- vision-language-models
- cultures
- vlms
pretty_name: CulturalGround
size_categories:
- 10M<n<100M
viewer: false
---

# [EMNLP 2025 Oral 🔥] CulturalGround: Grounding Multilingual Multimodal LLMs With Cultural Knowledge


🌍 🇩🇪 🇫🇷 🇬🇧 🇪🇸 🇮🇹 🇵🇱 🇷🇺 🇨🇿 🇯🇵 🇺🇦 🇧🇷 🇮🇳 🇨🇳 🇳🇴 🇵🇹 🇮🇩 🇮🇱 🇹🇷 🇬🇷 🇷🇴 🇮🇷 🇹🇼 🇲🇽 🇮🇪 🇰🇷 🇧🇬 🇹🇭 🇳🇱 🇪🇬 🇵🇰 🇳🇬 🇮🇩 🇻🇳 🇲🇾 🇸🇦 🇮🇩 🇧🇩 🇸🇬 🇱🇰 🇰🇪 🇲🇳 🇪🇹 🇹🇿 🇷🇼

[🏠 Homepage](https://neulab.github.io/CulturalGround/) | [🤖 CulturalPangea-7B](https://huggingface.co/neulab/CulturalPangea-7B) | [📊 CulturalGround](https://huggingface.co/datasets/neulab/CulturalGround) | [💻 Github](https://github.com/neulab/CulturalGround) | [📄 Arxiv](https://arxiv.org/abs/2508.07414) 

<img src="https://neulab.github.io/CulturalGround/static/img/icons/culturalpangea1.png" alt="CulturalGround" style="width: 35%; margin-right: 1em;">

We introduce <strong>CulturalGround</strong>, a large-scale cultural VQA dataset and a pipeline for creating cultural grounded VQA data for improving cultural understanding in multilingual multimodal LLMs. Our results demonstrate strong cross-lingual and cultural generalization, and we evaluate models across diverse geographic and cultural contexts.


This repository contains the <strong>CulturalGround</strong> dataset, a large-scale, multilingual, and multimodal visual question-answering (VQA) collection designed to ground multimodal language models in diverse cultural knowledge. The dataset was used to train the <strong>CulturalPangea</strong> model.

---
## 📜 Description of CulturalGround

**CulturalGround** is a high-quality, culturally-rich dataset comprising over **22 million** open-ended, and **8 million** multiple-choices VQA pairs. It spans **42 countries** and **39 languages**, with a focus on culturally significant entities often underrepresented in standard training corpora. The dataset was created using a scalable pipeline that leverages Wikidata to identify cultural concepts, gather corresponding images from Wikimedia Commons, and generate factually grounded VQA pairs.

The data is provided in four main splits:
1.  **22M Open-Ended (OE) VQA Samples**: The full, unfiltered set of open-ended questions generated from templates and refined by LLM for clarity and naturalness.
2.  **14M Filtered Open-Ended (OE) VQA Samples**: A cleaner subset of the OE questions, filtered for relevance and quality using a VLM.
3.  **8M Multiple-Choices VQA Samples**: The full, unfiltered set of multiple-choices question generated from cultural entities
4.  **6M Filtered Multiple-Choice (MCQ) VQA**: A set of multiple-choice and true/false questions, also filtered for quality.

---
<p align="center">
  <img src="https://neulab.github.io/CulturalGround/static/img/teaser.jpg" alt="CulturalGround" style="width:80%;">
</p>

## 📊 Dataset Statistics

The dataset was constructed by identifying culturally significant entities from Wikidata, collecting 1-3 images per entity, and generating questions based on 76 cultural properties.

### Data Distribution by Country/Region

Below is brief distribution of the dataset across regions and languages. For detailed breakdown, check the tables below.

<p align="center">
  <img src="https://neulab.github.io/CulturalGround/static/img/data_distribution_region_language.png" alt="CulturalGround" style="width:80%;">
</p>

| Country | Total Entities | Total Images | Template QA (Unfiltered) | Open-Ended (Unfiltered) | MCQ (Unfiltered) | Open-Ended (Filtered) | MCQs (Filtered) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Germany** | 332,650 | 350,828 | 2,752,048 | 2,835,679 | 965,541 | 1,506,438 | 426,272 |
| **France** | 268,298 | 276,983 | 2,676,838 | 2,729,262 | 941,466 | 1,435,627 | 528,449 |
| **United Kingdom** | 175,486 | 328,906 | 1,355,577 | 2,183,466 | 891,282 | 1,319,135 | 469,302 |
| **Italy** | 128,821 | 222,351 | 1,133,463 | 1,763,658 | 745,977 | 1,323,626 | 653,884 |
| **Spain** | 124,280 | 216,019 | 985,241 | 1,519,295 | 616,304 | 906,943 | 545,056 |
| **Japan** | 82,690 | 145,843 | 793,759 | 1,214,762 | 483,233 | 799,963 | 431,739 |
| **Czechia** | 110,384 | 198,223 | 636,978 | 994,864 | 401,437 | 679,115 | 380,160 |
| **Poland** | 98,577 | 131,155 | 753,750 | 936,799 | 361,028 | 529,669 | 328,143 |
| **Russia** | 119,158 | 180,253 | 613,822 | 848,540 | 343,834 | 628,558 | 311,416 |
| **India** | 29,574 | 72,683 | 365,804 | 717,067 | 218,854 | 542,516 | 270,301 |
| **Brazil** | 38,575 | 68,775 | 419,684 | 648,164 | 257,966 | 479,162 | 236,749 |
| **Ukraine** | 57,665 | 100,367 | 367,819 | 562,770 | 224,044 | 421,096 | 207,434 |
| **China** | 38,435 | 68,858 | 288,524 | 468,916 | 200,950 | 365,277 | 187,660 |
| **Norway** | 27,632 | 47,615 | 255,226 | 382,264 | 146,757 | 273,697 | 118,463 |
| **Netherlands** | 72,709 | 72,709 | 375,078 | 375,020 | 119,563 | 225,651 | 114,602 |
| **Mexico** | 12,224 | 29,724 | 184,998 | 370,152 | 113,682 | 271,408 | 122,758 |
| **Israel** | 19,689 | 33,731 | 183,099 | 289,430 | 124,912 | 233,556 | 105,840 |
| **Romania** | 15,408 | 26,451 | 196,705 | 287,122 | 109,326 | 194,952 | 104,126 |
| **Indonesia** | 9,026 | 22,060 | 145,832 | 256,309 | 66,731 | 148,594 | 79,859 |
| **Turkey** | 13,610 | 23,876 | 163,963 | 256,350 | 107,366 | 183,648 | 99,250 |
| **Iran** | 12,930 | 32,496 | 114,996 | 252,235 | 80,307 | 194,867 | 103,478 |
| **Greece** | 9,975 | 24,887 | 125,163 | 250,048 | 76,779 | 172,912 | 95,873 |
| **Portugal** | 19,733 | 35,229 | 155,542 | 237,166 | 94,069 | 162,184 | 93,708 |
| **South Korea** | 8,809 | 15,175 | 149,796 | 209,911 | 71,649 | 123,550 | 65,233 |
| **Ireland** | 9,115 | 22,856 | 86,838 | 185,033 | 58,225 | 146,654 | 72,337 |
| **Bulgaria** | 7,167 | 17,315 | 94,452 | 177,989 | 54,002 | 129,713 | 64,048 |
| **Taiwan** | 12,644 | 33,410 | 71,483 | 166,306 | 54,930 | 142,712 | 70,085 |
| **Egypt** | 3,920 | 9,596 | 63,237 | 136,891 | 43,655 | 104,816 | 48,698 |
| **Thailand** | 5,837 | 15,037 | 58,397 | 125,292 | 39,345 | 101,078 | 49,959 |
| **Pakistan** | 2,851 | 6,973 | 38,005 | 76,927 | 24,085 | 59,778 | 29,507 |
| **Malaysia** | 3,858 | 9,788 | 38,208 | 79,684 | 24,666 | 63,484 | 31,065 |
| **Nigeria** | 2,519 | 6,368 | 42,080 | 77,164 | 21,339 | 53,213 | 25,948 |
| **Bangladesh** | 3,659 | 9,236 | 29,253 | 62,700 | 20,382 | 51,071 | 25,715 |
| **Vietnam** | 3,230 | 5,744 | 37,035 | 58,513 | 24,297 | 43,626 | 21,855 |
| **Singapore** | 1,752 | 4,298 | 23,619 | 54,281 | 17,059 | 41,825 | 19,176 |
| **Saudi Arabia** | 948 | 2,292 | 17,759 | 35,046 | 10,772 | 26,547 | 13,087 |
| **Kenya** | 1,120 | 2,763 | 17,251 | 36,337 | 11,412 | 29,164 | 14,657 |
| **Ethiopia** | 880 | 2,163 | 14,244 | 29,976 | 9,551 | 23,713 | 10,955 |
| **Sri Lanka** | 1,066 | 2,651 | 14,643 | 29,484 | 8,861 | 22,177 | 10,913 |
| **Tanzania** | 592 | 1,454 | 11,966 | 26,332 | 8,451 | 17,689 | 11,589 |
| **Mongolia** | 542 | 1,306 | 12,482 | 23,604 | 6,900 | 16,429 | 8,765 |
| **Rwanda** | 572 | 1,393 | 7,332 | 15,693 | 5,157 | 11,850 | 5,821 |
| **Total** | **1,888,610** | **2,879,840** | **15,871,989** | **21,986,501** | **8,206,146** | **14,207,683** | **6,613,935** |

### Data Distribution by Language

| Language | Open-Ended (Unfiltered) | MCQs (Unfiltered) | Open-Ended (Filtered) | MCQs (Filtered) |
| :--- | :--- | :--- | :--- | :--- |
| **en** (English) | 3,778,963 | 1,369,758 | 2,501,144 | 1,152,830 |
| **fr** (French) | 1,822,466 | 668,153 | 1,181,935 | 530,004 |
| **de** (German) | 1,782,256 | 626,116 | 1,083,314 | 469,522 |
| **nl** (Dutch) | 1,648,445 | 602,869 | 1,053,835 | 487,091 |
| **es** (Spanish) | 1,415,511 | 508,136 | 878,913 | 412,530 |
| **it** (Italian) | 1,114,458 | 430,928 | 745,316 | 347,233 |
| **ga** (Irish) | 964,614 | 357,266 | 615,712 | 282,814 |
| **pl** (Polish) | 818,624 | 312,878 | 511,913 | 245,297 |
| **ru** (Russian) | 849,610 | 336,357 | 553,662 | 277,540 |
| **pt** (Portuguese) | 872,402 | 324,938 | 542,464 | 244,671 |
| **cs** (Czech) | 781,353 | 285,846 | 480,799 | 233,627 |
| **ja** (Japanese) | 685,032 | 267,259 | 441,822 | 215,680 |
| **zh** (Chinese) | 728,825 | 286,369 | 491,016 | 236,206 |
| **tr** (Turkish) | 640,652 | 246,485 | 415,126 | 194,963 |
| **uk** (Ukrainian) | 526,988 | 208,179 | 346,493 | 172,357 |
| **ro** (Romanian) | 366,781 | 141,767 | 242,138 | 105,055 |
| **fa** (Persian) | 362,570 | 145,847 | 241,236 | 115,227 |
| **id** (Indonesian) | 347,249 | 130,057 | 223,098 | 100,871 |
| **ar** (Arabic) | 346,263 | 134,798 | 229,576 | 110,000 |
| **vi** (Vietnamese) | 298,369 | 118,273 | 199,562 | 87,990 |
| **ko** (Korean) | 256,574 | 104,499 | 172,769 | 84,691 |
| **he** (Hebrew) | 221,549 | 91,434 | 150,173 | 71,602 |
| **ms** (Malay) | 243,026 | 93,024 | 161,397 | 69,462 |
| **el** (Greek) | 166,436 | 64,092 | 102,493 | 50,733 |
| **bg** (Bulgarian) | 139,184 | 55,340 | 92,766 | 45,780 |
| **bn** (Bengali) | 137,984 | 48,763 | 95,023 | 46,212 |
| **ur** (Urdu) | 97,025 | 37,085 | 65,567 | 33,166 |
| **hi** (Hindi) | 77,997 | 27,260 | 57,202 | 29,295 |
| **sw** (Swahili) | 128,935 | 46,746 | 77,641 | 32,988 |
| **ta** (Tamil) | 75,908 | 27,264 | 53,259 | 26,670 |
| **th** (Thai) | 85,927 | 33,369 | 58,433 | 30,558 |
| **te** (Telugu) | 55,477 | 20,068 | 38,837 | 20,015 |
| **jv** (Javanese) | 58,164 | 21,218 | 39,747 | 19,933 |
| **su** (Sundanese) | 30,857 | 10,840 | 21,238 | 10,583 |
| **ig** (Igbo) | 23,854 | 8,278 | 16,154 | 7,729 |
| **si** (Sinhala) | 16,828 | 6,687 | 12,407 | 6,306 |
| **mn** (Mongolian) | 13,495 | 5,605 | 9,650 | 4,682 |
| **am** (Amharic) | 3,975 | 1,627 | 2,704 | 1,483 |
| **no** (Norwegian) | 1,875 | 668 | 1,149 | 539 |
| **TOTAL** | **21,986,501** | **8,206,146** | **14,207,683** | **6,613,935** |


---
## 🛠️ How to Use

The data is provided as a series of `.tar.gz` archives, one for each country, containing the relevant images. The VQA data is provided in separate JSON files.

To download the image archives for a specific country, you can use the following `huggingface-cli` command:

```bash
huggingface-cli download neulab/CulturalGround CultureGroundImages/germany.tar.gz --repo-type dataset --local-dir ./
```

Once downloaded, you can extract the images:

```bash
tar -xvf germany.tar.gz
```

## 📜 Citation

If you use the CulturalGround dataset or the CulturalPangea model, please cite our paper:

```
@preprint{nyandwi2025grounding,
  title={Grounding Multilingual Multimodal LLMs With Cultural Knowledge},
  author={Nyandwi, Jean de Dieu and Song, Yueqi and Khanuja, Simran and Neubig, Graham},
  year={2025}
}
```
## 📞 Contact

For questions about the dataset, please contact {jeandedi, yueqis, skhanuja, gneubig}@andrew.cmu.edu.