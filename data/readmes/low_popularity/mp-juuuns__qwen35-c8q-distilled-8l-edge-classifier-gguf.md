---
license: apache-2.0
base_model: Qwen/Qwen3.5-0.8B
pipeline_tag: text-classification
library_name: gguf
tags:
  - gguf
  - qwen3.5
  - text-classification
  - edge-ai
  - arduino-uno-q
  - korean
language:
  - ko
---

# Qwen3.5 C8Q Distilled 8L Edge Classifier — Mixed Q6_K GGUF

> **Experimental research artifact — not a production-safe scam detector.**  
> 한국어 원문을 생성하지 않고 3개의 문맥/의도 logit으로 분류하는 CPU용 GGUF입니다.

This repository contains an 8-layer classification-only architecture derived from
`Qwen/Qwen3.5-0.8B`. It was distilled from a 24-layer task-specific teacher and exported
as a mixed-precision GGUF for CPU-only local inference on Arduino UNO Q. The architecture
can be retrained for arbitrary N-class tasks; the published weights remain a three-class
scam-context research checkpoint.

> **지원 실행 경로: Arduino UNO Q, Linux/aarch64 CPU, OpenBLAS, patched `llama-embedding`.**  
> **일반 채팅·텍스트 생성 불가. Ollama, `llama-cli`, MPS, CUDA, OpenCL 또는 GPU offload용 모델이 아닙니다.**

```text
Input UTF-8 text
  → tokenizer
  → distilled 8-layer Qwen3.5 text backbone
  → rightmost non-padding hidden state
  → bias-free linear classifier
  → 3-class logits
  → normal / scam_attempt / scam_news_edu
```

## 한눈에 보기

| 질문 | 답 |
|---|---|
| 무엇인가? | Qwen3.5의 생성 head와 decode loop를 제거하고 3개 고정 logit을 내는 8-layer 분류기 |
| 입력 | UTF-8 한국어 원문 한 건. 별도 지시 prompt나 chat template 불필요 |
| 출력 | `[normal, scam_attempt, scam_news_edu]` 순서의 실수 logit 3개 |
| 판단하는가? | 아니요. 문맥/의도 class를 검출할 뿐 최종 사기 판정을 하지 않음 |
| 어디서 돌렸나? | Arduino UNO Q Linux/aarch64 CPU, OpenBLAS, custom llama.cpp/GGML runtime |
| 공개본 class 수 | **3개**. 4-class 또는 임의 N-class로 바꾸려면 새 head 학습과 GGUF 재변환 필요 |
| 핵심 내부 결과 | 37-row에서 C8Q 97.30% accuracy / 0.9781 Macro-F1, 151.03s, 1169.0MiB peak RSS |

## 왜 만들었나

초기 문제의식은 “매 요청마다 긴 지시문을 넣고, 언어모델이 그 지시를 다시 해석하고,
자연어 또는 JSON을 생성한 뒤 다시 파싱하는 비용이 단순 분류에 꼭 필요한가?”였습니다.
이 edge gate가 필요한 것은 긴 답변이 아니라 다음 단계로 넘길 **고정된 문맥 신호**입니다.

프로젝트에서는 GPU/NPU 경로도 실제로 조사했습니다. Vulkan은 실행되었지만 이 짧은 분류 workload에서
실속 가속이 아니었고, QNN HTP/GPU·OpenCL·ExecuTorch 경로는 현재 stack에서 빌드 또는 runtime gate에
막혔습니다. 그래서 외부 API나 별도 PC 서버 없이 UNO Q 한 대에서 실행할 수 있는 CPU-first 경로를
택했습니다. 생성형 Qwen의 vocabulary head와 autoregressive decode를 없애고, 24-layer teacher를
8-layer student로 압축한 이유가 여기에 있습니다.

이 공개본이 증명하는 것은 “완벽한 사기 탐지”가 아닙니다. **생성 prompt baseline보다 작은
classification-only Qwen을 로컬 edge 장치에서 실행하고, 정확도·시간·메모리·수치 오차를 함께
감사할 수 있다**는 ML systems/edge-AI feasibility artifact입니다.

## 핵심 벤치마크 결과

