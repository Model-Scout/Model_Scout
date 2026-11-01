---
language:
- ko
license: apache-2.0
size_categories:
- 10K<n<100K
task_categories:
- visual-question-answering
- image-text-to-text
pretty_name: LLaVA-CoT
viewer: false
tags:
- reasoning
- multimodal
- VLM
- chain-of-thought
---

This dataset is the Korean version of the LLaVA-CoT-100k dataset, which was introduced in the paper [LLaVA-CoT: Let Vision Language Models Reason Step-by-Step](https://huggingface.co/papers/2411.10440).

**Abstract:**
Large language models have demonstrated substantial advancements in reasoning capabilities. However, current Vision-Language Models (VLMs) often struggle to perform systematic and structured reasoning, especially when handling complex visual question-answering tasks. In this work, we introduce LLaVA-CoT, a large VLM designed to conduct autonomous multistage reasoning. Unlike chain-of-thought prompting, LLaVA-CoT independently engages in sequential stages of summarization, visual interpretation, logical reasoning, and conclusion generation. This structured approach enables LLaVA-CoT to achieve marked improvements on reasoning-intensive tasks. To accomplish this, we construct the LLaVA-CoT-100k dataset, integrating samples from various visual question answering sources and providing structured reasoning annotations. Besides, we propose a test-time stage-wise retracing search method (SWIRES), which enables effective and efficient test-time scaling. Remarkably, with only 100k training samples and test-time scaling, LLaVA-CoT not only outperforms its base model by 9.4% on a wide range of multimodal reasoning benchmarks, but also surpasses the performance of larger and even closed-source models, such as Gemini-1.5-pro, GPT-4o-mini, and Llama-3.2-90B-Vision-Instruct. The code, dataset, and pre-trained weights are publicly available at this https URL .

**Code:** [GitHub Repository](https://github.com/PKU-YuanGroup/LLaVA-CoT)

---

![img](https://huggingface.co/datasets/Nagase-Kotono/Image-Detailed-Description-Korean/resolve/1c4f0efbabb642e3ea165640d1b92925a3213956/img/videodler_1719153657068-ezgif.com-video-to-gif-converter.gif)
# LLaVA-CoT-ko

## 개요
**[Xkev/LLaVA-CoT-100k](https://huggingface.co/datasets/Xkev/LLaVA-CoT-100k)** paper에 적힌대로 비슷하게 한국어로 만든 데이터셋입니다.  
자세한 내용은 이쪽에서 확인 부탁드립니다.  
- **[LLaVA-CoT: Let Vision Language Models Reason Step-by-Step](https://huggingface.co/papers/2411.10440)**

## 1. img-1.zip
한국어 차트 이미지-텍스트 멀티런 데이터셋입니다... 대충 이미지 18k 정도 입니다...

<details>
<summary>**img-1.zip 데이터 예시**</summary>

![img](https://cdn-uploads.huggingface.co/production/uploads/641b25e91911d3be6743e143/SltV3sWgroy3m2itHmPWo.png)
```json
{
    "id": "1c7f169e-f759-5182-8355-a287a5a15e00",
    "image": "image_folder_1-82.jpg",
    "conversations": [
        {
            "from": "human",
            "value": "<image>
2022년 소비생활 만족도 비율은 몇 퍼센트인가요?"
        },
        {
            "from": "gpt",
            "value": "<SUMMARY>이 질문은 2022년 '만족' 비율을 묻는 간단한 사실 확인 질문입니다. 그래프에서 해당 막대의 수치를 직접 읽어 답변합니다.</SUMMARY>

<CAPTION>이 그래프는 2020년부터 2022년까지 대전 시민의 소비생활 만족도를 나타냅니다. 각 연도별로 '만족', '보통', '불만족'의 비율이 수치와 함께 막대 그래프로 표시되어 있습니다. 2022년의 '만족' 비율은 파란색 막대로 가장 왼쪽에 위치합니다.</CAPTION>

<REASONING>
1. [관찰/식별]
   - 2022년 막대에서 '만족'에 해당하는 파란색 부분을 찾습니다.
   - 해당 막대에 표시된 수치는 '32.9'입니다.
2. [상세 분석]
   - 그래프 범례에서 파란색은 '만족'을 의미합니다.
   - 따라서 2022년 소비생활 '만족' 비율은 32.9%임을 확인했습니다.
3. [심화 추론/연결]
   - (단순 사실 확인 질문이므로 심화 추론은 불필요)
4. [결론 도출]
   - 2022년 소비생활 만족도 비율은 32.9%입니다.
</REASONING>

<CONCLUSION>2022년 대전 시민의 소비생활 만족도 비율은 32.9%입니다.</CONCLUSION>"
        },
        {
            "from": "human",
            "value": "2020년부터 2022년까지 소비생활 만족도 비율은 어떻게 변화했나요?"
        },
        {
            "from": "gpt",
            "value": "<SUMMARY>이 질문은 2020년부터 2022년까지 '만족' 비율의 변화 추이를 분석하는 질문입니다. 각 연도별 '만족' 비율을 비교하여 변화 양상을 설명합니다.</SUMMARY>

<CAPTION>이 그래프는 3개년도(2020년, 2021년, 2022년)에 걸쳐 대전 시민의 소비생활 만족도를 보여줍니다. '만족'은 파란색, '보통'은 회색, '불만족'은 주황색으로 표시됩니다. 각 연도별 '만족' 비율을 비교하면 변화 추이를 파악할 수 있습니다.</CAPTION>

<REASONING>
1. [관찰/식별]
   - 2020년, 2021년, 2022년 각 연도의 '만족' 비율을 확인합니다.
   - 2020년: 17.4%, 2021년: 25.8%, 2022년: 32.9%
2. [상세 분석]
   - 2020년부터 2021년까지 만족도 비율이 17.4%에서 25.8%로 증가했습니다.
   - 2021년부터 2022년까지 만족도 비율이 25.8%에서 32.9%로 더욱 증가했습니다.
   - 전반적으로 2020년부터 2022년까지 만족도 비율은 꾸준히 증가하는 추세입니다.
3. [심화 추론/연결]
   - (분석 질문이므로 심화 추론은 불필요)
4. [결론 도출]
   - 2020년부터 2022년까지 대전 시민의 소비생활 만족도 비율은 지속적으로 증가했습니다.
</REASONING>

<CONCLUSION>2020년부터 2022년까지 대전 시민의 소비생활 만족도 비율은 꾸준히 증가하는 경향을 보입니다.</CONCLUSION>"
        },
        {
            "from": "human",
            "value": "2021년에서 2022년 사이 소비생활 만족도 비율이 크게 상승한 이유는 무엇이라고 추측할 수 있나요? 당시 경제 상황과 연관지어 설명해주세요."
        },
        {
            "from": "gpt",
            "value": "<SUMMARY>이 질문은 2021년에서 2022년 사이 '만족' 비율의 급격한 상승 원인을 묻는 전문가 수준의 심화 질문입니다. 당시 경제 상황과 소비 심리 변화를 추론하여 답변합니다.</SUMMARY>

<CAPTION>그래프에서 2021년 대비 2022년에 '만족' 비율이 크게 상승한 것을 확인할 수 있습니다. 2021년 '만족' 비율은 25.8%였으나, 2022년에는 32.9%로 증가했습니다. 이는 7.1%p의 상승폭입니다.</CAPTION>

<REASONING>
1. [관찰/식별]
   - 2021년 '만족' 비율은 25.8%, 2022년 '만족' 비율은 32.9%입니다.
   - 2021년에서 2022년 사이 '만족' 비율이 뚜렷하게 상승했습니다.
2. [상세 분석]
   - 2020년에서 2021년 사이 '만족' 비율 상승폭(25.8% - 17.4% = 8.4%p)과 유사하게 2021년에서 2022년 사이에도 높은 상승폭을 보입니다.
   - '보통' 비율은 2021년에서 2022년 사이 감소(57.6% → 52.4%)했으며, '불만족' 비율 또한 소폭 감소(16.6% → 14.7%)했습니다. 이는 '보통' 및 '불만족'에서 '만족'으로 이동한 인구가 증가했음을 시사합니다.
3. [심화 추론/연결]
   - 2021년에서 2022년은 코로나19 팬데믹의 영향이 점차 완화되고, 경제 활동이 재개되는 시점이었습니다. 백신 접종 확대 및 사회적 거리두기 완화 정책으로 소비 심리가 회복되었을 가능성이 높습니다.
   - 2022년에는 정부의 소비 촉진 정책(예: 소비 쿠폰 발행, 긴급재난지원금 지급 등)이 시행되었을 수 있으며, 이는 가계의 가처분 소득 증가 및 소비 여력 확대로 이어져 소비 만족도 상승에 기여했을 수 있습니다.
   - 다만, 2022년 하반기부터는 러시아-우크라이나 전쟁 발발 및 글로벌 공급망 불안정으로 인해 인플레이션 우려가 커지기 시작했습니다. 하지만 해당 조사는 2022년 '현재' 소비생활 만족도를 묻고 있으므로, 2022년 상반기 또는 그 이전 시점의 소비 심리 회복세가 반영되었을 가능성이 더 높습니다.
   - 또한, 대전 지역 경제 특성(예: 연구 개발 중심 도시, 안정적인 공공 부문 일자리 비중 등)이 다른 지역에 비해 경제 변동에 덜 민감하게 작용했을 가능성도 고려해볼 수 있습니다.
4. [결론 도출]
   - 2021년에서 2022년 사이 소비생활 만족도 비율의 증가는 코로나19 팬데믹 완화에 따른 소비 심리 회복, 정부의 소비 촉진 정책, 그리고 대전 지역 경제의 상대적 안정성 등이 복합적으로 작용한 결과로 추측됩니다.
</REASONING>

<CONCLUSION>2021년에서 2022년 사이 대전 시민의 소비생활 만족도 비율이 크게 상승한 것은 코로나19 팬데믹 상황 완화와 함께 소비 심리가 회복되고, 정부의 소비 촉진 정책 등이 시행되면서 나타난 현상으로 추측됩니다. 또한 대전 지역 경제의 특성 또한 긍정적인 영향을 미쳤을 가능성이 있습니다.</CONCLUSION>"
        }
    ]
},...
```
### 입력

> **2021년에서 2022년 사이 소비생활 만족도 비율이 크게 상승한 이유는 무엇이라고 추측할 수 있나요? 당시 경제 상황과 연관지어 설명해주세요.**
### 출력
> **\<SUMMARY>이 질문은 2021년에서 2022년 사이 '만족' 비율의 급격한 상승 원인을 묻는 전문가 수준의 심화 질문입니다. 당시 경제 상황과 소비 심리 변화를 추론하여 답변합니다.\</SUMMARY>**  
>  
> **\<CAPTION>그래프에서 2021년 대비 2022년에 '만족' 비율이 크게 상승한 것을 확인할 수 있습니다. 2021년 '만족' 비율은 25.8%였으나, 2022년에는 32.9%로 증가했습니다. 이는 7.1%p의 상승폭입니다.\</CAPTION>**  
>  
> **\<REASONING>**  
> **1. [관찰/식별]**  
> - 2021년 '만족' 비율은 25.8%, 2022년 '만족' 비율은 32.9%입니다.  
> - 2021년에서 2022년 사이 '만족' 비율이 뚜렷하게 상승했습니다.  
>  
> **2. [상세 분석]**  
> - 2020년에서 2021년 사이 '만족' 비율 상승폭(25.8% - 17.4% = 8.4%p)과 유사하게 2021년에서 2022년 사이에도 높은 상승폭을 보입니다.  
> - '보통' 비율은 2021년에서 2022년 사이 감소(57.6% → 52.4%)했으며, '불만족' 비율 또한 소폭 감소(16.6% → 14.7%)했습니다.  
> - 이는 '보통' 및 '불만족'에서 '만족'으로 이동한 인구가 증가했음을 시사합니다.  
>  
> **3. [심화 추론/연결]**  
> - 2021년에서 2022년은 코로나19 팬데믹의 영향이 점차 완화되고, 경제 활동이 재개되는 시점이었습니다.  
> - 백신 접종 확대 및 사회적 거리두기 완화 정책으로 소비 심리가 회복되었을 가능성이 높습니다.  
> - 2022년에는 정부의 소비 촉진 정책(예: 소비 쿠폰 발행, 긴급재난지원금 지급 등)이 시행되었을 수 있으며, 이는 가계의 가처분 소득 증가 및 소비 여력 확대로 이어져 소비 만족도 상승에 기여했을 수 있습니다.  
> - 다만, 2022년 하반기부터는 러시아-우크라이나 전쟁 발발 및 글로벌 공급망 불안정으로 인해 인플레이션 우려가 커지기 시작했습니다.  
> - 하지만 해당 조사는 2022년 '현재' 소비생활 만족도를 묻고 있으므로, 2022년 상반기 또는 그 이전 시점의 소비 심리 회복세가 반영되었을 가능성이 더 높습니다.  
> - 또한, 대전 지역 경제 특성(예: 연구 개발 중심 도시, 안정적인 공공 부문 일자리 비중 등)이 다른 지역에 비해 경제 변동에 덜 민감하게 작용했을 가능성도 고려해볼 수 있습니다.  
>  
> **4. [결론 도출]**  
> - 2021년에서 2022년 사이 소비생활 만족도 비율의 증가는 코로나19 팬데믹 완화에 따른 소비 심리 회복, 정부의 소비 촉진 정책, 그리고 대전 지역 경제의 상대적 안정성 등이 복합적으로 작용한 결과로 추측됩니다.  
>  
> **\</REASONING>**  
>  
> **\<CONCLUSION>2021년에서 2022년 사이 대전 시민의 소비생활 만족도 비율이 크게 상승한 것은 코로나19 팬데믹 상황 완화와 함께 소비 심리가 회복되고, 정부의 소비 촉진 정책 등이 시행되면서 나타난 현상으로 추측됩니다. 또한 대전 지역 경제의 특성 또한 긍정적인 영향을 미쳤을 가능성이 있습니다.\</CONCLUSION>**

</details>