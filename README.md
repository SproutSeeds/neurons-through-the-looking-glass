# Neurons Through the Looking Glass

**Constructing an Interacting Quantum Field in Two Dimensions**  
Cody Mitchell, Fractal Research Group (independent researcher) · Version 1 · 23 October 2026

[Read the paper](https://doi.org/10.5281/zenodo.23603995) · [Archived source and supporting materials](https://doi.org/10.5281/zenodo.23603997) · [PDF](paper/neurons-through-the-looking-glass.pdf)

Can random building blocks be assembled into an interacting quantum field?
This paper gives two process-neuron constructions that approach the established
massive, weakly coupled two-dimensional Wick-quartic field. Their normalized
interacting laws preserve reflection positivity across the two central
coordinate axes at every finite stage. One deterministic sequence works for
both architectures and for compactly supported measurements chosen afterwards.

The proof establishes whole-field weak convergence on local negative Sobolev
space, local-seminorm moment convergence and compact-test joint correlations at
every order. Classical results supply the infinite-volume target and its
relativistic reconstruction; the paper identifies the inputs and checks their
hypotheses where used.

## Scope

The building blocks are stochastic processes: products of independent telegraph
sign processes and a stationary signed Mondrian tessellation. Finite width counts
whole process neurons; each uses countably many random variables globally.
The common limiting sequence is existential. An effective end-to-end schedule,
computational speedup and extensions to other field models remain open.
The target field and reflection positivity itself are classical. The contribution
is the specified neural construction and convergence argument, with the bounded
prior-work comparison stated in the paper.

## Read and reproduce

- `paper/` contains the complete manuscript PDF, LaTeX source, bibliography and
  compiled bibliography. The paper has no external figures.
- `REPRODUCE.md` describes the supporting checks and their limits.
- `REVIEW.md` describes internal review, provenance and the public export boundary.
- `SHA256SUMS` identifies every release payload file other than the manifest itself.

Build the paper with a TeX Live installation containing the standard packages
used by the source:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error neural-construction.tex
```

The generated file is `neural-construction.pdf`. The distributed PDF is named
`neurons-through-the-looking-glass.pdf`. A rebuild may differ in PDF timestamps;
the source hashes and release manifest identify the archived version.

## Related work from this project

This is a new whole-plane construction manuscript, continuing the finite-volume
study [Positivity Before the Limit](https://doi.org/10.5281/zenodo.23095904)
and the earlier [Determinism, Not Finiteness](https://doi.org/10.5281/zenodo.23130675).
It is released as a new paper rather than a replacement version of either.

## Attribution and license

The manuscript discloses the roles of Claude Opus 5.5, GPT-6 Astra and GPT-6.1 Sol
under Cody Mitchell's direction, including adopted arguments and internal model
reviews. Internal review is distinct from independent expert peer review and
formal proof certification. See the provenance appendix and `REVIEW.md`.

Paper and its source: CC BY 4.0 (`LICENSE-PAPER.md`). Software and project
documentation: Apache 2.0 (`LICENSE`). Citation metadata is in `CITATION.cff`.
