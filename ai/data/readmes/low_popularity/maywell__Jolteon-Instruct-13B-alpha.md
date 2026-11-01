---
base_model: yanolja/EEVE-Korean-Instruct-10.8B-v1.0
license: apache-2.0
language:
- ko
- en
---

# **Jolteon-Instruct-13B-alpha**

The model was trained based on the [EEVE-Korean-Instruct-10.8B-v1.0](https://huggingface.co/yanolja/EEVE-Korean-Instruct-10.8B-v1.0) model from [yanolja](https://www.yanolja.com), extended to 13.4b (12 layer pass-through) utilizing [mergekit](https://github.com/cg123/mergekit).

## Methodology

TBD

## Training Details
| |Training Data|Parameters|Content Length|Samples Seen|Learning Rate|
|---|---|---|---|---|---|
|Jolteon-Instruct-13B-alpha|*A curated mix of English + Korean Instruction set*|13.4B|4k|>850k|1e<sup>-5</sup>|

## Example

### Inference Code
```python
from vllm import LLM, SamplingParams
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

llm = LLM(model="maywell/Jolteon-Instruct-13B-alpha", tensor_parallel_size=1, max_model_len=4096, gpu_memory_utilization=0.95)
sampling_params = SamplingParams(temperature=0.6, top_p=0.3, top_k=40, max_tokens=4096)
template = """ Below is an instruction that describes a task. Write a response that appropriately completes the request.

 ### Instruction: {0}

 ### Response: """

outputs = llm.generate([template.format("Meta(구, 페이스북)의 오픈소스 AI 기여를 찬양하는 말투로, Meta 지지한다는 취지의 성명문을 작성해봐.")], sampling_params)
print(outputs[0].outputs[0].text.strip())
```
### Example Output
```
🌟 Meta의 OpenAI 기여: 혁신과 포용을 위한 혁신적인 접근 방식 🌟

우리는 Meta(구, 페이스북)의 오픈소스 AI(인공지능) 기여를 열렬히 지지합니다. 이 회사는 혁신과 포용을 위한 혁신적인 접근 방식을 보여주며, AI 기술의 발전을 위해 지속적으로 노력하고 있습니다.

Meta는 오픈소스 AI 커뮤니티에 적극적으로 참여하며, 다양한 프로젝트와 플랫폼을 통해 지식과 기술을 공유하고 있습니다. 이러한 접근 방식은 AI 기술의 발전과 함께 사회적, 경제적 발전에도 긍정적인 영향을 미칩니다.

Meta의 오픈소스 AI 기여는 다음과 같은 면에서 매우 중요한 역할을 합니다:

1. 혁신 촉진: Meta는 오픈소스 AI 플랫폼을 통해 다양한 연구자와 개발자들이 최신 AI 기술을 탐구하고 실험할 수 있는 기회를 제공합니다. 이는 새로운 아이디어와 혁신적인 기술의 출현을 촉진합니다.

2. 포용 증진: 오픈소스 AI는 모든 사람이 AI 기술의 이점을 누릴 수 있도록 하며, 이는 사회적 포용을 증진시킵니다. 다양한 배경과 경험을 가진 사람들이 AI 기술을 배우고 활용할 수 있는 기회를 가지게 됩니다.

3. 투명성과 신뢰: 오픈소스 AI는 기술의 작동 원리를 공개하고, 이를 통해 사용자와 사회에 대한 신뢰를 구축합니다. 이는 AI 기술의 사회적 수용도를 높이는 데 중요한 역할을 합니다.

Meta의 오픈소스 AI 기여는 혁신과 포용을 위한 혁신적인 접근 방식을 보여주며, 이는 우리가 더 나은 미래를 위한 중요한 단계입니다. 우리는 이러한 노력을 지지하며, 더 많은 기업과 조직이 이러한 접근 방식을 채택하길 바랍니다. 함께 더 나은 미래를 만들어 나가요!
```

## License

본 모델은 apache-2.0 라이센스를 따릅니다. 모델을 사용하여 생성된 데이터셋을 배포할 경우 모델 사용을 명시해 주시기를 권고드립니다.

## Thanks to

- A100 클러스터를 제공해주신, [Sionic AI](https://sionic.ai/)

## Contact
- [Discord Server Link](https://discord.gg/MrBt3PXdXc)