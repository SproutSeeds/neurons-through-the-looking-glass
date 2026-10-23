# Bounded diagnostics for Neurons Through the Looking Glass

The manuscript contains the mathematical construction, with 100 named results
(including 23 remarks) and 80 proof environments. These two small, deterministic
programs provide finite diagnostics for selected formulas. They do not verify
the whole construction theorem, reflection positivity of an infinite law,
continuum or infinite-volume convergence, classical source theorems, or the
internal review process.

## Contents and scope

| Folder | Program | Saved result | Manuscript connection | Scope |
| --- | --- | --- | --- | --- |
| `diagnostics/gaussian/` | `checks.py` | `expected-results.json` | Theorems 7.2, 7.6 and 7.8 (`thm:G-shift`, `thm:G-diff`, `thm:G-bounds`); diagonal constant (2), `eq:ca` | 2,835 sampled spectral checks with 70-digit Decimal arithmetic; 2,403 sampled logarithmic-majorant checks; 2,070 displacement checks; 14 noncommuting 2-by-2 resolvent/PSD examples; six ordinary Simpson quadratures. Total: 7,328 finite cases. |
| `diagnostics/geometry-action/` | `ef3_math_check.py` | `expected-results.json` | Remark 6.8 (`rem:rotated`), invariant-potential Corollary 6.7 (`cor:E-general`), polynomial action (7), `eq:vV`, and bounded-width parameter map Lemma A.2 (`lem:E-fields`) | Exact rational geometry and positive-area margins for the displayed rotated square; a pi/4 invariant-square control; 578 axis-parallel point/boundary cases; ten rational action/bound examples with negative controls; the width-one constant-action and clipped-map checks. |

The Gaussian script's `am=1` quadrature row checks an endpoint limiting expression.
The paper's regulated increment theorem still assumes `0 < a < 1/m`.
Two-by-two positive-semidefinite matrix examples supply no continuum or
pointwise-kernel ordering proof. Decimal arithmetic and ordinary floating-point
quadrature are diagnostics; neither is interval certification.

The geometry script shows failure of the required potential symmetry for one
rotated square. It establishes no failure of reflection positivity for that
square. Its pi/4 control is relevant to the general invariant-potential clause;
the manuscript's physical-square definition stays axis-parallel. The positive
rational value substituted for `c_a` is an algebraic test value, not a computed
physical Wick variance.

## Reproduce

Only Python's standard library is needed. The programs were rerun with
Python 3.14.7 on 23 October 2026. No network access, third-party Python package,
private input, sampling data, or predecessor code archive is needed.

Run from the companion-package root:

```sh
mkdir -p runs/gaussian runs/geometry-action
(cd runs/gaussian && python3 ../../diagnostics/gaussian/checks.py)
(cd runs/geometry-action && python3 ../../diagnostics/geometry-action/ef3_math_check.py)
```

Both commands exit zero on successful checks. The first prints a JSON record
with `status: PASS` and `total_cases: 7328`, and writes
`runs/gaussian/check-results.json`. The second prints its PASS summary and
writes `runs/geometry-action/MATH-CHECK.json`. Its second printed line preserves
the historical audit wording concerning the pi/4 control.

The saved results are the original historical diagnostic records, retained
without edits. The emitted `REPORT.md` pointer and stage labels such as F2,
D10 and T5 refer to the private EF3 audit record. For the public arguments,
use the manuscript locations in the scope table above. Regenerated timestamps differ. After omitting only the timestamp
keys `generated_at_utc` and `at`, the regenerated payloads matched the saved
records on the checked machine. The geometry result also records the SHA-256 of
its script; keep the supplied program bytes unchanged for that comparison.
Floating-point last digits can depend on the platform. All rational comparisons
inside the geometry program use `fractions.Fraction` exactly.

## Provenance and license

The programs and expected-result records are unchanged copies of the project's
GB and EF3 foundation diagnostic artifacts, under Cody Mitchell's direction.
Both tasks requested GPT-6 Astra at max effort through the included native
subscription. Their retained execution records specify the requested model;
separate response-model telemetry was unavailable. These are internal model
work products; their finite results are supporting evidence for the specific
formulas listed above.

The software, saved diagnostic records and this documentation are licensed under
Apache License 2.0; preserve the accompanying `LICENSE` and attribution. The
manuscript, its source, bibliography and compiled bibliography use CC BY 4.0 as
stated by the release. Prior published code archives retain their own notices
and identities; these programs do not depend on those archives.
