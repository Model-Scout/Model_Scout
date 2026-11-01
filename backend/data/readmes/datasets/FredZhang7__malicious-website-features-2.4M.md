---
license: apache-2.0
task_categories:
- text-classification
- feature-extraction
- tabular-classification
language:
- 'no'
- af
- en
- et
- sw
- sv
- sq
- de
- ca
- hu
- da
- tl
- so
- fi
- fr
- cs
- hr
- cy
- es
- sl
- tr
- pl
- pt
- nl
- id
- sk
- lt
- lv
- vi
- it
- ro
- ru
- mk
- bg
- th
- ja
- ko
- multilingual
size_categories:
- 1M<n<10M
---

**Important Notice:**
- A subset of the URL dataset is from Kaggle, and the Kaggle datasets contained 10%-15% mislabelled data. See [this dicussion I opened](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset/discussion/431505) for some false positives. I have contacted Kaggle regarding their erroneous "Usability" score calculation for these unreliable datasets.
- The feature extraction methods shown here are not robust at all in 2023, and there're even silly mistakes in 3 functions: `not_indexed_by_google`, `domain_registration_length`, and `age_of_domain`.

<br>

The *features* dataset is original, and my feature extraction method is covered in [feature_extraction.py](./feature_extraction.py).
To extract features from a website, simply passed the URL and label to `collect_data()`. The features are saved to `phishing_detection_dataset.csv` locally by default.

In the *features* dataset, there're 911,180 websites online at the time of data collection. The plots below show the regression line and correlation coefficients of 22+ features extracted and whether the URL is malicious.
If we could plot the lifespan of URLs, we could see that the oldest website has been online since Nov 7th, 2008, while the most recent phishing websites appeared as late as July 10th, 2023.

## Malicious URL Categories
- Defacement
- Malware
- Phishing

## Data Analysis
Here are two images showing the correlation coefficient and correlation of determination between predictor values and the target value `is_malicious`.

![Correlation Coefficient](https://i.imgur.com/LLD3pmt.png)

![Correlation of Determination](https://i.imgur.com/GJM3Cl6.png)

Let's exmain the correlations one by one and cross out any unreasonable or insignificant correlations.

|  Variable                   |   Justification for Crossing Out    |
|-----------------------------|------------------------------------- |
| ~~redirects~~                 |   contracdicts previous research (as redirects increase, is_malicious tends to decrease by a little) |
| ~~not_indexed_by_google~~     |   0.00 correlation |
| ~~email_submission~~          |   contracdicts previous research  |
| request_url_percentage        |                               |
| issuer     |         |
| certificate_age     |         |
| ~~url_anchor_percentage~~     |   contracdicts previous research  |
| ~~meta_percentage~~           |   0.00 correlation  |
| script_percentage             |                       |
| link_percentage               |                       |
| ~~mouseover_changes~~         |   contracdicts previous research  &   0.00 correlation     |
| ~~right_clicked_disabled~~         |   contracdicts previous research   &   0.00 correlation     |
| ~~popup_window_has_text_field~~   |    contracdicts previous research    |
| ~~use_iframe~~   |    contracdicts previous research    |
| ~~has_suspicious_ports~~   |    contracdicts previous research    |
| ~~external_favicons~~   |    contracdicts previous research    |
| TTL (Time to Live)      |       |
| ip_address_count      |       |
| ~~TXT_record~~      |  all websites had a TXT record |
| ~~check_sfh~~      |  contracdicts previous research  |
| count_domain_occurrences   |      |
|   domain_registration_length   |        |
|   abnormal_url   |        |
|   age_of_domain   |        |
|   page_rank_decimal   |        |



## Pre-training Ideas

For training, I split the classification task into two stages in anticipation of the limited availability of online phishing websites due to their short lifespan, as well as the possibility that research done on phishing is not up-to-date:
1. a small multilingual BERT model to output the confidence level of a URL being malicious to model #2, by finetuning on 2,436,727 legitimate and malicious URLs
2. (probably) LightGBM to analyze the confidence level, along with roughly 10 extracted features

This way, I can make the most out of the limited phishing websites avaliable.

## Source of the URLs
- https://moz.com/top500
- https://phishtank.org/phish_search.php?valid=y&active=y&Search=Search
- https://www.kaggle.com/datasets/siddharthkumar25/malicious-and-benign-urls
- https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset
- https://github.com/ESDAUNG/PhishDataset
- https://github.com/JPCERTCC/phishurl-list
- https://github.com/Dogino/Discord-Phishing-URLs

## Reference
- https://www.kaggle.com/datasets/akashkr/phishing-website-dataset
- https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset
- https://www.kaggle.com/datasets/aman9d/phishing-data

## Side notes
- Cloudflare offers an [API for phishing URL scanning](https://developers.cloudflare.com/api/operations/phishing-url-information-get-results-for-a-url-scan), with a generous global rate limit of 1200 requests every 5 minutes.