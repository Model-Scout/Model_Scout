---
license: apache-2.0
base_model: kakaocorp/kanana-nano-2.1b-instruct
tags:
- gguf
- llama.cpp
- on-device
- diary
- dpo
- kanana
- korean
language:
- ko
pipeline_tag: text-generation
---

# kanana-2.1b-diary-dpo-gguf

**알파리움(Alpharium) 온디바이스 일기 생성 전용 2.1B sLLM (DPO 정렬 Q4_K_M GGUF)**

- **베이스 모델**: [`kakaocorp/kanana-nano-2.1b-instruct`](https://huggingface.co/kakaocorp/kanana-nano-2.1b-instruct)
- **튜닝 기법**: LoRA SFT + DPO (Direct Preference Optimization, EXP-007)
- **양자화 포맷**: GGUF `Q4_K_M` (1154.5 MB, ~1.13 GiB)
- **연구/엔지니어링 저장소**: `terrarium` (알파리움 온디바이스 모델 엔지니어링 연구소)

---

## 1. 모델 개요 및 핵심 특징

본 모델은 모바일 환경(RAM < 2.0GB, 순차 라이프사이클)에서 초고속·고품질의 한국어 감성 일기를 즉각 작성하도록 특화 튜닝된 전용 모델입니다.

1. **상투어 및 틀에 박힌 접속부사 완전 근절 (0.00개)**:
   - '어느덧', '드디어', '결국', '문득' 등 기계적 접속부사 반복을 DPO 선호도 데이터셋 학습을 통해 완전 제거.
2. **단정한 경어체('~요') 종결 일관성 (100.0%)**:
   - 휴대폰 관점 화자('금동이')의 서정적 수필 톤을 유지하며 중간에 비격식체나 해라체로 튀는 현상 방지.
3. **시간대 맥락 일관성 (Temporal Grounding)**:
   - 저녁 사진에 점심 서술을 지어내지 않고, 시간대 앵커에 정합하는 자연스러운 서사 전개.
4. **온디바이스 최적화 분량 (300~380자)**:
   - 군더더기 없이 밀도 높은 7~8문장 분량으로 즉시 수렴하여 불필요한 토큰 낭비 방지.

---

## 2. 모바일 추론 벤치마크 실측치 (EXP-008 기준)

| 항목 | 실측치 | 비고 |
| :--- | :---: | :--- |
| **GGUF 파일 크기** | **1.127 GiB** (1154.5 MB) | 모바일 RAM 2GB 예산 이내 |
| **생성 속도 (TPS)** | **20.8 tokens/sec** | 실시간 온디바이스 생성 |
| **추론 소요 시간** | **평균 4.69초** | 370자 내외 일기 기준 |
| **계약 판정 통과율** | **100.0% (6/6)** | 알파리움 `acceptance.ts` 계약 통과 |
| **엄격 가드레일 통과율** | **100.0% (6/6)** | 분량/어미/시간모순/장면체화 전수 통과 |

---

## 3. 실행 방법 (llama.cpp)

### llama-cli / llama-completion
```bash
llama-completion \
  -m kanana_dpo_q4km.gguf \
  -p "<|im_start|>user\n[HandPrompt V5 템플릿]<|im_end|>\n<|im_start|>assistant\n" \
  --temp 0.8 --top-p 0.95 --repeat-penalty 1.1 -n 512
```

### Python (llama-cpp-python)
```python
from llama_cpp import Llama

llm = Llama(
    model_path="kanana_dpo_q4km.gguf",
    n_ctx=2048,
    n_gpu_layers=99,
)

prompt = """<|im_start|>user
너는 '금동이'라 불리는, 주인의 휴대폰이다. 하루가 끝나면 그날 본 것으로 일기를 쓴다.
오늘 내가 본 것은 이래요.
사진은 한 장이 남았어요. 오후에 찍혔어요.
다녀온 곳은 성수동 카페거리 근처였어요.
오후에 담은 장면: A white coffee cup sits on a saucer with a spoon beside it.

이 기록으로 그 하루의 일기를 써라. 첫 문장은 '오늘 주인이 나에게 보여 준 것은 ~이었어요'처럼 시작하고, 끝까지 '요'로 끝나는 말투로 쓴다.<|im_end|>
<|im_start|>assistant
"""

output = llm(prompt, max_tokens=512, stop=["<|im_end|>"], temperature=0.7)
print(output["choices"][0]["text"])
```

---

## 4. 라이선스

본 모델 가중치는 원본 베이스 모델인 [`kakaocorp/kanana-nano-2.1b-instruct`](https://huggingface.co/kakaocorp/kanana-nano-2.1b-instruct)의 라이선스(Apache-2.0)를 따릅니다.
