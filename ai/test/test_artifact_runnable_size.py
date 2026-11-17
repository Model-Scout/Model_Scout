"""실행 가능한 모델 묶음과 보조/불완전 파일을 구분한다."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from resolvers import artifacts, resolve  # noqa: E402


def _raw(files, **extra):
    return {"id": extra.pop("model_id", "org/model"),
            "siblings": [{"rfilename": name, "size": size} for name, size in files], **extra}


def test_real_small_model_never_rounds_to_zero():
    raw = _raw([("model.safetensors", 3_169_960)])
    record = resolve.build(raw, stage2={})
    artifact = record["deployment"]["vram_estimate"]["artifact"]
    assert artifact["bytes"] == 3_169_960
    assert artifact["gib"] > 0


def test_arbitrary_bin_is_not_a_pytorch_weight():
    raw = _raw([("tokenizer.bin", 1_744_786), ("model.tflite", 75_000_000)])
    result = artifacts.resolve(raw)["artifacts"]
    assert result["formats"]["pytorch_bin"]["present"] is False
    assert artifacts.smallest_runnable_bytes(result) is None


def test_conventional_pytorch_weight_is_kept():
    raw = _raw([("pytorch_model.bin", 3_169_960)])
    result = artifacts.resolve(raw)["artifacts"]
    assert artifacts.smallest_runnable_bytes(result) == ("pytorch_bin", 3_169_960)


def test_adapter_repository_has_no_standalone_runnable_size():
    raw = _raw(
        [("adapter.F32.gguf", 2_557_408)],
        base_models=["base/model"],
        cardData={"base_model_relation": "adapter"},
    )
    record = resolve.build(raw, stage2={})
    assert record["deployment"]["vram_estimate"]["artifact"] is None


def test_impossible_size_for_declared_70b_is_unknown():
    raw = _raw([("pytorch_model.bin", 15_000)], model_id="org/Outlier-70B")
    record = resolve.build(raw, stage2={})
    assert record["deployment"]["vram_estimate"]["artifact"] is None


def test_tiny_derived_weight_is_not_called_standalone():
    raw = _raw([("model.safetensors", 31_000)], base_models=["base/model"])
    record = resolve.build(raw, stage2={})
    assert record["deployment"]["vram_estimate"]["artifact"] is None


def test_small_onnx_graph_without_confirmed_external_tensors_is_unknown():
    raw = _raw([("model.onnx", 4_927_402), ("assets/archive.dat", 788_000_000)])
    record = resolve.build(raw, stage2={})
    assert record["deployment"]["vram_estimate"]["artifact"] is None


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
