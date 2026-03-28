#!/usr/bin/env python3
"""Build a LaTeX CV from TOML profile data.

Default input:  CV_assemble/cv_profile.toml
Default output: CV_assemble/cv.tex
"""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore


SECTION_ORDER = [
    "education",
    "research_experience",
    "scientific_appointments",
    "presentations",
    "honors_awards",
    "teaching_mentoring",
    "journal_reviewer",
    "skills",
    "publications",
]

SECTION_TITLES = {
    "education": "Education",
    "research_experience": "Research Experience",
    "scientific_appointments": "Scientific Appointments",
    "presentations": "Presentations and Invited Lectures",
    "honors_awards": "Honors and Awards",
    "teaching_mentoring": "Teaching and Mentoring",
    "journal_reviewer": "Journal Reviewer",
    "skills": "Programming Skills",
    "publications": "Publications",
}


LATEX_PREAMBLE = r"""%-------------------------
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
\setlength{\footskip}{6pt}

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
"""


def escape_latex(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    out = []
    for ch in str(text):
        out.append(replacements.get(ch, ch))
    return "".join(out)


def timeline(item: dict) -> str:
    start = item.get("start")
    end = item.get("end")
    if start and end:
        return f"{start} - {end}"
    return str(item.get("date") or item.get("year") or start or end or "")


def discover_extra_sections(data: dict) -> list[str]:
    excluded = {"schema", "person"}
    known = set(SECTION_ORDER)
    extras = []
    for key, value in data.items():
        if key in excluded or key in known:
            continue
        if isinstance(value, dict) and isinstance(value.get("items"), list):
            extras.append(key)
    return extras


def render_heading(person: dict) -> list[str]:
    name = escape_latex(person.get("full_name", ""))
    website = person.get("website", "")
    email = person.get("email", "")
    phone = person.get("phone", "")

    lines = [
        "%----------HEADING-----------------",
        r"\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}",
        f"  \\textbf{{\\href{{{website}}}{{\\Large {name}}}}} & Email : \\href{{mailto:{email}}}{{{escape_latex(email)}}}\\\\",
        f"  \\href{{{website}}}{{{escape_latex(website)}}} & Mobile : {escape_latex(phone)} \\\\",
        r"\end{tabular*}",
        "",
    ]
    return lines


def first_present(item: dict, keys: list[str]) -> str:
    for k in keys:
        if item.get(k):
            return str(item[k])
    return ""


def render_generic_subheading_section(
    section_name: str, section_data: dict
) -> list[str]:
    title = SECTION_TITLES.get(section_name, section_name.replace("_", " ").title())
    items = section_data.get("items", [])
    if not items:
        return []

    lines = [
        f"%-----------{title.upper()}-----------------",
        f"\\section{{{escape_latex(title)}}}",
        "  \\resumeSubHeadingListStart",
    ]

    for item in items:
        left = first_present(
            item,
            [
                "title",
                "role",
                "name",
                "degree",
                "type",
                "event",
                "outlet",
                "authors",
                "label",
            ],
        )
        when = timeline(item)

        # Prefer informative detail line while remaining extensible.
        detail_keys = [
            "institution",
            "advisor",
            "organization",
            "event",
            "host",
            "field",
            "venue",
            "status",
            "preprint",
        ]
        detail_parts = [str(item[k]) for k in detail_keys if item.get(k)]
        detail = ", ".join(detail_parts)

        # Include any future fields not yet represented.
        hidden = {
            "title",
            "role",
            "name",
            "degree",
            "type",
            "event",
            "outlet",
            "authors",
            "label",
            "start",
            "end",
            "date",
            "year",
            "location",
            "order",
        }
        extra_parts = [
            f"{k.replace('_', ' ').title()}: {item[k]}"
            for k in item
            if k not in hidden
            and k not in detail_keys
            and item[k] not in (None, "", [])
        ]
        if extra_parts:
            detail = ", ".join([p for p in [detail, "; ".join(extra_parts)] if p])

        location = str(item.get("location", ""))

        lines.extend(
            [
                "    \\resumeSubheading",
                f"      {{{escape_latex(left)}}}{{{escape_latex(when)}}}",
                f"      {{{escape_latex(detail)}}}{{{escape_latex(location)}}}",
            ]
        )

    lines.append("  \\resumeSubHeadingListEnd")
    lines.append("")
    return lines


def render_journal_reviewer(section_data: dict) -> list[str]:
    items = section_data.get("items", [])
    if not items:
        return []

    lines = [
        "%-----------Journal Reviewer-----------------",
        "\\section{Journal Reviewer}",
        "  \\resumeSubHeadingListStart",
    ]

    for item in items:
        role = item.get("role", "Reviewer")
        outlet = item.get("outlet", "")
        label = f"{role} - {outlet}".strip(" -")
        when = timeline(item)
        lines.append(
            f"    \\resumeReviewerItem{{{escape_latex(label)}}}{{{escape_latex(when)}}}"
        )

    lines.append("  \\resumeSubHeadingListEnd")
    lines.append("")
    return lines


def render_skills(skills: dict) -> list[str]:
    lines = [
        "%--------PROGRAMMING SKILLS------------",
        "\\section{Programming Skills}",
        " \\resumeSubHeadingListStart",
    ]
    for key, value in skills.items():
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value)
        lines.extend(
            [
                "   \\item{",
                f"     \\textbf{{{escape_latex(key.replace('_', ' ').title())}}}{{: {escape_latex(str(value))}}}",
                "    }",
            ]
        )
    lines.append(" \\resumeSubHeadingListEnd")
    lines.append("")
    return lines


