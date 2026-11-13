"""Generation routing must not leak the paid key or redirect embedding clients."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import recommendation_llm as llm


@pytest.fixture(autouse=True)
def clean_settings(monkeypatch):
    for name in ("RECOMMEND_LLM_PROVIDER", "RECOMMEND_LLM_MODEL", "RECOMMEND_LLM_BASE_URL", "OPENAI_BASE_URL"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("OPENAI_API_KEY", "test-paid-key")


def test_default_preserves_openai():
    assert llm.model_name() == "gpt-4.1-mini"
    with llm.create_client() as client:
        assert str(client.base_url) == "https://api.openai.com/v1/"
        assert client.api_key == "test-paid-key"


def test_local_generation_without_paid_key(monkeypatch):
    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "ollama")
    monkeypatch.delenv("OPENAI_API_KEY")
    assert llm.model_name() == "gemma3:4b"
    with llm.create_client() as client:
        assert str(client.base_url) == "http://127.0.0.1:11434/v1/"
        assert client.api_key == "ollama"
        assert client.max_retries == 0


def test_local_settings_do_not_change_embedding_environment(monkeypatch):
    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "ollama")
    monkeypatch.setenv("RECOMMEND_LLM_BASE_URL", "http://ollama:11434/v1")
    monkeypatch.setenv("RECOMMEND_LLM_MODEL", "local-test-model")
    assert llm.model_name() == "local-test-model"
    with llm.create_client() as client:
        assert str(client.base_url) == "http://ollama:11434/v1/"
        assert client.api_key != "test-paid-key"
    import os
    assert os.environ["OPENAI_API_KEY"] == "test-paid-key"
    assert "OPENAI_BASE_URL" not in os.environ


def test_switch_back_ignores_local_url(monkeypatch):
    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "openai")
    monkeypatch.setenv("RECOMMEND_LLM_MODEL", "gpt-4.1-mini")
    monkeypatch.setenv("RECOMMEND_LLM_BASE_URL", "http://ollama:11434/v1")
    with llm.create_client() as client:
        assert str(client.base_url) == "https://api.openai.com/v1/"


def test_invalid_provider_does_not_fall_back(monkeypatch):
    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "olama")
    with pytest.raises(ValueError, match="RECOMMEND_LLM_PROVIDER"):
        llm.create_client()
