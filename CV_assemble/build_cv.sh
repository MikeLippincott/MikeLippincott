#!/bin/bash

# generate the tex file from toml file
python build_tex_cv.py --input "cv_profile.toml" --output "cv.tex"

# Compile LaTeX to PDF
# Build CV from LaTeX tex file
pdflatex -interaction=nonstopmode cv.tex

rm cv.aux cv.log cv.out

current_year=$(date +%Y)
current_year=$(date +%Y)
mv cv.pdf ../Michael_J_Lippincott_CV_${current_year}.pdf
# remove previous year's CV
if [ -f ../Michael_J_Lippincott_CV_$((current_year - 1)).pdf ]; then
    rm ../Michael_J_Lippincott_CV_$((current_year - 1)).pdf
fi

echo "PDF built successfully: Michael_J_Lippincott_CV_${current_year}.pdf"
