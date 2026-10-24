"""Check the docs for broken links and inconsistent IDs or counts.

Run it from anywhere: python scripts/check_spec.py
It prints every problem it finds and exits 1, or exits 0 when the spec is
consistent.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
}  # fmt: skip


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" not in path.parts:
            yield path


def check_links(errors):
    pattern = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")
    for path in markdown_files():
        for match in pattern.finditer(path.read_text()):
            target = match.group(1)
            if re.match(r"[a-z]+://|mailto:", target):
                continue
            if not (path.parent / target).resolve().exists():
                rel = path.relative_to(ROOT)
                errors.append(f"broken link in {rel}: {target}")


def check_sequence(ids, name, errors):
    numbers = [int(item.split("-")[-1].lstrip("UC")) for item in ids]
    if numbers != list(range(1, len(numbers) + 1)):
        errors.append(f"{name} ids are not unique and sequential: {ids}")


def number_from_word(word):
    return NUMBER_WORDS.get(word.lower(), int(word) if word.isdigit() else -1)


def check_requirements(errors):
    functional = (DOCS / "requirements/functional.md").read_text()
    rows = re.findall(
        r"^\| (FR-\d+) \| .* \| ([MSC]) \| (.*) \|$", functional, re.M
    )
    fr_ids = [row[0] for row in rows]
    check_sequence(fr_ids, "FR", errors)

    lead = re.search(
        r"(\d+) functional requirements in (\w+) groups; (\d+) are Must", functional
    )
    groups = [
        h for h in re.findall(r"^## (.+)$", functional, re.M) if h != "Coverage check"
    ]
    musts = sum(1 for row in rows if row[1] == "M")
    if not lead:
        errors.append("functional.md: lead sentence with counts not found")
    else:
        said_frs, said_groups, said_musts = lead.groups()
        if int(said_frs) != len(fr_ids):
            errors.append(f"functional.md says {said_frs} FRs, found {len(fr_ids)}")
        if number_from_word(said_groups) != len(groups):
            errors.append(
                f"functional.md says {said_groups} groups, found {len(groups)}"
            )
        if int(said_musts) != musts:
            errors.append(f"functional.md says {said_musts} Must, found {musts}")

    use_cases = (DOCS / "requirements/use-cases.md").read_text()
    uc_ids = re.findall(r"^\| (UC\d+) \|", use_cases, re.M)
    check_sequence(uc_ids, "UC", errors)
    uc_lead = re.search(r"(\w+) use cases define", use_cases)
    if not uc_lead or number_from_word(uc_lead.group(1)) != len(uc_ids):
        errors.append(f"use-cases.md lead does not match {len(uc_ids)} use cases")

    for fr_id, _, cell in rows:
        for uc in re.findall(r"UC\d+", cell):
            if uc not in uc_ids:
                errors.append(f"{fr_id} references unknown {uc}")

    coverage = functional.split("## Coverage check")[-1]
    for uc in uc_ids:
        if not re.search(rf"\b{uc}\b", coverage):
            errors.append(f"{uc} is missing from the coverage check")

    nfr_text = (DOCS / "requirements/non-functional.md").read_text()
    nfr_ids = re.findall(r"^\| (NFR-\d+) \|", nfr_text, re.M)
    check_sequence(nfr_ids, "NFR", errors)
    return len(fr_ids), len(nfr_ids)


def check_references(fr_count, nfr_count, errors):
    for path in markdown_files():
        text = path.read_text()
        rel = path.relative_to(ROOT)
        for number in re.findall(r"\bFR-(\d+)\b", text):
            if not 1 <= int(number) <= fr_count:
                errors.append(f"{rel}: FR-{number} does not exist")
        for number in re.findall(r"\bNFR-(\d+)\b", text):
            if not 1 <= int(number) <= nfr_count:
                errors.append(f"{rel}: NFR-{number} does not exist")


def check_adr_index(errors):
    index = (DOCS / "README.md").read_text()
    for adr in sorted((DOCS / "decisions").glob("0*.md")):
        if adr.name not in index:
            errors.append(f"docs/README.md does not list {adr.name}")


def main():
    errors = []
    check_links(errors)
    fr_count, nfr_count = check_requirements(errors)
    check_references(fr_count, nfr_count, errors)
    check_adr_index(errors)
    for error in errors:
        print(f"FAIL {error}")
    if errors:
        return 1
    print(f"ok   {fr_count} FRs, {nfr_count} NFRs, links and references consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
