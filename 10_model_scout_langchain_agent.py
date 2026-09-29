#!/usr/bin/env python3
"""10 - LangChain agent connected to the Model Scout read-only MCP server.

Usage:

    python 10_model_scout_langchain_agent.py \
        "한국어 문서 임베딩에 적합하고 1B 이하인 모델을 추천해줘"

The agent launches 09_model_scout_mcp_readonly.py over stdio. The child MCP
server inherits the current environment, including the Supabase and OpenAI
credentials loaded from .env.
"""

from __future__ import annotations

import argparse
import asyncio
import difflib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv

try:
    from langchain.agents import create_agent
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from langchain_openai import ChatOpenAI
except ImportError as exc:  # pragma: no cover - exercised during setup only
    raise SystemExit(
        "LangChain MCP dependencies are missing. Install with: "
        "python -m pip install -r requirements_mcp.txt"
    ) from exc


ROOT = Path(__file__).resolve().parent
MCP_SERVER = ROOT / "09_model_scout_mcp_readonly.py"
load_dotenv(ROOT / ".env")

# Keep the agent contract explicit and bounded.  This is the prompt passed to
# LangChain; the output layer below also enforces the audit fields.
SYSTEM_PROMPT = """
너는 Model Scout 추천 에이전트다.

반드시 지킬 규칙:
1. 모델 검색은 model_scout_readonly MCP 도구만 사용한다.
2. 사용자의 요구에서 한국어 지원, 파라미터 수, context length, popularity 같은 조건을 추출해 search_models의 명시적 필터로 전달한다.
3. 문서 임베딩·벡터 검색·semantic search는 `feature-extraction`과 `sentence-similarity`를 함께 사용한다. `text-embedding`이라는 존재하지 않는 단일 task 필터를 만들지 않는다.
4. 모델을 추천하기 전에 반드시 search_models를 호출한다.
5. 기본 추천 수는 3~5개이며, 최종 추천은 최대 5개로 제한한다. 5개보다 많은 후보를 나열하지 않는다.
6. 최종 후보마다 get_model_evidence를 호출한다. 호출하지 못한 모델은 추천 목록에 넣지 않는다.
7. 최종 답변의 본문에서는 README 직접 근거와 LLM 해석을 분리한다.
   - 본문의 `LLM 해석`: 검색·evidence 결과에서 추론한 추천 이유로 표시한다.
   - `supporting_quote`, `README section`, `evidence_level`은 본문에 반복하지 않는다.
     실행 코드가 마지막에 `감사 근거 (README 원문)` 블록으로 모델마다 한 번만 출력한다.
8. 각 모델 본문에는 model_id, 도메인 범위, LLM 해석을 표시한다. 도메인 범위는 MCP의 `domain_scope`를 사용하고 `unknown`이면 추측하지 않는다.
9. 도구가 반환한 model_id와 model_url을 그대로 복사한다. 모델 ID를 만들어내거나 URL을 추측하지 않는다.
10. README/evidence에 없는 성능·강점·제한·벤치마크·런타임 정보를 단정하지 않는다.
11. 조건을 만족하는 후보가 없으면 억지로 추천하지 말고 없다고 설명한다.
12. MCP 도구에서 쓰기 작업이나 임의 SQL 실행을 시도하지 않는다.
13. 임베딩 요청에는 번역·생성·음성인식 모델을 추천하지 않는다. 검색 결과의 task 일관성을 확인한다.

권장 답변 형식:
### 결론
### 추천 모델
각 모델마다:
- model_id
- 도메인 범위: domain_specific, general_purpose 또는 unknown
- 조건에 맞는 이유 (LLM 해석)
- 주의사항
※ supporting_quote, README section, evidence_level은 실행 코드가 추가하는 감사 근거 블록에서 한 번만 표시한다.
""".strip()


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "query",
        nargs="*",
        help="Natural-language model recommendation request",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("LANGCHAIN_MODEL", "gpt-4o-mini"),
        help="Chat model used by the LangChain agent",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the complete agent result as JSON",
    )
    return parser.parse_args()


def _content_to_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: List[str] = []
        for item in content:
            if isinstance(item, dict) and isinstance(item.get("text"), str):
                parts.append(item["text"])
            else:
                parts.append(str(item))
        return "\n".join(parts)
    return str(content)


def _payload_from_content(content: Any) -> Any:
    try:
        return json.loads(_content_to_text(content))
    except (TypeError, ValueError):
        return None


def _collect_search_model_ids(messages: List[Any]) -> List[str]:
    """Collect exact IDs returned by MCP so the final text cannot typo them."""

    model_ids = set()
    for message in messages:
        for tool_call in getattr(message, "tool_calls", None) or []:
            name = str(tool_call.get("name") or "")
            args = tool_call.get("args") or {}
            if name.endswith("search_models"):
                # Search results are collected from the following ToolMessage;
                # this branch only covers exact IDs passed to detail tools.
                pass
            if name.endswith("get_model") or name.endswith("get_model_evidence"):
                model_id = args.get("model_id")
                if isinstance(model_id, str) and model_id.strip():
                    model_ids.add(model_id.strip())
            for model_id in args.get("model_ids") or []:
                if isinstance(model_id, str) and model_id.strip():
                    model_ids.add(model_id.strip())

        tool_name = str(getattr(message, "name", None) or "")
        payload = _payload_from_content(getattr(message, "content", None))
        if tool_name.endswith("search_models") and isinstance(payload, dict):
            for result in payload.get("results") or []:
                if isinstance(result, dict) and isinstance(result.get("model_id"), str):
                    model_ids.add(result["model_id"])
        elif tool_name.endswith("get_model_evidence") and isinstance(payload, dict):
            model_id = payload.get("model_id")
            if isinstance(model_id, str) and model_id.strip():
                model_ids.add(model_id.strip())
    return sorted(model_ids)


