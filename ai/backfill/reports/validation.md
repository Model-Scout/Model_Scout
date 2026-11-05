# 델타 검증

`gguf.total`을 네 가지로 검증하고 신뢰도를 조정했다. 값을 지어내지 않고 등급만 내렸다.

| 검사 | 수 |
|---|---:|
| 검증 대상 (parameter_count 패치) | 1278 |
| ✅ 원본 파라미터와 5% 이내 일치 | 427 |
| ⚠️ 원본과 불일치 | 83 |
| ⚠️ mmproj 있음 (VL, 비전 인코더 제외) | 238 |
| ⚠️ MoE 신호 | 120 |
| └ 파일 크기로 전체 파라미터 확인됨 | 88 |
| ⚠️ 파일 크기 불일치 | 27 |

| 최종 신뢰도 | 수 | 비율 |
|---|---:|---:|
| **high** — 검증을 전부 통과 | 966 | 75.6% |
| **medium** — 사람 확인 필요 | 312 | 24.4% |

medium으로 내려간 사례 (앞 15건)

- `alphaZimuth/Hy-MT2-30B-A3B-APEX-GGUF` 30.06B
    - MoE 신호 (model_id 패턴 -A3B) — 전체인지 활성인지 불명확. 파일 크기로도 확인 안 됨
- `alphaZimuth/Hy-MT2-30B-A3B-Uncensored-Heretic-APEX-GGUF` 30.06B
    - MoE 신호 (model_id 패턴 -A3B) — 전체인지 활성인지 불명확. 파일 크기로도 확인 안 됨
- `alphaZimuth/Hy-MT2-30B-A3B-Uncensored-v1-APEX-GGUF` 30.06B
    - MoE 신호 (model_id 패턴 -A3B) — 전체인지 활성인지 불명확. 파일 크기로도 확인 안 됨
- `Archsloth/Qwen3.5-9B-GGUF` 9.2B
    - mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수
- `AtomicChat/LFM3-VL-2B-GGUF` 1.73B
    - 원본 LiquidAI/LFM3-VL-2B 은 1.918B 인데 gguf.total 은 1.73B (10% 차이)
    - mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수
- `AX1Y2JP/LFM2.5-VL-3B-heretic-GGUF` 2.7B
    - 원본 heretic-org/LFM2.5-VL-3B-heretic 은 3.123B 인데 gguf.total 은 2.70B (14% 차이)
    - mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수
- `Baekpica/A.X-K2-VQ-GGUF` 14.06B
    - 원본 skt/A.X-K2 은 691.69B 인데 gguf.total 은 14.06B (98% 차이)
    - 파일 embed-tokens-bf16.gguf 이 0.17 B/param — 2.0 기대값의 0.1배. gguf.total 이 전체를 못 셀 가능성
- `Baekpica/MiniMax-M3.1-Flash-VQ-GGUF` 11.84B
    - 파일 dspark-q8_0.gguf 이 0.18 B/param — 1.06 기대값의 0.2배. gguf.total 이 전체를 못 셀 가능성
- `bartowski/EXAONE-3.5-2.4B-Instruct-GGUF` 2.67B
    - 원본 LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct 은 2.405B 인데 gguf.total 은 2.67B (10% 차이)
- `bartowski/FINAL-Bench_Darwin-35B-A3B-Opus-GGUF` 34.66B
    - mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수
- `bartowski/Jackrong_Qwen3.5-4B-Neo-GGUF` 4.21B
    - 원본 Jackrong/Qwen3.5-4B-Neo 은 4.66B 인데 gguf.total 은 4.21B (10% 차이)
    - mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수
- `bartowski/LiquidAI_LFM2.5-VL-3B-GGUF` 2.7B
    - 원본 LiquidAI/LFM2.5-VL-3B 은 3.123B 인데 gguf.total 은 2.70B (14% 차이)
    - mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수
- `bartowski/mistralai_Devstral-Small-2505-GGUF` 23.57B
    - mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수
- `bartowski/mistralai_Devstral-Small-2507-GGUF` 23.57B
    - mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수
- `bartowski/mistralai_Ministral-3-14B-Instruct-2512-GGUF` 13.51B
    - mmproj 파일 있음 — 비전 인코더가 빠진 언어부만의 수

