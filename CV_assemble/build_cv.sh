#!/bin/bash
if [ -f "../Michael_J_Lippincott_CV_*.pdf" ]; then
  rm ../Michael_J_Lippincott_CV_*.pdf
fi

# generate the tex file from toml file
python build_tex_cv.py --input "cv_profile.toml" --output "cv.tex"

# Compile LaTeX to PDF
# Build CV from LaTeX tex file
pdflatex -interaction=nonstopmode cv.tex

rm cv.aux cv.log cv.out

current_year=$(date +%Y)
current_month=$(date +%m)
mv cv.pdf ../Michael_J_Lippincott_CV_${current_year}_${current_month}.pdf
# remove previous year's CV


echo "PDF built successfully: Michael_J_Lippincott_CV_${current_year}_${current_month}.pdf"
