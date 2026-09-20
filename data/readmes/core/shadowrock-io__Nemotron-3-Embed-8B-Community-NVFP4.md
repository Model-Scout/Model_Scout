---
license: other
license_name: openmdw-1.1
license_link: LICENSE
base_model: nvidia/Nemotron-3-Embed-8B-BF16
base_model_relation: quantized
pipeline_tag: sentence-similarity
inference: false
quantized_by: shadowrock-io
metrics:
  - ndcg_at_10
tags:
  - nvfp4
  - modelopt
  - fp4
  - blackwell
  - vllm
  - embeddings
  - text-embeddings
  - feature-extraction
  - retrieval
  - semantic-search
  - rag
  - mteb
  - nemotron
  - ministral3
  - quantized
  - safetensors
  - 4-bit
  - information-retrieval
  - dense-retrieval
  - vector-search
  - matryoshka
  - arxiv:2502.13595
language:
  - multilingual
  - en
  - ar
  - as
  - bn
  - bg
  - zh
  - da
  - nl
  - fi
  - fr
  - de
  - hi
  - id
  - it
  - ja
  - ko
  - ms
  - mr
  - ne
  - no
  - fa
  - pt
  - ro
  - ru
  - es
  - sw
  - sv
  - ta
  - te
  - th
  - uk
  - ur
  - vi
library_name: vllm
model-index:
  - name: Nemotron-3-Embed-8B-Community-NVFP4
    results:
      - task:
          type: Retrieval
        dataset:
          name: MTEB HumanEvalRetrieval
          type: embedding-benchmark/HumanEval
          config: default
          split: test
          revision: ed1f48aca747f10bac146795328e2f03326e7625
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 1.0
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB MBPPRetrieval
          type: embedding-benchmark/MBPP
          config: default
          split: test
          revision: 586a1fd6a0c63fdeda3b49c0293559a81c79cdec
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.95722
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB WikiSQLRetrieval
          type: embedding-benchmark/WikiSQL_mteb
          config: default
          split: test
          revision: 4e099ab42dffd49d72c1472f451371e53343e3d7
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.99459
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB DS1000Retrieval
          type: embedding-benchmark/DS1000
          config: default
          split: test
          revision: 25cd4dc8172e799235d83c66439b6b7b8e6583ec
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.76043
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB FinanceBenchRetrieval
          type: embedding-benchmark/FinanceBench
          config: default
          split: test
          revision: e68478442112cae36b70a216f52cc2777acf0a7e
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.95452
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB HC3FinanceRetrieval
          type: embedding-benchmark/HC3Finance
          config: default
          split: test
          revision: fda6fad068f2ed814d99f29dc95dbb28ac586943
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.79529
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB FinQARetrieval
          type: embedding-benchmark/FinQA
          config: default
          split: test
          revision: bdd1903ce03153129480bfc14b710e3d612c1efd
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.88238
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB LegalQuAD
          type: mteb/LegalQuAD
          config: default
          split: test
          revision: 37aa6cfb01d48960b0f8e3f17d6e3d99bf1ebc3e
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.76582
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB LegalSummarization
          type: mteb/legal_summarization
          config: default
          split: test
          revision: 3bb1a05c66872889662af04c5691c14489cebd72
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.76423
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB ChatDoctorRetrieval
          type: embedding-benchmark/ChatDoctor_HealthCareMagic
          config: default
          split: test
          revision: 50c2986fedffa33b38afd5c1752026f8e9e5ed1d
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.76902
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB AILAStatutes
          type: mteb/AILA_statutes
          config: default
          split: test
          revision: ebfcd844eadd3d667efa3c57fc5c8c87f5c2867e
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.58951
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB AILACasedocs
          type: mteb/AILA_casedocs
          config: default
          split: test
          revision: 4106e6bcc72e0698d714ea8b101355e3e238431a
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.48622
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB NFCorpus
          type: mteb/nfcorpus
          config: default
          split: test
          revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.42288
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB SciFact
          type: mteb/scifact
          config: default
          split: test
          revision: d56462d0e63a25450459c4f213e49ffdb866f7f9
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.83381
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB FiQA2018
          type: mteb/fiqa
          config: default
          split: test
          revision: 27a168819829fe9bcd655c2df245fb19452e8e06
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.65296
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB ArguAna
          type: mteb/arguana
          config: default
          split: test
          revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.63134
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB TRECCOVID
          type: mteb/trec-covid
          config: default
          split: test
          revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.86058
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB MIRACLRetrievalHardNegatives (sw)
          type: mteb/MIRACLRetrievalHardNegatives
          config: sw
          split: dev
          revision: d7d94fa4b946cec4a27c84653aa0cf6b33f74a3c
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.79704
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
      - task:
          type: Retrieval
        dataset:
          name: MTEB LEMBNarrativeQARetrieval
          type: dwzhu/LongEmbed
          config: default
          split: test
          revision: 6e346642246bfb4928c560ee08640dc84d074e8c
        metrics:
          - type: ndcg_at_10
            name: NDCG@10
            value: 0.6979
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/tree/main/results
---
<a href="https://shadowrock.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://a.shadowrock.team/assets/logos/full/shadowrock-logo-white.svg">
    <img alt="ShadowRock" src="https://a.shadowrock.team/assets/logos/full/shadowrock-logo-black.svg" width="340">
  </picture>
