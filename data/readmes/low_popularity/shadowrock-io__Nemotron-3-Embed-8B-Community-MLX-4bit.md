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
  - mlx
  - apple-silicon
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
library_name: mlx
model-index:
  - name: Nemotron-3-Embed-8B-Community-MLX-4bit
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
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.95644
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.76267
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.94053
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.79763
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.88571
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.76243
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.76165
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.76924
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.4199
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
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
            value: 0.8338
        source:
          name: ShadowRock eval (raw JSON)
          url: https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results
---
<a href="https://shadowrock.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://a.shadowrock.team/assets/logos/full/shadowrock-logo-white.svg">
    <img alt="ShadowRock" src="https://a.shadowrock.team/assets/logos/full/shadowrock-logo-black.svg" width="340">
  </picture>
</a>

# Nemotron-3-Embed-8B — Community MLX 4-bit

**Unofficial community quantization — not an NVIDIA release.**

4-bit MLX build of [nvidia/Nemotron-3-Embed-8B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16) (revision [`8ca3ff38`](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16/tree/8ca3ff382cf1de715e05acac8b553e0a084680d0)), the top-ranked open embedding model on RTEB at time of writing, quantized for Apple-Silicon Macs. All credit for the base model and its training belongs to NVIDIA; this repo only changes the weight storage format. 4.7 GB on disk; runs in the memory budget of a 16–24 GB machine. Embedding cosine fidelity vs the BF16 reference is 0.991, and retrieval scores on our regression subset sit within 0.004 nDCG@10 of BF16.

> [!NOTE]
> The Hugging Face file widget reports "~1B params, BF16 · U32". That is a counting artifact: MLX packs eight 4-bit weights into each uint32 element, so the scanner sees one eighth of the logical weights. The model is the full **8B parameters** of the base; BF16 tensors are the unquantized embeddings and per-group quantization scales.

The base model is a Ministral3 encoder with **bidirectional attention** and mean pooling. Stock `mlx-lm` runs causal attention and would produce wrong embeddings while appearing to work, so this repo ships a small standalone module (`nemotron3_embed_mlx.py`) that implements the encoder faithfully. Our fixture suite includes a suffix-sensitivity probe confirming bidirectional attention is active in this build.

## Use

```python
import importlib.util
from huggingface_hub import snapshot_download

path = snapshot_download("shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit")
spec = importlib.util.spec_from_file_location("nemo_mlx", f"{path}/nemotron3_embed_mlx.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

model, tok = mod.load(path)
docs = mod.encode(model, tok, ["passage: MLX runs on Apple Silicon."])
qry  = mod.encode(model, tok, ["query: what does MLX run on?"])
print((docs @ qry.T))  # cosine similarity (outputs are L2-normalized)
```

Prefixes matter: prepend `query: ` to queries and `passage: ` to documents, matching the base model card. Nothing adds them for you.

Embeddings are 4096-dim, L2-normalized, mean-pooled. Matryoshka truncation to 2048 or 1024 dims works as in the base model: slice, then re-normalize.

## Why group size 32

Local sweeps on an Apple M5 Pro (24 GB), scored as cosine fidelity against the BF16 reference on fixed token-ID-locked fixtures:

| Recipe | Fidelity (mean) | Fidelity (min) | Size |
|---|---|---|---|
| **4-bit, gs32 (this repo)** | **0.9912** | **0.9901** | **4.7 GB** |
| 4-bit, gs64 | 0.9884 | 0.9868 | 4.5 GB |
| 6-bit, gs64 | 0.9991 | 0.9990 | 6.5 GB |

6-bit is near-lossless if you have the memory headroom; the conversion script in the source repo reproduces it with `--bits 6`. We ship gs32 as the best fidelity-per-GB at 4-bit.

## MTEB retrieval regression vs BF16

MTEB (v2, mteb 2.18.12) on the laptop subset of our frozen regression suite. BF16 baseline computed with the same harness, adapter, and prefixes on an A100:

| Task (nDCG@10) | BF16 | MLX 4-bit gs32 | Delta |
|---|---|---|---|
| NFCorpus | 0.4237 | 0.4199 | −0.0038 |
| SciFact | 0.8330 | 0.8338 | +0.0008 |

