# Batik Nusantara (Batik Indonesia) Dataset

Batik Nusantara (Batik Indonesia) Dataset images @ a fine resolution of 224x224

## Batik Background
Indonesian textile craftsmanship has evolved over millennia, transitioning from basic utilitarian weaving techniques around 2500 BC to more intricate patterns and religious symbolism and social and culture during the time, with production hubs across regions like Sumatra, Borneo, Java, Celebes, Nusa Tenggara, and Bali. These textiles evolved from utilitarian items to carriers of sacred meanings, divided into secular and sacred cloths, both renowned for their aesthetic beauty. They played a pivotal role in individuals' cultural journeys, symbolizing life stages like maternity, matrimony, and mortality, with designs reflecting religious beliefs and the era's influence.  The **Batik** technique, a hallmark of Indonesian textile artistry, involves creating intricate patterns using a resist wax method. Traditionally, artisans used a tool called a canting to draw patterns on fabric, a process known as batik tulis (drawn batik). Following the drawing phase, the cloth was dyed using natural dyes, and then subjected to the "lorot" process, involving boiling the wax out of the fabric.
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F19051508%2Fe543b4e91ad5dffe2b54e7f4300cc7b2%2F2024-02-16%2015.09.06%20copy%202.jpg?generation=1708074019154098&alt=media)
Batik making is revered for its complexity and demands high craftsmanship, requiring precise hand gestures and mastery of the canting tool. It stands as one of the most challenging pattern-making techniques in textile artistry. [1]

## Dataset Collection
The primary objective of this dataset is to serve as a resource for **research or academic or educational purposes** rather than commercial endeavors. The dataset was meticulously compiled to include high-quality images representative of various types of Batik, encompassing the rich diversity of Batik Nusantara or Indonesian Batik from the Aceh to Papua regions. 

Andrew has mentioned that the cornerstone of effective machine learning lies in the ***quality of the data.*** Meticulously curated datasets hold the power to unlock valuable insights and drive meaningful results. In other words, data is more important than models. In contrast, datasets lacking in quality may hinder the learning process and lead to suboptimal outcomes. Therefore, prioritizing data quality is paramount, as it lays the foundation for successful machine learning initiatives [2]. Also Sebastian added that the ***effectiveness of a machine learning algorithm greatly depends on the quality of the data*** and the richness of the information it encapsulates [3].

