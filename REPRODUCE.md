# Reproduce the release artifacts and bounded checks

The complete mathematical argument is in the manuscript. Its 100 named results
include 23 remarks; it contains 80 proof environments, 15 definitions and six
explicit classical inputs. The two executable diagnostics check selected
finite identities and examples. Their precise mapping to the manuscript,
arithmetic methods, provenance and limitations are in
[diagnostics/README.md](diagnostics/README.md).

## Check package integrity

From the extracted archive or release checkout:

```sh
shasum -a 256 -c SHA256SUMS
```

Every listed file should report `OK`. The manifest covers the archived payload,
including the PDF and sources. It does not claim to establish mathematical truth.

## Build the manuscript

Use TeX Live or an equivalent installation with `latexmk` and the standard
packages named in the source. No external figures, private inputs or Python
packages are required for the paper build.

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error neural-construction.tex
```

The build produces `neural-construction.pdf`. The archived PDF is
`neurons-through-the-looking-glass.pdf`. This release was checked as a 79-page
PDF with 945 resolved internal links, no unresolved citations/references and no
overfull boxes. The two changed pages of the public presentation were visually
checked; the other 77 pages render identically to the accepted editorial copy.
Different TeX installations or PDF timestamps can change the rebuilt file hash.

## Run the diagnostics

Python's standard library is sufficient; the recorded run used Python 3.14.7.
From the package root:

```sh
mkdir -p runs/gaussian runs/geometry-action
(cd runs/gaussian && python3 ../../diagnostics/gaussian/checks.py)
(cd runs/geometry-action && python3 ../../diagnostics/geometry-action/ef3_math_check.py)
```

Both commands should exit zero. The Gaussian program writes `check-results.json`
with `status: PASS` and `total_cases: 7328`. The geometry/action program writes
`MATH-CHECK.json` and prints its PASS summary. Original results are preserved as
`expected-results.json` beside each program. Regenerated timestamp fields differ;
floating-point last digits may depend on the platform. The recorded stable
payloads agreed after removing only their timestamp field.

These diagnostics cover sampled Gaussian identities, small noncommuting matrix
examples, ordinary quadrature and exact rational geometry/action examples.
They do not implement or verify the infinite-dimensional construction, the
classical source theorems, or an effective end-to-end approximation schedule.
