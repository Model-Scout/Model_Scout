"""Response schemas of the public API, and the mapping from the AI's SSE events to them.

python backend/app/result.py    # self-check
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field


class Check(BaseModel):
    key: Literal["license", "gpu", "context"]
    label: str
    status: Literal["met", "review", "unknown"] = Field(description="충족 / 확인 필요 / 미확인")
    reason: str


class Candidate(BaseModel):
    task: str = Field(description="the role this model plays in the project")
    purpose: str
    model_id: str
    rank_score: float
    license: str
    url: str | None = None
    context_length: int | None = None
    parameters_b: float | None = None
    benchmarks: list[dict[str, Any]] = []
    evidence: str | None = Field(default=None, description="README quote behind the recommendation")
    checks: list[Check]


class Source(BaseModel):
    source_id: str = Field(description="pass to GET /api/files/{source_id}")
    kind: Literal["model", "dataset"]
    title: str | None = None
    url: str | None = None


class ChatResult(BaseModel):
    summary: str
    candidates: list[Candidate]
    datasets: dict[str, Any] = Field(description="per_model, project_training, service_data")
    assessment: dict[str, Any] | None = Field(default=None, description="commercial launch verdict")
    sources: list[Source]


class ChatDone(BaseModel):
    """Payload of the final `done` SSE event; `type` says which fields are set."""

    type: Literal["answer", "clarify", "reject"]
    group_id: UUID
    elapsed: float
    answer: str | None = Field(default=None, description="set for answer")
    result: ChatResult | None = Field(default=None, description="set for answer")
    questions: list[str] | None = Field(default=None, description="set for clarify")
    message: str | None = Field(default=None, description="set for reject")


class GroupSummary(BaseModel):
    group_id: UUID
    title: str
    created_at: datetime
    updated_at: datetime


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    type: Literal["answer", "clarify", "reject"] | None = None
    result: ChatResult | None = None
    created_at: datetime


class GroupDetail(GroupSummary):
    messages: list[Message]


class SourceFile(BaseModel):
    source_id: str
    content: str = Field(description="README in markdown")


REJECT_MESSAGE = "모델과 데이터를 추천할 수 있는 프로젝트 아이디어로 다시 입력해 주세요."


def _checks(model: dict[str, Any], constraints: dict[str, Any]) -> list[Check]:
    use = model.get("commercial_use")
    license_status: Literal["met", "review", "unknown"] = (
        "met" if use == "commercial" else "unknown" if use in (None, "unknown") else "review"
    )
    checks = [
        Check(
            key="license",
            label="상업 이용",
            status=license_status,
            reason=f"라이선스 {model.get('license') or 'unknown'}",
        )
    ]
    if constraints.get("gpu_memory_gb") is not None:
        fit = model.get("gpu_fit") or {}
        status = {"runs": "met", "runs_quantized": "review", "too_large": "review"}.get(
            str(fit.get("verdict")), "unknown"
        )
        checks.append(
            Check(key="gpu", label="GPU 메모리", status=status, reason=fit.get("label") or "GPU 정보를 찾지 못함")  # type: ignore[arg-type]
        )
    minimum = constraints.get("min_context_length")
    if minimum is not None:
        length = model.get("context_length")
        checks.append(
            Check(
                key="context",
                label="입력 길이",
                status="unknown" if length is None else "met" if length >= minimum else "review",
                reason=f"요구 {minimum}, 모델 {length if length is not None else '미확인'}",
            )
        )
    return checks


def build_result(events: dict[str, Any]) -> ChatResult:
    plan = events.get("plan") or {}
    constraints = plan.get("constraints") or {}
    candidates, sources, seen = [], [], set()

    def add_source(source_id: str, kind: Literal["model", "dataset"], title: str | None, url: str | None) -> None:
        if source_id not in seen:
            seen.add(source_id)
            sources.append(Source(source_id=source_id, kind=kind, title=title, url=url))

    for group in events.get("models") or []:
        need = group["need"]
        for model in group["models"]:
            candidates.append(
                Candidate(
                    task=need["task"],
                    purpose=need["purpose_ko"],
                    model_id=model["model_id"],
                    rank_score=model["rank_score"],
                    license=model.get("license") or "unknown",
                    url=model.get("url"),
                    context_length=model.get("context_length"),
                    parameters_b=model.get("parameters_b"),
                    benchmarks=model.get("benchmarks") or [],
                    evidence=model.get("evidence"),
                    checks=_checks(model, constraints),
                )
            )
            add_source(model["model_id"], "model", model["model_id"], model.get("url"))
    datasets = events.get("datasets") or {}
    rows = [row for rows in (datasets.get("per_model") or {}).values() for row in rows]
    rows += (datasets.get("project_training") or []) + (datasets.get("service_data") or [])
    for row in rows:
        add_source(row["dataset"], "dataset", row.get("title"), row.get("url"))
    return ChatResult(
        summary=plan.get("summary_ko") or "",
        candidates=candidates,
        datasets=datasets,
        assessment=events.get("assessment"),
        sources=sources,
    )


def build_done(events: dict[str, Any], group_id: UUID, answer: str, elapsed: float) -> ChatDone:
    """clarify and reject stop before the search, so they carry no result."""
    if events.get("clarify"):
        return ChatDone(type="clarify", group_id=group_id, elapsed=elapsed, questions=events["clarify"]["questions"])
    if not (events.get("plan") or {}).get("needs"):
        return ChatDone(type="reject", group_id=group_id, elapsed=elapsed, message=REJECT_MESSAGE)
    return ChatDone(type="answer", group_id=group_id, elapsed=elapsed, answer=answer, result=build_result(events))


def stored_text(done: ChatDone) -> str:
    """What the assistant said, as the history shows it."""
    if done.type == "clarify":
        return "\n".join(done.questions or [])
    return done.message or done.answer or ""


if __name__ == "__main__":
    gid = UUID(int=1)
    plan: dict[str, Any] = {
        "summary_ko": "계획",
        "needs": [{"task": "retrieval", "purpose_ko": "검색", "model_query": "q"}],
        "constraints": {"gpu_memory_gb": 8, "min_context_length": 1000},
    }
    model = {
        "model_id": "a/b",
        "rank_score": 0.9,
        "license": "mit",
        "commercial_use": "commercial",
        "context_length": 512,
        "gpu_fit": {"verdict": "too_large", "label": "8GB로 부족"},
    }
    dataset = {"dataset": "seoul_open_data/OA-1", "title": "따릉이", "url": "u"}
    events = {
        "plan": plan,
        "models": [{"need": plan["needs"][0], "models": [model]}],
        "datasets": {"per_model": {"a/b": [dataset]}, "project_training": [dataset], "service_data": []},
    }
    done = build_done(events, gid, "답변", 1.0)
    assert done.type == "answer" and done.result
    statuses = {c.key: c.status for c in done.result.candidates[0].checks}
    assert statuses == {"license": "met", "gpu": "review", "context": "review"}, statuses
    assert [s.source_id for s in done.result.sources] == ["a/b", "seoul_open_data/OA-1"], "sources are unique"
    no_limits = build_done({**events, "plan": {**plan, "constraints": {}}}, gid, "답변", 1.0)
    assert no_limits.result and [c.key for c in no_limits.result.candidates[0].checks] == ["license"]
    clarify = build_done({"plan": plan, "clarify": {"questions": ["용도는?"]}}, gid, "", 1.0)
    assert clarify.type == "clarify" and clarify.result is None and stored_text(clarify) == "용도는?"
    assert build_done({"plan": {"needs": []}}, gid, "", 1.0).type == "reject"
    print("result self-check ok")
