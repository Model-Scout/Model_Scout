# Novel Covid-19 Dataset

Day level Info On Covid-19 affected cases Worldwide

## Context:
From World Health Organization - On 31 December 2019, WHO was alerted to several cases of pneumonia in Wuhan City, Hubei Province of China. The virus did not match any other known virus. This raised concern because when a virus is new, we do not know how it affects people.

So daily level information on the affected people can give some interesting insights when it is made available to the broader data science community.

Johns Hopkins University has made an excellent dashboard using the affected cases data. Data is extracted from the google sheets associated and made available here.

## Edited:
Now data is available as csv files in the Johns Hopkins Github repository. Please refer to the github repository for the Terms of Use details. Uploading it here for using it in Kaggle kernels and getting insights from the broader DS community.

### Content
2019 Novel Coronavirus (2019-nCoV) is a virus (more specifically, a coronavirus) identified as the cause of an outbreak of respiratory illness first detected in Wuhan, China. Early on, many of the patients in the outbreak in Wuhan, China reportedly had some link to a large seafood and animal market, suggesting animal-to-person spread. However, a growing number of patients reportedly have not had exposure to animal markets, indicating person-to-person spread is occurring. At this time, it’s unclear how easily or sustainably this virus is spreading between people - CDC

This dataset has daily level information on the number of affected cases, deaths and recovery from 2019 novel coronavirus. Please note that this is a time series data and so the number of cases on any given day is the cumulative number.

The data is available from 22 Jan, 2020.

Here’s a polished version suitable for a professional Kaggle dataset description:

---

## Dataset Description

This dataset contains time-series and case-level records of the COVID-19 pandemic. The primary file is **`covid_19_data.csv`**, with supporting files for earlier records and individual-level line list data.

### Files and Columns

#### **1. covid\_19\_data.csv (Main File)**

This is the primary dataset and contains aggregated COVID-19 statistics by location and date.

* **Sno** – Serial number of the record
* **ObservationDate** – Date of the observation (MM/DD/YYYY)
* **Province/State** – Province or state of the observation (may be missing for some entries)
* **Country/Region** – Country of the observation
* **Last Update** – Timestamp (UTC) when the record was last updated (not standardized, requires cleaning before use)
* **Confirmed** – Cumulative number of confirmed cases on that date
* **Deaths** – Cumulative number of deaths on that date
* **Recovered** – Cumulative number of recoveries on that date

#### **2. 2019\_ncov\_data.csv (Legacy File)**

This file contains earlier COVID-19 records. It is **no longer updated** and is provided only for historical reference. For current analysis, please use **`covid_19_data.csv`**.

#### **3. COVID\_open\_line\_list\_data.csv**

This file provides **individual-level case information**, obtained from an open data source. It includes patient demographics, travel history, and case outcomes.

#### **4. COVID19\_line\_list\_data.csv**

Another **individual-level case dataset**, also obtained from public sources, with detailed patient-level information useful for micro-level epidemiological analysis.

---

✅ Use **`covid_19_data.csv`** for up-to-date aggregated global trends.

✅ Use the **line list datasets** for detailed, individual-level case analysis.

---
### Country level datasets: 
If you are interested in knowing country level data, please refer to the following Kaggle datasets:

India - https://www.kaggle.com/sudalairajkumar/covid19-in-india

South Korea - https://www.kaggle.com/kimjihoo/coronavirusdataset

Italy - https://www.kaggle.com/sudalairajkumar/covid19-in-italy

Brazil - https://www.kaggle.com/unanimad/corona-virus-brazil

USA - https://www.kaggle.com/sudalairajkumar/covid19-in-usa

Switzerland - https://www.kaggle.com/daenuprobst/covid19-cases-switzerland

Indonesia - https://www.kaggle.com/ardisragen/indonesia-coronavirus-cases


### Acknowledgements :
Johns Hopkins University for making the data available for educational and academic research purposes

MoBS lab - https://www.mobs-lab.org/2019ncov.html

World Health Organization (WHO): https://www.who.int/

DXY.cn. Pneumonia. 2020. http://3g.dxy.cn/newh5/view/pneumonia.

BNO News: https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/

National Health Commission of the People’s Republic of China (NHC):
http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml

China CDC (CCDC): http://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm

Hong Kong Department of Health: https://www.chp.gov.hk/en/features/102465.html

Macau Government: https://www.ssm.gov.mo/portal/

Taiwan CDC: https://sites.google.com/cdc.gov.tw/2019ncov/taiwan?authuser=0

US CDC: https://www.cdc.gov/coronavirus/2019-ncov/index.html

Government of Canada: https://www.canada.ca/en/public-health/services/diseases/coronavirus.html

Australia Government Department of Health: https://www.health.gov.au/news/coronavirus-update-at-a-glance

European Centre for Disease Prevention and Control (ECDC): https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases

Ministry of Health Singapore (MOH): https://www.moh.gov.sg/covid-19

Italy Ministry of Health: http://www.salute.gov.it/nuovocoronavirus

출처: Kaggle (ghost5612/novel-covid-19-dataset)
태그: public health, health, law, data analytics, public safety
라이선스: MIT
수정일: 2025-09-18T06:23:52.250Z
