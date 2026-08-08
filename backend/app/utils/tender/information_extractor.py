
import re


def extract_tender_information(text: str) -> dict:
    """
    Extract basic structured information from tender PDF text.
    """

    information = {
        "nit_number": None,
        "tender_date": None,
        "title": None,
        "project_location": None,
        "project_length_km": None,
        "project_cost_cr": None,
        "bid_start_date": None,
        "bid_end_date": None,
        "bid_opening_date": None,
    }

    # NIT Number
    nit_match = re.search(
        r"NIT\s*No\.\s*(.*?)(?=\s+Dated:)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if nit_match:
        information["nit_number"] = " ".join(
            nit_match.group(1).split()
        ).strip()

    # Tender date
    date_match = re.search(
        r"Dated:\s*(\d{2}\.\d{2}\.\d{4})",
        text,
        re.IGNORECASE
    )

    if date_match:
        information["tender_date"] = date_match.group(1)

    # Title / Subject
    subject_match = re.search(
        r"Sub\.\s*:\s*(.*?)(?=\n\s*1\.\s+The Ministry)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if subject_match:
        title = " ".join(subject_match.group(1).split())
        information["title"] = title

    # Project location
    location_match = re.search(
        r"in the state of\s+([A-Za-z\s]+?)(?:\s+on EPC mode|\.)",
        text,
        re.IGNORECASE
    )

    if location_match:
        information["project_location"] = location_match.group(1).strip()

    # Project length
    length_match = re.search(
        r"Total length\s*=\s*([\d.]+)\s*km",
        text,
        re.IGNORECASE
    )

    if length_match:
        information["project_length_km"] = float(
            length_match.group(1)
        )

    # Project cost
    cost_match = re.search(
        r"Rs\.\s*([\d.]+)\s*Cr",
        text,
        re.IGNORECASE
    )

    if cost_match:
        information["project_cost_cr"] = float(
            cost_match.group(1)
        )

    # Bid dates
    bid_match = re.search(
        r"from\s+(\d{2}\.\d{2}\.\d{4}).*?"
        r"to\s+(\d{2}\.\d{2}\.\d{4})",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if bid_match:
        information["bid_start_date"] = bid_match.group(1)
        information["bid_end_date"] = bid_match.group(2)

    # Bid opening date
    opening_match = re.search(
        r"opened\s+(\d{2}\.\d{2}\.\d{4})",
        text,
        re.IGNORECASE
    )

    if opening_match:
        information["bid_opening_date"] = opening_match.group(1)

    return information

