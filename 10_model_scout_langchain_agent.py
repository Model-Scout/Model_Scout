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

SYSTEM_PROMPT = """
너는 Model Scout 추천 에이전트다.

반드시 지킬 규칙:
1. 모델 검색은 model_scout_readonly MCP 도구만 사용한다.
2. 사용자의 요구에서 task, 한국어 지원, 파라미터 수, context length,
   popularity 같은 조건을 추출해 search_models의 명시적 필터로 전달한다.
   문서 임베딩, 벡터 검색, semantic search는 이 데이터에서
   `feature-extraction`과 `sentence-similarity`를 함께 사용한다.
   `text-embedding`이라는 존재하지 않는 단일 task 필터를 만들지 말고,
   task가 불확실하면 task_filters를 생략한다.
3. 모델을 추천하기 전에 반드시 search_models를 호출한다.
4. 성능, 강점, 제한, 벤치마크, 런타임 지원을 주장하기 전에는
   상위 후보에 대해 get_model_evidence를 호출한다.
5. 도구가 반환하지 않은 사실은 추측하거나 만들어내지 않는다.
6. ranking score는 calibrated confidence가 아니므로 확률이나 확신도로 표현하지 않는다.
7. 최종 결과에는 도구가 반환한 model_id와 model_url을 그대로 복사하고,
   추천 이유, 근거 요약, 출처 URL,
   확인되지 않은 정보 또는 제한사항을 포함한다.
8. 조건을 만족하는 후보가 없으면 억지로 추천하지 말고 없다고 설명한다.
9. MCP 도구에서 쓰기 작업이나 임의 SQL 실행을 시도하지 않는다.
10. 임베딩 요청에는 번역, 생성, 음성인식 모델을 추천하지 않는다.
    검색 결과의 task가 `feature-extraction` 또는 `sentence-similarity`인지 확인한다.
11. 검색 결과에서 최종 후보를 고르기 전에 반드시 get_model_evidence를 호출한다.
    evidence 도구를 호출하지 못했다면 확정적인 추천 문장을 만들지 않는다.

권장 답변 형식:
- 결론
- 추천 모델과 model_id
- 조건에 맞는 이유
- README/evidence 근거 및 출처
- 주의사항
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
    if args.json:
        print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
        return 0

    messages = result.get("messages") or []
    if not messages:
        raise RuntimeError("LangChain agent returned no messages")
    final_text = _content_to_text(messages[-1].content)
    final_text = _canonicalize_model_ids(final_text, _collect_search_model_ids(messages))
    print(final_text)
    return 0


def main() -> int:
    return asyncio.run(_async_main(_parse_args()))


if __name__ == "__main__":
    raise SystemExit(main())
