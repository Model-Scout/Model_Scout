"""Generate frontend mock fixtures and schemas from the actual V2 response models.

Run from repository root: python backend/examples/generate.py
All values below are synthetic examples, not verified recommendation/benchmark results.
"""
import json
import sys
from pathlib import Path
from uuid import UUID

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from backend.app.main import app, sse
from backend.app.result import ChatDone, build_done

OUT = Path(__file__).resolve().parent
GID = UUID("00000000-0000-4000-8000-000000000001")


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def generate():
    need = {"task": "retrieval", "purpose_ko": "문서 검색"}
    model = {"model_id": "example/search-model", "rank_score": 0.8,
        "license": "unknown", "commercial_use": "unknown", "context_length": None,
        "evidence": "Example quote for frontend mock rendering only.",
        "gpu_fit": {"verdict": "unknown", "label": "GPU 요구량 미확인"}}
    dataset = {"dataset": "example/documents", "title": "문서 데이터 (Mock)", "licenses": [],
        "source": "huggingface", "url": "https://huggingface.co/datasets/example/documents",
        "evidence": [{"concept": "문서 검색", "source": "README 인용", "text": "Synthetic dataset quote for mock rendering."}]}
    events = {"plan": {"summary_ko": "문서 검색 서비스 (Mock)", "needs": [need],
        "constraints": {"commercial_only": True, "gpu_memory_gb": 8}},
        "models": [{"need": need, "models": [model]}],
        "datasets": {"per_model": {model["model_id"]: [dataset]}, "project_training": [], "service_data": []}}
    answer = build_done(events, GID, "화면 연동을 위한 가상 추천 예시입니다.", 12.5)
    question = ChatDone(type="answer", group_id=GID, elapsed=2.1, answer="저장된 예시에는 GPU 요구량 근거가 없어 확인이 필요해요.",
                        sources=[s for s in answer.sources if s.kind == "model"])
    fixtures = {"answer": answer, "question": question,
        "clarify": build_done({"clarify": {"questions": ["어떤 데이터를 검색하나요?"]}}, GID, "", 1.2),
        "reject": build_done({"plan": {"needs": []}}, GID, "", .2),
        "empty": build_done({"plan": {"needs": [need], "summary_ko": "후보 없음 (Mock)"}}, GID, "조건에 맞는 후보가 없어요.", 4)}
    fixtures["save-failed"] = answer.model_copy(update={"history_saved": False})
    for name, payload in fixtures.items():
        write(f"{name}.json", payload.model_dump(mode="json"))
    write("error.json", {"code": "AI_UNAVAILABLE", "message": "잠시 후 다시 시도해 주세요.", "group_id": str(GID)})
    write("request.json", {"group_id": None, "query": "문서 검색 서비스를 만들고 싶어. 조건: 한국어, 로컬 GPU 8GB, 상업적 이용.",
                           "mode": "recommend", "target_id": None})
    timestamp = "2026-11-06T00:00:00Z"
    write("group.json", {"group_id": str(GID), "title": answer.result.title, "created_at": timestamp,
        "updated_at": timestamp, "result": answer.result.model_dump(), "messages": [
            {"id": 1, "role": "user", "content": "문서 검색", "type": None, "result": None, "sources": [], "created_at": timestamp},
            {"id": 2, "role": "assistant", "content": answer.answer, "type": "answer", "result": answer.result.model_dump(),
             "sources": [s.model_dump() for s in answer.sources], "created_at": timestamp},
            {"id": 3, "role": "user", "content": "GPU 요구량?", "type": None, "result": None, "sources": [], "created_at": timestamp},
            {"id": 4, "role": "assistant", "content": question.answer, "type": "answer", "result": None,
             "sources": [s.model_dump() for s in question.sources], "created_at": timestamp}]})
    write("chat-done.schema.json", ChatDone.model_json_schema())
    write("openapi.json", app.openapi())
    stream = sse("status", {"step": 1, "total": 4, "label": "요구사항 분석", "elapsed": 0})
    stream += sse("token", {"text": answer.answer}) + sse("done", answer.model_dump(mode="json"))
    (OUT / "answer.sse").write_text(stream, encoding="utf-8")
    print("Generated V2 fixtures, SSE and schemas")


if __name__ == "__main__":
    generate()
