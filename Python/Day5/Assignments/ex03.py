#Corporate Directory Search & Scraper

import re


def scrape_directory_phones(directory_text):
    pattern = re.compile(
        r"""
        (?<!\d)
        (?:\((\d{3})\)\s*(\d{3})-(\d{4})   # (AAA) PPP-LLLL
        |
        (\d{3})-(\d{3})-(\d{4})            # AAA-PPP-LLLL
        |
        (\d{3})(\d{3})(\d{4}))             # AAAPPPLLLL
        (?!\d)
        """,
        re.VERBOSE
    )

    records = []

    for match in pattern.finditer(directory_text):
        groups = match.groups()

        # Select the groups corresponding to the matched format.
        if groups[0] is not None:
            area_code, prefix, line_number = groups[0:3]
        elif groups[3] is not None:
            area_code, prefix, line_number = groups[3:6]
        else:
            area_code, prefix, line_number = groups[6:9]

        records.append({
            "area_code": area_code,
            "prefix": prefix,
            "line_number": line_number,
            "formatted": f"({area_code}) {prefix}-{line_number}"
        })

    return records

directory = (
    "Contact HR at 123-456-7890 or the helpdesk at "
    "(987) 654-3210. Direct line is 5558881234."
)

print(scrape_directory_phones(directory))
