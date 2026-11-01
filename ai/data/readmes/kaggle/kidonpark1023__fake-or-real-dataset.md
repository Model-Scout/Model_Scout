# Fake or Real Competition Dataset

2023 fake or real image discrimination competition dataset

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3032492%2Ff4201da2a12cae17fed7a8f5a242c78e%2F2023-07-12%20%208.33.10.png?generation=1689161628737196&alt=media)

2023 Fake or Real: AI-generated Image Discrimination Competition dataset is now available on Kaggle!
---


Hello, Kagglers🖐️

We are excited to announce the release of the dataset for the 2023 Fake or Real: AI-generated Image Discrimination Competition. The competition was held on AI CONNECT(https://aiconnect.kr/) from June 26th to July 6th, 2023, with 768 participants.

If you're interested in evaluating the performance of your model on the test dataset, we encourage you to visit the [competition page](https://aiconnect.kr/competition/detail/227/task/295/taskInfo) on AI CONNECT and submit your results. Please note that it supports only Korean yet. Of course we data scientists can always use Chrome translate, and/or even better translation models🥳. Plus, multilingual service will be provided in the (hopefully near) future, so please stay tuned!


# Background
As the advancement of generative AI technology has enabled the easy creation of indistinguishable fake information from genuine content, concerns regarding its misuse have surfaced. Image generation AI, in particular, has raised significant alarm due to its potential risks such as identity theft, revenge porn, and political manipulation. In response, it has become imperative to develop technologies that can effectively discern between real and AI-generated fake images.

The training dataset consists of diffusiondb (https://huggingface.co/datasets/poloclub/diffusiondb) and Flickr images, with the inclusion of some low-quality fake images. For the test dataset, we took measures to construct it in a manner that closely resembles real-world scenarios involving image misuse. We utilized multiple generative AI models, fine-tuned on diverse photorealistic datasets, and applied negative prompt keywords like 'cartoon' and 'too many fingers' to generate realistic images.

We hope this dataset encourages the development of robust solutions and stimulates discussions on tackling the challenges associated with AI-generated fake images. 

Best Regards,
AI CONNECT

출처: Kaggle (kidonpark1023/fake-or-real-dataset)
태그: computer science, classification, image
라이선스: CC0: Public Domain
수정일: 2023-07-12T09:38:14.650Z
