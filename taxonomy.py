"""Load taxonomy.yaml and map raw NER/metadata values onto its concepts.

Every concept is a wiki hub page; mapping a model or dataset to a concept links it to
everything else mapped there. Alias collisions inside a facet fail at load time so a
typo in the vocabulary cannot silently send values to the wrong hub.
"""
from __future__ import annotations

import functools
import re
from pathlib import Path
from typing import Any, Optional

import yaml

from retrieval_metadata import normalize_language_code

TAXONOMY_PATH = Path(__file__).with_name("taxonomy.yaml")
_SEP_RE = re.compile(r"[\s_\-]+")


def _key(value: Any) -> str:
    return _SEP_RE.sub(" ", str(value if value is not None else "").casefold()).strip()


@functools.lru_cache(maxsize=1)
def load_taxonomy() -> dict:
    data = yaml.safe_load(TAXONOMY_PATH.read_text(encoding="utf-8"))
    for facet, spec in data["facets"].items():
        index: dict[str, str] = {}
        for value, concept in spec["values"].items():
            for alias in (value, concept["label"], *concept.get("aliases", [])):
                previous = index.setdefault(_key(alias), value)
                if previous != value:
                    raise ValueError(f"{facet}: alias {alias!r} maps to both {previous!r} and {value!r}")
        spec["alias_index"] = index
    return data


def normalize(facet: str, raw: Any) -> Optional[str]:
    """Return the concept key for a raw value, or None when the vocabulary has no match."""
    spec = load_taxonomy()["facets"][facet]
    if isinstance(raw, (list, tuple)) and len(raw) == 1:
        raw = raw[0]
    if spec.get("ordinal") and isinstance(raw, (int, float)) and not isinstance(raw, bool):
        for value, concept in spec["values"].items():
            if concept.get("max") is None or raw <= concept["max"]:
                return value
    if facet == "language":
        code = normalize_language_code(raw)
        return spec["alias_index"].get(_key(code)) or spec["alias_index"].get(_key(raw)) or (code or None)
    return spec["alias_index"].get(_key(raw))


def label(facet: str, value: str) -> str:
    """Wiki page name for a concept; open-facet values without an entry use their key."""
    concept = load_taxonomy()["facets"][facet]["values"].get(value)
    return concept["label"] if concept else value


if __name__ == "__main__":
    assert normalize("task", "feature-extraction") == "embedding"
    assert normalize("task", "Text_Generation") == "generation"
    assert normalize("input_length", 512) == "short"
    assert normalize("input_length", 513) == "medium"
    assert normalize("input_length", 8192) == "long"
    assert normalize("input_length", 10**7) == "ultra_long"
    assert normalize("input_length", "긴 문서") == "long"
    assert normalize("language", "Korean") == "ko"
    assert normalize("language", "fi") == "fi"
    assert normalize("commercial_use", "CC-BY-NC-4.0") == "non_commercial"
    assert normalize("commercial_use", "공공누리 제1유형") == "commercial"
    assert normalize("commercial_use", None) == "unknown"
    assert normalize("commercial_use", ["mit"]) == "commercial"
    assert normalize("domain", "따릉이") == "transport"
    assert normalize("model_size", 7.6) == "small"
    assert normalize("task", "no such task") is None
    assert label("input_length", "long") == "장문"
    print("taxonomy ok")
