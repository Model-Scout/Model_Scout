# Novel COVID-19 Chestxray Repository

a public chestxray dataset

##_Authors of the Dataset_:
- Pratik Bhowal (B.E., Dept of Electronics and Instrumentation Engineering, Jadavpur University Kolkata, India) [[LinkedIn]](https://www.linkedin.com/in/pratik-bhowal-1066aa198?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B%2BqgwqwxJRIep5K454MTQ6w%3D%3D), [[Github]](https://github.com/prat1999)
- Subhankar Sen (B.Tech, Dept of Computer Science Engineering, Manipal University Jaipur, India) [[LinkedIn]](https://www.linkedin.com/in/subhankar-sen-a62457190lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BP2gUaNhAT0uL2etYJDiGqw%3D%3D), [[Github]](https://github.com/subhankar01), [[Google Scholar]](https://scholar.google.com/citations?user=MSXb0xoAAAAJ&hl=en)
- Jin Hee Yoon (faculty of the Dept. of Mathematics and Statistics at Sejong University, Seoul, South Korea) [[LinkedIn]](https://www.linkedin.com/in/jin-hee-yoon-2418a069), [[Google Scholar]](https://scholar.google.com/citations?user=Rq_TQc0AAAAJ&hl=en)
- Zong Woo Geem (faculty of College of IT Convergence at Gachon University, South Korea) [[LinkedIn]](https://www.linkedin.com/in/zong-woo-geem-66273113), [[Google Scholar]](https://scholar.google.com/citations?hl=en&user=Je3-B2YAAAAJ)
- Ram Sarkar( Professor at Dept. of Computer Science Engineering, Jadavpur Univeristy Kolkata, India) [[LinkedIn]](https://www.linkedin.com/in/ram-sarkar-0ba8a758?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BvwKX%2Frm5RNSySsSaIQTiVQ%3D%3D), [[Google Scholar]](https://scholar.google.com/citations?hl=en&user=bDj0BUEAAAAJ&view_op=list_works&citft=1&citft=2&citft=3&email_for_op=subhankarsen2001%40gmail.com&gmla=AJsN-F5CKj5MB0jIcLJssFUKVVcxdf5jt8CBMbzSZf6W9RJvYUYp61X3OC6sXa_lzg1FHW7A8BpuLWwkMtDLWxJje2eowsNWqllMazckf90f5PsxhFZ2D1PcmhyhjJ8OT5q2-3Pc3DcwNuIj4E0s2LfWgQVOZBVVGs76xTjTPWNSKVvqBhvA-u05tkPXamKiItj8RSd_vApWN6jtmvYA9JcJ4ObPprLRFPV10T5a0A4nmrQVxyniapy6XIgng1L8D1qTtb2oFAow)

## Journal Paper
If you are using this dataset for your research papers and find it useful for your publications, please consider citing:
```
@article{bhowal2021choquet,
  title={Choquet Integral and Coalition Game-based Ensemble of Deep Learning Models for COVID-19 Screening from Chest X-ray Images},
  author={Bhowal, Pratik and Sen, Subhankar and Yoon, Jin Hee and Geem, Zong Woo and Sarkar, Ram},
  journal={IEEE Journal of Biomedical and Health Informatics},
  year={2021},
  publisher={IEEE}
}
  ```

##Overview
The authors have created a new dataset known as Novel COVID-19 Chestxray Repository by the fusion of publicly available chest-xray image repositories. In creating this combined dataset, three different datasets obtained from the Github and Kaggle databases,created by the authors of other research studies in this field, were utilized.In our study,frontal and lateral chest X-ray images are used since this view of radiography is widely used by radiologist in clinical diagnosis.In the following section, authors have summarized how this dataset is created.

- [COVID-19 Radiography Database](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database): The first release of this dataset reports 219 COVID-19,1345 viral pneumonia and 1341 normal radiographic chest X-ray images. This dataset was created by a team of researchers from Qatar University, Doha, Qatar, and the University of Dhaka, Bangladesh in collaboration with medical doctors and specialists from Pakistan and Malaysia.This database is regularly updated with the emergence of new cases of COVID-19 patients worldwide.Related Paper:https://arxiv.org/abs/2003.13145

- [COVID-Chestxray set](https://github.com/ieee8023/covid-chestxray-dataset):Joseph Paul Cohen and Paul Morrison and Lan Dao have created a public image repository on Github  which consists both CT scans and digital chest x-rays.The data was collected mainly from retrospective cohorts of pediatric patients from Guangzhou Women and Children’s medical center.With the aid of metadata information provided along with the dataset,we were able to extract 521 COVID-19 positive,239 viral and bacterial pneumonias;which are of the following three broad categories:Middle East Respiratory Syndrome (MERS),Severe Acute Respiratory Syndrome (SARS), and Acute Respiratory Distress syndrome (ARDS);and 218 normal radiographic chest X-ray images of varying image resolutions. Related Paper: https://arxiv.org/abs/2006.11988

- [Actualmed COVID chestxray dataset](https://github.com/agchung/Actualmed-COVID-chestxray-dataset):Actualmed-COVID-chestxray-dataset comprises of 12 COVID-19 positive and 80 normal radiographic chest x-ray images.

The combined dataset includes chest X-ray images of COVID-19,Pneumonia and Normal (healthy) classes, with a total of 752, 1584, and 1639 images respectively. Information about the  Novel  COVID-19  Chestxray  Database and its parent image repositories is provided in [Table 1](#tab1).

### Table 1: Dataset Description

| Dataset| COVID-19 |Pneumonia | Normal |
| ------------- | ------------- | ------------- | -------------|
| [COVID Chestxray set](https://github.com/ieee8023/covid-chestxray-dataset) | 521 |239|218|
| [COVID-19 Radiography Database(first release)](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database) | 219 |1345|1341|
| [Actualmed COVID chestxray dataset](https://github.com/agchung/Actualmed-COVID-chestxray-dataset)| 12 |0|80|
| **Total**|**752**|**1584**|**1639**|

DATA ACCESS AND USE: Academic/Non-Commercial Use

출처: Kaggle (subhankarsen/novel-covid19-chestxray-repository)
태그: universities and colleges, literature, health, classification, image, covid19
라이선스: Database: Open Database, Contents: Database Contents
수정일: 2021-07-07T08:58:21.587Z
