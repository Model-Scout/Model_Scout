# K-Politician

Korean Politician Facial Image Dataset

Faces are rich sources of information – voters acquire political information from politicians’ faces. However, we do not know which and how politicians’ facial impressions influence voters’ political decision-making.

PoliticGAN is a dataset of K-Politicians built with electoral poster images, annotated with evaluations for facial impressions (competence, dominance, trustworthiness, sex-typicality) via surveys conducted by a research team at Seoul National University (Do Won Kim, Center for Political Communication). We have experimented on StyleGAN2-ADA, GANSpace, and StarGANv2 models to inspect which neural network will be appropriate for generating artificial images with interpretable dimensions of facial cues. This GAN experiment was designed by Haemin Song.

Our final goal is to create a UI application with interpretable dimensions of facial cues, and we expect that researchers could use our generated images with specific target scores of facial cues in future experiments to analyze how specific facial cues influence voting behavior.

Our contributions are twofold. First, PoliticGAN adds racial diversity to existing face datasets, which were previously dominated by Caucasian faces. Second, we use transfer learning to overcome the problem of small datasets and augment our data.

image label	[45,850]
1. Run autocrop to align faces, crop, and standardize images to 256x256 size
2. Run backgroundremover to remove other cues (partisan cues-number and color, texts, etc.)

출처: Kaggle (o0hihan0o/k-politician)
태그: politics, artificial intelligence, image, korea, image classification
라이선스: Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
수정일: 2023-09-28T07:07:59.437Z
