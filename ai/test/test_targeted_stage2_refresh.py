"""명시적 resolver 복구 대상은 동일 revision이어도 Stage 2를 다시 계산한다."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("stage2_for_targeted_refresh_test", ROOT / "02_enrich_metadata.py")
assert SPEC is not None and SPEC.loader is not None
stage2 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stage2)


def test_force_model_ids_bypasses_resume_for_selected_row():
    row = {"model_id": "org/selected"}
    assert stage2.can_resume_selected_row(
        row,
        {},
        "core",
        model_ids={"org/selected"},
        force_model_ids=True,
    ) is False


def test_force_model_ids_does_not_affect_unselected_row():
    original = stage2.resume_matches
    try:
        stage2.resume_matches = lambda row, source, pool: True
        assert stage2.can_resume_selected_row(
            {"model_id": "org/other"},
            {},
            "core",
            model_ids={"org/selected"},
            force_model_ids=True,
        ) is True
    finally:
        stage2.resume_matches = original


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