설명을 읽은 뒤 성능과 edge 비용을 바로 비교할 수 있도록 핵심 결과를 먼저 제시합니다.
모든 품질 수치는 **human-gold가 아닌 reused legacy 37-row 내부 세트**의 exploratory 결과이며,
가장 작은 class는 3건입니다. 따라서 실제 환경의 사기 탐지 정확도나 외부 일반화 성능을 뜻하지 않습니다.

![Eight strong baselines: internal Accuracy and Macro-F1](benchmark_quality_internal.png)

품질 그래프는 MiniLM, mBERT, XLM-R, original Qwen prompt generation, 24L classifier,
naive 8L layer deletion, hard-label 8L fine-tuning, 8L knowledge distillation의 8개 arm을 포함합니다.
P0 prompt의 품질은 같은 test37을 완주한 historical run에서 가져왔고, final cgroup resource run은
30/37에서 OOM으로 중단됐습니다. hard-label 8L의 37/37 결과도 작은 reused set의 point estimate일
뿐 일반적으로 KD보다 우수하다는 증거가 아닙니다.

![Eight strong baselines: artifact size, measured wall time, and peak memory](benchmark_edge_efficiency.png)

![Eight strong baselines: mean CPU and peak temperature](benchmark_cpu_thermal.png)

| Arm | Accuracy | Macro-F1 | Measured wall | Peak memory | Mean CPU | Peak temp. | Run status |
|---|---:|---:|---:|---:|---:|---:|---|
| MiniLM INT8 | 0.973 | 0.978 | 17.16s | 595.4MiB | 74.4% | 57.3°C | 37/37 complete |
| mBERT INT8 | 0.946 | 0.883 | 40.48s | 438.6MiB | 92.2% | 61.1°C | 37/37 complete |
| XLM-R INT8 | 0.919 | 0.937 | 38.97s | 806.0MiB | 87.4% | 61.1°C | 37/37 complete |
| Qwen prompt Q4_0 | 0.622 | 0.256 | 299.49s | 2500.0MiB | 80.0% | 65.5°C | 30/37 OOM |
| Qwen C24 24L | 0.946 | 0.957 | 427.90s | 1436.7MiB | 95.2% | 79.6°C | 37/37 complete |
| Qwen naive 8L | 0.378 | 0.387 | 149.03s | 1143.1MiB | 92.0% | 72.1°C | 37/37 complete |
| Qwen hard-label 8L | 1.000 | 1.000 | 151.01s | 1128.5MiB | 92.2% | 71.8°C | 37/37 complete |
| **Qwen KD 8L (published)** | 0.973 | 0.978 | 151.03s | 1169.0MiB | 92.4% | 71.8°C | 37/37 complete |

동일 custom classifier runtime에서 C8Q는 C24보다 **2.83배 빠르고**, artifact는
**37.2% 작으며**, peak RSS는 **18.6% 낮았습니다**. prompt arm은
HTTP/container+cgroup 계층이고 30/37 OOM이므로 direct foreground 37-row arm과 절대 시간·메모리를
같은 척도로 해석하면 안 됩니다.

## Critical limitations

- The evaluation set has only 37 rows and is **not human-gold**.
- The same test hash was used in earlier experiments, so it is not an untouched confirmatory holdout.
- The smallest class has only 3 examples.
- System cost, CPU, and thermal values are from one final v4 run per arm, not repeated-run means.
- Template-family provenance and license/consent coverage in the training database are 0%.
- The artifact runs on UNO Q and preserved all 37 labels relative to the Mac candidate, but its
  strict max relative-L2 was **0.033243**, above the project-specific **0.02** gate.
- The 0.02 threshold is an internal numerical regression criterion, not an IEEE, NIST,
  MLPerf, Hugging Face, Arduino, or safety certification threshold.
- Do not claim real-world scam-detection accuracy, external generalization, or production safety
  from the reported exploratory metrics.

## 이 모델이 하는 일

The model does not generate text. A Qwen3.5 language backbone produces the last valid token hidden
state, and a bias-free linear classification head emits three logits:

| ID | Label | Meaning |
|---:|---|---|
| 0 | `normal` | Ordinary or benign context |
| 1 | `scam_attempt` | Direct scam-attempt style context |
| 2 | `scam_news_edu` | News, education, or quoted scam context |

