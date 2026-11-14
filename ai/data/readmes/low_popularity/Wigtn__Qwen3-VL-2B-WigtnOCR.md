---
license: apache-2.0
language:
  - ko
  - en
  - zh
library_name: transformers
base_model: Qwen/Qwen3-VL-2B-Instruct
tags:
  - document-parsing
  - document-intelligence
  - ocr
  - vlm
  - vision-language-model
  - lora
  - distillation
  - korean
  - qwen3-vl
  - structure-preserving
  - rag
  - government-document
  - table-extraction

pipeline_tag: image-text-to-text
datasets:
  - Wigtn/KoGovDoc-Bench
metrics:
  - teds
  - hit@1
model-index:
  - name: WigtnOCR-2B
    results:
      - task:
          type: document-parsing
        dataset:
          name: OmniDocBench
          type: opendatalab/OmniDocBench
        metrics:
          - name: Text NED
            type: ned
            value: 0.288
          - name: Table TEDS
            type: teds
            value: 0.649
          - name: Table TEDS-S
            type: teds
            value: 0.732
          - name: Formula CDM F1
            type: f1
            value: 0.884
          - name: Reading Order NED
            type: ned
            value: 0.211
      - task:
          type: document-parsing
        dataset:
          name: KoGovDoc-Bench
          type: Wigtn/KoGovDoc-Bench
        metrics:
          - name: NED
            type: ned
            value: 0.285
          - name: Hit@1
            type: accuracy
            value: 0.739
          - name: MRR@10
            type: mrr
            value: 0.788
---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://huggingface.co/Wigtn/Qwen3-VL-2B-WigtnOCR/resolve/main/assets/wigtn-logo-white.png">
  <img src="assets/wigtn-logo-navy.png" width="320" alt="WIGTN">
</picture>

# WigtnOCR-2B: Pseudo-Label Distillation for Structure-Preserving Document Parsing

