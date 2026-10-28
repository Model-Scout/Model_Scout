---
language:
- ko
- en
license: apache-2.0
library_name: pytorch
pipeline_tag: text-generation
tags:
- korean
- gated-deltanet
- hybrid
- linear-attention
- from-scratch
- base-model
datasets:
- HuggingFaceFW/fineweb-2
- wikimedia/wikipedia
- HuggingFaceFW/fineweb-edu
---

# Korean 1B hybrid base model (Gated DeltaNet + GQA), trained from scratch

A 1.0B-parameter Korean language model pretrained from random initialisation on 25.17B tokens
(89% Korean). Architecture, tokenizer, Gated DeltaNet Triton kernels, Muon optimizer and training loop
are our own code (PyTorch + Triton).

## Model

| | |
|---|---|
| parameters | 1.002B  |
| layers | 20, interleaved 3:1 ratio of Gated DeltaNet to attention layers |
| width | d_model 2048, SwiGLU FFN 4352, RMSNorm (pre-norm) |
| attention layers | GQA, 16 query / 4 KV heads × 128, RoPE (θ=10000), QK-norm |
| Gated DeltaNet layers | 16 heads, d_k = d_v = 128, short causal conv (k=4), L2-normalised q/k, output gate; chunkwise (C=64) WY-form kernel in Triton |
| vocabulary | 48,000 (byte-level BPE trained on this corpus) |
| context | 2048 tokens |

## Training corpus

| source | Hugging Face dataset | tokenized size after filtering | tokens seen in training |
|---|---|---|---|
| FineWeb-2, Korean (`kor_Hang`, train split) | `HuggingFaceFW/fineweb-2` | 38.28B (52.65M of 60.87M docs) | 21.62B (≈0.56 epochs) |
| Korean Wikipedia (2023-11-01 dump) | `wikimedia/wikipedia`, `20231101.ko` | 0.28B (455k articles) | 0.82B (≈2.9 epochs) |
| FineWeb-Edu, English (`sample-10BT`, 5 of its files) | `HuggingFaceFW/fineweb-edu` | 4.42B (3.66M docs) | 2.73B (≈0.62 epochs) |

- **Mixture.** 88% FineWeb-2 / 2% Wikipedia / 10% English during
  the stable phase; 78% / 8% / 14% during the final
  learning-rate decay. The English share keeps some English ability and adds
  educational content.
- **Filtering.** FineWeb-2 documents shorter than 200 characters (1.57M) or without Hangul (0.18M) were dropped.
- **Decontamination.** Before any training, a held-out set was frozen: 2,000 FineWeb-2 *test-split* documents and
  500 Wikipedia articles, the latter removed from training. Training documents were dropped if they shared any 13-word
  n-gram with a held-out document, or any 8-word n-gram with KoBEST (all splits), the KMMLU test set or our chat eval
  prompts. This removed 6.47M FineWeb-2 documents (10.6%), mostly template boilerplate shared with held-out pages.
- **Tokenizer.** Byte-level BPE, 48,000 tokens, trained on a 2 GB sample (1.55 GB FineWeb-2, 0.25 GB
  Wikipedia, 0.2 GB English), NFC normalisation, single-digit splitting, 16 reserved special tokens
  (`<|endoftext|>`, chat-role tokens, …). 5.03 bytes per token on the held-out Korean text.

## Training method

- **Objective.** Next-token prediction on packed 2048-token sequences; each document is followed by `<|endoftext|>`.
- **Batch.** 512 × 2048 = 1.05M tokens per step (gradient accumulation), 24,000 steps,
  25.17B tokens in total (≈25 tokens per parameter).
- **Optimizer.** Muon (Newton–Schulz-5 orthogonalised momentum, 0.95 Nesterov, with the RMS-matching update scale of
  Moonlight so one learning rate serves both optimizers) for all 2-D weight matrices; AdamW (β = 0.9/0.95) for
  embeddings, norms and scalar parameters. Weight decay 0.1, gradient clipping 1.0. In a short ablation (150M model) Muon reached
  0.024 lower BPB than AdamW after 1,000 steps (0.5B tokens).
