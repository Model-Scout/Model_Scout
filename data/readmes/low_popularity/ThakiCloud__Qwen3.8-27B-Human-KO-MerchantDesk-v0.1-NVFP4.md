---
license: apache-2.0
base_model: ThakiCloud/Qwen3.8-27B-Human-KO-MerchantDesk-v0.1
language:
- ko
pipeline_tag: text-generation
tags:
- korean
- customer-service
- small-business
- nvfp4
- compressed-tensors
- blackwell
- qwen
---

# Qwen3.8-27B-Human-KO-MerchantDesk-v0.1-NVFP4

**우리나라 소상공인 사장님들을 위해 만든 모델**의 4비트(NVFP4) 서빙판입니다. 원본은 [`ThakiCloud/Qwen3.8-27B-Human-KO-MerchantDesk-v0.1`](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Human-KO-MerchantDesk-v0.1)이고, 모델이 하는 일·사용법·주의사항은 원본 카드와 같습니다. 가중치가 약 55.6GB에서 약 22GB로 줄어 Blackwell(B200 등) GPU 한 장에서 넉넉히 서빙됩니다.

## 양자화

llm-compressor GPTQ, NVFP4 가중치·활성, 어텐션 계열(self_attn·linear_attn)은 FP8, 일반 텍스트 교정 1,024개 × 2,048 토큰. `compressed-tensors`(mixed-precision) 형식이라 vLLM 에서 그대로 읽힙니다. 교정 데이터에는 매장 응대 데이터를 쓰지 않았습니다.

## 결과 (규칙 컴파일러 적용, 프롬프트 v1.2)

| 지표 | 기준 모델 | BF16 원본 | 이 모델 (NVFP4) |
|---|---|---|---|
| 해결률, IID 6,000건 | 0.609 | 0.708 | **0.700** |
| 해결률, Hard 600건 | 0.473 | 0.557 | **0.550** |
| 근거 없는 사실 | 0 | 0 | **0** |

기준 모델보다 IID 에서 +9.1%p(8.1 ~ 10.1), Hard 에서 +7.7%p(3.7 ~ 11.9) 높습니다. BF16 원본과 비교하면 IID 에서 0.9%p 낮고(구간 −1.4 ~ −0.4) Hard 에서는 차이가 구간 안입니다(−0.7%p, −2.2 ~ +0.9). 다만 BF16 원본은 H200, 이 모델은 B200 에서 쟀기 때문에 이 차이에는 하드웨어 차이가 섞여 있습니다. 같은 B200 에서 교정 400건으로 나란히 잰 결과는 BF16 0.698, NVFP4 0.713 이었습니다.

⚠️ 원본과 마찬가지로 **모델이 직접 쓴 문장을 고객에게 그대로 보내지 마세요.** 의도와 슬롯만 받아 쓰고, 문장은 매장 프로필 값으로 채우는 코드로 만드는 것을 전제로 한 수치입니다.

일반 능력·안전 표는 원본(BF16) 카드에 있습니다.

## 서빙

vLLM 0.28 에서 `--max-model-len 8192`, greedy, `chat_template_kwargs={"enable_thinking": false}` 로 평가했습니다. NVFP4 네이티브 커널은 Blackwell 세대에서 동작합니다.

## 출처

이 모델은 과학기술정보통신부의 재원으로 한국지능정보사회진흥원의 지원을 받아 구축된 AI 허브(https://aihub.or.kr) 데이터 「소상공인 고객 주문 질의-응답 텍스트」를 학습에 활용했습니다. 이 저장소에는 원본 데이터나 그 가공본이 들어 있지 않습니다.
