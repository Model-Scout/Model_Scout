---
license: mit
pretty_name: Crazyrouter Model Pricing Comparison
tags:
  - api-pricing
  - llm
  - ai-gateway
  - crazyrouter
  - model-comparison
  - openai
  - anthropic
  - gemini
size_categories:
  - n<1K
configs:
  - config_name: default
    data_files: pricing.csv


language:
  - en
  - ja
  - ko
  - ru
  - pt
---

# Crazyrouter Model Pricing Comparison

Per-1M-token API prices for 40 chat models, updated **2026-10-10**: the vendor's official list price where available, the same
model on Azure / AWS Bedrock / Google Vertex AI / OpenRouter where it is offered, and the price on
[Crazyrouter](https://crazyrouter.com/?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_01__en) (one API key, OpenAI/Anthropic/Gemini-compatible endpoints).

## Files

| File | What it holds |
|---|---|
| `pricing.csv` | One row per model, flat columns (see schema below). First seven columns are unchanged from earlier releases. |
| `pricing.json` | Same data with per-provider objects, plus cache-read / batch prices and source URLs. |

## Snapshot (2026-10-10)

Prices are USD per 1M tokens, `input / output`.
For tiered models, the table shows the first context tier; `pricing.json` includes every tier and its input-token limits.
Blank official prices mean no comparable official price is present in the source snapshot. They do not mean zero cost.

| Model | Vendor | Official | Crazyrouter | Savings |
|---|---|---|---|---|
| [`claude-opus-5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_02__en) | Anthropic | $5.00 / $25.00 | $3.25 / $16.25 | 35% |
| [`claude-opus-4-8`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_03__en) | Anthropic | $5.00 / $25.00 | $3.25 / $16.25 | 35% |
| [`claude-opus-4-7`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_04__en) | Anthropic | $5.00 / $25.00 | $3.25 / $16.25 | 35% |
| [`claude-sonnet-4-6`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_05__en) | Anthropic | $3.00 / $15.00 | $1.95 / $9.75 | 35% |
| [`claude-haiku-4-5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_06__en) | Anthropic | $1.00 / $5.00 | $0.65 / $3.25 | 35% |
| [`claude-fable-5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_07__en) | Anthropic | $10.00 / $50.00 | $6.50 / $32.50 | 35% |
| [`gpt-5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_08__en) | OpenAI | $1.25 / $10.00 | $0.8125 / $6.50 | 35% |
| [`gpt-5.5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_09__en) | OpenAI | $5.00 / $30.00 | $3.25 / $19.50 | 35% |
| [`gpt-5.4`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_10__en) | OpenAI | $2.50 / $15.00 | $1.625 / $9.75 | 35% |
| [`gpt-5.4-mini`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_11__en) | OpenAI | $0.75 / $4.50 | $0.4875 / $2.925 | 35% |
| [`gpt-5.6-sol`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_12__en) | OpenAI | $4.00 / $20.00 | $2.60 / $13.00 | 35% |
| [`gpt-6-astra`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_13__en) | OpenAI | $10.00 / $50.00 | $6.50 / $32.50 | 35% |
| [`gpt-5.3-codex`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_14__en) | OpenAI | $1.75 / $14.00 | $1.1375 / $9.10 | 35% |
| [`gpt-5-codex`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_15__en) | OpenAI | $1.25 / $10.00 | $0.8125 / $6.50 | 35% |
| [`gpt-4.1`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_16__en) | OpenAI | $2.00 / $8.00 | $1.30 / $5.20 | 35% |
| [`gpt-4.1-mini`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_17__en) | OpenAI | $0.40 / $1.60 | $0.26 / $1.04 | 35% |
| [`gpt-4o`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_18__en) | OpenAI | $2.50 / $10.00 | $1.625 / $6.50 | 35% |
| [`gpt-4o-mini`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_19__en) | OpenAI | $0.15 / $0.60 | $0.0975 / $0.39 | 35% |
| [`o3`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_20__en) | OpenAI | $2.00 / $8.00 | $2.00 / $8.00 | 0% |
| [`gemini-3.1-pro`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_21__en) | Google AI | $2.00 / $12.00 | $1.10 / $6.60 | 45% |
| [`gemini-3-flash`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_22__en) | Google AI | $0.50 / $3.00 | $0.165 / $1.32 | 57.6% |
| [`gemini-2.5-pro`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_23__en) | Google AI | $1.25 / $10.00 | $0.6875 / $5.50 | 45% |
| [`gemini-2.5-flash`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_24__en) | Google AI | $0.30 / $2.50 | $0.165 / $1.375 | 45% |
| [`gemini-2.5-flash-lite`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_25__en) | Google AI | $0.10 / $0.40 | $0.055 / $0.22 | 45% |
| [`kimi-k3`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_26__en) | Moonshot AI | $3.00 / $15.00 | $3.00 / $15.00 | 0% |
| [`kimi-k2.5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_27__en) | Moonshot AI | $0.60 / $3.00 | $0.60 / $3.15 | -4.2% |
| [`glm-5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_28__en) | Zhipu AI | $1.00 / $3.20 | $1.00 / $3.20 | 0% |
| [`qwen3.8-max`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_29__en) | Alibaba Cloud | $2.00 / $6.00 | $2.00 / $6.00 | 0% |
| [`MiniMax-M3`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_30__en) | MiniMax | $0.30 / $1.20 | $0.30 / $1.20 | 0% |
| [`claude-opus-5-5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_31__en) |  | — / — | $4.00 / $20.00 | — |
| [`qwen3.8-flash`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_32__en) |  | — / — | $0.15 / $0.47 | — |
| [`claude-sonnet-5-5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_33__en) |  | — / — | $2.00 / $10.00 | — |
| [`gpt-6-luna`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_34__en) |  | — / — | $0.065 / $0.325 | — |
| [`claude-haiku-5-5`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_35__en) |  | — / — | $0.10 / $0.50 | — |
| [`gpt-5.6-luna`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_36__en) |  | — / — | $0.13 / $0.78 | — |
| [`gpt-5.4-pro`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_37__en) |  | — / — | $30.00 / $180.00 | — |
| [`gpt-6-sol`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_38__en) |  | — / — | $1.30 / $6.50 | — |
| [`qwen3.8-omni-flash`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_39__en) |  | — / — | $0.15 / $0.47 | — |
| [`gpt-5.6-terra`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_40__en) |  | — / — | $1.30 / $7.80 | — |
| [`gpt-6.1-sol`](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_41__en) |  | — / — | $2.00 / $10.00 | — |

Savings = `1 − (crazyrouter_input + crazyrouter_output) / (official_input + official_output)`; a negative value means
Crazyrouter is more expensive for that model.

Each model name links to the current pricing table. Browse by vendor: [Anthropic](https://crazyrouter.com/en/models/anthropic?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_42__en) ·
[OpenAI](https://crazyrouter.com/en/models/openai?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_43__en) · [Google](https://crazyrouter.com/en/models/google?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_44__en) ·
[DeepSeek](https://crazyrouter.com/en/models/deepseek?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_45__en) · [all vendors](https://crazyrouter.com/en/models?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_46__en) ·
[full price table](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_47__en).

## Schema (`pricing.csv`)

| Column | Meaning |
|---|---|
| `model` | Model id as accepted by the Crazyrouter API |
| `provider` | Vendor that publishes the official price (, Alibaba Cloud, Anthropic, Google AI, MiniMax, Moonshot AI, OpenAI, Zhipu AI) |
| `crazyrouter_input_per_1m` / `crazyrouter_output_per_1m` | Crazyrouter list price for the default group, discount already applied |
| `direct_input_per_1m` / `direct_output_per_1m` | Vendor's official price |
| `savings_pct` | See formula above |
| `crazyrouter_cached_input_per_1m` / `direct_cached_input_per_1m` | Prompt-cache read price where published |
| `context_window` | Max input tokens per the vendor |
| `azure_*`, `bedrock_*`, `vertex_*`, `openrouter_*` | Same model on that platform; empty when not offered (coverage: azure 20, bedrock 6, vertex 11, openrouter 0) |
| `direct_pricing_url` | Vendor's pricing page |
| `crazyrouter_pricing_url` | Per-model comparison page on crazyrouter.com |
| `updated_at` | Date this row was generated |
| `billing_mode`, `price_tier`, `input_tokens_at_most` | Pricing method, displayed tier and its inclusive input-token limit; blank limit means unbounded |
| `official_snapshot_date` | Date of the external provider snapshot, separate from the live Crazyrouter fetch |

## Method

- Official, Azure, Bedrock, Vertex and OpenRouter prices come from LiteLLM's
  [`model_prices_and_context_window.json`](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json)
  (snapshot dated 2026-10-10), which tracks the vendors' published price pages.
- Crazyrouter prices are read live from `https://crazyrouter.com/api/pricing`?utm_source=huggingface&utm_campaign=model_pricing&utm_content=readme_48__en at build time
  (`model_ratio × $2 × group_ratio × discount` for ratio billing). For `tiered_expr`, coefficients in `billing_expr`
  are already USD per 1M tokens: apply the default-group ratio and discount exactly once. Long-context tiers can cost more.
- Unknown expression shapes fail the build rather than publishing legacy ratio prices. Request-dependent billing is not flattened.
- Token-billed models with an official comparison and current tiered text models are included. Image, video and audio models are on the
  [full pricing page](https://crazyrouter.com/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_49__en).
- Regenerated by `scripts/publish_model_pricing_huggingface.py` in the Crazyrouter repository; prices change often, so
  treat any row older than a month as historical.

## Load it

```python
from datasets import load_dataset
ds = load_dataset("xujfcn/Crazyrouter-Model-Pricing")
print(ds["train"].to_pandas().sort_values("savings_pct", ascending=False).head())
```

🔗 [Get an API key](https://crazyrouter.com/?utm_source=huggingface&utm_medium=dataset&utm_campaign=model_pricing&utm_content=readme_50__en) · 📚 [Docs](https://docs.crazyrouter.com?utm_source=huggingface&utm_campaign=model_pricing&utm_content=readme_51__en) · 🐦 [@metaviiii](https://twitter.com/metaviiii)

<!-- channel-localized-access -->

## API access: 日本語 / 한국어 / Русский / Português

Documentation below is localized. The interactive interfaces retain their existing languages. Updated 2026-10-10.

### 日本語：API 接続と料金

料金は USD 表示です。API 呼び出しは従量課金です。長いコンテキストでは料金区分が変わる場合があります。データセットの全区分を確認してください。

API キーは環境変数に設定し、公開しないでください。モデル名は現在のモデル一覧で確認できます。

[モデルと料金](https://crazyrouter.com/ja/pricing?utm_source=huggingface&utm_campaign=model_pricing&utm_content=guide_prices__ja&utm_medium=dataset) · [API キーを作成](https://crazyrouter.com/console/token?utm_source=huggingface&utm_campaign=model_pricing&utm_content=guide_api_key__ja&utm_medium=dataset)

### 한국어: API 연결 및 요금

요금은 USD 기준이며 API 호출은 사용량에 따라 청구됩니다. 긴 컨텍스트에는 다른 요금 구간이 적용될 수 있습니다. 데이터셋의 전체 구간을 확인하세요.

API 키는 환경 변수로 설정하고 공개하지 마세요. 현재 모델 목록에서 모델 이름을 확인할 수 있습니다.

[모델 및 요금](https://crazyrouter.com/ko/pricing?utm_source=huggingface&utm_campaign=model_pricing&utm_content=guide_prices__ko&utm_medium=dataset) · [API 키 만들기](https://crazyrouter.com/console/token?utm_source=huggingface&utm_campaign=model_pricing&utm_content=guide_api_key__ko&utm_medium=dataset)

### Русский: подключение API и цены

Цены указаны в USD. Вызовы API оплачиваются по использованию. Для длинного контекста может действовать другой тариф. Все диапазоны приведены в наборе данных.

Храните ключ API в переменной окружения и не публикуйте его. Имена моделей доступны в текущем каталоге.

[Модели и цены](https://crazyrouter.com/ru/pricing?utm_source=huggingface&utm_campaign=model_pricing&utm_content=guide_prices__ru&utm_medium=dataset) · [Создать ключ API](https://crazyrouter.com/console/token?utm_source=huggingface&utm_campaign=model_pricing&utm_content=guide_api_key__ru&utm_medium=dataset)

### Português: acesso à API e preços

Os preços são em USD. As chamadas de API são cobradas por uso. Contextos longos podem ter outra faixa de preço. Consulte todas as faixas no conjunto de dados.

Guarde a chave de API numa variável de ambiente e não a publique. Os nomes dos modelos estão no catálogo atual.

[Modelos e preços](https://crazyrouter.com/pt/pricing?utm_source=huggingface&utm_campaign=model_pricing&utm_content=guide_prices__pt&utm_medium=dataset) · [Criar chave de API](https://crazyrouter.com/console/token?utm_source=huggingface&utm_campaign=model_pricing&utm_content=guide_api_key__pt&utm_medium=dataset)

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://crazyrouter.com/v1", api_key=os.environ["CRAZYROUTER_API_KEY"])
response = client.chat.completions.create(
    model="gpt-4o-mini", messages=[{"role": "user", "content": "Hello"}], max_tokens=64
)
print(response.choices[0].message.content)
```