These are legacy project labels. They are not the newer hierarchical ambiguity/evidence/malicious-
intent ontology and should not be interpreted as a final fraud judgment.

쉽게 말하면, 원문을 읽은 뒤 “일반 문맥인가 / 직접적인 시도 문맥인가 / 사기 사례를 설명하는
뉴스·교육 문맥인가”를 구분합니다. `scam_attempt`가 가장 높아도 모델 출력만으로 “사기 확정”이라고
말하면 안 됩니다. 실제 서비스는 URL·발신자·공식기관 조회 같은 외부 evidence와 human review를
별도로 결합해야 합니다.

## Artifact

| File | Bytes | SHA256 |
|---|---:|---|
| `qwen35-c8q-distilled-8l-mixed-q6_k-395mb.gguf` | 395,274,304 | `0f2d92e578e1420b8dec69e19c7636f2e144ed058756bc80cf32b5df9677a39b` |

Architecture summary:

- Base family: Qwen3.5-0.8B
- Language blocks: fixed 8 layers selected from a 24-layer teacher
- Layer types: 6 linear-attention blocks and 2 full-attention blocks
- Output: 3 fixed logits, no vocabulary generation head, no autoregressive decode loop
- Quantization: mixed F16 and importance-matrix Q6_K
- Target runtime: custom llama.cpp/GGML classifier fork

### 내부 계산

1. tokenizer가 원문을 token ID와 attention mask로 바꿉니다.
2. 8개 Qwen3.5 text block이 hidden state를 계산합니다.
3. 마지막 padding이 아닌 token의 1,024차원 hidden state를 pooling합니다.
4. bias가 없는 `Linear(1024, 3)` head가 logit 3개를 냅니다.
5. 가장 큰 logit의 index를 `labels.json`으로 label에 매핑합니다.

보존한 teacher source layer는 `[0, 4, 8, 11, 14, 17, 20, 23]`이며, student 구성은
linear-attention 6개와 full-attention 2개입니다. 단순 삭제 뒤 성능이 무너졌기 때문에 teacher의
logit, 중간 interface hidden state, final hidden state를 함께 맞추는 distillation로 복구했습니다.

## 입력 데이터 계약

### 추론 입력

- 형식: 한 건의 UTF-8 raw text
- 주 언어: 한국어
- chat message 배열이나 system prompt: 필요 없음
- 학습 시 truncation: 최대 256 tokens
- model metadata context: 262,144 tokens이지만, **256 tokens를 크게 넘는 입력은 학습 분포 밖**이므로
  같은 품질을 가정하면 안 됩니다.
- URL, 전화번호, 줄바꿈은 문자열 일부로 그대로 넣을 수 있습니다.
- 이미지·음성·PDF는 이 GGUF의 직접 입력이 아닙니다. 먼저 OCR/STT로 text를 만들어야 합니다.

예시 입력은 설명용 가상 문장입니다.

```text
[알림] 주소 확인이 필요합니다. 공식 앱에서 배송 내역을 확인해 주세요.
```

### 재학습용 JSONL 권장 schema

```json
{"sample_id":"train-000001","source_group_id":"case-001","split":"train","text":"원문 텍스트","label":"normal"}
{"sample_id":"train-000002","source_group_id":"case-002","split":"train","text":"원문 텍스트","label":"scam_attempt"}
```

필수 값은 `text`와 `label`이며, 누출 방지를 위해 `source_group_id` 단위로 train/calibration/test를
나누는 것을 권장합니다. 같은 사건의 문장 변형이 서로 다른 split에 들어가면 정확도가 부풀 수 있습니다.

## 출력 데이터 계약

patched `llama-embedding`의 `--embd-output-format array` 출력은 다음 모양입니다.

```json
[[1.25, 6.80, -4.10]]
```

- 바깥 배열: 입력 sample 수
- 안쪽 배열: class 순서대로 된 raw logits
- 위 예시의 argmax는 index `1`, 즉 `scam_attempt`
- 값은 probability가 아닙니다. 필요하면 softmax를 적용할 수 있지만 이 작은 내부 데이터의 confidence를
  실제 사기 확률로 해석하면 안 됩니다.
- batch 출력 shape는 `[batch_size, 3]`입니다.

