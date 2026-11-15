---
language:
- ko
license: apache-2.0
base_model: TeamUNIVA/qwen3_asr_1.7b_ko
pipeline_tag: automatic-speech-recognition
library_name: mlx
tags:
- automatic-speech-recognition
- speech
- korean
- qwen3-asr
- mlx
- 4-bit
- quantized
- apple-silicon
---

# yeowon/qwen3_asr_1.7b_ko-MLX-4bit

<div align="center">
  <p>
    <a href="https://buymeacoffee.com/tripleyoung" target="_blank">
      <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Priority%20Model%20Queue%20%E2%9A%A1-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee" />
    </a>
    <a href="https://qr.kakaopay.com/FVgCIrWbX" target="_blank">
      <img src="https://img.shields.io/badge/KakaoPay%20QR-%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%8E%98%EC%9D%B4%20%EC%86%A1%EA%B8%88-FEE500?style=for-the-badge&logo=kakaotalk&logoColor=black" alt="KakaoPay QR" />
    </a>
    <img src="https://img.shields.io/badge/NH%EB%86%8D%ED%98%91(%EB%86%8D%EC%B6%95%ED%98%91)-352--1556--0640--33%20(%EC%9C%A4%EC%97%AC%EC%9B%90)-0072BC?style=for-the-badge" alt="NH농협 352-1556-0640-33 (윤여원)" />
    <a href="https://huggingface.co/yeowon/qwen3_asr_1.7b_ko-MLX-4bit/discussions" target="_blank">
      <img src="https://img.shields.io/badge/HF%20Community-Request%20Models%20%F0%9F%92%AC-38BDF8?style=for-the-badge" alt="Community Discussions" />
    </a>
  </p>
  <p>
    <a href="https://qr.kakaopay.com/FVgCIrWbX" target="_blank">
      <img src="https://huggingface.co/yeowon/index-tts-ko/resolve/main/assets/kakaopay_qr.jpg" width="160" alt="KakaoPay QR Transfer (윤여원)" style="border-radius: 12px; border: 1px solid #e5e7eb;" />
    </a>
    <a href="https://www.buymeacoffee.com/tripleyoung" target="_blank">
      <img src="https://huggingface.co/yeowon/index-tts-ko/resolve/main/assets/buymeacoffee_qr.png" width="160" alt="Buy Me a Coffee QR (tripleyoung)" style="border-radius: 12px; border: 1px solid #e5e7eb;" />
    </a>
  </p>
  <p>
    🏦 <b>국내 계좌이체 후원:</b> <code>NH농협(농축협) 352-1556-0640-33 (예금주: 윤여원)</code> &nbsp;|&nbsp;
    💛 <a href="https://qr.kakaopay.com/FVgCIrWbX" target="_blank"><b>카카오페이 QR 송금</b></a> &nbsp;|&nbsp;
    ☕ <a href="https://buymeacoffee.com/tripleyoung" target="_blank"><b>Buy Me a Coffee</b></a>
  </p>
</div>

