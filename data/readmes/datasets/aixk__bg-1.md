---
language:
- en
- ko
license: apache-2.0
tags:
- cybersecurity
- zero-trust
- ai-defense
- botnet-detection
- network-traffic
- time-series
size_categories:
- 10K<n<100K
task_categories:
- tabular-classification
- time-series-forecasting
pretty_name: BAAR3-guard Advanced AI & Botnet Threat Telemetry Dataset
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
dataset_info:
  features:
  - name: x_macro
    list:
      list: float32
  - name: x_micro
    list:
      list: float32
  - name: label_class
    dtype: int64
  - name: label_threat
    dtype: float64
  splits:
  - name: train
    num_bytes: 52337808
    num_examples: 25066
  - name: validation
    num_bytes: 13085496
    num_examples: 6267
  download_size: 57584422
  dataset_size: 65423304
---

# 🛡️ aixk/bg-1 (Enhanced Multi-Vector Threat Dataset)

이 데이터셋은 기존의 단순 웹/스캔 공격을 넘어 **AI 자율 봇넷(Botnet), 내부 침투(Infiltration), 크리덴셜 탈취(Patator), 복합 L7 DoS** 등 실제 공격 패킷 트래픽을 종합 반영한 듀얼 시계열 데이터셋입니다.

## 📊 Ground-Truth Class Mapping
- `0`: **정상 트래픽 (BENIGN / Normal)**
- `1`: **AI 자율 정찰 / 봇넷 / 침투 (Bot / PortScan / Infiltration)**
- `2`: **실제 L7 웹 공격 및 DoS (Web Attacks / SQLi / XSS / DoS / DDoS)**
- `3`: **크리덴셜 탈취 무차별 대입 (SSH/FTP-Patator / Brute-force)**