def _collect_evidence_payloads(messages: List[Any]) -> Dict[str, Dict[str, Any]]:
    """Collect exact evidence records returned by the read-only MCP server."""
    payloads: Dict[str, Dict[str, Any]] = {}
    for message in messages:
        tool_name = str(getattr(message, "name", "") or "")
        if not tool_name.endswith("get_model_evidence"):
            continue
        payload = _payload_from_content(getattr(message, "content", None))
        if not isinstance(payload, dict):
            continue
        model_id = payload.get("model_id")
        if isinstance(model_id, str) and model_id.strip():
            payloads[model_id.strip()] = payload
    return payloads


def _audit_evidence_block(payload: Dict[str, Any]) -> str:
    """Render mandatory, deterministic evidence fields from MCP output."""
    model_id = str(payload.get("model_id") or "unknown")
    audit = payload.get("audit_evidence") or {}
    if not isinstance(audit, dict):
        audit = {}
    quote = audit.get("supporting_quote") or "없음"
    section = audit.get("readme_section") or "없음"
    level = audit.get("evidence_level") or "unknown"
    domain_scope = payload.get("domain_scope") or {}
    if isinstance(domain_scope, dict):
        domain_label = domain_scope.get("label") or "unknown"
        domains = domain_scope.get("domains") or []
        domain_text = domain_label
        if domains:
            domain_text += f" ({', '.join(str(item) for item in domains)})"
    else:
        domain_text = "unknown"
    quote_note = " (발췌가 긴 경우 앞부분만 표시)" if audit.get("quote_truncated") else ""
    model_url = payload.get("model_url") or f"https://huggingface.co/{model_id}"
    return (
        f"### {model_id}\n"
        f"- model_url: {model_url}\n"
        f"- 도메인 범위: `{domain_text}`\n"
        f"- README 직접 근거(supporting_quote){quote_note}:\n"
        f"  > {quote}\n"
        f"- README section: `{section}`\n"
        f"- evidence_level: `{level}`"
    )


def _append_audit_evidence(text: str, messages: List[Any]) -> str:
    """Guarantee a compact evidence block for the models actually inspected."""
    payloads = _collect_evidence_payloads(messages)
    if not payloads:
        return text

    # Prefer models named in the final answer, while retaining tool-call order.
    selected = [model_id for model_id in payloads if model_id in text]
    if not selected:
        selected = list(payloads)
    selected = selected[:5]
    blocks = [_audit_evidence_block(payloads[model_id]) for model_id in selected]
    return text.rstrip() + "\n\n## 감사 근거 (README 원문)\n" + "\n\n".join(blocks)


def _canonicalize_model_ids(text: str, known_ids: List[str]) -> str:
    """Repair only high-confidence model-ID typos against MCP-returned IDs."""

    if not text or not known_ids:
        return text
    pattern = re.compile(r"(?<![A-Za-z0-9_.-])([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)(?![A-Za-z0-9_.-])")
    replacements = {}
    for candidate in pattern.findall(text):
        if candidate in known_ids:
            continue
        matches = difflib.get_close_matches(candidate, known_ids, n=1, cutoff=0.90)
        if matches:
            replacements[candidate] = matches[0]
    for candidate, canonical in sorted(replacements.items(), key=lambda item: -len(item[0])):
        text = text.replace(candidate, canonical)
    return text


async def _run_agent(query: str, model_name: str) -> Dict[str, Any]:
    if not query.strip():
        raise ValueError("A natural-language query is required")
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for the LangChain agent")

    client = MultiServerMCPClient(
        {
            "model_scout_readonly": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [str(MCP_SERVER)],
            }
        }
    )
    tools = await client.get_tools()
    model = ChatOpenAI(model=model_name, temperature=0, max_tokens=1200)
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )
    return await agent.ainvoke(
        {
            "messages": [
                {"role": "user", "content": query.strip()},
            ]
        }
    )


async def _async_main(args: argparse.Namespace) -> int:
    query = " ".join(args.query).strip()
    if not query:
        query = input("Model Scout 검색 질문: ").strip()

    result = await _run_agent(query, args.model)
    messages = result.get("messages") or []
    if not messages:
        raise RuntimeError("LangChain agent returned no messages")
    final_text = _content_to_text(messages[-1].content)
    final_text = _canonicalize_model_ids(final_text, _collect_search_model_ids(messages))
    final_text = _append_audit_evidence(final_text, messages)
    if args.json:
        result["final_text"] = final_text
        result["audit_evidence"] = list(_collect_evidence_payloads(messages).values())
        print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
        return 0
    print(final_text)
    return 0


def main() -> int:
    return asyncio.run(_async_main(_parse_args()))


if __name__ == "__main__":
    raise SystemExit(main())
