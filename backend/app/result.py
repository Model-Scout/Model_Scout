"""V2 public response contract and adapter for internal AI events."""
from __future__ import annotations

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field, model_validator


class Source(BaseModel):
    source_id: str
    kind: Literal["model", "dataset"]
    title: str | None = None
    url: str | None = None
    quote: str | None = None
    origin: Literal["readme", "metadata", "estimate", "unknown"] = "unknown"
    location: str | None = None


class Check(BaseModel):
    key: str
    label: str
    status: Literal["ok", "check", "unknown"]
    reason: str
    source_id: str | None = None
    quote: str | None = None
    origin: Literal["readme", "metadata", "estimate", "unknown"] = "unknown"


class Evidence(BaseModel):
    """Why a dataset was recommended. Relevance only, so it is kept apart from condition checks."""
    label: str
    text: str | None = None
    origin: Literal["readme", "metadata"] = "metadata"


class Candidate(BaseModel):
    id: str = Field(description="model:<source_id> or dataset:<source_id>; target_id uses this value")
    type: Literal["model", "dataset"]
    source_id: str
    name: str
    role: str
    tags: list[str] = Field(default_factory=list)
    source: str
    url: str | None = None
    checks: list[Check] = Field(default_factory=list)
    evidence: list[Evidence] = Field(default_factory=list)
    related: list[str] = Field(default_factory=list)
    rank_score: float | None = None
    context_length: int | None = None
    parameters_b: float | None = None
    benchmarks: list[dict[str, Any]] = Field(default_factory=list)
    gpu_fit: dict[str, Any] | None = None


class ChatResult(BaseModel):
    title: str
    summary: list[str]
    needs_check: list[str] = Field(default_factory=list)
    candidates: list[Candidate]
    assessment: dict[str, Any] | None = None

    @model_validator(mode="before")
    @classmethod
    def restore_legacy(cls, value: Any) -> Any:
        # Old stored snapshots remain readable; do not re-run AI during restoration.
        if isinstance(value, dict) and isinstance(value.get("summary"), str):
            models = []
            for row in value.get("candidates", []):
                models.append({"need": {"task": row.get("task", ""), "purpose_ko": row.get("purpose", "")},
                               "models": [row]})
            result = build_result({"plan": {"summary_ko": value["summary"]}, "models": models,
                                 "datasets": value.get("datasets", {}),
                                 "assessment": value.get("assessment")}).model_dump()
            # Preserve the original condition decisions rather than recomputing from absent constraints.
            original = {f"model:{r['model_id']}": r for r in value.get("candidates", [])}
            for candidate in result["candidates"]:
                old = original.get(candidate["id"])
                if old is not None:
                    candidate["checks"] = [dict(check, status={"met": "ok", "review": "check"}.get(check["status"], check["status"]))
                                            for check in old.get("checks", [])]
            result["needs_check"] = list(dict.fromkeys(f"{c['name']}: {k['label']}" for c in result["candidates"]
                                                       if c["type"] == "model"
                                                       for k in c["checks"] if k["status"] != "ok"))
            return result
        return value


class ChatDone(BaseModel):
    schema_version: Literal[2] = 2
    type: Literal["answer", "clarify", "reject"]
    group_id: UUID
    elapsed: float
    answer: str
    sources: list[Source] = Field(default_factory=list)
    result: ChatResult | None = None
    history_saved: bool = True


class GroupSummary(BaseModel):
    group_id: UUID
    title: str
    created_at: datetime
    updated_at: datetime


class Message(BaseModel):
    id: int
    role: Literal["user", "assistant"]
    content: str
    type: Literal["answer", "clarify", "reject"] | None = None
    result: ChatResult | None = None
    sources: list[Source] = Field(default_factory=list)
    created_at: datetime


class GroupDetail(GroupSummary):
    messages: list[Message]
    result: ChatResult | None = None


class SourceFile(BaseModel):
    source_id: str
    content: str
    truncated: bool = False


REJECT_MESSAGE = "모델과 데이터를 추천할 수 있는 프로젝트 아이디어로 다시 입력해 주세요."


def _checks(model: dict[str, Any], constraints: dict[str, Any]) -> list[Check]:
    sid = model["model_id"]
    use = model.get("commercial_use")
    checks = [Check(key="license", label="상업 이용",
                    status="ok" if use == "commercial" else "unknown" if use in (None, "unknown") else "check",
                    reason=f"라이선스 {model.get('license') or 'unknown'}", source_id=sid,
                    origin="metadata" if model.get("license") not in (None, "unknown") else "unknown")]
    if constraints.get("gpu_memory_gb") is not None:
        fit = model.get("gpu_fit") or {}
        checks.append(Check(key="gpu", label="GPU 메모리",
                            status={"runs": "ok", "runs_quantized": "check", "too_large": "check"}.get(fit.get("verdict"), "unknown"),
                            reason=fit.get("label") or "GPU 정보를 찾지 못함", source_id=sid, origin="estimate"))
    minimum = constraints.get("min_context_length")
    if minimum is not None:
        length = model.get("context_length")
        checks.append(Check(key="context", label="입력 길이",
                            status="unknown" if length is None else "ok" if length >= minimum else "check",
                            reason=f"요구 {minimum}, 모델 {length if length is not None else '미확인'}",
                            source_id=sid, origin="metadata" if length is not None else "unknown"))
    # These cannot be established from the current AI response; never infer support from a name.
    checks.extend([Check(key="language", label="한국어 지원", status="unknown", reason="구조화된 언어 지원 근거가 제공되지 않았어요."),
                   Check(key="execution", label="로컬 실행", status="unknown", reason="실행 환경에 대한 검증이 필요해요.")])
    return checks


