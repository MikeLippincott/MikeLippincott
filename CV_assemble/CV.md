%-------------------------
% Resume in Latex
% Author : Michael J. Lippincott
% Website: https://mikelippincott.github.io/
% License : MIT
%------------------------

\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[pdftex]{hyperref}
\usepackage{fancyhdr}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.375in}
\addtolength{\evensidemargin}{-0.375in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}



% Sections formatting
\titleformat{\section}{
  \vspace{-2pt}\scshape\raggedright\Large
}{}{0em}{}[\color{black}\titlerule \vspace{-2pt}]

%-------------------------
% Custom commands
\newcommand{\resumeItem}[2]{
  \item\small{
    \textbf{#1}{: #2 \vspace{-10pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-0pt}\item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-10pt}
}
\newcommand{\resumeReviewerItem}[2]{
  \vspace{-0pt}\item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
    \end{tabular*}\vspace{-15pt}
}
\newcommand{\resumeSubItem}[2]{\resumeItem{#1}{#2}\vspace{-2pt}}

\renewcommand{\labelitemii}{$\circ$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=*]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-10pt}}
\newcommand{\resumePubListStart}{\begin{itemize}}
\newcommand{\resumePubListEnd}{\end{itemize}\vspace{-10pt}}
\newcommand{\resumeSubPubItem}[1]{\item #1 \vspace{-10pt}}
%-------------------------------------------
%%%%%%  CV STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%

\renewcommand{\labelitemi}{--}
\begin{document}

%----------HEADING-----------------
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
  \textbf{\href{http://mikelippincott.github.io/}{\Large Michael J. Lippincott}} & Email : \href{mailto:mail@website.com}{1michaell2017@gmail.com}\\
  \href{http://mikelippincott.github.io/}{http://www.mikelippincott.github.io} & Mobile : +1-(636)-300-7577 \\
\end{tabular*}


%-----------EDUCATION-----------------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {PhD  Computational Cell Biology}{Aug. 2022 - May. 2027}
      {University of Colorado Anschutz Medical Campus}{Aurora, CO}
    \resumeSubheading
      {BS  Biochemistry and Data Science}{Aug. 2017 - May. 2021}
      {Maryville University of Saint Louis}{Saint Louis, MO}
  \resumeSubHeadingListEnd


%-----------RESEARCH EXPERIENCE-----------------
\section{Research Experience}
  \resumeSubHeadingListStart
    \resumeSubheading
      {PhD Research - Computational Cell Biology}{Oct 2022 - Present}
      {Advisor: Gregory P. Way, PhD, University of Colorado}{Aurora, CO}
    \resumeSubheading
      {Research Assistant - Genomics}{2021 - 2022}
      {Advisor: Shawn Ahmed, University of North Carolina at Chapel Hill}{Chapel Hill, NC}
    \resumeSubheading
      {Research Assistant - Genome editing}{2020 – 2021}
      {Centro de Technologia Canavieria}{Saint Louis, MO}
    \resumeSubheading
      {Research Assistant - Quantitative spectroscopy}{2019 – 2020}
      {Advisor: Thomas Spudich, PhD, Maryville University of Saint Louis}{Saint Louis, MO}
    \resumeSubheading
      {Research Assistant - Cell Biology}{2018 – 2021}
      {Advisor: Stacy L. Donovan, PhD, Maryville University of Saint Louis}{Saint Louis, MO}
    \resumeSubheading
      {Research Intern - Biochemistry}{2018 – 2019}
      {Elemental Enzymes}{Saint Louis, MO}
  \resumeSubHeadingListEnd

%-----------Scientific Appointments-----------------
\section{Scientific Appointments}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Wellbeing and engagement committee, Department of
      Biomedical Informatics}{2024 – Present}
      {University of Colorado Anschutz Medical Campus}{Aurora, CO}
    \resumeSubheading
      {PhD student}{Aug. 2022 - Present}
      {University of Colorado Anschutz Medical Campus}{Aurora, CO}
    \resumeSubheading
        {Journal Club Committee, Cell Biology, Stem Cells, and Development}{2023 – 2025}
        {University of Colorado Anschutz Medical Campus}{Aurora, CO}
    \resumeSubheading
        {Volunteer}{2023 – Present}
        {Clear Directions Mentoring}{Aurora, CO}
    \resumeSubheading
        {Cell Biology Graduate Teaching Assistant}{2023 – Present}
        {University of Colorado Anschutz Medical Campus}{Aurora, CO}
    \resumeSubheading
      {Research Assistant}{May. 2021 - May. 2022}
      {University of North Carolina at Chapel Hill}{Chapel Hill, NC}
    \resumeSubheading
        {Teaching Aid – Chemistry/Cell Biology}{2019 – 2021}
        {Maryville University of Saint Louis}{Saint Louis, MO}
    \resumeSubheading
        {Lab technician training manager}{2019 – 2021}
        {Maryville University of Saint Louis}{Saint Louis, MO}
    \resumeSubheading
        {Biology and Maths Tutor}{2017 – 2019}
        {Maryville University of Saint Louis}{Saint Louis, MO}
        
  \resumeSubHeadingListEnd

%-----------Presentations and Invited Lectures-----------------
\section{Presentations and Invited Lectures}
  \resumeSubHeadingListStart
    \resumeSubheading
        {Invited speaker}{Jan. 28, 2026}
        {Michael Johnson Seminar Series, Maryville University}{Saint Louis, MO}
    \resumeSubheading
        {Oral presentation}{Dec. 4, 2025}
        {Neurofibramatosis Young Investigator's Forum}{Baltimore, MD}
    \resumeSubheading
        {Oral presentation}{Oct. 27, 2025}
        {Society of Biomolecular Imaging and Informatics}{Boston, MA}
    \resumeSubheading
        {Oral presentation}{Oct. 24, 2025}
        {Cell Biology, Stem Cells, and Development Retreat}{Estes Park, CO}
    \resumeSubheading
        {Poster presentation}{Feb. 10, 2025}
        {Systems applications for cancer biology}{Aurora, CO}
    \resumeSubheading
        {Oral presentation}{Dec. 3, 2024}
        {American Society for Cell Biology Cell Bio conference}{San Diego, CA}
    \resumeSubheading
        {Poster presentation}{Oct. 18, 2024}
        {Cell Biology, Stem Cells, and Development Retreat}{Breckinridge, CO}
    \resumeSubheading
        {Poster presentation}{Aug. 27, 2024}
        {Center for Health Artificial Intelligence Retreat}{Denver, CO}
    \resumeSubheading
        {Oral presentation}{Jul. 18, 2024}
        {Computational Systems for Integrative Genomics}{New York, NY}
    \resumeSubheading
        {Poster presentation}{Dec. 3, 2023}
        {American Society for Cell Biology Cell Bio conference}{Boston, MA}
    \resumeSubheading
        {Oral presentation}{Aug. 19, 2023}
        {Center for Health Artificial Intelligence Retreat}{Aurora, CO}
    \resumeSubheading
        {Poster presentation}{Oct. 13, 2023}
        {Cell Biology, Stem Cells, and Development Retreat}{Breckinridge, CO}
    \resumeSubHeadingListEnd

%-----------Honors and Awards-----------------
\section{Honors and Awards}
  \resumeSubHeadingListStart
    \resumeSubheading
        {Neurofibromatosis Young Investigator's Forum Travel Award}{2025}
        {Neurofibromatosis Young Investigator's Forum}{Baltimore, MD}
    \resumeSubheading
        {Best Oral Presentation}{2021}
        {Maryville University Research Conference}{Saint Louis, MO}
    \resumeSubheading
        {Excellence in Biological \& Physical Sciences}{2021}
        {Maryville University}{Saint Louis, MO}
    \resumeSubheading
        {Best Poster Award}{2019}
        {Maryville University Research Conference}{Saint Louis, MO}
    \resumeSubheading
        {Outstanding Junior Chemistry Student}{2019}
        {American Chemical Society}{Saint Louis, MO}
    \resumeSubHeadingListEnd

%-----------Teaching and Mentoring-----------------
\section{Teaching and Mentoring}
  \resumeSubHeadingListStart
    \resumeSubheading
        {Mentor - High School Student}{Jan 2025 - Present}
        {University of Colorado Anschutz Medical Campus}{Aurora, CO}
    \resumeSubheading
        {Guest Lecturer - CPBS 7601 Reproducible Computational methods course}{Oct. 17, 2025}
        {University of Colorado Anschutz Medical Campus}{Aurora, CO}
    \resumeSubheading
        {Guest Lecturer - Leveraging AI in Cell Biology}{Apr. 10, 2025}
        {Maryville University of Saint Louis}{Saint Louis, MO}
    \resumeSubheading
        {Guest Lecturer - CPBS 7601 Reproducible Computational methods course}{Nov. 15, 2024}
        {University of Colorado Anschutz Medical Campus}{Aurora, CO}
    \resumeSubHeadingListEnd
%-----------Journal Reviewer-----------------
\section{Journal Reviewer}
  \resumeSubHeadingListStart
    \resumeReviewerItem{Ad hoc Reviewer - Review Commons}{2025 - Present}
    \resumeReviewerItem{Ad hoc Reviewer - Cell}{2024 - Present}
    \resumeReviewerItem{Ad hoc Reviewer - Molecular Biology of the Cell}{2024 - Present}
    \resumeReviewerItem{Ad hoc Reviewer - BiorXiv}{2023 - Present}
  \resumeSubHeadingListEnd

%--------PROGRAMMING SKILLS------------
\section{Programming Skills}
 \resumeSubHeadingListStart
   \item{
     \textbf{Languages}{: Python, R, SQL, Bash, Nextflow}
    }
    \item{
     \textbf{Technologies}{: HPC Orchestration (SLURM), Nextflow, Cloud (AWS, GCP), terraform, Docker, Git}
    }
    \item{
     \textbf{Frameworks}{: Pytorch, Scikit-learn, Pandas, NumPy, SciPy, Optuna, Seaborn}
    }
    \item{
     \textbf{Visualization}{: Matplotlib, Seaborn, ggoplot2, Plotly, dash}
    }
    \item{
     \textbf{Image software}{: CellProfiler, napari, Fiji/ImageJ }
    }
    \item{
     \textbf{Skills}{: Machine Learning, Deep Learning, Statistical Analysis, Data Visualization, Data Wrangling, Data Mining, database Management}
   }
 \resumeSubHeadingListEnd
%-----------Publications-----------------
\section{Publications}
  Google Scholar page (with citation metrics):
    \href{https://scholar.google.com/citations?user=mTdpDrwAAAAJ&hl=en}{https://scholar.google.com/citations?user=mTdpDrwAAAAJ\&hl=en}
    \begin{enumerate}[label=\arabic*, start=9, before=\let\originalitem\item\renewcommand{\item}{\addtocounter{enumi}{-2}\originalitem}]
    \item {\textbf{Michael J. Lippincott}, Jenna Tomkinson, Ibrahim Bilem, Mahomi Suzuki, Akiko Nakde, Toshiaki Endou, Simon Mathien, Felix Lavoie-Perusse, Carla Basualto-Alarcón, Gregory P Way. (2025)
    High-content live-cell time-lapse imaging predicts cells about to die via apoptosis. In Review at Cell Systems Methods. bioRxiv: https://doi.org/10.1101/2025.10.23.684203 
    }
    \item {Dave Bunten, Jenna Tomkinson, Erik Serrano, \textbf{Michael J. Lippincott}, Kenneth I. Brewer, Vince Rubinetti, Faisal Alquaddoomi, Gregory P. Way (2025)
    Scalable data harmonization for single-cell image-based profiling with CytoTable. In Review at Patterns. bioRxiv: https://doi.org/10.1101/2025.06.19.660613 
    }
    \item {Erik Serrano, John Peters, Jesko Wagner, Rebecca E. Graham, Zhenghao Chen, Brian Feng, Gisele Miranda, Alexandr A. Kalinin, Loan Vulliard, Jenna Tomkinson, Cameron Mattson, \textbf{Michael J. Lippincott}, Ziqi Kang, Divya Sitani, Dave Bunten, Srijit Seal, Neil O. Carragher, Anne E. Carpenter, Shantanu Singh, Paula A. Marin Zapata, Juan C. Caicedo, Gregory P. Way. (2025) Progress and new challenges in image-based profiling. arXiv: https://doi.org/10.48550/arXiv.2508.05800
    }
    \item {Abigail Mumme-Monheit, Grace E. Gustafson, Colette A. Hopkins, Raisa Bailon-Zambrano, Juliana Sucharov, \textbf{Michael J. Lippincott}, Gregory P. Way, Kathryn L. Colborn & James T. Nichols. (2025) A quadratic paradigm describes the relationship between phenotype severity and variation. Nature Communications: https://doi.org/10.1038/s41467-025-63316-2
    }
    \item {\textbf{Michael J. Lippincott}, Jenna Tomkinson, Dave Bunten, Milad Mohammadi, Johanna Kastl, Johannes Knop, Ralf Schwandner, Jiamin Huang, Grant Ongo, Nathaniel Robichaud, Milad Dagher, Masafumi Tsuboi, Carla Basualto-Alarcón, Gregory P. Way. (2025) A morphology and secretome map of pyroptosis. MBoC: https://doi.org/10.1091/mbc.E25-03-0119
    }
    \item {Srivastava H, \textbf{Michael J. Lippincott}, Currie J, Canfield R, Lam MPY, Lau E. (2022). Protein prediction models support widespread post-transcriptional regulation of protein abundance by interacting partners. PLOS Computational Biology: https://doi.org/10.1371/journal.pcbi.1010702
    }
    \item {Lister-Shimauchi EH, McCarthy B, \textbf{Michael J. Lippincott}, Ahmed S. (2022) Genetic and Epigenetic Inheritance at Telomeres. Epigenomes: https://doi.org/10.3390/epigenomes6010009
    }

    \end{etaremune}

%-------------------------------------------
\end{document}
