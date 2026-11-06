# Reproduce the document

Use an existing local TeX Live installation with latexmk, pdfLaTeX and the
standard packages declared by the source. From this extracted package:

    sh paper/build.sh

The result is `paper/output/neural-construction.pdf`. The distributed paper is
`paper/neurons-through-the-looking-glass-v2.pdf`. The bibliography is supplied
in `references.bib`; latexmk runs BibTeX as needed. No network, credentials,
external figures, hosted CI or cloud compute is required by the build.

The script fixes the source date and timezone. PDF bytes can still vary with
TeX/toolchain versions or build paths. The release checks compare text, rendered
pages, source hashes and the exact distributed PDF separately.

Two inherited TeX diagnostics report ignored infinite glue shrinkage in long
tables. The baseline and candidate retain those diagnostics. Their affected
pages require visual inspection; a zero process exit code alone does not prove
layout quality. This is not a warning-free build claim.

`SHA256SUMS` identifies every exported payload file except itself. Check it from
the package root with `shasum -a 256 -c SHA256SUMS` on macOS, or an equivalent
local SHA-256 checker.

This is a document reproduction package. The original private symbolic selector
software, its source trees and review transcripts are not exported. Software
contracts in the manuscript retain their historical exact versions and source
premises; they do not claim an executable simulator is included here. The old
version 1 finite diagnostics remain available in its separately archived release
and do not validate the new quantitative or composite results.

The build and checksums establish document reproduction and identity. The
mathematical arguments, classical citations and full named assumptions determine
the scientific claims. See `REVIEW.md` and `paper/COMPANION-INDEX.md` for scope.