```python
import json

labels = ["normal", "scam_attempt", "scam_news_edu"]
logits = json.loads('[[1.25, 6.80, -4.10]]')[0]
class_id = max(range(len(logits)), key=logits.__getitem__)
result = {"class_id": class_id, "label": labels[class_id], "logits": logits}
print(result)
```

## 지원 실행 경로: UNO Q edge CPU only

This GGUF requires the included **custom llama.cpp patch**. Upstream llama.cpp does not provide this
Qwen3.5 sequence-classification graph, `cls.output.weight` loader, RANK pooling consumer, or fixed-logit
output contract.

### 사용하면 안 되는 loader

- `ollama run`: 지원하지 않음
- upstream `llama-cli`: 생성 vocabulary head가 없으므로 지원하지 않음
- MPS, CUDA, OpenCL, Vulkan 또는 GPU offload: 이 release의 배포·benchmark 경로가 아님
- `-ngl`을 1 이상으로 설정: 검증하지 않음
- chat template로 assistant 답변 생성: 모델 목적과 출력 계약이 다름

지원 경로는 **UNO Q Linux/aarch64 CPU + OpenBLAS + patched `llama-embedding` + `-ngl 0`** 하나입니다.

### 1. UNO Q 시스템 확인

아래 명령은 UNO Q의 Linux shell에서 실행합니다.

```bash
uname -m
cat /etc/os-release
free -h
df -h "$HOME"
```

검증 장치는 `aarch64`, Debian 계열이었습니다. 다른 architecture에서는 별도 build와 parity
검증이 필요합니다.

### 2. UNO Q에 model과 patch 다운로드

```bash
sudo apt-get update
sudo apt-get install -y git cmake ninja-build build-essential libopenblas-dev python3-venv time

ROOT="$HOME/qwen35-c8q-edge"
mkdir -p "$ROOT/model" "$ROOT/src" "$ROOT/output"
python3 -m venv "$ROOT/hf-env"
. "$ROOT/hf-env/bin/activate"
python -m pip install --upgrade huggingface_hub

hf download mp-juuuns/qwen35-c8q-distilled-8l-edge-classifier-gguf \
  qwen35-c8q-distilled-8l-mixed-q6_k-395mb.gguf \
  qwen35-classifier-llamacpp.patch \
  labels.json benchmark_results.json \
  --local-dir "$ROOT/model"
```

외부 PC에서 먼저 받은 경우에도 최종적으로 위와 같은 `$HOME/qwen35-c8q-edge/model/` 구조에
파일을 두면 이후 명령이 동일합니다.

### 3. model SHA-256 확인

```bash
sha256sum "$ROOT/model/qwen35-c8q-distilled-8l-mixed-q6_k-395mb.gguf"
```

예상 결과:

```text
0f2d92e578e1420b8dec69e19c7636f2e144ed058756bc80cf32b5df9677a39b  qwen35-c8q-distilled-8l-mixed-q6_k-395mb.gguf
```

다르면 실행하지 말고 다시 다운로드합니다.

### 4. UNO Q에서 CPU/OpenBLAS runtime 빌드

```bash
cd "$ROOT/src"
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
git checkout f113e02d5ab4c4910709d46e8d81af92ef945289
git apply "$ROOT/model/qwen35-classifier-llamacpp.patch"

cmake -S . -B build-edge -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DGGML_NATIVE=OFF \
  -DGGML_BLAS=ON \
  -DGGML_BLAS_VENDOR=OpenBLAS \
  -DBLA_VENDOR=OpenBLAS \
  -DGGML_CUDA=OFF \
  -DGGML_VULKAN=OFF \
  -DGGML_METAL=OFF \
  -DLLAMA_BUILD_EXAMPLES=ON \
  -DLLAMA_BUILD_TESTS=OFF

cmake --build build-edge --target llama-embedding llama-bench -j 4
file build-edge/bin/llama-embedding
ldd build-edge/bin/llama-embedding
```

`file`은 aarch64 ELF를 보여야 하고, `ldd`에는 OpenBLAS가 resolve되어야 하며 `not found`가
있으면 안 됩니다. 이 단계에서 MPS/CUDA/OpenCL runtime을 별도로 설치하거나 선택하지 않습니다.

