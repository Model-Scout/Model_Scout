"""Does the planner ask one clarifying question exactly when the label says so?

Run: python test/golden/run_planner_clarify.py [--runs N]
Uses the configured LLM (RECOMMEND_LLM_PROVIDER=ollama for a local model).
"""

import argparse
import importlib.util
import json
import sys
from pathlib import Path

AI = Path(__file__).resolve().parents[2]
LABELS = Path(__file__).parent / "labels" / "planner_clarify_queries.jsonl"

sys.path.insert(0, str(AI))
spec = importlib.util.spec_from_file_location("recommend_graph", AI / "17_recommend_graph.py")
graph17 = importlib.util.module_from_spec(spec)
sys.modules["recommend_graph"] = graph17
spec.loader.exec_module(graph17)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=1)
    args = parser.parse_args()
    rows = [json.loads(line) for line in LABELS.read_text(encoding="utf-8").splitlines() if line.strip()]
    print(f"model={graph17.LLM_MODEL} runs={args.runs}", flush=True)
    correct = checks = total = 0
    for row in rows:
        questions, stated = [], []
        for _ in range(args.runs):
            try:
                plan = graph17._parse_plan(row["text"], row["target"])
                questions.append(plan.get("clarifying_questions") or [])
                stated.append(plan.get("ai_job_stated"))
            except Exception as error:  # a failed call counts as wrong, not as a crash of the whole run
                questions.append([f"ERROR {type(error).__name__}: {error}"[:120]])
        right = sum(bool(q) == row["ask"] and not (q and q[0].startswith("ERROR")) for q in questions)
        # may_ask: a question is fine if its answer changes the model search; a person reads it to decide.
        review = sum(bool(q) and not row["ask"] and row.get("may_ask", False) and not q[0].startswith("ERROR")
                     for q in questions)
        correct, checks, total = correct + right, checks + review, total + args.runs
        mark = "OK " if right == args.runs else "CHK" if right + review == args.runs else "BAD"
        print(f"{mark} {row['id']} {right}/{args.runs} want={'ask' if row['ask'] else 'none'} "
              f"ai_job_stated={stated} [{row['target']}] {row['text']}", flush=True)
        for q in {q[0] for q in questions if q}:
            print(f"      {q}", flush=True)
    print(f"\naccuracy {correct}/{total}, to review (CHK) {checks}, wrong {total - correct - checks}")


if __name__ == "__main__":
    main()
