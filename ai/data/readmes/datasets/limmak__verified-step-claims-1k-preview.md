---
language:
  - en
  - ko
tags:
  - process-supervision
  - prm
  - math
  - sympy
  - reasoning
  - step-verification
  - math-reasoning
  - verified-claims
size_categories:
  - 1K<n<10K
license: cc-by-nc-4.0
---

# Verified Step Claims 1K (Preview)

**Mathematically verified step-level claims with witness evidence for process supervision research.**

This is a 1K preview sampled from a larger in-progress corpus built from thousands of verified math solvers, covering Korean CSAT (수능), national mock exams, and advanced textbook problems across calculus, probability, sequences, and more.

## What Makes This Different

| | PRM800K (OpenAI) | This Dataset |
|---|---|---|
| **Label source** | Human annotators | SymPy-based verification (simplify + counterexample search) |
| **Granularity** | "Is this step correct?" | Specific claim: `lhs ⊕ rhs` |
| **Evidence** | None (just label) | `sympy_diff`, `counterexample` |
| **Scalability** | Expensive (human labor) | Automated (verifier pipeline) |

Existing process supervision datasets rely on human judgment. This dataset provides **mathematically grounded verdicts**: each claim is verified by SymPy with explicit witness evidence — either a symbolic diff proving equality, or a concrete counterexample disproving it.

## Use Cases

- **PRM / Step-Verifier Training**: Direct `(step, verdict)` pairs for reward model training
- **Math Debugging / Error Detection**: `fail` claims with counterexamples for training error-localization models  
- **Reasoning Chain Validation**: Verify intermediate steps in chain-of-thought outputs

## Schema

| Field | Type | Description |
|---|---|---|
| `node_id` | string | Unique problem identifier (blake2b hash) |
| `tags_C` | list[str] | Concept tags (e.g., `C:Limits`, `C:Probability`) |
| `tags_T` | list[str] | Technique tags (e.g., `T:L'Hopital Rule`) |
| `tags_P` | list[str] | Pattern tags (e.g., `P:Parameter Determination`) |
| `step_index` | int | Step position in solution trace |
| `step_text` | string | Full step text |
| `claim_lhs` | string | Left-hand side of claim |
| `claim_relation` | string | Relation operator (`=`, `<`, `<=`, etc.) |
| `claim_rhs` | string | Right-hand side of claim |
| `verdict` | string | `pass` or `fail` |
| `witness_sympy_diff` | string \| null | `simplify(lhs - rhs)` result. `"0"` for pass. |
| `witness_counterexample` | object \| null | Concrete values disproving the claim (e.g., `{"a": 1}`) |
| `context_prev_steps` | list[str] | Previous 1-2 steps for context |

## Verdict Distribution

- **pass**: 500 (50%) — claim is mathematically verified (`sympy_diff = 0`)
- **fail**: 500 (50%) — claim is disproven with evidence (nonzero diff, which may include numeric or constant expressions like `sqrt(2)`, `log(5)`, or counterexample)

Only strong verdicts are included. Ambiguous or unparseable claims are excluded.

## Examples

### ✅ Pass — Algebraic identity verified

```json
{
  "step_text": "Right limit: (3-a)(-3+4) = 3 - a",
  "claim_lhs": "(3-a)(-3+4)",
  "claim_relation": "=",
  "claim_rhs": "3 - a",
  "verdict": "pass",
  "witness_sympy_diff": "0",
  "context_prev_steps": ["Left limit: (3-a)(3+a) = 9 - a**2"]
}
```

### ❌ Fail — Counterexample provided

```json
{
  "step_text": "Solving for a: a = 3",
  "claim_lhs": "a",
  "claim_relation": "=",
  "claim_rhs": "3",
  "verdict": "fail",
  "witness_sympy_diff": "a - 3",
  "witness_counterexample": {"a": 1},
  "context_prev_steps": ["Tangent slope equation: a*(2*2 + 1) + 5 = 20"]
}
```

### ❌ Fail — Constant diff ≠ 0

```json
{
  "step_text": "Common ratio r^6 = b7/b1 = 54/2 = 27",
  "claim_lhs": "b7/b1",
  "claim_relation": "=",
  "claim_rhs": "54/2",
  "verdict": "fail",
  "witness_sympy_diff": "-20",
  "witness_counterexample": null,
  "context_prev_steps": ["From sum formula: a7 = 2*196/7 - 2 = 54"]
}
```

## Topic Coverage (150+ unique concepts in this preview)

Top categories: Limits, Combinatorics, Arithmetic Sequences, Conditional Probability, Definite Integration, Cubic Functions, Trigonometric Functions, Binomial Distribution, Geometric Sequences, and more.

## Noise Policy

- **Included**: `pass` (sympy_diff = 0) and `fail` with evidence (counterexample or nonzero sympy_diff)
- **Excluded**: `fail_parse` (SymPy couldn't parse), `ambiguous` (context-dependent claims)

## Full Dataset

This 1K preview is sampled from a larger verified claim corpus. The generation pipeline is actively expanding. For access to the full dataset or custom generation for specific domains, please open a Discussion.

## Citation

```bibtex
@dataset{verified_step_claims_2026,
  title={Verified Step Claims: Mathematically Grounded Process Supervision Data},
  year={2026},
  note={Preview release. 1K verified claims with SymPy witness evidence.}
}
```