</a>

# Nemotron-3-Embed-8B — Community NVFP4

**Unofficial community quantization — not an NVIDIA release.**

NVFP4 build of [nvidia/Nemotron-3-Embed-8B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16) (revision [`8ca3ff38`](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16/tree/8ca3ff382cf1de715e05acac8b553e0a084680d0)), the top-ranked open embedding model on the RTEB leaderboard at time of writing. All credit for the base model belongs to NVIDIA; this repo only changes the weight storage format. NVFP4 is Blackwell's native 4-bit format — ~3.5× smaller than BF16 with FP4 tensor-core execution on SM100/SM120 GPUs — and on the benchmarks where this model leads the leaderboard, the quantized scores land within 0.008 of NVIDIA's own published numbers.

Pick this variant for Blackwell GPUs where memory is the constraint. The companion [FP8 build](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-FP8) is closer to lossless and runs natively on Ada/Hopper too; the [MLX 4-bit build](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit) serves Apple-Silicon Macs.

## Benchmarks vs the unquantized model

Comparison column = NVIDIA's official per-task results from the [mteb results repo](https://github.com/embeddings-benchmark/results) — their numbers, not our reproduction. Our runs: mteb 2.18.12, vLLM 0.26.0, mean pooling, `query: `/`passage: ` prefixes, max length 8192 (NVIDIA evaluated at 4096; few documents in these tasks exceed either limit). Tasks are the open (public) RTEB datasets in the domains where the base model ranks top-4 on the [RTEB leaderboard](https://mteb-leaderboard.hf.space/benchmark/RTEB(beta)): Finance #1, German #1, Code #2, Healthcare #4, Legal #4.

| Task (nDCG@10) | NVIDIA official BF16 | NVFP4 (this repo) | Delta |
|---|---|---|---|
| HumanEvalRetrieval | 1.0000 | 1.0000 | ±0.0000 |
| MBPPRetrieval | 0.9560 | 0.9572 | +0.0012 |
| WikiSQLRetrieval | 0.9950 | 0.9946 | −0.0004 |
| DS1000Retrieval | 0.7646 | 0.7604 | −0.0042 |
| FinanceBenchRetrieval | 0.9526 | 0.9545 | +0.0019 |
| HC3FinanceRetrieval | 0.7981 | 0.7953 | −0.0028 |
| FinQARetrieval | 0.8871 | 0.8824 | −0.0047 |
| LegalQuAD (German) | 0.7718 | 0.7658 | −0.0060 |
| LegalSummarization | 0.7666 | 0.7642 | −0.0024 |
| ChatDoctorRetrieval | 0.7690 | 0.7690 | ±0.0000 |
| AILAStatutes | 0.5826 | 0.5895 | +0.0069 |
| AILACasedocs | 0.4942 | 0.4862 | −0.0080 |

Mean delta −0.0015 across all 12 tasks; −0.0017 on the 10-task subset shared by all three community builds (the two AILA legal tasks were run only on the CUDA builds). The private RTEB datasets can only be run by the MTEB team, so this table covers the open subset.

### Regression vs our own BF16 baseline (identical harness both sides)

BF16 baseline computed with the same code, adapter, prefixes, and pins on an A100. Gate: per-task nDCG@10 loss ≤ 0.01.

| Task | BF16 | NVFP4 | Delta | Gate |
|---|---|---|---|---|
| NFCorpus | 0.4237 | 0.4229 | −0.0008 | pass |
| SciFact | 0.8330 | 0.8338 | +0.0008 | pass |
| FiQA2018 | 0.6564 | 0.6530 | −0.0035 | pass |
| ArguAna | 0.6314 | 0.6313 | −0.0000 | pass |
| TRECCOVID | 0.8710 | 0.8606 | −0.0105 | marginal* |
| MIRACL-sw (held-out lang) | 0.8027 | 0.7970 | −0.0056 | pass |
| LEMBNarrativeQA (long-doc) | 0.7005 | 0.6979 | −0.0026 | pass |

\* TRECCOVID has 50 queries — the highest-variance task in the suite. The FP8 companion dips on the same task (−0.0076), so the dip is shared across quant formats and amplified by 4-bit; we report it as measured rather than excluding it. Embedding-level fidelity vs BF16 on token-ID-locked fixtures: cosine 0.9901–0.9930. Raw result JSON ships under `results/`.

