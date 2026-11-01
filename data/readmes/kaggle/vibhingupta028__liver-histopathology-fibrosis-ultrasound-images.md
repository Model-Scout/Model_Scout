# Liver Histopathology (Fibrosis) Ultrasound Images

High-Resolution Ultrasound Images for Classifying Liver Fibrosis Stages

Ultrasound (US) images, which can be obtained without harmful radiation being applied to the human body, are mainly used in the medical field. In abdominal radiology, US images are most used in the continuous observation of patients with liver cirrhosis or chronic hepatitis to detect hepatocellular carcinoma and evaluate the degree of liver fibrosis.

US images are taken using the reflected wave of a sound wave pulse. Unlike superficial organs, such as the breasts and thyroid gland, the liver is located deep inside the human body. Therefore, during the process of transmitting and receiving signals inside the human body, which has numerous obstacles, the signals are weakened and the probability of exposure to various noises increases. 

**Dataset Description:**
This dataset is derived from the research conducted by *Y. Joo, H. -C. Park, O. -J. Lee, C. Yoon, M. H. Choi, and C. Choi, titled "Classification of Liver Fibrosis From Heterogeneous Ultrasound Image," published in IEEE Access, vol. 11, pp. 9920-9930, 2023*. The dataset includes ultrasound (US) images obtained from a tertiary university hospital (Seoul St. Mary’s Hospital) used for training and validation purposes. Data from another university hospital (Eunpyeong St. Mary’s Hospital) were utilized for testing. 

In general, F0 and F4 are easily obtained, and they account for more than half of the dataset. Class F4, which represents significantly advanced liver cirrhosis, accounted for 27% of the dataset. However, the distributions of F1, F2, and F3 were relatively low because only a small number of patients were tested in the early stages of cirrhosis. The proportions of F1, F2, and F3 in our dataset are each 13%.


**What is Liver Fibrosis?**
A condition where liver tissue becomes scarred due to prolonged inflammation or damage, affecting liver function and potentially leading to severe complications if untreated.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F22008125%2F76cf81716a93feb41855064a570e2bc0%2F1.jpeg?generation=1723052923988251&alt=media)

**Image Format:** JPG files
**Categories:** 5 stages of liver fibrosis


**Class Breakdown:**

F0 - No Fibrosis: 2114 images
Description: Represents healthy liver tissue with no signs of fibrosis. The tissue appears normal, with no scarring or fibrosis present.

F1 - Portal Fibrosis: 861 images
Description: Indicates fibrosis occurring around portal areas of the liver. Portal fibrosis involves the formation of scar tissue around the portal veins, which are small blood vessels in the liver.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F22008125%2Ff95b4266098940465d66cd123294d9f6%2F5-Figure1-1.png?generation=1723052991794689&alt=media)

F2 - Periportal Fibrosis: 793 images
Description: Shows fibrosis around the edges of the liver's portal areas. Periportal fibrosis is characterized by scarring around the liver's boundary regions, often affecting the areas near the portal veins.

F3 - Septal Fibrosis: 857 images
Description: Features fibrosis that forms bands or septa throughout the liver tissue. Septal fibrosis involves the development of thickened scar tissue that creates bands or partitions within the liver.

F4 - Cirrhosis: 1698 images
Description: Represents advanced fibrosis leading to cirrhosis. Cirrhosis is the most severe stage, marked by extensive scarring and loss of liver function, which can significantly impact liver health.

출처: Kaggle (vibhingupta028/liver-histopathology-fibrosis-ultrasound-images)
태그: health conditions
라이선스: CC BY-SA 4.0
수정일: 2024-08-27T08:08:32.760Z
