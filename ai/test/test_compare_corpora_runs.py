"""A comparison run keeps its own folder: existing rankings are never replaced unless asked."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))
spec = importlib.util.spec_from_file_location("compare_runs", AI / "test/public_data/corpus_v2/compare_corpora.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)


def test_a_run_folder_is_never_overwritten(tmp_path, monkeypatch):
    (tmp_path / "rankings_v2.jsonl").write_text("{}\n", encoding="utf-8")
    monkeypatch.setattr(cc.hs, "use_corpus", lambda name: pytest.fail("searched before refusing"))
    with pytest.raises(SystemExit, match="exists"):
        cc.run("v2", tmp_path)


def test_scoring_reads_the_aliases_saved_with_the_run(tmp_path):
    (tmp_path / "aliases.json").write_text(json.dumps([["a/x", "b/x"]]), encoding="utf-8")
    assert cc.saved_aliases(tmp_path) == {"a/x": {"a/x", "b/x"}, "b/x": {"a/x", "b/x"}}


LABEL = {"query_id": "p1", "query": "주차장", "dataset_terms": ["주차장"], "conditions": {"delivery": "any"}}


def fake_run(monkeypatch, tmp_path, groups):
    labels = tmp_path / "labels.jsonl"
    labels.write_text(json.dumps(LABEL, ensure_ascii=False) + "\n", encoding="utf-8")
    monkeypatch.setattr(cc.hs, "use_corpus", lambda name: {"corpus": name})
    monkeypatch.setattr(cc, "alias_groups", lambda: groups)
    monkeypatch.setattr(cc, "use_saved_vectors", lambda allow: ({}, {}))
    monkeypatch.setattr(cc.ev, "_public_top", lambda label, depth: [])
    monkeypatch.setattr(cc.ev, "evaluate", lambda: [])
    monkeypatch.setattr(cc, "read_jsonl", lambda p: [LABEL] if Path(p) == labels else [])
    return labels


def test_a_second_corpus_run_keeps_the_first_runs_aliases_or_stops(tmp_path, monkeypatch):
    labels = fake_run(monkeypatch, tmp_path, [["a/x", "b/x"]])
    cc.run("v1", tmp_path / "run", labels)
    saved = (tmp_path / "run" / "aliases.json").read_bytes()
    cc.run("v2", tmp_path / "run", labels)  # same duplicate list: the file is left as it was
    assert (tmp_path / "run" / "aliases.json").read_bytes() == saved
    (tmp_path / "run" / "rankings_v2.jsonl").unlink()
    monkeypatch.setattr(cc, "alias_groups", lambda: [["a/x", "c/x"]])
    with pytest.raises(SystemExit, match="another duplicate list"):
        cc.run("v2", tmp_path / "run", labels)
    assert (tmp_path / "run" / "aliases.json").read_bytes() == saved and not (tmp_path / "run" / "rankings_v2.jsonl").exists()
    monkeypatch.setattr(cc, "alias_groups", lambda: [["a/x", "b/x"]])
    other = tmp_path / "labels2.jsonl"
    other.write_text(json.dumps({**LABEL, "query": "다른 질문"}, ensure_ascii=False) + "\n", encoding="utf-8")
    monkeypatch.setattr(cc, "read_jsonl", lambda p: [{**LABEL, "query": "다른 질문"}] if Path(p) == other else [])
    with pytest.raises(SystemExit, match="other questions"):
        cc.run("v2", tmp_path / "run", other)


def test_rescoring_checks_the_saved_hashes(tmp_path, monkeypatch):
    labels = fake_run(monkeypatch, tmp_path, [["a/x", "b/x"]])
    cc.run("v2", tmp_path / "run", labels)
    cc.check_run_record(tmp_path / "run", [{**LABEL, "relevant": {"a/x": 2}}])  # judgments may differ
    with pytest.raises(SystemExit, match="other questions"):
        cc.check_run_record(tmp_path / "run", [{**LABEL, "conditions": {"delivery": "api"}}])
    (tmp_path / "run" / "aliases.json").write_text("[]\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="not the duplicate list"):
        cc.check_run_record(tmp_path / "run", [LABEL])


def test_a_run_records_line_end_free_hashes(tmp_path):
    # Windows 작업본(CRLF)과 git·Linux·Mac(LF)에서 같은 파일이 같은 해시를 가져야 재채점이 거부되지 않는다
    (tmp_path / "lf.jsonl").write_bytes(b'{"a": 1}\n{"b": 2}\n')
    (tmp_path / "crlf.jsonl").write_bytes(b'{"a": 1}\r\n{"b": 2}\r\n')
    assert cc.file_record(tmp_path / "lf.jsonl")["sha256"] == cc.file_record(tmp_path / "crlf.jsonl")["sha256"]
