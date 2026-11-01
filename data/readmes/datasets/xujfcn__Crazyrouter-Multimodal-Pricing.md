---
license: mit
pretty_name: Crazyrouter Multimodal Pricing
tags:
  - api-pricing
  - multimodal
  - image-generation
  - video-generation
  - audio-generation
  - 3d-generation
  - ai-gateway
  - crazyrouter
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

# Crazyrouter Multimodal Pricing

Live default-group pricing for image, video, audio, music, and 3D model APIs on **2026-10-11**.
The dataset keeps the provider's original billing unit: per image, per second, per request,
or per 1M output tokens. It does not convert media prices into text-token prices.

## Snapshot

**421 rule rows** across 57 models (3d: 3 rows, audio: 1 rows, image: 28 rows, video: 389 rows).
Structured image/video matrices are expanded one row per capability and parameter combination.
Text-only or unpriced API entries are omitted (120 API entries omitted).

| File | Contents |
|---|---|
| `pricing.csv` | Flat, queryable rule-level dataset |
| `pricing.json` | Full API records, generated rows, and omission reasons |

## Important fields

| Field | Meaning |
|---|---|
| `crazyrouter_price_usd` | Default-group Crazyrouter price in USD for the row's native unit |
| `billing_mode` / `billing_unit` | `per_image`, `per_second`, `per_request`, or `per_output_token` and its display unit |
| `capability_bucket` | `t2i`, `i2i`, `t2v`, `i2v`, `reference`, `start_end`, and similar capability bucket |
| `resolution`, `quality`, `duration_seconds`, `audio`, `video_input` | Structured pricing dimensions when supplied by the API |
| `official_price` / `official_currency` / `official_price_usd` | Provider reference price retained exactly as returned |
| `crazyrouter_price_basis` | Structured platform base price or legacy model price times default-group discount |
| `verification_status` / `verification_notes` | Price verification metadata from the production pricing registry |

## Method and sources

Every row is sourced from the public [Crazyrouter pricing API](https://crazyrouter.com/api/pricing).
Model links point to the [Crazyrouter price table](https://crazyrouter.com/en/pricing?utm_source=huggingface&utm_medium=dataset&utm_campaign=multimodal_pricing&utm_content=readme_02__en).
Structured rules are the preferred source. Legacy rows are included only for explicitly classified
non-text models with a positive fixed price; unknown prices are never represented as zero.

Prices change frequently. Treat this snapshot as historical after one month.

## Load it

```python
from datasets import load_dataset
ds = load_dataset("xujfcn/Crazyrouter-Multimodal-Pricing")
print(ds["train"].to_pandas().query("modality == 'video'").head())
```

🔗 [Get an API key](https://crazyrouter.com/?utm_source=huggingface&utm_medium=dataset&utm_campaign=multimodal_pricing&utm_content=readme_03__en) · 📚 [Docs](https://docs.crazyrouter.com?utm_source=huggingface&utm_campaign=multimodal_pricing&utm_content=readme_04__en)

<!-- channel-localized-access -->

## API access: 日本語 / 한국어 / Русский / Português

Documentation below is localized. The interactive interfaces retain their existing languages. Updated 2026-10-10.

### 日本語：API 接続と料金

料金は USD 表示です。API 呼び出しは従量課金です。長いコンテキストでは料金区分が変わる場合があります。データセットの全区分を確認してください。

API キーは環境変数に設定し、公開しないでください。モデル名は現在のモデル一覧で確認できます。

[モデルと料金](https://crazyrouter.com/ja/pricing?utm_source=huggingface&utm_campaign=multimodal_pricing&utm_content=guide_prices__ja&utm_medium=dataset) · [API キーを作成](https://crazyrouter.com/console/token?utm_source=huggingface&utm_campaign=multimodal_pricing&utm_content=guide_api_key__ja&utm_medium=dataset)

### 한국어: API 연결 및 요금

요금은 USD 기준이며 API 호출은 사용량에 따라 청구됩니다. 긴 컨텍스트에는 다른 요금 구간이 적용될 수 있습니다. 데이터셋의 전체 구간을 확인하세요.

API 키는 환경 변수로 설정하고 공개하지 마세요. 현재 모델 목록에서 모델 이름을 확인할 수 있습니다.

[모델 및 요금](https://crazyrouter.com/ko/pricing?utm_source=huggingface&utm_campaign=multimodal_pricing&utm_content=guide_prices__ko&utm_medium=dataset) · [API 키 만들기](https://crazyrouter.com/console/token?utm_source=huggingface&utm_campaign=multimodal_pricing&utm_content=guide_api_key__ko&utm_medium=dataset)

### Русский: подключение API и цены

Цены указаны в USD. Вызовы API оплачиваются по использованию. Для длинного контекста может действовать другой тариф. Все диапазоны приведены в наборе данных.

Храните ключ API в переменной окружения и не публикуйте его. Имена моделей доступны в текущем каталоге.

[Модели и цены](https://crazyrouter.com/ru/pricing?utm_source=huggingface&utm_campaign=multimodal_pricing&utm_content=guide_prices__ru&utm_medium=dataset) · [Создать ключ API](https://crazyrouter.com/console/token?utm_source=huggingface&utm_campaign=multimodal_pricing&utm_content=guide_api_key__ru&utm_medium=dataset)

### Português: acesso à API e preços

Os preços são em USD. As chamadas de API são cobradas por uso. Contextos longos podem ter outra faixa de preço. Consulte todas as faixas no conjunto de dados.

Guarde a chave de API numa variável de ambiente e não a publique. Os nomes dos modelos estão no catálogo atual.

[Modelos e preços](https://crazyrouter.com/pt/pricing?utm_source=huggingface&utm_campaign=multimodal_pricing&utm_content=guide_prices__pt&utm_medium=dataset) · [Criar chave de API](https://crazyrouter.com/console/token?utm_source=huggingface&utm_campaign=multimodal_pricing&utm_content=guide_api_key__pt&utm_medium=dataset)

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://crazyrouter.com/v1", api_key=os.environ["CRAZYROUTER_API_KEY"])
response = client.chat.completions.create(
    model="gpt-4o-mini", messages=[{"role": "user", "content": "Hello"}], max_tokens=64
)
print(response.choices[0].message.content)
```