### 5. 한 문장 분류

복사 가능한 한 줄 명령:

```bash
OPENBLAS_NUM_THREADS=4 SCAMGUARDIAN_BLAS_MIN_BATCH=1 LD_LIBRARY_PATH="$ROOT/src/llama.cpp/build-edge/bin" "$ROOT/src/llama.cpp/build-edge/bin/llama-embedding" -m "$ROOT/model/qwen35-c8q-distilled-8l-mixed-q6_k-395mb.gguf" --pooling rank --embd-normalize -1 --embd-output-format array --parallel 2 -t 4 -ngl 0 -fa 0 -ctk f32 -ctv f32 -c 512 -p "분류할 UTF-8 원문"
```

읽기 쉽게 풀면:

```bash
OPENBLAS_NUM_THREADS=4 \
SCAMGUARDIAN_BLAS_MIN_BATCH=1 \
LD_LIBRARY_PATH="$ROOT/src/llama.cpp/build-edge/bin" \
  "$ROOT/src/llama.cpp/build-edge/bin/llama-embedding" \
  -m "$ROOT/model/qwen35-c8q-distilled-8l-mixed-q6_k-395mb.gguf" \
  --pooling rank \
  --embd-normalize -1 \
  --embd-output-format array \
  --parallel 2 \
  -t 4 \
  -ngl 0 \
  -fa 0 \
  -ctk f32 \
  -ctv f32 \
  -c 512 \
  -p "분류할 UTF-8 원문" \
  >"$ROOT/output/logits.json"

cat "$ROOT/output/logits.json"
```

예상 shape는 `[[logit_0, logit_1, logit_2]]`이며 순서는 `labels.json`과 같습니다.

### 6. batch 실행

여러 입력은 각 원문에 존재하지 않는 separator로 분리합니다. 원문 자체의 줄바꿈을 separator로
사용하면 sample이 잘릴 수 있습니다.

```bash
OPENBLAS_NUM_THREADS=4 \
SCAMGUARDIAN_BLAS_MIN_BATCH=1 \
LD_LIBRARY_PATH="$ROOT/src/llama.cpp/build-edge/bin" \
  "$ROOT/src/llama.cpp/build-edge/bin/llama-embedding" \
  -m "$ROOT/model/qwen35-c8q-distilled-8l-mixed-q6_k-395mb.gguf" \
  --pooling rank --embd-normalize -1 --embd-output-format array \
  --parallel 2 -t 4 -ngl 0 -fa 0 -ctk f32 -ctv f32 -c 1024 \
  --embd-separator '<|edge_classifier_separator_0|>' \
  -f "$ROOT/input.prompts.txt"
```

### 7. 자원 측정과 운용 주의

final v4에서 검증된 C8Q test37 process peak RSS는 약 `1169.0 MiB`였습니다. 다른 model server를 동시에
상주시킨 상태에서는 board memory pressure나 OOM이 발생할 수 있으므로 clean foreground process로
먼저 확인하세요. 기존 service가 있다면 사용자가 lifecycle을 알고 있을 때만 중지·복구하십시오.

```bash
/usr/bin/time -v env \
  OPENBLAS_NUM_THREADS=4 \
  SCAMGUARDIAN_BLAS_MIN_BATCH=1 \
  LD_LIBRARY_PATH="$ROOT/src/llama.cpp/build-edge/bin" \
  "$ROOT/src/llama.cpp/build-edge/bin/llama-embedding" \
  -m "$ROOT/model/qwen35-c8q-distilled-8l-mixed-q6_k-395mb.gguf" \
  --pooling rank --embd-normalize -1 --embd-output-format array \
  --parallel 2 -t 4 -ngl 0 -fa 0 -ctk f32 -ctv f32 -c 512 \
  -p "분류할 UTF-8 원문"
```

`SCAMGUARDIAN_BLAS_MIN_BATCH=1`은 모델 이름이 아니라 현재 patch가 유지하는 historical compatibility
environment variable이며 inference batch size가 아닌 BLAS routing threshold입니다.

## 현재 공개본은 4-class가 아니다