> **🔓 로그인·승인 없이 바로 받는 공개 모델**: 가중치와 추론 코드를 누구나 바로 내려받을 수 있습니다.
> **⚡ 다른 모델도 Rung Ω로 양자화하거나, 다른 언어로 파인튜닝해 드릴까요?** [커뮤니티 게시판](https://huggingface.co/yeowon/qwen3_asr_1.7b_ko-MLX-4bit/discussions)에 요청을 남기거나, [**Buy Me a Coffee**](https://buymeacoffee.com/tripleyoung)로 후원하시면 **우선 처리**해 드립니다!


이 모델은 한국어 음성 인식(ASR) 파인튜닝 모델인 [`TeamUNIVA/qwen3_asr_1.7b_ko`](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko)를 Apple Silicon(M1/M2/M3/M4)용 **MLX 4-bit (`group_size=64`)** 포맷으로 양자화한 버전입니다.

* **원본 모델 크기 (BF16/FP16):** `4,480.9 MB` (~4.48 GB)
* **양자화 후 크기 (Full INT4, Group Size 64):** **`1,099.6 MB` (~1.07 GB, 75.5% 용량 절감)**
  * Audio Encoder (`audio_tower.*`): `176.4 MB` (Linear 4-bit + Conv2D/Norm BF16)
  * Text Decoder (`model.*`): `923.2 MB` (28-layer Qwen3 + 151,936 Vocab Tied Embedding 4-bit)
* **모델 로드 시간 (Apple M1 Pro 기준):** **약 0.43초**
* **추론 속도 (Apple M1 Pro 기준):** **평균 RTF `0.133x` (실시간 대비 7.5배속)**

---

## 벤치마크 실측 비교 (Apple M1 Pro 16GB)

총 26.34초 분량의 한국어 테스트 오디오 3개(`example_1.wav` 2.50s, `example_2.wav` 7.20s, `example_3.wav` 16.64s) 기준 실측 결과입니다:

| 정밀도 구성 | 전체 메모리 | 인코더 메모리 | 디코더 메모리 | 3개 오디오 총 추론 시간 | 평균 RTF | 실시간 대비 배속 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **MLX BF16 (원본)** | 3,887.3 MB | 605.5 MB | 3,281.7 MB | 5,533.3 ms | `0.210x` | 4.8x |
| **MLX INT8 (Decoder 8-bit)** | 2,349.1 MB | 605.5 MB | 1,743.5 MB | 3,707.1 ms | `0.141x` | 7.1x |
| **MLX INT4 (Decoder+Encoder 4-bit, 본 모델)** | **1,099.6 MB** | **176.4 MB** | **923.2 MB** | **3,499.4 ms** | **`0.133x`** | **7.5x** |

---

## 사용법 (Quick Start)

### 1. 패키지 설치

```bash
pip install qwen3-asr-mlx mlx soundfile
```

### 2. 파이썬 단일 오디오 추론 (`mlx_quantized_asr.py` 포함)

저장소에 포함된 `mlx_quantized_asr.py`를 사용하여 사전 양자화된 4-bit 가중치를 0.4초 만에 바로 로드해 추론할 수 있습니다:

```python
from mlx_quantized_asr import QuantizedMLXQwen3ASR

# 허깅페이스 리포지토리 ID 또는 로컬 폴더 경로 지정
engine = QuantizedMLXQwen3ASR("yeowon/qwen3_asr_1.7b_ko-MLX-4bit")

result = engine.transcribe("audio.wav", language="Korean")
print(result.text)
```

### 3. 실시간 마이크 스트리밍 웹 서버 실행

```bash
python mlx_quantized_asr.py --model-id yeowon/qwen3_asr_1.7b_ko-MLX-4bit --serve --port 7860
```
브라우저에서 `http://127.0.0.1:7860` 접속 후 마이크 버튼을 눌러 실시간 한국어 음성 인식을 사용할 수 있습니다.

---

## 라이선스 및 출처 (License & Credits)

* **Base Model:** [`TeamUNIVA/qwen3_asr_1.7b_ko`](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko) (by TeamUNIVA, fine-tuned from [`Qwen/Qwen3-ASR-1.7B`](https://huggingface.co/Qwen/Qwen3-ASR-1.7B))
* **License:** Apache-2.0

---

## ☕ 후원 & 우선 모델 요청

이 모델과 [Talkit](https://github.com/muzuksazo/desktop-recorder) 앱은 로그인·승인 없이 공개하고 있습니다. 이 모델이 강의 기록이나 연구에 도움이 되셨다면 후원으로 응원해 주세요.

1. **⚡ 후원자 우선 처리**: [Buy Me a Coffee](https://buymeacoffee.com/tripleyoung) 후원 메모나 카카오페이·계좌이체 메모에 원하는 모델·언어를 적어 주시면 **먼저** 작업합니다.
2. **💬 커뮤니티 요청 게시판**: 언제든 [Hugging Face Discussions](https://huggingface.co/yeowon/qwen3_asr_1.7b_ko-MLX-4bit/discussions)에 글을 남겨 주세요.

<p align="left">
  <a href="https://buymeacoffee.com/tripleyoung" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50" />
  </a>
</p>

* **☕ Buy Me a Coffee (해외 후원 · 우선 요청)**: [https://buymeacoffee.com/tripleyoung](https://buymeacoffee.com/tripleyoung)
* **💛 카카오페이 QR 송금**: [https://qr.kakaopay.com/FVgCIrWbX](https://qr.kakaopay.com/FVgCIrWbX)
* **🏦 국내 계좌이체**: `NH농협(농축협) 352-1556-0640-33 (예금주: 윤여원)`
* **💬 커뮤니티 · 모델 요청 게시판**: [https://huggingface.co/yeowon/qwen3_asr_1.7b_ko-MLX-4bit/discussions](https://huggingface.co/yeowon/qwen3_asr_1.7b_ko-MLX-4bit/discussions)

<p align="center">
  <a href="https://qr.kakaopay.com/FVgCIrWbX" target="_blank">
    <img src="https://huggingface.co/yeowon/index-tts-ko/resolve/main/assets/kakaopay_qr.jpg" width="160" alt="KakaoPay QR Transfer (윤여원)" style="border-radius: 12px; border: 1px solid #e5e7eb;" />
  </a>
  <a href="https://www.buymeacoffee.com/tripleyoung" target="_blank">
    <img src="https://huggingface.co/yeowon/index-tts-ko/resolve/main/assets/buymeacoffee_qr.png" width="160" alt="Buy Me a Coffee QR (tripleyoung)" style="border-radius: 12px; border: 1px solid #e5e7eb;" />
  </a>
</p>
