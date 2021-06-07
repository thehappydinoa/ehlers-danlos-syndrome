import re
from typing import List

import requests
from bs4 import BeautifulSoup

RSID_REGEX = re.compile(r"rs\d{4,8}")


def read_rsids_from_file(file_path: str) -> List[str]:
    with open(file_path, "r") as rsids_file:
        lines = rsids_file.read().splitlines()
    return [
        rsid.strip().lower()
        for rsid in lines
        if not rsid == "" and not rsid.startswith("#")
    ]


def read_rsids_from_link(link: str) -> List[str]:
    res = requests.get(link)
    bs = BeautifulSoup(res.text, "html.parser")
    rsids_html = bs.find_all(RSID_REGEX)
    return [rsid.string.strip().lower() for rsid in rsids_html]
