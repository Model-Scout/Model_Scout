---
pretty_name: KoTAU Development Data
language:
- ko
- en
tags:
- travel
- agents
- tool-use
- development
configs:
- config_name: rail_fares
  data_files:
  - split: development
    path: data/rail/fares.parquet
- config_name: rail_inventory
  data_files:
  - split: development
    path: data/rail/inventory.parquet
- config_name: rail_inventory_init
  data_files:
  - split: development
    path: data/rail/inventory_init.parquet
- config_name: rail_meta
  data_files:
  - split: development
    path: data/rail/meta.parquet
- config_name: rail_stations
  data_files:
  - split: development
    path: data/rail/stations.parquet
- config_name: rail_stops
  data_files:
  - split: development
    path: data/rail/stops.parquet
- config_name: rail_trains
  data_files:
  - split: development
    path: data/rail/trains.parquet
- config_name: lodging_direct_site_pages
  data_files:
  - split: development
    path: data/lodging/direct_site_pages.parquet
- config_name: lodging_direct_site_policy
  data_files:
  - split: development
    path: data/lodging/direct_site_policy.parquet
- config_name: lodging_direct_sites
  data_files:
  - split: development
    path: data/lodging/direct_sites.parquet
- config_name: lodging_engine_hotels
  data_files:
  - split: development
    path: data/lodging/engine_hotels.parquet
- config_name: lodging_engine_open_dates
  data_files:
  - split: development
    path: data/lodging/engine_open_dates.parquet
- config_name: lodging_engine_rate_plans
  data_files:
  - split: development
    path: data/lodging/engine_rate_plans.parquet
- config_name: lodging_engine_rates
  data_files:
  - split: development
    path: data/lodging/engine_rates.parquet
- config_name: lodging_engine_stay_hotels
  data_files:
  - split: development
    path: data/lodging/engine_stay_hotels.parquet
- config_name: lodging_hotels
  data_files:
  - split: development
    path: data/lodging/hotels.parquet
- config_name: lodging_meta
  data_files:
  - split: development
    path: data/lodging/meta.parquet
- config_name: lodging_naver_booking
  data_files:
  - split: development
    path: data/lodging/naver_booking.parquet
- config_name: lodging_stay_fee_pages
  data_files:
  - split: development
    path: data/lodging/stay_fee_pages.parquet
- config_name: lodging_stay_homepages
  data_files:
  - split: development
    path: data/lodging/stay_homepages.parquet
- config_name: lodging_stay_policy_quotes
  data_files:
  - split: development
    path: data/lodging/stay_policy_quotes.parquet
- config_name: lodging_stay_ratings
  data_files:
  - split: development
    path: data/lodging/stay_ratings.parquet
- config_name: lodging_stays
  data_files:
  - split: development
    path: data/lodging/stays.parquet
- config_name: lodging_tourapi_areas
  data_files:
  - split: development
    path: data/lodging/tourapi_areas.parquet
- config_name: lodging_tourapi_common
  data_files:
  - split: development
    path: data/lodging/tourapi_common.parquet
- config_name: lodging_tourapi_images
  data_files:
  - split: development
    path: data/lodging/tourapi_images.parquet
- config_name: lodging_tourapi_intro
  data_files:
  - split: development
    path: data/lodging/tourapi_intro.parquet
- config_name: lodging_tourapi_pet
  data_files:
  - split: development
    path: data/lodging/tourapi_pet.parquet
- config_name: lodging_tourapi_rooms
  data_files:
  - split: development
    path: data/lodging/tourapi_rooms.parquet
- config_name: lodging_tourapi_stays
  data_files:
  - split: development
    path: data/lodging/tourapi_stays.parquet
- config_name: lodging_yanolja_places
  data_files:
  - split: development
    path: data/lodging/yanolja_places.parquet
- config_name: bus_routes
  data_files:
  - split: development
    path: data/bus/bus_routes.parquet
- config_name: bus_stops
  data_files:
  - split: development
    path: data/bus/bus_stops.parquet
- config_name: bus_route_stops
  data_files:
  - split: development
    path: data/bus/route_stops.parquet
- config_name: bus_fares
  data_files:
  - split: development
    path: data/bus/bus_fares.parquet
- config_name: bus_meta
  data_files:
  - split: development
    path: data/bus/meta.parquet
- config_name: attraction_attractions
  data_files:
  - split: development
    path: data/attraction/attractions.parquet
- config_name: attraction_intro
  data_files:
  - split: development
    path: data/attraction/attraction_intro.parquet
- config_name: attraction_info
  data_files:
  - split: development
    path: data/attraction/attraction_info.parquet
- config_name: attraction_cls_codes
  data_files:
  - split: development
    path: data/attraction/cls_codes.parquet
- config_name: attraction_meta
  data_files:
  - split: development
    path: data/attraction/meta.parquet
---


# KoTAU Development Data

Working data for **KoTAU**, a Korean travel agent benchmark. Parquet tables support analysis; source captures and SQLite databases preserve the offline environment.

[Code and tools](https://github.com/HAE-RAE/KoTAU/tree/feat/hf-data-migration) | [File inventory](https://huggingface.co/datasets/HAERAE-HUB/KoTau-dev-data/blob/main/manifest.json) | [Export report](https://huggingface.co/datasets/HAERAE-HUB/KoTau-dev-data/blob/main/artifacts/parquet-export.json)

## Data

| Layer | Contents |
| --- | --- |
| `data/rail/` | Stations, schedules, fares, inventory, booking state |
| `data/lodging/` | Properties, rooms, policies, ratings, dated prices |
| `data/bus/` | Seoul city bus routes, stops, schedules, fares |
| `data/attraction/` | Seoul tourist spots & cultural facilities, hours, fees |
| `sources/` | Original documents, captures, and benchmark archives |
| `databases/` | `rail/korail.db`, `lodging/lodging.db`, `bus/seoul_bus.db`, `attraction/attraction.db`, `seoul/kotau_seoul.db` |
| `artifacts/`, `provenance/` | Runtime download bundle, checks, source provenance |

The initial export contains **32 Parquet tables**. The 31 populated tables have separate configs with a `development` split. The empty `rail/reservations.parquet` preserves the booking-state schema. Relational table rows are not benchmark episodes.

## Load

```python
from datasets import load_dataset

stays = load_dataset(
    "HAERAE-HUB/KoTau-dev-data",
    "lodging_stays",
    split="development",
    token=True,
)
```

```bash
hf auth login
hf download HAERAE-HUB/KoTau-dev-data --repo-type dataset \
  --include "data/**" --local-dir .
```

Use a full commit hash with `revision` for reproducible analysis. For the offline tools, run `uv run python tools/data.py download` from the code checkout. It uses `data.lock.json`, verifies SHA-256, and restores source files and databases to their runtime paths.

## Schema and status

SQLite table and column names are preserved in Parquet.

Rail inventory is synthetic. Prices and availability reflect collection time, recorded with the sources.

This is a private development repository. The paper release will use a separate repository with frozen data and experiment splits. Third-party source materials retain their original terms and licenses.
