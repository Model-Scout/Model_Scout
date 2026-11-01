---
license: apache-2.0
language:
- ko
task_categories:
- visual-question-answering
---
<img src="https://huggingface.co/datasets/Nagase-Kotono/Image-Detailed-Description-Korean/resolve/1c4f0efbabb642e3ea165640d1b92925a3213956/img/videodler_1719153657068-ezgif.com-video-to-gif-converter.gif">

# Image-Detailed-Description-Korean
[LLaVA-NeXT](https://llava-vl.github.io/blog/2024-05-25-llava-next-ablations/)에 적혀있는 내용중 [High-Quality Knowledge Learning](https://llava-vl.github.io/blog/2024-05-25-llava-next-ablations/#stage-1-5-high-quality-knowledge-learning)부분에 다음의 내용이 있습니다:  
> **Enhanced Performance with Recaptioned Data**  
> - Models trained with recaptioned data (ReCap) datasets, show a trend of enhanced performance in tasks requiring detailed image descriptions and document understanding.  
> - The regenerated captions, ranging from 118K to 3M, demonstrate better scaling behaviors than the original captions, consistently improve model performance across various metrics.  
> - With recap data, full-model training is more effective than projector tuning, because larger model capacity is needed to digest high-quality knowledge.  
> - This approach results in notable improvements in metrics like AI2D, DocVQA, ChartQA, InfoVQA, and ScienceQA.  


이렇게 작성되어 있습니다. 해당 내용을 바탕으로 하여, **claude3.5-sonnet**을 활용해 **Recaptioned Data**를 제작중에 있습니다.  

## 데이터 형식
LLaVA 형식에 맞게 제작되었습니다. 사용법은 LLaVA, KoLLaVA 참고 하시기 바랍니다.  

## 1. OutsideKnowledge  
 - jp1924/OutsideKnowledgebasedMultimodalQAData의 이미지를 기반으로 recaption한 데이터셋입니다.

## 2. llava-ko-recap-120k-CC3M  
- liuhaotian/LLaVA-CC3M-Pretrain-595K의 이미지에서 120k만 recaption한 데이터셋입니다

## License 
**Apache-2.0; and it should abide by the policy of Anthropic: [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms)**