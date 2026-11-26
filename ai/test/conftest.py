import pytest


@pytest.fixture(autouse=True)
def _no_dataset_rerank_call(monkeypatch):
    """Tests never reach the paid reorder call by accident; test_dataset_rerank.py turns it on where it fakes it."""
    monkeypatch.setenv("DATASET_RERANK", "off")
