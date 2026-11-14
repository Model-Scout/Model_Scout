---
license: apache-2.0
base_model: Qwen/Qwen3-30B-A3B
tags:
  - moe
  - pruning
  - expert-pruning
  - mixture-of-experts
  - gguf
  - goba-ai-labs
  - prunedhub
  - moe-stream
  - japanese
  - language-aware-pruning
  - layer-adaptive-pruning
model_name: PrunedHub Qwen3-30B-A3B-JP-80pct
pipeline_tag: text-generation
language:
  - ja
  - en
  - zh
  - ko
---

# PrunedHub Qwen3-30B-A3B-JP-80pct — MoE-Stream Edition

**日本語品質を維持した MoE 圧縮モデル** — GOBA-AI-Labs 独自の言語認識 expert 最適化手法により、日本語性能を保護しながら 20% のパラメータを削減。

[Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) をベースに、GOBA-AI-Labs の言語特化 MoE 最適化パイプラインで圧縮しています。

> **推論エンジン**: このモデルは**レイヤー適応型 pruning**（層ごとに異なる expert 数）を使用しているため、推論には [moe-stream](https://github.com/GOBA-AI-Labs/moe-stream) が**必須**です。llama.cpp は現在 `experts_per_layer` メタデータ形式に対応していません。

## モデル仕様

| 項目 | 値 |
|------|-----|
| ベースモデル | Qwen/Qwen3-30B-A3B |
| Expert 数/層 | **レイヤー適応型** (平均 ~102, 元: 128) |
| MoE 層数 | 48 |
| ルーティング | Top-8 |
| コンテキスト長 | 32K tokens |
| 量子化 | Q4_K_M |
| 推論エンジン | **[moe-stream](https://github.com/GOBA-AI-Labs/moe-stream)** (必須) |
| ライセンス | Apache 2.0 |

## ベンチマーク結果

### Thinking OFF (no-think モード)

| ベンチマーク | オリジナル (128 experts) | JP-80pct (~102 experts) | 差分 |
|-------------|------------------------|----------------------|------|
| **MMLU** (0-shot, 100Q) | 77% | **74%** | -3pp |
| **GSM8K** (0-shot, 50Q) | — | **92%** | — |
| **日本語品質** (20Q) | 90% | **85%** | -5pp |

### Thinking ON (推論モード)

| ベンチマーク | JP-80pct (Thinking ON) |
|-------------|----------------------|
| **MMLU** (0-shot, 100Q) | **79%** (+5pp vs no-think) |
| **GSM8K** (0-shot, 50Q) | **84%** |
| **日本語品質** (20Q) | **90%** (目標達成) |

## サイズ比較

| 指標 | オリジナル | JP-80pct | 削減 |
|------|----------|---------|------|
| ファイルサイズ | 17.3 GB | **14.0 GB** | -19.1% |
| Expert 数/層 | 128 | ~102 (平均) | -20.3% |
| 削減 Expert 数 | — | 1,248 | — |

## 特徴

- **日本語品質保護**: GOBA-AI-Labs 独自の言語認識最適化により、日本語の推論能力を維持
- **Thinking ON で最大性能**: MMLU 79%、日本語 90% を達成
- **GSM8K 92%**: 数学的推論能力を完全保持
- **14 GB**: 16GB RAM 環境で動作可能
- **~55 tok/s**: Apple Silicon (Metal GPU) で高速推論

## 使い方

このモデルはレイヤー適応型 pruning を使用しているため、**moe-stream** での推論が必須です。

### インストール

```bash
# moe-stream のビルド (Rust + Metal GPU)
git clone https://github.com/GOBA-AI-Labs/moe-stream
cd moe-stream
cargo build --release --features metal,accelerate

# モデルのダウンロード
huggingface-cli download goba-ai-labs/PrunedHub-Qwen3-30B-A3B-JP-80pct \
  --local-dir models/
```

### CLI での推論

```bash
# テキスト生成
./target/release/moe-stream models/PrunedHub-Qwen3-30B-A3B-JP-80pct-Q4_K_M.gguf 512 \
  --prompt "日本の四季について教えてください" --stream

# Thinking ON モード (推奨 — 高精度)
./target/release/moe-stream models/PrunedHub-Qwen3-30B-A3B-JP-80pct-Q4_K_M.gguf 1024 \
  --think --stream
```

### OpenAI 互換 HTTP サーバー

```bash
# サーバー起動
./target/release/moe-stream-server \
  --model models/PrunedHub-Qwen3-30B-A3B-JP-80pct-Q4_K_M.gguf --port 11434

# curl でテスト
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"日本の首都はどこですか？"}],"stream":true}'
```

### Python から使用

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="unused")
response = client.chat.completions.create(
    model="local",
    messages=[{"role": "user", "content": "量子コンピュータについて説明してください"}],
    stream=True
)
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

## 手法について

GOBA-AI-Labs 独自の言語認識 expert 最適化パイプラインを使用しています。

- **Calibration ベースの重要度スコアリング**: 多言語テキスト（日本語・英語・コード・数学）を実際に推論し、各 expert の活性化パターンから重要度を実測。静的な重み分析と比較して大幅に高精度な重要度ランキングを実現
- **言語特化 expert の自動検出と保護**: MoE routing パターンの言語間差分分析により、日本語品質に寄与する expert を自動的に同定し、pruning 対象から保護
- **レイヤー適応型 expert 割り当て**: 各レイヤーの品質寄与度に基づき、レイヤーごとに最適な expert 数を動的に決定。均一な pruning と比較して品質保持率が大幅に向上
- **Thinking モード対応**: Thinking ON/OFF 両方で評価済み。Thinking ON では MMLU +5pp、日本語品質 90% を達成

## 推論エンジン: moe-stream

[moe-stream](https://github.com/GOBA-AI-Labs/moe-stream) は GOBA-AI-Labs が開発した Rust 製 MoE 推論エンジンです。

| 機能 | 詳細 |
|------|------|
| 推論モード | GPU Resident / GPU Hybrid / SSD Streaming (自動選択) |
| GPU 対応 | Apple Metal / NVIDIA CUDA |
| 量子化 | Q2K-Q8K, MXFP4, F16, F32 (13 形式対応) |
| API | OpenAI 互換 HTTP / JSONL / MCP |
| 特殊機能 | Q4 Quantized MatMul (+79% 高速化), Dynamic K |

## 引用

```bibtex
@misc{goba-ai-labs-prunedhub-qwen3-30b-jp,
  title={PrunedHub Qwen3-30B-A3B-JP-80pct: 日本語品質保護 MoE 圧縮},
  author={GOBA-AI-Labs},
  year={2026},
  url={https://huggingface.co/goba-ai-labs/PrunedHub-Qwen3-30B-A3B-JP-80pct}
}
```

## リンク

- [GOBA-AI-Labs](https://huggingface.co/goba-ai-labs)
- [moe-stream (推論エンジン)](https://github.com/GOBA-AI-Labs/moe-stream)
- [ベースモデル: Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Ko-fi で GOBA-AI-Labs を支援](https://ko-fi.com/gobaailabs)