## Serving with vLLM

Requires a Blackwell GPU (SM100/SM120) for native FP4 execution.

```python
from vllm import LLM
from vllm.config import PoolerConfig

llm = LLM(
    model="shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4",
    runner="pooling",
    pooler_config=PoolerConfig(seq_pooling_type="MEAN"),  # default LAST is silently wrong
    max_model_len=8192,
)
out = llm.embed(["query: what is NVFP4?", "passage: Blackwell's native 4-bit format."])
```

**Required patch for vLLM ≤ 0.26.0**: vLLM's pooling adapter replaces the checkpoint's absent `lm_head` with a placeholder layer, and `ModelOptNvFp4LinearMethod.process_weights_after_loading` crashes on the placeholder's meta tensors. Run [`scripts/patch_modelopt_guard.py`](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/blob/main/scripts/patch_modelopt_guard.py) once against your vLLM install before loading (idempotent; an upstream fix has been proposed).

Notes that matter for correct embeddings:
- **Pooling must be MEAN** and attention is bidirectional; both come from the checkpoint config, but the pooler override above guards against defaults.
- **Prefixes are your job**: `query: ` / `passage: `. The server does not add them.
- Texts longer than `max_model_len` are rejected by vLLM's pooling runner — truncate at the tokenizer (`truncation=True, max_length=8192`) and pass token IDs.
- Embeddings are 4096-dim; L2-normalize before use. Matryoshka truncation (2048/1024): slice, then re-normalize.

Measured on: GeForce RTX 5070 Ti (SM120) and RTX PRO 6000 (Blackwell), vLLM 0.26.0, CUDA 12.8.

## Quantization details

- Method: NVIDIA TensorRT Model Optimizer (ModelOpt) NVFP4 post-training quantization — FP4 weights with per-block FP8 scales, MLP-focused config per current ModelOpt accuracy guidance; embeddings, norms, and pooling untouched. Full module inventory: [`quantization/module_inventory.json`](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4/blob/main/quantization/module_inventory.json).
- Derived in a fresh process from the pinned BF16 snapshot.
- Calibration: ~1k public samples from MS MARCO and MIRACL **train** splits, token-bucketed (32–16k tokens) with real prefix distribution. MS MARCO is research-licensed, so the manifest ships dataset IDs + a deterministic builder script, not text. Eval-set contamination audit (by ID and content hash) included; Swahili and Telugu were held out of calibration entirely, with Swahili evaluated as the regression suite's held-out language.
- Quantize/eval scripts ship under `scripts/`; raw eval JSON under `results/`.

## Caveats

- "Blackwell-native format" is a statement about the artifact; verified FP4 kernel execution is claimed only for the GPUs and vLLM build listed above.
- TRECCOVID's marginal delta is disclosed above rather than averaged away. If your workload resembles high-variance biomedical retrieval, prefer the FP8 build.
- Multilingual evidence: one held-out language (Swahili, hard-negatives variant) plus German LegalQuAD. Telugu was also held out of calibration but not evaluated; full-corpus MIRACL was excluded for compute cost.

## Intended use & limitations

Intended uses are the base model's: dense retrieval, semantic search, and RAG indexing over text corpora, with `query: `/`passage: ` prefixed inputs. The base card's intended-use, safety, and language-coverage statements — [nvidia/Nemotron-3-Embed-8B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16) — carry over unchanged; quantization alters none of the model's behavior boundaries, only its numeric precision. Our evaluation establishes parity on the benchmarks listed above and nothing beyond them: other languages, domains, sequence-length regimes, and hardware/runtime combinations inherit the base model's behavior with quantization noise that we have not measured there.

## Attribution & citation

Quantization, validation harness, and card by [Matt Busi](https://www.linkedin.com/in/matt-busi) ([@mattbusi](https://huggingface.co/mattbusi) on Hugging Face) at [ShadowRock](https://shadowrock.io). If you use this build, cite the NVIDIA base model — the embedding quality is theirs:

```bibtex
@misc{nvidia2026nemotron3embed,
  title  = {Nemotron-3-Embed-8B},
  author = {NVIDIA},
  year   = {2026},
  url    = {https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16}
}
```

## License

OpenMDW-1.1, inherited from the base model (see `LICENSE`). `NOTICE` carries the upstream Apache-2.0 attribution for the Ministral component plus our modification statement. Community build by [ShadowRock](https://shadowrock.io); no NVIDIA affiliation or endorsement.

## About ShadowRock

[ShadowRock](https://shadowrock.io) is an AI-specialized systems integrator and Zendesk Premier Partner. We help businesses get real value from their go-to-market technology, from CRM and support platforms to applied AI like the models in this collection. Find us at [shadowrock.io](https://shadowrock.io) or on [LinkedIn](https://www.linkedin.com/company/shadowrock).
