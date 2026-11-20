"""Checks a release running on Docker Desktop (deploy/compose.local.yml); writes <release>/verified.json.

    python deploy/local/check_release.py deploy/.releases/<id> [--query]

Without --query nothing calls OpenAI, and production Supabase is only read: the AI's start-up build
check and one `show transaction_read_only`. --query sends one question through the backend (a few
gpt-4o-mini calls and one embedding, under one cent) and then checks that the conversation and its
checkpoint landed in the local postgres and not in production. Every failed check stops the run, so
verified.json exists only for a release that passed.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import subprocess
import sys
import time
import urllib.request
import uuid
from pathlib import Path

COMPOSE = ["docker", "compose", "-f", "deploy/compose.local.yml"]
SERVICES = ("ai", "backend")
PORT = os.environ.get("LOCAL_BACKEND_PORT", "8000")
QUESTION = "서울 따릉이 대여소 실시간 현황으로 대여 가능 대수 예측 서비스를 만들고 싶어"
FAILED = []


def sh(*args, env=None, check=True):
    out = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", env={**os.environ, **(env or {})})
    if check and out.returncode:
        raise RuntimeError(f"{' '.join(args[:6])}…: {out.stderr.strip()[-400:]}")
    return out


def check(name, ok, detail):
    print(f"[{'ok' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAILED.append(name)
    return ok


def exec_py(service, code, env=None):
    """Python inside a running service, from its code folder; returns (exit code, output)."""
    flags = [x for k, v in (env or {}).items() for x in ("-e", f"{k}={v}")]
    workdir = "/app/ai" if service == "ai" else "/app/backend/app"
    out = sh(*COMPOSE, "exec", "-T", *flags, "-w", workdir, service, "python", "-c", code, check=False)
    return out.returncode, (out.stdout + out.stderr).strip()


def psql(sql):
    return sh(*COMPOSE, "exec", "-T", "postgres", "psql", "-U", "model_scout", "-d", "model_scout", "-tAc", sql).stdout.strip()


def ask_backend(session):
    body = json.dumps({"query": QUESTION, "group_id": None, "mode": "recommend", "target_id": None}).encode()
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}/api/chat", body,
                                 {"Content-Type": "application/json", "X-Session-Id": session})
    events, done, started = {}, None, time.time()
    with urllib.request.urlopen(req, timeout=300) as resp:
        event = None
        for raw in resp:
            line = raw.decode("utf-8").rstrip("\n")
            if line.startswith("event:"):
                event = line[6:].strip()
                events[event] = events.get(event, 0) + 1
            elif line.startswith("data:") and event in ("done", "error"):
                done = (event, json.loads(line[5:].strip()))
    return events, done, round(time.time() - started, 1)


PROD_COUNT = """
import json, sys
from supabase_db import db_connection
c = db_connection(); cur = c.cursor()
gid = sys.argv[1] if len(sys.argv) > 1 else {gid!r}
cur.execute("select count(*) from app.groups where group_id = %s", (gid,)); groups = cur.fetchone()[0]
cur.execute("select count(*) from langgraph.checkpoints where thread_id = %s", (gid,)); points = cur.fetchone()[0]
print(json.dumps([groups, points]))
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("release", type=Path)
    parser.add_argument("--query", action="store_true", help="one real question (OpenAI cost, under one cent)")
    args = parser.parse_args()
    record = json.loads((args.release / "release.json").read_text(encoding="utf-8"))
    rid = record["release_id"]
    os.environ.update(RELEASE_DIR=str(args.release.resolve()), MODEL_SCOUT_RELEASE=rid)
    result = {"release_id": rid, "verified_at": None, "images": {}, "checks": {}, "query": None}

    for s in SERVICES:  # the containers run exactly the built images
        cid = sh(*COMPOSE, "ps", "-q", s).stdout.strip()
        running = sh("docker", "inspect", "-f", "{{.Image}}", cid).stdout.strip() if cid else None
        result["images"][s] = running
        check(f"{s} image", running == record["images"][s], f"{(running or 'not running')[7:19]} (built {record['images'][s][7:19]})")

    code, out = exec_py("ai", "import json, hypergraph_search as h; print(json.dumps(h.corpus_identity()))")
    identity = json.loads(out.splitlines()[-1]) if code == 0 else {}
    check("ai serves the release data", identity.get("documents_id") == record["data"]["documents_id"],
          f"documents {str(identity.get('documents_id'))[:16]}, vectors {identity.get('vectors')}" if identity else out[-300:])

    code, out = exec_py("ai", "from supabase_db import db_connection; c = db_connection(); cur = c.cursor(); "
                              "cur.execute('show transaction_read_only'); print(cur.fetchone()[0])")
    check("production Supabase read-only", code == 0 and out.splitlines()[-1] == "on", out.splitlines()[-1] if out else "")
    # The proof: a write is refused. A temp table would vanish with the session anyway, and it is rolled back.
    probe_write = ("from supabase_db import db_connection\nc = db_connection(); cur = c.cursor()\ntry:\n"
                   "    cur.execute('create temp table model_scout_write_probe (i int)'); print('WRITE ALLOWED')\n"
                   "except Exception as e:\n    print(type(e).__name__, str(e).splitlines()[0])\n"
                   "finally:\n    c.rollback(); c.close()")
    for label, opener in (("search", "from supabase_db import db_connection"),
                          ("model search (09)", "import importlib.util as u\ns = u.spec_from_file_location('m09', '09_model_scout_mcp_readonly.py')\n"
                                                "m = u.module_from_spec(s); s.loader.exec_module(m); db_connection = m._db_connection")):
        code, out = exec_py("ai", opener + "\n" + probe_write.split("\n", 1)[1])
        check(f"production Supabase refuses a write ({label})", "read-only transaction" in out, out.splitlines()[-1] if out else "")

    present = psql("select to_regclass('langgraph.checkpoints') is not null and to_regclass('app.groups') is not null")
    check("checkpoint and conversation tables in local postgres", present == "t", present)

    # Guards: a local service with a missing or non-local write target must refuse to start.
    probe = "import importlib.util as u; s = u.spec_from_file_location('rg', '17_recommend_graph.py'); m = u.module_from_spec(s); s.loader.exec_module(m); m.checkpoint_conninfo()"
    for label, url in (("missing", ""), ("production host", "postgresql://u:p@db.example.supabase.co:5432/postgres")):
        code, out = exec_py("ai", probe, {"CHECKPOINT_DATABASE_URL": url})
        check(f"ai refuses checkpoint target ({label})", code != 0 and "MODEL_SCOUT_LOCAL=1" in out, out.splitlines()[-1][:160] if out else "")
    code, out = exec_py("backend", "import main; main._conninfo()", {"SUPABASE_DB_HOST": "db.example.supabase.co"})
    check("backend refuses conversation DB (production host)", code != 0 and "MODEL_SCOUT_LOCAL=1" in out,
          out.splitlines()[-1][:160] if out else "")

    health = urllib.request.urlopen(f"http://127.0.0.1:{PORT}/api/health", timeout=10).read().decode()
    check("backend /api/health on 127.0.0.1", '"ok":true' in health.replace(" ", ""), health)

    if args.query:
        session = str(uuid.uuid4())
        events, done, elapsed = ask_backend(session)
        gid = (done or (None, {}))[1].get("group_id")
        check("query answered", bool(done) and done[0] == "done" and gid, f"{events} in {elapsed}s")
        local = psql(f"select (select count(*) from app.groups where group_id = '{gid}') || ',' || "
                     f"(select count(*) from langgraph.checkpoints where thread_id = '{gid}')") if gid else ""
        check("conversation and checkpoint stored locally", local.split(",")[0] == "1" and local.split(",")[1] not in ("", "0"), local)
        code, out = exec_py("ai", PROD_COUNT.format(gid=gid))
        prod = json.loads(out.splitlines()[-1]) if code == 0 else None
        check("nothing stored in production", prod == [0, 0], str(prod) if prod is not None else out[-200:])
        result["query"] = {"question": QUESTION, "events": events, "elapsed_s": elapsed, "group_id": gid,
                           "local_rows": local, "production_rows": prod, "cost": "OpenAI: a few gpt-4o-mini calls + 1 embedding"}

    stats = sh("docker", "stats", "--no-stream", "--format", "{{.Name}} {{.MemUsage}}").stdout
    restarts = {s: sh("docker", "inspect", "-f", "{{.RestartCount}}", sh(*COMPOSE, "ps", "-q", s).stdout.strip()).stdout.strip() for s in SERVICES}
    errors = {s: sum(("Traceback" in l or " ERROR " in l) for l in sh(*COMPOSE, "logs", s).stdout.splitlines()) for s in SERVICES}
    result["checks"] = {"memory": [l for l in stats.splitlines() if "model-scout-local" in l], "restarts": restarts, "error_log_lines": errors}
    check("no restarts", all(v == "0" for v in restarts.values()), str(restarts))
    print("memory:", *result["checks"]["memory"], sep="\n  ")
    print("error log lines:", errors)

    if FAILED:
        sys.exit(f"release {rid} failed: {', '.join(FAILED)} (no verified.json written)")
    result["verified_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    result["note"] = "one local run: basic behaviour and memory under one request, not a load test; check the VPS after deploying"
    (args.release / "verified.json").write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