Gate: per-task loss ≤ 0.01. Both pass. Raw mteb result JSON lives in this repo under [`results/`](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results); rerun with mteb 2.18.12 and the pinned harness from the source repo to verify.

Pooling fixtures (batch-vs-single, batch order, padding invariance, unit norm, prefix discrimination, suffix sensitivity): all pass; cosines ≥ 0.99994 on invariance checks.

## RTEB benchmarks vs NVIDIA's published numbers

The base model's public identity is its [RTEB leaderboard](https://mteb-leaderboard.hf.space/benchmark/RTEB(beta)) ranking (Finance #1, German #1, Code #2, Healthcare #4, Legal #4). We ran the open RTEB datasets from those domains on this 4-bit MLX build; the comparison column is NVIDIA's official per-task result from the [mteb results repo](https://github.com/embeddings-benchmark/results), not our reproduction.

| Task (nDCG@10) | NVIDIA official BF16 | MLX 4-bit (this repo) | Delta |
|---|---|---|---|
| HumanEvalRetrieval | 1.0000 | 1.0000 | ±0.0000 |
| MBPPRetrieval | 0.9560 | 0.9564 | +0.0004 |
| WikiSQLRetrieval | 0.9950 | 0.9946 | −0.0004 |
| DS1000Retrieval | 0.7646 | 0.7627 | −0.0019 |
| FinanceBenchRetrieval | 0.9526 | 0.9405 | −0.0121* |
| HC3FinanceRetrieval | 0.7981 | 0.7976 | −0.0005 |
| FinQARetrieval | 0.8871 | 0.8857 | −0.0014 |
| LegalQuAD (German) | 0.7718 | 0.7624 | −0.0094 |
| LegalSummarization | 0.7666 | 0.7617 | −0.0050 |
| ChatDoctorRetrieval | 0.7690 | 0.7692 | +0.0002 |

\* FinanceBench has 150 queries — one ranking flip moves the score ~0.007. The CUDA quants score at or above official on this task (FP8 +0.0006, NVFP4 +0.0019), so we read this as small-task noise rather than systematic 4-bit loss, and report it as measured. Mean delta −0.0030 across the 10 tasks — the same 10-task set appears in the [FP8](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-FP8) and [NVFP4](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4) cards for direct comparison (those builds add two AILA legal tasks not run here). The private RTEB datasets can only be run by the MTEB team, so this table covers the open subset.

## Performance

Test device: **MacBook Pro, Apple M5 Pro** — 15-core CPU (5 super / 10 performance), 16-core GPU, **24 GB unified memory**, macOS 27. The model needs ~5 GB of that budget, so 16 GB machines fit with room for a working set.

Batch size 8, real token counts:

| Input length | Texts/s | Tokens/s | p50 batch latency |
|---|---|---|---|
| ~28 tok (short query) | 39.0 | 1,092 | 0.21 s |
| ~102 tok | 13.5 | 1,372 | 0.60 s |
| ~512 tok | 3.5 | 1,392 | 2.3 s |
| ~2,048 tok | 0.8 | 1,271 | 9.9 s |

Throughput saturates near 1,300–1,400 tokens/s at document lengths (memory-bandwidth-bound); larger batches add latency, not throughput. For mixed-length corpora, sort by length before batching: padding to the longest batch member dominates cost otherwise.

## Quantization details

- Method: `mlx.nn.quantize`, affine, 4-bit, group size 32, applied uniformly to all linear layers; embeddings and norms untouched. No calibration data (data-free quantization).
- Converted with [`scripts/convert_8b.py`](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/blob/main/scripts/convert_8b.py) (in this repo), from base revision `8ca3ff382cf1de715e05acac8b553e0a084680d0`.
- Raw eval JSON ships under [`results/`](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/results); the fixture/eval harness ships under [`scripts/`](https://huggingface.co/shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit/tree/main/scripts).

## Caveats


- The regression subset is English retrieval; the multilingual and long-document tasks in the full suite run on the CUDA artifacts, not this one. Expect the base model's multilingual behavior with 4-bit noise on top, unmeasured here.
- `mlx-embeddings`/`mlx-lm` do not load this architecture correctly (causal attention). Use the bundled module.
- Quantization was validated on macOS 27 / mlx 0.29; older mlx releases may not support the quantized layout.

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