def build_result(events: dict[str, Any]) -> ChatResult:
    plan = events.get("plan") or {}
    constraints = plan.get("constraints") or {}
    datasets = events.get("datasets") or {}
    candidates: dict[str, Candidate] = {}
    for group in events.get("models") or []:
        need = group["need"]
        for model in group["models"]:
            sid = model["model_id"]
            cid = f"model:{sid}"
            role = need.get("purpose_ko") or need.get("task", "")
            if cid in candidates:
                if role not in candidates[cid].role:
                    candidates[cid].role += f" / {role}"
                continue
            candidates[cid] = Candidate(id=cid, type="model", source_id=sid, name=sid.split("/")[-1],
                role=role, tags=[v for v in [need.get("task"), model.get("license")] if v],
                source="Hugging Face", url=model.get("url"), checks=_checks(model, constraints),
                rank_score=model.get("rank_score"), context_length=model.get("context_length"),
                parameters_b=model.get("parameters_b"), benchmarks=model.get("benchmarks") or [], gpu_fit=model.get("gpu_fit"))
    def add_dataset(row: dict[str, Any], role: str, model_id: str | None = None) -> None:
        sid = row["dataset"]
        cid = f"dataset:{sid}"
        if cid not in candidates:
            licenses = row.get("licenses") or []
            # A license name alone does not settle commercial use, so it is never "ok".
            checks = [Check(key="license", label="라이선스", status="check" if licenses else "unknown",
                            reason=f"라이선스 {', '.join(licenses)}" if licenses else "라이선스 정보를 찾지 못했어요.",
                            source_id=sid, origin="metadata" if licenses else "unknown")]
            evidence = [Evidence(label=e.get("concept") or "추천 근거", text=e.get("text"),
                                 origin="readme" if e.get("text") and e.get("source") == "README 인용" else "metadata")
                        for e in row.get("evidence") or []]
            candidates[cid] = Candidate(id=cid, type="dataset", source_id=sid,
                name=row.get("title") or sid, role=role, tags=licenses, source=row.get("source") or "unknown",
                url=row.get("url"), checks=checks, evidence=evidence, rank_score=row.get("score"))
        elif role not in candidates[cid].role:
            candidates[cid].role += f" / {role}"
        mid = f"model:{model_id}" if model_id else None
        if mid in candidates:
            if cid not in candidates[mid].related:
                candidates[mid].related.append(cid)
            if mid not in candidates[cid].related:
                candidates[cid].related.append(mid)
    for mid, rows in (datasets.get("per_model") or {}).items():
        for row in rows:
            add_dataset(row, "모델 학습·평가", mid)
    for key, role in [("project_training", "프로젝트 학습·평가"), ("service_data", "서비스 데이터")]:
        for row in datasets.get(key) or []:
            add_dataset(row, role)
    summary = [plan.get("summary_ko") or "추천 결과"]
    if constraints.get("commercial_only"):
        summary.append("상업 이용 가능한 모델만")
    for key, label in [("gpu_memory_gb", "GPU 메모리(GB)"), ("min_context_length", "최소 입력 길이(tokens)")]:
        if constraints.get(key) is not None:
            summary.append(f"{label}: {constraints[key]}")
    # language/execution are unknown for every model, so listing them would bury the real items.
    needs = list(dict.fromkeys(f"{c.name}: {k.label}" for c in candidates.values() if c.type == "model"
                               for k in c.checks if k.status != "ok" and k.key not in ("language", "execution")))
    return ChatResult(title=summary[0][:80], summary=summary, needs_check=needs,
                      candidates=list(candidates.values()), assessment=events.get("assessment"))


def build_sources(events: dict[str, Any]) -> list[Source]:
    sources: dict[tuple[str, str, str | None, str], Source] = {}
    def add(sid: str, kind: str, title: str, url: str | None, quote: str | None, origin: str) -> None:
        sources[(sid, kind, quote, origin)] = Source(source_id=sid, kind=kind, title=title, url=url, quote=quote, origin=origin)
    for group in events.get("models") or []:
        for row in group["models"]:
            quote = row.get("evidence")
            add(row["model_id"], "model", row["model_id"], row.get("url"), quote, "readme" if quote else "metadata")
    ds = events.get("datasets") or {}
    rows = [r for group in (ds.get("per_model") or {}).values() for r in group]
    rows += (ds.get("project_training") or []) + (ds.get("service_data") or [])
    for row in rows:
        evidence = row.get("evidence") or [{}]
        for e in evidence:
            quote = e.get("text")
            add(row["dataset"], "dataset", row.get("title") or row["dataset"], row.get("url"), quote,
                "readme" if quote and e.get("source") == "README 인용" else "metadata")
    return list(sources.values())


def build_done(events: dict[str, Any], group_id: UUID, answer: str, elapsed: float) -> ChatDone:
    if events.get("clarify"):
        return ChatDone(type="clarify", group_id=group_id, elapsed=elapsed,
                        answer="\n".join(events["clarify"]["questions"]))
    if not (events.get("plan") or {}).get("needs"):
        return ChatDone(type="reject", group_id=group_id, elapsed=elapsed, answer=REJECT_MESSAGE)
    return ChatDone(type="answer", group_id=group_id, elapsed=elapsed, answer=answer,
                    result=build_result(events), sources=build_sources(events))


def stored_text(done: ChatDone) -> str:
    return done.answer