- **Learning-rate schedule.** Warmup–stable–decay: linear warmup over 1,500 steps to 0.0015,
  constant until step 19,000, then a 1−sqrt decay to 0 over the last 5,000 steps
  (21% of training). Most of the late improvement comes in that decay: held-out FineWeb-2 BPB went from
  0.786 at its start to 0.738 at the end (Wikipedia 0.837 → 0.755).
- **Precision.** bf16 autocast with fp32 master weights; the Gated DeltaNet triangular inverse and state recurrence run
  in fp32/TF32.
- **Hardware.** NVIDIA RTX A6000 48 GB (PCIe), plain data parallel: 4 GPUs for the first 13k steps, then
  2 GPUs (same global batch). About 680 GPU-hours.

![validation BPB during pretraining](assets/pretrain_val_bpb.png)

## Evaluation

Held-out bits per byte (lower is better; tokenizer-independent, sliding window, stride 512) and KoBEST 0-shot accuracy, all models run through the same harness:

| model | BPB all / FineWeb-2 / Wikipedia | COPA | HellaSwag | SentiNeg | BoolQ | WiC |
|---|---|---|---|---|---|---|
| **this model** (1.0B) | **0.729 / 0.727 / 0.735** | 0.690 | 0.418 | 0.599 | 0.496 | 0.487 |
| EleutherAI/polyglot-ko-1.3b | 1.052 / 1.008 / 1.200 | 0.711 | 0.408 | 0.703 | 0.499 | 0.487 |
| skt/kogpt2-base-v2 (125M) | 1.092 / 1.073 / 1.157 | 0.584 | 0.318 | 0.615 | 0.502 | 0.490 |

 KMMLU 0-shot: 0.255 (chance 0.25; zero-shot letter scoring is dominated by answer-letter bias at this scale, so it is reported for reference only).

## Sample completions

One sample per prompt (seed 0, temperature 0.8, top-p 0.95, repetition penalty 1.1, up to 120 new tokens), unedited. The completions are fluent but contain factual errors (e.g. wrong population figures and an invented history of Hangul), so do not read them as facts.

> **대한민국의 수도는** 대한민국의 수도이다.  
> 대한민국  
> 대한민국의 수도(首都) 또는 약칭으로 수도를 규정하는 법령은 지방자치법 제164조와 동법 시행령 제32조다. 단, 수도의 개념에 포함하지 않는 도시도 많다. 이들 도시들은 광역자치단체를 설치하거나 광역시급 행정단위로서 특별시·광역시·특별자치시 및 도 등이 존재한다.  
>
> 인천광역시는 대한민국 최대의 도시이다. 70만 명 정도가 거주하고 있으며 수도권 인구의 약 절반을 차지하고 있다. 대한민국 5대 광역시 중의 하나이다.  
>
> 서울특별시에는 2천만 명이 거주하며 주로 서울  

> **조선 시대의 과거 제도는** 크게 문과와 무과(武科)로 구분되었는데, 조선 전기 관제의 가장 큰 특징은 과거 제도가 지방관의 출세 수단으로 사용되었다는 사실이다. 이는 지방관이 중앙의 부서를 장악함으로써 중앙집권의 체제를 구축하고자 했던 것과 밀접한 관련이 있다. 그 결과, 지방에는 중앙에서 임명된 관리가 파견됨으로써 중앙과의 유기적 관계가 형성되었다.  
> 무과는 전란이 빈번했던 후기부터 쇠퇴기에 걸쳐 시행되었으며, 국가에서 필요로 하는 전문 인력을 양성하는 데 목적이 있었다. 무과의 주요 과목은 육해공 각 3개 과목으로 구성되었고, 급제하면 무과에 응시  

> **광합성은 식물이** 태양 에너지를 흡수하여 탄수화물을 합성하는 과정이다. 광합성 과정에서 식물 세포는 엽록체를 통해 광전자 에너지인 전자 수용체(electron acceptor)를 흡수한다.  
>
> 전자수용체가 포함된 물 분자를 흡수한 이후, 엽록체는 엽록체에서 방출되는 광자 에너지원으로부터 에너지를 얻는다. 광자를 흡수하여 전자가 결합하게 되면 이 결합을 전기적으로 중성인 전자 수용체와 공유함으로써 전자와 결합된 에너지가 내부 합성을 통한 무기 인산 생성으로 전환된다. 생성된 유기물이 바로 탄소이다. 따라서 광합성의 핵심은 빛에 의해 전  

