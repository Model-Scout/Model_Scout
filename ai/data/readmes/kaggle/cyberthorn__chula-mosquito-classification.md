# 6 Species Mosquito in Thailand for Classification

The microscopy dataset contains 6 species of mosquito and one miscellaneous.

The data availability for "***Enhancement of VGG16 medel with multi-view and spartial dropout for classification of mosquito vectors***" by Department of Parasitology, Center of Excellence in Vector Biology and Vector-Borne Disease, Faculty of Medicine and Department of Electrical Engineering, Chulalongkorn University, Bangkok, Thailand.

The dataset contains six species of mosquito and one miscellaneous species. (Aedes aegypti, Aedes albopictus, Aedes venaxs, Anopheles tessellatus, Culex quinquefasciatus, Culex vishnui and miscellaneous) taken by smart phone camera. Image augmentation using Albumentations libraries.

**Article Source: Enhancement of VGG16 model with multi-view and spatial dropout for classification of mosquito vectors
Pora W, Kasamsumran N, Tharawatcharasart K, Ampol R, Siriyasatien P, et al. (2023) Enhancement of VGG16 model with multi-view and spatial dropout for classification of mosquito vectors. PLOS ONE 18(7): e0284330.**  https://doi.org/10.1371/journal.pone.0284330

**Abstract**
Mosquitoes transmit pathogens that can cause numerous significant infectious diseases in humans and animals such as malaria, dengue fever, chikungunya fever, and encephalitis. Although the VGG16 model is not one of the most advanced CNN networks, it is reported that a fine-tuned VGG16 model achieves accuracy over 90% when applied to the classification of mosquitoes. The present study sets out to improve the accuracy and robustness of the VGG16 network by incorporating spatial dropout layers to regularize the network and by modifying its structure to incorporate multi-view inputs. Herein, four models are implemented: (A) early-combined, (B) middle-combined, (C) late-combined, and (D) ensemble model. Moreover, a structure for combining Models (A), (B), (C), and (D), known as the classifier, is developed. Two image datasets, including a reference dataset of mosquitoes in South Korea and a newly generated dataset of mosquitoes in Thailand, are used to evaluate our models. Regards the reference dataset, the average accuracy of ten runs improved from 83.26% to 99.77%, while the standard deviation decreased from 2.60% to 0.12%. When tested on the new dataset, the classifier’s accuracy was also over 99% with a standard deviation of less than 2%. This indicates that the algorithm achieves high accuracy with low variation and is independent of a particular dataset. To evaluate the robustness of the classifier, it was applied to a small dataset consisting of mosquito images captured under various conditions. Its accuracy dropped to 86.14%, but after retraining with the small dataset, it regained its previous level of precision. This demonstrates that the classifier is resilient to variation in the dataset and can be retrained to adapt to the variation. The classifier and the new mosquito dataset could be utilized to develop an application for efficient and rapid entomological surveillance for the prevention and control of mosquito-borne diseases.

출처: Kaggle (cyberthorn/chula-mosquito-classification)
태그: earth and nature, multiclass classification, image classification, image augmentation
라이선스: Community Data License Agreement - Permissive - Version 1.0
수정일: 2023-04-03T08:32:05.693Z