## Acknowledgments
This dataset was meticulously carefully collected with the assistance of [Ultralytics](https://github.com/ultralytics). The ownership of all images within this dataset belongs to respective parties, to whom we extend our gratitude for their contribution of these visually captivating images.

### To cite from Kaggle:
[Dataset creator's name]. ([Year & Month of dataset creation]). [Name of the dataset], [Version of the dataset]. Retrieved [Date Retrieved] from [URL of the dataset].

## Dataset
Comprising 40 raw images per class with image dimension of 224 x 224, this dataset encompasses a wide array of Batik designs, each representing a distinct category. The classes include 'Aceh PintuAceh', 'Bali Barong', 'Bali Merak', 'DKI OndelOndel', 'JawaBarat Megamendung', 'JawaTimur Pring', 'Kalimantan Dayak', 'Lampung Gajah', 'Madura Mataketeran', 'Maluku Pala', 'NTB Lumbung', 'Papua Asmat', 'Papua Cendrawasih', 'Papua Tifa', 'Solo Parang', 'SulawesiSelatan Lontara', 'SumateraBarat Rumah Minang', 'SumateraUtara Boraspati', 'Yogyakarta Kawung', and 'Yogyakarta Parang' [2][3][4][5][6][7]. These classes collectively portray the rich heritage of Batik Nusantara or Batik Indonesia, spanning from the Aceh to Papua regions. 
Feel free to explore `image augmentation` techniques to further enhance the dataset.

Simple Coding is available @ [git](https://github.com/hendryhb/kecakbali) with assumption using Colab. ***For reference, the following pre-trained architectures have been added: VGG16, ResNet50, Xception, MobileNetV2, along with Content-Based Image Retrieval (CBIR), Random Forest, a CNN architecture, and modeling, in addition to the MLP. It is also available on Kaggle Dataset Notebooks (Code).***

### Instructions for Dataset Usage
Below are steps to utilise the dataset using either Google Colab or Jupyter Notebook:
1. Begin by downloading the dataset.
2. Upon extraction, you'll find separate folders for `training` and `testing` data. Should you require `validation` data, either manually split a portion (approximately around 20%) from the training set and store it separately, or perform on-the-fly splitting during coding.
3. If splitting validation data manually, remember to re-zip the dataset after the separation process.
4. For Google Colab users, mount the Google Drive to access the dataset. If utilising Jupyter Notebook, this step can be skipped.
5. Proceed with extracting the zipped file and defining constants.
6. Utilise a generator to gather the data, ensuring to incorporate the validation split (as per step 2) if applicable.

### Note:
**raw_batik_v2:** Dataset containing original resolution images.<br>
**raw_batik_v2.1:** Dataset with images resized to 224x224 pixels.

## Bibliography
[1]	K.-C. Langi and S. Park, “An Analysis on Characteristics of Ancient Indonesian Textiles (II) - Focus on the Techniques and the Patterns of the ‘Sacred Cloths’ -,” J. Korean Soc. Costume, vol. 66, no. 7, pp. 34–49, Nov. 2016, doi: 10.7233/jksc.2016.66.7.034.

[2]	A. Ng, "The next 10 years in AI: From bits to things" Venturebeat, [Online]. Available: https://venturebeat.com/ai/andrew-ng-predicts-the-next-10-years-in-ai/. Accessed: January, 2024.

[3]	S. Raschka, V. Mirjalili. Python Machine Learning. Machine Learning and Deep Learning with Python Scikit-Learn and Tensorflow 2, 3rd Edition. PACKT Publishing, 2019.

[4]	A. Wulandari, “Makna Leksikal dan Makna Filosofis Motif-Motif Batik Papua:,” Pros. Semin. Nas. Ind. Kerajinan Dan Batik, vol. 4, no. 1, p. 01 1-9, 2022, Accessed: Feb. 05, 2024. [Online]. Available: https://proceeding.batik.go.id/index.php/SNBK/article/view/155

[5]	D. Saragi, “Pengembangan Tekstil Berbasis Motif dan Nilai Filosofis Ornamen Tradisional Sumatra Utara,” Panggung, vol. 28, Jun. 2018, doi: 10.26742/panggung.v28i2.445.

[6]	H. S. Hadi, M. G. Supiarmo, M. Q. Hidayat, and L. A. A, “Ethnomathematics: Concept of Transformation Geometry in Sasambo Batik Motifs Bale Lumbung Sasak,” J. Pendidik. Mat. Raflesia, vol. 7, no. 1, Art. no. 1, Mar. 2022, doi: 10.33369/jpmr.v7i1.20659.

[7]	L. D. Dwitama, “Kontruksi sosial makna kultural batik betawi (studi kasus :komunitas batik Betawi Teroggong),” bachelorThesis, Jakarta: Fakultas Ilmu Sosial dan Ilmu Politik UIN Syarif Hidayatullah, 2017. Accessed: Nov. 09, 2023. [Online]. Available: https://repository.uinjkt.ac.id/dspace/handle/123456789/43089

[8]	R. Dwi Agustin, “KAJIAN MOTIF BATIK PRING SEDAPUR KARYA NUNUNG WIJAYANTI DI GROBOGAN MENGGUNAKAN KONSEP PENCIPTAAN KRIYA,” Ornamen, vol. 18, no. 1, Jun. 2021, doi: 10.33153/ornamen.v18i1.3662.

[9]	T. P. Siburian, “Bentuk Visual Dan Makna Simbolik Gorga Batak Toba,” J. Contemp. Indones. Art, vol. 8, no. 1, pp. 49–57, Apr. 2022, doi: https://doi.org/10.24821/jocia.v8i1.7047.


<h4><em>If the data card (dataset) and kernels are found helpful, an upvote (▲) would be greatly appreciated.</em></h4>

출처: Kaggle (hendryhb/batik-nusantara-batik-indonesia-dataset)
태그: intermediate, deep learning, image, multiclass classification, image classification
라이선스: CC0: Public Domain
수정일: 2024-02-17T09:43:16.423Z