> **김치찌개를 맛있게 끓이려면 먼저** 재료를 준비해야 한다.  
> 우선 대파와 양파를 썰고, 돼지고기 목살은 한 입 크기로 자르고 , 도톰한 앞다리 살과 불고기감 소고기를 준비한다.  
> 김치는 무우 배추의 3잎 정도, 맛술이나 소주 약간을 섞어서 썰어준다. 그리고 고기는 앞다리살을 준비하고, 기름을 걷어내고 먹기 좋은 크기로 잘라 놓는다. 냄비에 고기를 넣고, 물을 붓고 된장 반 큰술을 넣고 푹 삶아 준다. 찌개가 끓기 시작하면 다시마 육수와 고추장으로 간을 맞춘다.  
> 그리고 돼지고기와 잘 익은 김치도 함께  

> **오늘 서울은 아침부터 비가 내리면서** 대기가 불안정해져 곳곳의 도로가 곳곳에서 통제되고 있습니다.  
> 오늘 오후 4시쯤부터 인천 강화, 경기도 김포 등 수도권과 서해안 지역에 호우 특보가 발효됐습니다.  
> 특히 서울과 경기 남부에 시간당 최대 20mm 안팎으로 강하게 내리는 곳이 있겠습니다.  
> 또 비구름 뒤로 산발적인 빗방울이 떨어지는 곳도 있겠고요.  
> 곳곳에서 천둥 번개를 동반한 강한 소나기도 쏟아질 것으로 보입니다.  
> 예상되는 강우량은 서울 남서 내륙에서 많게는 150mm 이상 예상됩니다.  
> 비의 양은 중부와 남부 지방 모두 30~  

> **인공지능 기술이 발전하면서 일자리에 미치는 영향은** 더욱 커지고 있습니다. 인공지능이 인간을 대체할 것이라는 전망이 나오는 가운데, 이러한 변화에 맞서기 위한 노력이 이루어지고 있습니다. 특히, 미래에는 인공지능 기술이 더 발전할 것으로 예상되면서 이에 대한 대비가 더욱 중요해지고 있는데요. 그렇다면 미래에 대비하는 교육은 어떤 방향으로 진행될까요? 오늘 IBK기업은행에서는 미래 사회의 인재상을 고려한 교육 방향성을 살펴보겠습니다. 4차 산업혁명 시대를 살아가는 우리에게 필요한 역량은 무엇일까요? 오늘은 미래를 준비하는 교육에서 중요하게 생각하는 역량을 살펴보려고 합니다. ■ 4차산업혁명..  
> 금융의 새로운 영역인 핀테크 스타트업! 핀테크 산업은 금융과 IT기술의 융합으로 탄생한 새로운 시장으로, 기존 은행 및  

> **The history of the Korean alphabet, Hangul, begins** with the vowel-numbering system in 1440 CE (Korean: Kyeonggisan Jujipunsil). The first consonant-vowel-picture script was the alphabetic writing system introduced by Samgak (Samgyecheok) and is based on the nodal point between throat and tongue. The first important stage in the development of Korean alphabetic writing system began when the Joseon Dynasty (1392–1897) changed from  

## Usage

Requires a CUDA GPU, PyTorch, Triton, `tokenizers` and `safetensors` (tested with PyTorch 2.8 + Triton 3.4). The model is not a `transformers`
architecture; load it with the included code:

```python
import sys
from huggingface_hub import snapshot_download
path = snapshot_download("shopkeeper/kor-finewiki-1b-base")
sys.path.insert(0, path)
from kollm.load import load_model
from kollm.generate import generate, special_ids

model, tok, _ = load_model(path)                       # bf16 on cuda
eot = special_ids(tok)["endoftext"]
ids = [eot] + tok.encode("대한민국의 수도는").ids        # documents start after <|endoftext|>
out = generate(model, ids, max_new_tokens=100, temperature=0.8, top_p=0.95, stop_ids={eot})
print(tok.decode(out))
```

Or interactively: `python complete.py` inside the downloaded folder.


## License and data attribution

Model weights and code: apache-2.0. Training data: FineWeb-2 and FineWeb-Edu (ODC-By 1.0, subject to Common Crawl's
terms of use) and Wikipedia (CC BY-SA 4.0).
