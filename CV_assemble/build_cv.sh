#!/bin/bash

# Build CV from LaTeX markdown file

# Compile LaTeX to PDF
pdflatex -interaction=nonstopmode CV.md

# Clean up auxiliary files
rm -f CV.aux CV.log CV.out

echo "PDF built successfully: CV.pdf"