[![HF Model](https://img.shields.io/badge/%F0%9F%A4%97%20Model-blue)](https://huggingface.co/Wigtn/Qwen3-VL-2B-WigtnOCR) [![HF Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Dataset-orange)](https://huggingface.co/datasets/Wigtn/KoGovDoc-Bench) [![GitHub](https://img.shields.io/badge/GitHub-Code-181717.svg?logo=github)](https://github.com/wigtn/wigtnOCR-v1) [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE) [![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![vLLM](https://img.shields.io/badge/vLLM-Serving-purple)](https://github.com/vllm-project/vllm)

**Built by [WIGTN](https://wigtn.com)**

_A 2B VLM distilled from a 30B teacher. It matches or beats the teacher on 3 of 5 OmniDocBench metrics, and is level with it on the retrieval probe of the [RCPS paper](https://aclanthology.org/2026.emnlp-industry.90/) (EMNLP 2026 Industry Track)._

<img src="assets/fig_highlights.png" width="100%" alt="Highlights">

</div>

---

⭐️ **Base Model**: [Qwen3-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct)<br>
⭐️ **Dataset**: [huggingface.co/datasets/Wigtn/KoGovDoc-Bench](https://huggingface.co/datasets/Wigtn/KoGovDoc-Bench)<br>
⭐️ **GitHub**: [github.com/wigtn/wigtnOCR-v1](https://github.com/wigtn/wigtnOCR-v1)

---

## Key Features

* **30B → 2B Distillation**: Matches or beats its 30B teacher on 3 of 5 OmniDocBench metrics (Text NED, Table TEDS, Reading Order) via quality-filtered pseudo-labeling
* **Table TEDS +12.6pp**: Surpasses teacher on table structure recognition through selective training on high-quality GT
* **Retrieval**: Hit@1 0.739 and MRR@10 0.788, first of 6 parsers in the v1 KoGovDoc evaluation, whose queries come from WigtnOCR-2B's own outputs. On the RCPS paper's 663-question probe it is level with the 30B teacher (RCPS 0.583 vs 0.584)
* **Korean Government Documents**: Optimized for complex Korean government layouts (tables, forms, multi-column)
* **Production-Ready**: Single GPU serving via vLLM, 2B params, fast inference

---

## Highlights

<table width="100%">
<tr>
<th width="18%">Category</th>
<th width="22%">Metric</th>
<th width="20%">WigtnOCR-2B</th>
<th width="20%">vs 30B Teacher</th>
<th width="20%">vs PaddleOCR</th>
</tr>
<tr>
<td><b>Parsing</b></td>
<td>Text NED ↓</td>
<td align="center"><b>0.288</b></td>
<td align="center">-0.001 (matches)</td>
<td align="center">—</td>
</tr>
<tr>
<td><b>Tables</b></td>
<td>Table TEDS ↑</td>
<td align="center"><b>0.649</b></td>
<td align="center"><b>+12.6pp</b></td>
<td align="center">—</td>
</tr>
<tr>
<td><b>Retrieval</b></td>
<td>Hit@1 ↑</td>
<td align="center"><b>0.739</b></td>
<td align="center"><b>+2.3pp</b></td>
<td align="center"><b>+22.7pp</b></td>
</tr>
<tr>
<td><b>Retrieval</b></td>
<td>MRR@10 ↑</td>
<td align="center"><b>0.788</b></td>
<td align="center"><b>+1.7pp</b></td>
<td align="center"><b>+19.6pp</b></td>
</tr>
<tr>
<td><b>Reliability</b></td>
<td>Skip Rate ↓</td>
<td align="center"><b>5.8%</b></td>
<td align="center">-13.0pp from base</td>
<td align="center">—</td>
</tr>
</table>

---

## Quick Start

### Transformers (Direct Inference)

```python
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
from PIL import Image

model = Qwen3VLForConditionalGeneration.from_pretrained(
    "Wigtn/Qwen3-VL-2B-WigtnOCR",
    torch_dtype="auto",
    device_map="auto",
)
processor = AutoProcessor.from_pretrained("Wigtn/Qwen3-VL-2B-WigtnOCR")

image = Image.open("document_page.png")

messages = [
    {"role": "system", "content": "You are WigtnOCR, a document parser. Convert the document image to well-structured Markdown."},
    {"role": "user", "content": [
        {"type": "image", "image": image},
        {"type": "text", "text": "Convert this document page to Markdown. Preserve all headings, tables, formulas, and reading order."},
    ]},
]

text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=[text], images=[image], return_tensors="pt").to(model.device)

output_ids = model.generate(**inputs, max_new_tokens=4096)
output = processor.batch_decode(output_ids[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)[0]
print(output)
```

### vLLM (Production Serving)

```bash
vllm serve Wigtn/Qwen3-VL-2B-WigtnOCR \
    --max-model-len 16384 \
    --trust-remote-code
```

```python
from openai import OpenAI
import base64

client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy")

with open("document_page.png", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

response = client.chat.completions.create(
    model="Wigtn/Qwen3-VL-2B-WigtnOCR",
    messages=[
        {"role": "system", "content": "You are WigtnOCR, a document parser. Convert the document image to well-structured Markdown."},
        {"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}},
            {"type": "text", "text": "Convert this document page to Markdown."},
        ]},
    ],
    max_tokens=4096,
)
print(response.choices[0].message.content)
```

---

## OmniDocBench Results

<div align="center">
<img src="assets/fig1_omnidocbench.png" width="100%" alt="OmniDocBench Results">
</div>

Evaluated on [OmniDocBench](https://github.com/opendatalab/OmniDocBench) (CVPR 2025) — 1,355 pages across 9 document types.

<table width="100%">
<tr><th width="22%">Metric</th><th width="16%">Qwen3-VL-2B</th><th width="18%"><b>WigtnOCR-2B</b></th><th width="16%">Qwen3-VL-30B</th><th width="14%">Marker</th><th width="14%">Direction</th></tr>
<tr><td>Text NED</td><td align="center">0.364</td><td align="center"><b>0.288</b></td><td align="center">0.289</td><td align="center">0.218</td><td align="center">lower=better</td></tr>
<tr><td>Table TEDS</td><td align="center">0.561</td><td align="center"><b>0.649</b></td><td align="center">0.523</td><td align="center">0.586</td><td align="center">higher=better</td></tr>
<tr><td>Table TEDS-S</td><td align="center">0.667</td><td align="center"><b>0.732</b></td><td align="center">0.657</td><td align="center">0.658</td><td align="center">higher=better</td></tr>
<tr><td>Formula CDM F1</td><td align="center">0.865</td><td align="center"><b>0.884</b></td><td align="center"><b>0.939</b></td><td align="center">0.863</td><td align="center">higher=better</td></tr>
<tr><td>Formula ExpRate</td><td align="center">0.504</td><td align="center"><b>0.600</b></td><td align="center"><b>0.692</b></td><td align="center">0.582</td><td align="center">higher=better</td></tr>
<tr><td>Reading Order NED</td><td align="center">0.300</td><td align="center"><b>0.211</b></td><td align="center">0.227</td><td align="center"><b>0.165</b></td><td align="center">lower=better</td></tr>
<tr><td>Skip Rate</td><td align="center">18.8%</td><td align="center">5.8%</td><td align="center">5.5%</td><td align="center"><b>0.4%</b></td><td align="center">lower=better</td></tr>
</table>

**WigtnOCR-2B matches or exceeds its 30B teacher on 3 of 5 metrics: Text NED, Table TEDS and Reading Order.** The teacher stays ahead on CDM F1 (0.939 vs 0.884) and Skip Rate (5.5% vs 5.8%). Table TEDS surpasses the teacher by +12.6pp. The 30B column was evaluated with Qwen3-VL-30B-A3B-Instruct-FP8; the pseudo-labels came from the Thinking variant.

---

## KoGovDoc Retrieval Results

<div align="center">
<img src="assets/fig2_retrieval.png" width="85%" alt="KoGovDoc Retrieval">
</div>

Semantic chunking (BGE-M3) → FAISS retrieval on [KoGovDoc-Bench](https://huggingface.co/datasets/Wigtn/KoGovDoc-Bench) — 294 val pages, 564 queries, 6 parsers compared.

<table width="100%">
<tr><th width="20%">Model</th><th width="14%">Type</th><th width="13%">Hit@1 ↑</th><th width="13%">Hit@5 ↑</th><th width="13%">MRR@10 ↑</th><th width="13%">nDCG@10 ↑</th></tr>
<tr><td><b>WigtnOCR-2B</b></td><td>VLM (ours)</td><td align="center"><b>0.739</b></td><td align="center"><b>0.855</b></td><td align="center"><b>0.788</b></td><td align="center">0.437</td></tr>
<tr><td>Qwen3-VL-30B</td><td>VLM (teacher)</td><td align="center">0.716</td><td align="center">0.839</td><td align="center">0.771</td><td align="center">0.411</td></tr>
<tr><td>Marker</td><td>PDF parser</td><td align="center">0.711</td><td align="center">0.853</td><td align="center">0.771</td><td align="center">0.412</td></tr>
<tr><td>Qwen3-VL-2B</td><td>VLM (base)</td><td align="center">0.709</td><td align="center">0.814</td><td align="center">0.756</td><td align="center"><b>0.444</b></td></tr>
<tr><td>MinerU</td><td>PDF parser</td><td align="center">0.608</td><td align="center">0.789</td><td align="center">0.682</td><td align="center">0.384</td></tr>
<tr><td>PaddleOCR</td><td>Pure OCR</td><td align="center">0.512</td><td align="center">0.693</td><td align="center">0.592</td><td align="center">0.293</td></tr>
</table>

**WigtnOCR-2B ranks #1 in Hit@1, Hit@5, and MRR@10** across the 6 parsers; the 2B base leads nDCG@10.

**How this table was measured.** [`run_retrieval_eval.py`](https://github.com/wigtn/wigtnOCR-v1/blob/main/scripts/eval_kogovdoc/run_retrieval_eval.py) takes up to 20 queries per document from the headings and first sentences of **WigtnOCR-2B's own outputs** (564 queries over 38 documents) and counts every chunk of the query's document as relevant. Queries drawn from one parser's output can favour that parser. The [RCPS paper](https://aclanthology.org/2026.emnlp-industry.90/) instead uses 663 question–answer pairs whose answers occur verbatim on the reference pages, with page-level relevance; under that protocol the 30B teacher and WigtnOCR-2B are a near-tie.

---

## BC vs. Retrieval: An Interesting Finding

<div align="center">
<img src="assets/fig3_bc_vs_retrieval.png" width="100%" alt="BC vs Retrieval">
</div>

Chunk quality (BC/CS, MoC framework) does **not** predict retrieval performance.

<table width="100%">
<tr><th width="30%">Model</th><th width="20%">BC ↑</th><th width="20%">CS ↓</th><th width="30%">Hit@1 ↑</th></tr>
<tr><td>MinerU</td><td align="center"><b>0.735</b></td><td align="center"><b>2.711</b></td><td align="center">0.608 (5th)</td></tr>
<tr><td><b>WigtnOCR-2B</b></td><td align="center">0.706</td><td align="center">2.859</td><td align="center"><b>0.739 (1st)</b></td></tr>
<tr><td>PaddleOCR</td><td align="center">0.654</td><td align="center">3.420</td><td align="center">0.512 (6th)</td></tr>
</table>

MinerU produces the cleanest chunk boundaries but ranks 5th in retrieval. **Text richness and structural fidelity matter more than boundary quality for end-to-end RAG.**

---

## KoGovDoc Parsing Quality

<table width="100%">
<tr><th width="40%">Model</th><th width="30%">NED ↓</th><th width="30%">Evaluated</th></tr>
<tr><td><b>WigtnOCR-2B</b></td><td align="center"><b>0.285</b></td><td align="center">289/294</td></tr>
<tr><td>Qwen3-VL-30B (Teacher)</td><td align="center">0.334</td><td align="center">294/294</td></tr>
<tr><td>Qwen3-VL-2B (Base)</td><td align="center">0.390</td><td align="center">294/294</td></tr>
</table>

WigtnOCR-2B surpasses its 30B teacher on Korean government documents.

---

## Ablation Study

<table width="100%">
<tr><th>Config</th><th>LoRA r</th><th>Epochs</th><th>Text NED ↓</th><th>Table TEDS ↑</th><th>TEDS-S ↑</th><th>CDM F1 ↑</th><th>RO NED ↓</th><th>Skip % ↓</th><th>Verdict</th></tr>
<tr><td><b>v1 (final)</b></td><td align="center"><b>8</b></td><td align="center"><b>3</b></td><td align="center"><b>0.288</b></td><td align="center"><b>0.649</b></td><td align="center"><b>0.732</b></td><td align="center">0.884</td><td align="center"><b>0.211</b></td><td align="center">5.8%</td><td><b>Best overall</b></td></tr>
<tr><td>v2-best</td><td align="center">32</td><td align="center">3</td><td align="center">0.309</td><td align="center">0.600</td><td align="center">0.697</td><td align="center">—</td><td align="center">0.215</td><td align="center">0.7%</td><td>Table regression</td></tr>
<tr><td>v2-last</td><td align="center">32</td><td align="center">5</td><td align="center">0.306</td><td align="center">0.610</td><td align="center">0.695</td><td align="center">0.892</td><td align="center">0.214</td><td align="center"><b>0.0%</b></td><td>Overfitting on text</td></tr>
</table>

**Key findings:**
- **LoRA rank 8 outperforms rank 32** — larger capacity leads to table structure regression (-4.9pp TEDS) despite marginally better formula recognition
- **3 epochs optimal** — 5 epochs causes overfitting (eval loss rises after epoch 3)
- **v2 improves skip rate** to 0% but at the cost of core parsing quality
- **v1 selected as final model** due to superior table/text quality which matters most for downstream RAG

---

## Training Details

| Parameter | Value |
|-----------|-------|
| Base model | [Qwen3-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct) |
| Teacher | Qwen3-VL-30B-A3B-Thinking |
| Judge | Qwen3.5-122B-A10B-NVFP4 (text-only, 5-dim scoring) |
| Method | LoRA (rank=8, alpha=32, target=all linear layers) |
| Training samples | 2,667 (filtered from 4,501 pages, score ≥ 3/5) |
| Validation samples | 294 (held out) |
| Training time | 31 minutes |
| Framework | [ms-swift](https://github.com/modelscope/ms-swift) + DeepSpeed ZeRO-2 |
| Epochs | 3 scheduled; the released weights are checkpoint-600 (epoch 1.8, lowest eval loss) |
| Learning rate | 1e-4 |
| Batch size | 1 per GPU × gradient accumulation 4 × 2 GPUs (effective 8) |
| Hardware | 2 × NVIDIA RTX PRO 6000 (98GB each) |
| Trainable params | 8.7M (0.4% of total) |

### Training Data

| Dataset | Documents | Pages | Language | Source |
|---------|:---------:|:-----:|:--------:|--------|
| KoGovDoc | 10 | 3,637 | Korean | Government publications |
| ArXivPapers | 39 | 864 | English | arXiv (cs.CL, cs.CV, cs.LG) |
| **Total** | 49 | 4,501 | Bilingual | — |

GT generated by Qwen3-VL-30B, validated by Qwen3.5-122B with 74–75% pass rate. Quality filtering removes hallucinations, repetitions, and chain-of-thought contamination.

---

## Evaluation Stack

| Component | Tool | Purpose |
|-----------|------|---------|
| Preprocessing | PyMuPDF | PDF → page images (200 DPI) |
| Chunking | BGE-M3 (semantic) | Embedding-based boundary detection |
| BC/CS Metrics | Qwen2.5-1.5B | Perplexity computation (MoC, ACL 2025) |
| Embedding | BAAI/bge-m3 | Chunk → vector |
| Retrieval | FAISS | Cosine similarity search |

---

## Intended Use

- Korean government document digitization and parsing
- RAG pipeline preprocessing (PDF → structured Markdown → chunks → retrieval)
- Academic paper parsing (tables, formulas, reading order)
- Bilingual (Korean + English) document processing

## Limitations

- Optimized for Korean and English; other languages may have reduced quality
- Formula recognition still trails 30B teacher (CDM F1: 0.884 vs 0.939)
- Best results at 200 DPI; lower resolution degrades quality
- Skip rate 5.8% — some complex pages may fail (v2 achieves 0% but with quality trade-offs)

---

## Example Output

Comparison on a complex Korean government document page (kogov_001 p.9 — survey tables + statistical charts + mixed layout).

| | 30B Teacher | WigtnOCR-2B (Ours) |
|---|---|---|
| Charts | `[Figure: ...]` placeholder | Extracts data into tables |
| Content | 1,582 chars | **1,912 chars (+21%)** |
| Tables | 3 tables | **4 tables** (chart → table) |

<details>
<summary><b>PDF Original</b></summary>

<img src="assets/example_kogov001_p9.png" width="50%" alt="PDF Original — kogov_001 page 9">

</details>

<details>
<summary><b>30B Teacher Output (Qwen3-VL-30B)</b> — 1,582 chars</summary>

```markdown
- 지역 주민 의견 및 수요

## [군민 설문조사] 군민 478명 대상 설문조사로 도시문제 도출
- 군민 대상 설문조사 사항

| No. | 설문 항목 |
|-----|-----------|
| Q1 | 성별 / 연령 / 지역 / 불편사항 |
| Q2 | 안전 / 환경 / 에너지 / 교통 / 산업 / 행정 / 복지 / 문화 / 관광 / 농업 / 교육 |
| Q3 | 스마트도시 요소 / 지역 / 서비스 / 리빙랩 |

### - 군민 설문결과

[Figure: 보다 안전한 부여를 위해 개선해야 할 문제]
[Figure: 스마트도시 우선도입 서비스]

자료 : 부여군 스마트도시계획(2023)

## [농어업인 복지실태조사] 생활안전 개선을 위해 필요한 사항 설문결과

| 특성 | 도로안전시설 | 보행자길 정비 | 가로등 확충 | CCTV 설치 | 주민 방범 순찰 | 노후시설 | 안심 귀가 서비스 | 기타 |
|------|-------------|-------------|------------|----------|--------------|---------|----------------|------|
| 농어촌 | 10.1 | 21.0 | 23.1 | 25.7 | 8.1 | 8.2 | 3.4 | 0.3 |
| 읍 | 10.7 | 20.8 | 20.5 | 28.1 | 8.4 | 7.2 | 4.2 | 0.1 |
| 면 | 9.5 | 21.2 | 25.8 | 23.3 | 7.8 | 9.3 | 2.7 | 0.4 |
| 농어가 | 8.7 | 22.3 | 23.2 | 23.1 | 7.9 | 12.1 | 2.5 | 0.2 |
| 비농어가 | 10.6 | 20.5 | 23.1 | 26.6 | 8.2 | 6.9 | 3.7 | 0.3 |
| 30대 이하 | 14.6 | 16.5 | 27.6 | 25.2 | 6.4 | 5.8 | 3.6 | 0.2 |
| 40대 | 6.3 | 20.1 | 19.6 | 33.1 | 10.9 | 4.6 | 5.1 | 0.2 |
| 50대 | 10.8 | 19.4 | 23.0 | 27.2 | 6.8 | 8.4 | 4.1 | 0.3 |
| 60대 | 10.5 | 22.9 | 22.8 | 23.4 | 7.2 | 10.2 | 2.6 | 0.4 |
| 70대 이상 | 9.9 | 23.5 | 24.0 | 21.1 | 8.7 | 10.4 | 2.2 | 0.2 |

자료 : 농촌진흥청 2023 농어업인등에 대한 복지실태조사

| 구분 | 도시문제 | 주민 수요 | 수요 주민 |
|------|----------|-----------|-----------|
| 복지 | 독거노인 돌봄 | - 부여군 보건복지 분야 개선사항으로 지적 | 70대 남성 |
| 복지 | 독거노인 돌봄 | - 인공지능 돌봄서비스 시범 사용 희망 | 60대 여성 |
| 복지 | 시설노후화 | - 부여군 읍면 경로당 내 시설 노후화 | 80대 남성 |
| 복지 | 여가 콘텐츠 부족 | - 경로당 내 여가 콘텐츠 부족 | 60대 여성 |
| 안전 | 안전 인프라 부족 | - 부여시장 근교 노인 보행자 교통사고 위험 높음 | 60대 남성 |
| 관광 | 관광 콘텐츠 부족 | - 수년 동안 업데이트되지 않은 박물관 내 콘텐츠 | 50대 남성 |
```

</details>

<details>
<summary><b>WigtnOCR-2B Output (Ours)</b> — 1,912 chars</summary>

```markdown
- 지역 주민 의견 및 수요

[균민 설문조사] 균민 478명 대상 설문조사로 도시문제 도출
- 균민 대상 설문조사 사항

| No. | 설문 항목 |
| --- | --- |
| Q1 | 성별 / 연령 / 지역 / 불편사항 |
| Q2 | 안전 / 환경 / 에너지 / 교통 / 산업 / 행정 / 보건 / 복지 / 문화 / 관광 / 농업 / 교육 |
| Q3 | 스마트도시 요소 / 지역 / 서비스 / 리빙랩 |

- 균민 설문결과

| 보다 안전한 부여를 위해 개선해야 할 문제 | 스마트도시 우선도입 서비스 |
| --- | --- |
| 시설 노후화 | 34.1% |
| 교통사고 다발구간 | 13.7% |
| 자연재해감시 | 12.8% |
| 심야시간 범죄 | 10.0% |
| 통학 안전 | 9.3% |
| 인재 | 8.2% |
| 재난 예경보 | 8.7% |
| 기타 | 3.4% |
| 스마트 보건/의료/복지 | 17.4% |
| 스마트 교통 | 15.7% |
| 스마트 환경/에너지/수자원 | 10.5% |
| 스마트 문화/관광/스포츠 | 10.1% |
| 스마트 근로/고용 | 9.9% |
| 스마트 행정 | 8.9% |
| 스마트 교육 | 7.6% |
| 스마트 방법/방재 | 6.4% |
| 스마트 시설물관리 | 4.5% |
| 스마트 주거 | 3.2% |
| 스마트 물류 | 2.8% |
| 기타 | 2.9% |

자료 : 부여군 스마트도시계획(2023)

[농어업인 복지실례조사] 생활안전 개선을 위해 필요한 사항 설문결과

| 특성 | 도로안전시설 | 보행자길 정비 | 가로등 확충 | CCTV 설치 | 주민 방법순찰 | 노후시설 | 안심 귀가 서비스 | 기타 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 농어촌 | 10.1 | 21.0 | 23.1 | 25.7 | 8.1 | 8.2 | 3.4 | 0.3 |
| 읍 | 10.7 | 20.8 | 20.5 | 28.1 | 8.4 | 7.2 | 4.2 | 0.1 |
| 면 | 9.5 | 21.2 | 25.8 | 23.3 | 7.8 | 9.3 | 2.7 | 0.4 |
| 농어가 | 8.7 | 22.3 | 23.2 | 23.1 | 7.9 | 12.1 | 2.5 | 0.2 |
| 비농어가 | 10.6 | 20.5 | 23.1 | 26.6 | 8.2 | 6.9 | 3.7 | 0.3 |
| 30대 이하 | 14.6 | 16.5 | 27.6 | 25.2 | 6.4 | 5.8 | 3.6 | 0.2 |
| 40대 | 6.3 | 20.1 | 19.6 | 33.1 | 10.9 | 4.6 | 5.1 | 0.2 |
| 50대 | 10.8 | 19.4 | 23.0 | 27.2 | 6.8 | 8.4 | 4.1 | 0.3 |
| 60대 | 10.5 | 22.9 | 22.8 | 23.4 | 7.2 | 10.2 | 2.6 | 0.4 |
| 70대 이상 | 9.9 | 23.5 | 24.0 | 21.1 | 8.7 | 10.4 | 2.2 | 0.2 |

자료 : 농촌진흥청 2023 농어업인등에 대한 복지실례조사

| 구분 | 도시문제 | 주민 수요 | 수요 주민 |
| --- | --- | --- | --- |
| 복지 | 독거노인 돌봄 | - 부여군 보건복지 분야 개선사항으로 지적 | 70대 남성 |
| 복지 | 독거노인 돌봄 | - 인공지능 돌봄서비스 시범 사용 호평 | 60대 여성 |
| 복지 | 시설노후화 | - 부여군 읍면 경로당 내 시설 노후화 | 80대 남성 |
| 복지 | 여가 콘텐츠 부족 | - 경로당 내 여가 콘텐츠 부족 | 60대 여성 |
| 안전 | 안전 인프라 부족 | - 부여시장 근교 노인 보행자 교통사고 위험 높음 | 60대 남성 |
| 관광 | 관광 콘텐츠 부족 | - 수년 동안 업데이트되지 않은 박물관 내 콘텐츠 | 50대 남성 |
```

</details>

> **Key difference:** The 30B teacher replaces charts with `[Figure: ...]` placeholders, while WigtnOCR-2B extracts the actual data from charts into structured markdown tables — producing 21% more content from the same page.

---

## 📎 Citation

If you use WigtnOCR in your research, please cite:
```bibtex
@software{wigtnocr2026,
  title   = {WigtnOCR: VLM-based Korean Government Document Parser using Teacher-Student Pseudo-GT Pipeline},
  author  = {WIGTN},
  year    = {2026},
  url     = {https://huggingface.co/Wigtn/Qwen3-VL-2B-WigtnOCR}
}

@inproceedings{son2026rcps,
  title     = {Retrieval-Conditional Parsing Score ({RCPS}): Choosing Document Parsers by Retrieval, Not by Appearance},
  author    = {Son, Sang-Woo and Kim, Hyeong-seob and Kim, Hyeonsang and Cho, Hyun-woo and Kim, Jinmo},
  editor    = {Atanasova, Pepa and Haffari, Gholamreza and Wang, Minghan},
  booktitle = {Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing: Industry Track},
  month     = oct,
  year      = {2026},
  address   = {Budapest, Hungary},
  publisher = {Association for Computational Linguistics},
  pages     = {1531--1544},
  url       = {https://aclanthology.org/2026.emnlp-industry.90/}
}
```

---

## 🏢 About WIGTN

[WIGTN](https://wigtn.com) is an AI company in Korea with three teams. Solutions takes AI transformation (AX) for enterprises from consulting to the systems that run it. Product ships the open-source tools we build and use ourselves. Research publishes peer-reviewed work on LLMs, their evaluation, and speech.

- 🌐 Website: https://wigtn.com  
- 🐙 GitHub: https://github.com/wigtn  
- 🤗 HuggingFace: https://huggingface.co/Wigtn