이 파일의 `cls.output.weight`는 `[1024, 3]`이고 출력 class는 정확히 3개입니다. 프로젝트에서
검토한 4개짜리 새 ontology 또는 트리형 label 설계는 이 weight로 학습·평가되지 않았습니다.
`labels.json`이나 `config.json`의 이름만 4개로 바꾸는 것은 **모델을 4-class로 만드는 방법이
아닙니다**. 존재하지 않는 네 번째 logit은 생기지 않습니다.

## 4-class 또는 임의 N-class로 설정하고 학습하는 법

### 1. 먼저 label 의미와 판정 단위를 고정

예를 들어 `N=4`라면 순서를 명시적으로 고정합니다.

```python
labels = [
    "BENIGN",
    "DECEPTIVE_INTENT",
    "CLAIM_REQUIRES_VERIFICATION",
    "UNCERTAIN",
]
label2id = {label: index for index, label in enumerate(labels)}
id2label = {index: label for label, index in label2id.items()}
```

서로 연결된 의미라면 억지로 single-label로 만들지 말고 hierarchical 또는 multi-label task가 더
적합한지 먼저 결정해야 합니다. 이 공개 runtime은 **single-label classification** 계약이므로
multi-label sigmoid나 tree traversal을 원하면 loss, output interpretation, evaluation과 runtime
API를 추가로 바꿔야 합니다.

### 2. config와 classifier head를 N에 맞게 새로 생성

```python
config.num_labels = len(labels)
config.label2id = label2id
config.id2label = id2label
config.problem_type = "single_label_classification"
model.score = torch.nn.Linear(config.hidden_size, len(labels), bias=False)
```

핵심은 `Linear(hidden_size, N)`입니다. 기존 3-class `score.weight`를 이름만 바꾸지 말고 새 N행
head를 학습해야 합니다.

### 3. 모든 split의 label 집합과 순서를 검증

- train/calibration/test 모두 같은 label 집합을 사용합니다.
- class별 support와 source-group 분리를 기록합니다.
- class imbalance가 크면 accuracy뿐 아니라 Macro-F1, per-class precision/recall/F1,
  confusion matrix를 봅니다.
- test는 model selection이나 quantization policy 선택에 재사용하지 않습니다.
- human-gold가 없다면 결과를 human-gold 성능으로 쓰지 않습니다.

### 4. full-depth teacher head 학습

이 연구의 24L teacher recipe는 backbone feature를 고정하고 rightmost non-padding hidden state 위의
bias-free head를 먼저 학습했습니다. 현재 데이터에서는 train 1,668 / calibration 37 / test 37,
max length 256, head batch 128, 40 epochs, AdamW learning rate `1e-2`, weight decay `1e-2`를
사용했습니다. 선택은 calibration/test가 아니라 최소 train loss였습니다.

새 N-class 데이터에서는 이 숫자를 정답처럼 복사하지 말고 calibration으로 다시 정해야 합니다.
특히 head를 새로 만들었으면 반드시 fresh-load 뒤 output shape `[batch, N]`, finite logits,
label order를 검사합니다.

### 5. 선택 사항: 24L teacher를 8L student로 distillation

이 공개본은 source layer `[0,4,8,11,14,17,20,23]`를 보존한 8L student에 다음 loss를 사용했습니다.

```text
L = 1.0 * L_hard_CE
  + 0.1 * L_teacher_logit_KL(T=4)
  + 1.0 * L_interface_hidden
  + 1.0 * L_final_hidden
```

실제 stable-v2 run은 5 epochs, learning rate `5e-6`, train batch 8, gradient accumulation 2,
weight decay `1e-2`였습니다. 단순 layer 삭제만 하면 interface가 끊어져 성능이 하락했기 때문에
중간 hidden boundary까지 teacher에 맞췄습니다. 새로운 ontology에서는 teacher와 student의
`id2label` 순서가 완전히 같은지 먼저 검사해야 합니다.

### 6. F16 GGUF로 변환하고 N차원 출력을 확인

included patch를 적용한 converter/runtime에서:

```bash
python convert_hf_to_gguf.py /path/to/new-N-class-checkpoint \
  --outfile new-N-class-f16.gguf \
  --outtype f16 \
  --no-mtp

./build/bin/llama-embedding -m new-N-class-f16.gguf --verbose
```

