"""Retrieval experiment lab: query-type planner, pre-retrieval, dense+sparse fusion.

Pipeline (see retrieval_lab/README.md):
    query -> pre-retrieval (rewrite / decomposition / multi-query / HyDE)
          -> retrieval plan (hard filters, weights, top_k)
          -> dense (BGE-M3) + sparse (fielded BM25) over hard-filtered rows
          -> weighted RRF -> top-k candidates
"""