def render_publications(publications: dict) -> list[str]:
    items = publications.get("items", [])
    if not items:
        return []

    items = sorted(items, key=lambda x: x.get("order", 9999))
    scholar = publications.get("google_scholar")

    lines = ["%-----------Publications-----------------", "\\section{Publications}"]
    if scholar:
        lines.append("  Google Scholar page (with citation metrics):")
        lines.append(f"    \\href{{{scholar}}}{{{escape_latex(scholar)}}}")

    start = items[0].get("order", 1)
    lines.append(
        f"    \\begin{{enumerate}}[label=\\arabic*, start={start}, before=\\let\\originalitem\\item\\renewcommand{{\\item}}{{\\addtocounter{{enumi}}{{-2}}\\originalitem}}]"
    )

    for p in items:
        authors = escape_latex(str(p.get("authors", "")))
        year = escape_latex(str(p.get("year", "")))
        title = escape_latex(str(p.get("title", "")))
        status = escape_latex(str(p.get("status", "")))
        venue = escape_latex(str(p.get("venue", "")))
        preprint = escape_latex(str(p.get("preprint", "")))
        doi = str(p.get("doi", ""))

        tail_bits = []
        if status and venue:
            tail_bits.append(f"{status} at {venue}")
        elif venue:
            tail_bits.append(venue)
        if preprint:
            tail_bits.append(preprint)
        if doi:
            tail_bits.append(f"{doi}")

        tail = ". ".join([b for b in tail_bits if b])
        lines.append(
            f"    \\item {{{authors}. ({year}) {title}. {escape_latex(tail)} }}"
        )

    lines.extend(["", "    \\end{enumerate}", ""])
    return lines


def build_latex(data: dict) -> str:
    lines: list[str] = [LATEX_PREAMBLE.rstrip(), ""]
    lines.extend(render_heading(data.get("person", {})))

    sections = SECTION_ORDER + discover_extra_sections(data)
    for key in sections:
        section_data = data.get(key)
        if not isinstance(section_data, dict):
            continue

        if key == "skills":
            lines.extend(render_skills(section_data))
        elif key == "journal_reviewer":
            lines.extend(render_journal_reviewer(section_data))
        elif key == "publications":
            lines.extend(render_publications(section_data))
        else:
            lines.extend(render_generic_subheading_section(key, section_data))

    lines.extend(
        ["%-------------------------------------------", "\\end{document}", ""]
    )
    return "\n".join(lines)


def load_toml(path: Path) -> dict:
    with path.open("rb") as f:
        return tomllib.load(f)


def parse_args() -> argparse.Namespace:
    default_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Build LaTeX CV from TOML data")
    parser.add_argument(
        "--input",
        type=Path,
        default=default_dir / "cv_profile.toml",
        help="Path to cv_profile.toml",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=default_dir / "cv.tex",
        help="Path to output LaTeX CV",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = load_toml(args.input)
    tex = build_latex(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(tex, encoding="utf-8")
    print(f"LaTeX CV generated: {args.output}")


if __name__ == "__main__":
    main()
