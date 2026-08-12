set shell := ["bash", "-euo", "pipefail", "-c"]

cv_dir := "CV_assemble"
venv_dir := ".venv"

# List available recipes
default:
    @just --list

# Create the virtualenv (via uv) if it doesn't already exist
venv:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ -d "{{venv_dir}}" ]; then
        echo "venv already exists at {{venv_dir}}"
    else
        uv venv {{venv_dir}}
        echo "venv created at {{venv_dir}}"
    fi

# Generate cv.tex from cv_profile.toml
tex: venv
    {{venv_dir}}/bin/python {{cv_dir}}/build_tex_cv.py \
        --input {{cv_dir}}/cv_profile.toml --output {{cv_dir}}/cv.tex

# Compile cv.tex to a PDF (run twice for stable refs/links)
pdf: tex
    cd {{cv_dir}} && pdflatex -interaction=nonstopmode cv.tex
    cd {{cv_dir}} && pdflatex -interaction=nonstopmode cv.tex
    @rm -f {{cv_dir}}/cv.aux {{cv_dir}}/cv.log {{cv_dir}}/cv.out

# Full build: regenerate tex, compile, and drop a dated PDF at the repo root
build: pdf
    #!/usr/bin/env bash
    set -euo pipefail
    dated="./Michael_J_Lippincott_CV_$(date +%Y_%m).pdf"
    mv {{cv_dir}}/cv.pdf "$dated"
    echo "PDF built successfully: $dated"

# Remove build artifacts
clean:
    rm -f {{cv_dir}}/cv.aux {{cv_dir}}/cv.log {{cv_dir}}/cv.out {{cv_dir}}/cv.pdf

all: build clean
