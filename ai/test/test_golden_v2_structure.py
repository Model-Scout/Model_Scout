"""골든셋 v2 구조 검증(--structure-only)과 재적재 Action 의 스냅샷 분리.

골든셋 v2 의 eligible 수와 정답 후보는 2026-10-31 Supabase active 동결본
(test/golden/v2/corpus_snapshot.jsonl, gitignore 대상)에 묶여 있다. 이 파일은 GitHub
runner 에 없고, 새 전체 재적재의 입력도 기준도 아니다. 재적재 Action 은 스냅샷 없이
할 수 있는 구조 검사만 한다.

    python test/test_golden_v2_structure.py
"""

from __future__ import annotations

import contextlib
import copy
import io
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
V2 = ROOT / "test" / "golden" / "v2"
sys.path.insert(0, str(V2 / "tools"))
sys.path.insert(0, str(ROOT / "retrieval_lab"))

import corpus_v2  # noqa: E402
import verify  # noqa: E402

TYPES = sorted(path.stem for path in (V2 / "judged").glob("*.jsonl"))
WORKFLOW = ROOT.parent / ".github" / "workflows" / "model-scout-reingest.yml"


@contextlib.contextmanager
def no_snapshot():
    """구조 검사가 스냅샷을 열면 실패하게 한다. runner 와 같은 조건이다."""
    original = corpus_v2.load_rows

    def refuse():
        raise AssertionError("구조 검사가 코퍼스 스냅샷을 읽었다")

    corpus_v2.load_rows = refuse
    try:
        yield
    finally:
        corpus_v2.load_rows = original


def _judged_copy(mutate):
    """judged/ 를 임시 폴더에 복사하고 한 유형의 레코드를 바꾼다."""
    temp = tempfile.TemporaryDirectory()
    target = Path(temp.name)
    for query_type in TYPES:
        records = verify.read_records(query_type)
        records = mutate(query_type, copy.deepcopy(records)) or records
        (target / f"{query_type}.jsonl").write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), encoding="utf-8")
    return temp, target


def _problems(mutate):
    temp, target = _judged_copy(mutate)
    with temp, no_snapshot():
        return verify.check_structure(TYPES, target)


def test_committed_golden_set_passes_without_the_snapshot():
    with no_snapshot():
        assert verify.check_structure(TYPES) == []


def test_cli_structure_only_needs_no_snapshot():
    out = io.StringIO()
    with no_snapshot(), contextlib.redirect_stdout(out):
        old = sys.argv
        sys.argv = ["verify.py", "--structure-only"]
        try:
            verify.main()
        finally:
            sys.argv = old
    assert "구조 검증 통과" in out.getvalue()


def test_duplicate_query_id_fails_even_across_types():
    def mutate(query_type, records):
        if query_type == TYPES[1]:
            records[0]["query_id"] = verify.read_records(TYPES[0])[0]["query_id"]
        return records

    assert any("query_id 중복" in p for p in _problems(mutate))


def test_wrong_count_per_type_fails():
    assert any("질의 수 9개" in p for p in _problems(lambda t, r: r[:-1] if t == TYPES[0] else r))


def test_unknown_condition_key_fails():
    def mutate(query_type, records):
        if query_type == "structured_constraint":
            records[0]["conditions"]["max_vram_gb"] = 8
            records[0]["conditions_fidelity"]["max_vram_gb"] = "8GB"
        return records

    assert any("하드 필터가 모르는 조건" in p for p in _problems(mutate))


def test_condition_without_query_evidence_fails():
    def mutate(query_type, records):
        if query_type == "structured_constraint":
            key = next(iter(records[0]["conditions"]))
            records[0]["conditions_fidelity"][key] = "  "
        return records

    assert any("질의문 근거 없는 조건" in p for p in _problems(mutate))


def test_missing_keys_and_broken_json_fail():
    def drop_key(query_type, records):
        if query_type == TYPES[0]:
            del records[0]["conditions"]
        return records

    assert any("필수 키 없음" in p for p in _problems(drop_key))
    temp, target = _judged_copy(lambda t, r: r)
    with temp:
        (target / f"{TYPES[0]}.jsonl").write_text('{"query_id": \n', encoding="utf-8")
        assert any("JSON 형식 오류" in p for p in verify.check_structure(TYPES, target))


def test_abstention_invariants_are_structural():
    def mutate(query_type, records):
        if query_type == "abstention":
            records[0]["expected_behavior"] = "recommend"
            records[1]["expected_any"] = ["org/model"]
        return records

    problems = _problems(mutate)
    assert any("expected_behavior=recommend" in p for p in problems)
    assert any("abstention인데 정답" in p for p in problems)


def test_verifier_keys_match_the_planner():
    import planner

    assert verify.HARD_FILTER_KEYS == set(planner.HARD_FILTER_KEYS)


# ── 재적재 Action ─────────────────────────────────────────────────────────

def _runs():
    flow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    return {
        step["name"]: step.get("run", "")
        for job in flow["jobs"].values()
        for step in job["steps"]
    }


def test_reingest_workflow_does_not_need_the_ignored_snapshot():
    text = "\n".join(_runs().values())
    for line in text.splitlines():
        if "verify.py" in line:
            assert "--structure-only" in line, line
    assert "--compare" not in text, "coverage --compare 는 옛 스냅샷을 읽는다"
    assert "corpus_snapshot" not in text


def test_reingest_workflow_keeps_the_taxonomy_and_project_checks():
    """taxonomy 는 모델 commercial_status·task 분류·라이선스 정규화가 쓴다."""
    checks = _runs()["Offline retrieval checks"]
    assert "python taxonomy.py" in checks and "python project_checks.py" in checks


def test_old_snapshot_stays_out_of_git():
    tracked = subprocess.run(
        ["git", "ls-files", "--", "test/golden/v2/corpus_snapshot.jsonl"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.strip()
    assert tracked == "", "옛 스냅샷이 Git 에 들어갔다"
    attributes = (ROOT.parent / ".gitattributes").read_text(encoding="utf-8")
    assert "corpus_snapshot" not in attributes, "옛 스냅샷이 LFS 대상이 됐다"
    ignored = subprocess.run(
        ["git", "check-ignore", "-q", "test/golden/v2/corpus_snapshot.jsonl"], cwd=ROOT,
    )
    assert ignored.returncode == 0


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