loader log의 `cls.output.weight`가 `[1024, N]`이고 실제 출력 vector 길이가 N인지 확인합니다.
그 뒤 HF logits와 F16 GGUF logits의 argmax, cosine similarity, relative-L2를 고정 fixture에서
비교합니다.

### 7. 양자화는 F16 parity 뒤에 별도 수행

일반 Q6_K는 `llama-quantize new-N-class-f16.gguf new-N-class-q6_k.gguf Q6_K`로 만들 수 있지만,
이 공개 395MB 파일은 단순 uniform Q6_K가 아니라 train-only importance matrix와 tensor sensitivity를
사용해 일부 tensor를 F16으로 보존한 mixed artifact입니다. 정확히 재현하려면 같은 calibration
corpus, imatrix, tensor override policy, pinned quantizer가 필요합니다. class 수를 바꾼 뒤에는
이 policy도 다시 검증해야 하며 현재 3-class 결과를 그대로 승계할 수 없습니다.

## Exploratory UNO Q benchmark

All quality values use the same reused 37-row internal legacy test and are reported for systems
comparison only. They are not human-gold or an untouched confirmatory holdout.

### 전체 결과

| Arm | Accuracy | Macro-F1 | Measured wall | Peak memory | Mean CPU | Peak temp. | Run status |
|---|---:|---:|---:|---:|---:|---:|---|
| MiniLM INT8 | 0.973 | 0.978 | 17.16s | 595.4MiB | 74.4% | 57.3°C | 37/37 complete |
| mBERT INT8 | 0.946 | 0.883 | 40.48s | 438.6MiB | 92.2% | 61.1°C | 37/37 complete |
| XLM-R INT8 | 0.919 | 0.937 | 38.97s | 806.0MiB | 87.4% | 61.1°C | 37/37 complete |
| Qwen prompt Q4_0 | 0.622 | 0.256 | 299.49s | 2500.0MiB | 80.0% | 65.5°C | 30/37 OOM |
| Qwen C24 24L | 0.946 | 0.957 | 427.90s | 1436.7MiB | 95.2% | 79.6°C | 37/37 complete |
| Qwen naive 8L | 0.378 | 0.387 | 149.03s | 1143.1MiB | 92.0% | 72.1°C | 37/37 complete |
| Qwen hard-label 8L | 1.000 | 1.000 | 151.01s | 1128.5MiB | 92.2% | 71.8°C | 37/37 complete |
| **Qwen KD 8L (published)** | 0.973 | 0.978 | 151.03s | 1169.0MiB | 92.4% | 71.8°C | 37/37 complete |

encoder와 classifier 7개는 final v4에서 37/37을 완료했습니다. prompt resource run은 30/37에서
cgroup memory `2,621,440,000 bytes`를 채운 뒤 `OOMKilled=true`가 기록됐고 HTTP 500으로 중단됐습니다. prompt의
표시 품질은 동일 test37의 historical complete run이고, resource 수치는 final cgroup run입니다.

### class별 F1과 confusion matrix

| Arm | normal F1 (n=11) | scam_attempt F1 (n=23) | scam_news_edu F1 (n=3) |
|---|---:|---:|---:|
| MiniLM INT8 | 0.9565 | 0.9778 | 1.0000 |
| mBERT INT8 | 0.9000 | 1.0000 | 0.7500 |
| XLM-R INT8 | 0.8800 | 0.9302 | 1.0000 |
| Qwen prompt Q4_0 | 0.0000 | 0.7667 | 0.0000 |
| Qwen C24 24L | 0.9167 | 0.9545 | 1.0000 |
| Qwen naive 8L | 0.4667 | 0.2667 | 0.4286 |
| Qwen hard-label 8L | 1.0000 | 1.0000 | 1.0000 |
| Qwen KD 8L (published) | 0.9565 | 0.9778 | 1.0000 |

전체 confusion matrix, MCC, artifact hash, raw source hash와 measurement layer는
`benchmark_results.json`에 있습니다.

The prompt arm used local HTTP/container cgroup measurement. Encoder and Qwen classifier arms used
foreground direct-child wall time and Linux `ru_maxrss`. Therefore prompt/direct-arm absolute timing
and memory are not identical measurement layers. C24 and C8Q use the same custom classifier runtime
and form the cleanest direct comparison.

