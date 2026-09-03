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
    "publications",
    "honors_awards",
    "software_contributions",
    "presentations",
    "teaching_mentoring",
    "journal_reviewer",
    "skills",
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
    "software_contributions": "Software Contributions",
    "publications": "Publications",
}


LATEX_PREAMBLE = r"""%-------------------------
% Resume in Latex
% Author : Michael J. Lippincott
% Website: https://mikelippincott.github.io/
% License : MIT
%------------------------

\documentclass[10.5pt,letterpaper]{article}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{libertine}
\usepackage[libertine]{newtxmath}
\usepackage{microtype}
\usepackage[margin=0.7in,top=0.55in,bottom=0.55in]{geometry}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage{fontawesome5}
\usepackage{needspace}
\usepackage[hidelinks]{hyperref}

\newcolumntype{Y}{>{\raggedright\arraybackslash}X}

\definecolor{accent}{HTML}{0E3A53}
\definecolor{muted}{HTML}{5B6472}

\hypersetup{colorlinks=true, urlcolor=accent, linkcolor=accent}
\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}
\pagestyle{empty}

% Sections formatting
\titleformat{\section}
  {\normalfont\sffamily\bfseries\color{accent}\large}
  {}{0em}{\Needspace{3\baselineskip}}
  [{\color{accent}\titlerule[0.8pt]}]
\titlespacing*{\section}{0pt}{14pt}{6pt}

%-------------------------
% Custom commands
\newcommand{\resumeItem}[2]{
  \item\small{
    \textbf{#1}{: #2}
  }
}

\newcommand{\subheadingskip}{3pt}
\newcommand{\rightcolwidth}{1.3in}
\newcommand{\resumeSubheading}[4]{%
  \vspace{\subheadingskip}\item[]
  \begingroup\rightskip0pt\parfillskip0pt
  \noindent\begin{minipage}[t]{\dimexpr\textwidth-\rightcolwidth-6pt\relax}
    \raggedright\textbf{#1}\\
    \textit{\small\color{muted}#3}
  \end{minipage}%
  \hfill
  \begin{minipage}[t]{\rightcolwidth}
    \raggedleft\textcolor{accent}{\small #2}\\
    \textit{\small\color{muted}#4}
  \end{minipage}
  \par\endgroup
}
\newcommand{\resumeSubheadingCompact}[3]{%
  \vspace{3pt}\item[]
  \begin{tabularx}{\textwidth}{@{}Y r@{}}
    \textbf{#1} & \textcolor{accent}{\small #2} \\
    \multicolumn{2}{@{}l@{}}{\parbox{\textwidth}{\raggedright\itshape\small\color{muted}#3}} \\
  \end{tabularx}
}
\newcommand{\resumeReviewerItem}[2]{%
  \item[]
  \begin{tabularx}{\textwidth}{@{}Y r@{}}
    \textbf{#1} & \textcolor{accent}{\small #2} \\
  \end{tabularx}
}
\newcommand{\resumeSubItem}[2]{\resumeItem{#1}{#2}}
\newcommand{\columnheading}[1]{{\sffamily\bfseries\color{accent} #1}\\[3pt]}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0pt,label={},itemsep=2pt,topsep=2pt,parsep=0pt]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=14pt,itemsep=1pt,topsep=2pt]}
\newcommand{\resumeItemListEnd}{\end{itemize}}
\newcommand{\resumePubListStart}{\begin{itemize}}
\newcommand{\resumePubListEnd}{\end{itemize}}
\newcommand{\resumeSubPubItem}[1]{\item #1}
%-------------------------------------------
%%%%%%  CV STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%

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


def bold_own_name_in_authors(authors: str) -> str:
    rendered = escape_latex(str(authors))
    name_variants = [
        "Michael J. Lippincott",
        "Michael J Lippincott",
    ]
    for name in name_variants:
        escaped_name = escape_latex(name)
        rendered = rendered.replace(escaped_name, rf"\textbf{{{escaped_name}}}")
    return rendered


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


def render_heading(person: dict, mission: dict) -> list[str]:
    name = escape_latex(person.get("full_name", ""))
    website = person.get("website", "")
    website_display = escape_latex(website.split("://", 1)[-1].rstrip("/"))
    email = person.get("email", "")
    tagline = escape_latex(person.get("tagline", ""))
    location = escape_latex(person.get("location", ""))
    mission_description = escape_latex(mission.get("description", ""))

    contact_bits = []
    if location:
        contact_bits.append(f"\\faIcon{{map-marker-alt}}\\ {location}")
    if email:
        contact_bits.append(
            f"\\faIcon{{envelope}}\\ \\href{{mailto:{email}}}{{{escape_latex(email)}}}"
        )
    if website:
        contact_bits.append(
            f"\\faIcon{{globe}}\\ \\href{{{website}}}{{{website_display}}}"
        )
    contact_line = "\n    \\quad\\textcolor{muted}{|}\\quad\n    ".join(contact_bits)

    lines = [
        "%----------HEADING-----------------",
        r"\begin{center}",
        f"  {{\\sffamily\\bfseries\\Huge\\color{{accent}} {name}}}\\\\[3pt]",
    ]
    if tagline:
        lines.append(f"  {{\\normalfont\\itshape\\color{{muted}} {tagline}}}\\\\[6pt]")
    if contact_line:
        contact_end = "  }\\\\[3pt]" if mission_description else "  }"
        lines.extend(["  {\\small", f"    {contact_line}", contact_end])
    if mission_description:
        lines.append(
            f"  {{\\normalfont\\small\\color{{muted}} \\textbf{{Mission:}} {mission_description}}}\\\\[3pt]"
        )
    lines.extend([r"\end{center}", r"\vspace{-4pt}", ""])
    return lines


def first_present(item: dict, keys: list[str]) -> str:
    for k in keys:
        if item.get(k):
            return str(item[k])
    return ""


def render_subheading_items(
    items: list[dict], section_name: str, compact: bool = False
) -> list[str]:
    lines: list[str] = []
    for item in items:
        # Presentations are already split into Talks/Posters columns, so lead
        # with the venue instead of repeating "Oral presentation"/"Poster
        # presentation" as the heading.
        if section_name == "presentations" and compact:
            left_keys = [
                "event",
                "type",
                "role",
                "name",
                "degree",
                "outlet",
                "authors",
                "label",
            ]
        elif section_name == "presentations":
            left_keys = [
                "type",
                "event",
                "role",
                "name",
                "degree",
                "outlet",
                "authors",
                "label",
            ]
        else:
            left_keys = [
                "title",
                "role",
                "name",
                "degree",
                "type",
                "event",
                "outlet",
                "authors",
                "label",
            ]

        if section_name == "education" and item.get("degree") and item.get("field"):
            left = f"{item['degree']} - {item['field']}"
        else:
            left = first_present(item, left_keys)
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
        if section_name == "presentations" and compact:
            # "event" is already shown as the bold heading above.
            detail_keys = [k for k in detail_keys if k != "event"]
        if section_name == "education":
            # "field" is already folded into the "Degree - Field" heading above.
            detail_keys = [k for k in detail_keys if k != "field"]
        detail_parts = [str(item[k]) for k in detail_keys if item.get(k)]
        detail = ", ".join(detail_parts)

        # Include any future fields not yet represented.
        hidden = {
            "title",
            "role",
            "name",
            "degree",
            "field",
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
            "bullets",
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

        bullets = [b for b in item.get("bullets") or [] if str(b).strip()]
        if bullets:
            lines.append("    \\resumeItemListStart")
            for bullet in bullets:
                lines.append(f"      \\item\\small{{{escape_latex(bullet)}}}")
            lines.append("    \\resumeItemListEnd")

    return lines


def render_generic_subheading_section(
    section_name: str, section_data: dict, tight: bool = False
) -> list[str]:
    title = SECTION_TITLES.get(section_name, section_name.replace("_", " ").title())
    items = section_data.get("items", [])
    if not items:
        return []

    lines = [
        f"%-----------{title.upper()}-----------------",
        f"\\section{{{escape_latex(title)}}}",
    ]
    if tight:
        lines.append(r"  {\renewcommand{\subheadingskip}{2pt}")
        lines.append(
            "  \\begin{itemize}[leftmargin=0pt,label={},itemsep=0pt,topsep=2pt,parsep=0pt]"
        )
    else:
        lines.append("  \\resumeSubHeadingListStart")
    lines.extend(render_subheading_items(items, section_name))
    if tight:
        lines.append("  \\end{itemize}}")
    else:
        lines.append("  \\resumeSubHeadingListEnd")
    lines.append("")
    return lines


def render_presentations(section_data: dict) -> list[str]:
    items = section_data.get("items", [])
    if not items:
        return []

    def is_poster(item: dict) -> bool:
        return "poster" in str(item.get("type", "")).lower()

    posters = [item for item in items if is_poster(item)]
    talks = [item for item in items if not is_poster(item)]

    title = SECTION_TITLES.get("presentations", "Presentations and Invited Lectures")
    tight_list_start = [
        r"  {\renewcommand{\subheadingskip}{1pt}",
        "  \\begin{itemize}[leftmargin=0pt,label={},itemsep=0pt,topsep=2pt,parsep=0pt]",
    ]
    tight_list_end = "  \\end{itemize}}"

    lines = [
        "%-----------PRESENTATIONS AND INVITED LECTURES-----------------",
        r"\Needspace{4in}",
        f"\\section{{{escape_latex(title)}}}",
        r"\noindent\begin{minipage}[t]{0.485\textwidth}",
        r"  \columnheading{Talks}",
    ]
    if talks:
        lines.extend(tight_list_start)
        lines.extend(render_subheading_items(talks, "presentations", compact=True))
        lines.append(tight_list_end)
    lines.extend(
        [
            r"\end{minipage}%",
            r"\hfill",
            r"\begin{minipage}[t]{0.485\textwidth}",
            r"  \columnheading{Posters}",
        ]
    )
    if posters:
        lines.extend(tight_list_start)
        lines.extend(render_subheading_items(posters, "presentations", compact=True))
        lines.append(tight_list_end)
    lines.extend([r"\end{minipage}", ""])
    return lines


def render_journal_reviewer(section_data: dict) -> list[str]:
    items = section_data.get("items", [])
    if not items:
        return []

    lines = [
        "%-----------Journal Reviewer-----------------",
        "\\section{Journal Reviewer}",
        "  \\begin{itemize}[leftmargin=0pt,label={},itemsep=0pt,topsep=2pt,parsep=0pt]",
    ]

    for item in items:
        role = item.get("role", "Reviewer")
        outlet = item.get("outlet", "")
        label = f"{role} - {outlet}".strip(" -")
        when = timeline(item)
        lines.append(
            f"    \\resumeReviewerItem{{{escape_latex(label)}}}{{{escape_latex(when)}}}"
        )

    lines.append("  \\end{itemize}")
    lines.append("")
    return lines


def render_software_contributions(section_data: dict) -> list[str]:
    items = section_data.get("items", [])
    if not items:
        return []

    lines = [
        "%-----------SOFTWARE CONTRIBUTIONS-----------------",
        "\\section{Software Contributions}",
        "  \\resumeSubHeadingListStart",
    ]

    for item in items:
        name = str(item.get("name", ""))
        year = str(item.get("year", ""))
        role = str(item.get("role", "")).strip()
        description = str(item.get("description", "")).strip().rstrip(".")
        url = str(item.get("url", "")).strip()

        detail_bits = []
        if role:
            detail_bits.append(role[:1].upper() + role[1:])
        if description:
            detail_bits.append(description)
        detail = escape_latex(". ".join(detail_bits))
        if url:
            link = f"\\href{{{url}}}{{{escape_latex(url)}}}"
            detail = f"{detail}. {link}" if detail else link

        lines.extend(
            [
                "    \\resumeSubheadingCompact",
                f"      {{{escape_latex(name)}}}{{{escape_latex(year)}}}",
                f"      {{{detail}}}",
            ]
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
        lines.append(
            f"  {{\\small\\color{{muted}} Google Scholar page (with citation metrics): "
            f"\\href{{{scholar}}}{{{escape_latex(scholar)}}}}}\\\\[4pt]"
        )

    lines.append(
        r"    \begin{enumerate}[label=\arabic*.,leftmargin=1.6em,itemsep=5pt,topsep=3pt]"
    )

    for p in items:
        authors = bold_own_name_in_authors(str(p.get("authors", "")))
        year = escape_latex(str(p.get("year", "")))
        title = escape_latex(str(p.get("title", "")))
        status = escape_latex(str(p.get("status", "")))
        venue = escape_latex(str(p.get("venue", "")))
        preprint = escape_latex(str(p.get("preprint", "")))
        doi = str(p.get("doi", ""))

        tail_bits = []
        if status and venue:
            tail_bits.append(f"{status} at {venue}")
        elif status and not venue:
            tail_bits.append(status)
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
    lines.extend(render_heading(data.get("person", {}), data.get("Mission", {})))

    # Sections that should sit closer to the section above them than the
    # default \titlespacing "before" gap.
    tighter_gap_before = {"teaching_mentoring", "journal_reviewer", "skills"}

    sections = SECTION_ORDER + discover_extra_sections(data)
    for key in sections:
        section_data = data.get(key)
        if not isinstance(section_data, dict):
            continue

        if key == "skills":
            section_lines = render_skills(section_data)
        elif key == "journal_reviewer":
            section_lines = render_journal_reviewer(section_data)
        elif key == "publications":
            section_lines = render_publications(section_data)
        elif key == "presentations":
            section_lines = render_presentations(section_data)
        elif key == "software_contributions":
            section_lines = render_software_contributions(section_data)
        else:
            section_lines = render_generic_subheading_section(
                key,
                section_data,
                tight=key in {"honors_awards", "teaching_mentoring"},
            )

        if section_lines and key in tighter_gap_before:
            lines.append(r"\vspace{-16pt}")
        lines.extend(section_lines)

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
