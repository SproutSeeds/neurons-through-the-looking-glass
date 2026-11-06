#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p output
SOURCE_DATE_EPOCH=1793966400 FORCE_SOURCE_DATE=1 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=output neural-construction.tex
