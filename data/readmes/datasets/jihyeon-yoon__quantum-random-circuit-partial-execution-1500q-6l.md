---
license: mit
language:
- ko
- en
pretty_name: Random Circuit Partial Execution (1500 qubits, 6 layers)
tags:
- quantum-computing
- quantum-simulation
- tensor-network
- quantum-circuits
- amplitudes
- openqasm
- physics
size_categories:
- 1K<n<10K
viewer: false
---

# Symbolicinfo Q log amplitude dataset

**Simulator contact:** [jihyeon.yoon@symbolicinfo.com](mailto:jihyeon.yoon@symbolicinfo.com)

This directory contains log-encoded circuit amplitudes, the original circuit,
and a Python reader. [한국어 설명서](README.ko.md)

## Files

| File | Contents |
|---|---|
| `amplitudes.npy` | Completed structured log-amplitude array |
| `amplitudes.npy.partial` | Published prefix of an active or interrupted export |
| `manifest.json` | Circuit settings, selection, execution metadata and completion status |
| `circuit.json` | Original gates and binary64 angle bits |
| `circuit.qasm` | Original unmeasured circuit in OpenQASM 3.0 |
| `error_bounds.jsonl` | Per-key slice bounds; created only with an active slice cap |
| `read_log_amplitudes.py` | Log reader and optional amplitude reconstruction helper |
| `README.md` / `README.ko.md` | English / Korean documentation |

## Storage format

Load the array directly with NumPy:

```python
import numpy as np

rows = np.load("amplitudes.npy", mmap_mode="r", allow_pickle=False)
key = int.from_bytes(rows[0]["key"].tobytes(), "little")
```

| Field | Type | Meaning |
|---|---|---|
| `log2_abs` | float64 | Base-2 logarithm of amplitude magnitude |
| `log2_abs_phase` | float64 | Base-2 logarithm of absolute phase in radians |
| `phase_sign` | int8 | Phase sign: -1, 0 or +1 |
| `key` | uint8 array | Fixed-width little-endian key; qubit 0 is the least significant bit |

Phase is the principal argument in [-pi, pi]. Reconstruct phase as
`phase_sign * 2**log2_abs_phase`, or zero when `phase_sign` is zero.
Amplitude is `2**log2_abs * (cos(phase) + 1j*sin(phase))`.
Zero amplitude has both logs -inf and phase_sign 0; zero phase has
log2_abs_phase -inf and phase_sign 0. Reconstruction precision is the reader's choice.
Logs are computed before conversion to float64. This encoding is lossy;
it does not preserve all source precision. Probability need not be stored:
`log2_probability = 2 * log2_abs`.

## Quick start

Run inside this dataset directory:

```sh
python3 -m pip install numpy mpmath

# Read stored log values.
python3 read_log_amplitudes.py . --limit 10

# Read the published prefix of an interrupted export.
python3 read_log_amplitudes.py . --allow-incomplete --limit 10

# Reconstruct requested amplitudes at 256-bit precision.
python3 read_log_amplitudes.py . --restore --limit 10 --precision 256
```

## Python usage

The helper returns the structured array directly by default:

```python
from read_log_amplitudes import load_amplitudes

a = load_amplitudes(".")
print(a[0]["log2_abs"])
```

For on-demand reconstruction, install mpmath and use:

```python
from read_log_amplitudes import load_restored_amplitudes

a = load_restored_amplitudes(".")
z = a[0]
print(z.real, z.imag)
print(a.key(0))
raw_logs = a.raw
```

Only requested rows are reconstructed; z.real and z.imag are high-precision values.
Slices remain lazy. a.key(0) reads a key; a.raw exposes the log array.
No async, threads or result cache. Increasing reconstruction precision cannot
recover information lost by float64 log encoding.

## Circuit and selection

Read `manifest.json` for circuit, source precision, selection and slice semantics.
layers is the configured layer count as a JSON integer: --layers 10 or --depth 10
records "layers": 10. No separate depth or scheduled layer counts are stored.
--max-controls accepts any positive platform-sized integer; the generated
control count is limited by the available qubits, reserving the last wire as
target. Counts above four use MCX gates, exported as ctrl(N) @ x in QASM.
The precise engine contracts these through compact AND/XOR factors, avoiding
an exponentially sized dense matrix for each many-control gate.
## Execution metadata

The manifest's `execution` object (`schema_version: 1`) records the Symbolicinfo Q CPU tensor-network
engine/version, OS, CPU, RAM, worker limits, slicing plan and run measurements.
### Exact and truncated execution

`simulation.mode` is `exact` only when no slices were discarded, even if a slice
cap was configured. Exact does not remove finite-precision or log-encoding error.
Approximation here is slice truncation, not MPS/SVD compression: bond_dimension
and cutoff_error are null with their applicable flags false. Read max_slices,
evaluated/total slices and the per-key error_bounds.jsonl instead.
### Timing

`timing.compile_seconds` includes constant/dense contractions and plan construction.
timing.contraction_seconds covers query engine wall time for all requested keys,
including result callbacks, error-bound calculation, output and progress overhead.
Callbacks may overlap other workers, so result_callback_seconds must not be
subtracted to infer pure contraction time. query_phase_seconds also includes
batch scheduling/flushes. elapsed_before_finalize_seconds ends before final
dataset fsync/rename/publication. All durations use a monotonic clock.
### Memory

`memory.process_*` contains OS-reported RSS and lifetime peak RSS for the whole
process, not contraction-only memory. Buffer estimates are separate and are
not RSS caps. Missing hardware/RSS fields are null, with sources/scopes recorded.
## Completion and partial output

Environment metadata is written before compilation and the plan after compilation;
final query measurements are available only after the query loop completes.
**Only `status: complete` certifies all requested records.** During writing,
amplitudes.npy.partial has a header updated on flush to expose a completed
prefix. The first result is published immediately, then output is flushed at
batch boundaries or after 250 ms / 4096 completed records, checked on result
callbacks. A stalled query can delay a timed flush; an interrupted write can
leave unadvertised trailing bytes.
**There is no resume protocol. Existing directories are never overwritten.**
## Slice error bounds

`error_bounds.jsonl` is created only when a --max-slices cap is active, including
when the cap is large enough to evaluate every slice. --no-approx clears the
cap; the default and --no-approx exports omit this file and report its path as
null in the manifest. The last --max-slices/--no-approx option wins.
When present, the file retains numerical slice bounds, excluding roundoff
and log encoding error. Partial slice sums are not Born probabilities.
## Circuit source

`circuit.json` includes original binary64 gate angle bits.
circuit.qasm is OpenQASM 3.0 source for the original unmeasured zero-input circuit.
It uses stdgates.inc, an explicit RZZ definition and ctrl modifiers for multi-control X.
Gate order and qubit order are preserved; decimal angles round-trip to binary64.
Slice limits and precision settings are simulator metadata, not QASM gates.

## License

MIT License.
