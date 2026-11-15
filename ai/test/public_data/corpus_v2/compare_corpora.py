"""Compare corpus v1 and v2 under the same questions, query vectors and search settings.

    python test/public_data/corpus_v2/compare_corpora.py run --corpus v1
    python test/public_data/corpus_v2/compare_corpora.py run --corpus v2
    python test/public_data/corpus_v2/compare_corpora.py score [--labels L] [--unjudged-out F]

`run` saves, per question, the top 30 datasets the public evaluation reads (22's _public_top: the
same terms, roles and filters), the top 30 for the 14 proposed v2-specific questions, and 22's
quality scenarios. Query vectors come from compare/query_vectors.jsonl only, so both corpora
search with the same vectors and no run calls the embedding API (--allow-embed adds missing ones).
`score` re-scores saved rankings against one label file, so new judgments need no new search.

The saved compare/rankings_*.jsonl were searched on 2026-11-13 against v2 documents_id f2fd56aa
(not the later pinned 04239c20); `run` today searches whatever v2 build is checked out, so it makes a
new comparison rather than reproducing that record (compare/README.md, "실험 기준").

A judged dataset also matches its copies only when the v2 graph still records them as duplicates
(v2's refinement confirmed them); v1's merges that v2 split are not credited, on either side.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AI = HERE.parents[2]
sys.path.insert(0, str(AI))
import hypergraph_search as hs  # noqa: E402

_spec = importlib.util.spec_from_file_location("eval22", AI / "22_eval_recommendations.py")
ev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ev)

OUT = HERE / "compare"
VECTORS = OUT / "query_vectors.jsonl"
LABELS = HERE / "golden_prep" / "batch2" / "labels_llm_v4.jsonl"
PROPOSED = HERE / "golden_prep" / "proposed_queries.jsonl"
V2_ENTITIES = AI / "data" / "hypergraph_v2" / "entities.jsonl"
DEPTH = 3 * ev.K


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path, rows):
    Path(path).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def vector_key(model, text):
    return hashlib.sha256(f"{model}\n{text}".encode()).hexdigest()  # same key as golden_prep.query_vectors


def use_saved_vectors(allow_embed):
    """Route hs.embed_query to the saved vectors; a missing one stops the run unless allowed."""
    cache = {r["key"]: r["vector"] for r in read_jsonl(VECTORS)} if VECTORS.exists() else {}
    added = []
    real = hs._embed_query

    def lookup(text, model):
        key = vector_key(model, text)
        if key not in cache:
            if not allow_embed:
                raise SystemExit(f"저장된 질문 벡터 없음 (API 호출 안 함, --allow-embed로 추가): {text[:40]}")
            cache[key] = real(text, model)
            added.append(text)
        return cache[key]

    hs._embed_query = lookup
    return cache, added


def proposed_as_label(p):
    """A proposed question searched like a label: its pool terms + region, roles=service."""
    return {"query": p["query"], "dataset_terms": p["pool_terms"], "conditions": p["conditions"]}


def run(corpus, allow_embed):
    identity = hs.use_corpus(corpus)
    cache, added = use_saved_vectors(allow_embed)
    rows = [{"kind": "identity", "corpus": corpus, **identity}]
    for label in read_jsonl(LABELS):
        rows.append({"kind": "public", "query_id": label["query_id"], "top": ev._public_top(label, DEPTH)})
    for p in read_jsonl(PROPOSED):
        rows.append({"kind": "proposed", "query_id": p["query_id"], "top": ev._public_top(proposed_as_label(p), DEPTH)})
    for name, p, r, mrr, note in ev.evaluate():
        rows.append({"kind": "scenario", "name": name, "p10": p, "r10": r, "mrr": mrr, "note": note})
    OUT.mkdir(exist_ok=True)
    write_jsonl(OUT / f"rankings_{corpus}.jsonl", rows)
    if added:
        write_jsonl(VECTORS, [{"key": k, "vector": v} for k, v in cache.items()])
    print(f"{corpus}: {len(rows) - 1} rankings -> {OUT / f'rankings_{corpus}.jsonl'}"
          f" (documents_id {identity.get('documents_id') or '-'}, vectors {identity.get('vectors')}, new query vectors {len(added)})")


def confirmed_aliases():
    """name -> names counted as the same dataset: duplicates the v2 refinement kept."""
    out = {}
    for e in read_jsonl(V2_ENTITIES):
        if e["kind"] == "dataset":
            names = {e["name"], *(e.get("duplicates") or [])}
            for name in names:
                out[name] = names
    return out


def score_public(label, deep, alias):
    grades = {}
    for dataset, grade in label["relevant"].items():
        for name in alias.get(dataset, {dataset}):
            grades[name] = max(grade, grades.get(name, 0))
    excluded = {n for d in label["must_exclude"] for n in alias.get(d, {d})}
    judged = set(grades) | excluded | {n for d in label["judged_irrelevant"] for n in alias.get(d, {d})}
    pending = {n for d in label["unjudged"] for n in alias.get(d, {d})}
    top = deep[:ev.K]
    result = {
        "unjudged": [d for d in top if d not in judged],
        "held": [d for d in top if d in pending],
        "excluded_in_top": sum(d in excluded for d in top),
    }
    if label["expected_behavior"] == "abstain":
        result["abstain_hits"] = sum(d in excluded or d in grades for d in top)
        return result
    condensed = [d for d in deep if d in judged][:ev.K]
    result["raw"] = ev._metrics(top, grades, label["relevant"])
    result["condensed"] = ev._metrics(condensed, grades, label["relevant"])
    result["judged10"] = sum(d in judged for d in top) / ev.K
    return result


def mean(rows, key, i):
    vals = [r[key][i] for r in rows if key in r]
    return sum(vals) / len(vals) if vals else float("nan")


def score(labels_path, unjudged_out):
    labels = {r["query_id"]: r for r in read_jsonl(labels_path)}
    runs = {}
    for corpus in ("v1", "v2"):
        rows = read_jsonl(OUT / f"rankings_{corpus}.jsonl")
        runs[corpus] = {"identity": rows[0], **{k: {r.get("query_id") or r["name"]: r for r in rows[1:] if r["kind"] == k}
                                                for k in ("public", "proposed", "scenario")}}
    alias = confirmed_aliases()
    print(f"labels {labels_path.name} | aliases: duplicates kept by v2")
    for corpus, r in runs.items():
        i = r["identity"]
        print(f"  {corpus}: corpus_id {str(i.get('corpus_id'))[:16]} documents_id {str(i.get('documents_id'))[:16]} vectors {i.get('vectors')}")

    # 1. common questions (58)
    per = {c: {} for c in runs}
    for corpus, r in runs.items():
        for qid, label in labels.items():
            if not label["evaluable"]:
                continue
            per[corpus][qid] = score_public(label, r["public"][qid]["top"], alias)
    head = "P@10  R@10  MRR   nDCG"
    print(f"\n[공통 질문] raw | condensed (미판정 제외)  judged@10")
    for corpus in runs:
        rows = [x for x in per[corpus].values() if "raw" in x]
        raw = " ".join(f"{mean(rows, 'raw', i):.2f}" for i in range(4))
        con = " ".join(f"{mean(rows, 'condensed', i):.2f}" for i in range(4))
        jd = sum(x["judged10"] for x in rows) / len(rows)
        print(f"  {corpus} ({len(rows)}문항)  {head}: {raw} | {con}  {jd:.2f}")
    print("\n  질문별 (condensed nDCG / raw P@10, v1 -> v2, 변화가 있는 것만)")
    changes = []
    for qid in labels:
        a, b = per["v1"].get(qid), per["v2"].get(qid)
        if a and b and "raw" in a:
            d = b["condensed"][3] - a["condensed"][3]
            if abs(d) > 1e-9 or abs(b["raw"][0] - a["raw"][0]) > 1e-9:
                changes.append((d, qid, a, b))
    for d, qid, a, b in sorted(changes, key=lambda x: x[0]):
        print(f"    {qid} {labels[qid]['query_type']:<12} nDCG {a['condensed'][3]:.2f} -> {b['condensed'][3]:.2f} ({d:+.2f})"
              f"  P@10 {a['raw'][0]:.2f} -> {b['raw'][0]:.2f}  judged@10 {a['judged10']:.1f} -> {b['judged10']:.1f}")
    for corpus in runs:
        for qid, x in per[corpus].items():
            if "abstain_hits" in x:
                print(f"  abstain {qid} {corpus}: 판정된 관련·제외 데이터 {x['abstain_hits']}개가 상위 10에")
            for d in x["held"]:
                print(f"  held {qid} {corpus}: {d} (공식 확인 대기, 맞음·틀림으로 세지 않음)")
    skipped = [q for q, l in labels.items() if not l["evaluable"]]
    if skipped:
        print(f"  평가 제외(evaluable=false): {', '.join(skipped)}")

    # 2. proposed v2-specific questions (selection bias: reported apart)
    print("\n[v2 특화 제안 질문 14개] 설계 목표 데이터의 순위 (상위 30, 없으면 -)")
    for p in read_jsonl(PROPOSED):
        cells = []
        for corpus, r in runs.items():
            top = r["proposed"][p["query_id"]]["top"]
            ranks = [str(top.index(t) + 1) if t in top else "-" for t in p["designer_targets"]]
            cells.append(f"{corpus} {','.join(ranks)}")
        print(f"  {p['query_id']:<7} {p['variant_kind']:<10} {' | '.join(cells)}   {p['query'][:40]}")

    # 3. quality scenarios (22's model/dataset golden set)
    print("\n[기존 품질 시나리오] P@10 / R@10 / MRR")
    for name in runs["v1"]["scenario"]:
        cells = []
        for corpus, r in runs.items():
            s = r["scenario"].get(name) or {}
            fmt = lambda v: "  -  " if v is None else f"{v:.2f}"  # noqa: E731
            cells.append(f"{corpus} {fmt(s.get('p10'))} {fmt(s.get('r10'))} {fmt(s.get('mrr'))}")
        print(f"  {name:<34} {' | '.join(cells)}")
    for corpus, r in runs.items():
        vals = [s for s in r["scenario"].values() if s["p10"] is not None]
        print(f"  {corpus} mean P@10 {sum(s['p10'] for s in vals) / len(vals):.2f} ({len(vals)}개, 기준 0.65)")

    if unjudged_out:
        union = {}
        for corpus in runs:
            for qid, x in per[corpus].items():
                for d in x["unjudged"]:
                    key = (qid, d)
                    union.setdefault(key, {"query_id": qid, "dataset_id": d, "held": d in x["held"], "found_by": []})
                    union[key]["found_by"].append(corpus)
        write_jsonl(unjudged_out, list(union.values()))
        both = sum(len(u["found_by"]) == 2 for u in union.values())
        print(f"\n미판정 (질문, 데이터) {len(union)}쌍 (v1·v2 공통 {both}) -> {unjudged_out}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    r = sub.add_parser("run")
    r.add_argument("--corpus", choices=("v1", "v2"), required=True)
    r.add_argument("--allow-embed", action="store_true", help="embed questions missing from compare/query_vectors.jsonl")
    s = sub.add_parser("score")
    s.add_argument("--labels", type=Path, default=LABELS)
    s.add_argument("--unjudged-out", type=Path)
    args = parser.parse_args()
    if args.command == "run":
        run(args.corpus, args.allow_embed)
    else:
        score(args.labels, args.unjudged_out)


if __name__ == "__main__":
    main()