The published 8L model reduced 37-row wall time by about 2.83x, artifact size by
37.2%, and classifier peak RSS by 18.6% relative to C24 in final v4.
This is a quality-preserving efficiency candidate, not proof that it is more accurate or externally valid.

벤치마크 원수치의 공개용 구조화 요약은 `benchmark_results.json`에 있습니다.

## Numerical fidelity

The numerical reference hierarchy was:

1. Hugging Face FP32 reference
2. F32 custom llama.cpp correctness oracle
3. F16 GGUF reference candidate
4. Mixed Q6_K deployment candidate

For each fixed fixture, relative-L2 is

`||logits_candidate - logits_reference||_2 / (||logits_reference||_2 + epsilon)`.

`strict max relative-L2` is the worst value across all fixtures, not the mean. This release is
operational on UNO Q but does not pass the 0.02 research parity gate.

서로 다른 두 수치를 혼동하면 안 됩니다.

- HF/F16 reference 대비 mixed candidate의 strict max relative-L2: `0.033243`
- 별도 forced-BLAS single diagnostic의 Mac Accelerate↔UNO Q relative-L2: `0.036515`

둘 다 project-specific `0.02` numerical gate보다 큽니다. label agreement나 UNO Q operational
success가 numerical parity 통과를 의미하지 않습니다.

## Intended use

- Reproducing edge-AI sequence-classifier and GGUF runtime experiments
- Studying fixed-depth distillation and mixed-precision deployment
- Comparing generation-based prompting with fixed-logit classification under explicit protocols
- Local, offline research prototypes where a human reviews the result

## Out-of-scope use

- Making autonomous fraud, legal, financial, or safety decisions
- Telling a user that content is definitively a scam
- Ranking individuals or organizations by risk
- Treating the three labels as an externally validated Korean scam ontology
- Using the exploratory metrics as real-world prevalence-weighted accuracy

## Training and data boundary

- Train: 1,668 rows
- Calibration: 37 rows
- Test: 37 rows
- Operational database human annotations: 0
- Exact text and source-group train/test overlap: 0
- Strong char 3-gram near-duplicate matches at Jaccard >= 0.8: 0
- Human-gold, consent/license provenance, and untouched confirmatory holdout: missing

Training class counts were `normal=367`, `scam_attempt=1,177`, `scam_news_edu=124`. The test support
was `11/23/3`. Exact normalized-text overlap and source-group overlap between train and test were zero,
but that fact alone does not establish data provenance or external validity.

Synthetic and project seed data may be useful for architecture feasibility, but they do not replace
independently reviewed human-gold evaluation.

## User / Codex / Upstream provenance

- **User:** research question, UNO Q-only and local-only deployment constraint, 24L-to-8L hypothesis,
  benchmark requirements, project assets, and authorization to run measurements and publish this release.
- **Codex:** literature audit, protocol design, training/evaluation scripts, custom runtime and converter
  changes, foreground Mac/UNO Q measurements, error diagnosis, statistical summaries, documentation,
  and release preparation.
- **Upstream:** Qwen3.5 model and architecture, PyTorch, Transformers, llama.cpp/GGML/GGUF,
  OpenBLAS, ExecuTorch/QNN, and Arduino UNO Q.
- Per-sample original authorship, collection, augmentation, and review are not fully attributable from
  the current metadata and remain unresolved.

## Licenses

- Derived Qwen3.5 weights: Apache-2.0, following the upstream model metadata.
- Included model-card support files: Apache-2.0.
- llama.cpp upstream runtime: MIT. The included patch is a modification against pinned commit
  `f113e02d5ab4c4910709d46e8d81af92ef945289` and must be used under the upstream runtime license.

## Reproducibility

`release_manifest.json` records SHA256 hashes for every uploaded support file and the GGUF artifact.
`benchmark_results.json` and all three PNGs are generated from the sealed strong-baseline reports and
final UNO Q v4 raw JSON/JSONL rather than manually retyped. The full paper-style report, raw row-level predictions, and data audit remain in the research
workspace because the underlying dataset does not yet have sufficient redistribution provenance.


## DOI

- `10.57967/hf/9614`
