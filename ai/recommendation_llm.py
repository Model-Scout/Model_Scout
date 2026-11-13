"""Generation-only LLM settings. Retrieval embeddings keep their own OpenAI client."""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load before resolving the graph's model name. Explicit process settings win.
load_dotenv(Path(__file__).resolve().parent / ".env", override=False)


def provider() -> str:
    value = os.getenv("RECOMMEND_LLM_PROVIDER", "openai").strip().lower()
    if value not in {"openai", "ollama"}:
        raise ValueError("RECOMMEND_LLM_PROVIDER must be openai or ollama")
    return value


def model_name() -> str:
    return os.getenv("RECOMMEND_LLM_MODEL") or (
        "gemma3:4b" if provider() == "ollama" else "gpt-4.1-mini"
    )


def create_client() -> OpenAI:
    if provider() == "ollama":
        # Never reuse the paid OpenAI key or fall back to a paid model on errors.
        return OpenAI(
            base_url=os.getenv("RECOMMEND_LLM_BASE_URL") or "http://127.0.0.1:11434/v1",
            api_key="ollama",
            timeout=120.0,
            max_retries=0,
        )
    return OpenAI(api_key=os.environ["OPENAI_API_KEY"], base_url="https://api.openai.com/v1")
