# Handwritten Hangul Korean Syllables 손으로 쓴 음절

64 classes, initial 100 samples per class, augmented 2000 samples per class.

Hangul Database contains 64 of the most common hangul syllables as jpg images with 100 samples per each syllable, according to the syllable frequency analysis from professor 강승식 [http://nlp.kookmin.ac.kr](url) (site in korean), along with some common korean surnames (최, 김, 박, 강). They were all written with some style variation by myself using GIMP image editor. Hangul Database Extended was made using 20 random image distorsions made with python albumentations image processing library. It contains 64 * 100 * 20 = 128000 samples. The classes consist of the Revised Romanization [https://en.wikipedia.org/wiki/Revised_Romanization_of_Korean](url) of the character, and the files use the unicode character. In the extended directory, both the classes and the individual files use RR. 

The cover image is an excerpt from 훈민정음, the first document written in hangul alphabet.

출처: Kaggle (jkim289/handwritten-korean-characters)
태그: arts and entertainment, categorical, linguistics, image classification, english, korean
라이선스: Database: Open Database, Contents: © Original Authors
수정일: 2024-12-05T01:26:27.827Z
