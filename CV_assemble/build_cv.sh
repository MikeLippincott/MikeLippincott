#!/bin/bash

# Build CV from LaTeX markdown file

# Compile LaTeX to PDF
pdflatex -interaction=nonstopmode CV.md

# Clean up auxiliary files
rm -f CV.aux CV.log CV.out

current_year=$(date +%Y)
mv CV.pdf ../Michael_J_Lippincott_CV_${current_year}.pdf

# remove previous year's CV
if [ -f ../Michael_J_Lippincott_CV_$((current_year - 1)).pdf ]; then
    rm ../Michael_J_Lippincott_CV_$((current_year - 1)).pdf
fi

echo "PDF built successfully: CV.pdf"
